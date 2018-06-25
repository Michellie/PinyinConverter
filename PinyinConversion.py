"""
Date: 17/06/18
Author: Michelle Arthars
This program takes in a text file of improper pinyin and
produces an output file containing pinyin with the correct tonal marks.
"""



def toneMarks(letter, tone):
    toneList = ['āáǎà', 'ēéěè', 'īíǐì', 'ōóǒò', 'ūúǔù', 'ĀÁǍÀ', 'ĒÉĚÈ', 'ĪÍǏÌ', 'ŌÓǑÒ', 'ŪÚǓÙ']
    return toneList[letter][tone]



def pinyinConvert(content):
    vowels = 'aeiouAEIOU'
    holder = -1
    convertText = ''
    prevchar = ''
    for c in content:
        if c.isalpha() == 1:  # differentiating numbers and letters
            if len(prevchar) > 0:
                convertText += prevchar              # prev letter doesn't have tone mark
                prevchar = ''
            charpos = vowels.find(c)                 # determine if character is a vowel
            if charpos != -1:
                holder = charpos                     # holds the vowel position in the tone array
                prevchar = c                         # replace prevchar with new character
            else:
                convertText += c
        elif '0' <= c < '5':
            if holder != -1 and len(prevchar) > 0:
                tone = int(c) % 5 - 1                # gets tone mark position
                pinyin = toneMarks(holder, tone)     # append converted character retrieves from
                holder = -1                          # clear holder value
                prevchar = ''
                convertText += pinyin
            else:
                convertText += c
        else:
            if len(prevchar) > 0:
                convertText += prevchar
            prevchar = ''
            convertText += c  # append integers and symbols to output
    return convertText


def main():
    print("Welcome. This program will help you produce a text file with the proper pinyin tone marls.")
    fileName = input("Convert file: ")
    fopen = open(fileName, "r")
    content = fopen.read()
    print("Original Text: ")
    print(content,"\n")
    convertedText = pinyinConvert(content)
    print("Converted Text:" + convertedText)


main()
