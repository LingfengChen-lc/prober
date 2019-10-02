import requests
import time
import sys

def record(URL,out_file):
    response = requests.get(URL,timeout=30)
    # successfully responde
    with open(out_file, 'a') as f:
        if response.status_code:
            f.write(f'{int(time.time())},{response.status_code}\n')

def main():
    # ensure length of arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python prober.py <URL> <output_file>")
    #ensure URL is valid, sample url: http://www.cs.nyu.edu
    URL = sys.argv[1]
    if URL.startswith("www."):
        sys.exit("Invalid URL, maybe you mean http://" + URL)
    if not (URL.startswith("http://") or URL.startswith("https://")):
        sys.exit("Invalid URL")
    out_file = sys.argv[2]
    issue_interval = 30
    f = open(out_file, 'w')
    f.write(f'URL={URL}\n')
    f.close()
    time_limit = time.time() + issue_interval
    while True:
        try:
            record(URL,out_file)
        # if timeout, immediately continue next iteration
        except requests.exceptions.RequestException:
            with open(out_file, 'a') as f:
                f.write(f'{int(time.time())},-1\n')
        # if success, then sleep to the time_limit
        sleep_time = time_limit - time.time()
        time.sleep(sleep_time)
        time_limit = time.time() + issue_interval

main()

