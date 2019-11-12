import dash_html_components as html

layout = html.Div(
    children=[html.H1("Dashboard 1"), html.Div("This dashboard is first")]
)


def create_app(factory):
    app = factory(__name__, external_stylesheets=["/static/dashboard_1.css"])
    app.layout = layout
    return app
