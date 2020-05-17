"""Given a string, write a function to check if it is a permutation of a 
palindrome. A palindrome is a word or phrase that is the same forwards and 
backwards. A permutation is a rearrangement of letters. The palindrome does not 
need to be limited to just dictionary words.

Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)
"""

def permutation_is_palindrome(word):
    
    char_dict = {}

    for char in word:
        if char != " ":
            char_dict[char.lower()] = char_dict.get(char.lower(), 0) + 1

    counter = 0

    for count in char_dict:
        if char_dict[count] % 2 != 0:
            counter += 1

        if counter > 1:
            return False
    
    return True

# testcases
print(permutation_is_palindrome('Tact Coa')) # True 
print(permutation_is_palindrome('Not a palindrome')) # False 
print(permutation_is_palindrome('aaa')) # True 
print(permutation_is_palindrome('aaab')) # False 
print(permutation_is_palindrome('aaaab')) # True 
print(permutation_is_palindrome('aaaabc')) # False 
print(permutation_is_palindrome('aaaabcc')) # True 
