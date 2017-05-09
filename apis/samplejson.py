Services { 
{'id': 2, 
'created': '2013-01-29T12:34:56.000000Z', 
'name': 'thermostat',
'defaultconfig':'{
  "thermostat:": {
    "defaultMode:default": {},
    "maxErrors:3": {},
    "modes:": {
      "default:": {
        "high:80": {},
        "low:69": {}
      },
      "night:": {
        "high:80": {},
        "low:65": {}
      }
    },
    "overshoot:2 # degrees of unitPreference": {},
    "pollInterval:1m # minutes": {},
    "minFan:5m # minutes/hour": {},
    "schedule:": {},
    "-days:": {
      "-1": {},
      "-2": {},
      "-3": {},
      "-4": {},
      "-5": {},
      "end:7:00AM": {},
      "mode:night": {},
      "start:12:01AM": {},
      "end:12:00AM": {},
      "start:11:00PM": {}
    },
    "unitPreference:Fahrenheit": {}
  },
  "controller:": {
    "pins:": {
      "fan:21": {},
      "cool:20": {},
      "heat:16": {}
    }
  },
  "thermometer:": {
    "type:remote": {},
    "endpoint:http://pi2/temperature": {}
  },
  "serveAt:\"127.0.0.1:9000\"": {}
}' 
}

Devices {
{'id': 1, 
'created': '2013-01-29T12:34:56.000000Z', 
'name': 'BasementPi',
'type': 'RaspberryPi',
'hostname': 'HomeNetwork6875'
}

HomesServices
{'id': 1, 
'created': '2013-01-29T12:34:56.000000Z', 
'device_Id': '1',
'service_Id': '2',
'active': 'True'
'config': '{
  "thermostat:": {
    "defaultMode:default": {},
    "maxErrors:3": {},
    "modes:": {
      "default:": {
        "high:80": {},
        "low:69": {}
      },
      "night:": {
        "high:80": {},
        "low:65": {}
      }
    },
    "overshoot:2 # degrees of unitPreference": {},
    "pollInterval:1m # minutes": {},
    "minFan:5m # minutes/hour": {},
    "schedule:": {},
    "-days:": {
      "-1": {},
      "-2": {},
      "-3": {},
      "-4": {},
      "-5": {},
      "end:7:00AM": {},
      "mode:night": {},
      "start:12:01AM": {},
      "end:12:00AM": {},
      "start:11:00PM": {}
    },
    "unitPreference:Fahrenheit": {}
  },
  "controller:": {
    "pins:": {
      "fan:21": {},
      "cool:20": {},
      "heat:16": {}
    }
  },
  "thermometer:": {
    "type:remote": {},
    "endpoint:http://pi2/temperature": {}
  },
  "serveAt:\"127.0.0.1:9000\"": {}
}'
}