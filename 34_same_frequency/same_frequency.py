def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    snum1 = str(num1)
    snum2 = str(num2)
    set1 = set(num1)
    set1 = set(num2)
    counts1 = []
    counts2 = []

    for num in set1:
        count1.append(snum1.count(num))
    for num in set2:
        count2.append(snum2.count(num))

    return count1 == count2
    