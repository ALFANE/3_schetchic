from flask import Flask, render_template, session, request, make_response



app = Flask(__name__)

@app.route('/')

def test():
    test = dir(session)
    return render_template('test.html', test=test)

app.run(debug=True)