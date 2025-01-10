from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0010.bin",                # FileName
        "m0010",                    # MapName
        "m0010",                    # Location
        0x0067,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 103, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0010",                  # 0
        "bm0011",                 # 1
        "bm0011",                 # 2
        "bm0011",                 # 3
        "bm0011",                 # 4
        "bm0010",                 # 5
        "bm0010",                 # 6
        "bm0010",                 # 7
        "bm0010",                 # 8
        "bm0013",                 # 9
        "bm0013",                 # 10
        "bm0013",                 # 11
        "bm0013",                 # 12
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 14,  2,   10,  8,   2,   2,   0)
    Sepith("Sepith_B4", 4,   10,  14,  5,   2,   0,   2)
    Sepith("Sepith_C4", 7,   14,  6,   4,   0,   3,   3)
    Sepith("Sepith_D4", 0,   0,   0,   14,  8,   8,   8)

    MonsterBattlePostion("MonsterBattlePostion_E4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_108", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_10C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_110", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_114", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_118", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_11C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_124", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 9, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_144", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_148", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_14C", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_150", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_154", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_158", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_15C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 0, 0, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_164", 0x0000, 22, 6, 45, 4, 1, 25, 0, "bm0013", "Sepith_A4", 60, 30, 10, 0,
        (
            ("ms60400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60400.dat", "ms60400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60400.dat", "ms60400.dat", "ms60400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_200", 0x0000, 22, 6, 45, 4, 1, 30, 0, "bm0013", "Sepith_B4", 60, 30, 10, 0,
        (
            ("ms62000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62000.dat", "ms62000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62000.dat", "ms62000.dat", "ms62000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_29C", 0x0000, 22, 6, 45, 4, 1, 40, 0, "bm0011", "Sepith_C4", 60, 30, 10, 0,
        (
            ("ms69000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69000.dat", "ms69000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69000.dat", "ms75500.dat", "ms69000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_338", 0x0000, 22, 6, 45, 4, 1, 40, 0, "bm0010", "Sepith_D4", 60, 30, 10, 0,
        (
            ("ms75500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms75500.dat", "ms75500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms75500.dat", "ms75500.dat", "ms75500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3D4", 0x0000, 22, 6, 45, 4, 1, 25, 0, "bm0011", "Sepith_A4", 60, 30, 10, 0,
        (
            ("ms60400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60400.dat", "ms60400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60400.dat", "ms62000.dat", "ms60400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_470", 0x0000, 22, 6, 45, 4, 1, 40, 0, "bm0013", "Sepith_C4", 60, 30, 10, 0,
        (
            ("ms69000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69000.dat", "ms69000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69000.dat", "ms69000.dat", "ms69000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_50C", 0x0000, 22, 6, 45, 4, 1, 40, 0, "bm0011", "Sepith_D4", 60, 30, 10, 0,
        (
            ("ms75500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms75500.dat", "ms75500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms75500.dat", "ms60400.dat", "ms75500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
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
        "monster/ch69050.itc",               # 10
        "monster/ch69051.itc",               # 11
        "monster/ch62050.itc",               # 12
        "monster/ch62051.itc",               # 13
        "monster/ch60450.itc",               # 14
        "monster/ch60450.itc",               # 15
        "monster/ch75550.itc",               # 16
        "monster/ch75550.itc",               # 17
    ))

    DeclMonster(197620,  197110,  0,       0x1010000,    "BattleInfo_164", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(202780,  202660,  0,       0x1010000,    "BattleInfo_200", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-420,    -202500, 0,       0x1010000,    "BattleInfo_29C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(2070,    -398070, 100,     0x1010000,    "BattleInfo_338", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(98120,   -400140, 0,       0x1010000,    "BattleInfo_3D4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(203150,  -203670, 0,       0x1010000,    "BattleInfo_200", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(196930,  -197950, 0,       0x1010000,    "BattleInfo_470", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(199720,  -498190, 100,     0x1010000,    "BattleInfo_338", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(596800,  -203330, 0,       0x1010000,    "BattleInfo_164", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(601260,  -198470, 0,       0x1010000,    "BattleInfo_200", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(493500,  -398740, 0,       0x1010000,    "BattleInfo_29C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(499960,  -401800, 0,       0x1010000,    "BattleInfo_50C", 0,   22,  0xFFFF, 6,  7)

    DeclActor(200000,  0,       0,       1200,    200000,  1000,    0,       0x007C, 0,  3,  0x0000)
    DeclActor(100000,  0,       -100000, 1200,    100000,  1000,    -100000, 0x007C, 0,  4,  0x0000)
    DeclActor(200000,  0,       -500000, 1200,    200000,  1000,    -500000, 0x007C, 0,  5,  0x0000)
    DeclActor(0,       0,       2000,    1200,    0,       1000,    2500,    0x007C, 0,  6,  0x0000)
    DeclActor(602000,  0,       -400000, 1200,    602500,  1000,    -400000, 0x007C, 0,  8,  0x0000)
    DeclActor(207100,  12000,   -393000, 2000,    207100,  13000,   -393000, 0x007C, 0,  10, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_8F0",          # 00, 0
        "Function_1_963",          # 01, 1
        "Function_2_10BA",         # 02, 2
        "Function_3_1172",         # 03, 3
        "Function_4_12DB",         # 04, 4
        "Function_5_1465",         # 05, 5
        "Function_6_161A",         # 06, 6
        "Function_7_17A1",         # 07, 7
        "Function_8_18E8",         # 08, 8
        "Function_9_1A71",         # 09, 9
        "Function_10_1BB8",        # 0A, 10
        "Function_11_1E12",        # 0B, 11
    ))


    def Function_0_8F0(): pass

    label("Function_0_8F0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_937")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91D")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)
    Jump("loc_937")

    label("loc_91D")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_937")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)

    label("loc_937")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_948")
    SetScenarioFlags(0x54, 0)

    label("loc_948")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_962")
    Event(0, 11)

    label("loc_962")

    Return()

    # Function_0_8F0 end

    def Function_1_963(): pass

    label("Function_1_963")

    SetMapObjFrame(0x9, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0xA, "m00ele00", 0x2, "up_kp")
    SetBarrier(0x0, 0x0, 0x1, 0x0, 196000, 12000, -400000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 200000, 12000, -396000, 4000, 2000, 0)
    SetBarrier(0x0, 0x2, 0x1, 0x0, 204000, 12000, -400000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x3, 0x1, 0x0, 196000, -2000, -400000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x4, 0x1, 0x0, 200000, -2000, -396000, 4000, 2000, 0)
    SetBarrier(0x0, 0x5, 0x1, 0x0, 204000, -2000, -400000, 4000, 2000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 1)), scpexpr(EXPR_END)), "loc_A7E")
    SetMapObjFrame(0xB, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "obj01", 0x2, "up_kp")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    Jump("loc_ABA")

    label("loc_A7E")

    SetMapObjFrame(0xB, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "obj01", 0x2, "down_kp")
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)

    label("loc_ABA")

    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 0)), scpexpr(EXPR_END)), "loc_B25")
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign00", 0x1, 0x1)
    SetMapObjFrame(0x1, "light00", 0x1, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_B65")

    label("loc_B25")

    SetMapObjFrame(0x1, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x1, "light00", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x1, 0x1)
    SetMapObjFrame(0x1, "light01", 0x1, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_B65")

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
    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1084")
    OP_70(0xC, 0x0)
    Jump("loc_1088")

    label("loc_1084")

    OP_70(0xC, 0x1E)

    label("loc_1088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109B")
    OP_70(0xD, 0x0)
    Jump("loc_109F")

    label("loc_109B")

    OP_70(0xD, 0x1E)

    label("loc_109F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B2")
    OP_70(0xE, 0x0)
    Jump("loc_10B6")

    label("loc_10B2")

    OP_70(0xE, 0x1E)

    label("loc_10B6")

    Call(0, 2)
    Return()

    # Function_1_963 end

    def Function_2_10BA(): pass

    label("Function_2_10BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8B), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x91), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10DC")
    SetMapObjFlags(0xC, 0x4)
    Jump("loc_10E2")

    label("loc_10DC")

    ClearMapObjFlags(0xC, 0x4)

    label("loc_10E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1103")
    SetChrFlags(0xB, 0x8)
    Jump("loc_1108")

    label("loc_1103")

    ClearChrFlags(0xB, 0x8)

    label("loc_1108")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1129")
    SetChrFlags(0xD, 0x8)
    Jump("loc_112E")

    label("loc_1129")

    ClearChrFlags(0xD, 0x8)

    label("loc_112E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1146")
    SetChrFlags(0xF, 0x8)
    Jump("loc_114B")

    label("loc_1146")

    ClearChrFlags(0xF, 0x8)

    label("loc_114B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x81), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_116C")
    SetChrFlags(0x10, 0x8)
    Jump("loc_1171")

    label("loc_116C")

    ClearChrFlags(0x10, 0x8)

    label("loc_1171")

    Return()

    # Function_2_10BA end

    def Function_3_1172(): pass

    label("Function_3_1172")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125C")
    Sound(14, 0, 100, 0)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_11F2")
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
    SetScenarioFlags(0x10B, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1257")

    label("loc_11F2")

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
    OP_71(0xC, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1257")

    Jump("loc_12CF")

    label("loc_125C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Luck skill checked...\x01",
            "Luck skill check failed.\x01",
            "The chest is still empty.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_12CF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1172 end

    def Function_4_12DB(): pass

    label("Function_4_12DB")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C5")
    Sound(14, 0, 100, 0)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3E, 1)"), scpexpr(EXPR_END)), "loc_135B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x3E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10B, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_13C0")

    label("loc_135B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x3E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xD, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13C0")

    Jump("loc_1459")

    label("loc_13C5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You find fingerprints inside the chest that point to\x01",
            "the likely culprit. Three guesses as to who that is.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1459")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_12DB end

    def Function_5_1465(): pass

    label("Function_5_1465")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_154F")
    Sound(14, 0, 100, 0)
    OP_71(0xE, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E4, 1)"), scpexpr(EXPR_END)), "loc_14E5")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5E4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10B, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_154A")

    label("loc_14E5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5E4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xE, 0x1E, 0x0, 0x0, 0x0)

    label("loc_154A")

    Jump("loc_160E")

    label("loc_154F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You are sucked into the chest. A teacher forces\x01",
            "you to write 'I will not steal from treasure chests'\x01",
            "100 times on a chalkboard before you can leave.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_160E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1465 end

    def Function_6_161A(): pass

    label("Function_6_161A")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1799")
    Fade(500)
    SetChrPos(0x0, -600, 0, 600, 0)
    SetChrPos(0x1, 600, 0, 600, 0)
    SetChrPos(0x2, -600, 0, -600, 0)
    SetChrPos(0x3, 600, 0, -600, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16F9")
    SetChrPos(0x4, -600, 0, -1800, 0)
    SetChrPos(0x5, 600, 0, -1800, 0)
    Jump("loc_1718")

    label("loc_16F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1718")
    SetChrPos(0x4, 0, 0, -1800, 0)

    label("loc_1718")

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
    SetMapObjFrame(0x9, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0001", 0, 0, 0)
    IdleLoop()

    label("loc_1799")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_161A end

    def Function_7_17A1(): pass

    label("Function_7_17A1")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0x9, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(600, 11000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, -600, 30000, 600, 0)
    OP_90(0x1, 600, 30000, 600, 0)
    OP_90(0x2, -600, 30000, -600, 0)
    OP_90(0x3, 600, 30000, -600, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1874")
    OP_90(0x4, -600, 30000, -1800, 0)
    OP_90(0x5, 600, 30000, -1800, 0)
    Jump("loc_1893")

    label("loc_1874")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1893")
    OP_90(0x4, 0, 30000, -1800, 0)

    label("loc_1893")

    Sound(145, 0, 100, 0)
    OP_68(600, 1000, 0, 3000)
    SetMapObjFrame(0x9, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x9)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_17A1 end

    def Function_8_18E8(): pass

    label("Function_8_18E8")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A69")
    Fade(500)
    SetChrPos(0x0, 600600, 0, -400600, 90)
    SetChrPos(0x1, 600600, 0, -399400, 90)
    SetChrPos(0x2, 599400, 0, -400600, 90)
    SetChrPos(0x3, 599400, 0, -399400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C7")
    SetChrPos(0x4, 598200, 0, -400600, 90)
    SetChrPos(0x5, 598200, 0, -399400, 90)
    Jump("loc_19E6")

    label("loc_19C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E6")
    SetChrPos(0x4, 598200, 0, -400000, 90)

    label("loc_19E6")

    OP_68(600000, 0, -400000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(600000, -5000, -400000, 2000)
    SetMapObjFrame(0xA, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0011", 0, 0, 0)
    IdleLoop()

    label("loc_1A69")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_18E8 end

    def Function_9_1A71(): pass

    label("Function_9_1A71")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xA, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(600000, -5000, -400000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600600, -10000, -400600, 90)
    OP_90(0x1, 600600, -10000, -399400, 90)
    OP_90(0x2, 599400, -10000, -400600, 90)
    OP_90(0x3, 599400, -10000, -399400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B46")
    OP_90(0x4, 598200, 30000, -400600, 90)
    OP_90(0x5, 598200, 30000, -399400, 90)
    Jump("loc_1B65")

    label("loc_1B46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B65")
    OP_90(0x4, 598200, 30000, -400000, 90)

    label("loc_1B65")

    Sound(145, 0, 100, 0)
    OP_68(600000, 0, -400000, 3000)
    SetMapObjFrame(0xA, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xA)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1A71 end

    def Function_10_1BB8(): pass

    label("Function_10_1BB8")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lift control valve.\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E0A")
    Fade(500)
    SetChrPos(0x0, 205650, 12000, -394120, 45)
    SetChrPos(0x1, 204410, 12000, -393450, 90)
    SetChrPos(0x2, 204340, 12000, -392080, 90)
    SetChrPos(0x3, 202600, 12000, -393170, 90)
    OP_68(205850, 13000, -393690, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 1)), scpexpr(EXPR_END)), "loc_1D52")
    SetMapObjFrame(0xB, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    Fade(500)
    OP_68(198660, 13000, -400580, 0)
    MoveCamera(45, 56, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(29000, 0)
    Sleep(500)
    OP_0D()
    Sound(146, 2, 100, 0)
    SetMapObjFrame(0xFF, "obj01", 0x2, "down")
    Sleep(5000)
    OP_24(0x92)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_6F(0x1)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    ClearScenarioFlags(0x54, 1)
    Jump("loc_1E0A")

    label("loc_1D52")

    SetMapObjFrame(0xB, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    Fade(500)
    OP_68(198660, 13000, -400580, 0)
    MoveCamera(45, 56, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(29000, 0)
    Sleep(500)
    OP_0D()
    Sound(146, 2, 100, 0)
    SetMapObjFrame(0xFF, "obj01", 0x2, "up")
    Sleep(6000)
    OP_24(0x92)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_6F(0x1)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetScenarioFlags(0x54, 1)

    label("loc_1E0A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1BB8 end

    def Function_11_1E12(): pass

    label("Function_11_1E12")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(106000, 1800, 0, 0)
    MoveCamera(55, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 83500, 150, -400, 90)
    SetChrPos(0x103, 83500, 150, 400, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(100000, 1800, 0, 8000)
    MoveCamera(65, 11, 0, 8000)
    SetCameraDistance(21000, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(85800, 1100, 0, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)

    def lambda_1EEF():
        OP_96(0xFE, 0x14F28, 0x0, 0xFFFFFDA8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EEF)

    def lambda_1F09():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F09)
    Sleep(400)

    def lambda_1F1D():
        OP_96(0xFE, 0x14F28, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F1D)

    def lambda_1F37():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1F37)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x101,
        (
            "#3300272V#6P#0008FYou know, compared to the upper levels,\x01",
            "the lighting system here seems more dated...\x02\x03",
            "#3300273V#0000FAre the lower levels older or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300274V#0203F#5PYes. The lower stratums were the\x01",
            "first Geofront sections to be built.\x02\x03",
            "#3300275V#0200FThe Geofront, as a whole, is the product of an\x01",
            "urban planning project that spans 20 years...\x02\x03",
            "#3300276VDue to its construction undergoing some\x01",
            "spontaneous changes, the entire structure\x01",
            "became more complex than originally intended.\x02\x03",
            "#3300277V#0206FIn fact, Elie told me stories about how the\x01",
            "construction of the Geofront was manipulated\x01",
            "by all sorts of diet members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300278V#6P#0006FIs that so...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3300279V#12P#0001FStill, the sheer size of this place\x01",
            "never fails to surprise me.\x02\x03",
            "#3300280VDid you really think you would\x01",
            "be okay going at this alone, Tio?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#3300281V#0208F#5PWell...\x02\x03",
            "#3300282V#0206FNo. My apologies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300283V#12P#0012FIt's fine, Tio.\x02\x03",
            "#3300284V#0000FThe last thing I want is for you to\x01",
            "get hurt, okay?\x02\x03",
            "#3300285VStay behind me, and I'll protect you.\x01",
            "I promise you that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300286V#0202F#5PUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#3300287V#0203F#5PUm, Lloyd...\x02\x03",
            "#3300288V#0201FWould you like to practice a combination\x01",
            "craft while we are here?\x02\x03",
            "#3300289VI may not be as proficient as Randy or Elie,\x01",
            "but I would still like to try...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3300290V#12P#0002FThat's a great idea.\x02\x03",
            "#3300291V#0014FSince we're by ourselves, let's give it a shot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300292V#0202F#5PRoger!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 3)), scpexpr(EXPR_END)), "loc_2604")
    AddCraft(0x0, 0x155)
    AddCraft(0x2, 0x155)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Tio learned \x07\x02",
            "[Omega Strike 2]\x07\x05",
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By spending 100 CP each, a powerful\x01",
            "combination attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_269B")

    label("loc_2604")

    AddCraft(0x0, 0x14B)
    AddCraft(0x2, 0x14B)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Tio learned \x07\x02",
            "[Omega Strike]\x07\x05",
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By spending 100 CP each, a powerful\x01",
            "combination attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_269B")

    SetChrPos(0x0, 85800, 0, 0, 90)
    SetScenarioFlags(0xA1, 0)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_11_1E12 end

    SaveToFile()

Try(main)
