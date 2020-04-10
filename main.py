from pynput import mouse, keyboard
from datetime import datetime
import time
import pygetwindow as gw

#def on_move(x, y):
#	currTime = datetime.now()
#	f.write("mouse_move, " + currTime.strftime('%Y-%m-%d %H:%M:%S') + "\n")

#def on_scroll(x, y, dx, dy):
#	currTime = datetime.now()
#	f.write("mouse_scroll," + currTime.strftime('%Y-%m-%d %H:%M:%S') + "\n")
	
def on_click(x, y, button, pressed):
	currTime = datetime.now()
	f.write("mouse_click," + currTime.strftime('%Y-%m-%d %H:%M:%S,') + activeWindow + "\n")
	f.flush()

def on_press(key):
	currTime = datetime.now()
	f.write("keypress," + currTime.strftime('%Y-%m-%d %H:%M:%S,') + activeWindow + "\n")
	f.flush()

def start_listeners():
	mouseListener = mouse.Listener(on_click=on_click)
	keyboardListener = keyboard.Listener(on_press=on_press)
	mouseListener.start()
	keyboardListener.start()

# returns the active window title
def get_active_window():
	currWindow = gw.getActiveWindow()
	if currWindow.title == "":
		return "None"
	elif currWindow._hWnd not in apps:
		apps[currWindow._hWnd] = currWindow.title
	
	return apps[currWindow._hWnd]

if __name__ == "__main__":
	
	f = open("activity_data.csv", "w")
	f.write("ACTION, TIME, APPLICATION\n")

	activeWindow = None
	apps = {}
	start_listeners()
	
	while True:
		time.sleep(.5)
		activeWindow = get_active_window()

	f.close()