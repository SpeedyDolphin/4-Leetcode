# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# solution times out :(
def divideInt(dividend: int, divisor: int):
    result:int = 0
    sign = 1 if ((divisor > 0 and dividend > 0) or  (divisor < 0 and dividend < 0)) else -1
    divisor = abs(divisor)
    dividend = abs(dividend)
    while dividend >= divisor:
        dividend -= divisor
        result += 1 
    return result * sign


print(divideInt(11,-2))