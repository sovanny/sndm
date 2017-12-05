from app import app
import numpy as np 
import pandas as pd 
from nltk import FreqDist
from pandas import Series, DataFrame
import networkx as nx
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



# df = pd.read_csv('./app/static/data/steam-200k.csv')

# #select played games
# edgelist = [[Userid,gameTitle,10*(1+playTime**(-2))**(-4.0)] for Userid,gameTitle,p,playTime,e in df.values if p =="play"]

# gamerList = []
# gameList = []
# for i in edgelist:
#     gamerList.append(i[0])
#     gameList.append(i[1])
# AllgameList = set(gameList)
# gamerList = set(gamerList)
# #print '# of gamer in csv is ', len(gamerList)
# #print '# of game in csv is ',len(AllgameList)

# G = nx.Graph()
# G.add_weighted_edges_from(edgelist)
# df = nx.to_pandas_dataframe(G)
# GG_matrix = DataFrame(df, columns = AllgameList, index = gamerList)


# def mainCF(steamid): 
#     similaruser = find_10similarUsers(steamid)
#     return expectedScoreToGame(similaruser)
    
# def expectedScoreToGame(similarUsers):
#     a = []
#     for i,j in similarUsers.items():
#         b = {}
#         for k,l in dict(GG_matrix.ix[i]).items():
#             if l*j != 0:
#                 b[k] = l*j
#         a.append(b)
        
#     from collections import Counter
#     expectedScore = Counter()
#     for i in a:
#         x = Counter(i)
#         expectedScore.update(x)
#     expectedScoreForSorting = dict(expectedScore).items()  
#     expectedScoreForSorting.sort( key=lambda x: x[1] , reverse=True )

#     return expectedScoreForSorting
        
# def find_10similarUsers(a):
#     Usersim = {}
#     for i in gamerList:
#         usercosim = cos_sim(list(GG_matrix.ix[a]),list(GG_matrix.ix[i]))
#         if usercosim != 0 and i!=a :
#             Usersim[i] = usercosim
    
#     Usersimd = Usersim.items()
#     Usersimd.sort( key=lambda x: x[1] , reverse=True )
#     find_10similarUsers = {}
#     for i in range(0,20):
#         find_10similarUsers[Usersimd[i][0]] = Usersimd[i][1]  
#     return find_10similarUsers 
          
# def cos_sim(a, b):
#     from numpy import dot
#     from numpy.linalg import norm
#     cos_sim = dot(a, b)/(norm(a)*norm(b))
#     return cos_sim


