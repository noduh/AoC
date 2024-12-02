##########
# Part 2 #
##########

def get_reports(file_location):
    """Gives a list of lists where each sub-list is a report"""
    reports = []
    with open(file_location, "r") as file:
        for line in file:
            reports.append(line.split())

    return reports


def is_safe(report):
    """Checks if a report is safe"""
    ascending = None
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
            if distance > 3 or distance < 1:
                return False

        # Case if it's descending
        else:
            if distance < -3 or distance > -1:
                return False
    return True


def total_true(reports_results):
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
