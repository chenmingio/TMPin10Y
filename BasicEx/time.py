import time


def show_name(function, result):
    print(f"function: {function}, result: {result}")


# time.clock() is process time, which is according to system function...

show_name("time.clock", time.clock())

# time.time() is epoche time, seconds since begin of 1970.

show_name("time.time", time.time())

# time.ctime(sec) transfer epoche time below to readable string.(local time).
# with () it will take current time using time.time.

show_name("time.ctime()", time.ctime())

# time.gmtime transfer a epoche time to UTC time

show_name("time.gmtime()", time.gmtime())

# time.localtime transfer UTC time above to localtime.

show_name("time.localtime()", time.localtime())

# mktime Make More Time.

# time.strftime convert time structure to format you need.
