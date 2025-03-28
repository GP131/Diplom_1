import pytest

from praktikum.database import Database


@pytest.fixture
def database_instance():
    """Создание экземпляра Database перед каждым тестом"""
    db = Database()
    yield db
    # no teardown necessary
