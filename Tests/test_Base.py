import pytest


@pytest.mark.usefixtures("init_driver")
@pytest.mark.usefixtures("input_data_for_add_user")
class BaseTest:
    pass
