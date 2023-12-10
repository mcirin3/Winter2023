from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_POLYGON_API_KEY' with your actual Polygon.io API key
POLYGON_API_KEY = 'WDc3YFVhkBMDetvC0CpRgtZpeofkMgGX'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    if request.method == 'POST':
        symbol = request.form['symbol']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        # Make a request to Polygon.io API for historical daily stock data
        url = f'https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/{start_date}/{end_date}?apiKey={POLYGON_API_KEY}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            stock_data = data['results']

            # Process the stock data as needed
            # ...

            # Return the stock data to the client (assuming JSON format for simplicity)
            return jsonify({'success': True, 'stock_data': stock_data})
        else:
            return jsonify({'success': False, 'message': 'Failed to fetch stock data'})

if __name__ == '__main__':
    app.run(debug=True)
