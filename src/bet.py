import urllib.request
import urllib.parse
import json


def bet(amount):
    address = "https://www.saltybet.com/ajax_place_bet.php"

    data = urllib.parse.urlencode({"selectedplayer":"player1", "wager":amount}).encode()

    request = urllib.request.Request(address,
                                     headers={
                                        "method": "POST",
                                        "authority": "www.saltybet.com",
                                        "scheme": "https",
                                        "path": "/ajax_place_bet.php",
                                        "accept": "*/*",
                                        "origin": "https://www.saltybet.com",
                                        "x-requested-with": "XMLHttpRequest",
                                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
                                        "sec-fetch-site": "same-origin",
                                        "sec-fetch-mode": "cors",
                                        "referer": "https://www.saltybet.com/",
                                        "accept-encoding": "gzip, deflate, br",
                                        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
                                        "cookie": "__cfduid=d05b1b8860d8d0ccfffffef683737f88e1576881726; PHPSESSID=eidl1l8h1rm8ehma8tk9rfau05"
                                     },
                                     data=data)
    response = urllib.request.urlopen(request)
    print("Bet sent")
    return response.read()

