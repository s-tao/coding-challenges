# Is Unique: Implement an algorithm to determine if a string has all unique 
# characters. What if you cannot use additional data structures?

def is_unique(s):
    
    # O(1) runtime b/c len uses constant time and O(n) space to create set
    return True if len(set(s)) == len(s) else False

    # O(n) runtime, O(n) space
    # ASCII unicode standard 128 
    # if len(s) > 128:
    #     return False

    # check_char = [False for _ in range(128)]

    # for char in s:
    #     unicode = ord(char)
        
    #     if check_char[unicode]:
    #         return False
        
    #     check_char[unicode] = True

    # return True


    # brute force O(n^2), O(1) space
    # for idx_1, char_1 in enumerate(s):
    #     for idx_2, char_2 in enumerate(s):
    #         if char_1 == char_2 and idx_1 != idx_2:

    #             return False

    # return True

    

print(is_unique('abcd efg')) # should return True
print(is_unique('same chars')) # should return False 
