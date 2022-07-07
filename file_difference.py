"""
Project for for finding differences in file contents.

"""
IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the x where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if len(line1) > len(line2):
        for itrb in range(len(line2)):
            if line1[itrb] != line2[itrb]:
                return itrb
    else:
        for itrb in range(len(line1)):
            if line2[itrb] != line1[itrb]:
                return itrb 
    if line1 != line2:
        return min(len(line1), len(line2))
    else:
        return IDENTICAL
   
def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - x at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid x, then returns an empty string.
    """
    #conditions to be checked
    gt_line1, gt_line2, lt_zero = idx > len(line1),  idx > len(line2), idx<0
    new_line, crg_ret = "\n", "\r"

    #checking conditonals
    if gt_line1 or gt_line2 or lt_zero:
        return ""
    if new_line in line1 or new_line in line2 or crg_ret in line1 or crg_ret in line2:
        return ""
    
    return line1 + "\n" + "="*idx + "^\n" + line2 + "\n"


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the x in that line where the first difference between lines1 and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """    
    if len(lines1) > len(lines2):
        for line in range(len(lines2)):
            itrb = singleline_diff(lines1[line], lines2[line])
            if itrb != IDENTICAL:
                return (line, itrb)
    else:
        for line in range(len(lines1)):
            itrb = singleline_diff(lines1[line], lines2[line])
            if itrb != IDENTICAL:
                return (line, itrb)
    if len(lines1) == len(lines2):
        return (IDENTICAL, IDENTICAL)
    else:
        return (min(len(lines1), len(lines2)), 0)

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    with open(filename, "rt") as file1:
        file_lines = file1.readlines()
    lst_of_lines = []
    for line in file_lines:
        lst_of_lines.append(line.strip())
    return lst_of_lines


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    
    # Turn each file's content into a list of single line
    # string with no newline or return characters.
    f1_lines = get_file_lines(filename1)
    f2_lines = get_file_lines(filename2)
    
    lines_diff = multiline_diff(f1_lines, f2_lines)
    lnidx_diff = lines_diff[0]
    stridx_diff = lines_diff[1]

    fst_line = f1_lines[lnidx_diff]
    sec_line = f2_lines[lnidx_diff]

    #checking for empty files/lines
    is_f1ln_0 = len(f1_lines) == 0
    is_f2ln_0 = len(f2_lines) == 0
    is_bothfi_0 = is_f1ln_0 and is_f2ln_0
    
    if lines_diff == (IDENTICAL, IDENTICAL):
        return "No differences\n"
    else:
        if not is_bothfi_0: 
            return "Line "+str(lnidx_diff)+":\n"+singleline_diff_format(fst_line,sec_line,stridx_diff)
        elif is_f1ln_0:
            return "Line "+str(lnidx_diff)+"+:\n"+fst_line+"\n"+"="*stridx_diff+"^\n"+sec_line+"\n"
        elif is_f2ln_0:
            return "Line "+str(lnidx_diff)+"+:\n"+sec_line+"\n"+"="*stridx_diff+fst_line+"\n^\n\n"
        else:
            lnidx_diff = None
            return "No differences\n"