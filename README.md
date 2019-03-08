# WEB AUTOMATION INSTRUCATIONS
## Steps:
1. Create virtual environment: virtualenv venv (optional)
2. Activate virtual environment: source venv/bin/activate (optional)
cd to main folder to locate the requirement.txt file and execute: pip install --no-cache-dir -r requirements.txt. requiremments.txt should provide all needed modules but just in case something is not working please use requirements1.txt.
3. Run automation: py.test -v -s tests/test_gnucash.py --browser= --html=report.html Example: py.test -v -s tests/test_gnucash.py --browser=chrome --html=report.html
4. View report in browser: <report_dir>/report.html
5. This frameworks generates automation logs but not screenshots

## Make sure make sure that the gekodriver and chromedriver are installed in some local directory and point the PATH in .bash_profile.
### Example:
PATH="/Users/yourusername/your_driver_directory/lib:${PATH}"

## Browser name choices are:
Chrome, Firefox

## NOTES:
For this demonstration I have used page object model as a design pattern. Pytest was chosen to drive the automation because makes test results readable and can be easily expanded to deliver different style of test reports.
