# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.telemetry import capture


@frappe.whitelist()
def is_enabled():
    return frappe.get_system_settings().enable_telemetry


@frappe.whitelist()
def get_credentials():
    return {
        "project_id": frappe.conf.get("posthog_project_id"),
        "telemetry_host": frappe.conf.get("posthog_host"),
    }


def track(event):
    return capture(event, "insights")