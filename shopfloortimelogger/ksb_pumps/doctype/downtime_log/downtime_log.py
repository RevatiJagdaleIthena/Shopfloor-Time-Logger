# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DowntimeLog(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		confirmation_number: DF.Data | None
		date: DF.Date | None
		downtime: DF.Data | None
		operator_dashboard: DF.Link | None
		operator_ticket_no: DF.Data | None
		production_order: DF.Data | None
		reason_code: DF.Data | None
		reason_description: DF.Data | None
		reason_type: DF.Data | None
		remark: DF.Data | None
		shift_name: DF.Data | None
		work_centre: DF.Data | None
	# end: auto-generated types
	pass
