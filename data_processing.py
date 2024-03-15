from data_utilities import retrieve_data
from data_modelling import model_data_iterrows, model_data_itertuples
import time


def measure_iterating_methods():
    start = time.time()
    df = retrieve_data("connection_graph_unique.csv")
    end = time.time()
    result = end - start
    print(f"Retrieve time: {result}")

    start = time.time()
    model_data_itertuples(df)
    end = time.time()
    result = end - start
    print(f"Iterate time: {result}")

