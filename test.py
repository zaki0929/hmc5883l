import hmc5883l
from time import sleep

sensor = hmc5883l.hmc5883l();

print('[Press CTRL-C to stop]')

try:
    while True:
        (x, y, z) = sensor.axes()
        print('(X, Y, Z) = ({}, {}, {})'.format(x, y, z))
        sleep(0.5)

except KeyboardInterrupt:
    print('\nScript finished')
