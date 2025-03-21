import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def interpret_heuristics_comparison():
    df_euclidean = pd.read_csv("./statistics_results/astar_heuristic_comparison/euclidean.csv")
    df_manhattan = pd.read_csv("./statistics_results/astar_heuristic_comparison/manhattan.csv")
    df_chebyshev = pd.read_csv("./statistics_results/astar_heuristic_comparison/chebyshev.csv")

    data = [df_euclidean, df_manhattan, df_chebyshev]

    p_len_mean = []
    cost_mean = []
    comp_time_mean = []

    for df in data:
        p_len_mean.append(df.loc[:, 'p_len'].mean())
        cost_mean.append(df.loc[:, 'cost'].mean())
        comp_time_mean.append(df.loc[:, 'comp_time'].mean())

    x = np.array(["Euclidean", "Manhattan", "Chebyshev"])
    # y = np.array(p_len_mean)
    # plt.title("Średnia długość ścieżki")
    # plt.bar(x, y)
    # plt.savefig("./plots/heuristic_comparison/mean_path_len.png")
    # y = np.array(cost_mean)
    # plt.title("Średni koszt ścieżki")
    # plt.bar(x, y)
    # plt.savefig("./plots/heuristic_comparison/mean_path_cost.png")
    y = np.array(comp_time_mean)
    plt.title("Średni czas wykonania")
    plt.bar(x, y)
    plt.savefig("./plots/heuristic_comparison/mean_computation_timee.png")


def interpret_dijkstra_vs_astar():
    df_astar = pd.read_csv("./statistics_results/dijkstra_vs_astar/astar.csv")
    df_dijkstra = pd.read_csv("./statistics_results/dijkstra_vs_astar/dijkstra.csv")
    data = [df_astar, df_dijkstra]
    p_len_mean = []
    cost_mean = []
    comp_time_mean = []

    for df in data:
        p_len_mean.append(df.loc[:, 'p_len'].mean())
        cost_mean.append(df.loc[:, 'cost'].mean())
        comp_time_mean.append(df.loc[:, 'comp_time'].mean())

    x = np.array(["A*", "Dijkstra"])
    # y = np.array(p_len_mean)
    # plt.title("Średnia długość ścieżki")
    # plt.bar(x, y)
    # plt.savefig("./plots/dijkstra_vs_astar/mean_path_len.png")
    # y = np.array(cost_mean)
    # plt.title("Średni koszt ścieżki")
    # plt.bar(x, y)
    # plt.savefig("./plots/dijkstra_vs_astar/mean_path_cost.png")
    y = np.array(comp_time_mean)
    plt.title("Średni czas wykonania")
    plt.bar(x, y)
    plt.savefig("./plots/dijkstra_vs_astar/mean_computation_timee.png")



def interpret_ch_cost():
    x = []
    time = []
    diff = []
    df_scalar = pd.read_csv("./statistics_results/astar_ch_cost/scalar.csv")
    df_heuristic = pd.read_csv("./statistics_results/astar_ch_cost/heuristic.csv")
    val_group = df_scalar.groupby('ch_val').mean()
    for item in val_group.itertuples():
        x.append(item.Index)
        time.append(item.time)
        diff.append(item.diff)

    plt.plot(x, time, label='time_scalar')
    plt.plot(x, diff, label='diff_scalar')
    plt.xticks(range(0, 50, 4))
    time_h = []
    diff_h = []
    val_group = df_heuristic.groupby('ch_val').mean()
    for item in val_group.itertuples():
        time_h.append(item.time)
        diff_h.append(item.diff)

    plt.plot(x, time_h, label='time_heuristic')
    plt.plot(x, diff_h, label='diff_heuristic')
    plt.legend()
    plt.savefig("./plots/change_cost/both_plot.png")
    plt.clf()
    plt.xticks(range(0, 50, 4))
    plt.plot(x, time, label='time_scalar')
    plt.plot(x, time_h, label='time_heuristic')
    plt.legend()
    plt.savefig("./plots/change_cost/both_time_plot.png")


interpret_heuristics_comparison()

