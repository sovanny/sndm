from flask import render_template, flash, redirect, session
from app import app
from .forms import LoginForm
from .cf import loadMockData, mainCF
from .dataformatter import tupleToDict

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['session_steamid'] = form.steamid.data
        flash('Login requested for SteamID="%s"' % form.steamid.data)
        return redirect('/feed')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)

@app.route('/feed')
def feed():
    steamid = session.get('session_steamid', None)
    #user = {'nickname': 'Miguel'}  # fake user
    #games = loadMockData(steamid)
    games = mainCF(151603712)[:10]
    games = tupleToDict(games)
    return render_template("feed.html",
                           steamid=steamid,
                           games=games)

