from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/<container>')
def about(container):
    return render_template('about.html',somevar=container)


@app.route('/contact/<container>')
def contact(container):
    return container

if __name__ == '__main__':
    app.run(debug=True)