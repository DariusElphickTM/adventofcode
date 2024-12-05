"""Module providing functions for processing safety reports."""

import re

def main() -> None:
    """Main Function."""
    reports = read_file("1.txt")
    safe_reports = process_reports(reports)
    print("Safe reports:", safe_reports.count(True))

def process_reports(reports):
    """Processes a list of reports and returns whether they're safe."""
    return list(map(check_safety, reports))

def check_safety(report, use_dampner = True):
    """Processes a single report and returns whether it's safe."""
    report_values = list(map(int, re.findall(r'\d+', report)))
    is_safe = check_the_levels(report_values)
    if not is_safe and use_dampner:
        return check_safety_with_dampner(report_values)
    else:
        return is_safe
    
def check_the_levels(report_values):
    is_safe = True
    is_report_ascending = True
    for i in range(len(report_values) - 1):
        current_diff = report_values[i + 1] - report_values[i]
        if(abs(current_diff) < 1 or abs(current_diff) > 3):
            is_safe = False
            break
        is_report_currently_ascending = current_diff > 0
        if i == 0:
            is_report_ascending = is_report_currently_ascending
        else:
            is_safe = is_report_ascending == is_report_currently_ascending
            if not is_safe:
                break
    return is_safe

def check_safety_with_dampner(report_values):
    """Processes a single report and returns whether it's safe, using the dampner."""
    for i in range(len(report_values)):
        report_values_copy = report_values.copy()
        report_values_copy.pop(i)
        is_safe = check_the_levels(report_values_copy)
        if is_safe:
            return is_safe
    return False

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.readlines()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()