var fruits = []
fruits.push("apple")
fruits.push('pear')

console.log(fruits)
fruits.pop()
console.log(fruits)


function ArrayBuilder(a, b, c){
    var arr = []
    arr.push(a)
    arr.push(b)
    arr.push(c)
    return arr
}

var simplearr = ArrayBuilder(fruits, "orange", 'strawberry')
console.log(simplearr)
var simplearr2 = ArrayBuilder(Math.round(Math.PI), simplearr, fruits)
console.log(simplearr2)