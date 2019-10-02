'use strict';

(function (window, document) {

    function randint(from, to) {
        //5, 10; - 5 + (0 + 5) (10 - 5)
        var x = to - from;
        var result = from + Math.floor(Math.random() * x);
        return result;
    }

    function colorizeTexts() {
        var colors = [
            'red',
            'grey',
            'black',
            'blue',
            'orange'
        ];

        var color = colors[randint(0, colors.length)];

        var texts = document.querySelector('.texts'); // compare with querySelectorAll
        texts.style['background-color'] = color;
    }

    function setStatus(status) {
        var statusAlert = document.getElementById('status');
        var successColor = statusAlert.getAttribute('data-success-color');
        var failureColor = statusAlert.getAttribute('data-failure-color');

        var textStatus = status ? 'Success' : 'Failure';

        var element = document.createElement('p');

        element.style.backgroundColor = status ? successColor : failureColor;
        element.innerText = textStatus; // test this on firefox and safari

        statusAlert.appendChild(element);
    }

    // http://stackoverflow.com/questions/9899372/pure-javascript-equivalent-to-jquerys-ready-how-to-call-a-function-when-the

    // function clickEventsHandler(event) {
    //     console.log(this, event);
    //     colorizeTexts();
    //     setStatus(Math.round(Math.random()));
    // }


    document.addEventListener('DOMContentLoaded', function () {
        // var links = document.getElementsByTagName('a')

        var control = document.getElementById('toggle');
        var texts = document.querySelector('.texts');

        // control.onclick = function (event) {
        //    console.log(event);
        //    colorizeTexts();
        //    setStatus(Math.round(Math.random()));
        // };

        // or:
        // control.addEventListener('click', clickEventsHandler);

        function click_handler(event) {
            console.log(this, event);
            colorizeTexts();
            setStatus(Math.round(Math.random()));
            var cnt = 5;
            do {
                cnt ++;
            } while(true);
            console.log(cnt);
        }

        control.addEventListener('click', click_handler);
        texts.addEventListener('click', click_handler);


        //control.addEventListener('click', function(event) {
        //    collectStatistics();
        //});
    });
})(window, document);
