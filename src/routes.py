from flask import render_template, request, redirect
from incident_workflow import handle_incident, get_all_incidents

def setup_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/incident-form')
    def incident_form():
        return render_template('incident_form.html')

    @app.route('/submit-incident', methods=['POST'])
    def submit_incident():
        handle_incident(request.form)
        return redirect('/report')

    @app.route('/report')
    def report():
        incidents = get_all_incidents()
        return render_template('report.html', incidents=incidents)
