import matplotlib.pyplot as plt
infinity = float('inf')


def present_graph(graph):
    vertices = graph.get_vertices()
    x, y = [], []
    for v in vertices:
        x.append(v.longitude)
        y.append(v.latitude)
    plt.scatter(x, y, s=5)


def present_path_verbose(path):
    pad_length = 45
    print("Linia".ljust(pad_length) + "Start".ljust(pad_length) + "Czas wejscia".ljust(pad_length) + "Stop".ljust(pad_length) + "Czas wyjscia".ljust(pad_length))
    print("="*5*pad_length)
    for item in path:
        stop, connection, execution = item[0], item[1], item[2]
        print(
            f"{execution.line}".ljust(pad_length) +
            f"{connection.start_stop.name}".ljust(pad_length) +
            f"{execution.departure_time}".ljust(pad_length) +
            f"{connection.end_stop.name}".ljust(pad_length) +
            f"{execution.arrival_time}".ljust(pad_length)
        )


def segment_path(path):
    if len(path) == 0:
        return []

    segmented_path = []
    segmented_connection = path[0][1]
    segmented_execution = path[0][2]
    stops_between = []

    for item in path[1:]:
        if item[2].line == segmented_execution.line:
            stops_between.append((item[1].start_stop.name, item[2].departure_time))
            segmented_connection.end_stop = item[1].end_stop
            segmented_execution.arrival_time = item[2].arrival_time
        else:
            segmented_path.append((segmented_connection.start_stop, segmented_connection, segmented_execution, stops_between))
            segmented_connection = item[1]
            segmented_execution = item[2]
            stops_between = []

    segmented_path.append((segmented_connection.start_stop, segmented_connection, segmented_execution, stops_between))

    return segmented_path


def datetime_to_day_time(datetime):
    hour = str(datetime.hour)
    if len(hour) < 2:
        hour = f'0{hour}'

    minute = str(datetime.minute)
    if len(minute) < 2:
        minute = f'0{minute}'

    second = str(datetime.second)
    if len(second) < 2:
        second = f'0{second}'

    return f'{hour}:{minute}:{second}'


def print_path_concise(path):
    for item in path:
        start, end = item[1].start_stop.name, item[1].end_stop.name
        dep_time, arr_time = datetime_to_day_time(item[2].departure_time), datetime_to_day_time(item[2].arrival_time)
        line = item[2].line
        stops = 0
        if len(item) > 3:
            stops = item[3]
        print(f'{start} -> {end} | {dep_time} -> {arr_time} | {line}, {stops}')
