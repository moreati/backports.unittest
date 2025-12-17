import os.path
from backports.unittest._test.support import load_package_tests


def load_tests(*args):
    return load_package_tests(os.path.dirname(__file__), *args)
