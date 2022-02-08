import io
import os
from os import path
from pylint import epylint as lint


class SyntaxCheck:
    '''
    Create an object to conduct syntax check on python program
    '''
    def __init__(self, path):
        self.path = path
        self.result = self.check()

    
    def check(self):
        '''
        Conduct syntax check. 
        
        Returns:
        [Bool]: True if syntax check passed, False if error occurs or syntax check failed
        '''
        print("Syntax checking...")

        if path.exists(self.path) == False:
            print("Path doesn't exist.")
            return False

        try:
            (pylint_stdout, pylint_stderr) = lint.py_run(self.path +' --errors-only', return_std=True)
        except:
            print("Check failed.")
            return False

        check_result = pylint_stdout.read()
        if len(pylint_stderr.read()) != 0:
            print("Check failed.")
            return False

        if "syntax-error" in check_result:
            print("Syntax error!!")
            return False
        else:
            print("Ready for testing!!")
            return True

if __name__=='__main__':
    syntaxCheck = SyntaxCheck("./server.py")