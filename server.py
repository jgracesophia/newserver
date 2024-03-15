from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    numbers = data['numbers']
    total = sum(numbers)
    return jsonify({'sum': total})

if __name__ == '__main__':
    app.run(debug=True)
