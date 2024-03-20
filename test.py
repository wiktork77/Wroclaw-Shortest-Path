from data_utilities import retrieve_data
from data_modelling import model_graph, Stop
from dijkstra import dsp
from astar_v1 import astar
from astar_v2 import astar2
from data_presentation import present_graph, present_path
from dijkstra import reconstruct_path
from metrics.time_metrics import measure_computation_time
from heuristics import euclidean_distance, manhattan_distance, chebyshev_distance


df = retrieve_data("connection_graph_unique.csv")
graph = model_graph(df)


test_entries = [
    ("Babimojska", "Biegasa", "16:58:00"),
    ("SPISKA (Ośrodek sportu)", "Wallenroda", "14:45:00"),
    ("Kadłub NŻ", "Rogowska (P+R)", "24:44:00"),
    ("most Grunwaldzki", "Krasińskiego", "10:16:00"),
    ("Bajana", "Smolec - Wrocławska", "21:03:00"),
    ("Krępicka", "Kadłub wieś", "29:58:00"),
    ("KOSZAROWA (Szpital)", "Brzezia Łąka - cmentarz", "11:38:00"),
    ("RĘDZIŃSKA", "TARNOGAJ", "25:38:00"),
    ("Muchobór Wielki", "Wysoka - Lipowa", "27:14:00"),
    ("Zabrodzie - pętla", "Wiślańska", "19:52:00"),
    ("Maślicka (Osiedle)", "Iwiny - Kolejowa", "16:07:00"),
    ("Małkowice - Główna", "Kiełczów - Zgodna", "10:39:00")
]

for entry in test_entries:
    measure_computation_time("astar2", astar2, graph, entry[0], entry[1], entry[2], euclidean_distance)





