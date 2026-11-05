# Warehouse Management System Lab

This repository contains the codebase and simulated test scripts generated for the Warehouse Management System case study (Modules 3-5).

## Files Included:
1. `Dockerfile`: Container configuration for the environment (Module 3).
2. `bin_allocation.py`: The core algorithm with simulated fixes from SonarQube & AI Code Review (Module 5).
3. `test_bin_allocation.py`: PyTest unit tests covering edge cases and intentional code weakness fixes (Module 4 & 5).
4. `test_selenium_ui.py`: Simulated Selenium WebDriver automated UI testing script (Module 4.3).
5. `monitor.py`: The simulated 10-minute system health check script (Module 4.5).

## How to run (Simulated Environment)
To run unit tests:
`pytest test_bin_allocation.py -v`

To run the monitor script:
`python monitor.py`

To run the simulated Selenium tests:
`python test_selenium_ui.py`
