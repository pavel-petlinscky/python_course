(function (document, window) {
    function scoped() {
        console.log('scoped');
        console.log(window, document);

        console.log(String(scoped));
    }

    scoped();
    // globalFunction();
}) (document, window);
