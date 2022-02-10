import os
from os import path
import pytest

class Test:
    """ Create an object to conduct test on python program 
    """
    def __init__(self, pathToTestSuite):
        self.path = pathToTestSuite
        self.result = self.test()
    
    def test(self):
        '''
        Conduct test with test suite. 
        
        Returns:
        [Bool]: True if test passed, False if error occurs or test failed
        '''
        print("Testing...")

        if path.exists(self.path) == False:
            print("Test suite doesn't exist.")
            return False
        
        try:
            exit_code = pytest.main([self.path])
        except:
            print("Error occurs during testing.")
            return False

        if exit_code == 0:
            print("All testcases are passed!!")
            return True
        elif exit_code == 1:
            print("Some tests are failed.")
            return False
        else:
            print("Error occurs during testing.")
            return False
        

    


if __name__ == "__main__":
    testing = Test("./test_server.py")
    print(testing.result)