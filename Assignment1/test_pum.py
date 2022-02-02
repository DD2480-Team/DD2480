import unittest
from pum import *


class FormPumTestCase(unittest.TestCase):
    def test(self):
        # the result of function form_the_pum() should be the same as variable pum (calculated by hand)
        cmv = [
            True,
            False,
            True,
            True,
            False,
            True,
            False,
            True,
            True,
            False,
            True,
            False,
            True,
            True,
            False,
        ]
        lcm = [
            [
                "ORR",
                "ANDD",
                "ORR",
                "ORR",
                "NOTUSED",
                "NOTUSED",
                "ORR",
                "ORR",
                "NOTUSED",
                "ORR",
                "NOTUSED",
                "NOTUSED",
                "ANDD",
                "ORR",
                "ANDD",
            ],
            [
                "ANDD",
                "ORR",
                "NOTUSED",
                "NOTUSED",
                "NOTUSED",
                "ANDD",
                "NOTUSED",
                "NOTUSED",
                "ANDD",
                "ANDD",
                "ORR",
                "ORR",
                "ANDD",
                "ORR",
                "ORR",
            ],
            [
                "ORR",
                "NOTUSED",
                "ANDD",
                "ORR",
                "ANDD",
                "ANDD",
                "NOTUSED",
                "NOTUSED",
                "ORR",
                "NOTUSED",
                "ANDD",
                "ORR",
                "NOTUSED",
                "ORR",
                "ORR",
            ],
            [
                "ORR",
                "NOTUSED",
                "ORR",
                "ORR",
                "NOTUSED",
                "ANDD",
                "NOTUSED",
                "ORR",
                "ORR",
                "ANDD",
                "ANDD",
                "NOTUSED",
                "NOTUSED",
                "ANDD",
                "ANDD",
            ],
            [
                "NOTUSED",
                "NOTUSED",
                "ANDD",
                "NOTUSED",
                "NOTUSED",
                "ANDD",
                "NOTUSED",
                "ANDD",
                "NOTUSED",
                "NOTUSED",
                "NOTUSED",
                "ANDD",
                "ORR",
                "NOTUSED",
                "NOTUSED",
            ],
            [
                "NOTUSED",
                "ANDD",
                "ANDD",
                "ANDD",
                "ANDD",
                "NOTUSED",
                "NOTUSED",
                "ORR",
                "ANDD",
                "ANDD",
                "ANDD",
                "ANDD",
                "NOTUSED",
                "ORR",
                "ANDD",
            ],
            [
                "ORR",
                "NOTUSED",
                "NOTUSED",
                "NOTUSED",
                "NOTUSED",
                "NOTUSED",
                "NOTUSED",
                "ANDD",
                "ANDD",
                "ORR",
                "ANDD",
                "ANDD",
                "NOTUSED",
                "ANDD",
                "NOTUSED",
            ],
            [
                "ORR",
                "NOTUSED",
                "NOTUSED",
                "ORR",
                "ANDD",
                "ORR",
                "ANDD",
                "ORR",
                "NOTUSED",
                "ANDD",
                "ANDD",
                "NOTUSED",
                "ANDD",
                "ANDD",
                "ANDD",
            ],
            [
                "NOTUSED",
                "ANDD",
                "ORR",
                "ORR",
                "NOTUSED",
                "ANDD",
                "ANDD",
                "NOTUSED",
                "ANDD",
                "NOTUSED",
                "ANDD",
                "NOTUSED",
                "ANDD",
                "ORR",
                "ANDD",
            ],
            [
                "ORR",
                "ANDD",
                "NOTUSED",
                "ANDD",
                "NOTUSED",
                "ANDD",
                "ORR",
                "ANDD",
                "NOTUSED",
                "ORR",
                "NOTUSED",
                "NOTUSED",
                "NOTUSED",
                "ORR",
                "ORR",
            ],
            [
                "NOTUSED",
                "ORR",
                "ANDD",
                "ANDD",
                "NOTUSED",
                "ANDD",
                "ANDD",
                "ANDD",
                "ANDD",
                "NOTUSED",
                "ORR",
                "NOTUSED",
                "ORR",
                "NOTUSED",
                "ANDD",
            ],
            [
                "NOTUSED",
                "ORR",
                "ORR",
                "NOTUSED",
                "ANDD",
                "ANDD",
                "ANDD",
                "NOTUSED",
                "NOTUSED",
                "NOTUSED",
                "NOTUSED",
                "ORR",
                "ANDD",
                "NOTUSED",
                "NOTUSED",
            ],
            [
                "ANDD",
                "ANDD",
                "NOTUSED",
                "NOTUSED",
                "ORR",
                "NOTUSED",
                "NOTUSED",
                "ANDD",
                "ANDD",
                "NOTUSED",
                "ORR",
                "ANDD",
                "ANDD",
                "NOTUSED",
                "NOTUSED",
            ],
            [
                "ORR",
                "ORR",
                "ORR",
                "ANDD",
                "NOTUSED",
                "ORR",
                "ANDD",
                "ANDD",
                "ORR",
                "ORR",
                "NOTUSED",
                "NOTUSED",
                "NOTUSED",
                "ANDD",
                "NOTUSED",
            ],
            [
                "ANDD",
                "ORR",
                "ORR",
                "ANDD",
                "NOTUSED",
                "ANDD",
                "NOTUSED",
                "ANDD",
                "ANDD",
                "ORR",
                "ANDD",
                "NOTUSED",
                "NOTUSED",
                "NOTUSED",
                "ANDD",
            ],
        ]

        pum = [
            [
                True,
                False,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                False,
            ],
            [
                False,
                False,
                True,
                True,
                True,
                False,
                True,
                True,
                False,
                False,
                True,
                False,
                False,
                True,
                False,
            ],
            [
                True,
                True,
                True,
                True,
                False,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
            ],
            [
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                False,
                True,
                True,
                True,
                True,
                False,
            ],
            [
                True,
                True,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                True,
                False,
                True,
                True,
                True,
            ],
            [
                True,
                False,
                True,
                True,
                False,
                True,
                True,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
            ],
            [
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                False,
                False,
                False,
                False,
                False,
                True,
                False,
                True,
            ],
            [
                True,
                True,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
                False,
                True,
                True,
                True,
                True,
                False,
            ],
            [
                True,
                False,
                True,
                True,
                True,
                True,
                False,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                False,
            ],
            [
                True,
                False,
                True,
                False,
                True,
                False,
                False,
                False,
                True,
                False,
                True,
                True,
                True,
                True,
                False,
            ],
            [
                True,
                True,
                True,
                True,
                True,
                True,
                False,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                False,
            ],
            [
                True,
                False,
                True,
                True,
                False,
                False,
                False,
                True,
                True,
                True,
                True,
                False,
                False,
                True,
                True,
            ],
            [
                True,
                False,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                False,
                True,
                True,
                True,
            ],
            [
                True,
                True,
                True,
                True,
                True,
                True,
                False,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
            ],
            [
                False,
                False,
                True,
                False,
                True,
                False,
                True,
                False,
                False,
                False,
                False,
                True,
                True,
                True,
                False,
            ],
        ]
        self.assertTrue(form_the_pum(cmv, lcm) == pum)

if __name__ == "__main__":
    unittest.main()