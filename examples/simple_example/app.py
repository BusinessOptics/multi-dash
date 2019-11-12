from flask import Flask
from multi_dash import MultiDash

app = Flask(__name__)

(
    MultiDash(
        server=app,
        template="multi_dash/example_base.html.j2"        
    ).register_dash(
        module_name="simple_example.dashboard_1", title="Dashboard One"
    ).register_dash(
        module_name="simple_example.dashboard_2", title="Dashboard Two"
    )
)