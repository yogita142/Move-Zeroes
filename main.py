def first_non_reapeating_char(s):
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for index, char in enumerate(s):
        if count[char] == 1:
            return index

    return -1
    
s = "leetcode"
result = first_non_reapeating_char(s)
print("The first non reapeating character is:", result)
