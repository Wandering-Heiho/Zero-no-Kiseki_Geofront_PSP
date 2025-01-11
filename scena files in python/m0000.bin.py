from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0000.bin",                # FileName
        "m0000",                    # MapName
        "m0000",                    # Location
        0x0067,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 103, 0, 5, 0, 6],
    )

    BuildStringList((
        "m0000",                  # 0
        "Monster",                # 1
        "Monster",                # 2
        "Monster",                # 3
        "Monster",                # 4
        "bm0001",                 # 5
        "bm0001",                 # 6
        "bm0001",                 # 7
        "bm0001",                 # 8
        "bm0001",                 # 9
        "bm0001",                 # 10
        "bm0000",                 # 11
        "bm0001",                 # 12
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 1, 0, 1, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0)

    Sepith("Sepith_B4", 2,   0,   3,   2,   1,   0,   2)
    Sepith("Sepith_C4", 3,   1,   2,   0,   1,   2,   1)
    Sepith("Sepith_D4", 1,   4,   0,   2,   0,   2,   1)
    Sepith("Sepith_E4", 1,   2,   0,   4,   1,   1,   0)

    MonsterBattlePostion("MonsterBattlePostion_F4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_118", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_120", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_124", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_128", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_12C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_144", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_148", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_14C", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_150", 9, 15, 180)

    # monster count: 10

    BattleInfo(
        "BattleInfo_154", 0x0000, 3, 6, 45, 10, 1, 40, 0, "bm0001", "Sepith_B4", 75, 25, 0, 0,
        (
            ("ms61700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61700.dat", "ms61700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1C4", 0x0000, 3, 6, 45, 6, 1, 40, 0, "bm0001", "Sepith_C4", 75, 25, 0, 0,
        (
            ("ms60100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60100.dat", "ms60100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_234", 0x0000, 1, 6, 0, 0, 0, 0, 2, "bm0001", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60100.dat", "ms60100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_278", 0x0000, 1, 6, 0, 0, 0, 0, 3, "bm0001", 0x00000000, 100, 0, 0, 0,
        (
            ("ms73100.dat", "ms73100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2BC", 0x0000, 1, 6, 0, 0, 0, 0, 4, "bm0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60300.dat", "ms60300.dat", "ms60300.dat", "ms60300.dat", 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_300", 0x0000, 1, 6, 0, 0, 0, 0, 5, "bm0001", 0x00000000, 100, 0, 0, 0,
        (
            ("ms61700.dat", "ms61700.dat", "ms61700.dat", "ms61700.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_344", 0x0000, 3, 6, 45, 6, 1, 25, 0, "bm0001", "Sepith_D4", 100, 0, 0, 0,
        (
            ("ms73100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_388", 0x0000, 3, 6, 45, 6, 1, 30, 0, "bm0001", "Sepith_E4", 75, 25, 0, 0,
        (
            ("ms60300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60300.dat", "ms60300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch60150.itc",               # 10
        "monster/ch60151.itc",               # 11
        "monster/ch60350.itc",               # 12
        "monster/ch60351.itc",               # 13
        "monster/ch73150.itc",               # 14
        "monster/ch73151.itc",               # 15
        "monster/ch61750.itc",               # 16
        "monster/ch61750.itc",               # 17
    ))

    DeclNpc(-209,    0,       97279,   0,    385,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-102120, 0,       199509,  90,   385,  0x0, 0,   20,  0,   0,   3,   255, 255, 255,  0)
    DeclNpc(-200190, 100,     199740,  90,   385,  0x0, 0,   18,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(-200100, 0,       294179,  180,  385,  0x0, 0,   22,  0,   0,   4,   255, 255, 255,  0)

    DeclMonster(-200100, 294180,  0,       0x1010000,    "BattleInfo_154", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-106700, 399680,  0,       0x1010000,    "BattleInfo_1C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-97580,  396200,  0,       0x1010000,    "BattleInfo_1C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-210,    97280,   0,       0x1810000,    "BattleInfo_234", 2,   16,  0xFFFF, 0,  1)
    DeclMonster(-102120, 199510,  0,       0x181005A,    "BattleInfo_278", 670, 20,  0xFFFF, 4,  5)
    DeclMonster(-200190, 199740,  100,     0x181005A,    "BattleInfo_2BC", 588, 18,  0xFFFF, 2,  3)
    DeclMonster(-200100, 294180,  0,       0x18100B4,    "BattleInfo_300", 669, 22,  0xFFFF, 6,  7)
    DeclMonster(-210,    97280,   0,       0x1010000,    "BattleInfo_1C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-102120, 199510,  0,       0x1010000,    "BattleInfo_344", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-200190, 199740,  100,     0x1010000,    "BattleInfo_388", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 21,  -100.0,                -5.0,                  -1.0,                  25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   19.999998092651367,    2.5,                   0.19999998807907104,   1.0])
    DeclEvent(0x0000, 0, 34,  -100.0,                -7.050000190734863,    -1.0,                  25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   19.999998092651367,    3.5250000953674316,    0.19999998807907104,   1.0])
    DeclEvent(0x0000, 0, 25,  -0.10999999940395355,  113.54000091552734,    0.15000000596046448,   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.02199999801814556,   -56.77000045776367,    -0.029999999329447746, 1.0])
    DeclEvent(0x0000, 0, 27,  -112.47000122070312,   199.7899932861328,     -0.0,                  156.25,                [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  1.0,                   0.0,                   22.493999481201172,    -39.9579963684082,     0.0,                   1.0])
    DeclEvent(0x0000, 0, 29,  -199.9600067138672,    207.3300018310547,     0.1599999964237213,    25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   39.992000579833984,    -103.66500091552734,   -0.03199999779462814,  1.0])
    DeclEvent(0x0000, 0, 30,  -200.0,                192.57000732421875,    0.0,                   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   39.999996185302734,    -96.28500366210938,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 32,  -200.0,                319.0,                 0.0,                   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   39.999996185302734,    -159.5,                -0.0,                  1.0])

    DeclActor(100000,  0,       2000,    1200,    100000,  1000,    2500,    0x007C, 0,  15, 0x0000)
    DeclActor(100000,  0,       102000,  1200,    100000,  1000,    102500,  0x007C, 0,  17, 0x0000)
    DeclActor(2000,    0,       400000,  1200,    2500,    1000,    400000,  0x007C, 0,  19, 0x0000)
    DeclActor(5000,    0,       200000,  1200,    5000,    1000,    200000,  0x007C, 0,  9,  0x0000)
    DeclActor(-200000, 0,       104000,  1200,    -200000, 1000,    104000,  0x007C, 0,  10, 0x0000)
    DeclActor(-100000, 0,       404500,  1200,    -100000, 1000,    404500,  0x007C, 0,  11, 0x0000)
    DeclActor(-194710, 4000,    405550,  1200,    -194710, 5500,    405550,  0x007C, 0,  14, 0x0000)
    DeclActor(-97500,  0,       5000,    1200,    -97500,  1500,    5000,    0x007C, 0,  13, 0x0000)
    DeclActor(-90570,  0,       0,       1200,    -90570,  1500,    0,       0x007C, 0,  35, 0x0000)
    DeclActor(100000,  0,       11820,   1200,    100000,  1500,    11820,   0x007C, 0,  36, 0x0000)
    DeclActor(-205000, 0,       200000,  1200,    -205000, 1000,    200000,  0x007C, 0,  12, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3])                         # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_B28",          # 00, 0
        "Function_1_BE0",          # 01, 1
        "Function_2_BFD",          # 02, 2
        "Function_3_C1C",          # 03, 3
        "Function_4_C3B",          # 04, 4
        "Function_5_C57",          # 05, 5
        "Function_6_D7A",          # 06, 6
        "Function_7_1292",         # 07, 7
        "Function_8_12ED",         # 08, 8
        "Function_9_139F",         # 09, 9
        "Function_10_1519",        # 0A, 10
        "Function_11_1661",        # 0B, 11
        "Function_12_17DC",        # 0C, 12
        "Function_13_18D2",        # 0D, 13
        "Function_14_19D2",        # 0E, 14
        "Function_15_1F9D",        # 0F, 15
        "Function_16_2126",        # 10, 16
        "Function_17_226D",        # 11, 17
        "Function_18_23F6",        # 12, 18
        "Function_19_2533",        # 13, 19
        "Function_20_26BC",        # 14, 20
        "Function_21_2803",        # 15, 21
        "Function_22_32C8",        # 16, 22
        "Function_23_3404",        # 17, 23
        "Function_24_3851",        # 18, 24
        "Function_25_4081",        # 19, 25
        "Function_26_4130",        # 1A, 26
        "Function_27_4356",        # 1B, 27
        "Function_28_4409",        # 1C, 28
        "Function_29_466D",        # 1D, 29
        "Function_30_470D",        # 1E, 30
        "Function_31_47AD",        # 1F, 31
        "Function_32_4ADA",        # 20, 32
        "Function_33_4B92",        # 21, 33
        "Function_34_529C",        # 22, 34
        "Function_35_564D",        # 23, 35
        "Function_36_5689",        # 24, 36
    ))


    def Function_0_B28(): pass

    label("Function_0_B28")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_B68"),
        (1, "loc_B74"),
        (2, "loc_B80"),
        (3, "loc_B8C"),
        (4, "loc_B98"),
        (5, "loc_BA4"),
        (6, "loc_BB0"),
        (SWITCH_DEFAULT, "loc_BBC"),
    )


    label("loc_B68")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_B74")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_B80")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_B8C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_B98")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_BA4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_BB0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_BBC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_BC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BDF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_BDF")

    Return()

    # Function_0_B28 end

    def Function_1_BE0(): pass

    label("Function_1_BE0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BFC")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_BE0")

    label("loc_BFC")

    Return()

    # Function_1_BE0 end

    def Function_2_BFD(): pass

    label("Function_2_BFD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C1B")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_BFD")

    label("loc_C1B")

    Return()

    # Function_2_BFD end

    def Function_3_C1C(): pass

    label("Function_3_C1C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C3A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_3_C1C")

    label("loc_C3A")

    Return()

    # Function_3_C1C end

    def Function_4_C3B(): pass

    label("Function_4_C3B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C56")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_4_C3B")

    label("loc_C56")

    Return()

    # Function_4_C3B end

    def Function_5_C57(): pass

    label("Function_5_C57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBD")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C84")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)
    Jump("loc_CBD")

    label("loc_C84")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA3")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 18)
    Jump("loc_CBD")

    label("loc_CA3")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBD")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 20)

    label("loc_CBD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD7")
    Event(0, 22)

    label("loc_CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_CE6")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 33)

    label("loc_CE6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF7")
    SetScenarioFlags(0x58, 0)

    label("loc_CF7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D08")
    SetScenarioFlags(0x58, 1)

    label("loc_D08")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D23")
    Event(0, 26)

    label("loc_D23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D3E")
    Event(0, 28)

    label("loc_D3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D59")
    Event(0, 31)

    label("loc_D59")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x81), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D76")
    OP_C7(0x0, 0x1000)

    label("loc_D76")

    Call(0, 7)
    Return()

    # Function_5_C57 end

    def Function_6_D7A(): pass

    label("Function_6_D7A")

    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0xD, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0xE, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    OP_65(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58, 0)), scpexpr(EXPR_END)), "loc_E41")
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign00", 0x1, 0x1)
    SetMapObjFrame(0x2, "light00", 0x1, 0x1)
    SetMapObjFlags(0x2, 0x10)
    Jump("loc_E85")

    label("loc_E41")

    SetMapObjFrame(0x2, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x2, "light00", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x1, 0x1)
    SetMapObjFrame(0x2, "light01", 0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)
    OP_66(0x8, 0x1)

    label("loc_E85")

    SetMapObjFrame(0x3, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x3, "light01", 0x0, 0x1)
    SetMapObjFrame(0x4, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x4, "light01", 0x0, 0x1)
    SetMapObjFrame(0x5, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x5, "light01", 0x0, 0x1)
    SetMapObjFrame(0x6, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x6, "light01", 0x0, 0x1)
    SetMapObjFrame(0x7, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x7, "light01", 0x0, 0x1)
    SetMapObjFrame(0x8, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x8, "light01", 0x0, 0x1)
    SetMapObjFrame(0x9, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x9, "light01", 0x0, 0x1)
    SetMapObjFrame(0xA, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xA, "light01", 0x0, 0x1)
    OP_65(0x9, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58, 1)), scpexpr(EXPR_END)), "loc_FBF")
    SetMapObjFrame(0xB, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xB, "light01", 0x0, 0x1)
    SetMapObjFrame(0xB, "sign00", 0x1, 0x1)
    SetMapObjFrame(0xB, "light00", 0x1, 0x1)
    SetMapObjFlags(0xB, 0x10)
    Jump("loc_1003")

    label("loc_FBF")

    SetMapObjFrame(0xB, "sign00", 0x0, 0x1)
    SetMapObjFrame(0xB, "light00", 0x0, 0x1)
    SetMapObjFrame(0xB, "sign01", 0x1, 0x1)
    SetMapObjFrame(0xB, "light01", 0x1, 0x1)
    ClearMapObjFlags(0xB, 0x10)
    OP_66(0x9, 0x1)

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1016")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1027")
    Event(0, 24)

    label("loc_1027")

    OP_10(0x19, 0x0)
    OP_10(0x1E, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1046")
    OP_10(0x10, 0x0)
    OP_10(0x1D, 0x1)
    Jump("loc_104C")

    label("loc_1046")

    OP_10(0x10, 0x1)
    OP_10(0x1D, 0x0)

    label("loc_104C")

    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BF")
    OP_70(0xF, 0x0)
    Jump("loc_11C3")

    label("loc_11BF")

    OP_70(0xF, 0x1E)

    label("loc_11C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D6")
    OP_70(0x10, 0x0)
    Jump("loc_11DA")

    label("loc_11D6")

    OP_70(0x10, 0x1E)

    label("loc_11DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11ED")
    OP_70(0x11, 0x0)
    Jump("loc_11F1")

    label("loc_11ED")

    OP_70(0x11, 0x1E)

    label("loc_11F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1204")
    OP_70(0x13, 0x0)
    Jump("loc_1208")

    label("loc_1204")

    OP_70(0x13, 0x1E)

    label("loc_1208")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1220")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1220")

    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    ModifyEventFlags(0, 6, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_124D")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_124D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1261")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_127A")
    ModifyEventFlags(1, 4, 0x80)
    ModifyEventFlags(1, 5, 0x80)

    label("loc_127A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_128E")
    ModifyEventFlags(1, 6, 0x80)

    label("loc_128E")

    Call(0, 8)
    Return()

    # Function_6_D7A end

    def Function_7_1292(): pass

    label("Function_7_1292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A1")
    ClearChrFlags(0xF, 0x80)

    label("loc_12A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B0")
    ClearChrFlags(0x10, 0x80)

    label("loc_12B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12BF")
    ClearChrFlags(0x11, 0x80)

    label("loc_12BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CE")
    ClearChrFlags(0x12, 0x80)

    label("loc_12CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12EC")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0xC, 0x80)

    label("loc_12EC")

    Return()

    # Function_7_1292 end

    def Function_8_12ED(): pass

    label("Function_8_12ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1313")
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x13, 0x8)
    Jump("loc_1330")

    label("loc_1313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1322")
    ClearChrFlags(0xF, 0x8)

    label("loc_1322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_END)), "loc_1330")
    ClearChrFlags(0x13, 0x8)

    label("loc_1330")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_135F")
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x15, 0x8)
    Jump("loc_1378")

    label("loc_135F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1373")
    ClearChrFlags(0x11, 0x8)
    Jump("loc_1378")

    label("loc_1373")

    ClearChrFlags(0x15, 0x8)

    label("loc_1378")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1399")
    SetChrFlags(0xD, 0x8)
    Jump("loc_139E")

    label("loc_1399")

    ClearChrFlags(0xD, 0x8)

    label("loc_139E")

    Return()

    # Function_8_12ED end

    def Function_9_139F(): pass

    label("Function_9_139F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1489")
    Sound(14, 0, 100, 0)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F4, 1)"), scpexpr(EXPR_END)), "loc_141F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10A, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1484")

    label("loc_141F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xF, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1484")

    Jump("loc_150D")

    label("loc_1489")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Welcome to the Geofront. I promise this dungeon\x01",
            "won't take as long as the other Geofront.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_150D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_139F end

    def Function_10_1519(): pass

    label("Function_10_1519")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F6")
    Sound(14, 0, 100, 0)
    OP_71(0x10, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x10, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 20)
    AddSepith(0x1, 20)
    AddSepith(0x2, 20)
    AddSepith(0x3, 20)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x20\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x20\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x20\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x20.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10A, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_164F")

    label("loc_15F6")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Geofront team developed PTSD arguing\x01",
            "whether to name it the CPD or CSPD.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_164F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1519 end

    def Function_11_1661(): pass

    label("Function_11_1661")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_174B")
    Sound(14, 0, 100, 0)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_16E1")
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
    SetScenarioFlags(0x10A, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_1746")

    label("loc_16E1")

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
    OP_71(0x11, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1746")

    Jump("loc_17D0")

    label("loc_174B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Signs and equipment were left down here so that\x01",
            "this place would be perfectly serviceable.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_17D0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1661 end

    def Function_12_17DC(): pass

    label("Function_12_17DC")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1851")
    Sound(14, 0, 100, 0)
    OP_71(0x13, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x13, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddItemNumber(0x20D, 5)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x20D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10A, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_18C0")

    label("loc_1851")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "What? You thought that because it's a fan translation,\x01",
            "all you would find is 'The chest is empty'?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_18C0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_17DC end

    def Function_13_18D2(): pass

    label("Function_13_18D2")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station here.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19B5")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x12, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x12, 0x0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x12)
    OP_71(0x12, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x12, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_19B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19D1")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_19D1")

    Return()

    # Function_13_18D2 end

    def Function_14_19D2(): pass

    label("Function_14_19D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F23")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B87")

    ChrTalk(
        0x101,
        "#0100506V#0005FThis ladder leads to Central Square, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100507V#0200FYes, apparently so. For some reason,\x01",
            "the database has no record of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100502V#0305FWhy'd they leave it open?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100503V#0103FWho knows? Perhaps one of the city's\x01",
            "maintenance workers forgot to close it.\x02\x03",
            "#0100504V#0100FWe should report this later after we're\x01",
            "done here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100505V#0003FDefinitely.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 3)
    Jump("loc_1F1B")

    label("loc_1B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D68")

    ChrTalk(
        0x101,
        (
            "#0100500V#0005FThis ladder leads up to Central\x01",
            "Square, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100501V#0200FYes, apparently so. For some reason,\x01",
            "the database has no mention of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100508V#0300FAha. So you snuck down\x01",
            "through there, did ya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        (
            "#0100509VY-Yes, sir... I'm sorry. We didn't have\x01",
            "permission, but we still did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100513V#0100FYou can take that up with your parents later.\x02\x03",
            "#0102002VLet's focus on finding your friend, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        "#0100514VO-Okay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EAC")

    label("loc_1D68")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a ladder that leads to the surface.\x02\x03",
            "It connects to the manhole in Central Square.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x197,
        (
            "#0100512VS-Sorry, everyone. This is all because\x01",
            "we came down here without permission...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100510V#0100FDon't fret about that now, Anri.\x02\x03",
            "#0102001VLet's focus on finding your friend, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        "#0100511VO-Okay!\x02",
    )

    CloseMessageWindow()

    label("loc_1EAC")

    SetScenarioFlags(0x4B, 1)
    Jump("loc_1F1B")

    label("loc_1EB4")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's a ladder that leads to the surface.\x02\x03",
            "It connects to the manhole in Central Square.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1F1B")

    TalkEnd(0xFF)
    Jump("loc_1F9C")

    label("loc_1F23")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a ladder.\x01",
            "Climb up?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F8A")
    EventEnd(0x5)
    NewScene("c010C", 111, 0, 0)
    IdleLoop()
    Jump("loc_1F95")

    label("loc_1F8A")

    EventEnd(0x5)
    NewScene("c0100", 111, 0, 0)
    IdleLoop()

    label("loc_1F95")

    Jump("loc_1F9C")

    label("loc_1F9A")

    EventEnd(0x5)

    label("loc_1F9C")

    Return()

    # Function_14_19D2 end

    def Function_15_1F9D(): pass

    label("Function_15_1F9D")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an elevator control panel.\x01",
            "Operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_211E")
    Fade(500)
    SetChrPos(0x0, 99400, 0, 600, 0)
    SetChrPos(0x1, 100600, 0, 600, 0)
    SetChrPos(0x2, 99400, 0, -600, 0)
    SetChrPos(0x3, 100600, 0, -600, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_207C")
    SetChrPos(0x4, 99400, 0, -1800, 0)
    SetChrPos(0x5, 100600, 0, -1800, 0)
    Jump("loc_209B")

    label("loc_207C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_209B")
    SetChrPos(0x4, 100000, 0, -1800, 0)

    label("loc_209B")

    OP_68(100000, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(100000, -4000, 0, 2000)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0001", 0, 0, 0)
    IdleLoop()

    label("loc_211E")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_1F9D end

    def Function_16_2126(): pass

    label("Function_16_2126")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(100000, -4000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 99400, -10000, 600, 0)
    OP_90(0x1, 100600, -10000, 600, 0)
    OP_90(0x2, 99400, -10000, -600, 0)
    OP_90(0x3, 100600, -10000, -600, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21FB")
    OP_90(0x4, 99400, 0, -1800, 0)
    OP_90(0x5, 100600, 0, -1800, 0)
    Jump("loc_221A")

    label("loc_21FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_221A")
    OP_90(0x4, 100000, 0, -1800, 0)

    label("loc_221A")

    Sound(145, 0, 100, 0)
    OP_68(100000, 1000, 0, 3000)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xC)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_16_2126 end

    def Function_17_226D(): pass

    label("Function_17_226D")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an elevator control panel.\x01",
            "Operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23EE")
    Fade(500)
    SetChrPos(0x0, 99400, 0, 100600, 0)
    SetChrPos(0x1, 100600, 0, 100600, 0)
    SetChrPos(0x2, 99400, 0, 99400, 0)
    SetChrPos(0x3, 100600, 0, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_234C")
    SetChrPos(0x4, 99400, 0, 98200, 0)
    SetChrPos(0x5, 100600, 0, 98200, 0)
    Jump("loc_236B")

    label("loc_234C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_236B")
    SetChrPos(0x4, 100000, 0, 98200, 0)

    label("loc_236B")

    OP_68(100000, 1000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(100000, -4000, 100000, 2000)
    SetMapObjFrame(0xD, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0011", 0, 0, 0)
    IdleLoop()

    label("loc_23EE")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_17_226D end

    def Function_18_23F6(): pass

    label("Function_18_23F6")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xD, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(100000, -4000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 99400, -10000, 100600, 0)
    OP_90(0x1, 100600, -10000, 100600, 0)
    OP_90(0x2, 99400, -10000, 99400, 0)
    OP_90(0x3, 100600, -10000, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C1")
    OP_90(0x4, 99400, 0, 98200, 0)
    OP_90(0x5, 100600, 0, 98200, 0)
    Jump("loc_24E0")

    label("loc_24C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24E0")
    OP_90(0x4, 100000, 0, 98200, 0)

    label("loc_24E0")

    Sound(145, 0, 100, 0)
    OP_68(100000, 1000, 100000, 3000)
    SetMapObjFrame(0xD, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xD)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_18_23F6 end

    def Function_19_2533(): pass

    label("Function_19_2533")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an elevator control panel.\x01",
            "Operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B4")
    Fade(500)
    SetChrPos(0x0, 600, 0, 399400, 90)
    SetChrPos(0x1, 600, 0, 400600, 90)
    SetChrPos(0x2, -600, 0, 399400, 90)
    SetChrPos(0x3, -600, 0, 400600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2612")
    SetChrPos(0x4, -1800, 0, 399400, 90)
    SetChrPos(0x5, -1800, 0, 400600, 90)
    Jump("loc_2631")

    label("loc_2612")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2631")
    SetChrPos(0x4, -1800, 0, 400000, 90)

    label("loc_2631")

    OP_68(0, 1000, 400000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(0, -4000, 400000, 2000)
    SetMapObjFrame(0xE, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0001", 0, 0, 0)
    IdleLoop()

    label("loc_26B4")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_19_2533 end

    def Function_20_26BC(): pass

    label("Function_20_26BC")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xE, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(0, -4000, 400000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, -10000, 399400, 90)
    OP_90(0x1, 600, -10000, 400600, 90)
    OP_90(0x2, -600, -10000, 399400, 90)
    OP_90(0x3, -600, -10000, 400600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2791")
    OP_90(0x4, -1800, 0, 399400, 90)
    OP_90(0x5, -1800, 0, 400600, 90)
    Jump("loc_27B0")

    label("loc_2791")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27B0")
    OP_90(0x4, -1800, 0, 400000, 90)

    label("loc_27B0")

    Sound(145, 0, 100, 0)
    OP_68(0, 1000, 400000, 3000)
    SetMapObjFrame(0xE, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xE)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_20_26BC end

    def Function_21_2803(): pass

    label("Function_21_2803")

    EventBegin(0x0)
    OP_E0(0x1)
    Fade(1000)
    OP_68(-100000, 3500, 0, 0)
    MoveCamera(55, 32, 0, 0)
    OP_6E(840, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -100000, 100, 1200, 0)
    SetChrPos(0x102, -98800, 100, 0, 90)
    SetChrPos(0x103, -101200, 100, 0, 270)
    SetChrPos(0x104, -100000, 100, -1200, 180)
    OP_68(-100000, 500, 0, 7000)
    MoveCamera(35, 24, 0, 7000)
    SetCameraDistance(22000, 7000)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)
    Sleep(500)
    Fade(500)
    OP_68(-100000, 1100, 0, 0)
    MoveCamera(65, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0100435V#5P#0001FSo, this is the Geofront.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100436V#11P#0101FI've heard rumors about it, but I wasn't\x01",
            "expecting something this massive to be\x01",
            "under the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100437V#7P#0305FPhew, now that's a relief.\x02\x03",
            "#0100438VI thought we were gonna be trudgin' through\x01",
            "some nasty-ass sewage, honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100439V#6P#0200FAccording to database records, the Geofront's construction\x01",
            "began at approximately the same time Crossbell ventured\x01",
            "into large-scale urban planning 20 years ago.\x02\x03",
            "#0100440VThe entire system includes waterworks, sewage systems,\x01",
            "and a waste disposal plant. It is also used to wire orbal\x01",
            "cables and other modern tech.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B6A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B6A)
    Sleep(150)

    def lambda_2B7A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2B7A)
    Sleep(50)

    def lambda_2B8A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2B8A)
    Sleep(50)

    def lambda_2B9A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2B9A)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x101,
        (
            "#0100441V#5P#0006FWell, it's safe to say that this place isn't\x01",
            "at all what I expected it to be.\x02\x03",
            "#0100442V#0001FCentral Square is directly above us, right?\x02\x03",
            "#0100443VIt's hard to believe that monsters are\x01",
            "roaming around just under your feet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100444V#6P#0203FThe area is usually sealed off, so monsters\x01",
            "cannot exactly wander onto the streets.\x02\x03",
            "#0100445VHowever, there have been reports of\x01",
            "maintenance workers being assaulted\x01",
            "while working down here.\x02\x03",
            "#0100446V#0200FUnfortunately, the police seem too busy\x01",
            "at the moment to provide the appropriate\x01",
            "countermeasures for these incidents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100447V#5P#0008FWow, I had no idea...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100448V#11P#0101FCould this be one of the reasons why\x01",
            "the Special Support Section was created?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100449V#7P#0304FI think I'm startin' to see the big picture here.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0100450V#5P#0003FOur mission is clear.\x02\x03",
            "#0100451V#0001FWhether this is a detective's job or not,\x01",
            "it's a job that needs to be done.\x02\x03",
            "#0100452VYou can treat this as a test if you want,\x01",
            "but let's get it done properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100453V#12P#0309FListen to Mr. Formality, here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100454V#11P#0104FStill, he's right.\x02\x03",
            "#0100455V#0100FWe should take advantage of this mission\x01",
            "to refresh ourselves with the basics, one\x01",
            "step at a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100456V#6P#0203FRoger.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-97900, 1100, 4730, 2000)
    MoveCamera(65, 20, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(20000, 2000)

    def lambda_3108():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3108)
    Sleep(150)

    def lambda_3118():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3118)
    Sleep(50)

    def lambda_3128():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3128)
    Sleep(50)

    def lambda_3138():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3138)
    WaitChrThread(0x103, 2)
    CloseMessageWindow()
    OP_6F(0x79)
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This machine, found in dangerous areas,\x01",
            "is an orbment charging station.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By inspecting it and selecting 'Rest,'\x01",
            "HP and EP is fully recovered.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When the party is in critical condition,\x01",
            "try using these to recover!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#11P#0000F(All right, if we ever find ourselves in a pinch,\x01",
            "let's come back here and heal up!)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -100000, 100, 0, 0)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0x40, 3)
    OP_29(0x3C, 0x1, 0x1)
    OP_E0(0x0)
    Call(0, 7)
    EventEnd(0x5)
    Return()

    # Function_21_2803 end

    def Function_22_32C8(): pass

    label("Function_22_32C8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_32F3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3367")

    label("loc_32F3")

    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Would you like to go through the battle tutorial?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_3367")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_337D"),
        (1, "loc_3388"),
        (SWITCH_DEFAULT, "loc_33EA"),
    )


    label("loc_337D")

    SetScenarioFlags(0x49, 5)
    Call(0, 23)
    Jump("loc_33F9")

    label("loc_3388")

    SetScenarioFlags(0x40, 4)
    SetScenarioFlags(0x40, 5)
    SetScenarioFlags(0x44, 1)
    SetScenarioFlags(0x44, 2)
    SetScenarioFlags(0x53, 6)
    SetScenarioFlags(0x49, 4)
    SetScenarioFlags(0x53, 5)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    ModifyEventFlags(0, 6, 0x80)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_33F9")

    label("loc_33EA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33F9")

    label("loc_33F9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_22_32C8 end

    def Function_23_3404(): pass

    label("Function_23_3404")

    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, -900, 0, 88300, 0)
    SetChrPos(0x102, 400, 0, 88300, 0)
    SetChrPos(0x103, -900, 0, 87300, 0)
    SetChrPos(0x104, 400, 0, 87300, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis201.itp")
    OP_68(-2370, 2000, 94890, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(17390, 0)
    SetCameraDistance(16970, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#0100457V#0101F#5P(There...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100458V#0301F#5P(That didn't take long.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100459V#0201F#5P(Monster targeted.)\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-2330, 2000, 89270, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18390, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0100460V#0003F#5P(This will be our first combat\x01",
            "operation as a team.)\x02\x03",
            "#0100461V#0001F(Let's proceed carefully and strike.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3827")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters cannot be seen from far away.\x01",
            "When close enough, they'll become visible.\x02\x03",
            "Initial battle advantage changes depending on how\x01",
            "you encounter them. Gain it by encountering them\x01",
            "from behind, and lose it by being encountered.\x02\x03",
            "When #163I is pressed on the field, the lead\x01",
            "party member will perform a field attack.\x02\x03",
            "It is possible to stun a monster by striking them\x01",
            "when they don't see you.\x02\x03",
            "If you successfully do this then encounter them,\x01",
            "the party will gain an even greater advantage.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    label("loc_3827")

    OP_CA(0x1, 0xFF, 0x0)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x0, 0, 0, 87500, 0)
    SetScenarioFlags(0x40, 4)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_23_3404 end

    def Function_24_3851(): pass

    label("Function_24_3851")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    OP_68(-2120, 2000, 94220, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, -900, 0, 94300, 0)
    SetChrPos(0x102, 400, 0, 94300, 0)
    SetChrPos(0x103, -1600, 0, 92800, 0)
    SetChrPos(0x104, 1100, 0, 92800, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis006.itp")
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetCameraDistance(19000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#0100462V#0000F#11PAll right, we did it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100463V#0304F#11PBetter perk up, 'cause those guys are\x01",
            "probably at the bottom of the food chain.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#0100464V#0104F#11PThat may be, but at least we learned a\x01",
            "little about each of our fighting styles.\x02\x03",
            "#0100465V#0100FTio's orbal staff gave quite the surprise\x01",
            "at first...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-2160, 2000, 92630, 1500)

    def lambda_3ADC():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3ADC)
    Sleep(50)

    def lambda_3AEC():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3AEC)
    Sleep(50)

    def lambda_3AFC():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3AFC)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#0100466V#0000F#5PI was thinking the same.\x02\x03",
            "#0100467VDoes the staff fire off some\x01",
            "sort of miniaturized arts?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#0100468V#0203F#6PYes, basically.\x02\x03",
            "#0100469V#0200FUnlike normal arts, it is possible for the\x01",
            "enemy to dodge my attacks.\x02\x03",
            "#0100470VIt essentially functions as a short-range\x01",
            "burst of arts, without the casting time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100471V#0300F#11PWe could come up with a bunch of different\x01",
            "tactics with somethin' like that on our side.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)

    ChrTalk(
        0x103,
        (
            "#0100472V#0204F#6P#NThat was the goal for this technology.\x02\x03",
            "#0100473V#0200FAlso, take a look at this breastplate\x01",
            "that I am wearing.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x103,
        (
            "#0100474V#0200F#6PThis links with the orbal staff's systems and\x01",
            "provides me with a protective field, increasing\x01",
            "my defense.\x02\x03",
            "#0100475V#0204FThanks to that, I am able to withstand much more\x01",
            "than my physique suggests. If you ever need me\x01",
            "on the front line, there should be no problems.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0x102,
        (
            "#0100476V#0102F#5PIncredible... I had no idea that orbal technology\x01",
            "had advanced that much already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100477V#0309FMight as well take advantage of it, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100478V#0008F#5PI suppose, but...\x02\x03",
            "#0100479V...having a girl her age on the\x01",
            "frontlines stills feels kind of...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        "#0100480V#0211F#12P(*glare*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100481V#0012F#5PS-Sorry. Forget I said anything.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -900, 0, 94300, 0)
    ClearScenarioFlags(0x0, 2)
    SetScenarioFlags(0x40, 5)
    ModifyEventFlags(0, 2, 0x80)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_37()
    ClearMapFlags(0x8000000)
    Call(0, 7)
    EventEnd(0x5)
    Return()

    # Function_24_3851 end

    def Function_25_4081(): pass

    label("Function_25_4081")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    ChrTalk(
        0x101,
        (
            "#0001FThis will be our first battle as a team.\x02\x03",
            "We should engage that monster out so we\x01",
            "can understand each other's fighting styles.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -150, 0, 111280, 180)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_25_4081 end

    def Function_26_4130(): pass

    label("Function_26_4130")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_68(-100220, 2000, 197860, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(17850, 0)
    SetCameraDistance(16850, 2000)
    SetChrPos(0x101, -95300, 0, 199300, 270)
    SetChrPos(0x102, -95300, 0, 200500, 270)
    SetChrPos(0x103, -94100, 0, 199300, 270)
    SetChrPos(0x104, -94100, 0, 200500, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x104,
        (
            "#0100482V#0305F#12PHuh... Looks like we got a couple\x01",
            "of jellybeans in our path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100483V#0001F#12PI think arts will be more effective than our\x01",
            "weapons against these types of monsters.\x02\x03",
            "#0100484V#0000FWe should try fighting this one with our\x01",
            "arts, as well, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100485V#0100F#12PYes, good idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100486V#0204F#12PRoger.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x0, -95300, 0, 199300, 270)
    SetScenarioFlags(0x44, 1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_26_4130 end

    def Function_27_4356(): pass

    label("Function_27_4356")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    ChrTalk(
        0x101,
        (
            "#0001FWe should defeat that monster before\x01",
            "proceeding.\x02\x03",
            "#0000FIt may look like trouble, but if we use\x01",
            "arts to our advantage, we can win.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -108410, 0, 199890, 90)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_27_4356 end

    def Function_28_4409(): pass

    label("Function_28_4409")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_68(-198820, 1150, 198900, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20170, 0)
    SetCameraDistance(19170, 2000)
    SetChrPos(0x101, -195700, 0, 199000, 270)
    SetChrPos(0x102, -195700, 0, 200200, 270)
    SetChrPos(0x103, -194500, 0, 199000, 270)
    SetChrPos(0x104, -194500, 0, 200200, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        (
            "#0100487V#0000F#12PLet's try using crafts against the\x01",
            "enemy this time!\x02\x03",
            "#0100488VCombined with our arts, a wide\x01",
            "range of tactics are open to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100489V#0204F#12PYes, let us fight effectively.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100490V#0304F#12PLooks like it's my time to shine.\x02\x03",
            "#0100491V#0309FTrust me, you don't want to miss any\x01",
            "of my killer moves! Watch and learn!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100492V#0106F#12P*sigh* Try not to hurt yourself.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x0, -195700, 0, 199000, 270)
    SetScenarioFlags(0x44, 2)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_28_4409 end

    def Function_29_466D(): pass

    label("Function_29_466D")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    ChrTalk(
        0x101,
        (
            "#0000FLet's try using crafts against the\x01",
            "enemy this time.\x02\x03",
            "This will be a good way to see\x01",
            "what everyone's capable of.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -200160, 0, 205020, 180)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_29_466D end

    def Function_30_470D(): pass

    label("Function_30_470D")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    ChrTalk(
        0x101,
        (
            "#0000FLet's try using crafts against the\x01",
            "enemy this time.\x02\x03",
            "This will be a good way to see what\x01",
            "everyone's capable of.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -200060, 0, 194270, 0)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_30_470D end

    def Function_31_47AD(): pass

    label("Function_31_47AD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0xB, 0x80)
    OP_68(-200470, 2000, 288110, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22670, 0)
    SetCameraDistance(21670, 2000)
    SetChrPos(0x101, -199200, 0, 287270, 0)
    SetChrPos(0x102, -200610, 0, 287270, 0)
    SetChrPos(0x103, -200610, 0, 285570, 0)
    SetChrPos(0x104, -199200, 0, 285570, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x104,
        (
            "#0100493V#0305FGeez, there's more of these guys?\x02\x03",
            "#0100494V#0306FI'd rather just take them out all at\x01",
            "once, y'know? Fighting battle after\x01",
            "battle is kind of a drag.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100495V#0003FWe should try using S-Crafts, then.\x02\x03",
            "#0100496V#0001FThe battle shouldn't last long if we\x01",
            "use the power of S-Crafts and S-Breaks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100497V#0203FThose are powerful moves that can be used\x01",
            "when CP is over 100, correct?\x02\x03",
            "#0100498V#0201FVery well. Knowing how each of our S-Crafts\x01",
            "work will help us in the long term.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100499V#0102FI use a recovery S-Craft, so don't hesitate\x01",
            "to rely on me when the going gets rough.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x0, -200070, 0, 286380, 0)
    SetScenarioFlags(0x49, 3)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_31_47AD end

    def Function_32_4ADA(): pass

    label("Function_32_4ADA")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    ChrTalk(
        0x101,
        (
            "#0000FLet's use our S-Crafts this time around.\x02\x03",
            "They're incredibly powerful... They might even\x01",
            "be able to take out these monsters in one hit.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -200300, 0, 316760, 180)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_32_4ADA end

    def Function_33_4B92(): pass

    label("Function_33_4B92")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-100000, 2100, -8800, 0)
    MoveCamera(40, 40, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_90(0x101, -99400, 3800, -12600, 0)
    OP_90(0x103, -100600, 3800, -13300, 0)

    def lambda_4BF5():
        OP_96(0xFE, 0xFFFE7708, 0x0, 0xFFFFED40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4BF5)
    Sleep(50)

    def lambda_4C12():
        OP_96(0xFE, 0xFFFE7BB8, 0x0, 0xFFFFED40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C12)
    OP_68(-100000, 1100, -4800, 4000)
    MoveCamera(40, 25, 0, 4000)
    SetCameraDistance(19500, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#3300247V#12P#0001FSo, we just need to take the\x01",
            "elevator down, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 3)), scpexpr(EXPR_END)), "loc_4DC6")

    ChrTalk(
        0x103,
        (
            "#3300263V#6P#0203FCorrect.\x02\x03",
            "#3300249V#0200FDo you recall coming across an\x01",
            "inoperable elevator when we\x01",
            "initially came down here?\x02\x03",
            "#3300253VThat is the one we need. Once I input the\x01",
            "authentication code, we will be able to\x01",
            "ride the elevator to the area below.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EE5")

    label("loc_4DC6")


    ChrTalk(
        0x103,
        (
            "#3300251V#6P#0203FCorrect.\x02\x03",
            "#3300252V#0200FDo you recall our first mission in here?\x01",
            "There should have been a deactivated\x01",
            "elevator somewhere near that area.\x02\x03",
            "#3300250VThat's the one we need. Once I input the\x01",
            "authentication code, we'll be able to\x01",
            "ride the elevator to the area below.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EE5")

    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3300254V#6P#0000FUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#3300255V#0005F#11PBut Tio, how exactly did you get your hands\x01",
            "on a Geofront authentication code?\x01",
            "Don't tell me Jona is rubbing off on you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300256V#6P#0203FYou see, when I was using the IBC's main\x01",
            "terminal, I stumbled across it by chance\x01",
            "when I was determining Jona's location.\x02\x03",
            "#3300257VIt should be the right code.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3300258V#0001F#11PAre you sure this is a bright idea? We didn't\x01",
            "exactly get that through proper means...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300259V#6P#0204FThe Geofront is a Crossbell City facility,\x01",
            "so legally, I do not see an issue.\x02\x03",
            "#3300260V#0202FWe are merely shortening the process,\x01",
            "that is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300261V#0012F#11PIf you say so.\x02\x03",
            "#3300262V#0000FHmm... No turning back now, I guess.\x01",
            "Let's head on down, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300248V#6P#0202FRoger.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -100000, 0, -4800, 0)
    SetScenarioFlags(0xA0, 6)
    OP_C7(0x0, 0x1000)
    OP_29(0x45, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5282")
    OP_29(0x1D, 0x4, 0x40)
    Jump("loc_5294")

    label("loc_5282")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5294")
    OP_29(0x1D, 0x4, 0x40)

    label("loc_5294")

    OP_E0(0x0)
    Call(0, 7)
    EventEnd(0x5)
    Return()

    # Function_33_4B92 end

    def Function_34_529C(): pass

    label("Function_34_529C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55E2")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5396")

    ChrTalk(
        0x102,
        (
            "#0100FLloyd, are you planning on leaving\x01",
            "the other child in here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FN-No, of course not. We can't afford\x01",
            "to head to the surface right now.\x02\x03",
            "If we want to find him, we should\x01",
            "head deeper into the Geofront.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55DA")

    label("loc_5396")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_544E")

    ChrTalk(
        0x101,
        (
            "#0000FHold on a second. We need to\x01",
            "keep searching for the other kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FRight. Judging by what Anri told\x01",
            "us, he must be on a lower floor.\x02\x03",
            "Let's hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55DA")

    label("loc_544E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_551B")

    ChrTalk(
        0x101,
        (
            "#0000FHold on a second. We need to\x01",
            "keep searching for the other kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FYou are correct. It is likely that the other\x01",
            "boy is in the depths of the Geofront.\x02\x03",
            "We should hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55DA")

    label("loc_551B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55DA")

    ChrTalk(
        0x101,
        (
            "#0000FHold on a second. We need to\x01",
            "keep searching for the other kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FWhoops, my bad. Kid made his\x01",
            "way deeper into this place, right?\x02\x03",
            "Let's get a move on, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55DA")

    SetScenarioFlags(0x0, 0)
    Jump("loc_5636")

    label("loc_55E2")


    ChrTalk(
        0x101,
        (
            "#0000FWe still haven't located Anri's friend...\x02\x03",
            "Let's investigate furhter in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5636")

    Sleep(50)
    SetChrPos(0x0, -100000, 0, -4500, 0)
    EventEnd(0x4)
    Return()

    # Function_34_529C end

    def Function_35_564D(): pass

    label("Function_35_564D")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and cannot be opened.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_35_564D end

    def Function_36_5689(): pass

    label("Function_36_5689")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and cannot be opened.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_36_5689 end

    SaveToFile()

Try(main)
