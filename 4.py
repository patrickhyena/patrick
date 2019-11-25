def vowel_check(letters:str):
    vowel = ["a","e","i","o","u"]
    for i in range(len(vowel)):
        if vowel[i] == letters:
            return True
    return False

print(vowel_check("a"))