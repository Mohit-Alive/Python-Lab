def same(s):
    words = s.split()
    return words[0][0].lower() == words[1][0].lower()
    
print(same("Hello hi"))