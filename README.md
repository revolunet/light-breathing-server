# Light breathing server

Make lights breath using RaspberryPI GPIO and an HTTP API

## Install

```python
git clone https://github.com/revolunet/light-breathing-server.git
cd light-breathing-server
pip install -r requirements.txt
```

## Usage

`python server.py --pin 12`

```sh
usage: server.py [-h] [--port PORT] [--pin PIN] [--frequency FREQUENCY]
                 [--intensity INTENSITY] [--delay DELAY]

Make rPI light breath using GPIO

optional arguments:
  -h, --help            show this help message and exit
  --port PORT           HTTP API listening port
  --pin PIN             GPIO LED pin
  --frequency FREQUENCY
                        GPIO frequency
  --intensity INTENSITY
                        Max breath intensity
  --delay DELAY         Breath refresh delay in seconds
```

Then use API on `http://127.0.0.1:9200` 

#### Launch at boot :

add this to `/etc/rc.local` :

```sh
#!/bin/sh -e

# start server.py in a dedicated screen session


cd /path/to/light-breathing-server && screen -dmS breath ./server.py --pin 12 --intensity 3 --delay 0.05

exit 0
```

Recommended rPI distribs for rock solid setups : http://nutcom.hu/ipe

## API

 - `/breath/80/0.01` : breath at 80% max intensity with a 0.01s refresh delay
 - `on`: power on the LED
 - `off`: power off the LED

#### Some pre-defined setings:

 - `/breath/mode/high-fast` : fast breathing
 - `/breath/mode/high-slow` : slow breathing
