// Using an object literal for a jQuery feature
var myFeature = {
    init: function( settings ) {
        myFeature.config = {
            items: $( "#myFeature li" ),
            container: $( "<div class='container'></div>" ),
            urlBase: "/foo.php?item="
        };

        // Allow overriding the default config
        $.extend( myFeature.config, settings );

        myFeature.setup();
    },

    setup: function() {
        myFeature.config.items
            .each( myFeature.createContainer )
            .click( myFeature.showItem );
    },

    createContainer: function() {
        var item = $( this );
        var container = myFeature.config.container
            .clone()
            .appendTo( item );
        item.data( "container", container );
    },

    buildUrl: function() {
        return myFeature.config.urlBase + myFeature.currentItem.attr( "id" );
    },

    showItem: function() {
        myFeature.currentItem = $( this );
        myFeature.getContent( myFeature.showContent );
    },

    getContent: function( callback ) {
        var url = myFeature.buildUrl();
        myFeature.currentItem.data( "container" ).load( url, callback );
    },

    showContent: function() {
        myFeature.currentItem.data( "container" ).show();
        myFeature.hideContent();
    },

    hideContent: function() {
        myFeature.currentItem.siblings().each(function() {
            $( this ).data( "container" ).hide();
        });
    }
};

$( document ).ready( myFeature.init );
