
import RPi.GPIO as GPIO
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

# humidity_bit = data[1:9]
# humidity_point_bit = data[9:17]
# temperature_bit = data[17:25]
# temperature_point_bit = data[25:33]
# check_bit = data[33:41]


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

# 打印显示由模块数据解释的温湿度数据

# if check == tmp:
#     print("temperature :", temperature, "*C, humidity :", humidity, "%")
#
#     # 将内容写进txt文件
#     res = '{value:%f}' % temperature
#     import json
#     with open('/home/pi/Desktop/data.txt', 'a') as outfile:
#         json.dump(res, outfile)
#     outest = open('/home/pi/Desktop/data.txt', 'a')
#     outest.write(res)
#     outest.close
#     print(res)
# else:
#     print("wrong")
#     print("temperature :", temperature, "*C, humidity :", humidity, "% check :", check, ",tmp :", tmp)


print("temperature :", temperature, "*C, humidity :", humidity, "%")
# 将内容写进txt文件
# res = '{value:%f}' % temperature
# import json
#
# with open('/home/pi/data.txt', 'a') as outfile:
#     json.dump(res, outfile)
# outest = open('/home/pi/data.txt', 'a')
# outest.write(res)
# outest.close
# print(res)
#
#
#
#
# rqs_headers={'Content-Type': 'application/json'}
# requrl ='http://192.168.1.3:8000/temperature_api/'
# new_data = {
#     "captime": datetime.datetime.now(),
#     "captemperature": temperature
# }
#
# class ComplexEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime.datetime):
#             return obj.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(obj, datetime.date):
#             return obj.strftime('%Y-%m-%d')
#         else:
#             return json.JSONEncoder.default(self, obj)
#
# test_data = json.dumps(new_data, cls=ComplexEncoder)
#
# response = requests.post(url=requrl, headers=rqs_headers, data=test_data)
#

# 结束进程，释放GPIO引脚
GPIO.cleanup()
