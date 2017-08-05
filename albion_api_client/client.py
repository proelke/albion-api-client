import requests


class API(object):
    def _url(self, endpoint):
        return 'https://gameinfo.albiononline.com/api/gameinfo' + endpoint

    def get_player_info(self, player_id):
        return requests.get(self._url('/players/{player_id}'.format(
            player_id=player_id))).json()

    def get_guild_id(self, guild_name):
        guild = self.search(guild_name)
        return guild.json()['guilds'][0]['Id']

    def get_guild_info(self, guild_id):
        return requests.get(self._url(
            '/guilds/{guild_id}'.format(guild_id=guild_id))).json()

    def get_guild_data(self, guild_id):
        return requests.get(self._url('/guilds/{guild_id}/data'.format(
            guild_id=guild_id))).json()

    def get_guild_top_kills(self, guild_id, offset=None, limit=None,
                            _range=None):
        params = {}

        if offset:
            params['offset'] = offset
        if limit:
            params['limit'] = limit
        if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
            params['range'] = _range

        return requests.get(
            self._url('/guilds/{guild_id}/top'.format(guild_id=guild_id)),
            params=params).json()

    def get_guild_stats(self, guild_id):
        return requests.get(self._url('/guilds/{guild_id}/stats'.format(
            guild_id=guild_id))).json()

    def get_guild_members(self, guild_id):
        return requests.get(self._url('/guilds/{guild_id}/members'.format(
            guild_id=guild_id))).json()

    def get_guild_fued(self, guild_id, rival_guild_id):
        return requests.get(
            self._url('/guilds/{guild_id}/fued/{rival_guild_id}'.format(
                guild_id=guild_id, rival_guild_id=rival_guild_id))).json()

    def get_server_status(self, server='live'):
        if server == 'live' or server == 'staging':
            return requests.get(
                'http://{server}.albiononline.com/status.txt'.format(
                    server=server)).json()

    def get_event(self, event_id):
        return requests.get(self._url('/events/{event_id}'.format(
            event_id=event_id))).json()

    def get_recent_events(self):
        params = {}
        params['limit'] = '50'
        params['offset'] = '0'

        return requests.get(self._url('/events'), params=params).json()

    def get_events_between(self, start_event, end_event):
        return requests.get(
            self._url('/events/{start_event}/history/{end_event}'.format(
                start_event=start_event, end_event=end_event))).json()

    def search(self, query):
        params = {}
        params['q'] = query
        return requests.get(self._url('/search'), params=params).json()

    def top_player_kill_fame(self, offset='0', limit='11', _range='week'):
        params = {}
        params['offset'] = offset
        params['limit'] = limit
        if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
            params['range'] = _range

        return requests.get(self._url('/playerfame'), params=params).json()

    def top_guild_kill_fame(self, offset='0', limit='11', _range='week'):
            params = {}
            params['offset'] = offset
            params['limit'] = limit
            if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
                params['range'] = _range

            return requests.get(self._url('/guildfame'), params=params).json()

    def top_kill_fame_ratio(self, offset='0', limit='11', _range='week'):
        params = {}
        params['offset'] = offset
        params['limit'] = limit
        if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
            params['range'] = _range

        return requests.get(self._url('/fameratio'), params=params).json()

    def top_guilds_by_attack(self, offset='0', limit='11', _range='week'):
            params = {}
            params['offset'] = offset
            params['limit'] = limit
            if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
                params['range'] = _range

            return requests.get(self._url('/topguildsbyattack'),
                                params=params).json()

    def top_guilds_by_defense(self, offset='0', limit='11', _range='week'):
            params = {}
            params['offset'] = offset
            params['limit'] = limit
            if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
                params['range'] = _range

            return requests.get(self._url('/topguildsbydefense'),
                                params=params).json()

    def player_weapon_ranking(self, offset='0', limit='11', _range='week'):
            params = {}
            params['offset'] = offset
            params['limit'] = limit
            if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
                params['range'] = _range

            return requests.get(self._url('/playerweaponfame'),
                                params=params).json()

    def get_battles(self, offset='0', limit='51', _range=None,
                    sort='recent'):
        params = {}
        params['offset'] = offset
        params['limit'] = limit
        if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
            params['range'] = _range
        if sort and sort in ['recent', 'topfame']:
            params['sort'] = sort

        return requests.get(self._url('/battles'),
                            params=params).json()

    def get_weapon_categories(self):
        return requests.get(self._url('/items/_weaponCategories')).json()
