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
     * Static URL of the admin.
     */
    staticURL: '/static/admin/',

    /**
     * Static URL to the loader image.
     */
    loaderImageURL: '/static/admin_timeline/loader.gif',

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
        'staticURL',
        'loaderImageURL'
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

        // Init fancy selects
        this.initSelects();
    },

    /**
     * Load on scroll.
     */
    loadOnScroll: function(ev) {
        var self = ev.data.context;
        // If the current scroll position is past out cutoff point...
        if (jQuery(window).scrollTop() > jQuery(document).height() - (jQuery(window).height() * 3)) {
            self.loadItems();
        }
    },

    /**
     * Runs the app.
     */
    run: function() {
        // Bind <this.loadOnScroll> to the "scroll" event of <window>
        jQuery(window).bind('scroll', {context: this}, this.loadOnScroll);
    },

    /**
     * Init selects.
     */
    initSelects: function() {
        jQuery('.admin-timeline-filter-form select').multipleSelect({
            filter: true,
            //multiple: true,
            width: '100%'
        });
    },

    /**
     *
     */
    showPreloader: function(stream) {
        jQuery(stream).append(
            '<l' +
            'i class="preloader" style="text-align:center;"><i' +
            'mg class="preloader" src="' +
            this.loaderImageURL +
            '" /></l' +
            'i>');
    },

    /**
     *
     */
    hidePreloader: function(stream) {
        jQuery(stream).find('.preloader').remove();
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

        jQuery.post(
            this.url,
            {'page': this.pageNum, 'last_date': this.lastDate,
             'users': this.users, 'content_types': this.contentTypes,
             'start_date': this.startDate, 'end_date': this.endDate},
            function(data) {
                try {
                    jsonData = jQuery.parseJSON(data);
                } catch(err) {
                    jsonData = {success: 0};
                }
                if (1 == jsonData.success) {
                    // Update global next page variable
                    self.hasNextPage = true;
                    self.hidePreloader("ul#admin-timeline");

                    // Pop all our items out into the page
                    jQuery("ul#admin-timeline").append(jsonData.html);
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
