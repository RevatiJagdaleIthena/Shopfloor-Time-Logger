# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class OrderConfirmation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.ksb_pumps.doctype.downtime_booking_status.downtime_booking_status import DowntimeBookingStatus
		from frappe.ksb_pumps.doctype.user_booking_history.user_booking_history import UserBookingHistory
		from frappe.types import DF

		alternate_work_centre: DF.Data | None
		balance_operation_time: DF.Data | None
		balanced_operation_qty: DF.Data | None
		confirmation_number: DF.Data
		date: DF.Date | None
		downtime_booking_status: DF.Table[DowntimeBookingStatus]
		material_code: DF.Data | None
		material_description: DF.Data | None
		operation_description: DF.Data | None
		operation_qty: DF.Data | None
		operationnumber: DF.Data | None
		order_work_centre: DF.Data | None
		plant: DF.Data | None
		production_order: DF.Link | None
		std_operation_time: DF.Data | None
		std_setup_time: DF.Data | None
		user_booking_history: DF.Table[UserBookingHistory]
	# end: auto-generated types
	pass
