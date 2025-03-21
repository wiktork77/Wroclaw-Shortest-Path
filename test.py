from data_utilities import retrieve_data, count_line_changes
from data_modelling import model_graph, Stop
from dijkstra import dsp
from astar import astar
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
    ("KOSZAROWA (Szpital)", "Brzezia Łąka - cmentarz", "11:38:00") , #p-
    ("RĘDZIŃSKA", "TARNOGAJ", "25:38:00"),
    ("Muchobór Wielki", "Wysoka - Lipowa", "27:14:00"),
    ("Zabrodzie - pętla", "Wiślańska", "19:52:00"), #p~
    ("Maślicka (Osiedle)", "Iwiny - Kolejowa", "16:07:00"), #p+
    ("Małkowice - Główna", "Kiełczów - Zgodna", "10:39:00")  #p~
]






