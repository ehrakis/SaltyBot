import src.data_fetcher as df
import src.bet as bet
import json
import time

SECONDS_BETWEEN_GAME_STATUS_CHECKING = 30


def print_json(json_data):
    print(json.dumps(json_data, indent=4, sort_keys=True))


def play():
    while True:
        print("Check if a fight is in progress...")
        simple_fight_data = df.fetch_simple_fight_data()

        if not df.is_match_in_progress(simple_fight_data):
            print("Fight over !")
            bet.bet(1)
        else:
            print("Fight in progress... going back to sleep")

        time.sleep(20)
