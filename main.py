from data_modelling import model_graph
from data_utilities import retrieve_data
from metrics.time_metrics import measure_computation_time


df = retrieve_data("connection_graph_unique.csv")
measure_computation_time("Creating graph", model_graph, df)

