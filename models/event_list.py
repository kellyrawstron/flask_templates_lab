from models.event import *


event1 = Event("20/02/2022", "Pottery Class", "2", "unicorn room", "Make your own bowl, woo!")
event2 = Event("21/02/2020", "Metallica concert", "6", "lion room", "Heavy Metal concert")
events = [event1, event2]

def add_new_event(event):
    events.append(event)