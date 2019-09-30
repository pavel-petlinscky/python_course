/**
 * Комментарий
 * в несколько
 * строк
 */

'use strict';  // https://learn.javascript.ru/strict-mode

// x = 'Another';

// Primitives:
// const str_another = "Another str"; // not supported in all browsers
var str = "A string";
//str = 5;
var alsoString = 'A string';
//var also_string = 'A string';
var s; // variables without value

console.log(str == alsoString);
console.log(str === alsoString);
console.log(str != alsoString);
console.log(str !== alsoString);
console.log(typeof(str), typeof alsoString);
console.error("Some error", 1, 2, 3, 4);

var num1 = 1;
var num2 = 2.0;

console.log(num1 + num2);
console.log(num1 * num2);
console.log(1 === 1.0);
console.log(1 / 0);
console.log(1 / 0 + 10 - 3);

var x;
console.log(x);

x = null;
console.log(x);

console.log(null === undefined);

// Objects:

var obj = {property: 'value'};
console.log(obj.property);
console.log(obj['property']);
console.log(typeof(obj), obj);
var x = 'key';
var o = {x: 16};
console.log(o);
o[x] = 16;

var array = [obj, obj];
array.push(1);
array.push(2);
console.log(typeof(array), array, array.length);

// Mutability:
var obj = {property: 'value'};
var newObject = obj;
newObject.newProperty = 'new value';
newObject.property = 'replace';
console.log(newObject, obj);


// Copy objects
JSON.parse(JSON.stringify({'sd': 12}));


Object.keys({1: 2, 'a': 'b'}); // not all browser support
