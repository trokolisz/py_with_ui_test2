import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

# Sample Data
data = [
    {"id": "123456", "name": "Alice", "username": "alice123", "enabled": True, "permissions": ["read", "write"]},
    {"id": "234567", "name": "Bob", "username": "bob234", "enabled": False, "permissions": ["read"]},
    {"id": "345678", "name": "Charlie", "username": "charlie345", "enabled": True, "permissions": ["write"]},
]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

def generate_table(data):
    table_rows = []
    for i, row in enumerate(data):
        row_color = "table-light" if i % 2 == 0 else "table-secondary"
        table_rows.append(
            html.Tr([
                html.Td(row["id"]),
                html.Td(row["name"]),
                html.Td(row["username"]),
                html.Td(dbc.Badge("Enabled", color="success") if row["enabled"] else dbc.Badge("Disabled", color="danger")),
                html.Td(
                    dbc.Button("Permissions", id={"type": "dropdown-button", "index": row["id"]}, n_clicks=0, color="info", size="sm")
                ),
            ], id={"type": "table-row", "index": row["id"]}, className=row_color)
        )
        table_rows.append(
            html.Tr([
                html.Td(
                    dbc.Collapse(
                        dbc.Card(
                            dbc.CardBody(
                                [dbc.Badge(permission, color="primary", className="mr-1") for permission in row["permissions"]]
                            )
                        ),
                        id={"type": "collapse", "index": row["id"]},
                        is_open=False,
                    ),
                    colSpan=5  # Span across all columns
                ),
            ], style={"display": "none"}, id={"type": "collapse-row", "index": row["id"]})
        )
    return table_rows

app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            dcc.Input(id="search-bar", placeholder="Search...", type="text", value="", className="form-control mb-3"),
            width={"size": 6, "offset": 3}
        ),
    ),
    dbc.Row(
        dbc.Col(
            dbc.Table(id="table", children=generate_table(data), striped=True, bordered=True, hover=True, responsive=True, className="table-sm")
        )
    )
])

@app.callback(
    Output("table", "children"),
    Input("search-bar", "value")
)
def update_table(search_value):
    filtered_data = [row for row in data if search_value.lower() in row["name"].lower() or search_value.lower() in row["username"].lower() or search_value.lower() in row["id"]]
    return generate_table(filtered_data)

@app.callback(
    Output({"type": "collapse", "index": dash.dependencies.ALL}, "is_open"),
    Input({"type": "dropdown-button", "index": dash.dependencies.ALL}, "n_clicks"),
    State({"type": "collapse", "index": dash.dependencies.ALL}, "is_open"),
)
def toggle_collapse(n_clicks_list, is_open_list):
    return [not is_open if n_clicks > 0 else is_open for n_clicks, is_open in zip(n_clicks_list, is_open_list)]

if __name__ == "__main__":
    app.run_server(debug=True)
