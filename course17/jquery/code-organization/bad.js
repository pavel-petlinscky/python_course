// Clicking on a list item loads some content using the
// list item's ID, and hides content in sibling list items
$( document ).ready(function() {

    $( "#myFeature li" ).append( "<div>" ).click(function() {

        var item = $( this );
        var div = item.find( "div" );
        div.load( "foo.php?item=" + item.attr( "id" ), function() {

            div.show();
            item.siblings().find( "div" ).hide();
        });
    });
});
