from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0100.bin",                # FileName
        "m0100",                    # MapName
        "m0100",                    # Location
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
        "m0100",                  # 0
        "Geofront Management Official",# 1
        "bm0101",                 # 2
        "bm0101",                 # 3
        "bm0101",                 # 4
        "bm0101",                 # 5
        "bm0100",                 # 6
        "bm0100",                 # 7
        "bm0100",                 # 8
        "bm0100",                 # 9
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 8,   0,   12,  0,   0,   5,   7)
    Sepith("Sepith_B4", 12,  1,   8,   0,   3,   7,   0)
    Sepith("Sepith_C4", 0,   0,   0,   10,  7,   7,   7)
    Sepith("Sepith_D4", 0,   12,  5,   0,   7,   2,   6)

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

    # monster count: 9

    BattleInfo(
        "BattleInfo_1A4", 0x0000, 18, 6, 60, 6, 1, 30, 0, "bm0101", "Sepith_A4", 30, 45, 20, 5,
        (
            ("ms68700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68700.dat", "ms68700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68700.dat", "ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_26C", 0x0000, 18, 6, 60, 6, 1, 25, 0, "bm0100", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms75800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms75800.dat", "ms75800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms75800.dat", "ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_334", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_C4", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3FC", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0100", "Sepith_D4", 30, 45, 20, 5,
        (
            ("ms63800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63800.dat", "ms63800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63800.dat", "ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_4C4", 0x0000, 18, 6, 60, 6, 1, 30, 0, "bm0100", "Sepith_A4", 30, 45, 20, 5,
        (
            ("ms68700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68700.dat", "ms68700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68700.dat", "ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_58C", 0x0000, 18, 6, 60, 6, 1, 25, 0, "bm0101", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms75800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms75800.dat", "ms75800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms75800.dat", "ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_654", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0100", "Sepith_C4", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    AddCharChip((
        "chr/ch26000.itc",                   # 00
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
        "monster/ch63850.itc",               # 10
        "monster/ch63851.itc",               # 11
        "monster/ch68750.itc",               # 12
        "monster/ch68750.itc",               # 13
        "monster/ch75850.itc",               # 14
        "monster/ch75851.itc",               # 15
        "monster/ch60550.itc",               # 16
        "monster/ch60550.itc",               # 17
    ))

    DeclNpc(93000,   0,       3400,    225,  389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)

    DeclMonster(194920,  60,      0,       0x1010000,    "BattleInfo_1A4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(399500,  10,      0,       0x1010000,    "BattleInfo_26C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(199710,  -100350, 0,       0x1010000,    "BattleInfo_334", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(199570,  -203180, 0,       0x1010000,    "BattleInfo_3FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(300340,  -100040, 4000,    0x1010000,    "BattleInfo_4C4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(214950,  -16210,  4000,    0x1010000,    "BattleInfo_58C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(199840,  -3150,   4000,    0x1010000,    "BattleInfo_334", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(199810,  199380,  0,       0x1010000,    "BattleInfo_3FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(299660,  303250,  0,       0x1010000,    "BattleInfo_654", 0,   22,  0xFFFF, 6,  7)

    DeclActor(200000,  0,       -200000, 1200,    200000,  1000,    -200000, 0x007C, 0,  4,  0x0000)
    DeclActor(300000,  0,       300000,  1200,    300000,  1000,    300000,  0x007C, 0,  5,  0x0000)
    DeclActor(0,       0,       102000,  1200,    0,       1000,    102500,  0x007C, 0,  10, 0x0000)
    DeclActor(100000,  0,       202000,  1200,    100000,  1000,    202500,  0x007C, 0,  12, 0x0000)
    DeclActor(402000,  0,       200000,  1200,    402500,  1000,    200000,  0x007C, 0,  14, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7

    ScpFunction((
        "Function_0_A10",          # 00, 0
        "Function_1_AC8",          # 01, 1
        "Function_2_BBA",          # 02, 2
        "Function_3_118D",         # 03, 3
        "Function_4_1287",         # 04, 4
        "Function_5_13C3",         # 05, 5
        "Function_6_1548",         # 06, 6
        "Function_7_1977",         # 07, 7
        "Function_8_25DF",         # 08, 8
        "Function_9_32B5",         # 09, 9
        "Function_10_32D0",        # 0A, 10
        "Function_11_3459",        # 0B, 11
        "Function_12_35A0",        # 0C, 12
        "Function_13_3729",        # 0D, 13
        "Function_14_3870",        # 0E, 14
        "Function_15_39F9",        # 0F, 15
        "Function_16_3B40",        # 10, 16
    ))


    def Function_0_A10(): pass

    label("Function_0_A10")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_A50"),
        (1, "loc_A5C"),
        (2, "loc_A68"),
        (3, "loc_A74"),
        (4, "loc_A80"),
        (5, "loc_A8C"),
        (6, "loc_A98"),
        (SWITCH_DEFAULT, "loc_AA4"),
    )


    label("loc_A50")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_AB0")

    label("loc_A5C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_AB0")

    label("loc_A68")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_AB0")

    label("loc_A74")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_AB0")

    label("loc_A80")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_AB0")

    label("loc_A8C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_AB0")

    label("loc_A98")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AB0")

    label("loc_AA4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AB0")

    label("loc_AB0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AB0")

    label("loc_AC7")

    Return()

    # Function_0_A10 end

    def Function_1_AC8(): pass

    label("Function_1_AC8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2E")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF5")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)
    Jump("loc_B2E")

    label("loc_AF5")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B14")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)
    Jump("loc_B2E")

    label("loc_B14")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2E")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)

    label("loc_B2E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B48")
    Event(0, 16)

    label("loc_B48")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B65")
    OP_C7(0x0, 0x1000)

    label("loc_B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_BB9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B88")
    Jump("loc_BB9")

    label("loc_B88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_B9E")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_BB9")

    label("loc_B9E")

    SetChrPos(0x8, 89500, 0, 6000, 0)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x80)

    label("loc_BB9")

    Return()

    # Function_1_AC8 end

    def Function_2_BBA(): pass

    label("Function_2_BBA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCE")
    VolumeBGM(0x64, 0x64)

    label("loc_BCE")

    SetMapObjFrame(0xF, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0x10, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0x11, "m00ele00", 0x2, "up_kp")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_C1C")
    ClearMapObjFlags(0x14, 0x10)
    OP_70(0x14, 0x1E)
    Jump("loc_C22")

    label("loc_C1C")

    ClearMapObjFlags(0x14, 0x10)

    label("loc_C22")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C41")
    OP_10(0x1E, 0x0)
    OP_10(0x28, 0x1)
    OP_10(0x1F, 0x0)
    OP_10(0x29, 0x1)
    Jump("loc_C4D")

    label("loc_C41")

    OP_10(0x1E, 0x1)
    OP_10(0x28, 0x0)
    OP_10(0x1F, 0x1)
    OP_10(0x29, 0x0)

    label("loc_C4D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C9C")
    Sound(122, 1, 100, 0)
    Jump("loc_C9F")

    label("loc_C9C")

    OP_24(0x7A)

    label("loc_C9F")

    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_DEA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_D17")
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign00", 0x1, 0x1)
    SetMapObjFrame(0x1, "light00", 0x1, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_D57")

    label("loc_D17")

    SetMapObjFrame(0x1, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x1, "light00", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x1, 0x1)
    SetMapObjFrame(0x1, "light01", 0x1, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57, 7)), scpexpr(EXPR_END)), "loc_DA5")
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign00", 0x1, 0x1)
    SetMapObjFrame(0x2, "light00", 0x1, 0x1)
    SetMapObjFlags(0x2, 0x10)
    Jump("loc_DE5")

    label("loc_DA5")

    SetMapObjFrame(0x2, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x2, "light00", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x1, 0x1)
    SetMapObjFrame(0x2, "light01", 0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_DE5")

    Jump("loc_E6A")

    label("loc_DEA")

    SetMapObjFrame(0x1, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x1, "light00", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x1, 0x1)
    SetMapObjFrame(0x1, "light01", 0x1, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    SetMapObjFrame(0x2, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x2, "light00", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x1, 0x1)
    SetMapObjFrame(0x2, "light01", 0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_E6A")

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
    SetMapObjFrame(0xE, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xE, "light01", 0x0, 0x1)
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1139")
    OP_70(0x12, 0x0)
    Jump("loc_113D")

    label("loc_1139")

    OP_70(0x12, 0x1E)

    label("loc_113D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1150")
    OP_70(0x13, 0x0)
    Jump("loc_1154")

    label("loc_1150")

    OP_70(0x13, 0x1E)

    label("loc_1154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1189")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_1189")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1177")
    Jump("loc_1189")

    label("loc_1177")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_1189")
    OP_1B(0x7, 0x0, 0x8)

    label("loc_1189")

    Call(0, 3)
    Return()

    # Function_2_BBA end

    def Function_3_118D(): pass

    label("Function_3_118D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11D3")
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    Jump("loc_11E2")

    label("loc_11D3")

    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)

    label("loc_11E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1203")
    SetChrFlags(0xA, 0x8)
    Jump("loc_1208")

    label("loc_1203")

    ClearChrFlags(0xA, 0x8)

    label("loc_1208")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1232")
    SetChrFlags(0xB, 0x8)
    Jump("loc_1237")

    label("loc_1232")

    ClearChrFlags(0xB, 0x8)

    label("loc_1237")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1258")
    SetChrFlags(0xD, 0x8)
    Jump("loc_125D")

    label("loc_1258")

    ClearChrFlags(0xD, 0x8)

    label("loc_125D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_127B")
    SetChrFlags(0xC, 0x8)
    SetMapObjFlags(0x12, 0x4)
    Jump("loc_1286")

    label("loc_127B")

    ClearChrFlags(0xC, 0x8)
    ClearMapObjFlags(0x12, 0x4)

    label("loc_1286")

    Return()

    # Function_3_118D end

    def Function_4_1287(): pass

    label("Function_4_1287")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1371")
    Sound(14, 0, 100, 0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x38E, 1)"), scpexpr(EXPR_END)), "loc_1307")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_136C")

    label("loc_1307")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x12, 0x1E, 0x0, 0x0, 0x0)

    label("loc_136C")

    Jump("loc_13B7")

    label("loc_1371")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Barrier? I hardly know her!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_13B7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1287 end

    def Function_5_13C3(): pass

    label("Function_5_13C3")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14AD")
    Sound(14, 0, 100, 0)
    OP_71(0x13, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_1443")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_14A8")

    label("loc_1443")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
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

    label("loc_14A8")

    Jump("loc_153C")

    label("loc_14AD")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell is so advanced that even this chest is\x01",
            "connected to the orbal network. Can you believe it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_153C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_13C3 end

    def Function_6_1548(): pass

    label("Function_6_1548")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_17C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1642")

    ChrTalk(
        0x8,
        (
            "B Sector is primarily focused on waterworks\x01",
            "management and water purification.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If something were to happen to the facilities\x01",
            "here, the entire city might fall into chaos.\x01",
            "Please, find the source of the anomaly!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BF")

    label("loc_1642")


    ChrTalk(
        0x8,
        (
            "The Geofront's primary functions are\x01",
            "divided between four sectors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A Sector controls and maintains the city's\x01",
            "exhaust and ventilation systems...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...and B Sector primarily focuses on waterworks\x01",
            "management and purification.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If something were to happen to the facilities\x01",
            "here, the entire city might fall into chaos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please, find the source of the anomaly!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_17BF")

    Jump("loc_1973")

    label("loc_17C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_17D8")
    Call(0, 7)
    Jump("loc_1973")

    label("loc_17D8")


    ChrTalk(
        0x8,
        (
            "What are the odds that the entire Bracer Guild\x01",
            "staff would be out-of-state when something\x01",
            "like this is happening?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My only choice was to submit a\x01",
            "request to the police, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh* Will they even understand\x01",
            "how big of an issue this is?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1973")

    ChrTalk(
        0x101,
        (
            "#0005F(Did he say a request to the police...?\x01",
            "Is he talking about us?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(Maybe we should check the SSS\x01",
            "terminal, just to be sure.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1973")

    TalkEnd(0xFE)
    Return()

    # Function_6_1548 end

    def Function_7_1977(): pass

    label("Function_7_1977")

    EventBegin(0x0)
    Fade(500)
    OP_68(91900, 1500, 1520, 0)
    MoveCamera(4, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22740, 0)
    SetChrPos(0x101, 91970, 0, 1640, 45)
    SetChrPos(0x102, 91120, 0, 1980, 45)
    SetChrPos(0x103, 91050, 0, 720, 45)
    SetChrPos(0x104, 90040, 0, 940, 45)
    OP_93(0x8, 0xE1, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#11PAre you who I think you are?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FCPD, Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FYour request mentioned an abnormality in\x01",
            "the lower stratum of B Sector?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYes, that's correct. I never imagined\x01",
            "something like this happening...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSomehow, there's a water shortage\x01",
            "in the waterworks area of the Geofront.\x02",
        )
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
        "#12P#0005FWhat did you say?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0105FHow is that even possible...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSince the shortage is relatively minor,\x01",
            "citizens haven't noticed yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...but if things continue as they are, there might\x01",
            "be water shortages throughout the entire city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI NEED you to investigate this quickly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FU-Understood.\x02\x03",
            "#0001FThis lower stratum... We aren't\x01",
            "usually allowed there, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYeah, that's true. This is an exception, though.\x01",
            "The door is right over there, so give me a\x01",
            "minute to unlock it for you all.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(90000, 1200, 6500, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x8, 90000, 150, 7250, 0)
    SetChrPos(0x101, 90500, 0, 5750, 0)
    SetChrPos(0x102, 89500, 0, 5500, 0)
    SetChrPos(0x103, 90500, 0, 4250, 0)
    SetChrPos(0x104, 89500, 0, 4000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign00", 0x1, 0x1)
    SetMapObjFrame(0x1, "light00", 0x1, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Sound(72, 0, 100, 0)
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#5PThere's an elevator a little ways down that'll\x01",
            "take you to the lower stratum. You can't miss it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PJust so you know, the anomaly was detected\x01",
            "in the lowest depths of B Sector.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt may be tough, but I need you all to look\x01",
            "into this. For the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FNo problem. Leave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FA moment, please.\x02\x03",
            "#0200FIs that door there not the fastest way\x01",
            "to reach the bottom of B Sector?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_68(110000, 1500, 6500, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        "#2P#0305FOh, there an elevator or somethin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2P#0100FMaybe. Most of the other areas we've explored\x01",
            "have followed that general layout.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(90000, 1200, 6500, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PThat's true. There is indeed an elevator\x01",
            "that could take you directly to the bottom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, last time I tried to call it up,\x01",
            "it wasn't responding. It must be stuck\x01",
            "at the lower stratum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POrbal energy was still coursing through the terminal,\x01",
            "so lack of power doesn't seem to be the issue...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FHmm, that is strange.\x02",
    )

    CloseMessageWindow()

    def lambda_22EB():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22EB)
    Sleep(50)

    def lambda_22FB():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_22FB)
    Sleep(50)

    def lambda_230B():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_230B)
    Sleep(50)

    def lambda_231B():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_231B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#11P#0003FThat must be connected to the\x01",
            "abnormality we're investigating.\x02\x03",
            "#0001FIn that case, let's use this elevator to\x01",
            "reach the lower stratum.\x02\x03",
            "Also, if we need to take care of our equipment,\x01",
            "let's do that now. This place sounds pretty big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0101FOf course. We still need to head\x01",
            "to the hospital, so we don't have\x01",
            "too much time to waste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FOnce we're good to go,\x01",
            "let's mosey on down!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Strange Phenomenon in the Geofront]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(90000, 1000, 5750, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33000, 0)
    SetChrPos(0x0, 90000, 0, 5750, 0)
    SetChrPos(0x1, 90000, 0, 5750, 0)
    SetChrPos(0x2, 90000, 0, 5750, 0)
    SetChrPos(0x3, 90000, 0, 5750, 0)
    SetChrPos(0x8, 93000, 0, 3400, 225)
    OP_29(0x34, 0x1, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_7_1977 end

    def Function_8_25DF(): pass

    label("Function_8_25DF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    LoadChrToIndex("apl/ch50544.itc", 0x1E)
    OP_68(109900, 1150, 8000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 109400, 1500, 9250, 180)
    SetChrPos(0x102, 110400, 1500, 9500, 180)
    SetChrPos(0x103, 109400, 1500, 10750, 180)
    SetChrPos(0x104, 110400, 1500, 11000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign00", 0x1, 0x1)
    SetMapObjFrame(0x2, "light00", 0x1, 0x1)
    Sound(72, 0, 100, 0)
    Sleep(500)
    OP_71(0x2, 0x1, 0xA, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x2)
    OP_68(109900, 1150, 3000, 3000)

    def lambda_270B():
        OP_97(0x101, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_270B)

    def lambda_2725():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2725)
    Sleep(50)

    def lambda_2739():
        OP_97(0x102, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2739)

    def lambda_2753():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2753)
    Sleep(50)

    def lambda_2767():
        OP_97(0x103, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2767)

    def lambda_2781():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2781)
    Sleep(50)

    def lambda_2795():
        OP_97(0x104, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2795)

    def lambda_27AF():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_27AF)
    Sleep(2000)
    Fade(500)
    OP_68(93000, 1150, 3400, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    OP_93(0x8, 0x5A, 0x1F4)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_97(0x8, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)

    def lambda_282D():
        OP_97(0x8, 0x2710, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_282D)
    Sleep(1000)
    Fade(500)
    OP_68(109620, 1150, 2220, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    EndChrThread(0x8, 0x1)
    SetChrPos(0x8, 104900, 0, 500, 180)

    def lambda_2892():

        label("loc_2892")

        TurnDirection(0x101, 0x8, 0)
        Yield()
        Jump("loc_2892")

    QueueWorkItem2(0x101, 1, lambda_2892)

    def lambda_28A4():

        label("loc_28A4")

        TurnDirection(0x102, 0x8, 0)
        Yield()
        Jump("loc_28A4")

    QueueWorkItem2(0x102, 1, lambda_28A4)

    def lambda_28B6():

        label("loc_28B6")

        TurnDirection(0x103, 0x8, 0)
        Yield()
        Jump("loc_28B6")

    QueueWorkItem2(0x103, 1, lambda_28B6)

    def lambda_28C8():

        label("loc_28C8")

        TurnDirection(0x104, 0x8, 0)
        Yield()
        Jump("loc_28C8")

    QueueWorkItem2(0x104, 1, lambda_28C8)

    def lambda_28DA():
        OP_97(0x8, 0x1388, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_28DA)
    OP_0D()
    OP_71(0x2, 0xA, 0x1, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x0, 0x1F4)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)

    ChrTalk(
        0x8,
        "#12PThe SSS?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12PYou came from this side...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PWait! Does that mean that\x01",
            "the elevator is working again?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FYes, it is. If you're ready,\x01",
            "we'd like to give our report.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(109940, 1150, 560, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 109400, 1500, 2250, 180)
    SetChrPos(0x102, 110400, 1500, 2500, 180)
    SetChrPos(0x103, 109400, 1500, 3750, 180)
    SetChrPos(0x104, 110400, 1500, 4000, 180)
    TurnDirection(0x101, 0x104, 0)
    TurnDirection(0x102, 0x103, 0)
    TurnDirection(0x103, 0x102, 0)
    TurnDirection(0x104, 0x101, 0)
    SetChrPos(0x8, 109900, 0, 500, 180)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#12POh, yes. Of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12PI see! What a relief!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PUnderstood. I'll head back\x01",
            "right away.\x02",
        )
    )

    CloseMessageWindow()
    Sound(807, 0, 100, 0)
    Fade(500)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_68(109620, 1150, 2220, 2000)
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_2B53():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B53)
    Sleep(50)

    def lambda_2B63():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B63)
    Sleep(50)

    def lambda_2B73():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B73)
    Sleep(50)

    def lambda_2B83():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B83)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#5P#0000FSo everything's going to be all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PYes, it appears as if the waterworks have\x01",
            "completely returned to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PThank you, everyone! I don't know what\x01",
            "I would have done without you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FIt's not like we could ignore such\x01",
            "a pressing issue for the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0304FI'm just glad we made it out in one piece.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PYeah, I was getting real\x01",
            "worried for a second there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PAnyway, I can't believe monsters were\x01",
            "able to interrupt Geofront facilities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PWe might have to adopt new countermeasures\x01",
            "against them to protect the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0001FThat's a smart idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#0203F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PWell, in any case, I can't thank you\x01",
            "enough for all your hard work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PI still have some repairs to wrap up,\x01",
            "so I'll have to excuse myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#0100FGood luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0300FSee ya later, dude.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    BeginChrThread(0x101, 1, 0, 9)
    BeginChrThread(0x102, 1, 0, 9)
    BeginChrThread(0x103, 1, 0, 9)
    BeginChrThread(0x104, 1, 0, 9)
    OP_97(0x8, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_68(109900, 1150, 3000, 1000)

    def lambda_2FA1():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FA1)
    Sleep(50)

    def lambda_2FB1():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2FB1)
    Sleep(50)

    def lambda_2FC1():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2FC1)
    Sleep(50)

    def lambda_2FD1():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2FD1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#0003FI still can't shake the feeling\x01",
            "that was no average monster.\x02\x03",
            "#0001FIt wouldn't be a bad idea to consult\x01",
            "with the guild about this in the future, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0103FRemember, the mafia and the missing\x01",
            "persons take priority right now.\x02\x03",
            "#0101FThis request took longer than I thought.\x01",
            "We should hurry to St. Ursula, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0301FYeah, sun's gonna set if we take any longer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0203FLet us be off, then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Strange Phenomenon in the Geofront]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_37()
    OP_68(109900, 1000, 3200, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33000, 0)
    SetChrPos(0x0, 109900, 0, 3200, 180)
    SetChrPos(0x1, 109900, 0, 3200, 180)
    SetChrPos(0x2, 109900, 0, 3200, 180)
    SetChrPos(0x3, 109900, 0, 3200, 180)
    SetScenarioFlags(0x57, 7)
    OP_29(0x34, 0x1, 0x3)
    OP_29(0x34, 0x4, 0x10)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_8_25DF end

    def Function_9_32B5(): pass

    label("Function_9_32B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32CF")
    TurnDirection(0xFE, 0x8, 500)
    Sleep(200)
    Jump("Function_9_32B5")

    label("loc_32CF")

    Return()

    # Function_9_32B5 end

    def Function_10_32D0(): pass

    label("Function_10_32D0")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3451")
    Fade(500)
    SetChrPos(0x0, 600, 0, 100600, 0)
    SetChrPos(0x1, -600, 0, 100600, 0)
    SetChrPos(0x2, -600, 0, 99400, 0)
    SetChrPos(0x3, 600, 0, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33AF")
    SetChrPos(0x4, -600, 0, 98200, 0)
    SetChrPos(0x5, 600, 0, 98200, 0)
    Jump("loc_33CE")

    label("loc_33AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33CE")
    SetChrPos(0x4, 0, 0, 98200, 0)

    label("loc_33CE")

    OP_68(0, 1000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(0, -4000, 100000, 2000)
    SetMapObjFrame(0xF, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0110", 0, 0, 0)
    IdleLoop()

    label("loc_3451")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_32D0 end

    def Function_11_3459(): pass

    label("Function_11_3459")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xF, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(0, -4000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, -10000, 100600, 0)
    OP_90(0x1, -600, -10000, 100600, 0)
    OP_90(0x2, -600, -10000, 99400, 0)
    OP_90(0x3, 600, -10000, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_352E")
    OP_90(0x4, -600, -10000, 98200, 0)
    OP_90(0x5, 600, -10000, 98200, 0)
    Jump("loc_354D")

    label("loc_352E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_354D")
    OP_90(0x4, 0, -10000, 98200, 0)

    label("loc_354D")

    Sound(145, 0, 100, 0)
    OP_68(0, 1000, 100000, 3000)
    SetMapObjFrame(0xF, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xF)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_3459 end

    def Function_12_35A0(): pass

    label("Function_12_35A0")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3721")
    Fade(500)
    SetChrPos(0x0, 100600, 0, 200600, 0)
    SetChrPos(0x1, 99400, 0, 200600, 0)
    SetChrPos(0x2, 99400, 0, 199400, 0)
    SetChrPos(0x3, 100600, 0, 199400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_367F")
    SetChrPos(0x4, 99400, 0, 198200, 0)
    SetChrPos(0x5, 100600, 0, 198200, 0)
    Jump("loc_369E")

    label("loc_367F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_369E")
    SetChrPos(0x4, 100000, 0, 198200, 0)

    label("loc_369E")

    OP_68(100000, 1000, 200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(100000, -4000, 200000, 2000)
    SetMapObjFrame(0x10, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0113", 0, 0, 0)
    IdleLoop()

    label("loc_3721")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_35A0 end

    def Function_13_3729(): pass

    label("Function_13_3729")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0x10, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(100000, -4000, 200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 100600, -10000, 200600, 0)
    OP_90(0x1, 99400, -10000, 200600, 0)
    OP_90(0x2, 99400, -10000, 199400, 0)
    OP_90(0x3, 100600, -10000, 199400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37FE")
    OP_90(0x4, 99400, -10000, 198200, 0)
    OP_90(0x5, 100600, -10000, 198200, 0)
    Jump("loc_381D")

    label("loc_37FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_381D")
    OP_90(0x4, 100000, -10000, 198200, 0)

    label("loc_381D")

    Sound(145, 0, 100, 0)
    OP_68(100000, 1000, 200000, 3000)
    SetMapObjFrame(0x10, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x10)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_3729 end

    def Function_14_3870(): pass

    label("Function_14_3870")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39F1")
    Fade(500)
    SetChrPos(0x0, 400600, 0, 200600, 90)
    SetChrPos(0x1, 400600, 0, 199400, 90)
    SetChrPos(0x2, 399400, 0, 199400, 90)
    SetChrPos(0x3, 399400, 0, 200600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_394F")
    SetChrPos(0x4, 398200, 0, 199400, 90)
    SetChrPos(0x5, 398200, 0, 200600, 90)
    Jump("loc_396E")

    label("loc_394F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_396E")
    SetChrPos(0x4, 398200, 0, 200000, 90)

    label("loc_396E")

    OP_68(400000, 1000, 200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(400000, -4000, 200000, 2000)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0101", 0, 0, 0)
    IdleLoop()

    label("loc_39F1")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_3870 end

    def Function_15_39F9(): pass

    label("Function_15_39F9")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(400000, -4000, 200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 400600, -10000, 200600, 90)
    OP_90(0x1, 400600, -10000, 199400, 90)
    OP_90(0x2, 399400, -10000, 199400, 90)
    OP_90(0x3, 399400, -10000, 200600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ACE")
    OP_90(0x4, 398200, 0, 199400, 90)
    OP_90(0x5, 398200, 0, 200600, 90)
    Jump("loc_3AED")

    label("loc_3ACE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AED")
    OP_90(0x4, 398200, 0, 200000, 90)

    label("loc_3AED")

    Sound(145, 0, 100, 0)
    OP_68(400000, 1000, 200000, 3000)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x11)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_39F9 end

    def Function_16_3B40(): pass

    label("Function_16_3B40")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(110000, 500, 1500, 0)
    MoveCamera(60, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 84500, 0, -200, 90)
    SetChrPos(0x102, 84500, 0, 300, 90)
    SetChrPos(0x103, 84500, 0, -200, 90)
    SetChrPos(0x104, 84500, 0, 300, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_68(95000, 500, 1500, 8000)
    SetCameraDistance(25000, 8000)
    FadeToBright(1000, 0)
    Sleep(5000)

    def lambda_3C21():
        OP_96(0xFE, 0x15888, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C21)

    def lambda_3C3B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C3B)
    Sleep(500)

    def lambda_3C4F():
        OP_96(0xFE, 0x15888, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C4F)

    def lambda_3C69():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3C69)
    Sleep(500)

    def lambda_3C7D():
        OP_96(0xFE, 0x15374, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3C7D)

    def lambda_3C97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3C97)
    Sleep(500)

    def lambda_3CAB():
        OP_96(0xFE, 0x15374, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3CAB)

    def lambda_3CC5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3CC5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x11)
    Sleep(500)
    Fade(500)
    OP_68(88130, 1000, 160, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#2200833V#0001F#6PThis is the Geofront's B Sector?\x02\x03",
            "#2200834VHonestly, it doesn't look all that\x01",
            "different from A Sector...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200835V#6P#0203FAccording to the database, this sector is\x01",
            "used to control the city's water systems.\x02\x03",
            "#2200836V#0200FThe terminal in question should be\x01",
            "located somewhere in the upper stratum.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E65():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3E65)
    Sleep(50)

    def lambda_3E75():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3E75)
    Sleep(50)

    def lambda_3E85():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E85)
    Sleep(50)

    def lambda_3E95():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3E95)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2200837V#5P#0106FBased on the orbmail, he'll be expecting us.\x02\x03",
            "#2200838V#0101FWe should proceed with caution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200839V#5P#0303FTrue. There's no way to know if this is a\x01",
            "trap or not, so let's keep our eyes peeled.\x02\x03",
            "#2200840V#0301FDon't wanna get caught off guard, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200841V#0013F#11PRight. Let's tread lightly.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 87000, 0, 0, 90)
    SetScenarioFlags(0x83, 3)
    OP_29(0x43, 0x1, 0x6)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_16_3B40 end

    SaveToFile()

Try(main)
