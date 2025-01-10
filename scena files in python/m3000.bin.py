from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3000.bin",                # FileName
        "m3000",                    # MapName
        "m3000",                    # Location
        0x007B,                     # MapIndex
        "ed7510",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -210000, 27000, 0, 0, 0, 1, 123, 0, 1, 0, 2],
    )

    BuildStringList((
        "m3000",                  # 0
        "Boss 1",                 # 1
        "Tio",                    # 2
        "bm3000",                 # 3
        "bm3000",                 # 4
        "bm3000",                 # 5
        "bm3000",                 # 6
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_B4", 24,  0,   0,   2,   8,   14,  14)
    Sepith("Sepith_C4", 4,   4,   20,  0,   16,  12,  7)
    Sepith("Sepith_D4", 0,   29,  0,   0,   9,   3,   19)

    MonsterBattlePostion("MonsterBattlePostion_E4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_108", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_10C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_110", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_114", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_118", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_11C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 5, 5, 45)

    # monster count: 6

    BattleInfo(
        "BattleInfo_124", 0x0000, 37, 6, 60, 4, 1, 35, 0, "bm3000", "Sepith_B4", 60, 25, 10, 5,
        (
            ("ms70900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7402", "ed7403", "ATBonus_94"),
            ("ms70900.dat", "ms60600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7402", "ed7403", "ATBonus_94"),
            ("ms70900.dat", "ms60600.dat", "ms60600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7402", "ed7403", "ATBonus_94"),
            ("ms70900.dat", "ms60600.dat", "ms60600.dat", "ms60600.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7402", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_1EC", 0x0000, 37, 6, 60, 4, 1, 30, 0, "bm3000", "Sepith_C4", 60, 25, 10, 5,
        (
            ("ms60600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7402", "ed7403", "ATBonus_94"),
            ("ms60600.dat", "ms60600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7402", "ed7403", "ATBonus_94"),
            ("ms60600.dat", "ms68600.dat", "ms60600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7402", "ed7403", "ATBonus_94"),
            ("ms60600.dat", "ms60600.dat", "ms68600.dat", "ms60600.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7402", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_2B4", 0x0000, 37, 6, 60, 4, 1, 40, 0, "bm3000", "Sepith_D4", 60, 25, 10, 5,
        (
            ("ms68600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7402", "ed7403", "ATBonus_94"),
            ("ms68600.dat", "ms68600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7402", "ed7403", "ATBonus_94"),
            ("ms68600.dat", "ms60600.dat", "ms68600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7402", "ed7403", "ATBonus_94"),
            ("ms68600.dat", "ms68600.dat", "ms60600.dat", "ms68600.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7402", "ed7403", "ATBonus_94"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_37C", 0x0042, 37, 6, 60, 0, 1, 0, 0, "bm3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7405", "ed7000", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00200.itc",                   # 00
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
        "monster/ch68850.itc",               # 10
        "monster/ch68850.itc",               # 11
        "monster/ch68650.itc",               # 12
        "monster/ch68651.itc",               # 13
        "monster/ch60650.itc",               # 14
        "monster/ch60650.itc",               # 15
        "monster/ch70950.itc",               # 16
        "monster/ch70951.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-4850,   19250,   3040,    0x1010000,    "BattleInfo_124", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-2260,   26030,   9040,    0x1010000,    "BattleInfo_1EC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-450,    149030,  9040,    0x1010000,    "BattleInfo_2B4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(12520,   -18730,  9040,    0x1010000,    "BattleInfo_1EC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-630,    -136810, 9040,    0x1010000,    "BattleInfo_124", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-280,    -155150, 9040,    0x1010000,    "BattleInfo_124", 0,   22,  0xFFFF, 6,  7)

    DeclActor(-4500,   3000,    -19500,  1200,    -4500,   4000,    -19500,  0x007C, 0,  3,  0x0000)
    DeclActor(-5600,   9000,    25500,   1200,    -5600,   10000,   25500,   0x007C, 0,  4,  0x0000)
    DeclActor(11250,   9000,    0,       1200,    11250,   10000,   0,       0x007C, 0,  5,  0x0000)
    DeclActor(0,       9000,    154500,  1200,    0,       10000,   154500,  0x007C, 0,  6,  0x0000)
    DeclActor(251250,  2500,    10750,   1200,    251250,  3500,    10750,   0x007C, 0,  7,  0x0000)
    DeclActor(253000,  2500,    -7000,   1200,    253000,  3500,    -7000,   0x007C, 0,  8,  0x0000)
    DeclActor(6000,    9000,    -150000, 1200,    6000,    10000,   -150000, 0x007C, 0,  10, 0x0000)
    DeclActor(5000,    3000,    3500,    1200,    5000,    4500,    3500,    0x007C, 0,  9,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7

    ScpFunction((
        "Function_0_6DC",          # 00, 0
        "Function_1_6F9",          # 01, 1
        "Function_2_737",          # 02, 2
        "Function_3_B1F",          # 03, 3
        "Function_4_CBF",          # 04, 4
        "Function_5_E36",          # 05, 5
        "Function_6_F96",          # 06, 6
        "Function_7_10FA",         # 07, 7
        "Function_8_123C",         # 08, 8
        "Function_9_13AF",         # 09, 9
        "Function_10_14AF",        # 0A, 10
        "Function_11_16A9",        # 0B, 11
        "Function_12_1EA2",        # 0C, 12
        "Function_13_2B0E",        # 0D, 13
        "Function_14_2B47",        # 0E, 14
        "Function_15_2DD3",        # 0F, 15
        "Function_16_33B5",        # 10, 16
    ))


    def Function_0_6DC(): pass

    label("Function_0_6DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F8")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_6DC")

    label("loc_6F8")

    Return()

    # Function_0_6DC end

    def Function_1_6F9(): pass

    label("Function_1_6F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_713")
    Event(0, 12)

    label("loc_713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_727")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 11)
    Jump("loc_736")

    label("loc_727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_736")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 15)

    label("loc_736")

    Return()

    # Function_1_6F9 end

    def Function_2_737(): pass

    label("Function_2_737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 7)), scpexpr(EXPR_END)), "loc_749")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75C")
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_75C")

    ClearMapObjFlags(0x22, 0x10)
    OP_70(0x22, 0x41)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_778")
    OP_70(0x22, 0x0)

    label("loc_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 0)), scpexpr(EXPR_END)), "loc_78E")
    OP_70(0x18, 0x0)
    OP_70(0x23, 0x41)
    Jump("loc_796")

    label("loc_78E")

    OP_70(0x18, 0x5)
    OP_70(0x23, 0x0)

    label("loc_796")

    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A06")
    OP_70(0x8, 0x0)
    Jump("loc_A0A")

    label("loc_A06")

    OP_70(0x8, 0x1E)

    label("loc_A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1D")
    OP_70(0x9, 0x0)
    Jump("loc_A21")

    label("loc_A1D")

    OP_70(0x9, 0x1E)

    label("loc_A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A34")
    OP_70(0xA, 0x0)
    Jump("loc_A38")

    label("loc_A34")

    OP_70(0xA, 0x1E)

    label("loc_A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4B")
    OP_70(0x15, 0x0)
    Jump("loc_A4F")

    label("loc_A4B")

    OP_70(0x15, 0x1E)

    label("loc_A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A62")
    OP_70(0x21, 0x0)
    Jump("loc_A66")

    label("loc_A62")

    OP_70(0x21, 0x1E)

    label("loc_A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A79")
    OP_70(0x24, 0x0)
    Jump("loc_A7D")

    label("loc_A79")

    OP_70(0x24, 0x1E)

    label("loc_A7D")

    Sound(129, 1, 100, 0)
    OP_1B(0x0, 0x0, 0x10)
    SetMapObjFlags(0x26, 0x4)
    ClearMapObjFlags(0x26, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1E")
    OP_65(0x6, 0x1)
    OP_70(0x18, 0x0)
    OP_70(0x23, 0x41)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x21, 0x4)
    SetMapObjFlags(0x24, 0x4)
    SetMapObjFlags(0x25, 0x4)
    OP_65(0x7, 0x1)
    ClearMapObjFlags(0x26, 0x4)
    SetMapObjFlags(0x26, 0x2)

    label("loc_B1E")

    Return()

    # Function_2_737 end

    def Function_3_B1F(): pass

    label("Function_3_B1F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C09")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_B9F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11E, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_C04")

    label("loc_B9F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C04")

    Jump("loc_CB3")

    label("loc_C09")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Rest in peace, Unsho Ishizuka. Though you may\x01",
            "be gone, your voice lives on through Sergei Lou\x01",
            "and many others you gave life to.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_CB3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_B1F end

    def Function_4_CBF(): pass

    label("Function_4_CBF")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA9")
    Sound(14, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x48, 1)"), scpexpr(EXPR_END)), "loc_D3F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x48),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11E, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_DA4")

    label("loc_D3F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x48),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_DA4")

    Jump("loc_E2A")

    label("loc_DA9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The amount of things in this chest now equals\x01",
            "the game's title. Thanks a lot for that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_E2A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_CBF end

    def Function_5_E36(): pass

    label("Function_5_E36")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F20")
    Sound(14, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x59, 1)"), scpexpr(EXPR_END)), "loc_EB6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x59),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11E, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_F1B")

    label("loc_EB6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x59),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F1B")

    Jump("loc_F8A")

    label("loc_F20")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Not even the Aureole can match your\x01",
            "obsession with empty space.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_F8A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_E36 end

    def Function_6_F96(): pass

    label("Function_6_F96")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1080")
    Sound(14, 0, 100, 0)
    OP_71(0x15, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_1016")
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
    SetScenarioFlags(0x11E, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_107B")

    label("loc_1016")

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

    label("loc_107B")

    Jump("loc_10EE")

    label("loc_1080")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I CLAPPED! I CLAPPED WHEN HE USED\x01",
            "THE EIGHT LEAVES ONE BLADE STYLE!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_10EE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_F96 end

    def Function_7_10FA(): pass

    label("Function_7_10FA")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E4")
    Sound(14, 0, 100, 0)
    OP_71(0x21, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_117A")
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
    SetScenarioFlags(0x11E, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_11DF")

    label("loc_117A")

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
    OP_71(0x21, 0x1E, 0x0, 0x0, 0x0)

    label("loc_11DF")

    Jump("loc_1230")

    label("loc_11E4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Abandon all hope, ye who open me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1230")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_10FA end

    def Function_8_123C(): pass

    label("Function_8_123C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1326")
    Sound(14, 0, 100, 0)
    OP_71(0x24, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_12BC")
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
    SetScenarioFlags(0x11E, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1321")

    label("loc_12BC")

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
    OP_71(0x24, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1321")

    Jump("loc_13A3")

    label("loc_1326")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mafia, assassins, corrupt politicians, and\x01",
            "a drug-dealing cult. Hell of a day, eh?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_13A3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_123C end

    def Function_9_13AF(): pass

    label("Function_9_13AF")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1492")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x25, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x25, 0x0)
    OP_71(0x25, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x25)
    OP_71(0x25, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x25, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1492")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14AE")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_14AE")

    Return()

    # Function_9_13AF end

    def Function_10_14AF(): pass

    label("Function_10_14AF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 0)), scpexpr(EXPR_END)), "loc_1508")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a statue of a knight brandishing a sword.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_16A8")

    label("loc_1508")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It looks like the sword on this statue can be moved.\x01",
            "Move the sword?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A1")
    Fade(500)
    SetChrPos(0x0, 4460, 9040, -150060, 89)
    SetChrPos(0x1, 2510, 9040, -148900, 89)
    SetChrPos(0x2, 2510, 9040, -151310, 89)
    SetChrPos(0x3, 920, 9040, -150530, 89)
    OP_68(4110, 10290, -150590, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(22000, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0x18, 0x5, 0x23, 0x0, 0x0)
    Sleep(1000)
    Sound(149, 0, 100, 0)
    OP_82(0x64, 0x0, 0x7D0, 0xC8)
    Sleep(500)
    Fade(500)
    OP_68(9520, 4290, 340, 0)
    MoveCamera(55, 33, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(27000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    OP_82(0x0, 0x64, 0x7D0, 0xC8)
    OP_71(0x23, 0x0, 0x41, 0x0, 0x0)
    OP_79(0x23)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetScenarioFlags(0xF4, 0)

    label("loc_16A1")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_16A8")

    Return()

    # Function_10_14AF end

    def Function_11_16A9(): pass

    label("Function_11_16A9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-194000, 24040, 0, 0)
    MoveCamera(35, 35, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -203400, 27040, 0, 90)
    SetChrPos(0x102, -204900, 27040, -900, 90)
    SetChrPos(0x104, -204900, 27040, 900, 90)
    SetChrPos(0x103, -206200, 27040, 0, 90)
    SetChrPos(0x107, -207200, 27040, 500, 90)
    SetChrPos(0x108, -206900, 27040, 1600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_1764():
        OP_96(0xFE, 0xFFFD7218, 0x3AC0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1764)
    Sleep(120)

    def lambda_1781():
        OP_96(0xFE, 0xFFFD6980, 0x3AC0, 0x384, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1781)
    Sleep(30)

    def lambda_179E():
        OP_96(0xFE, 0xFFFD6980, 0x3AC0, 0xFFFFFC7C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_179E)
    Sleep(30)

    def lambda_17BB():
        OP_96(0xFE, 0xFFFD6728, 0x3AC0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_17BB)
    Sleep(50)

    def lambda_17D8():
        OP_96(0xFE, 0xFFFD646C, 0x3AC0, 0x640, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_17D8)
    Sleep(50)

    def lambda_17F5():
        OP_96(0xFE, 0xFFFD6340, 0x3AC0, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_17F5)
    SetCameraDistance(13000, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(-184600, 18440, 0, 0)
    MoveCamera(325, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15000, 0)
    OP_68(-179600, 16440, 0, 4000)
    MoveCamera(310, 13, 0, 4000)
    SetCameraDistance(16000, 4000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-168720, 16040, 710, 0)
    MoveCamera(53, 21, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x108, 1)
    WaitChrThread(0x107, 1)
    Sleep(500)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5300105V#0001F#11PWell, Tio?\x02",
    )

    CloseMessageWindow()

    def lambda_18FA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_18FA)
    Sleep(50)

    def lambda_190A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_190A)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#5300106V#6P#0206FIt is as I feared.\x02\x03",
            "#5300107V#0208FThe higher elements--time, space,\x01",
            "and mirage--are indeed present.\x02\x03",
            "#5300108V#0201FJust like the tower and temple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300109V#12P#0106FI feared as much...\x02\x03",
            "#5300110V#0101FThis will be a difficult operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300111V#0306F#5PGuess that means we'll run into\x01",
            "more supernatural scum.\x02\x03",
            "#5300112V#0301FMan, I'm gettin' chills down my\x01",
            "spine already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300113V#6P#0801FWe've explored quite a few places\x01",
            "like this before. Not fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300114V#0903FFrankly, I can only guess what kinds\x01",
            "of fiends await us.\x02\x03",
            "#5300115V#0901FWe mustn't let our guard down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300116V#0013F#11PUnderstood.\x02\x03",
            "#5300117V#0003FKnowing our enemy, they'll try to\x01",
            "ambush us.\x02\x03",
            "#5300118V#0007FEveryone, keep your eyes peeled!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C35():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1C35)
    Sleep(50)

    def lambda_1C45():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1C45)
    Sleep(50)
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0x9, -169120, 12600, 220, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Sound(1153, 255, 100, 0)
    Sound(1249, 255, 100, 1)
    Sound(1343, 255, 100, 2)
    Sound(1689, 255, 100, 3)
    Sound(1759, 255, 100, 4)

    ChrTalk(
        0x108,
        "#0901F#1K#N#1PReady!\x02",
    )


    ChrTalk(
        0x9,
        "#0201F#1K#N#5PYes!\x02",
    )


    ChrTalk(
        0x102,
        "#0107F#1K#N#4PRight!\x02",
    )


    NpcTalk(
        0x101,
        "Randy",
        "#0307F#1K#N#2PRoger!\x02",
    )


    ChrTalk(
        0x107,
        "#5300119V#0807F#1K#N#3PLet's go!\x02",
    )

    OP_57(0x1)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle and Joshua have joined the party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can add them to the active party in\x01",
            "the [TACTICS] menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-168500, 16040, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x0, -168500, 15040, 0, 90)
    SetChrPos(0x1, -168500, 15040, 0, 90)
    SetChrPos(0x2, -168500, 15040, 0, 90)
    SetChrPos(0x3, -168500, 15040, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetScenarioFlags(0xE4, 5)
    OP_29(0x4F, 0x4, 0x2)
    OP_29(0x4F, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E8B")
    OP_29(0x31, 0x4, 0x40)
    Jump("loc_1E9D")

    label("loc_1E8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9D")
    OP_29(0x31, 0x4, 0x40)

    label("loc_1E9D")

    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_11_16A9 end

    def Function_12_1EA2(): pass

    label("Function_12_1EA2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00650.itc", 0x22)
    LoadChrToIndex("chr/ch00750.itc", 0x23)
    LoadChrToIndex("monster/ch68852.itc", 0x24)
    OP_68(238000, 4000, 0, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 238100, 3500, -1300, 90)
    SetChrPos(0x102, 237800, 3500, -300, 90)
    SetChrPos(0x103, 236500, 3500, -1800, 90)
    SetChrPos(0x104, 236200, 3500, -800, 90)
    SetChrPos(0x107, 237900, 3500, 1500, 90)
    SetChrPos(0x108, 236900, 3500, 1900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x10)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 272000, 1500, 0, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x0, "event\\ev501_00.eff")
    SetCameraDistance(17500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#5300124V#0005F#6PThis place...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300125V#6P#0101FCould this be the fort commander's chamber?\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#5300126V#6P#0201FLook...!\x02",
    )

    CloseMessageWindow()
    OP_68(279000, 6500, 0, 4000)
    MoveCamera(65, 10, 0, 4000)
    SetCameraDistance(23000, 4000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5300127V#0013FNo way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300128V#0107FThat's the same crest as the\x01",
            "one inside the temple!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(272000, 5500, 0, 0)
    MoveCamera(55, 12, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 262100, 3500, -1300, 90)
    SetChrPos(0x102, 261800, 3500, -300, 90)
    SetChrPos(0x103, 260500, 3500, -1800, 90)
    SetChrPos(0x104, 260200, 3500, -800, 90)
    SetChrPos(0x107, 261899, 3500, 1500, 90)
    SetChrPos(0x108, 260899, 3500, 1900, 90)

    def lambda_21E1():
        OP_98(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21E1)
    Sleep(50)

    def lambda_21FE():
        OP_98(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_21FE)

    def lambda_2218():
        OP_98(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2218)
    Sleep(50)

    def lambda_2235():
        OP_98(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2235)

    def lambda_224F():
        OP_98(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_224F)
    Sleep(50)

    def lambda_226C():
        OP_98(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_226C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x108, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x107,
        (
            "#5300129V#0808F#5PThe mark of the cult... This is it.\x02\x03",
            "#5300130V#0801FThough, it's a little different from the ones in\x01",
            "the report about the incident six years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300131V#0303F#5POn top of that, it's also different from the\x01",
            "one in Joachim's folder.\x02\x03",
            "#5300132V#0301FThat crest had wings or somethin', I think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300133V#0901F#5PIt's probably just a simplification of\x01",
            "the cult's current crest.\x02\x03",
            "#5300134VPerhaps this is what that is based on.\x02\x03",
            "#5300135V#0908FAnd considering its location,\x01",
            "that means...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300136V#0006F#5PThe cult's origins date back to over\x01",
            "500 years ago.\x02\x03",
            "#5300137V#0013FIt may even have been founded\x01",
            "here in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300138V#0903F#5PRight. The crest in the temple dates\x01",
            "back to a period of war, 500 years ago.\x02\x03",
            "#5300139V#0901FIt's possible that the cult took advantage\x01",
            "of influential figures back then to spread\x01",
            "its hold all over Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300140V#0106F#5PThis is crazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300141V#0008F#5PWe'll unravel the truth behind\x01",
            "the cult soon enough.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#5300142V#0207F#5PEveryone, look out!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    ReplaceBGM("ed7000", "ed7000")
    Fade(250)
    OP_68(272000, 4000, 0, 0)
    MoveCamera(33, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    OP_0D()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(13500, 1000)
    Sleep(900)

    def lambda_2742():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2742)

    def lambda_275C():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_275C)
    Sleep(50)

    def lambda_2779():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2779)

    def lambda_2793():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2793)
    Sleep(50)

    def lambda_27B0():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27B0)

    def lambda_27CA():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_27CA)
    OP_6F(0x10)
    OP_68(272000, 5000, 0, 3500)
    MoveCamera(33, 30, 0, 3500)
    SetCameraDistance(18000, 3500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    BeginChrThread(0x101, 3, 0, 13)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 272000, 3500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    OP_24(0x81)
    Sleep(500)

    def lambda_2870():
        OP_96(0xFE, 0x42680, 0xDAC, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2870)

    def lambda_288A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_288A)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    WaitChrThread(0x102, 1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x107, 1)
    SetChrChipByIndex(0x107, 0x22)
    SetChrSubChip(0x107, 0x0)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x108, 1)
    SetChrChipByIndex(0x108, 0x23)
    SetChrSubChip(0x108, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x8, 1)
    Sleep(500)
    CancelBlur(2000)
    OP_68(268300, 4900, 0, 2000)
    MoveCamera(55, 15, 0, 2000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5300143V#0007F#6P#NSomething's here!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        (
            "#5300144V#0813F#6PIs that thing like the devils\x01",
            "from Phantasma?!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x108,
        (
            "#5300145V#0907F#6PThe whole place is starting\x01",
            "to warp! Be careful!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#5300146V#0307F#6P#NLet's beat the hell out of it!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    OP_68(272000, 4900, 0, 0)
    MoveCamera(90, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    Sleep(170)
    SetChrSubChip(0x8, 0x1)
    Sleep(170)

    def lambda_2A7A():
        OP_A6(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2A7A)
    Sleep(1000)
    Sound(948, 0, 100, 0)
    OP_68(269000, 4900, 0, 400)
    SetCameraDistance(15000, 400)
    SetChrFlags(0x8, 0x20)
    SetChrSubChip(0x8, 0x2)

    def lambda_2ABF():
        OP_98(0xFE, 0xFFFFF060, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2ABF)
    BlurSwitch(0x190, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(400)
    EndChrThread(0x101, 0x3)
    Battle("BattleInfo_37C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    StopEffect(0x0, 0x2)
    Call(0, 14)
    Return()

    # Function_12_1EA2 end

    def Function_13_2B0E(): pass

    label("Function_13_2B0E")

    OP_82(0x96, 0x96, 0xBB8, 0xDAC)
    Sleep(3500)

    label("loc_2B22")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B46")
    OP_82(0x64, 0x64, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("loc_2B22")

    label("loc_2B46")

    Return()

    # Function_13_2B0E end

    def Function_14_2B47(): pass

    label("Function_14_2B47")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)
    OP_68(272000, 4500, 0, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 268100, 3500, -1300, 90)
    SetChrPos(0x102, 267800, 3500, -300, 90)
    SetChrPos(0x103, 266500, 3500, -1800, 90)
    SetChrPos(0x104, 266200, 3500, -800, 90)
    SetChrPos(0x107, 267900, 3500, 1500, 90)
    SetChrPos(0x108, 266900, 3500, 1900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(155, 2, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0xFA0)
    OP_74(0x22, 0xF)
    OP_71(0x22, 0x0, 0x41, 0x0, 0x0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_79(0x22)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)

    ChrTalk(
        0x107,
        "#5300147V#0801F#5PWhoa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300148V#0901F#5PIt looks like we've finally\x01",
            "reached the heart of the lodge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300149V#0013F#5PEveryone, let's move.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 268000, 3500, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0xE4, 6)
    OP_29(0x4F, 0x1, 0x1)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_14_2B47 end

    def Function_15_2DD3(): pass

    label("Function_15_2DD3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x0)
    SetScenarioFlags(0x5A, 0)
    OP_C7(0x0, 0x1000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_68(-194000, 24040, 0, 0)
    MoveCamera(35, 35, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -203400, 27040, 0, 90)
    SetChrPos(0x102, -204900, 27040, -900, 90)
    SetChrPos(0x104, -204900, 27040, 900, 90)
    SetChrPos(0x103, -206200, 27040, 0, 90)
    SubItemNumber(0x270F, 99)
    OP_32(0x0, 0x10, 0x28)
    AddCraft(0x0, 0xFFFF)
    RemoveCraft(0x0, 0xFFFF)
    OP_38(0x0, 0x80, 0x2)
    OP_38(0x0, 0x81, 0x2)
    OP_38(0x0, 0x82, 0x2)
    OP_38(0x0, 0x83, 0x2)
    OP_38(0x0, 0x84, 0x2)
    OP_38(0x0, 0x85, 0x2)
    OP_38(0x0, 0x86, 0x2)
    OP_42(0x0, 0x3F2, 0xFF)
    OP_42(0x0, 0x5EC, 0xFF)
    OP_42(0x0, 0x650, 0xFF)
    OP_32(0x1, 0x10, 0x28)
    AddCraft(0x1, 0xFFFF)
    RemoveCraft(0x1, 0xFFFF)
    OP_38(0x1, 0x80, 0x2)
    OP_38(0x1, 0x81, 0x2)
    OP_38(0x1, 0x82, 0x2)
    OP_38(0x1, 0x83, 0x2)
    OP_38(0x1, 0x84, 0x2)
    OP_38(0x1, 0x85, 0x2)
    OP_38(0x1, 0x86, 0x2)
    OP_42(0x1, 0x406, 0xFF)
    OP_42(0x1, 0x5EC, 0xFF)
    OP_42(0x1, 0x650, 0xFF)
    OP_32(0x2, 0x10, 0x28)
    AddCraft(0x2, 0xFFFF)
    RemoveCraft(0x2, 0xFFFF)
    OP_38(0x2, 0x80, 0x2)
    OP_38(0x2, 0x81, 0x2)
    OP_38(0x2, 0x82, 0x2)
    OP_38(0x2, 0x83, 0x2)
    OP_38(0x2, 0x84, 0x2)
    OP_38(0x2, 0x85, 0x2)
    OP_38(0x2, 0x86, 0x2)
    OP_42(0x2, 0x41A, 0xFF)
    OP_42(0x2, 0x5EC, 0xFF)
    OP_42(0x2, 0x650, 0xFF)
    OP_32(0x3, 0x10, 0x28)
    AddCraft(0x3, 0xFFFF)
    RemoveCraft(0x3, 0xFFFF)
    OP_38(0x3, 0x80, 0x2)
    OP_38(0x3, 0x81, 0x2)
    OP_38(0x3, 0x82, 0x2)
    OP_38(0x3, 0x83, 0x2)
    OP_38(0x3, 0x84, 0x2)
    OP_38(0x3, 0x85, 0x2)
    OP_38(0x3, 0x86, 0x2)
    OP_42(0x3, 0x42E, 0xFF)
    OP_42(0x3, 0x5EC, 0xFF)
    OP_42(0x3, 0x650, 0xFF)
    OP_C5(0x1, 0x0)
    OP_C5(0x1, 0x1F)

    def lambda_2F58():
        OP_96(0xFE, 0xFFFD7218, 0x3AC0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F58)
    Sleep(120)

    def lambda_2F75():
        OP_96(0xFE, 0xFFFD6980, 0x3AC0, 0x384, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2F75)
    Sleep(30)

    def lambda_2F92():
        OP_96(0xFE, 0xFFFD6980, 0x3AC0, 0xFFFFFC7C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F92)
    Sleep(30)

    def lambda_2FAF():
        OP_96(0xFE, 0xFFFD6728, 0x3AC0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2FAF)
    SetCameraDistance(13000, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(-184600, 18440, 0, 0)
    MoveCamera(325, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15000, 0)
    OP_68(-179600, 16440, 0, 4000)
    MoveCamera(310, 13, 0, 4000)
    SetCameraDistance(16000, 4000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-168720, 16040, 710, 0)
    MoveCamera(53, 21, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(500)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#0100001V#0001F#11PWell, Tio?\x02",
    )

    CloseMessageWindow()

    def lambda_30AC():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_30AC)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#0100002V#6P#0206FIt is as I feared.\x02\x03",
            "#0100003V#0208FThe higher elements--time, space,\x01",
            "and mirage--are indeed present.\x02\x03",
            "#0100004V#0201FJust like the tower and temple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100005V#12P#0106FI feared as much...\x02\x03",
            "#0100006V#0101FThis will be a difficult operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100007V#0306F#5PGuess that means we'll run into\x01",
            "more supernatural scum.\x02\x03",
            "#0100008V#0301FMan, I'm gettin' chills down my\x01",
            "spine already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100009V#0013F#11PUnderstood.\x02\x03",
            "#0100010V#0003FKnowing our enemy, they'll try to\x01",
            "ambush us.\x02\x03",
            "#0100011V#0007FEveryone, keep your eyes peeled!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3307():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3307)
    Sleep(50)
    OP_93(0x104, 0x5A, 0x1F4)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Sound(1153, 255, 100, 0)
    Sound(1249, 255, 100, 1)
    Sound(1343, 255, 100, 2)

    ChrTalk(
        0x103,
        "#0201F#1K#6PYes!\x02",
    )


    ChrTalk(
        0x104,
        "#0307F#1K#1PRoger!\x02",
    )


    ChrTalk(
        0x102,
        "#0100012V#0107F#1K#2PRight!\x02",
    )

    OP_57(0x1)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -168500, 15040, 0, 90)
    SetScenarioFlags(0x40, 0)
    Sleep(500)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_15_2DD3 end

    def Function_16_33B5(): pass

    label("Function_16_33B5")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341E")

    ChrTalk(
        0x101,
        (
            "#0001FWe can't go back now.\x02\x03",
            "All we can do is move forward\x01",
            "and crack this case!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3467")

    label("loc_341E")


    ChrTalk(
        0x101,
        (
            "#0001FNo time to go back now. Let's hurry\x01",
            "toward the ruin's depths!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3467")

    Sleep(50)
    SetChrPos(0x0, -211500, 27040, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_16_33B5 end

    SaveToFile()

Try(main)
