;
var DjangoAdminTimeline = function() {};
DjangoAdminTimeline.prototype = {
    /**
     * Current page number.
     */
    pageNum: 1,

    /**
     * Show if has next page.
     */
    hasNextPage: true,

    /**
     * Show if currenly busy with loading.
     */
    loading: false,

    /**
     * 
     */
    loadingFeatured: false,

    /**
     * Last date loaded.
     */
    lastDate: null,

    /**
     * 
     */
    users: null,

    /**
     *
     */
    contentTypes: null,

    /**
     *
     */
    startDate: null,

    /**
     *
     */
    endDate: null,

    /**
     *
     */
    url: '',

    /**
     * Static URL (STATIC_URL).
     */
    static_url: '/static/',

    /**
     * List/array of configurable properties (to avoid accidental mistakes).
     */
    configurable: [
        'lastDate',
        'users',
        'contentTypes',
        'startDate',
        'endDate',
        'url',
        'static_url'
    ],

    /**
     * Configure the app defaults. All default settings that are allowed to be
     * overridden are listed in ``configurable`` array. Of course,
     * this doesn't protect us from overriding the settings explicitly.
     *
     * @param {Dictionary} options:
     */
    config: function(options) {
        // Handling settings override
        if (options) {
            for (key in options) {
                if ((key in this) && (this.configurable.indexOf(key) !== -1)) {
                    this[key] = options[key];
                }
            }
        }
    },

    /**
     * Init the app.
     *
     * @param {Dictionary} options:
     */
    init: function(options) {
        // Configure
        this.config(options);

        // Run
        this.run();
    },

    /**
     * Load on scroll.
     */
    loadOnScroll: function(ev) {
        var self = ev.data.context;
        // If the current scroll position is past out cutoff point...
        if (django.jQuery(window).scrollTop() > django.jQuery(document).height() - (django.jQuery(window).height() * 3)) {
            self.loadItems();
        }
    },

    run: function() {
        django.jQuery(window).bind('scroll', {context: this}, this.loadOnScroll);
    },

    /**
     *
     */
    showPreloader: function(stream) {
        django.jQuery(stream).append(
            '<l' +
            'i class="preloader" style="text-align:center;"><i' +
            'mg class="preloader" src="' +
            this.static_url +
            'images/loading.gif" /></l' +
            'i>');
    },

    /**
     *
     */
    hidePreloader: function(stream) {
        django.jQuery(stream).find('.preloader').remove();
    },

    /**
     * Load items.
     */
    loadItems: function() {
        var self = this;
        if (!this.hasNextPage || this.loading) {
            return;
        }
        this.loading = true;
        // If the next page doesn't exist, just quit now
        // Update the page number
        this.pageNum = this.pageNum + 1;
        // Configure the url we're about to hit
        this.showPreloader("ul#admin-timeline");

        django.jQuery.post(
            this.url,
            {'page': this.pageNum, 'last_date': this.lastDate,
             'users': this.users, 'content_types': this.contentTypes,
             'start_date': this.startDate, 'end_date': this.endDate},
            function(data) {
                try {
                    jsonData = django.jQuery.parseJSON(data);
                } catch(err) {
                    jsonData = {success: 0};
                }
                if (1 == jsonData.success) {
                    // Update global next page variable
                    self.hasNextPage = true;
                    self.hidePreloader("ul#admin-timeline");

                    // Pop all our items out into the page
                    django.jQuery("ul#admin-timeline").append(jsonData.html);
                    self.lastDate = jsonData.last_date;
                    self.loading = false;
                } else {
                    self.hasNextPage = false;
                    self.hidePreloader("ul#admin-timeline");
                }
        }).error(function() {
            self.hasNextPage = false;
            self.hidePreloader("ul#admin-timeline");
        });
    }
};
