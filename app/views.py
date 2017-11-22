from flask import render_template, flash, redirect, session
from app import app
from .forms import LoginForm

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
    games = loadMockData(steamid)
    return render_template("feed.html",
                           steamid=steamid,
                           games=games)

def loadMockData(steamid):
    mockdata = [ 
        {
            'gameTitle': 'The Elder Scrolls V Skyrim',
            'similarityScore': 53.502989714865578,
            'metascore': '97'
        },
        {
            'gameTitle': 'Fallout New Vegas',
            'similarityScore':  36.277176853396433,
            'metascore': '97'
        },
        {
            'gameTitle': 'Left 4 Dead 2',
            'similarityScore': 32.757423768662711,
            'metascore': 'N/A'
        },
        {
            'gameTitle': 'Team Fortress 2',
            'similarityScore': 29.213237962323173,
            'metascore': '97'
        },
        {
            'gameTitle': 'Fallout 4',
            'similarityScore': 16.145297797440694,
            'metascore': '97'
        },
        {
            'gameTitle': 'Spore',
            'similarityScore': 7.9382914544637844,
            'metascore': 'N/A'
        },
        {
            'gameTitle': 'POSTAL 2',
            'similarityScore': 7.1796941580365861,
            'metascore': '97'
        },
        {
            'gameTitle': 'Borderlands 2',
            'similarityScore': 6.8079846548986964,
            'metascore': '97'
        },
        {
            'gameTitle': 'Wargame European Escalation',
            'similarityScore': 4.7935830585677648,
            'metascore': '97'
        },
        {
            'gameTitle': 'Tomb Raider',
            'similarityScore': 4.437999873445559,
            'metascore': '97'
        }
    ]
    return mockdata


