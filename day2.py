def report_is_safe(report: str) -> bool:
    """
    Checks wether a report is safe or not.
    A report is a list of numbers separated by a space.

    A report is considered safe when:
     * all numbers are either all increasing or all decreasing.
     * Any two adjacent levels differ by at least one and at most three.

    Args:
        report (str): The report to check.
    """
    levels = list(map(int, report.split(" ")))

    # Make a list of the differences between adjacent levels
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    # Check if differences are all increasing or all decreasing
    all_increasing = all(diff > 0 for diff in differences)
    all_decreasing = all(diff < 0 for diff in differences)

    # Check if differences are between 1 and 3
    valid_differences = all(1 <= abs(diff) <= 3 for diff in differences)

    return (all_increasing or all_decreasing) and valid_differences


def safe_with_dampener(report: str) -> bool:
    """
    Checks if a report is safe by removing one number.
    If running report_is_safe on the report returns True, the report is safe.
    """
    levels = list(map(int, report.split(" ")))

    for i in range(len(levels)):
        new_report = levels[:i] + levels[i + 1 :]
        if report_is_safe(" ".join(map(str, new_report))):
            return True

    return False


def create_reports_from_file(file: str) -> list[str]:
    with open(file, "r") as f:
        return f.readlines()


if __name__ == "__main__":
    safe_reports = 0
    safe_reports_with_dampener = 0
    reports = create_reports_from_file("day2_input.txt")
    for report in reports:
        if safe_with_dampener(report):
            safe_reports_with_dampener += 1
        if report_is_safe(report):
            safe_reports += 1
    print(f"Safe reports: {safe_reports}")
    print(f"Safe report with dapener: {safe_reports_with_dampener}")
