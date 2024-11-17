
def find_dup_str(s, n):
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if s.count(substring) >= 2:
            return substring
    return ""

def find_max_dup(s):
    max_length = 0
    max_substring = ""
    for i in range(1, len(s)):
        substring = find_dup_str(s, i)
        if len(substring) > max_length:
            max_length = len(substring)
            max_substring = substring
    return max_substring


s = input("Enter a string: you have to know this  ")
n = int(input("Enter the length of the substring: plz it is very important "))

result_a = find_dup_str(s, n)
print("Result for find_dup_str:", result_a)

result_b = find_max_dup(s)
print("Result for find_max_dup:", result_b)