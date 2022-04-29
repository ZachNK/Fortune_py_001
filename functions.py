import names as nm
import time

class Fives:

    def colors(five):
        c = ['\033[34m', '\033[31m', '\033[32m', '\033[37m', '\033[33m']
        return c[five-1]

    def stemfives(stem):
        num5 = [3, 3, 2, 2, 5, 5, 4, 4, 1, 1]
        return num5[stem - 1]

class toNum:

    # 정수로 10천간 찾기
    def filter_Stem(stem):
        stem %= 10
        if stem <= 0:
            stem += 10
        return stem

    # 정수로 12지지 찾기
    def filter_Branch(branch):
        branch %= 12
        if branch <= 0:
            branch += 12
        return branch

    # sky = 천간 수, land = 지지 수로 60갑자 1~60 수 찾기
    def cycle2num(sky, land):
        result = land
        sky %= 10
        while True:
            if result % 10 == sky:
                break
            else:
                result += 12
        return result

    # 체가 용을 바라볼 때 육친 찾기
    def deity_stem2stem(subj, obj):
        diety = obj - subj
        if subj % 2 == 0 and diety % 2 != 0:
            diety += 2
        if diety < 0:
            diety += 10
        return diety

class toList:

    # 1~60 수로 60갑자 찾기 (리스트형)
    def num2cycle(num):
        cycle = []
        stemNum = toNum.filter_Stem(num)
        branchNum = toNum.filter_Branch(num)
        cycle.append(int(stemNum))
        cycle.append(int(branchNum))
        return cycle

    # 지장간 (리스트형)
    def men_in_branch(branch):
        #          0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22, 23,24,25
        #          ㆍ=0, 甲=1, 乙=2, 丙=3, 丁=4, 戊=5, 己=6, 庚=7, 辛=8, 壬=9, 癸=10
        all_men = [5, 3, 1, 0, 2, 10, 5, 7, 3, 6, 4, 2, 6, 5, 9, 7, 0, 8, 4, 5, 1, 9, 0, 10, 8, 6]
        # 寅 0: 0, 1, 2
        # 卯 1: 2, 3, 4
        # 辰 2: 4, 5, 6
        # 巳 3: 6, 7, 8
        # 午 4: 8, 9, 10
        # 未 5: 10, 11, 12
        # 申 6: 13, 14, 15
        # 酉 7: 15, 16, 17
        # 戌 8: 17, 18, 19
        # 亥 9: 19, 20, 21
        # 子 10: 21, 22, 23
        # 丑 11: 23, 24, 25
        add = 0
        branch -= 3
        if branch < 0:
            branch += 12
        if branch >= 6:
            add = 1
        # men = [ 여기, 중기, 정기 ] (지장간 숫자 1~10=甲~癸, 0=ㆍ)
        men = [all_men[(branch * 2 + add)], all_men[(branch * 2 + add) + 1], all_men[(branch * 2 + add) + 2]]
        return men

    # 천간으로 다음 세대 갑자 찾기 (리스트형: major=60갑자(혹은 천간), minor=다음세대 지지)
    def find_cycle(major, minor):
        dragon = 0
        major = toNum.filter_Stem(major)
        if (major % 5) == 1:  # 甲, 己
            dragon = 5
        elif (major % 5) == 2:  # 乙, 庚
            dragon = 7
        elif (major % 5) == 3:  # 丙, 辛
            dragon = 9
        elif (major % 5) == 4:  # 丁, 壬
            dragon = 1
        else:  # 戊, 癸
            dragon = 3

        sky = toNum.filter_Stem(dragon + minor + 5)
        land = toNum.filter_Branch(minor)
        result = [sky, land]
        return result

    def all_fives(f=[8]):
        re = [Fives.stemfives(f[0]), Fives.stemfives(toList.men_in_branch(f[1])[2]),
              Fives.stemfives(f[2]), Fives.stemfives(toList.men_in_branch(f[3])[2]),
              Fives.stemfives(f[4]), Fives.stemfives(toList.men_in_branch(f[5])[2]),
              Fives.stemfives(f[6]), Fives.stemfives(toList.men_in_branch(f[7])[2])]
        return re


