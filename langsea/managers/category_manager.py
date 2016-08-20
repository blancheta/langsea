#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from langsea.models.category import Category


class CategoryManager:

	categories_api_url = 'http://www.langsea.org/api/categories/'

	def all(self):
		response = requests.get(self.categories_api_url)

		if response.ok:

			categories = []

			for category_json in response.json():

				categories.append(Category(*category_json))

		return categories

	def get(self, name):
		response = requests.get(self.categories_api_url + name)
		category = None
		if response.ok:
			category = Category(*response.json())
		return category
