from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1500.bin",                # FileName
        "r1500",                    # MapName
        "r1500",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("r1500", "r0000_1", "", "", "", ""),   # include
        0x05,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, -65000, 0, 0, 1, 96, 0, 1, 0, 2],
    )

    BuildStringList((
        "r1500",                  # 0
        "Citizen",                # 1
        "Citizen",                # 2
        "Citizen",                # 3
        "Citizen",                # 4
        "Citizen",                # 5
        "Citizen",                # 6
        "Citizen",                # 7
        "Detective",              # 8
        "Citizen",                # 9
        "Citizen",                # 10
        "Girl",                   # 11
        "Citizen",                # 12
        "Tourist",                # 13
        "Citizen",                # 14
        "Citizen",                # 15
        "Citizen",                # 16
        "Citizen",                # 17
        "Citizen",                # 18
        "Tourist",                # 19
        "Reporter",               # 20
        "Reporter",               # 21
        "Tourist",                # 22
        "Tourist",                # 23
        "Tourist",                # 24
        "Tourist",                # 25
        "Tourist",                # 26
        "Tourist",                # 27
        "Tourist",                # 28
        "Tourist",                # 29
        "Citizen",                # 30
        "Billy",                  # 31
        "Transportation Division Officer",# 32
        "Detective Raymond",      # 33
        "Detective Emma",         # 34
        "Inspector Donovan",      # 35
        "Bus",                    # 36
        "バス待ち",               # 37
        "バス待ち",               # 38
        "バス待ち",               # 39
        "バス待ち",               # 40
        "Transportation Division Officer",# 41
        "Zeit",                   # 42
        "ビリーのバン",           # 43
        "SE制御",                 # 44
        "br1500",                 # 45
        "br1500",                 # 46
        "br1500",                 # 47
        "br1500",                 # 48
        "br1500",                 # 49
        "To Crossbell City",      # 50
        "To St. Ursula Medical College",# 51
        "To Crossbell Airport",   # 52
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 4,   2,   0,   8,   0,   3,   2)
    Sepith("Sepith_B4", 8,   2,   0,   0,   3,   0,   5)
    Sepith("Sepith_C4", 0,   8,   0,   4,   4,   2,   0)
    Sepith("Sepith_D4", 8,   0,   5,   2,   0,   0,   4)
    Sepith("Sepith_E4", 2,   8,   0,   6,   2,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_F4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_118", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_11C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_120", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_124", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_128", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_12C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_134", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_144", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_148", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_14C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_150", 2, 13, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_154", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_A4", 30, 45, 20, 5,
        (
            ("ms62100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62100.dat", "ms62100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62100.dat", "ms69700.dat", "ms62100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62100.dat", "ms62100.dat", "ms65800.dat", "ms62100.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_21C", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms65800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65800.dat", "ms65800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65800.dat", "ms63600.dat", "ms65800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65800.dat", "ms65800.dat", "ms66600.dat", "ms65800.dat", 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_2E4", 0x0010, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_C4", 60, 25, 10, 5,
        (
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63600.dat", "ms66600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "ms63600.dat", 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63600.dat", "ms63600.dat", "ms62100.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3AC", 0x0000, 12, 6, 45, 10, 1, 45, 0, "br1500", "Sepith_D4", 30, 45, 20, 5,
        (
            ("ms66600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66600.dat", "ms66600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66600.dat", "ms62100.dat", "ms66600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66600.dat", "ms66600.dat", "ms69700.dat", "ms66600.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_474", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_E4", 30, 45, 20, 5,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", "ms69800.dat", 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    AddCharChip((
        "chr/ch28100.itc",                   # 00
        "chr/ch21900.itc",                   # 01
        "chr/ch20800.itc",                   # 02
        "chr/ch24400.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch21600.itc",                   # 05
        "chr/ch21100.itc",                   # 06
        "chr/ch23600.itc",                   # 07
        "chr/ch21200.itc",                   # 08
        "chr/ch21300.itc",                   # 09
        "chr/ch21000.itc",                   # 0A
        "chr/ch20700.itc",                   # 0B
        "chr/ch20300.itc",                   # 0C
        "chr/ch21800.itc",                   # 0D
        "chr/ch20000.itc",                   # 0E
        "chr/ch20100.itc",                   # 0F
        "chr/ch20200.itc",                   # 10
        "chr/ch20400.itc",                   # 11
        "chr/ch23700.itc",                   # 12
        "chr/ch24500.itc",                   # 13
        "chr/ch27800.itc",                   # 14
        "chr/ch28100.itc",                   # 15
        "chr/ch30200.itc",                   # 16
        "chr/ch30500.itc",                   # 17
        "chr/ch30300.itc",                   # 18
        "chr/ch26800.itc",                   # 19
        "chr/ch22100.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
        "monster/ch62150.itc",               # 1E
        "monster/ch62151.itc",               # 1F
        "monster/ch66650.itc",               # 20
        "monster/ch66651.itc",               # 21
        "monster/ch63650.itc",               # 22
        "monster/ch63650.itc",               # 23
        "monster/ch65850.itc",               # 24
        "monster/ch65851.itc",               # 25
        "monster/ch69750.itc",               # 26
        "monster/ch69750.itc",               # 27
    ))

    DeclNpc(-9779,   180,     -10890,  135,  389,  0x0, 0,   1,   0,   0,   0,   0,   35,  255,  0)
    DeclNpc(-9560,   180,     -8470,   135,  389,  0x0, 0,   2,   0,   0,   0,   0,   36,  255,  0)
    DeclNpc(-9479,   180,     -7039,   315,  389,  0x0, 0,   3,   0,   0,   0,   0,   37,  255,  0)
    DeclNpc(-9409,   180,     -5860,   225,  389,  0x0, 0,   4,   0,   0,   0,   0,   38,  255,  0)
    DeclNpc(-8899,   180,     -4000,   90,   389,  0x0, 0,   5,   0,   0,   0,   0,   39,  255,  0)
    DeclNpc(-7699,   180,     -4000,   270,  389,  0x0, 0,   6,   0,   0,   0,   0,   40,  255,  0)
    DeclNpc(-10020,  180,     -9489,   180,  389,  0x0, 0,   7,   0,   0,   0,   0,   41,  255,  0)
    DeclNpc(12989,   0,       -17559,  270,  389,  0x0, 0,   20,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(-9810,   180,     -9920,   180,  389,  0x0, 0,   9,   0,   0,   0,   0,   43,  255,  0)
    DeclNpc(-7010,   180,     -4260,   90,   389,  0x0, 0,   10,  0,   0,   0,   0,   44,  255,  0)
    DeclNpc(9979,    0,       -14819,  180,  389,  0x0, 0,   11,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(9859,    0,       -16450,  0,    389,  0x0, 0,   12,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10609,   0,       -14939,  270,  389,  0x0, 0,   13,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(10609,   0,       -14939,  270,  389,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(10609,   0,       -14939,  270,  389,  0x0, 0,   1,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(9979,    0,       -14819,  180,  389,  0x0, 0,   14,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(9859,    0,       -16450,  0,    389,  0x0, 0,   15,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(10609,   0,       -14939,  90,   389,  0x0, 0,   16,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(10609,   0,       -14939,  270,  389,  0x0, 0,   25,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(9979,    0,       -14819,  180,  389,  0x0, 0,   10,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(9859,    0,       -16450,  0,    389,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(9979,    0,       -14819,  180,  389,  0x0, 0,   3,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(9859,    0,       -16450,  0,    389,  0x0, 0,   19,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(9979,    0,       -14819,  180,  389,  0x0, 0,   18,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(9859,    0,       -16450,  0,    389,  0x0, 0,   26,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(5340,    0,       -20360,  0,    389,  0x0, 0,   19,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(5340,    0,       -19159,  180,  389,  0x0, 0,   3,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(9859,    0,       -16450,  0,    389,  0x0, 0,   1,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(9979,    0,       -14819,  180,  389,  0x0, 0,   13,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(10609,   0,       -14939,  270,  389,  0x0, 0,   20,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(4980,    0,       -12670,  270,  389,  0x0, 0,   7,   0,   0,   0,   0,   31,  255,  0)
    DeclNpc(2210,    0,       -34220,  270,  389,  0x0, 0,   21,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(-5639,   180,     -4260,   270,  389,  0x0, 0,   22,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(13060,   0,       -16149,  180,  389,  0x0, 0,   23,  0,   0,   0,   0,   45,  255,  0)
    DeclNpc(11449,   0,       -15000,  180,  389,  0x0, 0,   24,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-18740,  -70990,  0,       0x1010000,    "BattleInfo_154", 0,   30,  0xFFFF, 0,  1)
    DeclMonster(-19320,  -73460,  10,      0x1010000,    "BattleInfo_154", 0,   30,  0xFFFF, 0,  1)
    DeclMonster(-9910,   -96620,  10,      0x1010000,    "BattleInfo_21C", 0,   36,  0xFFFF, 6,  7)
    DeclMonster(-20260,  -97980,  0,       0x1010000,    "BattleInfo_2E4", 0,   34,  0xFFFF, 4,  5)
    DeclMonster(16920,   -84000,  10,      0x1010000,    "BattleInfo_21C", 0,   36,  0xFFFF, 6,  7)
    DeclMonster(22580,   -65740,  10,      0x1010000,    "BattleInfo_3AC", 0,   32,  0xFFFF, 2,  3)
    DeclMonster(32310,   -111280, 0,       0x1010000,    "BattleInfo_474", 0,   38,  0xFFFF, 8,  9)
    DeclMonster(46440,   -108530, 900,     0x1010000,    "BattleInfo_3AC", 0,   32,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 66,  14.0,                  -17.5,                 -0.5,                  100.0,                 [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.09999999403953552,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -7.0,                  1.7499998807907104,    0.09999999403953552,   1.0])

    DeclActor(-10300,  180,     -13000,  1500,    -10300,  1680,    -13000,  0x007C, 0,  47, 0x0000)
    DeclActor(53350,   900,     -104390, 1200,    67060,   -5900,   -100200, 0x007C, 0,  46, 0x0000)
    DeclActor(22470,   0,       -63690,  1200,    22470,   0,       -63690,  0x007C, 0,  3,  0x0000)
    DeclActor(8160,    0,       -11670,  1200,    8160,    2000,    -11670,  0x007C, 0,  10, 0x0000)
    DeclActor(44690,   900,     -108690, 7500,    44690,   900,     -108690, 0x007C, 0,  64, 0x0000)
    DeclActor(9210,    0,       -24210,  1500,    9210,    1700,    -24210,  0x007C, 0,  69, 0x0000)

    PlaceName(2.0, 0.0, 20.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(-27.0, 0.0, -159.0, 0x0000, 0x0000, "To St. Ursula Medical College")
    PlaceName(45.0, 0.0, -24.0, 0x0000, 0x0000, "To Crossbell Airport")
    PlaceName(-10.649999618530273, 0.0, -11.800000190734863, 0x0000, 0x0055, "")
    PlaceName(8.25, 0.0, -10.0, 0x0000, 0x0056, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5, 6, 7])              # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9

    ScpFunction((
        "Function_0_ED8",          # 00, 0
        "Function_1_F90",          # 01, 1
        "Function_2_15A1",         # 02, 2
        "Function_3_19CB",         # 03, 3
        "Function_4_19DF",         # 04, 4
        "Function_5_1A2C",         # 05, 5
        "Function_6_1AE9",         # 06, 6
        "Function_7_1C6B",         # 07, 7
        "Function_8_1D00",         # 08, 8
        "Function_9_22D9",         # 09, 9
        "Function_10_23C8",        # 0A, 10
        "Function_11_23D6",        # 0B, 11
        "Function_12_246C",        # 0C, 12
        "Function_13_250D",        # 0D, 13
        "Function_14_25DA",        # 0E, 14
        "Function_15_2779",        # 0F, 15
        "Function_16_281B",        # 10, 16
        "Function_17_28AD",        # 11, 17
        "Function_18_29F1",        # 12, 18
        "Function_19_2B01",        # 13, 19
        "Function_20_2BAC",        # 14, 20
        "Function_21_2C80",        # 15, 21
        "Function_22_2D5D",        # 16, 22
        "Function_23_2DEE",        # 17, 23
        "Function_24_2E86",        # 18, 24
        "Function_25_2F45",        # 19, 25
        "Function_26_3015",        # 1A, 26
        "Function_27_307F",        # 1B, 27
        "Function_28_30EC",        # 1C, 28
        "Function_29_31D4",        # 1D, 29
        "Function_30_3296",        # 1E, 30
        "Function_31_3365",        # 1F, 31
        "Function_32_371A",        # 20, 32
        "Function_33_3CBE",        # 21, 33
        "Function_34_3D22",        # 22, 34
        "Function_35_4417",        # 23, 35
        "Function_36_4467",        # 24, 36
        "Function_37_44F4",        # 25, 37
        "Function_38_462E",        # 26, 38
        "Function_39_471F",        # 27, 39
        "Function_40_47A8",        # 28, 40
        "Function_41_482F",        # 29, 41
        "Function_42_48B8",        # 2A, 42
        "Function_43_4B74",        # 2B, 43
        "Function_44_4CB5",        # 2C, 44
        "Function_45_4D5A",        # 2D, 45
        "Function_46_5013",        # 2E, 46
        "Function_47_5352",        # 2F, 47
        "Function_48_545F",        # 30, 48
        "Function_49_74D2",        # 31, 49
        "Function_50_7516",        # 32, 50
        "Function_51_7B95",        # 33, 51
        "Function_52_7BB1",        # 34, 52
        "Function_53_7BD0",        # 35, 53
        "Function_54_7BE0",        # 36, 54
        "Function_55_7BFC",        # 37, 55
        "Function_56_7C21",        # 38, 56
        "Function_57_84F0",        # 39, 57
        "Function_58_8525",        # 3A, 58
        "Function_59_8536",        # 3B, 59
        "Function_60_85EA",        # 3C, 60
        "Function_61_8637",        # 3D, 61
        "Function_62_867A",        # 3E, 62
        "Function_63_A60E",        # 3F, 63
        "Function_64_A6E7",        # 40, 64
        "Function_65_B631",        # 41, 65
        "Function_66_BA62",        # 42, 66
        "Function_67_BCAC",        # 43, 67
        "Function_68_BE9F",        # 44, 68
        "Function_69_BF64",        # 45, 69
    ))


    def Function_0_ED8(): pass

    label("Function_0_ED8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_F18"),
        (1, "loc_F24"),
        (2, "loc_F30"),
        (3, "loc_F3C"),
        (4, "loc_F48"),
        (5, "loc_F54"),
        (6, "loc_F60"),
        (SWITCH_DEFAULT, "loc_F6C"),
    )


    label("loc_F18")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_F78")

    label("loc_F24")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_F78")

    label("loc_F30")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_F78")

    label("loc_F3C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_F78")

    label("loc_F48")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_F78")

    label("loc_F54")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_F78")

    label("loc_F60")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F78")

    label("loc_F6C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F78")

    label("loc_F78")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F8F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F78")

    label("loc_F8F")

    Return()

    # Function_0_ED8 end

    def Function_1_F90(): pass

    label("Function_1_F90")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xF9, 5)
    SetScenarioFlags(0xFB, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FB5")
    SetMapFlags(0x10000000)
    Event(0, 62)

    label("loc_FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_FC4")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 50)

    label("loc_FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1040")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xA, -10010, 180, -11740, 180)
    SetChrPos(0xB, -10010, 180, -10540, 180)
    SetChrPos(0xE, -10010, 180, -9240, 180)
    SetChrPos(0xF, -10010, 180, -8039, 180)
    SetChrPos(0x10, -10010, 180, -6840, 180)
    Jump("loc_1128")

    label("loc_1040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1084")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    SetChrPos(0xF, 15000, 0, -16570, 0)
    SetChrPos(0x29, 15000, 0, -15170, 180)
    Jump("loc_1128")

    label("loc_1084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_10A1")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x28, 0x80)
    Jump("loc_1128")

    label("loc_10A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 4)), scpexpr(EXPR_END)), "loc_10AF")
    Jump("loc_1128")

    label("loc_10AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_10C7")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_1128")

    label("loc_10C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_END)), "loc_10D5")
    Jump("loc_1128")

    label("loc_10D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1101")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x27, 0x80)
    Jump("loc_1128")

    label("loc_1101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_1128")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x27, 0x80)

    label("loc_1128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1136")
    Jump("loc_12B5")

    label("loc_1136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1144")
    Jump("loc_12B5")

    label("loc_1144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1157")
    ClearChrFlags(0x25, 0x80)
    Jump("loc_12B5")

    label("loc_1157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1165")
    Jump("loc_12B5")

    label("loc_1165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1182")
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x10)
    Jump("loc_12B5")

    label("loc_1182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_11A9")
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x10)
    SetChrFlags(0x21, 0x10)
    Jump("loc_12B5")

    label("loc_11A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_11CB")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x10)
    SetChrFlags(0x1F, 0x10)
    Jump("loc_12B5")

    label("loc_11CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_11E3")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_12B5")

    label("loc_11E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_122B")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1226")
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, 11450, 0, -16500, 0)
    ClearChrFlags(0x2A, 0x80)

    label("loc_1226")

    Jump("loc_12B5")

    label("loc_122B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_123E")
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_12B5")

    label("loc_123E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1251")
    ClearChrFlags(0x19, 0x80)
    Jump("loc_12B5")

    label("loc_1251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1269")
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_12B5")

    label("loc_1269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_127C")
    ClearChrFlags(0x16, 0x80)
    Jump("loc_12B5")

    label("loc_127C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_128F")
    ClearChrFlags(0x15, 0x80)
    Jump("loc_12B5")

    label("loc_128F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_12A2")
    ClearChrFlags(0x14, 0x80)
    Jump("loc_12B5")

    label("loc_12A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_12B5")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)

    label("loc_12B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_12C3")
    Jump("loc_12D3")

    label("loc_12C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12D3")
    Event(0, 4)

    label("loc_12D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12E9")
    Event(0, 63)

    label("loc_12E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_12F8")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 7)

    label("loc_12F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_1310")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)

    label("loc_1310")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15A0")
    ClearScenarioFlags(0x7A, 0)
    ClearScenarioFlags(0x7A, 1)
    ClearScenarioFlags(0x7A, 2)
    ClearScenarioFlags(0x7A, 3)
    ClearScenarioFlags(0x7A, 4)
    ClearScenarioFlags(0x7A, 5)
    ClearScenarioFlags(0x7A, 6)
    ClearScenarioFlags(0x7A, 7)
    ClearScenarioFlags(0x7B, 0)
    ClearScenarioFlags(0x7B, 1)
    ClearScenarioFlags(0x7B, 2)
    ClearScenarioFlags(0x7B, 3)
    ClearScenarioFlags(0x7B, 4)
    ClearScenarioFlags(0x7B, 5)
    ClearScenarioFlags(0x7B, 6)
    ClearScenarioFlags(0x7B, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137F")
    SetScenarioFlags(0x7A, 0)

    label("loc_137F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1395")
    SetScenarioFlags(0x7A, 1)

    label("loc_1395")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AB")
    SetScenarioFlags(0x7A, 2)

    label("loc_13AB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C1")
    SetScenarioFlags(0x7A, 3)

    label("loc_13C1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D7")
    SetScenarioFlags(0x7A, 4)

    label("loc_13D7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13ED")
    SetScenarioFlags(0x7A, 5)

    label("loc_13ED")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1403")
    SetScenarioFlags(0x7A, 6)

    label("loc_1403")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1419")
    SetScenarioFlags(0x7A, 7)

    label("loc_1419")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142F")
    SetScenarioFlags(0x7B, 0)

    label("loc_142F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1445")
    SetScenarioFlags(0x7B, 1)

    label("loc_1445")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145B")
    SetScenarioFlags(0x7B, 2)

    label("loc_145B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1471")
    SetScenarioFlags(0x7B, 3)

    label("loc_1471")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1487")
    SetScenarioFlags(0x7B, 4)

    label("loc_1487")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149D")
    SetScenarioFlags(0x7B, 5)

    label("loc_149D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B3")
    SetScenarioFlags(0x7B, 6)

    label("loc_14B3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C9")
    SetScenarioFlags(0x7B, 7)

    label("loc_14C9")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1504")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_15A0")

    label("loc_1504")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_151B")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_15A0")

    label("loc_151B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1532")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_15A0")

    label("loc_1532")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1549")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_15A0")

    label("loc_1549")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1560")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_15A0")

    label("loc_1560")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1577")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_15A0")

    label("loc_1577")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158E")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_15A0")

    label("loc_158E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A0")
    SetScenarioFlags(0x7C, 7)

    label("loc_15A0")

    Return()

    # Function_1_F90 end

    def Function_2_15A1(): pass

    label("Function_2_15A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F9")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15EB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15F4")

    label("loc_15EB")

    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15F4")

    Jump("loc_164B")

    label("loc_15F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_164B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1642")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_164B")

    label("loc_1642")

    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_164B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1664")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)
    Jump("loc_166A")

    label("loc_1664")

    OP_10(0x0, 0x1)
    OP_10(0x5, 0x0)

    label("loc_166A")

    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16B7")
    SetMapFlags(0x2000)
    OP_E0(0x1)
    ClearScenarioFlags(0x1, 0)
    Jump("loc_16CB")

    label("loc_16B7")

    ClearMapFlags(0x2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16CB")
    OP_E0(0x0)
    SetScenarioFlags(0x1, 0)

    label("loc_16CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_16D9")
    Jump("loc_16FB")

    label("loc_16D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_16FB")
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetMapObjFlags(0x2, 0x2)

    label("loc_16FB")

    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_174C")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD2, 0xAE, 0x9B, 0x5, 0x190, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    SetMapObjFrame(0xFF, "water00", 0x2, "red")
    SetMapObjFrame(0xFF, "water01", 0x2, "red")

    label("loc_174C")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_175E")
    Jump("loc_179F")

    label("loc_175E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_179F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1778")
    Jump("loc_179F")

    label("loc_1778")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_178A")
    Jump("loc_179F")

    label("loc_178A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_179F")
    OP_66(0x4, 0x1)
    OP_65(0x1, 0x1)

    label("loc_179F")

    SetMapObjFlags(0x3, 0x4)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17DC")
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    ClearMapObjFlags(0x3, 0x4)
    OP_66(0x3, 0x1)
    Jump("loc_17E1")

    label("loc_17DC")

    OP_16(0x3, 0x4, 0x1, 0x0)

    label("loc_17E1")

    OP_1B(0x4, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1807")
    OP_1B(0x4, 0x0, 0x41)

    label("loc_1807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1823")
    OP_1B(0x4, 0x0, 0x41)

    label("loc_1823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1836")
    OP_1B(0x4, 0x0, 0x41)

    label("loc_1836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1858")
    OP_1B(0x4, 0x0, 0x41)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1858")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1858")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1880")
    OP_1B(0x2, 0x0, 0x43)

    label("loc_1880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1893")
    OP_1B(0x2, 0x0, 0x43)

    label("loc_1893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18A6")
    OP_1B(0x2, 0x0, 0x43)

    label("loc_18A6")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 0)), scpexpr(EXPR_END)), "loc_1903")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 22470, 0, -63690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_1903")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 67060, -5900, -100200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1987")
    OP_24(0x7D)
    Jump("loc_19CA")

    label("loc_1987")

    SoundDistance(0x7D, 0x34C6, 0x0, 0xFFFD8D16, 0x15F90, 0x11170, 0x64, 0x0)
    OP_E1(0x9D4E, 0x118, 0xFFFE0909)
    OP_E1(0xE06A, 0x384, 0xFFFE9238)
    OP_E1(0xFCDA, 0x5A, 0xFFFF282E)

    label("loc_19CA")

    Return()

    # Function_2_15A1 end

    def Function_3_19CB(): pass

    label("Function_3_19CB")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 0)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_3_19CB end

    def Function_4_19DF(): pass

    label("Function_4_19DF")

    ClearChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x8000)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetMapObjFlags(0x2, 0x1000)
    OP_78(0x2, 0x32)
    OP_49()
    SetChrPos(0x32, 2000, 1000, 14000, 0)
    OP_D3(0x32, 0x0, 0x2BF20, 0x0, 0x0)
    Return()

    # Function_4_19DF end

    def Function_5_1A2C(): pass

    label("Function_5_1A2C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x01",
            "Wait for a bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "St. Ursula Medical College\x01",      # 0
            "Fork (Sandbar)\x01",                  # 1
            "Leave\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AC1")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1AE1")

    label("loc_1AC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AE1")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()

    label("loc_1AE1")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_1A2C end

    def Function_6_1AE9(): pass

    label("Function_6_1AE9")

    Fade(1000)
    OP_68(0, 600, -32000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -9800, 180, -11100, 89)
    SetChrPos(0x1, -9800, 180, -10100, 89)
    SetChrPos(0x2, -9800, 180, -9100, 89)
    SetChrPos(0x3, -9800, 180, -8100, 89)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_78(0x1, 0x2B)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x2B, 0, 0, -40000, 0)
    OP_D3(0x2B, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)

    def lambda_1BC3():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_1BC3)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    Sleep(2500)
    Fade(500)
    OP_68(-10500, 780, -11600, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x2B, -6300, 0, -21000, 0)

    def lambda_1C30():
        OP_96(0xFE, 0xFFFFE764, 0x0, 0xFFFFD314, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_1C30)
    WaitChrThread(0x2B, 1)
    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x1)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_6_1AE9 end

    def Function_7_1C6B(): pass

    label("Function_7_1C6B")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -9830, 180, -11430, 90)
    SetChrPos(0x1, -9830, 180, -11430, 90)
    SetChrPos(0x2, -9830, 180, -11430, 90)
    SetChrPos(0x3, -9830, 180, -11430, 90)
    OP_68(-9830, 780, -11430, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_7_1C6B end

    def Function_8_1D00(): pass

    label("Function_8_1D00")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22D1")

    Menu(
        0,
        32,
        26,
        1,
        (
            "Ride in Guardian Force car\x01",      # 0
            "Rest\x01",                            # 1
            "Leave\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_226E")
    Sound(1500, 255, 100, 0)
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DA6")
    MenuCmd(1, 1, "★City - Central Square")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1DC1")

    label("loc_1DA6")

    MenuCmd(1, 1, "　City - Central Square")

    label("loc_1DC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DEF")
    MenuCmd(1, 1, "★City - East Exit")
    MenuCmd(3, 1, 0x1)
    Jump("loc_1E05")

    label("loc_1DEF")

    MenuCmd(1, 1, "　City - East Exit")

    label("loc_1E05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E33")
    MenuCmd(1, 1, "★City - West Exit")
    MenuCmd(3, 1, 0x2)
    Jump("loc_1E49")

    label("loc_1E33")

    MenuCmd(1, 1, "　City - West Exit")

    label("loc_1E49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E78")
    MenuCmd(1, 1, "★City - South Exit")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1E8F")

    label("loc_1E78")

    MenuCmd(1, 1, "　City - South Exit")

    label("loc_1E8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EBE")
    MenuCmd(1, 1, "★City - North Exit")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1ED5")

    label("loc_1EBE")

    MenuCmd(1, 1, "　City - North Exit")

    label("loc_1ED5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EFF")
    MenuCmd(1, 1, "★Tangram Gate")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1F11")

    label("loc_1EFF")

    MenuCmd(1, 1, "　Tangram Gate")

    label("loc_1F11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3D")
    MenuCmd(1, 1, "★Bellguard Gate")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1F51")

    label("loc_1F3D")

    MenuCmd(1, 1, "　Bellguard Gate")

    label("loc_1F51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F89")
    MenuCmd(1, 1, "★St. Ursula Medical College")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1FA9")

    label("loc_1F89")

    MenuCmd(1, 1, "　St. Ursula Medical College")

    label("loc_1FA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FD7")
    MenuCmd(1, 1, "★Armorica Village")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1FED")

    label("loc_1FD7")

    MenuCmd(1, 1, "　Armorica Village")

    label("loc_1FED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_201F")
    MenuCmd(1, 1, "★Mainz Mining Village")
    MenuCmd(3, 1, 0x9)
    Jump("loc_2039")

    label("loc_201F")

    MenuCmd(1, 1, "　Mainz Mining Village")

    label("loc_2039")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2073")
    MenuCmd(1, 1, "★Mainz Mountain Path - Tunnel")
    MenuCmd(3, 1, 0xA)
    Jump("loc_2095")

    label("loc_2073")

    MenuCmd(1, 1, "　Mainz Mountain Path - Tunnel")

    label("loc_2095")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20C4")
    MenuCmd(1, 1, "★Stargazer's Tower")
    MenuCmd(3, 1, 0xB)
    Jump("loc_20DB")

    label("loc_20C4")

    MenuCmd(1, 1, "　Stargazer's Tower")

    label("loc_20DB")

    MenuCmd(1, 1, "　Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_225F")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x3)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21B2"),
        (1, "loc_21C0"),
        (2, "loc_21CE"),
        (3, "loc_21DC"),
        (4, "loc_21EA"),
        (5, "loc_21F8"),
        (6, "loc_2206"),
        (7, "loc_2214"),
        (8, "loc_2222"),
        (9, "loc_2230"),
        (10, "loc_223E"),
        (11, "loc_224C"),
        (SWITCH_DEFAULT, "loc_225A"),
    )


    label("loc_21B2")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_225A")

    label("loc_21C0")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_225A")

    label("loc_21CE")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_225A")

    label("loc_21DC")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_225A")

    label("loc_21EA")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_225A")

    label("loc_21F8")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_225A")

    label("loc_2206")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_225A")

    label("loc_2214")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_225A")

    label("loc_2222")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_225A")

    label("loc_2230")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_225A")

    label("loc_223E")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_225A")

    label("loc_224C")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_225A")

    label("loc_225A")

    Jump("loc_2269")

    label("loc_225F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2269")

    Jump("loc_22CC")

    label("loc_226E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22B9")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_22CC")

    label("loc_22B9")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22CC")

    Jump("loc_1D1A")

    label("loc_22D1")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1D00 end

    def Function_9_22D9(): pass

    label("Function_9_22D9")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 8280, 0, -13050, 180)
    SetChrPos(0x1, 8280, 0, -13050, 180)
    SetChrPos(0x2, 8280, 0, -13050, 180)
    SetChrPos(0x3, 8280, 0, -13050, 180)
    SetChrPos(0x4, 8280, 0, -13050, 180)
    SetChrPos(0x5, 8280, 0, -13050, 180)
    Sleep(1)
    OP_68(8280, 600, -13050, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23AD")
    Sound(1502, 255, 100, 0)
    Jump("loc_23B3")

    label("loc_23AD")

    Sound(1503, 255, 100, 0)

    label("loc_23B3")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_22D9 end

    def Function_10_23C8(): pass

    label("Function_10_23C8")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)
    Return()

    # Function_10_23C8 end

    def Function_11_23D6(): pass

    label("Function_11_23D6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I love to hang out here to watch\x01",
            "the airships take off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's mind-boggling that something so\x01",
            "massive can easily fly through the sky.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_23D6 end

    def Function_12_246C(): pass

    label("Function_12_246C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm about to go on vacation\x01",
            "to Liberl with my kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard their food is delicious,\x01",
            "so I'm excited to try out all of their\x01",
            "local delicacies.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_246C end

    def Function_13_250D(): pass

    label("Function_13_250D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm taking a flight out of Crossbell Airport,\x01",
            "so I rode the train out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Between trains, buses, and airships,\x01",
            "Crossbell has just about every mode\x01",
            "of transportation. Must be convenient.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_250D end

    def Function_14_25DA(): pass

    label("Function_14_25DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EA")

    ChrTalk(
        0xFE,
        (
            "I'm planning to go to Remiferia\x01",
            "for a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, that reminds me. Remiferia also\x01",
            "has their own police department, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure it's far superior to Crossbell's\x01",
            "dinky little force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Well, wasn't THAT uncalled for?!)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2775")

    label("loc_26EA")


    ChrTalk(
        0xFE,
        (
            "I heard Remiferia also has their own\x01",
            "police department, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm sure it's far superior to\x01",
            "Crossbell's dinky little force.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2775")

    TalkEnd(0xFE)
    Return()

    # Function_14_25DA end

    def Function_15_2779(): pass

    label("Function_15_2779")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I just saw my husband off at the airport.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, dear me... I'm no longer young,\x01",
            "but I couldn't help but wave as he left.\x01",
            "Heehee. How embarrassing.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_2779 end

    def Function_16_281B(): pass

    label("Function_16_281B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "The missus and I are going to visit Liberl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Times Department Store's pretty crazy, but\x01",
            "I heard the Bose Market is just as crazy!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_281B end

    def Function_17_28AD(): pass

    label("Function_17_28AD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I think my husband fell in love with Liberl\x01",
            "when he went to watch the Martial Arts\x01",
            "Competition two years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I think he's been a bad influence\x01",
            "on me, 'cause I can't help but constantly\x01",
            "wonder about what kind of place Liberl is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whatever. I'm going to enjoy this trip\x01",
            "to the best of my ability!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_28AD end

    def Function_18_29F1(): pass

    label("Function_18_29F1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Traders like myself have to head out of state\x01",
            "to stock up on goods for the up-and-coming\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be gone up until the final moments before\x01",
            "the festival begins. Make sure to find me then,\x01",
            "'cause I'll have all sorts of nifty merchandise!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_29F1 end

    def Function_19_2B01(): pass

    label("Function_19_2B01")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I wanted to try traveling alone just\x01",
            "once in my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard all kinds of wild things about\x01",
            "Crossbell, but it's been an enjoyable\x01",
            "experience overall.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_2B01 end

    def Function_20_2BAC(): pass

    label("Function_20_2BAC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I work for a Calvardian news agency.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The editor-in-chief sent me out here to cover\x01",
            "the internationally famous Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But anyway, the stage is set and my camera's\x01",
            "ready to go!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2BAC end

    def Function_21_2C80(): pass

    label("Function_21_2C80")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "If there's one thing I've learned in my career,\x01",
            "it's that photos of the various food stalls will\x01",
            "always be a hit with the readers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys know any streets where I can take\x01",
            "some especially great photos?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2C80 end

    def Function_22_2D5D(): pass

    label("Function_22_2D5D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I've been saving up all of my money for\x01",
            "this very day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And now I'm about to party it up with my girl\x01",
            "in Crossbell till we drop!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2D5D end

    def Function_23_2DEE(): pass

    label("Function_23_2DEE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Weeelll... Given our age, I doubt we have\x01",
            "nearly enough mira to 'party till we drop.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But his enthusiasm is starting to\x01",
            "rub off on me!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_2DEE end

    def Function_24_2E86(): pass

    label("Function_24_2E86")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Welp... I can't believe the two of us keep\x01",
            "going on trips together every year...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My opportunity to go on vacation with the\x01",
            "man of my dreams has gone up in flames\x01",
            "once again.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_2E86 end

    def Function_25_2F45(): pass

    label("Function_25_2F45")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Wh-What's got your panties in a twist?!\x01",
            "Everyone goes on these kinds of trips\x01",
            "together--even guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "C'mon. We're best friends... Do you\x01",
            "really wanna ruin the good vibes with\x01",
            "your complaining?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_2F45 end

    def Function_26_3015(): pass

    label("Function_26_3015")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "It's already the final day. I wish\x01",
            "the good times could have lasted\x01",
            "just a little bit longer.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_3015 end

    def Function_27_307F(): pass

    label("Function_27_307F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well, you can't get too greedy. I'm\x01",
            "sure you managed to make some\x01",
            "unforgettable memories, right?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_307F end

    def Function_28_30EC(): pass

    label("Function_28_30EC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh* I thought staying at Mishelam was\x01",
            "going to be an amazing experience, but\x01",
            "it ended up being traumatizing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, really. War hounds? IN MISHELAM?\x01",
            "This guy over here slept through the whole\x01",
            "thing like a rock!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_30EC end

    def Function_29_31D4(): pass

    label("Function_29_31D4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Come on, honey. Cheer up. It's not like\x01",
            "those monsters intentionally showed up\x01",
            "to ruin our trip, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Isn't it about time you stopped pouting\x01",
            "and protesting next year's trip?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_31D4 end

    def Function_30_3296(): pass

    label("Function_30_3296")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Phew... Going on a day trip to Remiferia\x01",
            "is as exhausting as it sounds, trust me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay! The wifey's waiting back home for me.\x01",
            "I ought to get there ASAP, so the two of us\x01",
            "can relax together.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_3296 end

    def Function_31_3365(): pass

    label("Function_31_3365")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_3513")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3461")

    ChrTalk(
        0xFE,
        (
            "Service to Liberl and Remiferia has\x01",
            "finally begun at the Crossbell Airport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got some packages flying in\x01",
            "from Liberl today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay. I think it's almost time for the\x01",
            "Capua Delivery Service to show up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_350F")

    label("loc_3461")


    ChrTalk(
        0xFE,
        (
            "We've got some packages flying in\x01",
            "from Liberl today, so I'm waiting\x01",
            "here in anticipation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay. I think it's almost time for the\x01",
            "Capua Delivery Service to show up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_350F")

    TalkEnd(0xFE)
    Return()

    label("loc_3513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3653")

    ChrTalk(
        0xFE,
        (
            "Hmm? Aren't you guys supposed to be\x01",
            "working right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry for the mess yesterday. If I wasn't\x01",
            "such a lazy bum, that kid never would have\x01",
            "made it an arge out of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've decided to be a new man from here on out!\x01",
            "I'll make sure to work with purpose and to be\x01",
            "a responsible adult.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3716")

    label("loc_3653")


    ChrTalk(
        0xFE,
        (
            "I've got a bunch of packages coming in\x01",
            "from a foreign shipping company today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah... My old man gave me a walloping\x01",
            "I'll never forget yesterday, so I'm trying to\x01",
            "wipe the slate clean.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3716")

    TalkEnd(0xFE)
    Return()

    # Function_31_3365 end

    def Function_32_371A(): pass

    label("Function_32_371A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_3BF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A61")

    ChrTalk(
        0xFE,
        (
            "Oh, you guys are back... Wait!\x01",
            "What happened to the bus?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWe managed to find the bus broken down\x01",
            "in the middle of the road. It sounded like\x01",
            "the engine had broken down.\x02\x03",
            "We also temporarily warded off monsters\x01",
            "trying to attack passengers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FThere are currently two bracers handling\x01",
            "the aftermath.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, really?\x01",
            "Well, fine by me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure I have nothing to worry about\x01",
            "if bracers are already on the scene.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0006FY-Yeah, I guess so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108FI appreciate Estelle and Joshua saving us,\x01",
            "but I can't say I enjoy this recent trend of\x01",
            "bracers swooping in to save the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FI feel you, Mademois-Elie. But seriously, they've\x01",
            "got some real impeccable timing, don't they?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6D, 0)
    Jump("loc_3BF2")

    label("loc_3A61")


    ChrTalk(
        0xFE,
        (
            "Anyway. Bus is probably coming soon, yeah?\x01",
            "Good thing it wasn't anythin' too serious.\x01",
            "The schedule was getting real out of whack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't thank the four of you enough.\x01",
            "Who knows what would have happened\x01",
            "had you not intervened?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BF2")

    ChrTalk(
        0x101,
        (
            "#0000FYou're welcome, sir. We're just doing our job.\x01",
            "(Elie's right, though. Constantly relying on\x01",
            "luck is only going to hurt us in the long run.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_3BF2")

    Jump("loc_3CBA")

    label("loc_3BF7")


    ChrTalk(
        0xFE,
        (
            "The driver reported that the bus was\x01",
            "no longer functioning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wouldn't mind having you guys check up\x01",
            "on it if you were already heading out there.\x01",
            "Anyway, thanks again! I appreciate it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CBA")

    TalkEnd(0xFE)
    Return()

    # Function_32_371A end

    def Function_33_3CBE(): pass

    label("Function_33_3CBE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "We plan to stake out the station and\x01",
            "the airport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We'll leave Tangram Gate to you.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_3CBE end

    def Function_34_3D22(): pass

    label("Function_34_3D22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_43B6")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3EF9")
    TurnDirection(0xFE, 0x10A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EA3")

    ChrTalk(
        0xFE,
        (
            "Ugh...\x01",
            "Whoa! Detective Dudley?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "U-Uh... Good morning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0603FIt's almost noon, Raymond.\x02\x03",
            "#0600FI take it you're gathering information\x01",
            "at the moment, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep! No problems here, sir.\x01",
            "It's all smooth sailing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0603F...\x01",
            "(This is precisely why he's stuck\x01",
            "in the Second Division.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD9, 2)
    SetScenarioFlags(0x0, 4)
    Jump("loc_3EED")

    label("loc_3EA3")


    ChrTalk(
        0xFE,
        "Guess I better gather some intel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Time to get to work, Raymond.\x02",
    )

    CloseMessageWindow()

    label("loc_3EED")

    OP_93(0xFE, 0x10E, 0x0)
    Jump("loc_43B1")

    label("loc_3EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4320")

    ChrTalk(
        0xFE,
        "Oh, it's you guys. How's the SSS doing today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys here to help with the whole,\x01",
            "uh...airport thing?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4123")
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0105FHmm? What's wrong with the airport?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm gonna take that as a big, fat no.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh. Probably better you stay in the dark on\x01",
            "this one. First Division might end up working\x01",
            "you to the bone. Consider this a favor, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(It sounds like something happened, but\x01",
            "Raymond was being awfully vague.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4318")

    label("loc_4123")

    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FOh, no, that's not why we--\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FHey, how's the situation lookin', Ray?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Keep this one on the down low,\x01",
            "but we're still looking for leads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They even pulled in the Second Division\x01",
            "to help out. You can imagine how hard\x01",
            "they've been working us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108FWhile the threat may be fake, CPD protocol\x01",
            "requires you to treat it as if it were real.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yup. Fake or not, it's been a real pain\x01",
            "in my behind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4318")

    SetScenarioFlags(0x0, 4)
    Jump("loc_43B1")

    label("loc_4320")


    ChrTalk(
        0xFE,
        "I'm currently working on uncovering new leads.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though I gotta say, investigating covertly is\x01",
            "less fun and a lot harder than it sounds.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43B1")

    Jump("loc_4413")

    label("loc_43B6")


    ChrTalk(
        0xFE,
        (
            "We're always understaffed, too, which kinda\x01",
            "blows. One man can only do so much, y'know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4413")

    TalkEnd(0xFE)
    Return()

    # Function_34_3D22 end

    def Function_35_4417(): pass

    label("Function_35_4417")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Did I miss the bus? I hope not,\x01",
            "'cause I'm running a little late...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_4417 end

    def Function_36_4467(): pass

    label("Function_36_4467")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "My poor grandson has been hospitalized\x01",
            "for a while now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure it must get lonely wasting away\x01",
            "in a hospital like that.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_4467 end

    def Function_37_44F4(): pass

    label("Function_37_44F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4554")

    ChrTalk(
        0xFE,
        "Hmm? Why hasn't the bus come yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope it didn't break down again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_462A")

    label("loc_4554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45F6")

    ChrTalk(
        0xFE,
        (
            "*cough* How long are you planning\x01",
            "on making us wait?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This thing is way late already, and it feels\x01",
            "like I'm starting to catch a cold!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_462A")

    label("loc_45F6")


    ChrTalk(
        0xFE,
        "I'm going to keel over if it takes any longer!\x02",
    )

    CloseMessageWindow()

    label("loc_462A")

    TalkEnd(0xFE)
    Return()

    # Function_37_44F4 end

    def Function_38_462E(): pass

    label("Function_38_462E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_46C1")

    ChrTalk(
        0xFE,
        "Time to visit the hospital! ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My boyfriend's sick, so I'm going to visit!\x01",
            "Maybe I can help...nurse him back to health.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_471B")

    label("loc_46C1")


    ChrTalk(
        0xFE,
        (
            "We were just about to go\x01",
            "get a check up at the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why's the bus so late?\x02",
    )

    CloseMessageWindow()

    label("loc_471B")

    TalkEnd(0xFE)
    Return()

    # Function_38_462E end

    def Function_39_471F(): pass

    label("Function_39_471F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "*sniff* Ugh... My cold has gotten worse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*cough* *hack*\x01",
            "Working too many late nights is\x01",
            "probably taking its toll on me.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_471F end

    def Function_40_47A8(): pass

    label("Function_40_47A8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm here to look after my\x01",
            "father-in-law for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* If only he'd listened to me\x01",
            "when he started feeling sick.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_47A8 end

    def Function_41_482F(): pass

    label("Function_41_482F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This stinks... Visiting hours\x01",
            "end after 5:30PM.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to have to turn around\x01",
            "the second I get there at this rate...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_482F end

    def Function_42_48B8(): pass

    label("Function_42_48B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4926")

    NpcTalk(
        0xFE,
        "Citizen",
        "Heeeey! Is the bus coming or what?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Citizen",
        "Is this stupid schedule lying?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B70")

    label("loc_4926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4ADD")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A29")

    ChrTalk(
        0xFE,
        "It's good to see you, Detective Dudley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been total radio silence from the top brass,\x01",
            "so it's hard to make sense of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But still, leave the airport to us.\x01",
            "We'll have everything wrapped up by sundown.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AD8")

    label("loc_4A29")


    ChrTalk(
        0xFE,
        (
            "The First Division is prohibiting all entry\x01",
            "into the airport for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do us a favor and try not to make things\x01",
            "difficult for us, Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AD8")

    Jump("loc_4B70")

    label("loc_4ADD")


    ChrTalk(
        0xFE,
        (
            "This case is strictly under First Division\x01",
            "jurisdiction. Are we clear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Be prepared to suffer the consequences\x01",
            "if you act out of line.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD3, 6)

    label("loc_4B70")

    TalkEnd(0xFE)
    Return()

    # Function_42_48B8 end

    def Function_43_4B74(): pass

    label("Function_43_4B74")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4C33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE5")

    ChrTalk(
        0xFE,
        (
            "Oh, for crying out loud... City Hall's\x01",
            "about to get another piece of my mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4C2E")

    label("loc_4BE5")


    ChrTalk(
        0xFE,
        (
            "Sheesh... I think I'm going to call it quits\x01",
            "for now and head home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C2E")

    Jump("loc_4CB1")

    label("loc_4C33")


    ChrTalk(
        0xFE,
        (
            "I was going to see a sick friend of mine, but\x01",
            "I don't think that's happening anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What's up with the bus today?\x02",
    )

    CloseMessageWindow()

    label("loc_4CB1")

    TalkEnd(0xFE)
    Return()

    # Function_43_4B74 end

    def Function_44_4CB5(): pass

    label("Function_44_4CB5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Some police officer approached me,\x01",
            "asking if I'd seen anything suspicious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They weren't exactly clear on what\x01",
            "they meant by 'suspicious,' though.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_44_4CB5 end

    def Function_45_4D5A(): pass

    label("Function_45_4D5A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EAC")

    ChrTalk(
        0xFE,
        (
            "Nice work. We're currently investigating\x01",
            "the surrounding area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Second Division is assisting us, so\x01",
            "we'll be finished within the next three hours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0608FUnderstood.\x02\x03",
            "#0600FI'll be working solo for a while, Emma.\x01",
            "I'm leaving the rest of this to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, sir! You can count on me!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4F4C")

    label("loc_4EAC")


    ChrTalk(
        0xFE,
        (
            "Nice work. We're currently investigating\x01",
            "the surrounding area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Second Division is assisting us, so\x01",
            "we'll be finished within the next three hours.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F4C")

    Jump("loc_500F")

    label("loc_4F51")


    ChrTalk(
        0xFE,
        (
            "Do us a favor and try not to interfere\x01",
            "with our investigation, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're currently under Detective Dudley's\x01",
            "command...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There will be hell to pay if you disobey\x01",
            "his orders.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_500F")

    TalkEnd(0xFE)
    Return()

    # Function_45_4D5A end

    def Function_46_5013(): pass

    label("Function_46_5013")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FA beautiful day and fishing. Talk about\x01",
            "a match made in heaven.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(52890, 2860, -105330, 1500)
    MoveCamera(57, 25, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(16000, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Try fishing?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_534D")
    OP_E0(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_END)), "loc_510E")
    MiniGame(0x6, 0xA, 0xCB98, 0x384, 0xFFFE6934, 0x65, 0x105F4, 0xFFFFE8F4, 0xFFFE7898)
    Jump("loc_534D")

    label("loc_510E")

    MiniGame(0x6, 0xB, 0xCB98, 0x384, 0xFFFE6934, 0x65, 0x105F4, 0xFFFFE8F4, 0xFFFE7898)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_534D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_534D")
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_68(53380, 2860, -106080, 0)
    MoveCamera(58, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(13540, 0)
    LoadChrToIndex("apl/ch50161.itc", 0x28)
    SetChrChipByIndex(0x0, 0x28)
    SetChrSubChip(0x0, 0x12)
    SetChrFlags(0x0, 0x2)
    SetChrPos(0x0, 52120, 900, -104140, 101)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x0,
        "Lloyd",
        (
            "#0011FWh-Whoa!\x01",
            "What even IS this thing?! It's huge!\x02\x03",
            "#0006FIs this seriously a fish?! I thought\x01",
            "my rod was going to snap in half!\x02\x03",
            "#0000FHaha. Today's gotta be my lucky day!\x01",
            "Oh, man... I bet Cerdan's going to flip\x01",
            "when he gets a load of this!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x1, 52120, 900, -104140, 101)
    SetChrPos(0x2, 52120, 900, -104140, 101)
    SetChrPos(0x3, 52120, 900, -104140, 101)
    SetChrPos(0x4, 52120, 900, -104140, 101)
    SetChrPos(0x5, 52120, 900, -104140, 101)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrSubChip(0x0, 0x0)
    ClearChrFlags(0x0, 0x2)
    OP_49()
    OP_D5(0x28)
    OP_37()
    SetScenarioFlags(0x69, 4)

    label("loc_534D")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_46_5013 end

    def Function_47_5352(): pass

    label("Function_47_5352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_53B1")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The bus seems to be extremely delayed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_545E")

    label("loc_53B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53D7")
    Call(0, 68)
    Jump("loc_545E")

    label("loc_53D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53ED")
    Call(0, 48)
    Jump("loc_545E")

    label("loc_53ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5403")
    Call(0, 56)
    Jump("loc_545E")

    label("loc_5403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5414")
    Call(0, 5)
    Jump("loc_545E")

    label("loc_5414")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The bus is extremely delayed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_545E")

    Return()

    # Function_47_5352 end

    def Function_48_545F(): pass

    label("Function_48_545F")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_68(-10000, 1300, -10900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -10300, 180, -11500, 180)
    SetChrPos(0x102, -10300, 180, -10000, 180)
    SetChrPos(0x104, -8500, 180, -9400, 225)
    SetChrPos(0x103, -9800, 180, -8300, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#1100768V#0000F#5PThere's still...what, ten minutes\x01",
            "until the next bus leaves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100769V#0100F#5PThat's fortunately not too long a wait.\x02\x03",
            "#1100770V#0104FIt's been a while since I last visited\x01",
            "St. Ursula...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#1100771V#0000F#12PSame here.\x02\x03",
            "#1100772V#0006FI've been wanting to visit for a while, but\x01",
            "you know how busy our schedule is.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#1100773V#0105F#5PYou did? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100774V#0305F#5PYou feelin' sick, bud? I bet a cute nurse'd\x01",
            "get you back to top shape in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100775V#0004F#12PI'm not you, Randy. I have a friend who\x01",
            "works there.\x02\x03",
            "#1100776V#0002FThey've always been there for me, so I'm\x01",
            "kicking myself for not having gone sooner.\x02\x03",
            "#1100777VWe were both kind of busy, so we kept\x01",
            "putting it off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100778V#0100F#5PAh, I see. I can sympathize with that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100779V#0300F#5PYou know someone workin' there?\x01",
            "He's probably a doctor then, yeah?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#1100780V#0000F#6PNot quite. She's actually a nurse.\x02\x03",
            "#1100781VShe's more on the pediatric side of things,\x01",
            "so she's always insanely busy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#1100782V#0305F#5P'Scuse me? Did you just say...a nurse?\x02\x03",
            "#1100783VLike, one of those gals that pampers you\x01",
            "while takin' your body temp in their totally\x01",
            "smokin' hot uniforms? THAT kinda nurse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100784V#0005F#6PYeah?\x02\x03",
            "#1100785V#0000FAnd besides, their clothes are mandatory.\x01",
            "It's not like they wear them by choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100786V#0301F#5PSo...you gonna give me her age, or what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100787V#0004F#6PWell, she's five years older than me, so\x01",
            "I guess that makes her 23.\x02\x03",
            "#1100788V#0000FWe were next-door neighbors for a long\x01",
            "time, so she's basically like a sister to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100789V#0301F#5PShe a looker?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100790V#0011F#6PI...suppose. I'd say so, yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100791V#0303F#5PSo, to recap... She's two years older than me,\x01",
            "she's hot, and she's pretty much always\x01",
            "wearin' a nurse's uniform...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        (
            "#1100792V#5P#0307F#4SJACKPOT, BABY! I've been waiting all my\x01",
            "life for this day!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x104,
        (
            "#1100793V#5P#0309FMan, what'd I do to deserve this happiness?\x02\x03",
            "#1100794VYou're the best thing that's ever happened\x01",
            "to me, buddy ol' pal!\x02\x03",
            "#1100795V#0302FOh, and thanks for the assist, wingman. ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100796V#0006F#6PI don't remember ever agreeing to help you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100797V#0106F#5P*sigh* You men are all the same. Disgusting.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1100798V#0011F#12PHey, give me a little more credit than that!\x01",
            "We're nothing alike!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x103, 500)

    ChrTalk(
        0x102,
        (
            "#1100799V#0105F#6PIs something the matter, Tio?\x02\x03",
            "#1100800VWhy are you being so quiet?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F30():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F30)

    def lambda_5F3D():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5F3D)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#1100801V#0208F#5POh... I simply do not particularly care for\x01",
            "hospitals, is all.\x02\x03",
            "#1100802V#0206FBetween the smell of antiseptic solution and\x01",
            "the sight of large needles, I am not a fan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100803V#0102F#6PSo that's what it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100804V#0001F#12PAre you going to be okay?\x02\x03",
            "#1100805VIf you're not feeling well, Tio--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100806V#0203F#5PI will be fine.\x02\x03",
            "#1100807VIt is merely a dislike. It is not as though\x01",
            "I have a phobia of hospitals.\x02\x03",
            "#1100808V#0211FFor your sake, I hope you were not about\x01",
            "to give me permission to sit out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100809V#0011F#12PN-No, of course not.\x02\x03",
            "#1100810V#0006F(That was actually a little intimidating...\x01",
            "I should watch my mouth around her.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100811V#0204F#5PBesides, I would also like to meet\x01",
            "this friend of yours, Lloyd.\x02\x03",
            "#1100812V#0202FShe must have been the person you\x01",
            "were happily chatting away with on\x01",
            "the phone, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1100813V#0005F#12PH-How'd you know about that?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    def lambda_632A():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_632A)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#1100814V#0104F#5PYou weren't exaggerating about her\x01",
            "being like family, were you, Lloyd?\x02\x03",
            "#1100815V#0102FI'm looking forward to seeing what\x01",
            "kind of person she is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100816V#0309F#5PFor real. We'd better handle this case\x01",
            "like our lives are dependin' on it!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x104, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#1100817V#0011F#6PY-You guys! The investigation\x01",
            "takes precedence, okay?!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrPos(0x101, -10000, 180, -11500, 180)
    SetChrPos(0x102, -10000, 180, -8900, 180)
    SetChrPos(0x104, -10000, 180, -10200, 180)
    SetChrPos(0x103, -10000, 180, -7600, 180)
    ClearChrFlags(0x2C, 0x80)
    SetChrPos(0x2C, -10000, 180, -6300, 180)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2D, -10000, 180, -5000, 180)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0x2E, -8700, 180, -5000, 270)
    ClearChrFlags(0x2F, 0x80)
    SetChrPos(0x2F, -7400, 180, -5000, 270)
    Sleep(1000)
    OP_68(-10000, 1800, -10900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18000, 0)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_68(-10000, 1400, -10900, 3000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x102,
        "#1100818V#0106F#5PIt's not coming, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100819V#0203F#5PIt has been 30 minutes already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100820V#0306F#5PYou got some 'splainin' to do, Lloyd.\x02\x03",
            "#1100821V#0301FDidn't you say it was comin' in ten\x01",
            "minutes?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#1100822V#0006F#12PI'm in the same boat as you guys.\x02\x03",
            "#1100823V#0008FThis is really weird... The bus shouldn't\x01",
            "be this late.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x30, 0x4)
    SetChrPos(0x30, -1000, 900, 3000, 180)

    NpcTalk(
        0x30,
        "Young Man's Voice",
        "#1100824V#4P#2S*sigh* I was afraid of this happening...\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x30, 3, 0, 49)

    def lambda_678F():

        label("loc_678F")

        TurnDirection(0x101, 0x30, 500)
        Yield()
        Jump("loc_678F")

    QueueWorkItem2(0x101, 1, lambda_678F)

    def lambda_67A1():

        label("loc_67A1")

        TurnDirection(0x102, 0x30, 500)
        Yield()
        Jump("loc_67A1")

    QueueWorkItem2(0x102, 1, lambda_67A1)

    def lambda_67B3():

        label("loc_67B3")

        TurnDirection(0x103, 0x30, 500)
        Yield()
        Jump("loc_67B3")

    QueueWorkItem2(0x103, 1, lambda_67B3)

    def lambda_67C5():

        label("loc_67C5")

        TurnDirection(0x104, 0x30, 500)
        Yield()
        Jump("loc_67C5")

    QueueWorkItem2(0x104, 1, lambda_67C5)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-8590, 1000, -11890, 6000)
    OP_6F(0x1)
    WaitChrThread(0x30, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)

    NpcTalk(
        0x30,
        "Official-Looking Man",
        (
            "#1100825V#5PWhat are we going to do?\x01",
            "Why is it 20 minutes late?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x30,
        "Official-Looking Man",
        (
            "#1100826V#5PI tried contacting them, but they wouldn't\x01",
            "even pick up the stupid phone.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-8910, 1000, -11110, 0)
    MoveCamera(61, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -9780, 180, -11560, 90)
    SetChrPos(0x104, -9650, 180, -10110, 135)
    SetChrPos(0x102, -10840, 180, -10750, 90)
    SetChrPos(0x103, -10640, 180, -9430, 135)
    SetChrPos(0x2C, -10080, 180, -7470, 135)
    SetChrPos(0x2D, -8550, 180, -5520, 180)
    SetChrPos(0x2E, -9820, 180, -5930, 135)
    SetChrPos(0x2F, -7450, 180, -5520, 180)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#1100827V#0001F#6PUm, excuse me... Is something wrong\x01",
            "with the bus?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100828V#0101F#6PIt's rare to see it fall behind schedule\x01",
            "by this long.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x30, 0x101, 500)
    Sleep(300)

    NpcTalk(
        0x30,
        "Official-Looking Man",
        (
            "#1100829V#11PYeah... They've apparently run\x01",
            "into some trouble on the road.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x30,
        "Official-Looking Man",
        (
            "#1100830V#11PThe driver was able to contact us,\x01",
            "but we lost communication.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x30,
        "Official-Looking Man",
        (
            "#1100831V#11PThe line suddenly fell silent while he was\x01",
            "in the middle of explaining the situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1100832V#0005F#6PThe line died...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100833V#0203F#6PI sense trouble.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100834V#0305F#1PBy the way, who you workin' for, kid?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x30,
        "Official-Looking Man",
        (
            "#1100835V#11POh, me? I'm with the Crossbell City\x01",
            "Transportation Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "#1100836V#11PWe oversee the entirety of the\x01",
            "bus service across the state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "#1100837V#11PI doubt this is something to contact the CGF over,\x01",
            "so I guess the Bracer Guild is our only hope again.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    def lambda_6E35():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E35)

    def lambda_6E42():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E42)

    def lambda_6E4F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6E4F)

    def lambda_6E5C():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6E5C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1100838V#0001F#11P(Are you guys thinking what I'm thinking?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100839V#0101F#6P(Yes, I think so.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100840V#0203F#6P(*sigh* What other choice do we have?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100841V#0300F#1P(Guess we were at the right place\x01",
            "at the right time.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6F74():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F74)

    def lambda_6F81():
        TurnDirection(0xFE, 0x30, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F81)

    def lambda_6F8E():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6F8E)

    def lambda_6F9B():
        TurnDirection(0xFE, 0x30, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6F9B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1100842V#0000F#6PPardon me.\x02\x03",
            "#1100843VWould you mind letting us take care\x01",
            "of this?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x30,
        "#1100844V#11PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        "#1100845V#11PAnd you all are...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100846V#0000F#6PCrossbell Police Department,\x01",
            "Special Support Section.\x02\x03",
            "#1100847VWe were actually on our way to\x01",
            "the hospital for police business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        "#1100848V#11PReally? You guys are police officers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "#1100849V#11POh, yeah. I'm pretty sure I've read\x01",
            "about you guys in the paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "#1100850V#11PI guess the CPD took a page out of the\x01",
            "bracers' playbook and decided to start\x01",
            "helping the common folk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100851V#0006F#6PWe're not quite the same thing as them,\x01",
            "though.\x02\x03",
            "#1100852V#0000FBut we can absolutely go and assess the\x01",
            "situation for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "#1100853V#11PYou make a strong argument.\x01",
            "I guess I'll leave it to you, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        "#1100854V#11PShould I call some bracers in for backup?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100855V#0012F#6PN-No. I don't think it'll be necessary.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1100856V#0000F#11PLet's go, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100857V#0100F#6PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100858V#0302F#1PReady!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100859V#0202F#6PUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x30, 0x80)
    SetChrBattleFlags(0x30, 0x8000)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    SetChrFlags(0x2E, 0x80)
    SetChrBattleFlags(0x2E, 0x8000)
    SetChrFlags(0x2F, 0x80)
    SetChrBattleFlags(0x2F, 0x8000)
    SetChrPos(0x0, -5110, 0, -13100, 180)
    SetScenarioFlags(0x61, 2)
    OP_29(0x3F, 0x1, 0x6)
    OP_1B(0x2, 0xFF, 0xFFFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x8, -9780, 180, -10890, 180)
    SetChrPos(0x9, -9560, 180, -8470, 180)
    SetChrPos(0xA, -9480, 180, -7040, 180)
    SetChrPos(0xB, -9410, 180, -5860, 180)
    SetChrPos(0x10, -9810, 180, -9920, 180)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_48_545F end

    def Function_49_74D2(): pass

    label("Function_49_74D2")


    def lambda_74D7():
        OP_95(0xFE, -1000, 0, -7000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_74D7)
    WaitChrThread(0x30, 1)

    def lambda_74F5():
        OP_95(0xFE, -7000, 0, -13000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_74F5)
    WaitChrThread(0x30, 1)
    OP_93(0x30, 0xB4, 0x1F4)
    Return()

    # Function_49_74D2 end

    def Function_50_7516(): pass

    label("Function_50_7516")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch02600.itc", 0x28)
    LoadChrToIndex("chr/ch02651.itc", 0x29)
    LoadChrToIndex("chr/ch02602.itc", 0x2A)
    SetChrPos(0x0, 0, 0, -80000, 0)
    SetChrPos(0x1, 0, 0, -80000, 0)
    SetChrPos(0x2, 0, 0, -80000, 0)
    SetChrPos(0x3, 0, 0, -80000, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrChipByIndex(0x31, 0x29)
    SetChrSubChip(0x31, 0x0)
    SetChrPos(0x2B, 1850, 0, -99380, 0)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetMapObjFlags(0x1, 0x1000)
    ClearMapObjFlags(0x1, 0x4)
    OP_78(0x1, 0x2B)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x31, -15190, 0, -65690, 90)
    OP_D3(0x2B, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD2, 0xAE, 0x9B, 0x5, 0x190, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    SetMapObjFrame(0xFF, "water00", 0x2, "red")
    SetMapObjFrame(0xFF, "water01", 0x2, "red")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01200.itp")
    BeginChrThread(0x33, 1, 0, 53)
    FadeToBright(1000, 0)
    OP_68(4940, 600, -80110, 0)
    MoveCamera(46, 11, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(34420, 0)
    OP_68(3390, 600, -61360, 8000)

    def lambda_771C():
        OP_95(0xFE, -320, 0, -25730, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_771C)
    OP_6F(0x1)
    OP_0D()
    Sleep(2000)
    StopBGM(0x1770)
    WaitChrThread(0x2B, 1)
    OP_52(0x31, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x31, 0x29)
    SetChrSubChip(0x31, 0x0)
    OP_52(0x31, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x31, 0x1)

    def lambda_7789():
        OP_9D(0xFE, 0xFFFFE188, 0x0, 0xFFFF0344, 0xBB8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_7789)
    WaitChrThread(0x31, 1)
    SetChrFlags(0x31, 0x1)
    Sound(46, 0, 100, 0)
    SetChrSubChip(0x31, 0x1)
    Sleep(50)
    SetChrSubChip(0x31, 0x2)
    Sleep(50)
    SetChrSubChip(0x31, 0x3)
    Sleep(50)
    SetChrFlags(0x31, 0x20)
    BeginChrThread(0x31, 3, 0, 51)
    BeginChrThread(0x33, 1, 0, 54)

    def lambda_77DB():
        OP_96(0xFE, 0x3B6, 0x0, 0xFFFF06D2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_77DB)
    Sleep(1000)
    Fade(500)
    OP_68(2880, 600, -60120, 0)
    MoveCamera(41, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24800, 0)
    OP_0D()
    WaitChrThread(0x31, 1)
    EndChrThread(0x31, 0x3)
    EndChrThread(0x33, 0x1)
    ClearChrFlags(0x31, 0x20)

    def lambda_783D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_783D)
    WaitChrThread(0x31, 1)
    SetChrChipByIndex(0x31, 0x2A)
    SetChrSubChip(0x31, 0x0)
    OP_52(0x31, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x31, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x31, 0x20)
    BeginChrThread(0x31, 3, 0, 52)
    Sleep(800)
    Sound(2053, 255, 80, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(800)
    SetChrName("White Wolf")

    AnonymousTalk(
        0xFF,
        "#1101670V...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(300)
    EndChrThread(0x31, 0x3)
    ClearChrFlags(0x31, 0x20)
    OP_93(0x31, 0x10E, 0x1F4)
    SetChrChipByIndex(0x31, 0x29)
    SetChrSubChip(0x31, 0x0)
    OP_52(0x31, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x31, 0x20)
    BeginChrThread(0x31, 3, 0, 51)
    BeginChrThread(0x33, 1, 0, 55)
    SetCameraDistance(30800, 3000)
    OP_68(1020, 600, -61950, 3000)

    def lambda_7969():
        OP_96(0xFE, 0xFFFFC856, 0x0, 0xFFFEEA94, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_7969)
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    WaitChrThread(0x31, 1)
    EndChrThread(0x31, 0x3)
    EndChrThread(0x33, 0x1)
    ClearChrFlags(0x31, 0x20)
    OP_0D()
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x33, 0x1)
    Sleep(2000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others returned to the SSS\x01",
            "that night, and began compiling a report\x01",
            "of the day's investigation.\x02\x03",
            "The newly found evidence, uncertainties,\x01",
            "and theories were all discussed and\x01",
            "organized for Sergei's convenience.\x02\x03",
            "And before they knew it, the clock had struck\x01",
            "midnight. Once finished, they returned to their\x01",
            "respective rooms, exhausted, and fell asleep.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x64, 0)
    SetScenarioFlags(0x5C, 4)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_50_7516 end

    def Function_51_7B95(): pass

    label("Function_51_7B95")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7BB0")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_51_7B95")

    label("loc_7BB0")

    Return()

    # Function_51_7B95 end

    def Function_52_7BB1(): pass

    label("Function_52_7BB1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7BCF")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_52_7BB1")

    label("loc_7BCF")

    Return()

    # Function_52_7BB1 end

    def Function_53_7BD0(): pass

    label("Function_53_7BD0")

    Sound(465, 0, 100, 0)
    Sleep(4500)
    Sound(471, 0, 100, 0)
    Return()

    # Function_53_7BD0 end

    def Function_54_7BE0(): pass

    label("Function_54_7BE0")

    Sleep(500)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Return()

    # Function_54_7BE0 end

    def Function_55_7BFC(): pass

    label("Function_55_7BFC")

    Sleep(500)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 85, 0)
    Sleep(500)
    Sound(832, 0, 70, 0)
    Sleep(500)
    Sound(832, 0, 55, 0)
    Return()

    # Function_55_7BFC end

    def Function_56_7C21(): pass

    label("Function_56_7C21")

    EventBegin(0x0)
    SoundLoad(468)
    Fade(1000)
    OP_68(-9140, 780, -11210, 0)
    MoveCamera(55, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25710, 0)
    SetChrPos(0x101, -10500, 180, -11600, 180)
    SetChrPos(0x153, -9630, 180, -10060, 180)
    SetChrPos(0xEF, -9220, 180, -11310, 225)
    ClearChrFlags(0x2B, 0x80)
    SetMapObjFlags(0x1, 0x2)
    SetMapObjFlags(0x1, 0x1000)
    OP_78(0x1, 0x2B)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x2B, 0, 0, -40000, 0)
    OP_D3(0x2B, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#3600652V#0000F#5PLooks like the next bus is coming in...\x01",
            "Right around now, actually.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_7D87")

    ChrTalk(
        0x102,
        (
            "#3600653V#0109F#11PThat was good timing\x01",
            "on our part.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DFD")

    label("loc_7D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_7DC2")

    ChrTalk(
        0x103,
        "#3600654V#0204F#11PExactly on schedule.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7DFD")

    label("loc_7DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_7DFD")

    ChrTalk(
        0x104,
        "#3600655V#0304F#11PDamn. Good timin', Lloyd.\x02",
    )

    CloseMessageWindow()

    label("loc_7DFD")

    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        "#3600656V#1110F#5PWait, what's coming?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    TurnDirection(0xEF, 0x153, 500)

    ChrTalk(
        0x101,
        (
            "#3600657V#0004F#12PI think you'll be excited, KeA. It's\x01",
            "something you've been wanting\x01",
            "to ride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600658V#1105F#5PHmm?\x02",
    )

    CloseMessageWindow()
    Sound(467, 0, 100, 0)
    BeginChrThread(0x33, 1, 0, 60)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7F1F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F1F)
    Sleep(50)
    OP_93(0xEF, 0xB4, 0x1F4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_7F65")

    ChrTalk(
        0x102,
        "#3600659V#0102FIt's almost here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FD0")

    label("loc_7F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_7FA1")

    ChrTalk(
        0x103,
        "#3600660V#0202FApproximately 20 seconds.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FD0")

    label("loc_7FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_7FD0")

    ChrTalk(
        0x104,
        "#3600661V#0302FAny second now...\x02",
    )

    CloseMessageWindow()

    label("loc_7FD0")

    EndChrThread(0x33, 0x1)
    Fade(500)
    OP_68(2080, 600, -29850, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    ClearMapObjFlags(0x1, 0x4)

    def lambda_8012():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_8012)
    Sound(466, 0, 100, 0)
    BeginChrThread(0x33, 1, 0, 61)
    Sleep(3000)
    EndChrThread(0x33, 0x1)
    Fade(500)
    OP_68(-8650, 780, -10720, 0)
    MoveCamera(55, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18760, 0)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    SetChrPos(0x101, -11000, 180, -11600, 90)
    SetChrPos(0x153, -11000, 180, -10400, 90)
    SetChrPos(0xEF, -11000, 180, -9200, 90)
    SetChrPos(0xC, -11000, 180, -8000, 180)
    SetChrPos(0xD, -11000, 180, -6800, 180)
    SetChrPos(0x2B, -5300, 0, -21000, 0)

    def lambda_80E0():
        OP_96(0xFE, 0xFFFFEB4C, 0x0, 0xFFFFCD38, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_80E0)
    Sleep(1000)
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x2B, 1)

    ChrTalk(
        0x153,
        (
            "#3600662V#1107F#6PWhoaaaaa?! That's a\x01",
            "ginormous car!\x02",
        )
    )

    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600663V#0002F#6PThis type of car is called a bus,\x01",
            "KeA. Get it?\x02",
        )
    )

    CloseMessageWindow()
    OP_71(0x1, 0x1, 0x1E, 0x1, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x1)
    BeginChrThread(0xC, 3, 0, 57)
    Sleep(3000)

    ChrTalk(
        0x153,
        (
            "#3600664V#1105F#6PWh-Wh-What?! There's a bunch\x01",
            "of people coming out of it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600665V#0004F#6PYep. They're all people returning\x01",
            "from the hospital.\x02\x03",
            "#3600666V#0000FOnce we get on it, it'll take us\x01",
            "all the way south to St. Ursula.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x153, 0x101, 500)

    ChrTalk(
        0x153,
        (
            "#3600667V#1101F#5PWait... I get to ride this thing?!\x02\x03",
            "#3600668VWith you two?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    TurnDirection(0xEF, 0x153, 500)

    ChrTalk(
        0x101,
        "#3600669V#0002F#12PYeah, haha. I hope you're excited.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600670V#1109F#5PI'm SUPER excited!\x02\x03",
            "#3600671V#1110FC'mon, c'mon! Let's get on!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_83FC")

    ChrTalk(
        0x102,
        "#3600672V#0109F#5PWatch your step, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_849B")

    label("loc_83FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_8455")

    ChrTalk(
        0x103,
        (
            "#3600673V#0204F#5PTake note of your footing\x01",
            "as you ascend the stairs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_849B")

    label("loc_8455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_849B")

    ChrTalk(
        0x104,
        (
            "#3600674V#0309F#5PHaha. Don't trip on the way in,\x01",
            "KeDo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_849B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xC, 0x3)
    Call(0, 58)
    SetChrPos(0xC, -8900, 180, -4000, 90)
    SetChrPos(0xD, -7700, 180, -4000, 270)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x1D4)
    SetScenarioFlags(0x5C, 1)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_56_7C21 end

    def Function_57_84F0(): pass

    label("Function_57_84F0")

    BeginChrThread(0x18, 3, 0, 59)
    Sleep(1000)
    BeginChrThread(0x17, 3, 0, 59)
    Sleep(1000)
    BeginChrThread(0x1E, 3, 0, 59)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 59)
    Sleep(1000)
    WaitChrThread(0x18, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x1E, 3)
    WaitChrThread(0x11, 3)
    Return()

    # Function_57_84F0 end

    def Function_58_8525(): pass

    label("Function_58_8525")

    EndChrThread(0x18, 0x3)
    EndChrThread(0x17, 0x3)
    EndChrThread(0x1E, 0x3)
    EndChrThread(0x11, 0x3)
    Return()

    # Function_58_8525 end

    def Function_59_8536(): pass

    label("Function_59_8536")

    SetChrPos(0xFE, -6080, 600, -13010, 270)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_8561():
        OP_95(0xFE, -8730, 180, -12970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8561)

    def lambda_857B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_857B)
    WaitChrThread(0xFE, 1)

    def lambda_8590():
        OP_95(0xFE, -8850, 180, -7610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8590)
    WaitChrThread(0xFE, 1)

    def lambda_85AE():
        OP_95(0xFE, -1260, 0, -7620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_85AE)
    WaitChrThread(0xFE, 1)

    def lambda_85CC():
        OP_95(0xFE, -50, 900, 3490, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_85CC)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_59_8536 end

    def Function_60_85EA(): pass

    label("Function_60_85EA")

    Sound(468, 2, 0, 0)
    Sleep(100)
    OP_25(0x1D4, 0xA)
    Sleep(100)
    OP_25(0x1D4, 0x14)
    Sleep(100)
    OP_25(0x1D4, 0x1E)
    Sleep(100)
    OP_25(0x1D4, 0x28)
    Sleep(100)
    OP_25(0x1D4, 0x32)
    Sleep(100)
    OP_25(0x1D4, 0x3C)
    Sleep(100)
    OP_25(0x1D4, 0x46)
    Sleep(100)
    OP_25(0x1D4, 0x50)
    Sleep(100)
    OP_25(0x1D4, 0x5A)
    Sleep(100)
    OP_25(0x1D4, 0x64)
    Return()

    # Function_60_85EA end

    def Function_61_8637(): pass

    label("Function_61_8637")

    OP_25(0x1D4, 0x5A)
    Sleep(100)
    OP_25(0x1D4, 0x50)
    Sleep(100)
    OP_25(0x1D4, 0x46)
    Sleep(100)
    OP_25(0x1D4, 0x3C)
    Sleep(100)
    OP_25(0x1D4, 0x32)
    Sleep(100)
    OP_25(0x1D4, 0x28)
    Sleep(100)
    OP_25(0x1D4, 0x1E)
    Sleep(100)
    OP_25(0x1D4, 0x14)
    Sleep(100)
    OP_25(0x1D4, 0xA)
    Sleep(100)
    OP_24(0x1D4)
    Return()

    # Function_61_8637 end

    def Function_62_867A(): pass

    label("Function_62_867A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x28)
    LoadChrToIndex("apl/ch50111.itc", 0x29)
    SoundLoad(806)
    SoundLoad(891)
    OP_68(-5810, 1000, -9380, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24150, 0)
    SetChrPos(0x101, -5570, 0, -9390, 270)
    SetChrPos(0x102, -4760, 0, -10050, 270)
    SetChrPos(0x103, -3220, 0, -9280, 270)
    SetChrPos(0x104, -3850, 0, -8250, 270)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    FadeToBright(1000, 0)
    SetCameraDistance(23150, 2500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5100231V#0005F#11PHuh... That's a lot of people lined\x01",
            "up for the bus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100232V#0100F#11PThat's unusual for this time of day.\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#5100233V#0203F#11PIt is, indeed, peculiar.\x02\x03",
            "#5100234V#0200FThe most recent bus should have\x01",
            "departed five minutes ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_88A6():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_88A6)
    Sleep(50)

    def lambda_88B6():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_88B6)
    Sleep(50)

    def lambda_88C6():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_88C6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#5100235V#0001F#6PIs that right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100236V#0301F#5PHmm...\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x10E, 0x1F4)
    OP_68(-7200, 1000, -7930, 2500)

    def lambda_893B():
        OP_95(0xFE, -6860, 0, -8060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_893B)
    Sleep(300)

    def lambda_8958():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8958)
    Sleep(50)

    def lambda_8968():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8968)
    Sleep(50)

    def lambda_8978():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8978)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    TurnDirection(0x104, 0xE, 500)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#5100237V#0300F#11PYo, buddy.\x02\x03",
            "#5100238VThe bus runnin' late or somethin'?\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xE, 0xFF)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x104, 500)

    NpcTalk(
        0xE,
        "Young Man",
        "#5100239V#5PYeah, it looks that way.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Young Man",
        (
            "#5100240V#5PI've been waiting here for almost\x01",
            "20 minutes now, and not one bus\x01",
            "has shown up.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Young Man",
        (
            "#5100241V#5PWhy'd this have to happen today?\x01",
            "Visiting hours will be over by the\x01",
            "time I get there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100242V#0301F#11PYeah, huh?\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    OP_4C(0xE, 0xFF)
    OP_93(0x104, 0x5A, 0x1F4)
    OP_68(-3580, 1000, -8640, 3000)

    def lambda_8B64():

        label("loc_8B64")

        TurnDirection(0x101, 0x104, 500)
        Yield()
        Jump("loc_8B64")

    QueueWorkItem2(0x101, 1, lambda_8B64)

    def lambda_8B76():

        label("loc_8B76")

        TurnDirection(0x102, 0x104, 500)
        Yield()
        Jump("loc_8B76")

    QueueWorkItem2(0x102, 1, lambda_8B76)

    def lambda_8B88():

        label("loc_8B88")

        TurnDirection(0x103, 0x104, 500)
        Yield()
        Jump("loc_8B88")

    QueueWorkItem2(0x103, 1, lambda_8B88)

    def lambda_8B9A():
        OP_95(0xFE, -3850, 0, -8250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8B9A)
    WaitChrThread(0x104, 1)
    TurnDirection(0x104, 0x102, 500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        "#5100243V#0306F#5PThere we have it, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100244V#0108F#12PDo you think the bus is having\x01",
            "problems with the engine again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100245V#0206F#11PA likely scenario.\x02",
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8CD2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8CD2)
    Sleep(50)

    def lambda_8CE2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8CE2)
    Sleep(50)

    def lambda_8CF2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8CF2)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(150)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    SetChrSubChip(0x101, 0x5)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100246V#0001FThis is Lloyd Bannings,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5100247V\x07\x05",
            "This is Dudley. Give me a status report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100248V\x07\x00",
            "#0005FOh... Roger.\x02\x03",
            "#5100249V#0000FWe were able to successfully secure the\x01",
            "assistance of the Bracer Guild with the case.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that the guild agreed to aid\x01",
            "in the search for the missing persons and mafia.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5100250V\x07\x05",
            "Hmph. So you've gone and made yourselves\x01",
            "indebted to MacLaine.\x02\x03",
            "#5100251VFine. I'm sure that, with their abilities,\x01",
            "they'll be able to produce results.\x02\x03",
            "#5100252VI'm trying to deal with the top brass on my end.\x01",
            "Now that they've realized the whole damn mafia\x01",
            "has vanished, they're throwing a tantrum.\x02\x03",
            "#5100253VIt may be a while until I can act freely.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100254V\x07\x00",
            "#0003FUnderstood.\x02\x03",
            "#5100255V#0001FI just remembered. Your division was in\x01",
            "charge of investigating the airport, right?\x01",
            "What happened with the bomb threat?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5100256V\x07\x05",
            "There's a strong possibility the whole\x01",
            "thing was a hoax.\x02\x03",
            "#5100257VWe scanned the entire airport with orbal\x01",
            "detectors, but nothing was found.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100258V\x07\x00",
            "#0013FI can't help but shake the feeling that this\x01",
            "is related to Revache's disappearance...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5100259V\x07\x05",
            "We're looking into it.\x02\x03",
            "#5100260VWait. If you know the situation is clear\x01",
            "there, that must mean you're nearby.\x02\x03",
            "#5100261VI hope you don't plan to pull your usual\x01",
            "stunt by getting involved with cases that\x01",
            "clearly aren't yours.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100262V\x07\x00",
            "#0000FYou can rest easy, sir. We're actually\x01",
            "on the way to St. Ursula right now.\x02\x03",
            "#5100263VWe still haven't received the results of the\x01",
            "drug's composition, so we decided to go\x01",
            "pay the doctor a visit.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5100264V\x07\x05",
            "What? You still haven't heard back from him?\x02\x03",
            "#5100265VHah. Rookies will be rookies. You need to be\x01",
            "far more direct if you want any semblance of\x01",
            "punctuality from others.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100266V\x07\x00",
            "#0006FS-Sorry.\x01",
            "(We'll need to remember that...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5100267V\x07\x05",
            "It'll be much easier to convince the top brass\x01",
            "to take action once we've found out what those\x01",
            "pills actually are.\x02\x03",
            "#5100268VBut I'm afraid we have no choice but to place\x01",
            "our faith in that doctor of yours.\x02\x03",
            "#5100269VBy the way, what's the man's name?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100270V\x07\x00",
            "#0005FOh, we haven't told you yet?\x02\x03",
            "#5100271V#0000FDoctor Joachim Guenter. He's an associate professor\x01",
            "of neurology and pharmacology at St. Ursula.\x02\x03",
            "#5100272VHe's only in his mid-thirties, but he's managed to\x01",
            "build a name for himself.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5100273V\x07\x05",
            "I see. Hopefully, it means he'll come through\x01",
            "with proper results.\x02\x03",
            "#5100274VHmm?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100275V\x07\x00",
            "#0001FHuh? What's wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5100276V\x07\x05",
            "Back up a second. You said Guenter, right?\x02\x03",
            "#5100277VWears glasses? Far too relaxed?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100278V\x07\x00",
            "#0005FYes, that sounds like him...\x01",
            "Have you two met?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1388)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5100279V\x07\x05",
            "#40W...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100280V\x07\x00",
            "#0001FWhy the silence, Dudley?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5100281V\x07\x05",
            "I met him for the first time two months ago.\x02\x03",
            "#5100282VI was investigating the man who plotted the\x01",
            "mayor's assassination during Arc en Ciel's\x01",
            "private performance...\x02\x03",
            "#5100283VThe mayor's former secretary, Ernest Reis.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100284V\x07\x00",
            "#0005FWait.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7203", 0)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5100285V\x07\x05",
            "Sergei may have informed you already,\x01",
            "but Reis was completely deranged.\x02\x03",
            "#5100286VSo as a last resort, Sergei called Reis'\x01",
            "physician, a man working at St. Ursula.\x02\x03",
            "#5100287VAnd thanks to Guenter's help, I was\x01",
            "finally able to question Reis.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100288V\x07\x00",
            "#0011FH-Hold on a moment, Dudley.\x02\x03",
            "#5100289VAre you claiming that Doctor Guenter\x01",
            "was Ernest's physician?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5100290V\x07\x05",
            "Yes. The very same.\x02\x03",
            "#5100291VI'd gained an immense amount of respect\x01",
            "for him, given how helpful he was, but...\x02\x03",
            "#5100292V...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100297V\x07\x00",
            "#0003F...\x02\x03",
            "#5100294V#0013FUnderstood. We'll see what intel we can\x01",
            "get without tipping him off.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5100295V\x07\x05",
            "Good plan.\x02\x03",
            "#5100296VAnyway, try not to waste any time!\x01",
            "I'll contact you later.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(825, 0, 100, 0)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100293V\x07\x00",
            "#0008F#30W...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(807, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5100298V#0105F#12PWhat was that all about? Your\x01",
            "conversation sounded anything\x01",
            "but normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100299V#0205F#11PIs there a connection between Doctor Guenter\x01",
            "and Ernest?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#5100315V#0003F#6PY-Yeah, apparently.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained everything Dudley\x01",
            "told him to the others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#5100301V#0101F#12PTh-That can't be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100302V#0303F#5PHold up. Let's think back a bit...\x02\x03",
            "#5100303V#0301FRemember how Ernest's strength was\x01",
            "totally off the charts? Dude was cocky\x01",
            "as hell, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100304V#0206F#11PIt is eerily similar to Gantz's case,\x01",
            "is it not?\x02\x03",
            "#5100305V#0208FTo further that point, his attending\x01",
            "physician was Doctor Guenter...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x102,
        (
            "#5100306V#0101F#12PI'll try calling the hospital's reception desk.\x02\x03",
            "#5100307VWe have to confirm that Doctor Guenter hasn't\x01",
            "left the hospital.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A24C():
        TurnDirection(0xFE, 0x102, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A24C)

    def lambda_A259():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A259)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x101,
        "#5100308V#0001F#6PYeah, that's a good idea.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x190)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x10)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(200)
    Sound(807, 0, 100, 0)
    Sleep(800)
    Sound(891, 2, 100, 0)
    Sleep(2500)

    ChrTalk(
        0x102,
        (
            "#5100309V#0103F#5P...\x02\x03",
            "#5100310V#0108FNobody's answering the phone.\x02\x03",
            "#5100311VThe line isn't busy, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x37B)
    Sound(807, 0, 100, 0)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x2)
    ClearChrFlags(0x102, 0x10)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_93(0x102, 0x0, 0x190)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#5100312V#0203F#11PWe now have a late bus, an\x01",
            "unresponsive hospital...\x02\x03",
            "#5100313V#0201F...and a new, unexpected\x01",
            "relationship in the case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100314V#0301F#5PThis all seems a lil' too damn\x01",
            "convenient, doesn't it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5100300V#0003F#6PAgreed.\x02\x03",
            "#5100316V#0013FThe day's almost over. Let's hurry\x01",
            "to St. Ursula.\x02\x03",
            "#5100317VIf we manage to spot the bus, we'll\x01",
            "flag it down and get it to take us there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100318V#0101F#12POkay!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(21650, 2500)
    OP_6F(0x79)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x28)
    OP_D5(0x29)
    SetChrPos(0x0, -4680, 0, -11060, 180)
    SetScenarioFlags(0xE0, 1)
    OP_29(0x4D, 0x1, 0x1)
    ReplaceBGM("ed7000", "ed7000")
    ReplaceBGM("ed7200", "ed7203")
    ReplaceBGM("ed7202", "ed7203")
    ReplaceBGM("ed7100", "ed7203")
    ReplaceBGM("ed7101", "ed7203")
    ReplaceBGM("ed7111", "ed7203")
    ReplaceBGM("ed7116", "ed7203")
    ReplaceBGM("ed7117", "ed7203")
    ReplaceBGM("ed7124", "ed7203")
    OP_24(0x326)
    OP_24(0x37B)
    EventEnd(0x5)
    Return()

    # Function_62_867A end

    def Function_63_A60E(): pass

    label("Function_63_A60E")

    EventBegin(0x0)
    Sleep(1000)
    OP_68(-9260, 1500, -12230, 3000)
    MoveCamera(45, 21, 0, 3000)
    OP_6E(510, 5000)
    SetCameraDistance(23500, 5000)
    OP_6F(0x79)
    Sound(828, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Check any bus stop sign to board an orbal bus.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This allows you to quickly reach your\x01",
            "destination and travel across Crossbell State.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 7)
    EventEnd(0x5)
    Return()

    # Function_63_A60E end

    def Function_64_A6E7(): pass

    label("Function_64_A6E7")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0x3B, 0x80)
    OP_68(50680, 2860, -111330, 0)
    MoveCamera(55, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17280, 0)
    LoadChrToIndex("apl/ch50387.itc", 0x32)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, 49980, 900, -106970, 102)
    SetChrPos(0x102, 52090, 900, -107470, 102)
    SetChrPos(0x103, 50300, 900, -109260, 102)
    SetChrPos(0x104, 51400, 900, -110070, 102)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#12P#0300FSo this big ol' body of water\x01",
            "is the Lupinus River, eh?\x02\x03",
            "#0305FWhat's that thingy floatin' all the way\x01",
            "out in the middle supposed to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0003FI'm going to guess they're some old ruins...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FThe database contains no details, either.\x02\x03",
            "#0200FThe only information I found was that\x01",
            "entry is prohibited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FI can't speak to the ruins' origins, but I've\x01",
            "heard people refer to it as a matchmaking\x01",
            "shrine.\x02\x03",
            "#0104FIf a man stands on the left of the observation\x01",
            "platform, and a woman to the right, they can\x01",
            "give their vows and live happily ever after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0306FI-I don't know about that, Mademois-Elie.\x01",
            "That kind of sounds like an old wives' tale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FHmm. I bet we could take a great photo\x01",
            "of this area for Grace's article.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B278")
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#6P#0000FDo you mind taking a few photos\x01",
            "for us, Elie?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#6P#0108FN-Not at all. Don't expect a masterpiece\x01",
            "from me, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x104,
        (
            "#12P#0300FPssh. Relax, Mademois-Elie.\x02\x03",
            "Ya just gotta peek through that lens,\x01",
            "give it a lil' click, then bam, we good!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x102,
        (
            "#6P#0103F*sigh* If only capturing a great\x01",
            "photo were that simple...\x02\x03",
            "#0100FYou need to pay close attention to\x01",
            "your composition to ensure you've\x01",
            "captured everything in frame.\x02\x03",
            "The weather, wind speed, and lighting\x01",
            "can completely alter the impression\x01",
            "a photo gives.\x02\x03",
            "There are no second chances when\x01",
            "it comes to a picture-perfect moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FThe difference in quality between\x01",
            "amateur and professional photography\x01",
            "is immediately apparent.\x02\x03",
            "#0203FI would imagine a simpleton would have\x01",
            "difficulty grasping any level of intricacy\x01",
            "or nuance, however.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        "#12P#0306FDamn, Tio Tot. You implyin' something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FC-Calm down, everyone. We should\x01",
            "let Elie focus on taking the photo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FRight... I'll try to live up to your\x01",
            "expectations.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x66, 0x1F4)
    OP_93(0x101, 0x66, 0x1F4)
    OP_93(0x103, 0x66, 0x1F4)
    OP_93(0x104, 0x66, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#6P#0103FPhew... There we go. I took a\x01",
            "couple of extras, just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FHey, it looks like you pulled through.\x02\x03",
            "Well? How'd they turn out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FI won't have an answer for you until\x01",
            "I've seen the developed photos.\x02\x03",
            "At the very least, I think they'll\x01",
            "get the job done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FIt would be a safe assumption to think\x01",
            "Elie has regained her photography skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FWell, I'm no picture-takin' guru,\x01",
            "but I'm sure they turned out fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FRight. We should keep our eyes\x01",
            "peeled for other scenic locations\x01",
            "we can take photos of.\x02\x03",
            "But anyway, let's get a move on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5F1")

    label("loc_B278")

    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#6P#0000FWill you do the honors, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FOkay. Leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x66, 0x1F4)
    OP_93(0x101, 0x66, 0x1F4)
    OP_93(0x103, 0x66, 0x1F4)
    OP_93(0x104, 0x66, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#0100FPhew... I hope they turned out okay.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_B40E")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B40E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_B425")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B425")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_B43C")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B43C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_B453")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B453")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_B46A")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B46A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_B481")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B481")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_B498")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B498")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_B4AF")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_B4C6")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B593")

    ChrTalk(
        0x101,
        (
            "#6P#0000FGood job, Elie. You look like you're\x01",
            "getting the hang of it again.\x02\x03",
            "And now we've managed to meet Grace's\x01",
            "five-photo quota. Let's run these by her\x01",
            "when we get the chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5F1")

    label("loc_B593")


    ChrTalk(
        0x101,
        (
            "#6P#0000FNice, Elie! You looked pretty confident\x01",
            "taking that picture.\x02\x03",
            "Shall we move on?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5F1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 52100, 900, -107040, 102)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x32)
    OP_29(0x18, 0x1, 0x4)
    Sleep(500)
    ClearMapFlags(0x8000000)
    OP_37()
    OP_65(0x4, 0x1)
    OP_66(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_64_A6E7 end

    def Function_65_B631(): pass

    label("Function_65_B631")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B8B7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7E0")

    ChrTalk(
        0x10A,
        (
            "#0603FThey should have left matters in the\x01",
            "First Division's hands.\x02\x03",
            "#0601FIf there wasn't that matter with the top brass,\x01",
            "we could have been focusing our attention\x01",
            "on Revache by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FYou seem perturbed, Dudley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHey, poindexter. Sounds like the First Division's\x01",
            "got their fair share of problems, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0600FShut it, Orlando.\x01",
            "We have our own matters\x01",
            "to take care of!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8B2")

    label("loc_B7E0")


    ChrTalk(
        0x10A,
        (
            "#0601FAnd where do you think you're going?\x01",
            "Don't you DARE go to the airport. The\x01",
            "First Division has it handled! Understood?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FY-Yes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108F(Dudley seems awfully irritated, doesn't he?)\x02",
    )

    CloseMessageWindow()

    label("loc_B8B2")

    Jump("loc_BA4B")

    label("loc_B8B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA13")
    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9A3")

    ChrTalk(
        0xF,
        "Hold it, Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We're conducting an inspection of\x01",
            "the airport's equipment, so I can't\x01",
            "allow you to enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(Inspecting equipment...?\x01",
            "Something feels off.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_BA03")

    label("loc_B9A3")


    ChrTalk(
        0xF,
        (
            "Hold it, Special Support Section.\x01",
            "Entry into the Crossbell Airport\x01",
            "is strictly prohibited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA03")

    OP_93(0xF, 0x10E, 0x1F4)
    OP_4C(0xF, 0xFF)
    Jump("loc_BA4B")

    label("loc_BA13")


    ChrTalk(
        0x101,
        (
            "#0000FWe don't have any business\x01",
            "at the airport...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA4B")

    Sleep(50)
    SetChrPos(0x0, 11250, 0, -17610, 270)
    EventEnd(0x4)
    Return()

    # Function_65_B631 end

    def Function_66_BA62(): pass

    label("Function_66_BA62")

    EventBegin(0x1)
    OP_4B(0x29, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_63(0x29, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_BA9B():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_BA9B)

    def lambda_BAA8():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_BAA8)

    ChrTalk(
        0x29,
        "Dudley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "It's good to see you, Detective Dudley, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "But why are you with the\x01",
            "Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0603FI'll give you the details later.\x02\x03",
            "#0600FBut for now, how is the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "It was all a hoax, much like we anticipated.\x01",
            "We're currently investigating the origin\x01",
            "of the threat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0608FHmm, I see.\x02\x03",
            "#0600FI will reconvene with you later, but until then,\x01",
            "the First Division is in your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Roger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        "Yes, sir!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xC9, 3)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(50)
    OP_93(0x29, 0xB4, 0x0)
    OP_93(0xF, 0x0, 0x0)
    SetChrPos(0x0, 11250, 0, -17610, 270)
    OP_4C(0x29, 0xFF)
    OP_4C(0xF, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_66_BA62 end

    def Function_67_BCAC(): pass

    label("Function_67_BCAC")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD73")

    ChrTalk(
        0x101,
        (
            "#0003F(Wait. We still have that trunk we received\x01",
            "from the Rosenberg Studio.)\x02\x03",
            "#0000F(It looks pretty valuable, so we'd better\x01",
            "hand it off to Imelda first.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE8B")

    label("loc_BD73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE08")

    ChrTalk(
        0x101,
        (
            "#0000FSince we're here, let's take the bus.\x02\x03",
            "There's a schedule at the bus stop we can\x01",
            "check to see when the next bus comes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE8B")

    label("loc_BE08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE8B")

    ChrTalk(
        0x101,
        (
            "#0003FKeA's with us, so we can't really\x01",
            "traverse the highway on foot.\x02\x03",
            "#0000FIt'd be best to just take the bus.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE8B")

    SetChrPos(0x0, 0, 0, -46000, 0)
    EventEnd(0x4)
    Return()

    # Function_67_BCAC end

    def Function_68_BE9F(): pass

    label("Function_68_BE9F")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#0005FWait a second... We still have that trunk\x01",
            "we received from the Rosenberg Studio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FIt's quite valuable, so we should give it to\x01",
            "Imelda before we depart for the hospital.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_68_BE9F end

    def Function_69_BF64(): pass

    label("Function_69_BF64")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "North: Crossbell City\x01",
            "East: Crossbell Airport\x01",
            "South: St. Ursula Medical College - 153 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_69_BF64 end

    SaveToFile()

Try(main)
