import socket, threading
<<<<<<< HEAD
import signal
import sys

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        socket.close()
        sys.exit(0)
=======
import time
from neopixel import *

>>>>>>> 604cd56222e5f7accb487ce0d5b5f1afbbb48792

HOST = '0.0.0.0'
PORT = 51234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)
clients = [] #list of clients connected
lock = threading.Lock()



board_height=11
board_width=11

# LED strip configuration:
LED_COUNT      = board_height*board_width      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP = ws.WS2811_STRIP_GRB # Strip type and colour ordering

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()

def chunkstring(string, length):
    return list(string[0+i:length+i] for i in range(0, len(string), length))


class chatServer(threading.Thread):
    def __init__(self, (socket,address)):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address= address

    def run(self):
        lock.acquire()
        clients.append(self)
        lock.release()
        print '%s:%s connected.' % self.address
        while True:
            readline = self.socket.makefile().readline

            try:
                while self.socket:
                    for i in range(10):
                        line = readline(1024).strip()
                        if not line:
                            break
                        arguments = line.split()
                        #print arguments
                        if arguments[0].upper() == "PX":
                            #print "accepted"
                            positie = (int(arguments[2]))*11+int(arguments[1])
                            kleuren = chunkstring(arguments[3],2)
                            #print kleuren
                            strip.setPixelColor(positie, Color(int(kleuren[0],16), int(kleuren[1],16), int(kleuren[2],16)))
                            strip.show()
            finally:
                pass
            if not data:
                break
            for c in clients:
                c.socket.send(data)
        self.socket.close()
        print '%s:%s disconnected.' % self.address
        lock.acquire()
        clients.remove(self)
        lock.release()

while True: # wait for socket to connect
    # send socket to chatserver and start monitoring
    chatServer(s.accept()).start()
