def permute(s, current=""):
    if s == "":
        print(current)
        return
    
    for i in range(len(s)):
        new_s = s[:i] + s[i+1:]  # Remove the character at index i
        permute(new_s, current + s[i])

# Example usage
permute("abc")

Output:

abc
acb
bac
bca
cab
cba

