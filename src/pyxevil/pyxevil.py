import time
import requests


class Xevil:
    def __init__(self, apikey: str, timeout: int = 30):
        """
        apikey: Xevil bot apikey get in https://t.me/Xevil_check_bot
        timeout: requests timeout, default is 30
        """
        self.key = apikey
        self.timeout = timeout
        self.url_in = "http://api.sctg.xyz/in.php"
        self.url_res = "http://api.sctg.xyz/res.php"

    def log(self, data):
        year, mon, day, hour, minute, sec, wday, yday, dst = time.localtime()
        data = f"[{year}-{mon}-{day} {hour}:{minute}:{sec}] {data}\n"
        open("logs.txt", "a+").write(data)

    def countdown(self, t):
        while t:
            print("[-] captcha not ready! ", flush=True, end="\r")
            time.sleep(0.25)
            print("[\] captcha not ready! ", flush=True, end="\r")
            time.sleep(0.25)
            print("[|] captcha not ready! ", flush=True, end="\r")
            time.sleep(0.25)
            print("[/] captcha not ready! ", flush=True, end="\r")
            time.sleep(0.25)
            t -= 1
        print("                                 ", flush=True, end="\r")

    def send_req(self, data=None):
        while True:
            try:
                res = requests.post(self.url_in, data=data)
                self.log(res.text)
                return res.text
            except (
                requests.exceptions.ConnectionError,
                requests.exceptions.ConnectTimeout,
                requests.exceptions.ReadTimeout,
            ):
                print(
                    f"[x] connection timeout/ connection error !",
                    flush=True,
                    end="\r",
                )
                time.sleep(1)
                print(
                    "                                             ",
                    flush=True,
                    end="\r",
                )
                continue

    def get_result(self, task_id: str) -> tuple:
        """
        task_id: request captcha id from url_in

        return ()
        """

        params = {
            "key": self.key,
            "id": task_id,
        }
        while True:
            res = requests.get(self.url_res, params=params)
            self.log(res.text)
            if res.text.find("CAPCHA_NOT_READY") >= 0:
                self.countdown(3)
                continue

            if res.text.find("|") >= 0:
                return True, res.text.split("|")[1]

            if res.text.find("ERROR_CAPTCHA_UNSOLVABLE") >= 0:
                return False, "ERROR_CAPTCHA_UNSOLVABLE"

            return False, res.text

    def get_balance(self):
        params = {
            "key": self.key,
            "action": "getbalance",
        }
        res = requests.get(self.url_res, params=params)
        self.log(res.text)
        return True, res.text

    def anti_bot(self, data):
        data["method"] = "antibot"
        res = self.send_req(data)
        if res.find("|") >= 0:
            task_id = res.split("|")[1]
            res = self.get_result(task_id=task_id)
            return res

        return res

    def recaptchav2(self, site_key: str, site_url: str):
        """
        site_key:
        """
        data = {
            "key": self.key,
            "method": "userrecaptcha",
            "pageurl": site_url,
            "sitekey": site_key,
        }
        res = self.send_req(data)
        if res.find("|") >= 0:
            task_id = res.split("|")[1]
            res = self.get_result(task_id=task_id)
            return res

        return res

    def upside_down(self, base64_image):
        data = {
            "method": "viefaucet",
            "body": base64_image,
        }
        res = self.send_req(data)
        if res.find("|") >= 0:
            task_id = res.split("|")[1]
            res = self.get_result(task_id=task_id)
            return res

        return res

    def authkong(self, site_url, site_key):
        data = {
            "method": "authkong",
            "pageurl": site_url,
            "sitekey": site_key,
        }
        res = self.send_req(data)
        if res.find('|') >= 0:
            task_id = res.split('|')[1]
            res = self.get_result(task_id=task_id)
            return res
        
        return res
    
