def palidrome(str):
    n = len(str)
    longest = ''
    for i in range(n):
        for j in range(i+1, n+1):
            substr = str[i:j]
            print(substr)
            if substr == substr[::-1]:
                if len(substr) > len(longest):
                    longest = substr             
    return longest
# print(palidrome('adbab'))




def kmp(str, pattern):
    for i in range(len(str)):
        start = 0

        for j in range(len(pattern)):
            str_len = str[start : ] 
            pattern_len = pattern[0:j+1]
            print('str_len',str_len, pattern_len)
            if str_len== pattern_len:
                start += 1
                
        if len(pattern) == start:
            print("test", start)
            return i
    return -1


print(kmp('aaab', 'aab'))