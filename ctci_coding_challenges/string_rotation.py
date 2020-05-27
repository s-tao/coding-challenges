"""
String Rotation: Assume you have a method isSubstring which checks if one word 
is a substring of another. Given two strings, s1 and s2, write code to check if 
s2 is a rotation of s1 using only one call to isSubstring 
(e.g. "waterbottle" is a rotation of "erbottlewat").
"""

def str_rotation(word_1, word_2):

    idx_1 = 0
    idx_2 = 0

    while idx_1 < len(word_1):
        # wrap idx of word_2
        idx_2 %= len(word_2)

        if word_1[idx_1] == word_2[idx_2]:
            idx_1 += 1
            idx_2 += 1
        
        elif word_1[idx_1] != word_2[idx_2]:
            if idx_1 == 0:
                idx_2 += 1
            else:
                return False

    return True


print(str_rotation('waterbottle', 'erbottlewat')) # True
print(str_rotation('waterbottle', 'watebottler')) # False
print(str_rotation('waterbottle', 'bottlewater')) # True
print(str_rotation('waterbottle', 'bottlewatea')) # False
