from app import app
from .igdb_functions import getGameInfo
def loadMockData(steamid):
    mockdata = []

    game = getGameInfo('POSTAL 2')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 100,
        'igdbUrl': game['url']
    })

    game = getGameInfo('Borderlands 2')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore':  95,
        'igdbUrl': game['url']
    })

    game = getGameInfo('Wargame European Escalation')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 67,
        'igdbUrl': game['url']
    })

    game = getGameInfo('The Forest')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 62,
        'igdbUrl': game['url']
    })

    game = getGameInfo('Hatoful Boyfriend')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 60,
        'igdbUrl': game['url']
    })

    game = getGameInfo('Bastion')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 57,
        'igdbUrl': game['url']
    })
    
    game = getGameInfo("Sid Meier's Civilization V")
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 53,
        'igdbUrl': game['url']
    })

    game = getGameInfo('Counter-Strike Condition Zero')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 53,
        'igdbUrl': game['url']
    })

    game = getGameInfo('Dead Island')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 52,
        'igdbUrl': game['url']
    })

    game = getGameInfo('Counter-Strike Global Offensive')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 51,
        'igdbUrl': game['url']
    })
    
    return mockdata

def loadMockData2(games):
    mockdata = []

    game = getGameInfo('Bulletstorm')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 98,
        'igdbUrl': game['url']
    })

    game = getGameInfo('DC Universe Online')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 90,
        'igdbUrl': game['url']
    })

    game = getGameInfo('Aliens vs. Predator')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 67,
        'igdbUrl': game['url']
    })

    game = getGameInfo('Monopoly')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 65,
        'igdbUrl': game['url']
    })

    game = getGameInfo('Mortal Kombat X')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 147,
        'igdbUrl': game['url']
    })

    game = getGameInfo('Far Cry 2')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 61,
        'igdbUrl': game['url']
    })

    game = getGameInfo('Dying Light')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 57,
        'igdbUrl': game['url']
    })

    game = getGameInfo('Strider')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 56,
        'igdbUrl': game['url']
    })
    game = getGameInfo('The Flame in the Flood')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 55,
        'igdbUrl': game['url']
    })
    game = getGameInfo('Scribblenauts Unlimited')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 51,
        'igdbUrl': game['url']
    })

    return mockdata
