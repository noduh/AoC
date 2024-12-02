def get_reports(file_location):
    """Gives a list of lists where each sub-list is a report"""
    reports = []
    return reports


def is_safe(report):
    return True


def total_true(reports_results):
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
