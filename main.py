from pynput import mouse, keyboard
from datetime import datetime
import time
#import wnck  <-- this should let me track window IDs or something like that


#def on_move(x, y):
#	currTime = datetime.now()
#	f.write("mouse_move, " + currTime.strftime('%Y-%m-%d %H:%M:%S') + "\n")

#def on_scroll(x, y, dx, dy):
#	currTime = datetime.now()
#	f.write("mouse_scroll," + currTime.strftime('%Y-%m-%d %H:%M:%S') + "\n")
	
def on_click(x, y, button, pressed):
	currTime = datetime.now()
	f.write("mouse_click," + currTime.strftime('%Y-%m-%d %H:%M:%S') + "\n")

def on_press(key):
	currTime = datetime.now()
	f.write("keypress," + currTime.strftime('%Y-%m-%d %H:%M:%S') + "\n")

#Old blocking version
'''with mouse.Listener(on_click=on_click) as listener:
	with keyboard.Listener(on_press=on_press) as listener:
		listener.join()
'''

if __name__ == "__main__":
	
	f = open("log.txt", "w")
	f.write("ACTION, TIME\n")

	mouseListener = mouse.Listener(on_click=on_click)
	keyboardListener = keyboard.Listener(on_press=on_press)
	mouseListener.start()
	keyboardListener.start()


	time.sleep(10)

	f.close()