import time
import multiprocessing
from PIL import Image, ImageFilter

ids = [
    '1Z7c297PyFvIREiRmKZioSaANrqo3LErM',
    '1bPu3g3WGWeV8kKH4fbRJQb4jbrKJ673u',
    '1gzcb10_8Z6hM8Is35S-uEuX29ekF2QxT',
    '1jxceAfRU0WaaaqJmjQNQ_zyblZ-OFycS',
    '1IjSm2uokgFah3135uB0oBxCEBj27UEVM',
    '1NpKTiYIV04Uh3G22gNMu9kwEResspSvD',
    '1rFCxE7NAl7oXhpn55jkKgIFl4FH0ZLR9',
    '1s4iSFAV23Z2t0CGtKQ_2IKVoDAhWEHBB',
    '1_p7-VnhNbw0PavBjzbDo1uq4kP7kipF-',
    '1gPKbz2sdLGza6aqJB1avwk2jbzNAZqx8'
    ]

t1 = time.perf_counter()

size = (1200, 1200)

def process_image(img_name):
    img = Image.open(f'{img_name}.png')
    img = img.rotate(180) 
    width, height = img.size
    area = (0, 0, width/2, height/2)
    img = img.crop(area)
    img = img.resize((width//2, height//2))
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.save(f'processed/{img_name}.png')
    print(f'{img_name} was processed...')

processes = []

for i in range(10):
  p1 = multiprocessing.Process(target=process_image, args=[ids[i]])
  p1.start()
  processes.append(p1)

for p in processes:
  p.join()

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')