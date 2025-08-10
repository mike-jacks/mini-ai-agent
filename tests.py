# tests.py

import unittest
from textwrap import dedent
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


class TestRunPythonFile(unittest.TestCase):
    def test_run_python_file(self):
        result = run_python_file("calculator", "main.py")
        self.assertTrue("STDOUT:" in result)
        self.assertFalse("STDERR:" in result)
        print(result)

        result = run_python_file("calculator", "main.py", ["3 + 5"])
        self.assertTrue("STDOUT:" in result)
        self.assertFalse("STDERR:" in result)
        print(result)

        result = run_python_file("calculator", "tests.py")
        self.assertFalse("STDOUT:" in result)
        self.assertTrue("STDERR:" in result)
        print(result)

        result = run_python_file("calculator", "../main.py")
        self.assertTrue("Error:" in result)
        print(result)

        result = run_python_file("calculator", "nonexistent.py")
        self.assertTrue("Error:" in result)
        print(result)

# class TestWriteFile(unittest.TestCase):
#     def test_write_file(self):
#         result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#         self.assertTrue(result.startswith("Successfully wrote to"))
#         print(result)

#         result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#         self.assertTrue(result.startswith("Successfully wrote to"))
#         print(result)

#         result = write_file("calculator", "/tmp/tmp.txt", "this should not be allowed")
#         self.assertTrue(result.startswith("Error:"))
#         print(result)

# class TestGetFileContent(unittest.TestCase):
#     def test_get_file_content(self):
#         result = get_file_content("calculator", "lorem.txt")
#         expected_end = '"lorem.txt" truncated at 10000 characters'
#         self.assertTrue(result.endswith(expected_end))

#         result = get_file_content("calculator", "main.py")
#         not_expected_end = '"main.py" truncated at 10000 characters'
#         self.assertFalse(result.endswith(not_expected_end))
#         print(result)

#         result = get_file_content("calculator", "pkg/calculator.py")
#         not_expected_end = '"pkg/calculator.py" truncated at 10000 characters'
#         self.assertFalse(result.endswith(not_expected_end))
#         print(result)

#         result = get_file_content("calculator", "/bin/cat")
#         self.assertTrue(result.startswith("Error:"))
#         print(result)

#         result = get_file_content("calculator", "pkg/does_not_exist.py")
#         self.assertTrue(result.startswith("Error:"))
#         print(result)


# class TestGetFilesInfo(unittest.TestCase):
#     def test_get_files_info(self):
#         result = get_files_info("calculator", ".")
#         expected = dedent("""\
# Result for current directory:
#  - tests.py: file_size=1342 bytes, is_dir=False
#  - main.py: file_size=575 bytes, is_dir=False
#  - pkg: file_size=160 bytes, is_dir=True
# """).rstrip()
#         self.assertEqual(result.rstrip(), expected)
#         print(result)
    
#         result = get_files_info("calculator", "pkg")
#         expected = dedent("""\
# Result for 'pkg' directory:
#  - render.py: file_size=766 bytes, is_dir=False
#  - calculator.py: file_size=1737 bytes, is_dir=False
# """).rstrip()
#         self.assertEqual(result.rstrip(), expected)
#         print(result)

#         result = get_files_info("calculator", "/bin")
#         expected = 'Error: Cannot list "/bin" as it is outside the permitted working directory'
#         self.assertEqual(result, expected)
#         print(result)
    
#         result = get_files_info("calculator", "../")
#         expected = 'Error: Cannot list "../" as it is outside the permitted working directory'
#         self.assertEqual(result, expected)
#         print(result)

if __name__ == "__main__":
    unittest.main()