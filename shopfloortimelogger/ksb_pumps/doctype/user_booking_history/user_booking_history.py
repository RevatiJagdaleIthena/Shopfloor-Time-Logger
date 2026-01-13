# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class UserBookingHistory(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		actual_operation_qty: DF.Float
		actual_operation_time: DF.Float
		booked_qty: DF.Float
		confirmation_number: DF.Data | None
		material_description: DF.Data | None
		operation_description: DF.Data | None
		operator_ticket_no: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		production_log_created: DF.Check
		setup_time: DF.Float
		shift_name: DF.Data | None
		total_operation_time: DF.Float
		work_centre: DF.Data | None
	# end: auto-generated types
	pass
