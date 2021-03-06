import threading
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join() # complete the running thread
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

# Finished in 0.0 second(s) 라고 뜬 후 Done Sleeping... 이 프린트됨
# reason : while the tread is for sleeping, our script ran concurrently and continued on with the rest of the script