incident_db = []

def handle_incident(data):
    incident = {
        'id': len(incident_db) + 1,
        'title': data.get('title'),
        'description': data.get('description'),
        'severity': data.get('severity'),
        'status': 'Open'
    }
    incident_db.append(incident)
    return incident

def get_all_incidents():
    return incident_db
