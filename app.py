from flask import Flask, render_template, session, request, make_response


app = Flask(__name__)

app.secret_key = b'1234'



@app.route('/')

def counter():

    visit_counter = 0
    if session.get('visited'):
        visit_counter = session['visited']
    else:
        session['visited'] = 0

    if session.get('username'):
        username = session['username']
    else:
        username = 'unregister'

    response = make_response(render_template('index.html', visited=visit_counter, username=username))
    session['visited'] += 1

    return response

@app.route('/login', methods=['GET', 'POST'])


def add_user():

    response = make_response(render_template('login.html'))
    if session.get('username'):
        username = session['username']
        return f"{username} user"
    else:
        if request.method == 'GET"':
            return response
        elif request.method == 'POST':
            session['username'] = request.form["username"]
            username = session['username']
            return f"You have written your username: <b>{username}</b> and sent it by POST request"
    return  response



@app.route('/logout')

def clear():
    session.clear()
    return f"Session had been clear"





"""
EFE
EFEF
"""
if __name__ == '__main__':
    app.run(debug=True, port=5002)