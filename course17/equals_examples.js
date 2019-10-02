// Есть два способа сравнения

console.log(1 === '1'); // No problems

console.log(1 == '1'); // Приводим типы пока не станет true
console.log(1 == '2');
console.log(1 == true);
console.log(0 == false);
console.log(0 == '');
console.log(0 == []);
console.log(0 == {});
console.log(1 == {});
console.log({} == {});
console.log({} == []);
console.log([] == {});
console.log([] == []);
console.log({} == 1);
