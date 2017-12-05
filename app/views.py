from flask import render_template, flash, redirect, session
from app import app
from .forms import LoginForm, ThreeGamesForm
from .cf import loadMockData, loadMockData2 #, mainCF
from .dataformatter import tupleToDict

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    threeGamesForm = ThreeGamesForm()
    if loginForm.validate_on_submit():
        session['session_steamid'] = loginForm.steamid.data
        #flash('Login requested for SteamID="%s"' % loginForm.steamid.data)
        # these games should be fetched from steam api
        session['game1'] = "The Elder Scrolls V Skyrim"
        session['game2'] = "Fallout 4"
        session['game3'] = "Spore"
        session['loginType'] = 1
        return redirect('/feed')
    if threeGamesForm.validate_on_submit():
        session['session_steamid'] = threeGamesForm.username.data
        session['game1'] = threeGamesForm.game1.data
        session['game2'] = threeGamesForm.game2.data
        session['game3'] = threeGamesForm.game3.data
        session['loginType'] = 2       
        return redirect('/feed')      
        
    return render_template('login.html', 
                           loginForm=loginForm,
                           threeGamesForm = threeGamesForm)

@app.route('/feed')
def feed():
    steamid = session.get('session_steamid', None)

    if session.get('loginType', None) == 1:
        #games = mainCF(151603712)[:10]
        #games = tupleToDict(games)
        # should not be loadMockData in real app
        games = loadMockData(steamid)
        game1 = session.get('game1', None)
        game2 = session.get('game2', None)
        game3 = session.get('game3', None)
        playedGames = [game1, game2, game3]    
        profilePic = 'ron-winkle.jpg'
        steamid = 'Ron Winkle'
    elif session.get('loginType', None) == 2:
        game1 = session.get('game1', None)
        game2 = session.get('game2', None)
        game3 = session.get('game3', None)
        playedGames = [game1, game2, game3]    
        # should not be loadMockData in real app
        games = loadMockData2(playedGames)
        profilePic = 'wonder-woman.png'

            
    return render_template("feed.html",
                           steamid=steamid,
                           games=games,
                           playedGames = playedGames,
                           profilePic = profilePic)

