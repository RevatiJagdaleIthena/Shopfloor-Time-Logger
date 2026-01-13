# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class OperatorDashboard(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.ksb_pumps.doctype.downtime_booking_status.downtime_booking_status import DowntimeBookingStatus
		from frappe.ksb_pumps.doctype.user_booking_history.user_booking_history import UserBookingHistory
		from frappe.types import DF

		actual_operation_qty: DF.Float
		actual_operation_time: DF.Float
		actual_setup_time: DF.Float
		alt_work_centre: DF.Data | None
		amended_from: DF.Link | None
		balance_operation_time: DF.Data | None
		balanced_operation_qty: DF.Data | None
		confirmation_number: DF.Link | None
		date: DF.Date | None
		downtime_booking_status: DF.Table[DowntimeBookingStatus]
		material_code: DF.Data | None
		material_description: DF.Data | None
		operation_description: DF.Data | None
		operation_no: DF.Data | None
		operation_qty: DF.Data | None
		operator_ticket_no: DF.Link | None
		plant: DF.Data | None
		production_order: DF.Data | None
		shift_name: DF.Link | None
		status: DF.Data | None
		std_operation_time: DF.Float
		std_setup_time: DF.Float
		user_booking_history: DF.Table[UserBookingHistory]
		work_centre: DF.Link | None
	# end: auto-generated types
	pass
