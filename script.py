def search(list, target):
    """Returns the index (a number) of the target 
       in the given list, or -1 if absent
    Params:
        list - a list of items
        target - a target to search for
    """

    # Your code goes here!!
    for index in range(len(list)):
        if list[index]==target:
            return index
    return -1



print(search(['John','Paul','George','Ringo'], 'George'))
#=> 2

print(search(['John','Paul','George','Ringo'], 'Yoko'))
#=> -1
