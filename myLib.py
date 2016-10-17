
def readText(filepath):
    """
    read and return a text in a file
    :param filepath:
    :return:
    """
    f = open(filepath, 'r')
    returnText = f.read()
    f.close()
    return returnText.split()

def findNextWord(word, text):
    """
    find the words that appears in the text file
    :param word: the keywords
    :param text: the text file
    :return: a list of nextwords
    """
    nextWord, frequency = [], []
    for idx, wrd in enumerate(text):
        if wrd == word:
            #finding the next word
            nextWrd = text[idx+1]
            if nextWrd in nextWord:
                #counting the f
                frequency[nextWord.index(nextWrd)]+=1
            else:
                #if not yet on the list, add the word to the list,
                #f starts at 1
                nextWord.append(nextWrd)
                frequency.append(1)
    print(nextWord)
    print(frequency)
        #print('next word is {}'.format(text[idx+1]))
    return nextWord, frequency

def probOcurrence(count):
    nEvents = sum(count)
    prob = [1.0*x/nEvents for x in count]
    density = []
    total = 0
    for p in prob:
        total += p
        density.append(total)
    return density

def randomWord(words, density):
    '''
    generate the next word
    :param words:
    :param density:
    :return:
    '''
   import random as rn
    n = rn.random()
    idx = 0
    while n > density[idx]:
        idx += 1
    return words[idx]


