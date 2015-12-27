# Light breathing server

Make lights breath using RaspberryPI GPIO and an HTTP API

## Install

```python
git clone https://github.com/revolunet/light-breathing-server.git
cd light-breathing-server
pip install -r requirements.txt
```

## Usage

`python server.py --pin 17 --frequency 150 --port 3200`

Then use API on `http://127.0.0.1:9200` 

#### Launch at boot :

add this to `/etc/rc.local` :

`cd /root/prizoners/light-breathing-server && python server.py`

Recommended rPI distribs for rock solid setups : http://nutcom.hu/ipe

## API

 - `/breath/80/0.01` : breath at 80% max intensity with a 0.01s refresh delay

#### Some pre-defined setings:

 - `/breath/mode/high-fast` : fast breathing
 - `/breath/mode/high-slow` : slow breathing
