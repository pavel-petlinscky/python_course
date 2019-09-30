'use strict';

function log(value) {  // return undefined
    console.log(value);
}

function log(value) {
    console.log(value);
    return 'as';
}

function someFunction(a, b) {
    return a + b;
}

someFunction(1); // :(((( Bad, bad, bad
someFunction(1, 2, 3, 4); // :(((( Bad, bad, bad


var namedLog = function(value) {
    console.log('named', value);
    return 4;
};


var nfe = function namedFunctionalExpression (i) {
    if (i == 0) {
        return 0;
    }
    // namedFunctionalExpression = null;
    return i + namedFunctionalExpression(i - 1); // i-- or --i
};

var returnValue = log(123);
console.log(returnValue);

namedLog('asd');
console.log(nfe(5));
namedFunctionalExpression(5);

log = console.log;
log();

console.log(typeof namedLog);
console.log(namedLog);
namedLog = null;
// namedLog(23);
