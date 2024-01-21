from flask import Flask, render_template, request, jsonify
from calc import calculate_variable

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        Q = float(request.form['Q'])
        V = float(request.form['V'])
        C = float(request.form['C'])
        result = calculate_variable(Q=Q, V=V, C=C)
        return jsonify(result=result)
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
