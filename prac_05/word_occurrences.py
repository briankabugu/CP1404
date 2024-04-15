"""
Word Occurrences
Estimate: 20 minutes
Actual:   27 minutes
"""

# get count of words in string
def word_occurrences(str):
    words = {}
    string_array = str.split()
    
    string_array.sort()
    
    for word in string_array:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words
    
def main():
    string = str(input("Enter a string:"))
    
    words = word_occurrences(string)
    
    # get maximum length of string in list
    max_word_length = max(len(word) for word in words)
    
    print(f"Text: {string}")
    for word in words:
        print(f"{word:{max_word_length}} = {words[word]}")
        
main()