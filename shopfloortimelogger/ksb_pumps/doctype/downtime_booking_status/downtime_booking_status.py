# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DowntimeBookingStatus(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		downtime: DF.Int
		downtime_log_created: DF.Check
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		reason_code: DF.Link | None
		reason_description: DF.Data | None
		reason_type: DF.Data | None
		remark: DF.Data | None
		work_centre: DF.Data | None
	# end: auto-generated types
	pass
