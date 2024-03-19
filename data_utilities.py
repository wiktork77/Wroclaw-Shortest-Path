import bisect
import os
import numpy as np
import pandas as pd
from datetime import datetime
from IPython.display import display

infinity = float('inf')

# class CustomTime:
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     def __eq__(self, other):
#         return (self.hour, self.minute, self.second) == (other.hour, other.minute, other.second)
#
#     def __lt__(self, other):
#         self_seconds = express_time_as_seconds(self)
#         other_seconds = express_time_as_seconds(other)
#         return self_seconds < other_seconds
#
#     def __gt__(self, other):
#         self_seconds = express_time_as_seconds(self)
#         other_seconds = express_time_as_seconds(other)
#         return self_seconds > other_seconds
#
#     def __repr__(self):
#         return f"{self.hour}:{self.minute}:{self.second}"
#
#     def __add__(self, other):
#         hour = self.hour + other.hour
#         minute = self.minute + other.minute
#         second = self.second + other.second
#         if second >= 60:
#             second -= 60
#             minute += 1
#         if minute >= 60:
#             minute -= 60
#             hour += 1
#         return CustomTime(hour, minute, second)


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


# def parse_time_to_custom_time(time):
#     split = time.split(":")
#     custom_time = CustomTime(int(split[0]), int(split[1]), int(split[2]))
#     return custom_time


def parse_time_to_datetime(time):
    split = time.split(":")
    day, hour, minute, second = 1, int(split[0]), int(split[1]), int(split[2])
    if hour >= 24:
        hour -= 24
        day += 1
    dtime = datetime(2023, 3, day, hour, minute, second)
    return dtime


def find_best_future_execution(current_time, executions, last_line=None):
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


