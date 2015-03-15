__title__ = 'admin_timeline.views'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('log',)

import json
import datetime

from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.admin.models import LogEntry
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.template.defaultfilters import date as date_format
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt

from admin_timeline.settings import (
    NUMBER_OF_ENTRIES_PER_PAGE, SINGLE_LOG_ENTRY_DATE_FORMAT
    )
from admin_timeline.settings import LOG_ENTRIES_DAY_HEADINGS_DATE_FORMAT
from admin_timeline.forms import FilterForm
from admin_timeline.compat import TEMPLATE_NAME, TEMPLATE_NAME_AJAX

@csrf_exempt
@never_cache
@staff_member_required
def log(request, template_name=TEMPLATE_NAME, \
        template_name_ajax=TEMPLATE_NAME_AJAX):
    """
    Get number of log entires. Serves both non-AJAX and AJAX driven requests.

    Since we have a breakdown of entries per day per entry and we have an AJAX
    driven infinite scroll and we want to avoid having duplicated date headers,
    we always pass a variable named "last_date" when making another request
    to our main AJAX-driven view. So... this is our case scenario:

    Initial timeline rendered as a normal HTML (non AJAX request) (from a list
    of log entries). We send date of last element as "last_date" to the context
    too, which will be used an an initial value for a global JavaScript
    variable. Later on that date will be used to send it to the AJAX driven
    view and used in rendering ("render_to_string" method). After we have
    rendered the HTML to send back, we get the last date of the last element
    and send it along with the HTML rendered to our view in JSON response.
    When receiving the JSON response, we update the above mentioned global
    JavaScript variable with the value given.

    :param request: django.http.HttpRequest
    :param template_name: str
    :param template_name_ajax: str
    :return: django.http.HttpResponse

    This view accepts the following POST variables (all optional).
    :param page: int - Page number to get.
    :param user_id: int - If set, used to filter the user by.
    :param last_date: str - Example value "2012-05-24".
    :param start_date: str - If set, used as a start date to filter the actions
        with. Example value "2012-05-24".
    :param end_date: str - If set, used as an end date to filter the actions
        with. Example value "2012-05-24".

    NOTE: If it gets too complicatd with filtering, we need to have forms to
    validate and process the POST data.
    """
    def _get_date_from_string(s):
        """
        Gets date from a string given.

        :param s: str - date in string format
        :return: datetime.datetime
        """
        try:
            return datetime.date(*map(lambda x: int(x), s.split("-")))
        except Exception as e:
            return ""

    try:
        page = int(request.POST.get('page', 1))
        if page < 1:
            page = 1
    except Exception as e:
        page = 1

    users = []
    content_types = []
    filter_form = None

    if 'POST' == request.method:
        post = dict(request.POST)
        if 'users[]' in post:
            post['users'] = post.pop('users[]')
        if 'content_types[]' in post:
            post['content_types'] = post.pop('content_types[]')

        filter_form = FilterForm(post)
        if filter_form.is_valid():
            users = filter_form.cleaned_data['users']
            content_types = filter_form.cleaned_data['content_types']
        else:
            pass # Anything to do here?
    else:
        filter_form = FilterForm()

    # Some kind of a pagination
    start = (page - 1) * NUMBER_OF_ENTRIES_PER_PAGE
    end = page * NUMBER_OF_ENTRIES_PER_PAGE

    # Getting admin log entires taking page number into consideration.
    log_entries = LogEntry.objects.all().select_related('content_type', 'user')

    start_date = _get_date_from_string(request.POST.get('start_date'))
    end_date = _get_date_from_string(request.POST.get('end_date'))

    if start_date:
        log_entries = log_entries.filter(action_time__gte=start_date) # TODO

    if end_date:
        log_entries = log_entries.filter(action_time__lte=end_date) # TODO

    # If users given, filtering by users
    if users:
        log_entries = log_entries.filter(user__id__in=users)

    # If content types given, filtering by content types
    if content_types:
        log_entries = log_entries.filter(content_type__id__in=content_types)

    # Applying limits / freezing the queryset
    log_entries = log_entries[start:end]

    if log_entries:
        last_date = date_format(
            log_entries[len(log_entries) - 1].action_time, "Y-m-d"
            )
    else:
        last_date = request.POST.get('last_date', None)

    # Using different template for AJAX driven requests
    if request.is_ajax():
        # Context to render the AJAX driven HTML with
        context = {
            'admin_log': log_entries,
            'number_of_entries_per_page': NUMBER_OF_ENTRIES_PER_PAGE,
            'page': page,
            'last_date': request.POST.get('last_date', None),
            'SINGLE_LOG_ENTRY_DATE_FORMAT': SINGLE_LOG_ENTRY_DATE_FORMAT,
            'LOG_ENTRIES_DAY_HEADINGS_DATE_FORMAT': \
                LOG_ENTRIES_DAY_HEADINGS_DATE_FORMAT
        }

        # Rendering HTML for an AJAX driven request
        html = render_to_string(
            template_name_ajax,
            context,
            context_instance=RequestContext(request)
        )

        # Context to send back to user in a JSON response
        context = {
            'html': html,
            'last_date': last_date,
            'success': 1 if len(log_entries) else 0
        }
        return HttpResponse(json.dumps(context))

    # Context for a non-AJAX request
    context = {
        'admin_log': log_entries,
        'number_of_entries_per_page': NUMBER_OF_ENTRIES_PER_PAGE,
        'page': page,
        'last_date': last_date,
        'start_date': date_format(start_date, "Y-m-d") if start_date else "",
        'end_date': date_format(end_date, "Y-m-d") if end_date else "",
        'users': [int(u) for u in users],
        'content_types': [int(ct) for ct in content_types],
        'filter_form': filter_form,
        'SINGLE_LOG_ENTRY_DATE_FORMAT': SINGLE_LOG_ENTRY_DATE_FORMAT,
        'LOG_ENTRIES_DAY_HEADINGS_DATE_FORMAT': \
            LOG_ENTRIES_DAY_HEADINGS_DATE_FORMAT,
        'title': _("Timeline") # For template breadcrumbs, etc.
    }

    return render_to_response(
        template_name, context, context_instance=RequestContext(request)
        )
