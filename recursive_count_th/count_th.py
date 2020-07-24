'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word): 
    # Get the length of the word  
    wordLength = len(word); 
    # If the wordLength contains too little letters to contian "th", return 0  
    if (wordLength < 2): 
        return 0; 
    # Check the first 2 letters of the word for th
    if (word[0:2] == 'th'): 
        # If so, increment number of th's by 1 and move slice over 1 letter
        return count_th(word[1:]) + 1; 
    # Recurse through the word until all instances of th are counted
    return count_th(word[1:])