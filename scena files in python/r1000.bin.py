from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1000.bin",                # FileName
        "r1000",                    # MapName
        "r1000",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00000000,                 # Flags
        ("r1000", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 95, 0, 0, 0, 1],
    )

    BuildStringList((
        "r1000",                  # 0
        "Bus",                    # 1
        "車00",                   # 2
        "車01",                   # 3
        "車02",                   # 4
        "車03",                   # 5
        "SE制御",                 # 6
        "br1000",                 # 7
        "br1000",                 # 8
        "br1000",                 # 9
        "br1000",                 # 10
        "br1000",                 # 11
        "To Crossbell City",      # 12
        "To Bellguard Gate",      # 13
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 11,  3,   8,   0,   8,   0,   0)
    Sepith("Sepith_B4", 11,  0,   5,   7,   0,   0,   7)
    Sepith("Sepith_C4", 4,   4,   10,  2,   0,   5,   5)
    Sepith("Sepith_D4", 13,  13,  0,   4,   0,   0,   0)
    Sepith("Sepith_E4", 12,  7,   4,   3,   6,   14,  7)

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

    # monster count: 9

    BattleInfo(
        "BattleInfo_154", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_A4", 30, 40, 20, 10,
        (
            ("ms60900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60900.dat", "ms60900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60900.dat", "ms70400.dat", "ms60900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60900.dat", "ms60900.dat", "ms74800.dat", "ms60900.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_21C", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_B4", 30, 40, 20, 10,
        (
            ("ms74800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms74800.dat", "ms74800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms74800.dat", "ms70400.dat", "ms74800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms74800.dat", "ms74800.dat", "ms60900.dat", "ms74800.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_2E4", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_C4", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3AC", 0x0000, 17, 6, 60, 8, 1, 30, 0, "br1000", "Sepith_D4", 30, 40, 20, 10,
        (
            ("ms71500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71500.dat", "ms71500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71500.dat", "ms71900.dat", "ms71500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71500.dat", "ms71500.dat", "ms70400.dat", "ms71500.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_474", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br1000", "Sepith_E4", 40, 35, 25, 0,
        (
            ("ms60701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
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
        "monster/ch60950.itc",               # 10
        "monster/ch60951.itc",               # 11
        "monster/ch74850.itc",               # 12
        "monster/ch74851.itc",               # 13
        "monster/ch71950.itc",               # 14
        "monster/ch71950.itc",               # 15
        "monster/ch71550.itc",               # 16
        "monster/ch71551.itc",               # 17
        "monster/ch60750.itc",               # 18
        "monster/ch60750.itc",               # 19
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-36920,  25180,   -2000,   0x1010000,    "BattleInfo_154", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-27400,  39160,   -2000,   0x1010000,    "BattleInfo_21C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-61100,  16450,   -2000,   0x1010000,    "BattleInfo_2E4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-82360,  38870,   -2000,   0x1010000,    "BattleInfo_3AC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-76380,  52370,   -2000,   0x1010000,    "BattleInfo_154", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-99040,  47600,   -2000,   0x1010000,    "BattleInfo_21C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-93520,  16270,   -2000,   0x1010000,    "BattleInfo_2E4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-30170,  11920,   -2000,   0x1010000,    "BattleInfo_474", 0,   24,  0xFFFF, 10, 11)
    DeclMonster(-103540, 6520,    -1080,   0x1010000,    "BattleInfo_474", 0,   24,  0xFFFF, 10, 11)

    DeclActor(-98650,  -2000,   50740,   1200,    -98650,  -1000,   50740,   0x007C, 0,  2,  0x0000)
    DeclActor(-26460,  -2000,   42260,   1200,    -26460,  -1000,   42260,   0x007C, 0,  3,  0x0000)
    DeclActor(-4330,   -2000,   5700,    1200,    -4330,   -1000,   5700,    0x007C, 0,  22, 0x0000)
    DeclActor(-100260, -1990,   14160,   1200,    -100260, -1990,   14160,   0x007C, 0,  4,  0x0000)
    DeclActor(-6170,   -2000,   11420,   1200,    -6170,   0,       11420,   0x007C, 0,  23, 0x0000)
    DeclActor(-3320,   -2000,   13000,   800,     -3320,   -500,    13020,   0x007C, 0,  11, 0x0000)
    DeclActor(-7980,   -2000,   13000,   800,     -7980,   -500,    13000,   0x007C, 0,  12, 0x0000)
    DeclActor(-10240,  -2000,   13000,   800,     -10240,  -500,    13000,   0x007C, 0,  13, 0x0000)
    DeclActor(-14600,  -2000,   12970,   800,     -14600,  -500,    12970,   0x007C, 0,  14, 0x0000)
    DeclActor(-17290,  -2000,   13580,   800,     -17290,  -500,    13580,   0x007C, 0,  15, 0x0000)
    DeclActor(-21800,  -2000,   16000,   800,     -21800,  -500,    16000,   0x007C, 0,  16, 0x0000)
    DeclActor(-24050,  -2000,   16800,   800,     -24050,  -500,    16800,   0x007C, 0,  17, 0x0000)
    DeclActor(-28160,  -2000,   17520,   800,     -28160,  -500,    17520,   0x007C, 0,  18, 0x0000)
    DeclActor(-11530,  -2000,   5320,    1500,    -11530,  -300,    5320,    0x007C, 0,  27, 0x0000)

    PlaceName(23.0, 0.0, 4.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(-137.0, 0.0, -28.0, 0x0000, 0x0000, "To Bellguard Gate")
    PlaceName(-4.0, 0.0, 5.900000095367432, 0x0000, 0x0055, "")
    PlaceName(-6.400000095367432, 0.0, 13.0, 0x0000, 0x0056, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11

    ScpFunction((
        "Function_0_A88",          # 00, 0
        "Function_1_D75",          # 01, 1
        "Function_2_143D",         # 02, 2
        "Function_3_15EF",         # 03, 3
        "Function_4_171E",         # 04, 4
        "Function_5_1732",         # 05, 5
        "Function_6_174B",         # 06, 6
        "Function_7_1807",         # 07, 7
        "Function_8_192B",         # 08, 8
        "Function_9_19C0",         # 09, 9
        "Function_10_1F99",        # 0A, 10
        "Function_11_2088",        # 0B, 11
        "Function_12_20EE",        # 0C, 12
        "Function_13_2171",        # 0D, 13
        "Function_14_21D4",        # 0E, 14
        "Function_15_2257",        # 0F, 15
        "Function_16_23C6",        # 10, 16
        "Function_17_2449",        # 11, 17
        "Function_18_24AE",        # 12, 18
        "Function_19_2531",        # 13, 19
        "Function_20_25A0",        # 14, 20
        "Function_21_279C",        # 15, 21
        "Function_22_2A5D",        # 16, 22
        "Function_23_2B8F",        # 17, 23
        "Function_24_2B9D",        # 18, 24
        "Function_25_3427",        # 19, 25
        "Function_26_346A",        # 1A, 26
        "Function_27_3543",        # 1B, 27
    ))


    def Function_0_A88(): pass

    label("Function_0_A88")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xF9, 7)
    SetScenarioFlags(0xFB, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AAD")
    SetMapFlags(0x10000000)
    Event(0, 24)

    label("loc_AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC3")
    Event(0, 26)

    label("loc_AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_AD2")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 8)

    label("loc_AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_AEA")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_AEA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D71")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B50")
    SetScenarioFlags(0x7A, 0)

    label("loc_B50")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B66")
    SetScenarioFlags(0x7A, 1)

    label("loc_B66")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7C")
    SetScenarioFlags(0x7A, 2)

    label("loc_B7C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B92")
    SetScenarioFlags(0x7A, 3)

    label("loc_B92")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA8")
    SetScenarioFlags(0x7A, 4)

    label("loc_BA8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBE")
    SetScenarioFlags(0x7A, 5)

    label("loc_BBE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD4")
    SetScenarioFlags(0x7A, 6)

    label("loc_BD4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEA")
    SetScenarioFlags(0x7A, 7)

    label("loc_BEA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C00")
    SetScenarioFlags(0x7B, 0)

    label("loc_C00")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C16")
    SetScenarioFlags(0x7B, 1)

    label("loc_C16")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2C")
    SetScenarioFlags(0x7B, 2)

    label("loc_C2C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C42")
    SetScenarioFlags(0x7B, 3)

    label("loc_C42")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C58")
    SetScenarioFlags(0x7B, 4)

    label("loc_C58")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6E")
    SetScenarioFlags(0x7B, 5)

    label("loc_C6E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C84")
    SetScenarioFlags(0x7B, 6)

    label("loc_C84")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9A")
    SetScenarioFlags(0x7B, 7)

    label("loc_C9A")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD5")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_D71")

    label("loc_CD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEC")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_D71")

    label("loc_CEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D03")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_D71")

    label("loc_D03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1A")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_D71")

    label("loc_D1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D31")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_D71")

    label("loc_D31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D48")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_D71")

    label("loc_D48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5F")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_D71")

    label("loc_D5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D71")
    SetScenarioFlags(0x7C, 7)

    label("loc_D71")

    Call(0, 5)
    Return()

    # Function_0_A88 end

    def Function_1_D75(): pass

    label("Function_1_D75")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8E")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_D94")

    label("loc_D8E")

    OP_10(0x0, 0x1)
    OP_10(0x2, 0x0)

    label("loc_D94")

    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x3, 0x4)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C8")
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    ClearMapObjFlags(0x3, 0x4)
    OP_66(0x4, 0x1)
    Jump("loc_10CD")

    label("loc_10C8")

    OP_16(0x3, 0x3, 0x1, 0x0)

    label("loc_10CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E0")
    OP_70(0x1, 0x0)
    Jump("loc_10E4")

    label("loc_10E0")

    OP_70(0x1, 0x1E)

    label("loc_10E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F7")
    OP_70(0x2, 0x0)
    Jump("loc_10FB")

    label("loc_10F7")

    OP_70(0x2, 0x1E)

    label("loc_10FB")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 0)), scpexpr(EXPR_END)), "loc_1158")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -100260, -1990, 14160, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_1158")

    OP_78(0x4, 0x9)
    OP_78(0x5, 0xA)
    OP_78(0x6, 0xB)
    OP_78(0x7, 0xC)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x4, "chukin", 0x0, 0x1)
    SetMapObjFrame(0x5, "chukin", 0x0, 0x1)
    SetMapObjFrame(0x6, "chukin", 0x0, 0x1)
    SetMapObjFrame(0x7, "chukin", 0x0, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    OP_65(0x9, 0x1)
    OP_65(0xA, 0x1)
    OP_65(0xB, 0x1)
    OP_65(0xC, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_121A")
    Jump("loc_143C")

    label("loc_121A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_12E1")
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    SetChrPos(0xA, -12350, -2000, 13000, 270)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0xB, -19900, -2000, 15000, 300)
    OP_D3(0xB, 0x0, 0x493E0, 0x0, 0x0)
    SetChrPos(0xC, -26000, -2000, 17180, 280)
    OP_D3(0xC, 0x0, 0x445C0, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12B2")
    Jump("loc_12DC")

    label("loc_12B2")

    ClearMapObjFlags(0x4, 0x4)
    SetChrPos(0x9, -5500, -2000, 13000, 270)
    OP_D3(0x9, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_12DC")

    Jump("loc_143C")

    label("loc_12E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_143C")
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    SetChrPos(0x9, -5500, -2000, 13000, 270)
    OP_D3(0x9, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0xA, -12350, -2000, 13000, 270)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0xB, -19900, -2000, 15000, 300)
    OP_D3(0xB, 0x0, 0x493E0, 0x0, 0x0)
    SetChrPos(0xC, -26000, -2000, 17180, 280)
    OP_D3(0xC, 0x0, 0x445C0, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_13A3")
    Jump("loc_143C")

    label("loc_13A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_143C")
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)
    OP_66(0x7, 0x1)
    OP_66(0x8, 0x1)
    OP_66(0x9, 0x1)
    OP_66(0xA, 0x1)
    OP_66(0xB, 0x1)
    OP_66(0xC, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_13EB")
    SetMapObjFrame(0x4, "chukin", 0x1, 0x1)

    label("loc_13EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_1406")
    SetMapObjFrame(0x5, "chukin", 0x1, 0x1)

    label("loc_1406")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_1421")
    SetMapObjFrame(0x6, "chukin", 0x1, 0x1)

    label("loc_1421")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_143C")
    SetMapObjFrame(0x7, "chukin", 0x1, 0x1)

    label("loc_143C")

    Return()

    # Function_1_D75 end

    def Function_2_143D(): pass

    label("Function_2_143D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1527")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_14BD")
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
    SetScenarioFlags(0x118, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1522")

    label("loc_14BD")

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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1522")

    Jump("loc_15E3")

    label("loc_1527")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A note inside of the treasure chest reads:\x01",
            "'I already have 99, so you guys take this one.\x01",
            "                                             - Estelle'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_15E3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_143D end

    def Function_3_15EF(): pass

    label("Function_3_15EF")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D9")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_166F")
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
    SetScenarioFlags(0x118, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_16D4")

    label("loc_166F")

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

    label("loc_16D4")

    Jump("loc_1712")

    label("loc_16D9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Made you look.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1712")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_15EF end

    def Function_4_171E(): pass

    label("Function_4_171E")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_4_171E end

    def Function_5_1732(): pass

    label("Function_5_1732")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_174A")
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    label("loc_174A")

    Return()

    # Function_5_1732 end

    def Function_6_174B(): pass

    label("Function_6_174B")

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
            "Bellguard Gate\x01",                 # 0
            "Bus Stop (Police Academy)\x01",      # 1
            "Leave\x01",                          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DF")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_17FF")

    label("loc_17DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FF")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()

    label("loc_17FF")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_174B end

    def Function_7_1807(): pass

    label("Function_7_1807")

    Fade(1000)
    OP_68(-9910, -1400, 11630, 0)
    MoveCamera(39, 32, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(24500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -5700, -2000, 5500, 0)
    SetChrPos(0x1, -7000, -2000, 5500, 0)
    SetChrPos(0x2, -8300, -2000, 5500, 0)
    SetChrPos(0x3, -9600, -2000, 5500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0x8)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x8, -34340, -2000, 9000, 0)
    OP_D3(0x8, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_18E2():
        OP_95(0xFE, -8200, -2000, 9000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18E2)
    Sleep(1500)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x8, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_7_1807 end

    def Function_8_192B(): pass

    label("Function_8_192B")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -5770, -2000, 5580, 270)
    SetChrPos(0x1, -5770, -2000, 5580, 270)
    SetChrPos(0x2, -5770, -2000, 5580, 270)
    SetChrPos(0x3, -5770, -2000, 5580, 270)
    OP_68(-5770, -1400, 5580, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_8_192B end

    def Function_9_19C0(): pass

    label("Function_9_19C0")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F91")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F2E")
    Sound(1500, 255, 100, 0)
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A66")
    MenuCmd(1, 1, "★City - Central Square")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1A81")

    label("loc_1A66")

    MenuCmd(1, 1, "　City - Central Square")

    label("loc_1A81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AAF")
    MenuCmd(1, 1, "★City - East Exit")
    MenuCmd(3, 1, 0x1)
    Jump("loc_1AC5")

    label("loc_1AAF")

    MenuCmd(1, 1, "　City - East Exit")

    label("loc_1AC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF3")
    MenuCmd(1, 1, "★City - West Exit")
    MenuCmd(3, 1, 0x2)
    Jump("loc_1B09")

    label("loc_1AF3")

    MenuCmd(1, 1, "　City - West Exit")

    label("loc_1B09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B38")
    MenuCmd(1, 1, "★City - South Exit")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1B4F")

    label("loc_1B38")

    MenuCmd(1, 1, "　City - South Exit")

    label("loc_1B4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B7E")
    MenuCmd(1, 1, "★City - North Exit")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1B95")

    label("loc_1B7E")

    MenuCmd(1, 1, "　City - North Exit")

    label("loc_1B95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BBF")
    MenuCmd(1, 1, "★Tangram Gate")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1BD1")

    label("loc_1BBF")

    MenuCmd(1, 1, "　Tangram Gate")

    label("loc_1BD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BFD")
    MenuCmd(1, 1, "★Bellguard Gate")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1C11")

    label("loc_1BFD")

    MenuCmd(1, 1, "　Bellguard Gate")

    label("loc_1C11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C49")
    MenuCmd(1, 1, "★St. Ursula Medical College")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1C69")

    label("loc_1C49")

    MenuCmd(1, 1, "　St. Ursula Medical College")

    label("loc_1C69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C97")
    MenuCmd(1, 1, "★Armorica Village")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1CAD")

    label("loc_1C97")

    MenuCmd(1, 1, "　Armorica Village")

    label("loc_1CAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CDF")
    MenuCmd(1, 1, "★Mainz Mining Village")
    MenuCmd(3, 1, 0x9)
    Jump("loc_1CF9")

    label("loc_1CDF")

    MenuCmd(1, 1, "　Mainz Mining Village")

    label("loc_1CF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D33")
    MenuCmd(1, 1, "★Mainz Mountain Path - Tunnel")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1D55")

    label("loc_1D33")

    MenuCmd(1, 1, "　Mainz Mountain Path - Tunnel")

    label("loc_1D55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D84")
    MenuCmd(1, 1, "★Stargazer's Tower")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1D9B")

    label("loc_1D84")

    MenuCmd(1, 1, "　Stargazer's Tower")

    label("loc_1D9B")

    MenuCmd(1, 1, "　Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F1F")
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
        (0, "loc_1E72"),
        (1, "loc_1E80"),
        (2, "loc_1E8E"),
        (3, "loc_1E9C"),
        (4, "loc_1EAA"),
        (5, "loc_1EB8"),
        (6, "loc_1EC6"),
        (7, "loc_1ED4"),
        (8, "loc_1EE2"),
        (9, "loc_1EF0"),
        (10, "loc_1EFE"),
        (11, "loc_1F0C"),
        (SWITCH_DEFAULT, "loc_1F1A"),
    )


    label("loc_1E72")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1F1A")

    label("loc_1E80")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1F1A")

    label("loc_1E8E")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1F1A")

    label("loc_1E9C")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1F1A")

    label("loc_1EAA")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1F1A")

    label("loc_1EB8")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1F1A")

    label("loc_1EC6")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1F1A")

    label("loc_1ED4")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1F1A")

    label("loc_1EE2")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1F1A")

    label("loc_1EF0")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1F1A")

    label("loc_1EFE")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_1F1A")

    label("loc_1F0C")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1F1A")

    label("loc_1F1A")

    Jump("loc_1F29")

    label("loc_1F1F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F29")

    Jump("loc_1F8C")

    label("loc_1F2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F79")
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
    Jump("loc_1F8C")

    label("loc_1F79")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F8C")

    Jump("loc_19DA")

    label("loc_1F91")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_19C0 end

    def Function_10_1F99(): pass

    label("Function_10_1F99")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -6360, -2000, 9850, 180)
    SetChrPos(0x1, -6360, -2000, 9850, 180)
    SetChrPos(0x2, -6360, -2000, 9850, 180)
    SetChrPos(0x3, -6360, -2000, 9850, 180)
    SetChrPos(0x4, -6360, -2000, 9850, 180)
    SetChrPos(0x5, -6360, -2000, 9850, 180)
    Sleep(1)
    OP_68(-6360, -1400, 9850, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24500, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_206D")
    Sound(1502, 255, 100, 0)
    Jump("loc_2073")

    label("loc_206D")

    Sound(1503, 255, 100, 0)

    label("loc_2073")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1F99 end

    def Function_11_2088(): pass

    label("Function_11_2088")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a Reinford Company private car.\x02\x03",
            "The license plate number is 'EW 3100.'\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBD, 5)
    Call(0, 20)
    TalkEnd(0xFF)
    Return()

    # Function_11_2088 end

    def Function_12_20EE(): pass

    label("Function_12_20EE")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2143")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An illegal parking warning\x01",
            "sticker is placed on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_216D")

    label("loc_2143")

    Call(0, 19)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_216D")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x4, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x2)

    label("loc_216D")

    TalkEnd(0xFF)
    Return()

    # Function_12_20EE end

    def Function_13_2171(): pass

    label("Function_13_2171")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a Verne Company private car.\x02\x03",
            "The license plate number is 'CZ 3323.'\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBD, 6)
    Call(0, 20)
    TalkEnd(0xFF)
    Return()

    # Function_13_2171 end

    def Function_14_21D4(): pass

    label("Function_14_21D4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2229")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An illegal parking warning\x01",
            "sticker is placed on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2253")

    label("loc_2229")

    Call(0, 19)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2253")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x5, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x4)

    label("loc_2253")

    TalkEnd(0xFF)
    Return()

    # Function_14_21D4 end

    def Function_15_2257(): pass

    label("Function_15_2257")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a Verne Company orbal truck.\x02\x03",
            "The license plate number is 'CL 1101.'\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_231E")

    ChrTalk(
        0x101,
        (
            "#0001F(I'm pretty sure I saw this license plate\x01",
            "number over at the eastern exit, too.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23BC")

    label("loc_231E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2337")
    Call(0, 21)
    Jump("loc_23BC")

    label("loc_2337")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23AF")

    ChrTalk(
        0x101,
        (
            "#0005F(Hold on a second...)\x02\x03",
            "#0003F(I feel like I've seen this license plate\x01",
            "number before.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23BC")

    label("loc_23AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23BC")
    SetScenarioFlags(0xBC, 4)

    label("loc_23BC")

    SetScenarioFlags(0xBD, 7)
    Call(0, 20)
    TalkEnd(0xFF)
    Return()

    # Function_15_2257 end

    def Function_16_23C6(): pass

    label("Function_16_23C6")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_241B")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An illegal parking warning\x01",
            "sticker is placed on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2445")

    label("loc_241B")

    Call(0, 19)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2445")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x6, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x6)

    label("loc_2445")

    TalkEnd(0xFF)
    Return()

    # Function_16_23C6 end

    def Function_17_2449(): pass

    label("Function_17_2449")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a Reinford Company luxury car.\x02\x03",
            "The license plate number is 'ED 0028.'\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 0)
    Call(0, 20)
    TalkEnd(0xFF)
    Return()

    # Function_17_2449 end

    def Function_18_24AE(): pass

    label("Function_18_24AE")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_2503")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An illegal parking warning\x01",
            "sticker is placed on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_252D")

    label("loc_2503")

    Call(0, 19)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_252D")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x7, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x8)

    label("loc_252D")

    TalkEnd(0xFF)
    Return()

    # Function_18_24AE end

    def Function_19_2531(): pass

    label("Function_19_2531")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Place a warning sticker?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        1,
        (
            "[Place]\x01",            # 0
            "[Don't Place]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Return()

    # Function_19_2531 end

    def Function_20_25A0(): pass

    label("Function_20_25A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_279B")

    ChrTalk(
        0x101,
        (
            "#0003FAll right. I think we've checked\x01",
            "all of the cars.\x02\x03",
            "#0000FLet's finish placing the remaining\x01",
            "stickers so we can give our report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FSounds like a plan, my man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FI don't think they were in a hurry, so it\x01",
            "may be a good idea to check all of the\x01",
            "cars one more time before we return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FHowever, we are unable to remove any\x01",
            "incorrectly placed stickers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWell, I don't think we'll have\x01",
            "anything to worry about.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x17, 0x1, 0x13)

    label("loc_279B")

    Return()

    # Function_20_25A0 end

    def Function_21_279C(): pass

    label("Function_21_279C")

    EventBegin(0x0)
    Fade(500)
    OP_E0(0x1)
    OP_68(-16510, -1000, 12930, 0)
    MoveCamera(35, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19610, 0)
    SetChrPos(0x101, -16190, -2000, 12370, 315)
    SetChrPos(0x102, -16030, -2000, 13480, 270)
    SetChrPos(0x103, -15170, -2000, 12270, 315)
    SetChrPos(0x104, -17080, -2000, 10620, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#0005FWait, what...?\x02\x03",
            "#0001FDidn't we see this plate number over\x01",
            "at the east exit, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0105FActually, I think you're right.\x02\x03",
            "#0101FI don't think it was this\x01",
            "type of truck, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FIt is against state regulation for multiple\x01",
            "vehicles to share an identical license\x01",
            "plate number.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FYeah, Tio Tot's right. Gotta have a unique\x01",
            "number, or you're breakin' the law.\x02\x03",
            "#0300FProbably a good idea to jot this plate\x01",
            "down, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FAbsolutely. We'd better report this\x01",
            "to the Metropolitan Division later.\x02",
        )
    )

    CloseMessageWindow()
    OP_E0(0x0)
    Call(0, 5)
    SetChrPos(0x0, -16190, -2000, 12370, 315)
    OP_29(0x17, 0x1, 0x14)
    EventEnd(0x5)
    Return()

    # Function_21_279C end

    def Function_22_2A5D(): pass

    label("Function_22_2A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B22")
    TalkBegin(0xFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to the ongoing monster infestation, the\x01",
            "bus service has been temporarily suspended.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x95, 2)
    TalkEnd(0xFF)
    Jump("loc_2B8E")

    label("loc_2B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B8B")
    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#0001FThere's no time to wait for the bus.\x01",
            "We need to go search for Colin!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_2B8E")

    label("loc_2B8B")

    Call(0, 6)

    label("loc_2B8E")

    Return()

    # Function_22_2A5D end

    def Function_23_2B8F(): pass

    label("Function_23_2B8F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_23_2B8F end

    def Function_24_2B9D(): pass

    label("Function_24_2B9D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x3)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(840)
    OP_68(8300, 2400, -2710, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(15190, 0)
    SetChrPos(0x101, 15950, 0, -140, 270)
    SetChrPos(0x102, 17240, 0, 710, 270)
    SetChrPos(0x103, 16970, 0, -1080, 270)
    SetChrPos(0x104, 18870, 0, 780, 270)
    SetChrPos(0x160, 18510, 0, -770, 270)
    FadeToBright(1000, 0)
    SetCameraDistance(13690, 3000)

    def lambda_2C7E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C7E)

    def lambda_2C93():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C93)

    def lambda_2CA8():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2CA8)

    def lambda_2CBD():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CBD)

    def lambda_2CD2():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2CD2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x160, 1)
    OP_6F(0x79)
    OP_0D()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#3400582V#0001F#5PCan you do me a favor and scan the\x01",
            "surrounding area, Tio?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D56():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D56)

    def lambda_2D63():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D63)
    Sleep(100)

    def lambda_2D73():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D73)

    def lambda_2D80():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2D80)
    Sleep(100)

    def lambda_2D90():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2D90)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x160, 1)

    ChrTalk(
        0x103,
        "#3400583V#0203F#12PRoger.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x103, 0xE1, 0x1F4)
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
    Sound(820, 0, 100, 0)
    BeginChrThread(0xD, 1, 0, 25)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(500)
    EndChrThread(0xD, 0x1)
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#3400584V#0208F#12PI was unable to detect him within\x01",
            "close proximity of Crossbell City.\x02\x03",
            "#3400585V#0201FHowever, I am detecting a slight reaction\x01",
            "from a transportation truck approximately\x01",
            "60 selge away from us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3400586V#0301F#5PJust means we gotta go flag\x01",
            "down this truck, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400587V#3305F#11PAn orbal staff? Very interesting.\x02\x03",
            "#3400588V#3304FI recall the other professor having a weapon\x01",
            "similar to yours.\x02\x03",
            "#3400589V#3302FThe Epstein Foundation's gone and created\x01",
            "quite the amusing trinket, haven't they?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3115():
        TurnDirection(0xFE, 0x160, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3115)

    def lambda_3122():
        TurnDirection(0xFE, 0x160, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3122)
    Sleep(100)

    def lambda_3132():
        TurnDirection(0xFE, 0x160, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3132)

    def lambda_313F():
        TurnDirection(0xFE, 0x160, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_313F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#3400590V#0005F#6POther professor? Who are these people you\x01",
            "keep talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400591V#0205F#6PAnd you claim he had something similar\x01",
            "to the orbal staff? It is supposed to be\x01",
            "the foundation's latest...\x02\x03",
            "#3400592V#0201FYou... You couldn't be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400593V#3309F#11PWhatever could you mean?\x02\x03",
            "#3400594V#3304FRegardless of who made what staff first,\x01",
            "we should find that silly little boy.\x02\x03",
            "#3400595V#3302FBefore tragedy befalls his adorable face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400596V#0001F#6PYeah, you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400597V#0103F#5PLet's continue the search, then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_37()
    OP_68(10000, 600, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 10000, 0, 0, 270)
    SetChrPos(0x1, 10000, 0, 0, 270)
    SetChrPos(0x2, 10000, 0, 0, 270)
    SetChrPos(0x3, 10000, 0, 0, 270)
    SetChrPos(0x4, 10000, 0, 0, 270)
    OP_E0(0x2)
    SetScenarioFlags(0xA3, 0)
    OP_24(0x348)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_24_2B9D end

    def Function_25_3427(): pass

    label("Function_25_3427")

    OP_25(0x348, 0x5A)
    Sleep(50)
    OP_25(0x348, 0x50)
    Sleep(50)
    OP_25(0x348, 0x46)
    Sleep(50)
    OP_25(0x348, 0x3C)
    Sleep(50)
    OP_25(0x348, 0x32)
    Sleep(50)
    OP_25(0x348, 0x28)
    Sleep(50)
    OP_25(0x348, 0x1E)
    Sleep(50)
    OP_25(0x348, 0x14)
    Sleep(50)
    OP_25(0x348, 0xA)
    Sleep(50)
    OP_24(0x348)
    Return()

    # Function_25_3427 end

    def Function_26_346A(): pass

    label("Function_26_346A")

    EventBegin(0x0)
    Sleep(1000)
    OP_68(-5690, 600, 4440, 4000)
    MoveCamera(45, 25, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(24500, 4000)
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

    # Function_26_346A end

    def Function_27_3543(): pass

    label("Function_27_3543")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "East: Crossbell City\x01",
            "West: Bellguard Gate - 198 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_3543 end

    SaveToFile()

Try(main)
