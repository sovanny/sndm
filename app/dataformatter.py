from app import app
from .igdb_functions import getGameInfo

def tupleToDict(listOfTuples):
    games =[]
    for game in listOfTuples:
        games.append(
            {
                'gameTitle': game[0],
                'similarityScore': game[1],
                'metascore': '97'
            }
        )
    return games

def getGameInfoList(listOfTuples):
    games = []
    for gameTuple in listOfTuples:
        game = getGameInfo(gameTuple[0])
        games.append({
            'gameTitle': game['title'],        
            'summary': game['summary'],
            'rating': game['rating'],
            'cover': game['cover'],
            'similarityScore': gameTuple[1],
            'igdbUrl': game['url']
        })
    return games

        
