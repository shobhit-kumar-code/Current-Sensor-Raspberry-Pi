from flask import Flask, render_template
import boto3
import plotly.graph_objs as go
import json
import plotly
app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table=dynamodb.Table('globalproject')

@app.route('/')
def getTableVals():
    response = table.scan()
    
#     gj={
#   'x': [1, 2, 3, 4],
#   'y': [10, 15, 13, 17],
#   type: 'scatter',
# }
    gj=1
    x1=[]
    x2=[]
    for x in response['Items']:
        print(float(x['current']),float(x['timestamp']))
        x1.append(float(x['current']))
        x2.append(float(x['timestamp']))
    trace1 = go.Scatter(
        x=x2,
        y=x1,
        mode='markers',
        name='Data',
        marker=dict(
            size=12
        )
    )
    data=[trace1]
    gj = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    print(gj)
    
    
    return render_template('hello.html',currenttable=response['Items'],graphJSON=gj)
    




@app.route('/h')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()