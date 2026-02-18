function sum(a,b){
    return a+b;
}
console.log(sum(10,10));



// checking positive or not
function ispositive(num){
    return num>0;
}
console.log(ispositive(4))



function hello(){
    console.log('HELLO')
}
hello()



console.log(findproduct(4,7)) //hoisting
function findproduct(a,b){
    return a*b
}
console.log(findproduct)
console.log(typeof findproduct)



function greet(name='there'){
    console.log('Hi',name)
}
greet("Sree")
greet()



// recursive function
function fact(num){
    if (num==1)
        return 1
    return num*fact(num-1)
}
console.log(fact(3));
console.log('sree')



// even or odd
let iseven=function(num){
    return num%2==0
}
console.log(iseven(4))
console.log(iseven)