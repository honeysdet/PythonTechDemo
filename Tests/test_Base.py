import pytest

"""this is the base test class for all tests"""
@pytest.mark.usefixtures("init_driver")
@pytest.mark.usefixtures("input_data_for_add_user")
class BaseTest:
    pass
