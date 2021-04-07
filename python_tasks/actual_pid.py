"""
Task 4
We took a little look on os module. Write a small script which will print a
string using all the types of string formatting which were considered during the
lecture with the following context: This script has the following PID:
<ACTUAL_PID_HERE>. It was ran by <ACTUAL_USERNAME_HERE> to work happily on
<ACTUAL_OS_NAME>-<ACTUAL_OS_RELEASE>.
"""


import os


def main():
    actual_pid = os.getpid()
    user_name = os.getlogin()
    os_name = os.uname().sysname
    # os_name = os.name
    os_release = os.uname().release

    print('This script has the following PID: %s. It was ran by %s to work happily on %s - %s' % (actual_pid, user_name,
                                                                                               os_name, os_release))

    print("This script has the following PID: {}. It was ran by {} to work happily on {} - {}".format(actual_pid,
                                                                                    user_name, os_name, os_release))

    print("This script has the following PID: {0}. It was ran by {2} to work happily on {1} - {3}".format(actual_pid,
                                                                                    os_name, user_name, os_release))

    print(f"This script has the following PID: {actual_pid}. It was ran by {user_name} to work happily on {os_name} - "
      f"{os_release}")


main()
