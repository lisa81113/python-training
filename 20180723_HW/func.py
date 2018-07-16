#作業1
#1.1把99乘法表包裝成函式，可做成nxn 乘法
#1.2把四則運算幾包裝成函式
#1.3將以上函式包裝在你自己的模組和封包中,並且在主程式成功使用
print("作業1：將以上函式包裝在你自己的模組和封包中,並且在主程式成功使用")

import lib.core as hw
print("作業1.1：99乘法表")
hw.list()
print("作業1.2：四則運算")
hw.op(3,4,"+")

#作業2
print("作業2：使用系統內建的模組radom產生1~100間的亂數")
import random 
print (random.randrange(101))