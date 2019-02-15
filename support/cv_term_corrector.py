# !/usr/bin/env python3
# coding: utf-8
# -----------------------------------------------------------------------------------------
# Filename      : 	cv_term_corrector.py
# Authors       : 	Suresh Hewapathirana
# Date          : 	2019-02-14
# Description   : 	Remove CV term description from Submission.px Metadata
# Format        :   python3 cv_term_corrector.py -i  <input file> -o  <output file>
# Example       :   python3 cv_term_corrector.py -i path/to/input/submission.px -o  path/to/output/submission.px
# -----------------------------------------------------------------------------------------

import argparse
import progressbar
import re


def main():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Input filename")
    ap.add_argument("-o", "--output", required=True, help="output filename")
    args = vars(ap.parse_args())

    # assign values of the arguments
    input_filename = args["input"]
    output_filename = args["output"]
    input_px_submission_file = open(input_filename, "r")


    # initialise variables
    modified_data = ""
    line_number = 0

    for line in input_px_submission_file.readlines():
        match = re.search('MTD\t\w*\t\[\w*,.*:\d*,.*,(.*)]', line)
        if match and match.group(1) is not None and match.group(1) != " ":
            line = modify_line(match, line, line_number)
        modified_data += line
        line_number = line_number + 1
    input_px_submission_file.close()

    output_px_submission_file = open(output_filename, 'w')
    output_px_submission_file.write(modified_data)
    output_px_submission_file.close()
    progressbar.show()


def modify_line(match, line, line_number):
    modified_line = line.split(match.group(1))[0] + " ]\n"
    print("Line number: " + str(line_number))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(line[:-1])
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(modified_line)
    return modified_line


if __name__ == "__main__":
    main()
