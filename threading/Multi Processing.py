# Multiprocessing = running tasks in parallel on different CPU cores.
#                   Bypasses Global Interpreter Lock (GIL) used for multithreading.
#                   Multiprocessing is better for CPU bound (intensive usage) tasks
#                   Multithreading is better for IO bound tasks (waiting on IO subsystem operations)

from multiprocessing import Process, cpu_count
import time

# In this example, we will set a function that will count to 500 million.
# We will run once instance of each function on multiple processes (CPU Cores)
# and analyze the behaviour of the program.


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())
    # The cpu_count() will display how many CPU cores your system has which will
    # determine how many processes can be spawned.

    # We will be executing the counter() function on four different processes.

    a = Process(target=counter, args=(500000000,))
    b = Process(target=counter, args=(500000000,))
    c = Process(target=counter, args=(500000000,))
    d = Process(target=counter, args=(500000000,))

    # Try running a single process first, then two at a time, then three, then four and
    # analysis the length of time it takes for all processes to complete.

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print(f"Instructions completed in: {time.perf_counter()} seconds.")


if __name__ == '__main__':
    main()

'''
The multiprocessing program must be run in the main function to avoid execution errors.

In Python, the role of the main function is to act as the starting point of execution 
for any software program. The execution of the program starts only when the main function 
is defined in Python because the program executes only when it runs directly, 
and if it is imported as a module, then it will not run.

In other words, when all Python modules are packaged together to be run, the main function
identifies where the program execution should start.
'''