from app import app

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

        
