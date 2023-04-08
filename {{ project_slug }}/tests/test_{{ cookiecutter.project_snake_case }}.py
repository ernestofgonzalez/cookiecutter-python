from {{ cookiecutter.project_snake_case }} import roads


def test_roads():
    assert roads() == "Roads?"