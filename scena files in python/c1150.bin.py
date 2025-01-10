from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1150.bin",                # FileName
        "c1150",                    # MapName
        "c1150",                    # Location
        0x0018,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 5000, 1500, 0, 0, 1, 24, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1150",                  # 0
        "Receptionist Rebecca",   # 1
        "Receptionist Fran",      # 2
        "Inspector Donovan",      # 3
        "Detective Raymond",      # 4
        "Officer Franz",          # 5
        "Officer",                # 6
        "Chief Jolich",           # 7
        "Officer Kate",           # 8
        "Detective Emma",         # 9
        "Chief Sergei",           # 10
        "Vice Commissioner Pierre",# 11
        "Officer",                # 12
        "Officer",                # 13
        "Officer",                # 14
        "イス",                   # 15
        "イス",                   # 16
        "イス",                   # 17
        "イス",                   # 18
        "イス",                   # 19
        "イス",                   # 20
    ))

    AddCharChip((
        "chr/ch30400.itc",                   # 00
        "chr/ch06900.itc",                   # 01
        "chr/ch30300.itc",                   # 02
        "chr/ch30200.itc",                   # 03
        "chr/ch30000.itc",                   # 04
        "chr/ch30100.itc",                   # 05
        "chr/ch30100.itc",                   # 06
        "chr/ch02500.itc",                   # 07
        "chr/ch30600.itc",                   # 08
        "chr/ch30500.itc",                   # 09
        "chr/ch30002.itc",                   # 0A
        "chr/ch06400.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-100,    0,       15399,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(3000,    0,       15930,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-60700,  29,      21360,   135,  389,  0x0, 0,   4,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   4,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-58049,  0,       15899,   90,   261,  0x0, 0,   6,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-59229,  29,      21360,   270,  389,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-125379, 0,       19520,   0,    389,  0x0, 0,   9,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-11039,  0,       13810,   90,   389,  0x0, 0,   7,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   11,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(-60659,  180,     20159,   180,  469,  0x0, 0,   10,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(-60610,  129,     15789,   0,    469,  0x0, 0,   10,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(-64050,  129,     15850,   0,    469,  0x0, 0,   10,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 47,  -9.199999809265137,    10.0,                  -0.5,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.599999904632568,     -2.5,                  0.10000000149011612,   1.0])
    DeclEvent(0x0000, 0, 48,  -12.699999809265137,   19.8700008392334,      -0.5,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142984867096,    0.0,                   4.233333587646484,     -9.9350004196167,      0.1428571492433548,    1.0])

    DeclActor(-100,    0,       14400,   1100,    -100,    1500,    15400,   0x007E, 0,  5,  0x0000)
    DeclActor(2770,    0,       14280,   1000,    3000,    1500,    15930,   0x007E, 0,  8,  0x0000)
    DeclActor(1970,    0,       14310,   1000,    1970,    1500,    15610,   0x007E, 0,  8,  0x0000)
    DeclActor(1120,    0,       14070,   1000,    900,     1500,    15400,   0x007E, 0,  8,  0x0000)
    DeclActor(-9850,   0,       16000,   1000,    -9850,   1500,    16000,   0x007C, 0,  49, 0x0000)
    DeclActor(-9850,   0,       13750,   1000,    -9850,   1500,    13750,   0x007C, 0,  49, 0x0000)

    ScpFunction((
        "Function_0_59C",          # 00, 0
        "Function_1_654",          # 01, 1
        "Function_2_67F",          # 02, 2
        "Function_3_6D2",          # 03, 3
        "Function_4_C11",          # 04, 4
        "Function_5_D66",          # 05, 5
        "Function_6_D7B",          # 06, 6
        "Function_7_1890",         # 07, 7
        "Function_8_405B",         # 08, 8
        "Function_9_405F",         # 09, 9
        "Function_10_7755",        # 0A, 10
        "Function_11_7C98",        # 0B, 11
        "Function_12_8055",        # 0C, 12
        "Function_13_957D",        # 0D, 13
        "Function_14_A6C0",        # 0E, 14
        "Function_15_A87B",        # 0F, 15
        "Function_16_AB20",        # 10, 16
        "Function_17_AD61",        # 11, 17
        "Function_18_B0DB",        # 12, 18
        "Function_19_BEA0",        # 13, 19
        "Function_20_C153",        # 14, 20
        "Function_21_CA19",        # 15, 21
        "Function_22_D039",        # 16, 22
        "Function_23_D171",        # 17, 23
        "Function_24_D36B",        # 18, 24
        "Function_25_D4D0",        # 19, 25
        "Function_26_D633",        # 1A, 26
        "Function_27_D77D",        # 1B, 27
        "Function_28_D9C5",        # 1C, 28
        "Function_29_E4B5",        # 1D, 29
        "Function_30_F422",        # 1E, 30
        "Function_31_F475",        # 1F, 31
        "Function_32_F500",        # 20, 32
        "Function_33_1071C",       # 21, 33
        "Function_34_10940",       # 22, 34
        "Function_35_12E85",       # 23, 35
        "Function_36_12E95",       # 24, 36
        "Function_37_12ED2",       # 25, 37
        "Function_38_12F1C",       # 26, 38
        "Function_39_12F67",       # 27, 39
        "Function_40_1301D",       # 28, 40
        "Function_41_14ADE",       # 29, 41
        "Function_42_14BB4",       # 2A, 42
        "Function_43_14C5F",       # 2B, 43
        "Function_44_15C79",       # 2C, 44
        "Function_45_16578",       # 2D, 45
        "Function_46_176DA",       # 2E, 46
        "Function_47_177B7",       # 2F, 47
        "Function_48_17894",       # 30, 48
        "Function_49_182E9",       # 31, 49
    ))


    def Function_0_59C(): pass

    label("Function_0_59C")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_5DC"),
        (1, "loc_5E8"),
        (2, "loc_5F4"),
        (3, "loc_600"),
        (4, "loc_60C"),
        (5, "loc_618"),
        (6, "loc_624"),
        (SWITCH_DEFAULT, "loc_630"),
    )


    label("loc_5DC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_5E8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_5F4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_600")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_60C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_618")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_624")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_630")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_63C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_653")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_653")

    Return()

    # Function_0_59C end

    def Function_1_654(): pass

    label("Function_1_654")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67E")
    OP_94(0xFE, 0xFFFF8508, 0x24CC, 0xFFFF93C2, 0x288C, 0x3E8)
    Sleep(300)
    Jump("Function_1_654")

    label("loc_67E")

    Return()

    # Function_1_654 end

    def Function_2_67F(): pass

    label("Function_2_67F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D1")
    OP_95(0x12, -57300, 0, 20000, 2000, 0x0)
    Sleep(500)
    OP_93(0x12, 0xB4, 0x2EE)
    Sleep(500)
    OP_95(0x12, -57300, 0, 16000, 2000, 0x0)
    Sleep(500)
    OP_93(0x12, 0x0, 0x2EE)
    Sleep(500)
    Jump("Function_2_67F")

    label("loc_6D1")

    Return()

    # Function_2_67F end

    def Function_3_6D2(): pass

    label("Function_3_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_700")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xD, -125380, 0, 19520, 0)
    SetChrFlags(0xE, 0x80)
    Jump("loc_BD9")

    label("loc_700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_76B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72B")
    OP_93(0x8, 0x5A, 0x0)
    SetChrPos(0x9, 1970, 0, 15610, 270)

    label("loc_72B")

    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xE, -57640, 0, 18750, 270)
    SetChrPos(0xD, -57640, 0, 17260, 270)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_BD9")

    label("loc_76B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7B1")
    OP_93(0x8, 0x5A, 0x0)
    SetChrPos(0x9, 1970, 0, 15610, 270)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xD, -58050, 0, 15900, 90)
    SetChrFlags(0xE, 0x80)
    Jump("loc_BD9")

    label("loc_7B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7F7")
    SetChrPos(0xA, -11040, 0, 13810, 90)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    SetChrPos(0xD, -58050, 0, 15900, 90)
    SetChrFlags(0xE, 0x80)
    Jump("loc_BD9")

    label("loc_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_83B")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, -12850, 0, 7690, 90)
    SetChrPos(0xB, -11260, 0, 7690, 270)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_BD9")

    label("loc_83B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_897")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xD, -123350, 0, 19180, 0)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_892")
    SetChrPos(0x12, -57300, 0, 18000, 0)
    BeginChrThread(0x12, 0, 0, 2)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x12, 0x80)

    label("loc_892")

    Jump("loc_BD9")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_916")
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    SetChrPos(0xD, -29870, 0, 9900, 90)
    BeginChrThread(0xD, 0, 0, 1)
    SetChrPos(0xE, -11040, 0, 13810, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_911")
    SetChrPos(0x12, -57300, 0, 18000, 0)
    BeginChrThread(0x12, 0, 0, 2)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)

    label("loc_911")

    Jump("loc_BD9")

    label("loc_916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_94A")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xD, -57630, 0, 17300, 135)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 0)
    Jump("loc_BD9")

    label("loc_94A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_990")
    SetChrPos(0xA, -125380, 0, 19520, 0)
    SetChrPos(0xB, -123490, 0, 18220, 180)
    SetChrPos(0xD, -58050, 0, 15900, 90)
    SetChrFlags(0xE, 0x80)
    Jump("loc_BD9")

    label("loc_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9D6")
    SetChrPos(0xA, -11040, 0, 13810, 90)
    SetChrPos(0xB, -12290, 0, 12530, 45)
    SetChrPos(0xD, -125380, 0, 19520, 0)
    SetChrFlags(0xE, 0x80)
    Jump("loc_BD9")

    label("loc_9D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A32")
    SetChrPos(0xA, -121660, 0, 18190, 90)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    SetChrPos(0xD, -58050, 0, 15900, 180)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -58050, 30, 14700, 0)
    Jump("loc_BD9")

    label("loc_A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A9F")
    SetChrPos(0xA, -125380, 0, 19520, 0)
    SetChrPos(0xB, -11040, 0, 13810, 90)
    SetChrPos(0xE, -57420, 0, 18000, 270)
    SetChrPos(0xF, -57270, 0, 16580, 270)
    SetChrPos(0xD, -59320, 30, 21250, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_BD9")

    label("loc_A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_AEF")
    SetChrPos(0xA, -125380, 0, 19520, 0)
    SetChrPos(0xB, -11040, 0, 13810, 90)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -56940, 0, 19650, 90)
    Jump("loc_BD9")

    label("loc_AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_B91")
    SetChrPos(0xA, -126060, 0, 19340, 90)
    SetChrPos(0xB, -124880, 0, 19200, 270)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xF, -57420, 0, 16239, 90)
    SetChrPos(0xD, -57020, 0, 17260, 135)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B75")
    SetChrPos(0x9, 900, 0, 15400, 180)
    Jump("loc_B8C")

    label("loc_B75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8C")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_B8C")

    Jump("loc_BD9")

    label("loc_B91")

    SetChrPos(0x9, -100, 0, 15400, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)

    label("loc_BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_BED")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 33)
    Jump("loc_C10")

    label("loc_BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_C01")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 40)
    Jump("loc_C10")

    label("loc_C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_C10")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 31)

    label("loc_C10")

    Return()

    # Function_3_6D2 end

    def Function_4_C11(): pass

    label("Function_4_C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 2)), scpexpr(EXPR_END)), "loc_C23")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C23")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C39")
    Jump("loc_C8A")

    label("loc_C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C54")
    OP_65(0x1, 0x1)
    OP_66(0x2, 0x1)

    label("loc_C54")

    Jump("loc_C8A")

    label("loc_C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C6F")
    OP_65(0x1, 0x1)
    OP_66(0x2, 0x1)
    Jump("loc_C8A")

    label("loc_C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C7D")
    Jump("loc_C8A")

    label("loc_C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C8A")
    OP_65(0x1, 0x1)

    label("loc_C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_CB8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB3")
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_CB3")

    Jump("loc_CC0")

    label("loc_CB8")

    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)

    label("loc_CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE1")
    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)

    label("loc_CE1")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D21")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_D38")

    label("loc_D21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D38")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_D38")

    label("loc_D38")

    OP_1B(0x0, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5A")
    OP_1B(0x0, 0x0, 0x2E)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_D5A")

    ModifyEventFlags(1, 1, 0x80)
    ClearMapObjFlags(0x2, 0x10)
    Return()

    # Function_4_C11 end

    def Function_5_D66(): pass

    label("Function_5_D66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_D77")
    Call(0, 6)
    Jump("loc_D7A")

    label("loc_D77")

    Call(0, 9)

    label("loc_D7A")

    Return()

    # Function_5_D66 end

    def Function_6_D7B(): pass

    label("Function_6_D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D95")
    Call(0, 43)
    Return()

    label("loc_D95")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_F4B")

    ChrTalk(
        0x8,
        "Good work out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Were you able to confirm the additional\x01",
            "support requests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FYes, we were.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWe plan on tackling the extermination\x01",
            "request right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "The extermination, hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The monster seems to be located at the end\x01",
            "of the Geofront's A Sector.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's also been reports of an influx of\x01",
            "monsters lurking down there.\x01",
            "You should proceed with caution.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 1)
    Jump("loc_1002")

    label("loc_F4B")


    ChrTalk(
        0x8,
        (
            "All right, I believe that should wrap up\x01",
            "the explanation on support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When you return to the SSS building, try pressing\x01",
            "the 'Report' option on your terminal screen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1002")


    ChrTalk(
        0x8,
        (
            "Allow me to give you a short explanation about\x01",
            "the support request workflow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is anything you want to check on, please\x01",
            "don't hesitate to ask me, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4B, 0)
    Jump("loc_15B6")

    label("loc_10B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15B6")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1109")

    ChrTalk(
        0x8,
        "Thank you so much for handling the extermination.\x02",
    )

    CloseMessageWindow()

    label("loc_1109")


    ChrTalk(
        0x8,
        (
            "Oh, that's right. Did you hear the news? The CPD\x01",
            "is currently conducting an information survey about\x01",
            "local monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FReally? What exactly does that entail?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, it starts with your Combat Notebook's monster\x01",
            "entries. You've been keeping it up-to-date, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once you defeat a monster, officers are supposed\x01",
            "to record their information in their notebooks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The survey's simple. After you've recorded\x01",
            "enough monster data, come show it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That information will be conglomerated and become\x01",
            "the foundation for our new security procedures. It's\x01",
            "quite the smart idea, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13E6")

    ChrTalk(
        0x102,
        (
            "#0100FI can't disagree. I'm glad to see that we're thinking\x01",
            "things out before accidents happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E5")

    label("loc_13E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1472")

    ChrTalk(
        0x103,
        (
            "#0200FIndeed. The amount of foresight demonstrated\x01",
            "by the department is admirable. Not to mention,\x01",
            "unprecedented.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E5")

    label("loc_1472")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14E5")

    ChrTalk(
        0x104,
        (
            "#0300FWell, look at us, takin' action for a change. That\x01",
            "in itself is pretty damn reassuring.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E5")


    ChrTalk(
        0x8,
        "Of course. After all, this is to protect the citizenry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah, I nearly forgot! Whenever you supply me with\x01",
            "information, I'll give you a small bonus, too.\x01",
            "Make sure to stop by when you can, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 2)
    SetScenarioFlags(0x2, 0)

    label("loc_15B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16AA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A5")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                            # 0
            "Ask About Support Requests\x01",      # 1
            "Leave\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1636")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_163D")

    label("loc_1636")

    OP_60(0x0)
    OP_5A()
    Sleep(150)

    label("loc_163D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1670")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 5)
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x1, 7)
    Call(0, 44)
    Sleep(150)
    Jump("loc_16A0")

    label("loc_1670")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1684")
    Jump("loc_16A0")

    label("loc_1684")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_16A0")

    Jump("loc_15CA")

    label("loc_16A5")

    Jump("loc_188C")

    label("loc_16AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D2")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                            # 0
            "Ask About Support Requests\x01",      # 1
            "Show Combat Notebook\x01",            # 2
            "Leave\x01",                           # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_173F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_1746")

    label("loc_173F")

    OP_60(0x0)
    OP_5A()
    Sleep(150)

    label("loc_1746")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1779")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 5)
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x1, 7)
    Call(0, 44)
    Sleep(150)
    Jump("loc_17CD")

    label("loc_1779")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x2, 1)
    Call(0, 45)
    Jump("loc_17CD")

    label("loc_179D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17B1")
    Jump("loc_17CD")

    label("loc_17B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_17CD")

    Jump("loc_16BE")

    label("loc_17D2")

    Jump("loc_188C")

    label("loc_17D7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_188C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                      # 0
            "Show Combat Notebook\x01",      # 1
            "Leave\x01",                     # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1857")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x2, 1)
    Call(0, 45)
    Jump("loc_1887")

    label("loc_1857")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_186B")
    Jump("loc_1887")

    label("loc_186B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1887")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_1887")

    Jump("loc_17E1")

    label("loc_188C")

    TalkEnd(0x8)
    Return()

    # Function_6_D7B end

    def Function_7_1890(): pass

    label("Function_7_1890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_19B1")

    ChrTalk(
        0x8,
        (
            "Once you have filled out a certain amount of entries\x01",
            "in your Combat Notebook, please bring it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'll be using the information you gather to put\x01",
            "more effective safety procedures in place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You'll even get a small bonus, so please stop by\x01",
            "whenever you can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_405A")

    label("loc_19B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1B39")

    ChrTalk(
        0x8,
        (
            "Dudley just stormed into the lobby with\x01",
            "a serious look on his face. It was clear\x01",
            "as day that something happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The situation might be getting worse than\x01",
            "the higher-ups expected...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please try to be careful out there. I don't\x01",
            "want anything to happen to our officers.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B34")

    ChrTalk(
        0x101,
        "#0000FDon't worry about us, Rebecca.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYeah! We've got this handled.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B34")

    Jump("loc_405A")

    label("loc_1B39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1E15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB0")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Hmm? Now here's a pair that you don't see\x01",
            "very often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYeah, well... It wasn't exactly planned.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0603FThe circumstances demanded it.\x02\x03",
            "#0600FIs there any news on the airport lockdown?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, actually. I just received a call from Emma\x01",
            "a few minutes ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To be frank, I wish you would have asked for\x01",
            "a debriefing a little bit more quickly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, you seem to have your hands full with work,\x01",
            "so I'll tone down the snark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#0603FMuch appreciated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(Wow, Dudley is being pushed around...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100F(This is surely a rare sight to behold.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E10")

    label("loc_1DB0")


    ChrTalk(
        0x8,
        "Let us handle the airport lockdown.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Keep up the good work with your\x01",
            "duties, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E10")

    Jump("loc_405A")

    label("loc_1E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1EE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E30")
    Call(0, 11)
    Jump("loc_1EE0")

    label("loc_1E30")


    ChrTalk(
        0x8,
        (
            "They've apparently called in people from\x01",
            "the Second Investigative Division this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The First Division tends to work in secrecy,\x01",
            "but they occasionally collaborate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE0")

    Jump("loc_405A")

    label("loc_1EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1FFB")

    ChrTalk(
        0x8,
        (
            "We've had a few inquiries come in about the\x01",
            "firefight that took place in the Harbor District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can only imagine the flood of questions\x01",
            "we'll get once the press learns more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'll need to come up with countermeasures\x01",
            "to handle the oncoming barrage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_405A")

    label("loc_1FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_223B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2161")

    ChrTalk(
        0x8,
        "Oh, you're all here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The First Division is working their hardest\x01",
            "investigating the raid on Heiyue's office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "They've all been out there the whole morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FO-Oh, I see.\x01",
            "Wow, they're really on the ball.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FI don't think anyone's outdoin' the First Division\x01",
            "on this kinda investigation any time soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2236")

    label("loc_2161")


    ChrTalk(
        0x8,
        "The First Division is working their hardest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They went out into the field the moment\x01",
            "their morning meeting let out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F(I hope the SSS can one day reach the\x01",
            "First Division's level of diligence.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2236")

    Jump("loc_405A")

    label("loc_223B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2669")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2328")

    ChrTalk(
        0x8,
        (
            "Fran came back to work on time, which\x01",
            "I can't help but feel a little disappointed by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Imagine the interesting turn of events we\x01",
            "would have had on our hands if she and\x01",
            "that tourist actually hit it off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2664")

    label("loc_2328")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_23C7")

    ChrTalk(
        0x8,
        "It sounded like they had an...intriguing time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Don't you worry. I'll cover for her, so\x01",
            "Fran will have plenty of time on her break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2664")

    label("loc_23C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25AF")

    ChrTalk(
        0x8,
        "Good afternoon, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Did you guys know that we've been having\x01",
            "more citizens come to the CPD for\x01",
            "consultations lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I have an inkling that this is all thanks to you\x01",
            "grinding out one request after another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWe'd be elated if that were truly the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, no need to be modest! I'm sure it is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Keep up the good work, everyone.\x01",
            "I'm rooting for my ace detectives!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309F(Oh... Such sweet words of praise from\x01",
            "my dear Rebecca!)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2664")

    label("loc_25AF")


    ChrTalk(
        0x8,
        (
            "We've been having more citizens come to\x01",
            "the CPD for consultations lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heehee. I have an inkling that this is all thanks\x01",
            "to you grinding out one request after another.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2664")

    Jump("loc_405A")

    label("loc_2669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2910")

    ChrTalk(
        0x8,
        "Oh, it's good to see you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1105FWooow, you're really pretty, miss!\x02\x03",
            "#1111FUhh, what was that word again?\x01",
            "Oh, yeah, you're alluring!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 500)

    ChrTalk(
        0x8,
        "Oh, you flatter me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        (
            "You're just as lovely as the rumors\x01",
            "say you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha... Yeah, she's great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've come to an informal settlement with\x01",
            "Revache regarding the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That doesn't mean you can rest easy, though.\x01",
            "You'd better watch each other's backs well, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYeah, got it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_289B")

    ChrTalk(
        0x102,
        "#0101FWe'll be sure to take extra care.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2908")

    label("loc_289B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_28BB")

    ChrTalk(
        0x103,
        "#0200FRoger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2908")

    label("loc_28BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2908")

    ChrTalk(
        0x104,
        (
            "#0300FDon't you worry about a thing.\x01",
            "We'll keep her protected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2908")

    SetScenarioFlags(0xB1, 1)
    Jump("loc_2B17")

    label("loc_2910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A38")

    ChrTalk(
        0x8,
        (
            "By the way, a monster needing extermination\x01",
            "appeared in Sector A2 of the Geofront today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I haven't been able to send the info on it yet,\x01",
            "as our terminal is under maintenance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's fairly dangerous, so I'd really appreciate\x01",
            "it if you were to take care of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x25, 0x4, 0x2)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2B17")

    label("loc_2A38")


    ChrTalk(
        0x8,
        (
            "The orbal terminal's under maintenance,\x01",
            "and Fran's not in today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She's been working without break ever\x01",
            "since the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope she can shake off some of\x01",
            "that fatigue she's been building up.\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)

    label("loc_2B17")

    Jump("loc_405A")

    label("loc_2B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2C69")

    ChrTalk(
        0x8,
        (
            "We had three separate meetings to discuss\x01",
            "security during the Anniversary Festival today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Namely, patrolling the city during the festival\x01",
            "and security detail for the reception hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We need to remain especially vigilant during\x01",
            "the opening ceremony, as we'll have many\x01",
            "VIPs coming from foreign countries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_405A")

    label("loc_2C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2DD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D52")

    ChrTalk(
        0x8,
        "The First Division acts in complete secrecy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They hardly ever reveal the nature\x01",
            "of their investigations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, when you think about the work they do,\x01",
            "they don't really have much of a choice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2DCE")

    label("loc_2D52")


    ChrTalk(
        0x8,
        "The First Division acts in complete secrecy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They seem level-headed, but I doubt\x01",
            "that they have any other option.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCE")

    Jump("loc_405A")

    label("loc_2DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2FD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F11")

    ChrTalk(
        0x8,
        (
            "Fran and I have had a lot of extra work to deal\x01",
            "with due to the approaching Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There are all sorts of approvals that have to\x01",
            "be submitted--whether it's for food stalls,\x01",
            "decorations, or tourist attractions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Things are going to get really busy around here...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2FCF")

    label("loc_2F11")


    ChrTalk(
        0x8,
        (
            "Fran and I have had a lot of extra work to deal\x01",
            "with due to the approaching Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For as long as I can remember, this has always\x01",
            "been the busiest time of the year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FCF")

    Jump("loc_405A")

    label("loc_2FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3253")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3186")

    ChrTalk(
        0x8,
        "Oh, Elie and Tio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Thank you for the help earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FIt was strangely satisfying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FReading over those old cases was much more\x01",
            "informative than I was anticipating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'm glad it wasn't too boring, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've been steadily building a database\x01",
            "ever since they decided to place an orbal\x01",
            "terminal at the station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Can I count on you to help me again\x01",
            "when the time comes?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_324E")

    label("loc_3186")


    ChrTalk(
        0x8,
        (
            "They decided to place an orbal terminal\x01",
            "at the police station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've been steadily building a database\x01",
            "of all of our old cases.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Can I count on you to help me again\x01",
            "when the time comes?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_324E")

    Jump("loc_405A")

    label("loc_3253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3452")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33BD")

    ChrTalk(
        0x8,
        (
            "Detective Raymond from the Second Division\x01",
            "is an interesting man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He always stops by here to converse with me\x01",
            "before he gets to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I could tell he was pushing his luck\x01",
            "this morning. Inspector Donovan had\x01",
            "to come here and drag him to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(I'm not surprised a beauty like Rebecca\x01",
            "is popular with the men.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_344D")

    label("loc_33BD")


    ChrTalk(
        0x8,
        (
            "Detective Raymond from the Second Division\x01",
            "is an interesting man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He always stops by here to converse with me\x01",
            "before he gets to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_344D")

    Jump("loc_405A")

    label("loc_3452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_36AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_361B")

    ChrTalk(
        0x8,
        (
            "Hi, guys. It's Crime Prevention Week\x01",
            "at headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd like to remind you all to confirm that your\x01",
            "doors and windows are locked before leaving\x01",
            "your home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FWhat's Crime Prevention Week?\x01",
            "This is the first time I've ever heard of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "*sigh* Figures.\x01",
            "I can't say I'm surprised that you're unaware.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It'd be nice if the higher-ups allocated a bigger\x01",
            "budget towards awareness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_36A7")

    label("loc_361B")


    ChrTalk(
        0x8,
        (
            "It's Crime Prevention Week at the\x01",
            "headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'd like for the populace to be more mindful\x01",
            "of locking their doors and windows.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36A7")

    Jump("loc_405A")

    label("loc_36AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3AB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A6")

    ChrTalk(
        0x8,
        (
            "Deputy Commander Baelz was here\x01",
            "not too long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She's from the Guardian Force, but she comes\x01",
            "here from time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FI never really thought about it, but the CPD and CGF\x01",
            "truly are separate chains of command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You're not wrong. Though, the official stance is that\x01",
            "we're both under the umbrella of the 'state police.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The nature of the CGF's work is similar to\x01",
            "that of an army's, so their chain of command\x01",
            "is structured uniquely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The commissioner of the CPD and the commander\x01",
            "of the CGF may hold the same rank, but they act\x01",
            "independently of each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FYeah, they're pretty much different organizations.\x02\x03",
            "#0300FYou get the occasional rare dude like me hoppin'\x01",
            "from one place to the other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3AB4")

    label("loc_39A6")


    ChrTalk(
        0x8,
        (
            "The official stance is that the CGF and the CPD\x01",
            "are the same organization, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Considering they're headed by different people,\x01",
            "they may as well be separate entities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The only person from the CGF that keeps in\x01",
            "contact with us is Deputy Commander Baelz.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AB4")

    Jump("loc_405A")

    label("loc_3AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3B2D")

    ChrTalk(
        0x8,
        (
            "We've got a situation on our hands in the\x01",
            "Downtown District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Stay safe out there, everyone.\x02",
    )

    CloseMessageWindow()
    Jump("loc_405A")

    label("loc_3B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_405A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3CAD")

    ChrTalk(
        0x8,
        (
            "I heard you guys took care of the\x01",
            "wanted monster in the Geofront.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Word of wanted monsters reaches the\x01",
            "Bracer Guild, too, so you don't always\x01",
            "have to be the ones to exterminate them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In fact, they can get pretty tough.\x01",
            "Exterminating all of them wouldn't be easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, if you ever have the time, feel\x01",
            "free to take on as many as you'd like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_405A")

    label("loc_3CAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_3F20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E62")

    ChrTalk(
        0x8,
        "Good work out there, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Were you able to confirm the additional\x01",
            "support requests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FYes, we were.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWe plan on tackling the extermination\x01",
            "request right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "The extermination, hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The monster seems to be located at the end\x01",
            "of the Geofront's A Sector.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's also been reports of an influx of\x01",
            "monsters lurking down there.\x01",
            "You should proceed with caution.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 1)
    Jump("loc_3F1B")

    label("loc_3E62")


    ChrTalk(
        0x8,
        (
            "The monster seems to be located at the end\x01",
            "of the Geofront's A Sector.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's also been reports of an influx of\x01",
            "monsters lurking down there.\x01",
            "You should proceed with caution.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F1B")

    Jump("loc_405A")

    label("loc_3F20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_405A")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0x8,
        (
            "All right, I believe that should wrap up the\x01",
            "explanation on support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, then, once you return to the SSS, try pressing\x01",
            "the 'Report' option on your terminal screen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1900FHeehee. I'll be handling any incoming\x01",
            "requests for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_405A")

    label("loc_405A")

    Return()

    # Function_7_1890 end

    def Function_8_405B(): pass

    label("Function_8_405B")

    Call(0, 9)
    Return()

    # Function_8_405B end

    def Function_9_405F(): pass

    label("Function_9_405F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4071")
    Call(0, 34)
    Return()

    label("loc_4071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_408B")
    Call(0, 43)
    Return()

    label("loc_408B")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4424")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4359")
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#1905FOh... Are you all going somewhere?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FYeah, we're headin' out to St. Ursula\x01",
            "Medical College for a lil' while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FYou look exhausted, Fran.\x01",
            "Are you okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1900FOh, well...\x02\x03",
            "I've had people screaming at me on the phone\x01",
            "over the lockdown all day.\x02\x03",
            "#1903FThere was supposedly a bomb threat, but it\x01",
            "ended up being false. What a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FI'm sorry you had to deal with that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1909FThat's okay. All I need is a bit of\x01",
            "rest and I'll be good to go again!\x02\x03",
            "#1900FDon't let my fatigue prevent you from\x01",
            "contacting me for help, okay?\x02\x03",
            "I, Fran Seeker, will support you\x01",
            "in any way possible!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FYou're always so reliable, Fran.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 6)
    Jump("loc_441F")

    label("loc_4359")


    ChrTalk(
        0x9,
        (
            "#1900FTaking an orbal bus to St. Ursula Medical\x01",
            "College will greatly reduce travel time.\x02\x03",
            "I don't anticipate there being any issues,\x01",
            "but don't hesitate to contact me if anything\x01",
            "pops up, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_441F")

    Jump("loc_7751")

    label("loc_4424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_45A8")
    OP_93(0x9, 0x5A, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fran is using a communication device.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#1901FYes, yes...\x02\x03",
            "#1903FWe're terribly sorry. The lockdown\x01",
            "is only temporary.\x02\x03",
            "#1901FWe expect it to be over in about an hour.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A3")

    ChrTalk(
        0x101,
        (
            "#0000F(Think she's dealing with complaints over the\x01",
            "lockdown?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(Yeah, it seems likely. She looks awfully\x01",
            "busy, so it'd be best if we don't disturb her.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_45A3")

    Jump("loc_7751")

    label("loc_45A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_468E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45C3")
    Call(0, 11)
    Jump("loc_4689")

    label("loc_45C3")


    ChrTalk(
        0x9,
        (
            "#1901FI know it's only temporary, but locking down\x01",
            "the airport is a bit concerning...\x02\x03",
            "#1903FNot to mention, there was that raid yesterday.\x01",
            "There's plenty of reasons to be worried right now...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4689")

    Jump("loc_7751")

    label("loc_468E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_47EF")

    ChrTalk(
        0x9,
        (
            "#1900FHi, everyone.\x01",
            "Keep up the good work.\x02\x03",
            "There were hardly any follow-up reports\x01",
            "on the Heiyue raid.\x02\x03",
            "#1903FI sure hope we can resolve the issue without\x01",
            "having it blow up into something more serious.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47EA")

    ChrTalk(
        0x101,
        "#0003FYeah, I'm with you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FAll we can do for now is leave it up to\x01",
            "the First Division's investigation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_47EA")

    Jump("loc_7751")

    label("loc_47EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_49B0")
    TurnDirection(0x9, 0x8, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4955")

    ChrTalk(
        0x9,
        (
            "#1905FWhoa, a gunfight?\x02\x03",
            "What the heck is going on out there?!\x01",
            "How'd something so dangerous happen\x01",
            "in the middle of the city?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(I believe Fran only recently became privy to\x01",
            "the details of the incident.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Yeah, I doubt any information is going to leak\x01",
            "with how tight-lipped the First Division is.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_49AB")

    label("loc_4955")


    ChrTalk(
        0x9,
        (
            "#1905FHow'd something so dangerous happen?\x02\x03",
            "#1901FThat...really grinds my gears!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49AB")

    Jump("loc_7751")

    label("loc_49B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4C0B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4A75")

    ChrTalk(
        0x9,
        (
            "#1900FHmm... I wonder how Anton's doing.\x01",
            "Has he gone home already?\x02\x03",
            "#1903FI feel kinda bad for him. He took me out to a nice\x01",
            "meal and I forgot to thank him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B61")

    label("loc_4A75")


    ChrTalk(
        0x9,
        (
            "#1900FI'm still glad I got the opportunity to enjoy a nice\x01",
            "meal with him, though.\x02\x03",
            "#1909FThanks for your help, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(Poor Anton... I don't think she realizes she\x01",
            "broke the heart of a man madly in love with her.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4B61")

    Jump("loc_4C06")

    label("loc_4B66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_4BEE")

    ChrTalk(
        0x9,
        (
            "#1900FI'll be heading off to Vingt-Sept\x01",
            "in Central Square in a bit.\x02\x03",
            "#1909FPlease send Anton my warmest regards.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C06")

    label("loc_4BEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_4C03")
    Call(0, 32)
    Jump("loc_4C06")

    label("loc_4C03")

    Call(0, 10)

    label("loc_4C06")

    Jump("loc_7751")

    label("loc_4C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4C19")
    Jump("loc_7751")

    label("loc_4C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 2)), scpexpr(EXPR_END)), "loc_4EF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E93")

    ChrTalk(
        0x9,
        (
            "#1900FHi, everyone.\x01",
            "You look kinda busy. What's up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYeah, we're sorta in the middle of something.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the details of the investigation\x01",
            "and their meeting with Noel at the entrance of\x01",
            "the Stargazer's Tower.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#1905FS-Sounds like you've got a lot on your plate.\x02\x03",
            "So, what's my sister up to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301FShe's waitin' for us back at the tower.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FWe plan to reconvene with her once we've\x01",
            "finished preparing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1903FAh, okay. Makes sense.\x02\x03",
            "#1901FBe careful, guys.\x02\x03",
            "Please take good care of Noey, too.\x01",
            "I'm counting on all of you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 6)
    Jump("loc_4EF1")

    label("loc_4E93")


    ChrTalk(
        0x9,
        (
            "#1901FBe careful, guys.\x02\x03",
            "Please take good care of Noey, too.\x01",
            "I'm counting on all of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF1")

    Jump("loc_7751")

    label("loc_4EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_50A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5020")

    ChrTalk(
        0x9,
        (
            "#1900FYou guys hear about Arc en Ciel's new show\x01",
            "for the opening day of the Anniversary Festival?\x02\x03",
            "Both the festival and Arc en Ciel are fantastic,\x01",
            "so we're bound to get something incredible\x01",
            "with them joining forces.\x02\x03",
            "#1906F*sigh* I wanna go and watch it with Noey.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_50A1")

    label("loc_5020")


    ChrTalk(
        0x9,
        (
            "#1900FI bet Arc en Ciel's new show is going\x01",
            "to be absolutely amazing!\x02\x03",
            "#1906F*sigh* Aww, I wanna go and watch\x01",
            "it with Noey.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50A1")

    Jump("loc_7751")

    label("loc_50A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_549A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5392")
    OP_93(0x9, 0x5A, 0x0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    ChrTalk(
        0x9,
        (
            "#1905FAh, you guys are here!\x02\x03",
            "#1903FWhat a bummer. I can't imagine it felt\x01",
            "good having the First Division take your\x01",
            "case from you.\x02\x03",
            "#1900FI've been cheering you guys on from\x01",
            "the beginning, so I feel pretty bad about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FDon't worry about it. It's not worth\x01",
            "beating yourself up over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FThank you for being concerned\x01",
            "about us, Fran.\x02\x03",
            "We're fine, though. We've already set aside\x01",
            "our feelings and moved on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FHaving you send us support requests\x01",
            "is enough to keep us happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1903FOkay... If you guys say so.\x02\x03",
            "#1900FEhehe, sorry about that.\x02\x03",
            "#1901FI, Fran Seeker, will also set aside my\x01",
            "feelings and continue supporting you\x01",
            "to the best of my abilities!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 6)
    Jump("loc_5495")

    label("loc_5392")


    ChrTalk(
        0x9,
        (
            "#1900FNone of the First Division members\x01",
            "bother to greet me when they pass by\x01",
            "reception...\x02\x03",
            "#1903FI get that they're busy, but it almost feels\x01",
            "like they don't like me.\x02\x03",
            "#1903FWe're colleagues, so I'd like it if we could\x01",
            "open up to each other a bit more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5495")

    Jump("loc_7751")

    label("loc_549A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_585B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57B7")
    OP_93(0x9, 0x5A, 0x0)

    ChrTalk(
        0x9,
        (
            "#1906FRebecca and I have been getting a lot\x01",
            "more requests over the orbal network.\x02\x03",
            "#1900FThe Anniversary Festival is starting soon,\x01",
            "so I've gotta keep at it!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    ChrTalk(
        0x9,
        (
            "#1905FOh, hey, everyone!\x02\x03",
            "#1900FHow's that client's request\x01",
            "coming along?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_END)), "loc_56B9")

    ChrTalk(
        0x101,
        (
            "#0003FWell, uh, there's a lot to go over.\x02\x03",
            "#0000FWe'll include it all in our report later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#1905FI feel like I might be missing something...\x02\x03",
            "#1901FChin up, guys! I believe in you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57AF")

    label("loc_56B9")


    ChrTalk(
        0x101,
        (
            "#0000FIt went well. We decided to give them a hand.\x02\x03",
            "#0001FIt seems like it's going to be hard work,\x01",
            "but I can't just let it slide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1900FI'm glad you guys are headstrong.\x02\x03",
            "#1901FAnyway... Keep up the good work,\x01",
            "my favorite detectives!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57AF")

    SetScenarioFlags(0x0, 1)
    Jump("loc_5856")

    label("loc_57B7")


    ChrTalk(
        0x9,
        (
            "#1900FRebecca and I have been getting\x01",
            "a lot more jobs on the orbal network.\x02\x03",
            "The Anniversary Festival is starting soon,\x01",
            "so I've gotta keep doing my best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5856")

    Jump("loc_7751")

    label("loc_585B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_END)), "loc_59E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5959")

    ChrTalk(
        0x9,
        (
            "#1900FHi, everyone. Were you able to\x01",
            "see the client?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0304FHell, yeah... They were friggin' huge!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1905F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FRandy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203FOh, boy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0111F*sigh* Try and restrain yourself\x01",
            "just a little bit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_59E1")

    label("loc_5959")


    ChrTalk(
        0x9,
        (
            "#1903FI don't really get what's going on,\x01",
            "but the request sounded serious.\x02\x03",
            "#1900FDo what you can to help the poor\x01",
            "girl out, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59E1")

    Jump("loc_7751")

    label("loc_59E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_END)), "loc_5C38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BC7")

    ChrTalk(
        0x9,
        (
            "#1900FHey, everyone!\x02\x03",
            "The client was such a cutie!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FYou thinkin' what I'm thinkin', Lloyd?\x01",
            "Let's hurry our asses back there!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AAB")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5AAB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AD1")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5AD1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AF7")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5AF7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B1D")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5B1D")

    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#1903FUhh...\x02\x03",
            "#1901FHer request seemed pretty serious,\x01",
            "so I had her go directly to the SSS.\x02\x03",
            "#1900FYou guys should probably go there\x01",
            "as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5C33")

    label("loc_5BC7")


    ChrTalk(
        0x9,
        (
            "#1900FI had the client go directly to the\x01",
            "SSS.\x02\x03",
            "You guys should probably go there\x01",
            "as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C33")

    Jump("loc_7751")

    label("loc_5C38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5F5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E4B")

    ChrTalk(
        0x9,
        (
            "#1906FListen to this, guys!\x02\x03",
            "#1901FThe First Division got their very own\x01",
            "operations room yesterday!\x01",
            "It's down in the basement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWow, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1903FYeah, it's pretty amazing!\x02\x03",
            "They've got three operators working\x01",
            "down there.\x02\x03",
            "#1901FDarn it... I'm kinda frustrated!\x01",
            "I'm not going to let them make me look bad!\x02",
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
        (
            "#0303FHah, no surprises here.\x01",
            "The First Division's the pride of the CPD.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5F5A")

    label("loc_5E4B")


    ChrTalk(
        0x9,
        (
            "#1903FThe First Division got their very own\x01",
            "operations room yesterday!\x01",
            "It's down in the basement.\x02\x03",
            "#1901FDarn it... I'm not going to let this bring me down.\x01",
            "I'm going to keep supporting you as hard as I can!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha, thanks Fran. I know we're in good hands.\x02",
    )

    CloseMessageWindow()

    label("loc_5F5A")

    Jump("loc_7751")

    label("loc_5F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6355")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62CD")

    ChrTalk(
        0x9,
        "#1909FHehehe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300F'Sup, Fran? You're lookin as cheery as ever.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#1900FHi, everyone!\x01",
            "I heard the news!\x02\x03",
            "#1909FNoey came to headquarters earlier\x01",
            "and hung out with me for a bit!\x02\x03",
            "#1900FShe apparently came by yesterday,\x01",
            "but we missed each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FOh, yeah. She said you two were sisters.\x01",
            "Sergeant Major Noel Seeker, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FWe were recently introduced to her.\x02\x03",
            "I got the impression that she was well mannered\x01",
            "and intelligent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FHer personality is significantly different to\x01",
            "that of Fran's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1900FHehehe, you've got that right.\x02\x03",
            "#1903FMy sister's both cool and dignified,\x01",
            "yet she manages to look cute, too.\x02\x03",
            "#1900FI've admired her ever since we were little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYou make it sound like she has it all.\x01",
            "It's no surprise that you admire her.\x02\x03",
            "#0008F(A sibling to look up to...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 6)
    Jump("loc_6350")

    label("loc_62CD")


    ChrTalk(
        0x9,
        (
            "#1900FYou guys are going to Mainz today, right?\x02\x03",
            "Please don't let my sister down! She's\x01",
            "expecting great things from you guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6350")

    Jump("loc_7751")

    label("loc_6355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_695E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67F7")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x9,
        (
            "#1900FKeep up the good work, everyone!\x02\x03",
            "Did anything interesting happen while you\x01",
            "were investigating Armorica?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FNo, nothing yet. We haven't\x01",
            "learned anything outside of the\x01",
            "CGF's investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1903FAww, what a shame.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#1900FOh, yeah. I guess the CGF did conduct\x01",
            "their own investigation.\x02\x03",
            "You guys think Noey was out in the field, too?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        (
            "Fran loves to boast about her\x01",
            "older sister in the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I have to sit here listening to Fran go on about her\x01",
            "pretty much every day.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)
    TurnDirection(0x9, 0x8, 500)
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x9,
        (
            "#1906FC-C'mon, Rebecca. Don't tease me like that.\x02\x03",
            "I only do it because my sister hardly\x01",
            "ever contacts me.\x02\x03",
            "#1900FNothing more, nothing less. I-I'm not\x01",
            "feeling lonely, or anything. I swear!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x104,
        (
            "#0303F(Can't say I ever feel good goin' to\x01",
            "headquarters, but...)\x02\x03",
            "#0300F(Bein' at reception with these lovely ladies\x01",
            "always brightens my day... ㈱)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102F(I'm beginning to understand why these\x01",
            "two were appointed as receptionists.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x6B, 5)
    Jump("loc_6959")

    label("loc_67F7")


    ChrTalk(
        0x9,
        (
            "#1903FAhem! Let's just erase that last conversation\x01",
            "from our memories!\x02\x03",
            "#1900FI'm a member of the force, too, guys.\x01",
            "It's not professional of me to mix my\x01",
            "personal matters with work.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#1903F*sigh* Oh, Noey...\x01",
            "What are you up to these days?\x02",
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

    label("loc_6959")

    Jump("loc_7751")

    label("loc_695E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6F5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E82")
    OP_93(0x9, 0x5A, 0x0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    ChrTalk(
        0x9,
        (
            "#1905FHey, guys! I heard the news.\x02\x03",
            "#1900FYou've gotta leave the city to investigate\x01",
            "the monster incidents, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, we're about to depart for\x01",
            "Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1901FI, Fran Seeker, will support you\x01",
            "with everything I've got!\x02\x03",
            "#1903F...Is what I'd like to say.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#1900FBut, I'm not too sure you'll be in range\x01",
            "to receive orbal communication.\x02\x03",
            "We'll just have to try and find out.\x01",
            "It's usually fine inside of the city, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FI-I see. Do you think our Enigmas will be\x01",
            "too far away to communicate with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FThe operating system was intended for\x01",
            "investigative use only within city limits.\x02\x03",
            "#0200FThough, theoretically speaking, orbal waves\x01",
            "should be able to travel up to 200 selge\x01",
            "outside of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FHmm, 200 selge... I think that'll just barely\x01",
            "reach anywhere inhabited by people within\x01",
            "the state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1900FSo we'll be able to keep up communications,\x01",
            "then? Thank Aidios...\x02\x03",
            "Don't forget to contact your pal Fran Seeker\x01",
            "if you get yourselves into a bind, guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FRoger that, Fran. You don't have\x01",
            "to feel so anxious. We'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYeah, we're just doin' an investigation.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6F58")

    label("loc_6E82")


    ChrTalk(
        0x9,
        (
            "#1900FPhew... It was such a pain to get used to operating\x01",
            "this darn thing! I woulda been so annoyed if I couldn't\x01",
            "support you guys.\x02\x03",
            "Don't forget to contact your trusty operator\x01",
            "if you run into trouble, guys!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F58")

    Jump("loc_7751")

    label("loc_6F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7381")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_718B")

    ChrTalk(
        0x9,
        (
            "#1900FHey, everyone.\x01",
            "I'm glad you're all okay.\x02\x03",
            "You're going to go stop the delinquents from\x01",
            "stirring up trouble downtown, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYeah. At least, that's the plan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1900FWell, I hope it all turns out okay.\x02\x03",
            "I live on East Street, so I occasionally\x01",
            "catch those guys causing a ruckus.\x02\x03",
            "#1903FI get a little bit scared when they\x01",
            "get together and start brawling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FIt must be hard dealing with it every day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FWe definitely need to do something about\x01",
            "their behavior. It's about time they stopped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_737C")

    label("loc_718B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72D5")

    ChrTalk(
        0x9,
        (
            "#1900FOh, yeah! I had something to tell you guys\x01",
            "about that monster extermination request.\x02\x03",
            "Sorry for making you guys jump through some\x01",
            "extra hoops, but can you file the report through\x01",
            "the terminal at the SSS building?\x02\x03",
            "They're planning on pairing your report with\x01",
            "an orbal network diagnostics test.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_737C")

    label("loc_72D5")


    ChrTalk(
        0x9,
        (
            "#1900FI live on East Street, so I occasionally\x01",
            "catch those guys causing a ruckus.\x02\x03",
            "#1903FI get a little bit scared watching them\x01",
            "get together and start fighting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_737C")

    Jump("loc_7751")

    label("loc_7381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7751")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_7617")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7571")

    ChrTalk(
        0x9,
        (
            "#1909FHiya, everyone!\x02\x03",
            "#1900FAm I doing a good job as your operator?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYep, you did great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FWe'll be counting on you in the future, Fran.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1900FYep, likewise!\x02\x03",
            "#1903FThe only problem is...\x01",
            "I can't gossip with you guys all the time,\x01",
            "since every exchange is recorded...\x02\x03",
            "#1900FDon't forget to visit me in person every\x01",
            "once in a while, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FAnythin' for my favorite gal!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWe'll be sure to come by again soon.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_7612")

    label("loc_7571")


    ChrTalk(
        0x9,
        (
            "#1903FI can't gossip with you guys all the time,\x01",
            "since every exchange is recorded...\x02\x03",
            "#1900FDon't forget to visit me in person every\x01",
            "once in a while, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7612")

    Jump("loc_7751")

    label("loc_7617")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7751")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0x8,
        (
            "All right, I believe that should wrap up the\x01",
            "explanation on support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, then, once you return to the SSS, try pressing\x01",
            "the 'Report' option on your terminal screen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1900FHeehee. I'll be handling any incoming\x01",
            "requests for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_7751")

    label("loc_7751")

    TalkEnd(0x9)
    Return()

    # Function_9_405F end

    def Function_10_7755(): pass

    label("Function_10_7755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B90")
    EventBegin(0x0)
    Fade(500)
    OP_68(3000, 1500, 14000, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x109, 3000, 0, 13500, 0)
    SetChrPos(0x104, 3750, 0, 13000, 0)
    SetChrPos(0x102, 2250, 0, 12250, 0)
    SetChrPos(0x103, 4000, 0, 12000, 0)
    SetChrPos(0x101, 2750, 0, 11500, 0)
    TurnDirection(0x9, 0x109, 0)
    SetChrSubChip(0x9, 0x0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#1905FHey, Noey!\x02\x03",
            "Did you end up talking to Lloyd and\x01",
            "the others about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#0500FYeah, they said they'd help.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x109, 500)

    ChrTalk(
        0x104,
        "#0305FOh, you told Fran?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x104, 500)

    ChrTalk(
        0x109,
        (
            "#0500FI had originally consulted Fran before\x01",
            "talking to you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1903FYou guys actually think there's\x01",
            "a ghost out there?\x02\x03",
            "#1900FI'm having trouble believing a load of\x01",
            "baloney like that!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_796E():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_796E)
    Sleep(50)

    def lambda_797E():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_797E)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x109,
        (
            "#0503FI told you I really saw one!\x02\x03",
            "#0500FI'm not entirely certain that it was a ghost,\x01",
            "but it was definitely monstrous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1900FHuh? But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FSorry to interrupt you two, but\x01",
            "you're spooking Elie out.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7A96():
        TurnDirection(0x9, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7A96)

    def lambda_7AA3():
        TurnDirection(0x109, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7AA3)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x109,
        "#0505FO-Oh, I'm so sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1900FHeehee, I'm sorry, Elie.\x01",
            "(Is she scared of ghosts or something?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0109FN-No, I'm fine. A simple discussion\x01",
            "isn't enough to s-scare me...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 3000, 0, 13500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xCE, 4)
    EventEnd(0x5)
    Jump("loc_7C97")

    label("loc_7B90")


    ChrTalk(
        0x9,
        (
            "#1900FI heard the story from my sister, but I'm\x01",
            "having a hard time believing there's a ghost.\x02\x03",
            "#1906F*sigh* If only I wasn't a receptionist...\x01",
            "I'd totally wanna tag along with Noey\x01",
            "to check it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106F(I can't relate to Fran in any way\x01",
            "right now...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C97")

    Return()

    # Function_10_7755 end

    def Function_11_7C98(): pass

    label("Function_11_7C98")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x9, 0x0, 0)
    TurnDirection(0x8, 0x0, 0)

    ChrTalk(
        0x9,
        (
            "#1901FHey, everyone...\x01",
            "Did you hear the news about Crossbell Airport?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FNo, what happened?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 6)), scpexpr(EXPR_END)), "loc_7D75")

    ChrTalk(
        0x104,
        (
            "#0301FOh, yeah, I noticed a detective hangin' out there\x01",
            "in his normal clothing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D75")


    ChrTalk(
        0x8,
        (
            "The First Division mobilized the entire\x01",
            "force a short while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They've apparently placed a temporary lockdown\x01",
            "on the entire airport.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0011FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0101FWhat's the situation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1906FWell...\x01",
            "They were told to keep it hush, so\x01",
            "we couldn't get any info out of them.\x02\x03",
            "#1901FLooks like you guys don't know anything\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FWe are not ones to receive important\x01",
            "information, usually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FI'd be lying if I said I wasn't concerned.\x02\x03",
            "#0008F(Maybe we can squeeze something\x01",
            "out of Detective Dudley later.)\x02\x03",
            "#0001F(We should focus on investigating the\x01",
            "missing people for now.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 0)
    TurnDirection(0x8, 0x9, 0)
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_7C98 end

    def Function_12_8055(): pass

    label("Function_12_8055")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8066")
    Jump("loc_9579")

    label("loc_8066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8074")
    Jump("loc_9579")

    label("loc_8074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8082")
    Jump("loc_9579")

    label("loc_8082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_829B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81F4")
    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        "Man, what a pain in the ass.\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        "Oh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm likin' the expressions you've got on your\x01",
            "faces today! I gotta say, I envy you SSS\x01",
            "guys at times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWhat's the matter, Inspector Donovan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Eh, nothing serious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm just a little salty the First Division\x01",
            "took our case away.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8296")

    label("loc_81F4")


    ChrTalk(
        0xFE,
        (
            "I was going to investigate the raid by\x01",
            "Revache's members, but, uh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The First Division coerced us into\x01",
            "giving it to them. Man, what a\x01",
            "pain in the ass.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8296")

    Jump("loc_9579")

    label("loc_829B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_864D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_856F")

    ChrTalk(
        0xFE,
        "Well, if it isn't the Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hah, heard you guys got stuck indoors\x01",
            "after playing with fire and getting placed\x01",
            "on Revache's watch list.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew you'd all do something to piss off\x01",
            "the wrong people eventually, but damn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FWe know we've caused problems for the\x01",
            "department in the last week. I apologize\x01",
            "for that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_8440")

    ChrTalk(
        0x102,
        "#0103FI don't know what to say...\x02",
    )

    CloseMessageWindow()
    Jump("loc_849E")

    label("loc_8440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_8473")

    ChrTalk(
        0x103,
        "#0203FI am at a loss for words.\x02",
    )

    CloseMessageWindow()
    Jump("loc_849E")

    label("loc_8473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_849E")

    ChrTalk(
        0x104,
        "#0303FDunno what to tell ya.\x02",
    )

    CloseMessageWindow()

    label("loc_849E")


    ChrTalk(
        0xFE,
        (
            "Eh, it's mostly just the top brass\x01",
            "that are furious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys were on house arrest for a week, yeah?\x01",
            "Don't feel too bad about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think you guys were in the wrong,\x01",
            "to be honest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB1, 2)
    Jump("loc_8648")

    label("loc_856F")


    ChrTalk(
        0xFE,
        (
            "The Second Division has been on high alert all\x01",
            "week, but apparently, a deal was struck up\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nothing particularly interesting has happened, so\x01",
            "isn't it about time you guys got back to your lives?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8648")

    Jump("loc_9579")

    label("loc_864D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_865B")
    Jump("loc_9579")

    label("loc_865B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8669")
    Jump("loc_9579")

    label("loc_8669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8677")
    Jump("loc_9579")

    label("loc_8677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_893A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_887C")

    ChrTalk(
        0xFE,
        "What's up, guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's been an uptick in violent crimes\x01",
            "as of late. Us Second Division guys don't\x01",
            "have any time to take a break.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 1)), scpexpr(EXPR_END)), "loc_8784")

    ChrTalk(
        0x101,
        (
            "#0008FYou know, now that you mention it...\x01",
            "We've been hearing rumors throughout the city.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87C0")

    label("loc_8784")


    ChrTalk(
        0x101,
        (
            "#0005FOh, really?\x01",
            "That's kind of concerning, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87C0")


    ChrTalk(
        0xFE,
        (
            "Yeah, it looks like the Anniversary Festival isn't\x01",
            "the only thing that's approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stay safe out there, guys.\x01",
            "Be aware of your surroundings while you\x01",
            "patrol the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8935")

    label("loc_887C")


    ChrTalk(
        0xFE,
        (
            "There's been a recent increase in unsettling\x01",
            "stories about acts of violence committed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was even a shooting last night, man.\x01",
            "I was just on my way to do some questioning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8935")

    Jump("loc_9579")

    label("loc_893A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8AE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A2E")

    ChrTalk(
        0xFE,
        (
            "Hey there, guys. Sounds like you have\x01",
            "another annoying job on your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Be careful not to get dragged into the\x01",
            "top brass' problems, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha, thanks...\x01",
            "(A little too late for that... Oh, well.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8ADD")

    label("loc_8A2E")


    ChrTalk(
        0xFE,
        (
            "Sounds like you guys have another\x01",
            "annoying job on your hands!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, even the top brass have their own circumstances.\x01",
            "Try not to get dragged into their problems, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8ADD")

    Jump("loc_9579")

    label("loc_8AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8D0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C96")

    ChrTalk(
        0xFE,
        (
            "It's come to my understanding that last month's\x01",
            "incident involved a diet member.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The top brass is acting all wishy-washy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's all 'cause they know it involves a politician.\x01",
            "Great. Another CPD special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FWhy not just arrest the politician?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it's not that simple...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've been low-key pressuring us, so we've gotta\x01",
            "be more prudent with the investigation going forward.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8D08")

    label("loc_8C96")


    ChrTalk(
        0xFE,
        (
            "Our top brass has become all wishy-washy because\x01",
            "a diet member is involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Great. Another CPD special.\x02",
    )

    CloseMessageWindow()

    label("loc_8D08")

    Jump("loc_9579")

    label("loc_8D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F00")

    ChrTalk(
        0xFE,
        "Hey, guys. Keep up the good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys still going hard at those\x01",
            "support requests you do all the time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FYeah, I'd say so. Haha.\x02\x03",
            "#0000FHow's everyone in the Second Division\x01",
            "doing these days?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We ain't doing too poorly ourselves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got a few cases on our hands, but\x01",
            "it's not like they progress quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "All we can do is diligently work on one at a time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FYeah, definitely. That's the best way\x01",
            "to handle an investigation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8F7D")

    label("loc_8F00")


    ChrTalk(
        0xFE,
        "The Second Division's slowly doing their work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ultimately, all we can do is diligently work on\x01",
            "one case at a time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F7D")

    Jump("loc_9579")

    label("loc_8F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_912D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9094")

    ChrTalk(
        0xFE,
        (
            "*sigh* Great Goddess above...\x01",
            "Getting evidence is such a pain in the ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only is Crossbell City way too damn big,\x01",
            "but there's a ton of people living here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It doesn't matter how many people you question\x01",
            "in a day. It never ends.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_9128")

    label("loc_9094")


    ChrTalk(
        0xFE,
        (
            "Oh, thank Aidios.\x01",
            "I can finally get me some lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, us slackers in the Second Division have\x01",
            "always had problems being short-staffed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9128")

    Jump("loc_9579")

    label("loc_912D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9579")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9414")

    ChrTalk(
        0xFE,
        "Hey. Looks like you guys are already hard at work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, you may be police officers, but most\x01",
            "of us don't think too kindly of you.\x01",
            "Try not to pick any fights, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FWhat's with all the hate, man?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the more hardcore guys in the force think of\x01",
            "you as discount bracers, so their pride has taken\x01",
            "a severe blow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doesn't matter if you live in your own detached office.\x01",
            "Most of the department considers you an eyesore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FUgh... Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FWe were fortunate enough to have our\x01",
            "office in a separate building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, don't let it bother you too much.\x01",
            "You gotta get used to your job ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's the easiest shortcut to knockin'\x01",
            "these guys off their high horses.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4A, 0)
    SetScenarioFlags(0x0, 2)
    Jump("loc_9579")

    label("loc_9414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94D5")

    ChrTalk(
        0xFE,
        "Hey. Looks like you guys are already hard at work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, you may be police officers, but most\x01",
            "of us don't think too kindly of you.\x01",
            "Try not to pick any fights, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_9579")

    label("loc_94D5")


    ChrTalk(
        0xFE,
        (
            "Well, you may be police officers, but most\x01",
            "of us don't think too kindly of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whether that bothers you are not,\x01",
            "do what you can to not pick any fights.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9579")

    TalkEnd(0xFE)
    Return()

    # Function_12_8055 end

    def Function_13_957D(): pass

    label("Function_13_957D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_958E")
    Jump("loc_A6BC")

    label("loc_958E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_959C")
    Jump("loc_A6BC")

    label("loc_959C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_95AA")
    Jump("loc_A6BC")

    label("loc_95AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_96DE")

    ChrTalk(
        0xFE,
        (
            "The First Division snatched the Revache case\x01",
            "from our hands this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only that, but they made us hand over any\x01",
            "information regarding the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn it! I'm so pissed off! Don'tcha just lose\x01",
            "all your motivation when you keep getting\x01",
            "screwed over and over again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6BC")

    label("loc_96DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9ADA")

    ChrTalk(
        0xFE,
        (
            "The comissioner and vice commissioners were\x01",
            "summoned to City Hall today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Vice Commissioner Pierre's been worried about\x01",
            "his job. Sounds like he's on a pretty short leash.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_97DE")

    ChrTalk(
        0x102,
        "#0106FThat's welcome news, but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_985A")

    label("loc_97DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_9819")

    ChrTalk(
        0x103,
        "#0206FI am not sad to hear that, but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_985A")

    label("loc_9819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_985A")

    ChrTalk(
        0x104,
        "#0306FServes Vice Commish Jackass right, but uh...\x02",
    )

    CloseMessageWindow()

    label("loc_985A")


    ChrTalk(
        0x101,
        (
            "#0003FI doubt it would stop him from giving\x01",
            "us an earful regardless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, he'd probably snap at you for\x01",
            "everything that happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That sly old fox would do anything to protect\x01",
            "his interests.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_99CA")

    ChrTalk(
        0x102,
        (
            "#0106FRevache aren't the only ones to be wary of.\x01",
            "We can't overlook the vice commissioner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AA0")

    label("loc_99CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_9A3A")

    ChrTalk(
        0x103,
        (
            "#0200FIn addition to Revache, we cannot neglect\x01",
            "the threat that the vice commissioner poses.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AA0")

    label("loc_9A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9AA0")

    ChrTalk(
        0x104,
        (
            "#0300FBad enough we have Revache to worry about.\x01",
            "We gotta account for a mangy fox, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AA0")


    ChrTalk(
        0x153,
        "#1111F(Fox? What's everybody talking about?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_9B88")

    label("loc_9ADA")


    ChrTalk(
        0xFE,
        (
            "The commissioner and vice commissioners were\x01",
            "summoned to City Hall today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Color me surprised. You guys manage to pull off\x01",
            "some amazing stuff every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B88")

    Jump("loc_A6BC")

    label("loc_9B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9B9B")
    Jump("loc_A6BC")

    label("loc_9B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9D05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C5B")

    ChrTalk(
        0xFE,
        "You know that chick, Emma, in the First Division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She and I used to be classmates.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She was an elite back in the day, too.\x01",
            "Ugh, I can't deal with her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_9D00")

    label("loc_9C5B")


    ChrTalk(
        0xFE,
        (
            "Emma's been an elite for as long\x01",
            "as I can remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She takes on a condescending tone with me, even\x01",
            "though we were classmates. Ugh, I can't deal with her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D00")

    Jump("loc_A6BC")

    label("loc_9D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9D13")
    Jump("loc_A6BC")

    label("loc_9D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9EBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E5F")

    ChrTalk(
        0xFE,
        (
            "*sigh* It's been one goddamn incident after\x01",
            "another this week!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I pulled an all-nighter doing an on-site inspection...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the other hand, it sounds like there was a shooting\x01",
            "near all those warehouses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sheesh, I wish the citizenry would at least\x01",
            "try and understand some of my hardships.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_9EB6")

    label("loc_9E5F")


    ChrTalk(
        0xFE,
        "Pulling an all-nighter is rough!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I don't get paid well enough for this crap.\x02",
    )

    CloseMessageWindow()

    label("loc_9EB6")

    Jump("loc_A6BC")

    label("loc_9EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9F9F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9ED8")
    Call(0, 14)
    Jump("loc_9F9A")

    label("loc_9ED8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_9F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9EF6")
    Call(0, 14)
    Jump("loc_9F7D")

    label("loc_9EF6")


    ChrTalk(
        0xB,
        (
            "*sigh* Thanks for coming to\x01",
            "grab the book for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'll be sure to properly check the contents\x01",
            "the next time I borrow one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_9F7D")

    Jump("loc_9F9A")

    label("loc_9F82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_9F97")
    Call(0, 28)
    Jump("loc_9F9A")

    label("loc_9F97")

    Call(0, 14)

    label("loc_9F9A")

    Jump("loc_A6BC")

    label("loc_9F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A083")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9FBC")
    Call(0, 15)
    Jump("loc_A07E")

    label("loc_9FBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_A066")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9FDA")
    Call(0, 15)
    Jump("loc_A061")

    label("loc_9FDA")


    ChrTalk(
        0xB,
        (
            "*sigh* Thanks for coming to\x01",
            "grab the book for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'll be sure to properly check the contents\x01",
            "the next time I borrow one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_A061")

    Jump("loc_A07E")

    label("loc_A066")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_A07B")
    Call(0, 28)
    Jump("loc_A07E")

    label("loc_A07B")

    Call(0, 15)

    label("loc_A07E")

    Jump("loc_A6BC")

    label("loc_A083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A167")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A0A0")
    Call(0, 16)
    Jump("loc_A162")

    label("loc_A0A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_A14A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_A0BE")
    Call(0, 16)
    Jump("loc_A145")

    label("loc_A0BE")


    ChrTalk(
        0xB,
        (
            "*sigh* Thanks for coming to\x01",
            "grab the book for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'll be sure to properly check the contents\x01",
            "the next time I borrow one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_A145")

    Jump("loc_A162")

    label("loc_A14A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_A15F")
    Call(0, 28)
    Jump("loc_A162")

    label("loc_A15F")

    Call(0, 16)

    label("loc_A162")

    Jump("loc_A6BC")

    label("loc_A167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A229")

    ChrTalk(
        0xFE,
        (
            "*sigh* It's hard to even get these records organized.\x01",
            "Caffeine... I need caffeine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd better go and get a quick boost of energy\x01",
            "by seeing Rebecca, while I'm at it. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6BC")

    label("loc_A229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_A6BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4FE")

    ChrTalk(
        0xFE,
        (
            "So, Fran told me you guys ended up\x01",
            "stayin' in that weird new division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Pretty gutsy move, to be honest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regardless, you're still my juniors. Feel free to\x01",
            "ask me questions about anything you don't\x01",
            "understand, and I'll try my hardest to answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThanks. We appreciate it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    ChrTalk(
        0xFE,
        (
            "By the way...are you free right now,\x01",
            "my dear Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How 'bout we grab some lunch together?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FI'll have to respectfully decline.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aw, shucks. Really? Hahaha... I can tell\x01",
            "you act extra careful around us men.\x02",
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
        "#0000F(This guy doesn't have a care in the world, does he?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4A, 1)
    SetScenarioFlags(0x0, 3)
    Jump("loc_A6BC")

    label("loc_A4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A603")

    ChrTalk(
        0xFE,
        (
            "Heard you guys ended up stayin' in that weird,\x01",
            "new section. Pretty gutsy move, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regardless, you're still my juniors.\x01",
            "Feel free to ask me questions about anything\x01",
            "you don't understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll try my hardest to answer.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_A6BC")

    label("loc_A603")

    OP_93(0xFE, 0x10E, 0x0)

    ChrTalk(
        0xFE,
        (
            "Hey there. I've finished up my legwork,\x01",
            "but there were no witnesses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, Inspector. We're not going to progress any\x01",
            "further even if we continue to investigate, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6BC")

    TalkEnd(0xFE)
    Return()

    # Function_13_957D end

    def Function_14_A6C0(): pass

    label("Function_14_A6C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7DE")
    OP_4B(0xA, 0xFF)
    TurnDirection(0xFE, 0xA, 0)

    ChrTalk(
        0xA,
        (
            "Let's start by inquiring at the hotel.\x01",
            "We can follow that up by questioning\x01",
            "any nearby shops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "More legwork today? Seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, what a paaaaaaain...\x01",
            "The Entertainment District is huge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For cryin' out loud...\x01",
            "Get your act together!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_4C(0xA, 0xFF)
    Jump("loc_A87A")

    label("loc_A7DE")


    ChrTalk(
        0xFE,
        "Hey, you guys busy with an investigation, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like we're both pretty busy.\x01",
            "Don't even have the time to take a\x01",
            "pretty girl out on a date...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A87A")

    Return()

    # Function_14_A6C0 end

    def Function_15_A87B(): pass

    label("Function_15_A87B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA64")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "Hey, this dude's wife is pretty hot...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehehe... I suddenly feel more motivated\x01",
            "to do some investigatin'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(This guy is a dead ringer for Randy...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305F(Uh, 'scuse me?\x01",
            "Doesn't everybody do that?)\x02\x03",
            "#0300F(It's a pretty sweet method to get the\x01",
            "juices flowin' when you're in a slump.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9E7")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_A9E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA0D")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_AA0D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA33")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_AA33")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA59")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_AA59")

    Sleep(1000)
    SetScenarioFlags(0x0, 3)
    Jump("loc_AB1F")

    label("loc_AA64")


    ChrTalk(
        0xFE,
        (
            "Oh, you guys here to look for some\x01",
            "documents for your investigations, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those documents can be real nice, sometimes...\x01",
            "You get to meet the occasional beautiful married lady.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB1F")

    Return()

    # Function_15_A87B end

    def Function_16_AB20(): pass

    label("Function_16_AB20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACB6")

    ChrTalk(
        0xFE,
        "I walked by the CGF's Deputy Commander Baelz earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The CGF seems nice... I wouldn't mind getting\x01",
            "ordered around by someone like her, too. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FI'd stay away from her if I were you, pal.\x01",
            "Her trainin' is actually hard as hell.\x02\x03",
            "Y'know, runnin' marathons down the highway\x01",
            "in full gear and whatnot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gah. On second thought, I don't think\x01",
            "I'd be able to handle it...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_AD60")

    label("loc_ACB6")


    ChrTalk(
        0xFE,
        (
            "It must be nice getting bossed around by\x01",
            "a pretty lady like those CGF guys do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The entire top brass of the CPD is such\x01",
            "a sausage fest. I'm friggin' sick of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD60")

    Return()

    # Function_16_AB20 end

    def Function_17_AD61(): pass

    label("Function_17_AD61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B003")

    ChrTalk(
        0xFE,
        (
            "Hey! What's up, guys?\x01",
            "You guys look like you've been hard at it all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FYeah, we've got a busy day on our hands.\x02\x03",
            "#0000FHey, Franz. You've got a meeting to go\x01",
            "to, right? What's that all about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're determining everybody's patrol routes\x01",
            "in the Metropolitan Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been a month since I joined the CPD, so they\x01",
            "think it's time to throw me into the thick of things.\x01",
            "My superiors are pretty giddy about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha. Good luck, man.\x01",
            "Things seem pretty busy on your end, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah, let's give it everything we've got!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not like it's easier for you, either.\x01",
            "We're still a bunch of rookies, after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x70, 4)
    Jump("loc_B0D7")

    label("loc_B003")


    ChrTalk(
        0xFE,
        (
            "Our main duty as the Metropolitan Division\x01",
            "is to patrol the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been a month since I joined the CPD...\x01",
            "I think it's about time I start undertaking\x01",
            "some jobs. I feel like I'm up to the challenge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0D7")

    TalkEnd(0xFE)
    Return()

    # Function_17_AD61 end

    def Function_18_B0DB(): pass

    label("Function_18_B0DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B22C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1D3")

    ChrTalk(
        0xFE,
        (
            "All of the division chiefs are gathered in the\x01",
            "commissioner's office for an important meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think they're flippin' out over Revache or something.\x01",
            "Oh, how I'd love to be a fly on the wall of that room...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B227")

    label("loc_B1D3")


    ChrTalk(
        0xFE,
        "It's one incident after another.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What else could possibly go\x01",
            "wrong today?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B227")

    Jump("loc_BE9C")

    label("loc_B22C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B361")

    ChrTalk(
        0xFE,
        (
            "They established a joint investigation\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What if yet another incident occurs?\x01",
            "It'd be an excellent opportunity for the CPD\x01",
            "to display its collaborative abilities!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're not gonna get done in by some lowly terrorists!\x01",
            "We'll take 'em down before they can pull anything!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE9C")

    label("loc_B361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B50C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B423")

    ChrTalk(
        0xFE,
        "A raid? Are they insane?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're blessed to have come out of it\x01",
            "without any casualties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'd be nice if we could arrest those\x01",
            "dirtbags immediately, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B507")

    label("loc_B423")


    ChrTalk(
        0xFE,
        (
            "It's obvious that Revache did it, but we have\x01",
            "to gather adequate evidence before we\x01",
            "can actually issue a warrant for their arrests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Metropolitan Division has already launched\x01",
            "an investigation to start the process.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B507")

    Jump("loc_BE9C")

    label("loc_B50C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B5FF")

    ChrTalk(
        0xFE,
        (
            "The mafia's been getting out of hand.\x01",
            "More and more citizens are getting caught\x01",
            "up in their crimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The First Division is at their wits' end, too.\x01",
            "They're even giving special missions to the\x01",
            "Metropolitan Division, now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE9C")

    label("loc_B5FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_B60D")
    Jump("loc_BE9C")

    label("loc_B60D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_B733")

    ChrTalk(
        0xFE,
        (
            "You guys hear the news?\x01",
            "There's apparently been another incident\x01",
            "in the Entertainment District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as an officer in the Metropolitan\x01",
            "Division has located the perpetrator, the\x01",
            "Second Division will mobilize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think they're out questioning people\x01",
            "at the moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE9C")

    label("loc_B733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_B7BC")

    ChrTalk(
        0xFE,
        "All right, it's time to start today's patrol.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, going on patrol during the morning\x01",
            "can put you in a bad mood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE9C")

    label("loc_B7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_B9DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B924")

    ChrTalk(
        0xFE,
        (
            "VIPs from every nation on the continent will be\x01",
            "visiting during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The First and Second Investigative Divisions are handling\x01",
            "the security detail of the opening ceremony, so we've\x01",
            "gotta strengthen our patrols around the city as much as we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* This year's festival is gonna be a huge job.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B9D8")

    label("loc_B924")


    ChrTalk(
        0xFE,
        (
            "Covering the opening ceremony will be especially tough.\x01",
            "VIPs from all over the continent will be in attendance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've gotta decide on the patrol\x01",
            "routes pretty soon here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9D8")

    Jump("loc_BE9C")

    label("loc_B9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_BB53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB04")

    ChrTalk(
        0xFE,
        (
            "There's going to be all sorts of events during\x01",
            "the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Between guiding citizens and playing security,\x01",
            "us officers have our work cut out for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is the biggest job of the year, so we've\x01",
            "really gotta make sure not to screw this up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_BB4E")

    label("loc_BB04")


    ChrTalk(
        0xFE,
        (
            "Come next month, the Metropolitan Division\x01",
            "will be plenty busy, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB4E")

    Jump("loc_BE9C")

    label("loc_BB53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_BD31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC7F")

    ChrTalk(
        0xFE,
        (
            "We had some new recruits join our\x01",
            "division this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope they're handling themselves okay.\x01",
            "Even though we've got one of the calmer positions,\x01",
            "it's not exactly sunshine and daisies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I hope they don't get discouraged\x01",
            "trying to grow into their roles.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_BD2C")

    label("loc_BC7F")


    ChrTalk(
        0xFE,
        (
            "Even though we've got one of the calmer\x01",
            "positions, it can still get painfully difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope our rookies don't get discouraged\x01",
            "trying to grow into their roles.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD2C")

    Jump("loc_BE9C")

    label("loc_BD31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_BD42")
    Call(0, 19)
    Jump("loc_BE9C")

    label("loc_BD42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_BDE7")

    ChrTalk(
        0xFE,
        (
            "They suddenly changed the location\x01",
            "of today's meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did everybody go to the meeting room on the\x01",
            "second floor? There's nobody here at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE9C")

    label("loc_BDE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_BE9C")

    ChrTalk(
        0xFE,
        (
            "My supervisor, Kate, is showing me the ropes\x01",
            "on how to patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's a great coach, so it's easy to follow her\x01",
            "instructions. Pretty helpful, too, if I might add.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE9C")

    TalkEnd(0xFE)
    Return()

    # Function_18_B0DB end

    def Function_19_BEA0(): pass

    label("Function_19_BEA0")

    OP_4B(0xD, 0xFF)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xD, 0xF, 0)
    TurnDirection(0xF, 0xD, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C022")

    ChrTalk(
        0xD,
        (
            "They were able to smoothly allocate patrol\x01",
            "routes to all of the rookies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What about you, though, Officer Kate?\x01",
            "A veteran like you should go to a district\x01",
            "with weaker support.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Officer, please.\x01",
            "Spare me the 'Veteran' title.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Doesn't it make me sound like I'm\x01",
            "an old lady?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "Sorry about that, ma'am.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_C13C")

    label("loc_C022")


    ChrTalk(
        0xD,
        (
            "Well, Officer Kate? How do you feel\x01",
            "about this assignment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Let me take a look...\x01",
            "There's been more orbal vehicles on the road,\x01",
            "so I think I'll go to Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I'm a veteran, after all!\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "O-Okay. I guess you can handle it\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C13C")

    OP_4C(0xD, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_93(0xD, 0xB4, 0x0)
    OP_93(0xF, 0x0, 0x0)
    Return()

    # Function_19_BEA0 end

    def Function_20_C153(): pass

    label("Function_20_C153")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C164")
    Jump("loc_CA15")

    label("loc_C164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C355")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C294")

    ChrTalk(
        0xFE,
        "Hey, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something this huge could lead to mass panic,\x01",
            "so we're keeping people in the dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You'd do well to keep that in mind.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C250")

    ChrTalk(
        0x101,
        (
            "#0000FS-Sure...\x01",
            "(What's he even talking about?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C28C")

    label("loc_C250")


    ChrTalk(
        0x101,
        (
            "#0000FS-Sure...\x01",
            "(It's looking pretty serious, then...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C28C")

    SetScenarioFlags(0x0, 6)
    Jump("loc_C350")

    label("loc_C294")

    OP_4B(0xD, 0xFF)
    OP_93(0xFE, 0x10E, 0x0)
    TurnDirection(0xD, 0xFE, 0)

    ChrTalk(
        0xFE,
        "Hey, listen up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The First and Second Divisions are taking care\x01",
            "of the station and airport, so it's up to all of you\x01",
            "to handle the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Sir, yes, sir!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)

    label("loc_C350")

    Jump("loc_CA15")

    label("loc_C355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C363")
    Jump("loc_CA15")

    label("loc_C363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C371")
    Jump("loc_CA15")

    label("loc_C371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C37F")
    Jump("loc_CA15")

    label("loc_C37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_C38D")
    Jump("loc_CA15")

    label("loc_C38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C770")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5D9")

    ChrTalk(
        0xFE,
        (
            "Oh, it's you guys.\x01",
            "You're those newbies under Sergei's command, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Interesting. Who thought he'd create a new division\x01",
            "this late into his career? I guess Sergei's trying his\x01",
            "hardest to innovate the CPD.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm impressed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FAre you acquainted with Chief Sergei?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, pretty much.\x01",
            "That guy used to be one of the most\x01",
            "conspicuous officers on the force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, see to it that you don't\x01",
            "cause him too much trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's still got a while longer on the force.\x01",
            "He's not an old geezer on the verge of\x01",
            "retirement, unlike myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 7)
    Jump("loc_C76B")

    label("loc_C5D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6FF")

    ChrTalk(
        0xFE,
        (
            "By the way...\x01",
            "Are you fans of black tea or coffee?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I don't know about you, but I'm a huge fan of coffee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, it'd be great if I had a coffee grinder at\x01",
            "my desk.\x02",
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
    SetScenarioFlags(0x0, 6)
    Jump("loc_C76B")

    label("loc_C6FF")


    ChrTalk(
        0xFE,
        "I suppose canned coffee will have to suffice, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I should grab a drink with Sergei sometime.\x02",
    )

    CloseMessageWindow()

    label("loc_C76B")

    Jump("loc_CA15")

    label("loc_C770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_C88D")
    OP_93(0xFE, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C855")

    ChrTalk(
        0xFE,
        (
            "Ugh. I have to deal with the assignments every year,\x01",
            "but it never gets any easier. What a pain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Here? Or, maybe here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, how I'd love for someone else\x01",
            "to decide them in my stead.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_C888")

    label("loc_C855")


    ChrTalk(
        0xFE,
        (
            "Maybe I should just go with my\x01",
            "original plan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C888")

    Jump("loc_CA15")

    label("loc_C88D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_C89B")
    Jump("loc_CA15")

    label("loc_C89B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_C8A9")
    Jump("loc_CA15")

    label("loc_C8A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_C8B7")
    Jump("loc_CA15")

    label("loc_C8B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_CA15")
    OP_93(0xFE, 0x10E, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C960")

    ChrTalk(
        0xFE,
        (
            "Argh... Okay, I think it's about time\x01",
            "I get started...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "One, two, three...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wait, what the...?\x01",
            "Why aren't they all here?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_CA15")

    label("loc_C960")

    TurnDirection(0xFE, 0xF, 0)

    ChrTalk(
        0xFE,
        (
            "Officer Kate.\x01",
            "Could you do me a favor and call the rest of them?\x01",
            "I can't get started at all...\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0xFE, 0)

    ChrTalk(
        0xF,
        (
            "Yes, Chief.\x01",
            "Wait just a moment, please!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x10E, 0x0)
    OP_93(0xF, 0x10E, 0x0)
    OP_4C(0xF, 0xFF)

    label("loc_CA15")

    TalkEnd(0xFE)
    Return()

    # Function_20_C153 end

    def Function_21_CA19(): pass

    label("Function_21_CA19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD6F")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Whoa... Is that you, Lloyd?\x01",
            "Long time no see!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FOh, Kate... It's good to see you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FThe heck? She an acquaintance, or somethin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, she's one of my superiors who'd drop by\x01",
            "the academy every once in a while.\x02\x03",
            "I learned a lot under Kate. Everything from\x01",
            "firing a gun to regular classroom lessons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd was such a natural that\x01",
            "I ended up having a ton of fun\x01",
            "teaching him everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like the division you were assigned\x01",
            "to is a bit unorthodox. But I believe in you,\x01",
            "so I'm sure you'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And don't forget: Good things come to those\x01",
            "who work hard. I promise it'll pay off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FY-Yeah, I'm sure you're right.\x01",
            "(Now I'm even MORE worried...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108F(I think it's clear that the Special Support Section\x01",
            "is the outcast of the CPD.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 7)
    Jump("loc_D035")

    label("loc_CD6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_CD80")
    Call(0, 19)
    Jump("loc_D035")

    label("loc_CD80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_CE56")

    ChrTalk(
        0xFE,
        "Let's see, the roster sheets, and...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We were supposed to use the meeting room\x01",
            "upstairs, but the First Division took it for\x01",
            "themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those guys always do whatever the hell\x01",
            "they want.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D035")

    label("loc_CE56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_CF04")

    ChrTalk(
        0xFE,
        (
            "Phew, I'm glad we can send the rookies\x01",
            "out into the world without any worries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to report to the chief after I've\x01",
            "gathered all written reports.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D035")

    label("loc_CF04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_D035")

    ChrTalk(
        0xFE,
        (
            "Let's see... Should I be tough on\x01",
            "you rookies?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh. In case you didn't know, we're a part\x01",
            "of the Metropolitan Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our main duty is to patrol the city.\x01",
            "I hope we bump into each other again!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D035")

    ChrTalk(
        0x101,
        (
            "#0000FYeah, likewise. It's nice to finally be\x01",
            "on the force together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_D035")

    TalkEnd(0xFE)
    Return()

    # Function_21_CA19 end

    def Function_22_D039(): pass

    label("Function_22_D039")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D11C")

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sheesh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got nothing but meetings after this.\x01",
            "*sigh* My shoulders are so stiff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(Ugh... Isn't she from the First Division?)\x02\x03",
            "(Well, I guess she has\x01",
            "a right to complain...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_D16D")

    label("loc_D11C")


    ChrTalk(
        0xFE,
        (
            "I've got nothing but meetings after this.\x01",
            "*sigh* My shoulders are so stiff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D16D")

    TalkEnd(0xFE)
    Return()

    # Function_22_D039 end

    def Function_23_D171(): pass

    label("Function_23_D171")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D27F")

    ChrTalk(
        0x101,
        "#0005FOh? I'm surprised to see you here, Chief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FNo kiddin'. You get summoned here by\x01",
            "the Vice Commish Jackass, or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1006FI have a meeting to attend at headquarters,\x01",
            "so watch your mouth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FHaha. My bad, Chief.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_D367")

    label("loc_D27F")


    ChrTalk(
        0xFE,
        (
            "#1006FActually, I've got a bunch of meetings I need to\x01",
            "attend because of the Anniversary Festival.\x02\x03",
            "#1000FDon't bother worrying about me, though.\x01",
            "Just focus on your own tasks, and if you\x01",
            "have any reports, I'll hear them later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D367")

    TalkEnd(0xFE)
    Return()

    # Function_23_D171 end

    def Function_24_D36B(): pass

    label("Function_24_D36B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D3FF")
    Jump("loc_D449")

    label("loc_D3FF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D41F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D449")

    label("loc_D41F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D43F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D449")

    label("loc_D43F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D449")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I can't believe someone would target the airport...\x01",
            "Are we dealing with terrorists?!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_D36B end

    def Function_25_D4D0(): pass

    label("Function_25_D4D0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D564")
    Jump("loc_D5AE")

    label("loc_D564")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D584")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D5AE")

    label("loc_D584")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D5A4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D5AE")

    label("loc_D5A4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D5AE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "I was summoned here while I was off duty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "To think it's blown up this much...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_D4D0 end

    def Function_26_D633(): pass

    label("Function_26_D633")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D6C7")
    Jump("loc_D711")

    label("loc_D6C7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D6E7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D711")

    label("loc_D6E7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D707")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D711")

    label("loc_D707")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D711")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Another incident? This year doesn't\x01",
            "know when to give up.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_D633 end

    def Function_27_D77D(): pass

    label("Function_27_D77D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D876")

    ChrTalk(
        0xFE,
        "Uhh, where'd it go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't tell me it's...there?\x01",
            "No, there's no way that's possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(What's the vice commissioner going on about?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(He's trying his hardest to do...whatever\x01",
            "he's doing.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_D8A9")

    label("loc_D876")


    ChrTalk(
        0xFE,
        "Must...find it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhh, where'd it go...?\x02",
    )

    CloseMessageWindow()

    label("loc_D8A9")

    Jump("loc_D9C1")

    label("loc_D8AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_D9BE")

    ChrTalk(
        0x12,
        (
            "I'm trying to find a wedding ring\x01",
            "imbued with a carnelian gemstone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Inform me at once if you find it!\x01",
            "Do I make myself clear?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(We might be able to find the ring\x01",
            "if we use Zeit's nose to sniff it out.)\x02\x03",
            "#0000F(Let's try asking Zeit.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D9C1")

    label("loc_D9BE")

    Call(0, 29)

    label("loc_D9C1")

    TalkEnd(0xFE)
    Return()

    # Function_27_D77D end

    def Function_28_D9C5(): pass

    label("Function_28_D9C5")

    EventBegin(0x0)
    Fade(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_DA5B")
    OP_4B(0xA, 0xFF)
    OP_68(-13360, 1500, 10430, 0)
    MoveCamera(39, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21320, 0)
    SetChrPos(0x101, -11800, 0, 11000, 0)
    SetChrPos(0x102, -12800, 0, 10750, 0)
    SetChrPos(0x103, -11800, 0, 9500, 0)
    SetChrPos(0x104, -12800, 0, 9250, 0)
    OP_93(0xB, 0xB4, 0x0)
    SetChrSubChip(0xB, 0x0)
    Jump("loc_DB67")

    label("loc_DA5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_DAEA")
    OP_4B(0xA, 0xFF)
    OP_68(-125470, 1200, 18490, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24860, 0)
    SetChrPos(0x101, -125400, 0, 18000, 0)
    SetChrPos(0x102, -126400, 0, 17750, 45)
    SetChrPos(0x103, -124000, 0, 18390, 315)
    SetChrPos(0x104, -123620, 0, 19500, 270)
    OP_93(0xB, 0xB4, 0x0)
    SetChrSubChip(0xB, 0x0)
    Jump("loc_DB67")

    label("loc_DAEA")

    OP_68(-11160, 1100, 12770, 0)
    MoveCamera(39, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20160, 0)
    SetChrPos(0x101, -10500, 0, 12500, 0)
    SetChrPos(0x102, -11500, 0, 12250, 0)
    SetChrPos(0x103, -10500, 0, 11000, 0)
    SetChrPos(0x104, -11500, 0, 10750, 0)
    OP_93(0xB, 0xB4, 0x0)
    SetChrSubChip(0xB, 0x0)

    label("loc_DB67")

    OP_0D()

    ChrTalk(
        0x101,
        "#11P#0000FHow's it going, Detective Raymond?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5POh, it's the SSS guys. Got some\x01",
            "business at HQ to tend to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0304FHeh heh heh... I'll admit, you got guts\x01",
            "playin' dumb like this...\x02\x03",
            "#0307F#4SBut the real culprit here...is YOU!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x104, 500)

    ChrTalk(
        0xB,
        "#5PWH-WHAAAAAAT?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(500)

    def lambda_DCCA():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DCCA)

    def lambda_DCD7():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DCD7)

    def lambda_DCE4():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DCE4)
    Sleep(500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x101,
        "#5P#0006FRandy... Cool it with the pranks, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0203FIt was not even clever.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x104,
        (
            "#12P#0306FOh, c'mon. I'm a police officer, aren't I?\x01",
            "I had to pull out that line at least once\x01",
            "in my life, y'know?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        "#5PU-Uh... What's he going on about?\x02",
    )

    CloseMessageWindow()

    def lambda_DE0D():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DE0D)

    def lambda_DE1A():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DE1A)

    def lambda_DE27():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DE27)

    def lambda_DE34():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DE34)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        (
            "#12P#0103FAhem. Sorry about that, Detective Raymond.\x01",
            "We're here about a request from the library.\x02\x03",
            "#0100FYou wouldn't happen to have an overdue\x01",
            "library book, would you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#5PAw crap, now that you mention it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PYeah, I'm pretty sure I have one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PYeah, I, uh... Yeah... Haha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0006FYou, uh...\x02\x03",
            "#0012FYou lost the book, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PPsh, n-no... I don't...think...so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0211FWhy the uncertainty, then?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_E0A2")
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        (
            "#11PRaymond. Stop standing there\x01",
            "and go find it!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    ChrTalk(
        0xB,
        "#5PY-Yes, sir!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E0CD")

    label("loc_E0A2")


    ChrTalk(
        0xB,
        "#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PI-I'll go look for it!\x02",
    )

    CloseMessageWindow()

    label("loc_E0CD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_93(0xA, 0x5A, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xB,
        "#5PYes! Found it! This is the one!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D7, 1)

    ChrTalk(
        0x101,
        "#11P#0003FPhew, thank goodness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0306FReally left us in suspense there, Raymond.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0105FAnyway, why check out this particular book?\x02\x03",
            "Isn't this book about historic female figures\x01",
            "who've accomplished outstanding deeds?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PY-Yeah, well, I thought it was a photo album with\x01",
            "a bunch of hot chicks from across the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PWhen I found out it wasn't what I thought it was,\x01",
            "I kinda just left it in my drawer and forgot about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0206FI do not think the library is the right\x01",
            "place to search for that kind of book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0012FW-Well... We got the book back,\x01",
            "so all's well that ends well.\x02\x03",
            "#0000FWe appreciate your cooperation,\x01",
            "Detective Raymond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PAny time, guys.\x02",
    )

    CloseMessageWindow()
    OP_29(0x5, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E45B")
    OP_29(0x5, 0x1, 0x1F)

    label("loc_E45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_E47E")
    SetChrPos(0x0, -12300, 0, 11000, 0)
    OP_4C(0xA, 0xFF)
    Jump("loc_E4B2")

    label("loc_E47E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_E4A1")
    SetChrPos(0x0, -125400, 0, 18000, 0)
    OP_4C(0xA, 0xFF)
    Jump("loc_E4B2")

    label("loc_E4A1")

    SetChrPos(0x0, -11000, 0, 12500, 0)

    label("loc_E4B2")

    EventEnd(0x5)
    Return()

    # Function_28_D9C5 end

    def Function_29_E4B5(): pass

    label("Function_29_E4B5")

    EventBegin(0x0)
    Fade(500)
    OP_68(-57380, 1500, 17520, 0)
    MoveCamera(40, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -56800, 0, 17500, 0)
    SetChrPos(0x102, -57800, 0, 17250, 0)
    SetChrPos(0x103, -56800, 0, 16000, 0)
    SetChrPos(0x104, -57800, 0, 15750, 0)
    SetChrPos(0x12, -57300, 0, 19000, 0)
    SetChrSubChip(0x12, 0x0)
    OP_0D()

    ChrTalk(
        0x12,
        "#5PNo, no, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5PUgh, where in the world is it?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_93(0x12, 0xB4, 0x2EE)
    Sleep(750)

    ChrTalk(
        0x12,
        "#5PHmm, the Special Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PHmph, go on! Scram!\x01",
            "Can't you see I'm busy?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0005FR-Right... Sorry about that.\x01",
            "(Huh? Is that smell...booze?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0306FVice Commish Jackass seems a lil' more\x01",
            "pissed off than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FI do not particularly enjoy being scolded\x01",
            "for the sport of it, so let's escape his\x01",
            "temper while we still can.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-59280, 1700, 16460, 2000)
    MoveCamera(77, 25, 0, 2000)

    def lambda_E72E():
        OP_97(0x104, 0xFFFFF736, 0x0, 0xFFFFF736, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E72E)
    Sleep(50)

    def lambda_E74B():
        OP_97(0x103, 0xFFFFF830, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E74B)
    Sleep(50)

    def lambda_E768():
        OP_97(0x102, 0xFFFFF92A, 0x0, 0xFFFFF92A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E768)
    Sleep(50)

    def lambda_E785():
        OP_97(0x101, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E785)
    Sleep(200)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x12, 0xE1, 0x2EE)

    ChrTalk(
        0x12,
        "#5PW-Wait a minute!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    def lambda_E84D():
        TurnDirection(0x101, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E84D)

    def lambda_E85A():
        TurnDirection(0x102, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E85A)

    def lambda_E867():
        TurnDirection(0x103, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E867)

    def lambda_E874():
        TurnDirection(0x104, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E874)
    Sleep(500)

    ChrTalk(
        0x12,
        (
            "#5PHave you stumbled across a\x01",
            "ring anywhere in the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PIt's a wedding ring garnished with\x01",
            "the most beautiful carnelian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FA wedding ring?\x01",
            "(Where'd this topic pop up from?)\x02\x03",
            "#0000FUh, I don't think so. Have you, Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0103FNo, I don't recall coming across\x01",
            "anything like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FSame. Nada.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FLikewise. Vice Commissioner Pierre, did you\x01",
            "perhaps misplace your wedding ring?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5PUgh...\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x12, 1, 0, 30)
    Sleep(500)

    ChrTalk(
        0x12,
        "#5POh, sweet Aidios... If she finds out about this...\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x12, 0x1)
    OP_64(0x12)
    OP_95(0x12, -57300, 0, 19000, 2000, 0x0)
    OP_A6(0x12, 0x0, 0x32, 0x190, 0xBB8)

    ChrTalk(
        0x12,
        "#5P*shudder*\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x12, 1, 0, 30)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#0003F(It sounds like the vice comissioner's wife\x01",
            "really has him on a leash...)\x02\x03",
            "#0000FUmm, sir. We could possibly track it down\x01",
            "for you, if you give us a little bit more\x01",
            "information.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x12, 0x1)
    OP_64(0x12)
    OP_95(0x12, -57300, 0, 19000, 2000, 0x0)
    OP_93(0x12, 0xE1, 0x2EE)

    ChrTalk(
        0x12,
        "#5PR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5P*cough* It's nothing to fuss about, really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PLast night, I merely lost sight of\x01",
            "my wedding ring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5PAND IT'S NOWHERE TO BE FOUND!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PJust like I thought, I must have dropped it\x01",
            "somewhere in the Entertainment District...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0105FThe Entertainment District?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PDon't give me those condescending looks.\x01",
            "I just went to relax and have a few drinks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PAfterwards, I played a few games of roulette\x01",
            "at the casino and returned home... That's it!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x12,
        (
            "#5PAt that time, I'm positive my\x01",
            "ring was on this very finger!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P#5PI was a little tipsy, but, for some reason, I don't\x01",
            "remember anything after I left the Barca Casino...\x01",
            "That's the truth, I swear!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FYou do not have any memories after leaving\x01",
            "Barca?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5PHmph. No, not a single one!\x02",
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
        0x104,
        (
            "#12P#0306F(This dude sounds like he blacked out.\x01",
            "Smell of booze is still coverin' him.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0101F(If he dropped a tiny wedding ring in an\x01",
            "area that massive...the odds of finding\x01",
            "it aren't in our favor.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006F(Yeah, if the vice commissioner was as drunk as we\x01",
            "think he was, the responsibility is entirely his...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#0000FExcuse us, Vice Commissioner. Do you have\x01",
            "a handkerchief or anything similar on you?\x02\x03",
            "We might be able to pinpoint your ring's location\x01",
            "if we can borrow it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PWh-What?\x01",
            "Do you have some plan in mind?\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x101, -57800, 0, 18000, 2000, 0x0)
    OP_93(0x101, 0x2D, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x33D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x33D, 1)
    OP_98(0x101, 0xFFFFFF06, 0x0, 0xFFFFFC18, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        "#12P#0000FYeah, I do. Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0205F(You have lost me, Lloyd. What do you\x01",
            "plan to do with something like this?)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#5P#0000F(Well, I thought we could try to use\x01",
            "Zeit's nose to track down his scent.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#0000F(He seems to be having a panic\x01",
            "attack, so why don't we ask\x01",
            "Zeit to help us out later?)\x02",
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
            "[Lost Wedding Ring]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x15, 0x4, 0x2)
    SetChrPos(0x0, -58800, 30, 15500, 45)
    EventEnd(0x5)
    Return()

    # Function_29_E4B5 end

    def Function_30_F422(): pass

    label("Function_30_F422")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F474")
    OP_95(0x12, -57800, 0, 19000, 2000, 0x0)
    Sleep(500)
    OP_93(0x12, 0x5A, 0x1F4)
    Sleep(500)
    OP_95(0x12, -56800, 0, 19000, 2000, 0x0)
    Sleep(500)
    OP_93(0x12, 0x10E, 0x1F4)
    Sleep(500)
    Jump("Function_30_F422")

    label("loc_F474")

    Return()

    # Function_30_F422 end

    def Function_31_F475(): pass

    label("Function_31_F475")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-12810, 1500, 17000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, -12810, 0, 17000, 180)
    SetChrPos(0x1, -12810, 0, 17000, 180)
    SetChrPos(0x2, -12810, 0, 17000, 180)
    SetChrPos(0x3, -12810, 0, 17000, 180)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_31_F475 end

    def Function_32_F500(): pass

    label("Function_32_F500")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(2330, 1510, 13680, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 3000, 0, 13500, 0)
    SetChrPos(0x109, 3750, 0, 13000, 0)
    SetChrPos(0x102, 2250, 0, 12500, 0)
    SetChrPos(0x103, 3500, 0, 12000, 0)
    SetChrPos(0x104, 2250, 0, 11500, 0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#5P#1905FHiya, everyone! Oh, and you\x01",
            "still have Noey with you, too?!\x02\x03",
            "#1900FDid you guys run into a snag while\x01",
            "you were investigating those ruins?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#0500FNo, not quite...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FWe're actually here to speak to you, Fran.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#5P#1905FWith me? D-Did I do something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FN-No. We're in the middle of an important request.\x02\x03",
            "#0000FYou see, there's a tourist claiming that you helped\x01",
            "him during the last day of the Anniversary Festival...\x02\x03",
            "You apparently helped him find his wallet.\x01",
            "Does that ring any bells?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1903FHmm... A wallet...? Lemme think about\x01",
            "that for a second...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#5P#1900FOh, right! I DO remember that!\x02\x03",
            "He's a traveler from Liberl, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FSo he really DID meet Fran.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1900FBoy, let me tell you. That was one hard day.\x02\x03",
            "#1904FI was on my way home from work, when I\x01",
            "ran into a man on the verge of tears...\x01",
            "I knew I couldn't just leave him like that.\x02\x03",
            "#1900FWe were out past sundown trying to track\x01",
            "down that darn wallet of his!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FLeave it to Fran to drop everything to help\x01",
            "some poor schmuck she doesn't even know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1909FWell, I AM a member of the police force.\x01",
            "It's my duty to help those in need, too!\x02\x03",
            "#1903FI called HQ over and over again to\x01",
            "see if the wallet got turned in...\x02\x03",
            "#1900FFunnily enough, we found it under his\x01",
            "bed at the inn he was staying at. I was\x01",
            "relieved it wasn't stolen, at least.\x02",
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
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#12P#0203FSo, it was all a false alarm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1900FAnyway... What did you need from me?\x01",
            "Did something happen to him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#0503FA-Actually, we found out his name is Anton,\x01",
            "and...\x02\x03",
            "#0500F...he's still here in Crossbell City, even though\x01",
            "the festival is well over.\x02\x03",
            "He's been trying to track you down for weeks,\x01",
            "and he doesn't want to leave until he's had\x01",
            "the chance to thank you.\x02\x03",
            "That's why his friend submitted a request\x01",
            "to the SSS to help him out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1900FWow, really? He's going to make\x01",
            "me blush...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FWhat do you say, Fran? Can you do it?\x02\x03",
            "#0003FNo one's forcing you to meet him, so you have\x01",
            "every right to refuse if you don't want to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1900FNo, that's okay. I don't mind meeting him.\x01",
            "He's been trying his hardest to find me, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#11P#0505FSeriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FYou really don't have to help us just because\x01",
            "it's a support request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1900FOh, no, that's not why I'm doing it. I kinda\x01",
            "wanna meet him, too.\x02\x03",
            "#1909FDoesn't this feel so exciting?\x02\x03",
            "#1906FOh, but I might not be able to make time\x01",
            "for him, considering I'm working...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FIf that's the case, then it's out of\x01",
            "our hands.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x1F4)

    ChrTalk(
        0x8,
        "#6PExcuse me, everyone.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_68(1600, 1500, 14500, 1500)

    def lambda_10148():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10148)

    def lambda_10155():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10155)

    def lambda_10162():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10162)

    def lambda_1016F():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1016F)

    def lambda_1017C():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1017C)

    def lambda_10189():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10189)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#11P#1905FWhat's up, Rebecca?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PI'm sorry for interrupting your conversation\x01",
            "like this, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P...it's almost time for Fran's lunch break, so\x01",
            "why don't you ask him to meet you during it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#1905FReally? Do you mind?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PIt's a little unorthodox, since you're\x01",
            "technically on duty, but you should\x01",
            "have enough time to meet.\x02\x03",
            "As long as you do it during your break,\x01",
            "I'll be able to hold down the fort.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#11P#0506F(Rebecca... You aren't doing this for\x01",
            "your own amusement, are you?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#1900FWell, since you're going out of your way\x01",
            "to help me out, I'll accept your offer!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1042A():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1042A)

    def lambda_10437():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10437)

    def lambda_10444():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10444)

    def lambda_10451():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10451)

    def lambda_1045E():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1045E)

    def lambda_1046B():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1046B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x9,
        (
            "#5P#1900FWell, then, about this little rendezvous...\x01",
            "Would Vingt-Sept in Central Square\x01",
            "be all right?\x02\x03",
            "I can head there in a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FW-Well, as long as you're okay with it...\x02\x03",
            "#0000FWe should go and tell Anton the plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1909FMake sure he knows I'm looking\x01",
            "forward to it, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#0501F(Fran...? Don't tell me she's actually\x01",
            "interested in this Anton guy...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FWhat's up, Noel? You look kinda\x01",
            "conflicted.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#11P#0503FIt's nothing, Randy. I'm fine.\x02\x03",
            "#0500FAnyway, Lloyd. Let's go report the\x01",
            "news to Anton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FSounds good.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 3000, 0, 13500, 0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_29(0x2A, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_32_F500 end

    def Function_33_1071C(): pass

    label("Function_33_1071C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 900, 15000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 0, 0, 1000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 900, 7000, 5000)
    SetCameraDistance(24500, 5000)
    FadeToBright(2000, 0)
    OP_6F(0x11)

    def lambda_1079C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1079C)

    def lambda_107AD():
        OP_95(0xFE, 0, 0, 5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_107AD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        (
            "#0100165V#0000F#4P(The Crossbell Police Department.\x01",
            "Definitely not my first time here...)\x02\x03",
            "#0100166V#0004F(Hard to believe that this is going to\x01",
            "be my workplace from here on out.)\x02\x03",
            "#0100167V#0001F(Well, then, enough standing around.\x01",
            "I should go introduce myself to the\x01",
            "receptionist.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_32(0x0, 0x0, 0x3)
    RemoveCraft(0x0, 0xFFFF)
    OP_38(0x0, 0x80, 0x1)
    OP_42(0x0, 0x3E8, 0xFF)
    OP_42(0x0, 0x5DC, 0xFF)
    OP_42(0x0, 0x640, 0xFF)
    AddCraft(0x0, 0x96)
    AddCraft(0x0, 0xFA)
    SetChrChipPat(0x0, 0x6, 0xFA)
    SetChrPos(0x0, 0, 0, 4500, 0)
    SetScenarioFlags(0x40, 1)
    OP_C5(0x1, 0x0)
    OP_C5(0x1, 0x4)
    OP_1B(0x0, 0x0, 0x2E)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_33_1071C end

    def Function_34_10940(): pass

    label("Function_34_10940")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(1000)
    OP_68(-100, 1000, 14000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -100, 0, 13000, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01900.itp")
    OP_0D()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    BeginChrThread(0x9, 1, 0, 35)
    Sleep(500)
    SetChrName("Receptionist")

    AnonymousTalk(
        0xFF,
        (
            "#0100168VGood day, and welcome to the\x01",
            "Crossbell Police Department.\x02\x03",
            "#0100169VHow can I help you?\x02",
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

    ChrTalk(
        0x101,
        (
            "#0100170V#7P#0005FUm, well...\x02\x03",
            "#0100171V#0003FMy name is Lloyd Bannings, and\x01",
            "today's my first day on the job.\x02\x03",
            "#0100172V#0000FIt's nice to meet you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x9,
        "Receptionist",
        (
            "#0100173V#5P#1902FOh, is that right?\x02\x03",
            "#0100174V#1909FHeehee, that's wonderful!\x01",
            "I'm always happy to see new\x01",
            "members joining the force.\x02\x03",
            "#0100175V#1905FHmm, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(500)

    NpcTalk(
        0x9,
        "Receptionist",
        (
            "#0100176V#5P#1903FThis is pretty abnormal.\x02\x03",
            "#0100177VThere's no information in the system about\x01",
            "a new recruit coming for assignment today...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(300)

    NpcTalk(
        0x9,
        "Receptionist",
        (
            "#0100178V#5P#1900FUm, are you sure you weren't supposed to\x01",
            "go to the Crossbell Guardian Force?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100179V#7P#0000FYes, I'm positive that I've been assigned to\x01",
            "the Crossbell Police Department.\x02\x03",
            "#0100180VIf you need proof, I can show you my detective\x01",
            "qualifications I earned at the police academy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x9,
        "Receptionist",
        (
            "#0100181V#5P#1905FWow! You managed to pass the detective\x01",
            "exam?!\x02\x03",
            "#0100182V#1902FThat's amazing! It's not every day you\x01",
            "see a newcomer this qualified!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100183V#7P#0012FN-No, it's not a big deal or anything...\x01",
            "I'm pretty sure I just got lucky.\x02\x03",
            "#0100184V#0002FAnd besides, I was apparently the only\x01",
            "person that took the exam this time.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Receptionist",
        (
            "#0100185V#5P#1909FOh, come on. No need to be so\x01",
            "modest.\x02\x03",
            "#0100186V#1905FBut, this is really bizarre...\x01",
            "We should have been notified\x01",
            "of your assignment already...\x02\x03",
            "#0100187V#1900FPardon me asking, but do you\x01",
            "know what division you've been\x01",
            "assigned to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100188V#7P#0006FO-Oh, about that...\x02\x03",
            "#0100189V#0000FI think it was called something like\x01",
            "the 'Special Support Section'?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Receptionist",
        "#0100190V#5P#1905FThe 'Special Support Section'?\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1100)
    Sound(2082, 255, 100, 0)
    Sleep(600)

    NpcTalk(
        0x9,
        "Receptionist",
        (
            "#0100191V#5P#1901FUhhh...do we even have a division\x01",
            "with that name?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0100192V#7P#0011FW-Wait, it doesn't even exist?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Receptionist",
        (
            "#0100193V#5P#1901FPlease wait a moment.\x02\x03",
            "#0100194VI think I've heard that name somewhere,\x01",
            "but I'm having a hard time remembering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100195V#7P#0011F...\x02",
    )

    CloseMessageWindow()
    OP_68(-2600, 1000, 14000, 1500)
    OP_6F(0x1)
    SetChrPos(0x11, -13000, 0, 11000, 90)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)

    NpcTalk(
        0x11,
        "Man's Voice",
        "#0100196VOh, you made it.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x11, 3, 0, 36)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_11377():

        label("loc_11377")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_11377")

    QueueWorkItem2(0x9, 2, lambda_11377)
    Sleep(50)

    def lambda_1138C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1138C)
    OP_68(-100, 900, 14000, 4000)
    OP_6F(0x1)

    NpcTalk(
        0x9,
        "Receptionist",
        "#0100197V#5P#1900FAh, Chief Sergei!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 3)
    Sleep(300)

    NpcTalk(
        0x11,
        "Unshaven Man",
        (
            "#0100198V#1000F#6PI can take it from here, Fran.\x02\x03",
            "#0100199VHe's one of the recruits for my division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0100200V#5P#1905FOh, he is?\x02\x03",
            "#0100201V#1900FSo, that's the name of the new division\x01",
            "you're starting?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x11,
        "Unshaven Man",
        (
            "#0100202V#1003F#6PYep, I look forward to working with you.\x02\x03",
            "#0100203V#1002FThen again, who knows if this team will\x01",
            "last for more than six months?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#0100204V#5P#1909FOh, hahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100205V#11P#0011FUmm, sir?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Unshaven Man")

    AnonymousTalk(
        0xFF,
        (
            "#0100206VI'm Sergei Lou, chief of the\x01",
            "Special Support Section.\x02\x03",
            "#0100207VSo you're Lloyd, huh?\x02",
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

    ChrTalk(
        0x101,
        (
            "#0100208V#11P#0001FY-Yes, sir. My name is Lloyd Bannings.\x02\x03",
            "#0100209VReporting for duty to the Crossbell\x01",
            "Police Department's Special Supp--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#0100210V#1003F#6PHold the formalities for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100211V#11P#0005FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100212V#1000F#6PIt's still a little early to be reporting\x01",
            "in for your assignment.\x02\x03",
            "#0100213VJust follow me. Your new partners\x01",
            "are waiting.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x11, 3, 0, 37)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0100214V#11P#0005FHuh? W-Wait...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 3)
    OP_6F(0x1)
    EndChrThread(0x9, 0x2)
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#0100215V#5P#1909FUmmm... Well, best of luck?\x02\x03",
            "#0100216V#1901FSounds like you might have some trouble,\x01",
            "but work hard and I'm sure you'll be fine!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0100217V#7P#0012FTh-Thanks...\x01",
            "(My nerves are starting to kick in.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_68(-18500, 1000, 10000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18000, 0)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x11, -14500, 0, 10000, 270)
    SetChrPos(0x101, -11500, 0, 10000, 270)

    def lambda_119A1():
        OP_95(0xFE, -26000, 0, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_119A1)
    Sleep(50)

    def lambda_119BE():
        OP_95(0xFE, -24500, 0, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_119BE)
    PlayBGM("ed7111", 0)
    OP_68(-25500, 1000, 10000, 6000)
    SetCameraDistance(20000, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x11, 1)

    def lambda_11A04():
        OP_95(0xFE, -26000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_11A04)
    WaitChrThread(0x101, 1)

    def lambda_11A22():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11A22)
    WaitChrThread(0x11, 1)
    Sound(103, 0, 100, 0)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x0)

    def lambda_11A48():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_11A48)

    def lambda_11A59():
        OP_95(0xFE, -26000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_11A59)
    Sleep(500)

    def lambda_11A76():
        OP_95(0xFE, -26000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11A76)
    WaitChrThread(0x101, 1)

    def lambda_11A94():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11A94)

    def lambda_11AA5():
        OP_95(0xFE, -26000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11AA5)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x11, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x11, 0x2)
    EndChrThread(0x101, 0x2)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch00102.itc", 0x1E)
    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("apl/ch50006.itc", 0x21)
    SoundLoad(806)
    OP_68(-62200, 700, 16200, 0)
    MoveCamera(70, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x1)
    SetChrPos(0x11, -62700, 0, 13500, 270)
    SetChrPos(0x101, -65000, 0, 11000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x102, -60500, 150, 19800, 180)
    SetChrPos(0x103, -62500, 150, 19800, 180)
    SetChrPos(0x104, -61800, 150, 16100, 315)
    SetMapObjFrame(0xFF, "isu", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu_sd", 0x0, 0x1)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    OP_78(0x3, 0x16)
    OP_78(0x4, 0x17)
    OP_78(0x5, 0x18)
    OP_78(0x6, 0x19)
    OP_78(0x7, 0x1A)
    OP_78(0x8, 0x1B)
    OP_49()
    SetChrPos(0x16, -61500, 0, 15900, 0)
    OP_D3(0x16, 0x0, 0xFFFF5038, 0x0, 0x0)
    SetChrPos(0x17, -60500, 0, 20100, 0)
    OP_D3(0x17, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x18, -65000, 0, 15900, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x19, -62500, 0, 20100, 0)
    OP_D3(0x19, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x1A, -67500, 0, 15900, 0)
    OP_D3(0x1A, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x1B, -65000, 0, 20100, 0)
    OP_D3(0x1B, 0x0, 0x2BF20, 0x0, 0x0)
    OP_CA(0x1, 0x0, 0x0)
    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00100.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00200.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00300.itp")
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_11DCB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11DCB)

    def lambda_11DDC():
        OP_95(0xFE, -65000, 0, 13500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11DDC)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)
    SetChrName("Young Woman")

    NpcTalk(
        0x102,
        "Young Woman",
        "#0100218V#0105FOh...\x02",
    )

    CloseMessageWindow()
    SetChrName("Red-Haired Young Man")

    NpcTalk(
        0x104,
        "Red-Haired Young Man",
        (
            "#0100219V#5P#0300FWould ya look at that?\x01",
            "Our big star's finally arrived.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Girl in Black")

    NpcTalk(
        0x103,
        "Girl in Black",
        "#0100220V#0200F...\x02",
    )

    CloseMessageWindow()
    OP_68(-59320, 900, 18530, 6000)
    SetCameraDistance(20500, 6000)
    MoveCamera(45, 17, 0, 6000)
    BeginChrThread(0x11, 3, 0, 38)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 39)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)

    ChrTalk(
        0x11,
        (
            "#0100221V#1000F#5PSorry for the wait, everyone.\x01",
            "Here's our last member.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x11,
        "#0100222V#1000F#5PDon't just stand there. Introduce yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100223V#11P#0005FAh, right.\x02",
    )

    CloseMessageWindow()

    def lambda_11FE0():
        OP_95(0xFE, -58500, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11FE0)
    WaitChrThread(0x101, 1)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0100224V#0001F#11P(Hmm? All three of them look too young\x01",
            "to be senior officers of the CPD...)\x02\x03",
            "#0100225V(Are they also rookies? Then again,\x01",
            "that girl looks like she's too young to\x01",
            "even be a part of the force...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100226V#1000F#5PHey, got cotton stuck in your ears?\x02\x03",
            "#0100227VIt ain't hard, kid. Just give your name\x01",
            "and where you're from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100228V#0005F#11PS-Sorry.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#0100229VMy name is Lloyd Bannings,\x01",
            "and I was born in Crossbell.\x02\x03",
            "#0100230VUntil recently, I had been\x01",
            "living abroad.\x02\x03",
            "#0100231VBut I've decided to return home\x01",
            "in pursuit of joining the CPD.\x02\x03",
            "#0100232VI look forward to working with\x01",
            "all of you.\x02",
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
    SetChrName("Red-Haired Young Man")

    NpcTalk(
        0x104,
        "Red-Haired Young Man",
        "#0100233V#6P#0302FOh? So you're the serious type.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1361, 255, 100, 0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Red-Haired Young Man")

    AnonymousTalk(
        0xFF,
        (
            "#0100234VYo, I'm Randy. Randy Orlando.\x02\x03",
            "#0100235VMy hobbies include flirting with\x01",
            "lovely ladies, gamblin',...\x02\x03",
            "And checkin' out sexy new\x01",
            "mags like Hot Shot. Y'know, \x01",
            "that kinda stuff.\x02\x03",
            "#0100236VRemind me later and I'll let ya\x01",
            "take a peek at some of my prized\x01",
            "collections when this is all done.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    ChrTalk(
        0x101,
        "#0100237V#0011F#11PY-Your what?!\x02",
    )

    CloseMessageWindow()
    SetChrName("Young Woman")

    NpcTalk(
        0x102,
        "Young Woman",
        "#0100238V#5P#0103FAhem.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1171, 255, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Young Woman")

    AnonymousTalk(
        0xFF,
        (
            "#0100239VPleased to meet you. My name is\x01",
            "Elie MacDowell.\x02\x03",
            "#0100240VI'm Crossbellan, much like yourself.\x02\x03",
            "#0100241VI look forward to working with you.\x02",
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

    ChrTalk(
        0x101,
        "#0100242V#0005F#11PL-Likewise...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1267, 255, 100, 0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Girl in Black")

    AnonymousTalk(
        0xFF,
        (
            "#0100243VTio Plato, Leman State.\x02\x03",
            "#0100244VA pleasure to meet you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    ChrTalk(
        0x101,
        "#0100245V#0012F#11PYeah, you, too...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#0100246V#12P#0011FUm, Chief Sergei?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#0100247V#1000F#5PHmm, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100248V#12P#0001FI've been wondering... What exactly\x01",
            "is the Special Support Section?\x02\x03",
            "#0100249VIt's clear as day that everyone here\x01",
            "is fairly young, myself included.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100250V#1004F#5PYeah, well, we're in a unique situation here.\x02\x03",
            "#0100251VAfter all, everyone at this table is a promising\x01",
            "newcomer to the police force, just like you.\x02\x03",
            "#0100252V#1002FThat should calm your nerves, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100253V#12P#0011FI-I guess so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100254V#5P#0106FIs this really okay for a police division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100255V#6P#0309FWell, I, for one, am extremely grateful we don't\x01",
            "have any preachy old-timers bossin' us around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100256V#5P#0203F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100257V#12P#0006F(Wh-What in the world is this?)\x02\x03",
            "#0100258V#0001F(I can't shake this bad feeling\x01",
            "I have about all of this...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x11, 0x1)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#0100259V#1005F#5PSergei here...\x02\x03",
            "#0100260V#1002FHmm, that so? Appreciate it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0100261V#12P#0005F(Is that a portable communication device?)\x02\x03",
            "#0100262V(Hard to believe technology like that\x01",
            "has already been developed...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0100263V#1004F#5PYeah, roger that.\x02\x03",
            "#0100264V#1002FWe can handle things from here.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 0x0)
    Sleep(300)
    Sound(807, 0, 100, 0)
    Fade(250)
    ClearChrFlags(0x11, 0x20)
    ClearChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 0x7)
    SetChrSubChip(0x11, 0x0)
    OP_0D()
    OP_93(0x11, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#0100265V#5P#1003FAll right, greenhorns. Time to perk up.\x02\x03",
            "#0100266V#1002FYou wanted to know what kind of\x01",
            "responsibilities the SSS is going to\x01",
            "have, right?\x02\x03",
            "#0100267VI imagine this little mission will give you\x01",
            "a good idea. Get ready for a helluva ride.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_CA(0x1, 0x0, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
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
    OP_24(0x326)
    SetScenarioFlags(0x5C, 1)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_10940 end

    def Function_35_12E85(): pass

    label("Function_35_12E85")

    Sound(2080, 255, 100, 0)
    Sleep(1000)
    Sound(2081, 255, 100, 0)
    Return()

    # Function_35_12E85 end

    def Function_36_12E95(): pass

    label("Function_36_12E95")


    def lambda_12E9A():
        OP_95(0xFE, -5000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12E9A)
    WaitChrThread(0x11, 1)

    def lambda_12EB8():
        OP_95(0xFE, -2000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12EB8)
    WaitChrThread(0x11, 1)
    Return()

    # Function_36_12E95 end

    def Function_37_12ED2(): pass

    label("Function_37_12ED2")

    OP_92(0x11, 0xFFFFEC78, 0x2AF8, 0x1F4)

    def lambda_12EE4():
        OP_95(0xFE, -5000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12EE4)
    WaitChrThread(0x11, 1)

    def lambda_12F02():
        OP_95(0xFE, -13000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12F02)
    WaitChrThread(0x11, 1)
    Return()

    # Function_37_12ED2 end

    def Function_38_12F1C(): pass

    label("Function_38_12F1C")

    OP_93(0x11, 0x59, 0x1F4)

    def lambda_12F28():
        OP_95(0xFE, -58000, 0, 15000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12F28)
    WaitChrThread(0x11, 1)

    def lambda_12F46():
        OP_95(0xFE, -58000, 0, 20500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12F46)
    WaitChrThread(0x11, 1)
    OP_93(0x11, 0xE1, 0x1F4)
    Return()

    # Function_38_12F1C end

    def Function_39_12F67(): pass

    label("Function_39_12F67")


    def lambda_12F6C():
        OP_95(0xFE, -58000, 0, 15000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12F6C)
    Sleep(1000)
    SetChrFlags(0x104, 0x20)

    def lambda_12F8E():
        OP_96(0xFE, 0xFFFF0FC4, 0x96, 0x3F48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12F8E)

    def lambda_12FA8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12FA8)

    def lambda_12FB5():
        OP_D3(0xFE, 0x0, 0x0, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_12FB5)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    SetChrSubChip(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x101, 1)

    def lambda_12FEE():
        OP_95(0xFE, -58000, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12FEE)
    Sleep(300)
    SetChrSubChip(0x102, 0x1)
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_39_12F67 end

    def Function_40_1301D(): pass

    label("Function_40_1301D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-12300, 1000, 20300, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -12700, 0, 21000, 180)
    SetChrPos(0x102, -12700, 0, 21000, 180)
    SetChrPos(0x103, -12700, 0, 21000, 180)
    SetChrPos(0x104, -12700, 0, 21000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, -5000, 0, 10400, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xB, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -3700, 0, 10400, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearMapObjFlags(0x2, 0x10)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(160, 0, 100, 0)
    Sleep(1000)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    OP_68(-12700, 1000, 14200, 4000)
    MoveCamera(30, 25, 0, 4000)
    SetCameraDistance(22000, 4000)

    def lambda_131D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_131D4)

    def lambda_131E5():
        OP_96(0xFE, 0xFFFFCBA8, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_131E5)
    Sleep(600)

    def lambda_13202():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_13202)

    def lambda_13213():
        OP_96(0xFE, 0xFFFFD120, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13213)
    Sleep(600)

    def lambda_13230():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_13230)

    def lambda_13241():
        OP_96(0xFE, 0xFFFFCBA8, 0x0, 0x3A34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13241)
    Sleep(600)

    def lambda_1325E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1325E)

    def lambda_1326F():
        OP_96(0xFE, 0xFFFFD120, 0x0, 0x3A34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1326F)
    Sleep(1000)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#0100882V#6P#0008F...\x02",
    )

    CloseMessageWindow()

    def lambda_132C6():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_132C6)
    Sleep(50)

    def lambda_132D6():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_132D6)
    Sleep(50)

    def lambda_132E6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_132E6)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x104,
        (
            "#0100830V#5P#0306FGeez, man... Talk about a hell\x01",
            "of a first day on the job.\x02\x03",
            "#0100831V#0301FThat guy wants us to refuse our\x01",
            "assignment to the SSS?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100832V#12P#0103FIt's apparent that the CPD has its\x01",
            "share of internal conflict, as well...\x02\x03",
            "#0100833V#0108FI'd only heard rumors, but this\x01",
            "confirms it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100834V#5P#0208FRight. All of this is a bit different\x01",
            "than what was originally arranged.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0100835V#12P#0105FArranged?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100836V#5P#0203FSimply talking to myself.\x02\x03",
            "#0100837V#0200FMore importantly, where could\x01",
            "Chief Sergei be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100838V#5P#0301FYeah, I was wonderin' about that, too.\x02\x03",
            "#0100839VWhat's the deal with not hangin' around\x01",
            "until we finished the task HE gave us?\x02\x03",
            "#0100840V#0306FInstead, we got nagged by that sneerin'\x01",
            "jackass of a vice commissioner.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#0100841V#5P#0305FWhat's up, Lloyd? Feelin' down?\x02",
    )

    CloseMessageWindow()

    def lambda_13670():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_13670)
    Sleep(50)

    def lambda_13680():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_13680)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x102,
        (
            "#0100842V#11P#0108FWas being told to refuse your assignment\x01",
            "that big a shock?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0100843V#6P#0002FOh, no. That's not it...\x02\x03",
            "#0100844V#0006FIt's just, this place is a lot more different\x01",
            "than I had imagined...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100845V#11P#0105F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100846V#5P#0305FYeah?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100847V#5P#0200F...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Man's Voice",
        (
            "#0100848V#3PHey there, rookies. Sounds like\x01",
            "you've had a tough day.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_13889():
        OP_95(0xFE, -13300, 0, 10400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_13889)
    Sleep(150)

    def lambda_138A6():
        OP_95(0xFE, -12000, 0, 10400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_138A6)
    Sleep(300)
    OP_68(-12700, 1200, 12400, 3500)
    MoveCamera(35, 19, 0, 3500)
    SetCameraDistance(20500, 3500)

    def lambda_138E8():

        label("loc_138E8")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_138E8")

    QueueWorkItem2(0x101, 2, lambda_138E8)
    Sleep(50)

    def lambda_138FD():

        label("loc_138FD")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_138FD")

    QueueWorkItem2(0x103, 2, lambda_138FD)
    Sleep(50)

    def lambda_13912():

        label("loc_13912")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_13912")

    QueueWorkItem2(0x102, 2, lambda_13912)
    Sleep(50)

    def lambda_13927():

        label("loc_13927")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_13927")

    QueueWorkItem2(0x104, 2, lambda_13927)
    WaitChrThread(0xA, 1)

    def lambda_1393D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1393D)
    WaitChrThread(0xB, 1)

    def lambda_1394E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1394E)
    WaitChrThread(0xB, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#0100849V#0005F#5PAnd you are...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Bearded Man",
        (
            "#0100850V#12PDonovan. Chief inspector of the\x01",
            "Second Investigative Division.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Blond-Haired Man",
        "#0100851V#4PAnd I'm Raymond, of the same affiliation.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Blond-Haired Man",
        (
            "#0100852V#4PHmm, I'd heard rumors, but you really\x01",
            "DO have a kid in your squad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100853V#5P#0211F(Rude.)       \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100854V#0000F#5PNice to meet you two. I'm Lloyd Bannings.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100855V#5P#0100FMy name is Elie MacDowell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100856V#5P#0300FYo, Randy Orlando. Nice to meet'cha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#0100857V#12PLikewise. Welcome to the CPD.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#0100858V#12PI see, so you're his...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100859V#0005F#5PHuh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    ChrTalk(
        0xB,
        "#0100860V#11PChief Inspector...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#0100861V#12POh, it's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0100862V#12PAnyway, Sergei likes to come up\x01",
            "with some pretty wild ideas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0100863V#12PBidding for the citizens' approval by\x01",
            "offering a bunch of rookies like you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100864V#0011F#5P...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100865V#5P#0105FBidding...? What in the world does that mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#0100866V#12POh, really? You haven't heard about it yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0100867V#12POh, well, oops. Maybe I should\x01",
            "have kept my mouth shut.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#0100868V#4PWeeell, anyway. You guys unfortunately\x01",
            "received the short end of the stick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#0100869V#4PCan't imagine how tough your job's gonna end\x01",
            "up being. If I were you, I would've refused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100870V#0005F#5P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        (
            "#0100871V#6PIsn't it about time you grew\x01",
            "a backbone, Raymond?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0100872V#6PMaybe I should hand you over\x01",
            "to Sergei's squad, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#0100873V#11PC-C'mon, Chief Inspector...\x01",
            "Cut me some slack.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#0100874V#12PWell, I'm sure this is a lot to process, but\x01",
            "try to think carefully on whether you want\x01",
            "to work under Sergei or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0100875V#12PJust...don't attempt the impossible. If you\x01",
            "all wanted, I'd be more than happy to merge\x01",
            "the four of you into the Second Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100876V#0012F#5PTh-Thank you, sir...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)

    ChrTalk(
        0xB,
        "#0100877V#4PWell, then, work hard out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#0100878V#4PAnd, Elie, was it? How about we\x01",
            "grab a bite to eat sometime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#0100879V#4PI just discovered this awesome restaurant and--\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0xB, 500)

    def lambda_141DF():
        OP_95(0xFE, -12500, 0, 10400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_141DF)
    WaitChrThread(0xA, 1)

    def lambda_141FD():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_141FD)

    def lambda_14216():
        OP_96(0xFE, 0xFFFFCC0C, 0x0, 0x28A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14216)
    Sound(819, 0, 100, 0)
    WaitChrThread(0xA, 1)

    ChrTalk(
        0xA,
        "#0100880V#6PHey, dumbass. We're leaving!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    ChrTalk(
        0xB,
        "#0100881V#11POuch! I was just trying to be a gentleman!\x02",
    )

    CloseMessageWindow()
    OP_92(0xA, 0xFFFFC6F8, 0x2E18, 0x1F4)
    BeginChrThread(0xA, 3, 0, 41)
    BeginChrThread(0xB, 3, 0, 42)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_6F(0x79)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
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
        "#0100829V#6P#0008F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100883V#11P#0306F*sigh* They were sugarcoatin' it, but\x01",
            "I could tell they weren't kiddin' about\x01",
            "our jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100884V#5P#0206FIn any case, I am concerned about the\x01",
            "'short end of the stick' they mentioned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100885V#12P#0106FWell, let's at least go and hear the chief out.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#0100886V#11P#0101FPerhaps someone at the reception desk\x01",
            "knows where we can find him?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#0100887V#6P#0008FYeah, good call.\x02",
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_14533():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_14533)
    Sleep(50)

    def lambda_14543():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_14543)
    WaitChrThread(0x103, 2)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(1085, 255, 100, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0100888V\x07\x00",
            "#0001FHello. Lloyd Bannings speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0100889V\x07\x05",
            "Sounds like your scolding session with the\x01",
            "fox has come to an end.\x02\x03",
            "#0100890VImagine you have quite the headache, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0100891V\x07\x00",
            "#0006FYeah, that guy's a...\x02\x03",
            "#0100892V#0013FNo, wait a second! Where in the world are you?!\x02\x03",
            "#0100893VDidn't you tell us to return to the CPD?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0100894V\x07\x05",
            "Oh, right. All your luggage arrived, so I was\x01",
            "making sure the move-in went smoothly.\x02\x03",
            "#0100895VWow, look at me. Aren't I such a kind boss?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0100896V\x07\x00",
            "#0005FLuggage...? Are you at our dormitory?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0100897V\x07\x05",
            "Correct. We'll talk more\x01",
            "in detail when you get here.\x02\x03",
            "#0100898VI'm waiting, so don't dawdle.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0100899V\x07\x00",
            "#0006F*sigh* Understood.\x02\x03",
            "#0100900V#0001FSo, where exactly is the dormitory?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0100901V\x07\x05",
            "Ah, well, it's not a dormitory, per se.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0100902V\x07\x00",
            "#0011FHuh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0100903V\x07\x05",
            "Actually, it's the CPD's very own\x01",
            "Special Support Section building.\x02\x03",
            "#0100904VThe second and third floors of the\x01",
            "complex will serve as your rooms.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 0)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_1301D end

    def Function_41_14ADE(): pass

    label("Function_41_14ADE")


    def lambda_14AE3():
        OP_95(0xFE, -14600, 0, 11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14AE3)
    WaitChrThread(0xA, 1)
    OP_68(-12700, 1000, 14200, 3000)
    MoveCamera(30, 25, 0, 3000)
    SetCameraDistance(22000, 3000)

    def lambda_14B26():
        OP_95(0xFE, -14600, 0, 17100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14B26)
    WaitChrThread(0xA, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x103, 0x2)

    def lambda_14B4C():
        OP_95(0xFE, -12500, 0, 19000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14B4C)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    def lambda_14B86():
        OP_95(0xFE, -12500, 0, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14B86)
    Sleep(500)

    def lambda_14BA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_14BA3)
    WaitChrThread(0xA, 1)
    Return()

    # Function_41_14ADE end

    def Function_42_14BB4(): pass

    label("Function_42_14BB4")

    Sleep(600)

    def lambda_14BBC():
        OP_95(0xFE, -14600, 0, 11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14BBC)
    WaitChrThread(0xB, 1)
    Sleep(100)

    def lambda_14BDD():
        OP_95(0xFE, -14600, 0, 17100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14BDD)
    WaitChrThread(0xB, 1)

    def lambda_14BFB():
        OP_95(0xFE, -12500, 0, 19000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14BFB)
    WaitChrThread(0xB, 1)

    def lambda_14C19():
        OP_95(0xFE, -12500, 0, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14C19)
    Sleep(500)

    def lambda_14C36():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_14C36)
    WaitChrThread(0xB, 1)
    Sleep(300)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    Return()

    # Function_42_14BB4 end

    def Function_43_14C5F(): pass

    label("Function_43_14C5F")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-70, 1500, 13120, 0)
    MoveCamera(32, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 680, 0, 12880, 0)
    SetChrPos(0x102, -460, 0, 12880, 0)
    SetChrPos(0x103, -460, 0, 11820, 0)
    SetChrPos(0x104, 680, 0, 11820, 0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    NpcTalk(
        0x8,
        "Bespectacled Woman",
        "#5POh, my.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    NpcTalk(
        0x9,
        "Receptionist",
        "#1905F#5POh, Lloyd!\x02",
    )

    CloseMessageWindow()
    OP_95(0x9, 900, 0, 15400, 2000, 0x0)
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#0012F#12PHaha... Hello again.\x02\x03",
            "#0000FWe saw the request on the terminal,\x01",
            "so here we are...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Bespectacled Woman",
        "#5PGreat, I've been waiting for you guys.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Bespectacled Woman",
        (
            "#5PA pleasure to make your acquaintance.\x01",
            "I'm Rebecca, the head receptionist of\x01",
            "the CPD.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Receptionist",
        (
            "#1900F#5PAnd I'm Fran Seeker, also a receptionist\x01",
            "of the CPD.\x02\x03",
            "#1909FI don't think I had the chance to properly\x01",
            "introduce myself the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002F#12PYeah, I suppose you didn't. That day\x01",
            "wasn't one of our finest moments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0204F#6PWhat you mean to say is, we were scolded\x01",
            "by the vice commissioner after we let a\x01",
            "bracer steal all of our credit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011F#12PDon't remind me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F#6PT-Tio...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1909F#5PO-Oh... Yeah. Well, there's nowhere\x01",
            "to go but up, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PDon't worry too much about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe SSS was only established recently,\x01",
            "so you're bound to run into your fair\x01",
            "share of uncomfortable situations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf you all ever need a helping hand,\x01",
            "you can always rely on us, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002F#12PTh-Thanks. We appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309F#12PHaha, your kind words have put\x01",
            "this tremblin' heart at ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104F#6PThe pleasure's all ours.\x02\x03",
            "#0100FSo, do you mind explaining the additional\x01",
            "details regarding support requests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5POf course not. Let's get started.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PFirst of all, HQ has assigned a dedicated\x01",
            "operator to support the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThat's our very own Fran right here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1909F#5PIt's a pleasure to work with you all.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#0005F#12PAn operator?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105F#6PSo Fran will be supporting us via our Enigmas?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1904F#5PWell, my specialty isn't really\x01",
            "supporting you guys in the field...\x02\x03",
            "#1900FMy main duty is to help report and\x01",
            "process the completion of support\x01",
            "requests.\x02\x03",
            "This'll be done via the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301F#12PI dunno 'bout you guys, but I'm gettin'\x01",
            "real confused right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F#6PIn other words, the SSS will be accepting a\x01",
            "myriad of different requests from now on...\x02\x03",
            "#0200FAnd once we finish these requests, Fran will\x01",
            "process our reports that we submit using her\x01",
            "own terminal here at HQ.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001F#12PSo then, that means...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F#6PWe don't have to come to headquarters\x01",
            "every time we need to submit a report.\x01",
            "Is that right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PPrecisely. Once your reports are approved\x01",
            "and processed within the system, we will\x01",
            "send the proper compensation your way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PFurthermore, when your DP accumulates beyond\x01",
            "a certain threshold, your Detective Rank will also\x01",
            "increase. Feel free to ask me about that later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1909F#5PBasically, these are all my new duties\x01",
            "as the very first operator of the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0004F#12PI see. That makes sense...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F#12PSo we can avoid all those irritating\x01",
            "procedures by usin' the terminal\x01",
            "down at the SSS building, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PCorrect. It's actually a part of the\x01",
            "orbal network initiative in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTio, has the terminal at the SSS\x01",
            "been installed and tested yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0202F#6PYes, it is good to go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PGood to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, then, please allow me to explain\x01",
            "the additional details regarding your\x01",
            "support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf there's anything you don't understand,\x01",
            "don't be afraid to speak up.\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 3)
    ClearScenarioFlags(0x1, 4)
    ClearScenarioFlags(0x1, 5)
    ClearScenarioFlags(0x1, 6)
    FadeToDark(300, 0, 100)
    OP_0D()
    Call(0, 44)

    ChrTalk(
        0x8,
        (
            "#5PAll right, I believe that should wrap up\x01",
            "the explanation on support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1900F#5PWhen you return to the SSS, try pressing\x01",
            "the 'Report' option on your terminal screen.\x02\x03",
            "I'll make sure to send more support requests\x01",
            "your way as they come in!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F#12PGot it. Thanks, you two.\x02",
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
            "[Support Request Explanation]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_68(-350, 1540, 12250, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, -350, 0, 12250, 0)
    SetChrPos(0x1, -350, 0, 12250, 0)
    SetChrPos(0x2, -350, 0, 12250, 0)
    SetChrPos(0x3, -350, 0, 12250, 0)
    OP_29(0x1, 0x4, 0x10)
    OP_29(0x1, 0x1, 0x0)
    OP_29(0x1, 0x1, 0x1)
    OP_29(0x3D, 0x1, 0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_43_14C5F end

    def Function_44_15C79(): pass

    label("Function_44_15C79")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15C83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1656D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15D4A")

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "[What are support requests?]\x01",                 # 0
            "[Where do we check available requests?]\x01",      # 1
            "[How do we submit our report?]\x01",               # 2
            "[What does Detective Rank mean?]\x01",             # 3
            "Nothing else\x01",                                 # 4
        )
    )

    MenuEnd(0x1)
    Jump("loc_15DDB")

    label("loc_15D4A")


    Menu(
        1,
        -1,
        -1,
        0,
        (
            "[What are support requests?]\x01",                 # 0
            "[Where do we check available requests?]\x01",      # 1
            "[How do we submit our report?]\x01",               # 2
            "[What does Detective Rank mean?]\x01",             # 3
        )
    )

    MenuEnd(0x1)

    label("loc_15DDB")

    OP_60(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DFA")
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_15E13")

    label("loc_15DFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E13")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_15E13")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_15E3B"),
        (1, "loc_16009"),
        (2, "loc_161C9"),
        (3, "loc_16320"),
        (4, "loc_1653A"),
        (SWITCH_DEFAULT, "loc_16549"),
    )


    label("loc_15E3B")


    ChrTalk(
        0x8,
        (
            "#5PSupport requests are requests submitted\x01",
            "by various individuals to the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSupport requests vary from person to person,\x01",
            "ranging from simple assistance requests to\x01",
            "formal investigations and monster exterminations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWith the exception of a few special cases,\x01",
            "you retain the right to decide whether you'll\x01",
            "accept support requests or not...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, if you do accept them, make sure to\x01",
            "complete them within the given deadline.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_1654E")

    label("loc_16009")


    ChrTalk(
        0x8,
        (
            "#5PAs far as the current support requests go,\x01",
            "you're able to accept and report them on\x01",
            "the Special Support Section's terminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POnce you confirm them, the details will\x01",
            "also be recorded in your Detective Notebook.\x01",
            "Please try to keep track of your requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAlso, your terminal will automatically update\x01",
            "each day with new support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWe recommend that you make a habit\x01",
            "of checking the terminal each morning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1654E")

    label("loc_161C9")


    ChrTalk(
        0x8,
        (
            "#5PWhenever you complete a support request,\x01",
            "please make sure to submit your report at\x01",
            "your terminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWe'll be able to immediately process\x01",
            "it via the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBased on the contents of the requests, you'll be\x01",
            "compensated with special rewards from time to time.\x01",
            "Report your completed requests whenever you can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_1654E")

    label("loc_16320")


    ChrTalk(
        0x8,
        (
            "#5PBy completing investigations successfully and\x01",
            "finishing support requests, your achievements\x01",
            "within the CPD will be noted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYour accomplishments will be determined by the amount of\x01",
            "Detective Points--or 'DP'--earned. Extra DP may be obtained,\x01",
            "depending on your performance during missions and requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWhen your DP reaches a certain threshold,\x01",
            "you will be promoted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PCurrently, ranks are divided into 15 levels.\x01",
            "You'll be rewarded with every rank promotion,\x01",
            "so it's definitely worth the extra effort.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_1654E")

    label("loc_1653A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1654E")

    label("loc_16549")

    Jump("loc_1654E")

    label("loc_1654E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16568")
    FadeToDark(300, 0, 100)
    OP_0D()

    label("loc_16568")

    Jump("loc_15C83")

    label("loc_1656D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_44_15C79 end

    def Function_45_16578(): pass

    label("Function_45_16578")

    ClearScenarioFlags(0x2, 1)
    ClearScenarioFlags(0x2, 2)
    ClearScenarioFlags(0x2, 3)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1658B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_167AE")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_165CA")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_167A9")

    label("loc_165CA")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_165FE")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_167A9")

    label("loc_165FE")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16632")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_167A9")

    label("loc_16632")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16666")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_167A9")

    label("loc_16666")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1669A")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_167A9")

    label("loc_1669A")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_166CE")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_167A9")

    label("loc_166CE")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16702")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_167A9")

    label("loc_16702")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16736")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_167A9")

    label("loc_16736")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1676D")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    SetScenarioFlags(0x2, 2)
    Jump("loc_167A9")

    label("loc_1676D")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xEE), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_167A4")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    SetScenarioFlags(0x2, 3)
    Jump("loc_167A9")

    label("loc_167A4")

    Jump("loc_167AE")

    label("loc_167A9")

    Jump("loc_1658B")

    label("loc_167AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_17563")
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-900, 1540, 13420, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19950, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16838")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0xEF, 300, 40, 13000, 0)
    SetChrPos(0x153, -900, 40, 11800, 0)
    Jump("loc_16960")

    label("loc_16838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_168AA")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)
    SetChrPos(0x109, -900, 40, 10600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_16960")

    label("loc_168AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1691C")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)
    SetChrPos(0x10A, -900, 40, 10600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_16960")

    label("loc_1691C")

    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)

    label("loc_16960")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "It looks to me like you've been hard at\x01",
            "work filling out your Combat Notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd like to record your information into\x01",
            "our database. Mind if I see it for a minute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWith pleasure.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1800)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Thank you very much. Here's your\x01",
            "notebook back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Let me gather your compensation...\x01",
            "Please accept this.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B3F")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "500 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x1.\x02",
        )
    )

    AddItemNumber(0x38E, 1)
    Jump("loc_16E65")

    label("loc_16B3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B99")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "1000 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(1000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2.\x02",
        )
    )

    AddItemNumber(0x38E, 2)
    Jump("loc_16E65")

    label("loc_16B99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BF3")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "1500 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(1500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3.\x02",
        )
    )

    AddItemNumber(0x38E, 3)
    Jump("loc_16E65")

    label("loc_16BF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C4D")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "2000 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(2000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x4.\x02",
        )
    )

    AddItemNumber(0x38E, 4)
    Jump("loc_16E65")

    label("loc_16C4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16CA7")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "2500 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(2500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5.\x02",
        )
    )

    AddItemNumber(0x38E, 5)
    Jump("loc_16E65")

    label("loc_16CA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16D01")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "3000 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(3000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x6.\x02",
        )
    )

    AddItemNumber(0x38E, 6)
    Jump("loc_16E65")

    label("loc_16D01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16D5B")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "3500 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(3500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x7.\x02",
        )
    )

    AddItemNumber(0x38E, 7)
    Jump("loc_16E65")

    label("loc_16D5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16DB5")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "4000 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(4000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x8.\x02",
        )
    )

    AddItemNumber(0x38E, 8)
    Jump("loc_16E65")

    label("loc_16DB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E0F")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "4500 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(4500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x9.\x02",
        )
    )

    AddItemNumber(0x38E, 9)
    Jump("loc_16E65")

    label("loc_16E0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E65")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "5000 mira\x07\x00",
            ".\x02",
        )
    )

    AddMira(5000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10.\x02",
        )
    )

    AddItemNumber(0x38E, 10)

    label("loc_16E65")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16E9D")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2.\x02",
        )
    )

    AddItemNumber(0x395, 2)
    CloseMessageWindow()
    Jump("loc_16ECC")

    label("loc_16E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16ECC")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x395, 1)
    CloseMessageWindow()

    label("loc_16ECC")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1702F")

    ChrTalk(
        0x8,
        (
            "Don't forget to stop by once you've\x01",
            "collected more monster data, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThanks. We will.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16FA1")

    ChrTalk(
        0x102,
        "#0100FOf course. We'll see to it that we visit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1702A")

    label("loc_16FA1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16FE8")

    ChrTalk(
        0x103,
        "#0200FNo need to worry. I will analyze more.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1702A")

    label("loc_16FE8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1702A")

    ChrTalk(
        0x104,
        "#0300FYou better watch your backs, monsters!\x02",
    )

    CloseMessageWindow()

    label("loc_1702A")

    Jump("loc_174E0")

    label("loc_1702F")


    ChrTalk(
        0x8,
        (
            "Thank you so much for going out of your\x01",
            "way to gather this much data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You see, I asked all the other detectives\x01",
            "to help out, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...but I think the Special Support Section\x01",
            "were the only ones who took it seriously.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17179")

    ChrTalk(
        0x104,
        (
            "#0300FYou know us. We're bustin' our\x01",
            "asses all over the place for work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1725B")

    label("loc_17179")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_171E8")

    ChrTalk(
        0x102,
        (
            "#0100FWell, our jobs require us to traverse\x01",
            "all over Crossbell, so it's no big deal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1725B")

    label("loc_171E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1725B")

    ChrTalk(
        0x103,
        (
            "#0200FWe travel all over Crossbell on a daily basis.\x01",
            "It's only natural we would collect data.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1725B")


    ChrTalk(
        0x101,
        (
            "#0000FWe also have our fair share of fights...\x02\x03",
            "Either way, the important thing is that\x01",
            "we were able to help you out, Rebecca.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You really are a dependable bunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since you've already gathered more\x01",
            "than a sufficient amount of data for HQ,\x01",
            "this marks the end of my request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thank you all so much for seeing it\x01",
            "through to the end. You deserve a\x01",
            "special reward for this occasion.\x02",
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
            "Received \x07\x02",
            "10,000 mira\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddMira(10000)

    ChrTalk(
        0x8,
        (
            "I might still have some requests in the\x01",
            "near future. When that time comes,\x01",
            "I hope I can rely on the SSS again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FOf course. Our doors are always open.\x02",
    )

    CloseMessageWindow()

    label("loc_174E0")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_174FE")
    Jump("loc_17538")

    label("loc_174FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1751B")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_17538")

    label("loc_1751B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17538")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_17538")

    label("loc_17538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_17544")
    ClearScenarioFlags(0x2, 0)

    label("loc_17544")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -340, 40, 13280, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Jump("loc_176D9")

    label("loc_17563")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1763E")

    ChrTalk(
        0x8,
        (
            "Since you've already gathered a more\x01",
            "than a sufficient amount of data for HQ,\x01",
            "this marks the end of my request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope I can rely on the SSS again for\x01",
            "any requests I may have in the future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176D9")

    label("loc_1763E")


    ChrTalk(
        0x8,
        (
            "It appears your Combat Notebook is\x01",
            "coming along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please come show it to me once you've\x01",
            "gathered a bit more data. I'll record it\x01",
            "in our database.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_176D9")

    Return()

    # Function_45_16578 end

    def Function_46_176DA(): pass

    label("Function_46_176DA")

    EventBegin(0x1)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#0005F(Whoops... I don't think this is the\x01",
            "best time to be leaving.)\x02\x03",
            "#0003F(I should go greet the receptionist first...\x01",
            "Might be a good idea to ask her about\x01",
            "my assignment while I'm at it.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 80, 40, 2480, 0)
    EventEnd(0x4)
    Return()

    # Function_46_176DA end

    def Function_47_177B7(): pass

    label("Function_47_177B7")

    EventBegin(0x1)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#0005F(Whoops... I don't think this is the\x01",
            "best time to be leaving.)\x02\x03",
            "#0003F(I should go greet the receptionist first...\x01",
            "Might be a good idea to ask her about\x01",
            "my assignment while I'm at it.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -6760, 0, 10110, 89)
    EventEnd(0x4)
    Return()

    # Function_47_177B7 end

    def Function_48_17894(): pass

    label("Function_48_17894")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18234")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1819C")
    Fade(500)
    OP_68(-12470, 1500, 17150, 0)
    MoveCamera(31, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -13130, 0, 17450, 0)
    SetChrPos(0x102, -11910, 0, 17450, 0)
    SetChrPos(0x103, -13130, 0, 16280, 0)
    SetChrPos(0x104, -11910, 0, 16280, 0)
    OP_0D()
    Sound(160, 0, 100, 0)
    Sleep(1000)
    ClearMapObjFlags(0x2, 0x10)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FOh, someone was using the elevator.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x12, -12480, 0, 20980, 180)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)

    def lambda_179F6():
        OP_95(0xFE, -12480, 0, 19600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_179F6)
    Sleep(200)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
    WaitChrThread(0x12, 1)
    Sleep(600)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)

    ChrTalk(
        0x12,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305F(Damn...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(It's him...)\x02",
    )

    CloseMessageWindow()

    def lambda_17A6E():
        OP_95(0xFE, -12480, 0, 18200, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_17A6E)
    Sleep(500)

    def lambda_17A8B():
        OP_96(0xFE, 0xFFFFCCB6, 0x0, 0x40A6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17A8B)

    def lambda_17AA5():
        OP_96(0xFE, 0xFFFFD17A, 0x0, 0x40A6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17AA5)
    Sleep(100)

    def lambda_17AC2():
        OP_96(0xFE, 0xFFFFCCB6, 0x0, 0x3C14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_17AC2)

    def lambda_17ADC():
        OP_96(0xFE, 0xFFFFD17A, 0x0, 0x3C14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_17ADC)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x12,
        (
            "What are you mutts doing\x01",
            "in a place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "This place has no use for outcasts\x01",
            "like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FYeah? That right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FI cannot deny the outcasts part...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "But more importantly, I see that you\x01",
            "didn't bother to heed my advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Didn't I tell you to refuse your assignment\x01",
            "to the Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "It's a waste of CPD funding that was\x01",
            "only established because of that\x01",
            "damned Sergei.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "It's trash. Meaningless. A rotten\x01",
            "ship that will sink in half a year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "To think I even had the kindness to\x01",
            "warn you from the bottom of my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FE-Excuse me, Vice Commissioner.\x01",
            "Weren't you in a hurry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Hmph, yes. I'm a busy man. I nearly forgot,\x01",
            "thanks to the lot of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-12470, 1500, 15150, 4000)

    def lambda_17DE2():
        OP_95(0xFE, -12480, 0, 13330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_17DE2)

    def lambda_17DFC():

        label("loc_17DFC")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_17DFC")

    QueueWorkItem2(0x101, 2, lambda_17DFC)

    def lambda_17E0E():

        label("loc_17E0E")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_17E0E")

    QueueWorkItem2(0x102, 2, lambda_17E0E)

    def lambda_17E20():

        label("loc_17E20")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_17E20")

    QueueWorkItem2(0x103, 2, lambda_17E20)

    def lambda_17E32():

        label("loc_17E32")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_17E32")

    QueueWorkItem2(0x104, 2, lambda_17E32)

    def lambda_17E44():
        OP_96(0xFE, 0xFFFFCB8A, 0x0, 0x3FAC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17E44)

    def lambda_17E5E():
        OP_96(0xFE, 0xFFFFD2A6, 0x0, 0x3FAC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17E5E)
    Sleep(100)

    def lambda_17E7B():
        OP_96(0xFE, 0xFFFFCB8A, 0x0, 0x3B1A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_17E7B)

    def lambda_17E95():
        OP_96(0xFE, 0xFFFFD2A6, 0x0, 0x3B1A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_17E95)
    OP_6F(0x1)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x101, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    Sleep(500)
    OP_93(0x12, 0x0, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x12,
        (
            "Listen. Leave the hard work to the capable\x01",
            "detectives and don't make a mess, got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Just keep an eye on the citizens\x01",
            "and make sure they stay happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Don't go prowling where you don't belong.\x01",
            "Now get back to that dump you call your office!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(100)
    OP_95(0x12, -12480, 0, 10350, 2000, 0x0)

    def lambda_17FF5():
        OP_95(0xFE, -3890, 0, 10680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_17FF5)
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
        "#0006FUmm... Should we still take the elevator, or no?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FI dunno if there's a nicer way to word this...\x01",
            "I've got a feelin' we aren't even recognized\x01",
            "as police officers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FIt may be prudent of us to avoid going\x01",
            "upstairs unless we have some special\x01",
            "business to attend to.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x12, 0x1)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetScenarioFlags(0x46, 7)
    Jump("loc_18234")

    label("loc_1819C")


    ChrTalk(
        0x101,
        (
            "#0003FWe don't have any business upstairs...\x02\x03",
            "#0000FAnd I think we'd all rather not get chewed out\x01",
            "by the vice commissioner, so let's not risk it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_182D5")

    ChrTalk(
        0x101,
        (
            "#0003FWe don't have any business upstairs...\x02\x03",
            "#0000FAnd I think we'd all rather not get chewed out\x01",
            "by the vice commissioner, so let's not risk it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_182D5")

    SetChrPos(0x0, -12810, 0, 14970, 180)
    EventEnd(0x4)
    Return()

    # Function_48_17894 end

    def Function_49_182E9(): pass

    label("Function_49_182E9")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18AD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187A7")

    ChrTalk(
        0x101,
        (
            "#0005FYou know, this has been bothering\x01",
            "me for a while now...\x02\x03",
            "#0001FWhat exactly is this thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FYeah, I've been eyein' it, too.\x02\x03",
            "#0300FThere's a bunch of juice and coffee\x01",
            "on display... What gives?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202FThis would be an orbal vending machine.\x01",
            "Is this the first time you have seen one?\x02\x03",
            "#0204FIf you insert mira coins into this slot, you\x01",
            "can choose the drink you want, and the\x01",
            "machine dispenses it accordingly.\x02\x03",
            "Since they were originally developed by\x01",
            "the Epstein Foundation, you would often\x01",
            "find them all over their research facilities...\x02\x03",
            "#0202FApparently, they are being tested out in\x01",
            "Crossbell as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWow, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FWere ya aware of these gadgets, Mademois-Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FNo, this is my first time seeing one, too.\x02\x03",
            "#0100FIt's hard to believe that all these inventions\x01",
            "by the Epstein Foundation are starting to\x01",
            "pop up all over Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FGranted, I have heard that they have some\x01",
            "incredibly influential and wealthy sponsors...\x02\x03",
            "#0200FPlease resort to coins if you intend on using it.\x01",
            "Bills are incompatible with this model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThanks for the heads-up.\x01",
            "(I'm kinda curious... I should\x01",
            "try it out at least once, right?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18AD1")

    label("loc_187A7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbal vending machine.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#0005FI think I'll come here to buy myself\x01",
            "a drink next time I'm thirsty.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_188EB")

    ChrTalk(
        0x103,
        (
            "#0200FYes. This is a vending machine developed\x01",
            "by the Epstein Foundation.\x02\x03",
            "I believe Crossbell is one of the regions\x01",
            "designated to experiment with them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A7D")

    label("loc_188EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_189C3")

    ChrTalk(
        0x102,
        (
            "#0100FThis is a vending machine developed\x01",
            "by the Epstein Foundation, isn't it?\x02\x03",
            "If I remember correctly, Tio said that\x01",
            "they've been placed all around Crossbell\x01",
            "for their experimental stage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A7D")

    label("loc_189C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18A7D")

    ChrTalk(
        0x104,
        (
            "#0300FA vending machine created by the\x01",
            "Epstein Foundation, eh?\x02\x03",
            "Accordin' to Tio Tot, the foundation has\x01",
            "been using Crossbell as a testing\x01",
            "ground for these suckers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A7D")


    ChrTalk(
        0x101,
        (
            "#0000FLeave it to Crossbell to incorporate\x01",
            "a broad spectrum of new technology.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AD1")

    SetScenarioFlags(0x95, 3)
    Jump("loc_18AF0")

    label("loc_18AD9")

    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_18AF0")

    TalkEnd(0xFF)
    Return()

    # Function_49_182E9 end

    SaveToFile()

Try(main)
