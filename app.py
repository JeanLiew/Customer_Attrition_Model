import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import base64

external_stylesheets = [dbc.themes.GRID, dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = 'Customer Attrition Dashboard - Jean Liew'
df = pd.read_csv('file/telco_clustered_dash.csv')
df.sort_values('customer_id', inplace=True)

#title
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

#nav icons
email = dbc.NavLink(dbc.CardImg(src="/assets/icons/email.svg",
                                style={'height':'50px'}),href="mailto:huijin.liew@gmail.com")
linkedin = dbc.NavLink(dbc.CardImg(src="/assets/icons/linkedin.svg",
                                   style={'height':'50px'}),href="https://www.linkedin.com/in/liewhuijin/", target='_blank')
git = dbc.NavLink(dbc.CardImg(src="/assets/icons/github.svg", 
                              style={'height':'50px'}),href="https://github.com/JeanLiew", target='_blank')
resume =  dbc.NavLink(dbc.CardImg(src="/assets/icons/resume.svg", 
                              style={'height':'50px'}),href="https://drive.google.com/file/d/17lCZRr30bzwfMv5BAjqOPYZUH2O8EBiv/view?usp=sharing", target='_blank')
#navbar
navbar = dbc.Navbar(
    dbc.Row(
        [
        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px", 
                         style={'border':'2px solid #384053', 'align':'center'}, className='ml-5'), width=1),
        dbc.Col(dbc.NavbarBrand("Customer Attrition Dashboard"), width=8),
        dbc.Col(dbc.Nav([email, linkedin, git, resume]), style={'text-align':'right'}, width=3),
        ], style={'width':'100%'}, align='center'), light=True, sticky='top')

#users image
image_card = html.Div([html.Img(src="/assets/user_image_default.jpg", 
                                   style={"width": "15rem", "margin":'auto','border-style':'outset','border-radius':'50%'},
                                   className='my-5', id='image_card')], style={'border':'hidden'}, id='user-image')

#active status
au_card = dbc.Button("Status", outline=True, color="#fe9d24", active=True, id='status', 
                      style={'text-align':'center',  "margin":'auto', 'width': '10rem'})

#revenue per quarter
revenue_card = dbc.Card(dbc.CardBody(html.H6('Total Revenue',id='revenue')), className="my-2", 
                     style={"width": "100%", 'padding':'10px', 'text-align': 'left','border':'hidden'})

#cluster card
cluster_card = dbc.Card([html.H2('', id='cluster', className='mt-2 ml-2'),
                         dbc.CardBody(html.H6('',id='cluster_description'))], 
                        className="my-2", 
                        style={"width": "100%", 'padding':'10px', 'text-align': 'left','border':'hidden', 'height': '195px', 'color': '#fffafa'},id='clus-card')


#input cust ID
cust_id_input = dcc.Dropdown(id='cust_id_input', 
                             placeholder='Customer ID Query', 
                             options=[{'label': idx, 'value':idx} for idx in df.customer_id.to_list()],
                            style={'sticky':'top', 'color': '#aaa'})


#cltv score 
cltv_card = dbc.Card([html.H4('Customer Lifetime Value (CLTV)'),
                     dbc.CardBody(
                          [html.Span('',id='cltv'), html.Span('', id='revenue')], id='cltv-container'
                      )], className="my-2", 
                     style={"width": "100%", 'padding':'10px', 'text-align': 'left','border':'hidden'})
    
#month to churn
mon_to_churn = html.Div(dbc.Progress([dbc.Progress(value=100, color="success", bar=True, id='progress'),
                                         dbc.Progress(value=0, color="danger", bar=True, id='countdown')], multi=True))

churn_card = dbc.Card([html.H6('Months to Churn', id='months_to_churn'),
                       dbc.CardBody(mon_to_churn)
                      ], 
                      style={"width": "100%", 'text-align': 'left','border':'hidden', 'background': 'none'})
    
#churn risk
churn_risk_card = dbc.Card([html.H2('', id='churn_score', className='mt-2 ml-2'),
                            dbc.CardBody(churn_card)],
                           className="my-2", 
                           style={"width": "100%", 'padding':'8px', 'text-align': 'left','border':'hidden'},
                           id='churn-card')


#quadrant 
quad_card = dbc.Card(dbc.CardBody([
                          html.H4("Customer Quadrant"),
                          dcc.Graph(
                              id='quadrant_chart',style={'height': '60vh'})]),
                     style={'border':'hidden'})

