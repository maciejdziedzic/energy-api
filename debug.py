from prometheus_client import start_http_server, Counter, Summary
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds',
                       'Time spent processing request')
c = Counter('my_requests_total', 'Total number of requests')

# Decorate function with metric.


@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


start_http_server(8000)  # Choose a port that isn't already in use
while True:
    process_request(random.random())
    c.inc()
