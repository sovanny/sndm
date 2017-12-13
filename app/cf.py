from app import app
import numpy as np 
import pandas as pd 
from nltk import FreqDist
from pandas import Series, DataFrame
import networkx as nx
from .igdb_functions import getGameInfo



df = pd.read_csv('./app/static/data/steam-200k.csv')

#select played games
edgelist = [[Userid,gameTitle,10*(1+playTime**(-2))**(-4.0)] for Userid,gameTitle,p,playTime,e in df.values if p =="play"]

gamerList = []
gameList = []
for i in edgelist:
    gamerList.append(i[0])
    gameList.append(i[1])
AllgameList = set(gameList)
gamerList = set(gamerList)
#print '# of gamer in csv is ', len(gamerList)
#print '# of game in csv is ',len(AllgameList)

G = nx.Graph()
G.add_weighted_edges_from(edgelist)
df = nx.to_pandas_dataframe(G)
GG_matrix = DataFrame(df, columns = AllgameList, index = gamerList)


def mainCF(steamid): 
    similaruser = find_10similarUsers(steamid)
    return expectedScoreToGame(similaruser)
    
def expectedScoreToGame(similarUsers):
    a = []
    for i,j in similarUsers.items():
        b = {}
        for k,l in dict(GG_matrix.ix[i]).items():
            if l*j != 0:
                b[k] = l*j
        a.append(b)
        
    from collections import Counter
    expectedScore = Counter()
    for i in a:
        x = Counter(i)
        expectedScore.update(x)
    expectedScoreForSorting = dict(expectedScore).items()  
    expectedScoreForSorting.sort( key=lambda x: x[1] , reverse=True )

    return expectedScoreForSorting
        
def find_10similarUsers(a):
    Usersim = {}
    for i in gamerList:
        usercosim = cos_sim(list(GG_matrix.ix[a]),list(GG_matrix.ix[i]))
        if usercosim != 0 and i!=a :
            Usersim[i] = usercosim
    
    Usersimd = Usersim.items()
    Usersimd.sort( key=lambda x: x[1] , reverse=True )
    find_10similarUsers = {}
    for i in range(0,20):
        find_10similarUsers[Usersimd[i][0]] = Usersimd[i][1]  
    return find_10similarUsers 
          
def cos_sim(a, b):
    from numpy import dot
    from numpy.linalg import norm
    cos_sim = dot(a, b)/(norm(a)*norm(b))
    return cos_sim


