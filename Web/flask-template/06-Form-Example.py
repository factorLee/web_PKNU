from flask import Flask, render_template, request
app  = Flask(__name__)

@app.route('/')
def index():
    return render_template('06-index.html')

@app.route('/signup_form')
def signup_form():
    return render_template('06-Sign-up.html')

@app.route('/thankyou')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('06-thankyou.html', first = first, last = last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('06-404.html')


if __name__ == '__main__':
    app.run()