import pytest
import time

@pytest.fixture
def smtp():
    import smtplib
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=1)


def test_ehlo(smtp):

    #time.sleep(10)
    response, msg = smtp.ehlo()

    assert response == 250
