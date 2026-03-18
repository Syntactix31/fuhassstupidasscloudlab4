import azure.functions as func
import json
import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:
    tasks_near_deadline = [
        {"id": 1, "title": "Lab 4 Due Tomorrow!", "due_date": "2026-03-18"}
    ]
    
    notification = {
        "message": f"{len(tasks_near_deadline)} tasks near deadline!",
        "tasks": tasks_near_deadline,
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    return func.HttpResponse(
        json.dumps(notification, indent=2),
        status_code=200,
        mimetype="application/json"
    )
