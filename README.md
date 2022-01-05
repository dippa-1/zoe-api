# zoe-api
## Requirements
- Python 3
- Renault Account

## How to set up
1. Install the python packages with `pip install -r requirements.txt`
2. In start_server.py, edit the ip address to your server's address
3. Run `renault-api login` and fill in your Renault login data. When asked if you want to store the credentials, I would type `y`
4. Run `./start_server.sh`. If you aren't on Linux, copy the command inside `start_server.sh` and execute it in your terminal.

## How to use
With the server running, open your browser at <ip>:8000/<command>.
<command> is the string of the [renault-api](https://github.com/hacf-fr/renault-api) that is after `renault-api`.

For example, if you run the server locally and open `127.0.0.1:8000/charge mode --set 1`, the Zoe charge mode is set to scheduled charging.

The respone from renault-api is always returned to you.
