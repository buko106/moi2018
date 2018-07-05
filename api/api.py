import requests


class APIService:
    def __init__(self, authorization_token: str):
        self.authorization_token = authorization_token
        self.endpoint = "https://apiv2.twitcasting.tv/internships/2018/games"
        self.level = None
        self.game_id = None

    def _get_authorization_header(self):
        return "Bearer " + self.authorization_token

    def start(self, level: int):
        assert(type(level) == int)
        assert(3 <= level <= 10)
        self.level = level
        resp = requests.get(
            self.endpoint,
            params={"level": str(level)},
            headers={"Authorization": self._get_authorization_header()}
        )
        as_dict = resp.json()
        self.game_id = as_dict["id"]
        return as_dict

    def answer(self, answer: str):
        assert(len(answer) == self.level)
        assert(self.game_id is not None)
        resp = requests.post(
            self.endpoint + "/" + self.game_id,
            json={"answer": answer},
            headers={"Authorization": self._get_authorization_header()}
        )
        if not resp.ok:
            print(resp.json())
            resp.raise_for_status()
        return resp.json()
