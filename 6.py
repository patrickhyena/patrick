def is_palindrome(text:str):
    return text[::-1] == text
print(is_palindrome("tacocat"))