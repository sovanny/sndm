from flask import render_template, flash, redirect, session
from app import app
from .forms import LoginForm, ThreeGamesForm
from .cf import main_CF, gamerList2
from .mockData import loadMockData, loadMockData2
from .pagerank import main_PR_category, main_PR, gameListFiltered
from .dataformatter import tupleToDict, getGameInfoList

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    threeGamesForm = ThreeGamesForm()
    if loginForm.validate_on_submit():
        session['session_steamid'] = loginForm.steamid.data
        #flash('Login requested for SteamID="%s"' % loginForm.steamid.data)
        # these games should be fetched from steam api
        #session['game1'] = "The Elder Scrolls V Skyrim"
        #session['game2'] = "Fallout 4"
        #session['game3'] = "Spore"
        #session['loginType'] = 1
        return redirect('/feed')
    if threeGamesForm.validate_on_submit():
        session['session_steamid'] = threeGamesForm.username.data
        session['game1'] = threeGamesForm.game1.data
        session['game2'] = threeGamesForm.game2.data
        session['game3'] = threeGamesForm.game3.data
        session['loginType'] = 2       
        return redirect('/feed')      

    gamerList = gamerList2
    
        
    return render_template('login.html', 
                            gamerList = gamerList,
                            gameListFiltered = gameListFiltered,
                            loginForm=loginForm,
                            threeGamesForm = threeGamesForm)

@app.route('/feed')
def feed():
    

    if session.get('loginType', None) == 1:
        steamid = long(session.get('session_steamid', None))
        resultingGames = main_CF(steamid)
        games = getGameInfoList(resultingGames)
        #games = tupleToDict(games)
        # should not be loadMockData in real app
        #games = loadMockData(steamid)
        game1 = session.get('game1', None)
        game2 = session.get('game2', None)
        game3 = session.get('game3', None)
        playedGames = [game1, game2, game3]    
        #profilePic = 'ron-winkle.jpg'
        #steamid = 'Ron Winkle'
    elif session.get('loginType', None) == 2:
        steamid = session.get('session_steamid', None)
        game1 = session.get('game1', None)
        game2 = session.get('game2', None)
        game3 = session.get('game3', None)
        playedGames = [game1, game2, game3]    
        # should not be loadMockData in real app
        #games = loadMockData2(playedGames)
        #resultingGames = main_PR_category(game1, game2, game3)
        resultingGames = main_PR(game1, game2, game3)        
        games = getGameInfoList(resultingGames)
        

    profilePic = 'wonder-woman.png'   

            
    return render_template("feed.html",
                           steamid=steamid,
                           games=games,
                           playedGames = playedGames,
                           profilePic = profilePic)

