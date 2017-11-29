from app import app
import numpy as np 
import pandas as pd 
from nltk import FreqDist
from pandas import Series, DataFrame
import networkx as nx
from .igdb_functions import getGameInfo

def loadMockData(steamid):
    mockdata = []

    game = getGameInfo('The Elder Scrolls V Skyrim')
    
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 54
    })

    game = getGameInfo('Fallout New Vegas')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore':  36
    })

    game = getGameInfo('Left 4 Dead 2')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 33
    })

    game = getGameInfo('Team Fortress 2')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 29
    })

    game = getGameInfo('Fallout 4')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 16
    })

    game = getGameInfo('Spore')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 8
    })
    
    game = getGameInfo('POSTAL 2')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 7
    })

    game = getGameInfo('Borderlands 2')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 7
    })

    game = getGameInfo('Wargame European Escalation')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 5
    })

    game = getGameInfo('Tomb Raider')
    mockdata.append({
        'gameTitle': game['title'],        
        'summary': game['summary'],
        'rating': game['rating'],
        'cover': game['cover'],
        'similarityScore': 4
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


