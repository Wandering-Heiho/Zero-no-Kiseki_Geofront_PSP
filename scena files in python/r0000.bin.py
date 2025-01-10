from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0000.bin",                # FileName
        "r0000",                    # MapName
        "r0000",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("r0000", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 5700, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 94, 0, 1, 0, 2],
    )

    BuildStringList((
        "r0000",                  # 0
        "Man",                    # 1
        "Officer",                # 2
        "Bus",                    # 3
        "Black-Haired Woman",     # 4
        "Old Lady",               # 5
        "Old Man",                # 6
        "Merchant",               # 7
        "Woman",                  # 8
        "Older Brother",          # 9
        "Younger Sister",         # 10
        "Father",                 # 11
        "Boy",                    # 12
        "車00",                   # 13
        "車01",                   # 14
        "車02",                   # 15
        "車03",                   # 16
        "車04",                   # 17
        "SE制御",                 # 18
        "br0000",                 # 19
        "br0000",                 # 20
        "To Crossbell City",      # 21
        "To Armorica Village & Tangram Gate",# 22
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 5,   2,   3,   0,   0,   3,   0)
    Sepith("Sepith_B4", 1,   6,   0,   3,   2,   1,   1)

    MonsterBattlePostion("MonsterBattlePostion_C4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_C8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_CC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_D0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_D4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_D8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_DC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_E4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_E8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_EC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_F0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_F4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_F8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_FC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_104", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 2, 13, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_124", 0x0000, 8, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_A4", 50, 50, 0, 0,
        (
            ("ms66500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66500.dat", "ms66500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_194", 0x0000, 8, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_B4", 50, 50, 0, 0,
        (
            ("ms69900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69900.dat", "ms69900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch24200.itc",                   # 00
        "chr/ch30000.itc",                   # 01
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
        "monster/ch66550.itc",               # 10
        "monster/ch66551.itc",               # 11
        "monster/ch69950.itc",               # 12
        "monster/ch69950.itc",               # 13
    ))

    DeclNpc(26100,   0,       -3000,   270,  405,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(24799,   0,       -3000,   90,   405,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(130449,  38270,   2000,    0x1010000,    "BattleInfo_124", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(133810,  75570,   3000,    0x1010000,    "BattleInfo_194", 0,   18,  0xFFFF, 2,  3)

    DeclActor(111510,  -2000,   78150,   1200,    111510,  -1000,   78150,   0x007C, 0,  3,  0x0000)
    DeclActor(118170,  3000,    85350,   1200,    118170,  4000,    85350,   0x007C, 0,  4,  0x0000)
    DeclActor(550,     0,       4660,    1200,    550,     1000,    4660,    0x007C, 0,  26, 0x0000)
    DeclActor(121570,  3000,    68820,   1200,    121570,  3000,    68820,   0x007C, 0,  5,  0x0000)
    DeclActor(14350,   0,       4400,    1200,    14350,   2000,    4400,    0x007C, 0,  27, 0x0000)
    DeclActor(134500,  3000,    82200,   1200,    134470,  4000,    82230,   0x007C, 0,  51, 0x0000)
    DeclActor(6200,    0,       -5000,   800,     6200,    1500,    -5000,   0x007C, 0,  13, 0x0000)
    DeclActor(2200,    0,       -5000,   800,     2200,    1500,    -5000,   0x007C, 0,  14, 0x0000)
    DeclActor(13550,   0,       -5000,   800,     13550,   1500,    -5000,   0x007C, 0,  15, 0x0000)
    DeclActor(8450,    0,       -5000,   800,     8450,    1500,    -5000,   0x007C, 0,  16, 0x0000)
    DeclActor(16950,   0,       5800,    800,     16950,   1500,    5800,    0x007C, 0,  17, 0x0000)
    DeclActor(11850,   0,       5800,    800,     11850,   1500,    5800,    0x007C, 0,  18, 0x0000)
    DeclActor(22600,   0,       -5000,   800,     22600,   1500,    -5000,   0x007C, 0,  19, 0x0000)
    DeclActor(18350,   0,       -5000,   800,     18360,   1500,    -5000,   0x007C, 0,  20, 0x0000)
    DeclActor(29400,   0,       -5000,   800,     29400,   1500,    -5000,   0x007C, 0,  21, 0x0000)
    DeclActor(24900,   0,       -5000,   800,     24900,   1500,    -5000,   0x007C, 0,  22, 0x0000)
    DeclActor(4010,    0,       6840,    1500,    4010,    1700,    6840,    0x007C, 0,  52, 0x0000)

    PlaceName(-17.0, 0.0, -7.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(203.0, 0.0, 27.5, 0x0000, 0x0000, "To Armorica Village & Tangram Gate")
    PlaceName(0.5899999737739563, 0.0, 4.840000152587891, 0x0000, 0x0055, "")
    PlaceName(14.899999618530273, 0.0, 6.0, 0x0000, 0x0056, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 3

    ScpFunction((
        "Function_0_844",          # 00, 0
        "Function_1_8FC",          # 01, 1
        "Function_2_C2F",          # 02, 2
        "Function_3_1222",         # 03, 3
        "Function_4_1383",         # 04, 4
        "Function_5_14F0",         # 05, 5
        "Function_6_1504",         # 06, 6
        "Function_7_15EA",         # 07, 7
        "Function_8_1706",         # 08, 8
        "Function_9_179E",         # 09, 9
        "Function_10_1D77",        # 0A, 10
        "Function_11_1E66",        # 0B, 11
        "Function_12_1ED0",        # 0C, 12
        "Function_13_1F50",        # 0D, 13
        "Function_14_1FB2",        # 0E, 14
        "Function_15_2035",        # 0F, 15
        "Function_16_2098",        # 10, 16
        "Function_17_211B",        # 11, 17
        "Function_18_217E",        # 12, 18
        "Function_19_2201",        # 13, 19
        "Function_20_2264",        # 14, 20
        "Function_21_22E7",        # 15, 21
        "Function_22_2450",        # 16, 22
        "Function_23_24D3",        # 17, 23
        "Function_24_2542",        # 18, 24
        "Function_25_2738",        # 19, 25
        "Function_26_29F3",        # 1A, 26
        "Function_27_2A63",        # 1B, 27
        "Function_28_2A71",        # 1C, 28
        "Function_29_3C8B",        # 1D, 29
        "Function_30_3CEC",        # 1E, 30
        "Function_31_3DC5",        # 1F, 31
        "Function_32_41C7",        # 20, 32
        "Function_33_5AAE",        # 21, 33
        "Function_34_6809",        # 22, 34
        "Function_35_7817",        # 23, 35
        "Function_36_8867",        # 24, 36
        "Function_37_9889",        # 25, 37
        "Function_38_98F8",        # 26, 38
        "Function_39_9986",        # 27, 39
        "Function_40_9A1C",        # 28, 40
        "Function_41_9AB2",        # 29, 41
        "Function_42_9B09",        # 2A, 42
        "Function_43_9B60",        # 2B, 43
        "Function_44_9BB2",        # 2C, 44
        "Function_45_9BD1",        # 2D, 45
        "Function_46_9BF0",        # 2E, 46
        "Function_47_9C0F",        # 2F, 47
        "Function_48_9C2E",        # 30, 48
        "Function_49_9C4D",        # 31, 49
        "Function_50_9C98",        # 32, 50
        "Function_51_9CC0",        # 33, 51
        "Function_52_A090",        # 34, 52
    ))


    def Function_0_844(): pass

    label("Function_0_844")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_884"),
        (1, "loc_890"),
        (2, "loc_89C"),
        (3, "loc_8A8"),
        (4, "loc_8B4"),
        (5, "loc_8C0"),
        (6, "loc_8CC"),
        (SWITCH_DEFAULT, "loc_8D8"),
    )


    label("loc_884")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_890")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_89C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8A8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8B4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8C0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8FB")

    Return()

    # Function_0_844 end

    def Function_1_8FC(): pass

    label("Function_1_8FC")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xF9, 4)
    SetScenarioFlags(0xFB, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_91A")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 31)

    label("loc_91A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_930")
    SetMapFlags(0x10000000)
    Event(0, 28)

    label("loc_930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_93F")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 8)

    label("loc_93F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_957")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_957")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BDE")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BD")
    SetScenarioFlags(0x7A, 0)

    label("loc_9BD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D3")
    SetScenarioFlags(0x7A, 1)

    label("loc_9D3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E9")
    SetScenarioFlags(0x7A, 2)

    label("loc_9E9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FF")
    SetScenarioFlags(0x7A, 3)

    label("loc_9FF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A15")
    SetScenarioFlags(0x7A, 4)

    label("loc_A15")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2B")
    SetScenarioFlags(0x7A, 5)

    label("loc_A2B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A41")
    SetScenarioFlags(0x7A, 6)

    label("loc_A41")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A57")
    SetScenarioFlags(0x7A, 7)

    label("loc_A57")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6D")
    SetScenarioFlags(0x7B, 0)

    label("loc_A6D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A83")
    SetScenarioFlags(0x7B, 1)

    label("loc_A83")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A99")
    SetScenarioFlags(0x7B, 2)

    label("loc_A99")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAF")
    SetScenarioFlags(0x7B, 3)

    label("loc_AAF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC5")
    SetScenarioFlags(0x7B, 4)

    label("loc_AC5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADB")
    SetScenarioFlags(0x7B, 5)

    label("loc_ADB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF1")
    SetScenarioFlags(0x7B, 6)

    label("loc_AF1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B07")
    SetScenarioFlags(0x7B, 7)

    label("loc_B07")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B42")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_BDE")

    label("loc_B42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B59")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_BDE")

    label("loc_B59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B70")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_BDE")

    label("loc_B70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B87")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_BDE")

    label("loc_B87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9E")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_BDE")

    label("loc_B9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB5")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_BDE")

    label("loc_BB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCC")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_BDE")

    label("loc_BCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDE")
    SetScenarioFlags(0x7C, 7)

    label("loc_BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_BEC")
    Jump("loc_C18")

    label("loc_BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C18")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C18")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_C18")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C2E")
    Event(0, 30)

    label("loc_C2E")

    Return()

    # Function_1_8FC end

    def Function_2_C2F(): pass

    label("Function_2_C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C42")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C42")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5B")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_C61")

    label("loc_C5B")

    OP_10(0x0, 0x1)
    OP_10(0x2, 0x0)

    label("loc_C61")

    SetChrFlags(0xA, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA9")
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    ClearMapObjFlags(0x5, 0x4)
    OP_66(0x4, 0x1)
    Jump("loc_CAE")

    label("loc_CA9")

    OP_16(0x3, 0x3, 0x1, 0x0)

    label("loc_CAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC1")
    OP_70(0x2, 0x0)
    Jump("loc_CC5")

    label("loc_CC1")

    OP_70(0x2, 0x1E)

    label("loc_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD8")
    OP_70(0x3, 0x0)
    Jump("loc_CDC")

    label("loc_CD8")

    OP_70(0x3, 0x1E)

    label("loc_CDC")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 0)), scpexpr(EXPR_END)), "loc_D39")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 121570, 3000, 68820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_D39")

    OP_65(0x5, 0x1)
    SetMapObjFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5D")
    OP_66(0x5, 0x1)

    label("loc_D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D6C")
    ClearMapObjFlags(0xB, 0x4)

    label("loc_D6C")

    OP_78(0x6, 0x14)
    OP_78(0x7, 0x15)
    OP_78(0x8, 0x16)
    OP_78(0x9, 0x17)
    OP_78(0xA, 0x18)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    SetMapObjFrame(0x6, "chukin", 0x0, 0x1)
    SetMapObjFrame(0x7, "chukin", 0x0, 0x1)
    SetMapObjFrame(0x8, "chukin", 0x0, 0x1)
    SetMapObjFrame(0x9, "chukin", 0x0, 0x1)
    SetMapObjFrame(0xA, "chukin", 0x0, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    OP_65(0x9, 0x1)
    OP_65(0xA, 0x1)
    OP_65(0xB, 0x1)
    OP_65(0xC, 0x1)
    OP_65(0xD, 0x1)
    OP_65(0xE, 0x1)
    OP_65(0xF, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_E5B")
    Jump("loc_1221")

    label("loc_E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_F88")
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    SetChrPos(0x14, 4270, 0, -5000, 270)
    OP_D3(0x14, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x15, 10750, 0, -5000, 270)
    OP_D3(0x15, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x16, 14000, 0, 5750, 270)
    OP_D3(0x16, 0x0, 0x41EB0, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F2F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_F00")
    Jump("loc_F2A")

    label("loc_F00")

    ClearMapObjFlags(0xA, 0x4)
    SetChrPos(0x18, 27500, 0, -5000, 270)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_F2A")

    Jump("loc_F83")

    label("loc_F2F")

    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetChrPos(0x17, 20500, 0, -5000, 270)
    OP_D3(0x17, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x18, 27500, 0, -5000, 270)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_F83")

    Jump("loc_1221")

    label("loc_F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1079")
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetChrPos(0x14, 4270, 0, -5000, 270)
    OP_D3(0x14, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x15, 10750, 0, -5000, 270)
    OP_D3(0x15, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x16, 14000, 0, 5750, 270)
    OP_D3(0x16, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x18, 27500, 0, -5000, 270)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_104A")
    Jump("loc_1074")

    label("loc_104A")

    ClearMapObjFlags(0x9, 0x4)
    SetChrPos(0x17, 20500, 0, -5000, 270)
    OP_D3(0x17, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_1074")

    Jump("loc_1221")

    label("loc_1079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1221")
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetChrPos(0x14, 4270, 0, -5000, 270)
    OP_D3(0x14, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x15, 10750, 0, -5000, 270)
    OP_D3(0x15, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x16, 14000, 0, 5750, 270)
    OP_D3(0x16, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x17, 20500, 0, -5000, 270)
    OP_D3(0x17, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x18, 27500, 0, -5000, 270)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1165")
    Jump("loc_1221")

    label("loc_1165")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_1221")
    OP_66(0x6, 0x1)
    OP_66(0x7, 0x1)
    OP_66(0x8, 0x1)
    OP_66(0x9, 0x1)
    OP_66(0xA, 0x1)
    OP_66(0xB, 0x1)
    OP_66(0xC, 0x1)
    OP_66(0xD, 0x1)
    OP_66(0xE, 0x1)
    OP_66(0xF, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_11B5")
    SetMapObjFrame(0x6, "chukin", 0x1, 0x1)

    label("loc_11B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_11D0")
    SetMapObjFrame(0x7, "chukin", 0x1, 0x1)

    label("loc_11D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_11EB")
    SetMapObjFrame(0x8, "chukin", 0x1, 0x1)

    label("loc_11EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_1206")
    SetMapObjFrame(0x9, "chukin", 0x1, 0x1)

    label("loc_1206")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x12)"), scpexpr(EXPR_END)), "loc_1221")
    SetMapObjFrame(0xA, "chukin", 0x1, 0x1)

    label("loc_1221")

    Return()

    # Function_2_C2F end

    def Function_3_1222(): pass

    label("Function_3_1222")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_130C")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_12A2")
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
    SetScenarioFlags(0x100, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1307")

    label("loc_12A2")

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
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1307")

    Jump("loc_1377")

    label("loc_130C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "AHHH! Goddess, it hurts! The grass\x01",
            "is clipping right through me!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1377")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1222 end

    def Function_4_1383(): pass

    label("Function_4_1383")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146D")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5DF, 1)"), scpexpr(EXPR_END)), "loc_1403")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5DF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x100, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_1468")

    label("loc_1403")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5DF),
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

    label("loc_1468")

    Jump("loc_14E4")

    label("loc_146D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Welcome to the Crossbell Watchtower.\x01",
            "...We don't know what it's for, either.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_14E4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1383 end

    def Function_5_14F0(): pass

    label("Function_5_14F0")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_5_14F0 end

    def Function_6_1504(): pass

    label("Function_6_1504")

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
            "Armorica Village\x01",      # 0
            "Tangram Gate\x01",          # 1
            "Bus Stop (Fork)\x01",       # 2
            "Leave\x01",                 # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159D")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_15E2")

    label("loc_159D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C2")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_15E2")

    label("loc_15C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E2")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_15E2")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_1504 end

    def Function_7_15EA(): pass

    label("Function_7_15EA")

    Fade(1000)
    OP_68(-620, 600, 4110, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(27000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -1000, 0, 4500, 180)
    SetChrPos(0x1, -1000, 0, 5600, 180)
    SetChrPos(0x2, -1000, 0, 6700, 180)
    SetChrPos(0x3, -1000, 0, 7800, 180)
    ClearChrFlags(0xA, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0xA)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xA, 16000, 0, 0, 0)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_0D()
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_16C0():
        OP_98(0xFE, 0xFFFFC180, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16C0)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xA, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_7_15EA end

    def Function_8_1706(): pass

    label("Function_8_1706")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -1000, 0, 4500, 180)
    SetChrPos(0x1, -1000, 0, 4500, 180)
    SetChrPos(0x2, -1000, 0, 4500, 180)
    SetChrPos(0x3, -1000, 0, 4500, 180)
    Sleep(1)
    OP_68(-1000, 600, 4500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(25000, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_8_1706 end

    def Function_9_179E(): pass

    label("Function_9_179E")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D6F")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D0C")
    Sound(1500, 255, 100, 0)
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1844")
    MenuCmd(1, 1, "★City - Central Square")
    MenuCmd(3, 1, 0x0)
    Jump("loc_185F")

    label("loc_1844")

    MenuCmd(1, 1, "　City - Central Square")

    label("loc_185F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_188D")
    MenuCmd(1, 1, "★City - East Exit")
    MenuCmd(3, 1, 0x1)
    Jump("loc_18A3")

    label("loc_188D")

    MenuCmd(1, 1, "　City - East Exit")

    label("loc_18A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D1")
    MenuCmd(1, 1, "★City - West Exit")
    MenuCmd(3, 1, 0x2)
    Jump("loc_18E7")

    label("loc_18D1")

    MenuCmd(1, 1, "　City - West Exit")

    label("loc_18E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1916")
    MenuCmd(1, 1, "★City - South Exit")
    MenuCmd(3, 1, 0x3)
    Jump("loc_192D")

    label("loc_1916")

    MenuCmd(1, 1, "　City - South Exit")

    label("loc_192D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_195C")
    MenuCmd(1, 1, "★City - North Exit")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1973")

    label("loc_195C")

    MenuCmd(1, 1, "　City - North Exit")

    label("loc_1973")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_199D")
    MenuCmd(1, 1, "★Tangram Gate")
    MenuCmd(3, 1, 0x5)
    Jump("loc_19AF")

    label("loc_199D")

    MenuCmd(1, 1, "　Tangram Gate")

    label("loc_19AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19DB")
    MenuCmd(1, 1, "★Bellguard Gate")
    MenuCmd(3, 1, 0x6)
    Jump("loc_19EF")

    label("loc_19DB")

    MenuCmd(1, 1, "　Bellguard Gate")

    label("loc_19EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A27")
    MenuCmd(1, 1, "★St. Ursula Medical College")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1A47")

    label("loc_1A27")

    MenuCmd(1, 1, "　St. Ursula Medical College")

    label("loc_1A47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A75")
    MenuCmd(1, 1, "★Armorica Village")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1A8B")

    label("loc_1A75")

    MenuCmd(1, 1, "　Armorica Village")

    label("loc_1A8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ABD")
    MenuCmd(1, 1, "★Mainz Mining Village")
    MenuCmd(3, 1, 0x9)
    Jump("loc_1AD7")

    label("loc_1ABD")

    MenuCmd(1, 1, "　Mainz Mining Village")

    label("loc_1AD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B11")
    MenuCmd(1, 1, "★Mainz Mountain Path - Tunnel")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1B33")

    label("loc_1B11")

    MenuCmd(1, 1, "　Mainz Mountain Path - Tunnel")

    label("loc_1B33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B62")
    MenuCmd(1, 1, "★Stargazer's Tower")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1B79")

    label("loc_1B62")

    MenuCmd(1, 1, "　Stargazer's Tower")

    label("loc_1B79")

    MenuCmd(1, 1, "　Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CFD")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xF1, 0x10E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x5)
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
        (0, "loc_1C50"),
        (1, "loc_1C5E"),
        (2, "loc_1C6C"),
        (3, "loc_1C7A"),
        (4, "loc_1C88"),
        (5, "loc_1C96"),
        (6, "loc_1CA4"),
        (7, "loc_1CB2"),
        (8, "loc_1CC0"),
        (9, "loc_1CCE"),
        (10, "loc_1CDC"),
        (11, "loc_1CEA"),
        (SWITCH_DEFAULT, "loc_1CF8"),
    )


    label("loc_1C50")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CF8")

    label("loc_1C5E")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CF8")

    label("loc_1C6C")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CF8")

    label("loc_1C7A")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CF8")

    label("loc_1C88")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CF8")

    label("loc_1C96")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CF8")

    label("loc_1CA4")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CF8")

    label("loc_1CB2")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CF8")

    label("loc_1CC0")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CF8")

    label("loc_1CCE")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CF8")

    label("loc_1CDC")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CF8")

    label("loc_1CEA")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CF8")

    label("loc_1CF8")

    Jump("loc_1D07")

    label("loc_1CFD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D07")

    Jump("loc_1D6A")

    label("loc_1D0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D57")
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
    Jump("loc_1D6A")

    label("loc_1D57")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D6A")

    Jump("loc_17B8")

    label("loc_1D6F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_179E end

    def Function_10_1D77(): pass

    label("Function_10_1D77")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 14360, 0, 2630, 180)
    SetChrPos(0x1, 14360, 0, 2630, 180)
    SetChrPos(0x2, 14360, 0, 2630, 180)
    SetChrPos(0x3, 14360, 0, 2630, 180)
    SetChrPos(0x4, 14360, 0, 2630, 180)
    SetChrPos(0x5, 14360, 0, 2630, 180)
    Sleep(1)
    OP_68(14360, 600, 2630, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(25000, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E4B")
    Sound(1502, 255, 100, 0)
    Jump("loc_1E51")

    label("loc_1E4B")

    Sound(1503, 255, 100, 0)

    label("loc_1E51")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1D77 end

    def Function_11_1E66(): pass

    label("Function_11_1E66")

    TalkBegin(0xFE)

    ChrTalk(
        0x8,
        "Damn, they caught on to us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I thought we'd be all right during\x01",
            "the Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1E66 end

    def Function_12_1ED0(): pass

    label("Function_12_1ED0")

    TalkBegin(0xFE)

    ChrTalk(
        0x9,
        (
            "Let's see... You parked two cars on\x01",
            "a single permit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Okay, sign this for me.\x01",
            "All that's left is the fine, now.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1ED0 end

    def Function_13_1F50(): pass

    label("Function_13_1F50")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a Verne Company luxury car.\x02\x03",
            "The license plate number is 'VE 4310.'\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 1)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_13_1F50 end

    def Function_14_1FB2(): pass

    label("Function_14_1FB2")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_2007")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An illegal parking warning sticker\x01",
            "is placed on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2031")

    label("loc_2007")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2031")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x6, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0xA)

    label("loc_2031")

    TalkEnd(0xFF)
    Return()

    # Function_14_1FB2 end

    def Function_15_2035(): pass

    label("Function_15_2035")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a Verne Company orbal truck.\x02\x03",
            "The license plate number is 'ES 4521.'\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 2)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_15_2035 end

    def Function_16_2098(): pass

    label("Function_16_2098")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_20ED")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An illegal parking warning sticker\x01",
            "is placed on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2117")

    label("loc_20ED")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2117")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x7, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0xC)

    label("loc_2117")

    TalkEnd(0xFF)
    Return()

    # Function_16_2098 end

    def Function_17_211B(): pass

    label("Function_17_211B")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a Verne Company orbal truck.\x02\x03",
            "The license plate number is 'LA 5828.'\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 3)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_17_211B end

    def Function_18_217E(): pass

    label("Function_18_217E")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_21D3")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An illegal parking warning sticker\x01",
            "is placed on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_21FD")

    label("loc_21D3")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21FD")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x8, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0xE)

    label("loc_21FD")

    TalkEnd(0xFF)
    Return()

    # Function_18_217E end

    def Function_19_2201(): pass

    label("Function_19_2201")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a Verne Company private car.\x02\x03",
            "The license plate number is 'CW 6422.'\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 4)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_19_2201 end

    def Function_20_2264(): pass

    label("Function_20_2264")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_22B9")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An illegal parking warning sticker\x01",
            "is placed on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_22E3")

    label("loc_22B9")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E3")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x9, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x10)

    label("loc_22E3")

    TalkEnd(0xFF)
    Return()

    # Function_20_2264 end

    def Function_21_22E7(): pass

    label("Function_21_22E7")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a Reinford Company luxury car.\x02\x03",
            "The license plate number is 'CL 1101.'\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_23A8")

    ChrTalk(
        0x101,
        (
            "#0001F(I'm pretty sure I saw this plate number\x01",
            "over at the western exit, too.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2446")

    label("loc_23A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23C1")
    Call(0, 25)
    Jump("loc_2446")

    label("loc_23C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2439")

    ChrTalk(
        0x101,
        (
            "#0005F(Hold on a second...)\x02\x03",
            "#0003F(I feel like I've seen this license plate\x01",
            "number before.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2446")

    label("loc_2439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2446")
    SetScenarioFlags(0xBC, 5)

    label("loc_2446")

    SetScenarioFlags(0xBE, 5)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_21_22E7 end

    def Function_22_2450(): pass

    label("Function_22_2450")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x12)"), scpexpr(EXPR_END)), "loc_24A5")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An illegal parking warning sticker\x01",
            "is placed on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_24CF")

    label("loc_24A5")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24CF")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0xA, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x12)

    label("loc_24CF")

    TalkEnd(0xFF)
    Return()

    # Function_22_2450 end

    def Function_23_24D3(): pass

    label("Function_23_24D3")

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

    # Function_23_24D3 end

    def Function_24_2542(): pass

    label("Function_24_2542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2737")

    ChrTalk(
        0x101,
        (
            "#0000FAll right. I think we've checked\x01",
            "all of the cars.\x02\x03",
            "Let's finish placing the remaining\x01",
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

    label("loc_2737")

    Return()

    # Function_24_2542 end

    def Function_25_2738(): pass

    label("Function_25_2738")

    EventBegin(0x0)
    Fade(500)
    OP_E0(0x1)
    OP_68(31390, 600, -2940, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(490, 0)
    SetCameraDistance(19340, 0)
    SetChrPos(0x101, 31050, 0, -4940, 270)
    SetChrPos(0x102, 32700, 0, -4120, 270)
    SetChrPos(0x103, 31500, 0, -3440, 225)
    SetChrPos(0x104, 31000, 0, -2310, 225)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0005FWait, what...?\x02\x03",
            "#0001FDidn't we see this plate number over\x01",
            "at the west exit, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0105FActually, I think you're right.\x02\x03",
            "#0100FI don't think it was this\x01",
            "type of car, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0200FIt is against state regulation for multiple\x01",
            "vehicles to share an identical license\x01",
            "plate number.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0303FYeah, Tio Tot's right. Gotta have a unique\x01",
            "number, or you're breakin' the law.\x02\x03",
            "#0300FProbably a good idea to jot this plate\x01",
            "down, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FAbsolutely. We'd better report this\x01",
            "to the Metropolitan Division later.\x02",
        )
    )

    CloseMessageWindow()
    OP_E0(0x0)
    SetChrPos(0x0, 31050, 0, -4940, 270)
    OP_29(0x17, 0x1, 0x14)
    EventEnd(0x5)
    Return()

    # Function_25_2738 end

    def Function_26_29F3(): pass

    label("Function_26_29F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A04")
    Call(0, 6)
    Jump("loc_2A62")

    label("loc_2A04")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#0006FLet's try to get to Armorica Village\x01",
            "by foot.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_2A62")

    Return()

    # Function_26_29F3 end

    def Function_27_2A63(): pass

    label("Function_27_2A63")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_27_2A63 end

    def Function_28_2A71(): pass

    label("Function_28_2A71")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-5000, 1000, 0, 0)
    MoveCamera(36, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -7100, 0, -700, 90)
    SetChrPos(0x102, -8500, 0, -700, 90)
    SetChrPos(0x103, -8500, 0, 700, 90)
    SetChrPos(0x104, -7100, 0, 700, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0xA)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xA, 16000, 0, 6000, 0)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x1E)
    FadeToBright(1000, 0)

    def lambda_2B51():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B51)

    def lambda_2B6B():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B6B)

    def lambda_2B85():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B85)

    def lambda_2B9F():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B9F)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
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
    OP_68(15320, 1000, 6120, 2500)
    OP_6F(0x1)
    OP_71(0x0, 0x1F, 0x3C, 0x0, 0x0)
    Sound(463, 0, 100, 0)
    OP_79(0x0)

    ChrTalk(
        0x101,
        "#1100261V#0011FOh, shoot!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x19, 1, 0, 29)
    OP_71(0x0, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0xB4, 0x79, 0x0, 0x20)

    def lambda_2C9E():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2C9E)
    WaitChrThread(0xA, 1)
    Sleep(100)
    OP_68(15320, 1000, 0, 4000)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2CDC():
        OP_9E(0xFE, 0x4268, 0x7D0, 0xFFFD40E0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2CDC)
    WaitChrThread(0xA, 1)
    OP_71(0x0, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2D16():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2D16)
    WaitChrThread(0xA, 1)
    SetMapObjFlags(0x0, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_6F(0x1)
    OP_68(3200, 800, 0, 2000)

    def lambda_2D57():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D57)
    Sleep(50)

    def lambda_2D74():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D74)
    Sleep(50)

    def lambda_2D91():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2D91)
    Sleep(50)

    def lambda_2DAE():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2DAE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x102,
        "#1100262V#0106F#6PWe just barely missed it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100263V#0306F#5PMan, you kiddin' me?\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#1100264V#0308F#5PYou got any idea how many trips\x01",
            "the bus makes?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1100265V#0006F#12PHmm... I'm sure it comes by\x01",
            "pretty frequently.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(500)

    def lambda_2EFC():

        label("loc_2EFC")

        TurnDirection(0x101, 0x103, 500)
        Yield()
        Jump("loc_2EFC")

    QueueWorkItem2(0x101, 1, lambda_2EFC)

    def lambda_2F0E():

        label("loc_2F0E")

        TurnDirection(0x102, 0x103, 500)
        Yield()
        Jump("loc_2F0E")

    QueueWorkItem2(0x102, 1, lambda_2F0E)

    def lambda_2F20():

        label("loc_2F20")

        TurnDirection(0x104, 0x103, 500)
        Yield()
        Jump("loc_2F20")

    QueueWorkItem2(0x104, 1, lambda_2F20)
    OP_68(1810, 800, 2340, 2000)

    def lambda_2F43():
        OP_95(0xFE, 610, 0, 3820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2F43)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)

    ChrTalk(
        0x103,
        (
            "#1100266V#0203F#6PAccording to the schedule here...\x02\x03",
            "#1100267V#0200F...the next bus will depart in\x01",
            "approximately two hours.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#1100268V#0105F#6PIt's that long of a wait?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100269V#0306F#11PDoesn't sound as frequent as you\x01",
            "were hopin' for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100270V#0006F#12PWell, that's just great. And here I was,\x01",
            "hoping we could also make it to the\x01",
            "hospital later.\x02\x03",
            "#1100271V#0008FAnd that's not even mentioning the\x01",
            "other areas we still need to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100272V#0106F#6PAnd we had just decided on how\x01",
            "to proceed with our investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_93(0x103, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1100273V#0200F#5PGiven the circumstances, could we not\x01",
            "simply walk to Armorica Village?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1100274V#0005F#12PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100275V#0105F#6PTio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100276V#0305F#2PYou for real?\x02",
    )

    CloseMessageWindow()
    OP_68(1980, 800, 790, 1500)

    def lambda_3309():

        label("loc_3309")

        TurnDirection(0x101, 0x103, 500)
        Yield()
        Jump("loc_3309")

    QueueWorkItem2(0x101, 1, lambda_3309)

    def lambda_331B():

        label("loc_331B")

        TurnDirection(0x102, 0x103, 500)
        Yield()
        Jump("loc_331B")

    QueueWorkItem2(0x102, 1, lambda_331B)

    def lambda_332D():

        label("loc_332D")

        TurnDirection(0x104, 0x103, 500)
        Yield()
        Jump("loc_332D")

    QueueWorkItem2(0x104, 1, lambda_332D)

    def lambda_333F():
        OP_95(0xFE, 500, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_333F)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)

    ChrTalk(
        0x103,
        (
            "#1100277V#0204F#5PJudging by the distance shown on the map,\x01",
            "I would estimate that it takes approximately\x01",
            "one and a half hours to walk to Armorica.\x02\x03",
            "#1100278V#0202FConversely, sitting and waiting for the next\x01",
            "bus will result in a two and a half hour trip.\x02\x03",
            "#1100279VWould it not be more efficient of us to walk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100280V#0100F#6PWhen you spell it out like that, it certainly\x01",
            "does make sense.\x02\x03",
            "#1100281V#0104FI've actually heard stories of how scenic\x01",
            "the road leading to Armorica is.\x02\x03",
            "#1100282V#0102FPerhaps it'd be more enjoyable if we think\x01",
            "of it as a fun little hiking trip, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x104,
        (
            "#1100283V#0306F#5P(Dude... These gals seriously tryin' to\x01",
            "convince themselves this'll be a jolly\x01",
            "good time?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100284V#0006F#11P(It's painfully obvious they've never\x01",
            "trekked the highway on foot.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_36D7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36D7)
    Sleep(50)

    def lambda_36E7():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_36E7)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        "#1100285V#0105F#6PWhat are you two whispering about?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#1100286V#0012F#11PN-Nothing.\x02\x03",
            "#1100287V#0001FYou know, monsters tend to roam around\x01",
            "the highways. Are you girls okay with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100288V#0106F#6PHmm, I hadn't thought of that...\x02\x03",
            "#1100289V#0100FHowever, we've ventured into the Geofront,\x01",
            "so I think we'll be fine if we run into a few\x01",
            "monsters here and there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100290V#0203F#6PAdditionally, I still need to accumulate\x01",
            "more combat data for my orbal staff.\x02\x03",
            "#1100291V#0200FParticipating in more skirmishes is a\x01",
            "necessary task.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100292V#0006F#11PHmm...\x02\x03",
            "#1100293V#0000F...All right. If you're dead set on walking,\x01",
            "then we'll do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100294V#0100F#6PSounds lovely. Let's get going.\x02",
    )

    CloseMessageWindow()
    StopBGM(0x5DC)

    def lambda_39CE():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39CE)
    Sleep(100)

    def lambda_39DE():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_39DE)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7204", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x102,
        (
            "#1100295V#0109F#12PHeehee. I'm starting to get a little excited.\x02\x03",
            "#1100296V#0102FHad I known this would happen, I would\x01",
            "have prepared us lunch.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x103,
        (
            "#1100297V#0204F#5PThat is true.\x02\x03",
            "#1100298V#0202FShould we depart soon, we will arrive at the\x01",
            "village by noon. I am certain we can have\x01",
            "lunch while we are there.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x104)

    ChrTalk(
        0x101,
        (
            "#1100299V#0008F#11P(It's up to us to protect them\x01",
            "if they get exhausted.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100300V#0302F#5P(Yeah, yeah. I got this, man.)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(25500, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1070, 600, -160, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, -1070, 0, -160, 90)
    SetScenarioFlags(0x60, 1)
    OP_29(0x3F, 0x1, 0x1)
    EndChrThread(0x19, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_28_2A71 end

    def Function_29_3C8B(): pass

    label("Function_29_3C8B")

    Sound(470, 0, 100, 0)
    Sleep(2000)
    Sound(465, 0, 100, 0)
    Sleep(500)
    Sound(467, 0, 100, 0)
    Sleep(4500)
    Sound(469, 0, 100, 0)
    Sleep(2000)
    OP_25(0x1D5, 0x5A)
    Sleep(300)
    OP_25(0x1D5, 0x50)
    Sleep(300)
    OP_25(0x1D5, 0x46)
    Sleep(300)
    OP_25(0x1D5, 0x3C)
    Sleep(300)
    OP_25(0x1D5, 0x32)
    Sleep(300)
    OP_25(0x1D5, 0x28)
    Sleep(300)
    OP_25(0x1D5, 0x1E)
    Sleep(300)
    OP_25(0x1D5, 0x14)
    Sleep(300)
    OP_25(0x1D5, 0xA)
    Return()

    # Function_29_3C8B end

    def Function_30_3CEC(): pass

    label("Function_30_3CEC")

    EventBegin(0x0)
    Sleep(1000)
    OP_68(920, 600, 5160, 5000)
    MoveCamera(45, 21, 0, 5000)
    OP_6E(450, 5000)
    SetCameraDistance(25000, 5000)
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

    # Function_30_3CEC end

    def Function_31_3DC5(): pass

    label("Function_31_3DC5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch07300.itc", 0x23)
    LoadChrToIndex("chr/ch24100.itc", 0x24)
    LoadChrToIndex("chr/ch20800.itc", 0x25)
    LoadChrToIndex("chr/ch33000.itc", 0x26)
    LoadChrToIndex("chr/ch24500.itc", 0x27)
    LoadChrToIndex("chr/ch21200.itc", 0x28)
    LoadChrToIndex("chr/ch21300.itc", 0x29)
    LoadChrToIndex("chr/ch21000.itc", 0x2A)
    LoadChrToIndex("chr/ch21400.itc", 0x2B)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x27)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x28)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x2A)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x2B)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x101, 9700, 0, 1350, 270)
    SetChrPos(0x102, 9700, 0, 2950, 270)
    SetChrPos(0x103, 11200, 0, 1350, 270)
    SetChrPos(0x104, 11200, 0, 2950, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 16000, 600, 5380, 180)
    SetChrPos(0xC, 16000, 600, 5380, 180)
    SetChrPos(0xD, 16000, 600, 5380, 180)
    SetChrPos(0xE, 16000, 600, 5380, 180)
    SetChrPos(0xF, 16000, 600, 5380, 180)
    SetChrPos(0x10, 16000, 600, 5380, 180)
    SetChrPos(0x11, 16000, 600, 5380, 180)
    SetChrPos(0x12, 16000, 600, 5380, 180)
    SetChrPos(0x13, 16000, 600, 5380, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0xA)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xA, 16000, 0, 6000, 0)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x1E)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    OP_68(16230, 600, 5720, 0)
    MoveCamera(29, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(28500, 0)
    SetCameraDistance(26000, 12000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_40D8")
    Call(0, 36)
    OP_29(0x1B, 0x1, 0x14)
    Jump("loc_413F")

    label("loc_40D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xF)"), scpexpr(EXPR_END)), "loc_40F3")
    Call(0, 32)
    OP_29(0x1B, 0x1, 0x13)
    Jump("loc_413F")

    label("loc_40F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_410E")
    Call(0, 33)
    OP_29(0x1B, 0x1, 0x14)
    Jump("loc_413F")

    label("loc_410E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x11)"), scpexpr(EXPR_END)), "loc_4129")
    Call(0, 35)
    OP_29(0x1B, 0x1, 0x14)
    Jump("loc_413F")

    label("loc_4129")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x12)"), scpexpr(EXPR_END)), "loc_413F")
    Call(0, 34)
    OP_29(0x1B, 0x1, 0x14)

    label("loc_413F")

    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_49()
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    SetScenarioFlags(0x5C, 1)
    NewScene("c100C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_3DC5 end

    def Function_32_41C7(): pass

    label("Function_32_41C7")

    BeginChrThread(0x13, 3, 0, 38)
    Sleep(750)
    BeginChrThread(0x12, 3, 0, 37)
    Sleep(4000)
    BeginChrThread(0xD, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0x10, 3, 0, 39)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 40)
    Sleep(1500)
    BeginChrThread(0xE, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xF, 3, 0, 42)
    Sleep(1500)
    BeginChrThread(0xB, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xC, 3, 0, 43)
    Sleep(2500)
    OP_6F(0x10)
    Fade(500)
    OP_68(2130, 1200, 2100, 0)
    MoveCamera(317, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19910, 0)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0xC, 3)

    ChrTalk(
        0x101,
        "#1P#0001FCould you please wait a moment?\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_42C6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_42C6)
    BeginChrThread(0x101, 3, 0, 44)
    BeginChrThread(0x102, 3, 0, 45)
    BeginChrThread(0x103, 3, 0, 46)
    BeginChrThread(0x104, 3, 0, 47)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    ChrTalk(
        0xC,
        (
            "#5POh! If it isn't those fine young folk\x01",
            "I met at the border.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PWhat might you dearies need with a\x01",
            "little old lady like myself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FWe apologize for not having told\x01",
            "you this sooner, but...\x02\x03",
            "#0001F...we're with the Crossbell police,\x01",
            "Special Support Section.\x02\x03",
            "We'd like for you to answer a few\x01",
            "quick questions, ma'am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PHmm? E-Excuse me, sonny? Are you\x01",
            "implying something? What am I guilty of?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PNo matter the situation, isn't it rude to\x01",
            "bother a frail old lady like myself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FI understand your reservation, but the CPD\x01",
            "received some interesting information today.\x02\x03",
            "A certain group of criminals are supposedly\x01",
            "trying to infiltrate Crossbell.\x02\x03",
            "#0001FWe were tasked with investigating Tangram Gate,\x01",
            "so we covertly questioned any inbound tourists\x01",
            "there.\x02\x03",
            "One of them stood out due to a particularly\x01",
            "strange remark. That remark came from\x01",
            "you, ma'am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PWhat's that supposed to mean, son?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0001FOne of your statements in the dining hall\x01",
            "struck me as incredibly suspicious.\x02\x03",
            "#0003FI believe you claimed that it's been about\x01",
            "three years since you last came to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PAnd? What's so strange about that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PThe area in Calvard I'm from isn't very close\x01",
            "to Crossbell. There's nothing weird about me\x01",
            "visiting infrequently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FI wasn't suggesting anything of the sort.\x01",
            "The problem is what followed.\x02\x03",
            "#0001FYou said you went to the theme park with\x01",
            "your grandson during your last visit, if I'm\x01",
            "not mistaken.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#12P#0104FOh. I see the issue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FYou sly dog, you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FYour fate has already been sealed, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PHmm? I'm not following.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FIt's quite simple, really.\x02\x03",
            "If you had REALLY visited Crossbell\x01",
            "three years ago like you claimed...\x02\x03",
            "#0001F...you would have had trouble visiting\x01",
            "Mishelam Wonderland, considering it\x01",
            "didn't even exist at the time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PWHAT?! This can't be!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PErr... I mean, uh... You see...\x01",
            "The thing is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PO-Oh, yeah! This is all a misunderstanding!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PSilly old me must have read about it\x01",
            "somewhere and got myself confused!\x01",
            "You know how it is with us elderly folks, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FOh, it was a misunderstanding? No problem.\x02\x03",
            "#0000FDo you mind if we give your grandson's\x01",
            "family a quick call to corroborate your\x01",
            "story?\x02\x03",
            "I'm sure they'd be quick to defend you if\x01",
            "the police suspected you, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FThen again, that's not even an option.\x01",
            "You can't call someone who isn't real.\x02\x03",
            "#0003FIt's pretty funny when you think about it.\x01",
            "You went to visit a non-existent theme park\x01",
            "with a non-existent grandson.\x02\x03",
            "This type of mistake would have only been\x01",
            "possible for someone who has visited\x01",
            "Crossbell in the last two years.\x02\x03",
            "#0001FFrequently coming here to run your crooked\x01",
            "business is exactly what allowed for that\x01",
            "contradiction in your statement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PI-I-I...have no idea what you're talking about!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PDo you seriously think a kind elderly lady like\x01",
            "myself would be heinous enough to pawn off\x01",
            "counterfeit goods on unsuspecting people?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0101FI do believe you just put the final nail\x01",
            "in your coffin, ma'am.\x02\x03",
            "Not once during this exchange did\x01",
            "we specify the crime in question.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#5POh. Crap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0309FHahaha! Way to fall for one of the\x01",
            "oldest tricks in the book, ya old bat!\x02\x03",
            "#0300FThink it's about time you face the music.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI am sure you have a perfectly logical\x01",
            "explanation as to why you have access\x01",
            "to sensitive information.\x02\x03",
            "We will be more than happy to listen\x01",
            "to you in our interrogation room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003F(So...that's that, right?)\x02\x03",
            "#0001FI'll give you one last chance, ma'am.\x01",
            "Please turn yourself in peacefully,\x01",
            "or else--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#200WWh-Who#200W...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0xC,
        "Counterfeit Dealer",
        (
            "#5P#5SWHO'D GO ALONG WITH A BUNCH OF\x01",
            "IDIOTIC WHIPPERSNAPPERS?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0011FWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0105FEek!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0305FShe's gone off her rocker!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FHer true nature has finally been revealed.\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0xC,
        "Counterfeit Dealer",
        (
            "#5P#5SYou're all just a bunch of cowards\x01",
            "trying to deceive a helpless old\x01",
            "lady like myself!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0xC,
        "Counterfeit Dealer",
        (
            "#5P#5SI'm sure the Goddess will smite you all\x01",
            "if you don't correct your nasty behavior!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FIt is honestly laughable you can utter\x01",
            "such nonsense without a hint of irony.\x02\x03",
            "#0201FAre you not guilty of deceiving others\x01",
            "with your unscrupulous business?\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0xC,
        "Counterfeit Dealer",
        "#5P#5SShaddap, you damned munchkin!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0205FM-Munchkin...?!\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0xC,
        "Counterfeit Dealer",
        (
            "#5P#5SI hate you! I hate you all! This is exactly\x01",
            "why the police and bracers are trash!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0xC,
        "Counterfeit Dealer",
        (
            "#5P#5SI bet you think you're so righteous!\x01",
            "Maybe you morons should get off\x01",
            "your friggin' high horses!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0011FC-Calm down, ma'am! If you could\x01",
            "just come with us quietl--\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0xC,
        "Counterfeit Dealer",
        (
            "#5P#5SZip it, punk! Got cotton in your ears?!\x01",
            "I said I'm not going with you!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0xC,
        "Counterfeit Dealer",
        "#5P#5SDon't make me repeat myself again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0006F(No! Don't make ME repeat myself!)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Counterfeit Dealer",
        "#5PIf you think you can catch me so easily...\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_57D7():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_57D7)
    Sleep(1000)

    def lambda_57F4():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_57F4)
    Sleep(1000)
    Sleep(10)
    PlayBGM("ed7401", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x191), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(21000, 3000)

    def lambda_582A():
        OP_95(0xFE, -22570, 0, 2200, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_582A)
    Sound(250, 0, 80, 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-50, 20, -1, -1)
    SetChrName("Counterfeit Dealer")

    AnonymousTalk(
        0xC,
        "#5P#5S...then why don't you go ahead and try me?!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    WaitChrThread(0xC, 1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x103)

    ChrTalk(
        0x101,
        (
            "#6P#0005FSeriously?! How can an old lady\x01",
            "move so quickly?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0306FWh-Where the hell did that whole\x01",
            "nicest-grandma-you'd-ever-meet\x01",
            "charade disappear off to?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0206FMunchkin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0103FIs it REALLY the time for this, you guys?!\x02\x03",
            "#0101FWe need to hurry up and chase after her,\x01",
            "or else she might actually escape!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0001FT-True... Let's go after her!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 48)
    BeginChrThread(0x102, 3, 0, 48)
    BeginChrThread(0x103, 3, 0, 48)
    BeginChrThread(0x104, 3, 0, 48)
    Return()

    # Function_32_41C7 end

    def Function_33_5AAE(): pass

    label("Function_33_5AAE")

    BeginChrThread(0x13, 3, 0, 38)
    Sleep(750)
    BeginChrThread(0x12, 3, 0, 37)
    Sleep(4000)
    BeginChrThread(0xD, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0x10, 3, 0, 39)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 40)
    Sleep(1500)
    BeginChrThread(0xE, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xF, 3, 0, 42)
    Sleep(1500)
    BeginChrThread(0xC, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xB, 3, 0, 43)
    Sleep(2500)
    OP_6F(0x10)
    Fade(500)
    OP_68(2130, 1200, 2100, 0)
    MoveCamera(317, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19910, 0)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0xB, 3)

    ChrTalk(
        0x101,
        (
            "#1P#0001FExcuse me, miss. Do you\x01",
            "have a moment?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5BB4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5BB4)
    BeginChrThread(0x101, 3, 0, 44)
    BeginChrThread(0x102, 3, 0, 45)
    BeginChrThread(0x103, 3, 0, 46)
    BeginChrThread(0x104, 3, 0, 47)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    ChrTalk(
        0xB,
        "#5P#3405FHmm? Is there something I can help you with?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FWe apologize for not having told\x01",
            "you this sooner, but...\x02\x03",
            "...we're with the Crossbell police,\x01",
            "Special Support Section.\x02\x03",
            "We'd like you to answer\x01",
            "a few of our questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FI see. I am fully aware of the subject\x01",
            "matter you wish to discuss.\x02\x03",
            "I overheard you speaking on the bus.\x01",
            "You're looking for a counterfeit dealer,\x01",
            "if I'm not mistaken.\x02\x03",
            "#3400FAm I considered a suspect in your investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FU-Uh...\x02\x03",
            "(O-Oh, she overheard us?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FYou're perceptive, at the very least.\x02\x03",
            "I would imagine my ambiguous manner\x01",
            "of speaking aroused suspicion during our\x01",
            "conversation.\x02\x03",
            "#3401FHowever, I regret to inform you that you've\x01",
            "missed an important, yet simple detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FWhat important detail are you referring to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FI paid close attention to your interrogations,\x01",
            "and I noticed a rather...peculiar detail from\x01",
            "one of the passengers.\x02\x03",
            "#3401FI am, of course, referring to your conversation\x01",
            "with the 'sweet' elderly lady.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#0105FYou mean the one that hasn't seen\x01",
            "her grandson in three years?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FI'm not sure I follow you... What was\x01",
            "the issue with their story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FTry to recall the details of your conversation.\x02\x03",
            "She claimed that she had last visited\x01",
            "Crossbell three years ago...\x02\x03",
            "Furthermore, she stated that she had gone\x01",
            "to that theme park with her grandson.\x02\x03",
            "#3402FAny Crossbellan would be able to point out\x01",
            "the contradiction in those two statements\x01",
            "with ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FOh! I get it now!\x02\x03",
            "If she'd truly visited Mishelam Wonderland\x01",
            "three years ago like she claimed she did...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200F...such a theme park would not have\x01",
            "existed.\x02\x03",
            "Therefore, she claims to have visited\x01",
            "a non-existent location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0301FSo...we goin' all in on the granny now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106FI can't believe we let something so\x01",
            "obvious fly right over our heads...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3400FShe managed to successfully deceive\x01",
            "the lot of you with her 'sweet' elderly\x01",
            "lady persona, did she not?\x02\x03",
            "Her contradiction would only be possible had\x01",
            "she been to Crossbell more recently than that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FSo she only recently started visiting Crossbell\x01",
            "for her business...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_64C1():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64C1)

    def lambda_64CE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_64CE)

    def lambda_64DB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_64DB)

    def lambda_64E8():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_64E8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#6P#0005FG-Guys! Anybody know where she is?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI would assume she is on East Street\x01",
            "by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FWe'd better hurry the hell up, or she'll\x01",
            "be home free!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0101FWe have to do something, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0001FYeah, I know!\x02",
    )

    CloseMessageWindow()

    def lambda_6604():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6604)

    def lambda_6611():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6611)

    def lambda_661E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_661E)

    def lambda_662B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_662B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#6P#0006FW-We're really sorry for suspecting you,\x01",
            "ma'am! Thank you so much for your help!\x02\x03",
            "#0001FAs much as I'd love to give you a more\x01",
            "appropriate apology, we don't exactly\x01",
            "have the time for that right now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FRest assured, I do not mind.\x02\x03",
            "You have far more pressing concerns than\x01",
            "a mere apology, do you not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FYeah, you're right!\x02\x03",
            "#0001FLet's go catch us a counterfeit dealer!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 3000)

    def lambda_67E8():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_67E8)
    BeginChrThread(0x101, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 3, 0, 49)
    BeginChrThread(0x104, 3, 0, 49)
    Return()

    # Function_33_5AAE end

    def Function_34_6809(): pass

    label("Function_34_6809")

    BeginChrThread(0x13, 3, 0, 38)
    Sleep(750)
    BeginChrThread(0x12, 3, 0, 37)
    Sleep(4000)
    BeginChrThread(0xD, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0x10, 3, 0, 39)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 40)
    Sleep(1500)
    BeginChrThread(0xF, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xC, 3, 0, 42)
    Sleep(1500)
    BeginChrThread(0xB, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xE, 3, 0, 43)
    Sleep(2500)
    OP_6F(0x10)
    Fade(500)
    OP_68(2130, 1200, 2100, 0)
    MoveCamera(317, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19910, 0)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0xE, 3)

    ChrTalk(
        0x101,
        (
            "#1P#0001FExcuse me, sir. Could you spare\x01",
            "a moment of your time?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_691F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_691F)
    BeginChrThread(0x101, 3, 0, 44)
    BeginChrThread(0x102, 3, 0, 45)
    BeginChrThread(0x103, 3, 0, 46)
    BeginChrThread(0x104, 3, 0, 47)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    ChrTalk(
        0xE,
        (
            "#5POh, I remember you all from\x01",
            "Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PIs there something I can help you with?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0001FWe apologize for not having told\x01",
            "you this sooner, but...\x02\x03",
            "...we're with the Crossbell police,\x01",
            "Special Support Section.\x02\x03",
            "We have a few questions\x01",
            "we need to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PTh-The police?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PHave I committed a crime?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FNot necessarily, but you are a prime\x01",
            "suspect in our ongoing investigation.\x02\x03",
            "#0001FTo start things off--\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-50, 20, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xB,
        "#1PThat'll be far enough.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#0005FHuh?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -10500, 0, 2200, 90)

    def lambda_6B83():
        OP_95(0xFE, -800, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6B83)

    def lambda_6B9D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6B9D)
    WaitChrThread(0xE, 1)
    Sleep(3800)

    def lambda_6BB1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6BB1)

    def lambda_6BBE():
        OP_98(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_6BBE)
    WaitChrThread(0xB, 1)

    ChrTalk(
        0x101,
        "#6P#0005FW-Wait... I recognize you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FWhoa! The black-haired babe?!\x01",
            "Thought you already went into town, miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3404FThat was my intention, yes.\x02\x03",
            "#3400FHowever, given that you are interrogating\x01",
            "an innocent man, I had to return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0205FInnocent? How?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3401FAllow me to explain.\x02\x03",
            "I overheard you speaking on the bus.\x01",
            "You're looking for a counterfeit dealer,\x01",
            "if I'm not mistaken.\x02\x03",
            "#3403FThis man is not your culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FHuh?\x02\x03",
            "Hold on! How do you figure?!\x02\x03",
            "(Wait... She overheard us?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FYou're perceptive, at the very least.\x02\x03",
            "His occupation biased you into thinking\x01",
            "he was your prime suspect.\x02\x03",
            "#3401FHowever, I regret to inform you that you've\x01",
            "missed an important, yet simple detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FWhat important detail are you referring to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FI paid close attention to your interrogations,\x01",
            "and I noticed a rather...peculiar detail from\x01",
            "one of the passengers.\x02\x03",
            "#3401FI am, of course, referring to your conversation\x01",
            "with the 'sweet' elderly lady.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#0105FYou mean the one that hasn't seen\x01",
            "her grandson in three years?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FI'm not sure I follow you... What was\x01",
            "the issue with their story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FTry to recall the details of your conversation.\x02\x03",
            "She claimed that she had last visited\x01",
            "Crossbell three years ago...\x02\x03",
            "Furthermore, she stated that she had gone\x01",
            "to that theme park with her grandson.\x02\x03",
            "#3402FAny Crossbellan would be able to point out\x01",
            "the contradiction in those two statements\x01",
            "with ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FOh! I get it now!\x02\x03",
            "If she'd truly visited Mishelam Wonderland\x01",
            "three years ago like she claimed she did...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200F...such a theme park would have not\x01",
            "existed.\x02\x03",
            "Therefore, she claims to have visited\x01",
            "a non-existent location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0301FSo...we goin' all in on the granny now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106FI can't believe we let something so\x01",
            "obvious fly right over our heads...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3400FShe managed to successfully deceive\x01",
            "the lot of you with her 'sweet' elderly\x01",
            "lady persona, did she not?\x02\x03",
            "Her contradiction would only be possible had\x01",
            "she been to Crossbell more recently than that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FSo she only recently started visiting Crossbell\x01",
            "for her business...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_74A0():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_74A0)

    def lambda_74AD():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_74AD)

    def lambda_74BA():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_74BA)

    def lambda_74C7():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_74C7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#6P#0005FG-Guys! Anybody know where she is?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI would assume she is on East Street\x01",
            "by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FWe'd better hurry the hell up, or she'll\x01",
            "be home free!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0101FWe have to do something, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0001FYeah, I know!\x02",
    )

    CloseMessageWindow()

    def lambda_75E3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75E3)

    def lambda_75F0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_75F0)

    def lambda_75FD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_75FD)

    def lambda_760A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_760A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#6P#0006FWe've made a terrible mistake, sir!\x01",
            "We apologize for suspecting you!\x02\x03",
            "As much as I'd love to give you a more\x01",
            "appropriate apology, we don't exactly\x01",
            "have the time for that right now!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_76EA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_76EA)
    WaitChrThread(0xE, 1)

    ChrTalk(
        0xE,
        (
            "#5PU-Uh...sure? I don't really get\x01",
            "what's going on, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FYou have far more pressing concerns than\x01",
            "a mere apology, do you not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FYeah, you're right!\x02\x03",
            "#0001FLet's go catch us a counterfeit dealer!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 3000)

    def lambda_77E9():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_77E9)

    def lambda_77F6():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_77F6)
    BeginChrThread(0x101, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 3, 0, 49)
    BeginChrThread(0x104, 3, 0, 49)
    Return()

    # Function_34_6809 end

    def Function_35_7817(): pass

    label("Function_35_7817")

    BeginChrThread(0x13, 3, 0, 38)
    Sleep(750)
    BeginChrThread(0x12, 3, 0, 37)
    Sleep(4000)
    BeginChrThread(0xD, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0x10, 3, 0, 39)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 40)
    Sleep(1500)
    BeginChrThread(0xE, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xC, 3, 0, 42)
    Sleep(1500)
    BeginChrThread(0xB, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xF, 3, 0, 43)
    Sleep(2500)
    OP_6F(0x10)
    Fade(500)
    OP_68(2130, 1200, 2100, 0)
    MoveCamera(317, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19910, 0)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0xF, 3)

    ChrTalk(
        0x101,
        (
            "#1P#0001FExcuse me, ma'am. Could we\x01",
            "borrow a moment of your time?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_792F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_792F)
    BeginChrThread(0x101, 3, 0, 44)
    BeginChrThread(0x102, 3, 0, 45)
    BeginChrThread(0x103, 3, 0, 46)
    BeginChrThread(0x104, 3, 0, 47)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    ChrTalk(
        0xF,
        "#5POh, sure. I remember you from earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5PHow can I help you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0001FWe apologize for not having told\x01",
            "you this sooner, but...\x02\x03",
            "...we're with the Crossbell police,\x01",
            "Special Support Section.\x02\x03",
            "There's a few questions we\x01",
            "need to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5PCome again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PWhat are you accusing me of?!\x01",
            "Who do you think you are?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FI'm a detective, but you haven't been\x01",
            "charged with anything...yet. You're a\x01",
            "suspect in our ongoing investigation.\x02\x03",
            "#0001FTo start things off--\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-50, 20, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xB,
        "#1PThat'll be far enough.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#0005FHuh?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -10500, 0, 2200, 90)

    def lambda_7BBE():
        OP_95(0xFE, -800, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7BBE)

    def lambda_7BD8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7BD8)
    WaitChrThread(0xF, 1)
    Sleep(3800)

    def lambda_7BEC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7BEC)

    def lambda_7BF9():
        OP_98(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_7BF9)
    WaitChrThread(0xB, 1)

    ChrTalk(
        0x101,
        "#6P#0005FW-Wait... I recognize you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FWhoa! The black-haired babe?!\x01",
            "Thought you already went into town, miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3404FThat was my intention, yes.\x02\x03",
            "#3400FHowever, given that you are interrogating\x01",
            "an innocent lady, I had to return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0205FInnocent? How?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3401FAllow me to explain.\x02\x03",
            "I overheard you speaking on the bus.\x01",
            "You're looking for a counterfeit dealer,\x01",
            "if I'm not mistaken.\x02\x03",
            "#3403FThis woman is not your culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FHuh?\x02\x03",
            "Hold on! How do you figure?!\x02\x03",
            "(Wait... She overheard us?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FYou had your heart in the right place, at least.\x02\x03",
            "You must have thought she was trying to\x01",
            "divert attention from herself by labeling\x01",
            "me as suspicious, correct?\x02\x03",
            "#3401FHowever, I regret to inform you that you've\x01",
            "missed an important, yet simple detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FWhat are you referring to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FI paid close attention to your interrogations,\x01",
            "and I noticed a rather...peculiar detail from\x01",
            "one of the passengers.\x02\x03",
            "#3401FI am, of course, referring to your conversation\x01",
            "with the 'sweet' elderly lady.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#0105FYou mean the one that hasn't seen\x01",
            "her grandson in three years?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FI'm not sure I follow you... What was\x01",
            "the issue with their story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FTry to recall the details of your conversation.\x02\x03",
            "She claimed that she had last visited\x01",
            "Crossbell three years ago...\x02\x03",
            "Furthermore, she stated that she had gone\x01",
            "to that theme park with her grandson.\x02\x03",
            "#3402FAny Crossbellan would be able to point out\x01",
            "the contradiction in those two statements\x01",
            "with ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FOh! I get it now!\x02\x03",
            "If she'd truly visited Mishelam Wonderland\x01",
            "three years ago like she claimed she did...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200F...such a theme park would have not\x01",
            "existed.\x02\x03",
            "Therefore, she claims to have visited\x01",
            "a non-existent location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0301FSo...we goin' all in on the granny now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106FI can't believe we let something so\x01",
            "obvious fly right over our heads...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3400FShe managed to successfully deceive\x01",
            "the lot of you with her 'sweet' elderly\x01",
            "lady persona, did she not?\x02\x03",
            "Her contradiction would only be possible had\x01",
            "she been to Crossbell more recently than that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FSo she only recently started visiting Crossbell\x01",
            "for her business...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8502():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8502)

    def lambda_850F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_850F)

    def lambda_851C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_851C)

    def lambda_8529():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8529)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#6P#0005FG-Guys! Anybody know where she is?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI would assume she is on East Street\x01",
            "by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FWe'd better hurry the hell up, or she'll\x01",
            "be home free!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0101FWe have to do something, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0001FYeah, I know!\x02",
    )

    CloseMessageWindow()

    def lambda_8645():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8645)

    def lambda_8652():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8652)

    def lambda_865F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_865F)

    def lambda_866C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_866C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#6P#0006FWe've made a terrible mistake, ma'am!\x01",
            "We apologize for suspecting you!\x02\x03",
            "As much as I'd love to give you a more\x01",
            "appropriate apology, we don't exactly\x01",
            "have the time for that right now!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_874E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_874E)
    WaitChrThread(0xF, 1)

    ChrTalk(
        0xF,
        "#5PMy goodness! You people are so rude!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FYou have far more pressing concerns than\x01",
            "a mere apology, do you not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FYeah, you're right!\x02\x03",
            "#0001FLet's go catch us a counterfeit dealer!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 3000)

    def lambda_8839():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8839)

    def lambda_8846():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8846)
    BeginChrThread(0x101, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 3, 0, 49)
    BeginChrThread(0x104, 3, 0, 49)
    Return()

    # Function_35_7817 end

    def Function_36_8867(): pass

    label("Function_36_8867")

    BeginChrThread(0x13, 3, 0, 38)
    Sleep(750)
    BeginChrThread(0x12, 3, 0, 37)
    Sleep(4000)
    BeginChrThread(0xF, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0x10, 3, 0, 39)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 40)
    Sleep(1500)
    BeginChrThread(0xE, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xC, 3, 0, 42)
    Sleep(1500)
    BeginChrThread(0xB, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xD, 3, 0, 43)
    Sleep(2500)
    OP_6F(0x10)
    Fade(500)
    OP_68(2130, 1200, 2100, 0)
    MoveCamera(317, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19910, 0)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0xD, 3)

    ChrTalk(
        0x101,
        (
            "#1P#0001FJust a minute, sir. I need to\x01",
            "talk to you for a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_897B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_897B)
    BeginChrThread(0x101, 3, 0, 44)
    BeginChrThread(0x102, 3, 0, 45)
    BeginChrThread(0x103, 3, 0, 46)
    BeginChrThread(0x104, 3, 0, 47)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    ChrTalk(
        0xD,
        "#5PWhat do YOU want?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PGoing to bother a defenseless\x01",
            "old man again?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0001FWe apologize for not having told\x01",
            "you this sooner, but...\x02\x03",
            "...we're with the Crossbell police,\x01",
            "Special Support Section.\x02\x03",
            "There's a few questions we need\x01",
            "to ask you, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PYou need to do WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PTh-There it is again! This has to\x01",
            "be some kind of cruel joke!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FIt isn't, and we have reason to suspect\x01",
            "you in our ongoing investigation.\x02\x03",
            "#0001FTo start things off--\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-50, 20, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xB,
        "#1PThat'll be far enough.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#0005FHuh?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -10500, 0, 2200, 90)

    def lambda_8BFB():
        OP_95(0xFE, -800, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8BFB)

    def lambda_8C15():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8C15)
    WaitChrThread(0xD, 1)
    Sleep(3800)

    def lambda_8C29():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8C29)

    def lambda_8C36():
        OP_98(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_8C36)
    WaitChrThread(0xB, 1)

    ChrTalk(
        0x101,
        "#6P#0005FW-Wait... I recognize you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FWhoa! The black-haired babe?!\x01",
            "Thought you already went into town, miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3404FThat was my intention, yes.\x02\x03",
            "#3400FHowever, given that you are interrogating\x01",
            "an innocent man, I had to return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0205FInnocent? How?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3401FAllow me to explain.\x02\x03",
            "I overheard you speaking on the bus.\x01",
            "You're looking for a counterfeit dealer,\x01",
            "if I'm not mistaken.\x02\x03",
            "#3403FThis man is not your culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FHuh?\x02\x03",
            "Hold on! How do you figure?!\x02\x03",
            "(Wait... She overheard us?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FYou're perceptive, at the very least.\x02\x03",
            "His refusal to speak with anybody has\x01",
            "deemed him to be suspicious, correct?\x02\x03",
            "#3401FHowever, I regret to inform you that you've\x01",
            "missed an important, yet simple detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FWhat important detail are you referring to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FI paid close attention to your interrogations,\x01",
            "and I noticed a rather...peculiar detail from\x01",
            "one of the passengers.\x02\x03",
            "#3401FI am, of course, referring to your conversation\x01",
            "with the 'sweet' elderly lady.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#0105FYou mean the one that hasn't seen\x01",
            "her grandson in three years?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FI'm not sure I follow you... What was\x01",
            "the issue with their story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FTry to recall the details of your conversation.\x02\x03",
            "She claimed that she had last visited\x01",
            "Crossbell three years ago...\x02\x03",
            "Furthermore, she stated that she had gone\x01",
            "to that theme park with her grandson.\x02\x03",
            "#3402FAny Crossbellan would be able to point out\x01",
            "the contradiction in those two statements\x01",
            "with ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FOh! I get it now!\x02\x03",
            "If she'd truly visited Mishelam Wonderland\x01",
            "three years ago like she claimed she did...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200F...such a theme park would have not\x01",
            "existed.\x02\x03",
            "Therefore, she claims to have visited\x01",
            "a non-existent location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0301FSo...we goin' all in on the granny now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106FI can't believe we let something so\x01",
            "obvious fly right over our heads...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3400FShe managed to successfully deceive\x01",
            "the lot of you with her 'sweet' elderly\x01",
            "lady persona, did she not?\x02\x03",
            "Her contradiction would only be possible had\x01",
            "she been to Crossbell more recently than that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FSo she only recently started visiting Crossbell\x01",
            "for her business...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9521():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9521)

    def lambda_952E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_952E)

    def lambda_953B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_953B)

    def lambda_9548():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9548)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#6P#0005FG-Guys! Anybody know where she is?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI would assume she is on East Street\x01",
            "by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FWe'd better hurry the hell up, or she'll\x01",
            "be home free!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0101FWe have to do something, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0001FYeah, I know!\x02",
    )

    CloseMessageWindow()

    def lambda_9664():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9664)

    def lambda_9671():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9671)

    def lambda_967E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_967E)

    def lambda_968B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_968B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#6P#0006FWe've made a terrible mistake, sir!\x01",
            "We apologize for suspecting you!\x02\x03",
            "As much as I'd love to give you a more\x01",
            "appropriate apology, we don't exactly\x01",
            "have the time for that right now!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_976B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_976B)
    WaitChrThread(0xD, 1)

    ChrTalk(
        0xD,
        "Don't think you'll get off so easily, sonny!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3403FYou have far more pressing concerns than\x01",
            "a mere apology, do you not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FYeah, you're right!\x02\x03",
            "#0001FLet's go catch us a counterfeit dealer!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 3000)

    def lambda_985B():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_985B)

    def lambda_9868():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_9868)
    BeginChrThread(0x101, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 3, 0, 49)
    BeginChrThread(0x104, 3, 0, 49)
    Return()

    # Function_36_8867 end

    def Function_37_9889(): pass

    label("Function_37_9889")

    Sleep(1200)

    def lambda_9891():
        OP_95(0xFE, 16000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9891)

    def lambda_98AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_98AB)
    WaitChrThread(0xFE, 1)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    def lambda_98D5():
        OP_95(0xFE, -12000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_98D5)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_37_9889 end

    def Function_38_98F8(): pass

    label("Function_38_98F8")


    def lambda_98FD():
        OP_95(0xFE, 16000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_98FD)

    def lambda_9917():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9917)
    WaitChrThread(0xFE, 1)

    def lambda_992C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_992C)
    WaitChrThread(0xFE, 1)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2250)

    def lambda_9952():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9952)
    WaitChrThread(0xFE, 1)

    def lambda_9963():
        OP_95(0xFE, -12000, 0, 2700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9963)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_38_98F8 end

    def Function_39_9986(): pass

    label("Function_39_9986")


    def lambda_998B():
        OP_95(0xFE, 16000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_998B)

    def lambda_99A5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_99A5)
    WaitChrThread(0xFE, 1)

    def lambda_99BA():
        OP_95(0xFE, -12000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_99BA)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_39_9986 end

    def Function_40_9A1C(): pass

    label("Function_40_9A1C")


    def lambda_9A21():
        OP_95(0xFE, 16000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A21)

    def lambda_9A3B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9A3B)
    WaitChrThread(0xFE, 1)

    def lambda_9A50():
        OP_95(0xFE, -12000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A50)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_40_9A1C end

    def Function_41_9AB2(): pass

    label("Function_41_9AB2")


    def lambda_9AB7():
        OP_95(0xFE, 16000, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9AB7)

    def lambda_9AD1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9AD1)
    WaitChrThread(0xFE, 1)

    def lambda_9AE6():
        OP_95(0xFE, -12000, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9AE6)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_41_9AB2 end

    def Function_42_9B09(): pass

    label("Function_42_9B09")


    def lambda_9B0E():
        OP_95(0xFE, 16000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9B0E)

    def lambda_9B28():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9B28)
    WaitChrThread(0xFE, 1)

    def lambda_9B3D():
        OP_95(0xFE, -12000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9B3D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_42_9B09 end

    def Function_43_9B60(): pass

    label("Function_43_9B60")


    def lambda_9B65():
        OP_95(0xFE, 16000, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9B65)

    def lambda_9B7F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9B7F)
    WaitChrThread(0xFE, 1)

    def lambda_9B94():
        OP_95(0xFE, 0, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9B94)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_43_9B60 end

    def Function_44_9BB2(): pass

    label("Function_44_9BB2")


    def lambda_9BB7():
        OP_95(0xFE, 3000, 0, 1350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9BB7)
    WaitChrThread(0x101, 1)
    Return()

    # Function_44_9BB2 end

    def Function_45_9BD1(): pass

    label("Function_45_9BD1")


    def lambda_9BD6():
        OP_95(0xFE, 3000, 0, 2950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9BD6)
    WaitChrThread(0x102, 1)
    Return()

    # Function_45_9BD1 end

    def Function_46_9BF0(): pass

    label("Function_46_9BF0")


    def lambda_9BF5():
        OP_95(0xFE, 4500, 0, 1350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9BF5)
    WaitChrThread(0x103, 1)
    Return()

    # Function_46_9BF0 end

    def Function_47_9C0F(): pass

    label("Function_47_9C0F")


    def lambda_9C14():
        OP_95(0xFE, 4500, 0, 2950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9C14)
    WaitChrThread(0x104, 1)
    Return()

    # Function_47_9C0F end

    def Function_48_9C2E(): pass

    label("Function_48_9C2E")


    def lambda_9C33():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C33)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_48_9C2E end

    def Function_49_9C4D(): pass

    label("Function_49_9C4D")

    OP_93(0xFE, 0xB4, 0x0)

    def lambda_9C59():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF8F8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C59)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x0)

    def lambda_9C7E():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C7E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_49_9C4D end

    def Function_50_9C98(): pass

    label("Function_50_9C98")


    def lambda_9C9D():
        OP_95(0xFE, -10000, 0, 3000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C9D)

    def lambda_9CB7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9CB7)
    Return()

    # Function_50_9C98 end

    def Function_51_9CC0(): pass

    label("Function_51_9CC0")

    EventBegin(0x0)
    Fade(500)
    OP_68(133180, 4800, 81440, 0)
    MoveCamera(8, 31, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(17670, 0)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrPos(0x101, 133170, 3000, 82030, 90)
    SetChrPos(0x102, 133230, 3000, 83640, 135)
    SetChrPos(0x103, 132220, 3000, 81240, 45)
    SetChrPos(0x104, 131880, 3000, 83280, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D6B")
    SetChrPos(0x10A, 131150, 3000, 81780, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_9D6B")

    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x34B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x34B, 1)

    ChrTalk(
        0x101,
        (
            "#12P#0000FOh, these white ones are Fainel Flowers,\x01",
            "aren't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#11P#0100FThis location is fairly close to Crossbell City,\x01",
            "so I'd imagine people frequently come by\x01",
            "here to pick them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0300FYeah. Doubt any strong monsters are\x01",
            "chillin' at a place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#06P#0200FRegardless, weaker monsters are still\x01",
            "a threat to children and the elderly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9FF1")

    ChrTalk(
        0x101,
        "#12P#0003FTrue enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#0603FIf you've picked your bloody flower, then let's\x01",
            "get moving already. We don't have the privilege\x01",
            "of standing around doing nothing right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A02F")

    label("loc_9FF1")


    ChrTalk(
        0x101,
        (
            "#12P#0003FYeah, you're right.\x02\x03",
            "#0000FShall we get going?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A02F")

    OP_65(0x5, 0x1)
    OP_29(0x2E, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A05C")
    OP_29(0x2E, 0x1, 0x6)

    label("loc_A05C")

    ClearMapFlags(0x8000000)
    OP_37()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A07C")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_A07C")

    SetChrPos(0x0, 133170, 3000, 82030, 90)
    EventEnd(0x5)
    Return()

    # Function_51_9CC0 end

    def Function_52_A090(): pass

    label("Function_52_A090")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "West: Crossbell City\x01",
            "East: Armorica Village - 274 selge\x01",
            "       Tangram Gate - 206 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_52_A090 end

    SaveToFile()

Try(main)
