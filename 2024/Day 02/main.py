def get_reports(file_location):
    """Gives a list of lists where each sub-list is a report"""
    reports = []
    with open(file_location, "r") as file:
        for line in file:
            reports.append(line.split())

    print(reports)
    return reports


def is_safe(report):
    """Checks if a report is safe"""
    return True


def total_true(reports_results):
    """Totals the number of elements that are True"""
    count = 0
    return count


def main():
    reports = get_reports("2024\Day 02\challenge_input.txt")
    reports_results = []
    for report in reports:
        reports_results.append(is_safe(report))
    safe_reports = total_true(reports_results)

    print(f"Safe Reports: {safe_reports}")
    return


main()
