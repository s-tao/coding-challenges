"""String Compression: Implement a method to perform basic string compression 
using the counts of repeated characters. For example, the string aabcccccaaa 
would become a2b1c5a3. If the "compressed" string would not become smaller than 
the original string, your method should return the original string. You can 
assume the string has only uppercase and lowercase letters (a - z).
"""

def str_compression(word):
    word = list(word)
    start = 0
    end = 1
    count = 1

    while end < len(word):
        if word[start] == word[end]:
            count += 1
            end += 1
        else:
            # if count is only 1, add to string instead of replacing
            if count == 1:
                word[start:end] += str(count)
                
            else:
                word[start+1:end] = str(count)
                count = 1

            start += 2
            end = start+1

    # add rest of count
    word[start+1:end] = str(count)

    return "".join(word)




print(str_compression('aabcccccaaa')) # a2b1c5a3
print(str_compression('abccddda')) # a1b1c2d3a1
print(str_compression('abc')) # a1b1c1
