from dirty_poetry.utils import get_final_phonemes
import unittest
import pdb


class TestFinalPhonemes(unittest.TestCase):

    def test_with_real_word(self):
        word = "house"
        fp = get_final_phonemes(word, "w")
        assert fp == ['AW1', 'S']

    def test_with_one_syllable_word(self):
        word = "I"
        fp = get_final_phonemes(word, "w")
        assert fp == ['AY1']

    def test_with_partial_word(self):
        word = "aardwolf"
        fp = get_final_phonemes(word, "w")
        assert fp == ['L', 'F']
    
    def test_with_nonsense_word(self):
        word = "anaH9|;':v"
        fp = get_final_phonemes(word, "n")
        assert fp == ['V', 'IY1']
