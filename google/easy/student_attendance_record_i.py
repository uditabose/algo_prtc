
def student_attendance_record_i(attendance):
    '''
    You are given a string representing an attendance record 
    for a student. The record only contains the following three 
    characters:
    'A' : Absent.
    'L' : Late.
    'P' : Present.
    A student could be rewarded if his attendance record 
    doesn't contain more than one 'A' (absent) or more than 
    two continuous 'L' (late).

    You need to return whether the student could be rewarded 
    according to his attendance record.

    Example 1:
    Input: "PPALLP"
    Output: True
    
    Example 2:
    Input: "PPALLL"
    Output: False

    https://leetcode.com/problems/student-attendance-record-i/description/

    Time : O(N)
    Space: O(1)
    Note :
    1. check for index of `LL`
    2. check for index of `A`
    '''
    if attendance == None or len(attendance) == 0:
        return False

    if attendance.count('A') > 1 or 'LLL' in attendance:
        return False
    else:
        return True
    

def run():
    print("%s" % str(student_attendance_record_i("PPALLP")))
    print("%s" % str(student_attendance_record_i("PPALLL")))

if __name__ == '__main__':
    run()

