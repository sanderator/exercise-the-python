from letter_count import letter_count


def list_letter_count(lst, letter):
    '''
    Counts the number of times a given letter appears in the strings of a list.
    
    @param strng: A list whose elements are strings.
    @param letter: The letter to count in the strings.
    @return: The number of occurrences of the letter.

    @author:
    '''
    count = 0
    for el in lst:
        count += letter_count(el, letter)
    return count


print(list_letter_count(['the', 'truth', 'is', 'out', 'there'], '
                        '))
