from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello():

    return 'hellow'

@app.route('/api/getSampleJson/<value>')
def sample(value):

    return jsonify({'return': value})

app.run(debug=True)