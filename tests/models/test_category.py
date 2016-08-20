from langsea import Category
import unittest


class TestCategoryModel(unittest.TestCase):

	def test_can_create_a_valid_category(self):
		self.assertTrue(Category(id=0, name="nature", image="nature.png"))

	def test_cannot_create_an_invalid_category(self):
		with self.assertRaises(TypeError):
			self.assertTrue(Category())
