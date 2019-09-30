// 'use strict';

console.log(-1 + 'b');
console.log(0 + -1 + 'b');
console.log(0 + -1 + 'b' * 0);
console.log(Infinity + NaN);
console.log(Infinity - Infinity);
console.log(typeof(NaN));


var apples = "2";
var oranges = "3";

console.log(apples + oranges);
console.log(+apples + +oranges); // Convert to int

console.log(parseInt('02.34ssd'));
console.log(parseInt('14v14'));
console.log(parseFloat('2.34ssd'));

console.log(Number('2.3'));

var toBool = 'string';
console.log(!!toBool);
console.log(Boolean(toBool));
console.log(Boolean(''));
console.log(Boolean(1));
console.log(Boolean(0));
console.log(Boolean(-9));
console.log(Boolean([]));
var arr = [];
console.log(Boolean(arr && arr.length));
var arr = null;
console.log(Boolean(arr && arr.length));
console.log(Boolean({}));
console.log(Boolean(null));
console.log(Boolean(undefined));


console.log(String(null));
console.log(String([]));
console.log(String([1, 2]));
console.log(String(undefined));
console.log(String({}));
console.log(String({1: 2, 'a': 'b'}));
console.log(+undefined);

/**
 > !!'s'
true
> !!''
false
> !!'1'
true
> !!'0'
true
> !!0
false
> !!!!0
false
> !![]
true
> !!{}
true
> !!null
false
> !!undefined
 false
 **/

// Comparing different types: StackOverflow for more fun - https://stackoverflow.com/questions/359494/which-equals-operator-vs-should-be-used-in-javascript-comparisons
console.log(1 == '1');                            // true
console.log(1 === '1');                          // false
console.log(0 == false);                         // true
console.log(1 == true);                         // true
console.log(1 === true);                        // false
console.log('' == null);                        // false
console.log(null == undefined);                     // true
console.log(null === undefined);                     // false
console.log(0 == []);                                   // false
console.log(1 == {});                                   // false
