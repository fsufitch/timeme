def check_time_within(time_expected, time_actual, threshold):
    time_diff = abs(time_actual-time_expected)
    assert time_diff < threshold
