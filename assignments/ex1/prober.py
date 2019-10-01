# write a prober program
import requests
import time
import sys

def record(URL,f):
    response = requests.get(URL,timeout=30)
    # successfully responde
    if response:
        f.write(f'{int(time.time())},{response.status_code}\n')
    else:
        f.write(f'{int(time.time())},-1\n')
    time.sleep(2)

def main():
    # ensure length of arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python prober.py <URL> <output_file>")
    #sample url: http://www.cs.nyu.edu
    URL = sys.argv[1]
    out_file = sys.argv[2]
    with open(out_file, 'w') as f:
        f.write(f'URL={URL}\n')
        while True:
            try:
                record(URL,f)
            except TimeoutError:
                continue

main()