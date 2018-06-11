
def task_scheduler(tasks, n):
    '''
    Given a char array representing tasks CPU need to do. 
    It contains capital letters A to Z where different 
    letters represent different tasks.Tasks could be done 
    without original order. Each task could be done in one 
    interval. For each interval, CPU could finish one 
    task or just be idle.

    However, there is a non-negative cooling interval n 
    that means between two same tasks, there must be at 
    least n intervals that CPU are doing different tasks 
    or just be idle.

    You need to return the least number of intervals the 
    CPU will take to finish all the given tasks.
    https://leetcode.com/problems/task-scheduler/description/

    Time : O(N*)
    Space:
    Note :
    '''
    if tasks == None or len(tasks) == 0:
        return 0

    if n == 0:
        return len(tasks)

    task_set = set(tasks)

    if len(task_set) < 2:
        return len(tasks)

    sched_arr = []
    while len(tasks) > 0:
        for x in task_set:
            if x in tasks:
                sched_arr.append(1)
                tasks.remove(x)
        if len(tasks) > 0:
            sched_arr.append(n)


    return sum(sched_arr)


def run():
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(task_scheduler(tasks, n))

    print()
    tasks = ["A","A","A","B","B","B"]
    n = 50
    print(task_scheduler(tasks, n))


if __name__ == '__main__':
    run()

