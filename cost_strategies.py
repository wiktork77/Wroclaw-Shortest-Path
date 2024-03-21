
def compute_change(current_line, execution):
    pass


def compute_time(current_time, execution):
    execution_cost = execution.arrival_time - execution.departure_time
    additional_cost = execution.departure_time - current_time
    return (execution_cost.seconds + additional_cost.seconds) / 60


def compute_p_cost(current_time, execution, current_line, h_value=None):
    execution_cost = execution.arrival_time - execution.departure_time
    additional_cost = execution.departure_time - current_time
    line_change_cost = 0 if execution.line == current_line else 26*h_value
    # 26 ponieważ statystycznie polepsza to wyniki w wymiarze czasu i jakosci, czyli minimalnej
    # liczby przesiadek (wykresy)
    return line_change_cost + (execution_cost.seconds + additional_cost.seconds) / 60


def compute_cost(criteria, current_time, execution, current_line=None, h_value=None):
    if criteria == 't':
        return compute_time(current_time, execution)
    elif criteria == 'p':
        return compute_p_cost(current_time, execution, current_line, h_value)

