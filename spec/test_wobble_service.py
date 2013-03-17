"""
WobbeService whitebox tests.
This test should test complex internal processes.
Only test really complex logic that would result in
confusing errors in whitebox interation testing.

In an ideal world we should have no test in here!
"""
from nose.tools import *
from wobble import *


def test_true():
    eq(True, True)
