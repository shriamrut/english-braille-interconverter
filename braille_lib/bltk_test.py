#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shriamrut14
"""
import unittest
import string
from bltk import *

class Test(unittest.TestCase):
    
    def test_is_english_available(self):
        message = "is_english_available failed"
        self.assertEqual(is_english_available('a'),True,message)
        self.assertEqual(is_english_available('@'),False,message)
        self.assertEqual(is_english_available(None),False,message)
        
    def test_is_braille_available(self):
        message = "is_braille_available() failed"
        self.assertEqual(is_braille_available('⠼⠁'),True,message)
        self.assertEqual(is_braille_available('@'),False,message)
        self.assertEqual(is_braille_available(None),False,message)
        
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
        
    def test_interconvertions(self):
        message = "interconvertions failed"
        self.assertEqual(convert_braille_word_to_english(convert_english_word_to_braille("12")),"12",message)
        self.assertEqual(convert_braille_word_to_english(convert_english_word_to_braille("1b!")),"1b!",message)
        self.assertEqual(convert_braille_word_to_english(convert_english_word_to_braille("1@")),"1",message)
        self.assertEqual(convert_braille_word_to_english(convert_english_word_to_braille("1@2")),"12",message)
    
    def test_isupper(self):
        # check if its caps
        message ="isupper() failed"
        self.assertEqual(isupper('⠠⠁'),True,message)
        for char in string.ascii_uppercase:
            self.assertEqual(isupper(convert_english_word_to_braille(char)),True,message)
        for char in string.ascii_lowercase:
            self.assertEqual(isupper(convert_english_word_to_braille(char)),False,message)
        #random chars if any
        self.assertEqual(isupper("@"),False,message)
        
    def test_tolower(self):
        message = "tolower() failed"
        #check tolower convertion is working for upper and lower case characters
        for char in string.ascii_uppercase:
            self.assertEqual(tolower(convert_english_word_to_braille(char)),convert_english_word_to_braille(char.lower()),message)
        for char in string.ascii_lowercase:
            self.assertEqual(tolower(convert_english_word_to_braille(char.lower())),convert_english_word_to_braille(char.lower()),message)
        self.assertEqual(tolower(convert_english_word_to_braille("ABCD")),convert_english_word_to_braille("abcd"),message)
        self.assertEqual(tolower(convert_english_word_to_braille("Hello")+" "+convert_english_word_to_braille("World")),convert_english_word_to_braille("hello")+" "+convert_english_word_to_braille("world"),message)
        self.assertEqual(tolower(convert_english_word_to_braille("Zxyw")),convert_english_word_to_braille("zxyw"),message)
        self.assertEqual(tolower(convert_english_word_to_braille("xAywAA")),convert_english_word_to_braille("xaywaa"),message)
    
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
            assert(letter.lower(),convert_braille_word_to_english(smallA))
    '''