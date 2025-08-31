from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2500.bin",                # FileName
        "t2500",                    # MapName
        "t2500",                    # Location
        0x005A,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -25330, 0, -250, 0, 0, 1, 90, 0, 2, 0, 4],
    )

    BuildStringList((
        "t2500",                  # 0
        "Guardsman Nowe",         # 1
        "Guardsman Daimon",       # 2
        "Guardsman Garrison",     # 3
        "Guardsman Burrell",      # 4
        "Guardsman Alexei",       # 5
        "Merchant",               # 6
        "Tourist",                # 7
        "Girl",                   # 8
        "Tourist",                # 9
        "Merchant",               # 10
        "Tourist",                # 11
        "Girl",                   # 12
        "Tourist",                # 13
        "Tourist",                # 14
        "Tourist Long",           # 15
        "Tourist Arfet",          # 16
        "Sergeant Major Seeker",  # 17
        "Deputy Commander Baelz", # 18
        "Rookie Guardsman",       # 19
        "Rookie Guardsman",       # 20
        "Rookie Guardsman",       # 21
        "Rookie Guardsman",       # 22
        "Bus",                    # 23
        "Bus Driver",             # 24
        "車１",                   # 25
        "bt2500",                 # 26
        "bt2500",                 # 27
        "East Crossbell Highway", # 28
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 3, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 6, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 13, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_E4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 5, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 6, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 0, 0, 180)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_104", 0x0022, 16, 6, 0, 0, 1, 0, 0, "bt2500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31201.dat", "ms31301.dat", "ms31301.dat", "ms31301.dat", 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_148", 0x0022, 16, 6, 0, 0, 1, 0, 0, "bt2500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms00801.dat", "ms31201.dat", "ms31301.dat", "ms31301.dat", "ms31301.dat", 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_C4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch31300.itc",                   # 01
        "chr/ch21000.itc",                   # 02
        "chr/ch21100.itc",                   # 03
        "chr/ch21500.itc",                   # 04
        "chr/ch21200.itc",                   # 05
        "chr/ch23600.itc",                   # 06
        "chr/ch20800.itc",                   # 07
        "chr/ch28300.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch22100.itc",                   # 0A
    ))

    DeclNpc(-22430,  0,       4730,    270,  257,  0x0, 0,   0,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-22239,  0,       -5489,   270,  257,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(13659,   10000,   2849,    90,   257,  0x0, 0,   0,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(13859,   10000,   -2640,   90,   257,  0x0, 0,   1,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(13859,   10000,   -2640,   90,   385,  0x0, 0,   1,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-31389,  0,       19799,   90,   385,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-34919,  0,       15539,   45,   385,  0x0, 0,   3,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-34409,  0,       15039,   315,  401,  0x0, 0,   4,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-37229,  0,       -3910,   270,  385,  0x0, 0,   5,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-19379,  0,       13590,   90,   385,  0x0, 0,   2,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-20319,  0,       -11380,  270,  385,  0x0, 0,   3,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-24770,  0,       -11600,  180,  385,  0x0, 0,   4,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-31459,  0,       22420,   90,   385,  0x0, 0,   6,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-31409,  0,       23840,   90,   385,  0x0, 0,   7,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(2450,    5000,    -17899,  90,   385,  0x0, 0,   5,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-20709,  159,     -25729,  180,  385,  0x0, 0,   10,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-31139,  0,       23909,   90,   453,  0x0, 0,   8,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 35,  -50.41999816894531,    -0.07999999821186066,  0.0,                   256.0,                 [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.0625,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   0.0,                   25.209999084472656,    0.004999999888241291,  -0.0,                  1.0])
    DeclEvent(0x0000, 0, 33,  -31.280000686645508,   23.739999771118164,    0.0,                   2500.0,                [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   0.0,                   3.128000020980835,     -2.374000072479248,    -0.0,                  1.0])

    DeclActor(-31150,  0,       27650,   1200,    -31150,  1000,    27650,   0x007C, 0,  28, 0x0000)
    DeclActor(-18980,  200,     -11720,  1200,    -18980,  1700,    -11720,  0x007C, 0,  34, 0x0000)
    DeclActor(-39780,  0,       1010,    1200,    -39780,  2000,    1010,    0x007C, 0,  11, 0x0000)
    DeclActor(-8000,   1500,    -37500,  1200,    -8000,   2500,    -37500,  0x007C, 0,  5,  0x0000)

    PlaceName(-71.0, 0.0, -8.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-5.25, 0.0, -2.5, 0x0000, 0x0052, "")
    PlaceName(-30.950000762939453, 0.0, 28.100000381469727, 0x0000, 0x0055, "")
    PlaceName(-39.619998931884766, 0.0, 2.5999999046325684, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_6A4",          # 00, 0
        "Function_1_75C",          # 01, 1
        "Function_2_787",          # 02, 2
        "Function_3_7F7",          # 03, 3
        "Function_4_8EE",          # 04, 4
        "Function_5_AF8",          # 05, 5
        "Function_6_C84",          # 06, 6
        "Function_7_D78",          # 07, 7
        "Function_8_E94",          # 08, 8
        "Function_9_F29",          # 09, 9
        "Function_10_1502",        # 0A, 10
        "Function_11_15F1",        # 0B, 11
        "Function_12_15FF",        # 0C, 12
        "Function_13_203F",        # 0D, 13
        "Function_14_2AB0",        # 0E, 14
        "Function_15_3398",        # 0F, 15
        "Function_16_3D51",        # 10, 16
        "Function_17_3EBB",        # 11, 17
        "Function_18_3F78",        # 12, 18
        "Function_19_4033",        # 13, 19
        "Function_20_408A",        # 14, 20
        "Function_21_40E1",        # 15, 21
        "Function_22_419A",        # 16, 22
        "Function_23_420A",        # 17, 23
        "Function_24_426B",        # 18, 24
        "Function_25_432F",        # 19, 25
        "Function_26_4401",        # 1A, 26
        "Function_27_452D",        # 1B, 27
        "Function_28_465A",        # 1C, 28
        "Function_29_465E",        # 1D, 29
        "Function_30_4B86",        # 1E, 30
        "Function_31_532B",        # 1F, 31
        "Function_32_6324",        # 20, 32
        "Function_33_7A94",        # 21, 33
        "Function_34_7EF4",        # 22, 34
        "Function_35_7F58",        # 23, 35
    ))


    def Function_0_6A4(): pass

    label("Function_0_6A4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_6E4"),
        (1, "loc_6F0"),
        (2, "loc_6FC"),
        (3, "loc_708"),
        (4, "loc_714"),
        (5, "loc_720"),
        (6, "loc_72C"),
        (SWITCH_DEFAULT, "loc_738"),
    )


    label("loc_6E4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_744")

    label("loc_6F0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_744")

    label("loc_6FC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_744")

    label("loc_708")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_744")

    label("loc_714")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_744")

    label("loc_720")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_744")

    label("loc_72C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_744")

    label("loc_738")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_744")

    label("loc_744")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_744")

    label("loc_75B")

    Return()

    # Function_0_6A4 end

    def Function_1_75C(): pass

    label("Function_1_75C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_786")
    OP_94(0xFE, 0xFFFF9D40, 0xFFFFC20C, 0xFFFFADE4, 0xFFFFDCC4, 0x3E8)
    Sleep(250)
    Jump("Function_1_75C")

    label("loc_786")

    Return()

    # Function_1_75C end

    def Function_2_787(): pass

    label("Function_2_787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_END)), "loc_793")
    Call(0, 3)

    label("loc_793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B5")
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_7B5")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 30)

    label("loc_7B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CF")
    SetMapFlags(0x10000000)
    Event(0, 29)
    SetScenarioFlags(0x88, 2)
    Jump("loc_7F6")

    label("loc_7CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_7DE")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 8)

    label("loc_7DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_7F6")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_7F6")

    Return()

    # Function_2_787 end

    def Function_3_7F7(): pass

    label("Function_3_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_80A")
    ClearChrFlags(0x15, 0x80)
    Jump("loc_8D5")

    label("loc_80A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_81D")
    ClearChrFlags(0x14, 0x80)
    Jump("loc_8D5")

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_835")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_8D5")

    label("loc_835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_853")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    BeginChrThread(0x13, 0, 0, 1)
    Jump("loc_8D5")

    label("loc_853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_866")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_8D5")

    label("loc_866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8A6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_885")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_8A1")

    label("loc_885")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_8A1")
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_8A1")

    label("loc_8A1")

    Jump("loc_8D5")

    label("loc_8A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8BE")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_8D5")

    label("loc_8BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8CC")
    Jump("loc_8D5")

    label("loc_8CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8D5")

    label("loc_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8ED")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    label("loc_8ED")

    Return()

    # Function_3_7F7 end

    def Function_4_8EE(): pass

    label("Function_4_8EE")

    SetMapObjFlags(0x4, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    SetMapObjFrame(0x4, "chukin", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_941")
    Jump("loc_A3D")

    label("loc_941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_94F")
    Jump("loc_A3D")

    label("loc_94F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_95D")
    Jump("loc_A3D")

    label("loc_95D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_96B")
    Jump("loc_A3D")

    label("loc_96B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_97F")
    ClearMapObjFlags(0x4, 0x4)
    Jump("loc_A3D")

    label("loc_97F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A0C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A07")
    OP_65(0x0, 0x1)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x2)
    OP_78(0x5, 0x1E)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    SetChrPos(0x1E, -26910, 0, 24000, 0)
    OP_D3(0x1E, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_71(0x5, 0x1E, 0x1E, 0x0, 0x0)
    OP_74(0x5, 0x1E)

    label("loc_A07")

    Jump("loc_A3D")

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A1A")
    Jump("loc_A3D")

    label("loc_A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A28")
    Jump("loc_A3D")

    label("loc_A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_A3D")
    ClearScenarioFlags(0x5C, 0)

    label("loc_A3D")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AAA")
    ClearMapObjFlags(0x2, 0x4)
    OP_78(0x2, 0x20)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetChrPos(0x20, -40000, 0, 2500, 0)
    OP_D3(0x20, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x2, 0x1E)
    OP_70(0x2, 0x0)
    OP_66(0x2, 0x1)
    Jump("loc_AAF")

    label("loc_AAA")

    OP_16(0x3, 0x3, 0x1, 0x0)

    label("loc_AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACC")
    SetMapObjFlags(0x2, 0x4)

    label("loc_ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE0")
    SetMapObjFlags(0x2, 0x4)

    label("loc_AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF3")
    OP_70(0x6, 0x0)
    Jump("loc_AF7")

    label("loc_AF3")

    OP_70(0x6, 0x1E)

    label("loc_AF7")

    Return()

    # Function_4_8EE end

    def Function_5_AF8(): pass

    label("Function_5_AF8")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE2")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E2, 1)"), scpexpr(EXPR_END)), "loc_B78")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

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
    SetScenarioFlags(0x113, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_BDD")

    label("loc_B78")

    FadeToDark(300, 0, 100)
    SetChrName("")

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
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_BDD")

    Jump("loc_C78")

    label("loc_BE2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "How did Clarice Seeker decide her eldest daughter's name?\x01",
            "She wanted to raise a girl who could take no L's.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_C78")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_AF8 end

    def Function_6_C84(): pass

    label("Function_6_C84")

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
            "Crossbell City - East Exit\x01",      # 0
            "Armorica Village\x01",                # 1
            "Bus Stop (Fork)\x01",                 # 2
            "Leave\x01",                           # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2B")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D70")

    label("loc_D2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D50")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D70")

    label("loc_D50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D70")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_D70")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_C84 end

    def Function_7_D78(): pass

    label("Function_7_D78")

    Fade(1000)
    OP_68(-27530, 1000, 24550, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(24000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -32119, 0, 25500, 89)
    SetChrPos(0x1, -32119, 0, 24000, 89)
    SetChrPos(0x2, -32119, 0, 22500, 89)
    SetChrPos(0x3, -32119, 0, 21000, 89)
    ClearChrFlags(0x1E, 0x80)
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0x1E)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1E, -27000, 0, 4810, 0)
    OP_D3(0x1E, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_0D()
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)

    def lambda_E4E():
        OP_95(0xFE, -27000, 0, 23850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_E4E)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x1E, 1)
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x5)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_7_D78 end

    def Function_8_E94(): pass

    label("Function_8_E94")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -31260, 0, 26050, 89)
    SetChrPos(0x1, -31260, 0, 26050, 89)
    SetChrPos(0x2, -31260, 0, 26050, 89)
    SetChrPos(0x3, -31260, 0, 26050, 89)
    OP_68(-31260, 1000, 26050, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_8_E94 end

    def Function_9_F29(): pass

    label("Function_9_F29")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FA")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1497")
    Sound(1500, 255, 100, 0)
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCF")
    MenuCmd(1, 1, "★City - Central Square")
    MenuCmd(3, 1, 0x0)
    Jump("loc_FEA")

    label("loc_FCF")

    MenuCmd(1, 1, "　City - Central Square")

    label("loc_FEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1018")
    MenuCmd(1, 1, "★City - East Exit")
    MenuCmd(3, 1, 0x1)
    Jump("loc_102E")

    label("loc_1018")

    MenuCmd(1, 1, "　City - East Exit")

    label("loc_102E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105C")
    MenuCmd(1, 1, "★City - West Exit")
    MenuCmd(3, 1, 0x2)
    Jump("loc_1072")

    label("loc_105C")

    MenuCmd(1, 1, "　City - West Exit")

    label("loc_1072")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A1")
    MenuCmd(1, 1, "★City - South Exit")
    MenuCmd(3, 1, 0x3)
    Jump("loc_10B8")

    label("loc_10A1")

    MenuCmd(1, 1, "　City - South Exit")

    label("loc_10B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E7")
    MenuCmd(1, 1, "★City - North Exit")
    MenuCmd(3, 1, 0x4)
    Jump("loc_10FE")

    label("loc_10E7")

    MenuCmd(1, 1, "　City - North Exit")

    label("loc_10FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1128")
    MenuCmd(1, 1, "★Tangram Gate")
    MenuCmd(3, 1, 0x5)
    Jump("loc_113A")

    label("loc_1128")

    MenuCmd(1, 1, "　Tangram Gate")

    label("loc_113A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1166")
    MenuCmd(1, 1, "★Bellguard Gate")
    MenuCmd(3, 1, 0x6)
    Jump("loc_117A")

    label("loc_1166")

    MenuCmd(1, 1, "　Bellguard Gate")

    label("loc_117A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B2")
    MenuCmd(1, 1, "★St. Ursula Medical College")
    MenuCmd(3, 1, 0x7)
    Jump("loc_11D2")

    label("loc_11B2")

    MenuCmd(1, 1, "　St. Ursula Medical College")

    label("loc_11D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1200")
    MenuCmd(1, 1, "★Armorica Village")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1216")

    label("loc_1200")

    MenuCmd(1, 1, "　Armorica Village")

    label("loc_1216")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1248")
    MenuCmd(1, 1, "★Mainz Mining Village")
    MenuCmd(3, 1, 0x9)
    Jump("loc_1262")

    label("loc_1248")

    MenuCmd(1, 1, "　Mainz Mining Village")

    label("loc_1262")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_129C")
    MenuCmd(1, 1, "★Mainz Mountain Path - Tunnel")
    MenuCmd(3, 1, 0xA)
    Jump("loc_12BE")

    label("loc_129C")

    MenuCmd(1, 1, "　Mainz Mountain Path - Tunnel")

    label("loc_12BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12ED")
    MenuCmd(1, 1, "★Stargazer's Tower")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1304")

    label("loc_12ED")

    MenuCmd(1, 1, "　Stargazer's Tower")

    label("loc_1304")

    MenuCmd(1, 1, "　Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1488")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x2)
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
        (0, "loc_13DB"),
        (1, "loc_13E9"),
        (2, "loc_13F7"),
        (3, "loc_1405"),
        (4, "loc_1413"),
        (5, "loc_1421"),
        (6, "loc_142F"),
        (7, "loc_143D"),
        (8, "loc_144B"),
        (9, "loc_1459"),
        (10, "loc_1467"),
        (11, "loc_1475"),
        (SWITCH_DEFAULT, "loc_1483"),
    )


    label("loc_13DB")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1483")

    label("loc_13E9")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1483")

    label("loc_13F7")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1483")

    label("loc_1405")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1483")

    label("loc_1413")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1483")

    label("loc_1421")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1483")

    label("loc_142F")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1483")

    label("loc_143D")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1483")

    label("loc_144B")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1483")

    label("loc_1459")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1483")

    label("loc_1467")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_1483")

    label("loc_1475")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1483")

    label("loc_1483")

    Jump("loc_1492")

    label("loc_1488")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1492")

    Jump("loc_14F5")

    label("loc_1497")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E2")
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
    Jump("loc_14F5")

    label("loc_14E2")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14F5")

    Jump("loc_F43")

    label("loc_14FA")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_F29 end

    def Function_10_1502(): pass

    label("Function_10_1502")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -39760, 0, -650, 180)
    SetChrPos(0x1, -39760, 0, -650, 180)
    SetChrPos(0x2, -39760, 0, -650, 180)
    SetChrPos(0x3, -39760, 0, -650, 180)
    SetChrPos(0x4, -39760, 0, -650, 180)
    SetChrPos(0x5, -39760, 0, -650, 180)
    Sleep(1)
    OP_68(-39760, 1000, -650, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15D6")
    Sound(1502, 255, 100, 0)
    Jump("loc_15DC")

    label("loc_15D6")

    Sound(1503, 255, 100, 0)

    label("loc_15DC")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1502 end

    def Function_11_15F1(): pass

    label("Function_11_15F1")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_11_15F1 end

    def Function_12_15FF(): pass

    label("Function_12_15FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_16DD")

    ChrTalk(
        0xFE,
        (
            "If you're looking for Sergeant Major Seeker, she\x01",
            "woke up at the crack of dawn to drive to\x01",
            "the Crossbell Cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think she went there to give her report\x01",
            "about the ruins to Archbishop Eralda.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_203B")

    label("loc_16DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1796")

    ChrTalk(
        0xFE,
        (
            "I'm a little disappointed that the sergeant major\x01",
            "and you SSS guys were put in charge of that\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Us ordinary guardsmen need to improve,\x01",
            "too, y'know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_203B")

    label("loc_1796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_197D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D1")

    ChrTalk(
        0xFE,
        (
            "After the Anniversary Festival ended, I took\x01",
            "a one-day vacation to Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That was a month ago, but I'm still feeling\x01",
            "better than I ever have. Man, my vacation\x01",
            "really must have helped me let loose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'Cause I feel so great, I'm going to go\x01",
            "100 percent today, too!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1978")

    label("loc_18D1")


    ChrTalk(
        0xFE,
        (
            "Your efficiency while working is bound to\x01",
            "drop if you're exhausted. It's undeniable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So that means getting the appropriate\x01",
            "amount of rest each night is key!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1978")

    Jump("loc_203B")

    label("loc_197D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1A36")

    ChrTalk(
        0xFE,
        (
            "*yawn* Almost time for a wave of\x01",
            "people to return home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had planned to take the day off tomorrow,\x01",
            "but maybe I should postpone it\x01",
            "if we're going to be so busy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_203B")

    label("loc_1A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1ABD")

    ChrTalk(
        0xFE,
        (
            "Little by little, Calvardian tourists have\x01",
            "started to make their way home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Tomorrow's going to be so packed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_203B")

    label("loc_1ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1CF5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1C33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B81")

    ChrTalk(
        0xFE,
        (
            "I actually plan to take a vacation day\x01",
            "once the festival is over and done with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to copy the tourists and relax\x01",
            "over at Armorica Village.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C2E")

    label("loc_1B81")


    ChrTalk(
        0xFE,
        (
            "Deputy Commander Baelz usually permits\x01",
            "time off if your assigned duties have been\x01",
            "flawlessly completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That being the case, I really have my work\x01",
            "cut out for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C2E")

    Jump("loc_1CF0")

    label("loc_1C33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_1CBF")

    ChrTalk(
        0xFE,
        (
            "So there's a counterfeit dealer hiding in the\x01",
            "group of people who just passed by...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmmmm... Which one was it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CF0")

    label("loc_1CBF")


    ChrTalk(
        0xFE,
        "*yawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Crap, I can't start dozing off.\x02",
    )

    CloseMessageWindow()

    label("loc_1CF0")

    Jump("loc_203B")

    label("loc_1CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1DDE")

    ChrTalk(
        0xFE,
        (
            "Yesterday, we had a large influx of tourists\x01",
            "coming from Calvard pass through the gate.\x01",
            "As you could probably guess, it was hectic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's still a lot more coming, so I should\x01",
            "brace myself while I still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_203B")

    label("loc_1DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1F64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ECF")

    ChrTalk(
        0xFE,
        (
            "Deputy Commander Baelz is the one who\x01",
            "actually runs Tangram Gate. Trust me, you\x01",
            "don't find guardsmen as skilled as her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It probably wouldn't be an exaggeration to\x01",
            "say she's the best the CGF has to offer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F5F")

    label("loc_1ECF")


    ChrTalk(
        0xFE,
        "If only that pesky commander wasn't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sorry. I almost said something out of line.\x01",
            "I'd appreciate it if you kept this between us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5F")

    Jump("loc_203B")

    label("loc_1F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_203B")

    ChrTalk(
        0xFE,
        (
            "Recently, a delivery truck got into a serious accident\x01",
            "not long after passing through Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It doesn't make sense. The road past here is always\x01",
            "clear. What could have caused the accident?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_203B")

    TalkEnd(0xFE)
    Return()

    # Function_12_15FF end

    def Function_13_203F(): pass

    label("Function_13_203F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_214A")

    ChrTalk(
        0xFE,
        (
            "You wouldn't believe the amount of\x01",
            "unsettling rumors I hear from people\x01",
            "passing through Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For example, I heard that there was a huge\x01",
            "fight somewhere in the city yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's something strange going on,\x01",
            "mark my words.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAC")

    label("loc_214A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_22D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2254")

    ChrTalk(
        0xFE,
        (
            "Everyone appreciates you all for backing up\x01",
            "Sergeant Major Seeker at the Moon Temple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Special Support Section really\x01",
            "is no joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, we're in your debt. If you ever need a\x01",
            "helping hand, feel free to call Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22D4")

    label("loc_2254")


    ChrTalk(
        0xFE,
        (
            "All the guardsmen here at Tangram Gate\x01",
            "are in the Special Support Section's debt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Just call us if you ever need help.\x02",
    )

    CloseMessageWindow()

    label("loc_22D4")

    Jump("loc_2AAC")

    label("loc_22D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_250E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E8")

    ChrTalk(
        0xFE,
        "Good afternoon, Sergeant Major Seeker!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500FKeep up the good work. Any suspicious\x01",
            "activity coming from the Republic?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nothing out of the ordinary, ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, there haven't been any serious issues\x01",
            "with any of the tourists passing through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0503FGood to hear. The Special Support Section\x01",
            "and I are going to investigate the ruins that\x01",
            "gave the scouting party trouble.\x02\x03",
            "#0501FI'll leave security in your capable hands.\x01",
            "Make the Crossbell Guardian Force proud!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, ma'am!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2509")

    label("loc_24E8")


    ChrTalk(
        0xFE,
        "Nothing abnormal to report!\x02",
    )

    CloseMessageWindow()

    label("loc_2509")

    Jump("loc_2AAC")

    label("loc_250E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_25C1")

    ChrTalk(
        0xFE,
        "Finally the last day of the festival.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess most of the tourists leaving had no\x01",
            "intention of staying for the closing ceremony.\x01",
            "Well, I can't blame them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAC")

    label("loc_25C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2649")

    ChrTalk(
        0xFE,
        (
            "Dang, what a crowd. I might be wrong, but it\x01",
            "looks like a lot more buses have been leaving\x01",
            "for the Republic today...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAC")

    label("loc_2649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_291D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2735")

    ChrTalk(
        0xFE,
        (
            "There's barely been any people coming to\x01",
            "Crossbell FROM Calvard.\x01",
            "Today must be the turning point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm willing to bet that people heading back to the\x01",
            "Republic will start trickling in again tomorrow...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2918")

    label("loc_2735")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_279C")

    ChrTalk(
        0xFE,
        (
            "There's something about that black-haired\x01",
            "lady that I can't put my finger on...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2918")

    label("loc_279C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2899")

    ChrTalk(
        0xFE,
        (
            "Nowe's going to get in trouble if he keeps\x01",
            "yawning and dozing off like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's no skin off my back if Deputy Commander\x01",
            "Baelz finds out.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Oh, yeah, you guys are that new police\x01",
            "squad or whatever, right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2899")


    ChrTalk(
        0xFE,
        (
            "If you need the deputy commander, her\x01",
            "office is on the second floor of the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm pretty sure she's in right now.\x02",
    )

    CloseMessageWindow()

    label("loc_2918")

    Jump("loc_2AAC")

    label("loc_291D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_29B2")

    ChrTalk(
        0xFE,
        (
            "I wanted to go to the Anniversary Festival,\x01",
            "but...we're really, REALLY busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm sure Bellguard Gate has it just as rough...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AAC")

    label("loc_29B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2A54")

    ChrTalk(
        0xFE,
        (
            "Our work is cut out for us next month. The\x01",
            "Anniversary Festival never fails to bring in\x01",
            "tons of tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I don't think I'm ready for it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AAC")

    label("loc_2A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2AAC")

    ChrTalk(
        0xFE,
        (
            "Beyond this gate is Calvardian territory.\x01",
            "Do you have some business here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AAC")

    TalkEnd(0xFE)
    Return()

    # Function_13_203F end

    def Function_14_2AB0(): pass

    label("Function_14_2AB0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B73")

    ChrTalk(
        0xFE,
        (
            "I wonder if us guarding the border\x01",
            "really makes a difference...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whenever it's this peaceful, I usually\x01",
            "think, 'What do we even have to worry\x01",
            "about? Everything's fine.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3394")

    label("loc_2B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2C36")

    ChrTalk(
        0xFE,
        (
            "Thank goodness it didn't take too long\x01",
            "for Burrell to get back on his feet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Some CGF guardsman he is. Getting\x01",
            "scared by monsters so bad he fainted?\x01",
            "Seriously uncool, man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3394")

    label("loc_2C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2CB6")

    ChrTalk(
        0xFE,
        "Hmm, I wonder how Burrell's doing...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, I can't worry about him. My post\x01",
            "needs to be my top priority.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3394")

    label("loc_2CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2D1A")

    ChrTalk(
        0xFE,
        (
            "This is where the buses to the Republic\x01",
            "depart from...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Festival's over, eh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3394")

    label("loc_2D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2DB6")

    ChrTalk(
        0xFE,
        "Traffic to Calvard has gotten a lot busier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*yaaaawn*\x01",
            "Crap, I almost fell asleep there. This spot\x01",
            "is too peaceful for its own good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3394")

    label("loc_2DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2EA6")

    ChrTalk(
        0xFE,
        (
            "You know, I feel a bit relieved to see all\x01",
            "the Calvardians laughing and smiling\x01",
            "when they stop by the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before the Non-Aggression Pact was\x01",
            "signed, terrorism was rampant here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You can't put a price on peace.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3394")

    label("loc_2EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2FA0")

    ChrTalk(
        0xFE,
        (
            "The view yesterday was something else,\x01",
            "let me tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I couldn't believe how many groups of Calvardians\x01",
            "were traveling by orbal bus...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, I've never seen THAT many people before,\x01",
            "not including our marching drills.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3394")

    label("loc_2FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_31B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3103")

    ChrTalk(
        0xFE,
        (
            "Past this gate, it's still quite a trek to get to the\x01",
            "Republic's border. The scenery is nice, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That being said, we can't use distance as an\x01",
            "excuse to slack off. And honestly, I'd rather\x01",
            "be stationed here than at Bellguard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Over there, you have that inept commander\x01",
            "running things, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301F...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31AD")

    label("loc_3103")


    ChrTalk(
        0xFE,
        (
            "In some ways, I think I'm lucky to have\x01",
            "been stationed at Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Instead of that blockhead, I'm able to work\x01",
            "under the brilliant Deputy Commander Baelz.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AD")

    Jump("loc_3394")

    label("loc_31B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3394")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E3")

    ChrTalk(
        0xFE,
        (
            "That massive port city you can see on\x01",
            "the other side of the river is Altair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Up until the signing of the Non-Aggression\x01",
            "Pact, Calvard was frequently conducting\x01",
            "drills around Tangram Hill all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It honestly felt like we were living\x01",
            "our lives at gunpoint...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3394")

    label("loc_32E3")


    ChrTalk(
        0xFE,
        (
            "Up until the signing of the Non-Aggression\x01",
            "Pact, Calvard was conducting giant military\x01",
            "drills around Tangram Hill all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Tensions ran awfully high back then...\x02",
    )

    CloseMessageWindow()

    label("loc_3394")

    TalkEnd(0xFE)
    Return()

    # Function_14_2AB0 end

    def Function_15_3398(): pass

    label("Function_15_3398")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_34B9")

    ChrTalk(
        0xFE,
        (
            "Everyone that travels to Crossbell brings\x01",
            "their own set of ideals with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given how many people that actually is,\x01",
            "I'm sure there are some bad apples\x01",
            "among them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, since I'm in charge of security today,\x01",
            "I want to crack down on as many of them\x01",
            "as I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D4D")

    label("loc_34B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_35B9")

    ChrTalk(
        0xFE,
        (
            "When we went to scout out that temple, I\x01",
            "got spooked real bad by some monsters.\x01",
            "I was bedridden for a while, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't mean to be such a burden on\x01",
            "everyone... I've got to work harder than\x01",
            "ever before to make it up to them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D4D")

    label("loc_35B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_35C7")
    Jump("loc_3D4D")

    label("loc_35C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_36C5")

    ChrTalk(
        0xFE,
        (
            "There's a bunch of people that I owe favors\x01",
            "to, and I WOULD go see what I can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But I can't really leave my post right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A part of me feels bad for them, and\x01",
            "the other part feels pretty lucky to\x01",
            "have comrades like them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D4D")

    label("loc_36C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3792")

    ChrTalk(
        0xFE,
        (
            "Believe me, I really do appreciate the beauty\x01",
            "that is guarding the Republican border...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but when I remember that Calvard has its\x01",
            "eyes set on us, it gets a little less beautiful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D4D")

    label("loc_3792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3842")

    ChrTalk(
        0xFE,
        "Wow, what a nice view...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite my complaints, I can never settle\x01",
            "down when I go to the city. With that in mind,\x01",
            "guarding the border isn't too shabby.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D4D")

    label("loc_3842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3A01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_394E")

    ChrTalk(
        0xFE,
        (
            "My pal Brood was stationed at Bellguard\x01",
            "Gate. I wonder how he's holding up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been friends with him ever since our\x01",
            "days in Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard they had some trouble over there,\x01",
            "so I can't help but wonder how he's doing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_39FC")

    label("loc_394E")


    ChrTalk(
        0xFE,
        (
            "In times like these, I keep wondering how\x01",
            "Brood's surviving over at Bellguard Gate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "CGF guardsmen live where they're stationed,\x01",
            "so I haven't seen him in a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39FC")

    Jump("loc_3D4D")

    label("loc_3A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3B19")

    ChrTalk(
        0xFE,
        (
            "The CGF can't afford to conduct larger military\x01",
            "drills. We never know what is going to provoke\x01",
            "the Empire or Republic, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And considering the fact that I joined the CGF\x01",
            "in order to practice my sharpshooting...I can't\x01",
            "help but feel a little depressed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D4D")

    label("loc_3B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3D4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD5")

    ChrTalk(
        0xFE,
        "Oh...? The Special Support Section, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good work solving those monster attacks\x01",
            "last month. Couldn't have been easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FH-Haha... Yeah, we barely scraped by.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FIf Zeit had not come to our rescue, I doubt\x01",
            "we would be standing here right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey, don't be so hard on yourselves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pretty sure Deputy Commander Baelz is\x01",
            "expecting great things from you, so try not\x01",
            "to let her down!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D4D")

    label("loc_3CD5")


    ChrTalk(
        0xFE,
        (
            "Deputy Commander Baelz is expecting\x01",
            "great things from the Special Support\x01",
            "Section. Keep doing your best, everyone!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D4D")

    TalkEnd(0xFE)
    Return()

    # Function_15_3398 end

    def Function_16_3D51(): pass

    label("Function_16_3D51")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E15")

    ChrTalk(
        0xFE,
        (
            "I've been having to cover guard duty\x01",
            "for Burrell lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anyone saw what shape he's in, I doubt\x01",
            "anyone would ever volunteer for another\x01",
            "scouting mission again...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3EB7")

    label("loc_3E15")


    ChrTalk(
        0xFE,
        (
            "Ever since that scouting mission of the\x01",
            "ruins near Mainz, Burrell's been holed up\x01",
            "in bed, and I've been covering his shifts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* Boy, am I hungry...\x02",
    )

    CloseMessageWindow()

    label("loc_3EB7")

    TalkEnd(0xFE)
    Return()

    # Function_16_3D51 end

    def Function_17_3EBB(): pass

    label("Function_17_3EBB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Phew, I finally made it to the gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Here marks the end to another great\x01",
            "shopping trip in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Time to get my papers checked and\x01",
            "head on back home to Calvard.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_3EBB end

    def Function_18_3F78(): pass

    label("Function_18_3F78")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Orbal buses are starting to get pretty\x01",
            "popular in Calvard, too, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Most of them are manufactured by the\x01",
            "Republic's Verne Company, even the\x01",
            "ones here in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_3F78 end

    def Function_19_4033(): pass

    label("Function_19_4033")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Mama, let's hurry and get on the bus.\x01",
            "I wanna get to the festival already!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_4033 end

    def Function_20_408A(): pass

    label("Function_20_408A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmmm, people weren't joking when they\x01",
            "told me how beautiful Crossbell was.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_408A end

    def Function_21_40E1(): pass

    label("Function_21_40E1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I had planned on getting my passport\x01",
            "checked and returning to Calvard early,\x01",
            "but...what's with this crowd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe taking the railway would have\x01",
            "been a smarter decision.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_40E1 end

    def Function_22_419A(): pass

    label("Function_22_419A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hohoho! If I wait here long enough,\x01",
            "I'll be the first person to board the\x01",
            "bus back to the Republic!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_419A end

    def Function_23_420A(): pass

    label("Function_23_420A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Whoa, look at all of the cool soldiers. Do\x01",
            "you think they'd play with me if I asked?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_420A end

    def Function_24_426B(): pass

    label("Function_24_426B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Crossbell City, a place where mafiosos\x01",
            "run free throughout the streets...\x01",
            "It sure sounds exciting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The stories of Crossbell being the continent's\x01",
            "City of Sin must have been true.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_426B end

    def Function_25_432F(): pass

    label("Function_25_432F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Phew. So this bus is going to take me\x01",
            "to Crossbell City?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being as old as I am, I don't handle standing\x01",
            "around well these days. I would much rather\x01",
            "take the train. At least I could relax, then.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_432F end

    def Function_26_4401(): pass

    label("Function_26_4401")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44AD")

    ChrTalk(
        0xFE,
        (
            "Whoaaa... Altair looks so tiny\x01",
            "from all the way out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm somewhat moved, thinking about\x01",
            "how we managed to cross the great\x01",
            "Tangram Hill.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4529")

    label("loc_44AD")


    ChrTalk(
        0xFE,
        (
            "We finally made it over the great\x01",
            "Tangram Hill, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Traveling by bus made the trip\x01",
            "pretty nice, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4529")

    TalkEnd(0xFE)
    Return()

    # Function_26_4401 end

    def Function_27_452D(): pass

    label("Function_27_452D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4605")

    ChrTalk(
        0xFE,
        (
            "It's always such a thrill to hear the\x01",
            "thundering sound of the trains when\x01",
            "they pass by the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the only bad thing is that the\x01",
            "wind from the train usually makes\x01",
            "my skirt fly up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4656")

    label("loc_4605")


    ChrTalk(
        0xFE,
        "Whoa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really should practice holding\x01",
            "my skirt down against the wind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4656")

    TalkEnd(0xFE)
    Return()

    # Function_27_452D end

    def Function_28_465A(): pass

    label("Function_28_465A")

    Call(0, 6)
    Return()

    # Function_28_465A end

    def Function_29_465E(): pass

    label("Function_29_465E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(-16650, 400, -10470, 0)
    MoveCamera(65, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22430, 0)
    OP_0D()
    Sleep(500)
    OP_68(-14930, 400, 890, 5000)
    MoveCamera(80, 18, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(56040, 5000)
    PlaceName2(340, 200, "c_plac19", 0x0, 4000)
    OP_6F(0x79)
    Sleep(3000)
    OP_68(-48970, 1000, -460, 4700)
    MoveCamera(45, 30, 0, 4700)
    OP_6E(510, 4700)
    SetCameraDistance(26660, 4700)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A5B")
    ClearChrFlags(0x1E, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_477A")
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0x1E)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    Jump("loc_4791")

    label("loc_477A")

    ClearMapObjFlags(0x2, 0x4)
    OP_78(0x2, 0x1E)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)

    label("loc_4791")

    OP_49()
    SetChrPos(0x1E, -63820, 0, -120, 0)
    OP_D3(0x1E, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_47DA")
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    Jump("loc_47F0")

    label("loc_47DA")

    SetMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)

    label("loc_47F0")

    Sleep(2200)

    def lambda_47F8():
        OP_95(0xFE, -26120, 0, -90, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_47F8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_482A")
    Sleep(1000)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    Jump("loc_4830")

    label("loc_482A")

    Sound(485, 0, 100, 0)

    label("loc_4830")

    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1E, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_485B")
    SetChrFlags(0x1E, 0x80)
    SetMapObjFlags(0x5, 0x4)
    Jump("loc_4892")

    label("loc_485B")

    SetChrPos(0x1E, -40000, 0, 2500, 0)
    OP_D3(0x1E, 0x0, 0x41EB0, 0x0, 0x0)
    OP_71(0x2, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x2)
    OP_66(0x2, 0x1)

    label("loc_4892")

    OP_68(-50970, 1000, -460, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26660, 0)
    Sleep(1)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_4977")
    SetChrPos(0x0, -31260, 0, 26050, 89)
    SetChrPos(0x1, -31260, 0, 26050, 89)
    SetChrPos(0x2, -31260, 0, 26050, 89)
    SetChrPos(0x3, -31260, 0, 26050, 89)
    OP_68(-31260, 1000, 26050, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    ClearScenarioFlags(0x7E, 0)
    Jump("loc_4A46")

    label("loc_4977")

    SetChrPos(0x0, -39760, 0, -650, 180)
    SetChrPos(0x1, -39760, 0, -650, 180)
    SetChrPos(0x2, -39760, 0, -650, 180)
    SetChrPos(0x3, -39760, 0, -650, 180)
    SetChrPos(0x4, -39760, 0, -650, 180)
    SetChrPos(0x5, -39760, 0, -650, 180)
    Sleep(1)
    OP_68(-39760, 1000, -650, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A31")
    Sound(1502, 255, 100, 0)
    Jump("loc_4A37")

    label("loc_4A31")

    Sound(1503, 255, 100, 0)

    label("loc_4A37")

    Sleep(500)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x7E, 1)

    label("loc_4A46")

    Call(0, 3)
    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_4B7E")

    label("loc_4A5B")

    Sleep(2500)
    SetChrPos(0x0, -54820, 0, -130, 270)
    SetChrPos(0x1, -56020, 0, -1200, 270)
    SetChrPos(0x2, -56170, 0, 1010, 270)
    SetChrPos(0x3, -57750, 0, -190, 270)
    OP_0D()

    def lambda_4AA8():
        OP_95(0xFE, -50820, 0, -130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4AA8)

    def lambda_4AC2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4AC2)
    Sleep(100)

    def lambda_4AD6():
        OP_95(0xFE, -52020, 0, -1200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4AD6)

    def lambda_4AF0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4AF0)
    Sleep(120)

    def lambda_4B04():
        OP_95(0xFE, -52170, 0, 1010, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4B04)

    def lambda_4B1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_4B1E)
    Sleep(90)

    def lambda_4B32():
        OP_95(0xFE, -53750, 0, -190, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4B32)

    def lambda_4B4C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_4B4C)
    WaitChrThread(0x0, 1)
    WaitChrThread(0x1, 1)
    WaitChrThread(0x2, 1)
    WaitChrThread(0x3, 1)
    WaitChrThread(0x0, 2)
    WaitChrThread(0x1, 2)
    WaitChrThread(0x2, 2)
    WaitChrThread(0x3, 2)
    Sleep(1000)
    Call(0, 3)

    label("loc_4B7E")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_29_465E end

    def Function_30_4B86(): pass

    label("Function_30_4B86")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-22750, 3100, 20090, 0)
    MoveCamera(52, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19040, 0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch05700.itc", 0x22)
    LoadChrToIndex("chr/ch00800.itc", 0x23)
    LoadChrToIndex("chr/ch31250.itc", 0x24)
    LoadChrToIndex("chr/ch31350.itc", 0x25)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrPos(0x18, -17000, 0, 22500, 270)
    SetChrPos(0x19, -16500, 0, 21500, 270)
    SetChrPos(0x101, -21000, 0, 19000, 0)
    SetChrPos(0x102, -22000, 0, 18000, 0)
    SetChrPos(0x103, -20000, 0, 18000, 0)
    SetChrPos(0x104, -21000, 0, 17000, 0)
    SetChrPos(0x1A, -19500, 0, 26000, 180)
    SetChrPos(0x1B, -20500, 0, 25500, 180)
    SetChrPos(0x1C, -21500, 0, 25500, 180)
    SetChrPos(0x1D, -22500, 0, 26000, 180)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_68(-22750, 2200, 20090, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x18,
        (
            "#11P#0501FIt's time for your combat training\x01",
            "session to begin.\x02\x03",
            "This will be a four-on-four fight. You'll have\x01",
            "to use each of your strengths strategically\x01",
            "if you want to come out on top.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PWe're up against the Special Support Section?\x01",
            "I've heard they're no slouches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#11PLook. Isn't that Randy Orlando...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#11PAw, crap. Are we going to be okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PDidn't the rumors say he tried to get with\x01",
            "one too many girls and got fired?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PHow strong can a playboy REALLY be...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PWhatever. We'll show what we're made of\x01",
            "and bring him down a peg or two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0203FThey sure are boastful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0304FHeh. These newbies are pretty lively.\x02\x03",
            "#0300FI'll make sure to give 'em a valuable\x01",
            "practice session, so they can come\x01",
            "at me however they like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11P#2003FOrlando. Keep your comments\x01",
            "to yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0306FWhy just me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11P#0507F#4S#NEveryone, advance!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopBGM(0x9C4)
    SetCameraDistance(16079, 1000)
    OP_68(-22750, 1900, 20090, 1000)

    def lambda_50D4():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50D4)

    def lambda_50EE():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_50EE)

    def lambda_5108():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5108)

    def lambda_5122():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5122)

    def lambda_513C():
        OP_98(0xFE, 0x1F4, 0x0, 0xFFFFF830, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_513C)

    def lambda_5156():
        OP_98(0xFE, 0x12C, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5156)

    def lambda_5170():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5170)

    def lambda_518A():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFF830, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_518A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1D, 1)
    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x25)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x25)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(100)
    Sound(531, 0, 100, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)

    ChrTalk(
        0x101,
        "#12P#0005FThese guys are no joke...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0101FWell, they're under impressive leadership.\x02\x03",
            "They may be new recruits, but we shouldn't\x01",
            "underestimate them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11P#0507F#4S#NNow, commence the operation!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Battle("BattleInfo_104", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5321")
    Call(0, 31)
    Jump("loc_532A")

    label("loc_5321")

    OP_29(0xF, 0x1, 0x1)
    Call(0, 32)

    label("loc_532A")

    Return()

    # Function_30_4B86 end

    def Function_31_532B(): pass

    label("Function_31_532B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-22750, 2200, 20090, 0)
    MoveCamera(52, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19040, 0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch05700.itc", 0x22)
    LoadChrToIndex("chr/ch00800.itc", 0x23)
    LoadChrToIndex("chr/ch00850.itc", 0x24)
    LoadChrToIndex("chr/ch31250.itc", 0x25)
    LoadChrToIndex("chr/ch31350.itc", 0x26)
    LoadChrToIndex("chr/ch31253.itc", 0x27)
    LoadChrToIndex("chr/ch31353.itc", 0x28)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x2)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x28)
    SetChrSubChip(0x1B, 0x2)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x28)
    SetChrSubChip(0x1C, 0x2)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x27)
    SetChrSubChip(0x1D, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x18, -17000, 0, 22500, 270)
    SetChrPos(0x19, -16500, 0, 21500, 270)
    SetChrPos(0x101, -21000, 0, 20000, 0)
    SetChrPos(0x102, -22000, 0, 19000, 0)
    SetChrPos(0x103, -20000, 0, 19000, 0)
    SetChrPos(0x104, -21000, 0, 18000, 0)
    SetChrPos(0x1A, -19000, 0, 24000, 180)
    SetChrPos(0x1B, -20200, 0, 25200, 180)
    SetChrPos(0x1C, -21800, 0, 25200, 180)
    SetChrPos(0x1D, -23000, 0, 24000, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x18,
        "#11P#0507F#4S#NThat's enough!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x1A,
        "#11PTch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PI-I knew they'd be strong, but not\x01",
            "THAT strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PEspecially that Orlando guy... Guess\x01",
            "the rumors were true, after all.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#12P#0304FThere ya go. Over in a flash.\x02\x03",
            "#0300FHey, you guys didn't do half bad\x01",
            "for newbies.\x02\x03",
            "You've still got a way to go to\x01",
            "catch up with us, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5PDamn it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FHey, you guys are in excellent shape.\x02\x03",
            "#0000FI'd say you're perfectly suited for the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FAgreed. If we had let our guard down\x01",
            "for even a second, we could have\x01",
            "easily lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FBut now our request should be completed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FThanks for remindin' me, Tio Tot.\x02\x03",
            "#0309FWell, Deputy Commander, it's been great\x01",
            "and all, but we're gonna have to excuse\x01",
            "ourselves for today.\x02\x03",
            "#0304FSo, Lloyd, what's on the sched--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x101, 300)

    ChrTalk(
        0x19,
        (
            "#11P#2005FOh? Who said that you were to only\x01",
            "participate in one battle?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#12P#0305FSay what now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FTh-There's more...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 300)

    ChrTalk(
        0x19,
        "#11P#2003FSergeant Major Seeker!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11P#0501F#N#4SYes, ma'am!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_5973():
        OP_95(0xFE, -21000, 0, 23700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5973)
    WaitChrThread(0x18, 1)

    def lambda_5991():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5991)
    WaitChrThread(0x18, 1)
    Fade(500)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x18,
        "#5P#0507F#4SAll troops, attention!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "CGF Guardsmen",
        "#N#4SY-Yes, ma'am!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x1A, 0x1)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x1)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x1)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x0)
    SetChrSubChip(0x1D, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#12P#0105FD-Deputy Commander Baelz, what\x01",
            "exactly do you want from us...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x101, 300)

    ChrTalk(
        0x19,
        (
            "#11P#2004FI think it should be obvious.\x02\x03",
            "#2001FYou will continue the combat training. Now\x01",
            "you will engage the recruits under Sergeant\x01",
            "Major Seeker's command.\x02",
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
        0x104,
        (
            "#12P#0305FTh-The hell?! Why didn't you mention that\x01",
            "we'd be fightin' two consecutive battles?!\x02\x03",
            "#0306FAnd now that Noel's with 'em, we're\x01",
            "outnumbered! How's that for fair?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11P#2005FWasn't the support request called 'Guardian\x01",
            "Force Drill Participation'?\x02\x03",
            "#2002FIsn't it only natural for you to continue with\x01",
            "their training like a proper mentor, Orlando?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0305FYou sly devil, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11P#2003FYou defeated the four recruits quite handily.\x02\x03",
            "#2000FWith the additional strength of Sergeant Major Seeker,\x01",
            "I think your abilities will be about equal now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0206FI see the logic, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FHaha. It looks like the deputy commander is\x01",
            "craftier than we thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5P#0506FS-Sorry about this. I know this challenge\x01",
            "came out of the blue and all...\x02\x03",
            "#0501FBut I plan to use this as a way to gauge my\x01",
            "own strength, so I'm going to go all out!\x02\x03",
            "#0503FLet's make this a good one, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0306FDamn it! How am I s'posed to say no now?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FIt appears we have no choice in the matter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FWe may not have been expecting this, but\x01",
            "let's go all out, same as Sergeant Major Seeker!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0202FLet us make the best of the situation.\x02",
    )

    CloseMessageWindow()

    def lambda_6037():
        OP_95(0xFE, -17000, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6037)
    WaitChrThread(0x19, 1)

    def lambda_6055():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6055)
    WaitChrThread(0x19, 1)

    ChrTalk(
        0x19,
        (
            "#11P#2004FNow that we're all on the same page...\x01",
            "I will be officiating the match this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11P#2001F#4S#NCGF, at the ready!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopBGM(0xBB8)
    SetCameraDistance(16079, 1000)
    OP_68(-22750, 1900, 20090, 1000)
    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x1A, 0x26)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x26)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrSubChip(0x1D, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(100)
    Sound(531, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x1B,
        (
            "#11PA-All right! If the sergeant major is on our side\x01",
            "this time, we'll be unstoppable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5PYeah! Let's do this!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)

    ChrTalk(
        0x101,
        (
            "#12P#0001FOur opponents are four CGF recruits, plus the\x01",
            "sergeant major...and they're all combat experts.\x02\x03",
            "#0007FFrom the looks of it, they've already recovered\x01",
            "from our last fight. We can't hold back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0307FYou said it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11P#2001F#4S#NBegin!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Battle("BattleInfo_148", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_631A")
    OP_29(0xF, 0x1, 0x3)
    Jump("loc_6320")

    label("loc_631A")

    OP_29(0xF, 0x1, 0x2)

    label("loc_6320")

    Call(0, 32)
    Return()

    # Function_31_532B end

    def Function_32_6324(): pass

    label("Function_32_6324")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-22750, 1900, 20090, 0)
    MoveCamera(52, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18940, 0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch05700.itc", 0x22)
    LoadChrToIndex("chr/ch00800.itc", 0x23)
    LoadChrToIndex("chr/ch00850.itc", 0x24)
    LoadChrToIndex("chr/ch31250.itc", 0x25)
    LoadChrToIndex("chr/ch31350.itc", 0x26)
    LoadChrToIndex("chr/ch31253.itc", 0x27)
    LoadChrToIndex("chr/ch31353.itc", 0x28)
    LoadChrToIndex("chr/ch00053.itc", 0x29)
    LoadChrToIndex("chr/ch00153.itc", 0x2A)
    LoadChrToIndex("chr/ch00253.itc", 0x2B)
    LoadChrToIndex("chr/ch00353.itc", 0x2C)
    LoadChrToIndex("chr/ch00853.itc", 0x2D)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrPos(0x101, -21000, 0, 20000, 0)
    SetChrPos(0x102, -22000, 0, 19000, 0)
    SetChrPos(0x103, -20000, 0, 19000, 0)
    SetChrPos(0x104, -21000, 0, 18000, 0)
    SetChrPos(0x1A, -19000, 0, 24000, 180)
    SetChrPos(0x1B, -20200, 0, 25200, 180)
    SetChrPos(0x1C, -21800, 0, 25200, 180)
    SetChrPos(0x1D, -23000, 0, 24000, 180)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_6B93")
    SetChrPos(0x18, -21000, 0, 23700, 180)
    SetChrPos(0x19, -17000, 0, 22500, 270)
    SetChrChipByIndex(0x18, 0x2D)
    SetChrSubChip(0x18, 0x2)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x2)
    SetChrChipByIndex(0x1B, 0x28)
    SetChrSubChip(0x1B, 0x2)
    SetChrChipByIndex(0x1C, 0x28)
    SetChrSubChip(0x1C, 0x2)
    SetChrChipByIndex(0x1D, 0x27)
    SetChrSubChip(0x1D, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x19,
        "#11P#2001F#4S#NCease!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x1A,
        "#11PDamn it all... Still no good?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PWe even had Sergeant Major Seeker with\x01",
            "us... How pathetic can we get?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5P#0506FYou all really are strong.\x02\x03",
            "I guess I'm still pretty inexperienced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FHaha, there's no need to be humble.\x01",
            "You had us on the ropes there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FOnce you took charge, Noel, everyone\x01",
            "else's skill shot up.\x02\x03",
            "#0304FHeh. Guess that's why they call you the\x01",
            "hope of the CGF or whatever it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#5P#0509FH-Haha... I'll take the compliment.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    TurnDirection(0x19, 0x1C, 300)

    ChrTalk(
        0x19,
        (
            "#11P#2001FTroops, listen and listen carefully.\x02\x03",
            "This is the strength of people who have fought\x01",
            "the mafia and monsters in live combat.\x02\x03",
            "#2003FIt's clear that your experience is nowhere near\x01",
            "sufficient as things stand.\x02\x03",
            "And to make matters worse, the Crossbell\x01",
            "Guardian Force isn't allowed to conduct any\x01",
            "large-scale training operations...\x02\x03",
            "#2001FBut, despite all that, there are still many ways\x01",
            "to acquire that experience you need.\x02\x03",
            "Now that you're in the CGF, continue to apply\x01",
            "yourselves daily in order to protect the citizenry\x01",
            "and Crossbell as a whole.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x1A, 0x1)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x1)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x1)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x0)
    SetChrSubChip(0x1D, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    NpcTalk(
        0x1B,
        "CGF Guardsmen",
        "#N#4SYes, ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11P#2002FI like your enthusiasm.\x02\x03",
            "As a reward, I'll make special, independent\x01",
            "training regimens for each and every one of\x01",
            "you, after you return to your posts.\x02\x03",
            "#2004FUntil your official assignments have been\x01",
            "decided, you'll stick to them daily. Are there\x01",
            "any questions?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "CGF Guardsmen",
        "#N(Eek!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FThey're no match for her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI expected no less from the most capable\x01",
            "woman in the CGF.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7935")

    label("loc_6B93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_72C7")
    SetChrPos(0x18, -21000, 0, 23700, 180)
    SetChrPos(0x19, -17000, 0, 22500, 270)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x1A, 0x26)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x26)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x102, 0x2A)
    SetChrSubChip(0x102, 0x3)
    SetChrChipByIndex(0x103, 0x2B)
    SetChrSubChip(0x103, 0x3)
    SetChrChipByIndex(0x104, 0x2C)
    SetChrSubChip(0x104, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x19,
        "#11P#2001F#4S#NThat's enough!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12P#0010FOuch... Looks like we couldn't manage\x01",
            "to keep up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0306FOnce Noel took the reins, everyone\x01",
            "else's skill shot up.\x02\x03",
            "#0300FHeh. Guess that's why they call her the\x01",
            "hope of the CGF or whatever it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5P#0502FHaha, that's not true. You four were\x01",
            "just as strong, if not stronger.\x02\x03",
            "#0504FIf we slacked off for even a second,\x01",
            "we would have been destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PWe might have won...but it wasn't\x01",
            "really our own strength that did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5PYeah. We only won because of the sergeant major.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x1C, 300)

    ChrTalk(
        0x19,
        (
            "#11P#2001FInteresting. It seems like you all recognize\x01",
            "the underlying problem here.\x02\x03",
            "This is the strength of people who have fought\x01",
            "the mafia and monsters in live combat.\x02\x03",
            "#2003FIt's clear that your experience is nowhere near\x01",
            "sufficient as things stand.\x02\x03",
            "And to make matters worse, the Crossbell\x01",
            "Guardian Force isn't allowed to conduct any\x01",
            "large-scale training operations...\x02\x03",
            "#2001FBut, despite all that, there are still many ways\x01",
            "to acquire that experience you need.\x02\x03",
            "Now that you're in the CGF, continue to apply\x01",
            "yourselves daily in order to protect the citizenry\x01",
            "and Crossbell as a whole.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x1A, 0x1)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x1)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x1)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x0)
    SetChrSubChip(0x1D, 0x0)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    NpcTalk(
        0x1B,
        "CGF Guardsmen",
        "#N#4SYes, ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11P#2002FI like your enthusiasm.\x02\x03",
            "As a reward, I'll make special, independent\x01",
            "training regimens for each and every one of\x01",
            "you, after you return to your posts.\x02\x03",
            "#2004FUntil your official assignments have been\x01",
            "decided, you'll stick to them daily. Is there\x01",
            "any questions?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "CGF Guardsmen",
        "#N(Eek!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FThey're no match for her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI expected no less from the most capable\x01",
            "woman in the CGF.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Jump("loc_7935")

    label("loc_72C7")

    SetChrChipByIndex(0x1A, 0x26)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x26)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x102, 0x2A)
    SetChrSubChip(0x102, 0x3)
    SetChrChipByIndex(0x103, 0x2B)
    SetChrSubChip(0x103, 0x3)
    SetChrChipByIndex(0x104, 0x2C)
    SetChrSubChip(0x104, 0x3)
    SetChrPos(0x18, -17000, 0, 22500, 270)
    SetChrPos(0x19, -16500, 0, 21500, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x18,
        "#5P#0507F#4S#NThat's enough!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12P#0010FOuch... Looks like we couldn't manage\x01",
            "to keep up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0310FTch. We underestimated them.\x02\x03",
            "#0306FBein' beaten by a bunch of newbies\x01",
            "feels pretty damn lame, man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PW-We won? I wasn't expecting the\x01",
            "SSS to be this strong, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PWeren't WE supposed to be the\x01",
            "combat elites...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5PYou're telling me. I'm beat...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x1C, 300)

    ChrTalk(
        0x19,
        (
            "#11P#2001FInteresting. It seems like you all recognize\x01",
            "the underlying problem here.\x02\x03",
            "This is the strength of people who have fought\x01",
            "the mafia and monsters in live combat.\x02\x03",
            "#2003FIt's clear that your experience is nowhere near\x01",
            "sufficient as things stand.\x02\x03",
            "And to make matters worse, the Crossbell\x01",
            "Guardian Force isn't allowed to conduct any\x01",
            "large-scale training operations...\x02\x03",
            "#2001FBut, despite all that, there are still many ways\x01",
            "to acquire that experience you need.\x02\x03",
            "Now that you're in the CGF, continue to apply\x01",
            "yourselves daily in order to protect the citizenry\x01",
            "and Crossbell as a whole.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x1A, 0x1)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x1)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x1)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x0)
    SetChrSubChip(0x1D, 0x0)
    Sound(531, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    NpcTalk(
        0x1B,
        "CGF Guardsmen",
        "#N#4SYes, ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11P#2002FI like your enthusiasm.\x02\x03",
            "As a reward, I'll make special, independent\x01",
            "training regimens for each and every one of\x01",
            "you, after you return to your posts.\x02\x03",
            "#2004FUntil your official assignments have been\x01",
            "decided, you'll stick to them daily. Is there\x01",
            "any questions?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "CGF Guardsmen",
        "#N(Eek!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FThey're no match for her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI expected no less from the most capable\x01",
            "woman in the CGF.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    label("loc_7935")

    TurnDirection(0x19, 0x101, 300)

    ChrTalk(
        0x19,
        (
            "#11P#2002FGood work, you four.\x02\x03",
            "Thanks to your efforts, I think this ended\x01",
            "up being a worthwhile training session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0012FHaha, I'm glad you think so. Honestly,\x01",
            "I'm a bit worn out now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11P#2004FThen let's not stand and talk.\x01",
            "Would you mind coming with me to the\x01",
            "commander's office?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FNot at all.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x5C, 0)
    NewScene("t2520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_6324 end

    def Function_33_7A94(): pass

    label("Function_33_7A94")

    EventBegin(0x0)
    OP_4B(0x1F, 0xFF)
    ClearMapObjFlags(0x5, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-31410, 1000, 22290, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18050, 0)
    SetChrPos(0x101, -32500, 0, 21500, 0)
    SetChrPos(0x102, -31000, 0, 21500, 0)
    SetChrPos(0x103, -32500, 0, 20000, 0)
    SetChrPos(0x104, -31000, 0, 20000, 0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    OP_93(0x1F, 0xB4, 0x1F4)

    ChrTalk(
        0x1F,
        "#5POh, you folks heading back, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYes. Sorry to keep you waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#5PYeah, well, the other passengers are\x01",
            "already on board. Hurry up and get in.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7BE2():
        OP_95(0xFE, -27390, 600, 24150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_7BE2)
    Sleep(1500)

    def lambda_7BFF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_7BFF)
    WaitChrThread(0x1F, 1)
    WaitChrThread(0x1F, 2)

    ChrTalk(
        0x101,
        (
            "#5P#0001FLike I said earlier, I plan to uncover\x01",
            "the identity of the counterfeit dealer\x01",
            "on the bus ride.\x02\x03",
            "Let's think through things and figure it\x01",
            "out before we reach Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FGot'cha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FWe are in a race against time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#0100FNo time to waste, then. Shall we?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-27170, 1000, 24690, 0)
    MoveCamera(68, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19950, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)
    Sound(463, 0, 100, 0)
    OP_79(0x5)
    Sleep(500)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sound(470, 0, 100, 0)
    OP_79(0x5)
    Sound(473, 0, 100, 0)
    OP_68(-26730, 1000, -2100, 6000)
    MoveCamera(37, 21, 0, 6000)
    OP_6E(510, 0)
    SetCameraDistance(23500, 6000)
    OP_71(0x5, 0xB4, 0x79, 0x0, 0x20)

    def lambda_7E26():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF92A0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7E26)
    WaitChrThread(0x1E, 1)
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x5)
    OP_68(-49120, 1000, -60, 5000)
    MoveCamera(45, 21, 0, 5000)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    Sound(467, 0, 100, 0)
    Sound(470, 0, 100, 0)

    def lambda_7E99():
        OP_9E(0xFE, 0xFFFF865C, 0xFFFFF060, 0xFFFEA070, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7E99)
    WaitChrThread(0x1E, 1)
    Sound(465, 0, 100, 0)

    def lambda_7EBE():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7EBE)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 3)
    NewScene("e0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_7A94 end

    def Function_34_7EF4(): pass

    label("Function_34_7EF4")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Calvard Republic Border\x01",
            "       Tangram Gate\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_34_7EF4 end

    def Function_35_7F58(): pass

    label("Function_35_7F58")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7FA8")

    ChrTalk(
        0x101,
        (
            "#0001FThe bus stop was over in the\x01",
            "parking lot, wasn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8016")

    label("loc_7FA8")


    ChrTalk(
        0x101,
        (
            "#0001FThe bus stop was over in the parking lot,\x01",
            "wasn't it?\x02\x03",
            "If we don't hurry, we might miss the bus.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_8016")

    SetChrPos(0x0, -45520, 0, -30, 90)
    EventEnd(0x5)
    Return()

    # Function_35_7F58 end

    SaveToFile()

Try(main)
