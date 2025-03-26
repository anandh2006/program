def subsequences(s):
    if s == "":
        return [""]  
    
    smaller_subsequences = subsequences(s[1:])  
    current_char = s[0]  
    
    result = smaller_subsequences + [current_char + sub for sub in smaller_subsequences]  
    return result  

# Example usage
s = "abc"
print(subsequences(s))  
