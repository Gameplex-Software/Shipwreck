# ----------------------------------------------------------------------------
# ShipHelm Copyright 2020-2023 by Gameplex Software and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

class Shipwreck:
    def __init__(self):
        self.error_info = ""
        self.suggested_fixes = []

    def handle_error(self):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_list = traceback.format_exception(exc_type, exc_value, exc_traceback)
        self.error_info = ''.join(tb_list)
        self.suggest_fixes()

    def suggest_fixes(self):
        # Look for common patterns in the traceback to suggest potential fixes.
        tb_lines = self.error_info.split("\n")
        for i, line in enumerate(tb_lines):
            # Check for "NameError"
            if "NameError" in line:
                match = re.search(r"name '(\w+)' is not defined", line)
                if match:
                    var_name = match.group(1)
                    self.suggested_fixes.append(f"Check that '{var_name}' is defined before use.")
            # Check for "TypeError"
            elif "TypeError" in line:
                match = re.search(r"'(\w+)' object is not callable", line)
                if match:
                    func_name = match.group(1)
                    self.suggested_fixes.append(f"Check that '{func_name}' is a function and not an object.")
                else:
                    self.suggested_fixes.append("Check that the function is being called with the correct number and type of arguments.")
            # Check for "AttributeError"
            elif "AttributeError" in line:
                match = re.search(r"object has no attribute '(\w+)'", line)
                if match:
                    attr_name = match.group(1)
                    self.suggested_fixes.append(f"Check that '{attr_name}' is a valid attribute of the object.")
                else:
                    self.suggested_fixes.append("Check that the object has the required attribute.")
            # Check for "IndexError"
            elif "IndexError" in line:
                match = re.search(r"list index out of range", line)
                if match:
                    self.suggested_fixes.append("Check that the index is within the range of the list.")
            # Check for "ZeroDivisionError"
            elif "ZeroDivisionError" in line:
                match = re.search(r"division by zero", line)
                if match:
                    self.suggested_fixes.append("Check that the divisor is not zero.")
            # Check for "SyntaxError"
            elif "SyntaxError" in line:
                match = re.search(r"invalid syntax", line)
                if match:
                    self.suggested_fixes.append("Check that the code is syntactically correct.")
            # Check for "ValueError"
            elif "ValueError" in line:
                match = re.search(r"invalid literal for int\(\) with base (\d+)", line)
                if match:
                    base = match.group(1)
                    self.suggested_fixes.append(f"Check that the value being converted to int is in base {base}.")
                else:
                    self.suggested_fixes.append("Check that the input value is valid.")
            # Check for "KeyError"
            elif "KeyError" in line:
                match = re.search(r"key '(.+)'", line)
                if match:
                    key = match.group(1)
                    self.suggested_fixes.append(f"Check that the key '{key}' is present in the dictionary.")
            # Check for "ImportError"
            elif "ImportError" in line:
                match = re.search(r"No module named '(\w+)'", line)
                if match:
                    module_name = match.group(1)
                    self.suggested_fixes.append(f"Check that the module '{module_name}' is installed and accessible.")
            # Check for "FileNotFoundError"
            elif "FileNotFoundError" in line:
                match = re.search(r"No such file or directory: '(.+)'", line)
                if match:
                    file_path = match.group(1)
                    self.suggested_fixes.append(f"Check that the file path '{file_path}' is correct.")
            # Check for "IndentationError"
            elif "IndentationError" in line:
                self.suggested_fixes.append("Check that the indentation of the code is correct.")

    def show_popup(self):
        print("An error occurred. Here is more information:\n")
        print(self.error_info)

        if self.suggested_fixes:
            print("\nSuggested fixes:\n")
            for fix in self.suggested_fixes:
                print(f"- {fix}")