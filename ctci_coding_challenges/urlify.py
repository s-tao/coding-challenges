"""Write a method to replace all spaces in a string with '%20: You may assume 
that the string has sufficient space at the end to hold the additional 
characters, and that you are given the "true" length of the string. (Note: If
implementing in Java, please use a character array so that you can perform 
this operation in place.)

EXAMPLE
Input: "Mr John Smith   ", 13 Output: "Mr%20John%20Smith"
"""

def urlify_str(url):

    # runtime O(n), spacetime O(n), reassign index
    url = list(url.strip())
    for idx in range(len(url)):
        if url[idx] == ' ':
            url[idx:idx+1] = '%20'

    
    return "".join(url)

    # runtime O(n), spacetime O(n), append to new list
    # url = list(url.strip())
    # result_url = []

    # for char in url:
    #     if char != " ":
    #         result_url.append(char)
    #     else:
    #         result_url.append('%20')
    
    # return "".join(result_url)

print(urlify_str('Mr John Smith    ')) # 'Mr%20John%20Smith
