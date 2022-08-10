from collections import Counter
def anagram(s, t):    
    # return Counter(s) == Counter(t) -- 1
    # return sorted(s) == sorted(t) -- 2
    #hashmap; 2; one for each string
    if len(s) != len(t):
        return False 
    
    hashmaps, hashmapt = {}, {}
    for i in range(len(s)):
        hashmaps[s[i]] = 1 + i
        hashmapt[t[i]] =1 + i
        print(hashmaps)
        print(hashmapt)
    for c in hashmaps:
        if hashmaps[c] != hashmapt.get(c, 0):
            
            return False
    return True

print(anagram('ana', 'nay'))


