from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1460.bin",                # FileName
        "c1460",                    # MapName
        "c1460",                    # Location
        0x0034,                     # MapIndex
        "ed7302",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 52, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1460",                  # 0
        "Wald",                   # 1
        "Elie",                   # 2
        "Tio",                    # 3
        "Monster",                # 4
        "Monster",                # 5
        "Monster",                # 6
        "Monster",                # 7
        "Monster",                # 8
        "Geralm Rat",             # 9
        "bc1470",                 # 10
        "bc1470",                 # 11
        "bc1460",                 # 12
        "bc1460",                 # 13
        "bc1470",                 # 14
        "bc1460",                 # 15
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_B4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_CC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_D0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_D4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_D8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_DC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_E0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_E4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_E8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_EC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 5, 5, 45)

    # monster count: 9

    BattleInfo(
        "BattleInfo_F4", 0x0400, 14, 6, 45, 10, 1, 40, 0, "bc1460", 0x00000000, 100, 0, 0, 0,
        (
            ("ms69001.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_138", 0x0400, 14, 6, 45, 10, 1, 30, 0, "bc1460", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62001.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_17C", 0x0400, 14, 6, 45, 10, 1, 40, 0, "bc1470", 0x00000000, 100, 0, 0, 0,
        (
            ("ms69001.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1C0", 0x0400, 14, 6, 45, 10, 1, 30, 0, "bc1470", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62001.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_204", 0x0000, 14, 6, 45, 0, 1, 0, 0, "bc1470", 0x00000000, 100, 0, 0, 0,
        (
            ("ms69001.dat", "ms69001.dat", "ms69001.dat", "ms69001.dat", 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_248", 0x0012, 15, 6, 45, 0, 1, 0, 0, "bc1460", 0x00000000, 100, 0, 0, 0,
        (
            ("ms64900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7401", "ed7403", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00200.itc",                   # 01
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
        "monster/ch64950.itc",               # 14
        "monster/ch64951.itc",               # 15
        "monster/ch75950.itc",               # 16
    ))

    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(1750,    0,       1500,    270,  389,  0x0, 0,   0,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(1750,    0,       3000,    315,  389,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-100000, 800,     211000,  0,    389,  0x0, 0,   20,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-102519, 0,       212080,  45,   389,  0x0, 0,   22,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-97589,  0,       212080,  315,  389,  0x0, 0,   22,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-101849, 29,      209210,  0,    389,  0x0, 0,   22,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-98279,  29,      209210,  0,    389,  0x0, 0,   22,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-84000,  4000,    156000,  0,    484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(6980,    54510,   30,      0x1010000,    "BattleInfo_F4", 887, 16,  0xFFFF, 0,  1)
    DeclMonster(55560,   6870,    30,      0x1010000,    "BattleInfo_138", 888, 18,  0xFFFF, 2,  3)
    DeclMonster(-117250, -610,    0,       0x1010000,    "BattleInfo_17C", 889, 16,  0xFFFF, 0,  1)
    DeclMonster(-104370, 56030,   30,      0x1010000,    "BattleInfo_1C0", 890, 18,  0xFFFF, 2,  3)
    DeclMonster(-107980, -53770,  30,      0x1010000,    "BattleInfo_F4", 891, 16,  0xFFFF, 0,  1)
    DeclMonster(-96040,  159080,  0,       0x1010000,    "BattleInfo_1C0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-45210,  156150,  30,      0x1010000,    "BattleInfo_F4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-108220, 98340,   0,       0x1010000,    "BattleInfo_F4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-108620, 93580,   0,       0x1010000,    "BattleInfo_138", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 17,  -5.46999979019165,     10.09000015258789,     0.0,                   6.25,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3999999761581421,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   2.734999895095825,     -4.035999774932861,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 20,  -130.0,                0.0,                   0.0,                   16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   65.0,                  -0.0,                  -0.0,                  1.0])
    DeclEvent(0x0000, 0, 21,  -100.0,                162.0,                 3.5,                   6.25,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3999999761581421,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   50.0,                  -64.79999542236328,    -0.6999999284744263,   1.0])

    DeclActor(-110000, 0,       -51000,  1200,    -110000, 1000,    -51000,  0x007C, 0,  7,  0x0000)
    DeclActor(-100000, 0,       161000,  1200,    -100000, 1000,    161000,  0x007C, 0,  8,  0x0000)
    DeclActor(-84000,  3500,    156000,  1200,    -84000,  4500,    156000,  0x007C, 0,  9,  0x0000)
    DeclActor(57000,   0,       -500,    1200,    57000,   1000,    -500,    0x007C, 0,  10, 0x0000)
    DeclActor(-95500,  0,       57000,   1200,    -95500,  1000,    57000,   0x007C, 0,  11, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3

    ScpFunction((
        "Function_0_77C",          # 00, 0
        "Function_1_834",          # 01, 1
        "Function_2_84C",          # 02, 2
        "Function_3_86B",          # 03, 3
        "Function_4_888",          # 04, 4
        "Function_5_9A1",          # 05, 5
        "Function_6_D35",          # 06, 6
        "Function_7_EBE",          # 07, 7
        "Function_8_102D",         # 08, 8
        "Function_9_1188",         # 09, 9
        "Function_10_13DB",        # 0A, 10
        "Function_11_1522",        # 0B, 11
        "Function_12_164C",        # 0C, 12
        "Function_13_1876",        # 0D, 13
        "Function_14_1B3E",        # 0E, 14
        "Function_15_1F1A",        # 0F, 15
        "Function_16_20B1",        # 10, 16
        "Function_17_239F",        # 11, 17
        "Function_18_250C",        # 12, 18
        "Function_19_34D6",        # 13, 19
        "Function_20_34F1",        # 14, 20
        "Function_21_363C",        # 15, 21
        "Function_22_38F4",        # 16, 22
        "Function_23_3BB8",        # 17, 23
        "Function_24_4746",        # 18, 24
        "Function_25_4765",        # 19, 25
        "Function_26_4784",        # 1A, 26
        "Function_27_47A3",        # 1B, 27
        "Function_28_47C2",        # 1C, 28
    ))


    def Function_0_77C(): pass

    label("Function_0_77C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_7BC"),
        (1, "loc_7C8"),
        (2, "loc_7D4"),
        (3, "loc_7E0"),
        (4, "loc_7EC"),
        (5, "loc_7F8"),
        (6, "loc_804"),
        (SWITCH_DEFAULT, "loc_810"),
    )


    label("loc_7BC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_81C")

    label("loc_7C8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_81C")

    label("loc_7D4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_81C")

    label("loc_7E0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_81C")

    label("loc_7EC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_81C")

    label("loc_7F8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_81C")

    label("loc_804")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_81C")

    label("loc_810")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_81C")

    label("loc_81C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_833")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_81C")

    label("loc_833")

    Return()

    # Function_0_77C end

    def Function_1_834(): pass

    label("Function_1_834")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_84B")
    OP_A0(0xFE, 1000, 0x0, 0xFB)
    Jump("Function_1_834")

    label("loc_84B")

    Return()

    # Function_1_834 end

    def Function_2_84C(): pass

    label("Function_2_84C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_86A")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_84C")

    label("loc_86A")

    Return()

    # Function_2_84C end

    def Function_3_86B(): pass

    label("Function_3_86B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_887")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_3_86B")

    label("loc_887")

    Return()

    # Function_3_86B end

    def Function_4_888(): pass

    label("Function_4_888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_896")
    Jump("loc_9A0")

    label("loc_896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8D1")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_9A0")

    label("loc_8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9A0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8EB")
    Jump("loc_91C")

    label("loc_8EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_907")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_91C")

    label("loc_907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91C")
    Event(0, 14)

    label("loc_91C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_95A")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_9A0")

    label("loc_95A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 7)), scpexpr(EXPR_END)), "loc_968")
    SetChrFlags(0x11, 0x80)

    label("loc_968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 0)), scpexpr(EXPR_END)), "loc_976")
    SetChrFlags(0x12, 0x80)

    label("loc_976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 1)), scpexpr(EXPR_END)), "loc_984")
    SetChrFlags(0x13, 0x80)

    label("loc_984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 2)), scpexpr(EXPR_END)), "loc_992")
    SetChrFlags(0x14, 0x80)

    label("loc_992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 3)), scpexpr(EXPR_END)), "loc_9A0")
    SetChrFlags(0x15, 0x80)

    label("loc_9A0")

    Return()

    # Function_4_888 end

    def Function_5_9A1(): pass

    label("Function_5_9A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BA")
    OP_10(0x0, 0x0)
    OP_10(0x19, 0x1)
    Jump("loc_9C0")

    label("loc_9BA")

    OP_10(0x0, 0x1)
    OP_10(0x19, 0x0)

    label("loc_9C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DC")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_9F3")

    label("loc_9DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9F3")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_9F3")

    label("loc_9F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A06")
    OP_70(0x9, 0x0)
    Jump("loc_A0A")

    label("loc_A06")

    OP_70(0x9, 0x1E)

    label("loc_A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1D")
    OP_70(0xA, 0x0)
    Jump("loc_A21")

    label("loc_A1D")

    OP_70(0xA, 0x1E)

    label("loc_A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A34")
    OP_70(0xB, 0x0)
    Jump("loc_A38")

    label("loc_A34")

    OP_70(0xB, 0x1E)

    label("loc_A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4B")
    OP_70(0xC, 0x0)
    Jump("loc_A4F")

    label("loc_A4B")

    OP_70(0xC, 0x1E)

    label("loc_A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A62")
    OP_70(0xD, 0x0)
    Jump("loc_A66")

    label("loc_A62")

    OP_70(0xD, 0x1E)

    label("loc_A66")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_AE1")
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "break", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "all01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x1, 0x2)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x2)
    Jump("loc_B3A")

    label("loc_AE1")

    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "break", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "all11", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA03", 0x1, 0x2)
    SetMapObjFrame(0xFF, "break", 0x1, 0x2)

    label("loc_B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_BB0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAB")
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "break", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "all01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x1, 0x2)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x2)

    label("loc_BAB")

    Jump("loc_D31")

    label("loc_BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_D31")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BCA")
    Jump("loc_D31")

    label("loc_BCA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_C40")
    OP_1B(0x0, 0x0, 0x1C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFA")
    SetScenarioFlags(0x0, 3)
    Event(0, 22)

    label("loc_BFA")

    Jump("loc_C3B")

    label("loc_BFF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C30")
    SetScenarioFlags(0x0, 2)
    OP_E0(0x0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_C30")

    Jump("loc_C3B")

    label("loc_C35")

    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 2)

    label("loc_C3B")

    Jump("loc_D31")

    label("loc_C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 0)), scpexpr(EXPR_END)), "loc_C91")
    OP_1B(0x0, 0x0, 0x1C)
    ModifyEventFlags(1, 2, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C84")
    SetScenarioFlags(0x0, 2)
    OP_E0(0x0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_C84")

    Jump("loc_C8C")

    label("loc_C89")

    ClearScenarioFlags(0x0, 2)

    label("loc_C8C")

    Jump("loc_D31")

    label("loc_C91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_CAD")
    OP_1B(0x0, 0x0, 0x1C)
    ModifyEventFlags(1, 1, 0x80)
    Jump("loc_D31")

    label("loc_CAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_CC4")
    ModifyEventFlags(1, 0, 0x80)
    Jump("loc_D31")

    label("loc_CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_END)), "loc_D31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D31")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D0E")
    Event(0, 15)
    Jump("loc_D31")

    label("loc_D0E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D31")
    Event(0, 16)

    label("loc_D31")

    Call(0, 6)
    Return()

    # Function_5_9A1 end

    def Function_6_D35(): pass

    label("Function_6_D35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D56")
    SetChrFlags(0x11, 0x8)
    Jump("loc_D5B")

    label("loc_D56")

    ClearChrFlags(0x11, 0x8)

    label("loc_D5B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D82")
    SetChrFlags(0x12, 0x8)
    SetMapObjFlags(0xC, 0x4)
    Jump("loc_D8D")

    label("loc_D82")

    ClearChrFlags(0x12, 0x8)
    ClearMapObjFlags(0xC, 0x4)

    label("loc_D8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC9")
    SetChrFlags(0x13, 0x8)
    Jump("loc_DCE")

    label("loc_DC9")

    ClearChrFlags(0x13, 0x8)

    label("loc_DCE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DEC")
    SetChrFlags(0x14, 0x8)
    SetMapObjFlags(0xD, 0x4)
    Jump("loc_DF7")

    label("loc_DEC")

    ClearChrFlags(0x14, 0x8)
    ClearMapObjFlags(0xD, 0x4)

    label("loc_DF7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E1E")
    SetChrFlags(0x15, 0x8)
    SetMapObjFlags(0x9, 0x4)
    Jump("loc_E29")

    label("loc_E1E")

    ClearChrFlags(0x15, 0x8)
    ClearMapObjFlags(0x9, 0x4)

    label("loc_E29")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E68")
    SetChrFlags(0x16, 0x8)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    Jump("loc_E79")

    label("loc_E68")

    ClearChrFlags(0x16, 0x8)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)

    label("loc_E79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E96")
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x19, 0x8)
    Jump("loc_EA0")

    label("loc_E96")

    ClearChrFlags(0x18, 0x8)
    ClearChrFlags(0x19, 0x8)

    label("loc_EA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB8")
    SetChrFlags(0x17, 0x8)
    Jump("loc_EBD")

    label("loc_EB8")

    ClearChrFlags(0x17, 0x8)

    label("loc_EBD")

    Return()

    # Function_6_D35 end

    def Function_7_EBE(): pass

    label("Function_7_EBE")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA8")
    Sound(14, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x4B, 1)"), scpexpr(EXPR_END)), "loc_F3E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x4B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_FA3")

    label("loc_F3E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x4B),
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

    label("loc_FA3")

    Jump("loc_1021")

    label("loc_FA8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'Hyeh hyeh hyeh!'\x01",
            "(Imelda appears to have left a voice recorder in the chest.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1021")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_EBE end

    def Function_8_102D(): pass

    label("Function_8_102D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1117")
    Sound(14, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x644, 1)"), scpexpr(EXPR_END)), "loc_10AD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x644),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1112")

    label("loc_10AD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x644),
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

    label("loc_1112")

    Jump("loc_117C")

    label("loc_1117")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I wonder how the Grand Chardonnay\x01",
            "I used to have ended up.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_117C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_102D end

    def Function_9_1188(): pass

    label("Function_9_1188")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1347")
    Sound(14, 0, 100, 0)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1287")
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x10, 0x0, 0)
    OP_98(0x10, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_11E1():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_11E1)

    def lambda_11FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_11FB)
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
    Battle("BattleInfo_204", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1268"),
        (2, "loc_1277"),
        (1, "loc_1284"),
        (SWITCH_DEFAULT, "loc_1287"),
    )


    label("loc_1268")

    SetScenarioFlags(0x74, 2)
    OP_70(0xB, 0x1E)
    Sleep(500)
    Jump("loc_1287")

    label("loc_1277")

    OP_70(0xB, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1284")

    OP_B7(0x0)
    Return()

    label("loc_1287")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E1, 1)"), scpexpr(EXPR_END)), "loc_12DF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5E1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1342")

    label("loc_12DF")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5E1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xB, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1342")

    Jump("loc_13CF")

    label("loc_1347")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You check the chest and find this text box.\x01",
            "It is a very good text box, I assure you.\x01",
            "Very well written.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_13CF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1188 end

    def Function_10_13DB(): pass

    label("Function_10_13DB")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_149D")
    Sound(14, 0, 100, 0)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xC, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x4, 40)
    AddSepith(0x5, 40)
    AddSepith(0x6, 40)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x40\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x40\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x40.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x111, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_1510")

    label("loc_149D")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Let's play hide-and-seek. You hide something valuable\x01",
            "in me, and then go seek therapy for kleptomania.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1510")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_13DB end

    def Function_11_1522(): pass

    label("Function_11_1522")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15FF")
    Sound(14, 0, 100, 0)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xD, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 40)
    AddSepith(0x1, 40)
    AddSepith(0x2, 40)
    AddSepith(0x3, 40)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x40\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x40\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x40\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x40.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x111, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_163A")

    label("loc_15FF")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The chest joins your party! It will wait here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_163A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1522 end

    def Function_12_164C(): pass

    label("Function_12_164C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16E3")

    ChrTalk(
        0x9,
        (
            "#0100FTio and I will manage if any monsters\x01",
            "make their way up here.\x02\x03",
            "Stay safe down there, you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_32(0x0, 0xFC, 0x0)
    OP_32(0x3, 0xFC, 0x0)
    OP_32(0x0, 0xFD, 0x270F)
    OP_32(0x3, 0xFD, 0x270F)
    Sound(8, 0, 100, 0)
    Sleep(800)
    Jump("loc_1872")

    label("loc_16E3")


    ChrTalk(
        0x9,
        (
            "#0100FTio and I will manage if any monsters\x01",
            "make their way up here.\x02\x03",
            "We'll leave the rest to you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309FWe got this in the bag!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0105FOh, wait a moment before you head in.\x01",
            "I have some medicine I can give you.\x02",
        )
    )

    CloseMessageWindow()
    OP_32(0x0, 0xFC, 0x0)
    OP_32(0x3, 0xFC, 0x0)
    OP_32(0x0, 0xFD, 0x270F)
    OP_32(0x3, 0xFD, 0x270F)
    Sound(8, 0, 100, 0)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            "#0100FDon't do anything too crazy while\x01",
            "you're down there, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, for sure. Anyway, I think it's time\x01",
            "we get started.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1872")

    TalkEnd(0xFE)
    Return()

    # Function_12_164C end

    def Function_13_1876(): pass

    label("Function_13_1876")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1901")

    ChrTalk(
        0xA,
        (
            "#0203FI detect the presence of many\x01",
            "monsters awaiting within.\x02\x03",
            "#0200FPlease proceed with caution.\x02",
        )
    )

    CloseMessageWindow()
    OP_32(0x0, 0xF8, 0x270F)
    OP_32(0x3, 0xF8, 0x270F)
    Sound(8, 0, 100, 0)
    Sleep(800)
    Jump("loc_1B3A")

    label("loc_1901")


    ChrTalk(
        0xA,
        (
            "#0200FI detect the presence of many\x01",
            "monsters awaiting within.\x02\x03",
            "Please proceed with caution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FGot it. Thanks. By the way, Tio...\x02\x03",
            "#0000FYou should have told us if anything felt\x01",
            "wrong earlier. You aren't bothering us\x01",
            "by doing so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0200FRight...\x02\x03",
            "#0203FI apologize. I am admittedly lacking\x01",
            "in the confidence department.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio operated the orbal staff.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#0200FOnly residual amounts of orbal energy\x01",
            "remain, but please make good use of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_32(0x0, 0xF8, 0x270F)
    OP_32(0x3, 0xF8, 0x270F)
    Sound(8, 0, 100, 0)
    Sleep(800)

    ChrTalk(
        0x104,
        "#0302FAppreciate it, Tio Tot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWill do, Tio.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1B3A")

    TalkEnd(0xFE)
    Return()

    # Function_13_1876 end

    def Function_14_1B3E(): pass

    label("Function_14_1B3E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1250, 0, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17640, 0)
    SetChrPos(0x101, 500, 0, -2500, 0)
    SetChrPos(0x102, -500, 0, -2750, 0)
    SetChrPos(0x103, 500, 0, -4000, 0)
    SetChrPos(0x104, -500, 0, -4250, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1BED():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BED)
    Sleep(50)

    def lambda_1C0A():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C0A)
    Sleep(50)

    def lambda_1C27():
        OP_97(0x103, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C27)
    Sleep(50)

    def lambda_1C44():
        OP_97(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C44)
    OP_68(0, 1250, 2000, 2000)
    FadeToBright(1000, 0)
    Sleep(200)

    def lambda_1C7B():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C7B)
    Sleep(50)

    def lambda_1C8F():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C8F)
    Sleep(50)

    def lambda_1CA3():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1CA3)
    Sleep(50)

    def lambda_1CB7():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1CB7)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_1CD1():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CD1)
    WaitChrThread(0x103, 1)

    def lambda_1CE2():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CE2)
    WaitChrThread(0x104, 1)

    def lambda_1CF3():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1CF3)

    ChrTalk(
        0x101,
        (
            "#0003FAll right, we made it in. Who knows what\x01",
            "lies ahead, so be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FDude, get a load of all this dust pilin'\x01",
            "up in this huge dump!\x02",
        )
    )

    CloseMessageWindow()
    Sound(837, 0, 100, 0)
    Sleep(1500)
    Sound(838, 0, 100, 0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x102,
        (
            "#0101FI would imagine there is no shortage\x01",
            "of monsters, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0201FIndeed. I sense they have been running\x01",
            "amok in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FTo be fair, we wouldn't have received a request\x01",
            "if this apartment was monster-free.\x02\x03",
            "#0001FStay sharp, everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, 2500, 0)
    OP_29(0xA, 0x1, 0x2)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_14_1B3E end

    def Function_15_1F1A(): pass

    label("Function_15_1F1A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-116040, 1250, 90, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17640, 0)
    SetChrPos(0x101, -115250, 0, -750, 315)
    SetChrPos(0x102, -115500, 0, 750, 225)
    SetChrPos(0x103, -116750, 0, -750, 45)
    SetChrPos(0x104, -117000, 0, 750, 135)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#5P#0101FDid we manage to clear them\x01",
            "all out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FYeah, I think so. I'm pretty sure\x01",
            "we've covered all of the rooms.\x02\x03",
            "#0001FWe can double-check them as\x01",
            "we make our way out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0309FSure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0203FLet us be off.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -115250, 0, 0, 90)
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0xA, 0x1, 0x3)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_15_1F1A end

    def Function_16_20B1(): pass

    label("Function_16_20B1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1250, 9000, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 750, 0, 10000, 225)
    SetChrPos(0x102, -750, 0, 9750, 135)
    SetChrPos(0x103, 750, 0, 8500, 315)
    SetChrPos(0x104, -750, 0, 8250, 45)
    SetChrPos(0x8, 0, 0, -2500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#5P#0101FDid we manage to clear them\x01",
            "all out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FYeah, I think so. I'm pretty sure\x01",
            "we've covered all of the rooms.\x02\x03",
            "#0001FWe can double-check the rooms\x01",
            "as we make our way back out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0309FSure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0203FLet us be off.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Rough Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Hey, ya punks. The hell do you think yer doin'\x01",
            "runnin' around like you own the damn place?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2315():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2315)

    def lambda_2322():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2322)

    def lambda_232F():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_232F)

    def lambda_233C():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_233C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#0005FHuh?\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1250, 0, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_29(0xA, 0x1, 0x3)
    Call(0, 18)
    Return()

    # Function_16_20B1 end

    def Function_17_239F(): pass

    label("Function_17_239F")

    EventBegin(0x1)
    SetChrPos(0x8, 0, 0, -2500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(
        0x8,
        "Rough Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#5PHey, ya punks. The hell do you think yer doin'\x01",
            "runnin' around like you own the damn place?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2488():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2488)

    def lambda_2495():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2495)

    def lambda_24A2():
        OP_93(0x103, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_24A2)

    def lambda_24AF():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_24AF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#0005FHuh?\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1250, 0, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Call(0, 18)
    Return()

    # Function_17_239F end

    def Function_18_250C(): pass

    label("Function_18_250C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02100.itc", 0x1E)
    OP_68(-640, 1250, 810, 0)
    MoveCamera(42, 35, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15760, 0)
    SetChrPos(0x101, 500, 0, 7750, 180)
    SetChrPos(0x104, -500, 0, 8000, 180)
    SetChrPos(0x102, 500, 0, 9500, 180)
    SetChrPos(0x103, -500, 0, 9750, 180)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, -2500, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_68(0, 1250, -500, 1500)

    def lambda_25D9():
        OP_97(0x8, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_25D9)

    def lambda_25F3():
        OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_25F3)
    Sound(103, 0, 100, 0)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)

    ChrTalk(
        0x8,
        (
            "#1601F#12PCare to explain what a bunch of cops\x01",
            "are doin' so close to Ignis' turf?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_2674():
        OP_97(0x101, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2674)
    Sleep(50)

    def lambda_2691():
        OP_97(0x104, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2691)
    Sleep(50)

    def lambda_26AE():
        OP_97(0x102, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_26AE)
    Sleep(50)

    def lambda_26CB():
        OP_97(0x103, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_26CB)
    OP_68(-750, 1650, 1230, 3000)
    MoveCamera(49, 26, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15800, 3000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x104,
        "#5P#0306FOh, pssh. It's just you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FI guess this apartment building is pretty\x01",
            "close to your base, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12P#1604FHaha...\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)

    ChrTalk(
        0x8,
        "#12P#1609F#4SHahahahaha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FWh-What's his deal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#1602FHAHAHA! Look at you guys!\x01",
            "Yer friggin' filthy!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#5P#0200FOh... I failed to take notice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0103FIt's unavoidable when we have to\x01",
            "fight monsters in a dusty den.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#1602FMonsters, eh?\x02\x03",
            "#1603FThey like to make nests outta the\x01",
            "abandoned buildings 'round here.\x01",
            "Nothin' new to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FInfestations like this are common?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0301FYeah? I can see why a pest like you\x01",
            "loves hangin' around here.\x02",
        )
    )

    CloseMessageWindow()
    Sound(837, 0, 100, 0)
    Sleep(1500)
    Sound(838, 0, 100, 0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#12P#1602FHeh. Runnin' your mouth when\x01",
            "you haven't even finished the\x01",
            "job in here yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001FW-Wait, what are you talking about?\x01",
            "We've gone over all of the rooms already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0203FIt just occurred to me...\x02\x03",
            "#0200FThere is a strong chance that monsters\x01",
            "have bred inside of here.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2BFA():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BFA)

    def lambda_2C07():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C07)

    def lambda_2C14():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2C14)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x103,
        (
            "#5P#0200FTruth be told, I have known about their\x01",
            "nest this entire time.\x02\x03",
            "It is a little deeper inside the apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0005FThere's still more?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#1602FYou figurin' that out just now? This is why\x01",
            "you're a bunch of trash-tier cops.\x02\x03",
            "#1600FWhy don'tcha drag yer asses back to the\x01",
            "city and patrol somethin' a lil' safer?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D7F():
        OP_97(0x8, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2D7F)
    BeginChrThread(0x101, 2, 0, 19)
    BeginChrThread(0x104, 2, 0, 19)
    BeginChrThread(0x102, 2, 0, 19)
    BeginChrThread(0x103, 2, 0, 19)
    Sleep(200)

    def lambda_2DB4():
        OP_98(0x101, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DB4)

    def lambda_2DCE():
        OP_98(0x104, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2DCE)
    Sleep(100)

    def lambda_2DEB():
        OP_98(0x102, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2DEB)

    def lambda_2E05():
        OP_98(0x103, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2E05)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x102, 0x2)

    ChrTalk(
        0x102,
        "#12P#0105FWait! Where are you going?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FHold on a minute! Who said you could\x01",
            "go in there all by yourself?!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-2770, 1250, 6170, 0)
    MoveCamera(65, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16430, 0)
    SetChrPos(0x8, -1390, 0, 6440, 315)
    BeginChrThread(0x101, 2, 0, 19)
    BeginChrThread(0x104, 2, 0, 19)
    BeginChrThread(0x102, 2, 0, 19)
    BeginChrThread(0x103, 2, 0, 19)
    OP_95(0x8, -5500, 0, 10000, 2000, 0x0)

    def lambda_2F30():
        OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F30)
    OP_95(0x8, -10000, -2000, 10000, 2000, 0x0)
    WaitChrThread(0x8, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x102, 0x2)
    Sleep(600)
    OP_68(-1280, 1250, 4610, 3000)
    MoveCamera(65, 24, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16430, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        "#12P#0306FGuess he's goin' in to pummel the rest of 'em.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0101FWell, considering his ego, I presume he believes\x01",
            "that he'll be able to neutralize the rest of the\x01",
            "monsters with ease.\x02",
        )
    )

    CloseMessageWindow()
    Sound(837, 0, 100, 0)
    Sound(818, 0, 100, 0)
    Sleep(1000)
    OP_82(0xC8, 0x64, 0x7D0, 0x320)
    Sound(834, 0, 100, 0)
    Sleep(1500)
    Sound(838, 0, 100, 0)
    Sleep(1000)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x104,
        "#12P#0301FYou think he'll be fine on his own?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FHmm... Wald may be freakishly strong, but it's\x01",
            "too dangerous to handle by himself.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(10, 1250, 2660, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16140, 0)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#0001FHey, Elie, Tio. Sorry, but can I leave you\x01",
            "two to watch the entrance?\x02\x03",
            "#0003FHe's, uh, a bit on the louder side, so he might\x01",
            "startle the monsters. I figure they might try to\x01",
            "escape by running through here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_329B():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_329B)

    def lambda_32A8():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_32A8)

    def lambda_32B5():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_32B5)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        "#5P#0100F#5PUnderstood. We'll stay on guard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0200FDo you two plan to go inside to save\x01",
            "Wald from his own ego?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0001FYeah, something like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0306FHopefully, he isn't cryin' for mommy yet.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x104,
        (
            "#6P#0300FShould probably get a move on, Lloyd.\x01",
            "Don't wanna be late to the show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0001FRight!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_68(0, 1000, 2500, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x0, 0, 0, 2500, 0)
    SetChrPos(0x1, 0, 0, 2500, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_E0(0x0)
    ClearScenarioFlags(0x6F, 1)
    ClearChrFlags(0x13, 0x80)
    OP_1B(0x0, 0x0, 0x1C)
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0xA, 0x1, 0x4)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_18_250C end

    def Function_19_34D6(): pass

    label("Function_19_34D6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34F0")
    TurnDirection(0xFE, 0x8, 500)
    Sleep(200)
    Jump("Function_19_34D6")

    label("loc_34F0")

    Return()

    # Function_19_34D6 end

    def Function_20_34F1(): pass

    label("Function_20_34F1")

    EventBegin(0x0)
    Fade(500)
    OP_68(-132910, 1000, 3230, 0)
    MoveCamera(41, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16170, 0)
    SetChrPos(0x101, -132000, 0, 1500, 0)
    SetChrPos(0x104, -133000, 0, 1250, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0005F#12PA wooden crate...? Looks like this thing was\x01",
            "blocking off the rooms leading deeper inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301F#6PWell, it's not in the way anymore, so let's\x01",
            "get goin'!\x02",
        )
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 1, 0x80)
    SetChrPos(0x0, -132500, 0, 1500, 0)
    SetScenarioFlags(0x71, 0)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_20_34F1 end

    def Function_21_363C(): pass

    label("Function_21_363C")

    EventBegin(0x0)
    Fade(500)
    OP_68(-97470, 4500, 165000, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -98740, 3500, 163210, 45)
    SetChrPos(0x104, -99750, 3500, 163400, 45)
    SetChrPos(0x8, -91930, 3500, 169750, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Wald's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SHaaaa!\x02",
        )
    )

    CloseMessageWindow()
    Sound(590, 0, 100, 0)
    Sleep(100)
    Sound(830, 0, 100, 0)
    Sound(819, 0, 100, 0)
    Sleep(1000)
    Sound(532, 0, 100, 0)
    Sleep(200)
    Sound(830, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005F#11PThat sounds like it came from up ahead!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Wald's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SDamn it...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0xC8, 0x64, 0x7D0, 0x4B0)
    Sound(813, 0, 100, 0)
    Sleep(500)
    Sound(830, 0, 100, 0)
    Sound(819, 0, 100, 0)

    NpcTalk(
        0x8,
        "Wald's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SNgh?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#5P#0305FSounds like he's havin' a helluva\x01",
            "time in there, doesn't it?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0001FThis is exactly why I didn't want him\x01",
            "to rush in there alone!\x02\x03",
            "Cover me, Randy!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_64(0x104)

    ChrTalk(
        0x104,
        "#5P#0301FYou got it, bud!\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 2, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x0, -98740, 3500, 163210, 45)
    OP_29(0xA, 0x1, 0x6)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_21_363C end

    def Function_22_38F4(): pass

    label("Function_22_38F4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x15, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch00351.itc", 0x21)
    LoadChrToIndex("chr/ch02153.itc", 0x22)
    OP_68(-100520, 1200, 212080, 0)
    MoveCamera(43, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19760, 0)
    SetChrPos(0x101, -99500, 0, 197250, 0)
    SetChrPos(0x104, -100500, 0, 197000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x116, 0x22)
    SetChrSubChip(0x116, 0x3)
    SetChrPos(0x116, -100000, 0, 213500, 180)
    ClearChrFlags(0x116, 0x80)
    ClearChrBattleFlags(0x116, 0x8000)
    SetChrFlags(0xB, 0x8000)
    BeginChrThread(0xB, 0, 0, 2)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    BeginChrThread(0xC, 0, 0, 3)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    BeginChrThread(0xD, 0, 0, 3)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    BeginChrThread(0xE, 0, 0, 3)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    BeginChrThread(0xF, 0, 0, 3)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    SetCameraDistance(18760, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x116,
        (
            "#5P#1607F*pant* *pant*\x02\x03",
            "Screw you!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-100310, 1000, 209140, 2500)

    def lambda_3A8D():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A8D)

    def lambda_3AA7():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3AA7)
    Sleep(50)

    def lambda_3ABB():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3ABB)

    def lambda_3AD5():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3AD5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(100)
    Sound(808, 0, 100, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#12P#0007FCalm down, Wald!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0307FWe're here to help ya, man!\x02",
    )

    CloseMessageWindow()

    def lambda_3B60():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B60)

    def lambda_3B7A():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3B7A)
    Sleep(200)
    Battle("BattleInfo_248", 0x30200011, 0x0, 0x0, 0x15, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x104, 0x1)
    Call(0, 23)
    Return()

    # Function_22_38F4 end

    def Function_23_3BB8(): pass

    label("Function_23_3BB8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RemoveParty(0x15, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00350.itc", 0x1F)
    LoadChrToIndex("chr/ch02153.itc", 0x20)
    LoadChrToIndex("chr/ch02100.itc", 0x21)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    OP_68(-100740, 1200, 210550, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -99500, 0, 209250, 0)
    SetChrPos(0x104, -100500, 0, 209000, 0)
    SetChrPos(0x102, -99500, 0, 199250, 0)
    SetChrPos(0x103, -100500, 0, 199000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x104, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x104, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x3)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -100000, 0, 213500, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
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
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#0010F*pant* *pant*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0306FWhew. That was actually kinda hard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FYeah. It really shows how much we rely\x01",
            "on Tio and Elie to support us, doesn't it?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(100)
    Sound(808, 0, 100, 0)
    OP_68(-100180, 1200, 212390, 3000)

    def lambda_3DCD():
        OP_97(0x101, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DCD)
    Sleep(50)

    def lambda_3DEA():
        OP_97(0x104, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3DEA)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#12P#0000FBut more importantly, are you okay, Wald?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#1603FHmph...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5P#1601FWhat the hell?! Did I ask you dumbasses\x01",
            "to interrupt my fight?!\x02\x03",
            "#1607FYou think I'm some kinda weakling?!\x01",
            "Huh?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#0006FWe were only trying to help you, so\x01",
            "why are you trying to pick a fight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FWell, not like I was expectin' this jerkwad\x01",
            "to say 'Thanks, kind officer!' anyway.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-101130, 1000, 205900, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21830, 0)
    Sleep(500)
    OP_68(-100390, 1400, 209890, 4000)
    Sound(103, 0, 100, 0)

    def lambda_402E():
        OP_97(0x102, 0x0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_402E)

    def lambda_4048():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4048)
    Sleep(50)

    def lambda_405C():
        OP_97(0x103, 0x0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_405C)

    def lambda_4076():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4076)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x102,
        (
            "#12P#0101FAre you two okay?! We heard some\x01",
            "frightening noises from our post.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        (
            "#5P#0304FYeah, we're good. Did manage to bail a\x01",
            "certain goon out of a tight spot, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#1607F'Scuse me, Red? You askin' to get\x01",
            "your skull cracked open?\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0x103, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_93(0x103, 0x2D, 0x2EE)
    Sleep(500)
    OP_93(0x103, 0x13B, 0x2EE)
    Sleep(500)
    OP_93(0x103, 0xD7, 0x2EE)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#6P#0203FOne moment, please...\x02\x03",
            "#0200FI no longer detect the presence\x01",
            "of any monsters.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x101, 1, 0, 24)
    BeginChrThread(0x102, 1, 0, 25)
    BeginChrThread(0x104, 1, 0, 26)
    BeginChrThread(0x8, 1, 0, 27)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x101,
        "#11P#0005FOh, good. What a relief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0304FOh, yeah. Does seem a lot more quiet, doesn't it?\x02\x03",
            "#0300FProbably 'cause we took out the head honcho\x01",
            "of this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#1603FHah. How pathetic. So this is\x01",
            "how it all ends, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0x8, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    OP_68(-100920, 1500, 208170, 3000)
    BeginChrThread(0x101, 1, 0, 19)

    ChrTalk(
        0x101,
        "#5P#0005FWhat do you mean, Wald?\x02",
    )

    OP_97(0x8, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
    EndChrThread(0x101, 0x1)
    CloseMessageWindow()

    def lambda_43F1():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43F1)

    def lambda_43FE():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_43FE)

    def lambda_440B():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_440B)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x8,
        (
            "#12P#1601FYa punks managed to ruin my fun.\x01",
            "Gonna head back to the base and have\x01",
            "a date with a bottle of booze.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "#12P#1601FAnd you punks better not think you can run\x01",
            "around the Downtown District doing whatever\x01",
            "you damn well please.\x02\x03",
            "#1607FThis is our turf, so if you've done yer job,\x01",
            "then get the HELL outta here!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_456D():
        OP_93(0x101, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_456D)

    def lambda_457A():
        OP_93(0x102, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_457A)

    def lambda_4587():
        OP_93(0x103, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4587)

    def lambda_4594():
        OP_93(0x104, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4594)
    OP_97(0x8, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        (
            "#5P#0104F*sigh* He needs to find a better coping\x01",
            "mechanism to hide his embarrassment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0306FMan. That dude's never going to change, is he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FIt's not really our problem, to be honest.\x02\x03",
            "#0000FAnyway, I think we've managed to clear out\x01",
            "the monsters, so let's head back to Imelda\x01",
            "and give her the good news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FLet us be off.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0580", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_3BB8 end

    def Function_24_4746(): pass

    label("Function_24_4746")

    OP_93(0x101, 0x87, 0x2EE)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x2EE)
    Sleep(500)
    OP_93(0x101, 0x2D, 0x2EE)
    Sleep(500)
    Return()

    # Function_24_4746 end

    def Function_25_4765(): pass

    label("Function_25_4765")

    OP_93(0x102, 0xB4, 0x2EE)
    Sleep(500)
    OP_93(0x102, 0x2D, 0x2EE)
    Sleep(500)
    OP_93(0x102, 0x13B, 0x2EE)
    Sleep(500)
    Return()

    # Function_25_4765 end

    def Function_26_4784(): pass

    label("Function_26_4784")

    OP_93(0x104, 0x10E, 0x2EE)
    Sleep(500)
    OP_93(0x104, 0x13B, 0x2EE)
    Sleep(500)
    OP_93(0x104, 0x0, 0x2EE)
    Sleep(500)
    Return()

    # Function_26_4784 end

    def Function_27_47A3(): pass

    label("Function_27_47A3")

    OP_93(0x8, 0xE1, 0x2EE)
    Sleep(500)
    OP_93(0x8, 0x87, 0x2EE)
    Sleep(500)
    OP_93(0x8, 0xB4, 0x2EE)
    Sleep(500)
    Return()

    # Function_27_47A3 end

    def Function_28_47C2(): pass

    label("Function_28_47C2")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_485D")
    TurnDirection(0x104, 0x101, 0)

    ChrTalk(
        0x104,
        (
            "#0305FHold up, Lloyd. We still haven't dragged\x01",
            "Wald outta there, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FOh, yeah. Let's give chase immediately!\x02",
    )

    CloseMessageWindow()
    Jump("loc_48F1")

    label("loc_485D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48F1")
    TurnDirection(0x101, 0x104, 0)

    ChrTalk(
        0x101,
        (
            "#0005FHold on, Randy. We have to go\x01",
            "find Wald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FOh, yeah. Kinda forgot about that.\x01",
            "Let's go fish us out a thug!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48F1")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 1000, 0)
    EventEnd(0x4)
    Return()

    # Function_28_47C2 end

    SaveToFile()

Try(main)
