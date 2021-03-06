from . import jobs


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    list = jobs.read(path)
    job_types = []
    for job in list:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """

    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    list = jobs.read(path)
    industries = []
    for job in list:
        if len(job["industry"]) > 0 and job["industry"] not in industries:
            industries.append(job["industry"])

    return industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """

    list = [job for job in jobs if job["industry"] == industry]

    return list


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    list = jobs.read(path)
    max_salaries = []
    for job in list:
        if len(job["max_salary"]) > 0 and job["max_salary"] != "invalid":
            max_salaries.append(int(job["max_salary"]))

    return max(max_salaries)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    list = jobs.read(path)
    min_salaries = []
    for job in list:
        if len(job["min_salary"]) > 0 and job["min_salary"] != "invalid":
            min_salaries.append(int(job["min_salary"]))

    return min(min_salaries)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    if type(salary) != int:
        raise ValueError("salary must be a number")
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min_salary or max_salary is not in dict")
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("min_salary and max_salary must be numbers")
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("min_salary must be smaller than max_salary")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list.append(job)
        except ValueError:
            pass

    return list
