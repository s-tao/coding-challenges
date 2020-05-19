"""There are three types of edits that can be performed on strings: insert a 
character, remove a character, or replace a character. Given two strings, write 
a function to check if they are one edit (or zero edits) away.
"""

def is_one_away(word_1, word_2):
    
    # space O(1), runtime O(n)
    count = 0
    idx_w_1, idx_w_2 = 0, 0

    while idx_w_1 < len(word_1) and idx_w_2 < len(word_2):
        if count > 1:
            return False

        if word_1[idx_w_1] != word_2[idx_w_2]:
            count += 1
            if len(word_1) > len(word_2):
                idx_w_1 += 1
            elif len(word_1) < len(word_2):
                idx_w_2 += 1
            else:
                idx_w_1 += 1
                idx_w_2 += 1

        else:
            idx_w_1 += 1
            idx_w_2 += 1
    
    return True


    # space O(n), runtime O(n)
    # word_1_set = set(word_1)
    # word_2_set = set(word_2)

    # diff = word_1_set - word_2_set

    # return False if len(diff) > 1 else True

print(is_one_away('pale', 'ple')) # true
print(is_one_away('pales', 'pale')) # true
print(is_one_away('pale', 'bale')) # true
print(is_one_away('pale', 'bake')) # false

