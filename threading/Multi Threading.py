import threading

# MULTITHREADING:


def listening_to_music(music):
    print(f"Listening to music by {music}...\n")


def studying(exam):
    print(f"Studying for the {exam} exam...\n")


def sip_coffee(coffee):
    print(f"Sipping on the {coffee} coffee..\n")


# The main thread will spawn three child threads responsible for execution their
# own instructions

print("Multithreading Functions:\n")
thread_1 = threading.Thread(target=listening_to_music, args=("Bach",))
thread_1.start()

thread_2 = threading.Thread(target=studying, args=("Science",))
thread_2.start()

thread_3 = threading.Thread(target=sip_coffee, args=("Belgian",))
thread_3.start()

# The "join" method synchronizes the running thread which will cause the main thread to wait
# until the child threads are done executing before resuming.

thread_1.join()
thread_2.join()
thread_3.join()

print(threading.enumerate())
print(threading.active_count())