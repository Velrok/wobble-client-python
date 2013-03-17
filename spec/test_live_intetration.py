"""
This are blackbox integration test agains the wobble api using
the WobbleService class.
It purpose is to ensure that the WobbleService is capable of
calling the wobble endpoint and return valid data.

No internals should be test. Also keep the dependencies agains
return data assumptions to a minimun. Test for structure not
content.
"""
from nose.tools import *
from wobble import *

WOBBLE_API_ENDPOINT = "http://wobble.moinz.de/endpoint.php"


def test_true():
    eq_(True, True)
