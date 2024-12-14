import logging
import requests
import time
import os
import urllib3
import sys
from datetime import datetime
# import sslkeylog

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#logging.basicConfig(level=logging.DEBUG)

# requests.packages.urllib3.util.connection.HAS_IPV6 = False
urllib3.util.connection.HAS_IPV6 = False

# sslkeylog.set_keylog("sessionsecrets")

#num of requests in each subprocess
start_idx = 0
end_idx = 10

sleep_time = 1

templogsdir = "templogs"

if not os.path.exists(f"{templogsdir}"):
    os.mkdir(f"{templogsdir}")

process_id = sys.argv[1] if len(sys.argv) >= 2 else 0
f = None

url = "http://localhost:5555/1"
expected_string = "path"

s = requests.Session()

count_errors = 0
ids_errors = []

try:
    for i in range(start_idx, end_idx):
        try:
            now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            f = open(f"{templogsdir}/log-{process_id}.txt", "a")
            parameter = f"{process_id}-{i}"

            start_time = time.perf_counter()
            r = s.request("GET", f"{url}?a={parameter}", verify=False)
            end_time = time.perf_counter()

            elapsed_time = round(end_time-start_time,3)
            print(f"{now} - {parameter} - elapsed_time: {elapsed_time} - \n{r.status_code} {r.text}")
            f.write(f"{now} - {parameter} - elapsed_time: {elapsed_time} - \n{r.status_code} {r.text}\n")
            #print(r.headers['X-Served-By'])
            time.sleep(sleep_time)

            if not expected_string in r.text:
                count_errors += 1
                ids_errors.append(parameter)

        except Exception as e:
            count_errors +=1
            ids_errors.append(parameter)
            print(f"EXCEPTION: {str(e)}")
            f.write(f"EXCEPTION: {str(e)}\n")

    print(f"Process ended {process_id}")
    f.write(f"Process ended {process_id}\n")
    print(f"Errors number: {count_errors}/{i+1} Errors IDs: {ids_errors}")
    f.write(f"Errors number: {count_errors}/{i+1} Errors IDs: {ids_errors}\n")
    f.close()

except KeyboardInterrupt:
    print(f"Process ended {process_id}")
    f.write(f"Process ended {process_id}\n")
    print(f"Errors number: {count_errors}/{i+1} Errors IDs: {ids_errors}")
    f.write(f"Errors number: {count_errors}/{i+1} Errors IDs: {ids_errors}\n")
    f.close()