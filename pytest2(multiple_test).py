# In a real scenario, we will have multiple test files and each file will have a number of tests. Tests will cover various modules and functionalities. Suppose, we want to run only a specific set of tests; how do we go about it?
#
# Pytest provides two ways to run the subset of the test suite.
#
#     -> Select tests to run based on substring matching of test names.
#     -> Select tests groups to run based on the markers applied.
#
# We will explain these two with examples in subsequent chapters.





#Substring Matching of Test Names :

# approches to run multiple test :
# 1. test name by substring matching(py.test -k method2 -v)

# To execute the tests containing a string in its name we can use the following syntax − pytest -k <substring> -v

import pytest

# def test_method1():
#     x=5
#     y=10
#     assert x==y
#
# def test_method2():
#     a=15
#     b=20
#     assert a+5==b



# # 2. Group them by markers : we have to specify the markers before each test
#
#
# Pytest allows us to use markers on test functions. Markers are used to set various features/attributes to test functions. Pytest provides many inbuilt markers such as xfail, skip and parametrize. Apart from that, users can create their own marker names. Markers are applied on the tests using the syntax given below −
#
# @pytest.mark.<markername>
#
# To use markers, we have to import pytest module in the test file. We can define our own marker names to the tests and run the tests having those marker names.
#
# To run the marked tests, we can use the following syntax −
#
# pytest -m <markername> -v
#
# -m <markername> represents the marker name of the tests to be executed.


@pytest.mark.one
def test_method1():
    x=5
    y=10
    assert x==y

@pytest.mark.two
def test_method2():
    a=15
    b=20
    assert a+5==b

# to run this -> py.test -m two
