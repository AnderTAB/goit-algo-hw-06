from random import uniform
import pprint

graph = {
'Акад': ['Житом'],
'Житом': ['Акад', 'Свят'],
'Свят': ['Житом', 'Нивки'],
'Нивки': ['Свят', 'Берес'],
'Берес': ['Нивки', 'Шуляв'],
'Шуляв': ['Берес', 'Політ'],
'Політ': ['Шуляв', 'Вокза'],
'Вокза': ['Політ', 'Уніве'],
'Уніве': ['Вокза', 'Театр'],
'Театр': ['Уніве', 'Хрещ', 'Золот'],
'Хрещ': ['Театр', 'Арсен', 'Майдан']
}

def random_time_station(graph_stations):
    graph_ws_rand_time = dict()
    for k, v in graph_stations.items():
        d = dict()
        for statin in v:
            d.update({statin : round(uniform(0, 4), 1)})
        graph_ws_rand_time.update({k : d})
    return graph_ws_rand_time
    
           
        
# for r_stat_time in random_time_station(graph):
pprint.pprint(random_time_station(graph))  
