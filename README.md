# HTTP Keepalive

## HTTP Traffic Generator

1. Update HTTPkeepalive.py with the required URL, expected return string and num of requests in each subprocess
2. Update HTTPkeepalive_loop.py with the num of subprocesses to run
3. python HTTPkeepalive_loop.py
4. The loop is running X TCP connections and in each connection is running Y HTTP requests (keepalive) with a specific interval
5. Each HTTP request is appended with a parameter with the unique value of process_id and request_id to track in logs or sniffers
6. The results are saved in a log file
7. Summary of errors per subprocess on program exit


