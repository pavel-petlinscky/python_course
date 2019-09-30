'use strict';

(function (window, document) {
    function colorizeTexts() {
        var colors = [
            'red',
            'grey',
            'black',
            'blue',
            'orange'
        ];

        var color = colors[
            Math.floor(Math.random() * colors.length)
        ];

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

    document.addEventListener('DOMContentLoaded', function () {
        var control = document.getElementById('toggle');
        // control.onclick = function (event) {
        //    console.log(event);
        //    colorizeTexts();
        //    setStatus(Math.round(Math.random()));
        // };

        // or:
        control.addEventListener('click', function(event) {
            console.log(this, event);
            colorizeTexts();
            setStatus(Math.round(Math.random()));
        });
        //control.addEventListener('click', function(event) {
        //    collectStatistics();
        //});
    });
})(window, document);
