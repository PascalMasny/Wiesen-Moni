# Wiesen WebMoni Bot 🍻

## Usage
A web monitor who monitors the websites of the 2022 Oktoberfet marquee's.
Ein Web Monitor der die Wiesen Festzelt Websiten (Hacker, Auguster, Paulaner) überwacht, damit ich sie rechtzeitig reservieren kann.


## Setup
Change the following lines with yout info in the ```monitor.py```

```
URL_TO_MONITOR = "https://example.com"
DELAY_TIME = 300 # seconds aka 5 minutes

SENDING_EMAIL_USERNAME = "yourgmail@gmail.com" 
SENDING_EMAIL_PASSWORD = "yourpassword"
RECIPIENT_EMAIL_ADDRESS = [
    "yourmail@mail.com",
    "yoursecondmail@mail.com"]

```

## What you need

- a gmail account (with low secutity appe enabelt)
- bs4 ```pip3 install bs4```
- yagmail ```pip3 install yagmail```


## Use the monitor

#### for Windows:

simply start the ```monitor.py``` 


#### for Linux and Mac:

in the shell ```./main.sh```
