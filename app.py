from flask import Flask, render_template, request, jsonify, send_from_directory
from backend.main import summarizeNews

app = Flask(__name__)



@app.route('/')
def root():
    return render_template("index.html")          


@app.route('/api/news', methods=['GET'])
def summarizetext():
    #index = request.args.get('index')
    return summarizeNews()




if __name__ == '__main__':
    print(f"Access the app at: http://localhost:8000")
    app.run(host='0.0.0.0', port=8000, debug=True)