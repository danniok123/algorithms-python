import sys
import math

def printAlgo(M, text, length):
    """
    Neat Print algorithm created for CS 124
    """

    # Array for optimal cost of arranging the words from 1 to j
    Opt = [0 for i in range(0, length)]
    wordCost = [0 for i in range(0, length)]

    extras = [[0 for i in range(length)] for i in range(length)]
    penalties = [[0 for i in range(length)] for i in range(length)]

    # computing extras
    for i in range(0, length):
        extras[i][i] = M - len(text[i])
        for j in range(i + 1, length):
            extras[i][j] = extras[i][j - 1] - len(text[j]) - 1


    # computing the penalties
    for i in range(0, length):
        for j in range(i, length):
            spaces = extras[i][j]
            if extras[i][j] < 0:
                penalties[i][j] = sys.maxint
            elif j == length - 1 and extras[i][j] >= 0:
                penalties[i][i] = 0
            else:
                penalties[i][j] = int(math.pow(extras[i][j], 3))

    # computing optimal cost and storing values into wordCost table
    for j in range(0, length):
        Opt[j] = sys.maxint
        for i in range(0, j):
            tmp = Opt[i - 1] + penalties[i][j]
            if tmp < Opt[j]:
                Opt[j] = tmp
                wordCost[j] = i
    
    # return last element of Opt array
    return wordCost, Opt.pop()


def neatPrint(words, M, length):

    textCost, opt = printAlgo(M, words, length)

    printtext = ''

    num = len(words)
    #print num

    # need to declare this so we don't change num
    # will be our iterator for our textCost array
    s = num

    # We will print our text from a bottom up fashion
    # since it's easier to do this way
    while s > 0:
        textC = textCost[s - 1]
        #print textCost

        # first position of the current line
        firstpos = ''

        # append the right words to the beginning word of that line
        for i in range(textC, s):
            firstpos += ' ' + words[i]
            #print line
        
        # declare the line
        if s == num:
            text = firstpos

        # now go to a new line
        else:
            text = firstpos + '\n' + text
            #print text

        # now set the iterator for next line 
        s = textC

    return opt, text


# Opening the text and splitting the words
with open('buffy.txt', 'r') as f:
    fulltext = f.read()

    text = fulltext.split()

    length = len(text)

    (cost, text) = neatPrint(text, 40, length)

     
    print text
    print cost
