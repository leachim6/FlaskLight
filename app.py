#!/usr/bin/env python3
from flask import Flask
from flask import jsonify
from flask import request
from pyHS100 import SmartBulb
bulb = SmartBulb("192.168.1.253")

app = Flask(__name__)

@app.route("/")
def index():
    return '''
<html>

  <head>
    <title> Turn the lights on/off </title>
  </head>
  <style type="text/css">
  body{
  background:#000;
  color:#00FF00;
 }

 .spacer{
 margin:20px;
 }
  </style>

  <body style="float:left;">
    <h1> Control the desk lamp </h1>
    <form id="controls" style="text-align:center;">
      <button name="on" type="button">On</button>
      <button name="off" type="button">Off</button>
      <div class="spacer"></div>
      <button name="bright25" type="button">25%</button>
      <button name="bright50" type="button">50%</button>
      <button name="bright75" type="button">75%</button>
      <button name="bright100" type="button">100%</button>
      <div class="spacer"></div>
      <label for="brightnessValue">Brightness:</label>
      <div class="spacer"></div>
      <input type="range" id="brightnessValue" name="brightnessValue" min="1" max="100 step="10" />
    </form>
    <div id="state" style="text-align:center;">
      <h2> The light is currently</h2>
      <div id="lightstate"></div>
    </div>
    
    <script>
     var form = document.getElementById('controls');
     var lightstate = document.getElementById('lightstate');  
     function updateLightState(){
      fetch('/lightState').then(r => r.json()).then(o => lightstate.innerHTML = "<b style='color:red;'>"+o.state+"</b>" + " at Brightness: " +  o.brightness +"%");
      }
      function setLightBright(brightness){
      fetch('/brightness?brightness='+brightness);
      }
     form.on.onclick = e => {
      	console.log('Light has been turned on');
        fetch('/lightOn').then(r => r.json()).then(console.log);
        updateLightState();
      }
      form.off.onclick = e => {
      	console.log('Light has been turned off');
        fetch('/lightOff').then(r => r.json()).then(console.log);
        updateLightState();
      }
      form.bright25.onclick = e => {
      	console.log('Light has been set to 25% brightness');
        setLightBright(brightness=25);
        updateLightState();
      }
      form.bright50.onclick = e => {
      	console.log('Light has been set to 50% brightness');
        setLightBright(brightness=50);
        updateLightState();
      }
      form.bright75.onclick = e => {
      	console.log('Light has been set to 75% brightness');
        setLightBright(brightness=75);
        updateLightState();
      }
      form.bright100.onclick = e => {
      	console.log('Light has been set to 100% brightness');
        setLightBright(brightness=100);
        updateLightState();
      }
      
      form.brightnessValue.onchange = e => { 
      console.log(e.target.value);
      setLightBright(brightness=e.target.value);
      updateLightState();
      };
      updateLightState();
    </script>
  </body>

</html>
'''

@app.route("/lightOn")
def lightOn():
    bulb.turn_on()
    return jsonify(state=bulb.state)

@app.route("/lightOff")
def lightOff():
    bulb.turn_off()
    return jsonify(state=bulb.state)

@app.route("/lightState")
def lightState():
    return jsonify(state=bulb.state,brightness=bulb.brightness)

@app.route("/brightness")
def lightSetBright():
    brightness = request.args.get('brightness', default = 100, type = int)
    bulb.brightness = brightness
    return jsonify(brightness=bulb.brightness)
