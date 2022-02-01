import unittest
from fuv import *
from cmv import *
from pum import *
from parser import *
from generate_datapoints import *


class FormFUVTestCase(unittest.TestCase):
    def test_successful_launch_1(self):
        puv = [False for _ in range(15)]
        cmv = read_CMV_PUV_LCM_from_file()
        lcm = generate_LCM_matrix()
        pum = form_the_pum(cmv.CMV_VECTOR, lcm)
        fuv = form_the_fuv(pum, puv)
        self.assertTrue(all([fuv[i] for i in range(len(fuv))]))

    def test_successful_launch_2(self):
        puv = [True for _ in range(15)]
        cmv = read_CMV_PUV_LCM_from_file()
        lcm = generate_LCM_matrix(vals=["NOTUSED"])
        pum = form_the_pum(cmv.CMV_VECTOR, lcm)
        fuv = form_the_fuv(pum, puv)
        self.assertTrue(all([fuv[i] for i in range(len(fuv))]))

    def test_failed_launch_1(self):
        puv = [True for _ in range(15)]
        cmv = read_CMV_PUV_LCM_from_file()
        lcm = generate_LCM_matrix(vals=["ORR"])
        pum = form_the_pum(cmv.CMV_VECTOR, lcm)
        fuv = form_the_fuv(pum, puv)
        self.assertFalse(all([fuv[i] for i in range(len(fuv))]))

    # specifying an incorrect K_PTS = -1 causes
    # the program to raise an assertion error
    def test_failed_launch(self):
        with self.assertRaises(AssertionError):
            read_CMV_PUV_LCM_from_file("invalid_input.txt")
