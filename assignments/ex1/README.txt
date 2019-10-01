TODO: Describe how to build your prober.
By using the Python requests module, I can keep issuing HTTP/1.1 get requests.
And by the python decorator timeout_decorator and time.sleep() function I put the request time limit to 30 seconds and if
request success with returned HTTP status_code between 200-400, the prober would wait up the rest 30 seconds
before issue another request. And if returned status_code other than 200-400, the prober will write
status_code as -1 to indicate a failure.

TODO: Describe how to run your prober.
python prober.py <URL> <output_file>

TODO: Describe how you prober handles HTTP redirects.
It will follow the redirects to the ultimate site and report the response from that
URL(return 200 if success) I tested that it will follow redirects.
