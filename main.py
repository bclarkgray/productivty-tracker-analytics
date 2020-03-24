from pynput import mouse, keyboard
from datetime import datetime

f = open("log.txt", "w")
f.write("ACTION, TIME\n")

#def on_move(x, y):
#	currTime = datetime.now()
#	f.write("mouse_move, " + currTime.strftime('%Y-%m-%d %H:%M:%S') + "\n")
	

def on_click(x, y, button, pressed):
	currTime = datetime.now()
	f.write("mouse_click," + currTime.strftime('%Y-%m-%d %H:%M:%S') + "\n")

#def on_scroll(x, y, dx, dy):
#	currTime = datetime.now()
#	f.write("mouse_scroll," + currTime.strftime('%Y-%m-%d %H:%M:%S') + "\n")

def on_press(key):
	currTime = datetime.now()
	f.write("keypress," + currTime.strftime('%Y-%m-%d %H:%M:%S') + "\n")


#with mouse.Listener(on_move=on_move, on_click=on_click) as mouse_listener:
#	mouse_listener.join()

#with keyboard.Listener(on_press=on_press) as keyboard_listener:
#	keyboard_listener.join()

#mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click)
#mouse_listener.start()

#keyboard_listener = keyboard.Listener(on_press=on_press)
#keyboard_listener.start()

with mouse.Listener(on_click=on_click) as listener:
	with keyboard.Listener(on_press=on_press) as listener:
		listener.join()

f.close()