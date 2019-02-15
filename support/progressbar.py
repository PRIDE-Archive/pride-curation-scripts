# !/usr/bin/env python3
# coding: utf-8
# -----------------------------------------------------------------------------------------
# Filename      : 	progressbar.py
# Authors       : 	Suresh Hewapathirana
# Date          : 	2019-02-14
# Description   : 	Show a progress bar to show that something is happening
# -----------------------------------------------------------------------------------------

import sys
import time


# Show progress bar with incrementing value
# This function was take from :
# Cordier, B. (2016). Text Progress Bar in the Console. [online] Stackoverflow.com.
# Available at: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
# [Accessed 24 Aug. 2016].
def show():
    """
    This function  increases the value of the progress bar
    However, this is just to show to the user, that something is happening
    Nothing to do with the value of the progress bar
    """
    items = list(range(0, 100))
    i = 0
    length = len(items)

    # Initial call to print 0% progress
    print_progress(i, length, prefix='Progress:', suffix='Complete', barLength=50)
    for item in items:
        time.sleep(0.008)
        # Update Progress Bar
        i += 1
        print_progress(i, length, prefix='Progress:', suffix='Complete', barLength=50)


# Print iterations progress
# This function was take from :
# Cordier, B. (2016). Text Progress Bar in the Console. [online] Stackoverflow.com.
# Available at: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
# [Accessed 24 Aug. 2016].
def print_progress(iteration, total, prefix='', suffix='', decimals=1, barLength=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    formattd_string = "{0:." + str(decimals) + "f}"
    percents = formattd_string.format(100 * (iteration / float(total)))
    filled_length = int(round(barLength * iteration / float(total)))
    bar = '█' * filled_length + '-' * (barLength - filled_length)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write('\n')
        sys.stdout.flush()
