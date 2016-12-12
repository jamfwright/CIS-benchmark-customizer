# CIS-benchmark-customizer
## Customize CIS Benchmarks with a custom exclusion list.

Maintaining custom benchmark XML files can be tedious.  This Python script aims to simplify things, allowing you to keep all of your approved exceptions in a text file.  The script runs through each exclusion, finds the matching test in the benchmark file, then disables it by setting the 'selected' attribute to 'false' (default is 'true', which runs the test).  The original benchmark is overwritten to mainting naming requirements.

## Important Note
The logic is not there to re-add tests removed from the exclusion file.  You should always run this script against a new copy of the benchmark file you wish to modify.

## Usage
Start by creating your exclusion list and saving it in a text file.  This is done most easily with copy/paste.  Start by opening the bencmark file, such as:  CIS_CentOS_Linux_7_Benchmark_v2.1.0-xccdf.xml

Then, scroll down past the 'Notice' text, until you reach the listing of tests.  It will look like something like this:

```
      <select idref="xccdf_org.cisecurity.benchmarks_rule_1.1.1.1_Ensure_mounting_of_cramfs_filesystems_is_disabled" selected="true"/>
      <select idref="xccdf_org.cisecurity.benchmarks_rule_1.1.1.2_Ensure_mounting_of_freevxfs_filesystems_is_disabled" selected="true"/>
      <select idref="xccdf_org.cisecurity.benchmarks_rule_1.1.1.3_Ensure_mounting_of_jffs2_filesystems_is_disabled" selected="true"/>
      <select idref="xccdf_org.cisecurity.benchmarks_rule_1.1.1.4_Ensure_mounting_of_hfs_filesystems_is_disabled" selected="true"/>
      <select idref="xccdf_org.cisecurity.benchmarks_rule_1.1.1.5_Ensure_mounting_of_hfsplus_filesystems_is_disabled" selected="true"/>
      <select idref="xccdf_org.cisecurity.benchmarks_rule_1.1.1.6_Ensure_mounting_of_squashfs_filesystems_is_disabled" selected="true"/>
      <select idref="xccdf_org.cisecurity.benchmarks_rule_1.1.1.7_Ensure_mounting_of_udf_filesystems_is_disabled" selected="true"/>
      <select idref="xccdf_org.cisecurity.benchmarks_rule_1.1.1.8_Ensure_mounting_of_FAT_filesystems_is_disabled" selected="true"/>
      <select idref="xccdf_org.cisecurity.benchmarks_rule_1.1.3_Ensure_nodev_option_set_on_tmp_partition" selected="true"/>
      <select idref="xccdf_org.cisecurity.benchmarks_rule_1.1.4_Ensure_nosuid_option_set_on_tmp_partition" selected="true"/>
      <select idref="xccdf_org.cisecurity.benchmarks_rule_1.1.5_Ensure_noexec_option_set_on_tmp_partition" selected="true"/>
```    

For each test you wish to exclude from the assessment, copy the data from the idref attribute, and paste it into a text file.  Make sure you do not copy the double-quotes.  Your exclusions text file may look something like this:

```
xccdf_org.cisecurity.benchmarks_rule_1.1.1.1_Ensure_mounting_of_cramfs_filesystems_is_disabled
xccdf_org.cisecurity.benchmarks_rule_1.1.1.5_Ensure_mounting_of_hfsplus_filesystems_is_disabled
xccdf_org.cisecurity.benchmarks_rule_1.1.1.8_Ensure_mounting_of_FAT_filesystems_is_disabled
xccdf_org.cisecurity.benchmarks_rule_1.1.5_Ensure_noexec_option_set_on_tmp_partition
```
