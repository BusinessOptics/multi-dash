import dash_html_components as html

layout = html.Div(
    children=[
        html.H1(children="Dashboard 1"),
        html.Div(
            children="""
            This dashboard is first
        """
        ),
    ]
)

def create_app(factory):
    app = factory(__name__)
    app.layout = layout
    return app