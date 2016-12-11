# CIS-benchmark-customizer
## Customize CIS Benchmarks with a custom exclusion list.

Maintaining custom benchmark XML files can be tedious.  This Python script aims to simplify things, allowing you to keep all of your approved exceptions in a text file.  The script runs through each exclusion, finds the matching test in the benchmark file, then disables it by setting the 'selected' attribute to 'false' (default is 'true', which runs the test).

## Important Note
The logic is not there to re-add tests removed from the exclusion file.  You should always run this script against a new copy of the benchmark file you wish to modify.

## Usage
Start by creating your exclusion list and saving it in a text file.  This is done most easily with copy/paste.  Start by opening the bencmark file, such as:  CIS_CentOS_Linux_7_Benchmark_v2.1.0-xccdf.xml

Then, scroll down past the 'Notice' text, until you reach the 
