README
I chose this exercise: https://homework.adhoc.team/slcsp/

ENVIRONMENT
I wrote all the code in Visual Studio Community. I'm running Windows 10 and Python 3.8.1.

ROOM FOR IMPROVEMENT
If I had more time I would have allowed command line inputs and added an additional test.

I currently have a test that looks at every zip code that appears in more than 
1 rate area and return False when they are provided as an input to zipcode_in_multiple_rate_areas().

HOW TO RUN
I tested this by using the Whack Whack Terminal extension for Visual Studio Community, but any terminal app should work.

1) Navigate to the folder containing these files
	slcp.py
	test.py
	zips.csv
	slcp.csv
	plans.csv

2) Start the Python interpreter. By default the command to do this in Windows is "py"
3) import all of slcsp.py
	"from slcsp import *"
4) Call the write_new_file() function
	"write_new_file()"
5) After a few seconds this will create a new file called "output_slcsp_[YYYY][mm][dd][HH][MM][SS]"
where YYYY is the year, mm is the month, dd is the day, HH is the hour
and SS is the second when the file was slcsp.py was imported.

Alternatively, if you have IDLE (the software that comes with your Python 
download from https://www.python.org/downloads/) installed then you can follow these steps.

1) From your Windows desktop, navigate to the folder containing slcsp.py.
2) Right-click slcsp.py
3) Click "Edit with IDLE".
	If multiple version of Python are installed then choose the Python 3.8 version of IDLE.
4) Press F5 to start the interpreter.
	You can also click Run>Run Module in the toolbar
5) Call "write_new_file()"

HOW TO RUN TESTS
1) Navigate to the folder containing these files
	slcp.py
	test.py
	zips.csv
	slcp.csv
	plans.csv

2) Start the Python interpreter. By default the command to do this in Windows is "py"
3) import all of test.py
	"from test import *"
4) Call the write_new_file() function
	"run_all_tests()"

Alternatively, if you have IDLE (the software that comes with your Python 
download from https://www.python.org/downloads/) installed then you can follow these steps.

1) From your Windows desktop, navigate to the folder containing test.py.
2) Right-click test.py
3) Click "Edit with IDLE".
	If multiple version of Python are installed then choose the Python 3.8 version of IDLE.
4) Press F5 to start the interpreter.
	You can also click Run>Run Module in the toolbar
5) Call "run_all_tests()"