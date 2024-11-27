def is_palindrome(s):
    return s ==s[::-1]
Sample_string="radar"
print(f"Is '{Sample_string}","is a palindrome?",is_palindrome(Sample_string))