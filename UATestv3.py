import sys
from UniversalAnalytics import Tracker

# be sure to replace the tracker with your own code!
tracker = Tracker.create('XX-XXX-X', client_id='PY_TEST')

for i in range(1, 10):
	eventCategory = 'test' + sys.argv[1]
	eventAction = 'PythonTest'
	tracker.send('event', eventCategory, eventAction)
	print("event %s %s sent" % (eventCategory, eventAction))
