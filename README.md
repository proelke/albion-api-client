# albion-api-client
An API client for Albion Online written in Python.

Disclaimer
------------
This API client uses Albion Online's unofficial API. The API is unstable and may change at any time. New endpoints will be added as they are discovered.

Installation
------------
To install from pip:

    pip install albion-api-client

To install from source:

    python setup.py install


Usage
-----
```
from albion_api_client import AlbionAPI

client = AlbionAPI()

player_id = client.get_player_id('Snaxxor')
# Gets first matching player's id
player_kills = client.get_player_topkills(player_id)
# Gets the players most recent 11 kills in the last week (default)
player_solo_kills = client.get_player_solokills(player_id, limit=50, _range='month')
# Gets the players most recent 50 solo kills over the last month

guild_id = client.get_guild_id('Awful Company')
# Gets first matching guild id
guild_info =  client.get_guild_info(guild_id)
# Gets basic guild information
guild_data = client.get_guild_data(guild_id)
# Gets basic guild information and GvG data, top players, and kill fame
```
