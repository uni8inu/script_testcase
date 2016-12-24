import sys
import runpy
from unittest import TestCase

# reffer to: http://stackoverflow.com/questions/3657955/how-to-execute-another-python-script-from-your-script-and-be-able-to-debug

class ScriptTest(TestCase):
    saved_argv = []

    def setUp(self):
        self.saved_argv = sys.argv

    def tearDown(self):
        sys.argv = self.saved_argv

    def test_hello_module_normal(self):
        my_args = ["hello.py","wanwan"]
        sys.argv = my_args

        runpy.run_path("hello.py",run_name="__main__")