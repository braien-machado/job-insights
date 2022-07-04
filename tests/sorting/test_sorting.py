from src.sorting import sort_by

JOB_ONE = {
    "job_title": "job_one",
    "min_salary": 1000,
    "max_salary": 2000,
    "date_posted": "2022-01-14",
}

JOB_TWO = {
    "job_title": "job_two",
    "min_salary": 750,
    "max_salary": 1500,
    "date_posted": "2010-01-12",
}

JOB_THREE = {
    "job_title": "job_three",
    "min_salary": 1500,
    "max_salary": 5000,
    "date_posted": "2022-01-13",
}

JOB_FOUR = {
    "job_title": "job_four",
    "max_salary": 2200,
    "date_posted": "2010-01-10",
}

JOB_FIVE = {
    "job_title": "job_five",
    "min_salary": 1300,
    "date_posted": "2022-01-18",
}

JOB_SIX = {
    "job_title": "job_six",
    "min_salary": 1800,
    "max_salary": 4000,
}


JOBS = [JOB_ONE, JOB_TWO, JOB_THREE, JOB_FOUR, JOB_FIVE, JOB_SIX]

SORTED_BY_MIN_SALARY = [
    JOB_TWO,
    JOB_ONE,
    JOB_FIVE,
    JOB_THREE,
    JOB_SIX,
    JOB_FOUR,
]

SORTED_BY_MAX_SALARY = [
    JOB_THREE,
    JOB_SIX,
    JOB_FOUR,
    JOB_ONE,
    JOB_TWO,
    JOB_FIVE,
]

SORTED_BY_DATE_POSTED = [
    JOB_FIVE,
    JOB_ONE,
    JOB_THREE,
    JOB_TWO,
    JOB_FOUR,
    JOB_SIX,
]


def test_sort_by_criteria():
    sort_by(JOBS, "min_salary")

    for number in range(len(JOBS)):
        assert (
            JOBS[number]["job_title"]
            == SORTED_BY_MIN_SALARY[number]["job_title"]
        )

    sort_by(JOBS, "max_salary")

    for number in range(len(JOBS)):
        assert (
            JOBS[number]["job_title"]
            == SORTED_BY_MAX_SALARY[number]["job_title"]
        )

    sort_by(JOBS, "date_posted")

    for number in range(len(JOBS)):
        assert (
            JOBS[number]["job_title"]
            == SORTED_BY_DATE_POSTED[number]["job_title"]
        )
