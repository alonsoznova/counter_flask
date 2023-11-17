from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def counter():
    if 'visit_count' in session:
        session['visit_count'] += 1
    else:
        session['visit_count'] = 1

    return render_template("index.html", visit_count=session['visit_count'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
