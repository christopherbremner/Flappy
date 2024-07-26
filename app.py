from flask import Flask, jsonify
import flappybirdclone  # Replace with the name of your Python script

app = Flask(__name__)

@app.route('/run-code', methods=['GET'])
def run_code():
    result = flappybirdclone.main()  # Replace with your function
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)