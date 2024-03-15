from data_utilities import retrieve_data, get_raw_row


def find_duplicates_in_data(df):
    uniques = set()
    uniques_index_dict = {}
    duplicates_count = {}

    for i, row in df.iterrows():
        raw = get_raw_row(row)
        if raw not in uniques:
            uniques.add(raw)
            uniques_index_dict[raw] = i
        else:
            index = uniques_index_dict[raw]
            if index not in duplicates_count:
                duplicates_count[index] = 1
            else:
                duplicates_count[index] += 1
    return duplicates_count


def count_all_duplicates(dupes):
    count = 0
    for entry in dupes:
        count += 1
        count += dupes[entry] - 1
    return count


def exploration_summary():
    df = retrieve_data("connection_graph.csv")
    row_count = len(df)
    duplicates = find_duplicates_in_data(df)
    dup_count = count_all_duplicates(duplicates)
    unique_count = row_count - dup_count
    min_dupes = min(duplicates.values())
    max_dupes = max(duplicates.values())
    print(f"Liczba wszystkich wierszy: {row_count}")
    print(f"Liczba duplikatów: {count_all_duplicates(duplicates)}")
    print(f"Liczba unikalnych wierszy: {unique_count}")
    print(f"Maksymalna liczba powtórzeń: {max_dupes}")
    print(f"Minimalna liczba powtórzeń: {min_dupes}")


exploration_summary()



