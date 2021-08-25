from enum import Enum

class SunOrMoon(Enum):
    陰 = 0 # minus
    陽 = 1 # plus

class Sex(Enum):
    坤 = 0 # Female
    乾 = 1 # Male

class Five(Enum):
    水 = 1 # 9, 10 # '\33[44m'
    火 = 2 # 3, 4 # '\33[41m'
    木 = 3 # 1, 2 # '\33[42m'
    金 = 4 # 7, 8 # '\33[107m'
    土 = 5 # 5, 6 # '\33[43m'

class Stem(Enum):
    甲=1
    乙=2
    丙=3
    丁=4
    戊=5
    己=6
    庚=7
    辛=8
    壬=9
    癸=10

class Branch(Enum):
    子=1
    丑=2
    寅=3
    卯=4
    辰=5
    巳=6
    午=7
    未=8
    申=9
    酉=10
    戌=11
    亥=12

class Deity(Enum):
    比肩=0
    劫財=1
    食神=2
    傷官=3
    偏財=4
    正財=5
    七殺=6
    正官=7
    梟神=8
    正印=9

class Road(Enum):
    絶=1
    胎=2
    養=3
    生=4
    浴=5
    帶=6
    祿=7
    旺=8
    衰=9
    病=10
    死=11
    墓=12

