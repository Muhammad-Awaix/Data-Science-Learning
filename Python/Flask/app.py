from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/success/<score>')
def success(score):
    return f"Your score is {score}"

@app.route('/')
def welcome():
    return "Welcome to this Flask Course"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method=="POST":
        name=request.form['name']
        return f"Hello {name} Welcome to the Course:)"
    return render_template('form.html')

if __name__ == "__main__":
    app.run()