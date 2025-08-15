# bpe.py
"""
A module that implements a simplified BPE tokenization.
It learns a BPE vocabulary based on given corpus
"""

## TODO: Add your functions below
def read_corpus(filename):
    with open(filename, 'r', encoding='utf-8') as file: #opens file and reads it
        return file.read() #return the file as a string
        
    
def split_corpus(corpus):
    words = corpus.lower().split() #splits corpus by whitespace and makes text into lowercase words
    split_words = [] #initialize list to store the list of lists of characters
    for word in words:  
        character_list = [] #for each word in words, character_list is intialized as an empty list to store inidividual characters of the word
        for character in word:
            character_list.append(character) #each character in word is added to character_list
        split_words.append(character_list) #after processing each character, character_list is added to split_words
    return split_words #returns a list of lists of characters
    
def create_alphabet(words):
    alphabet = [] #initialize empty list to store unique characters
    for word in words: #outer loop that iterates over each word in list words
        for letter in word: #inner loop that iterates over each lettter in the current word
            if letter not in alphabet: #checks for unique letters
                alphabet.append(letter) #adds unique letter to list
    return alphabet #returns a list of unique letters
    
    
def get_all_pairs(words):
    pairs= [] #initalize an empty list to store all the pairs
    for word in words: #outer loop that iterates over each word in list words
        for i in range(len(word) - 1): #iterates over indices up to the 2nd to last character in the word
            pairs.append([word[i],word[i+1]]) #each pair consists of current character (word[i]) and the next character (word[i+1]) and the character pairs are added to the pairs list
    return pairs #returns all adjacent character pairs
    
    
def index_of(target, lis):
     index = 0 #start index counter
     for item in lis:
         if item == target:
             return index #return the current index if target is found
         index += 1 #increment index counter
     return None #return None if target isn't found

def find_the_most_frequent_pair(pairs):
    pairs_seen = [] #initialize list of unique pairs
    counts = [] #initialize counter for the number of occurrences of the pairs
    for pair in (pairs): #iterates over all the pairs in list pairs
        index = index_of(pair, pairs_seen) #check if pair has been seen before
        if index == None: #when unique pair is found 
            pairs_seen.append(pair) #add unique pair to list of unique pairs
            counts.append(0) #append 0 to counts so that each unique pair in pairs_seen starts with count 0
        else: #when pair isn't unique
            counts[index] += 1 #increment counts for the existing pair 
    most_frequent = 0 #initialize the first pair as the most frequent pair
    for i in range(len(counts)):
        if counts[i] > counts[most_frequent]: #check if current count is higher
            most_frequent = i #update index of most frequent pair
    return pairs_seen[most_frequent] #return pair with the highest frequency
    
    
def merge_pair(words, pair, print_out = False):
    merged_words = [] #initialize list of merged words
    for word in words:
        merged_word = [] 
        i =0
        while i < len(word):
            #check if the current and next character match the pair we want to merge
            if i < (len(word)-1) and word[i] == pair[0] and word[i+1] == pair[1]:
                if print_out:
                    print(f'start with index {i} in {merged_word + word[i:]}')
                #Merge the pair and add it to the merged_word list
                merged_word.append(pair[0] + pair[1]) #skip the next character
                i +=2
                if print_out:
                    print(f'............ end with {merged_word + word[i:]}')
            else: #no merge; add the current character to merged_word
                merged_word.append(word[i])
                i +=1 #move to the next character 
        merged_words.append(merged_word)
            
    return merged_words

####
# DO NOT MODIFY THIS GIVEN FUNCTION 
def demo_merging():
    '''Demo the function merge_pair by printing out the process'''
    print('************************************************')
    print('test case for the function merge_pair:')
    test_words = [['h', 'e', 'l', 'l', 'o'], ['t', 'h', 'e', 'r', 'e', '!']]
    print('**************testing he:')
    print(merge_pair(test_words, ['h', 'e'], print_out=True))
    print('**************testing el:')
    print(merge_pair(test_words, ['e', 'l'], print_out=True))
    print('**************testing lo:')
    print(merge_pair(test_words, ['l', 'o'], print_out=True))
    print('************************************************')

    
