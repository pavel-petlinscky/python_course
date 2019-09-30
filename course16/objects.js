'use strict';

var MyClass = function (title) {

    this.title = title;
    var privateValue = 'secret';

    this.tellTitle = function (value) {
        console.log("tellTitle", value);
        console.log(this.title);
        console.log(this);
    };

    function privateFunction() {
        console.log("privateFunction");
        console.log(privateValue);
        console.log('This is:', this);
    }

    privateFunction();

    this.runPrivate = function () {
        console.log("runPrivate");
        privateFunction();
    };

    this.runPrivateWithCall = function () {
        console.log("runPrivateWithCall");
        privateFunction.call(this);
        privateFunction.apply(this, []);
    };
};

var inst = new MyClass('Hello, world!');
inst.tellTitle();
inst.runPrivate();
inst.runPrivateWithCall();
// inst.newFunction();

console.log('compare', typeof MyClass.prototype === typeof {});

// mutable class prototypes
// MyClass.prototype = {};
MyClass.prototype.newFunction = function () {
    console.log('Here I am!');
    console.log('Prototype has this:', this);
};

inst.newFunction();

// Sometimes life is just too hard:
var doNotDoThis = new Function('x, y', 'return x + y;');
console.log(doNotDoThis(1, 6));
