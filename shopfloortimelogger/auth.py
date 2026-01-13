import frappe

def login_redirect(*args, **kwargs):
    bootinfo = kwargs.get("bootinfo")
    if not bootinfo:
        return

    user = frappe.session.user
    roles = frappe.get_roles(user)

    # 🔒 FORCE frappe to ignore last visited route
    bootinfo["disable_last_route"] = True
    bootinfo["disable_redirect"] = True

    if user == "Administrator":
        return

    if "Work Centre Supervisor" in roles:
        bootinfo["redirect"] = "/sp-screen"
        return

    if "Work Centre" in roles:
        bootinfo["redirect"] = "/app/operator-dashboard/view/list"
        return
