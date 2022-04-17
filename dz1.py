# задание 1

import time

class TrafficLight:
    def __init__(self):
        self.__colors = ['red', 'yellow', 'green']

    def running(self):
        for color in self.__colors:
            if 'red' in color:
                sec = 4
                print(f'горит : Красный')
                time.sleep(sec)
            elif 'yellow' in color:
                sec = 4
                print(f'горит : Желтый')
                time.sleep(sec)
            elif 'green' in color:
                sec = 5
                print(f'горит : Зеленный')
                time.sleep(sec)


traffic_l = TrafficLight()
traffic_l.running()
