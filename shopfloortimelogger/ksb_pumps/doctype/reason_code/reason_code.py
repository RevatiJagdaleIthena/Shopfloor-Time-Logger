# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ReasonCode(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		enabled_for_breakdown: DF.Check
		reason_code: DF.Data
		reason_description: DF.Data | None
		reason_type: DF.Data | None
	# end: auto-generated types
	pass
