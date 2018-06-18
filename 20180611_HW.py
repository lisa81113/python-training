#20180611_HW
#讓使用者輸入5個數字：1.算總和；2.哪個數字最大

number= list(map(int, input('請輸入任意數字，間隔請以","隔開：').split(',')))
print ("輸入的數字總和為：",end=str(sum(number)))
print ("；輸入的數字中最大值為：",end=str(max(number)))

