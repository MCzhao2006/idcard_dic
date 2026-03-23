import time

print("\n\033[1;40m用途:生成中国大陆身份证字典,本工具免费/开源,无网络连接\033[0m"
      "\n\033[1;41m注意:仅供实验/测试本人身份证准确性,请勿用于非法用途,本作者概不负责\033[0m"
      "\n\033[1;44mMadeBy:https://github.com/MCzhao2006\033[0m\n")
output_file = str(input("请输入生成路径与文件名(如C:/Users/ASUS/Desktop/savefile.txt):"))
ran = int(time.time())    # 使用时间戳,防止重名文件覆盖
if not output_file:
    print(f'\033[34m[INFO]:未检测到输出文件名,已使用默认文件名"4aVef1le{ran}.txt"\033[0m')
    output_file = f'4aVef1le{ran}.txt'
bl = 0
while not 3 >= bl >= 1:
    try:
        bl = int(input("1知道生日,2知道后四位\n3自定义(残缺功能,不建议使用):"))
    except ValueError:
        continue

begin = "1"          # 设定空变量，为while做好准备
birth = "1"
genderstr = ""
divisor = ""
last = "1"
start = 0
end = 0
q = 0
year = '0'
check18list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check = [1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2]
def returnresult():
    result = 0
    for i in range(0, len(check18list)):
        result += (int(before17[i]) * int(check18list[i]))
    result = result % 11
    return result
def fuckX(X):
    if X == 'X' or X == 'x':
        return 10
    return int(X)

while not 659012 >= int(begin) >= 110101:           # 中华人民共和国区号验证
    try:
        begin = int(input("请输入前六位省市区号(如320211):"))
    except ValueError:
        continue
if bl == 1:
    with open(output_file, 'w') as f:
        while not 25001231 >= int(birth) >= 18500101:
            try:
                birth = int(input("请输入八位生日(如19980405):"))
            except ValueError:
                continue
        while True:
            genderstr = input("请输入性别(如男):")
            if genderstr == '男':  # 男性余数
                divisor = 1
                break
            elif genderstr == '女':  # 女性余数
                divisor = 0
                break
            else:
                continue
        for x in range(0, 10):
            for y in range(0, 10):
                for gender in range(0, 10):
                    before17 = list(f"{begin}{birth}{x}{y}{gender}")
                    result = returnresult()
                    if gender % 2 == divisor:   # 条件更改除数分流男女
                        for last in range(0, 11):  # 词条组合,并写入文件
                            if last != check[result]:
                                continue
                            if last == 10:  # 最后一位为10替换X
                                last = "X"
                            before17 = ''.join(before17)
                            f.write(f"{before17}{last}\n")
elif bl == 2:
    with open(output_file, 'w') as f:
        while True:
            last = input('请输入身份证后四位:')
            if len(last) != 4 or \
                ((not last[:-1].isdigit()) or \
                 (not last[3] == 'X' and last[3] == 'x' and last[3].isdigit())):
                # 初始4位判断    # 前三位不是数字||(最后一位不是X或x或数字)
                continue
            break
        while not 2500 >= start >= 1850:
            try:
                start = int(input("请输入生日起始年份:"))
            except ValueError:
                start = 0
                continue
        while not 2500 >= end >= 1850:
            try:
                end = int(input("请输入生日结束年份:"))
            except ValueError:
                end = 0
                continue
        for year in range(start, end + 1):
            for month in range(1, 13):
                if month < 10:
                    month = f"0{month}"
                for date in range(1, 32):
                    if date < 10:
                        date = f"0{date}"
                    if month == 2 and date > 29:
                        break
                    birth = str(year)+str(month)+str(date)
                    before17 = list(f"{begin}{birth}{last[0]}{last[1]}{last[2]}")
                    result = returnresult()
                    if fuckX(last[3]) != check[result]:
                        continue
                    before17 = ''.join(before17)
                    f.write(f"{before17}{last[3]}\n")
