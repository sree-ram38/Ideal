    // let person = {
    //     firstName: "Logesh",
    //     lastName: "Jayagopi",
    //     age: 23,
    //     isStudent: true
    //     };
// let newperson = Object.create()
// console.log(person.firstName)
// console.log(person['lastName'])

// changing the property value
// person.firstName = "sree"
// delete the property
// delete person.isStudent
// console.log('firstNam'in person)



// object.values() method
// const session = {
//     id: 1,
//     time: `26-July-2018`,
//     device: 'mobile',
//     browser: 'Chrome'
// };
// const values = Object.values(session);
// console.log(values);

// // object.keys() method
// const employees = {
//     boss: 'Michael',
//     secretary: 'Pam',
//     sales: 'Jim',
//     accountant: 'Oscar'
// };
// keys = Object.keys(employees);
// console.log(keys)

// // object.entries() metthod display the output in ascending order
// const obj = {name:'sree',age:23,location:'kanyakumari'}
// console.log(Object.entries(obj))

// // object freeze() method we cannot change the value in freeze
// let person = {name: 'sree', age: 23}
// console.log(Object.freeze(person))
// console.log(person.age = 30)
// console.log(delete person.age) //cannot delete
// console.log(person)

// // object seal()method we can change the value but we cannot delte the key and value 
// let person = {name: 'sree', age: 23}
// Object.seal(person)
// delete person.age
// console.log(person)

// // this keyword
// function createCharacter(name) {
//     return {
//         name,
//         greet: function () {
//             console.log(`${this.name} says hello!`)
//                 },
//                 }
//                 }
// const character = createCharacter('Logesh')
// character.greet()


// function createCharacter(name) {
//     return {
//         name,
//         greet: function () {
//             console.log(`${this.name} says hello!`)
//                 },
//                 }
//                 }
// const {greet} = createCharacter('Logesh')
// greet()

// // new keyword
// function character(name){
//     this.name = name
// }
// const Cartr = new character('sree')
// console.log(Cartr)

// // prototypes
// const character = {
//     attack: function(){
//         console.log('swing')
//     },
// }
// const fight ={
//     name:'Hulk',
//     __proto__:character,
// }
// fight.attack()

// const character = {
//     attack: function(){
//         console.log('swing')
//     },
// }
// const fight ={
//     name:'Hulk',
//     __proto__:character,
// }
// fight.attack()

function Character(name){
    this.name = name
    this.attack = function(){
        console.log(`${this.name} swings!`)
    }
}

function Fighter(name){
    this.name = name
}

// prototype need to be created
Fighter.prototype = new Character
const fighter = new Fighter('Hulk')
fighter.attack()