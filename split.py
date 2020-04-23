"""Split a string by splitter and return list of splits.

This should work like the built-in Python .split() method [*].
YOU MAY NOT USE the .split() method in your solution!
YOU MAY NOT USE regular expressions in your solution!

For example:

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

* Note: the actual Python split method has special behavior
  when it is not passed anything for the splitter -- you do
  not need to implement that.

"""


def split(astring, splitter):
    """Split a string by splitter and return list of splits."""

    split_lst = []
    # start and end idx to keep track of where to slice
    start_idx = 0
    end_idx = 0
    # check acts as tracker when char matches splitter
    check = 0

    for curr_idx, char in enumerate(astring):

        if char != splitter[check]:
            if check == 0:
                end_idx += 1
            elif check > 0:
                end_idx += check+1
                check = 0
            
        else:
            check += 1

            if check == len(splitter):
                split_lst.append(astring[start_idx:end_idx])
                start_idx = curr_idx + 1
                end_idx = curr_idx + 1

                check = 0
                
        # adds the remaining chars when reaches the end of string
        if curr_idx == len(astring) - 1:
            split_lst.append(astring[start_idx:])

    return split_lst

                
                


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. FINE SPLITTING!\n")
