import os
import random
import requests
import colorama
from pystyle import *
from colorama import *
import threading
from time import strftime, gmtime, time, sleep
from os import system


class TikTok:
    def __init__(self):
        self.added = 0
        self.lock = threading.Lock()

        try:
            system('title Black Tool V2 - [11]TT Sharing Bot')
            self.amount = int(Write.Input('[>] Desired Amount of Shares: ', Colors.green_to_white, interval=0.000))
        except ValueError:
            print('\nInteger expected.')
            os.system('title TikTok Share Botter - Restart required')
            os.system('pause >NUL')
            os._exit(0)

        try:
            self.video_id = Write.Input('[>] TikTok URL: ', Colors.green_to_white, interval=0.000).split('/')[5]
        except IndexError:
            print(
                f'\n{Fore.GREEN}[+]{Fore.WHITE}Invalid TikTok URL format.\n{Fore.GREEN}[+]{Fore.WHITE}Format expected: https://www.tiktok.com/@username/vi'
                f'deo/1234567891234567891'
            )
            sleep(1)
            input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}>{Fore.LIGHTMAGENTA_EX}]{Fore.WHITE}Press ENTER to exit:")
            os._exit(0)
        else:
            print()

    def status(self, code, intention):
        if code == 200:
            self.added += 1
        else:
            self.lock.acquire()
            print(f'Error: {intention} | Status Code: {code}')
            self.lock.release()

    def update_title(self):
        # Avoid ZeroDivisionError
        while self.added == 0:
            sleep(0.2)
        while self.added < self.amount:
            # Elapsed Time / Added * Remaining
            time_remaining = strftime(
                '%H:%M:%S', gmtime(
                    (time() - self.start_time) / self.added * (self.amount - self.added)
                )
            )
            os.system(
                f'title [TikTok Shares Botter] - Added: {self.added}/{self.amount} '
                f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
                f'{threading.active_count()} ^| Time Remaining: {time_remaining}'
            )
            sleep(0.2)
        os.system(
            f'title [TikTok Shares Botter] - Added: {self.added}/{self.amount} '
            f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
            f'{threading.active_count()} ^| Time Remaining: 00:00:00'
        )
        Write.Print(f"""[+]Successfully added {self.amount} visual!""", Colors.green_to_cyan, interval=0.000)

    def bot(self):
        action_time = round(time())
        install_id = ''.join(random.choice('0123456789') for _ in range(19))

        data = (
            f'action_time={action_time}&item_id={self.video_id}&item_type=1&share_delta=1&stats_cha'
            'nnel=copy'
        )
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-common-params-v2': 'version_code=16.6.5&app_name=musical_ly&channel=App%20Store&devi'
                                  f'ce_id={install_id}&aid=1233&os_version=13.5.1&device_platform=i'
                                  'phone&device_type=iPhone10,5'
        }

        try:
            response = requests.post(
                'https://api16-core-c-useast1a.tiktokv.com/aweme/v1/aweme/stats/?ac=WIFI&op_region='
                'SE&app_skin=white&', data=data, headers=headers
            )
        except Exception as e:
            print(f'Error: {e}')
        else:
            if 'Service Unavailable' not in response.text:
                self.status(response.status_code, response.text)

    def multi_threading(self):
        self.start_time = time()
        threading.Thread(target=self.update_title).start()

        for _ in range(self.amount):
            threading.Thread(target=self.bot).start()

        os.system('pause >NUL')
        os.system('title [TikTok Shares Botter] - Exiting...')
        sleep(3)


if __name__ == '__main__':
    os.system('cls && title TikTok Share Botter - Github: Alphalius')
    main = TikTok()
    main.multi_threading()