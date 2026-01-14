# shopfloortimelogger/shopfloor_time_logger/desktop.py
from frappe import _

def get_data():
    return [
        {
            "module_name": "Shopfloor Time Logger",
            "category": "Modules",
            "color": "#3498db",
            "icon": "fa fa-industry",
            "type": "module",
            "label": _("Shopfloor Time Logger")
        }
    ]
