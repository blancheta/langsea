import unittest
from langsea import Word, WordManager


class TestWordManager(unittest.TestCase):

	def setUp(self):
		self.word_manager = WordManager()

	def test_can_get_all_word_for_a_category(self):
		words = self.word_manager.all(category="fruits")
		for word in words:
			self.assertIsInstance(word, Word)

	def test_can_get_one_word(self):
		word = self.word_manager.get(name="apple")
		self.assertIsInstance(word, Word)
