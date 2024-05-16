from pywiegandpi import WiegandDecoder

data_0_pin = 6
data_1_pin = 5


def callback(value):
    print("Got Wiegand data: {}".format(value))


wiegand_reader = WiegandDecoder(data_0_pin, data_1_pin, callback)

while True:
    # do something else
    pass
