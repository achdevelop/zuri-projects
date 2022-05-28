# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

file="/Users/alejandro.chacon/Documents/code/git-zuri/zuri-projects/readfile/story.txt"

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as file:
        data = file.read().replace('\n','')
    return data

#print(read_file_content("/Users/alejandro.chacon/Documents/code/git-zuri/zuri-projects/readfile/story.txt"))
def count_words(filename):
    text = read_file_content(filename)
    # [assignment] Add your code here
    clean_string = text.lower().split()
    word_dict = {}

    for word in clean_string:
        # Check if the word is already in dictionary
        if word in word_dict:
            # Increment count of word by 1
            word_dict[word] = word_dict[word] + 1
        else:
            # Add the word to dictionary with count 1
            word_dict[word] = 1
    
    return word_dict

print(count_words(file))