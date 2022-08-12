# 在线安装  schedule
import time

import schedule
def job():
    print('哈哈哈-----')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
