from datetime import datetime, timezone
import time

### Print right now time and date in format windows registry (1601-01-01 00:00:00+00:00 or 2023-02-27 13:20:39.153328+00:00)
print(datetime.now(timezone.utc).isoformat(timespec='microseconds', sep=' ', ))

### Print right now time and date in format Unix
print( time.time() )


### OUTPUT#########################
# >>> 2023-02-27 13:20:39.153328+00:00
# >>> 1677504039.1533284
