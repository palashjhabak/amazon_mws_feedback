# -*- coding: utf-8 -*-
# Copyright (c) 2019, Techlift Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import datetime
from frappe.model.document import Document

class AmazonFeedbackRequest(Document):
	def send_feedback(self):
		amazon_mws_feedback_settings = frappe.get_doc('Amazon MWS Feedback Settings')
		feedback_base_url = amazon_mws_feedback_settings.feedback_base_url
		number_of_reminders = amazon_mws_feedback_settings.number_of_reminders
		customer_name = self.customer_name
		delivery_date = self.delivery_date
		todays_date = datetime.date.today() 

		date_difference = (todays_date - delivery_date).days

		if date_difference < 1:
			return

		phone = self.phone
		order_id = self.order_id
		is_send_sms = self.send_sms
		number_of_sent_sms = self.number_of_sent_sms
		final_url = feedback_base_url + order_id

		if not feedback_base_url:
			frappe.throw('Base Url is Empty')

		if number_of_sent_sms < number_of_reminders and is_send_sms == 'Yes':
			from frappe.core.doctype.sms_settings.sms_settings import send_sms
			message_sms = """Hi {0},\n\nThanks for Shopping with Everyday Kitchen on Amazon.\n\nPlease share your feedback by clicking on {1}\n\nTeam Everyday Kitchen""".format(customer_name, final_url)
			try:
				send_sms([phone], message_sms)
				self.number_of_sent_sms = number_of_sent_sms + 1
				self.save()
			except:
				pass

def send_amazon_feedback():
	amazon_mws_feedback_settings = frappe.get_doc('Amazon MWS Feedback Settings')
	feedback_base_url = amazon_mws_feedback_settings.feedback_base_url
	number_of_reminders = amazon_mws_feedback_settings.number_of_reminders

	all_orders_for_reminders = frappe.get_all('Amazon Feedback Request', filters={'send_sms': 'Yes'})

	for order in all_orders_for_reminders:
		order_doc = frappe.get_doc('Amazon Feedback Request', order)
		if order_doc:
			if order_doc.number_of_sent_sms < number_of_reminders:
				order_doc.send_feedback()
