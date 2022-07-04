from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    list = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for job in list:
        for header, data in list[0].items():
            assert header in ["title", "salary", "type"]
