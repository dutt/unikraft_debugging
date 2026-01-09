import time
from datetime import datetime

ts = time.time()
print(f"time.time() = {ts}")
print(f"datetime    = {datetime.fromtimestamp(ts)}")
print(f"monotonic   = {time.monotonic()}")
