import wave
import os
import requests

# Use this if you are on your own laptop/desktop and not on the server! Be sure to change path as you need it for your own individual computer

os.system("rec -t raw -c 1 -b 16 -r 8k -e signed-integer - trim 0 3 | nc 35.236.233.51 5050 > ~/Desktop/decode_audio/output.txt")

os.chdir("/")
os.chdir("Users/brianogbebor/Desktop/decode_audio")
os.system("cat output.txt")

with open("/Users/brianogbebor/Desktop/decode_audio/output.txt", "r") as output:
    for line in output:
        pass
    last_line = line  # Last line in the output file which is the complete decoded audio

RASA_URL = "http://35.236.233.51:5005/webhooks/rest/webhook"

info = {"sender": "User", "message": last_line}

print(info)
r = requests.post(url=RASA_URL, json=info)
print(r.status_code)
print(r.text)

# sudo rasa run -m models --enable-api --cors “*” --debug

if "turn on the lights" in r.text:
    ipaddress = "192.168.1.170"
    username = "-HB48KthRyKrIyHbJFv3N335SQ8gGQvxRW85X8Vo"

    try:
        url = "http://" + ipaddress + "/api/" + username + "/lights/1/state"
        # This is the setting for the light to be on
        data_on = {"on": True, "sat": 254, "bri": 254, "hue": 5000}
        r = requests.put(url, json.dumps(data_on), timeout=5)
        print("Turning on the lights")

    except:
        print(
            "Looks like we can't connect with the lights...")

else:
    print("You didn't say it right idiot. Ya snooze ya loose bozo")
