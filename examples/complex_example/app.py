from flask import Flask
from multi_dash import MultiDash

app = Flask(__name__)

(
    MultiDash(server=app, template="complex_shell.html.j2").register_dash(
        module_name="complex_example.dashboards.dashboard_1.app", title="Dashboard One"
    )
)
