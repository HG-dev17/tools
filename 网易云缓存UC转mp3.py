import sys

#使用方法：将此脚本放进一个文件夹，在此文件夹地址栏输入cmd运行此脚本加上需要转换的uc文件路径
#举例：网易云缓存UC转mp3.py "C:\Users\用户名\AppData\Local\Netease\CloudMusic\Cache\Cache\2129927846-320-e17c9df56f23b4826d1f79f682ec.uc"

fname =sys.argv[1]
print(fname)

with open(fname, "rb") as f:
	c = f.read()

arr = bytearray(c)
for i in range(len(arr)):
	arr[i] ^= 163

with open(fname+".mp3", "wb") as f:
	f.write(bytes(arr))

print('ok')