class Roads:
    #천간으로 십이운성 찾기 (천간-->지지)
    def see_road(stem, branch):
        r=0
        f = stem
        if f%2 == 0:
            f -=1
        f = int(f/2)
        # f = 1:0, 3:1, 5:2, 7:3, 9:4
        # f = 2:0, 4:1, 6:2, 8:3, 10:4
        # 1: 1-9, 2-10, 3-12, 4-1, 5-12, 6-1, 7-3, 8-4, 9-6, 10-7
        # 2: 1-10, 2-9, 3-1, 4-12, 5-1, 6-12, 7-4, 8-3, 9-7, 10-6
        # 3: 1-11, 2-8, 3-2, 4-11, 5-2, 6-11, 7-5, 8-2, 9-8, 10-5
        # 4: 1-12, 2-7, 3-3, 4-10, 5-3, 6-10, 7-6, 8-1, 9-9, 10-4
        # 5: 1-1, 2-6, 3-4, 4-9, 5-4
        # 6: 1-2, 2-5, 3-5, 4-8, 5-5
        # 7: 1-3, 2-4, 3-6, 4-7, 5-6
        # 8: 1-4, 2-3, 3-7, 4-6, 5-7
        # 9: 1-5, 2-2, 3-8, 4-5, 5-8
        #10: 1-6, 2-1, 3-9, 4-4, 5-9
        #11: 1-7, 2-12, 3-10, 4-3, 5-10
        #12: 1-8, 2-11, 3-11, 4-2, 5-11
        #go=(branch-8) (branch-11) (branch-11) (branch-2) (branch-5)
        #back=(11-branch) (2-branch) (2-branch) (5-branch) (8-branch)
        go = [8, 11, 11, 2, 5]
        back = [11, 2, 2, 5, 8]

        if stem %2 != 0:
            r = branch-go[f]
        if stem %2 ==0:
            r = back[f]-branch

        result = toNum.filter_Branch(r)
        return result

    def show_roads_LookUp(f=[8]):
        for i in range(4):
            x = Roads.see_road(f[4], f[7-(2*i)])
            c = Fives.stemfives(f[2*(3-i)])
            print(f'{Fives.colors(c)}{nm.Road(x).name}', end=' ')
        print('\033[37m')

    def show_roads_seat(f=[8]):
        p = []
        q = []
        r = []

        for i in range(4):
            # n = 7, 5, 3, 1
            n= 7 - (2 * i)
            # x = 여기 천간 숫자 (1~10; 甲, 乙 ... 壬, 癸)
            x = toList.men_in_branch(f[n])[0]
            p.append(Fives.stemfives(x))
            p.append(Roads.see_road(x, f[n]))

            # y = 중기 천간 숫자 (0~10; ㆍ, 甲, 乙 ... 壬, 癸)
            y = toList.men_in_branch(f[n])[1]
            if y != 0:
                q.append(Fives.stemfives(y))
                q.append(Roads.see_road(y, f[n]))
            else:
                q.append(Fives.stemfives(x))
                q.append(0)

            # z = 중기 천간 숫자 (1~10; 甲, 乙 ... 壬, 癸)
            z = toList.men_in_branch(f[n])[2]
            r.append(Fives.stemfives(z))
            r.append(Roads.see_road(z, f[n]))

        for a in range(8): # 0, 1, 2, 3, 4, 5, 6, 7
            if a == 7: # 6
                print(f'{nm.Road(p[a]).name}\033[37m', end='\n')
            elif a %2 == 0: # 0, 2, 4
                print(f'{Fives.colors(p[a])}', end='')
            elif a %2 != 0: # 1, 3, 5, 7
                print(f'{nm.Road(p[a]).name}', end=' ')

        for a in range(8):
            # 0, 1, 2, 3, 4, 5, 6, 7
            # 중기(q리스트)에서 짝수 번째: 색상 코드
            if a%2 == 0:
                color = Fives.colors(q[a]) if q[a] != 0 else Fives.colors(p[a])
                print(Fives.colors(q[a]), end='')
            # 중기(q리스트)에서 홀수 번째: 포태법 글자 코드
            else:
                # put (string), q[a] = 0인 경우 'ㆍ', 나머지는 포태법 글자 그대로 쓰기
                put = nm.Road(q[a]).name if q[a] != 0 else 'ㆍ'
                ent = '\n' if a == 7 else ' '
                print(put, end=ent)

        for a in range(8):
            if a == 7:
                print(f'{nm.Road(r[a]).name}\033[37m', end='\n')
            elif a %2 == 0:
                print(f'{Fives.colors(r[a])}', end='')
            elif a % 2 != 0:
                print(f'{nm.Road(r[a]).name}', end=' ')


    def show_roads_stay(f=[8]):
        s = []
        for i in range(4):
            sky = f[6-(2*i)]
            land = f[7-(2*i)]
            s.append(Fives.stemfives(sky))
            x = Roads.see_road(sky, land)
            s.append(x)

        for i in range(4):
            if i == 3:
                print(f'{Fives.colors(s[2*i])}{nm.Road(s[2*i+1]).name}\033[37m', end='\n')
            else:
                print(f'{Fives.colors(s[2*i])}{nm.Road(s[2*i+1]).name}', end=' ')


