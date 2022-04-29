import names as nm
from functions import Fives as f
from functions import  toNum as num
from functions import  toList as lst
from functions import Destiny as d
from functions import Roads as r
from functions import PrintOut as p


if __name__ == '__main__':
    while True:
        flag = 0
        while True:
            sex = int(input('\033[37m성별 [0:여자 / 1:남자]: '))
            if sex !=0 and sex !=1:
                print('Try again')
            else:
                break

        year = int(input('생년: '))
        month = int(input('생월: '))
        day = int(input('생일: '))
        hour = int(input("생시 (00~23): "))
        minute = int(input("생분 (00~59): "))

        fortune = d.fortune(year, month, day, hour, minute)
        # 사주 원국 출력
        print('=========사주원국======')
        p.print_fortune(fortune)
        print('========지장간========')
        p.print_mens(fortune)
        print('=========십이운성======')
        print('========봉법==========')
        r.show_roads_LookUp(fortune)
        print('========좌법==========')
        r.show_roads_seat(fortune)
        print('========거법==========')
        r.show_roads_stay(fortune)
        print('========육친==========')
        lunar = fortune[3]
        lord = fortune[4]
        p.print_deities(fortune)
        print('========대운==========')
        p.print_lucks(fortune, year, month, day, sex)
        print('=====================')
        print(f'{nm.Branch(lunar).name}월의 {nm.Stem(lord).name}{nm.Five(f.stemfives(lord)).name}')
        p.print_keys(fortune)

#===========================================================================#
        key = 0
        while True:
            ending = input('Exit? [y/n]:\n')
            if ending == 'y':
                key = 1
                print('>>> Good bye! \n')
                break
            elif ending == 'n':
                print('>>> Continue...\n')
                break
            else:
                print('>>> Wrong answer. Try again.\n')

        if key == 1:
            break
#===========================================================================#