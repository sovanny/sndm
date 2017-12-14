import sys
import copy
import networkx as nx
from operator import itemgetter
import pandas as pd 

df = pd.read_csv('./app/static/data/game_category.csv')
df2 = pd.read_csv('./app/static/data/game_keyword.csv')

edgelist1 = [[games1,categories] for games1,categories in df.values]
edgelist2 = [[games2,keywords] for games2,keywords in df2.values]

gameList = []



categoryList = []
keywordList = []
for i in edgelist1:
    gameList.append(i[0])
    categoryList.append(i[1])
for i in edgelist2:
    gameList.append(i[0])
    keywordList.append(i[1])
AllgameList = set(gameList)
AllcategoryList = set(categoryList)
AllkeywordList = set(keywordList)
#print ('# of game in csv is ', len(AllgameList))
#print ('# of category in csv is ',len(AllcategoryList))
#print ('# of keyword in csv is ',len(AllkeywordList))


# Because the number of games is too large for selectize... quick fix: get every 500th game
gameListFiltered = gameList[::100]


df3 = pd.read_csv('./app/static/data/steam-200k.csv')
#select played games
edgelist3 = [[Userid,gameTitle,10*(1+playTime**(-2))**(-4.0)] for Userid,gameTitle,p,playTime,e in df3.values]

gameList2 = []
for i in edgelist3:
    gameList2.append(i[1])
AllgameList2 = set(gameList2)

#print '# of game in csv is ',len(AllgameList2)
len(AllgameList & AllgameList2)
games = AllgameList & AllgameList2

def main_PR_category(game1,game2,game3):
    result = []
    G2 = nx.read_gexf("./app/static/data/pagerank2.gexf")
    games_dict = dict.fromkeys(G2.nodes(), 1)


    node_dict = copy.deepcopy(games_dict)
    node_dict[game1] = sys.maxsize
    node_dict[game2] = sys.maxsize
    node_dict[game3] = sys.maxsize
    dp = nx.pagerank(G2, personalization=node_dict)
    print(game1 + ", "+game2+ ", "+game3)
    sorted_node = sorted(dp.items(), key=itemgetter(1), reverse=True)
    recommend = [k for k, v in sorted_node if k in games]
    try: 
        recommend.remove(game1)        
    except ValueError:
        pass
    try: 
        recommend.remove(game2)        
    except ValueError:
        pass
    try: 
        recommend.remove(game3)        
    except ValueError:
        pass
    for p in recommend[0:10] :
        #print(p + ", score : " + str(round(pow(10,6)*dp[p])))
        result.append([p, pow(10,6)*dp[p]])
    maxvalue =  max(result,key=lambda item:item[1])[1]
    for i in range(10):
        result[i][1] = round((result[i][1] / maxvalue)*100)
    print("main_PR_category done")
    return result

#print main_PR_category("Zelda Breath of the Wild Explorer's Edition", "Halo: Combat Evolved","Guild Wars" )

def main_PR(game1,game2,game3):
    result = []
    G = nx.read_gexf("./app/static/data/pagerank.gexf")
    games_dict = dict.fromkeys(G.nodes(), 1)

    node_dict = copy.deepcopy(games_dict)
    node_dict[game1] = sys.maxsize
    node_dict[game2] = sys.maxsize
    node_dict[game3] = sys.maxsize
    dp = nx.pagerank(G, personalization=node_dict)
    print(game1 + ", "+game2+ ", "+game3)
    sorted_node = sorted(dp.items(), key=itemgetter(1), reverse=True)
    recommend = [k for k, v in sorted_node if k in games]
    try: 
        recommend.remove(game1)        
    except ValueError:
        pass
    try: 
        recommend.remove(game2)        
    except ValueError:
        pass
    try: 
        recommend.remove(game3)        
    except ValueError:
        pass
    for p in recommend[0:10] :
        #print(p + ", score : " + str(round(pow(10,6)*dp[p])))
        result.append([p, round(pow(10,6)*dp[p])])
    maxvalue =  max(result,key=lambda item:item[1])[1]
    for i in range(10):
        result[i][1] = round((result[i][1] / maxvalue)*100)
    print("main_PR done")
    return result


#print main_PR("Zelda Breath of the Wild Explorer's Edition", "Halo: Combat Evolved","Guild Wars" )
