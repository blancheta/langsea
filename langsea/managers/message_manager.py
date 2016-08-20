#!/usr/bin/env python
# -*- coding: utf-8 -*-
from langsea.models.word import Word
from langsea.models.message import Message
import requests


class MessageManager:

	messages_api_url = 'http://www.langsea.org/api/messages/'

	def all(self, date_from=None, date_to=None):

		response = requests.get(self.messages_api_url)
		messages = []

		if response.ok:

			for message_json in response.json():

				words_json = message_json['words']
				words = []

				for word_json in words_json:
					words.append(Word(*word_json))

				messages.append(Message(id=message_json['id'], words=words))

		return messages

	def get(self, id=None):

		response = requests.get(self.messages_api_url + str(id))
		if response.ok:
			message_json = response.json()
			words_json = message_json['words']
			words = []
			for word_json in words_json:
				words.append(Word(*word_json))

			return Message(id=message_json['id'], words=words)

		return None
