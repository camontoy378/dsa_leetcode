int fib(int n){

    //Base case
    if( n < 2){
        return n;
    }

    //Work and recursion
    return fib(n - 1) + fib(n - 2);
}