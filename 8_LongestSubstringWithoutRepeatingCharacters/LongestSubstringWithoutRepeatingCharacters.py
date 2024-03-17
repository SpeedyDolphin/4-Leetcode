

def lengthOfLongestSubstring(s, debug):
        """
        :type s: str
        :rtype: int
        """
        if(len(s) == 0):
            return 0

        memoryBank = dict()
        lastResetChar = None
        start = 0
        longest = 1

        for i in range(len(s)):
            if debug: 
                print(f'Looking at {s[i]}:{i}')
            #Reset 
            if s[i] in memoryBank.keys() and (memoryBank[s[i]][0] >= start or s[i] == lastResetChar):
                if debug:
                    print(f"Resetting - Conflict {s[i]}:{memoryBank[s[i]]} - Start: {start}")
                # Potential pattern a****a******a
                if lastResetChar == s[i] and s[i] != s[i-1]:
                    #pattern a****a******a
                    length = i - memoryBank[s[i]][0] -1
                    memoryBank[s[i]] = [memoryBank[s[i]][1], i]
                
                # Pattern a***a
                else:
                    # print('~~general reset~~')      
                    length = i-start
                    lastResetChar = s[i]
                    memoryBank[s[i]].append(i)

                #General
                if debug:
                    print(f'New : {length}, Old: {longest}')     
                longest = length if (length > longest) else longest
                start = i
            #Update key
            else:
                memoryBank[s[i]] = [i]
            
        if debug:
            print(memoryBank)
            print(f'Last entry : {len(s[start:])} - {s[start:]}')
            print(f'Current Longest: {longest}')
        return len(s)-start if (len(s)-start > longest) else longest
'''
Runtime
61
ms
Beats
29.08%
of users with Python

Memory
2.28
MB
Beats
56.80%
of users with Python

'''
def attempt2(s):
    if(len(s) == 0):
            return 0

    memoryBank = dict()
    start = 0
    longest = 1

    for i in range(len(s)):
        #Reset
        if s[i] in memoryBank.keys() and memoryBank[s[i]] >= start:
            # print(s[start:i])
            longest = i - start if i-start > longest else longest
            start = memoryBank[s[i]] + 1

        memoryBank[s[i]] = i

    return len(s)-start if (len(s)-start > longest) else longest

if __name__ == "__main__":
    s1 = 'abcabcbb' # expected 3
    au = 'au'
    s = 'dvdf'
    # s = 'asjrgapa'
    # s= 'pwwkew'
    # s = 'bbbbbbbbbbbbbbbbb'
    # s = "loddktdji"
    print(lengthOfLongestSubstring(s1, False))
    print(lengthOfLongestSubstring(s1[::-1], False))

