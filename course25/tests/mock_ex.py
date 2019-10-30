import pytest
from smtplib import SMTP
from pytest_mock import mocker

# https://pypi.python.org/pypi/pytest-mock


@pytest.fixture
def smtp():
    return SMTP("smtp.gmail.com", 587, timeout=5)


def test_ehlo(smtp, mocker):
    smtp = smtp
    print(smtp)
    mocker.patch.object(smtp, 'putcmd')  # just empty stub
    mocker.patch.object(smtp, 'getreply')
    smtp.getreply.return_value = (250, b'')
    response, msg = smtp.ehlo()
    assert response == 250
