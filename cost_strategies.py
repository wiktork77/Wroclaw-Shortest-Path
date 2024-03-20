
def compute_change(current_line, execution):
    pass


def compute_time(current_time, execution):
    execution_cost = execution.arrival_time - execution.departure_time
    additional_cost = execution.departure_time - current_time
    return (execution_cost.seconds + additional_cost.seconds) / 60


def compute_p_cost(current_time, execution, current_line, h_value=None):
    execution_cost = execution.arrival_time - execution.departure_time
    additional_cost = execution.departure_time - current_time
    line_change_cost = 0 if execution.line == current_line else 20
    # 20 because executions between particular nodes take less (minutes) so that way algorithm prefers executions
    # that use same line until its not possible, increasing decreases likelihood of changing line, making heuristic
    # less valuable, hence increasing computation time, making this number too low makes euclidean heuristic more
    # valuable, so it increases likelihood of changing the line if its profitable (position wise) so it needs to be
    # very carefully chosen, perhaps this number should be a function of heuristic value ?
    return line_change_cost + (execution_cost.seconds + additional_cost.seconds) / 60


def get_computation(criteria):
    if criteria == 't':
        return compute_time

