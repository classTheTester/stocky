from flask import Flask, render_template, request, jsonify, send_from_directory
from backend.main import summarizeNews
from backend.tester import getnews
app = Flask(__name__)



@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'endpoints' : [
        '/api/news',
        '/api/price'
        ]
        })       


@app.route('/api/news', methods=['GET'])
def summarizetext():
    #index = request.args.get('index')
    return getnews()




if __name__ == '__main__':
    print(f"Access the app at: http://localhost:8000")
    app.run(host='0.0.0.0', port=8000, debug=True)