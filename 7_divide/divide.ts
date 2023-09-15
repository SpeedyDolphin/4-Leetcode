function divideInt(dividend: number, divisor: number): number {
    var result:number = 0
    var sign:number = ((divisor > 0 && dividend > 0)||(divisor < 0 && dividend < 0))? 1 : -1
    divisor = Math.abs(divisor)
    dividend = Math.abs(dividend)
    while(dividend >= divisor){
        dividend -= divisor
        result += 1 
    }
    return result * sign
};

console.log(divideInt(10,2))