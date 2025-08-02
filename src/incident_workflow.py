import sqlite3
from datetime import datetime

def get_db_connection():
    conn = sqlite3.connect('incidents.db')
    conn.row_factory = sqlite3.Row
    return conn

def handle_incident(data):
    """Create a new incident and store in database"""
    conn = get_db_connection()
    cursor = conn.execute('''
        INSERT INTO incidents (title, description, severity, status)
        VALUES (?, ?, ?, ?)
    ''', (data['title'], data['description'], data['severity'], 'Open'))
    
    incident_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    # Return the created incident
    return get_incident_by_id(incident_id)

def get_all_incidents():
    """Retrieve all incidents from database"""
    conn = get_db_connection()
    incidents = conn.execute('''
        SELECT * FROM incidents ORDER BY created_at DESC
    ''').fetchall()
    conn.close()
    return [dict(incident) for incident in incidents]

def get_incident_by_id(incident_id):
    """Get a specific incident by ID"""
    conn = get_db_connection()
    incident = conn.execute('''
        SELECT * FROM incidents WHERE id = ?
    ''', (incident_id,)).fetchone()
    conn.close()
    return dict(incident) if incident else None

def update_incident_status(incident_id, new_status):
    """Update the status of an incident"""
    conn = get_db_connection()
    conn.execute('''
        UPDATE incidents SET status = ? WHERE id = ?
    ''', (new_status, incident_id))
    conn.commit()
    conn.close()
    return get_incident_by_id(incident_id)