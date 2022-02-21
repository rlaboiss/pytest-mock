from unittest.mock import Mock, patch

from run_command import RunCommand


### This unit test exercises the full functionality of the RunCommand class
### (the command "ls -l /etc/ssh" is effectively run in the system). It must
### succeed.
def test_success():
    rc = RunCommand("ls -l /etc/ssh")
    ret = rc.run()
    assert ret == 0


### This unit test must fail, unless there is a file or directory names
### /etc/foo in the system, what is very unlikely.
def test_failure():
    rc = RunCommand("ls -l /etc/foo")
    ret = rc.run()
    assert ret == 0


### This unit test must succeed, even though, like in the unit test
### test_failure above, it would try to list a non existing file in the
### system (/etc/foo). This is done by mocking the Popen class used in file
### run_command.py (through mock.patch) and by mocking the return value of
### the Popen method (through the __enter__ method of the context manager
### created by the "with Popen()" call).
@patch("run_command.Popen")
def test_patch(popen_mock: Mock):
    popen_mock.return_value.__enter__.return_value.returncode = 0
    rc = RunCommand("ls -l /etc/foo")
    ret = rc.run()
    assert ret == 0
