from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])

@app.route('/rsa', methods=['POST'])
def rsa():
    pass


if __name__ == '__main__':
    app.run(debug=True)