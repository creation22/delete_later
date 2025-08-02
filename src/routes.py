from flask import render_template, request, redirect, flash, jsonify
from incident_workflow import handle_incident, get_all_incidents, get_incident_by_id, update_incident_status

def setup_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/incident-form')
    def incident_form():
        return render_template('incident_form.html')

    @app.route('/submit-incident', methods=['POST'])
    def submit_incident():
        try:
            incident = handle_incident(request.form)
            flash(f'Incident "{incident["title"]}" has been successfully reported!', 'success')
            return redirect('/report')
        except Exception as e:
            flash(f'Error creating incident: {str(e)}', 'error')
            return redirect('/incident-form')

    @app.route('/report')
    def report():
        incidents = get_all_incidents()
        return render_template('report.html', incidents=incidents)

    @app.route('/incident/<int:incident_id>')
    def view_incident(incident_id):
        incident = get_incident_by_id(incident_id)
        if incident:
            return render_template('incident_detail.html', incident=incident)
        else:
            flash('Incident not found', 'error')
            return redirect('/report')

    @app.route('/update-status/<int:incident_id>', methods=['POST'])
    def update_status(incident_id):
        new_status = request.form.get('status')
        if new_status:
            try:
                update_incident_status(incident_id, new_status)
                flash('Incident status updated successfully!', 'success')
            except Exception as e:
                flash(f'Error updating status: {str(e)}', 'error')
        return redirect(f'/incident/{incident_id}')