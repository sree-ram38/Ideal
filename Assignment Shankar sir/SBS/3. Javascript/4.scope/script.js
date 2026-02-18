// global scope
const name = 'sreeram'
function globalscope(){
    console.log(name);
}
// console.log(name)
// globalscope()

// global and function scope
const car = 'BMW'
function vehicle(){
    const car = 'Audi'
    console.log(car)
}
// console.log(car)
// vehicle()

// block scope
const monster = 'BMW'
function vehicle(){
    const monster = 'Audi'
    if(true){
        const monster = 'superman from dc'
        console.log(monster)
    }
    // console.log(monster)
}
// console.log(monster)
// vehicle()

// variable keyword scope
function myname(){
    if(true){   //true will execute, false will not execute
        var name = 'My name is sreeram'
    }
    console.log(name)
}
// myname()

// coercion
// let a=42+'7'
// let a=42-'7'
// console.log(a)

// logical operatorreturn value
const a = 41
const b = "sreeram"
const c = null
// console.log(a&&c)

function greet(name){
    console.log(`Hello,${name || "Sreeram"}`)
}
// greet()
// greet("ram")

let res = 'sree'

res = res ?? 'hello';
res
// console.log(res)

let ab = 10;
ba = 20;
// console.log(ab, ba)

// reference object type
let user1 = {name:'john'};
let user2 = user1;
user2.name="Joe"
// console.log(user1.name)


// truthy or falsy value
let username = '';
let display = username || 'ram';
// console.log(display)

let islogedin = true && 'welcome back!'
// console.log(islogedin)

// template literal
const names = "sree";
const age = 23;
// console.log(`My name is ${names} and I'm ${age} year old`)  
const multi =`dnsdkjvns
dcdvvsv
sacasva`
// console.log(multi)


// symbol




// addEventListener  

let arr = [1,2,3,4,5]
// let findsum = function(arr){
//     let sum = 0
//     for(let val of arr){
//         sum+=val
//     }
//     return sum
// }
// console.log(findsum(arr))



// arrow function
// let volume = (l,b,h) => {return l*b*h}
// console.log(volume(7,8,9))

// let sumofarr = arr => {
//     let sum = 0
//     for(let val of arr){
//         sum+=val
//     }
//     return sum
// }
// console.log(sumofarr(arr))

// area of circle arrow function
// let circle =  r => Math.PI*r*r
// console.log(circle(2))

// variablearguments
// let prod = function(...args){
//     let result = 1
//     for(let val of args)
//         result *= val
//     return result
// }
// console.log(prod(7,6,5,4))

let prod2 = function(){
    let result = 1
    // console.log(arguments)
    for(i=0;i<arguments.length;i++)
        result *= arguments[i]
    return result
}
console.log(prod2(7,6,5,4))

console.clear()

// generators -  generates  value one by one
function* indexGenerator(){
    let index = 1
    while(true){
        yield index++
    }
}

const gen = indexGenerator();
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)