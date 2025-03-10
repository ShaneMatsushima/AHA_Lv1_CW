@echo off
echo Running unit tests...
python test/test_add.py
if %errorlevel% equ 0 (
    echo All tests passed!
) else (
    echo Some tests failed.
)
pause