def demo_bpe():
    """Demo learning a BPE vocabulary based on given corpus.
       Also print tokenization results for first 20 words of corpus.
    """
    ## 1st iteration of BPE tokenization
    # read corpus from a file
    corpus = read_corpus('article.txt')
    # split the corpus
    words = split_corpus(corpus)
    # create alphabet
    alphabet = create_alphabet(words)
    print(f'alphabet ({len(alphabet)}) in total: {alphabet}')
    # list all character pairs
    pairs = get_all_pairs(words)
    print(f'First 5 pairs ({len(pairs)} in total including duplicates): {pairs[:5]}') 
    # find the most frequent pair
    the_most_frequent_pair = find_the_most_frequent_pair(pairs)
    print(f'the_most_frequent_pair: {the_most_frequent_pair}')
    # merge the most frequent pair
    splited = merge_pair(words, the_most_frequent_pair)
    print(f'First 5 splited: {splited[:5]}')

    ## Continues with full BPE tokenization to learn a vocabulary
    # set the ideal vocabulary size
    ideal_vocab_size = 50
    # keep track of the pairs being merged
    merges = [the_most_frequent_pair]
    # vocabulary is composed of the basic alphabet and merged pairs
    vocab = alphabet + [the_most_frequent_pair[0] + the_most_frequent_pair[1]]
    # iterate until hitting the ideal vocabulary size
    while len(vocab) < ideal_vocab_size:
        pairs = get_all_pairs(splited)
        the_most_frequent_pair = find_the_most_frequent_pair(pairs) 
        splited = merge_pair(splited, the_most_frequent_pair)
        merges.append(the_most_frequent_pair)
        vocab.append(the_most_frequent_pair[0] + the_most_frequent_pair[1])
    
    print(f'After hitting the ideal vocab size {ideal_vocab_size}:')
    print(f'merged pairs ({len(merges)} in total): {merges}')
    print(f'vocabulary ({len(vocab)} in total): {vocab}')
    print('Tokenization results:')
    for i in range(20):
        print(f"{''.join(words[i])} --> {' '.join(splited[i])}")
   

#### Script code
if __name__ == '__main__':
    # Code in this if-block executes only if this file is run as a script.
    # Code in this if-block will not execute if this module is imported.
    
    #### Test each function implemented ####
    ## Read corpus from a file
    ## Uncomment the block of code below after implementing read_corpus
    print('Testing read_corpus() ...')
    corpus = read_corpus('article.txt')
    print(type(corpus))  # should be str
    print(len(corpus))  # should be 1140
    print('Function read_corpus() passed the tests.')
    
    ## TODO: add code below to test every function that you implement.
filename = 'article.txt'
    
print('Testing read_corpus()')
corpus = read_corpus(filename)
print(corpus)  #should print out full text of file

print('Testing split_corpus()')
words = split_corpus(corpus)
print(words) #should print a list of lists, with inner list representing a word as characters

print('Testing create_alphabet()')
alphabet = create_alphabet(words)
print(alphabet) #should print a list of unique characters

print('Testing get_all_pairs()')
pairs = get_all_pairs(words)
print(pairs) #should print a list of character pairs, including duplicates

print("\nTesting index_of()")
print("Test case 1:", index_of(['l', 'o'], pairs))   #should return the index of the first occurence of ['l','o']
print("Test case 2:", index_of(['x', 'y'], pairs))  # Should return None, as ['x', 'y'] is not in pairs
print("Test case 3:", index_of(['h', 'e'], pairs))  # Should return the index of the first occurrence of ['h', 'e']

print('Testing find_the_most_frequent_pair()')
most_frequent_pair = find_the_most_frequent_pair(pairs)
print(most_frequent_pair) # Should print the pair with the highest frequency in the list

print('Testing merge_pair()...')
merged_words = merge_pair(words, most_frequent_pair, print_out=False)
print(merged_words)  # Should print the list of words with the most frequent pair merged





    #### After testing your functions individually (above), you can run the
    #### following demonstrations.
    ####
    ## Demonstrate the fuction merge_pair
    #demo_merging()
    
    ## Demonstrate learning a BPE vocabulary from a corpus
    #demo_bpe()
    