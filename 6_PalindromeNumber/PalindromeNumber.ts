// Given an integer x, return true if x is a palindrome, and false otherwise.

function isPalindrome(x: number): boolean {
    let ogNum : number = x;
    let reverseNum : number = 0;
    
    while(x > 0 ){
        reverseNum = reverseNum * 10; 
        reverseNum += x % 10;

        x = Math.floor(x/10);
    }
    return ogNum === reverseNum
};
