import pytest

from main import BooksCollector


@pytest.fixture
def books():
    return BooksCollector()

