from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0111.bin",                # FileName
        "m0111",                    # MapName
        "m0111",                    # Location
        0x0068,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 104, 0, 1, 0, 2],
    )

    BuildStringList((
        "m0111",                  # 0
        "bm0110",                 # 1
        "bm0111",                 # 2
        "bm0111",                 # 3
        "bm0111",                 # 4
        "bm0111",                 # 5
        "bm0110",                 # 6
        "bm0110",                 # 7
        "bm0110",                 # 8
        "bm0110",                 # 9
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 1,   8,   6,   1,   1,   1,   2)
    Sepith("Sepith_B4", 0,   1,   0,   2,   0,   0,   0)
    Sepith("Sepith_C4", 1,   8,   6,   1,   1,   1,   2)
    Sepith("Sepith_D4", 1,   1,   0,   1,   1,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_E4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_108", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_110", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_114", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_118", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_11C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 9, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_144", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_148", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_14C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_150", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_154", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_158", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_15C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 5, 5, 45)

    # monster count: 9

    BattleInfo(
        "BattleInfo_164", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0111", "Sepith_A4", 30, 45, 20, 5,
        (
            ("ms61900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61900.dat", "ms61900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61900.dat", "ms61900.dat", "ms61900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61900.dat", "ms61900.dat", "ms61900.dat", "ms61900.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_22C", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0110", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms68000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68000.dat", "ms68000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68000.dat", "ms68000.dat", "ms68000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68000.dat", "ms68000.dat", "ms68000.dat", "ms68000.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_2F4", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0111", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms68000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68000.dat", "ms68000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68000.dat", "ms68000.dat", "ms68000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68000.dat", "ms68000.dat", "ms68000.dat", "ms68000.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3BC", 0x0000, 48, 6, 60, 6, 1, 25, 0, "bm0110", "Sepith_C4", 30, 45, 20, 5,
        (
            ("ms60200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60200.dat", "ms60200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60200.dat", "ms60200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60200.dat", "ms60200.dat", "ms60200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_484", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0110", "Sepith_D4", 30, 45, 20, 5,
        (
            ("ms71200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71200.dat", "ms71200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71200.dat", "ms71200.dat", "ms71200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71200.dat", "ms71200.dat", "ms71200.dat", "ms71200.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_54C", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0110", "Sepith_A4", 30, 45, 20, 5,
        (
            ("ms61900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61900.dat", "ms61900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61900.dat", "ms61900.dat", "ms61900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61900.dat", "ms61900.dat", "ms61900.dat", "ms61900.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_614", 0x0000, 48, 6, 60, 6, 1, 25, 0, "bm0111", "Sepith_C4", 30, 45, 20, 5,
        (
            ("ms60200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60200.dat", "ms60200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60200.dat", "ms60200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60200.dat", "ms60200.dat", "ms60200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
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
        "monster/ch68050.itc",               # 10
        "monster/ch68050.itc",               # 11
        "monster/ch60250.itc",               # 12
        "monster/ch60250.itc",               # 13
        "monster/ch61950.itc",               # 14
        "monster/ch61950.itc",               # 15
        "monster/ch71250.itc",               # 16
        "monster/ch71251.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(199700,  299140,  0,       0x1010000,    "BattleInfo_164", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(187850,  399810,  -6000,   0x1010000,    "BattleInfo_22C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(213870,  387530,  -10000,  0x1010000,    "BattleInfo_2F4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-3090,   399700,  0,       0x1010000,    "BattleInfo_3BC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-17980,  503930,  5000,    0x1010000,    "BattleInfo_22C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(18020,   504200,  5000,    0x1010000,    "BattleInfo_484", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(397570,  400020,  0,       0x1010000,    "BattleInfo_54C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(198570,  400020,  -2000,   0x1010000,    "BattleInfo_22C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(217950,  409500,  4000,    0x1010000,    "BattleInfo_614", 0,   18,  0xFFFF, 2,  3)

    DeclActor(220080,  -10000,  386550,  1200,    220080,  -9000,   386550,  0x007C, 0,  4,  0x0000)
    DeclActor(218000,  4000,    414000,  1200,    218000,  5000,    414000,  0x007C, 0,  5,  0x0000)
    DeclActor(182300,  -4000,   414800,  1200,    182300,  -3000,   414800,  0x007C, 0,  6,  0x0000)
    DeclActor(-40,     0,       400000,  1200,    -40,     1000,    400000,  0x007C, 0,  7,  0x0000)
    DeclActor(399970,  0,       399980,  1200,    399970,  1000,    399980,  0x007C, 0,  8,  0x0000)
    DeclActor(200000,  0,       602000,  1200,    200000,  1000,    602500,  0x007C, 0,  13, 0x0000)
    DeclActor(200370,  -10000,  389590,  1200,    200370,  -9000,   389590,  0x007C, 0,  9,  0x0000)
    DeclActor(190500,  0,       417500,  1200,    190500,  1000,    417500,  0x007C, 0,  10, 0x0000)
    DeclActor(209500,  -6000,   409500,  1200,    209500,  -5000,   409500,  0x007C, 0,  11, 0x0000)
    DeclActor(214500,  -2000,   405500,  1200,    214500,  -1000,   405500,  0x007C, 0,  12, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7

    ScpFunction((
        "Function_0_A7C",          # 00, 0
        "Function_1_AA7",          # 01, 1
        "Function_2_AD0",          # 02, 2
        "Function_3_112B",         # 03, 3
        "Function_4_121E",         # 04, 4
        "Function_5_1381",         # 05, 5
        "Function_6_1509",         # 06, 6
        "Function_7_164B",         # 07, 7
        "Function_8_17C8",         # 08, 8
        "Function_9_1923",         # 09, 9
        "Function_10_1AE3",        # 0A, 10
        "Function_11_1C9B",        # 0B, 11
        "Function_12_1E8A",        # 0C, 12
        "Function_13_2079",        # 0D, 13
        "Function_14_2202",        # 0E, 14
    ))


    def Function_0_A7C(): pass

    label("Function_0_A7C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A9E")
    Sound(150, 0, 100, 0)
    Sleep(900)
    Jump("loc_AA1")

    label("loc_A9E")

    Sleep(30)

    label("loc_AA1")

    Jump("Function_0_A7C")

    label("loc_AA6")

    Return()

    # Function_0_A7C end

    def Function_1_AA7(): pass

    label("Function_1_AA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACF")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACF")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)

    label("loc_ACF")

    Return()

    # Function_1_AA7 end

    def Function_2_AD0(): pass

    label("Function_2_AD0")

    ClearScenarioFlags(0x0, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 194000, -10000, 388000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 198000, -10000, 388000, 4000, 2000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 7)), scpexpr(EXPR_END)), "loc_B78")
    SetMapObjFrame(0xD, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xC, "m01gim00", 0x2, "loop")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B73")
    SetScenarioFlags(0x0, 0)

    label("loc_B73")

    Jump("loc_BA7")

    label("loc_B78")

    SetMapObjFrame(0xD, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xC, "m01gim00", 0x2, "stop_kp")
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)

    label("loc_BA7")

    SetBarrier(0x0, 0x2, 0x1, 0x0, 184000, -4000, 410000, 4000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 0)), scpexpr(EXPR_END)), "loc_BFD")
    SetMapObjFrame(0xE, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xB, "m01gim00", 0x2, "stop_kp")
    SetBarrier(0x2, 0x2, 0x1)
    Jump("loc_C50")

    label("loc_BFD")

    SetMapObjFrame(0xE, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xB, "m01gim00", 0x2, "loop")
    SetBarrier(0x3, 0x2, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C50")
    SetScenarioFlags(0x0, 0)

    label("loc_C50")

    SetBarrier(0x0, 0x3, 0x1, 0x0, 208000, -6000, 398000, 4000, 2000, 0)
    SetBarrier(0x0, 0x4, 0x1, 0x0, 208000, -6000, 402000, 4000, 2000, 0)
    SetBarrier(0x0, 0x5, 0x1, 0x0, 206000, -2000, 400000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x6, 0x1, 0x0, 210000, -2000, 400000, 4000, 2000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 1)), scpexpr(EXPR_END)), "loc_D1C")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xA, "m01gim00", 0x2, "stop_kp")
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    Jump("loc_D8D")

    label("loc_D1C")

    SetMapObjFrame(0xF, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xA, "m01gim00", 0x2, "loop")
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D8D")
    SetScenarioFlags(0x0, 0)

    label("loc_D8D")

    SetMapObjFrame(0x9, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
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
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C7")
    OP_70(0x11, 0x0)
    Jump("loc_10CB")

    label("loc_10C7")

    OP_70(0x11, 0x1E)

    label("loc_10CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DE")
    OP_70(0x12, 0x0)
    Jump("loc_10E2")

    label("loc_10DE")

    OP_70(0x12, 0x1E)

    label("loc_10E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F5")
    OP_70(0x13, 0x0)
    Jump("loc_10F9")

    label("loc_10F5")

    OP_70(0x13, 0x1E)

    label("loc_10F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110C")
    OP_70(0x14, 0x0)
    Jump("loc_1110")

    label("loc_110C")

    OP_70(0x14, 0x1E)

    label("loc_1110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1123")
    OP_70(0x15, 0x0)
    Jump("loc_1127")

    label("loc_1123")

    OP_70(0x15, 0x1E)

    label("loc_1127")

    Call(0, 3)
    Return()

    # Function_2_AD0 end

    def Function_3_112B(): pass

    label("Function_3_112B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_114C")
    SetChrFlags(0x9, 0x8)
    Jump("loc_1151")

    label("loc_114C")

    ClearChrFlags(0x9, 0x8)

    label("loc_1151")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11A5")
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    Jump("loc_11CB")

    label("loc_11A5")

    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x11, 0x8)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)

    label("loc_11CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E9")
    SetChrFlags(0xC, 0x8)
    SetMapObjFlags(0x14, 0x4)
    Jump("loc_11F4")

    label("loc_11E9")

    ClearChrFlags(0xC, 0x8)
    ClearMapObjFlags(0x14, 0x4)

    label("loc_11F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1212")
    SetChrFlags(0xF, 0x8)
    SetMapObjFlags(0x15, 0x4)
    Jump("loc_121D")

    label("loc_1212")

    ClearChrFlags(0xF, 0x8)
    ClearMapObjFlags(0x15, 0x4)

    label("loc_121D")

    Return()

    # Function_3_112B end

    def Function_4_121E(): pass

    label("Function_4_121E")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1308")
    Sound(14, 0, 100, 0)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_129E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10E, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1303")

    label("loc_129E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
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

    label("loc_1303")

    Jump("loc_1375")

    label("loc_1308")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "While you're here, don't forget to like,\x01",
            "comment, and chestscribe.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1375")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_121E end

    def Function_5_1381(): pass

    label("Function_5_1381")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14BC")
    Sound(14, 0, 100, 0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x12, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x200.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10E, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_14F7")

    label("loc_14BC")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Dieter chuckled. 'You mean the Chaos Septium?'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_14F7")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1381 end

    def Function_6_1509(): pass

    label("Function_6_1509")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F3")
    Sound(14, 0, 100, 0)
    OP_71(0x13, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x8B, 1)"), scpexpr(EXPR_END)), "loc_1589")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x8B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10E, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_15EE")

    label("loc_1589")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x8B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x13, 0x1E, 0x0, 0x0, 0x0)

    label("loc_15EE")

    Jump("loc_163F")

    label("loc_15F3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I'M ESKIMO. THERE'S NOTHING HERE.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_163F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1509 end

    def Function_7_164B(): pass

    label("Function_7_164B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1735")
    Sound(14, 0, 100, 0)
    OP_71(0x14, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_16CB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10E, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_1730")

    label("loc_16CB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x14, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1730")

    Jump("loc_17BC")

    label("loc_1735")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you get any more handsy, I'm going to\x01",
            "have to do your job for you and take you\x01",
            "in myself!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_17BC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_164B end

    def Function_8_17C8(): pass

    label("Function_8_17C8")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18B2")
    Sound(14, 0, 100, 0)
    OP_71(0x15, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1848")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10F, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_18AD")

    label("loc_1848")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x15, 0x1E, 0x0, 0x0, 0x0)

    label("loc_18AD")

    Jump("loc_1917")

    label("loc_18B2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The chest reaches into your pocket\x01",
            "and retrieves the item.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1917")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_17C8 end

    def Function_9_1923(): pass

    label("Function_9_1923")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a water flow control valve.\x01",
            "Turn it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ADB")
    Fade(500)
    SetChrPos(0x0, 200240, -10000, 387960, 0)
    SetChrPos(0x1, 202140, -10000, 388170, 270)
    SetChrPos(0x2, 201910, -10000, 386570, 270)
    SetChrPos(0x3, 203590, -10000, 387700, 270)
    OP_68(195890, -9000, 388020, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 7)), scpexpr(EXPR_END)), "loc_1A75")
    SetMapObjFrame(0xD, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    ClearScenarioFlags(0x55, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A4B")
    ClearScenarioFlags(0x0, 0)

    label("loc_1A4B")

    SetMapObjFrame(0xC, "m01gim00", 0x2, "stop")
    Sleep(900)
    Sound(151, 0, 100, 0)
    Sleep(300)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    Jump("loc_1ADB")

    label("loc_1A75")

    SetMapObjFrame(0xD, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    SetScenarioFlags(0x0, 0)
    SetMapObjFrame(0xC, "m01gim00", 0x2, "start")
    Sleep(1000)
    SetMapObjFrame(0xC, "m01gim00", 0x2, "loop")
    Sleep(500)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetScenarioFlags(0x55, 7)

    label("loc_1ADB")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1923 end

    def Function_10_1AE3(): pass

    label("Function_10_1AE3")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a water flow control valve.\x01",
            "Turn it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C93")
    Fade(500)
    SetChrPos(0x0, 190570, 0, 416000, 0)
    SetChrPos(0x1, 191500, 0, 415480, 270)
    SetChrPos(0x2, 191500, 0, 414270, 270)
    SetChrPos(0x3, 192820, 0, 414790, 270)
    OP_68(187710, -3000, 415370, 0)
    MoveCamera(45, 49, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(49500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 0)), scpexpr(EXPR_END)), "loc_1C2A")
    SetMapObjFrame(0xE, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    SetScenarioFlags(0x0, 0)
    SetMapObjFrame(0xB, "m01gim00", 0x2, "start")
    Sleep(1000)
    SetMapObjFrame(0xB, "m01gim00", 0x2, "loop")
    Sleep(500)
    SetBarrier(0x3, 0x2, 0x1)
    ClearScenarioFlags(0x56, 0)
    Jump("loc_1C93")

    label("loc_1C2A")

    SetMapObjFrame(0xE, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    SetScenarioFlags(0x56, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C72")
    ClearScenarioFlags(0x0, 0)

    label("loc_1C72")

    SetMapObjFrame(0xB, "m01gim00", 0x2, "stop")
    Sleep(900)
    Sound(151, 0, 100, 0)
    Sleep(300)
    SetBarrier(0x2, 0x2, 0x1)

    label("loc_1C93")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1AE3 end

    def Function_11_1C9B(): pass

    label("Function_11_1C9B")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a water flow control valve.\x01",
            "Turn it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E82")
    Fade(500)
    SetChrPos(0x0, 209440, -6000, 408170, 0)
    SetChrPos(0x1, 207500, -6000, 408360, 90)
    SetChrPos(0x2, 207500, -6000, 406730, 90)
    SetChrPos(0x3, 206140, -6000, 407330, 90)
    OP_68(208940, -5000, 404530, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(39000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 1)), scpexpr(EXPR_END)), "loc_1DFD")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "on")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    SetScenarioFlags(0x0, 0)
    SetMapObjFrame(0xA, "m01gim00", 0x2, "start")
    Sleep(1000)
    SetMapObjFrame(0xA, "m01gim00", 0x2, "loop")
    Sleep(500)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    ClearScenarioFlags(0x56, 1)
    Jump("loc_1E82")

    label("loc_1DFD")

    SetMapObjFrame(0xF, "m01gim01", 0x2, "off")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    SetScenarioFlags(0x56, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E55")
    ClearScenarioFlags(0x0, 0)

    label("loc_1E55")

    SetMapObjFrame(0xA, "m01gim00", 0x2, "stop")
    Sleep(900)
    Sound(151, 0, 100, 0)
    Sleep(300)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)

    label("loc_1E82")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_1C9B end

    def Function_12_1E8A(): pass

    label("Function_12_1E8A")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a water flow control valve.\x01",
            "Turn it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2071")
    Fade(500)
    SetChrPos(0x0, 214830, -2000, 403840, 0)
    SetChrPos(0x1, 216000, -2000, 403570, 270)
    SetChrPos(0x2, 216000, -2000, 401770, 270)
    SetChrPos(0x3, 218110, -2000, 403260, 270)
    OP_68(210030, -1000, 399030, 0)
    MoveCamera(45, 46, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(41000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 1)), scpexpr(EXPR_END)), "loc_1FEC")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "on")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    SetScenarioFlags(0x0, 0)
    SetMapObjFrame(0xA, "m01gim00", 0x2, "start")
    Sleep(1000)
    SetMapObjFrame(0xA, "m01gim00", 0x2, "loop")
    Sleep(500)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    ClearScenarioFlags(0x56, 1)
    Jump("loc_2071")

    label("loc_1FEC")

    SetMapObjFrame(0xF, "m01gim01", 0x2, "off")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    SetScenarioFlags(0x56, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2044")
    ClearScenarioFlags(0x0, 0)

    label("loc_2044")

    SetMapObjFrame(0xA, "m01gim00", 0x2, "stop")
    Sleep(900)
    Sound(151, 0, 100, 0)
    Sleep(300)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)

    label("loc_2071")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_1E8A end

    def Function_13_2079(): pass

    label("Function_13_2079")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21FA")
    Fade(500)
    SetChrPos(0x0, 200600, 0, 600600, 0)
    SetChrPos(0x1, 199400, 0, 600600, 0)
    SetChrPos(0x2, 199400, 0, 599400, 0)
    SetChrPos(0x3, 200600, 0, 599400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2158")
    SetChrPos(0x4, 199400, 0, 598200, 0)
    SetChrPos(0x5, 200600, 0, 598200, 0)
    Jump("loc_2177")

    label("loc_2158")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2177")
    SetChrPos(0x4, 200000, 0, 598200, 0)

    label("loc_2177")

    OP_68(200600, 1000, 600000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(200600, -4000, 600000, 3000)
    SetMapObjFrame(0x9, "m00ele00", 0x2, "down")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0112", 0, 0, 0)
    IdleLoop()

    label("loc_21FA")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_2079 end

    def Function_14_2202(): pass

    label("Function_14_2202")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0x9, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(200600, -4000, 600000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 200600, 30000, 600600, 0)
    OP_90(0x1, 199400, 30000, 600600, 0)
    OP_90(0x2, 199400, 30000, 599400, 0)
    OP_90(0x3, 200600, 30000, 599400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22D5")
    OP_90(0x4, 199400, 30000, 598200, 0)
    OP_90(0x5, 200600, 30000, 598200, 0)
    Jump("loc_22F4")

    label("loc_22D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22F4")
    OP_90(0x4, 200000, 30000, 598200, 0)

    label("loc_22F4")

    Sound(145, 0, 100, 0)
    OP_68(200600, 1000, 600000, 3000)
    SetMapObjFrame(0x9, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x9)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_2202 end

    SaveToFile()

Try(main)