class Destiny:

    # 시주 찾기 day_cycle: 1~60 수
    def find_time_cycle(day_cycle, hour, min):

        min -= 33
        if min < 0:
            min += 60
            hour -= 1
        if hour < 0:
            hour += 24

        hour = int((hour + 1) / 2) + 1
        cycle_time = toList.find_cycle(day_cycle, hour)

        return cycle_time

    # 절입일 # 1~12
    def first_day(month):
        days = [5, 4, 5, 4, 5, 5, 7, 7, 7, 8, 7, 7]
        return days[month-1]

    def last_day(month):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days[month-1]

    # 월차 조정일
    def adjust(month):
        d = [0, 31, -1, 30, 0, 31, 1, 32, 3, 33, 4, 34]
        return d[month-1]

    # 일주 찾기 (리스트형)
    def cycle(born_year, born_month, born_day):
        result = []
        a= born_year % 80
        b = 21*(int(a/4))
        c = 5*(a%4)
        f = b + c + 55 + born_day + Destiny.adjust(born_month)
        result = [toNum.filter_Stem(f), toNum.filter_Branch(f)]
        return result

    # 야자시를 위한 일주 찾기 (리스트형)
    def cycle_day(sky, land, hour, minute):
        if hour == 23 and minute >= 33:
            sky += 1
            land += 1
        result = [sky, land]
        return result

    # 년주 찾기 (리스트형)
    def cycle_year(born_year, born_month, born_day):
        year = born_year
        month = born_month
        if month ==1:
            year -= 1
        if month ==2 and born_day < Destiny.first_day(month):
            year -= 1
        year = (year - 3) % 60
        if year <= 0:
            year += 60
        result = [toNum.filter_Stem(year), toNum.filter_Branch(year)]
        return result

    # 월주 찾기 (리스트형)
    def cycle_month(born_year, born_month, born_day):
        year_cycle = (born_year-3)%60
        if year_cycle == 0:
            year_cycle = 60
        zodiac = born_month + 1
        if born_day < Destiny.first_day(born_month):
            zodiac -= 1
        result = toList.find_cycle(year_cycle, zodiac)
        return result

    def fortune(born_year, born_month, born_day, born_hour, born_min):
        sky = Destiny.cycle(born_year, born_month, born_day)[0]
        land = Destiny.cycle(born_year, born_month, born_day)[1]
        lord = toNum.cycle2num(sky, land)
        # [생년, 생월, 생일로 년주 출력하기] #
        y = Destiny.cycle_year(born_year, born_month, born_day)
        # [생년, 생월, 생일로 월주 출력하기] #
        m = Destiny.cycle_month(born_year, born_month, born_day)
        # [일간, 일지, 생시, 생분으로 야자시 일주 출력하기] #
        d = Destiny.cycle_day(sky, land, born_hour, born_min)
        # [생일, 생시, 생분으로 시주 출력하기] #
        t = Destiny.find_time_cycle(lord, born_hour, born_min)
        # result =[ 년간, 년지, 월간, 월지, 일간, 일지, 시간, 시지 ]
        result =[int(y[0]), int(y[1]), int(m[0]), int(m[1]), int(d[0]), int(d[1]), int(t[0]), int(t[1])]
        return  result

