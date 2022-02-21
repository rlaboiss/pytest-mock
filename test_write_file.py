from unittest.mock import Mock, patch
from write_file import WriteFile


def test_success():
    s = 'message'
    wf = WriteFile('/tmp/foo')
    ret = wf.write(s)
    assert ret == len(s)


def test_failure():
    s = 'message'
    wf = WriteFile('/root/foo')
    ret = wf.write(s)
    assert ret == len(s)


@patch('write_file.open')
def test_patch(open_mock: Mock):
    open_mock.return_value.__enter__.return_value.write.return_value = 0
    s = 'message'
    wf = WriteFile('/root/foo')
    ret = wf.write(s)
    assert ret == 0
