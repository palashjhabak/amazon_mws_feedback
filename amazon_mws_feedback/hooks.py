# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "amazon_mws_feedback"
app_title = "Amazon MWS Feedback"
app_publisher = "Techlift Technologies"
app_description = "Amazon MWS Feedback"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "palash@techlift.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/amazon_mws_feedback/css/amazon_mws_feedback.css"
# app_include_js = "/assets/amazon_mws_feedback/js/amazon_mws_feedback.js"

# include js, css files in header of web template
# web_include_css = "/assets/amazon_mws_feedback/css/amazon_mws_feedback.css"
# web_include_js = "/assets/amazon_mws_feedback/js/amazon_mws_feedback.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "amazon_mws_feedback.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "amazon_mws_feedback.install.before_install"
# after_install = "amazon_mws_feedback.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "amazon_mws_feedback.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	"all": [
		"amazon_mws_feedback.amazon_mws_feedback.doctype.amazon_feedback_request.amazon_feedback_request.send_amazon_feedback"
	]
}

# scheduler_events = {
# 	"all": [
# 		"amazon_mws_feedback.tasks.all"
# 	],
# 	"daily": [
# 		"amazon_mws_feedback.tasks.daily"
# 	],
# 	"hourly": [
# 		"amazon_mws_feedback.tasks.hourly"
# 	],
# 	"weekly": [
# 		"amazon_mws_feedback.tasks.weekly"
# 	]
# 	"monthly": [
# 		"amazon_mws_feedback.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "amazon_mws_feedback.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "amazon_mws_feedback.event.get_events"
# }

