def print_substrings(s, start=0, end=0):
    if start == len(s):
        return
    elif end == len(s) + 1:
        print_substrings(s, start + 1, start + 1)
    else:
        print(s[start:end])
        print_substrings(s, start, end + 1)

# Example usage
print_substrings("abc")

output:

a
ab
abc
b
bc
c

