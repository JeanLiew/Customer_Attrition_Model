import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = [dbc.themes.GRID, dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Customer Attrition Dashboard - Jean Liew'
df = pd.read_csv('../data/telco_clustered_ID.csv')

#title
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("Customer Attrition Dashboard", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ))], dark=True, sticky='top', color='dark', className="py-2")

#active users
au_card = dbc.Card([dbc.CardHeader('Customer Status'),
                    dbc.CardBody(html.H4('', id='status'))
                   ],className="my-2")

#revenue per quarter
revenue_card = dbc.Card([dbc.CardHeader('Total Revenue'),
                        dbc.CardBody(html.H4('',id='revenue'))
                        ], className="my-2")

#input cust ID
cust_id_input = dcc.Dropdown(id='cust_id_input', 
                             placeholder='Customer ID', 
                             options=[{'label': idx, 'value':idx} for idx in df.customer_id.to_list()])

cust_id_div = html.Div([dbc.Label("Customer ID Query"), cust_id_input], className='my-2')

#cltv score
cltv_card = dbc.Card([dbc.CardHeader('Customer CLTV'),
                      dbc.CardBody([
                          html.H4('',id='cltv')]
                      )], className="my-2")
 
#churn risk
churn_risk_card = dbc.Card([dbc.CardHeader('Churn Risk'),
                            dbc.CardBody([
                                html.H4('',id='churn_score')]
                      )], className="my-2")


#quadrant 
quad_card = dbc.Card(dbc.CardBody([
                          html.H4("Customer Quadrant", className="mx-1"),
                          dcc.Graph(
                              id='quadrant_chart'
                          )]),className='mt-4')

#table
table_header = [
    html.Thead(html.Tr([html.Th("Customer Engagement"), html.Th("Information")]))
]

row1 = html.Tr([html.Td("Tenure Months"), html.Td("24")])
row2 = html.Tr([html.Td("Internet Service"), html.Td("Fiber Optic")])
row3 = html.Tr([html.Td("Payment Method"), html.Td("Electronic Check")])
row4 = html.Tr([html.Td("Contract"), html.Td("Month-to-Month")])
row5 = html.Tr([html.Td("Streaming Subscription"), html.Td("TV, Movies")])
row6 = html.Tr([html.Td("Other Support"), html.Td("Online Backup, Online Support")])
row7 = html.Tr([html.Td("Cluster"), html.Td("Heavyweight")])

table_body = [html.Tbody([row1, row2, row3, row4, row5, row6, row7])]
table = dbc.Table(table_header + table_body, 
                  bordered=True,
                  hover=True,
                  responsive=True,
                  striped=True)


third_div = html.Div(
    [
        dbc.Row([dbc.Col(table, width=12)])    
    ]
)

second_div = html.Div(
    [
        dbc.Row([dbc.Col(au_card, width=3), 
                 dbc.Col(revenue_card, width=3), 
                 dbc.Col(cltv_card, width=3),
                 dbc.Col(churn_risk_card, width=3)]),
        dbc.Row([dbc.Col(quad_card)])
    ], className='mr-5 my-4'
)

first_div = html.Div(
    [
        dbc.Row([dbc.Col(cust_id_div)]),
        dbc.Row([dbc.Col(third_div, width=12)])
    ], className='mx-5 my-4'
)
app.layout = html.Div(
    [
        navbar,
        dbc.Row([dbc.Col(first_div, width=4), dbc.Col(second_div, width=8)]),
    ]
)

@app.callback(
    Output(component_id='quadrant_chart', component_property='figure'),
    Input(component_id='cust_id_input', component_property='value')
)
def update_graph(customer_id):
    color_discrete_map = {'vanilla':'blue','heavyweight':'green','price_sensitive':'red','minimalist':'orange'}
    #quad figure if customer id selected
    if customer_id:
        fig = px.scatter(df[df.customer_id == customer_id], x="cltv", y="churn_score", color="cluster",
                         color_discrete_map=color_discrete_map)
    else:
        fig = px.scatter()
    fig.add_annotation(x=5400, y=80, text='<b>RETAIN</b>', showarrow=False)
    fig.add_annotation(x=5400, y=40, text='<b>MAINTAIN</b>', showarrow=False)
    fig.add_annotation(x=3000, y=80, text='<b>DIVEST</b>', showarrow=False)
    fig.add_annotation(x=3000, y=40, text='<b>GROW</b>', showarrow=False)
    fig.update_layout(margin={'b':10, 't':20, 'pad':4}, showlegend=False,
                      xaxis_range=[1800, 6600], yaxis_range=[10,110],
                      shapes=[{'type':'line', 'yref':'paper', 'xref':'x', 
                               'y0':0, 'y1':1, 'x0':4200, 'x1':4200},
                              {'type':'line', 'yref':'y', 'xref':'paper', 
                               'y0':60, 'y1':60, 'x0':0, 'x1':1}])
    fig.update_xaxes({'title':'CLTV'})
    fig.update_yaxes({'title':'Churn Risk'})
    return fig

@app.callback(
    [Output(component_id='status', component_property='children'),
     Output(component_id='revenue', component_property='children'),
     Output(component_id='cltv', component_property='children'),
     Output(component_id='churn_score', component_property='children'),
    ],
    Input(component_id='cust_id_input', component_property='value')
)
def update_status(customer_id):
    if customer_id:
        columns = ['customer_status', 'total_revenue', 'cltv', 'churn_score']
        result = df.loc[df.customer_id==customer_id, columns]
        result['customer_status'] = result['customer_status'].apply(lambda x: 'Active' if x==0 else 'Churned')
        result['total_revenue'] = result['total_revenue'].apply('$ {:.2f}'.format)
        result['churn_score'] = result['churn_score'].astype(str) + ' %'
        return list(result.values[0])
    else:
        return ['-'] * 4


if __name__ == '__main__':
    app.run_server(debug=True)