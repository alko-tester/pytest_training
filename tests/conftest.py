import pytest


@pytest.fixture()
def clean_text_file():
    with open("tests/testfile.txt", "w"):
        pass
