import dash_html_components as html

layout = html.Div(
    children=[
        html.H1(children="Dashboard 2"),
        html.Div(
            children="""
            This dashboard is second
        """
        ),
    ]
)

def create_app(factory):
    app = factory(__name__)
    app.layout = layout
    return app