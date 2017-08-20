import requests


class AlbionAPI(object):
    def _url(self, endpoint):
        return 'https://gameinfo.albiononline.com/api/gameinfo' + endpoint

    def get_player_id(self, player_name):
        player = self.search(player_name)
        return player['players'][0]['Id']

    def get_player_info(self, player_id):
        return requests.get(self._url('/players/{player_id}'.format(
            player_id=player_id))).json()

    def get_player_topkills(self, player_id, offset=0, limit=11,
                            _range='week'):
        params = {}
        params['offset'] = offset
        params['limit'] = limit
        if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
            params['range'] = _range
        return requests.get(self._url('/players/{player_id}/topkills'.format(
            player_id=player_id)), params=params).json()

    def get_player_solokills(self, player_id, offset=0, limit=11,
                             _range='week'):
        params = {}
        params['offset'] = offset
        params['limit'] = limit
        if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
            params['range'] = _range
        return requests.get(self._url('/players/{player_id}/solokills'.format(
            player_id=player_id)), params=params).json()

    def get_player_death(self, player_id):
        return requests.get(self._url('/players/{player_id}/death'.format(
            player_id=player_id))).json()

    def get_guild_id(self, guild_name):
        guild = self.search(guild_name)
        return guild['guilds'][0]['Id']

    def get_guild_info(self, guild_id):
        return requests.get(self._url(
            '/guilds/{guild_id}'.format(guild_id=guild_id))).json()

    def get_guild_data(self, guild_id):
        return requests.get(self._url('/guilds/{guild_id}/data'.format(
            guild_id=guild_id))).json()

    def get_guild_top_kills(self, guild_id, offset=0, limit=11,
                            _range='week'):
        params = {}
        params['offset'] = offset
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

    def get_recent_events(self, limit=50, offset=0):
        params = {}
        params['limit'] = limit
        params['offset'] = offset

        return requests.get(self._url('/events'), params=params).json()

    def get_events_between(self, start_event, end_event):
        return requests.get(
            self._url('/events/{start_event}/history/{end_event}'.format(
                start_event=start_event, end_event=end_event))).json()

    def get_guildmatches(self, match_id, offset=0, limit=6):
        params = {}
        params['offset'] = offset
        params['limit'] = limit

        return requests.get(
            self._url('/guildmatches/{guild_id}'.format(
                match_id=match_id)), params=params).json()

    def get_guildmatches_top(self):
        return requests.get(self._url('/guildmatches/top')).json()

    def get_guildmatches_next(self, offset=0, limit=11):
        params = {}
        params['offset'] = offset
        params['limit'] = limit

        return requests.get(self._url('/guildmatches/next'),
                            params=params).json()

    def get_guildmatches_past(self, offset=0, limit=51):
        params = {}
        params['offset'] = offset
        params['limit'] = limit

        return requests.get(self._url('/guildmatches/past'),
                            params=params).json()

    def get_guildmatches_history(self, guild_id, rival_guild_id):
        return requests.get(self._url(
            '/guildmatches/history/{guild_id}/{rival_guild_id}'.format(
                guild_id=guild_id, rival_guild_id=rival_guild_id))).json()

    def search(self, query):
        params = {}
        params['q'] = query
        return requests.get(self._url('/search'), params=params).json()

    def top_player_kill_fame(self, offset=0, limit=11, _range='week'):
        params = {}
        params['offset'] = offset
        params['limit'] = limit
        if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
            params['range'] = _range

        return requests.get(self._url('/playerfame'), params=params).json()

    def top_guild_kill_fame(self, offset=0, limit=11, _range='week'):
            params = {}
            params['offset'] = offset
            params['limit'] = limit
            if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
                params['range'] = _range

            return requests.get(self._url('/guildfame'), params=params).json()

    def top_kill_fame_ratio(self, offset=0, limit=11, _range='week'):
        params = {}
        params['offset'] = offset
        params['limit'] = limit
        if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
            params['range'] = _range

        return requests.get(self._url('/fameratio'), params=params).json()

    def top_guilds_by_attack(self, offset=0, limit=11, _range='week'):
            params = {}
            params['offset'] = offset
            params['limit'] = limit
            if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
                params['range'] = _range

            return requests.get(self._url('/topguildsbyattack'),
                                params=params).json()

    def top_guilds_by_defense(self, offset=0, limit=11, _range='week'):
            params = {}
            params['offset'] = offset
            params['limit'] = limit
            if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
                params['range'] = _range

            return requests.get(self._url('/topguildsbydefense'),
                                params=params).json()

    def player_weapon_ranking(self, offset=0, limit=11, _range='week'):
            params = {}
            params['offset'] = offset
            params['limit'] = limit
            if _range and _range in ['week', 'lastWeek', 'month', 'lastMonth']:
                params['range'] = _range

            return requests.get(self._url('/playerweaponfame'),
                                params=params).json()

    def get_battles(self, offset=0, limit=51, _range=None,
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
