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

## API

 - `/breath/fast` : fast breathing
 - `/breath/slow` : slow breathing
