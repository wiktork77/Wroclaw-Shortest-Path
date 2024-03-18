from data_modelling import model_data
from data_utilities import retrieve_data
from metrics.time_metrics import measure_computation_time


df = retrieve_data("connection_graph_unique.csv")
model_data(df)



