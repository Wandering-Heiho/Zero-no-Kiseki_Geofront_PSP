from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0101.bin",                # FileName
        "m0101",                    # MapName
        "m0101",                    # Location
        0x0068,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -3000, 0, 0, 0, 0, 1, 104, 0, 2, 0, 3],
    )

    BuildStringList((
        "m0101",                  # 0
        "Jona",                   # 1
        "Tableware",              # 2
        "Tableware",              # 3
        "Tableware",              # 4
        "Tableware",              # 5
        "Tableware",              # 6
        "Tableware",              # 7
        "Jet Tortoise",           # 8
        "Ginuna",                 # 9
        "SE制御",                 # 10
        "bm0101",                 # 11
        "bm0101",                 # 12
        "bm0101",                 # 13
        "bm0101",                 # 14
        "bm0100",                 # 15
        "bm0100",                 # 16
        "bm0100",                 # 17
        "bm0100",                 # 18
        "bm0100",                 # 19
        "bm0100",                 # 20
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 12,  1,   8,   0,   3,   7,   0)
    Sepith("Sepith_B4", 0,   12,  5,   0,   7,   2,   6)
    Sepith("Sepith_C4", 0,   0,   0,   10,  7,   7,   7)
    Sepith("Sepith_D4", 8,   0,   12,  0,   0,   5,   7)

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
    MonsterBattlePostion("MonsterBattlePostion_144", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_148", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_14C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_150", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_154", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_158", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_15C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_164", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_168", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_16C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_170", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_174", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_178", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_17C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_180", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_184", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_188", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_18C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_190", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_194", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_198", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_19C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_1A0", 2, 13, 180)

    # monster count: 7

    BattleInfo(
        "BattleInfo_1A4", 0x0000, 18, 6, 60, 6, 1, 25, 0, "bm0101", "Sepith_A4", 30, 45, 20, 5,
        (
            ("ms75800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms75800.dat", "ms75800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms75800.dat", "ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_26C", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms63800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63800.dat", "ms63800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63800.dat", "ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_334", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0100", "Sepith_C4", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3FC", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_C4", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_4C4", 0x0000, 18, 6, 60, 6, 1, 30, 0, "bm0101", "Sepith_D4", 30, 45, 20, 5,
        (
            ("ms68700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68700.dat", "ms68700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68700.dat", "ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_58C", 0x0000, 18, 6, 60, 0, 1, 0, 0, "bm0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75800.dat", "ms75800.dat", "ms75800.dat", "ms68700.dat", "ms68700.dat", "ms75800.dat", 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_164", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5D0", 0x0000, 18, 6, 60, 0, 1, 0, 0, "bm0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63800.dat", "ms63800.dat", "ms68700.dat", "ms63800.dat", "ms63800.dat", "ms68700.dat", 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_164", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch06100.itc",                   # 00
        "chr/ch06102.itc",                   # 01
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
        "monster/ch63850.itc",               # 10
        "monster/ch63851.itc",               # 11
        "monster/ch68750.itc",               # 12
        "monster/ch68750.itc",               # 13
        "monster/ch75850.itc",               # 14
        "monster/ch75851.itc",               # 15
        "monster/ch60550.itc",               # 16
        "monster/ch60550.itc",               # 17
    ))

    DeclNpc(498200,  200,     302000,  0,    261,  0x0, 0,   1,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(109959,  -5500,   19,      0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(92000,   -8500,   90500,   0,    484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(99960,   100050,  -10000,  0x1010000,    "BattleInfo_1A4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(100360,  200740,  0,       0x1010000,    "BattleInfo_26C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-290,    199690,  0,       0x1010000,    "BattleInfo_334", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(109910,  99810,   -7000,   0x1010000,    "BattleInfo_3FC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(200810,  94840,   0,       0x1010000,    "BattleInfo_1A4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(199760,  195940,  -10000,  0x1010000,    "BattleInfo_4C4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(202350,  204410,  -10000,  0x1010000,    "BattleInfo_26C", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 33,  504.5,                 200.0,                 -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -252.25,               -100.0,                0.20000000298023224,   1.0])

    DeclActor(109960,  -6000,   20,      1200,    109960,  -5000,   20,      0x007C, 0,  5,  0x0000)
    DeclActor(109970,  -3000,   113430,  1200,    109970,  -2000,   113430,  0x007C, 0,  6,  0x0000)
    DeclActor(190010,  -4000,   200010,  1200,    190010,  -3000,   200010,  0x007C, 0,  7,  0x0000)
    DeclActor(92000,   -9000,   90500,   1200,    92000,   -8000,   90500,   0x007C, 0,  8,  0x0000)
    DeclActor(500000,  150,     208500,  1200,    500000,  1150,    208500,  0x007C, 0,  19, 0x0000)
    DeclActor(2000,    0,       0,       1200,    2500,    1000,    0,       0x007C, 0,  17, 0x0000)
    DeclActor(108000,  -6000,   2500,    2000,    108000,  -5000,   2500,    0x007C, 0,  13, 0x0000)
    DeclActor(85500,   -6000,   103000,  2000,    85500,   -5000,   103000,  0x007C, 0,  14, 0x0000)
    DeclActor(203430,  -6000,   184020,  2000,    203430,  -5000,   184020,  0x007C, 0,  15, 0x0000)
    DeclActor(320000,  -1000,   302800,  1200,    320000,  500,     302800,  0x007C, 0,  12, 0x0000)
    DeclActor(496130,  0,       296360,  1200,    496130,  1000,    296360,  0x007C, 0,  11, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7

    ScpFunction((
        "Function_0_B40",          # 00, 0
        "Function_1_B5D",          # 01, 1
        "Function_2_B7C",          # 02, 2
        "Function_3_C3C",          # 03, 3
        "Function_4_12AB",         # 04, 4
        "Function_5_1385",         # 05, 5
        "Function_6_15A9",         # 06, 6
        "Function_7_1715",         # 07, 7
        "Function_8_184B",         # 08, 8
        "Function_9_1A8A",         # 09, 9
        "Function_10_503F",        # 0A, 10
        "Function_11_53D2",        # 0B, 11
        "Function_12_5552",        # 0C, 12
        "Function_13_5652",        # 0D, 13
        "Function_14_566E",        # 0E, 14
        "Function_15_568A",        # 0F, 15
        "Function_16_56A6",        # 10, 16
        "Function_17_5B94",        # 11, 17
        "Function_18_5D1B",        # 12, 18
        "Function_19_5E62",        # 13, 19
        "Function_20_5EE8",        # 14, 20
        "Function_21_6910",        # 15, 21
        "Function_22_696C",        # 16, 22
        "Function_23_6D9E",        # 17, 23
        "Function_24_A3F4",        # 18, 24
        "Function_25_A4AE",        # 19, 25
        "Function_26_CD3A",        # 1A, 26
        "Function_27_CDF4",        # 1B, 27
        "Function_28_CE38",        # 1C, 28
        "Function_29_CEA1",        # 1D, 29
        "Function_30_D5A6",        # 1E, 30
        "Function_31_E85C",        # 1F, 31
        "Function_32_E877",        # 20, 32
        "Function_33_E8BD",        # 21, 33
    ))


    def Function_0_B40(): pass

    label("Function_0_B40")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B5C")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_B40")

    label("loc_B5C")

    Return()

    # Function_0_B40 end

    def Function_1_B5D(): pass

    label("Function_1_B5D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B7B")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_B5D")

    label("loc_B7B")

    Return()

    # Function_1_B5D end

    def Function_2_B7C(): pass

    label("Function_2_B7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA4")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA4")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 18)

    label("loc_BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_BB2")
    Jump("loc_BDF")

    label("loc_BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_BD1")
    SetChrPos(0x8, 497850, 200, 296250, 270)
    Jump("loc_BDF")

    label("loc_BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_END)), "loc_BDF")
    Jump("loc_BDF")

    label("loc_BDF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFE")
    Event(0, 22)
    Jump("loc_C18")

    label("loc_BFE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C18")
    Event(0, 25)

    label("loc_C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_C2C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 20)
    Jump("loc_C3B")

    label("loc_C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_C3B")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 30)

    label("loc_C3B")

    Return()

    # Function_2_B7C end

    def Function_3_C3C(): pass

    label("Function_3_C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C4F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x86), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C83")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x209), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x28, 0xC8)
    Jump("loc_CA0")

    label("loc_C83")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x209), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x64, 0xC8)

    label("loc_CA0")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBC")
    ClearMapObjFlags(0x13, 0x10)
    OP_66(0x4, 0x1)

    label("loc_CBC")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD0")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_CD0")

    ClearMapObjFlags(0x18, 0x10)
    OP_70(0x18, 0x1E)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x86), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D0F")
    SetMapFlags(0x2000)
    OP_E0(0x0)
    Jump("loc_D14")

    label("loc_D0F")

    ClearMapFlags(0x2000)

    label("loc_D14")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 106000, -6000, 0, 6000, 2000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 98000, -6000, 0, 6000, 2000, 90000)
    SetBarrier(0x0, 0x2, 0x1, 0x0, 100000, -7380, 89000, 4000, 2000, 0)
    SetBarrier(0x0, 0x3, 0x1, 0x0, 100000, -7800, 110000, 4000, 2000, 0)
    SetBarrier(0x0, 0x4, 0x1, 0x0, 96000, -7000, 100000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x5, 0x1, 0x0, 104000, -7000, 100000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x6, 0x1, 0x0, 92000, -8000, 96000, 4000, 2000, 0)
    SetBarrier(0x0, 0x7, 0x1, 0x0, 0, -7000, 100000, 4000, 2000, 0)
    SetBarrier(0x0, 0x8, 0x1, 0x0, 0, -7000, 92000, 4000, 2000, 0)
    SetBarrier(0x0, 0x9, 0x1, 0x0, 200000, -8000, 190000, 8000, 2000, 0)
    SetBarrier(0x0, 0xA, 0x1, 0x0, 200000, -8000, 210000, 8000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 6)), scpexpr(EXPR_END)), "loc_ED0")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    SetBarrier(0x2, 0x8, 0x1)
    SetBarrier(0x3, 0x9, 0x1)
    SetBarrier(0x3, 0xA, 0x1)
    SetMapObjFrame(0xE, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "Null", 0x2, "high")
    Jump("loc_F41")

    label("loc_ED0")

    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    SetBarrier(0x3, 0x8, 0x1)
    SetBarrier(0x2, 0x9, 0x1)
    SetBarrier(0x2, 0xA, 0x1)
    SetMapObjFrame(0xE, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "Null", 0x2, "low")

    label("loc_F41")

    SetMapObjFrame(0x11, "m00ele00", 0x2, "down_kp")
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
    SetMapObjFrame(0x9, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x9, "light01", 0x0, 0x1)
    SetMapObjFrame(0xA, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xA, "light01", 0x0, 0x1)
    SetMapObjFrame(0xB, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xB, "light01", 0x0, 0x1)
    SetMapObjFrame(0xC, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xC, "light01", 0x0, 0x1)
    SetMapObjFrame(0xD, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xD, "light01", 0x0, 0x1)
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125E")
    OP_70(0x14, 0x0)
    Jump("loc_1262")

    label("loc_125E")

    OP_70(0x14, 0x1E)

    label("loc_1262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1275")
    OP_70(0x15, 0x0)
    Jump("loc_1279")

    label("loc_1275")

    OP_70(0x15, 0x1E)

    label("loc_1279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128C")
    OP_70(0x16, 0x0)
    Jump("loc_1290")

    label("loc_128C")

    OP_70(0x16, 0x1E)

    label("loc_1290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A3")
    OP_70(0x17, 0x0)
    Jump("loc_12A7")

    label("loc_12A3")

    OP_70(0x17, 0x1E)

    label("loc_12A7")

    Call(0, 4)
    Return()

    # Function_3_C3C end

    def Function_4_12AB(): pass

    label("Function_4_12AB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12CD")
    SetMapObjFlags(0x14, 0x4)
    Jump("loc_12D3")

    label("loc_12CD")

    ClearMapObjFlags(0x14, 0x4)

    label("loc_12D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1312")
    SetChrFlags(0x15, 0x8)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x17, 0x4)
    Jump("loc_1323")

    label("loc_1312")

    ClearChrFlags(0x15, 0x8)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x17, 0x4)

    label("loc_1323")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7C), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1353")
    SetChrFlags(0x18, 0x8)
    SetMapObjFlags(0x16, 0x4)
    Jump("loc_135E")

    label("loc_1353")

    ClearChrFlags(0x18, 0x8)
    ClearMapObjFlags(0x16, 0x4)

    label("loc_135E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137F")
    SetChrFlags(0x16, 0x8)
    Jump("loc_1384")

    label("loc_137F")

    ClearChrFlags(0x16, 0x8)

    label("loc_1384")

    Return()

    # Function_4_12AB end

    def Function_5_1385(): pass

    label("Function_5_1385")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1544")
    Sound(14, 0, 100, 0)
    OP_71(0x14, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1484")
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xF, 0x0, 0)
    OP_98(0xF, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_13DE():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_13DE)

    def lambda_13F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_13F8)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xF, 1)
    Battle("BattleInfo_58C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1465"),
        (2, "loc_1474"),
        (1, "loc_1481"),
        (SWITCH_DEFAULT, "loc_1484"),
    )


    label("loc_1465")

    SetScenarioFlags(0x74, 6)
    OP_70(0x14, 0x1E)
    Sleep(500)
    Jump("loc_1484")

    label("loc_1474")

    OP_70(0x14, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1481")

    OP_B7(0x0)
    Return()

    label("loc_1484")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x86, 1)"), scpexpr(EXPR_END)), "loc_14DC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_153F")

    label("loc_14DC")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x86),
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

    label("loc_153F")

    Jump("loc_159D")

    label("loc_1544")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Everybody has a plan until they get punched in the chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_159D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1385 end

    def Function_6_15A9(): pass

    label("Function_6_15A9")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1693")
    Sound(14, 0, 100, 0)
    OP_71(0x15, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_1629")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_168E")

    label("loc_1629")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
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

    label("loc_168E")

    Jump("loc_1709")

    label("loc_1693")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Somewhere out there, someone is asking\x01",
            "Rixia to show bobs on the orbal net.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1709")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_15A9 end

    def Function_7_1715(): pass

    label("Function_7_1715")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17FF")
    Sound(14, 0, 100, 0)
    OP_71(0x16, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1795")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_17FA")

    label("loc_1795")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x16, 0x1E, 0x0, 0x0, 0x0)

    label("loc_17FA")

    Jump("loc_183F")

    label("loc_17FF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I wish I were a safe.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_183F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1715 end

    def Function_8_184B(): pass

    label("Function_8_184B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0A")
    Sound(14, 0, 100, 0)
    OP_71(0x17, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_194A")
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x10, 0x0, 0)
    OP_98(0x10, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_18A4():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_18A4)

    def lambda_18BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_18BE)
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
    Battle("BattleInfo_5D0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_192B"),
        (2, "loc_193A"),
        (1, "loc_1947"),
        (SWITCH_DEFAULT, "loc_194A"),
    )


    label("loc_192B")

    SetScenarioFlags(0x74, 7)
    OP_70(0x17, 0x1E)
    Sleep(500)
    Jump("loc_194A")

    label("loc_193A")

    OP_70(0x17, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1947")

    OP_B7(0x0)
    Return()

    label("loc_194A")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E2, 1)"), scpexpr(EXPR_END)), "loc_19A2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5E2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1A05")

    label("loc_19A2")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5E2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x17, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1A05")

    Jump("loc_1A7E")

    label("loc_1A0A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Had it not been for the laws of this autonomous state,\x01",
            "I would have slaughtered you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1A7E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_184B end

    def Function_9_1A8A(): pass

    label("Function_9_1A8A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B1E")
    Jump("loc_1B68")

    label("loc_1B1E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B3E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B68")

    label("loc_1B3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B5E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B68")

    label("loc_1B5E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B68")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_205A")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C6E")

    ChrTalk(
        0x8,
        (
            "#2306FArgh, my head's killing me...\x02\x03",
            "#2310FWhenever I wake up, my keyboard\x01",
            "game is always a little slow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FCome on, Jona. Couldn't you at least\x01",
            "take a bath and step outside for a bit?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2055")

    label("loc_1C6E")


    ChrTalk(
        0x8,
        (
            "#2300FWhat's up with you guys...?\x01",
            "Are you heading out somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, there's something we need to do.\x02\x03",
            "#0005FSay, Jona, is something wrong?\x01",
            "You seem kind of cranky.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DB9")
    Jump("loc_1E03")

    label("loc_1DB9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DD9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E03")

    label("loc_1DD9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DF9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E03")

    label("loc_1DF9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E03")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0x8,
        (
            "#2306FI only woke up moments before you\x01",
            "got here.\x02\x03",
            "Can't you cut me some slack? If you\x01",
            "were half the detectives you claim\x01",
            "to be, you'd be able to tell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F*sigh* What are we going to do with you?\x02\x03",
            "#0001F(It's not like I have any right to tell him what\x01",
            "to do, but he needs to get it together.)\x02\x03",
            "#0003F(Maybe we should contact the\x01",
            "Epstein Foundation after all...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0211FLloyd. You remind me\x01",
            "of a doting guardian.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 750)

    ChrTalk(
        0x101,
        "#0011FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FHeehee. I can see it, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FGeez. You've got real dad energy\x01",
            "these days, man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2055")

    Jump("loc_5037")

    label("loc_205A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_278A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_22CD")

    ChrTalk(
        0x8,
        (
            "#2310FDamn it! You'll regret denying the\x01",
            "genius of Jona Sacred like this!\x01",
            "I won't forget this!\x02\x03",
            "I'm going to gather so much info\x01",
            "that your eyes will burst due to\x01",
            "information overload!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2269")

    ChrTalk(
        0x10A,
        (
            "#0603FKeep your spirit up, kid.\x02\x03",
            "I'll stop by later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2305FHuh?\x02\x03",
            "#2301FWho even are you, old man?!\x01",
            "I don't deal with random strangers,\x01",
            "you know! I have standards!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0600FYou'll understand soon enough.\x01",
            "Get to work, kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(The First Division really knows\x01",
            "their stuff, don't they...?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C8")

    label("loc_2269")


    ChrTalk(
        0x103,
        (
            "#0203F(His pride as an information broker\x01",
            "seems to have been wounded...\x01",
            "Not that I care.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C8")

    Jump("loc_2785")

    label("loc_22CD")

    SetChrSubChip(0x8, 0x0)
    OP_63(0x8, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#2306FGeez, what's your deal? Don't get excited.\x01",
            "I don't have any good info for you today.\x02\x03",
            "Still, the mafia's disputes seem to\x01",
            "be escalating every day.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2430")
    Jump("loc_247A")

    label("loc_2430")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2450")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_247A")

    label("loc_2450")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2470")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_247A")

    label("loc_2470")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_247A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#2305FOh, perfect timing!\x02\x03",
            "#2302FSay, guys. You got any info\x01",
            "you're willing to sell?\x02\x03",
            "#2309FHow 'bout this? I'll buy it for 30 percent\x01",
            "more mira than usual!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    ChrTalk(
        0x101,
        (
            "#0006F*sigh* Looks like this visit was\x01",
            "a waste of our time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108FUnfortunately, it seems so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FFor a kid who acts like he is well informed,\x01",
            "he is pretty disappointing, isn't he?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2697")

    ChrTalk(
        0x10A,
        "#0603FHe doesn't amount to much, yes.\x02",
    )

    CloseMessageWindow()

    label("loc_2697")

    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#2305FWh-What is WRONG with you guys?!\x02\x03",
            "#2307FShut your traps! I'll dive in and\x01",
            "grab whatever info you want!\x02\x03",
            "C'mon, don't hold back!\x01",
            "What do you wanna know?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FKid's got fire. I'll give him that.\x02",
    )

    CloseMessageWindow()
    OP_64(0x8)
    SetScenarioFlags(0xCD, 2)

    label("loc_2785")

    Jump("loc_5037")

    label("loc_278A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_2A07")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_28A5")

    ChrTalk(
        0x8,
        (
            "#2301FSo we got rank A from here to there...\x01",
            "and B starts right around here.\x02\x03",
            "As for rumors involving our friends over\x01",
            "at Revache employing jaegers...\x01",
            "It's fishy, so let's stick that with C.\x02\x03",
            "#2304FNow, which of my regulars\x01",
            "is going to take the bait?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A02")

    label("loc_28A5")


    ChrTalk(
        0x8,
        (
            "#2309FOh, here we go!\x02\x03",
            "All this info on Heiyue\x01",
            "just keeps pouring in!\x02\x03",
            "#2301FNow to rank them by priority\x01",
            "and package everything...\x02\x03",
            "#2309FHehehehe! Easy money!\x02",
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
        "#0006F(Wow. He's really focused.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(We should just leave him be.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2A02")

    Jump("loc_5037")

    label("loc_2A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2E78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2B00")

    ChrTalk(
        0x8,
        (
            "#2305FHey, I was surprised to hear something\x01",
            "crazy like that, too, y'know!\x02\x03",
            "#2303FSince I accidentally spilled the beans,\x01",
            "could we settle on an installment plan?\x02\x03",
            "#2300FC'mon, no need to look so angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FJona...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E73")

    label("loc_2B00")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Jona is stuffing his face with pizza.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#2303F*munch* *crunch*... *slurp*.\x02\x03",
            "#2300FSo, how was Heiyue looking?\x01",
            "Pretty nasty, I bet.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_2C42")

    ChrTalk(
        0x101,
        (
            "#0003FYeah, it wasn't good...\x02\x03",
            "#0001FJona, just so we're clear...\x02\x03",
            "...you aren't going to sell this info\x01",
            "on the orbal network, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2305FU-Uh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CF9")

    label("loc_2C42")


    ChrTalk(
        0x101,
        (
            "#0000FWell, we were just about\x01",
            "to go check it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2306FC'mon, man...\x02\x03",
            "Now's not the time to be chilling here!\x01",
            "Go!\x02\x03",
            "#2300FMy customers don't like waiting for info,\x01",
            "y'know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF9")


    ChrTalk(
        0x104,
        (
            "#0306FSo you're just plannin' to circulate the\x01",
            "details after we work for 'em, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FJona, think very carefully about your response...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2305FUh, well...\x02\x03",
            "#2306FI just wanted to earn back a little mira!\x01",
            "Those information fees are killer! C'mon,\x01",
            "I'm just looking after my livelihood!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106F(This boy hasn't been disciplined\x01",
            "once in his life, has he...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2E73")

    Jump("loc_5037")

    label("loc_2E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_31C5")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 1)), scpexpr(EXPR_END)), "loc_2F1B")

    ChrTalk(
        0x8,
        (
            "#2306FZzz... Mmmnng...\x02\x03",
            "#2311F...*snore* Damn it, Kitty...\x01",
            "I'll never forgive you...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012F(Is Renne still toying with him?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_31C0")

    label("loc_2F1B")


    ChrTalk(
        0x8,
        "#2303FZzz... Mmmnng...\x02",
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
        0x104,
        "#0305FDamn, he's out cold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500FIs this kid the informant\x01",
            "Fran talked about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FYes, as hard as it is to believe. It looks\x01",
            "like we caught him at a bad time, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0206FJona is a night owl, after all.\x02\x03",
            "#0202FIf we wanted, I could\x01",
            "hack his entire system\x01",
            "while he is asleep.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 750)

    ChrTalk(
        0x101,
        (
            "#0005FY-You could...?\x02\x03",
            "#0006FWait! Tio, hacking isn't good!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 750)

    ChrTalk(
        0x103,
        (
            "#0204FIt is not like hacking is a crime yet...\x01",
            "and I do not do it very often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FF-Fair enough.\x02\x03",
            "#0001FStill, only do it when it's necessary,\x01",
            "all right...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCD, 1)

    label("loc_31C0")

    Jump("loc_5037")

    label("loc_31C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_373D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 3)), scpexpr(EXPR_END)), "loc_32D4")

    ChrTalk(
        0x8,
        (
            "#2306FHey, that Schwarze Auction info you scored\x01",
            "me was awesome for my business.\x02\x03",
            "#2301FI'll count this transaction as a freebie, okay?\x01",
            "Don't get used to it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1110FHuh? Why did your face get so red?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2311F#4SGahhhh...! Shuddup, you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3738")

    label("loc_32D4")


    ChrTalk(
        0x153,
        (
            "#1105FHuh? Isn't he that boy that Tio\x01",
            "likes to talk to on the computer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2305FOh, if it isn't the SSS's newest\x01",
            "addition and their head honcho.\x02\x03",
            "#2302FHah, how's the sunlight feel when\x01",
            "you haven't bathed in a week?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FYou're one to talk, Jona.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2304FHey, at least I'm sane! Who in their right mind\x01",
            "would decide to sneak into that auction?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3491")

    ChrTalk(
        0x102,
        (
            "#0101FJona, were you able to find any information\x01",
            "on KeA?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_356D")

    label("loc_3491")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34EF")

    ChrTalk(
        0x103,
        (
            "#0201FQuiet, Jona. Were you able to uncover any\x01",
            "information on KeA?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_356D")

    label("loc_34EF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_356D")

    ChrTalk(
        0x104,
        (
            "#0301FGotta do what you gotta do, Jon-ster.\x01",
            "By the way, were you able to dig up\x01",
            "any information on KeDo?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_356D")


    ChrTalk(
        0x8,
        (
            "#2305FListen, I've tried searching through\x01",
            "every database and source I have\x01",
            "access to.\x02\x03",
            "#2301FBut it's been a bust. There's no\x01",
            "trace of her anywhere on the\x01",
            "orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FI was afraid of that.\x02\x03",
            "#0000FStill, I appreciate all the\x01",
            "help, Jona.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2307FWhoa, don't go thinking that I have a\x01",
            "soft spot for you guys or something...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#2306FSince this was a freebie, you better\x01",
            "bring me even better info next time!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 3)

    label("loc_3738")

    Jump("loc_5037")

    label("loc_373D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3A48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_382A")

    ChrTalk(
        0x8,
        (
            "#2302FWherever you end up, just try to be careful to not\x01",
            "get run over.\x02\x03",
            "Never know what could happen with that massive\x01",
            "crowd outside. The police are making more noise\x01",
            "than usual, too, for some strange reason.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A43")

    label("loc_382A")


    ChrTalk(
        0x8,
        (
            "#2301FHuh? You guys heading out already?\x02\x03",
            "#2305FOh, riiiiight. Today's the last day of\x01",
            "the festival. And that means...it's\x01",
            "time for the Schwarze Auction.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#2309FWell, it's not like you're going there.\x02\x03",
            "#2302FWherever you end up, just try to be\x01",
            "careful and not get run over.\x02\x03",
            "Never know what could happen with\x01",
            "that massive crowd outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FGlad to see you're as\x01",
            "rude as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FI'd rather you worry less about us and\x01",
            "try not to get yourself into trouble on\x01",
            "the orbal network, Jona.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3A43")

    Jump("loc_5037")

    label("loc_3A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3CCC")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3AD2")

    ChrTalk(
        0x8,
        (
            "#2310FPsh, Kitty's probably just as big\x01",
            "a shut-in as me...\x02\x03",
            "There's no way she'd go to\x01",
            "an IRL festival...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CC7")

    label("loc_3AD2")


    ChrTalk(
        0x8,
        (
            "#2310FThat Kitty is a real jerk... She didn't\x01",
            "come online once today! I mean,\x01",
            "what's up with that?!\x02\x03",
            "#2305FN-No way! Did she actually end up\x01",
            "going to see that dumb parade...?!\x02\x03",
            "#2303FWhat am I saying? Kitty's probably\x01",
            "just as big a shut-in as me...\x02\x03",
            "There's no way she'd go to\x01",
            "an IRL festival...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(I don't think I have the whole story,\x01",
            "but I guess Kitty is someone like Jona?\x01",
            "At the very least, Jona thinks she is.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202F(Despite how he acts, Jona tends\x01",
            "to get lonely easily.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3CC7")

    Jump("loc_5037")

    label("loc_3CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_428B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3DAF")

    ChrTalk(
        0x8,
        (
            "#2310FTio Plato! After I defeat Kitty,\x01",
            "you're next!\x02\x03",
            "Remember the name, Jona Sacred!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0205FJona, I see you still have more free\x01",
            "time than you know what to do with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2311FSh-Shut it, Plato!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4286")

    label("loc_3DAF")


    ChrTalk(
        0x101,
        (
            "#0002FHey, Jona. We appreciate the information\x01",
            "you gave us yesterday. It really helped us\x01",
            "out in our investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2309FOf course it did! Especially that stuff\x01",
            "about the Schwarze Auction, I bet.\x02\x03",
            "#2305FYou DID take a good look\x01",
            "at all the data, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FYes. An auction of smuggled goods disguised\x01",
            "as a grand, high society party at Mishelam...\x02\x03",
            "#0101FReading it was a shock, I assure you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2309FHaha, I'm glad ya enjoyed it.\x02\x03",
            "#2304FI was a bit hesitant at first, but I managed\x01",
            "to bag myself a nice source of info.\x02\x03",
            "#2302FHope you guys appreciate me slipping\x01",
            "in those nice tidbits for you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0206FThat explains that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2302FTell me, Tio, how long did that\x01",
            "take you to figure out?\x02\x03",
            "#2309FI wouldn't be surprised if it took you\x01",
            "about an hour, but it's a breeze for\x01",
            "a genius like me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0204FNot even thirty seconds.\x01",
            "Jona, you continue to be as\x01",
            "easy to read as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2307FGah! Th-Thirty seconds...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FJon-ster, buddy. It might be best if you\x01",
            "stopped trying to one-up Tio Tot.\x02\x03",
            "#0300FDoubt it's ever gonna work out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2310FNever! Next time, damn it!\x01",
            "Next time, you're going down...!\x02",
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
    SetScenarioFlags(0x0, 0)

    label("loc_4286")

    Jump("loc_5037")

    label("loc_428B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_455D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4303")

    ChrTalk(
        0x8,
        (
            "#2301FA-Anyway, just hurry on over to\x01",
            "Control Terminal 3, okay?\x02\x03",
            "#2306FTime is running out!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4558")

    label("loc_4303")


    ChrTalk(
        0x8,
        (
            "#2300FThat hacker, Kitty, has been being a\x01",
            "pain in the butt ever since she appeared\x01",
            "on the net over half a year ago.\x02\x03",
            "#2302FBut today, I, the great genius Jona Sacred,\x01",
            "will finally catch Kitty with her tail between\x01",
            "her legs!\x02\x03",
            "#2301FAnyway, Control Terminal 3 is deep\x01",
            "within Geofront's A Sector. You can get there\x01",
            "from Station Street, if you forgot.\x02\x03",
            "C'mon, don't just sit around!\x01",
            "Get a move on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203FJona, your arrogance is showing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FPerhaps it would be best for us to\x01",
            "forget about this favor entirely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2306FI-I'm sorry, okay? I just need\x01",
            "you two to hurry, please...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_4558")

    Jump("loc_5037")

    label("loc_455D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 4)), scpexpr(EXPR_END)), "loc_456E")
    Call(0, 10)
    Jump("loc_5037")

    label("loc_456E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_47A3")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_45ED")

    ChrTalk(
        0x8,
        (
            "#2310FN-No one breaches my system\x01",
            "and gets away with it...\x02\x03",
            "Unacceptable...! *types furiously*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_479E")

    label("loc_45ED")


    ChrTalk(
        0x8,
        (
            "#2311FUgh, this is the last straw!\x02\x03",
            "#2310FI'll show you...! *types furiously*\x02",
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
        0x104,
        "#0305FWhat's got Jon-ster so fired up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0206FWho knows?\x02\x03",
            "#0201FEither way, it is easy to see that\x01",
            "Jona has put on his serious face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FYeah, that much is clear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FHmm, I just hope he's not getting\x01",
            "himself into trouble...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_479E")

    Jump("loc_5037")

    label("loc_47A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4B8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_48C8")

    ChrTalk(
        0x8,
        (
            "#2306FIt might be the Anniversary Festival,\x01",
            "but my regulars are still pestering me\x01",
            "for a bunch of info.\x02\x03",
            "I'm actually in the middle of filling\x01",
            "them in.\x02\x03",
            "#2302FIf anything interesting pops up, I'll\x01",
            "make sure to let you know.\x02\x03",
            "#2309FOnly the unsellable junk, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B8A")

    label("loc_48C8")


    ChrTalk(
        0x8,
        (
            "#2305FHey. You guys need something\x01",
            "from me?\x02\x03",
            "#2302FOr did you get swept up by the festive\x01",
            "mood and decided to stop by out of\x01",
            "the goodness of your hearts?\x02\x03",
            "#2309FHah, IRL stuff is such a pain to deal\x01",
            "with. I'd rather just avoid it, personally.\x02\x03",
            "Besides, the festival has never really\x01",
            "interested me. Don't even think about\x01",
            "trying to drag me outside or something!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FEvery time we stop by, you always\x01",
            "have the same, sour attitude.\x02\x03",
            "#0001FI see you're still hacking without\x01",
            "a care in the world, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0204FUnbelievable. I thought you would be\x01",
            "downcast after being annihilated yesterday.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#2310FDon't act so cocky, Tio Plato!\x01",
            "I'll beat you one of these days!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_4B8A")

    Jump("loc_5037")

    label("loc_4B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EE1")

    ChrTalk(
        0x8,
        (
            "#2305FHey, guys.\x02\x03",
            "#2300FYou were able to break through\x01",
            "those pieces of junk, right?\x02\x03",
            "#2302FYou're not nearly as strong as Yin,\x01",
            "but hey, you aren't too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FJunk...? Are you talking about\x01",
            "those machines?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0211FJona... You had better not say that\x01",
            "you were the one who created them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2306FSorry to disappoint. You know better than\x01",
            "anyone that hardware isn't my specialty.\x02\x03",
            "#2300FAs far as I know, they're just auto-cleaning\x01",
            "prototypes invented by some engineer.\x02\x03",
            "#2302FDunno how they ended up down here, but\x01",
            "when I tried to analyze them for data, they\x01",
            "ended up turning berserk.\x02",
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
        "#0006F(The culprit is revealed...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0211F(Not a huge surprise. Even at the foundation\x01",
            "lab, Jona was nothing but trouble.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x94, 1)
    Jump("loc_5037")

    label("loc_4EE1")


    ChrTalk(
        0x8,
        (
            "#2302FWell, you might be able to beat up some\x01",
            "vacuum cleaners, but you're no match for Yin.\x02\x03",
            "Stargazer's Tower, right? If you're crazy enough\x01",
            "to go, I'd definitely take some time to prepare.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5034")

    ChrTalk(
        0x101,
        "#0006F(It's like he doesn't know how to be nice...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Might as well do that and gear up before\x01",
            "we head to the tower.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5034")

    SetScenarioFlags(0x0, 0)

    label("loc_5037")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_1A8A end

    def Function_10_503F(): pass

    label("Function_10_503F")


    ChrTalk(
        0x8,
        "#3300217V#2305FHuh? Are you ready or what?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Still Have to Take Care of Something\x01",      # 0
            "Good to Go\x01",                                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_50D9"),
        (1, "loc_5171"),
        (SWITCH_DEFAULT, "loc_53D1"),
    )


    label("loc_50D9")


    ChrTalk(
        0x8,
        (
            "#3300218V#2302FHah, if that's the case, why are\x01",
            "you still here?\x02\x03",
            "#3300219VI'll be setting things up while you're\x01",
            "doing whatever you're doing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53D1")

    label("loc_5171")


    ChrTalk(
        0x8,
        (
            "#3300220V#2309FFinally! Let's get this\x01",
            "briefing underway!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3300221V#0100FWell, then, Randy and I will go on and\x01",
            "head to the police department.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        "#3300222V#0300FLloyd. Take care of Tio Tot, all right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#3300223V#0004FYeah, leave her to me.\x02\x03",
            "#3300224V#0000FRandy, don't go leaving\x01",
            "Elie out to dry, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3300225V#0309F*gulp*... C'mooon, I would never\x01",
            "do something like that, buddy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#3300226V#0104FDon't worry. I'll keep an eye on him.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    ChrTalk(
        0x102,
        "#3300227V#0102FTio, work hard!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        "#3300228V#0202FOf course. You, too, Elie.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x28, 0x3E8)
    Sleep(800)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)
    Call(0, 29)

    label("loc_53D1")

    Return()

    # Function_10_503F end

    def Function_11_53D2(): pass

    label("Function_11_53D2")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_551D")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A pizza lies on a cluttered table.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#0006FGeez. I bet his diet consists of 90 percent pizza.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0005FStill, I'm sure we could whip up something\x01",
            "like this with the right ingredients.\x02",
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
            "Learned the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xC)
    Jump("loc_554E")

    label("loc_551D")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A pizza lies on a cluttered table.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_554E")

    TalkEnd(0xFF)
    Return()

    # Function_11_53D2 end

    def Function_12_5552(): pass

    label("Function_12_5552")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5635")
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

    label("loc_5635")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5651")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_5651")

    Return()

    # Function_12_5552 end

    def Function_13_5652(): pass

    label("Function_13_5652")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_5652 end

    def Function_14_566E(): pass

    label("Function_14_566E")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_566E end

    def Function_15_568A(): pass

    label("Function_15_568A")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_568A end

    def Function_16_56A6(): pass

    label("Function_16_56A6")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a water level control valve.\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B93")
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_578A")
    SetChrPos(0x0, 107620, -6000, 200, 0)
    SetChrPos(0x1, 108620, -6000, -600, 0)
    SetChrPos(0x2, 106620, -6000, -600, 0)
    SetChrPos(0x3, 107620, -6000, -1900, 0)
    OP_68(107660, -5000, 850, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28500, 0)
    Jump("loc_5891")

    label("loc_578A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5810")
    SetChrPos(0x0, 85000, -6000, 101000, 0)
    SetChrPos(0x1, 83800, -6000, 101000, 0)
    SetChrPos(0x2, 83800, -6000, 99800, 0)
    SetChrPos(0x3, 85000, -6000, 99800, 0)
    OP_68(84580, -5000, 101000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27000, 0)
    Jump("loc_5891")

    label("loc_5810")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5891")
    SetChrPos(0x0, 201500, -6000, 184020, 90)
    SetChrPos(0x1, 200000, -6000, 184620, 90)
    SetChrPos(0x2, 200000, -6000, 184220, 90)
    SetChrPos(0x3, 198500, -6000, 184020, 90)
    OP_68(201500, -5000, 184020, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33500, 0)

    label("loc_5891")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 6)), scpexpr(EXPR_END)), "loc_5A1C")
    SetMapObjFrame(0xE, "m01gim01", 0x2, "off")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "off")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5935")
    OP_68(102040, -5000, 230, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38000, 0)
    Jump("loc_59B4")

    label("loc_5935")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5977")
    OP_68(99810, -6000, 100090, 0)
    MoveCamera(45, 45, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    Jump("loc_59B4")

    label("loc_5977")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59B4")
    OP_68(200130, -9000, 198310, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42500, 0)

    label("loc_59B4")

    OP_0D()
    Sound(157, 2, 100, 0)
    SetMapObjFrame(0xFF, "null", 0x2, "down")
    Sleep(4000)
    OP_24(0x9D)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    SetBarrier(0x3, 0x8, 0x1)
    SetBarrier(0x2, 0x9, 0x1)
    SetBarrier(0x2, 0xA, 0x1)
    ClearScenarioFlags(0x54, 6)
    Jump("loc_5B93")

    label("loc_5A1C")

    SetMapObjFrame(0xE, "m01gim01", 0x2, "on")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "on")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AB3")
    OP_68(102040, -5000, 230, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38000, 0)
    Jump("loc_5B32")

    label("loc_5AB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AF5")
    OP_68(99810, -6000, 100090, 0)
    MoveCamera(45, 45, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    Jump("loc_5B32")

    label("loc_5AF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B32")
    OP_68(200130, -9000, 198310, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42500, 0)

    label("loc_5B32")

    OP_0D()
    Sound(157, 2, 100, 0)
    SetMapObjFrame(0xFF, "null", 0x2, "up")
    Sleep(4000)
    OP_24(0x9D)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    SetBarrier(0x2, 0x8, 0x1)
    SetBarrier(0x3, 0x9, 0x1)
    SetBarrier(0x3, 0xA, 0x1)
    SetScenarioFlags(0x54, 6)

    label("loc_5B93")

    Return()

    # Function_16_56A6 end

    def Function_17_5B94(): pass

    label("Function_17_5B94")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D13")
    Fade(500)
    SetChrPos(0x0, 600, 0, 600, 90)
    SetChrPos(0x1, 600, 0, -600, 90)
    SetChrPos(0x2, -600, 0, -600, 90)
    SetChrPos(0x3, -600, 0, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C73")
    SetChrPos(0x4, -1800, 0, -600, 90)
    SetChrPos(0x5, -1800, 0, 600, 90)
    Jump("loc_5C92")

    label("loc_5C73")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C92")
    SetChrPos(0x4, -1800, 0, 0, 90)

    label("loc_5C92")

    OP_68(600, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(600, 6000, 0, 3000)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0100", 0, 0, 0)
    IdleLoop()

    label("loc_5D13")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_17_5B94 end

    def Function_18_5D1B(): pass

    label("Function_18_5D1B")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(600, 11000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, 30000, 600, 90)
    OP_90(0x1, 600, 30000, -600, 90)
    OP_90(0x2, -600, 30000, -600, 90)
    OP_90(0x3, -600, 30000, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DEE")
    OP_90(0x4, -1800, 0, -600, 90)
    OP_90(0x5, -1800, 0, 600, 90)
    Jump("loc_5E0D")

    label("loc_5DEE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E0D")
    OP_90(0x4, -1800, 0, 0, 90)

    label("loc_5E0D")

    Sound(145, 0, 100, 0)
    OP_68(600, 1000, 0, 3000)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x11)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_18_5D1B end

    def Function_19_5E62(): pass

    label("Function_19_5E62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EE7")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Peer Inside]\x01",      # 0
            "[Do Not]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5EC3"),
        (1, "loc_5EE0"),
        (SWITCH_DEFAULT, "loc_5EE5"),
    )


    label("loc_5EC3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x13, 0x10)
    OP_65(0x4, 0x1)
    Call(0, 23)
    Jump("loc_5EE5")

    label("loc_5EE0")

    Jump("loc_5EE5")

    label("loc_5EE5")

    EventEnd(0x3)

    label("loc_5EE7")

    Return()

    # Function_19_5E62 end

    def Function_20_5EE8(): pass

    label("Function_20_5EE8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    OP_68(498200, 1000, 302000, 0)
    MoveCamera(0, 25, 0, 0)
    MoveCamera(0, 14, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(16500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 498200, 200, 302000, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02300.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis122.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis154.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis123.itp")
    OP_C9(0x0, 0x4, 0x0, 0x0, 0x0)
    Sound(850, 0, 90, 0)
    Sleep(1500)
    PlayBGM("ed7521", 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100163VLet's see here... A list of major Imperial\x01",
            "investment enterprises...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        "#2100164VSpeculation from Calvardian assets...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2100165VSales reports of the three largest pharma\x01",
            "companies in Remiferia...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2100166VAnd Liberl...? Ah, the delivery destination\x01",
            "of the newest orbal engine model.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2100167VOh, I love you, Crossbell. Information\x01",
            "just flows into my open hands.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Freckled Boy")

    AnonymousTalk(
        0xFF,
        (
            "#2100168VHehe. A good haul, I'd say! ♪\x02\x03",
            "#2100169VThis job was a walk in the park.\x02\x03",
            "A proper search of the database was\x01",
            "#2100170Vall I needed to fish up that info\x01",
            "my client wanted!\x02\x03",
            "#2100171VSince those idiots running the net\x01",
            "don't realize how important security\x01",
            "is, I can do whatever I want online.\x02\x03",
            "#2100172VPhew, life's a breeze. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    SetCameraDistance(18000, 3000)
    OP_68(498200, 900, 302000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    Sound(857, 0, 100, 0)
    Sleep(2000)
    OP_63(0x8, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x2)
    Sleep(300)

    NpcTalk(
        0x8,
        "Freckled Boy",
        (
            "#2100173V#5P#2310FYuck... Cold pizza? I'd rather die.\x02\x03",
            "#2100174V#2302FYou know what they say: Information\x01",
            "and pizza are both best served hot.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)

    NpcTalk(
        0x8,
        "Freckled Boy",
        (
            "#2100175V#5P#2304FLet's see... Any farther and I'll\x01",
            "be in a private network.\x02\x03",
            "#2100176VMaybe I should just hack the IBC's\x01",
            "main terminal... That should give\x01",
            "me some hints on Kitty's identity.\x02\x03",
            "#2100177V#2302FWhew, I love my life.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(824, 0, 100, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Freckled Boy",
        "#2100178V#6P#2305FHuh? An orbmail...?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    FadeToDark(0, 0, -1)
    Sleep(500)
    SetChrName("Freckled Boy")

    AnonymousTalk(
        0xFF,
        (
            "#2100179V#2301F'Dear Mr. Jona Sacred...'\x02\x03",
            "#2100180V'Placing my trust in your skill, there's\x01",
            "a matter I'd like to discuss with you...'\x02\x03",
            "#2100181V#2305FWhoa, where's the source of this...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(849, 0, 100, 0)
    Sleep(800)
    SetChrName("Freckled Boy")

    AnonymousTalk(
        0xFF,
        (
            "#2100182V#2301FDefinitely coming from a strong\x01",
            "terminal somewhere.\x02\x03",
            "#2100183VIt was redirected from the Harbor District?\x02\x03",
            "#2100184V#2305F#30W...\x02\x03",
            "#2100185V#40WHeiyue Trading...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 21)
    SetChrName("Freckled Boy")

    AnonymousTalk(
        0xFF,
        "#2100186V#2309F#4SYEAH...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(0, 0)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(500)

    NpcTalk(
        0x8,
        "Freckled Boy",
        (
            "#2100187V#6P#2304FYin, huh?\x02\x03",
            "#2100188V#2302FHahaha! Things are starting to heat\x01",
            "up, aren't they? Just how I like it!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x101, 3)
    StopBGM(0xFA0)
    WaitBGM()
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_57(0x3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_E3(0xB)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 5)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_5EE8 end

    def Function_21_6910(): pass

    label("Function_21_6910")

    OP_C9(0x3, 0x0, 0x4B0, 0xFFFFFBB4, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0x640, 0xFFFFFB50, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1)
    OP_CA(0x0, 0xFF, 0x0)
    Return()

    # Function_21_6910 end

    def Function_22_696C(): pass

    label("Function_22_696C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(490300, 1000, 199800, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 491000, 0, 200300, 90)
    SetChrPos(0x102, 491000, 0, 199300, 90)
    SetChrPos(0x103, 489600, 0, 199300, 90)
    SetChrPos(0x104, 489600, 0, 200300, 90)
    FadeToBright(1000, 0)
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
        "#2200842V#0005F(There's music playing...)\x02",
    )

    CloseMessageWindow()
    OP_68(499600, 1000, 204800, 2000)
    OP_6F(0x1)

    def lambda_6AA9():
        OP_96(0xFE, 0x7A2B0, 0x0, 0x316A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AA9)
    Sleep(50)

    def lambda_6AC6():
        OP_96(0xFE, 0x7A2B0, 0x0, 0x312B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6AC6)
    Sleep(50)

    def lambda_6AE3():
        OP_96(0xFE, 0x79D38, 0x0, 0x316A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6AE3)
    Sleep(50)

    def lambda_6B00():
        OP_96(0xFE, 0x79D38, 0x0, 0x312B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B00)
    WaitChrThread(0x101, 1)

    def lambda_6B1E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6B1E)
    WaitChrThread(0x102, 1)

    def lambda_6B2F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6B2F)
    WaitChrThread(0x103, 1)

    def lambda_6B40():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6B40)
    WaitChrThread(0x104, 1)

    def lambda_6B51():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6B51)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x104,
        (
            "#2200843V#12P#0301F(I doubt some random radio\x01",
            "turned on all by itself.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200844V#4P#0203F(Control Terminal 8 should\x01",
            "be right past this door...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200845V#4P#0101F(Does that mean the Yin that hacked the\x01",
            "IBC is past there, too?)\x02",
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

    def lambda_6CAC():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6CAC)
    Sleep(50)

    def lambda_6CBC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6CBC)
    Sleep(50)

    def lambda_6CCC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6CCC)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2200846V#0003F#5P(It's possible. Let's take a closer look...)\x02\x03",
            "#2200847V#0001F(Yin might be inside. Stay alert, everyone.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200848V#4P#0101F(Right!)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 499600, 0, 202400, 0)
    ClearMapObjFlags(0x13, 0x10)
    OP_66(0x4, 0x1)
    SetScenarioFlags(0x83, 5)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_22_696C end

    def Function_23_6D9E(): pass

    label("Function_23_6D9E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis034.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02300.itp")
    OP_68(498200, 900, 302000, 0)
    MoveCamera(25, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 499800, 150, 207400, 0)
    SetChrPos(0x102, 500500, 150, 206700, 0)
    SetChrPos(0x103, 499400, 0, 206200, 0)
    SetChrPos(0x104, 500200, 0, 205600, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 498200, 200, 302000, 0)
    ClearMapObjFlags(0x13, 0x10)
    OP_70(0x13, 0x1)
    SetMapFlags(0x2000)
    SetMapFlags(0x8000000)
    OP_E0(0x0)
    VolumeBGM(0x64, 0x3E8)
    SetCameraDistance(21500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("Freckled Boy")

    AnonymousTalk(
        0xFF,
        (
            "#2200849VNext up... How about I earn a little bit of\x01",
            "pocket change? What's waiting for me...?\x02\x03",
            "#2200850VFirst, we've got specs on the new\x01",
            "Reinford Company train? Neat.\x02\x03",
            "#2200851VHmm, what's this? Specs on the\x01",
            "new Verne Company sportscar?\x02\x03",
            "#2200852VWhoa, ZCF is developing a brand new\x01",
            "model of airship liners?\x02\x03",
            "#2200853VBetween this and the Orbal Gear, they're\x01",
            "not missing a beat.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    VolumeBGM(0x28, 0x3E8)
    Fade(500)
    OP_68(499800, 1000, 207900, 0)
    MoveCamera(36, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
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
        0x101,
        "#2200854V#11P#0005F(Is this really...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200855V#0105F(I may be wrong, but this voice\x01",
            "doesn't really strike me as Yin...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200856V#4P#0301F(Is that a freakin' kid?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200857V#12P#0206F(I should have known...)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    VolumeBGM(0x64, 0x3E8)
    Fade(500)
    OP_68(498200, 900, 302000, 0)
    MoveCamera(25, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0x8,
        "Freckled Boy",
        (
            "#2200858V#12P#2304FYin sure was generous with this\x01",
            "ginormous argem crystal.\x02\x03",
            "#2200859VHeck, this might fetch me ten thousand mira!\x02\x03",
            "#2200860V#2302FHeh, I'll go exchange this at Neinvalli\x01",
            "sometime tomorrow.\x02\x03",
            "#2200861VMaybe that'll be enough for me to get\x01",
            "those parts from Guillaume.\x02",
        )
    )

    CloseMessageWindow()
    Sound(850, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Freckled Boy",
        (
            "#2200862V#12P#2309FStill, Yin really likes to ask for the impossible.\x02\x03",
            "#2200863VI was able to send the orbmail, but I doubt\x01",
            "anyone could trace it back to me.\x02\x03",
            "#2200864V#2302FOh, what am I saying? No one in Zemuria is\x01",
            "capable of tracing down the great Jona!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 500000, 0, 294300, 0)
    SetChrPos(0x102, 501000, 0, 294300, 0)
    SetChrPos(0x103, 500000, 0, 293300, 0)
    SetChrPos(0x104, 501000, 0, 293300, 0)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#2200865VIs that so?\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x20)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(499400, 900, 301200, 2500)
    MoveCamera(11, 15, 0, 2500)
    BeginChrThread(0x101, 3, 0, 24)
    Sleep(1000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)

    def lambda_7580():
        OP_96(0xFE, 0x79AE0, 0xC8, 0x49AE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7580)

    def lambda_759A():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_759A)
    Sound(820, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)

    NpcTalk(
        0x8,
        "Freckled Boy",
        "#2200866V#5P#2305FWho's there?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#2200867V#0001F#6PI'm hesitant to admit it, but I'm\x01",
            "guessing we found our hacker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200868V#4P#0301FWhat the hell... He really\x01",
            "is just a kid, eh?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Freckled Boy",
        "#2200869V#5P#2305FWh-Who are you people?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Freckled Boy",
        (
            "#2200870V#5P#2307FW-Wait! Are you that Special Support\x01",
            "Section Yin was yammering about?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200871V#0003F#6PYep. Nice to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200872V#0101FSo Yin is an acquaintance of\x01",
            "yours, then?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Freckled Boy",
        (
            "#2200873V#5P#2310FWh-What?! This can't be happening...\x02\x03",
            "#2200874VSome dumb cops were able to track\x01",
            "down a genius like myself...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200875V#12P#0206FYou are the same as ever...Jona Sacred.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#2200876V#5P#2305FTio Plato?!\x02\x03",
            "#2200877VWhat are YOU doing here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200878V#12P#0203FThat is my line.\x02\x03",
            "#2200879V#0211FYou were the one who ran away from the\x01",
            "foundation, you know. How did you end up\x01",
            "in a dark place like this?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_79A8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_79A8)
    Sleep(50)

    def lambda_79B8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_79B8)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#2200880V#5P#0011FTio, you know this kid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200881V#12P#0203FWe both worked in the same Epstein Foundation\x01",
            "research laboratory.\x02\x03",
            "#2200882V#0200FOur specialties are on two opposite ends of the\x01",
            "spectrum, so it is not like we know each other\x01",
            "that well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200883V#5P#2310FDamn it, I forgot...\x02\x03",
            "#2200884VIf you used that stupid system of yours,\x01",
            "you could probably trace the orbmail...\x02\x03",
            "#2200885V#2311FAh, man! If I knew Tio freaking Plato was\x01",
            "here, I would have been more careful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200886V#12P#0204FCareless as always, Jona.\x02\x03",
            "#2200887V#0211FYou ARE aware of how much your mischief\x01",
            "cost the foundation, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2200888V#5P#2301FSh-Shut up. I don't want to hear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200889V#0305FHmm? This dude hurt the foundation?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#2200890V#6P#0206FYes. At a young age, Jona undertook special\x01",
            "training as a systems engineer at one of the\x01",
            "foundation's research labs.\x02\x03",
            "#2200891VDuring one of his foul pranks, he managed\x01",
            "to ruin an important experiment, from which\x01",
            "the foundation suffered heavy losses.\x02\x03",
            "#2200892V#0211FThen, unhappy that the others were rightfully\x01",
            "angry at him, he packed up and ran away.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2200893V#5P#0001FA-Are you serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200894V#5P#0106F*sigh* For some strange reason,\x01",
            "that story doesn't surprise me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200895V#0306FWhew, so he's just as big of a\x01",
            "brat as he looks, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200896V#5P#2310FD-Damn you... Keep talking, if it\x01",
            "makes you feel better!\x02\x03",
            "#2200897V#2307FTio Plato! You aren't planning on\x01",
            "ratting me out to the foundation,\x01",
            "are you?!\x02\x03",
            "#2200898VIf you do, I'll post all your most\x01",
            "embarrassing secrets all over the net!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#2200899V#12P#0204FPlease, go ahead.\x02\x03",
            "#2200900V#0202FTo my knowledge, I do not have any\x01",
            "particularly embarrassing secrets.\x02\x03",
            "#2200901VEven if there were any, they would\x01",
            "be nearly impossible to discover.\x02\x03",
            "#2200902V#0204FNot to mention that I could easily eradicate\x01",
            "them even if you somehow posted them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2200903V#5P#2310FC-Curse you!\x02",
    )

    CloseMessageWindow()

    def lambda_81B5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_81B5)
    Sleep(50)

    def lambda_81C5():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_81C5)
    Sleep(50)

    def lambda_81D5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_81D5)
    Sleep(300)

    ChrTalk(
        0x102,
        "#2200904V#0102FHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200905V#4P#0304FHaha, looks like Tio Tot's a step ahead\x01",
            "of you at every turn, kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200906V#0001F#6PSo, your name is Jona, right?\x02\x03",
            "#2200907VWhy in the world are you holed\x01",
            "up here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200908V#5P#2301FShuddup. I have no obligation\x01",
            "to tell you anyth--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200909V#12P#0201FJona. Answer him.\x02\x03",
            "#2200910VWe managed to trace you to this\x01",
            "dump, so you have already lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200911V#5P#2310FUgh... Fine.\x02\x03",
            "#2200912V#2306FRight now, I'm working as an\x01",
            "informant in Crossbell State.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2200913V#0005F#6PInformant?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200914V#4P#0301FWhoa, now... Can't say a job like\x01",
            "that suits a kid like yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200915V#5P#2304FNowadays, being an informant\x01",
            "has nothing to do with age!\x02\x03",
            "#2200916V#2302FAnyway, I've built up quite a few\x01",
            "contacts in Crossbell.\x02\x03",
            "#2200917VI got info from Erebonia, Calvard, Liberl,\x01",
            "Remiferia, Leman State, to Arteria...you name it!\x02\x03",
            "#2200918VOn top of that, I got some insiders in a ton\x01",
            "of international companies and businesses!\x02\x03",
            "#2200919VAll thanks to the power and greatness\x01",
            "of the orbal network.\x02\x03",
            "#2200920V#2309FSince security surrounding the net is so weak,\x01",
            "all that delicious info is mine for the taking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200921V#0105FU-Unbelievable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200922V#0013F#6PThat HAS to be illegal, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200923V#12P#0206FUnfortunately not. Due to the orbal network\x01",
            "still being in its experimental phase, no laws\x01",
            "criminalizing hacking have been made.\x02\x03",
            "#2200924V#0200FBut I imagine it is only a matter of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200925V#5P#2304FEh, Crossbell's been pretty laid-back\x01",
            "regarding this kinda stuff.\x02\x03",
            "#2200926VAfter I got fed up with that foundation lab,\x01",
            "I set up shop here as an informant.\x02\x03",
            "#2200927V#2302FHehe, I get tons of regulars,\x01",
            "and I'm making bank!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200928V#4P#0306FGood grief. You really think you got the\x01",
            "world in the palm of your hand, don'tcha?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200929V#12P#0204FThen again, you seemed as if you were\x01",
            "unaware of my temporary transfer to the\x01",
            "police.\x02\x03",
            "#2200930V#0202FSome informant you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200931V#5P#2306FGimme a break, Plato!\x02\x03",
            "#2200932V#2310FIt's not like I know every nook and\x01",
            "cranny of Crossbell yet! Geez!\x02\x03",
            "#2200933VKitty keeps me busy enough as is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200934V#12P#0205FKitty?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200935V#5P#2305FI-Ignore that. Just thinking out loud.\x02\x03",
            "#2200936V#2301FWait, there's no way... You aren't\x01",
            "Kitty, are you?\x02\x03",
            "#2200937VWhen did you arrive in Crossbell?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200938V#12P#0206FI do not quite understand the question...\x02\x03",
            "#2200939V#0200F...but I transferred to Crossbell around\x01",
            "two months ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200940V#5P#2306FPhew, that's a relief. Well, to be fair,\x01",
            "your hacking style is way different\x01",
            "from Kitty's, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200941V#12P#0205F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200942V#0003F#6PNot quite sure what that was about, but...\x02\x03",
            "#2200943V#0013FIt's about time you answered my question.\x01",
            "What is your relationship with Yin?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#2200944V#5P#2300F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200945V#0001F#6PYou admitted to sending the orbal\x01",
            "mail earlier, right?\x02\x03",
            "#2200946VWhat for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2200947V#5P#2304FHmph, whatever.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrPos(0x8, 498600, 200, 301100, 150)
    ClearChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()

    def lambda_8E1B():
        OP_96(0xFE, 0x79EC8, 0x0, 0x493E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8E1B)
    WaitChrThread(0x8, 1)
    Sleep(300)

    ChrTalk(
        0x8,
        "#2200948V#2300F#5PHere, take this.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x325),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x325, 1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(300)
    SetMessageWindowPos(-1, 130, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "The door has been opened. I summon you\x01",
            "to challenge me at the Tower of the Stars\x01",
            "and hear my wish.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
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
        "#2200949V#0005F#6PNo way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200950V#0101FA message from Yin?!\x02",
    )

    CloseMessageWindow()

    def lambda_9036():
        OP_96(0xFE, 0x79BA8, 0xC8, 0x4982C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9036)
    WaitChrThread(0x8, 1)
    Fade(250)
    SetChrPos(0x8, 498400, 200, 301800, 90)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x2)
    Sound(820, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#2200951V#5P#2300FA request, too, apparently.\x02\x03",
            "#2200952VI was told to send the orbmail to the SSS,\x01",
            "then give you that card if you actually\x01",
            "made it here.\x02\x03",
            "#2200953V#2306FStill, I can't believe you were\x01",
            "actually able to find me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200954V#4P#0304FHuh, so that's how it is.\x02\x03",
            "#2200955V#0305FYou must've met Yin more\x01",
            "than once then, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200956V#5P#2300FYup, he's one of my regular customers.\x02\x03",
            "#2200957VEvery so often, he stops by to buy all\x01",
            "sorts of info from me.\x02\x03",
            "#2200958V#2306FThough, this is the first time he's asked\x01",
            "for something as strange as this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200959V#0001F#6PSo Yin's been here before...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200960V#12P#0201FCan you give us a description of him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200961V#5P#2300FKinda. He always wears black and covers\x01",
            "his face with a mask. Not very helpful, I know.\x02\x03",
            "#2200962V#2302FBut, from what I understand, he's some crazy\x01",
            "assassin from Calvard's Eastern Quarter.\x02\x03",
            "#2200963V#2309FHow sick is that?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2200964V#0011F#6PSick is one way to describe him, I guess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200965V#4P#0306FOh, boy. Our youngster here is\x01",
            "fearless, isn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200966V#0108FRegardless, Yin seems to be inviting\x01",
            "us to meet him at the tower.\x02\x03",
            "#2200967V#0101FBased on that letter, I can only assume\x01",
            "that there's something he'd like to discuss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200968V#5P#2300FLooks that way, doesn't it?\x02\x03",
            "#2200969VDunno what business he has with you\x01",
            "guys, but I know he's trying to test you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200970V#0013F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200971V#4P#0302FSounds like we've got a jokester on our\x01",
            "hands, doublin' as an assassin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200972V#6P#0201FWhat exactly is this 'Tower of the Stars'\x01",
            "that he mentioned?\x02\x03",
            "#2200973VIs it some sort of metaphor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200974V#0008F#5PThe Tower of the Stars... Something about\x01",
            "that sounds eerily familiar.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#2200975V#0105FHold on a second...\x02\x03",
            "#2200976V#0101FCould he be referring to Stargazer's Tower?\x01",
            "You know, on the southern outskirts of Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_984B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_984B)
    Sleep(50)

    def lambda_985B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_985B)
    Sleep(50)

    def lambda_986B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_986B)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#2200977V#5P#0005FOh, that's right...\x02\x03",
            "#2200978V#0001FIt's that tower from the Middle Ages that\x01",
            "we saw near Ursula Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200979V#4P#0306FWhy the hell did he choose a place\x01",
            "like that for our rendezvous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200980V#0103FI don't know, but it's our only lead.\x02\x03",
            "#2200981V#0101FAt this point, all we can do is go\x01",
            "there and investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200982V#5P#0004FYeah, I agree.\x02\x03",
            "#2200983V#0000FOnce we're ready, let's head out\x01",
            "the south exit toward the tower.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9A4D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9A4D)
    Sleep(50)

    def lambda_9A5D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A5D)

    def lambda_9A6A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9A6A)
    Sleep(50)

    def lambda_9A7A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9A7A)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#2200984V#4P#0301FThe problem still remains... What\x01",
            "are we gonna do with this kid?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#2200985V#5P#2305FH-Hey, now... You don't need me\x01",
            "for anything else, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200986V#0001F#6PListen, Jona. The Geofront is official\x01",
            "Crossbell City property.\x02\x03",
            "#2200987VThis is trespassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200988V#5P#2310FG-Geez! Sorry for using space that\x01",
            "was just going to fill up with dust.\x02\x03",
            "#2200989V#2307FBesides, there's no law saying you CAN'T\x01",
            "use the Geofront for personal reasons,\x01",
            "is there?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200990V#0003F#6PYou're just splitting hairs now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200991V#0106FIsn't living in a place like this dangerous,\x01",
            "Jona?\x02\x03",
            "#2200992V#0101FThere are monsters wandering about,\x01",
            "and don't get me started on your diet...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(498400, 900, 300530, 1200)

    def lambda_9D8D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9D8D)
    Sleep(200)

    def lambda_9D9D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9D9D)
    Sleep(50)

    def lambda_9DAD():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9DAD)
    Sleep(50)

    def lambda_9DBD():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9DBD)
    OP_6F(0x1)

    ChrTalk(
        0x103,
        (
            "#2200993V#11P#0211FIndeed. It is nothing but pizza boxes\x01",
            "as far as the eye can see.\x02\x03",
            "#2200994V#0205FAre you having someone deliver them\x01",
            "all the way down here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200995V#5P#2304FOf course not! I'm not stupid.\x02\x03",
            "#2200996V#2302FI just have them delivered\x01",
            "outside the Geofront door.\x02\x03",
            "#2200997VThere's a ventilation duct near\x01",
            "here that leads right to the\x01",
            "entrance, so it works out.\x02\x03",
            "#2200998V#2309FSee, that's my secret to traveling\x01",
            "through here safely! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200999V#2P#0306FThis guy's a lost cause...\x01",
            "A true shut-in, through and through.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(499400, 900, 301200, 1000)

    def lambda_A001():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A001)
    Sleep(50)

    def lambda_A011():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A011)
    Sleep(50)

    def lambda_A021():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A021)
    Sleep(50)
    OP_93(0x104, 0x10E, 0x190)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#2201000V#0006F#6PWell, we're busy right now, so we'll\x01",
            "overlook this for now.\x02\x03",
            "#2201001V#0001FTry not to overdo it, okay?\x02\x03",
            "#2201002VYou can make a lot of enemies in this\x01",
            "line of work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201003V#0106FYes, please be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2201004V#5P#2304FHah! I'm shaking in my boots!\x02\x03",
            "#2201005V#2302FStill, if there's info you need to get your\x01",
            "hands on, you know who to call.\x02\x03",
            "#2201006VPrice isn't cheap, though.\x02\x03",
            "#2201007V#2309FI doubt rookie police officers like you\x01",
            "guys could afford my services, honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201008V#0013F#6PJonaaaa...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#2201009V#6P#0202FDo not worry, Lloyd.\x02\x03",
            "#2201010V#0204FIf worst comes to worst, I can simply hack\x01",
            "this entire place and find us the necessary\x01",
            "information.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#2201011V#5P#4S#2310FHey!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(21750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x8, 498200, 200, 302000, 0)
    SetChrSubChip(0x8, 0x0)
    OP_68(500600, 1000, 296300, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33000, 0)
    SetChrPos(0x0, 500600, 0, 296300, 180)
    SetChrPos(0x1, 500600, 0, 296300, 180)
    SetChrPos(0x2, 500600, 0, 296300, 180)
    SetChrPos(0x3, 500600, 0, 296300, 180)
    OP_70(0x13, 0x0)
    SetMapObjFlags(0x13, 0x10)
    SetScenarioFlags(0x83, 6)
    OP_29(0x43, 0x1, 0x7)
    Sleep(500)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_23_6D9E end

    def Function_24_A3F4(): pass

    label("Function_24_A3F4")


    def lambda_A3F9():
        OP_96(0xFE, 0x7A058, 0x0, 0x48FF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A3F9)
    Sleep(400)

    def lambda_A416():
        OP_96(0xFE, 0x7A440, 0x0, 0x49188, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A416)
    Sleep(400)

    def lambda_A433():
        OP_96(0xFE, 0x7A058, 0x0, 0x48AE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A433)
    Sleep(400)

    def lambda_A450():
        OP_96(0xFE, 0x7A5D0, 0x0, 0x48DA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A450)
    WaitChrThread(0x101, 1)

    def lambda_A46E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A46E)
    WaitChrThread(0x102, 1)

    def lambda_A47F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A47F)
    WaitChrThread(0x103, 1)

    def lambda_A490():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A490)
    WaitChrThread(0x104, 1)

    def lambda_A4A1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A4A1)
    WaitChrThread(0x104, 2)
    Return()

    # Function_24_A3F4 end

    def Function_25_A4AE(): pass

    label("Function_25_A4AE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50090.itc", 0x22)
    OP_68(498200, 900, 302000, 0)
    MoveCamera(25, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 498200, 200, 302000, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02300.itp")
    SetCameraDistance(21500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    SetChrFlags(0x8, 0x20)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A58D():
        OP_96(0xFE, 0x79AE0, 0xC8, 0x49AE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A58D)

    def lambda_A5A7():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A5A7)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)

    ChrTalk(
        0x8,
        "#3300108V#2302FOh, nice of you to stop by.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x103, 500000, 0, 294300, 0)
    SetChrPos(0x102, 501000, 0, 294300, 0)
    SetChrPos(0x101, 500000, 0, 293300, 0)
    SetChrPos(0x104, 501000, 0, 293300, 0)
    OP_68(499400, 900, 301200, 2500)
    MoveCamera(11, 15, 0, 2500)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(2000)
    Fade(250)
    SetChrPos(0x8, 498600, 200, 301100, 150)
    ClearChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    OP_92(0x8, 0x79EC8, 0x493E0, 0x0)
    OP_0D()

    def lambda_A695():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A695)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        "#3300109V#12P#0001F'Nice of you to stop by,' he says...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300110V#0200FI assume you need my help with\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x8,
        (
            "#3300111VAh, well, y'see...\x02\x03",
            "#3300112VI kinda need a little bit of\x01",
            "help with some hacking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_93(0x103, 0xA0, 0x1F4)

    ChrTalk(
        0x103,
        "#3300113V#5P#0203FGoodbye.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#3300114V#2307F#5PW-Wait a sec!\x02\x03",
            "#3300115VWhy are you just leaving?!\x01",
            "You didn't even hear me out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300116V#12P#0006FIsn't it obvious, Jona...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3300117V#4P#0301FSheesh, this kid's a comedian.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3300118V#0106FAsking the police to assist in a crime\x01",
            "is brave, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300119V#2301F#5PI told you guys before! Hacking\x01",
            "is NOT a crime!\x02\x03",
            "#3300120VI'm not trying to wage war against the\x01",
            "IBC or something! I promise!\x02\x03",
            "#3300121VI'm just trying to get the jump on\x01",
            "my most fearsome rival yet!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x103, 0x8, 500)

    ChrTalk(
        0x103,
        "#3300122V#0200FFearsome rival? Explain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300123V#2302F#5POoh, looks like you took the bait.\x02\x03",
            "#3300124V#2303FC'mon, won't you at least hear\x01",
            "me out?\x02\x03",
            "#3300125V#2300FI have a gut feeling that you guys\x01",
            "will want to hear about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300213V#0203F...Fine.\x02\x03",
            "#3300127V#0211FIf this ends up being boring, prepare\x01",
            "for a world of hurt, Jona Sacred.\x02\x03",
            "#3300128VI will 20-chain combo you in Pom Party\x01",
            "or something equally frightening.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#3300129V#2306F#5PThat would be pretty freaking bad.\x01",
            "You're ruthless, Tio...\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_68(496800, 1400, 296600, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 495000, 200, 296300, 90)
    SetChrPos(0x102, 495000, 200, 295400, 90)
    SetChrPos(0x103, 497700, 200, 295400, 270)
    SetChrPos(0x104, 495000, 200, 297200, 90)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 497700, 200, 296600, 270)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x18)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 495850, 250, 296400, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x18)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 495850, 250, 295900, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x22)
    SetChrSubChip(0xB, 0x18)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 495850, 250, 296900, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x18)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 496850, 250, 296400, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x22)
    SetChrSubChip(0xD, 0x18)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 496850, 250, 295900, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetMapObjFrame(0xFF, "pizza", 0x0, 0x1)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x103,
        "#3300130V#0205FKitty...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    OP_68(496800, 900, 296600, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3300131V#6P#0001FCute name, but is this hacker even real?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300132V#11P#2303FWhy would I lie about this?\x02\x03",
            "#3300133V#2301FI first encountered her about half\x01",
            "a year ago...\x02\x03",
            "#3300134VI was busy hacking a few companies,\x01",
            "like usual, and then I realized that\x01",
            "someone was tracing me.\x02\x03",
            "#3300135V#2306FOf course, I was kinda flustered, so I\x01",
            "cut off my infiltration route, covered\x01",
            "my tracks, and managed to escape...\x02\x03",
            "#3300136VAfter that, as if to taunt me, she sent\x01",
            "me a little greeting and her online\x01",
            "handle, Kitty!\x02\x03",
            "#3300137V#2310FEver since that fateful day, she's been\x01",
            "screwing around with my business!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300138V#6P#0006FO-Okay, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3300139V#6P#0101FAccording to all the reports I've read, hackers\x01",
            "are extremely rare...\x02\x03",
            "#3300140VIs there really another hacker in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300141V#11P#2303FYeah, I'm positive!\x02\x03",
            "#3300142V#2307FEven I thought it was some fluke\x01",
            "at first!\x02\x03",
            "#3300143VTo think there's another hacker in the\x01",
            "city who's on the same level as my\x01",
            "genius...! It pisses me off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300144V#11P#0211FSame level? From what I am hearing,\x01",
            "this Kitty is far more skilled than you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x8, 0x0, 0xF, 0x1F4, 0xBB8)
    Sleep(150)

    ChrTalk(
        0x8,
        "#3300145V#11P#2310FUgh, c'mon...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300146V#11P#0204FIt is okay, Jona. After all, your specialty was\x01",
            "always in system languages, not hacking.\x02\x03",
            "#3300147V#0202FYou may have lost this fight, but perhaps\x01",
            "you can still win the war.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x8,
        (
            "#3300148V#5P#2307FKill the pity party, Tio!\x02\x03",
            "#3300149V#2310FBack to the subject at hand!\x01",
            "I want my revenge!\x02\x03",
            "#3300150VOnce I uncover her location,\x01",
            "I'm gonna seize her access point!\x02\x03",
            "#3300151VAnd you're gonna help me, Tio!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300152V#11P#0203FHmmm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#3300153V#11P#0201FCan you guarantee that Kitty will\x01",
            "come online today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300154V#5P#2304FI got it all planned out! Y'see, I analyzed\x01",
            "my data and crafted a foolproof operation!\x02\x03",
            "#3300155V#2302FKitty doesn't always stick on the orbal\x01",
            "network like me, but the thing is...\x02\x03",
            "#3300156V...all I need to do is spread some info she\x01",
            "might be curious about.\x02\x03",
            "#3300157VBased on her trends up until today, there's\x01",
            "a solid 90 percent chance she'll appear.\x02\x03",
            "#3300158V#2309FCan't let this opportunity slip away, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300159V#11P#0208FI understand...\x02\x03",
            "#3300160V#0204FIf that is the case, which one of us will serve as\x01",
            "the decoy? Kitty has to be lured out of hiding\x01",
            "somehow...\x02\x03",
            "#3300161VWhile the decoy acts, the other will trace Kitty's\x01",
            "infiltration route from a different terminal.\x02\x03",
            "#3300162V#0202FIf we repeat this process, we could possibly\x01",
            "corner Kitty.\x02\x03",
            "#3300163VAny complaints?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300164V#5P#2300FHeh. None from me.\x02\x03",
            "#3300165V#2304FIf you and that Aeon system of yours\x01",
            "work with me, Kitty is toast!\x02\x03",
            "#3300166VI prepared for this in advance, and trust me,\x01",
            "I have no intention of going easy on her.\x02\x03",
            "#3300167V#2302FConsidering it's two-on-one, there's no\x01",
            "way she'll be able to weasel out of this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300168V#11P#0203FTwo problems still stand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3300169V#5P#2305FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300170V#11P#0201FFirst, I need access to a suitable terminal\x01",
            "in order to provide backup.\x02\x03",
            "#3300171VI would rather not risk the integrity of the\x01",
            "Special Support Section's terminal back\x01",
            "at base.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300172V#5P#2302FOh, got'cha. I know the perfect place.\x02\x03",
            "#3300173VDeep within Geofront's A Sector, a certain\x01",
            "Control Terminal 3 sits ripe for the taking.\x02\x03",
            "#3300174VIts main router is separate from this one,\x01",
            "so it's perfect for our pincer maneuver!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300175V#11P#0205FHow convenient.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300176V#6P#0012F(Uh... Haha.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3300177V#0301F(Anyone gettin' this?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3300178V#6P#0100F(Too many technical terms are being tossed around...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300179V#11P#0206FNow for the other issue...\x02\x03",
            "#3300180V#0201FIt is the fact that you are wrapping us into\x01",
            "your schemes while we're busy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3300181V#6P#0005FThat's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3300182V#6P#0106FIt's not ideal, no.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3300183V#0306FYesterday's race ate up our entire afternoon,\x01",
            "so we've been busy as hell.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#3300184V#11P#2307FAre you trying to get out of this?!\x02\x03",
            "#3300185VThis is a support request, isn't it?\x01",
            "You can't just deny it because you\x01",
            "don't feel like it! Do your job!\x02\x03",
            "#3300186VC'mon, I'll toss in some information as\x01",
            "a bonus, so PLEASE JUST HELP ME!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300187V#6P#0006FJona, the thing is...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#3300188V#11P#0204FIt is fine, Lloyd. I will take care of his\x01",
            "so-called 'support request' myself.\x02\x03",
            "#3300189V#0202FEveryone. Please continue with SSS\x01",
            "duties like usual. Leave this to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x104, 0x2)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3300190V#6P#0005FAre you serious, Tio...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3300191V#6P#0101FB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300192V#11P#0202FIt is a simple fact of role proficiency.\x02\x03",
            "#3300193VWhen it comes to hacking, I am the\x01",
            "most appropriate for the job.\x02\x03",
            "#3300194VI am sure that my absence will not\x01",
            "hinder our work too terribly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3300195V#0301FJona said that terminal was deep in the\x01",
            "Geofront sector near the station, right?\x02\x03",
            "#3300196VAin't that a bit dangerous for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300197V#2P#0204FI will find a way to manage.\x02\x03",
            "#3300198VMy abilities alone should be enough to take\x01",
            "care of any monsters that show up by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3300199V#6P#0108FTio...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#3300200V#6P#0004FHow about we do this?\x02\x03",
            "#3300201V#0000FI'll accompany Tio to this Control Terminal 3\x01",
            "while you two head back to headquarters.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#3300202V#11P#0205FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3300203V#0300FYeah, that should work out.\x02\x03",
            "#3300204VI wasn't a fan of lettin' Tio Tot go\x01",
            "in alone, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3300205V#6P#0103FYes. I think this is for the best.\x02\x03",
            "#3300206V#0100FRandy and I should be able to handle the\x01",
            "odd jobs the department will throw us.\x01",
            "They'll appreciate the help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300207V#11P#0208FW-Wait...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#3300208V#5P#2300FWhat's the big deal, Tio? It's\x01",
            "just this guy you'll be with, right?\x02\x03",
            "#3300209VWere you ever the type of person\x01",
            "to worry about petty stuff like this?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(150)

    ChrTalk(
        0x103,
        "#3300210V#11P#0201F(*glare*)\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(800)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "#3300211V#5P#2305FWhoa, whoa. Forget I said anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300212V#11P#0203F...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#3300126V#11P#0202FFine. If you insist.\x02\x03",
            "#3300214VStill, we should finish any important\x01",
            "business we have before starting this.\x02\x03",
            "#3300215VI imagine this whole thing may last\x01",
            "well into the evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300216V#6P#0000FYeah, that's the plan.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xA0, 4)
    OP_29(0x45, 0x4, 0x2)
    OP_29(0x45, 0x1, 0x0)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Still Have to Take Care of Something\x01",      # 0
            "Good to Go\x01",                                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C7D3"),
        (1, "loc_C9A0"),
        (SWITCH_DEFAULT, "loc_CD39"),
    )


    label("loc_C7D3")

    SetChrSubChip(0x8, 0x0)
    Sleep(300)
    OP_29(0x45, 0x1, 0x1)

    ChrTalk(
        0x8,
        (
            "#3300218V#11P#2302FHah, if that's the case, why are\x01",
            "you still here?\x02\x03",
            "#3300219VI'll be setting things up while you're\x01",
            "doing whatever you're doing.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    SetChrPos(0x8, 498200, 200, 302000, 0)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_68(500600, 1000, 296300, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33000, 0)
    SetChrPos(0x0, 500600, 0, 296300, 180)
    SetChrPos(0x1, 500600, 0, 296300, 180)
    SetChrPos(0x2, 500600, 0, 296300, 180)
    SetChrPos(0x3, 500600, 0, 296300, 180)
    Sleep(10)
    PlayBGM("ed7521", 0)
    EventEnd(0x5)
    Jump("loc_CD39")

    label("loc_C9A0")

    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#3300220V#11P#2309FFinally! Let's get this\x01",
            "briefing underway!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 495400, 0, 295400, 90)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 495400, 0, 297200, 90)
    Sound(820, 0, 100, 0)
    OP_0D()

    def lambda_CA3A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CA3A)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#3300221V#12P#0100FWell, then, Randy and I will go on and\x01",
            "head to headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3300222V#0300F#5PLloyd. Take care of Tio Tot, all right?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3300223V#6P#0004FYeah, leave her to me.\x02\x03",
            "#3300224V#0000FRandy, don't go leaving\x01",
            "Elie out to dry, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3300225V#0309F#5P*gulp*... C'mooon, I would never\x01",
            "do something like that, buddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3300226V#12P#0104FDon't worry. I'll keep an eye on him.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    ChrTalk(
        0x102,
        "#3300227V#6P#0102FTio, work hard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300228V#0202F#11POf course. You, too, Elie.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 3, 0, 27)
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 28)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x102, 0x3)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x104, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)
    Sleep(10)
    PlayBGM("ed7521", 0)
    VolumeBGM(0x28, 0xC8)
    Call(0, 29)
    Jump("loc_CD39")

    label("loc_CD39")

    Return()

    # Function_25_A4AE end

    def Function_26_CD3A(): pass

    label("Function_26_CD3A")


    def lambda_CD3F():
        OP_96(0xFE, 0x7A058, 0x0, 0x48FF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CD3F)
    Sleep(400)

    def lambda_CD5C():
        OP_96(0xFE, 0x7A440, 0x0, 0x49188, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CD5C)
    Sleep(400)

    def lambda_CD79():
        OP_96(0xFE, 0x7A120, 0x0, 0x48A80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CD79)
    Sleep(400)

    def lambda_CD96():
        OP_96(0xFE, 0x7A5D0, 0x0, 0x48DA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CD96)
    WaitChrThread(0x103, 1)

    def lambda_CDB4():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CDB4)
    WaitChrThread(0x102, 1)

    def lambda_CDC5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CDC5)
    WaitChrThread(0x101, 1)

    def lambda_CDD6():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CDD6)
    WaitChrThread(0x104, 1)

    def lambda_CDE7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CDE7)
    WaitChrThread(0x104, 2)
    Return()

    # Function_26_CD3A end

    def Function_27_CDF4(): pass

    label("Function_27_CDF4")


    def lambda_CDF9():
        OP_95(0xFE, 499700, 0, 291700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CDF9)
    Sleep(500)
    SetChrSubChip(0x103, 0x1)
    WaitChrThread(0x102, 1)

    def lambda_CE1E():
        OP_95(0xFE, 499700, 0, 287700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CE1E)
    WaitChrThread(0x102, 1)
    Return()

    # Function_27_CDF4 end

    def Function_28_CE38(): pass

    label("Function_28_CE38")


    def lambda_CE3D():
        OP_95(0xFE, 495400, 0, 295400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CE3D)
    Sleep(500)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    SetChrSubChip(0x101, 0x2)
    WaitChrThread(0x104, 1)

    def lambda_CE69():
        OP_95(0xFE, 499700, 0, 291700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CE69)
    WaitChrThread(0x104, 1)

    def lambda_CE87():
        OP_95(0xFE, 499700, 0, 287700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CE87)
    WaitChrThread(0x104, 1)
    Return()

    # Function_28_CE38 end

    def Function_29_CEA1(): pass

    label("Function_29_CEA1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(500080, 1000, 207690, 0)
    MoveCamera(36, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x101, 500400, 0, 205500, 0)
    SetChrPos(0x103, 499300, 0, 205600, 0)
    SetChrPos(0x8, 499800, 150, 207700, 180)
    OP_70(0x13, 0xA)
    ClearMapObjFlags(0x13, 0x10)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#3300229V#2302F#5PAll right. Once you get there, just\x01",
            "gimme a call on your Enigma.\x02\x03",
            "#3300230VWe'll commence the operation, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300231V#6P#0202FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300232V#12P#0006FI can't pretend to understand this revenge\x01",
            "plot, but aren't you going a bit far, Jona?\x02\x03",
            "#3300233V#0001FIt just sounds to me like you're going to cause\x01",
            "trouble for the people who actually use the\x01",
            "orbal network for their job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300234V#2303F#5PHah. That's cute.\x02\x03",
            "#3300235V#2300FTio and I? We're pros. Kitty, too, probably.\x01",
            "We wouldn't let ourselves be noticed by\x01",
            "your average user.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#3300236V#6P#0204FWe are simply playing a game of tag,\x01",
            "two-against-one, behind the scenes.\x02\x03",
            "#3300237V#0202FThat is my best explanation of it, at least.\x01",
            "There is no need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300238V#12P#0000FHmm... Whatever you say, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300239V#2309F#5PSweet. I'm counting on you, Tio.\x02\x03",
            "#3300240V#2302FI think I'll order a large pizza to\x01",
            "get myself hyped up for this! ♪\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D308():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D308)
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_D31C():
        OP_95(0xFE, 499800, 15, 209700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D31C)
    Sleep(100)

    def lambda_D339():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D339)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_71(0x13, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x13)
    SetMapObjFlags(0x13, 0x10)
    OP_68(500550, 1000, 207480, 1000)

    def lambda_D388():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D388)
    Sleep(50)

    def lambda_D398():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D398)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#3300241V#0003F#11PTry a salad sometime...\x02\x03",
            "#3300242V#0000FWell, we'll head for the Geofront\x01",
            "entrance in front of the station.\x02\x03",
            "#3300243VYou said the lower floors of Geofront\x01",
            "A Sector are our goal, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300244V#6P#0204FYes, Control Terminal 3.\x02\x03",
            "#3300245V#0202FI will explain how everything will go\x01",
            "once we arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300246V#0000FRoger. Let's move out, Tio.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)

    def lambda_D532():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D532)
    Sleep(100)

    def lambda_D542():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D542)
    WaitChrThread(0x101, 2)

    def lambda_D553():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D553)
    WaitChrThread(0x103, 2)

    def lambda_D56C():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D56C)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0x5C, 1)
    NewScene("c000C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_CEA1 end

    def Function_30_D5A6(): pass

    label("Function_30_D5A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    LoadChrToIndex("apl/ch50330.itc", 0x20)
    LoadChrToIndex("apl/ch50331.itc", 0x21)
    LoadChrToIndex("apl/ch50090.itc", 0x22)
    SoundLoad(909)
    OP_68(496800, 1400, 296600, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 495000, 200, 296900, 90)
    SetChrPos(0x103, 495000, 200, 295700, 90)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 497700, 200, 296300, 270)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x18)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 495850, 250, 296700, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x18)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 495850, 250, 295900, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x22)
    SetChrSubChip(0xB, 0x18)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 496850, 250, 296300, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetMapObjFrame(0xFF, "pizza", 0x0, 0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis051.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x103,
        "#3300594V#0205FRosenberg Studio?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(496800, 900, 296600, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#3300595V#0005F#5PW-Wait a minute.\x02\x03",
            "#3300596V#0001FThe Rosenberg Studio is that\x01",
            "doll factory, isn't it?\x02\x03",
            "#3300597VIt was near the mountain path,\x01",
            "if I remember correctly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300598V#2306F#11PYep, that's the place.\x02\x03",
            "#3300599V#2310FWhen I was analyzing Kitty's location,\x01",
            "it led me there! I'm 100 percent certain!\x02\x03",
            "#3300600VBah! The freakin' doll factory...?\x01",
            "This doesn't make any sense!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300601V#6P#0208FIt is certainly strange...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3300602V#0001F#5PHow so?\x02\x03",
            "#3300603VIf Kitty IS at the studio, like Jona claims,\x01",
            "what's so weird about that?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(200)

    ChrTalk(
        0x103,
        (
            "#3300604V#6P#0206FWell...\x02\x03",
            "#3300605V#0201FCurrently, the orbal network is functioning\x01",
            "within the city and at St. Ursula Medical College.\x02\x03",
            "#3300606VThe health resort on the other side of the lake,\x01",
            "Mishelam, is also a part of the testing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3300607V#0005F#5POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300608V#2303F#11PY'see, because wireless orbal waves are unstable,\x01",
            "they're primarily only used for orbal telephones.\x02\x03",
            "#3300609VAnd since the orbal network is constantly exchanging\x01",
            "large amounts of information, it's fundamentally a\x01",
            "wired connection.\x02\x03",
            "#3300610V#2310FA giant orbal cable runs along the bottom of the\x01",
            "lake, connecting St. Ursula and Mishelam...\x02\x03",
            "#3300611VBut I've never heard of any connection being made\x01",
            "to Rosenberg Studio... Was it done in secret...?!\x02\x03",
            "#3300612V#2311FAh, enough already! What kind\x01",
            "of sick prank is this?!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3300613V#0003F#5PHmm...\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x32, 0x1F4)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x320)

    ChrTalk(
        0x101,
        "#3300614V#0008F#5P(No way...)\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#3300615V#6P#0203FThough the mystery still remains, we\x01",
            "succeeded in our objective.\x02\x03",
            "#3300616V#0202FI believe you mentioned a reward?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300617V#2306F#11P*sigh* Yeah, yeah.\x02\x03",
            "#3300618VNone of this would have been\x01",
            "possible without your help.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x330),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x330, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3300619V#0001F#5PThis is the information we\x01",
            "were asking for, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300620V#2303F#11PI'll cut to the chase. That contains info\x01",
            "on most of Revache's relationships.\x02\x03",
            "#3300621V#2300FSome other related topics were thrown\x01",
            "in for safe measure. Happy now?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3300622V#0005F#5PYeah, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300623V#6P#0201FThis is indeed the intel\x01",
            "we were trying to obtain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300624V#2306F#11PI'll just say this: All of that stuff is,\x01",
            "if someone dug hard enough, info\x01",
            "they'd already know by now.\x02\x03",
            "#3300625VFor example, the bosses over at the\x01",
            "CPD have known about this stuff\x01",
            "for a loooong time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300626V#0004F#5PRight. This will be really useful, Jona.\x02\x03",
            "#3300627V#0000FSince we didn't have access to all this,\x01",
            "we were at a bit of a disadvantage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3300628V#2303F#11PThat so? Good for you, then.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_68(497430, 900, 296660, 1000)
    SetCameraDistance(17100, 1000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 497700, 250, 296000, 0)
    Sound(804, 0, 100, 0)
    Sound(909, 2, 100, 0)
    BeginChrThread(0x8, 3, 0, 31)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#3300629V#2311F#11PScrew it! I'm taking a nap!\x02\x03",
            "#3300630VTomorrow, I'll use what we learned today\x01",
            "to finally uncover Kitty's true identity!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300631V#0012FHaha, don't work yourself to death now.\x02\x03",
            "#3300632V#0000FIt's the Anniversary Festival, Jona. Why\x01",
            "don't you go on a date or something,\x01",
            "instead of holing up in here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3300633V#2310F#11PSh-Shut up! It's none of your\x01",
            "business what I do or don't do!\x02\x03",
            "#3300634VYou damn normie! Go to hell!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3300635V#0013F#5PNot exactly sure what he meant...\x01",
            "But wasn't that a bit vulgar?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#3300636V#6P#0203FNow that you mention it...\x02\x03",
            "#3300637VYou went on a date with Cecile on the\x01",
            "opening day of the festival, correct?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    ChrTalk(
        0x101,
        "#3300638V#0005F#5PHuh?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_E66E")

    ChrTalk(
        0x103,
        (
            "#3300639V#6P#0211FAnd after that, you ended up spending\x01",
            "time with the beautiful Seeker sisters...\x02\x03",
            "#3300641VExperience really does trump everything\x01",
            "in the end...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E716")

    label("loc_E66E")


    ChrTalk(
        0x103,
        (
            "#3300640V#6P#0211FAnd after that, you and Randy enjoyed\x01",
            "an afternoon with the St. Ursula nurses...\x02\x03",
            "#3300641VExperience really does trump everything\x01",
            "in the end...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E716")

    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3300642V#0012F#5PUh, Tio? What are you trying to say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300643V#6P#0204FNothing in particular.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17600, 2000)
    FadeToDark(2000, 0, -1)
    BeginChrThread(0x11, 1, 0, 32)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x11, 1)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_24(0x38D)
    SetScenarioFlags(0x5C, 5)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_D5A6 end

    def Function_31_E85C(): pass

    label("Function_31_E85C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E876")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x0, 0x2)
    Jump("Function_31_E85C")

    label("loc_E876")

    Return()

    # Function_31_E85C end

    def Function_32_E877(): pass

    label("Function_32_E877")

    Sleep(500)
    OP_25(0x38D, 0x5A)
    Sleep(200)
    OP_25(0x38D, 0x50)
    Sleep(200)
    OP_25(0x38D, 0x46)
    Sleep(200)
    OP_25(0x38D, 0x3C)
    Sleep(200)
    OP_25(0x38D, 0x32)
    Sleep(200)
    OP_25(0x38D, 0x28)
    Sleep(200)
    OP_25(0x38D, 0x1E)
    Sleep(200)
    OP_25(0x38D, 0x14)
    Sleep(200)
    OP_25(0x38D, 0xA)
    Sleep(200)
    OP_24(0x38D)
    Return()

    # Function_32_E877 end

    def Function_33_E8BD(): pass

    label("Function_33_E8BD")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0001F(Our suspect should be inside\x01",
            "of that room...)\x02\x03",
            "(Let's check it out.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 502470, 0, 199800, 270)
    EventEnd(0x4)
    Return()

    # Function_33_E8BD end

    SaveToFile()

Try(main)
