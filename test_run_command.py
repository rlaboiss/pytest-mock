from unittest.mock import Mock, patch
from run_command import RunCommand


def test_success():
    rc = RunCommand('ls -l /etc/ssh')
    ret = rc.do()
    assert ret == 0


def test_failure():
    rc = RunCommand('ls -l /etc/foo')
    ret = rc.do()
    assert ret == 0


@patch('run_command.Popen')
def test_patch(popen_mock: Mock):
    popen_mock.return_value.__enter__.return_value.returncode = 0
    rc = RunCommand('ls -l /etc/foo')
    ret = rc.do()
    assert ret == 0
