# Daemon Thread = a low-priority thread that runs in the background to perform tasks
# such as long-running processes, garbage collection, background tasks, etc.
# Daemon threads will be killed once the main thread that has spawned it has completed
# executing its instructions. The main thread will not wait for the Daemon thread to
# complete executing its own instructions.

# Non-daemon threads are threads will continue to stay alive until their instructions have completed
# executing. Threads that are spawned are by default a non-daemon thread unless
# explicitly specified.

import threading
import time

# For our example, we will create a function timer() that will run in an infinite loop.


def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, "seconds")

# We will spawn a child thread to execute the timer() function.
# If we set the daemon parameter to True, we will spawn it as a daemon thread,
# which will cause it to be terminated once the main thread that spawned it
# has completed the execution of its instructions - in this case,
# the user input() function. It will terminate even though it is set to run as
# and infinite loop.


thread_1 = threading.Thread(target=timer, daemon=True)
thread_1.start()

# If we replace the above thread with the one below which does not contain the
# daemon=True parameter, the thread will be spawned as a non-daemon thread and will
# continue to run in an infinite loop even when the main thread has finished executing
# the user input() function.

"""
thread_2 = threading.Thread(target=timer)
thread_2.start()
"""

# Press the "enter" kay to exit the input() function.
answer = input("Do you wish to exit?\n")

# The input() function (running on the main thread) will wait for keyboard input
# and then will subsequently exit, which will terminate any daemon threads spawned from it.

# If the child thread spawned from the main thread was a non-daemon thread, the main thread will
# "hang" until the child thread has completed execution, which in this case will be never since
# it will be running in an infinite loop.

# NOTE: Even in an infinite loop you can press the "stop" button in the terminal which
# will send a forced kill signal to the running program.





