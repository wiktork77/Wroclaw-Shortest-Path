from data_modelling import model_graph
from data_utilities import retrieve_data, parse_time_to_datetime
from metrics.time_metrics import measure_computation_time
from dijkstra import dsp
from bisect import bisect_right

# df = retrieve_data("connection_graph_unique.csv")
# graph = measure_computation_time("Creating graph", model_graph, df)


a = parse_time_to_datetime("11:15:00")
b = parse_time_to_datetime("11:22:00")



