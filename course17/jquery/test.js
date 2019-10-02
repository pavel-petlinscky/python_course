'use strict';

   (function (document, window) {
   function scoped() {
       document.addEventListener('DOMContentLoaded', function () {
           var buttonSubmit = document.getElementById('buttonSubmit');
           var buttonClear = document.getElementById('buttonClear');

           function addDiv(){
               var text = "LoremIpsum";
               var randValue = Math.floor(Math.random()*3 + 2);

               var elementDiv = document.createElement('div');

               var elementP = document.createElement('p');
               elementP.innerText = text;
               elementDiv.appendChild(elementP);

               document.getElementsByTagName('body')[0].appendChild(elementDiv);
           }

           buttonSubmit.addEventListener('click', function(event) {
               addDiv();
           });

       });
   }

   scoped();
}) (document, window);
