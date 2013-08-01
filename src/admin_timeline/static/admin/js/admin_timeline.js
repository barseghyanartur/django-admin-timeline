;
// Scroll globals
var adminTimeline_pageNum = 1; // The latest page loaded
var adminTimeline_hasNextPage = true;
var adminTimeline_loading = false;
var adminTimeline_loadingFeatured = false;
var adminTimeline_lastDate = null;
var adminTimeline_users = null;
var adminTimeline_contentTypes = null;
var adminTimeline_startDate = null;
var adminTimeline_endDate = null;
var adminTimeline_url = '';

/**
 * Sets the initial values.
 *
 * @param {str} lastDate
 * @param {Array} users
 * @param {Array} contentTypes
 * @param {str} startDate
 * @param {str} endDate
 */
var adminTimeline_init = function(lastDate, users, contentTypes, startDate, endDate, url) {
    adminTimeline_lastDate = lastDate;
    adminTimeline_users = users;
    adminTimeline_contentTypes = contentTypes;
    adminTimeline_startDate = startDate;
    adminTimeline_endDate = endDate;
    adminTimeline_url = url;
};

/**
 * Load-on-scroll handler.
 */
var adminTimeline_loadOnScroll = function() {
    // If the current scroll position is past out cutoff point...
    if (django.jQuery(window).scrollTop() > django.jQuery(document).height() - (django.jQuery(window).height()*3)) {
        adminTimeline_loadItems();
    }
};

/**
 * Load items.
 */
var adminTimeline_loadItems = function() {
    if (!adminTimeline_hasNextPage || adminTimeline_loading) {
        return;
    }
    adminTimeline_loading = true;
    // If the next page doesn't exist, just quit now
    // Update the page number
    adminTimeline_pageNum = adminTimeline_pageNum + 1;
    // Configure the url we're about to hit
    adminTimeline_showPreloader("ul#admin-timeline");
    django.jQuery.post(
        adminTimeline_url,
        {'page': adminTimeline_pageNum, 'last_date': adminTimeline_lastDate, 'users': adminTimeline_users,
         'content_types': adminTimeline_contentTypes, 'start_date': adminTimeline_startDate,
         'end_date': adminTimeline_endDate},
        function(data) {
            try {
                jsonData = django.jQuery.parseJSON(data);
            } catch(err) {
                jsonData = {success: 0};
            }
            if (1 == jsonData.success) {
                // Update global next page variable
                adminTimeline_hasNextPage = true;
                adminTimeline_hidePreloader("ul#admin-timeline");

                // Pop all our items out into the page
                django.jQuery("ul#admin-timeline").append(jsonData.html);
                adminTimeline_lastDate = jsonData.last_date;
                adminTimeline_loading = false;
            } else {
                adminTimeline_hasNextPage = false;
                adminTimeline_hidePreloader("ul#admin-timeline");
            }
    }).error(function() {
        adminTimeline_hasNextPage = false;
        adminTimeline_hidePreloader("ul#admin-timeline");
    });
};

django.jQuery(document).ready(function(){
   django.jQuery(window).bind('scroll', adminTimeline_loadOnScroll);
});

var adminTimeline_showPreloader = function(stream) {
    django.jQuery(stream).append('<l'+'i class="preloader" style="text-align:center;"><i'+'mg class="preloader" src="{% static "images/loading.gif" %}" /></l'+'i>');
};

var adminTimeline_hidePreloader = function(stream) {
    django.jQuery(stream).find('.preloader').remove();
};
