from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1530.bin",                # FileName
        "r1530",                    # MapName
        "r1530",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("r1530", "r0000_1", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 3000, -90000, 28000, 0, 0, 1, 96, 0, 2, 0, 3],
    )

    BuildStringList((
        "r1530",                  # 0
        "Chiruru",                # 1
        "Kopan",                  # 2
        "Peter",                  # 3
        "Peter",                  # 4
        "Master Fisherman Lloyd", # 5
        "Branch Manager Cerdan",  # 6
        "Doctor Guenter",         # 7
        "Bus",                    # 8
        "Backlash",               # 9
        "br1500",                 # 10
        "br1520",                 # 11
        "br1500",                 # 12
        "br1520",                 # 13
        "br1500",                 # 14
        "br1500",                 # 15
        "br1520",                 # 16
        "br1520",                 # 17
        "br1520",                 # 18
        "To Crossbell City",      # 19
        "To St. Ursula Medical College",# 20
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 2,   8,   0,   6,   2,   0,   0)
    Sepith("Sepith_B4", 0,   8,   0,   4,   4,   2,   0)
    Sepith("Sepith_C4", 7,   3,   5,   3,   0,   0,   0)
    Sepith("Sepith_D4", 0,   3,   0,   0,   5,   5,   5)
    Sepith("Sepith_E4", 0,   8,   0,   2,   2,   4,   2)
    Sepith("Sepith_F4", 4,   2,   0,   8,   0,   3,   2)

    MonsterBattlePostion("MonsterBattlePostion_104", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_128", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_12C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_130", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_134", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_138", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_13C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_144", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_148", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_14C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_150", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_154", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_158", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_15C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 2, 13, 180)

    # monster count: 15

    BattleInfo(
        "BattleInfo_164", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_A4", 30, 40, 20, 10,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", "ms69800.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_22C", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_B4", 30, 40, 20, 10,
        (
            ("ms63600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63600.dat", "ms63600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_2F4", 0x0000, 12, 6, 45, 10, 1, 50, 0, "br1520", "Sepith_C4", 30, 40, 20, 10,
        (
            ("ms65300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65300.dat", "ms65300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65300.dat", "ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3BC", 0x0000, 12, 6, 45, 10, 1, 40, 0, "br1520", "Sepith_D4", 30, 40, 20, 10,
        (
            ("ms65200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65200.dat", "ms65200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65200.dat", "ms65200.dat", "ms65200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65200.dat", "ms65200.dat", "ms65200.dat", "ms65200.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_484", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1520", "Sepith_E4", 30, 40, 20, 10,
        (
            ("ms61300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61300.dat", "ms61300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61300.dat", "ms61300.dat", "ms61300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61300.dat", "ms61300.dat", "ms61300.dat", "ms61300.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_54C", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_F4", 30, 40, 20, 10,
        (
            ("ms62100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62100.dat", "ms62100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62100.dat", "ms69700.dat", "ms62100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62100.dat", "ms62100.dat", "ms65800.dat", "ms62100.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_614", 0x0000, 12, 6, 45, 10, 1, 50, 0, "br1500", "Sepith_C4", 30, 40, 20, 10,
        (
            ("ms65300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65300.dat", "ms65300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65300.dat", "ms65300.dat", "ms65200.dat", "ms65300.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_6DC", 0x0000, 12, 6, 45, 0, 1, 0, 0, "br1520", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65300.dat", "ms65300.dat", "ms65300.dat", "ms65300.dat", "ms65300.dat", "ms65300.dat", "ms65300.dat", "ms65300.dat", "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch20500.itc",                   # 00
        "apl/ch50166.itc",                   # 01
        "apl/ch50165.itc",                   # 02
        "chr/ch24200.itc",                   # 03
        "apl/ch50169.itc",                   # 04
        "apl/ch50164.itc",                   # 05
        "apl/ch50377.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch62150.itc",               # 10
        "monster/ch62151.itc",               # 11
        "monster/ch65250.itc",               # 12
        "monster/ch65251.itc",               # 13
        "monster/ch63650.itc",               # 14
        "monster/ch63650.itc",               # 15
        "monster/ch61350.itc",               # 16
        "monster/ch61350.itc",               # 17
        "monster/ch69750.itc",               # 18
        "monster/ch69750.itc",               # 19
        "monster/ch65350.itc",               # 1A
        "monster/ch65351.itc",               # 1B
    ))

    DeclNpc(-13489,  -6010,   -41110,  159,  385,  0x0, 0,   0,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(39619,   -6300,   -65120,  180,  405,  0x0, 0,   1,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(29520,   -6289,   -65250,  270,  405,  0x0, 0,   2,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-19620,  0,       -10680,  135,  389,  0x0, 0,   3,   0,   0,   1,   0,   16,  255,  0)
    DeclNpc(20459,   -6300,   -50159,  270,  405,  0x0, 0,   4,   0,   255, 255, 0,   34,  255,  0)
    DeclNpc(28489,   -6170,   -59029,  180,  405,  0x0, 0,   5,   0,   255, 255, 0,   35,  255,  0)
    DeclNpc(44099,   -5610,   -18569,  0,    439,  0x0, 0,   6,   0,   255, 255, 0,   33,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(38689,   -4500,   -53729,  0,    484,  0x0, 0,   26,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(4930,    10160,   0,       0x1010000,    "BattleInfo_164", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-33140,  -4930,   0,       0x1010000,    "BattleInfo_22C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-38450,  -31510,  -2800,   0x1010000,    "BattleInfo_22C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-17540,  -38170,  -5600,   0x1010000,    "BattleInfo_2F4", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-5060,   -13330,  -6300,   0x1010000,    "BattleInfo_3BC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4200,    -20550,  -6300,   0x1010000,    "BattleInfo_484", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(2370,    -42510,  -6300,   0x1010000,    "BattleInfo_3BC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(19970,   -49310,  -6300,   0x1010000,    "BattleInfo_484", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(33630,   -23560,  -5600,   0x1010000,    "BattleInfo_3BC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(52410,   -28230,  -5600,   0x1010000,    "BattleInfo_484", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-38810,  -52060,  -4200,   0x1010000,    "BattleInfo_54C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-21590,  -49910,  -4200,   0x1010000,    "BattleInfo_54C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-30050,  -108200, -4900,   0x1010000,    "BattleInfo_164", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-16070,  -108310, -5770,   0x1010000,    "BattleInfo_614", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-15000,  -92180,  -5770,   0x1010000,    "BattleInfo_614", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 25,  -37.0,                 -108.5,                -5.900000095367432,    225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   12.333333969116211,    10.850000381469727,    1.1800000667572021,    1.0])
    DeclEvent(0x0040, 0, 27,  -18.100000381469727,   -10.199999809265137,   -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.262500047683716,     1.274999976158142,     0.20000000298023224,   1.0])

    DeclActor(38690,   -5500,   -53730,  1200,    38690,   -4500,   -53730,  0x007C, 0,  4,  0x0000)
    DeclActor(49800,   -5600,   -17450,  1200,    49800,   -4600,   -17450,  0x007C, 0,  5,  0x0000)
    DeclActor(-14500,  -5800,   -88320,  1200,    -14500,  -4800,   -88320,  0x007C, 0,  6,  0x0000)
    DeclActor(-24850,  0,       -2920,   1200,    -24850,  1000,    -2920,   0x007C, 0,  20, 0x0000)
    DeclActor(51410,   -6300,   -59200,  1200,    57770,   -5300,   -59100,  0x007C, 0,  18, 0x0000)
    DeclActor(-5450,   0,       11740,   1200,    -5450,   0,       11740,   0x007C, 0,  7,  0x0000)
    DeclActor(-37940,  -4200,   -50580,  1200,    -37940,  -4200,   -50580,  0x007C, 0,  8,  0x0000)
    DeclActor(-50120,  -4900,   -118170, 1200,    -50120,  -4900,   -118170, 0x007C, 0,  9,  0x0000)
    DeclActor(18070,   -6300,   -56430,  1200,    14290,   -6300,   -56430,  0x007C, 0,  19, 0x0000)

    PlaceName(7.0, 0.0, 52.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(-89.0, 0.0, -115.0, 0x0000, 0x0000, "To St. Ursula Medical College")
    PlaceName(-24.700000762939453, 0.0, -2.950000047683716, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5, 6, 7])              # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 11

    ScpFunction((
        "Function_0_DD8",          # 00, 0
        "Function_1_DF7",          # 01, 1
        "Function_2_EAF",          # 02, 2
        "Function_3_100D",         # 03, 3
        "Function_4_156D",         # 04, 4
        "Function_5_178C",         # 05, 5
        "Function_6_18D5",         # 06, 6
        "Function_7_1A21",         # 07, 7
        "Function_8_1A35",         # 08, 8
        "Function_9_1A49",         # 09, 9
        "Function_10_1A5D",        # 0A, 10
        "Function_11_1B27",        # 0B, 11
        "Function_12_1C48",        # 0C, 12
        "Function_13_1D69",        # 0D, 13
        "Function_14_1DFE",        # 0E, 14
        "Function_15_1F42",        # 0F, 15
        "Function_16_272A",        # 10, 16
        "Function_17_2B60",        # 11, 17
        "Function_18_2D09",        # 12, 18
        "Function_19_2E2B",        # 13, 19
        "Function_20_2F11",        # 14, 20
        "Function_21_2FB1",        # 15, 21
        "Function_22_37BE",        # 16, 22
        "Function_23_39F4",        # 17, 23
        "Function_24_3A52",        # 18, 24
        "Function_25_3C2D",        # 19, 25
        "Function_26_444E",        # 1A, 26
        "Function_27_49F8",        # 1B, 27
        "Function_28_4AFE",        # 1C, 28
        "Function_29_4F6D",        # 1D, 29
        "Function_30_62B0",        # 1E, 30
        "Function_31_7AAC",        # 1F, 31
        "Function_32_7AD9",        # 20, 32
        "Function_33_7B06",        # 21, 33
        "Function_34_7F5E",        # 22, 34
        "Function_35_8B39",        # 23, 35
        "Function_36_95F5",        # 24, 36
        "Function_37_96B0",        # 25, 37
        "Function_38_99BF",        # 26, 38
    ))


    def Function_0_DD8(): pass

    label("Function_0_DD8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DF6")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_0_DD8")

    label("loc_DF6")

    Return()

    # Function_0_DD8 end

    def Function_1_DF7(): pass

    label("Function_1_DF7")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_E37"),
        (1, "loc_E43"),
        (2, "loc_E4F"),
        (3, "loc_E5B"),
        (4, "loc_E67"),
        (5, "loc_E73"),
        (6, "loc_E7F"),
        (SWITCH_DEFAULT, "loc_E8B"),
    )


    label("loc_E37")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_E97")

    label("loc_E43")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_E97")

    label("loc_E4F")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_E97")

    label("loc_E5B")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_E97")

    label("loc_E67")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_E97")

    label("loc_E73")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_E97")

    label("loc_E7F")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E97")

    label("loc_E8B")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E97")

    label("loc_E97")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EAE")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E97")

    label("loc_EAE")

    Return()

    # Function_1_DF7 end

    def Function_2_EAF(): pass

    label("Function_2_EAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F63")
    SetChrPos(0x9, 3350, -6300, -18380, 0)
    SetChrPos(0xA, 2660, -6300, -42330, 160)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F09")
    ClearChrFlags(0xE, 0x80)

    label("loc_F09")

    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)

    label("loc_F63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F7B")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    label("loc_F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F98")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)

    label("loc_F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FB5")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)

    label("loc_FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC6")
    Event(0, 21)

    label("loc_FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_FDA")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 22)
    Jump("loc_FFD")

    label("loc_FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_FEE")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 24)
    Jump("loc_FFD")

    label("loc_FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_FFD")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 26)

    label("loc_FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_100C")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 13)

    label("loc_100C")

    Return()

    # Function_2_EAF end

    def Function_3_100D(): pass

    label("Function_3_100D")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1025")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_10CF")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xF1, 0xC2, 0xB1, 0x0, 0x1AE, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    SetMapObjFrame(0xFF, "water00", 0x2, "red")
    SetMapObjFrame(0xFF, "water01", 0x2, "red")
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x2)
    SetMapObjFlags(0x0, 0x400)
    SetMapObjFlags(0x0, 0x1000)
    OP_78(0x0, 0xF)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    SetChrPos(0xF, -58400, -4900, -105400, 285)
    OP_D3(0xF, 0x0, 0x45948, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x1E)

    label("loc_10CF")

    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F1")
    Jump("loc_1110")

    label("loc_10F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_110B")
    Jump("loc_1110")

    label("loc_110B")

    ModifyEventFlags(0, 1, 0x80)

    label("loc_1110")

    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1333")
    OP_70(0x1, 0x0)
    Jump("loc_1337")

    label("loc_1333")

    OP_70(0x1, 0x1E)

    label("loc_1337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134A")
    OP_70(0x2, 0x0)
    Jump("loc_134E")

    label("loc_134A")

    OP_70(0x2, 0x1E)

    label("loc_134E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1361")
    OP_70(0x3, 0x0)
    Jump("loc_1365")

    label("loc_1361")

    OP_70(0x3, 0x1E)

    label("loc_1365")

    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 4)), scpexpr(EXPR_END)), "loc_13CF")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 25130, 2000, -11040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)
    Jump("loc_1486")

    label("loc_13CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 5)), scpexpr(EXPR_END)), "loc_142D")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 25130, 2000, -11040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x6, 0x1)
    Jump("loc_1486")

    label("loc_142D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 6)), scpexpr(EXPR_END)), "loc_1486")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 25130, 2000, -11040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x7, 0x1)

    label("loc_1486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1498")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)

    label("loc_1498")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 57770, -5300, -59100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_65(0x8, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1536")
    OP_66(0x8, 0x1)
    PlayEffect(0x8, 0x7, 0xFF, 0x0, 14290, -6300, -56430, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_1536")

    SoundDistance(0x7D, 0x8DF4, 0xFFFFEA20, 0xFA32, 0x15F90, 0x11170, 0x64, 0x0)
    OP_E1(0x3F52, 0xFFFFE976, 0xFFFE520A)
    OP_E1(0xFFFFF10A, 0xFFFFECDC, 0xFFFDF6AC)
    Return()

    # Function_3_100D end

    def Function_4_156D(): pass

    label("Function_4_156D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_172C")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166C")
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x10, 0x0, 0)
    OP_98(0x10, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_15C6():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_15C6)

    def lambda_15E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_15E0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x10, 1)
    Battle("BattleInfo_6DC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_164D"),
        (2, "loc_165C"),
        (1, "loc_1669"),
        (SWITCH_DEFAULT, "loc_166C"),
    )


    label("loc_164D")

    SetScenarioFlags(0x74, 1)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_166C")

    label("loc_165C")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1669")

    OP_B7(0x0)
    Return()

    label("loc_166C")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E0, 1)"), scpexpr(EXPR_END)), "loc_16C4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5E0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_1727")

    label("loc_16C4")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5E0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1727")

    Jump("loc_1780")

    label("loc_172C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Thanks, actually. I needed to get that\x01",
            "off my chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1780")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_156D end

    def Function_5_178C(): pass

    label("Function_5_178C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1876")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_180C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_1871")

    label("loc_180C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1871")

    Jump("loc_18C9")

    label("loc_1876")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Did it just get a lot Brighter out here?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_18C9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_178C end

    def Function_6_18D5(): pass

    label("Function_6_18D5")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BF")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x82, 1)"), scpexpr(EXPR_END)), "loc_1955")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_19BA")

    label("loc_1955")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_19BA")

    Jump("loc_1A15")

    label("loc_19BF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This tree didn't IMPEDE you from seeing me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1A15")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_18D5 end

    def Function_7_1A21(): pass

    label("Function_7_1A21")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 4)
    OP_65(0x5, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_1A21 end

    def Function_8_1A35(): pass

    label("Function_8_1A35")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_8_1A35 end

    def Function_9_1A49(): pass

    label("Function_9_1A49")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 6)
    OP_65(0x7, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_9_1A49 end

    def Function_10_1A5D(): pass

    label("Function_10_1A5D")

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
            "Crossbell City - South Exit\x01",      # 0
            "St. Ursula Medical College\x01",       # 1
            "Leave\x01",                            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AFF")
    Call(0, 11)
    ClearMapFlags(0x8000000)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1B1F")

    label("loc_1AFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B1F")
    Call(0, 12)
    ClearMapFlags(0x8000000)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()

    label("loc_1B1F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1A5D end

    def Function_11_1B27(): pass

    label("Function_11_1B27")

    Fade(1000)
    OP_68(-20430, 600, -680, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(26000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -25190, 0, -1760, 180)
    SetChrPos(0x1, -24640, 0, -460, 180)
    SetChrPos(0x2, -23960, 0, 1080, 180)
    SetChrPos(0x3, -23400, 0, 2850, 180)
    ClearChrFlags(0xF, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0xF)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xF, -29550, -10, -16070, 45)
    OP_D3(0xF, 0x0, 0xAFC8, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_1C02():
        OP_95(0xFE, -18960, 0, -5010, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1C02)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xF, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_11_1B27 end

    def Function_12_1C48(): pass

    label("Function_12_1C48")

    Fade(1000)
    OP_68(-22010, 600, -2420, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(26000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -25190, 0, -1760, 180)
    SetChrPos(0x1, -24640, 0, -460, 180)
    SetChrPos(0x2, -23960, 0, 1080, 180)
    SetChrPos(0x3, -23400, 0, 2850, 180)
    ClearChrFlags(0xF, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0xF)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xF, -6730, 0, 7220, 225)
    OP_D3(0xF, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_1D23():
        OP_95(0xFE, -18960, 0, -5010, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1D23)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xF, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_12_1C48 end

    def Function_13_1D69(): pass

    label("Function_13_1D69")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -25540, 0, -2260, 225)
    SetChrPos(0x1, -25540, 0, -2260, 225)
    SetChrPos(0x2, -25540, 0, -2260, 225)
    SetChrPos(0x3, -25540, 0, -2260, 225)
    OP_68(-25540, 600, -2260, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_13_1D69 end

    def Function_14_1DFE(): pass

    label("Function_14_1DFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E99")
    OP_93(0xFE, 0x9F, 0x0)

    ChrTalk(
        0xFE,
        "Look at how clear the water is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like I was right. The highway is\x01",
            "way better for walks than the city streets.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F3E")

    label("loc_1E99")

    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Did you guys come out here for an\x01",
            "afternoon stroll as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not every day you see people\x01",
            "skip the bus in favor of walking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F3E")

    TalkEnd(0xFE)
    Return()

    # Function_14_1DFE end

    def Function_15_1F42(): pass

    label("Function_15_1F42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_211C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B8")

    ChrTalk(
        0xFE,
        (
            "I actually saw that twintailed bracer girl\x01",
            "out here fishing yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She showed up and caught a gorgeous\x01",
            "pearlglass. That thing had to have been\x01",
            "220 rege long!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, she was all, 'Well, duty calls.\x01",
            "See you guys later!' and walked off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've never seen a girl that confident\x01",
            "in her angling abilities. What's her deal?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2117")

    label("loc_20B8")


    ChrTalk(
        0xFE,
        "Who the heck was that girl?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe the branch manager knows\x01",
            "a thing or two about her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2117")

    Jump("loc_2726")

    label("loc_211C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2207")

    ChrTalk(
        0xFE,
        (
            "Hmm. You're Master Fisherman Lloyd, huh?\x01",
            "Looks like you've made a lot of progress...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't get ahead of yourself, though...\x01",
            "I'm a Master Fisher, too, y'know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm not about to let you outdo me!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2271")

    label("loc_2207")


    ChrTalk(
        0xFE,
        (
            "Yesterday's competition was a close,\x01",
            "hard-fought battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Trust me. Next time will be different!\x02",
    )

    CloseMessageWindow()

    label("loc_2271")

    Jump("loc_2726")

    label("loc_2276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2726")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_22C6")

    ChrTalk(
        0xFE,
        (
            "What's this...? I sense fish\x01",
            "that need catching!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2726")

    label("loc_22C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_243B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B5")

    ChrTalk(
        0xFE,
        (
            "Oh, you're competing against\x01",
            "Joachim?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just remember to have a good time, okay?\x01",
            "Never forget that your desire to fish comes\x01",
            "from the heart, not out of obligation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sorry. I wanted to sound cool.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2436")

    label("loc_23B5")


    ChrTalk(
        0xFE,
        (
            "Just remember to have a good time, okay?\x01",
            "Never forget that your desire to fish comes\x01",
            "from the heart, not out of obligation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2436")

    Jump("loc_2726")

    label("loc_243B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25FC")

    ChrTalk(
        0xFE,
        (
            "Oh, there you are, Lloyd. I see you\x01",
            "brought your SSS buddies, too.\x01",
            "I'm glad you could make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Behold, the Fisher Cup! A tournament where\x01",
            "you can show off your fishing skills to honor\x01",
            "the Fisherman's Guild president, Mr. Fisher!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I call it a tournament, but it's more akin to\x01",
            "a social gathering for all fishing enthusiasts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You sadly missed the full explanation, so\x01",
            "you'll have to settle for that quick rundown.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2726")

    label("loc_25FC")


    ChrTalk(
        0xFE,
        (
            "Behold, the Fisher Cup! A tournament where\x01",
            "you can show off your fishing skills to honor\x01",
            "the Fisherman's Guild president, Mr. Fisher!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I call it a tournament, but it's more akin to\x01",
            "a social gathering for all fishing enthusiasts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, but don't get me wrong.\x01",
            "I'll tackle any challenge!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2726")

    TalkEnd(0xFE)
    Return()

    # Function_15_1F42 end

    def Function_16_272A(): pass

    label("Function_16_272A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2926")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_27CD")

    ChrTalk(
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'm still just your average\x01",
            "Hobbyist Fisherman after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't get a single bite...\x01",
            "Today's not my day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2921")

    label("loc_27CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2865")

    ChrTalk(
        0xFE,
        (
            "Don't think I'll be catching any\x01",
            "big ones here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems my fishing game isn't on the\x01",
            "level of Joachim's right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2921")

    label("loc_2865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2921")

    ChrTalk(
        0xFE,
        "You hear the big news?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Joachim managed to catch a real\x01",
            "monster of a fish near here yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Time to bait my hook and buckle up,\x01",
            "'cause you're going down, Doctor!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2921")

    Jump("loc_2B5C")

    label("loc_2926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2B5C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_29E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_294D")
    Call(0, 17)
    Jump("loc_29E1")

    label("loc_294D")


    ChrTalk(
        0xFE,
        (
            "Did you happen to see where\x01",
            "Joachim ran off to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Weird... He was going on about how this\x01",
            "was his much-needed vacation, so why'd\x01",
            "he vanish?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29E1")

    Jump("loc_2B5C")

    label("loc_29E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2AB6")

    ChrTalk(
        0xFE,
        (
            "Joachim has managed to gain quite the\x01",
            "reputation within the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite St. Ursula working him silly,\x01",
            "he always finds time to sharpen his\x01",
            "angling chops. What a guy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5C")

    label("loc_2AB6")


    ChrTalk(
        0xFE,
        (
            "It's been a while since I last fished\x01",
            "at this sandbar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we came out here all willy-nilly,\x01",
            "we'd get surrounded by monsters\x01",
            "before our hooks hit the water.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B5C")

    TalkEnd(0xFE)
    Return()

    # Function_16_272A end

    def Function_17_2B60(): pass

    label("Function_17_2B60")


    ChrTalk(
        0xFE,
        (
            "Joachim came up to me and insisted\x01",
            "I take this novel a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you ask me, he was being\x01",
            "a little too shady about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wouldn't you know it, he swiped some\x01",
            "of my bait while I was off guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(Does this guy just mess\x01",
            "around all day...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, I'm not a fan of books, so you\x01",
            "wanna take this off my hands?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x2CB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2CB, 1)
    SetScenarioFlags(0x9C, 5)
    Return()

    # Function_17_2B60 end

    def Function_18_2D09(): pass

    label("Function_18_2D09")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FI'm banking on some real\x01",
            "nice catches at this spot.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(54040, -5700, -57590, 1500)
    MoveCamera(45, 32, 0, 1500)
    OP_6E(430, 1500)
    SetCameraDistance(23500, 1500)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E26")
    OP_E0(0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E04")
    MiniGame(0x6, 0x10, 0xC526, 0xFFFFE764, 0xFFFF18A2, 0x59, 0xE1AA, 0xFFFFEB4C, 0xFFFF1924)
    Jump("loc_2E26")

    label("loc_2E04")

    MiniGame(0x6, 0xC, 0xC526, 0xFFFFE764, 0xFFFF18A2, 0x59, 0xE1AA, 0xFFFFEB4C, 0xFFFF1924)

    label("loc_2E26")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_18_2D09 end

    def Function_19_2E2B(): pass

    label("Function_19_2E2B")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FNothing wrong with starting\x01",
            "small before going big.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(13960, -5700, -56570, 1500)
    MoveCamera(45, 30, 0, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(19950, 1500)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F0C")
    OP_E0(0x2)
    MiniGame(0x6, 0xF, 0x4696, 0xFFFFE764, 0xFFFF2392, 0x10E, 0x37D2, 0xFFFFE764, 0xFFFF2392)

    label("loc_2F0C")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_19_2E2B end

    def Function_20_2F11(): pass

    label("Function_20_2F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2F5F")
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
            "The bus already left.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_2FB0")

    label("loc_2F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2F70")
    Call(0, 10)
    Jump("loc_2FB0")

    label("loc_2F70")

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
            "The bus already left.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_2FB0")

    Return()

    # Function_20_2F11 end

    def Function_21_2FB1(): pass

    label("Function_21_2FB1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(4900, 900, 29270, 0)
    MoveCamera(24, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(17800, 0)
    SetChrPos(0x101, 4050, 0, 29300, 180)
    SetChrPos(0x102, 5250, 0, 29300, 180)
    SetChrPos(0x103, 4050, 0, 30800, 180)
    SetChrPos(0x104, 5250, 0, 30800, 180)
    OP_68(4610, 900, 27270, 2500)

    def lambda_3047():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3047)
    Sleep(50)

    def lambda_3064():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3064)
    Sleep(60)

    def lambda_3081():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3081)
    Sleep(70)

    def lambda_309E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_309E)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#1101012V#0006F#5P*sigh*\x02",
    )

    CloseMessageWindow()

    def lambda_30F5():
        TurnDirection(0xFE, 0x104, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30F5)

    def lambda_3102():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3102)

    def lambda_310F():
        TurnDirection(0xFE, 0x102, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_310F)

    def lambda_311C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_311C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1101013V#0001F#6PEstelle and Joshua. Two more aces\x01",
            "up the guild's sleeve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101014V#0106F#12PNothing seems to ever go our way,\x01",
            "does it?\x02\x03",
            "#1101015V#0101FThey're the same age as us, but I get the\x01",
            "impression they're reputable bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101016V#0306F#11PYeah, they definitely look like pros to me.\x02\x03",
            "#1101017V#0301FBetween their attitudes and their combat\x01",
            "skills, I can tell they've had their fair share\x01",
            "of fights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101018V#0203F#5PIndeed. Those monsters were disposed of\x01",
            "in record time. We had difficulty defeating\x01",
            "two of them.\x02\x03",
            "#1101019V#0200FI suppose we have found ourselves rivals...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101020V#0008F#6PGreat...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#1101021V#0004F#6PWell, moping's not going to get us anywhere,\x01",
            "so we'll just have to work with what we have.\x02\x03",
            "#1101022V#0000FBesides, 'rival' is a bit too...extreme. Let's\x01",
            "look at them as friendly competition, okay?\x02\x03",
            "#1101023VThat'll hopefully keep us motivated.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_352A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_352A)

    def lambda_3537():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3537)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1101024V#0211F#5PI fail to see how the 'competition' is fair,\x01",
            "given the gap in our skill levels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101025V#0304F#11PLet's just be happy they aren't\x01",
            "on Arios' level, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101026V#0100F#11P*sigh* That's true, I suppose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101027V#0004F#6PStill, that's only one way to look at it.\x02\x03",
            "#1101028V#0000FThey're doing us a huge favor. Without them,\x01",
            "we wouldn't be able to make it to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101029V#0206F#5PNow, if only the bus were operational...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101030V#0102F#11PLook at the bright side, Tio. At least we're\x01",
            "getting in shape while on the job!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18300, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 5000, 0, 29400, 180)
    SetScenarioFlags(0x61, 5)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_21_2FB1 end

    def Function_22_37BE(): pass

    label("Function_22_37BE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0xF)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xF, -28200, -4900, -102400, 0)
    OP_D3(0xF, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xF1, 0xC2, 0xB1, 0x0, 0x1AE, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    SetMapObjFrame(0xFF, "water00", 0x2, "red")
    SetMapObjFrame(0xFF, "water01", 0x2, "red")
    ClearChrFlags(0xF, 0x4)
    FadeToBright(1000, 0)
    OP_68(-39300, -8300, -105090, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(42630, 0)
    OP_68(-26300, -5300, -94050, 12000)
    BeginChrThread(0xF, 3, 0, 23)
    OP_0D()
    Sleep(6300)
    Fade(1000)
    EndChrThread(0xF, 0x3)
    EndChrThread(0xF, 0x2)
    EndChrThread(0xF, 0x1)
    OP_68(-13410, -4300, -29940, 0)
    MoveCamera(62, 14, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(44090, 0)
    OP_68(-13410, -1300, -29940, 6000)
    SetCameraDistance(34090, 6000)
    Sleep(1000)
    SetChrPos(0xF, -28420, -4200, -50490, 0)

    def lambda_3933():
        OP_95(0xFE, -28280, 0, -16570, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3933)
    Sound(465, 0, 100, 0)
    OP_0D()
    Sleep(5000)
    Fade(1000)
    EndChrThread(0xF, 0x1)
    OP_68(-11620, -4300, -8150, 0)
    MoveCamera(31, 23, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(57130, 0)
    OP_68(-11620, -1600, -8150, 5000)
    Sound(471, 0, 100, 0)
    SetChrPos(0xF, -23750, 0, -9730, 0)

    def lambda_39B6():
        OP_95(0xFE, 1980, 0, 15000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_39B6)
    OP_0D()
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xF, 0x1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("e0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_37BE end

    def Function_23_39F4(): pass

    label("Function_23_39F4")

    SetChrPos(0xFE, -65379, -4900, -109290, 0)

    def lambda_3A0A():
        OP_95(0xFE, -41340, -4900, -109460, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A0A)
    Sound(469, 0, 100, 0)
    Sleep(4000)
    EndChrThread(0xFE, 0x1)

    def lambda_3A31():
        OP_9E(0xFE, 0xFFFF5E84, 0xFFFE8734, 0xFFFEA070, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A31)
    Sound(458, 0, 100, 0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_23_39F4 end

    def Function_24_3A52(): pass

    label("Function_24_3A52")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-28200, 600, -14200, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(23500, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0xF)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xF, -28200, 0, -14200, 180)
    OP_D3(0xF, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0xF, 0x4)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B8A")
    Sound(471, 0, 100, 0)
    FadeToBright(1000, 0)
    SetChrPos(0xF, -890, 0, 10890, 225)

    def lambda_3B1F():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3B1F)
    OP_68(-5600, -350, 2290, 0)
    MoveCamera(33, 11, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(52930, 0)
    OP_68(-5600, -2850, 2290, 6000)
    OP_0D()
    Sleep(1000)
    Sound(465, 0, 100, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xF, 0x1)

    label("loc_3B8A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C20")
    Fade(1000)
    SetChrPos(0xF, -28500, -830, -21530, 0)
    OP_68(-6650, -950, -31510, 0)
    MoveCamera(54, 12, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(37610, 0)
    OP_68(-19030, -950, -31410, 10000)
    OP_0D()
    Sleep(2000)

    def lambda_3BF3():
        OP_95(0xFE, -27920, -4200, -50960, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3BF3)
    Sound(458, 0, 100, 0)
    Sleep(4500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xF, 0x1)

    label("loc_3C20")

    SetScenarioFlags(0x5C, 1)
    NewScene("e0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_3A52 end

    def Function_25_3C2D(): pass

    label("Function_25_3C2D")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(840)
    OP_68(-38620, -4300, -107290, 0)
    MoveCamera(31, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20160, 0)
    SetChrPos(0x101, -36290, -4900, -108440, 270)
    SetChrPos(0x102, -35800, -4900, -109620, 270)
    SetChrPos(0x103, -34460, -4900, -107100, 270)
    SetChrPos(0x104, -33640, -4900, -108220, 270)
    FadeToBright(1000, 0)
    SetCameraDistance(19160, 2000)

    def lambda_3D11():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D11)
    Sleep(50)

    def lambda_3D29():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D29)
    Sleep(50)

    def lambda_3D41():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3D41)
    Sleep(50)

    def lambda_3D59():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3D59)
    WaitChrThread(0x101, 1)
    OP_0D()
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
        "#5100319V#0007F#11P...!\x02",
    )

    CloseMessageWindow()
    OP_68(-57020, -4100, -107490, 3500)
    SetCameraDistance(19000, 3500)
    Sleep(3500)
    SetChrPos(0x101, -48030, -4900, -109440, 270)
    SetChrPos(0x102, -48470, -4900, -111260, 270)
    SetChrPos(0x103, -46230, -4900, -111130, 270)
    SetChrPos(0x104, -46260, -4900, -109630, 270)
    SetCameraDistance(20000, 2000)

    def lambda_3E66():
        OP_95(0xFE, -57800, -4900, -108900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E66)

    def lambda_3E80():
        OP_95(0xFE, -58240, -4900, -111000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E80)

    def lambda_3E9A():
        OP_95(0xFE, -56460, -4900, -111100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3E9A)

    def lambda_3EB4():
        OP_95(0xFE, -56720, -4900, -109480, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3EB4)
    WaitChrThread(0x101, 1)

    def lambda_3ED2():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3ED2)
    WaitChrThread(0x102, 1)

    def lambda_3EE3():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EE3)
    WaitChrThread(0x103, 1)

    def lambda_3EF4():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3EF4)
    WaitChrThread(0x104, 1)

    def lambda_3F05():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3F05)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        (
            "#5100320V#0105F#12PWhy has it stopped here...?\x02\x03",
            "#5100321V#0101FActually, doesn't the bus look\x01",
            "completely empty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100322V#0301F#12PYeah, sure looks that way to me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        (
            "#5100323V#0301F#5PYou mind checkin' if anyone's still\x01",
            "around, Tio Tot?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4023():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4023)
    Sleep(50)

    def lambda_4033():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4033)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x103,
        "#5100324V#0201F#12PJust a moment...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(300)
    Sound(1278, 255, 100, 0)
    Sleep(800)
    VolumeBGM(0x3C, 0x3E8)
    Fade(250)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    Sound(831, 0, 100, 0)
    Sound(840, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Fade(250)
    OP_24(0x348)
    Sound(820, 0, 100, 0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#5100325V#0206F#12PNo luck.\x02\x03",
            "#5100326V#0201FI failed to detect the presence of any\x01",
            "people within a ten selge radius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100327V#0303F#5PWell, crap. Was hopin' that wouldn't\x01",
            "be the case.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#5100328V#0301F#11PI think it's probably safe to write off monsters\x01",
            "as the source of the problem, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100329V#0003F#5PRight. The bus had too clean a stop\x01",
            "for it to have been monsters.\x02\x03",
            "#5100330V#0008FIf I were to guess, the driver pulled over\x01",
            "of his own volition.\x02\x03",
            "#5100331VOr, it's possible that he had no choice but to\x01",
            "stop because of an accident on board.\x02\x03",
            "#5100332V#0001FWe should investigate inside the bus.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#5100333V#0101F#6PRight.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x348)
    SetScenarioFlags(0x5C, 2)
    NewScene("e0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_3C2D end

    def Function_26_444E(): pass

    label("Function_26_444E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    OP_68(-56490, -3100, -107870, 0)
    MoveCamera(31, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19160, 0)
    SetChrPos(0x101, -56790, -4900, -110680, 180)
    SetChrPos(0x102, -58500, -4900, -109250, 180)
    SetChrPos(0x103, -56840, -4900, -108730, 180)
    SetChrPos(0x104, -55360, -4900, -108810, 180)
    TurnDirection(0x102, 0x101, 0)
    TurnDirection(0x103, 0x101, 0)
    TurnDirection(0x104, 0x101, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x7)
    FadeToBright(1000, 0)
    OP_68(-56490, -4100, -107870, 3000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5100339V#0003F#5PRight... Yes...\x02\x03",
            "#5100340V#0013FUnderstood. We'll leave communications\x01",
            "to you, then.\x02\x03",
            "#5100341VWe'll continue on our way to St. Ursula.\x02\x03",
            "#5100342V#0003FYes, sir. You be careful, too.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(807, 0, 100, 0)
    SetChrSubChip(0x101, 0x6)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#5100343V#0201F#5PWere you speaking to the chief?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#5100344V#0006F#12PYeah. He's already contacted\x01",
            "Tangram Gate about the situation.\x02\x03",
            "#5100345V#0000FIf all goes well, he'll get Deputy Commander\x01",
            "Baelz to provide us with support.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100346V#0100F#5POh, really? That would be a great help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100347V#0300F#11PNo kiddin'. Baelz is one of the most\x01",
            "reliable people in the whole state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100348V#0200F#5PShall we continue on to the hospital?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100349V#0003F#12PYeah. We're almost there.\x02\x03",
            "#5100350V#0001FAlso, it's possible that the passengers\x01",
            "left for the hospital on foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100351V#0306F#11PI dunno, man... Kinda strange for people\x01",
            "to leave behind their get-well gifts, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100352V#0101F#5PIndeed, but we should hurry up.\x01",
            "It's almost nighttime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100353V#0013F#12PRight. Let's move!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()
    OP_D5(0x1E)
    OP_37()
    OP_68(-58000, -4300, -108800, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x0, -58000, -4900, -108800, 270)
    SetChrPos(0x1, -58000, -4900, -108800, 270)
    SetChrPos(0x2, -58000, -4900, -108800, 270)
    SetChrPos(0x3, -58000, -4900, -108800, 270)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE0, 2)
    OP_29(0x4D, 0x1, 0x2)
    Sleep(500)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_26_444E end

    def Function_27_49F8(): pass

    label("Function_27_49F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AFA")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AAE")

    ChrTalk(
        0x101,
        (
            "#0000FOh, right.\x02\x03",
            "It's against the rules to leave the\x01",
            "sandbar to resupply.\x02\x03",
            "I wouldn't resort to cheating to bring\x01",
            "back Doctor Guenter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4AE3")

    label("loc_4AAE")


    ChrTalk(
        0x101,
        "#0000FWe're not leaving without Doctor Guenter.\x02",
    )

    CloseMessageWindow()

    label("loc_4AE3")

    Sleep(50)
    SetChrPos(0x0, -17740, -1390, -15870, 156)
    EventEnd(0x4)
    Return()

    label("loc_4AFA")

    Call(0, 28)
    Return()

    # Function_27_49F8 end

    def Function_28_4AFE(): pass

    label("Function_28_4AFE")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    OP_E0(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-18840, 600, -8900, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(21100, 0)
    SetChrPos(0x101, -18810, 0, -10540, 180)
    SetChrPos(0x102, -18810, 0, -9120, 180)
    SetChrPos(0x103, -20390, 0, -10540, 180)
    SetChrPos(0x104, -20390, 0, -9120, 180)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xE, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#0005FOh, would you look at this...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(800)
    OP_68(6610, -5700, -12400, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(21000, 0)
    OP_68(3620, -5700, -17770, 3000)
    MoveCamera(34, 21, 0, 3000)
    Sleep(4000)
    Fade(800)
    OP_68(3180, -5430, -35010, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(23500, 0)
    OP_68(3460, -5430, -41130, 2600)
    MoveCamera(21, 23, 0, 2600)
    Sleep(3600)
    Fade(800)
    OP_68(21620, -5700, -48780, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(24500, 0)
    SetCameraDistance(19500, 2600)
    Sleep(3600)
    Fade(800)
    OP_68(44800, -5000, -18700, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(27000, 0)
    SetCameraDistance(26000, 2800)
    OP_63(0xE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(3600)
    Fade(800)
    OP_68(-18200, 600, -10810, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(21100, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#5P#0300FHaha. They look like they're enjoyin' themselves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0106FI'm impressed they can be so carefree with\x01",
            "all of these monsters on the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FThere are far fewer monsters than\x01",
            "normal today.\x02\x03",
            "Were they scared away by the horde of\x01",
            "fishermen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FI kind of doubt that...\x02\x03",
            "#0003FBut, either way, we've found\x01",
            "our fishing tournament.\x02\x03",
            "#0000FAll that's left to do is find Doctor Guenter.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0xBD, 3)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_28_4AFE end

    def Function_29_4F6D(): pass

    label("Function_29_4F6D")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    OP_E0(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(45080, -5000, -18980, 0)
    MoveCamera(43, 16, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 44540, -5600, -20590, 0)
    SetChrPos(0x102, 43130, -5600, -20590, 0)
    SetChrPos(0x103, 43130, -5600, -22300, 0)
    SetChrPos(0x104, 44540, -5600, -22300, 0)
    LoadChrToIndex("chr/ch07100.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02400.itp")
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0xE,
        "Man in Labcoat",
        (
            "#5P#2400FDoo doo doo doo... ♪\x01",
            "Doo doo doo doo doo dooooooo... ♪\x02\x03",
            "Ahhh... Fishing is truly delightful. I guess\x01",
            "what they say is true: The heart really IS\x01",
            "soothed with the cast of your line...\x02\x03",
            "It always helps me feel refreshed after\x01",
            "a long day at the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003F(Blue hair, white labcoat...\x01",
            "I think we've got our man.)\x02\x03",
            "#0001FExcuse me... Are you Doctor Joachim Guenter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2400F#5PJoachim? Yes, that's me.\x02\x03",
            "#2403FI apologize, but I'm in the middle of\x01",
            "something important.\x02\x03",
            "#2401FDid you need some... A-ha!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xE, 1, 0, 31)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#2405F#5PFinally, a bite!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F#5PHe's not even listening...\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xE, 1, 0, 32)

    ChrTalk(
        0xE,
        (
            "#2401F#5PI am, I am. I'm hooked\x01",
            "on your every word!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0206F(Lame pun...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FExcuse me, sir!\x02\x03",
            "#0001FSera, one of the hospital receptionists,\x01",
            "sent us a request to track you down,\x01",
            "Doctor!\x02\x03",
            "Your repeat absences are causing problems\x01",
            "for Lytton and the rest of the staff!\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0xE, 0x1)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xE,
        "#2400FI've got you now!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x2)
    Sleep(200)
    SetChrSubChip(0xE, 0x3)
    Sleep(200)
    Sound(11, 0, 100, 0)
    SetChrSubChip(0xE, 0x4)
    Sleep(200)
    SetChrSubChip(0xE, 0x5)
    Sleep(150)
    SetChrSubChip(0xE, 0x6)
    Sleep(150)
    SetChrSubChip(0xE, 0x7)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#2405F#5POh, wow! A viperhead! And a\x01",
            "pretty big one, at that.\x02\x03",
            "#2400FI can tell my daily trips from the hospital\x01",
            "are finally starting to pay off.\x02",
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
    Sleep(1200)

    ChrTalk(
        0x104,
        (
            "#12P#0306FThe dude's in his own little world...\x02\x03",
            "#0301FSorry, bud, but I don't think he\x01",
            "heard a single thing you said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0106F*sigh* I think you'll have to explain\x01",
            "yourself again, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(B-But, I was already yelling...)\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#2403F#5PNo, there's no need to raise your voice\x01",
            "any further.\x02\x03",
            "#2400FThe hospital staff is awaiting my return,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0xE, 0x2)
    ClearChrFlags(0xE, 0x20)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    OP_64(0xE)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_93(0xE, 0xB4, 0x190)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0xE,
        (
            "It's nice to meet you all.\x01",
            "I'm Doctor Joachim Guenter.\x02\x03",
            "I'm just a simple associate\x01",
            "professor over at St. Ursula\x01",
            "Hospital.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xE,
        (
            "#2405F#5PHmm? I can't help but feel that we've met\x01",
            "before...\x02\x03",
            "#2403FDeja vu perhaps? I suppose there's really\x01",
            "no point in trying to remember, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FNo... I wouldn't call this deja vu.\x01",
            "(We should have started with an introduction...\x01",
            "Oh, well. Better late than never, right?)\x02\x03",
            "#0001FUm... I'm Lloyd Bannings, member of the Crossbell\x01",
            "Police Department's Special Support Section.\x02\x03",
            "#0003FNow, Doctor Guenter, would you--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2409F#5PIt's fine, Lloyd. I understand the dilemma.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FSo, does that mean you'll return\x01",
            "to the hospital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2403F#5PThat's a good question...\x02\x03",
            "#2400F...however, I've been looking forward to\x01",
            "the Fisher Cup for the last two months.\x01",
            "It's kind of a big deal for us anglers.\x02\x03",
            "#2406FAnd since I won't have any free time\x01",
            "during the festival, I figured I'd treat\x01",
            "myself with this little fishing trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0211FDo you have no sense of responsibility\x01",
            "as a physician?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2400F#5PWell, of course I do.\x02\x03",
            "#2406FMy wrist is awfully sore from all of the\x01",
            "apology letters I had to write every time\x01",
            "I snuck out of the hospital last month.\x02\x03",
            "It's a good thing my old chum Lytton\x01",
            "was there to help me write half of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FWe're getting a little off topic now...\x02\x03",
            "#0001FWhat do we have to do to convince\x01",
            "you to return to the hospital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2403F#5PHmm. Let me think about that...\x02\x03",
            "#2400FWell, since we're already at the Fisher Cup,\x01",
            "why don't we settle this over a battle of\x01",
            "the baits?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FYou mean fishing...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2409F#5PExactly.\x02\x03",
            "#2400FIf you manage to reel in something larger\x01",
            "than the viperhead I just caught, I'll\x01",
            "gracefully accept defeat and return.\x02\x03",
            "#2409FSimple, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FSo it all comes down to a fishin' match, eh?\x01",
            "You think you're up for it, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FFine. I accept your challenge.\x01",
            "Any rules I should know of?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2409F#5PSpoken like a true angler.\x02\x03",
            "#2400FI'll show my viperhead to Cerdan in a little bit.\x02\x03",
            "Once you've caught a fish of your own, have\x01",
            "him inspect that one, as well.\x02\x03",
            "As long as you catch a larger fish than my\x01",
            "viperhead, you will be declared the winner.\x02\x03",
            "Keep in mind that there are no do-overs.\x01",
            "Once you've shown your fish to Cerdan,\x01",
            "that's it. Oh, and no leaving the sandbar.\x02\x03",
            "Come with all your gear in hand, because\x01",
            "leaving the sandbar to resupply is forbidden.\x02\x03",
            "#2409FSo? How do the rules sound?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FNo complaints from me.\x02\x03",
            "#0003F(I hope I have enough bait on me.\x01",
            "Maybe I should ask the other\x01",
            "fisherman if I don't, though.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2400F#5PI think it's time we start our bait-off!\x02\x03",
            "#2409FGood luck, Lloyd. Let's have some fun.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(43950, -5000, -20620, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x0, 43950, -5600, -20620, 0)
    SetChrPos(0x1, 43950, -5600, -20620, 0)
    SetChrPos(0x2, 43950, -5600, -20620, 0)
    SetChrPos(0x3, 43950, -5600, -20620, 0)
    SetChrFlags(0xE, 0x2)
    SetChrFlags(0xE, 0x20)
    OP_93(0xE, 0x0, 0x0)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    ClearScenarioFlags(0x0, 1)
    ModifyEventFlags(1, 1, 0x80)
    OP_29(0x16, 0x1, 0x2)
    Sleep(500)
    OP_37()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_29_4F6D end

    def Function_30_62B0(): pass

    label("Function_30_62B0")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    OP_E0(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_68(30260, -4900, -35640, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(710, 0)
    SetCameraDistance(14090, 0)
    SetChrPos(0x101, 30680, -5600, -37020, 315)
    SetChrPos(0xE, 28940, -5600, -35260, 135)
    SetChrPos(0xD, 31010, -5600, -34670, 225)
    SetChrPos(0x102, 32000, -5600, -39360, 0)
    SetChrPos(0x103, 30860, -5600, -39370, 0)
    SetChrPos(0x104, 29730, -5600, -39380, 0)
    LoadChrToIndex("chr/ch07100.itc", 0x1E)
    LoadChrToIndex("chr/ch32200.itc", 0x1F)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x2)
    ClearChrFlags(0xE, 0x20)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72F1")

    ChrTalk(
        0xE,
        (
            "#2400F#5PHahaha. Are you sure your fish\x01",
            "measures up to mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FI'm not sure, but I don't plan on\x01",
            "losing to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2409F#5PYeah? I'm excited to see the results!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 300)
    TurnDirection(0x101, 0xD, 300)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#2400F#5PIf you'll do the honors, Cerdan.\x01",
            "Judge away, my friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PHmm, let's see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PIn Doctor Guenter's corner, we've got\x01",
            "an impressive viperhead.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)

    ChrTalk(
        0xD,
        "#11PAfter judging, the winner is...\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)
    Sleep(300)

    ChrTalk(
        0x101,
        "#12P#0001F(*gulp*)\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AB0")
    OP_2C(0x16, 0x3)
    OP_29(0x16, 0x1, 0x5)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0xD,
        "#5S#11P...Lloyd Bannings!\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#2405F#5PC-Come again? Are you sure there\x01",
            "wasn't an error in your judgment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThem's the breaks, bud. Lloyd's\x01",
            "fish is absolutely massive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PTrust me. My eyes never lie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2406F#5PY-You're kidding...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0109FYou did it, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0309FHell yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0202FYou never fail to deliver.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FI-I won...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 300)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#2406F#5P*sigh* Fate is cruel.\x02\x03",
            "#2400FWell, a win's a win. Here's a\x01",
            "little present to celebrate your\x01",
            "victory.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 300)
    OP_95(0xE, 29970, -5600, -36340, 1000, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1FC, 1)
    OP_96(0xE, 0x710C, 0xFFFFEA20, 0xFFFF7644, 0x3E8, 0x0)
    Sleep(200)

    ChrTalk(
        0x101,
        "#12P#0005FThank you, Doctor Guenter. I appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2400F#5PNow it's time for me to hold up my end\x01",
            "of the bargain. Off to the hospital I go.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#12P#0105FReally? I was expecting you to throw\x01",
            "more of a fuss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2406F#5PExcuse me, miss? I'm not some rowdy child.\x02\x03",
            "#2400FAnyway, our little match was a great opportunity\x01",
            "to get some quality fishing in.\x02\x03",
            "#2409FI'm more than satisfied for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FHuh...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_72EC")

    label("loc_6AB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F1B")
    OP_29(0x16, 0x1, 0x4)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0xD,
        "#5S#11P...no one! It's a draw!\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#2405F#5PC-Come again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FA draw...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PIndeed. I carefully took their measurements,\x01",
            "and by some miracle, they're the exact\x01",
            "same size!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PI have no choice but to call this a draw.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006FHow does that even happen...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2406F#5POh, wow... I can't say I saw that one coming.\x02\x03",
            "If only I had made a rule to determine the\x01",
            "victor in the event of a draw...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 300)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#0011FS-So, about our deal...\x02\x03",
            "How should we proceed?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 300)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#2406F#5P*sigh* I think it's about time I returned\x01",
            "to the hospital, anyway.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#12P#0005FYou're going? Just like that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0105FReally? I was expecting you to throw\x01",
            "more of a fuss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2406F#5PExcuse me, miss? I'm not some rowdy child.\x02\x03",
            "#2400FWell, despite the draw, I had a great time\x01",
            "fishing with you. Still, I have a job that\x01",
            "awaits me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FHuh...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_72EC")

    label("loc_6F1B")

    OP_29(0x16, 0x1, 0x3)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0xD,
        "#5S#11P...Joachim Guenter!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#0006FYou're kidding me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PUnfortunately not. Joachim had\x01",
            "the larger catch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PTrust me. My eyes don't lie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FGuess I wasn't the ace angler\x01",
            "I was cracked up to be.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 300)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#2409F#5PHahaha. Don't feel too bad, Lloyd.\x01",
            "You were only a little bit off the mark.\x02\x03",
            "#2403FDon't beat yourself up over it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 300)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#0005FY-Yeah, okay...\x02\x03",
            "#0006F(I can't imagine how Sera's\x01",
            "going to respond to this...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2400F#5PI had a fun time, but still, I think it's\x01",
            "about time I return to the hospital.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#12P#0005FWait, what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0105FI thought the rules stated that Lloyd\x01",
            "had to win for you to return...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2403F#5PDid they, though?\x02\x03",
            "#2409FI never explicitly stated that I\x01",
            "WOULDN'T return, now did I?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72EC")

    Jump("loc_7677")

    label("loc_72F1")


    ChrTalk(
        0xE,
        (
            "#2400F#5PHahaha. Are you sure your fish\x01",
            "measures up to mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006FFunny story...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PHere's the thing, Joachim...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PHe didn't catch a single fish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PIt's a shame, but the match is forfeit.\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#2405F#5PWait, seriously?\x02\x03",
            "#2403FWell, okay, then. Talk about a letdown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FS-Sorry, Doctor. I didn't think my skills were\x01",
            "this dull.\x02\x03",
            "(I can't imagine how Sera's going to respond\x01",
            "to this...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2403F#5PIt's fine. We all have our off days, I suppose.\x02\x03",
            "#2400FWell, no matter. I've had enough fun for the day,\x01",
            "so I'm going to head back to the hospital.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#12P#0005FWait, what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0105FI thought the rules stated that Lloyd\x01",
            "had to win for you to return...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2400F#5PDid they, though?\x02\x03",
            "#2409FI never explicitly stated that I\x01",
            "WOULDN'T return, now did I?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7677")


    ChrTalk(
        0x104,
        (
            "#12P#0306FHe's a crafty one, ain't he? He was totally\x01",
            "usin' us to buy more fishin' time, I bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0211FUtterly despicable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2400F#5PI haven't the faintest idea what you mean.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 300)
    Sleep(300)

    ChrTalk(
        0xE,
        "#2403F#5PIt was a pleasure, Cerdan. I'll see you around.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PSure, pal. Look forward to seein' you at\x01",
            "the next competition!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2409F#5PLikewise, friend.\x02",
    )

    CloseMessageWindow()
    OP_95(0xD, 34960, -5600, -41280, 2000, 0x0)
    TurnDirection(0xE, 0x101, 300)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#2400F#5PNow if you'll excuse me, Special Support Section,\x01",
            "I have a hospital to tend to.\x02\x03",
            "I'll be waiting at the bus stop if there's\x01",
            "anything else you need from me.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_78B5():

        label("loc_78B5")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_78B5")

    QueueWorkItem2(0x0, 1, lambda_78B5)

    def lambda_78C7():

        label("loc_78C7")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_78C7")

    QueueWorkItem2(0x0, 1, lambda_78C7)

    def lambda_78D9():

        label("loc_78D9")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_78D9")

    QueueWorkItem2(0x0, 1, lambda_78D9)

    def lambda_78EB():

        label("loc_78EB")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_78EB")

    QueueWorkItem2(0x0, 1, lambda_78EB)
    OP_95(0xE, 25590, -5600, -32140, 2000, 0x0)
    OP_95(0xE, 19610, -5600, -32180, 2000, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    ChrTalk(
        0x104,
        (
            "#12P#0306FThat dude had us completely wrapped\x01",
            "around his finger...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0106FHe's cunning, all right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI do not trust him in the slightest...\x02\x03",
            "#0206FHe might swim away the moment\x01",
            "we take our eyes off of him.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#0000FYeah... We should take the same bus\x01",
            "to make sure he actually goes back\x01",
            "to the hospital.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    ClearMapFlags(0x8000000)
    SetScenarioFlags(0x5C, 1)
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_62B0 end

    def Function_31_7AAC(): pass

    label("Function_31_7AAC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AD8")
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(800)
    Jump("Function_31_7AAC")

    label("loc_7AD8")

    Return()

    # Function_31_7AAC end

    def Function_32_7AD9(): pass

    label("Function_32_7AD9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B05")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(800)
    Jump("Function_32_7AD9")

    label("loc_7B05")

    Return()

    # Function_32_7AD9 end

    def Function_33_7B06(): pass

    label("Function_33_7B06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B18")
    Call(0, 29)
    Return()

    label("loc_7B18")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Talk]\x01",               # 0
            "[Confirm rules]\x01",      # 1
            "[Cancel]\x01",             # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7B67"),
        (1, "loc_7D98"),
        (SWITCH_DEFAULT, "loc_7F4D"),
    )


    label("loc_7B67")

    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CA6")

    ChrTalk(
        0xE,
        (
            "#2400FHow's everything going on your end?\x02\x03",
            "I wouldn't worry too much about our\x01",
            "match, by the way. I'd rather you have\x01",
            "a good time fishing on this fine day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FSorry, but no can do.\x02\x03",
            "I'm going to win and drag you back to\x01",
            "the hospital, Doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#2406FYou need to relax a bit, Lloyd.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7D93")

    label("loc_7CA6")


    ChrTalk(
        0xE,
        (
            "#2400FYou know, it's actually a little funny that\x01",
            "your name is Lloyd.\x02\x03",
            "#2403FYou have the same name as a Master\x01",
            "Fisherman whom I greatly admire.\x02\x03",
            "#2409FYou're obviously not the same person, but\x01",
            "the name still makes me feel nervous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D93")

    Jump("loc_7F4D")

    label("loc_7D98")

    OP_60(0x0)

    ChrTalk(
        0xE,
        (
            "#2400FI'll show my viperhead to Cerdan in a\x01",
            "little bit, and you can show him your\x01",
            "catch when you're ready.\x02\x03",
            "#2400FAs long as you catch a larger fish than\x01",
            "my viperhead, you will be declared the\x01",
            "winner.\x02\x03",
            "Keep in mind that there are no do-overs.\x01",
            "Once you've shown your fish to Cerdan,\x01",
            "that's it. Oh, and no leaving the sandbar.\x02\x03",
            "And that should be everything. Let me\x01",
            "know if you need me to run through the\x01",
            "rules again for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F4D")

    label("loc_7F4D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_7B06 end

    def Function_34_7F5E(): pass

    label("Function_34_7F5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8348")
    EventBegin(0x0)
    SetMapFlags(0x8000000)
    OP_E0(0x2)
    Fade(500)
    OP_68(21800, -5700, -48170, 0)
    MoveCamera(51, 21, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x101, 19950, -6300, -47640, 180)
    SetChrPos(0x102, 21740, -6300, -46700, 180)
    SetChrPos(0x103, 22920, -6300, -47470, 225)
    SetChrPos(0x104, 23350, -6300, -48580, 225)
    OP_0D()

    NpcTalk(
        0xFE,
        "Man",
        (
            "#12PWow, that was a monster of a catch.\x01",
            "I think I've found the perfect fishing\x01",
            "spot.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Man",
        (
            "#12POh, are you guys members of the\x01",
            "Fisherman's Guild, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003F(I suppose I am...for the time being?)\x02\x03",
            "#0000FNice to meet you. My name is Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Man",
        (
            "#12PLloyd? That's a pretty funny\x01",
            "coincidence, if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#12PWe share the same name, my boy.\x01",
            "I'm Lloyd, a Master Fisher of the\x01",
            "Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#12PCerdan asked me to be a special guest\x01",
            "at the tournament, so I packed my things\x01",
            "and came all the way from Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#12PI'll be here for the duration of the Anniversary\x01",
            "Festival. Let's reel in some prize catches,\x01",
            "all right, other Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0005FY-Yeah, I'm looking forward to it.\x02\x03",
            "#0003F(Is this the 'Lloyd' that Estelle\x01",
            "was talking about earlier...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0xB7, 3)
    SetChrPos(0x0, 19950, -6300, -47640, 180)
    EventEnd(0x5)
    Jump("loc_8B35")

    label("loc_8348")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_843B")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, a good pal of mine\x01",
            "by the name of Estelle is in Crossbell\x01",
            "on Bracer Guild business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That gal knows her stuff, lemme tell you.\x01",
            "I challenged her to a match once, and I\x01",
            "was like a fish outta water.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B35")

    label("loc_843B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_8A45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8876")

    ChrTalk(
        0xFE,
        (
            "It looks like you're in the middle of a match\x01",
            "yourself, so have a great time out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I only saw it for a second, but boy,\x01",
            "was Joachim's catch enormous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're gonna have to pull out all the stops\x01",
            "to beat that monster. A catfish should\x01",
            "do the trick, 'cause it's king of this lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Well, that's reassuring...)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_886E")

    ChrTalk(
        0xFE,
        (
            "Haha. Come on, kid. Don't make that face.\x01",
            "Your first priority should be to have fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Know what? I'll give you a useful\x01",
            "piece of advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't go for the deadliest catch right off\x01",
            "the bat. The trick is to start off by stocking\x01",
            "up on small fry first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The real money catches won't be satisfied\x01",
            "with some dinky earthworm. You gotta bait\x01",
            "them with real food, like small fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This spot's good for catching small fry.\x01",
            "Here, try fishing with this bait.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x18B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x188),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x18B, 5)
    AddItemNumber(0x188, 5)

    ChrTalk(
        0x101,
        (
            "#0005FTh-Thanks, I appreciate it.\x02\x03",
            "#0003F(So I have to start small, huh?\x01",
            "All right, let's give this a shot.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB7, 7)

    label("loc_886E")

    SetScenarioFlags(0x0, 3)
    Jump("loc_8A40")

    label("loc_8876")


    ChrTalk(
        0xFE,
        (
            "You'll find more impressive fish, like the\x01",
            "catfish, in deeper waters. Don't even\x01",
            "bother if you don't have live bait, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't go for the deadliest catch right off\x01",
            "the bat. The trick is to start off by stocking\x01",
            "up on small fry first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This spot's good for catching small fry.\x01",
            "You'll want to start by catching yourself\x01",
            "some live bait for the big boys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, good luck out there. And remember,\x01",
            "your first priority should be to have fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A40")

    Jump("loc_8B35")

    label("loc_8A45")


    ChrTalk(
        0xFE,
        (
            "Cerdan asked me to be a special guest\x01",
            "at the tournament, so I packed my things\x01",
            "and came all the way from Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be here for the duration of the Anniversary\x01",
            "Festival. Let's reel in some prize catches,\x01",
            "all right, other Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B35")

    TalkEnd(0xFE)
    Return()

    # Function_34_7F5E end

    def Function_35_8B39(): pass

    label("Function_35_8B39")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F47")

    ChrTalk(
        0xFE,
        (
            "Oh, aren't you our newest member, Lloyd?\x01",
            "I've heard the stories about you, kid!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kopan went and invited you to\x01",
            "our guild, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nice to meet you, Lloyd. The name's\x01",
            "Cerdan, and I'm the Fisherman's Guild\x01",
            "manager here in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FWhat are you talking about...?\x02\x03",
            "#0006FI don't recall ever joining the guild.\x02\x03",
            "#0000FI mean, sure, I DID accept that\x01",
            "fishing rod earlier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bwahahaha! Don't sweat the details, kid!\x01",
            "You're already our comrade in rods!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(I don't think I'm escaping this one...)\x02\x03",
            "(Eh, looks like they all share a love\x01",
            "for fishing. I'm willing to bet Cerdan\x01",
            "could talk about it for hours on end...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_8EC1")

    ChrTalk(
        0xFE,
        (
            "Oh, yeah. I heard you're having a\x01",
            "showdown against Joachim, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The format's a little different from an\x01",
            "official fishing match, but that's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just give me a shout when you're\x01",
            "ready to have me deliberate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F40")

    label("loc_8EC1")


    ChrTalk(
        0xFE,
        (
            "Good to see you here, kid! I'm glad\x01",
            "you could make it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to find yourself an open\x01",
            "spot and fish, fish, fish!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F40")

    SetScenarioFlags(0x71, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_8F47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9000")

    ChrTalk(
        0xFE,
        (
            "O-Oh, crap. I just remembered that we left\x01",
            "the guild unlocked and unattended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to have to sprint back to the city\x01",
            "as soon as this tournament's over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95F1")

    label("loc_9000")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_9580")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Talk]\x01",                                     # 0
            "[Challenge Joachim with current fish]\x01",      # 1
            "[Cancel]\x01",                                   # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_906F"),
        (1, "loc_91FE"),
        (SWITCH_DEFAULT, "loc_956E"),
    )


    label("loc_906F")

    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_916F")

    ChrTalk(
        0xFE,
        (
            "I heard the news from Joachim. You guys\x01",
            "are gonna have a fishing match, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The format's a little different from an\x01",
            "official fishing match, but that's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just give me a shout when you're\x01",
            "ready to have me deliberate.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_91F9")

    label("loc_916F")


    ChrTalk(
        0xFE,
        (
            "Oh, yeah. I heard you're having a\x01",
            "showdown against Joachim, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just give me a shout when you're\x01",
            "ready to have me deliberate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91F9")

    Jump("loc_956E")

    label("loc_91FE")

    OP_60(0x0)
    Call(0, 36)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9390")

    ChrTalk(
        0xFE,
        (
            "I've already checked out Joachim's\x01",
            "viperhead, so it's all up to you now.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 37)

    ChrTalk(
        0xFE,
        (
            "Is this the fish you wanna challenge\x01",
            "him with?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_92CF"),
        (1, "loc_9325"),
        (SWITCH_DEFAULT, "loc_938B"),
    )


    label("loc_92CF")

    OP_60(0x1)

    ChrTalk(
        0xFE,
        "Sounds good!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll go grab Joachim so I can announce\x01",
            "the results.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 30)
    Jump("loc_938B")

    label("loc_9325")

    OP_60(0x1)

    ChrTalk(
        0xFE,
        "Oh, you're not ready yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just gimme a shout when you're\x01",
            "satisfied with your catch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_938B")

    label("loc_938B")

    Jump("loc_9569")

    label("loc_9390")


    ChrTalk(
        0xFE,
        (
            "I've already checked out Joachim's\x01",
            "viperhead, so it's all up to you now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We ready to start the match?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hold on a second. You haven't\x01",
            "caught a fish native to these waters!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Y-You aren't giving up, are you?\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_94A6"),
        (1, "loc_9508"),
        (SWITCH_DEFAULT, "loc_9569"),
    )


    label("loc_94A6")

    OP_60(0x1)

    ChrTalk(
        0xFE,
        "Hmm, really? A shame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guess I'll grab Joachim and be\x01",
            "the bearer of bad news.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 30)
    Jump("loc_9569")

    label("loc_9508")

    OP_60(0x1)

    ChrTalk(
        0xFE,
        "That's the spirit, kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come find me when you've found\x01",
            "yourself a worthy fish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9569")

    label("loc_9569")

    Jump("loc_956E")

    label("loc_956E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x0)
    Jump("loc_95F1")

    label("loc_9580")


    ChrTalk(
        0xFE,
        "Oh! More competitors for the Fisher Cup!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to find yourself an open\x01",
            "spot and fish, fish, fish!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95F1")

    TalkEnd(0xFE)
    Return()

    # Function_35_8B39 end

    def Function_36_95F5(): pass

    label("Function_36_95F5")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_9615")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_9615")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_962B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_962B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_9641")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_9641")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_9657")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_9657")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_966D")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_966D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_9683")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_9683")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_9699")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_9699")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_96AF")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_96AF")

    Return()

    # Function_36_95F5 end

    def Function_37_96B0(): pass

    label("Function_37_96B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9711")

    ChrTalk(
        0xD,
        (
            "Out of all the fish you caught, the largest\x01",
            "among them was...a catfish!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99BE")

    label("loc_9711")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9774")

    ChrTalk(
        0xD,
        (
            "Out of all the fish you caught, the largest\x01",
            "among them was...a viperhead!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99BE")

    label("loc_9774")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97DD")

    ChrTalk(
        0xD,
        (
            "Out of all the fish you caught, the largest\x01",
            "among them was...a gluttonous bass!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99BE")

    label("loc_97DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_983D")

    ChrTalk(
        0xD,
        (
            "Out of all the fish you caught, the largest\x01",
            "among them was...a salmon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99BE")

    label("loc_983D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_989C")

    ChrTalk(
        0xD,
        (
            "Out of all the fish you caught, the largest\x01",
            "among them was...a trout!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99BE")

    label("loc_989C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98FD")

    ChrTalk(
        0xD,
        (
            "Out of all the fish you caught, the largest\x01",
            "among them was...a kasagin!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99BE")

    label("loc_98FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9960")

    ChrTalk(
        0xD,
        (
            "Out of all the fish you caught, the largest\x01",
            "among them was...an azelfish!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99BE")

    label("loc_9960")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99BE")

    ChrTalk(
        0xD,
        (
            "Out of all the fish you caught, the largest\x01",
            "among them was...a snow crab!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99BE")

    Return()

    # Function_37_96B0 end

    def Function_38_99BF(): pass

    label("Function_38_99BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A26")

    ChrTalk(
        0xD,
        (
            "#11POut of all the fish Lloyd caught, the largest\x01",
            "among them was...a catfish!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CFD")

    label("loc_9A26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A8F")

    ChrTalk(
        0xD,
        (
            "#11POut of all the fish Lloyd caught, the largest\x01",
            "among them was...a viperhead!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CFD")

    label("loc_9A8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AFE")

    ChrTalk(
        0xD,
        (
            "#11POut of all the fish Lloyd caught, the largest\x01",
            "among them was...a gluttonous bass!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CFD")

    label("loc_9AFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B64")

    ChrTalk(
        0xD,
        (
            "#11POut of all the fish Lloyd caught, the largest\x01",
            "among them was...a salmon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CFD")

    label("loc_9B64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BC9")

    ChrTalk(
        0xD,
        (
            "#11POut of all the fish Lloyd caught, the largest\x01",
            "among them was...a trout!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CFD")

    label("loc_9BC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C30")

    ChrTalk(
        0xD,
        (
            "#11POut of all the fish Lloyd caught, the largest\x01",
            "among them was...a kasagin!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CFD")

    label("loc_9C30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C99")

    ChrTalk(
        0xD,
        (
            "#11POut of all the fish Lloyd caught, the largest\x01",
            "among them was...an azelfish!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CFD")

    label("loc_9C99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CFD")

    ChrTalk(
        0xD,
        (
            "#11POut of all the fish Lloyd caught, the largest\x01",
            "among them was...a snow crab!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CFD")

    Return()

    # Function_38_99BF end

    SaveToFile()

Try(main)
