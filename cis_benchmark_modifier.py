'''
Name: cis_benchmark_modifier.py
Author:  James Wright
Version:  1.0
Date: 12/13/2016

Purpose:  Modifies CIS Benchmark XCCDF XML files for exclusions that are maintained in a
          simple text file.
'''

# Imports

from lxml import etree
import os

os.chdir(r"c:\users\jamfw\tmo")

# Set the variables
exclusion_count = 0
change_count = 0

# XML Benchmark file to load
benchmark = raw_input('Enter Path and XML benchmark file to load (Make sure to use a copy of the original, this one will be over-written!): ')

# Text file of exclusions to load
disable_list = raw_input('Enter the path and filename of the exclusions: ')

# XML Tag we will be editing attributes for
btag = r".//{http://checklists.nist.gov/xccdf/1.2}select"



### Do the work

# Set the parser (fixes pretty_print, at least to some extent)
parser = etree.XMLParser(remove_blank_text=True)
# Read in the XML benchmark file
tree = etree.parse(benchmark, parser=parser)

# Run through the file of exclusions and set them
with open(disable_list) as f:
    for exclusion in f:
        exclusion_count += 1
        for each in tree.findall(".//{http://checklists.nist.gov/xccdf/1.2}select"):
            if exclusion.rstrip("\n") in str(each.get("idref")):
                each.attrib["selected"] = "false"
                change_count += 1
                break

# Write the XML data back
tree.write(benchmark, pretty_print=True)

# Tell us how things went
print("\nNumber of exclusions: " + str(exclusion_count))
print("Number of changes made: " + str(change_count))

if exclusion_count == change_count:
    print("\nThe number of exclusions matches the number of changes.  There's a good chance we got it right :)")
else:
    print("\nWARNING:  The number of exclusions does not match the number of changes.  Something went wrong :(")
    print("\nCheck your exclusions file for errors and make sure that you are using an original benchmarks XCCDF XML file (Not the OVAL one)")
