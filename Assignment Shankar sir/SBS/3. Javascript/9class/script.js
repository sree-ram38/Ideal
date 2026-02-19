class character{
    constructor(name){
        this.name = name
    }
    attack(){
        console.log(`${this.name}:swings!`)
    }
}

class Fighter extends character{
    constructor(name){
        super(name)
    }
}
const fighter = new Fighter('Hulk')
fighter.attack()