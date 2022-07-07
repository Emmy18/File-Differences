# Title: File Differences

**Description**: In this project I found differences in the contents of two files by identifying the location of the first character that differs between the two input files. This is usefule in comparing how something has changed.  The first difference is presented to the user to allow them to see what has happened.  

**In this project:**

    The singleline_diff(line1, line2) function returns the index where the first difference between line1 and line2 occurs.

    The singleline_diff_format(line1, line2, idx) function, a three line formatted string showing the location of the first difference between line1 and line2.

    The multiline_diff(lines1, lines2) function Returns a tuple containing the line number (starting from 0) and the index in that line where the first difference between lines1 and lines2 occurs.

    The get_file_lines(filename) function returns a list of lines from the file named filename

    The file_diff_format(filename1, filename2) function returns a four line string showing the location of the first difference between the two files named by the inputs.