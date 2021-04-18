#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Libraries used
from pybraille import convertText

braille_to_english = {}
english_to_braille = {}
punctuations = "!$'(),-./:;?" # Note these are the punctuations for which braille is available
braille_punctuations = []
string_vocab="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!$'(),-./:;?"

for c in string_vocab:
    braille_to_english[convertText(c)]=c
    english_to_braille[c]=convertText(c)
    
def get_all_available_characters_english():
    return english_to_braille.keys()
    
def get_all_available_characters_braille():
        return braille_to_english.keys()
    
def isEnglishAvailable(character):
    if character in get_all_available_characters_english():
        return True
    else:
        return False   
        
def isBrailleAvailable(character):
    if character in get_all_available_characters_braille():
        return True
    else:
        return False  

def get_english_character(character):
    if isBrailleAvailable(character)==False:
        return None
        
    return braille_to_english[character]
    
def get_braille_character(character):
    if isEnglishAvailable(character)==False:
        return None
    return english_to_braille[character]
      
def convertBrailleWordToEnglish(braille_text):
    #Iterate through characters of braille_text and perform conversion
    result = ""
    i=0
    while i<len(braille_text): 
        #for braille character that used 1 byte space
        if isBrailleAvailable(braille_text[i]):
            result += braille_to_english[braille_text[i]]
            i=i+1
        #for braille character that used 2 byte space
        elif i+1 < len(braille_text) and isBrailleAvailable(braille_text[i:i+2]):
            result += braille_to_english[braille_text[i:i+2]]
            i=i+2
            #unknown letters if any
        else:
            result +=""
            i=i+1
    return result

def convertEnglishWordtoBraille(text):
    #convertText module for converting words had issues
    #hence converting text by converting characters to braille
    result = ""
    for c in text:
        if isEnglishAvailable(c):
            result+=convertText(c)
        else:
            #do nothing
            pass
    return result

def isupper(braille_character):
    english_character = convertBrailleWordToEnglish(braille_character)
    if english_character.isupper():
        return True
    else:
        return False
    
def tolower(braille_text):
    i=0
    result = ""
    while i<len(braille_text):
        if braille_text[i]==" ":
            result = result + braille_text[i]
            i=i+1
        elif i+1 < len(braille_text) and isBrailleAvailable(braille_text[i:i+2]):
            if isupper(braille_text[i:i+2]):
                # so replacing the first dot, basically convert upper to lower
                result = result + braille_text[i+1]
                i=i+2
        else:
            result = result + braille_text[i]
            i=i+1
    return result

def cleanup(braille_text):
    i=0
    result = ""
    while i<len(braille_text):
        if braille_text[i]==" ":
            result = result + braille_text[i]
            i=i+1
        elif i+1 < len(braille_text) and isBrailleAvailable((braille_text[i:i+2])):
            result = result + braille_text[i:i+2]
            i=i+2
        elif isBrailleAvailable(braille_text[i]):
            result = result + braille_text[i]
            i=i+1
        else:
            # ignore unwanted characters
            i=i+1
            pass
    return result
            
# word_tokenize (best way is to use split)
# remove stop words (stop words in braille, get them in braille)
# remove available braille punctuations (try using regex on unicodes)
# other preprocessing are also welcome do explore