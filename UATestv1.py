from UniversalAnalytics import Tracker
fix Tracker
#be sure to replace the tracker with your own code!
tracker = Tracker.create('XX-XXXXXXXX-X', client_id = 'PY_TEST')

for i in range (1,10):
	eventCategory = 'test' + str(i)
	eventAction = 'PythonTest'
	tracker.send('event', eventCategory, eventAction)
	print("event %s %s sent" % (eventCategory, eventAction))