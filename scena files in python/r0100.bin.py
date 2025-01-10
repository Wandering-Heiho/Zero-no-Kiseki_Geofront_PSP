from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0100.bin",                # FileName
        "r0100",                    # MapName
        "r0100",                    # Location
        0x0061,                     # MapIndex
        "ed7201",
        0x00000000,                 # Flags
        ("r0100", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 97, 0, 1, 0, 2],
    )

    BuildStringList((
        "r0100",                  # 0
        "Monster",                # 1
        "Monster",                # 2
        "Monster",                # 3
        "Monster",                # 4
        "Monster",                # 5
        "br0100",                 # 6
        "br0100",                 # 7
        "br0100",                 # 8
        "br0100",                 # 9
        "br0100",                 # 10
        "br0100",                 # 11
        "To Crossbell City & Tangram Gate",# 12
        "To Armorica Village",    # 13
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 0,   2,   0,   7,   3,   5,   0)
    Sepith("Sepith_B4", 3,   0,   7,   0,   2,   1,   4)
    Sepith("Sepith_C4", 6,   3,   0,   0,   4,   3,   1)
    Sepith("Sepith_D4", 2,   0,   7,   1,   4,   2,   1)
    Sepith("Sepith_E4", 34,  15,  25,  15,  0,   0,   0)

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

    # monster count: 13

    BattleInfo(
        "BattleInfo_154", 0x0000, 10, 6, 45, 6, 1, 40, 0, "br0100", "Sepith_A4", 30, 45, 25, 0,
        (
            ("ms63900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63900.dat", "ms63900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63900.dat", "ms62600.dat", "ms63900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1F0", 0x0000, 10, 6, 45, 6, 1, 50, 0, "br0100", "Sepith_B4", 30, 45, 25, 0,
        (
            ("ms62600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62600.dat", "ms62600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62600.dat", "ms66200.dat", "ms62600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_28C", 0x0000, 10, 6, 45, 6, 1, 30, 0, "br0100", "Sepith_C4", 30, 45, 25, 0,
        (
            ("ms62200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62200.dat", "ms62200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62200.dat", "ms69800.dat", "ms62200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_328", 0x0000, 10, 6, 45, 6, 1, 25, 0, "br0100", "Sepith_D4", 30, 45, 25, 0,
        (
            ("ms69800.dat", "ms69800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69800.dat", "ms63900.dat", "ms69800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69800.dat", "ms69900.dat", "ms62600.dat", "ms69900.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3C4", 0x0400, 17, 6, 45, 6, 1, 30, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68901.dat", "ms68901.dat", "ms68901.dat", "ms68901.dat", "ms68901.dat", "ms68901.dat", "ms68901.dat", "ms68901.dat", "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_408", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br0100", "Sepith_E4", 40, 35, 25, 0,
        (
            ("ms76201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76201.dat", "ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
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
        "monster/ch63950.itc",               # 10
        "monster/ch63951.itc",               # 11
        "monster/ch62650.itc",               # 12
        "monster/ch62651.itc",               # 13
        "monster/ch62250.itc",               # 14
        "monster/ch62250.itc",               # 15
        "monster/ch69850.itc",               # 16
        "monster/ch69850.itc",               # 17
        "monster/ch68950.itc",               # 18
        "monster/ch68951.itc",               # 19
        "monster/ch76250.itc",               # 1A
        "monster/ch76251.itc",               # 1B
    ))

    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   25,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   25,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   25,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   25,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   25,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(7430,    10740,   0,       0x1010000,    "BattleInfo_154", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-26680,  23160,   0,       0x1010000,    "BattleInfo_1F0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-47820,  49480,   0,       0x1010000,    "BattleInfo_28C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-82330,  83810,   0,       0x1010000,    "BattleInfo_328", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-68630,  134320,  2000,    0x1010000,    "BattleInfo_154", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-88070,  136430,  2000,    0x1010000,    "BattleInfo_1F0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-28450,  88010,   0,       0x1810000,    "BattleInfo_3C4", 1078, 24,  0xFFFF, 8,  9)
    DeclMonster(10730,   40540,   -1000,   0x1810000,    "BattleInfo_3C4", 1079, 24,  0xFFFF, 8,  9)
    DeclMonster(740,     78220,   -1000,   0x1810000,    "BattleInfo_3C4", 1080, 24,  0xFFFF, 8,  9)
    DeclMonster(-16390,  76670,   -1000,   0x1810000,    "BattleInfo_3C4", 1081, 24,  0xFFFF, 8,  9)
    DeclMonster(-11580,  63140,   -1000,   0x1810000,    "BattleInfo_3C4", 1082, 24,  0xFFFF, 8,  9)
    DeclMonster(-20900,  36230,   0,       0x1010000,    "BattleInfo_408", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-75890,  91810,   0,       0x1010000,    "BattleInfo_408", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 10,  -29.729999542236328,   66.20999908447266,     -1.0,                  81.0,                  [0.11785110831260681,  0.23570236563682556,   -0.0,                  0.0,                   -0.11785118281841278,  0.23570221662521362,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   11.306639671325684,    -8.59841251373291,     0.1428571492433548,    1.0])
    DeclEvent(0x0000, 0, 12,  -29.729999542236328,   66.20999908447266,     -1.0,                  81.0,                  [0.11785110831260681,  0.23570236563682556,   -0.0,                  0.0,                   -0.11785118281841278,  0.23570221662521362,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   11.306639671325684,    -8.59841251373291,     0.1428571492433548,    1.0])

    DeclActor(-84150,  2000,    144490,  1200,    -84150,  3000,    144490,  0x007C, 0,  3,  0x0000)
    DeclActor(3220,    -1000,   92260,   1200,    3220,    0,       92260,   0x007C, 0,  4,  0x0000)
    DeclActor(4000,    -1000,   42910,   1200,    4000,    0,       42910,   0x007C, 0,  5,  0x0000)
    DeclActor(9820,    0,       10930,   1200,    9820,    1000,    10930,   0x007C, 0,  6,  0x0000)
    DeclActor(-29400,  0,       66620,   2000,    -29400,  1500,    66620,   0x007C, 0,  14, 0x0000)
    DeclActor(-28660,  0,       24760,   1200,    -28660,  0,       24760,   0x007C, 0,  7,  0x0000)
    DeclActor(-55620,  0,       75240,   1200,    -55620,  0,       75240,   0x007C, 0,  8,  0x0000)
    DeclActor(-18960,  0,       48760,   5000,    -18960,  0,       48760,   0x007C, 0,  13, 0x0000)

    PlaceName(-5.0, 0.0, -45.0, 0x0000, 0x0000, "To Crossbell City & Tangram Gate")
    PlaceName(-50.0, 0.0, 172.0, 0x0000, 0x0000, "To Armorica Village")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(1299, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(1250, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 8
    ChipFrameInfo(2500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 11

    ScpFunction((
        "Function_0_A14",          # 00, 0
        "Function_1_ACC",          # 01, 1
        "Function_2_B31",          # 02, 2
        "Function_3_116B",         # 03, 3
        "Function_4_12D1",         # 04, 4
        "Function_5_1442",         # 05, 5
        "Function_6_1597",         # 06, 6
        "Function_7_16D4",         # 07, 7
        "Function_8_16E8",         # 08, 8
        "Function_9_16FC",         # 09, 9
        "Function_10_1715",        # 0A, 10
        "Function_11_1E8C",        # 0B, 11
        "Function_12_20E5",        # 0C, 12
        "Function_13_2169",        # 0D, 13
        "Function_14_306E",        # 0E, 14
    ))


    def Function_0_A14(): pass

    label("Function_0_A14")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_A54"),
        (1, "loc_A60"),
        (2, "loc_A6C"),
        (3, "loc_A78"),
        (4, "loc_A84"),
        (5, "loc_A90"),
        (6, "loc_A9C"),
        (SWITCH_DEFAULT, "loc_AA8"),
    )


    label("loc_A54")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_AB4")

    label("loc_A60")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_AB4")

    label("loc_A6C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_AB4")

    label("loc_A78")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_AB4")

    label("loc_A84")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_AB4")

    label("loc_A90")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_AB4")

    label("loc_A9C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AB4")

    label("loc_AA8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AB4")

    label("loc_AB4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ACB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AB4")

    label("loc_ACB")

    Return()

    # Function_0_A14 end

    def Function_1_ACC(): pass

    label("Function_1_ACC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF1")
    ClearChrFlags(0x13, 0x80)

    label("loc_AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B00")
    ClearChrFlags(0x14, 0x80)

    label("loc_B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0F")
    ClearChrFlags(0x15, 0x80)

    label("loc_B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1E")
    ClearChrFlags(0x16, 0x80)

    label("loc_B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2D")
    ClearChrFlags(0x17, 0x80)

    label("loc_B2D")

    Call(0, 9)
    Return()

    # Function_1_ACC end

    def Function_2_B31(): pass

    label("Function_2_B31")

    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE0")
    OP_70(0x0, 0x0)
    Jump("loc_EE4")

    label("loc_EE0")

    OP_70(0x0, 0x1E)

    label("loc_EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF7")
    OP_70(0x1, 0x0)
    Jump("loc_EFB")

    label("loc_EF7")

    OP_70(0x1, 0x1E)

    label("loc_EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F0E")
    OP_70(0x2, 0x0)
    Jump("loc_F12")

    label("loc_F0E")

    OP_70(0x2, 0x1E)

    label("loc_F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F25")
    OP_70(0x3, 0x0)
    Jump("loc_F29")

    label("loc_F25")

    OP_70(0x3, 0x1E)

    label("loc_F29")

    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 0)), scpexpr(EXPR_END)), "loc_F8F")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -28660, 0, 24760, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)
    Jump("loc_FE8")

    label("loc_F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 1)), scpexpr(EXPR_END)), "loc_FE8")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -55620, 0, 75240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x6, 0x1)

    label("loc_FE8")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -29410, 0, 66630, 10000, 2000, 45000)
    SetMapObjFrame(0xFF, "Null_door", 0x2, "open")
    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1044")
    SetMapObjFrame(0xFF, "Null_door", 0x2, "close")
    SetBarrier(0x3, 0x0, 0x1)
    OP_66(0x4, 0x1)

    label("loc_1044")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_105F")
    Jump("loc_10B1")

    label("loc_105F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_1076")
    ModifyEventFlags(1, 1, 0x80)
    Jump("loc_10B1")

    label("loc_1076")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_10A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109F")
    Event(0, 11)

    label("loc_109F")

    Jump("loc_10B1")

    label("loc_10A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_10B1")

    label("loc_10B1")

    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_10C3")
    Jump("loc_1100")

    label("loc_10C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1100")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10DD")
    Jump("loc_1100")

    label("loc_10DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_10EF")
    Jump("loc_1100")

    label("loc_10EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_1100")
    OP_66(0x7, 0x1)

    label("loc_1100")

    SoundDistance(0x7B, 0x57DA, 0xFFFFFC22, 0xB0AE, 0x1388, 0x4E20, 0x64, 0x0)
    OP_E1(0xD8E, 0xFFFFFC22, 0xD4B2)
    OP_E1(0xFFFFF678, 0xFFFFFC22, 0xFF50)
    OP_E1(0x4EC, 0xFFFFFC22, 0x109C8)
    OP_E1(0xFFFFED5E, 0xFFFFFC18, 0x1195E)
    OP_E1(0xFFFFE700, 0xFFFFFDF8, 0x1451E)
    OP_E1(0xFFFFFE02, 0xFFFFFDF8, 0x1C7B4)
    Return()

    # Function_2_B31 end

    def Function_3_116B(): pass

    label("Function_3_116B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1255")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x643, 1)"), scpexpr(EXPR_END)), "loc_11EB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x643),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x102, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1250")

    label("loc_11EB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x643),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1250")

    Jump("loc_12C5")

    label("loc_1255")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Is the chest half-full or half-empty?\x01",
            "Neither. It's completely empty.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_12C5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_116B end

    def Function_4_12D1(): pass

    label("Function_4_12D1")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BB")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1351")
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
    SetScenarioFlags(0x102, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_13B6")

    label("loc_1351")

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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13B6")

    Jump("loc_1436")

    label("loc_13BB")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Don't call me a box! I'm not a box!\x01",
            "My cousin's a box and he's a complete idiot!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1436")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_12D1 end

    def Function_5_1442(): pass

    label("Function_5_1442")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_152C")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x33, 1)"), scpexpr(EXPR_END)), "loc_14C2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x33),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x102, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_1527")

    label("loc_14C2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x33),
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

    label("loc_1527")

    Jump("loc_158B")

    label("loc_152C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I always wanted to be a fisherman\x01",
            "but, well... *sob*\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_158B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1442 end

    def Function_6_1597(): pass

    label("Function_6_1597")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1681")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_1617")
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
    SetScenarioFlags(0x102, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_167C")

    label("loc_1617")

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
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_167C")

    Jump("loc_16C8")

    label("loc_1681")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Next time, I'm using a lock.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_16C8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1597 end

    def Function_7_16D4(): pass

    label("Function_7_16D4")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 0)
    OP_65(0x5, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_16D4 end

    def Function_8_16E8(): pass

    label("Function_8_16E8")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 1)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_8_16E8 end

    def Function_9_16FC(): pass

    label("Function_9_16FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1714")
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)

    label("loc_1714")

    Return()

    # Function_9_16FC end

    def Function_10_1715(): pass

    label("Function_10_1715")

    EventBegin(0x0)
    Fade(500)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    OP_68(-31360, 1500, 64599, 0)
    MoveCamera(357, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17060, 0)
    SetChrPos(0x101, -30900, 0, 65400, 45)
    SetChrPos(0x102, -32000, 0, 65390, 45)
    SetChrPos(0x103, -31280, 0, 63830, 45)
    SetChrPos(0x104, -32610, 0, 63700, 45)
    SetChrPos(0x8, -28450, 0, 88010, 135)
    SetChrPos(0x9, 3100, -1000, 35060, 0)
    SetChrPos(0xA, 740, -1000, 78220, 270)
    SetChrPos(0xB, -16390, -1000, 76670, 135)
    SetChrPos(0xC, -11580, -1000, 63140, 315)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
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
        "#5P#0005FIs this the place?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_68(-28540, 1000, 87990, 0)
    MoveCamera(71, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20760, 0)
    OP_68(-17430, 1500, 75900, 5000)
    MoveCamera(52, 25, 0, 5000)
    Sleep(4900)
    Fade(500)
    OP_68(-3110, 1000, 39950, 0)
    MoveCamera(70, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20760, 0)
    OP_68(-11940, 1000, 63130, 5000)
    MoveCamera(98, 31, 0, 5000)
    SetCameraDistance(16770, 5000)
    OP_6F(0x79)
    Fade(500)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_68(-31360, 1200, 64599, 0)
    MoveCamera(357, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18060, 0)
    SetCameraDistance(17060, 1000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x103,
        (
            "#6P#0200FIndeed. This definitely appears\x01",
            "to be our destination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0101FI still can't believe monsters managed\x01",
            "to turn this place into their lair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0303FNo kiddin'. They look tougher than\x01",
            "the stuff you'd find on the roads, too.\x02\x03",
            "#0301FMight be 'cause of all the stuff that went\x01",
            "down the other month. Probably came\x01",
            "here to look for new feedin' grounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FAnother consequence of Revache\x01",
            "using war hounds.\x02\x03",
            "#0001FWell, discussion isn't going to get us\x01",
            "anywhere. I'm going to unlock the door.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x101, -29840, 0, 66270, 2000, 0x0)
    Sound(809, 0, 100, 0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Used the Private Property Key.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMapObjFrame(0xFF, "Null_door", 0x2, "anime")
    Sound(851, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x101,
        "#5P#0003FEverybody ready?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#11P#0001FAll right! Let's exterminate\x01",
            "some monsters!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0101FUnderstood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0301FLet's give 'em hell!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FEntering extermination mode.\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 0, 0x80)
    OP_68(-29840, 1000, 66270, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x0, -29840, 0, 66270, 45)
    SetChrPos(0x1, -29840, 0, 66270, 45)
    SetChrPos(0x2, -29840, 0, 66270, 45)
    SetChrPos(0x3, -29840, 0, 66270, 45)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_65(0x4, 0x1)
    SetMapObjFrame(0xFF, "Null_door", 0x2, "open")
    SetBarrier(0x2, 0x0, 0x1)
    SetScenarioFlags(0x0, 0)
    OP_29(0xD, 0x1, 0x1)
    Call(0, 9)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -28450, 0, 88010, 0)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 10730, -1000, 40540, 0)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 740, -1000, 78220, 0)
    ClearChrFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -16390, -1000, 76670, 0)
    ClearChrFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -11580, -1000, 63140, 0)
    ClearChrFlags(0x17, 0x4)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1715 end

    def Function_11_1E8C(): pass

    label("Function_11_1E8C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    OP_68(-16510, 0, 74800, 0)
    MoveCamera(71, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19430, 0)
    SetChrPos(0x101, -17420, -1000, 75920, 135)
    SetChrPos(0x102, -15210, -1000, 76100, 225)
    SetChrPos(0x103, -17620, -1000, 73700, 45)
    SetChrPos(0x104, -15540, -1000, 73630, 315)
    SetCameraDistance(18430, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#0003FOkay... Looks like that was\x01",
            "the last of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FExtermination complete...\x01",
            "I no longer detect the presence of\x01",
            "any monsters within the perimeter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0306FThey put up a good fight, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FIndeed. Fortunately, we were\x01",
            "able to manage just fine.\x02\x03",
            "Okay. Let's go give our\x01",
            "report to Chief Tolta.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FYeah. Hopefully, he'll have a bit\x01",
            "more peace of mind now.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0xD, 0x1, 0x2)
    SetChrPos(0x0, -17420, -1000, 75920, 135)
    ModifyEventFlags(1, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_11_1E8C end

    def Function_12_20E5(): pass

    label("Function_12_20E5")

    EventBegin(0x1)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Return to Armorica Village]\x01",      # 0
            "[Cancel]\x01",                          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2152")
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    OP_24(0x7B)
    WaitBGM()
    ClearMapFlags(0x8000000)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Jump("loc_2168")

    label("loc_2152")

    Sleep(50)
    SetChrPos(0x0, -26840, -140, 69350, 45)
    EventEnd(0x5)

    label("loc_2168")

    Return()

    # Function_12_20E5 end

    def Function_13_2169(): pass

    label("Function_13_2169")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(-21240, 2200, 44210, 0)
    MoveCamera(38, 8, 2, 0)
    OP_6E(600, 0)
    SetCameraDistance(13590, 0)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    LoadChrToIndex("apl/ch50387.itc", 0x1E)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, -22370, 0, 48680, 65)
    SetChrPos(0x102, -21150, 0, 47760, 65)
    SetChrPos(0x103, -21330, 0, 46270, 65)
    SetChrPos(0x104, -20270, 0, 45630, 65)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#6P#0100FYou know, now that I've had a chance\x01",
            "to soak in the sights, the rural scenery\x01",
            "here is lovely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FYou can say that again. Didn't have much\x01",
            "of a chance to really check it out last time,\x01",
            "considerin' we had monsters to take down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI suspect this location would provide a\x01",
            "perfect setting for a countryside picnic.\x02\x03",
            "However, there is a high probability\x01",
            "nearby monsters would ruin our fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FStill, though. I bet it'd be really fun\x01",
            "to drive down this road.\x02\x03",
            "Traders like Mr. Hayworth probably know\x01",
            "the ins and outs of Crossbell like the back\x01",
            "of their hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FI'm sure they do.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CB6")
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
    TurnDirection(0x104, 0x103, 500)

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
            "#6P#0106F*sigh* If only capturing a great\x01",
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
    OP_93(0x102, 0x41, 0x1F4)
    OP_93(0x101, 0x41, 0x1F4)
    OP_93(0x103, 0x41, 0x1F4)
    OP_93(0x104, 0x41, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x1E)
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
    Jump("loc_302F")

    label("loc_2CB6")

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
    OP_93(0x102, 0x41, 0x1F4)
    OP_93(0x101, 0x41, 0x1F4)
    OP_93(0x103, 0x41, 0x1F4)
    OP_93(0x104, 0x41, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x1E)
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
        "#6P#0103FPhew... I hope they turned out okay.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2E4C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_2E63")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2E7A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_2E91")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2EA8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2EA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_2EBF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2EBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_2ED6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2ED6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_2EED")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2EED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_2F04")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD1")

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
    Jump("loc_302F")

    label("loc_2FD1")


    ChrTalk(
        0x101,
        (
            "#6P#0000FNice, Elie! You looked pretty confident\x01",
            "taking that picture.\x02\x03",
            "Shall we move on?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_302F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -18960, 0, 48760, 90)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x1E)
    OP_29(0x18, 0x1, 0x2)
    Sleep(500)
    OP_37()
    ClearMapFlags(0x8000000)
    Call(0, 9)
    OP_65(0x7, 0x1)
    EventEnd(0x5)
    Return()

    # Function_13_2169 end

    def Function_14_306E(): pass

    label("Function_14_306E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_311C")
    EventBegin(0x1)
    Sound(810, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is locked.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Open]\x01",        # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3115")
    Sound(809, 0, 100, 0)
    Sleep(500)
    SetMapObjFrame(0xFF, "Null_door", 0x2, "anime")
    Sound(851, 0, 100, 0)
    Sleep(1500)
    SetScenarioFlags(0x0, 0)
    SetMapObjFrame(0xFF, "Null_door", 0x2, "open")
    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x4, 0x1)

    label("loc_3115")

    EventEnd(0x5)
    Jump("loc_315D")

    label("loc_311C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_3131")
    Call(0, 10)
    Jump("loc_315D")

    label("loc_3131")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_315D")

    Return()

    # Function_14_306E end

    SaveToFile()

Try(main)
