from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Hello, world! </h1> <br/><h3> Selamat datang di halaman pertama Flask!</h3>"

if __name__ == '__main__':
    app.run(debug=True)