from data_utilities import retrieve_data
from data_modelling import model_graph, Stop
from dijkstra import dsp
import codecs

df = retrieve_data("connection_graph_unique.csv")
graph = model_graph(df)

# dsp(graph, "Babimojska", "Biegasa", "16:58:00")
# dsp(graph, "SPISKA (Ośrodek sportu)", "Wallenroda", "14:45:00")
# dsp(graph, "Kadłub NŻ", "Rogowska (P+R)", "24:44:00")
# dsp(graph, "most Grunwaldzki", "Krasińskiego", "10:16:00")
# dsp(graph, "Bajana", "Smolec - Wrocławska", "21:03:00")
# dsp(graph, "Krępicka", "Kadłub wieś", "29:58:00")
# dsp(graph, "KOSZAROWA (Szpital)", "Brzezia Łąka - cmentarz", "11:38:00")
# dsp(graph, "RĘDZIŃSKA", "TARNOGAJ", "25:38:00")
# dsp(graph, "Muchobór Wielki", "Wysoka - Lipowa", "27:14:00")
# dsp(graph, "Zabrodzie - pętla", "Wiślańska", "19:52:00")
# dsp(graph, "Maślicka (Osiedle)", "Iwiny - Kolejowa", "16:07:00")
# dsp(graph, "Małkowice - Główna", "Kiełczów - Zgodna", "10:39:00")


