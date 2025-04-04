def subsequences(s):
    if len(s) == 0:
        return [""]  # Base case: return list with empty string
    
    small_output = subsequences(s[1:])  # Get subsequences without first character
    result = []

    for item in small_output:
        result.append(item)           # Exclude current char
        result.append(s[0] + item)    # Include current char

    return result

# Example usage
s = "abc"
all_subseq = subsequences(s)
print(all_subseq)

output:

['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']

