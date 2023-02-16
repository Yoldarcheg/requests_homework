import requests
import json

from pprint import pprint
from Yandex_disk import YandexDisk
from superhero import Superhero


if __name__ == '__main__':
    Superhero.most_intelligence_hero(['Hulk', 'Captain america', 'Thanos'])
    ya = YandexDisk(token="")
    ya.upload_file_to_disk("/test", "text.txt")
 