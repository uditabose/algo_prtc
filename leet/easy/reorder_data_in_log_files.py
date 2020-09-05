#!/usr/local/bin/python3

from typing import List

def reorder_data_in_log_files(logs: List[str]) -> List[str]:
    """
    https://leetcode.com/problems/reorder-data-in-log-files/

    Time :
    Space:
    Note :
    """

    if len(logs) < 2:
        return logs

    dig_logs = []
    let_logs = []

    for log in logs:
        if log.startswith("let"):
            let_logs.append(log)
        else:
            dig_logs.append(log)

    formatted_logs = sorted(let_logs, key = lambda log: log.split()[1:]) + dig_logs
    return formatted_logs


def run():
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print(reorder_data_in_log_files(logs))


if __name__ == '__main__':
    run()