class Base:

    # 지지(정기 천간) 나열 = mens(f,2)[0], mens(f,2)[1], mens(f,2)[2], mens(f,2)[3]
    def mens(f=[8], n=2):
        result = [toList.men_in_branch(f[1])[n],
                  toList.men_in_branch(f[3])[n],
                  toList.men_in_branch(f[5])[n],
                  toList.men_in_branch(f[7])[n]]
        return result

    def show_mens(f = [8]):
        result = []
        for i in range(4):
            xi = toList.men_in_branch(f[7 - 2*i])[0]
            result.append(nm.Stem(xi).name)
        for i in range(4):
            yi = toList.men_in_branch(f[7 - 2*i])[1]
            if yi == 0:
                result.append('ㆍ')
            else:
                result.append(nm.Stem(yi).name)
        for i in range(4):
            zi = toList.men_in_branch(f[7 - 2*i])[2]
            result.append(nm.Stem(zi).name)
        return result

    # 지지 나열 (십성) = 년주 부터 deities(f)[1], deities(f)[3], deities(f)[4], deities(f)[5]
    def deities(f = [8]):
        d1, d3, d7 = toNum.deity_stem2stem(f[4], f[0]), \
                     toNum.deity_stem2stem(f[4], f[2]), \
                     toNum.deity_stem2stem(f[4], f[6])
        x1, x2, x3, x4 = Base.mens(f)[0], Base.mens(f)[1], Base.mens(f)[2], Base.mens(f)[3]
        d2, d4, d6, d8 = toNum.deity_stem2stem(f[4], x1), \
                         toNum.deity_stem2stem(f[4], x2), \
                         toNum.deity_stem2stem(f[4], x3), \
                         toNum.deity_stem2stem(f[4], x4)
        result = [d1, d2, d3, d4, d6, d7, d8]
        return result

    def lucks(f=[8], born_year =1, born_month=1, born_day=1, sex=1):
        now = time.localtime().tm_year
        age = now - born_year
        point = 0 #대운수
        c_year = toNum.cycle2num(f[0], f[1])
        cycleM = [f[2], f[3]]
        arrow1 = []
        arrow2 = []

        go = True
        if sex % 2 != c_year % 2:
            go = False

        prev = born_month-1
        if prev <= 0:
            prev += 12

        next = born_month + 1
        if next >= 12:
            next -= 12

        start0 = Destiny.first_day(prev)
        start1 = Destiny.first_day(born_month)
        start2 = Destiny.first_day(next)

        count = 0
        lucks = []
        if go == True:
            if born_day <= start1:
                count = start1 - born_day
            else:
                count = start2 + Destiny.last_day(born_month) - born_day
            for i in range(1, 11):
                goSky = toNum.filter_Stem(cycleM[0] + i)
                goLand = toNum.filter_Branch(cycleM[1] + i)
                lucks.append([round(count/3) + (i-1)*10, goSky, goLand])
        else:
            if born_day <= start1:
                count = Destiny.last_day(prev) + born_day - start0 # 2022-04-23 수정
            else:
                count = born_day - start1
            for i in range(1, 11):
                revSky = toNum.filter_Stem(cycleM[0] -i)
                revLand = toNum.filter_Branch(cycleM[1] - i)
                lucks.append([round(count/3) + (i-1)*10, revSky, revLand])

        for i in range(10):
            k = lucks[9 - i]
            if age >= k[0] and age < k[0] + 10:
                point = k[0] #대운수 자리
                arrow1.append('▼')
                arrow1.append('\t')
            else:
                arrow1.append('  ')
                arrow1.append('\t')

        ## 세운

        micro = []
        s = toList.num2cycle((point + born_year)-3)
        ord = age - point

        for num in range(10):
            yearNum = point + born_year + num
            pYear = yearNum % 100
            micro.append([pYear, toNum.filter_Stem(s[0] + num), toNum.filter_Branch(s[1] + num)])

        for num in range(10):
            if 9 - num == ord:
                arrow2.append('▼')
                arrow2.append('\t')
            else:
                arrow2.append('  ')
                arrow2.append('\t')

        return lucks, micro, arrow1, arrow2


