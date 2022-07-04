from src.counter import count_ocurrences


def test_counter():
    counter_lower_case = count_ocurrences('src/jobs.csv', 'Python')
    counter_upper_case = count_ocurrences('src/jobs.csv', 'PYTHON')

    assert counter_lower_case == counter_upper_case == 1639
