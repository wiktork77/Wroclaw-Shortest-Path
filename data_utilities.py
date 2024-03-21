import os
import pandas as pd
from datetime import datetime
from IPython.display import display

infinity = float('inf')


def get_data_source_path(file_name):
    current_dir = os.getcwd()
    paths_dir = os.path.join(current_dir, "data_sources")
    data_file = os.path.join(paths_dir, file_name)
    return data_file


def retrieve_data(file_name):
    data_file = get_data_source_path(file_name)
    df = pd.read_csv(data_file, low_memory=False, usecols=[i + 1 for i in range(10)])
    return df


def display_data(df):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    display(df)


def get_raw_row(series):
    raw_row = ""
    for key in series.keys():
        raw_row += f"{str(series[key])},"
    return raw_row[:-1]


def express_time_as_seconds(time_obj):
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second


def parse_time_to_datetime(time):
    split = time.split(":")
    day, hour, minute, second = 1, int(split[0]), int(split[1]), int(split[2])
    if hour >= 24:
        hour -= 24
        day += 1
    dtime = datetime(2023, 3, day, hour, minute, second)
    return dtime


def find_best_future_execution_time(current_time, executions):
    lowest_cost = infinity
    best = None
    for execution in executions:
        if execution.departure_time >= current_time:
            cost = execution.departure_time - current_time + (execution.arrival_time - execution.departure_time)
            cost_int = int(cost.seconds)
            if cost_int < lowest_cost:
                lowest_cost = cost_int
                best = execution
    return best


def find_best_future_execution_change(current_time, executions, current_line):
    if current_line is None:
        return find_best_future_execution_time(current_time, executions)

    best_executions = [execution for execution in executions if execution.departure_time >= current_time and execution.line == current_line]
    if not best_executions:
        best_alternative = min([execution for execution in executions if execution.departure_time >= current_time], key=lambda x: x.departure_time - current_time, default=None)
        return best_alternative
    else:
        return min(best_executions, key=lambda x: x.departure_time - current_time)


def find_best_execution(current_time, executions, criteria, current_line=None):
    if criteria == 't':
        return find_best_future_execution_time(current_time, executions)
    elif criteria == 'p':
        return find_best_future_execution_change(current_time, executions, current_line)


def reconstruct_path(previous, source, destination):
    current = destination
    path = [previous[current]]

    while True:
        current = previous[current][0]
        if current == source:
            break
        path.append(previous[current])

    path.reverse()
    return path


def compute_execution_duration(execution):
    result = execution.arrival_time - execution.departure_time
    result = int(result.seconds / 60)
    return result


def count_line_changes(path):
    changes = 0
    last_line = path[0][2].line
    for n in path:
        if n[2].line != last_line:
            changes += 1
            last_line = n[2].line
    return changes




