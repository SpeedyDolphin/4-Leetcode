// Given an integer x, return true if x is a palindrome, and false otherwise.
function isPalindrome(x) {
    var ogNum = x;
    var reverseNum = 0;
    while (x > 0) {
        reverseNum = reverseNum * 10;
        reverseNum += x % 10;
        x = Math.floor(x / 10);
    }
    return ogNum === reverseNum;
}
;
