import codecs
from data_utilities import retrieve_data, get_data_source_path, get_raw_row


def create_unique_connections(file_name):
    unique_raw_csv_rows = set()
    df_main = retrieve_data("connection_graph.csv")
    for i, row in df_main.iterrows():
        csv_row = get_raw_row(row)
        unique_raw_csv_rows.add(csv_row)

    with codecs.open(get_data_source_path(file_name), "w", "utf-8") as f:
        f.write("nr,company,line,departure_time,arrival_time,start_stop,end_stop,start_stop_lat,start_stop_lon,end_stop_lat,end_stop_lon\n")
        i = 0
        for row in unique_raw_csv_rows:
            f.write(f"{i},"+ row + "\n")
            i += 1


create_unique_connections("connection_graph_unique.csv")

