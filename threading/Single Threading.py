# thread = flow of execution.
#          A thread can be visualized its own separate stream instruction execution.
#          Each thread takes a turn running to achieve concurrency.
#          GIL = (Global Interpreter Lock), allows only on thread to hold the control
#          of the Python interpreter.
#          This thread is known as the "main" thread which all child threads can be spawn.

# TYPES OF TASK EXECUTION:
# CPU Bound Tasks = a computer program that spends most of its time waiting for internal events
#                   (CPU Intensive) computation should use multiprocessing.
#                   Multiprocessing is the concept of splitting a computer program into
#                   multiple processes to be run on different CPU cores.

# IO Bound Tasks =  a computer program that spends most of its time waiting for external events
#                   (user input, webscraping) should use multithreading.
#                   Multithreading is the concept of splitting a computer program to run
#                   within multiple spawn threads (streams of execution)


import threading
import time


# The following functions will all be executed sequentially on the main thread.
# This is an example of running excuted instructions on a single thread.


def warm_up():
    time.sleep(2)
    print("Warming up before the hockey game...")


def play_game():
    time.sleep(4)
    print("Playing the hockey game...")


def get_changed():
    time.sleep(6)
    print("Getting changed after the hockey game...")


def go_home():
    time.sleep(8)
    print("Going home to rest after the hockey game...")
    time.sleep(1)


warm_up()
play_game()
get_changed()
go_home()

# Active thread count.
print("Active Thread Count:")
print(threading.enumerate())
print(threading.active_count())


print("\n")

# Each function gets triggered in sequence within the main thread. The sleep timer was evoked.
# to demonstrate that each function is executed and processed one at a time on the main thread.


