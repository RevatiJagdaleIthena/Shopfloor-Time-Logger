# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ProductionLog(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		actual_operation_qty: DF.Float
		booked_qty: DF.Data | None
		confirmation_number: DF.Data | None
		date: DF.Date | None
		downtime: DF.Float
		material_description: DF.Data | None
		operator_dashboard: DF.Link | None
		operator_ticket: DF.Data | None
		plant: DF.Data | None
		production_order: DF.Data | None
		reason_code: DF.Link | None
		setup_time: DF.Float
		shift: DF.Data | None
		total_operation_time: DF.Float
		work_centre: DF.Data | None
	# end: auto-generated types
	pass
