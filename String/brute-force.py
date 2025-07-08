def brute_force(text, sub):
    n = len(text)
    m = len(sub)
    
    for i in range(n-m):
        match = True
        for j in range(m):
            if text[i+j] != sub[j]:
                match = False
                break
        
        if match:
            return i
        
    return 0

    

text = 'bacbabababacaca'
sub = 'ababac'

print(brute_force(text,sub))

def rabin_karp(text, sub):
    d = 256 # A number of characters in input alphabets 
    q = 101 # A prime number to reduce the collision. 
    p = 0
    t = 0
    
    n = len(text)
    m = len(sub)
    
    h = pow(d, m-1) % q
    
    for i in range(m):
        p = (d* p + ord(sub[i])) % q
        t = (d* t + ord(text[i])) % q
        
    for i in range(n-m+1):
        match = False
        if p == t:
            match = True
            
            for j in range(m):
                if text[i+j] != sub[j]:
                    match = False
            if match:
                return i
        
        if i < n-m:
            
            t = (d * (t - ord(text[i]) * h ) + ord(text[i+m])) % q
            
            if t <= 0:
                t += q
        
    return 0
    
    

    
print(rabin_karp(text,sub))


def kmp(txt, ptn):
    n = len(txt)
    m = len(ptn)
    lps = [0] * m
    prevLps, i = 0, 1
    
    while i < m:
        if ptn[i] == ptn[prevLps]:
            lps[i] = prevLps + 1
            prevLps += 1
            i+=1
            
        else:
            if prevLps == 0:
                lps[i] = 0
                i+=1
            else:
                prevLps = lps[prevLps-1]
    it = 0
    jp = 0
    
    while it< n:
        if txt[it] == ptn[jp]:
            it,jp = it+ 1, jp+1
            
        else:
            if jp ==0:
                it+=1
            else:
                jp = lps[jp-1]
        if jp == m:
            return it-m        
    return -1
    
txt = 'bacbabababacaca'
ptn = 'ababac'

print(kmp(txt,ptn))


def boyer_moore(txt, pattern):
    n = len(txt)
    m = len(pattern)
    
    no_alpha_order = 256
    bad_char_code = [-1] * no_alpha_order
    
    for i, char in enumerate(pattern):
        bad_char_code[ord(char)] = i
        
    s = 0
    
    while s <= n-m:
        j = m-1
        
        while j >= 0 and pattern[j] == txt[s+j]:
            j-=1
            
        if j < 0:
            print("Pattern is found at index: ", s)
            s += (m - bad_char_code[ord(txt[s+m])] if s+m < n else 1)
        else:
            s += max(1, j - bad_char_code[ord(txt[s+j])])
            
    
txt1 = 'bacbabababacacaababac'
pattern = 'ababac'
print(boyer_moore(txt1, pattern))