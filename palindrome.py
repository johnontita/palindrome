""""
Write a Python function that checks whether a word or phrase is palindrome or
not.
Note: A palindrome is word, phrase, or sequence that reads the same
backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"

"""

def word_is_palindrome(text):
    length=len(text)
    for index in range(0,length//2):#integer division rounds down
        if(text[index]!=text[length-index-1]):
            # print('the word is not palindrome')
            return False
        return True
string1='racecar'
string2='nurses run'
print(word_is_palindrome(string1))
print(word_is_palindrome(string2))
# print( f'{string1} word_is_palindrome(string1)')