#table
info_div = html.Div(
    [
        #sex
        dbc.Row(
            [dbc.Col(dbc.CardImg(src="/assets/icons/sex.svg"), width=3),
             dbc.Col([dbc.Row('Gender', className='property-name',),
                      dbc.Row('', id='gender', className='property-value')
                     ]
                    ,width=9)
            ], className='property-row'
        ),
        #age 
        dbc.Row(
            [dbc.Col(dbc.CardImg(src="/assets/icons/age-group.svg"), width=3),
             dbc.Col([dbc.Row('Age',className='property-name'),
                      dbc.Row('', id='age',className='property-value')
                     ]
                     ,width=9)
            ], className='property-row'
        ),
        #marriage
        dbc.Row(
            [dbc.Col(dbc.CardImg(src="/assets/icons/wedding-rings.svg"), width=3),
             dbc.Col([dbc.Row('Marriage Status',className='property-name'),
                      dbc.Row('', id='marriage',className='property-value')
                     ]
                     ,width=9)
            ], className='property-row'
        ),
        #city
        dbc.Row(
            [dbc.Col(dbc.CardImg(src="/assets/icons/skyline.svg"), width=3),
             dbc.Col([dbc.Row('City',className='property-name'),
                      dbc.Row('', id='city',className='property-value')
                     ]
                     ,width=9)
            ], className='property-row'
        ),
        #offer
        dbc.Row(
            [dbc.Col(dbc.CardImg(src="/assets/icons/offer.svg"), width=3),
             dbc.Col([dbc.Row('Offer',className='property-name'),
                      dbc.Row('', id='offer',className='property-value')
                     ]
                     ,width=9)
            ], className='property-row'
        ),
        #contract
        dbc.Row(
            [dbc.Col(dbc.CardImg(src="/assets/icons/contract.svg"), width=3),
             dbc.Col([dbc.Row('Contract',className='property-name'),
                      dbc.Row('', id='contract',className='property-value')
                     ]
                     ,width=9)
            ], className='property-row'
        ),
        #internet
        dbc.Row(
            [dbc.Col(dbc.CardImg(src="/assets/icons/internet.svg"), width=3),
             dbc.Col([dbc.Row('Internet Services',className='property-name'),
                      dbc.Row('', id='internet',className='property-value')
                     ]
                     ,width=9)
            ], className='property-row'
        ),
        #payment
        dbc.Row(
            [dbc.Col(dbc.CardImg(src="/assets/icons/credit-card.svg"), width=3),
             dbc.Col([dbc.Row('Payment Method',className='property-name'),
                      dbc.Row('', id='payment',className='property-value')
                     ]
                     ,width=9)
            ], className='property-row'
        ),
    ]
)


footer = html.Footer('Dashboard by Jean Liew, 2021', style={'font-size':'0.8em'}, id='footer-style')

right_div = html.Div(
    [
        dbc.Row([dbc.Col(cltv_card, width=12)]),
        dbc.Row([dbc.Col(cluster_card, width=6), 
                 dbc.Col(churn_risk_card, width=6)]),
        dbc.Row([dbc.Col(quad_card)])
    ]
)

left_div = html.Div(
    [
        dbc.Row([dbc.Col(cust_id_input)]),
        dbc.Row([dbc.Col(image_card)]),
        dbc.Row([dbc.Col(au_card)], justify="center"),
        dbc.Row([dbc.Col(info_div, width=12, className='mt-5')])
    ]
)


app.layout = html.Div(
    [
        navbar,
        dbc.Row([dbc.Col(left_div, width=3, id='sidebar'), dbc.Col(right_div, width=9, style={'padding':'30px'})], style={'margin':'0px'}),
        footer
    ]
)

#callback quadrant
@app.callback(
    Output(component_id='quadrant_chart', component_property='figure'),
    Input(component_id='cust_id_input', component_property='value')
)
def update_graph(customer_id):
#     quad figure if customer id selected
    if customer_id:
        fig = px.scatter(df[df.customer_id == customer_id], x="cltv", y="churn_score")
        fig.update_traces(marker_symbol='x', marker_size=15, marker=dict(color='#fe9d24',line=dict(color='#fe9d24')))
    else:
        fig = px.scatter()
    fig.add_annotation(x=5500, y=85, text='<b>RETAIN</b>', showarrow=False)
    fig.add_annotation(x=5500, y=35, text='<b>MAINTAIN</b>', showarrow=False)
    fig.add_annotation(x=3000, y=85, text='<b>DIVEST</b>', showarrow=False)
    fig.add_annotation(x=3000, y=35, text='<b>GROW</b>', showarrow=False)
    fig.update_layout(margin={'b':10, 't':20, 'r':15, 'pad':4}, showlegend=False,
                      xaxis_range=[1800, 6800], yaxis_range=[10,110],
                      shapes=[{'type':'line', 'yref':'paper', 'xref':'x', 
                               'y0':0, 'y1':1, 'x0':4200, 'x1':4200},
                              {'type':'line', 'yref':'y', 'xref':'paper', 
                               'y0':60, 'y1':60, 'x0':0, 'x1':1}])
    fig.update_xaxes({'title':'CLTV'})
    fig.update_yaxes({'title':'Churn Risk'})
    return fig

