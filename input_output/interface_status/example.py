import json

HEADER = """Name:     Status:
-----------------\n"""

def status(if_statuses):
    status = HEADER
    status_template = "{0:<9} {1:<4}\n"
    if if_statuses is None:
        return status
    if_statuses = json.loads(if_statuses)
    for if_status in if_statuses:
        name = if_status["name"]
        st = if_status["status"]
        status_line = status_template.format(name, st)
        status += status_line
    return status


