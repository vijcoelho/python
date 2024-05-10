def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    for i in s:
        if i not in t:
            return False
        if s.index(i) != t.index(i):
            return False
    
    return True
        
s = "rat"
t = "car"

print(isAnagram(s, t))