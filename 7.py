def sentence_palindrome(text:str):
    text_no_space:str = ""
    for t in text.split(' '):
        text_no_space+=t
    return text_no_space.upper() == text_no_space[::-1].upper()

print(sentence_palindrome("rise to vote sir"))