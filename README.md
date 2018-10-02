# FlaskLight

A quick and dirty Flask app to control a TP-Link Kasa smart bulb from a web interface

## Q&A
  
-   Doesn't  KASA already have a mobile app and cloud site to do this with?
	 Yes, but that's no fun and I wouldn't get to play with Flask

	 This allows me to access it from any device without installing anything
- Does it really need to be green text on a black background like a bad hacker movie?
	Yes
- How do I use this dang thing?
		Connect the KASA bulb to your wifi using their pesky mobile app
		Change the `bulb = SmartBulb("192.168.1.253")` in app.py to the IP of your bulb
		Run `pip3 install -r requirements.txt`
		Run ./run.sh
		Connect to localhost:8080
		???
		Profit
- How do I find the IP of my bulb?
	Run `pyhs100` with no arguments in a shell after installing the requirements with pip
- Help, I can't access the interface!
	By default Flask runs the dev server bound to 127.0.0.1 (localhost) only, if you're running the app on a different machine locally, you'll need to run `FLASK_APP=app.py flask run -h 0.0.0.0` to bind to all IPs
- Did you make all of these questions up yourself?
Yes
