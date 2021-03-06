import pytest  # type: ignore[import]

pytestmark = pytest.mark.checks


@pytest.mark.parametrize('params,expected_args', [
    ({
        "username": "user",
        "password": "password",
    }, ["-u", "user", "-p", "password", "address"]),
])
def test_hp_msa_argument_parsing(check_manager, params, expected_args):
    """Tests if all required arguments are present."""
    agent = check_manager.get_special_agent('agent_hp_msa')
    arguments = agent.argument_func(params, "host", "address")
    assert arguments == expected_args
