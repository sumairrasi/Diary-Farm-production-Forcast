from flask import Flask, render_template, request,jsonify
import os
import numpy as np
import pandas as pd
from mlproject.pipeline.forcasting import ForcastingPipeline
import plotly.graph_objs as go
import plotly.io as pio
import json
import plotly

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Fixed start date
start_date = '1975-12-01'

@app.route('/forecast', methods=['POST'])
def forecast():
    end_date = request.form['end_date']
    
    try:
        # predictions = sarimax_model.get_prediction(start=start_date, end=end_date)
        forcast = ForcastingPipeline()
        predictions = forcast.forcasting(start_date,end_date)
        prediction_summary = predictions.summary_frame()
        # prediction_json = prediction_summary.to_json(orient="split")


        fig = go.Figure()
        fig.add_trace(go.Scatter(x=prediction_summary.index, y=prediction_summary['mean'], 
                                 mode='lines', name='Prediction'))
        fig.add_trace(go.Scatter(x=prediction_summary.index, y=prediction_summary['mean_ci_lower'], 
                                 mode='lines', name='Lower CI', line=dict(dash='dash')))
        fig.add_trace(go.Scatter(x=prediction_summary.index, y=prediction_summary['mean_ci_upper'], 
                                 mode='lines', name='Upper CI', line=dict(dash='dash')))
        
        graph_json = pio.to_json(fig)
        
        return jsonify(graph_json)
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)