elif bl == 3:
    with open(output_file, 'w') as f:
        while not 2500 >= int(year) >= 1850:
            year = input("您至少给/猜一个出生年份:")   # 最现实的最有效缓和字典大小条件
            if (not year.isdigit()) or year == '':
                year = '0'
                continue
        last8 = 8*['?']                        # 后续一对一填值初始值
        while True:
            # print(type(last8))
            # print(last8)
            print(f"你目前的后八位:")
            for x in range(0, 8):              # 循环吐值
                print(last8[x],end="")
            print("")                          # \n
            while True:
                try:
                    q = int(input("***信息越少,字典越大,爆破越不现实***\n您还知道第几位?(0,我不知道了):"))
                except ValueError:
                    continue
                if 0 <= q <= 8:     # 规范值域
                    break
            if q == 0:              # 跳出验证
                break
            try:
                value = input("输入这一位的值:")       # 位:值一对一
            except ValueError:
                value = "0"
                continue
            if (q == 1 and (value != '1' and value != '0')) or (q == 2 and not 9 >= int(value) >= 0):
                print("\033[31m[ERROR]:月份不合法\033[0m\n")                    # 月份值校验
                continue
            elif (q == 3 and not 3 >= int(value) >= 0) or (q == 4 and not 9 >= int(value) >= 0):
                print("\033[31m[ERROR]:日期不合法\033[0m\n")                    # 日期值校验
                continue
            elif q == 8 and not (9 >= int(value) >= 0 or value == 'X' or value == 'x'):
                print("\033[31m[ERROR]:第八位不合法\033[0m\n")                  # 第八位校验
                continue
            elif 1 >= q >= 7 and not 9 >= int(value) >= 0:
                print("\033[31m[ERROR]\:值不合法033[0m\n")                     # 粗略校验
                continue
            last8[q-1] = value      # 位校准
            genderstr = last8[6]
        while genderstr != '男' and genderstr != '女' and genderstr != '6':
            genderstr = str(input("请输入性别(如男)(6,我不知道):"))       # 第二最现实的最有效缓和字典大小条件
            if genderstr == '男':  # 男性余数
                divisor = 1
            elif genderstr == '女':  # 女性余数
                divisor = 0
            elif genderstr == '6':  # 万能余数
                divisor = True or False

        for month in range(1, 13):
            if month < 10:
                month = f"0{month}"
            else:
                month = str(month)
            # if last8[0] != '?':
            #     month[0] = last8[0]
            # if last8[1] != '?':
            #     month[1] = last8[1]
            for date in range(1, 32):
                if date < 10:
                    date = f"0{date}"
                if month == 2 and date > 29:
                    break
                for x in range(0, 10):
                    for y in range(0, 10):
                        for gender in range(0, 10):
                            before17 = list(f"{begin}{year}{str(month)}{str(date)}{x}{y}{gender}")
                            if gender % 2 == divisor:  # 条件更改除数分流男女
                                if last8[7] == "?":     # 判断最后一位是否被自定义|没有被自定义
                                    for last in range(0, 11):  # 词条组合,并写入文件
                                        result = returnresult()     # 校验计算
                                        if fuckX(last) != check[result]:    # 校验验证
                                            continue
                                        if last == 10:  # 最后一位为10替换X
                                            last = "X"
                                        f.write(f"{''.join(before17)}{last}\n")
                                else:       # 被自定义
                                    result = returnresult()         # 校验计算
                                    if fuckX(last8[7]) != check[result]:    # 校验验证
                                        continue
                                    f.write(f"{''.join(before17)}{''.join(last8[7])}\n")

print("\033[1;44m[INFO]:程序即将退出\033[0m")     # 程序退出功能,也是为.bat用户的防"闪退"
for x in reversed(range(1, 6)):
    print(x)
    time.sleep(1)
print()


# info
# 第8位OK
#

# 已知bug
# 1.使用万能余数时只生成男性字典
# 2.忽略自定义数值问题
# 3.问题捕获不充分
# 4.
# 5.

