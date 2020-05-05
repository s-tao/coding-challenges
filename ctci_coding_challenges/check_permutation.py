# Given two strings, write a method to decide if one is a permutation of the 
# other.

def is_permutation(string_1, string_2):
    
    # runtime O(n), space O(n)

    check_char = {}

    # if lens don't match, then strings cannot be permutations of each other
    if len(string_1) != len(string_2):
        return False

    for char in string_1:
       check_char[char] = check_char.get(char, 0) + 1
    
    for char in string_2:
        check_char[char] = check_char.get(char, 0 ) - 1
    
    for val in check_char.values():
        if val != 0:
            return False


    return True



print(is_permutation('abcd', 'dbac')) # True
print(is_permutation('abcd', 'apdc')) # False
