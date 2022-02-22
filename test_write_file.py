from unittest.mock import Mock, patch

from write_file import WriteFile


### This unit test exercises the full functionality of the WriteFile class
### (the file /tmp/foo is effectively written in the file system). It must
### succeed.
def test_success():
    s = "message"
    wf = WriteFile("/tmp/foo")
    ret = wf.write(s)
    assert ret == len(s)


### This unit test must fail, unless it is run with root permissions.
### Indeed, it tries to write into the /root/foo file.
def test_failure():
    s = "message"
    wf = WriteFile("/root/foo")
    ret = wf.write(s)
    assert ret == len(s)


### This unit test must succeed, even though, like in the unit test
### test_failure above, it would write into a non accessible file
### (/root/foo). This is done by mocking the open class used in file
### write_file.py (through mock.patch) and by mocking the return value of
### the open.write() method (through the __enter__ method of the context
### manager created by the "with open()" call).
@patch("write_file.open")
def test_patch(open_mock: Mock):
    write_mock = open_mock.return_value.__enter__.return_value.write
    write_mock.return_value = 0
    f = "/root/foo"
    wf = WriteFile(f)
    s = "message"
    ret = wf.write(s)
    assert open_mock.call_args.args[0] == f
    assert write_mock.call_args.args[0] == s
    assert ret == 0
