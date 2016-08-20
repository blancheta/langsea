from langsea import Word
import unittest


class TestWordModel(unittest.TestCase):

	def test_can_create_a_valid_word(self):
		self.assertTrue(Word(id=0, name="testpic", image="testpic.png", category="nature"))

	def test_cannot_create_an_invalid_word(self):
		with self.assertRaises(TypeError):
			self.assertFalse(Word())
