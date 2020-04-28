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

# gets mouse click input
def on_click(x, y, button, pressed):
	currTime = datetime.now()
	f.write("mouse_click," + currTime.strftime('%Y-%m-%d %H:%M:%S,') + activeWindow + "\n")
	f.flush()

# gets keyboard input on key depress
def on_press(key):
	currTime = datetime.now()
	f.write("key_press," + currTime.strftime('%Y-%m-%d %H:%M:%S,') + activeWindow + "\n")
	f.flush()

# starts the on_click and on_press input listeners
def start_listeners():
	mouseListener = mouse.Listener(on_click=on_click)
	keyboardListener = keyboard.Listener(on_press=on_press)
	mouseListener.start()
	keyboardListener.start()

# returns the active window title
def get_active_window():
	currWindow = gw.getActiveWindow()
	if currWindow == None:
		return "Windows"
	#elif currWindow.title == "":
	#	return "None"
	elif currWindow._hWnd not in apps:
		title = parse_title(currWindow.title)
		apps[currWindow._hWnd] = title
	
	return apps[currWindow._hWnd]

# parses a window title for keyword and returns it (checks after the last '-' character)
def parse_title(title):
	splitList = title.split('- ')
	keyWord = splitList.pop()
	print(keyWord)
	return(keyWord)

if __name__ == "__main__":
	# creating and setting up CSV
	dataFile = 'activity_data.csv'
	f = open(dataFile, 'w')
	f.write('ACTION,TIME,APPLICATION\n')
	f.flush()

	# setting up for tracking the active window
	activeWindow = 'None'
	apps = {}
	start_listeners()
	
	while True:
		time.sleep(1)
		activeWindow = get_active_window()

	f.close()