class Format:

    def seasons(branch):
        s = [1, 1, 3, 3, 3, 2, 2, 2, 4, 4, 4, 1]
        return s[branch-1]

    def trium(branch):
        t = [1, 4, 2, 3, 1, 4, 2, 3, 1, 4, 2, 3]
        return t[branch-1]

    def key4target(deity):
        s = [[7, 6], [6, 7], [5, 6, 9], [9, 4, 5], [2, 3, 7], [2, 3, 7], [2, 8, 9, 3], [9, 4, 5], [4, 6, 7], [7, 3, 2]]
        keys = s[int(deity)]
        return keys

    def takeForm(f=[8]):
        moon = f[3]
        lunar = toList.men_in_branch(moon)[2]
        lord = f[4]

        target = 0
        plus = 0

        for sky in range(4):
            s = f[2 * sky]
            if Format.seasons(moon) == Fives.stemfives(s) and sky != 2:
                target = s
            elif Format.trium(moon) == Fives.stemfives(s) and sky != 2:
                if Format.trium(moon) == Format.trium(f[1]) or Format.trium(moon) == Format.trium(f[5]):
                    plus += 1
        if target == 0:
            for land in range(4):
                if Format.trium(moon) == Format.trium(f[2 * land - 1]) and land != 1:
                    plus += 1
        if plus >= 3:
            target = s

        if target != 0:
            form = toNum.deity_stem2stem(lord, target)
        else:
            form = toNum.deity_stem2stem(lord, lunar)

        return form

    def formula(f=[8]):
        d = []
        k = Format.takeForm(f)
        keys = Format.key4target(k)
        for i, con in enumerate(keys):
            for j in range(4):
                if con == toNum.deity_stem2stem(f[4], f[2*j]) and j != 2:
                    d.append(con)
        return d, k

