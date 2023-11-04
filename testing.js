
function dblconcatString(a){
    return a+a;
}
function ConcatString(a,b){
    return dblconcatString(dblconcatString(a)+dblconcatString(b));
}

console.log((ConcatString("123","456")))
