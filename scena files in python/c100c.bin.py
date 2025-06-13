from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c100c.bin",                # FileName
        "c100c",                    # MapName
        "c100c",                    # Location
        0x0010,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 16, 0, 5, 0, 6],
    )

    BuildStringList((
        "c100c",                  # 0
        "Cronk",                  # 1
        "Dinz",                   # 2
        "Lilly",                  # 3
        "Marte",                  # 4
        "Anne",                   # 5
        "Old Man Renault",        # 6
        "Roy",                    # 7
        "Meiling",                # 8
        "Susan",                  # 9
        "Couta",                  # 10
        "Sarina",                 # 11
        "Eugot",                  # 12
        "Azel",                   # 13
        "Tourist",                # 14
        "Tourist",                # 15
        "Aretha",                 # 16
        "Stefan",                 # 17
        "Wald",                   # 18
        "Luganov",                # 19
        "Jed",                    # 20
        "Koki",                   # 21
        "Black-Haired Woman",     # 22
        "Counterfeit Dealer",     # 23
        "Central Square",         # 24
        "West Street",            # 25
        "Administrative District",# 26
        "Residential District",   # 27
        "Entertainment District", # 28
        "East Street",            # 29
        "Downtown District",      # 30
        "Harbor District",        # 31
        "IBC",                    # 32
        "Station Street",         # 33
        "Back Alley",             # 34
        "Ursula Road",            # 35
        "East Crossbell Highway", # 36
        "West Crossbell Highway", # 37
        "Mainz Mountain Path",    # 38
    ))

    AddCharChip((
        "chr/ch22800.itc",                   # 00
        "chr/ch24800.itc",                   # 01
        "chr/ch24900.itc",                   # 02
        "chr/ch23500.itc",                   # 03
        "chr/ch21100.itc",                   # 04
        "chr/ch24000.itc",                   # 05
        "chr/ch21200.itc",                   # 06
        "chr/ch21500.itc",                   # 07
        "chr/ch10300.itc",                   # 08
        "chr/ch21400.itc",                   # 09
        "chr/ch20500.itc",                   # 0A
        "apl/ch50375.itc",                   # 0B
        "chr/ch23300.itc",                   # 0C
        "chr/ch23800.itc",                   # 0D
        "chr/ch20600.itc",                   # 0E
        "chr/ch02100.itc",                   # 0F
        "chr/ch30800.itc",                   # 10
        "chr/ch31700.itc",                   # 11
        "chr/ch22700.itc",                   # 12
        "chr/ch34200.itc",                   # 13
    ))

    DeclNpc(-24409,  -3000,   5239,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-13039,  -3000,   -810,    225,  261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-16500,  -3000,   2920,    45,   261,  0x0, 0,   2,   0,   0,   4,   0,   9,   255,  0)
    DeclNpc(-4559,   -3000,   -8949,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(26200,   -300,    -1049,   270,  261,  0x0, 0,   4,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(-40490,  -300,    15850,   90,   261,  0x0, 0,   5,   0,   0,   3,   0,   15,  255,  0)
    DeclNpc(-11560,  -300,    6820,    270,  389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-12609,  -300,    7650,    135,  389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-8470,   -3000,   -7349,   45,   261,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-15939,  -3000,   -600,    45,   261,  0x0, 0,   9,   0,   0,   2,   0,   19,  255,  0)
    DeclNpc(-15810,  -300,    16629,   180,  261,  0x0, 0,   10,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-14960,  -300,    15649,   315,  261,  0x0, 0,   19,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-17389,  -300,    16750,   90,   261,  0x0, 0,   11,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-19219,  -319,    17000,   135,  261,  0x0, 0,   12,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-17950,  -300,    17200,   225,  261,  0x0, 0,   13,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(5630,    -300,    3789,    135,  389,  0x0, 0,   18,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(7050,    -300,    3259,    225,  389,  0x0, 0,   14,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(5429,    -3000,   -13149,  315,  389,  0x0, 0,   15,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(5199,    -3000,   -11279,  180,  405,  0x0, 0,   16,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(4239,    -3000,   -12840,  90,   389,  0x0, 0,   17,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(3789,    -3000,   -11079,  135,  389,  0x0, 0,   16,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(17360,   -300,    4630,    1200,    17530,   1500,    5120,    0x007C, 0,  46, 0x0000)

    PlaceName(-111.26000213623047, 0.0, 15.239999771118164, 0x0000, 0x0000, "Central Square")
    PlaceName(-186.8800048828125, 0.0, 20.40999984741211, 0x0000, 0x0000, "West Street")
    PlaceName(-80.20999908447266, 0.0, 117.58999633789062, 0x0000, 0x0000, "Administrative District")
    PlaceName(-257.0299987792969, 0.0, 106.08999633789062, 0x0000, 0x0000, "Residential District")
    PlaceName(-173.0800018310547, 0.0, 96.88999938964844, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-17.829999923706055, 0.0, -11.210000038146973, 0x0000, 0x0000, "East Street")
    PlaceName(23.0, 0.0, -74.45999908447266, 0x0000, 0x0000, "Downtown District")
    PlaceName(14.380000114440918, 0.0, 64.69000244140625, 0x0000, 0x0000, "Harbor District")
    PlaceName(-15.529999732971191, 0.0, 172.7899932861328, 0x0000, 0x0000, "IBC")
    PlaceName(-98.33000183105469, 0.0, -64.11000061035156, 0x0000, 0x0000, "Station Street")
    PlaceName(-152.3800048828125, 0.0, 55.4900016784668, 0x0000, 0x0000, "Back Alley")
    PlaceName(-101.77999877929688, 0.0, -99.76000213623047, 0x0000, 0x0000, "Ursula Road")
    PlaceName(44.279998779296875, 0.0, 4.889999866485596, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-245.52999877929688, 0.0, 18.690000534057617, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-238.6300048828125, 0.0, 133.69000244140625, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-136.55999755859375, 0.0, -0.8600000143051147, 0x0000, 0x0051, "")
    PlaceName(-74.75, 0.0, 29.040000915527344, 0x0000, 0x0054, "")
    PlaceName(-108.38999938964844, 0.0, -10.0600004196167, 0x0000, 0x0057, "")
    PlaceName(-137.42999267578125, 0.0, 32.4900016784668, 0x0000, 0x0053, "")
    PlaceName(-113.8499984741211, 0.0, 60.09000015258789, 0x0000, 0x0053, "")
    PlaceName(-172.2100067138672, 0.0, 26.739999771118164, 0x0000, 0x0053, "")
    PlaceName(-183.42999267578125, 0.0, 50.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-155.8300018310547, 0.0, 87.69000244140625, 0x0000, 0x0052, "")
    PlaceName(-150.36000061035156, 0.0, 72.73999786376953, 0x0000, 0x0053, "")
    PlaceName(-140.3000030517578, 0.0, 62.959999084472656, 0x0000, 0x0053, "")
    PlaceName(-107.52999877929688, 0.0, 144.61000061035156, 0x0000, 0x0051, "")
    PlaceName(21.280000686645508, 0.0, -11.210000038146973, 0x0000, 0x0052, "")
    PlaceName(1.7300000190734863, 0.0, -115.29000091552734, 0x0000, 0x0053, "")
    PlaceName(-13.229999542236328, 0.0, -94.01000213623047, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_694",          # 00, 0
        "Function_1_74C",          # 01, 1
        "Function_2_7E5",          # 02, 2
        "Function_3_85A",          # 03, 3
        "Function_4_91B",          # 04, 4
        "Function_5_968",          # 05, 5
        "Function_6_D65",          # 06, 6
        "Function_7_E2A",          # 07, 7
        "Function_8_13DB",         # 08, 8
        "Function_9_1997",         # 09, 9
        "Function_10_2110",        # 0A, 10
        "Function_11_3F36",        # 0B, 11
        "Function_12_441A",        # 0C, 12
        "Function_13_455D",        # 0D, 13
        "Function_14_4726",        # 0E, 14
        "Function_15_4B08",        # 0F, 15
        "Function_16_4F90",        # 10, 16
        "Function_17_506E",        # 11, 17
        "Function_18_50D2",        # 12, 18
        "Function_19_5585",        # 13, 19
        "Function_20_5892",        # 14, 20
        "Function_21_5AA0",        # 15, 21
        "Function_22_5CAA",        # 16, 22
        "Function_23_5E39",        # 17, 23
        "Function_24_6256",        # 18, 24
        "Function_25_6398",        # 19, 25
        "Function_26_64B0",        # 1A, 26
        "Function_27_65D3",        # 1B, 27
        "Function_28_6AA5",        # 1C, 28
        "Function_29_6B10",        # 1D, 29
        "Function_30_6BAC",        # 1E, 30
        "Function_31_6C91",        # 1F, 31
        "Function_32_6E4F",        # 20, 32
        "Function_33_7195",        # 21, 33
        "Function_34_7280",        # 22, 34
        "Function_35_7AAF",        # 23, 35
        "Function_36_906D",        # 24, 36
        "Function_37_909D",        # 25, 37
        "Function_38_90D4",        # 26, 38
        "Function_39_90F3",        # 27, 39
        "Function_40_9119",        # 28, 40
        "Function_41_913F",        # 29, 41
        "Function_42_9165",        # 2A, 42
        "Function_43_91A2",        # 2B, 43
        "Function_44_91C1",        # 2C, 44
        "Function_45_91E0",        # 2D, 45
        "Function_46_9273",        # 2E, 46
        "Function_47_B0D9",        # 2F, 47
        "Function_48_B33C",        # 30, 48
    ))


    def Function_0_694(): pass

    label("Function_0_694")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_6D4"),
        (1, "loc_6E0"),
        (2, "loc_6EC"),
        (3, "loc_6F8"),
        (4, "loc_704"),
        (5, "loc_710"),
        (6, "loc_71C"),
        (SWITCH_DEFAULT, "loc_728"),
    )


    label("loc_6D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_6E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_6EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_6F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_704")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_710")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_71C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_728")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_734")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_74B")

    Return()

    # Function_0_694 end

    def Function_1_74C(): pass

    label("Function_1_74C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E4")
    OP_95(0xFE, -1180, -300, -1100, 2000, 0x0)
    OP_95(0xFE, -15670, -300, 12310, 2000, 0x0)
    OP_95(0xFE, -40270, -300, 12170, 2000, 0x0)
    Sleep(2500)
    OP_95(0xFE, -15670, -300, 12310, 2000, 0x0)
    OP_95(0xFE, -1180, -300, -1100, 2000, 0x0)
    OP_95(0xFE, 26200, -300, -1050, 2000, 0x0)
    Sleep(200)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    Jump("Function_1_74C")

    label("loc_7E4")

    Return()

    # Function_1_74C end

    def Function_2_7E5(): pass

    label("Function_2_7E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_859")
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -22610, -3000, 3390, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_2_7E5")

    label("loc_859")

    Return()

    # Function_2_7E5 end

    def Function_3_85A(): pass

    label("Function_3_85A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_91A")
    OP_95(0xFE, -16760, -300, 15130, 2000, 0x0)
    OP_95(0xFE, -13780, -300, 14160, 2000, 0x0)
    OP_95(0xFE, -1180, -300, 2190, 2000, 0x0)
    OP_95(0xFE, 26030, -300, 2230, 2000, 0x0)
    Sleep(200)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1180, -300, 2190, 2000, 0x0)
    OP_95(0xFE, -13780, -300, 14160, 2000, 0x0)
    OP_95(0xFE, -16760, -300, 15130, 2000, 0x0)
    OP_95(0xFE, -40490, -300, 15850, 2000, 0x0)
    Sleep(2400)
    Jump("Function_3_85A")

    label("loc_91A")

    Return()

    # Function_3_85A end

    def Function_4_91B(): pass

    label("Function_4_91B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_967")
    OP_95(0xFE, -15130, -3000, 1420, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    OP_95(0xFE, -16500, -3000, 2920, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    Jump("Function_4_91B")

    label("loc_967")

    Return()

    # Function_4_91B end

    def Function_5_968(): pass

    label("Function_5_968")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B88")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A33")
    SetChrPos(0x0, -20760, -310, 33300, 180)
    SetChrPos(0x1, -20760, -310, 33300, 180)
    SetChrPos(0x2, -20760, -310, 33300, 180)
    SetChrPos(0x3, -20760, -310, 33300, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A06")
    SetChrPos(0x4, -20760, -310, 33300, 180)
    SetChrPos(0x5, -20760, -310, 33300, 180)
    Jump("loc_A25")

    label("loc_A06")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A25")
    SetChrPos(0x4, -20760, -310, 33300, 180)

    label("loc_A25")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B88")

    label("loc_A33")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE7")
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    SetChrPos(0x1, 1910, -3000, -35980, 0)
    SetChrPos(0x2, 1910, -3000, -35980, 0)
    SetChrPos(0x3, 1910, -3000, -35980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ABA")
    SetChrPos(0x4, 1910, -3000, -35980, 0)
    SetChrPos(0x5, 1910, -3000, -35980, 0)
    Jump("loc_AD9")

    label("loc_ABA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD9")
    SetChrPos(0x4, 1910, -3000, -35980, 0)

    label("loc_AD9")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B88")

    label("loc_AE7")

    SetChrPos(0x0, -29790, -330, 13830, 90)
    SetChrPos(0x1, -29790, -330, 13830, 90)
    SetChrPos(0x2, -29790, -330, 13830, 90)
    SetChrPos(0x3, -29790, -330, 13830, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B60")
    SetChrPos(0x4, -29790, -330, 13830, 90)
    SetChrPos(0x5, -29790, -330, 13830, 90)
    Jump("loc_B7F")

    label("loc_B60")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7F")
    SetChrPos(0x4, -29790, -330, 13830, 90)

    label("loc_B7F")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B88")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_BF2")
    SetChrPos(0x12, -14960, -300, 15650, 315)
    SetChrPos(0x13, -15810, -300, 16630, 270)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0x15, -11870, -300, 6120, 315)
    SetChrPos(0x16, -12270, -300, 7480, 180)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x10)
    Jump("loc_D28")

    label("loc_BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_C58")
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x12, -14960, -300, 15650, 315)
    SetChrPos(0x13, -15810, -300, 16630, 180)
    SetChrPos(0x15, -12120, -310, 6540, 0)
    SetChrPos(0x16, -10940, -300, 6040, 315)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x10)
    Jump("loc_D28")

    label("loc_C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C9B")
    OP_93(0x12, 0x10E, 0x0)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x15, -13300, -3000, -2410, 0)
    SetChrPos(0x16, -12550, -3000, -3260, 315)
    OP_93(0x9, 0xB4, 0x0)
    Jump("loc_D28")

    label("loc_C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CFC")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x15, -24030, -3000, 3630, 315)
    SetChrPos(0x16, -21730, -3000, 5420, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_CF7")
    SetChrFlags(0x1C, 0x10)

    label("loc_CF7")

    Jump("loc_D28")

    label("loc_CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D28")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_D3C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 31)
    Jump("loc_D4B")

    label("loc_D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_D4B")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 33)

    label("loc_D4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D64")
    SetMapFlags(0x10000000)
    Event(0, 32)

    label("loc_D64")

    Return()

    # Function_5_968 end

    def Function_6_D65(): pass

    label("Function_6_D65")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0x1E)
    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -16000, -4300, 14000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 10000, -4300, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -16000, -6000, -10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_6_D65 end

    def Function_7_E2A(): pass

    label("Function_7_E2A")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D7")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E88")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_E88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA8")
    OP_AF(0x39)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13D2")

    label("loc_EA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EBC")
    Jump("loc_13D2")

    label("loc_EBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_105A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCB")

    ChrTalk(
        0xFE,
        "*sigh* I'm really sorry, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've somehow managed to sell out all of my\x01",
            "70th anniversary merch.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0xFE,
        (
            "Wait a sec... I sold out?! This is the\x01",
            "first time I've ever pulled it off!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1055")

    label("loc_FCB")


    ChrTalk(
        0xFE,
        (
            "*sigh* I'm really sorry, but I'm all outta\x01",
            "anniversary goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha. I guess it wasn't a waste of time\x01",
            "to make 'em, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1055")

    Jump("loc_13D2")

    label("loc_105A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_111D")

    ChrTalk(
        0xFE,
        (
            "Kids were buying my pinwheels like they\x01",
            "were the best thing since sliced bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like those kinda toys appeal to the\x01",
            "kiddies... Learn something every day,\x01",
            "I suppose!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D2")

    label("loc_111D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_118D")

    ChrTalk(
        0xFE,
        (
            "Is it just me, or are there a ton of\x01",
            "people around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Better up my advertising game!\x02",
    )

    CloseMessageWindow()
    Jump("loc_13D2")

    label("loc_118D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1243")

    ChrTalk(
        0xFE,
        (
            "I'm not really surprised, to be honest. The festival\x01",
            "usually brings some massive crowds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lemme tell you, anniversary merch\x01",
            "practically flies off the shelves!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D2")

    label("loc_1243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_13D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_138D")

    ChrTalk(
        0xFE,
        "#4SHey there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You lookin' for some awesome 70th\x01",
            "anniversary merch? I've got some\x01",
            "great stuff in stock!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got all the umbrella stands, tabletop\x01",
            "clocks, and cigarette cases you'd ever need!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our exclusive Crossbell City Hall replicas are\x01",
            "on a strict first come, first serve basis!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13D2")

    label("loc_138D")


    ChrTalk(
        0xFE,
        (
            "Would you like to take a gander at\x01",
            "our 70th anniversary merch?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D2")

    Jump("loc_E37")

    label("loc_13D7")

    TalkEnd(0xFE)
    Return()

    # Function_7_E2A end

    def Function_8_13DB(): pass

    label("Function_8_13DB")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1993")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1439")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1439")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1459")
    OP_AF(0x38)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_198E")

    label("loc_1459")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_146D")
    Jump("loc_198E")

    label("loc_146D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_198E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1540")

    ChrTalk(
        0xFE,
        (
            "Welcome one, welcome all! Thanks for\x01",
            "always coming to Dinz Fresh!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's the last day of our big sale, so you better\x01",
            "stock up on cheap veggies while you still can!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_198E")

    label("loc_1540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_15AC")

    ChrTalk(
        0xFE,
        "People are buying stuff up by the torim!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Heck, even the Goddess would be impressed!\x02",
    )

    CloseMessageWindow()
    Jump("loc_198E")

    label("loc_15AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1670")

    ChrTalk(
        0xFE,
        "Hello there, my dear customers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Stop, drop, and roll on over to Dinz Fresh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's finally time for the big bargain sale at\x01",
            "Dinz Fresh, the marketplace's pride and joy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_198E")

    label("loc_1670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_183D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A6")

    ChrTalk(
        0xFE,
        (
            "The Business Owners' Association called\x01",
            "me to one of their meetings last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The old geezers actually let me\x01",
            "drink a few glasses with 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I knocked back a few drinks with some\x01",
            "merchant buddies one night of the festival.\x01",
            "Lemme tell ya, THAT was a good night.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1838")

    label("loc_17A6")


    ChrTalk(
        0xFE,
        (
            "I got an invitation last night to do some drinking\x01",
            "at a Business Owners' Association meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, that was some high-quality booze. ♪\x02",
    )

    CloseMessageWindow()

    label("loc_1838")

    Jump("loc_198E")

    label("loc_183D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_198E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1901")

    ChrTalk(
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I tried to get Lilly to try and hang out\x01",
            "with me for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can you believe she told me she didn't feel\x01",
            "like it? The lady needs to lighten up!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_198E")

    label("loc_1901")


    ChrTalk(
        0xFE,
        (
            "Then again, Lilly's been a real uptight one\x01",
            "for as long as I can remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dang, lady. You're going to end up\x01",
            "regretting it later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_198E")

    Jump("loc_13E8")

    label("loc_1993")

    TalkEnd(0xFE)
    Return()

    # Function_8_13DB end

    def Function_9_1997(): pass

    label("Function_9_1997")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1AC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A2E")

    ChrTalk(
        0xFE,
        (
            "Hey there, folks! You here to take\x01",
            "a look around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I actually ran outta change earlier,\x01",
            "but don't sweat it, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1ABD")

    label("loc_1A2E")


    ChrTalk(
        0xFE,
        (
            "Man, why'd I have to run out of change\x01",
            "during such a busy time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I can get Marte and Cronk to do\x01",
            "me a solid and lend me some...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ABD")

    Jump("loc_210C")

    label("loc_1AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1B33")

    ChrTalk(
        0xFE,
        "Whoa. Wasn't expecting a crowd this big.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Bet the police are having a fun time with this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_210C")

    label("loc_1B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1E2B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BC9")

    ChrTalk(
        0xFE,
        (
            "Dude, Cronk's been getting so much\x01",
            "business today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, the marketplace's\x01",
            "MVP award is as good as his...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E26")

    label("loc_1BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D41")

    ChrTalk(
        0xFE,
        (
            "You folks hear about that thief who keeps\x01",
            "ransacking food stalls around the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Chairman Mors just came by to warn\x01",
            "me about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I told him that we're used to dealing with\x01",
            "thieves and pickpockets. We're not going to\x01",
            "let 'em take us down so easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm more worried the average stall might\x01",
            "get targeted. What an unfortunate situation...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1E26")

    label("loc_1D41")


    ChrTalk(
        0xFE,
        (
            "As far as us East Streeters go, we're used to\x01",
            "collaborating with fellow merchants to track\x01",
            "down thieves. Easy peasy lemon squeezy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm more worried the average stall might\x01",
            "get targeted. What an unfortunate situation...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E26")

    Jump("loc_210C")

    label("loc_1E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1F47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE3")

    ChrTalk(
        0xFE,
        "Is Dinz for real?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He SUPPOSEDLY managed to down a few drinks with\x01",
            "the chairman of the Business Owners' Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it is what it is...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F42")

    label("loc_1EE3")


    ChrTalk(
        0xFE,
        (
            "I can't fault Dinz for being an open book.\x01",
            "His honesty is his strongest point, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F42")

    Jump("loc_210C")

    label("loc_1F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_210C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20A2")

    ChrTalk(
        0xFE,
        (
            "Welcome! We're currently participating\x01",
            "in Crossbell's stamp collecting contest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tell me if you buy something so I can\x01",
            "give you your stamp, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Go to the Harbor District if you want to exchange them\x01",
            "for a prize. The Business Owners' Association should\x01",
            "have a tent set up, so you'll know when you see it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_210C")

    label("loc_20A2")


    ChrTalk(
        0xFE,
        (
            "Phew... Explaining this stamp collecting contest\x01",
            "over and over and over again is really darn tiring.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_210C")

    TalkEnd(0xFE)
    Return()

    # Function_9_1997 end

    def Function_10_2110(): pass

    label("Function_10_2110")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x1, 6)
    Call(0, 12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_22AB")

    ChrTalk(
        0xFE,
        (
            "Look who decided to stop by again.\x01",
            "Did you bring me some more fresh fish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys manage to fish these up yourself?\x01",
            "They're in pretty good condition... I could\x01",
            "probably sell these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... How 'bout it? Wanna let me\x01",
            "take those fish off your hands?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Remember, fish indigenous to Crossbell are popular,\x01",
            "so I'll give you a nice reward if you bring me some.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x51, 7)
    SetScenarioFlags(0x1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_22AB")

    Call(0, 11)
    Jump("loc_3F32")

    label("loc_22B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_3F2F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F2A")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "Talk")
    MenuCmd(1, 1, "Give Fish")
    MenuCmd(1, 1, "Leave")
    ClearScenarioFlags(0x1, 6)
    Call(0, 12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2314")
    MenuCmd(3, 1, 0x1)

    label("loc_2314")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2346")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2346")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EF5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_235F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EE6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23CD")
    MenuCmd(1, 1, "Snow Crab (for earth x10)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23C3")
    Call(0, 13)

    label("loc_23C3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_23CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2424")
    MenuCmd(1, 1, "Armorican Carp (for water x10)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_241A")
    Call(0, 13)

    label("loc_241A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2424")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_247A")
    MenuCmd(1, 1, "Tiger Rockfish (for fire x10)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2470")
    Call(0, 13)

    label("loc_2470")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_247A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_24CB")
    MenuCmd(1, 1, "Rockeater (for wind x10)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24C1")
    Call(0, 13)

    label("loc_24C1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_24CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2517")
    MenuCmd(1, 1, "Carp (for time x10)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_250D")
    Call(0, 13)

    label("loc_250D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2517")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_256A")
    MenuCmd(1, 1, "Raineater (for mirage x10)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2560")
    Call(0, 13)

    label("loc_2560")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_256A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25BB")
    MenuCmd(1, 1, "Azelfish (for earth x20)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25B1")
    Call(0, 13)

    label("loc_25B1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_25BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_260B")
    MenuCmd(1, 1, "Kasagin (for water x20)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2601")
    Call(0, 13)

    label("loc_2601")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_260B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2660")
    MenuCmd(1, 1, "Rainbow Trout (for fire x20)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2656")
    Call(0, 13)

    label("loc_2656")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2660")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26AD")
    MenuCmd(1, 1, "Trout (for wind x20)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A3")
    Call(0, 13)

    label("loc_26A3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_26AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26FB")
    MenuCmd(1, 1, "Salmon (for time x20)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26F1")
    Call(0, 13)

    label("loc_26F1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_26FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2748")
    MenuCmd(1, 1, "Eel (for mirage x20)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_273E")
    Call(0, 13)

    label("loc_273E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2748")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_279B")
    MenuCmd(1, 1, "Pearlglass (for space x20)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2791")
    Call(0, 13)

    label("loc_2791")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_279B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27F3")
    MenuCmd(1, 1, "Gluttonous Bass (for earth x40)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27E9")
    Call(0, 13)

    label("loc_27E9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_27F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2845")
    MenuCmd(1, 1, "Viperfish (for water x40)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283B")
    Call(0, 13)

    label("loc_283B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2845")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2897")
    MenuCmd(1, 1, "Pythonhead (for fire x40)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_288D")
    Call(0, 13)

    label("loc_288D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2897")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28E6")
    MenuCmd(1, 1, "Catfish (for wind x40)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28DC")
    Call(0, 13)

    label("loc_28DC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_28E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2938")
    MenuCmd(1, 1, "Queen Crab (for time x50)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_292E")
    Call(0, 13)

    label("loc_292E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2938")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_298E")
    MenuCmd(1, 1, "Electric Eel (for mirage x50)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2984")
    Call(0, 13)

    label("loc_2984")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_298E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29E3")
    MenuCmd(1, 1, "Demon Catfish (for time x50)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29D9")
    Call(0, 13)

    label("loc_29D9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A35")
    MenuCmd(1, 1, "Arch Crab (for space x50)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A2B")
    Call(0, 13)

    label("loc_2A2B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A89")
    MenuCmd(1, 1, "Gold Salmon (for time x100)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A7F")
    Call(0, 13)

    label("loc_2A7F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2ADD")
    MenuCmd(1, 1, "Noble Carp (for space x100)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD3")
    Call(0, 13)

    label("loc_2AD3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2ADD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B33")
    MenuCmd(1, 1, "Serpenthead (for mirage x100)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B29")
    Call(0, 13)

    label("loc_2B29")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2B33")

    MenuCmd(1, 1, "Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B74")
    Jump("loc_3EE1")

    label("loc_2B74")

    FadeToBright(300, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C12")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C08")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#56I10 Earth Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_2C08")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2C12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C93")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C89")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#57I10 Water Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_2C89")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2C93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D13")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D09")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#58I10 Fire Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_2D09")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D93")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D89")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#59I10 Wind Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_2D89")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E13")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E09")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#60I10 Time Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_2E09")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E95")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E8B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#62I10 Mirage Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_2E8B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F16")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F0C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#56I20 Earth Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_2F0C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F97")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F8D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#57I20 Water Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_2F8D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3017")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#58I20 Fire Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_300D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3017")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3097")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_308D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#59I20 Wind Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_308D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3097")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3117")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_310D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#60I20 Time Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_310D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3117")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3199")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_318F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#62I20 Mirage Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_318F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3199")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_321A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3210")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#61I20 Space Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_3210")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_321A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_329B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3291")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#56I40 Earth Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_3291")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_329B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_331C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3312")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#57I40 Water Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_3312")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_331C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_339C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3392")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#58I40 Fire Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_3392")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_339C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_341C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3412")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#59I40 Wind Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_3412")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_341C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_349C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3492")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#60I50 Time Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_3492")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_349C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_351E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3514")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#62I50 Mirage Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_3514")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_351E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_359E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3594")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#60I50 Time Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_3594")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_359E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_361F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3615")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#61I50 Space Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_3615")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_361F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36A0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3696")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#60I100 Time Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_3696")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_36A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3722")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3718")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#61I100 Space Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_3718")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3722")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_37A5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_379B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Will you trade me that fish in exchange\x01",
            "for \x07\x02",
            "#62I100 Mirage Sepith\x07\x00",
            "?\x02",
        )
    )


    label("loc_379B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_37A5")

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Exchange\x01",      # 0
            "Cancel\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EE1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_38D0")

    ChrTalk(
        0xFE,
        (
            "You sure it's okay for me to have this fish?\x01",
            "It's incredibly rare, so I doubt you'd ever be\x01",
            "able to catch one again.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38D0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ED7")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sleep(300)
    Sound(17, 0, 100, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3997"),
        (1, "loc_39CE"),
        (2, "loc_3A05"),
        (3, "loc_3A3B"),
        (4, "loc_3A71"),
        (5, "loc_3AA7"),
        (6, "loc_3ADF"),
        (7, "loc_3B16"),
        (8, "loc_3B4D"),
        (9, "loc_3B83"),
        (10, "loc_3BB9"),
        (11, "loc_3BEF"),
        (12, "loc_3C27"),
        (13, "loc_3C5E"),
        (14, "loc_3C95"),
        (15, "loc_3CCC"),
        (16, "loc_3D02"),
        (17, "loc_3D38"),
        (18, "loc_3D6E"),
        (19, "loc_3DA6"),
        (20, "loc_3DDC"),
        (21, "loc_3E13"),
        (22, "loc_3E4A"),
        (23, "loc_3E82"),
        (SWITCH_DEFAULT, "loc_3EBB"),
    )


    label("loc_3997")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x10.\x02",
        )
    )

    AddSepith(0x0, 10)
    SubItemNumber(0x15E, 1)
    Jump("loc_3EBB")

    label("loc_39CE")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#57IWater Sepith\x07\x00",
            " x10.\x02",
        )
    )

    AddSepith(0x1, 10)
    SubItemNumber(0x15F, 1)
    Jump("loc_3EBB")

    label("loc_3A05")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#58IFire Sepith\x07\x00",
            " x10.\x02",
        )
    )

    AddSepith(0x2, 10)
    SubItemNumber(0x160, 1)
    Jump("loc_3EBB")

    label("loc_3A3B")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#59IWind Sepith\x07\x00",
            " x10.\x02",
        )
    )

    AddSepith(0x3, 10)
    SubItemNumber(0x161, 1)
    Jump("loc_3EBB")

    label("loc_3A71")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#60ITime Sepith\x07\x00",
            " x10.\x02",
        )
    )

    AddSepith(0x4, 10)
    SubItemNumber(0x162, 1)
    Jump("loc_3EBB")

    label("loc_3AA7")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x10.\x02",
        )
    )

    AddSepith(0x6, 10)
    SubItemNumber(0x163, 1)
    Jump("loc_3EBB")

    label("loc_3ADF")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x20.\x02",
        )
    )

    AddSepith(0x0, 20)
    SubItemNumber(0x164, 1)
    Jump("loc_3EBB")

    label("loc_3B16")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#57IWater Sepith\x07\x00",
            " x20.\x02",
        )
    )

    AddSepith(0x1, 20)
    SubItemNumber(0x165, 1)
    Jump("loc_3EBB")

    label("loc_3B4D")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#58IFire Sepith\x07\x00",
            " x20.\x02",
        )
    )

    AddSepith(0x2, 20)
    SubItemNumber(0x166, 1)
    Jump("loc_3EBB")

    label("loc_3B83")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#59IWind Sepith\x07\x00",
            " x20.\x02",
        )
    )

    AddSepith(0x3, 20)
    SubItemNumber(0x167, 1)
    Jump("loc_3EBB")

    label("loc_3BB9")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#60ITime Sepith\x07\x00",
            " x20.\x02",
        )
    )

    AddSepith(0x4, 20)
    SubItemNumber(0x168, 1)
    Jump("loc_3EBB")

    label("loc_3BEF")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x20.\x02",
        )
    )

    AddSepith(0x6, 20)
    SubItemNumber(0x169, 1)
    Jump("loc_3EBB")

    label("loc_3C27")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x20.\x02",
        )
    )

    AddSepith(0x5, 20)
    SubItemNumber(0x16A, 1)
    Jump("loc_3EBB")

    label("loc_3C5E")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x40.\x02",
        )
    )

    AddSepith(0x0, 40)
    SubItemNumber(0x16B, 1)
    Jump("loc_3EBB")

    label("loc_3C95")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#57IWater Sepith\x07\x00",
            " x40.\x02",
        )
    )

    AddSepith(0x1, 40)
    SubItemNumber(0x16C, 1)
    Jump("loc_3EBB")

    label("loc_3CCC")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#58IFire Sepith\x07\x00",
            " x40.\x02",
        )
    )

    AddSepith(0x2, 40)
    SubItemNumber(0x16D, 1)
    Jump("loc_3EBB")

    label("loc_3D02")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#59IWind Sepith\x07\x00",
            " x40.\x02",
        )
    )

    AddSepith(0x3, 40)
    SubItemNumber(0x16E, 1)
    Jump("loc_3EBB")

    label("loc_3D38")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#60ITime Sepith\x07\x00",
            " x50.\x02",
        )
    )

    AddSepith(0x4, 50)
    SubItemNumber(0x16F, 1)
    Jump("loc_3EBB")

    label("loc_3D6E")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x50.\x02",
        )
    )

    AddSepith(0x6, 50)
    SubItemNumber(0x170, 1)
    Jump("loc_3EBB")

    label("loc_3DA6")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#60ITime Sepith\x07\x00",
            " x50.\x02",
        )
    )

    AddSepith(0x4, 50)
    SubItemNumber(0x171, 1)
    Jump("loc_3EBB")

    label("loc_3DDC")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x50.\x02",
        )
    )

    AddSepith(0x5, 50)
    SubItemNumber(0x172, 1)
    Jump("loc_3EBB")

    label("loc_3E13")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#60ITime Sepith\x07\x00",
            " x100.\x02",
        )
    )

    AddSepith(0x4, 100)
    SubItemNumber(0x173, 1)
    Jump("loc_3EBB")

    label("loc_3E4A")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x100.\x02",
        )
    )

    AddSepith(0x5, 100)
    SubItemNumber(0x174, 1)
    Jump("loc_3EBB")

    label("loc_3E82")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x100.\x02",
        )
    )

    AddSepith(0x6, 100)
    SubItemNumber(0x175, 1)
    Jump("loc_3EBB")

    label("loc_3EBB")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EE1")

    label("loc_3ED7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EE1")

    Jump("loc_235F")

    label("loc_3EE6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F25")

    label("loc_3EF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F09")
    Jump("loc_3F25")

    label("loc_3F09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F25")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 11)

    label("loc_3F25")

    Jump("loc_22C6")

    label("loc_3F2A")

    Jump("loc_3F32")

    label("loc_3F2F")

    Call(0, 11)

    label("loc_3F32")

    TalkEnd(0xB)
    Return()

    # Function_10_2110 end

    def Function_11_3F36(): pass

    label("Function_11_3F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_403D")

    ChrTalk(
        0xB,
        (
            "Fish indigenous to Crossbell have been a hot\x01",
            "ticket item, but it's always difficult to find\x01",
            "suppliers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Looks like you guys managed to find some\x01",
            "high-quality fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Would you mind selling them to me? I'll\x01",
            "even throw in a little reward.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4419")

    label("loc_403D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_40C1")

    ChrTalk(
        0xB,
        (
            "I made sure to stock five times the\x01",
            "usual amount today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Now I just need to figure out how to sell it all...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4419")

    label("loc_40C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4135")

    ChrTalk(
        0xB,
        "Demand this year has been extraordinary.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I'll be sure to brag about it to my husband later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4419")

    label("loc_4135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4202")

    ChrTalk(
        0xB,
        "Mornin', friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Y'know, the parade isn't the ONLY highlight\x01",
            "of the Anniversary Festival...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I feel bad for the suckers who skimp out on\x01",
            "comin' to the East Street marketplace!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4419")

    label("loc_4202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_42C6")

    ChrTalk(
        0xB,
        (
            "Mornin', friends! You came at just the right time.\x01",
            "Everything was freshly caught this morning!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you hurry up and use these in a dish,\x01",
            "you'll be cookin' up a masterpiece!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4419")

    label("loc_42C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4419")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_437D")

    ChrTalk(
        0xB,
        "Morning, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You wanna try some fantastic fish?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you bring them over to the folks at Long Lao,\x01",
            "they'll prepare the meat for cooking.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4419")

    label("loc_437D")


    ChrTalk(
        0xB,
        (
            "Any inn on East Street lets you bring your own\x01",
            "ingredients, if you're stayin' there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That's just how we roll here at the\x01",
            "East Street marketplace!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4419")

    Return()

    # Function_11_3F36 end

    def Function_12_441A(): pass

    label("Function_12_441A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_4428")
    SetScenarioFlags(0x1, 6)

    label("loc_4428")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_4436")
    SetScenarioFlags(0x1, 6)

    label("loc_4436")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_4444")
    SetScenarioFlags(0x1, 6)

    label("loc_4444")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_4452")
    SetScenarioFlags(0x1, 6)

    label("loc_4452")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_4460")
    SetScenarioFlags(0x1, 6)

    label("loc_4460")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_446E")
    SetScenarioFlags(0x1, 6)

    label("loc_446E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_447C")
    SetScenarioFlags(0x1, 6)

    label("loc_447C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_448A")
    SetScenarioFlags(0x1, 6)

    label("loc_448A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_4498")
    SetScenarioFlags(0x1, 6)

    label("loc_4498")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_44A6")
    SetScenarioFlags(0x1, 6)

    label("loc_44A6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_44B4")
    SetScenarioFlags(0x1, 6)

    label("loc_44B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_44C2")
    SetScenarioFlags(0x1, 6)

    label("loc_44C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_44D0")
    SetScenarioFlags(0x1, 6)

    label("loc_44D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_44DE")
    SetScenarioFlags(0x1, 6)

    label("loc_44DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_44EC")
    SetScenarioFlags(0x1, 6)

    label("loc_44EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_44FA")
    SetScenarioFlags(0x1, 6)

    label("loc_44FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_4508")
    SetScenarioFlags(0x1, 6)

    label("loc_4508")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_4516")
    SetScenarioFlags(0x1, 6)

    label("loc_4516")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_4524")
    SetScenarioFlags(0x1, 6)

    label("loc_4524")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_4532")
    SetScenarioFlags(0x1, 6)

    label("loc_4532")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_4540")
    SetScenarioFlags(0x1, 6)

    label("loc_4540")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_454E")
    SetScenarioFlags(0x1, 6)

    label("loc_454E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_455C")
    SetScenarioFlags(0x1, 6)

    label("loc_455C")

    Return()

    # Function_12_441A end

    def Function_13_455D(): pass

    label("Function_13_455D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4570")
    MenuCmd(3, 1, 0x0)

    label("loc_4570")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4583")
    MenuCmd(3, 1, 0x1)

    label("loc_4583")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4596")
    MenuCmd(3, 1, 0x2)

    label("loc_4596")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A9")
    MenuCmd(3, 1, 0x3)

    label("loc_45A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45BC")
    MenuCmd(3, 1, 0x4)

    label("loc_45BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45CF")
    MenuCmd(3, 1, 0x5)

    label("loc_45CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45E2")
    MenuCmd(3, 1, 0x6)

    label("loc_45E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45F5")
    MenuCmd(3, 1, 0x7)

    label("loc_45F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4608")
    MenuCmd(3, 1, 0x8)

    label("loc_4608")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_461B")
    MenuCmd(3, 1, 0x9)

    label("loc_461B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_462E")
    MenuCmd(3, 1, 0xA)

    label("loc_462E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4641")
    MenuCmd(3, 1, 0xB)

    label("loc_4641")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4654")
    MenuCmd(3, 1, 0xC)

    label("loc_4654")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4667")
    MenuCmd(3, 1, 0xD)

    label("loc_4667")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_467A")
    MenuCmd(3, 1, 0xE)

    label("loc_467A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_468D")
    MenuCmd(3, 1, 0xF)

    label("loc_468D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46A0")
    MenuCmd(3, 1, 0x10)

    label("loc_46A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46B3")
    MenuCmd(3, 1, 0x11)

    label("loc_46B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46C6")
    MenuCmd(3, 1, 0x12)

    label("loc_46C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46D9")
    MenuCmd(3, 1, 0x13)

    label("loc_46D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46EC")
    MenuCmd(3, 1, 0x14)

    label("loc_46EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46FF")
    MenuCmd(3, 1, 0x15)

    label("loc_46FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4712")
    MenuCmd(3, 1, 0x16)

    label("loc_4712")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4725")
    MenuCmd(3, 1, 0x17)

    label("loc_4725")

    Return()

    # Function_13_455D end

    def Function_14_4726(): pass

    label("Function_14_4726")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_47CA")

    ChrTalk(
        0xFE,
        (
            "Oh, dear! Today's stamp collection contest\x01",
            "has ended already, hasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to rush over and exchange\x01",
            "my stamps while I still can!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B04")

    label("loc_47CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_484C")

    ChrTalk(
        0xFE,
        "This year's parade was something else...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Watching the kids wave at the floats\x01",
            "passing by was so adorable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B04")

    label("loc_484C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_48F9")

    ChrTalk(
        0xFE,
        (
            "I ended up stopping by a few food stalls\x01",
            "while I was shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* This isn't good. Not good at all.\x01",
            "I've got to keep this secret from my family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B04")

    label("loc_48F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4A53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49B5")

    ChrTalk(
        0xFE,
        (
            "A lot of tourists are visiting\x01",
            "Armorica Village this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a gorgeous place, and not to mention,\x01",
            "they have the tastiest food in all of Crossbell!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4A4E")

    label("loc_49B5")


    ChrTalk(
        0xFE,
        (
            "Armorica Village is both beautiful and filled\x01",
            "with delicious food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can totally understand why a bunch\x01",
            "of tourists are going to check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A4E")

    Jump("loc_4B04")

    label("loc_4A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4B04")

    ChrTalk(
        0xFE,
        (
            "A housewife like myself could NEVER take a day off,\x01",
            "not even during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... I still need to go buy ingredients for\x01",
            "tonight's dinner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B04")

    TalkEnd(0xFE)
    Return()

    # Function_14_4726 end

    def Function_15_4B08(): pass

    label("Function_15_4B08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4C8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C19")

    ChrTalk(
        0xFE,
        (
            "I've heard plenty of attractions are being put on\x01",
            "in the Harbor District every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose I may have accidentally overlooked\x01",
            "the third day's big attraction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to make sure I'm not absentminded\x01",
            "and miss today's as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4C89")

    label("loc_4C19")


    ChrTalk(
        0xFE,
        (
            "There's apparently a stage event going on\x01",
            "in the Harbor District today. I can't miss this,\x01",
            "no matter what!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C89")

    Jump("loc_4F8C")

    label("loc_4C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4D3C")

    ChrTalk(
        0xFE,
        (
            "Hoho. The fourth float in the parade was funded\x01",
            "by the Business Owners' Association, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The ornate, Eastern-style design was a dead\x01",
            "giveaway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F8C")

    label("loc_4D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4DAF")

    ChrTalk(
        0xFE,
        "The parade's happening today, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been looking forward to this for\x01",
            "a long time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F8C")

    label("loc_4DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4E56")

    ChrTalk(
        0xFE,
        (
            "Oh, wow. The crowd's already started\x01",
            "to gather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's the hurry? They've got five whole days\x01",
            "to soak in everything the festival has to offer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F8C")

    label("loc_4E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4F8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EF4")

    ChrTalk(
        0xFE,
        "Happy anniversary!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This year is Crossbell's 70th anniversary.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come over here and celebrate as well,\x01",
            "you youngsters!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4F8C")

    label("loc_4EF4")


    ChrTalk(
        0xFE,
        (
            "Fun little fact for you kids. Crossbell's a little\x01",
            "younger than I am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm turning...72 this year? That'll be\x01",
            "the same age as Mayor MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F8C")

    TalkEnd(0xFE)
    Return()

    # Function_15_4B08 end

    def Function_16_4F90(): pass

    label("Function_16_4F90")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_506A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5033")

    ChrTalk(
        0xFE,
        (
            "My little sister wouldn't stop begging me\x01",
            "to take her around the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, man. How'd it end up like this?\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x10E, 0x0)
    SetChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 6)
    Jump("loc_506A")

    label("loc_5033")


    ChrTalk(
        0xFE,
        (
            "*sigh* Okay, Meiling. Where do you\x01",
            "wanna go next?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_506A")

    TalkEnd(0xFE)
    Return()

    # Function_16_4F90 end

    def Function_17_506E(): pass

    label("Function_17_506E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_50CE")

    ChrTalk(
        0xFE,
        "These festivaws are the bestest!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanna go wook at all\x01",
            "the pwetty shops!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50CE")

    TalkEnd(0xFE)
    Return()

    # Function_17_506E end

    def Function_18_50D2(): pass

    label("Function_18_50D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5244")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51F3")

    ChrTalk(
        0xFE,
        (
            "A lot of businesses close down for the final\x01",
            "day of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even my boys were able to get the day\x01",
            "off, so they're goofing off in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My sons forgot about the housework...\x01",
            "How dare they push all of this onto me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_523F")

    label("loc_51F3")


    ChrTalk(
        0xFE,
        (
            "Damn those boys... They're just mocking me\x01",
            "at this point, aren't they?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_523F")

    Jump("loc_5581")

    label("loc_5244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_52D8")

    ChrTalk(
        0xFE,
        (
            "Wow... How many years has it been since I've\x01",
            "been able to see the parade this up close?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can hardly contain my excitement!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5581")

    label("loc_52D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_533D")

    ChrTalk(
        0xFE,
        "Hmm, salmon, salmon...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've still got a bit of time\x01",
            "until the parade starts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5581")

    label("loc_533D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5449")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53EF")

    ChrTalk(
        0xFE,
        (
            "*sigh* I'd never hear the end of it from my boys\x01",
            "if I end up not cooking dinner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, salmon, salmon... If only\x01",
            "they'd cook their own meals.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5444")

    label("loc_53EF")


    ChrTalk(
        0xFE,
        (
            "What, housewives aren't allowed to relax\x01",
            "during the Anniversary Festival, too?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5444")

    Jump("loc_5581")

    label("loc_5449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5581")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5526")

    ChrTalk(
        0xFE,
        "Festivals are really great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Many of the stores are holding sales, so I'm\x01",
            "treating myself to a bit of luxury for once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it's time I break out my\x01",
            "super secret stash of mira.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5581")

    label("loc_5526")


    ChrTalk(
        0xFE,
        (
            "I think I'll drop by Times later. There was a\x01",
            "certain something that caught my eye...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5581")

    TalkEnd(0xFE)
    Return()

    # Function_18_50D2 end

    def Function_19_5585(): pass

    label("Function_19_5585")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_55F2")

    ChrTalk(
        0xFE,
        "It's time for the festival's finale sale!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm going to stock up as much as I can.\x02",
    )

    CloseMessageWindow()
    Jump("loc_588E")

    label("loc_55F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_568E")
    OP_63(0xFE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "The parade was awfully...extravagant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should we really be spending that much\x01",
            "mira for our entertainment?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_588E")

    label("loc_568E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_573D")

    ChrTalk(
        0xFE,
        (
            "Judging by the time...I should\x01",
            "be able to catch the parade when\x01",
            "I'm finished shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I might be able to find a better view of\x01",
            "the parade over there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_588E")

    label("loc_573D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_57E4")

    ChrTalk(
        0xFE,
        (
            "Hmm... Looks like they're having a bunch\x01",
            "of Anniversary Festival sales here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wait, not yet. I haven't had a chance to look\x01",
            "at every store yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_588E")

    label("loc_57E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_588E")
    OP_63(0xFE, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xFE,
        (
            "I feel so conflicted over all of these\x01",
            "sales during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder which one of these stalls has the\x01",
            "best prices...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_588E")

    TalkEnd(0xFE)
    Return()

    # Function_19_5585 end

    def Function_20_5892(): pass

    label("Function_20_5892")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5964")

    ChrTalk(
        0xFE,
        (
            "Azel's insisting that he'll treat me to dinner\x01",
            "with money he earned with his part-time job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eating out is a bit of a luxury, but I suppose\x01",
            "it's okay to indulge every once in a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A9C")

    label("loc_5964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_59FC")

    ChrTalk(
        0xFE,
        "I'm pretty tired from playing around so much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "C'mere, Eugot. I'll give you a piggyback ride.\x01",
            "Shouldn't we be getting home soon?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A9C")

    label("loc_59FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5A9C")
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0xFE,
        "Hmm. Here should be fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do you remember how we would always\x01",
            "play together when we were kids?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "P-Please give it a rest already.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)

    label("loc_5A9C")

    TalkEnd(0xFE)
    Return()

    # Function_20_5892 end

    def Function_21_5AA0(): pass

    label("Function_21_5AA0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5C11")
    OP_4B(0x14, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BA2")

    ChrTalk(
        0xFE,
        "Azzy, what are we going to play next?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Playing 'Bracer' has been super fun\x01",
            "lately, but I don't know if you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "No, let's do that, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I'll do anything you wanna do today,\x01",
            "you got that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wow! Really?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5C08")

    label("loc_5BA2")


    ChrTalk(
        0xFE,
        (
            "Then you gotta be the\x01",
            "big, bad mafia man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "(Th-This is bringing back some\x01",
            "painful memories!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C08")

    OP_4C(0x14, 0xFF)
    Jump("loc_5CA6")

    label("loc_5C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5C67")

    ChrTalk(
        0xFE,
        "Yeaaaaah... The parade...sure was great...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*mumble*... Zzz...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CA6")

    label("loc_5C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5CA6")

    ChrTalk(
        0xFE,
        (
            "Hey, shouldn't the parade be\x01",
            "on its way already?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA6")

    TalkEnd(0xFE)
    Return()

    # Function_21_5AA0 end

    def Function_22_5CAA(): pass

    label("Function_22_5CAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5D3A")

    ChrTalk(
        0xFE,
        (
            "The three of us are going out\x01",
            "to eat today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The question now is, where do we eat?\x01",
            "Maybe somewhere in Central Square?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E35")

    label("loc_5D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5D99")

    ChrTalk(
        0xFE,
        "You doing okay, Eugot?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You're still tiny, so tell me if you get tired.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E35")

    label("loc_5D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5E35")

    ChrTalk(
        0xFE,
        (
            "I was thinking about watching the\x01",
            "parade with my family...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Am I at the right place, though? Oh, shoot.\x01",
            "It's on the other side, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E35")

    TalkEnd(0xFE)
    Return()

    # Function_22_5CAA end

    def Function_23_5E39(): pass

    label("Function_23_5E39")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5F02")
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x15,
        (
            "Let's head over to the park at\x01",
            "the Harbor District next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I hear there are plenty of food stalls to keep\x01",
            "you fed in the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Woohoo! This'll be a blast!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_6252")

    label("loc_5F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_60E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_606E")
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x16,
        (
            "I was chasing after the parade but kinda\x01",
            "lost track of where I was along the way...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "I wouldn't worry too much about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You see that gauntlet over there?\x01",
            "That's the Bracer Guild's emblem,\x01",
            "so everything is going to be just fine.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x16,
        (
            "Oh, you're totally right! That IS\x01",
            "the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    SetScenarioFlags(0x1, 3)
    Jump("loc_60DF")

    label("loc_606E")


    ChrTalk(
        0xFE,
        "The Bracer Guild is right over there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I think I'll go and ask for\x01",
            "directions to the main road.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60DF")

    Jump("loc_6252")

    label("loc_60E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6141")

    ChrTalk(
        0xFE,
        (
            "Hmm, I was planning to just go sightseeing,\x01",
            "but...urge to spend...RISING!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6252")

    label("loc_6141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_61B4")

    ChrTalk(
        0xFE,
        "I'm trying to think up the perfect souvenir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Perhaps something my grandchild would like.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6252")

    label("loc_61B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6252")

    ChrTalk(
        0xFE,
        "This sure is a Crossbellan festival, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been to more than I can count, but it seems\x01",
            "the older I get, the gaudier they become.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6252")

    TalkEnd(0xFE)
    Return()

    # Function_23_5E39 end

    def Function_24_6256(): pass

    label("Function_24_6256")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_626A")
    Call(0, 23)
    Jump("loc_6394")

    label("loc_626A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_62BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6285")
    Call(0, 23)
    Jump("loc_62BA")

    label("loc_6285")


    ChrTalk(
        0xFE,
        (
            "While we're at it, can we\x01",
            "go meet the bracers?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62BA")

    Jump("loc_6394")

    label("loc_62BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6317")

    ChrTalk(
        0xFE,
        (
            "C'mon, Gran! Let's go check out the\x01",
            "parade, not worry about veggies!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6394")

    label("loc_6317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6370")

    ChrTalk(
        0xFE,
        "Whoa, I've never seen these before!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yippee! This toy is awesome!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6394")

    label("loc_6370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6394")

    ChrTalk(
        0xFE,
        "Check this out, Gran!\x02",
    )

    CloseMessageWindow()

    label("loc_6394")

    TalkEnd(0xFE)
    Return()

    # Function_24_6256 end

    def Function_25_6398(): pass

    label("Function_25_6398")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_64AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_644D")

    ChrTalk(
        0xFE,
        (
            "I tried to avoid the ridiculous crowd by\x01",
            "coming on the second day, but, uh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...some plan that was. It's just as packed\x01",
            "as the opening day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_64AC")

    label("loc_644D")


    ChrTalk(
        0xFE,
        (
            "I don't know what I was expecting...\x01",
            "Yesterday's crowd hasn't died down\x01",
            "in the slightest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64AC")

    TalkEnd(0xFE)
    Return()

    # Function_25_6398 end

    def Function_26_64B0(): pass

    label("Function_26_64B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_65CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6552")

    ChrTalk(
        0xFE,
        "I'm finally back in Crossbell City.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, ignoring the fact that it's the festival,\x01",
            "was this place always this big a dump?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_65CF")

    label("loc_6552")


    ChrTalk(
        0xFE,
        (
            "Was Crossbell City always\x01",
            "this big of a dump?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The tranquility of Armorica Village\x01",
            "must have spoiled me, I guess...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65CF")

    TalkEnd(0xFE)
    Return()

    # Function_26_64B0 end

    def Function_27_65D3(): pass

    label("Function_27_65D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 7)), scpexpr(EXPR_END)), "loc_6697")
    TurnDirection(0x19, 0x104, 0)

    ChrTalk(
        0x19,
        (
            "#1604FHeh. I'd love to beat the hell outta that\x01",
            "black-haired kid. How about you, asswipes?\x02\x03",
            "#1602FI'll beat the piss outta every single\x01",
            "one of ya, too. Wazy included.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AA1")

    label("loc_6697")


    ChrTalk(
        0x19,
        (
            "#1600FYo, you losers still at it?\x02\x03",
            "#1602FHaha... You guys are lookin' pretty tired.\x01",
            "What's the matter, you weak?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FUnfortunately, not all of us have freakish\x01",
            "stamina like you, Wald.\x02\x03",
            "#0001FWait a second, are you planning to\x01",
            "go out to the festival again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#1602FWhat's it matter to ya?\x02\x03",
            "How we spend our time at the festival is\x01",
            "none of yer damn business, kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F(Right. I'm not sure what we expected.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203F(We are completely incompatible with them.)\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x19, 0x104, 750)
    Sleep(750)

    ChrTalk(
        0x19,
        (
            "#1601FBy the way, Red... Let's have ourselves a real\x01",
            "fight next time. No more pussyfootin', ya coward.\x02\x03",
            "#1602FI'm not gonna sit here quietly after seein' that\x01",
            "little stunt ya pulled back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FYa gotta give me a break, dude.\x02\x03",
            "#0301FI got a little carried away yesterday.\x01",
            "Happens to the best of us, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#1604FKeeps gettin' more and more interesting.\x01",
            "I just wanna take you on when\x01",
            "ya got your head outta your ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FHahaha. Yeah? Either way, it was kinda\x01",
            "my mistake to get all riled up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB6, 7)

    label("loc_6AA1")

    TalkEnd(0xFE)
    Return()

    # Function_27_65D3 end

    def Function_28_6AA5(): pass

    label("Function_28_6AA5")

    TalkBegin(0xFE)

    ChrTalk(
        0x1A,
        "Yo, Wald, where ya headin' today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "OH YEEEEEAH!! I think I'm goin'\x01",
            "down to Central Square!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_6AA5 end

    def Function_29_6B10(): pass

    label("Function_29_6B10")

    TalkBegin(0xFE)

    ChrTalk(
        0x1B,
        (
            "Dude, we have the right to enjoy this\x01",
            "festival as much as anyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "A bunch of cops don't have the authority\x01",
            "to strip us of that right!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_6B10 end

    def Function_30_6BAC(): pass

    label("Function_30_6BAC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_6BF3")

    ChrTalk(
        0x1C,
        (
            "Hold on a sec, Wald! I'll go\x01",
            "buy us some drinks!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C8D")

    label("loc_6BF3")


    ChrTalk(
        0x1C,
        (
            "For delinquents like us, your bros are\x01",
            "more important than your family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "Am I ditching my family? Hell yes.\x01",
            "I ain't no hypocrite.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x19, 0)
    SetChrFlags(0x1C, 0x10)
    SetScenarioFlags(0x1, 4)

    label("loc_6C8D")

    TalkEnd(0xFE)
    Return()

    # Function_30_6BAC end

    def Function_31_6C91(): pass

    label("Function_31_6C91")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(885)
    Sound(885, 2, 90, 0)
    FadeToBright(2000, 0)
    LoadEffect(0x7, "event\\ev308_00.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 7970, -300, 790, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -3800, -3000, -5130, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -12310, -3000, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x0, -7080, -3000, 1450, 135)
    SetChrPos(0x1, -7080, -3000, 1450, 135)
    SetChrPos(0x2, -7080, -3000, 1450, 135)
    SetChrPos(0x3, -7080, -3000, 1450, 135)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    OP_68(2040, -1400, -8500, 0)
    MoveCamera(89, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)
    OP_68(-16140, -1400, 1060, 10000)
    MoveCamera(37, 30, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(25000, 10000)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x375)
    SetScenarioFlags(0x5C, 0)
    NewScene("c120C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_6C91 end

    def Function_32_6E4F(): pass

    label("Function_32_6E4F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(25400, 700, 500, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 29700, -300, -100, 270)
    SetChrPos(0x102, 29700, -300, 1100, 270)
    SetChrPos(0x103, 31100, -300, -100, 270)
    SetChrPos(0x104, 31100, -300, 1100, 270)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    def lambda_6EEE():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6EEE)
    Sleep(50)

    def lambda_6F0B():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F0B)
    Sleep(50)

    def lambda_6F28():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6F28)
    Sleep(50)

    def lambda_6F45():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6F45)
    SetCameraDistance(20500, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)

    ChrTalk(
        0x104,
        (
            "#11P#0305FWell, actually, ain't it already past noon?\x02\x03",
            "#0306FDamn. Looks like we didn't make it back\x01",
            "in time for the parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0208FA shame.\x01",
            "(I had heard rumors of Mishy riding in a car...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#6P#0006FYeah, searching the Ancient Battlefield ended\x01",
            "up being a lot tougher than I anticipated...\x02\x03",
            "#0000FLet's head back to the SSS and take a\x01",
            "much-needed break.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_70FB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_70FB)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x102,
        "#0102FYes, let's.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 24700, -300, 500, 270)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xAA, 2)
    OP_29(0x44, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7180")
    OP_29(0x20, 0x4, 0x40)
    Jump("loc_7192")

    label("loc_7180")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7192")
    OP_29(0x20, 0x4, 0x40)

    label("loc_7192")

    EventEnd(0x5)
    Return()

    # Function_32_6E4F end

    def Function_33_7195(): pass

    label("Function_33_7195")

    EventBegin(0x0)
    OP_EE(0x0, 0x1)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07300.itc", 0x1E)
    LoadChrToIndex("chr/ch24100.itc", 0x1F)
    LoadChrToIndex("apl/ch50388.itc", 0x20)
    LoadChrToIndex("apl/ch50389.itc", 0x21)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x13)"), scpexpr(EXPR_END)), "loc_722C")
    Call(0, 34)
    Jump("loc_723C")

    label("loc_722C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_723C")
    Call(0, 35)

    label("loc_723C")

    OP_EE(0x0, 0xA)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetScenarioFlags(0x5C, 0)
    NewScene("c115C", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_33_7195 end

    def Function_34_7280(): pass

    label("Function_34_7280")

    OP_68(10180, 1450, 550, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11550, 0)
    SetChrPos(0x1D, -4130, -300, 4860, 315)
    SetChrPos(0x1E, 24040, -300, 870, 270)
    SetChrPos(0x101, 24000, -300, 0, 270)
    SetChrPos(0x102, 25000, -300, 1500, 270)
    SetChrPos(0x103, 26000, -300, 0, 270)
    SetChrPos(0x104, 27000, -300, 1500, 270)

    def lambda_7319():
        OP_95(0xFE, -60, -300, 660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7319)
    OP_68(-5970, 1450, 2950, 8500)
    BeginChrThread(0x1E, 3, 0, 42)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1E,
        "#5P#04A*pant* *pant*\x02",
    )

    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#5P#04ADon't underestimate me,\x01",
            "you friggin' brats...\x02",
        )
    )

    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#5P#10AJust you wait and see. I forged these legs of mine\x01",
            "through the struggle of climbing mountains back\x01",
            "in my youth. Like hell you'll catch me!\x02",
        )
    )

    OP_5A()
    Sleep(250)

    def lambda_7442():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7442)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(150)
    SetChrSubChip(0x1D, 0x1)
    WaitChrThread(0x1E, 3)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1E, 0x2)

    def lambda_7476():
        OP_95(0xFE, -6500, -300, 5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7476)
    Sound(814, 0, 100, 0)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    Sleep(300)
    SetChrSubChip(0x1E, 0x1)
    Sound(819, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x1E,
        "#6P#5SAck!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    SetChrSubChip(0x1D, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x1D, 0x1E)
    OP_93(0x1D, 0x10E, 0x12C)

    ChrTalk(
        0x1D,
        (
            "#11P#3400FOh, dear. I must have 'accidentally' stuck\x01",
            "my leg out while I wasn't looking.\x02\x03",
            "Are you still breathing, madam?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#6PY-You bitch... What the hell do you think\x01",
            "you're doing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#11P#3404FI see you have much energy to\x01",
            "spare, despite your old age.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(11280, 1450, -20, 0)
    MoveCamera(45, 21, 0, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0x101, 3, 0, 36)
    BeginChrThread(0x102, 3, 0, 36)
    BeginChrThread(0x103, 3, 0, 36)
    BeginChrThread(0x104, 3, 0, 36)
    OP_68(-2430, 1450, -2420, 7000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0001F#6P#10ACrap! Considering how fast she was running,\x01",
            "she's probably way ahe--\x02",
        )
    )

    OP_5A()

    ChrTalk(
        0x102,
        "#0105F#6P#10ALook over there, Lloyd!\x02",
    )

    OP_5A()

    ChrTalk(
        0x101,
        "#0005F#6P#10AHuh...?\x02",
    )

    OP_5A()
    Fade(1000)
    OP_68(-4840, 1650, 1400, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12680, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    ChrTalk(
        0x101,
        "#12P#0005FSh-She...ended up collapsing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0305FYo, check it out! The hot black-haired\x01",
            "lady is here, too!\x02\x03",
            "#0301FWait, hold on a sec... Did you do this?!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x87, 0xE1)

    ChrTalk(
        0x1D,
        (
            "#5P#3403FTalk later. Restraining her is of\x01",
            "the utmost urgency at the moment.\x02\x03",
            "#3400FShe still has pep in her step, so I\x01",
            "imagine she's quick to recover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#6PD-Damn you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FGood call, ma'am. You mind\x01",
            "helping me out, Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0105FN-Not at all.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 37)
    BeginChrThread(0x102, 3, 0, 38)
    BeginChrThread(0x103, 3, 0, 39)
    BeginChrThread(0x104, 3, 0, 40)
    Sleep(2000)
    BeginChrThread(0x1D, 3, 0, 41)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x1D, 3)

    ChrTalk(
        0x103,
        (
            "#12P#0200FI apologize, but could you accompany\x01",
            "us for the time being?\x02\x03",
            "#0203FHaving analyzed the situation, it is clear\x01",
            "your assistance was crucial in the arrest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5P#3403FVery well.\x02\x03",
            "#3400FI wasn't intending on standing out,\x01",
            "but perhaps this was fate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0303FRest easy, ma'am!\x02\x03",
            "#0309FAllow me the pleasure of escorting\x01",
            "a fine lady such as yourself!\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_34_7280 end

    def Function_35_7AAF(): pass

    label("Function_35_7AAF")

    OP_68(19130, 1850, -1230, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14450, 0)
    SetChrPos(0x1E, 24040, -300, 870, 270)
    SetChrPos(0x101, 30000, -300, 0, 270)
    SetChrPos(0x102, 31000, -300, 1500, 270)
    SetChrPos(0x103, 32000, -300, 0, 270)
    SetChrPos(0x104, 33000, -300, 1500, 270)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7B42():
        OP_95(0xFE, 20000, -300, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7B42)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x1E, 1)
    OP_63(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x1E)

    NpcTalk(
        0x1E,
        "Old Lady",
        "#5PI've finally made it to Crossbell.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1E,
        "Old Lady",
        (
            "#5PMy next step should be to meet up with\x01",
            "those boys near the station and airport,\x01",
            "then find a suitable place to set up shop.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1E,
        "Old Lady",
        (
            "#5PI never fail to make a boatload of cash\x01",
            "from here... After all, money DOES\x01",
            "grow on trees in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(400, 20, -1, -1)
    SetChrName("Lloyd")

    AnonymousTalk(
        0xFF,
        (
            "#0001FH-Hold on a second!\x01",
            "Please, wait!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)

    NpcTalk(
        0x1E,
        "Old Lady",
        "#5P...?\x02",
    )

    CloseMessageWindow()
    OP_68(21470, 1850, -490, 3000)
    OP_93(0x1E, 0x5A, 0x1F4)

    def lambda_7D2E():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D2E)

    def lambda_7D48():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7D48)

    def lambda_7D62():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7D62)

    def lambda_7D7C():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7D7C)

    def lambda_7D96():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D96)

    def lambda_7DA7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7DA7)

    def lambda_7DB8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7DB8)

    def lambda_7DC9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7DC9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#0003F#11PWe're with the Crossbell Police Department,\x01",
            "Special Support Section.\x02\x03",
            "#0001FSorry to bother you, ma'am, but\x01",
            "we'd like to ask you a few questions.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1E,
        "Old Lady",
        "#6P...The...police?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1E,
        "Old Lady",
        (
            "#6PWh-What business would the police\x01",
            "have with an old lady like myself?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1E,
        "Old Lady",
        (
            "#6PI'm in a bit of a hurry to meet my grandson.\x01",
            "I'll be late if you hold me up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0001FThe jig is up, ma'am. We already know\x01",
            "you're the counterfeit dealer.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1E,
        "Old Lady",
        "#6P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0101FSurrender yourself peacefully, or else\x01",
            "we'll have to resort to using force.\x02\x03",
            "#0103FSo please, come peacefu--\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1E,
        "Old Lady",
        "#6PDon't...\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x1E,
        (
            "#6P#5SDON'T UNDERESTIMATE ME,\x01",
            "YOU IDIOTIC WHIPPERSNAPPERS!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0011FWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#0105FEek!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0305FShe's gone off her rocker!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0201FHer true nature has finally been revealed.\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x1E,
        (
            "#6P#5SThink you've got me cornered, do you?!\x01",
            "A bunch of two-bit cops like yourselves\x01",
            "won't catch me!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x1E,
        (
            "#6P#5SSure, not everything went as\x01",
            "planned, but I'll run to the ends of\x01",
            "the continent before I get caught!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#6P#5SIf you think you can\x01",
            "catch me so easily...\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_8292():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8292)
    Sleep(1000)

    def lambda_82AF():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_82AF)
    Sleep(1000)

    def lambda_82CC():
        OP_95(0xFE, 15000, -300, 1030, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_82CC)
    Sound(250, 0, 80, 0)
    PlayBGM("ed7401", 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-50, 200, -1, -1)
    SetChrName("Counterfeit Dealer")

    AnonymousTalk(
        0x1E,
        (
            "#5S...then why don't you\x01",
            "go ahead and try me?!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
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
        0x101,
        "#11P#0011FSh-She's actually making a break for it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0306FWh-Where the hell did that whole\x01",
            "nicest-grandma-you'd-ever-meet\x01",
            "charade disappear to?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0205FI failed to anticipate this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0106FIs it REALLY the time for this, you guys?!\x02\x03",
            "#0101FWe need to hurry up and chase after her,\x01",
            "or else she might actually escape!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0001FT-True... Let's go after her!\x02",
    )

    CloseMessageWindow()

    def lambda_8542():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8542)

    def lambda_855C():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_855C)

    def lambda_8576():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8576)

    def lambda_8590():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8590)
    Sleep(1500)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x1E, 11450, -300, 1000, 270)
    SetChrPos(0x101, 24000, -300, 0, 270)
    SetChrPos(0x102, 25000, -300, 1500, 270)
    SetChrPos(0x103, 26000, -300, 0, 270)
    SetChrPos(0x104, 27000, -300, 1500, 270)
    SetChrPos(0x1D, 8000, -300, 190, 270)
    OP_68(9270, 1450, -1540, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11550, 0)
    OP_68(-5970, 1450, 2950, 5000)
    BeginChrThread(0x1E, 3, 0, 42)
    BeginChrThread(0x101, 3, 0, 36)
    BeginChrThread(0x102, 3, 0, 36)
    BeginChrThread(0x103, 3, 0, 36)
    BeginChrThread(0x104, 3, 0, 36)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x1E,
        (
            "#5P#03ADon't underestimate me,\x01",
            "you friggin' brats...\x02",
        )
    )

    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#5P#05AI forged these legs of mine through the struggle\x01",
            "of climbing mountains back in my youth. Like\x01",
            "hell you'll catch me!\x02",
        )
    )

    OP_5A()
    WaitChrThread(0x1E, 3)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1E, 0x2)

    def lambda_874D():
        OP_95(0xFE, -6500, -300, 5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_874D)
    Sound(814, 0, 100, 0)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    Sleep(300)
    SetChrSubChip(0x1E, 0x1)
    Sound(819, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x1E,
        "#6P#5SAck!\x02",
    )

    OP_5A()
    OP_68(-4030, 1450, 1640, 2000)
    MoveCamera(45, 21, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(12760, 2000)
    OP_6F(0x1)

    ChrTalk(
        0x102,
        "#11P#0105FD-Did she just...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0305FOuch... That's gonna leave a mark.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0206FAnalysis: possible brain damage.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FI feel a little sorry for her now, but we have no\x01",
            "choice... Let's restrain her while we can!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-5970, 1450, 2950, 2000)
    BeginChrThread(0x101, 3, 0, 37)
    BeginChrThread(0x102, 3, 0, 38)
    BeginChrThread(0x103, 3, 0, 43)
    BeginChrThread(0x104, 3, 0, 44)
    Sleep(2000)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    ChrTalk(
        0x104,
        (
            "#11P#0306FGimme a break, man... It's a good thing\x01",
            "she wasn't able to break loose.\x02\x03",
            "#0300FStop tryin' to be a daredevil, you fossil!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#6PGrr... Gah!\x01",
            "Who are you callin' a fossil, you jackass?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FRestraining her required more effort\x01",
            "than I thought necessary...\x02\x03",
            "#0200FHowever, in the end...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Woman's Voice")
    SetMessageWindowPos(350, 0, -1, -1)

    ChrTalk(
        0x1D,
        "...it was a job well done.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8AC3():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8AC3)

    def lambda_8AD0():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8AD0)

    def lambda_8ADD():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8ADD)

    def lambda_8AEA():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8AEA)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0x1D, 3, 0, 45)
    OP_68(-3950, 1450, 1920, 2000)
    WaitChrThread(0x1D, 3)

    ChrTalk(
        0x1D,
        (
            "#3404FI suppose this is the first arrest I've\x01",
            "ever had the pleasure of having\x01",
            "front-row seats to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FAh, it's you...\x02\x03",
            "#0004FThanks for the advice. One more step\x01",
            "and she would have gotten away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FRight in the nick of time, eh?\x01",
            "'Preciate the assist!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FWe cannot discount the element of luck\x01",
            "involved, either, considering she tripped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FTrue... She must have tripped over one\x01",
            "of the rocks on the road.\x02\x03",
            "#0100FAnd despite falling flat on her face,\x01",
            "her injuries seem fairly minor.\x02\x03",
            "#0103FIf you take everything into consideration,\x01",
            "there are too many coincidences piling\x01",
            "on top of each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#3403FHmm? Well, the situation appears to\x01",
            "have sorted itself out.\x02\x03",
            "Perhaps this old lady stumbling wasn't\x01",
            "a coincidence, but rather an inevitability?\x02\x03",
            "#3400FRegardless, luck has abandoned her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#6PD-Damn you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FCome on, guys. Let's escort\x01",
            "her down to the station.\x02\x03",
            "#0006FWe don't want her escaping again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FRight, the sooner the better.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI apologize, but could you accompany\x01",
            "us for the time being?\x02\x03",
            "While your assistance in the arrest was\x01",
            "valuable, we are still required to ask\x01",
            "you a few questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#3404FVery well.\x02\x03",
            "#3400FI wasn't intending on standing out,\x01",
            "but perhaps this was fate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FRest easy, ma'am!\x02\x03",
            "#0309FAllow me the pleasure of escorting\x01",
            "a fine lady such as yourself!\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_35_7AAF end

    def Function_36_906D(): pass

    label("Function_36_906D")


    def lambda_9072():
        OP_98(0xFE, 0xFFFF9A70, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9072)
    WaitChrThread(0xFE, 1)

    def lambda_9090():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9090)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_36_906D end

    def Function_37_909D(): pass

    label("Function_37_909D")

    OP_68(-5580, 1450, 2490, 3000)

    def lambda_90B3():
        OP_95(0xFE, -7010, -300, 4430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90B3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x12C)
    Return()

    # Function_37_909D end

    def Function_38_90D4(): pass

    label("Function_38_90D4")


    def lambda_90D9():
        OP_95(0xFE, -5410, -300, 4430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90D9)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_90D4 end

    def Function_39_90F3(): pass

    label("Function_39_90F3")


    def lambda_90F8():
        OP_95(0xFE, -4750, -300, 2009, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90F8)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x1D, 300)
    Return()

    # Function_39_90F3 end

    def Function_40_9119(): pass

    label("Function_40_9119")


    def lambda_911E():
        OP_95(0xFE, -3190, -300, 2410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_911E)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x1D, 300)
    Return()

    # Function_40_9119 end

    def Function_41_913F(): pass

    label("Function_41_913F")


    def lambda_9144():
        OP_95(0xFE, -3800, -300, 3830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9144)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_41_913F end

    def Function_42_9165(): pass

    label("Function_42_9165")


    def lambda_916A():
        OP_95(0xFE, -60, -300, 660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_916A)
    WaitChrThread(0x1E, 1)

    def lambda_9188():
        OP_95(0xFE, -5000, -300, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_9188)
    WaitChrThread(0x1E, 1)
    Return()

    # Function_42_9165 end

    def Function_43_91A2(): pass

    label("Function_43_91A2")


    def lambda_91A7():
        OP_95(0xFE, -4750, -300, 2009, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91A7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_43_91A2 end

    def Function_44_91C1(): pass

    label("Function_44_91C1")


    def lambda_91C6():
        OP_95(0xFE, -4190, -300, 4030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91C6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_91C1 end

    def Function_45_91E0(): pass

    label("Function_45_91E0")


    def lambda_91E5():
        OP_98(0xFE, 0xFFFFE0C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91E5)
    WaitChrThread(0xFE, 1)

    def lambda_9203():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9203)

    def lambda_9210():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9210)

    def lambda_921D():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_921D)

    def lambda_922A():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_922A)

    def lambda_9237():
        OP_95(0xFE, -2870, -300, 2070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9237)
    OP_68(-5360, 1450, 2770, 2000)
    WaitChrThread(0xFE, 1)

    def lambda_9266():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9266)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_91E0 end

    def Function_46_9273(): pass

    label("Function_46_9273")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 7)), scpexpr(EXPR_END)), "loc_92B2")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an Eastern-looking Jizo.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_B0D5")

    label("loc_92B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_950A")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an Eastern-looking Jizo.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#0305FHeh. I knew East Street was, well, Eastern,\x01",
            "but I can't say I was expectin' them to\x01",
            "actually be worshipin' a big Jizo statue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FThis is my first time encountering one.\x01",
            "It has an enormous face.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#0205FWhat is the purpose of this counter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FI'd imagine it's used for offerings.\x02\x03",
            "We can try offering any exceptional\x01",
            "dishes we make here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, I guess we DO cook for ourselves often...\x02\x03",
            "If we cook any especially delicious dishes,\x01",
            "let's give this whole offering thing a try.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x98, 0)
    Jump("loc_B0D5")

    label("loc_950A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_9546")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an Eastern-looking Jizo.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_B0D5")

    label("loc_9546")

    Call(0, 47)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95F8")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an Eastern-looking Jizo.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#0000FWe don't have any dishes appropriate\x01",
            "for an offering right now.\x02\x03",
            "Let's try bringing one next time.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_95F8")

    Call(0, 48)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9896")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a letter accompanied by a\x01",
            "glimmering quartz.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "To you, who has offered the great Jizo with\x01",
            "unknown kindness, I give thee my sincerest\x01",
            "thanks. While such a letter may seem crude,\x01",
            "as a person whose heart is cleansed daily by\x01",
            "our deeds, I could not help but take action.\x01",
            "I assure you, these are my genuine feelings.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Though presumptuous to act on behalf of the\x01",
            "great Jizo, I have prepared an offering of my\x01",
            "gratitude. I pray that it will be of some use to\x01",
            "you. I hope you will accept it.\x01\x01",
            "~ From an anonymous neighbor\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0xAB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0xAB, 1)
    SetScenarioFlags(0x98, 7)
    Jump("loc_B0D5")

    label("loc_9896")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AAD")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " and a letter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I see that you have come to continue offering\x01",
            "the finest dishes to the Jizo under this bright\x01",
            "and sunny sky. I picked up my writing brush\x01",
            "while remembering your generous offerings\x01",
            "of fine cuisine. Kind soul, I thank you for the\x01",
            "constant warmth you spread across the land.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This is the extent of what I can offer you,\x01",
            "but please accept this gift on my behalf.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x1F4, 1)
    SetScenarioFlags(0x98, 6)
    Jump("loc_B0D5")

    label("loc_9AAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CDD")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " and a letter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "To the one who offers bountiful food, I pray\x01",
            "this letter reaches you. Each time I pass by\x01",
            "the statue, I am touched by your kind heart\x01",
            "and feel invigorated. Despite the strife that\x01",
            "plagues Crossbell, I feel society will become\x01",
            "brighter by the day if people like yourself\x01",
            "continue to persist with kindness.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Thank you for the hope you bring. Though a\x01",
            "meager gift, I hope you accept it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x1F4, 1)
    SetScenarioFlags(0x98, 5)
    Jump("loc_B0D5")

    label("loc_9CDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9EDE")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " and a letter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I am merely one who clasps his hands in prayer\x01",
            "to the statue every morning. I am jubilant to\x01",
            "learn that there is another soul other than\x01",
            "myself that communes with the great deity.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Though we have not directly met before, and\x01",
            "despite not knowing your true nature, it is my\x01",
            "belief that you remain faithful. Please, accept\x01",
            "this small gift.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x1F4, 1)
    SetScenarioFlags(0x98, 4)
    Jump("loc_B0D5")

    label("loc_9EDE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A04F")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " and a letter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "To you, who faithfully offers dishes, I give thanks.\x01",
            "I believe the gracious Jizo is delighted to be visited\x01",
            "by such kind, generous people. Though meager,\x01",
            "please accept this token of my appreciation.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x1F4, 1)
    SetScenarioFlags(0x98, 3)
    Jump("loc_B0D5")

    label("loc_A04F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A17A")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " and a letter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Though I know not who you are, I thank you for\x01",
            "your kind offering. As thanks, please accept this\x01",
            "small token of my appreciation.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x1F4, 1)
    SetScenarioFlags(0x98, 2)
    Jump("loc_B0D5")

    label("loc_A17A")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An Eastern-style Jizo is present before you.\x02\x03",
            "Offer a supreme dish?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A1D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0D5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A228")
    MenuCmd(1, 1, "Dynasty Noodles")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_END)), "loc_A21E")
    Call(0, 13)

    label("loc_A21E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A264")
    MenuCmd(1, 1, "Huanglong Mapo Tofu")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_END)), "loc_A25A")
    Call(0, 13)

    label("loc_A25A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A29B")
    MenuCmd(1, 1, "Baihu Chao Fan")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_END)), "loc_A291")
    Call(0, 13)

    label("loc_A291")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A29B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A2D1")
    MenuCmd(1, 1, "Elegant Steak")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_END)), "loc_A2C7")
    Call(0, 13)

    label("loc_A2C7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A307")
    MenuCmd(1, 1, "Aromatic Stew")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_END)), "loc_A2FD")
    Call(0, 13)

    label("loc_A2FD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A33F")
    MenuCmd(1, 1, "Gorgeous Hotpot")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_END)), "loc_A335")
    Call(0, 13)

    label("loc_A335")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A33F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A379")
    MenuCmd(1, 1, "Expressive Hotpot")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_END)), "loc_A36F")
    Call(0, 13)

    label("loc_A36F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A3B2")
    MenuCmd(1, 1, "Resurrection Fry")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_END)), "loc_A3A8")
    Call(0, 13)

    label("loc_A3A8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A3B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A3EE")
    MenuCmd(1, 1, "Radiant Omelet Rice")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_END)), "loc_A3E4")
    Call(0, 13)

    label("loc_A3E4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A428")
    MenuCmd(1, 1, "Radiant Carbonara")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_END)), "loc_A41E")
    Call(0, 13)

    label("loc_A41E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A45C")
    MenuCmd(1, 1, "King Burger")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_END)), "loc_A452")
    Call(0, 13)

    label("loc_A452")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A45C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A490")
    MenuCmd(1, 1, "Queen Pizza")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_END)), "loc_A486")
    Call(0, 13)

    label("loc_A486")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A4CB")
    MenuCmd(1, 1, "Partners' Sandwich")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_END)), "loc_A4C1")
    Call(0, 13)

    label("loc_A4C1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A505")
    MenuCmd(1, 1, "Mother's Lunchbox")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_END)), "loc_A4FB")
    Call(0, 13)

    label("loc_A4FB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A53C")
    MenuCmd(1, 1, "Full Moon Soup")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_END)), "loc_A532")
    Call(0, 13)

    label("loc_A532")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A53C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A577")
    MenuCmd(1, 1, "Crescent Moon Soup")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_END)), "loc_A56D")
    Call(0, 13)

    label("loc_A56D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A5AD")
    MenuCmd(1, 1, "Pure Cut Cake")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_END)), "loc_A5A3")
    Call(0, 13)

    label("loc_A5A3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A5E1")
    MenuCmd(1, 1, "Deep Yellow")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_END)), "loc_A5D7")
    Call(0, 13)

    label("loc_A5D7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A5E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A617")
    MenuCmd(1, 1, "Powdered Snow")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_END)), "loc_A60D")
    Call(0, 13)

    label("loc_A60D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A64E")
    MenuCmd(1, 1, "Drifting Cloud")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_END)), "loc_A644")
    Call(0, 13)

    label("loc_A644")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A684")
    MenuCmd(1, 1, "Supreme Latte")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_END)), "loc_A67A")
    Call(0, 13)

    label("loc_A67A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A6B9")
    MenuCmd(1, 1, "Ultimate Mix")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_END)), "loc_A6AF")
    Call(0, 13)

    label("loc_A6AF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A6B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A6F2")
    MenuCmd(1, 1, "Nightmare Killer")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_END)), "loc_A6E8")
    Call(0, 13)

    label("loc_A6E8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A6F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A730")
    MenuCmd(1, 1, "Moonlight Butterflies")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_END)), "loc_A726")
    Call(0, 13)

    label("loc_A726")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A730")

    MenuCmd(1, 1, "Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A771")
    Jump("loc_B0D0")

    label("loc_A771")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A7DD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7D3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x190, 1)
    SetScenarioFlags(0x99, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x190),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_A7D3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A82A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A820")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x193, 1)
    SetScenarioFlags(0x99, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x193),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_A820")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A82A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A877")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A86D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x196, 1)
    SetScenarioFlags(0x99, 2)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x196),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_A86D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A8C4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8BA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x199, 1)
    SetScenarioFlags(0x99, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x199),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_A8BA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A8C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A911")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A907")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19C, 1)
    SetScenarioFlags(0x99, 4)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x19C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_A907")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A95E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A954")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19F, 1)
    SetScenarioFlags(0x99, 5)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x19F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_A954")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A95E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A9AB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9A1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A2, 1)
    SetScenarioFlags(0x99, 6)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1A2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_A9A1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A9AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A9F8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9EE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A5, 1)
    SetScenarioFlags(0x99, 7)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1A5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_A9EE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A9F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AA45")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA3B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A8, 1)
    SetScenarioFlags(0x9A, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1A8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_AA3B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AA45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AA92")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA88")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AB, 1)
    SetScenarioFlags(0x9A, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1AB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_AA88")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AA92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AADF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAD5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AE, 1)
    SetScenarioFlags(0x9A, 2)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1AE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_AAD5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AB2C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB22")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B1, 1)
    SetScenarioFlags(0x9A, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_AB22")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AB2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AB79")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB6F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B4, 1)
    SetScenarioFlags(0x9A, 4)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_AB6F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AB79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ABC6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABBC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B7, 1)
    SetScenarioFlags(0x9A, 5)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_ABBC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ABC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AC13")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC09")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BA, 1)
    SetScenarioFlags(0x9A, 6)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1BA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_AC09")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AC13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AC60")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC56")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BD, 1)
    SetScenarioFlags(0x9A, 7)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1BD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_AC56")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AC60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ACAD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACA3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C0, 1)
    SetScenarioFlags(0x9B, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_ACA3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ACAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ACFA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACF0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C3, 1)
    SetScenarioFlags(0x9B, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_ACF0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ACFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AD47")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD3D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C6, 1)
    SetScenarioFlags(0x9B, 2)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_AD3D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AD47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AD94")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD8A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C9, 1)
    SetScenarioFlags(0x9B, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_AD8A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AD94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ADE1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADD7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CC, 1)
    SetScenarioFlags(0x9B, 4)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1CC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_ADD7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ADE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AE2E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE24")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CF, 1)
    SetScenarioFlags(0x9B, 5)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_AE24")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AE2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AE7B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE71")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D2, 1)
    SetScenarioFlags(0x9B, 6)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1D2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_AE71")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AE7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AEC8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEBE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D5, 1)
    SetScenarioFlags(0x9B, 7)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Offered ",
            scpstr(SCPSTR_CODE_ITEM, 0x1D5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )


    label("loc_AEBE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AEC8")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0CD")

    ChrTalk(
        0x101,
        (
            "#0000FAll right. Let's try bringing a different\x01",
            "dish next time.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFAE")

    ChrTalk(
        0x102,
        (
            "#0100FWe should avoid bringing any repeat\x01",
            "dishes, Lloyd. One of each kind should\x01",
            "suffice, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0A5")

    label("loc_AFAE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B02F")

    ChrTalk(
        0x103,
        (
            "#0200FIt may be impolite of us to offer the\x01",
            "same dish twice. I recommend\x01",
            "providing a variety of meals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0A5")

    label("loc_B02F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0A5")

    ChrTalk(
        0x104,
        (
            "#0300FBit rude to bring the guy the\x01",
            "same grub every time, eh?\x01",
            "Let's try to shake it up a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0A5")


    ChrTalk(
        0x101,
        "#0000FOkay. Sounds like a plan.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x98, 1)

    label("loc_B0CD")

    SetScenarioFlags(0x1, 7)

    label("loc_B0D0")

    Jump("loc_A1D4")

    label("loc_B0D5")

    TalkEnd(0xFF)
    Return()

    # Function_46_9273 end

    def Function_47_B0D9(): pass

    label("Function_47_B0D9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B0FC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B0FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B115")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B12E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B12E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B147")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B160")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B179")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B192")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B1AB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B1AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B1C4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B1C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B1DD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B1DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B1F6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B1F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B20F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B20F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B228")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B241")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B25A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B25A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B273")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B28C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B28C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B2A5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B2BE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B2D7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B2D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B2F0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B309")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B322")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B33B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B33B")

    Return()

    # Function_47_B0D9 end

    def Function_48_B33C(): pass

    label("Function_48_B33C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_END)), "loc_B359")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_END)), "loc_B36C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B36C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_END)), "loc_B37F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_END)), "loc_B392")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_END)), "loc_B3A5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_END)), "loc_B3B8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_END)), "loc_B3CB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B3CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_END)), "loc_B3DE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_END)), "loc_B3F1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_END)), "loc_B404")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_END)), "loc_B417")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_END)), "loc_B42A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B42A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_END)), "loc_B43D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_END)), "loc_B450")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_END)), "loc_B463")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_END)), "loc_B476")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_END)), "loc_B489")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_END)), "loc_B49C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B49C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_END)), "loc_B4AF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_END)), "loc_B4C2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_END)), "loc_B4D5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_END)), "loc_B4E8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_END)), "loc_B4FB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_END)), "loc_B50E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B50E")

    Return()

    # Function_48_B33C end

    SaveToFile()

Try(main)
