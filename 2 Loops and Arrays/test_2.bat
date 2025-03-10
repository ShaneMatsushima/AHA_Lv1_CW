@echo off
REM Navigate to the parent directory (where variables.py is located)
cd %~dp0

REM Run the test script using Python
python test/more_loops_test.py

REM Pause to see the output (optional)
pause