#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Word:

	def __init__(self, id, name, image, category=None):
		self.id = id
		self.name = name
		self.image = image
		self.category = category
