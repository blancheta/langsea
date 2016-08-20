from langsea import Message, Word
import unittest


class TestMessageModel(unittest.TestCase):

	def test_can_create_a_valid_message(self):

		words = [
			Word(id=0, name="testpic", image="testpic.png", category="nature"),
			Word(id=1, name="testpic2", image="testpic2.png", category="drink")
		]

		self.assertTrue(Message(0, words))

	def test_cannot_create_an_invalid_message(self):
		with self.assertRaises(TypeError):
			self.assertFalse(Message())
