#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from langsea.models.word import Word


class WordManager:

	words_api_url = 'http://www.langsea.org/api/words'
	words_by_category_api_url = 'http://www.langsea.org/api/categories/{}/words'

	def all(self, category=None):

		words = []
		if category is not None:
			response = requests.get(self.words_by_category_api_url.format(category))
			if response.ok:
				words_json = response.json()
				for word_json in words_json:
					words.append(Word(*word_json))

		return words

	def get(self, name=None):
		return Word(id=0, name="testpic", image="testpic.png", category="nature")
