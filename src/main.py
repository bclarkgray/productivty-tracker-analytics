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
	
	global tab
	activeWindow = get_active_window()
	currTime = datetime.now()
	f.write("mouse_click," + currTime.strftime('%Y-%m-%d %H:%M:%S,') + activeWindow + ',' + category + ',' + tab + '\n')
	f.flush()
	
	tab = ''
	#time.sleep(.1)

# gets keyboard input on key depress
def on_press(key):
	global tab
	activeWindow = get_active_window()
	currTime = datetime.now()
	f.write("key_press," + currTime.strftime('%Y-%m-%d %H:%M:%S,') + activeWindow + ',' + category + ',' + tab + '\n')
	f.flush()
	tab = ''
	time.sleep(.1)

# starts the on_click and on_press input listeners
def start_listeners():
	mouseListener = mouse.Listener(on_click=on_click)
	keyboardListener = keyboard.Listener(on_press=on_press)
	mouseListener.start()
	keyboardListener.start()

# returns the active window title
def get_active_window():
	global category
	currWindow = gw.getActiveWindow()
	if currWindow == None:
		return "Windows"
	elif currWindow.title == '':
		return 'Windows'
	elif currWindow._hWnd not in apps:
		title = parse_title(currWindow.title)
		apps[currWindow._hWnd] = title
	
	title = apps[currWindow._hWnd]

	if title in categories:
		category = categories[title]

	return title

# parses a window title for keyword and returns it (checks after the last '-' character)
def parse_title(title):
	global tab
	splitList = title.split('- ')
	keyWord = splitList.pop()
	print(keyWord)
	
	print(splitList)
	'''
	if keyWord == 'Google Chrome' or 'Firefox':
		if splitList:
			sp = splitList.pop()
			if sp == 'Gmail ':
				print("tab got tripped")
				tab = 'Gmail'
			#else:
				#tab = ''
			if sp in tabs:
				tab = sp
				print("tab set to " + tab)
			else:
				tab = ''
		else:
			tab = ''
			'''
	return(keyWord)

category = ''
tab = ''

categories = {
	'Visual Studio Code': 'Work', 
	'Google Chrome': 'Browsing',
	'Firefox': 'Browsing',
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
	'Stack Overflow',
	'Gmail ',
	'Twitter ',
	'Facebook ',
	'LinkedIn ',
	'Reddit ',
	'GeeksForGeeks '
]

if __name__ == "__main__":
	# creating and setting up CSV
	dataFile = 'activity_data.csv'
	f = open(dataFile, 'w')
	f.write('ACTION,TIME,APPLICATION,CATEGORY,TAB\n')
	f.flush()

	# setting up for tracking the active window
	activeWindow = 'None'
	apps = {}
	start_listeners()
	
	while True:
		pass
	f.close()