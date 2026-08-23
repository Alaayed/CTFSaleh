class Solution:
    def compress(self, chars) -> int:
        i = 0
        curChar = chars[0]
        count = 0
        for c in chars:
            if c == curChar:
                count +=1
            else: # transition boundary
                countStr = str(count)
                chars[i] = curChar
                i+=1
                
                if count != 1:
                    # for each char write something
                    for j in countStr:
                        chars[i] = j
                        i+=1
                # reset
                count = 1
                curChar = c
        chars[i] = curChar
        i+=1 
        print(chars)
        if count != 1:
            for j in str(count):
                chars[i] = j
                i+=1
        return i


