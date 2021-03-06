import pytest  # type: ignore[import]
import testlib


# TODO Orig conftest file (Python 2)
# If new fixtures are implemented, don't forget to port them to
#   tests-py3/unit/inventory/conftest.py


@pytest.fixture(scope="module")
def inventory_plugin_manager():
    return testlib.InventoryPluginManager()


@pytest.fixture(scope="module")
def check_manager():
    return testlib.CheckManager()
