import urllib.request
import json

USER_ID = "593540"

JSON_KEYS = {
    "wagger": "w",
    "balance": "b",
    "p1": "p1name",
    "p2": "p2name",
    "status": "status",
}
FIGHT_IN_PROGRESS_STATUS = "locked"


def fetch_json(address):
    user_agent = 'Chrome/35.0.1916.47'
    request = urllib.request.Request(address, headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode("utf8"))


def fetch_game_data():
    game_data_url = 'https://www.saltybet.com/zdata.json'
    return fetch_json(game_data_url)


def fetch_simple_fight_data():
    next_fight = 'https://www.saltybet.com/state.json'
    return fetch_json(next_fight)


def get_game_status(json_data):
    return json_data[JSON_KEYS["status"]]


def get_player_one(json_data):
    return json_data[JSON_KEYS["p1"]]


def get_player_two(json_data):
    return json_data[JSON_KEYS["p2"]]


def get_user_balance(json_data):
    return json_data[USER_ID][JSON_KEYS["balance"]]


def get_user_wager(json_data):
    return json_data[USER_ID][JSON_KEYS["wagger"]]


def is_match_in_progress(json_data):
    return get_game_status(json_data) == FIGHT_IN_PROGRESS_STATUS


def get_winner(json_data):
    """Only use with complete game data

    :param json_data:
    :return:
    """
    if get_game_status(json_data) == "1":
        return get_player_one(json_data)
    elif get_game_status(json_data) == "2":
        return get_player_two(json_data)
    else:
        raise ValueError("Wrong status game value")
