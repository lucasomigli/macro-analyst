from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/main')
def main():
    return render_template('main.html', hello=dict(
        a=1,
        b=2,
        c=3
    ))


if __name__ == "__main__":
    app.run(debug=True)
