from .users_repository import UserRepository




def test_insert_user():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 33

    users_repository = UserRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)
