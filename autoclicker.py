import threading

from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
from time import sleep

mouse = Controller()

class Autoclicker(threading.Thread):
	def __init__(self, delay=0.01):
		# inherit Thread properties
		super(Autoclicker, self).__init__()
		self.delay = delay
		self.running = False
		self.program_running = True

	def start_clicking(self):
		self.running = True

	def stop_clicking(self):
		self.running= False

	def run(self):
		while self.program_running:
			while self.running:
				mouse.click(Button.left)
				sleep(self.delay)
			sleep(0.05)

	def exit(self):
		self.stop_clicking()
		self.program_running = False


click_thread = Autoclicker(delay=0.001)
click_thread.start()

def handle_key():
    pass

def on_press(key):
	if key == Key.alt_r:
		print(f"click_thread.running = {click_thread.running}")
		if click_thread.running:
			click_thread.stop_clicking()
			print("stopping")
		else:
			click_thread.start_clicking()
			print("starting")
	if key == Key.esc:
		click_thread.exit()
		exit()

with Listener(on_press=on_press) as listener:
	listener.join()
