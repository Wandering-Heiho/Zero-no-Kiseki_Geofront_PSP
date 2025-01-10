from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0001.bin",                # FileName
        "m0001",                    # MapName
        "m0001",                    # Location
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
        "m0001",                  # 0
        "Anri",                   # 1
        "bm0001",                 # 2
        "bm0001",                 # 3
        "bm0001",                 # 4
        "bm0001",                 # 5
        "bm0000",                 # 6
        "bm0000",                 # 7
        "bm0000",                 # 8
        "bm0000",                 # 9
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 1,   2,   0,   4,   1,   1,   0)
    Sepith("Sepith_B4", 3,   1,   2,   0,   1,   2,   1)
    Sepith("Sepith_C4", 1,   4,   0,   2,   0,   2,   1)
    Sepith("Sepith_D4", 2,   0,   3,   2,   1,   0,   2)

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
        "BattleInfo_1A4", 0x0000, 3, 6, 45, 10, 1, 30, 0, "bm0001", "Sepith_A4", 75, 25, 0, 0,
        (
            ("ms60300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60300.dat", "ms60300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_214", 0x0000, 3, 6, 45, 10, 1, 40, 0, "bm0000", "Sepith_B4", 75, 25, 0, 0,
        (
            ("ms60100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60100.dat", "ms60100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_284", 0x0000, 3, 6, 45, 10, 1, 25, 0, "bm0000", "Sepith_C4", 100, 0, 0, 0,
        (
            ("ms73100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2C8", 0x0000, 3, 6, 45, 10, 1, 40, 0, "bm0001", "Sepith_D4", 75, 25, 0, 0,
        (
            ("ms61700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61700.dat", "ms61700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_338", 0x0000, 3, 6, 45, 10, 1, 40, 0, "bm0000", "Sepith_D4", 75, 25, 0, 0,
        (
            ("ms61700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61700.dat", "ms61700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3A8", 0x0000, 3, 6, 45, 10, 1, 30, 0, "bm0000", "Sepith_A4", 75, 25, 0, 0,
        (
            ("ms60300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60300.dat", "ms60300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_164", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch22200.itc",                   # 00
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(40,      97290,   0,       0x1010000,    "BattleInfo_1A4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(6830,    199320,  12000,   0x1010000,    "BattleInfo_214", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-7490,   199510,  12000,   0x1010000,    "BattleInfo_284", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(98790,   -400,    0,       0x1010000,    "BattleInfo_2C8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(199650,  -460,    100,     0x1010000,    "BattleInfo_338", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(2370,    202390,  -2000,   0x1010000,    "BattleInfo_3A8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-4410,   195610,  -2000,   0x1010000,    "BattleInfo_338", 0,   22,  0xFFFF, 6,  7)

    DeclActor(14000,   0,       502000,  1200,    14000,   1000,    502500,  0x007C, 0,  8,  0x0000)
    DeclActor(2000,    0,       0,       1200,    2500,    1000,    0,       0x007C, 0,  10, 0x0000)
    DeclActor(0,       0,       522000,  1200,    0,       1000,    522500,  0x007C, 0,  12, 0x0000)
    DeclActor(3230,    0,       309620,  1200,    3230,    1500,    309620,  0x007C, 0,  7,  0x0000)
    DeclActor(6870,    12000,   206910,  1200,    6870,    13000,   206910,  0x007C, 0,  3,  0x0000)
    DeclActor(198210,  3800,    193730,  1200,    198210,  4800,    193730,  0x007C, 0,  4,  0x0000)
    DeclActor(202520,  0,       5210,    1200,    202520,  1000,    5210,    0x007C, 0,  5,  0x0000)
    DeclActor(0,       -2000,   192500,  1200,    0,       -1000,   192500,  0x007C, 0,  6,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3])                         # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_73C",          # 00, 0
        "Function_1_7DC",          # 01, 1
        "Function_2_C10",          # 02, 2
        "Function_3_CFC",          # 03, 3
        "Function_4_EAC",          # 04, 4
        "Function_5_100C",         # 05, 5
        "Function_6_1164",         # 06, 6
        "Function_7_126B",         # 07, 7
        "Function_8_136B",         # 08, 8
        "Function_9_14F2",         # 09, 9
        "Function_10_1639",        # 0A, 10
        "Function_11_17C0",        # 0B, 11
        "Function_12_1907",        # 0C, 12
        "Function_13_1B2C",        # 0D, 13
        "Function_14_1C73",        # 0E, 14
        "Function_15_20FC",        # 0F, 15
        "Function_16_38FC",        # 10, 16
        "Function_17_3C83",        # 11, 17
    ))


    def Function_0_73C(): pass

    label("Function_0_73C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A2")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_769")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)
    Jump("loc_7A2")

    label("loc_769")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_788")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)
    Jump("loc_7A2")

    label("loc_788")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A2")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)

    label("loc_7A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x81), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C1")
    Event(0, 15)
    Jump("loc_7DB")

    label("loc_7C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DB")
    Event(0, 14)

    label("loc_7DB")

    Return()

    # Function_0_73C end

    def Function_1_7DC(): pass

    label("Function_1_7DC")

    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0xC, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0xD, "m00ele00", 0x2, "up_kp")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_988")
    SetMapObjFrame(0xD, "up", 0x0, 0x1)
    SetMapObjFrame(0xD, "down", 0x0, 0x1)
    SetMapObjFrame(0xD, "gauge", 0x0, 0x1)

    label("loc_988")

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
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAB")
    OP_70(0xF, 0x0)
    Jump("loc_BAF")

    label("loc_BAB")

    OP_70(0xF, 0x1E)

    label("loc_BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC2")
    OP_70(0x10, 0x0)
    Jump("loc_BC6")

    label("loc_BC2")

    OP_70(0x10, 0x1E)

    label("loc_BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD9")
    OP_70(0x11, 0x0)
    Jump("loc_BDD")

    label("loc_BD9")

    OP_70(0x11, 0x1E)

    label("loc_BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF0")
    OP_70(0x12, 0x0)
    Jump("loc_BF4")

    label("loc_BF0")

    OP_70(0x12, 0x1E)

    label("loc_BF4")

    OP_1B(0xA, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0C")
    OP_1B(0xA, 0x0, 0x11)

    label("loc_C0C")

    Call(0, 2)
    Return()

    # Function_1_7DC end

    def Function_2_C10(): pass

    label("Function_2_C10")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C31")
    SetChrFlags(0xC, 0x8)
    Jump("loc_C36")

    label("loc_C31")

    ClearChrFlags(0xC, 0x8)

    label("loc_C36")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C5D")
    SetChrFlags(0xD, 0x8)
    SetMapObjFlags(0x11, 0x4)
    Jump("loc_C68")

    label("loc_C5D")

    ClearChrFlags(0xD, 0x8)
    ClearMapObjFlags(0x11, 0x4)

    label("loc_C68")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9C")
    SetMapObjFlags(0x10, 0x4)
    Jump("loc_CA2")

    label("loc_C9C")

    ClearMapObjFlags(0x10, 0x4)

    label("loc_CA2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE1")
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetMapObjFlags(0xF, 0x4)
    Jump("loc_CFB")

    label("loc_CE1")

    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearMapObjFlags(0xF, 0x4)

    label("loc_CFB")

    Return()

    # Function_2_C10 end

    def Function_3_CFC(): pass

    label("Function_3_CFC")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E30")
    Sound(14, 0, 100, 0)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xF, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 20)
    AddSepith(0x1, 20)
    AddSepith(0x2, 20)
    AddSepith(0x3, 20)
    AddSepith(0x4, 20)
    AddSepith(0x5, 20)
    AddSepith(0x6, 20)

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
            " x20\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x20\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x20\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x20.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10A, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_E9A")

    label("loc_E30")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Why do they call it the GeoFRONT if it's under the city?\x01",
            "...Thank you. I'll be here all game.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_E9A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_CFC end

    def Function_4_EAC(): pass

    label("Function_4_EAC")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F96")
    Sound(14, 0, 100, 0)
    OP_71(0x10, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x41, 1)"), scpexpr(EXPR_END)), "loc_F2C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10A, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_F91")

    label("loc_F2C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x10, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F91")

    Jump("loc_1000")

    label("loc_F96")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You'll take a lost child with you, but not me.\x01",
            "I see how it is.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1000")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_EAC end

    def Function_5_100C(): pass

    label("Function_5_100C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F6")
    Sound(14, 0, 100, 0)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F4, 1)"), scpexpr(EXPR_END)), "loc_108C")
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
    SetScenarioFlags(0x10A, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_10F1")

    label("loc_108C")

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
    OP_71(0x11, 0x1E, 0x0, 0x0, 0x0)

    label("loc_10F1")

    Jump("loc_1158")

    label("loc_10F6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Phase 1: Collect Tear Balm\x01",
            "Phase 2: ???\x01",
            "Phase 3: Profit\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1158")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_100C end

    def Function_6_1164(): pass

    label("Function_6_1164")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D9")
    Sound(14, 0, 100, 0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x12, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddItemNumber(0x20E, 5)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x20E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10A, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_1259")

    label("loc_11D9")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Battle Scopes are one way you can scan enemies for the\x01",
            "Combat Notebook. You should probably get on that, Detective.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1259")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1164 end

    def Function_7_126B(): pass

    label("Function_7_126B")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_134E")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0xE, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0xE, 0x0)
    OP_71(0xE, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xE)
    OP_71(0xE, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0xE, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_134E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_136A")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_136A")

    Return()

    # Function_7_126B end

    def Function_8_136B(): pass

    label("Function_8_136B")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14EA")
    Fade(500)
    SetChrPos(0x0, 13400, 0, 500600, 0)
    SetChrPos(0x1, 14600, 0, 500600, 0)
    SetChrPos(0x2, 13400, 0, 499400, 0)
    SetChrPos(0x3, 14600, 0, 499400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_144A")
    SetChrPos(0x4, 13400, 0, 498200, 0)
    SetChrPos(0x5, 14600, 0, 498200, 0)
    Jump("loc_1469")

    label("loc_144A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1469")
    SetChrPos(0x4, 14000, 0, 498200, 0)

    label("loc_1469")

    OP_68(14000, 1000, 500000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(14000, 6000, 500000, 3000)
    SetMapObjFrame(0xB, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0000", 0, 0, 0)
    IdleLoop()

    label("loc_14EA")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_136B end

    def Function_9_14F2(): pass

    label("Function_9_14F2")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0xB, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(14000, 11000, 500000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 13400, 30000, 500600, 0)
    OP_90(0x1, 14600, 30000, 500600, 0)
    OP_90(0x2, 13400, 30000, 499400, 0)
    OP_90(0x3, 14600, 30000, 499400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C5")
    OP_90(0x4, 13400, 30000, 498200, 0)
    OP_90(0x5, 14600, 30000, 498200, 0)
    Jump("loc_15E4")

    label("loc_15C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E4")
    OP_90(0x4, 14000, 30000, 498200, 0)

    label("loc_15E4")

    Sound(145, 0, 100, 0)
    OP_68(14000, 1000, 500000, 3000)
    SetMapObjFrame(0xB, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xB)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_14F2 end

    def Function_10_1639(): pass

    label("Function_10_1639")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B8")
    Fade(500)
    SetChrPos(0x0, 600, 0, -600, 90)
    SetChrPos(0x1, 600, 0, 600, 90)
    SetChrPos(0x2, -600, 0, -600, 90)
    SetChrPos(0x3, -600, 0, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1718")
    SetChrPos(0x4, -1800, 0, -600, 90)
    SetChrPos(0x5, -1800, 0, 600, 90)
    Jump("loc_1737")

    label("loc_1718")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1737")
    SetChrPos(0x4, -1800, 0, 0, 90)

    label("loc_1737")

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
    SetMapObjFrame(0xC, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0000", 0, 0, 0)
    IdleLoop()

    label("loc_17B8")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1639 end

    def Function_11_17C0(): pass

    label("Function_11_17C0")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(600, 11000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, 30000, -600, 90)
    OP_90(0x1, 600, 30000, 600, 90)
    OP_90(0x2, -600, 30000, -600, 90)
    OP_90(0x3, -600, 30000, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1893")
    OP_90(0x4, -1800, 30000, -600, 90)
    OP_90(0x5, -1800, 30000, 600, 90)
    Jump("loc_18B2")

    label("loc_1893")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B2")
    OP_90(0x4, -1800, 30000, 0, 90)

    label("loc_18B2")

    Sound(145, 0, 100, 0)
    OP_68(600, 1000, 0, 3000)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xC)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_17C0 end

    def Function_12_1907(): pass

    label("Function_12_1907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_191D")
    Call(0, 16)
    Jump("loc_1B2B")

    label("loc_191D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 7)), scpexpr(EXPR_END)), "loc_1AB3")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA7")
    Fade(500)
    SetChrPos(0x0, -600, 0, 520600, 0)
    SetChrPos(0x1, 600, 0, 520600, 0)
    SetChrPos(0x2, -600, 0, 519400, 0)
    SetChrPos(0x3, 600, 0, 519400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A05")
    SetChrPos(0x4, -600, 0, 518200, 0)
    SetChrPos(0x5, 600, 0, 518200, 0)
    Jump("loc_1A24")

    label("loc_1A05")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A24")
    SetChrPos(0x4, 0, 0, 518200, 0)

    label("loc_1A24")

    OP_68(0, 0, 520000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(0, -5000, 520000, 2000)
    SetMapObjFrame(0xD, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0010", 0, 0, 0)
    IdleLoop()

    label("loc_1AA7")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_1B2B")

    label("loc_1AB3")

    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pressing the button does nothing.\x01",
            "The elevator cannot be used at the moment.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B23")
    SetScenarioFlags(0x53, 3)

    label("loc_1B23")

    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)

    label("loc_1B2B")

    Return()

    # Function_12_1907 end

    def Function_13_1B2C(): pass

    label("Function_13_1B2C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xD, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(0, -5000, 520000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, -600, -10000, 520600, 0)
    OP_90(0x1, 600, -10000, 520600, 0)
    OP_90(0x2, -600, -10000, 519400, 0)
    OP_90(0x3, 600, -10000, 519400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C01")
    OP_90(0x4, -600, -10000, 518200, 0)
    OP_90(0x5, 600, -10000, 518200, 0)
    Jump("loc_1C20")

    label("loc_1C01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C20")
    OP_90(0x4, 0, -10000, 518200, 0)

    label("loc_1C20")

    Sound(145, 0, 100, 0)
    OP_68(0, 0, 520000, 3000)
    SetMapObjFrame(0xD, "m00ele00", 0x2, "up")
    FadeToBright(1000, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xD)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_1B2C end

    def Function_14_1C73(): pass

    label("Function_14_1C73")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(200000, 900, 191200, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 199400, 0, 190000, 0)
    SetChrPos(0x102, 200600, 0, 190000, 0)
    SetChrPos(0x103, 199400, 0, 190000, 0)
    SetChrPos(0x104, 200600, 0, 190000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(200000, 900, 193200, 3000)

    def lambda_1D3E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D3E)

    def lambda_1D4F():
        OP_95(0xFE, 199400, 0, 193200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D4F)
    Sleep(300)

    def lambda_1D6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1D6C)

    def lambda_1D7D():
        OP_95(0xFE, 200600, 0, 193200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D7D)
    Sleep(1000)

    def lambda_1D9A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1D9A)

    def lambda_1DAB():
        OP_95(0xFE, 199400, 0, 192000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DAB)
    Sleep(300)

    def lambda_1DC8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1DC8)

    def lambda_1DD9():
        OP_95(0xFE, 200600, 0, 192000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1DD9)
    WaitChrThread(0x101, 1)
    SetMessageWindowPos(16, 16, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        "#0100515V#2S*sob* *sob*...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
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
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#0100516V#12P#0001FDid you hear that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100517V#0105F#11PListen! Someone's crying...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#0100518V#11P#0306FGeez. The hell is goin' on?\x02\x03",
            "#0100519V#0301FAin't this place supposed to be\x01",
            "sealed off from the public?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#0100520V#6P#0206F#6PNo point in complaining to me.\x02\x03",
            "#0100521V#0200FAs far as I know, the general public should\x01",
            "not have access to the Geofront...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2038():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2038)
    Sleep(100)
    TurnDirection(0x102, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#0100522V#6P#0001FSave the speculation for later!\x02\x03",
            "#0100523VWe need to find the source of\x01",
            "that crying, stat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100524V#5P#0101FRight!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 200000, 0, 192200, 0)
    SetScenarioFlags(0x40, 6)
    OP_29(0x3C, 0x1, 0x2)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_14_1C73 end

    def Function_15_20FC(): pass

    label("Function_15_20FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(201300, 5500, 399300, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 210700, 4500, 399300, 90)
    OP_A7(0x8, 0x0, 0x0, 0x0, 0xFF, 0x0)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x103, 0x40)
    SetChrFlags(0x104, 0x40)
    SetChrPos(0x101, 199800, 4500, 399000, 90)
    SetChrPos(0x102, 199500, 4500, 399800, 90)
    SetChrPos(0x103, 198400, 4500, 399000, 90)
    SetChrPos(0x104, 197800, 4500, 399800, 90)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x8,
        "Boy",
        "#0100525V#3P*sob* *sniff*...\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2231():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2231)
    OP_68(210700, 5500, 399300, 3000)
    SetCameraDistance(24000, 3000)
    OP_6F(0x11)

    NpcTalk(
        0x8,
        "Boy",
        (
            "#0100526VWhat do I do...?\x01",
            "If this keeps up, I'm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100527V#0007FHey! Is someone there?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xC8, 0xBB8)
    Sleep(500)
    OP_93(0x8, 0x10E, 0x1F4)

    NpcTalk(
        0x8,
        "Boy",
        "#0100528V#11P...!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Boy",
        "#0100529V#11PWh-Who's there?!\x02",
    )

    CloseMessageWindow()
    OP_68(209000, 5500, 399300, 2000)

    def lambda_2352():
        OP_97(0xFE, 0x2134, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2352)
    Sleep(50)

    def lambda_236F():
        OP_97(0xFE, 0x2134, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_236F)
    Sleep(50)

    def lambda_238C():
        OP_97(0xFE, 0x2134, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_238C)
    Sleep(50)

    def lambda_23A9():
        OP_97(0xFE, 0x2134, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23A9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#0100530V#6P#0006FThank goodness. Someone really was in here.\x02\x03",
            "#0100531V#0001FAre you okay? You aren't hurt, are you?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Boy",
        "#0100532V#11P*sob*...\x02",
    )

    CloseMessageWindow()

    def lambda_246F():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_246F)
    OP_82(0x0, 0x64, 0xBB8, 0x3E8)

    NpcTalk(
        0x8,
        "Boy",
        "#0100533V#11P#4SWaaaahhhh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100534V#6P#0011FE-Easy there...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100535V#3P#0305FPoor kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100536V#0106FHe can relax now that he's safe.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#0100537V#0100F#5PI'll take care of this, Lloyd.\x02",
    )

    CloseMessageWindow()

    def lambda_257D():

        label("loc_257D")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_257D")

    QueueWorkItem2(0x101, 2, lambda_257D)
    Sleep(100)

    ChrTalk(
        0x101,
        "#0100538V#12P#0005FO-Okay, go ahead.\x02",
    )

    CloseMessageWindow()
    OP_68(209710, 5500, 399580, 1500)

    def lambda_25CD():
        OP_95(0xFE, 210300, 4500, 399700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_25CD)
    WaitChrThread(0x102, 1)
    EndChrThread(0x101, 0x2)

    def lambda_25EF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_25EF)
    TurnDirection(0x102, 0x8, 500)

    ChrTalk(
        0x102,
        (
            "#0100539V#5P#0104FThere, there. I know you were scared.\x02\x03",
            "#0100540VEverything is okay now, I promise...\x01",
            "We're all here. We'll protect you.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Boy",
        "#0100541V*sob* *hic*...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Boy",
        "#0100542V*nod*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100543V#5P#0102FWe took care of all the scary\x01",
            "monsters outside.\x02\x03",
            "#0100544VIt's so dark and cramped in here.\x01",
            "How about we head for the exit?\x02\x03",
            "#0100545VHere, I can carry you if you want.\x01",
            "Make sure to hold on tight, okay?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Boy",
        "#0100546VI-I'm fine...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Boy",
        "#0100547VI can walk by myself!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    ChrTalk(
        0x102,
        (
            "#0100548V#5P#0109FYou sure? Heehee. You're such\x01",
            "a brave boy.\x02\x03",
            "#0100549V#0102FWhat's your name?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Boy",
        "#0100550VU-Um... It's Anri.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100551V#6P#0012F(Haha... Phew.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100552V#3P#0302F(Well, ain't this a charmin' sight.)\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(198000, 900, 202000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x8, 198000, 0, 203200, 180)
    SetChrPos(0x101, 199700, 0, 201300, 315)
    SetChrPos(0x102, 198000, 0, 201200, 0)
    SetChrPos(0x103, 197400, 0, 199800, 0)
    SetChrPos(0x104, 198700, 0, 199600, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    SetCameraDistance(21000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x102,
        (
            "#0100553V#12P#0100FWell, then, Anri. Can you tell me how\x01",
            "you ended up in a place like this?\x02\x03",
            "#0100554VThe Geofront should have been locked,\x01",
            "so how did you manage to get inside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0100555V#5PUm, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100556V#5PWe were playing near the\x01",
            "big bell in Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100557V#5PWhen we opened this weird lid on the ground,\x01",
            "we found a ladder leading down here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0100558V#5PA-And then...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C0B")

    ChrTalk(
        0x104,
        (
            "#0100559V#4P#0300FAh, your adventuring spirit was lit.\x01",
            "I can't blame you, kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100560V#12P#0205FA manhole down to the Geofront...?\x02\x03",
            "#0100561V#0203FI should add that to the database.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CAD")

    label("loc_2C0B")


    ChrTalk(
        0x104,
        (
            "#0100562V#4P#0300FSo, you decided to see where that\x01",
            "manhole led, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100563V#12P#0203FAll the more reason to add that\x01",
            "entrance to the database later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CAD")


    ChrTalk(
        0x101,
        (
            "#0100564V#11P#0001FBack up just a second!\x02\x03",
            "#0100565VYou said 'we'... Are you saying you\x01",
            "didn't come down here alone?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0100566V#6P#0105F...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        "#0100567V#5PY-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100568V#5PMy friend Ryu said we were\x01",
            "going on an adventure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100569V#5PB-But, when we got down here, we\x01",
            "ran into monsters and got separated!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0100570V#5P*sob*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100571V#12P#0103FSo, that's the full story...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#0100572V#6P#0101FLloyd, what should we do?\x02",
    )

    CloseMessageWindow()

    def lambda_2EE2():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2EE2)
    Sleep(50)

    def lambda_2EF2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2EF2)
    Sleep(50)

    def lambda_2F02():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2F02)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x101,
        "#0100573V#11P#0003FLet me think...\x02",
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
            "[Take Anri back now]\x01",            # 0
            "[Search for Ryu with Anri]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FA0"),
        (1, "loc_32D0"),
        (SWITCH_DEFAULT, "loc_3591"),
    )


    label("loc_2FA0")


    ChrTalk(
        0x101,
        (
            "#0100574V#11P#0008FFor now, we should escort Anri\x01",
            "back to the surface.\x02\x03",
            "#0100575V#0001FWe can't leave him here, and it'd be\x01",
            "too dangerous to bring him along\x01",
            "while searching for the other kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100576V#6P#0200FIs that really okay?\x02\x03",
            "#0100577VWhat if the other boy gets injured while\x01",
            "we are taking Anri back up...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30E8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30E8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0100578V#5P#0005FGood point...\x02\x03",
            "#0100579V#0008F...but I think it'd be worse to divide the\x01",
            "team here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100580V#4P#0306FWe still don't really know each other yet,\x01",
            "so splitting up would be a bad call.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#0100581V#6P#0103FWe don't have time, Lloyd.\x01",
            "Let's just take Anri with us.\x02\x03",
            "#0100590V#0101FIf we come across monsters,\x01",
            "we won't let them touch him.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#0100583V#11P#0003FRight... Well, let's move.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3591")

    label("loc_32D0")

    OP_2C(0x3C, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0100584V#11P#0003FThere's no time to waste. We should start\x01",
            "our search for Ryu with Anri alongside us.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#0100585V#6P#0205FShould we not prioritize getting this child\x01",
            "to safety?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100586V#4P#0301FY'know, we could always split into two\x01",
            "teams and go from there.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0100587V#5P#0001FWe're running out of time. Dividing our\x01",
            "strength in half wouldn't be a good call,\x01",
            "given our circumstances.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#0100588V#11P#0001FCan you keep an eye on Anri for now, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100589V#6P#0104FYes, leave him to me.\x02\x03",
            "#0100582V#0100FIf we come across any monsters,\x01",
            "I won't let them lay a hand on him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3591")

    label("loc_3591")

    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0100591V#11P#0000FWe're going to find your friend, Anri.\x01",
            "I promise you.\x02\x03",
            "#0100592VBut it's dangerous to stay here alone, so\x01",
            "can you be brave and tag along with us?\x02\x03",
            "#0100593VAll right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0100594V#5PO-Okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100595V#5PI want to save Ryu, too.\x01",
            "Let's do this together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100596V#11P#0002FGood to hear.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0100597V#5P#0003FAll right, everyone. This is now a rescue\x01",
            "mission as well as an escort job.\x02\x03",
            "#0100598V#0001FLet's be even more careful from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100599V#6P#0100FOf course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100600V#6P#0204FRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100601V#4P#0300FWell, then, shall we go find our\x01",
            "other lil' adventurer?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Anri has joined the party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If an NPC is K.O.'d in battle, it will be game over.\x01",
            "Protect them at all costs.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrFlags(0x8, 0x80)
    AddParty(0x96, 0xFF, 0xFF)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x103, 0x40)
    ClearChrFlags(0x104, 0x40)
    OP_49()
    OP_37()
    SetChrPos(0x0, 198000, 0, 201000, 0)
    SetScenarioFlags(0x40, 7)
    OP_1B(0xA, 0xFF, 0xFFFF)
    OP_29(0x3C, 0x1, 0x3)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_15_20FC end

    def Function_16_38FC(): pass

    label("Function_16_38FC")

    EventBegin(0x0)
    OP_E0(0x1)
    Fade(1000)
    OP_68(0, 1000, 521299, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 0, 0, 520100, 0)
    SetChrPos(0x103, 0, 0, 521299, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pressing the button does nothing.\x01",
            "The elevator cannot be used at the moment.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0x103,
        (
            "#3300264V#0200FThis should be the elevator that leads\x01",
            "to A Sector's lower stratum.\x02\x03",
            "#3300265VI will enter the authentication code.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio opened the control panel and\x01",
            "punched in an eight-digit code.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Fade(500)
    SetMapObjFrame(0xD, "down", 0x1, 0x1)
    SetMapObjFrame(0xD, "gauge", 0x1, 0x1)
    Sound(72, 0, 100, 0)
    OP_0D()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        "#3300266V#0202FIt should be operational now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300267V#12P#0004FAll right. Ready to head down?\x02\x03",
            "#3300268V#0000FWait... Do you have any idea where\x01",
            "that terminal is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300269V#0203FMost likely in the deepest part of the floor.\x02\x03",
            "#3300270V#0201FIt will be a long walk, so please be sure to\x01",
            "stay on guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300271V#12P#0005FR-Right...\x01",
            "(And you wanted to come here alone...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 520000, 0)
    SetScenarioFlags(0xA0, 7)
    OP_29(0x45, 0x1, 0x3)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_16_38FC end

    def Function_17_3C83(): pass

    label("Function_17_3C83")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0001FWe need to find the source of the crying.\x02\x03",
            "It came from around here, right?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 191670, 0, 200070, 90)
    EventEnd(0x4)
    Return()

    # Function_17_3C83 end

    SaveToFile()

Try(main)
