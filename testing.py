import names as nm
import functions as fx

if __name__ == '__main__':
    while True:

        # year = int(input('생년: '))
        # month = int(input('생월: '))
        # day = int(input('생일: '))
        # hour = int(input("생시 (00~23): "))
        # minute = int(input("생분 (00~59): "))
        #
        # f = fx.fortune(year, month, day, hour, minute)
        # lord = f[4]
        # lunar = f[3]
        #
        # print(f'{nm.Branch(lunar).name}월의 {nm.Stem(lord).name}')
        #사주 원국 출력
        # print('=========사주원국==========')
        # col = fx.all_fives(f)
        # c = [fx.colors(col[0]), fx.colors(col[1]), fx.colors(col[2]), fx.colors(col[3]), fx.colors(col[4]), fx.colors(col[5]), fx.colors(col[6]), fx.colors(col[7])]
        # print(c[6] + nm.Stem(f[6]).name +' '+ c[4] + nm.Stem(f[4]).name +' '+ c[2] + nm.Stem(f[2]).name +' '+ c[0] + nm.Stem(f[0]).name + ' ' + '\033[0m')
        # print(c[7] + nm.Branch(f[7]).name +' '+ c[5] + nm.Branch(f[5]).name +' '+ c[3] + nm.Branch(f[3]).name +' '+ c[1] + nm.Branch(f[1]).name + ' ' + '\033[0m')
        # print('==========================')
        # moon = f[3]
        # lord = f[4]
        # d = fx.deities(f)
        # print(c[6] + nm.Deity(d[5]).name + ' ' + c[4] + '我神' + ' ' + c[2] + nm.Deity(d[2]).name + ' ' + c[0] + nm.Deity(d[0]).name + ' ' + '\033[0m')
        # print(c[7] + nm.Deity(d[6]).name + ' ' + c[5] + nm.Deity(d[4]).name + ' ' + c[3] + nm.Deity(d[3]).name + ' ' + c[1] + nm.Deity(d[1]).name + ' ' + '\033[0m')
        # print('=========지장간===========')
        # p = fx.show_mens(f)
        # for t in range(3):
        #     print(fx.colors(fx.fives(fx.men_in_branch(f[7])[t])) + p[4*t] + ' ' + fx.colors(fx.fives(fx.men_in_branch(f[5])[t])) + p[4*t+1] + ' ' + fx.colors(fx.fives(fx.men_in_branch(f[3])[t])) + p[4*t+2] + ' ' + fx.colors(fx.fives(fx.men_in_branch(f[1])[t])) + p[4*t+3] + ' ' + '\033[0m')
        # print('==========================')
        # print(f'{nm.Branch(moon).name}월의 {nm.Stem(lord).name}{nm.Five(fx.fives(lord)).name}')
        #
        #
        # form = fx.takeForm(f)
        # keys = fx.key4target(form)
        #
        # key = 10
        # for i in range(len(keys)):
        #     k = keys[i]
        #     for s in range(4):
        #         if k == fx.deity_stem2stem(f[4], f[2*s]) and s != 2:
        #             key = k
        #             break
        # if key != 10:
        #     print(f'{nm.Deity(key).name}을 용하는 {nm.Deity(form).name}격')
        # elif key == 10:
        #     print(f'{nm.Deity(form).name}격')




        # [숫자로 지지의 지장간 출력하기]===================================================================#
        # b = int(input('1~12 중 십이지지 선택: '))
        # b = fx.filter_Branch(b)
        # print(nm.Branch(b).name)
        # print(nm.Stem(int(fx.men_in_branch(b)[0])).name + "\n" + nm.Stem(int(fx.men_in_branch(b)[1])).name + "\n" + nm.Stem(int(fx.men_in_branch(b)[2])).name)

        #[60 숫자로 60갑자 출력하기]======================================================================#
        # cyc = int(input('1~60 중 1 선택: '))
        # print(fx.num2cycle(cyc))
        # print(nm.Stem(fx.num2cycle(cyc)[0]).name +'\n'+ nm.Branch(fx.num2cycle(cyc)[1]).name)
        # ============================================================================================#

        #[숫자로 천간 십성 출력하기]=======================================================================#
        # me = int(input('숫자를 입력하세요:\n'))
        # who = int(input('숫자를 입력하세요:\n'))
        #
        # me = fx.filter_Stem(me)
        # who = fx.filter_Stem(who)
        #
        # print(nm.Stem(me).name + " --> " + nm.Stem(who).name)
        # print(nm.Deity(fx.deity_stem2stem(me, who)).name)
        #============================================================================================#

#===========================================================================#
        key = 0
        while True:
            ending = input('끝내시겠습니까? [y/n]:\n')
            if ending == 'y':
                key = 1
                print('종료합니다. \n')
                break
            elif ending == 'n':
                break
            else:
                print('잘못 입력했습니다.\n')

        if key == 1:
            break
#===========================================================================#