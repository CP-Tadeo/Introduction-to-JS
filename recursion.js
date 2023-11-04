function example(a){
    if ( a == 100) {
        console.log("done")
        return 0
    }
    a += 1
    console.log(a)
    example(a)
    
}


example(0)