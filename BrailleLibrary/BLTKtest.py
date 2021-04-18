#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shriamrut14
"""
import unittest
import string
from BLTK import *

class Test(unittest.TestCase):
    
    def test_isEnglishAvailable(self):
        message = "isEnglishAvailable() failed"
        self.assertEqual(isEnglishAvailable('a'),True,message)
        self.assertEqual(isEnglishAvailable('@'),False,message)
        self.assertEqual(isEnglishAvailable(None),False,message)
        
    def test_isBrailleAvailable(self):
        message = "isBrailleAvailable() failed"
        self.assertEqual(isBrailleAvailable('⠼⠁'),True,message)
        self.assertEqual(isBrailleAvailable('@'),False,message)
        self.assertEqual(isBrailleAvailable(None),False,message)
        
    def test_get_english_character(self):
        message = "get_english_character() failed"
        self.assertEqual(get_english_character('⠃'),'b',message)
        self.assertEqual(get_english_character('⠼⠋'),'6',message)
        self.assertEqual(get_english_character('^'),None,message)
        self.assertEqual(get_english_character(None),None,message)
    
    def test_get_braille_character(self):
        message = "get_braille_character() failed"
        self.assertEqual(get_braille_character('b'),'⠃',message)
        self.assertEqual(get_braille_character('6'),'⠼⠋',message)
        self.assertEqual(get_braille_character(None),None,message)
        
    def test_Interconvertions(self):
        message = "Interconvertions failed"
        self.assertEqual(convertBrailleWordToEnglish(convertEnglishWordtoBraille("12")),"12",message)
        self.assertEqual(convertBrailleWordToEnglish(convertEnglishWordtoBraille("1b!")),"1b!",message)
        self.assertEqual(convertBrailleWordToEnglish(convertEnglishWordtoBraille("1@")),"1",message)
        self.assertEqual(convertBrailleWordToEnglish(convertEnglishWordtoBraille("1@2")),"12",message)
    
    def test_isupper(self):
        # check if its caps
        message ="isupper() failed"
        self.assertEqual(isupper('⠠⠁'),True,message)
        for char in string.ascii_uppercase:
            self.assertEqual(isupper(convertEnglishWordtoBraille(char)),True,message)
        for char in string.ascii_lowercase:
            self.assertEqual(isupper(convertEnglishWordtoBraille(char)),False,message)
        #random chars if any
        self.assertEqual(isupper("@"),False,message)
        
    def test_tolower(self):
        message = "tolower() failed"
        #check tolower convertion is working for upper and lower case characters
        for char in string.ascii_uppercase:
            self.assertEqual(tolower(convertEnglishWordtoBraille(char)),convertEnglishWordtoBraille(char.lower()),message)
        for char in string.ascii_lowercase:
            self.assertEqual(tolower(convertEnglishWordtoBraille(char.lower())),convertEnglishWordtoBraille(char.lower()),message)
        self.assertEqual(tolower(convertEnglishWordtoBraille("ABCD")),convertEnglishWordtoBraille("abcd"),message)
        self.assertEqual(tolower(convertEnglishWordtoBraille("Hello")+" "+convertEnglishWordtoBraille("World")),convertEnglishWordtoBraille("hello")+" "+convertEnglishWordtoBraille("world"),message)
        self.assertEqual(tolower(convertEnglishWordtoBraille("Zxyw")),convertEnglishWordtoBraille("zxyw"),message)
        self.assertEqual(tolower(convertEnglishWordtoBraille("xAywAA")),convertEnglishWordtoBraille("xaywaa"),message)
    
    def test_cleanup(self):
        message = "cleanup() failed"
        #Hello World text with different unwanted characters in between
        self.assertEqual(cleanup("⠠⠓⠑⠇⠇⠕@⠠⠺⠕⠗⠇⠙"),"⠠⠓⠑⠇⠇⠕⠠⠺⠕⠗⠇⠙",message)
        self.assertEqual(cleanup(".@#123⠠⠓⠑⠇⠇⠕@⠠⠺⠕⠗⠇⠙"),"⠠⠓⠑⠇⠇⠕⠠⠺⠕⠗⠇⠙",message)
        self.assertEqual(cleanup("⠠⠓⠑⠇⠇⠕ ⠠⠺⠕⠗⠇⠙"),"⠠⠓⠑⠇⠇⠕ ⠠⠺⠕⠗⠇⠙",message)
if __name__=="__main__":
    unittest.main()
    '''for letter in english_to_braille.keys():
        if letter.isupper():
            caps = convertText(letter)        
            smallA = caps[1:]
            assert(letter.lower(),convertBrailleWordToEnglish(smallA))
    '''