#pylint: disable = use-implicit-booleaness-not-comparison
from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_finder import UserFinder

def test_find():
    first_name = 'name'
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

    assert repo.select_user_attributes['first_name'] == first_name

    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []

def test_find_error_in_valid_name():
    first_name = 'name123'
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Invalid format for first name"

def test_find_error_user_not_found():
    class UserRepositoryError(UsersRepositorySpy):
        def select_user(self, first_name: str):
            return []

    first_name = 'name'
    repo = UserRepositoryError()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "User not found"
