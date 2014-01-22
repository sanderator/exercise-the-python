def letter_count(strng, letter):
    '''
    Counts the number of times a given letter appears in a string.

    @param strng: A string.
    @param letter: The letter to count in the string.
    @return: The number of occurrences of the letter.

    @author:
    '''
    count = 0
    for l in strng:
        if l == letter:
            count += 1
    return count


#print(letter_count('the truth is out there', ' '))
