import unicodedata
import pronouncing
import string

import re
from spacy.lang.en import English
from spacy.tokenizer import Tokenizer


def tokenizer():
    
    nlp = English()
    infix_re = re.compile(r'''[ ]''')
    en_suffix_search =  nlp.tokenizer.suffix_search
    return Tokenizer(nlp.vocab, infix_finditer=infix_re.finditer, suffix_search=en_suffix_search)


def nonsense_metre(tokens, real_words):
    pattern = ""  
    for token in tokens:
        word = token.text
        if word not in string.punctuation: # skip single punctuation marks
            if word.lower() in real_words: # if it is in our giganto list of words
                pattern += "w" #real word 
            else:
                pattern += "n"
    return pattern

def nonsense_percent(metre):
    return metre.count("n")/len(metre)

def get_final_phonemes(word, metrical_unit):
    final_phone = [""]
    if metrical_unit == "w":
        for i in range(len(word)):
            phones = pronouncing.phones_for_word(word[i:])
            if phones:
                final_phone = phones[0].split()[-2:]
                break
    else:
        last_char = word[-1]
        try:
            full_name = unicodedata.name(last_char).split()
        except ValueError:
            print(f"No final phoneme for {word}")
            full_name = False
        if full_name:
            name = full_name[-1]
            phones = pronouncing.phones_for_word(name)
            if phones:
                final_phone = phones[0].split()[-4:]
    return final_phone