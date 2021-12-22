import sys
import datetime

time = datetime.datetime.now()

output = 'Hola %s, la hora actual es: %s' % (sys.argv[1], time)
print(output)
