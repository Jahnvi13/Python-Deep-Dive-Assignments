import concurrent.futures
import gdown
import time 

start = time.perf_counter()
ids = ['1Z7c297PyFvIREiRmKZioSaANrqo3LErM',
        '1bPu3g3WGWeV8kKH4fbRJQb4jbrKJ673u',
        '1gzcb10_8Z6hM8Is35S-uEuX29ekF2QxT',
        '1jxceAfRU0WaaaqJmjQNQ_zyblZ-OFycS',
        '1IjSm2uokgFah3135uB0oBxCEBj27UEVM',
        '1NpKTiYIV04Uh3G22gNMu9kwEResspSvD',
        '1rFCxE7NAl7oXhpn55jkKgIFl4FH0ZLR9',
        '1s4iSFAV23Z2t0CGtKQ_2IKVoDAhWEHBB',
        '1_p7-VnhNbw0PavBjzbDo1uq4kP7kipF-',
        '1gPKbz2sdLGza6aqJB1avwk2jbzNAZqx8']

def downloadimg(id):
    gdown.download(url=f'https://drive.google.com/file/d/{id}/view?usp=share_link', output=f'{id}.png', quiet=False, fuzzy=True)

with concurrent.futures.ThreadPoolExecutor() as executor:
    result = [executor.submit(downloadimg, id) for id in ids]
