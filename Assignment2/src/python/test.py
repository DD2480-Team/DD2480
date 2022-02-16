import os
from os import path
import py
import pytest


class Test:
    """Create an object to conduct test on python program"""

    def __init__(self, pathToTestSuite):
        self.path = pathToTestSuite
        self.result, self.capture = self.test()

    def test(self):
        """
        Conduct test with test suite.

        Returns:
        [Bool]: True if test passed, False if error occurs or test failed
        """
        print("Testing...")

        if path.exists(self.path) == False:
            print("Test suite doesn't exist.")
            return False, None

        try:
            capture = py.io.StdCapture()
            exit_code = pytest.main([self.path, "--collect-only", "-q"])
            capture.reset()
        except:
            print("Error occurs during testing.")
            return False, capture

        if exit_code == 0:
            print("All testcases are passed!!")
            print("The capture is", capture)
            return True, capture
        elif exit_code == 1:
            print("Some tests are failed.")
            return False, capture
        else:
            print("Error occurs during testing.")
            return False, capture


if __name__ == "__main__":
    testing = Test("./tests")
    print(testing.result)
