def doinhietdo(n):
    a=n*9/5+32
    return a
nhietdoC=float(input('Nhập nhiệt độ (°C): '))
nhietdoF= doinhietdo(nhietdoC)
print('Nhiệt độ sau khi đổi là: ',nhietdoF,'°F')