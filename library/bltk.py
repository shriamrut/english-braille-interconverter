import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

braille_to_english = {}
english_to_braille = {}
punctuations = "!$'(),-./:;?" # Note these are the punctuations for which braille is available
string_vocab="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!$'(),-./:;?"

character_to_braille_unicodes = {'a': '\u2801', 'b': '\u2803', 'k': '\u2805', 'l': '\u2807', 'c': '\u2809', 'i': '\u280A',
'f': '\u280B', 'm': '\u280D', 's': '\u280E', 'p': '\u280F', 'e': '\u2811', 'h': '\u2813', 'o': '\u2815', 'r': '\u2817',
'd': '\u2819', 'j': '\u281A', 'g': '\u281B', 'n': '\u281D', 't': '\u281E', 'q': '\u281F', 'u': '\u2825', 'v': '\u2827',
'x': '\u282D', 'z': '\u2835', 'w': '\u283A', 'y': '\u283D', 'num': '\u283C', 'caps': '\u2820', '.': '\u2832',
"'": '\u2804', ',': '\u2802', '-': '\u2824', '/': '\u280C', '!' : '\u2816', '?': '\u2826', '$': '\u2832', ':': '\u2812',
';': '\u2830', '(': '\u2836', ')': '\u2836', ' ': ' ', '1': '\u2801', '2': '\u2803', '3': '\u2809', '4': '\u2819',
'5': '\u2811', '6': '\u280B', '7': '\u281B', '8': '\u2813', '9': '\u280A', '0': '\u281A'}

#function to generate braille patterns for the corresponding text, numbers or special characters
def get_braille_character(character):
  braille_character = ''
  if character.isupper():
    braille_character += character_to_braille_unicodes.get('caps')
    braille_character += character_to_braille_unicodes.get(character.lower())
  elif character.isdigit():
    braille_character += character_to_braille_unicodes.get('num')
    braille_character += character_to_braille_unicodes.get(character)
  elif character in character_to_braille_unicodes.keys():
    braille_character += character_to_braille_unicodes.get(character)
  return braille_character

for c in string_vocab:
    braille_to_english[get_braille_character(c)]=c
    english_to_braille[c]=get_braille_character(c)
    
def get_all_available_characters_english():
    return english_to_braille.keys()
    
def get_all_available_characters_braille():
        return braille_to_english.keys()
    
def is_english_available(character):
    if character in get_all_available_characters_english():
        return True
    else:
        return False   
        
def is_braille_available(character):
    if character in get_all_available_characters_braille():
        return True
    else:
        return False  

def get_english_character(character):
    if is_braille_available(character)==False:
        return None
        
    return braille_to_english[character]
    
def get_braille_character(character):
    if is_english_available(character)==False:
        return None
    return english_to_braille[character]

######function to convert text to braille ######
def convert_english_text_to_braille_text(english_text):
    result_array_braille = []
    for word in word_tokenize(english_text):
        result_array_braille.append(convert_english_word_to_braille(word))
    result_braille = ' '.join(result_array_braille)
    return result_braille


def convert_english_word_to_braille(text):
    #hence converting text by converting characters to braille'
    result = ""
    if text=="\n" or text=="\t":
      result = text
      return result
    for c in text:
        if is_english_available(c):
            result+=english_to_braille[c]
        else:
            #do nothing
            pass
    return result

#####function to convert braille to text#######
def convert_braille_text_to_english_text(braille_text):
    result_array_english = []
    for word in braille_text.split(' '):
      result_array_english.append(convert_braille_word_to_english(word))
    result_english = ' '.join(result_array_english)
    return result_english

def convert_braille_word_to_english(braille_text):
    #Iterate through characters of braille_text and perform conversion
    result = ""
    i=0
    while i<len(braille_text): 
        #for braille character that used 1 byte space
        if is_braille_available(braille_text[i]):
            result += braille_to_english[braille_text[i]]
            i=i+1
        #for braille character that used 2 byte space
        elif i+1 < len(braille_text) and is_braille_available(braille_text[i:i+2]):
            result += braille_to_english[braille_text[i:i+2]]
            i=i+2
            #unknown letters if any
        else:
            result +=""
            i=i+1
    return result

def isupper(braille_character):
    english_character = convert_braille_word_to_english(braille_character)
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
        elif i+1 < len(braille_text) and is_braille_available(braille_text[i:i+2]):
            if isupper(braille_text[i:i+2]):
                # so replacing the first dot, basically convert upper to lower
                result = result + braille_text[i+1]
                i=i+2
        else:
            result = result + braille_text[i]
            i=i+1
    return result