class PrintOut:

    def print_fortune(f=[8]):
        col = toList.all_fives(f)
        c = [Fives.colors(col[0]), Fives.colors(col[1]), Fives.colors(col[2]), Fives.colors(col[3]), Fives.colors(col[4]), Fives.colors(col[5]), Fives.colors(col[6]), Fives.colors(col[7])]
        print(c[6] + nm.Stem(f[6]).name + ' ' + c[4] + nm.Stem(f[4]).name + ' ' + c[2] + nm.Stem(f[2]).name + ' ' + c[0] + nm.Stem(f[0]).name + ' ' + '\033[0m')
        print(c[7] + nm.Branch(f[7]).name + ' ' + c[5] + nm.Branch(f[5]).name + ' ' + c[3] + nm.Branch(f[3]).name + ' ' + c[1] + nm.Branch(f[1]).name + ' ' + '\033[0m')

    def print_deities(f=[8]):
        col = toList.all_fives(f)
        c = [Fives.colors(col[0]), Fives.colors(col[1]), Fives.colors(col[2]), Fives.colors(col[3]), Fives.colors(col[4]), Fives.colors(col[5]), Fives.colors(col[6]),Fives.colors(col[7])]
        d = Base.deities(f)
        print(c[6] + nm.Deity(d[5]).name + ' '
              + c[4] + '我神' + ' '
              + c[2] + nm.Deity(d[2]).name + ' '
              + c[0] + nm.Deity(d[0]).name + ' '
              + '\033[0m')
        print(c[7] + nm.Deity(d[6]).name + ' '
              + c[5] + nm.Deity(d[4]).name + ' '
              + c[3] + nm.Deity(d[3]).name + ' '
              + c[1] + nm.Deity(d[1]).name + ' '
              + '\033[0m')

    def print_mens(f=[8]):
        p = Base.show_mens(f)
        for i, con in enumerate(p):
            x = nm.Stem[con].value if con != 'ㆍ' else nm.Stem[p[i-4]].value
            c_num = int(Fives.stemfives(x))
            ent = '\n' if i==3 or i==7 else ' '
            print(f'{Fives.colors(c_num)}{con}', end=ent)
        print('\033[0m')

    def print_keys(f=[8]):
        form = Format.takeForm(f)
        keys = Format.key4target(form)
        key = 10
        for i in range(len(keys)):
            k = keys[i]
            for s in range(4):
                if k == toNum.deity_stem2stem(f[4], f[2 * s]) and s != 2:
                    key = k
                    break
        if key != 10:
            print(f'{nm.Deity(key).name}을 용하는 {nm.Deity(form).name}격')
        elif key == 10:
            print(f'{nm.Deity(form).name}격')

    def print_lucks(f=[8], born_year =1, born_month=1, born_day=1, sex=1):
        now = time.localtime().tm_year
        age = now - born_year
        point = 0 #대운수
        c_year = toNum.cycle2num(f[0], f[1])
        cycleM = [f[2], f[3]]
        arrow1 = []
        arrow2 = []

        go = True
        if sex % 2 != c_year % 2:
            go = False

        prev = born_month-1
        if prev <= 0:
            prev += 12

        next = born_month + 1
        if next >= 12:
            next -= 12

        start0 = Destiny.first_day(prev)
        start1 = Destiny.first_day(born_month)
        start2 = Destiny.first_day(next)

        count = 0
        lucks = []
        if go == True:
            if born_day <= start1:
                count = start1 - born_day
            else:
                count = start2 + Destiny.last_day(born_month) - born_day
            for i in range(1, 11):
                goSky = toNum.filter_Stem(cycleM[0] + i)
                goLand = toNum.filter_Branch(cycleM[1] + i)
                lucks.append([round(count/3) + (i-1)*10, goSky, goLand])
        else:
            if born_day <= start1:
                count = Destiny.last_day(prev) + born_day - start0 # 2022-04-23 수정
            else:
                count = born_day - start1
            for i in range(1, 11):
                revSky = toNum.filter_Stem(cycleM[0] -i)
                revLand = toNum.filter_Branch(cycleM[1] - i)
                lucks.append([round(count/3) + (i-1)*10, revSky, revLand])

        for i in range(10):
            k = lucks[9 - i]
            if age >= k[0] and age < k[0] + 10:
                point = k[0] #대운수 자리
                if i == 9:
                    print('▼', end='\n')
                else:
                    print('▼', end='\t')
                arrow1.append('▼')
                arrow1.append('\t')
            else:
                if i == 9:
                    print('  ', end='\n')
                else:
                    print('  ', end='\t')
                arrow1.append('  ')
                arrow1.append('\t')

        for i in range(10):
            k = lucks[9 - i]
            if k[0] < 10 and k[0] >= 0: # 대운수 표기
                print(f'0{k[0]}', end='\n')
            elif k[0] >= 10 and i == 9:
                print(k[0], end='\n')
            else:
                print(k[0], end='\t')

        for i in range(10):
            k = lucks[9 - i]
            name = nm.Stem(k[1]).name
            color = Fives.colors(Fives.stemfives(k[1]))
            if i == 9:
                print(f'{color + name}', end='\n')
            else:
                print(f'{color + name}', end='\t')

        for i in range(10):
            k = lucks[9 - i]
            name = nm.Branch(k[2]).name
            x = toList.men_in_branch(k[2])[2]
            color = Fives.colors(Fives.stemfives(x))
            if i == 9:
                print(f'{color + name}', end='\n')
            else:
                print(f'{color + name}', end='\t')

        print('\033[37m')
        ## 세운

        micro = []
        s = toList.num2cycle((point + born_year)-3)
        ord = age - point

        for num in range(10):
            yearNum = point + born_year + num
            pYear = yearNum % 100
            micro.append([pYear, toNum.filter_Stem(s[0] + num), toNum.filter_Branch(s[1] + num)])

        for num in range(10):
            if 9 - num == ord:
                if num == 9:
                    print('▼', end='\n')
                else:
                    print('▼', end='\t')
                arrow2.append('▼')
                arrow2.append('\t')
            else:
                if num == 9:
                    print('  ', end='\n')
                else:
                    print('  ', end='\t')
                arrow2.append('  ')
                arrow2.append('\t')

        for num in range(10):
            if num == 9:
                print(f'{micro[9-num][0]}\'', end='\n')
            else:
                print(f'{micro[9-num][0]}\'', end='\t')

        for num in range(10):
            n = micro[9-num]
            name = nm.Stem(n[1]).name
            color = Fives.colors(Fives.stemfives(n[1]))
            if num == 9:
                print(f'{color+name}', end='\n')
            else:
                print(f'{color + name}', end='\t')

        for num in range(10):
            n = micro[9-num]
            name = nm.Branch(n[2]).name
            color = Fives.colors(Fives.stemfives(toList.men_in_branch(n[2])[2]))
            if num == 9:
                print(f'{color+name}', end='\n')
            else:
                print(f'{color + name}', end='\t')
        print('\033[37m')

        return lucks, micro, arrow1, arrow2