#callback score
@app.callback(
     [Output(component_id='cltv', component_property='children'),
      Output(component_id='cluster', component_property='children'),
      Output(component_id='churn_score', component_property='children'),
      Output(component_id='months_to_churn', component_property='children'),
      Output(component_id='revenue', component_property='children')
    ],
    Input(component_id='cust_id_input', component_property='value')
)
def update_score(customer_id):
    if customer_id:
        columns = ['cltv', 'cluster','churn_score','months_to_churn','total_revenue']
        result = df.loc[df.customer_id==customer_id, columns]
        result['churn_score'] = result['churn_score'].apply('Churn Risk: {} %'.format)
        result['total_revenue'] = result['total_revenue'].apply('Total Revenue: $ {:.2f}'.format)
        result['months_to_churn'] = result['months_to_churn'].astype(int).apply('Months to Churn: {}'.format)
        
        return list(result.values[0]) 
    else:
        return ['CLTV','Customer Segmentation','Churn Risk (%)','Months to Churn', 'Total Revenue per Quarter']
    
#callback progress
@app.callback(
     [Output(component_id='progress', component_property='value'),
      Output(component_id='progress', component_property='color'),
      Output(component_id='countdown', component_property='value'),
      Output(component_id='countdown', component_property='color'),
      Output(component_id='image_card', component_property='src')
    ],
    Input(component_id='cust_id_input', component_property='value')
)
def update_progress(customer_id):
    if customer_id:
        n = df.loc[df.customer_id==customer_id, 'months_to_churn']
        n = n.values[0]
        countdown = n/80 * 100
        prog = 100 - countdown
        if 0 < n <= 18: # 18 months
            return [prog, 'success', countdown, 'danger', '/assets/user_image_shock.jpg']
        elif 12 < n <= 48: #12-48 months
            return [prog, 'success', countdown, 'warning', '/assets/user_image_ok.jpg']
        elif n > 48: #more 80months
            return [prog, 'success', countdown, 'success', '/assets/user_image_happy.jpg']  
        else:  #0 month
            return [prog, 'danger', countdown, 'danger', '/assets/user_image_cry.jpg']
    else:
        return [100,'#fe9d24', 0, 'white', '/assets/user_image_default.jpg'] 
        
    
#callback button
@app.callback([Output(component_id='status', component_property='children'),
               Output(component_id='status', component_property='color'),
              ],
              Input(component_id='cust_id_input', component_property='value')
)
def update_button(customer_id):
    if customer_id:
        result = df[df.customer_id==customer_id].customer_status
        result = result.values[0] # 1 or 0
        if result == 0:
            return ['Active','success']
        else:
            return ['Churned', 'danger']
    else:
        return ['Status', 'warning']

#callback table
@app.callback(
    [Output(component_id='gender', component_property='children'),
     Output(component_id='age', component_property='children'),
     Output(component_id='marriage', component_property='children'),
     Output(component_id='city', component_property='children'),
     Output(component_id='offer', component_property='children'),
     Output(component_id='contract', component_property='children'),
     Output(component_id='internet', component_property='children'),
     Output(component_id='payment', component_property='children'),
    ],
    Input(component_id='cust_id_input', component_property='value')
)

def update_table(customer_id):
    if customer_id:
        columns = ['gender','age','married','city', 'offer','contract','internet_service','payment_method']
        result = df.loc[df.customer_id==customer_id, columns]
        result['married'] = result['married'].apply(lambda x: 'Married' if x == 1 else 'Single')
        return list(result.values[0])
    else:
        return [' '] * 8

#callback clus description
@app.callback(
    Output(component_id='cluster_description', component_property='children'),
    Input(component_id='cluster', component_property='children')
)
def update_clus_description(cluster):
    if cluster != 'Customer Segmentation':
        description_dict = {
            'Vanilla':'Basic users that are tech savvy users with high data consumption and keen on online security. They only subsribed to selective services.',
            'Heavyweight':'They are users with high revenue with high CLTV profiles. Users are loyalist with long tenure months. They are engaged with most of our products.',
            'Minimalist': 'Low commitment users with no strings attached. They are users with the lowest revenue profile yet the easiest to satisfy. They are keen on bare minimum subsription.',
            'Price Sensitive' : 'They are users with lowest CLTV profile. Users are keen but not confident enough to extend for longer tenure months. These users are price-conscious.',
        }
        return description_dict.get(cluster)
    else:
        return 'Select a Customer ID to review cluster description.'


    
if __name__ == '__main__':
    app.run_server(debug=True)
    
