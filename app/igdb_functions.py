from igdb_api_python.igdb import igdb as igdb

#api key
igdb = igdb("e70abc7e20ad6ff740a2a9d67ffab3ad")

def getGameInfo(gameTitle):

    gameInfo = {}

    result = igdb.games({
        'search': gameTitle,
        'fields' : ['name', 'summary', 'total_rating', 'cover', 'url'] 
    })
    gameInfo['title'] = result.body[0]['name']
    gameInfo['url'] =  result.body[0]['url']

    if 'summary' in result.body[0]:
        gameInfo['summary'] = result.body[0]['summary'][:320]
    else: 
        gameInfo['summary'] = "No summary available."

    if 'total_rating' in result.body[0]:
        gameInfo['rating'] = round(result.body[0]['total_rating'])
    else:
        gameInfo['rating'] = "N/A"
    

    if 'cover' in result.body[0]:
        gameInfo['cover'] = "//images.igdb.com/igdb/image/upload/t_cover_big/" + result.body[0]['cover']['cloudinary_id'] + ".png"
    else:
        gameInfo['cover'] = "static/img/noCoverArt.gif"

    return gameInfo