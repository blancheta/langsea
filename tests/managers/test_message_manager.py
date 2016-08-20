from langsea import Message, MessageManager
import unittest


class TestMessageManager(unittest.TestCase):

	def setUp(self):
		self.message_manager = MessageManager()

	def test_can_get_all_messages(self):
		messages = self.message_manager.all(
			date_from="2015-08-07 10:15:00",
			date_to="2016-08-07 10:15:00"
		)

		for message in messages:
			self.assertIsInstance(message, Message)
			# between date_from and date_to

	def test_can_get_one_message_by_id(self):
		id_searched = 2
		message = self.message_manager.get(id=id_searched)
		self.assertIsInstance(message, Message)
		self.assertEqual(message.id, id_searched)
