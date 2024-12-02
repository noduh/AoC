##########
# Part 2 #
##########


def get_reports(file_location: str):
    """Gives a list of lists where each sub-list is a report"""
    reports = []
    with open(file_location, "r") as file:
        for line in file:
            reports.append(line.split())

    return reports


def is_safe(full_report: list):
    """Checks if a report is safe"""
    ascending = None
    for n in range(len(full_report)):
        report = full_report[:] # make a copy instead of passing reference
        report.pop(n)

        for i in range(1, len(report)):
            # Determine order if it hasn't been determined
            distance = int(report[i]) - int(report[i - 1])
            if ascending == None:
                if distance > 0:
                    ascending = True
                elif distance < 0:
                    ascending = False

            # Case if it's ascending
            if ascending:
                if distance < 3 or distance > 1:
                    return True

            # Case if it's descending
            else:
                if distance > -3 and distance < -1:
                    return True
    return False


def total_true(reports_results: list):
    """Totals the number of elements that are True"""
    count = 0
    for result in reports_results:
        if result == True:
            count += 1

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
