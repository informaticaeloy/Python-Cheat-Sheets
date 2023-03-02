### Este script genera fechas en formato UNIX. Los datos de fechas del registro de windows se guardan en este formato
from datetime import datetime, timezone, timedelta
import time

print(datetime.now(timezone.utc).isoformat(timespec='microseconds', sep=' ', ))

print( time.time() )

from datetime import datetime
print("Ahora:",datetime.utcnow())
date= datetime.utcnow() + timedelta(days=1)
date = date - datetime(1601, 1, 1)
print("Número de días desde epoch:",date)
seconds =(date.total_seconds())
milliseconds = round(seconds*10000000)
print("Milisegundos desde epoch:",milliseconds)

'''
OUTPUT:

2023-03-02 09:31:14.070499+00:00
1677749474.0715039
Ahora: 2023-03-02 09:31:14.071503
Número de días desde epoch: 154193 days, 9:31:14.072509
Milisegundos desde epoch: 133223094740725104 => Nº de milisegundos desde el 1 de enero de 1601

'''
