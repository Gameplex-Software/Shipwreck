<p align="center">
<a href="https://gameplex-software.github.io/Shipwreck/">  
<img src="https://user-images.githubusercontent.com/34868944/223500400-a63c020b-9aa9-47de-a91d-1e5fa42326b4.png" width="400" />
</a>
</p>


## Usage

To use Shipwreck, simply import the `Shipwreck` class and call its `handle_error` method with the exception that was raised:

```
from shipwreck import Shipwreck

try:
    # Some code that might raise an exception   
except Exception as e:
    sw = Shipwreck()
    sw.handle_error(e)
```

The `handle_error` method will display a popup window with information about the error, including the error message, traceback, and any suggested fixes.

## Suggested Fixes

Shipwreck can automatically detect common types of errors and suggest fixes for them. For example:

-   If an `AttributeError` is raised because a method or attribute is missing, Shipwreck will suggest checking the spelling of the method or attribute name.
-   If an `ImportError` is raised because a module is missing, Shipwreck will suggest checking that the module is installed and accessible.
-   If a `FileNotFoundError` is raised because a file is missing, Shipwreck will suggest checking that the file path is correct.
-   If an `IndentationError` is raised because of incorrect indentation, Shipwreck will suggest checking the indentation of the code.

Shipwreck can detect many other types of errors and provide suggested fixes for them. If you encounter an error that Shipwreck doesn't recognize, you can add a new error pattern and suggested fix by editing the `Shipwreck` class.
