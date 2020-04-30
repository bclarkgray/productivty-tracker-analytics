from pynput import mouse, keyboard
from datetime import datetime
import time
import pygetwindow as gw

# gets mouse click input
def on_click(x, y, button, pressed):
	activeWindow = Window()
	get_active_window(activeWindow)

	currTime = datetime.now()
	f.write("mouse_click," + currTime.strftime('%Y-%m-%d %H:%M:%S,') + activeWindow.title + ',' + activeWindow.category + ',' + activeWindow.tab + '\n')
	f.flush()


# gets keyboard input on key depress
def on_press(key):
	activeWindow = Window()
	get_active_window(activeWindow)

	currTime = datetime.now()
	f.write("key_press," + currTime.strftime('%Y-%m-%d %H:%M:%S,') + activeWindow.title + ',' + activeWindow.category + ',' + activeWindow.tab + '\n')
	f.flush()

# starts the on_click and on_press input listeners
def start_listeners():
	mouseListener = mouse.Listener(on_click=on_click)
	keyboardListener = keyboard.Listener(on_press=on_press)
	mouseListener.start()
	keyboardListener.start()

# returns the active window title
def get_active_window(window):
	currWindow = gw.getActiveWindow()
	if currWindow == None or currWindow.title == '':
		window.category = 'Unclassified'
		window.title = 'Windows'
		return
	elif currWindow._hWnd not in apps:
		window.title = parse_title(currWindow, window)
		apps[currWindow._hWnd] = window.title
	else:
		window.title = parse_title(currWindow, window)

	window.title = apps[currWindow._hWnd]

	if window.title in categories:
		window.category = categories[window.title]
	else:
		window.category = 'Unclassified'

	return

# parses a window title for keyword and returns it (checks after the last '-' character)
def parse_title(currWindow, window):
	splitList = currWindow.title.split('- ')
	keyWord = splitList.pop()

	if keyWord == 'Google Chrome' or keyWord == 'Firefox':
		parse_tab(currWindow, splitList, window)

	return keyWord


def parse_tab(currWindow, splitList, window):
	if splitList:
			sp = splitList.pop()
			if sp in tabs:
				window.tab = sp
			else:
				window.tab = 'Unclassified'


categories = {
	'Visual Studio Code': 'Work', 
	'Google Chrome': 'Browsing',
	'Firefox': 'Browsing',
	'Mozilla Firefox': 'Browsing',
	'Discord': 'Leisure',
	'Windows PowerShell': 'Work',
	'Spotify Premium': 'Leisure',
	'Word': 'Work',
	'Steam': 'Leisure',
	'Epic Games Launcher': 'Leisure',
	'Github Desktop': 'Work'
	}

tabs = [
	'YouTube ',
	'Stack Overflow ',
	'Gmail ',
	'Twitter ',
	'Facebook ',
	'LinkedIn ',
	'Reddit ',
	'GeeksforGeeks '
]

class Window:
	def __init__(self):
		self._title = ''
		self._category = ''
		self._tab = 'Unclassified'

	@property
	def title(self):
		return self._title
	
	@title.setter
	def title(self, x):
		self._title = x

	@property
	def category(self):
		return self._category
	
	@category.setter
	def category(self, x):
		self._category = x

	@property
	def tab(self):
		return self._tab
	
	@tab.setter
	def tab(self, x):
		self._tab = x


if __name__ == "__main__":
	# creating and setting up CSV
	dataFile = 'activity_data.csv'
	f = open(dataFile, 'w')
	f.write('ACTION,TIME,APPLICATION,CATEGORY,TAB\n')
	f.flush()

	# setting up for tracking the active window
	apps = {}
	start_listeners()

	while True:
		pass
	f.close()