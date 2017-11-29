from flask import render_template, flash, redirect, session
from app import app
from .forms import LoginForm, ThreeGamesForm
from .cf import loadMockData #, mainCF
from .dataformatter import tupleToDict

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    threeGamesForm = ThreeGamesForm()
    if loginForm.validate_on_submit():
        session['session_steamid'] = loginForm.steamid.data
        #flash('Login requested for SteamID="%s"' % loginForm.steamid.data)
        session['game1'] = "DARK SOULS III"
        session['game2'] = "Mount & Blade: Warband"
        session['game3'] = "Sid Meier's Civilization V"
        return redirect('/feed')
    if threeGamesForm.validate_on_submit():
        session['session_steamid'] = threeGamesForm.username.data
        session['game1'] = threeGamesForm.game1.data
        session['game2'] = threeGamesForm.game2.data
        session['game3'] = threeGamesForm.game3.data
        return redirect('/feed')      
        
    return render_template('login.html', 
                           #title='Sign In',
                           loginForm=loginForm,
                           threeGamesForm = threeGamesForm)

@app.route('/feed')
def feed():
    steamid = session.get('session_steamid', None)
    #user = {'nickname': 'Miguel'}  # fake user
    games = loadMockData(steamid)
    #games = mainCF(151603712)[:10]
    #games = tupleToDict(games)

    game1 = session.get('game1', None)
    game2 = session.get('game2', None)
    game3 = session.get('game3', None)
    playedGames = [game1, game2, game3]    
            
    return render_template("feed.html",
                           steamid=steamid,
                           games=games,
                           playedGames = playedGames)

