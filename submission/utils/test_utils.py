"""
file name:      test_utils.py
author:         Sachinthana Pathiranage
date created:   14/08/2022
purpose:        Test utilities - Mocks standard input and output capabilities.
version:        1.0
reference:      https://gist.github.com/metatoaster/64139971b53ad728dba636e34b8a5558
"""

# imports
import sys
import io

class StringIO(io.StringIO):
    """Wrapper class for io.StringIO

    :param value: Input/ output value
    :type value: str
    """

    def __init__(self, value = ''):
        """Constructor method.
        """
        value = value.encode('utf8', 'backslashreplace').decode('utf8')
        io.StringIO.__init__(self, value)

    def write(self, value):
        """Write value.

        :param value: Input/ output value
        :type value: str
        """
        io.StringIO.write(self, value.encode(
            'utf8', 'backslashreplace').decode('utf8'))

def stub_stdin(testcaseInst, inputs):
    """Mock standard input.

    :param testcaseInst: Test case instance.
    :type testcaseInst: unittest.TestCase
    :param inputs: Input to mock stdin.
    :type inputs: str
    """
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcaseInst.addCleanup(cleanup)
    sys.stdin = StringIO(inputs)

def stub_stdouts(testcase_inst):
    """Mock standard output.

    :param testcaseInst: Test case instance.
    :type testcaseInst: unittest.TestCase
    """
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = StringIO()
    sys.stdout = StringIO()