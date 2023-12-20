import RPi.GPIO as GPIO
import time
#import socket
from socket import *
import time

channel = 11
data = []
j = 0

GPIO.setmode(GPIO.BOARD)
# 0.2秒后开始工作
time.sleep(0.2)
# 设置GPIO接口为写入数据模式
GPIO.setup(channel, GPIO.OUT)
# 输出一个低电平信号
GPIO.output(channel, GPIO.LOW)
time.sleep(0.02)
# 0.02秒后输出一个高电平信号，启动模块测量
GPIO.output(channel, GPIO.HIGH)
# 设置GPIO接口为读取读取数据模式
GPIO.setup(channel, GPIO.IN)

# 等待，获取到高电平信号
while GPIO.input(channel) == GPIO.LOW:
    continue
# 等待，获取到低电平信号
while GPIO.input(channel) == GPIO.HIGH:
    continue

# 获取到高低电平信号后，开始读取模块获取数据
while j < 40:
    k = 0
    while GPIO.input(channel) == GPIO.LOW:
        continue
    while GPIO.input(channel) == GPIO.HIGH:
        k += 1
    if k > 100:
        break
    # 把获取数据放到list中
    if k < 40:
        data.append(0)
    else:
        data.append(1)
    j += 1

# 模块数据读取完毕，打印显示
print("sensor is working.")
print(data)

#根据获取数据定义解析数据（5组二进制数据）
humidity_bit = data[0:8]
humidity_point_bit = data[8:16]
temperature_bit = data[16:24]
temperature_point_bit = data[24:32]
check_bit = data[32:40]

humidity = 0
humidity_point = 0
temperature = 0
temperature_point = 0
check = 0

# 二进制转十进制，解析温湿度数据
for i in range(8):
    humidity += humidity_bit[i] * 2 ** (7 - i)
    humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
    temperature += temperature_bit[i] * 2 ** (7 - i)
    temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
    check += check_bit[i] * 2 ** (7 - i)

tmp = humidity + humidity_point + temperature + temperature_point


print("temperature :", temperature, "*C, humidity :", humidity, "%")




HOST = '101.132.115.197'
PORT = 2222
BUFSIZ = 1024
ADDR = (HOST,PORT)

try:
    mySocket = socket(AF_INET,SOCK_STREAM)
    mySocket.connect(ADDR)
    print("连接到服务器")
except :                           ##连接不成功，运行最初的ip
    print ('连接不成功')


msg = str(temperature)
#编码发送
mySocket.send(msg.encode("utf-8"))
print("发送完成")



# 结束进程，释放GPIO引脚
mySocket.close()
GPIO.cleanup()
print("程序结束\n")
