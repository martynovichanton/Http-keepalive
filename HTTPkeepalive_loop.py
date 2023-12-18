from subprocess import Popen
import time
import os
import shutil

#num of subprocesses
start_idx = 0
end_idx = 5

sleep_time = 1

templogsdir = "templogs"
logfile = "log.txt"

if not os.path.exists(f"{templogsdir}"):
    os.mkdir(f"{templogsdir}")
    
processes = []

try:
    for i in range(start_idx, end_idx):
        p = Popen(["python3", "HTTPkeepalive.py", f"{i}"])
        processes.append(p)
        time.sleep(sleep_time)

    exit_codes = [p.wait() for p in processes]
    print("Loop ended")
    print(exit_codes)

    #append all logs per process to on file and delete the temp log files
    with open(f"{logfile}","ab") as wfd:
        for f in os.listdir(f"{templogsdir}"):
            with open(f"{templogsdir}/{f}","rb") as fd:
                shutil.copyfileobj(fd, wfd)            
    shutil.rmtree(f"{templogsdir}")

except KeyboardInterrupt:
    exit_codes = [p.wait() for p in processes]
    print("Loop ended")
    print(exit_codes)

    #append all logs per process to on file and delete the temp log files
    with open(f"{logfile}","ab") as wfd:
        for f in os.listdir(f"{templogsdir}"):
            with open(f"{templogsdir}/{f}","rb") as fd:
                shutil.copyfileobj(fd, wfd)            
    shutil.rmtree(f"{templogsdir}")