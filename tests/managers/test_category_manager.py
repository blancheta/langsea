from langsea import Category, CategoryManager

import unittest


class TestCategoryManager(unittest.TestCase):

	def setUp(self):
		self.category_manager = CategoryManager()

	def test_can_get_all_categories(self):
		categories = self.category_manager.all()

		for categ in categories:
			self.assertIsInstance(categ, Category)

	def test_can_get_one_category(self):
		category = self.category_manager.get(name="fruits")
		self.assertIsInstance(category, Category)
