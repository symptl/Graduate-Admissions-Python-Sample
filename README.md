# Graduate-Admissions-Python-Sample

By: Shyam Patel

About: 

This code is intended as a demonstration of simple object-oriented concepts applied to some basic data structures and algorithms.
though it is not a comprehensive review of my DSA knowledge.

An array of integers, spanning the range from 0-100,000 in increments of 1, has been randomly shuffled as a simulated "dataset".
The posted "dataset" is the random iteration that corresponds to the results posted alongside it. Results can vary with each
execution of the dataset generation code (initial_list_generation.py) as well as the actual dataset manipulation code (main.py),
but the approximate order of magnitude should remain the same across attempts. Several array sorting and searching algorithms are
included in this demo, as well as some alternative data structures to hold/manipulate the initial data with their own methods to
accomplish similar tasks.

"main.py" drives the entire demo as far as actual array manipulation, repackaging into different data structures, and further
method execution on those structures. It also gathers the timing and variable size data that is output at the end. The current
"results.txt" and "randomized_list_int.txt" files are the official demo inputs/outputs but feel free to try it out for yourself
according to the instructions below or to open up the scripts and get a closer look at the implementation.


Requirements: The latest version of Python (scripts have only been tested on Windows), a reasonably powerful computer (eg Chromebooks aren't recommended)

Note: All scripts and folders relevant to the demo can be found under the "Sample Materials" folder.

Instructions:

1)	Check that the "Starting Dataset" folder is populated with a .txt file that holds randomly shuffled numbers from 0-100k.
	  The file should be named "randomized_list_int". If this is not present or if there are any questions around the file's 
	  integrity, run the "initial_list_generation.py" script by double clicking on the icon. Existing files named
	  "randomized_list_int" will be overwritten by this script. Execution should be virtually instantaneous.

2)	Ensure that all folders and scripts maintain their relative positions to each other that they started with in the repo. 
	  Changing this in any way will most likely cause the demo to fail.

3)	Run "main.py" to begin the demo. You will see an empty command line window while this script executes. Expect this to 	
	  take up to 10 minutes, depending on the power of the PC running this.

4) 	This window will disappear once the script completes, the "Results" folder will be populated with a "results.txt" file
	  that will display execution times of different algorithms executed as well as memory sizes for the starting data as it
	  gets manipulated or converted into different data structures. Keep in mind that the script will overwrite any previous
	  file named "results.txt" so this file should be copied into another directory for each run that the user would like to 
	  keep a record of.
