from ssg import hooks
import time

start_time = None
total_written = 0

@hooks.register("start_builder")
def start_build():
    global start_time
    start_time = time.ctime

@hooks.register("written")
def wtirren():
    global total_written
    total_written += 1

@hooks.register("stats")
def stats():
    final_time = time.ctime - start_time
    average = final_time / total_written