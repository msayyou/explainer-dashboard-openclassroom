"""
Deploy the dashboard as an application.
"""

from explainerdashboard import ExplainerDashboard, ClassifierExplainer
from flask import Flask

app = Flask(__name__)


explainer = ClassifierExplainer.from_file('explainer_1.joblib')
db = ExplainerDashboard(explainer,server=app, url_base_pathname="/dashboard/")

@app.route('/dashboard')
def return_dashboard():
    return db.app.index()
