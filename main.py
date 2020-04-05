from pynput import mouse, keyboard
from datetime import datetime
import time
import pygetwindow as gw
#IF THIS FAILS WE USE WIN32 YIKERS

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

def start_listeners():
	mouseListener = mouse.Listener(on_click=on_click)
	keyboardListener = keyboard.Listener(on_press=on_press)
	mouseListener.start()
	keyboardListener.start()

def get_active_window():
	currWindow = gw.getActiveWindow()

	flag = False
	for window in windows:
		if (currWindow == window):
			print(window.title)
			flag = True
			break
	if (flag == False):
		print(currWindow.title)
		windows.append(currWindow)
	




if __name__ == "__main__":
	
	f = open("log.txt", "w")
	f.write("ACTION, TIME\n")

	start_listeners()

	time.sleep(3)
	
	windows = []
	while True:
		time.sleep(2)
		get_active_window()

	f.close()