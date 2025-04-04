from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1000.bin",                # FileName
        "c1000",                    # MapName
        "c1000",                    # Location
        0x0010,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 16, 0, 8, 0, 9],
    )

    BuildStringList((
        "c1000",                  # 0
        "Cronk",                  # 1
        "Dinz",                   # 2
        "Lilly",                  # 3
        "Marte",                  # 4
        "Anne",                   # 5
        "Old Man Renault",        # 6
        "Roy",                    # 7
        "Roose",                  # 8
        "Meiling",                # 9
        "Susan",                  # 10
        "Gillet",                 # 11
        "Couta",                  # 12
        "Tourist",                # 13
        "Estelle",                # 14
        "Joshua",                 # 15
        "Shizuku",                # 16
        "列車",                   # 17
        "Central Square",         # 18
        "West Street",            # 19
        "Administrative District",# 20
        "Residential District",   # 21
        "Entertainment District", # 22
        "East Street",            # 23
        "Downtown District",      # 24
        "Harbor District",        # 25
        "IBC",                    # 26
        "Station Street",         # 27
        "Back Alley",             # 28
        "Ursula Road",            # 29
        "East Crossbell Highway", # 30
        "West Crossbell Highway", # 31
        "Mainz Mountain Path",    # 32
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch24800.itc",                   # 01
        "chr/ch24900.itc",                   # 02
        "chr/ch23500.itc",                   # 03
        "chr/ch21100.itc",                   # 04
        "chr/ch24000.itc",                   # 05
        "chr/ch21200.itc",                   # 06
        "chr/ch21500.itc",                   # 07
        "chr/ch10300.itc",                   # 08
        "chr/ch26200.itc",                   # 09
        "chr/ch21400.itc",                   # 0A
        "chr/ch00600.itc",                   # 0B
        "chr/ch00700.itc",                   # 0C
        "chr/ch08700.itc",                   # 0D
        "chr/ch22800.itc",                   # 0E
    ))

    DeclNpc(-24409,  -3000,   5239,    180,  261,  0x0, 0,   14,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-13039,  -3000,   -810,    225,  261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-16500,  -3000,   2920,    45,   261,  0x0, 0,   2,   0,   0,   6,   0,   12,  255,  0)
    DeclNpc(-4559,   -3000,   -8949,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(26200,   -300,    -1049,   270,  261,  0x0, 0,   4,   0,   0,   1,   0,   17,  255,  0)
    DeclNpc(-40490,  -300,    15850,   90,   261,  0x0, 0,   5,   0,   0,   5,   0,   18,  255,  0)
    DeclNpc(-18200,  -300,    18139,   270,  261,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(5300,    -3000,   -13220,  270,  389,  0x0, 0,   6,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-22280,  -300,    18370,   225,  261,  0x0, 0,   7,   0,   0,   2,   0,   20,  255,  0)
    DeclNpc(-8470,   -3000,   -7349,   45,   261,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-8470,   -3000,   -7349,   45,   389,  0x0, 0,   9,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-15939,  -3000,   -600,    45,   261,  0x0, 0,   10,  0,   0,   3,   0,   23,  255,  0)
    DeclNpc(-4190,   -300,    -1210,   225,  389,  0x0, 0,   0,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-23690,  -3000,   3190,    270,  405,  0x0, 0,   11,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-25129,  -3000,   3630,    90,   405,  0x0, 0,   12,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-23530,  -3000,   4090,    270,  405,  0x0, 0,   13,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 36,  -7.920000076293945,    13.430000305175781,    -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.9600000381469727,    -6.715000152587891,    0.10000000149011612,   1.0])
    DeclEvent(0x0000, 0, 37,  -7.789999961853027,    -7.980000019073486,    -3.0,                  25.0,                  [0.35355326533317566,  0.1414213925600052,    -0.0,                  0.0,                   -0.35355350375175476,  0.14142130315303802,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.06717704236507416,  2.2302145957946777,    0.5999999642372131,    1.0])
    DeclEvent(0x0000, 0, 38,  2.200000047683716,     -2.2300000190734863,   -0.30000001192092896,  25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.4399999976158142,   1.1150000095367432,    0.05999999865889549,   1.0])

    DeclActor(17360,   -300,    4630,    1200,    17530,   1500,    5120,    0x007C, 0,  39, 0x0000)

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
    PlaceName(-98.33000183105469, 0.0, 1.440000057220459, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_6F0",          # 00, 0
        "Function_1_7A8",          # 01, 1
        "Function_2_841",          # 02, 2
        "Function_3_86C",          # 03, 3
        "Function_4_8E1",          # 04, 4
        "Function_5_92E",          # 05, 5
        "Function_6_9EF",          # 06, 6
        "Function_7_A3C",          # 07, 7
        "Function_8_AAC",          # 08, 8
        "Function_9_F19",          # 09, 9
        "Function_10_10A5",        # 0A, 10
        "Function_11_26CD",        # 0B, 11
        "Function_12_406D",        # 0C, 12
        "Function_13_5794",        # 0D, 13
        "Function_14_75E7",        # 0E, 14
        "Function_15_8D84",        # 0F, 15
        "Function_16_8EC7",        # 10, 16
        "Function_17_9090",        # 11, 17
        "Function_18_A37D",        # 12, 18
        "Function_19_BCBC",        # 13, 19
        "Function_20_CDCA",        # 14, 20
        "Function_21_D61B",        # 15, 21
        "Function_22_E3CB",        # 16, 22
        "Function_23_E4A4",        # 17, 23
        "Function_24_F4CB",        # 18, 24
        "Function_25_F6FA",        # 19, 25
        "Function_26_F847",        # 1A, 26
        "Function_27_F940",        # 1B, 27
        "Function_28_FA80",        # 1C, 28
        "Function_29_FE9C",        # 1D, 29
        "Function_30_10469",       # 1E, 30
        "Function_31_10681",       # 1F, 31
        "Function_32_1179C",       # 20, 32
        "Function_33_117F9",       # 21, 33
        "Function_34_12263",       # 22, 34
        "Function_35_12792",       # 23, 35
        "Function_36_12C42",       # 24, 36
        "Function_37_12ED7",       # 25, 37
        "Function_38_13018",       # 26, 38
        "Function_39_13159",       # 27, 39
        "Function_40_15359",       # 28, 40
        "Function_41_155BC",       # 29, 41
    ))


    def Function_0_6F0(): pass

    label("Function_0_6F0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_730"),
        (1, "loc_73C"),
        (2, "loc_748"),
        (3, "loc_754"),
        (4, "loc_760"),
        (5, "loc_76C"),
        (6, "loc_778"),
        (SWITCH_DEFAULT, "loc_784"),
    )


    label("loc_730")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_73C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_748")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_754")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_760")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_76C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_778")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_784")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_790")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_7A7")

    Return()

    # Function_0_6F0 end

    def Function_1_7A8(): pass

    label("Function_1_7A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_840")
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
    Jump("Function_1_7A8")

    label("loc_840")

    Return()

    # Function_1_7A8 end

    def Function_2_841(): pass

    label("Function_2_841")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_86B")
    OP_94(0xFE, 0xFFFFB000, 0x4ECA, 0xFFFFA8EE, 0x3F01, 0x3E8)
    Sleep(300)
    Jump("Function_2_841")

    label("loc_86B")

    Return()

    # Function_2_841 end

    def Function_3_86C(): pass

    label("Function_3_86C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E0")
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -22610, -3000, 3390, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_3_86C")

    label("loc_8E0")

    Return()

    # Function_3_86C end

    def Function_4_8E1(): pass

    label("Function_4_8E1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_92D")
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -9950, -3000, -6670, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_4_8E1")

    label("loc_92D")

    Return()

    # Function_4_8E1 end

    def Function_5_92E(): pass

    label("Function_5_92E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9EE")
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
    Jump("Function_5_92E")

    label("loc_9EE")

    Return()

    # Function_5_92E end

    def Function_6_9EF(): pass

    label("Function_6_9EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A3B")
    OP_95(0xFE, -15130, -3000, 1420, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    OP_95(0xFE, -16500, -3000, 2920, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    Jump("Function_6_9EF")

    label("loc_A3B")

    Return()

    # Function_6_9EF end

    def Function_7_A3C(): pass

    label("Function_7_A3C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAB")
    SetChrPos(0x18, 70000, -27500, -17600, 0)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x0, 0x18)
    OP_49()
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_9B(0x0, 0x18, 0x10E, 0x30D40, 0x4E20, 0x0)
    SetChrFlags(0x18, 0x80)
    SetMapObjFlags(0x0, 0x4)

    label("loc_AAB")

    Return()

    # Function_7_A3C end

    def Function_8_AAC(): pass

    label("Function_8_AAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCC")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B77")
    SetChrPos(0x0, -20760, -310, 33300, 180)
    SetChrPos(0x1, -20760, -310, 33300, 180)
    SetChrPos(0x2, -20760, -310, 33300, 180)
    SetChrPos(0x3, -20760, -310, 33300, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4A")
    SetChrPos(0x4, -20760, -310, 33300, 180)
    SetChrPos(0x5, -20760, -310, 33300, 180)
    Jump("loc_B69")

    label("loc_B4A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B69")
    SetChrPos(0x4, -20760, -310, 33300, 180)

    label("loc_B69")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCC")

    label("loc_B77")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2B")
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    SetChrPos(0x1, 1910, -3000, -35980, 0)
    SetChrPos(0x2, 1910, -3000, -35980, 0)
    SetChrPos(0x3, 1910, -3000, -35980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFE")
    SetChrPos(0x4, 1910, -3000, -35980, 0)
    SetChrPos(0x5, 1910, -3000, -35980, 0)
    Jump("loc_C1D")

    label("loc_BFE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C1D")
    SetChrPos(0x4, 1910, -3000, -35980, 0)

    label("loc_C1D")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCC")

    label("loc_C2B")

    SetChrPos(0x0, -29790, -330, 13830, 90)
    SetChrPos(0x1, -29790, -330, 13830, 90)
    SetChrPos(0x2, -29790, -330, 13830, 90)
    SetChrPos(0x3, -29790, -330, 13830, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA4")
    SetChrPos(0x4, -29790, -330, 13830, 90)
    SetChrPos(0x5, -29790, -330, 13830, 90)
    Jump("loc_CC3")

    label("loc_CA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC3")
    SetChrPos(0x4, -29790, -330, 13830, 90)

    label("loc_CC3")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CCC")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEE")
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_D05")
    ClearScenarioFlags(0x5C, 0)
    SetScenarioFlags(0x2, 4)
    Event(0, 30)
    Jump("loc_D14")

    label("loc_D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_D14")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 31)

    label("loc_D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D6D")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0xE, -18200, -300, 18140, 0)
    SetChrPos(0x10, -18360, -310, 19590, 180)
    BeginChrThread(0x10, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D68")
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x10, 0x10)

    label("loc_D68")

    Jump("loc_F01")

    label("loc_D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_D90")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    BeginChrThread(0x13, 0, 0, 4)
    Jump("loc_F01")

    label("loc_D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D9E")
    Jump("loc_F01")

    label("loc_D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DAC")
    Jump("loc_F01")

    label("loc_DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_DDB")
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x10, -18360, -310, 19590, 180)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0x10, 0x10)
    Jump("loc_F01")

    label("loc_DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_DE9")
    Jump("loc_F01")

    label("loc_DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_DF7")
    Jump("loc_F01")

    label("loc_DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_E32")
    SetChrPos(0xE, -18820, -320, 21060, 0)
    SetChrPos(0x10, -18680, -310, 19940, 0)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0x10, 0x10)
    Jump("loc_F01")

    label("loc_E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_E6D")
    SetChrPos(0xE, -18200, -300, 18140, 135)
    SetChrPos(0x10, -18690, -320, 19040, 180)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0x10, 0x10)
    Jump("loc_F01")

    label("loc_E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_E7B")
    Jump("loc_F01")

    label("loc_E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_E89")
    Jump("loc_F01")

    label("loc_E89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_E97")
    Jump("loc_F01")

    label("loc_E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_EA5")
    Jump("loc_F01")

    label("loc_EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_EB3")
    Jump("loc_F01")

    label("loc_EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_EC6")
    ClearChrFlags(0x14, 0x80)
    Jump("loc_F01")

    label("loc_EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_F01")
    SetChrPos(0xE, -18200, -300, 18140, 0)
    SetChrPos(0x10, -18360, -310, 19590, 180)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x14, 0x80)

    label("loc_F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F18")
    SetMapFlags(0x10000000)
    Event(0, 29)

    label("loc_F18")

    Return()

    # Function_8_AAC end

    def Function_9_F19(): pass

    label("Function_9_F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_F2B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F6C")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_FCD")

    label("loc_F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_FA8")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_FCD")

    label("loc_FA8")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_FCD")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0x1E)
    OP_1B(0x8, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FEF")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1002")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_1002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1015")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_1015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1028")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_1028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_103B")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_103B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1049")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_1049")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1061")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1061")

    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1083")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109F")
    Jump("loc_10A4")

    label("loc_109F")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_10A4")

    Return()

    # Function_9_F19 end

    def Function_10_10A5(): pass

    label("Function_10_10A5")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26C9")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1103")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1103")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1123")
    OP_AF(0x39)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26C4")

    label("loc_1123")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1137")
    Jump("loc_26C4")

    label("loc_1137")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26C4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1331")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F6")

    ChrTalk(
        0x101,
        (
            "#0003F(Hmm... Tront said he walked around\x01",
            "East Street's marketplace. He might\x01",
            "have dropped something here.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_11F6")


    ChrTalk(
        0x101,
        (
            "#0000FExcuse me. Have you picked up any\x01",
            "items off the ground recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Have I picked up anything off the ground?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm... Sorry, 'fraid not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I tidy the stall daily, so I would have noticed if\x01",
            "I picked up anything weird off the ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F(I don't think we'll have much luck here.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1401")

    label("loc_1331")


    ChrTalk(
        0xFE,
        (
            "Somebody went and lost their stuff?\x01",
            "Sorry, I haven't seen anything around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why don't you try to ask the other vendors?\x01",
            "They're all good folks, so I'm sure they'd be\x01",
            "willing to give you a hand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1401")

    Jump("loc_26C4")

    label("loc_1406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1500")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148A")

    ChrTalk(
        0xFE,
        (
            "I just saw all of the bracers head out\x01",
            "of the guild together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What do you think they're up to?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_14FB")

    label("loc_148A")


    ChrTalk(
        0xFE,
        (
            "I just saw everybody leave the guild\x01",
            "and head off in different directions.\x01",
            "What do you think they're up to?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14FB")

    Jump("loc_26C4")

    label("loc_1500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_15C5")

    ChrTalk(
        0xFE,
        "Welcome, all! I just handcrafted a new strap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're looking for the perfect gift, then you\x01",
            "can't go wrong with this strap!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come, and feast your eyes upon my wares!\x02",
    )

    CloseMessageWindow()
    Jump("loc_26C4")

    label("loc_15C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_170B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1675")

    ChrTalk(
        0xFE,
        (
            "I heard there was some crazy shoot-out\x01",
            "in the Harbor District last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man... Crossbell's way scarier than\x01",
            "anybody gives it credit for.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1706")

    label("loc_1675")


    ChrTalk(
        0xFE,
        (
            "The Bracer Guild is nearby, so I figure\x01",
            "we should be safe, but still...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, Crossbell's way scarier than\x01",
            "anybody gives it credit for.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1706")

    Jump("loc_26C4")

    label("loc_170B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1899")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1840")

    ChrTalk(
        0xFE,
        (
            "You guys hear about those guys in black suits\x01",
            "trying to take over the area the other week?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were threatening us into paying them\x01",
            "protection money, or else we'd get shut down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Were they that mafia I kept hearing about?\x01",
            "I'd heard rumors, but dang, they were scary.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1894")

    label("loc_1840")


    ChrTalk(
        0xFE,
        (
            "I'd heard about the mafia before, but they're\x01",
            "actually pretty darn terrifying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1894")

    Jump("loc_26C4")

    label("loc_1899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1A91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F1")

    ChrTalk(
        0xFE,
        (
            "I got a ton of sales during the festival, so I thought\x01",
            "I may as well expand my lineup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although...I'm a bit of a clumsy oaf, so it's only\x01",
            "adding to the number of times I get injured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no point in worrying, though!\x01",
            "All I gotta do is go down to the hospital,\x01",
            "and they'll have me patched right up!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1A8C")

    label("loc_19F1")


    ChrTalk(
        0xFE,
        (
            "I'm going to head over to St. Ursula\x01",
            "later this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They'll patch me right up, so there's no point\x01",
            "in freaking out over every little cut.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8C")

    Jump("loc_26C4")

    label("loc_1A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1C20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB0")

    ChrTalk(
        0xFE,
        (
            "There's one thing about handicrafts that\x01",
            "always keeps me going, and that's seeing\x01",
            "people's reactions to my new works!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I love seeing how something I've made\x01",
            "can bring joy to others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Even if I keep injuring myself,\x01",
            "it'll always be worth it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C1B")

    label("loc_1BB0")


    ChrTalk(
        0xFE,
        (
            "I've got some real nice stuff cookin' in my noggin\x01",
            "for the Anniversary Festival, so get ready for it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1B")

    Jump("loc_26C4")

    label("loc_1C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1C8E")

    ChrTalk(
        0xFE,
        "Welcome, all! We've got new products for you today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why don't you take a little look?\x02",
    )

    CloseMessageWindow()
    Jump("loc_26C4")

    label("loc_1C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1DAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D42")

    ChrTalk(
        0xFE,
        "Welcome, all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had a bit of an oopsie when I was using\x01",
            "my tools and cut my hand badly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I should probably pay a liiiittle more attention.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1DA9")

    label("loc_1D42")


    ChrTalk(
        0xFE,
        "I feel like a bumbling oaf from all these injuries.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Here's hoping for a speedy recovery, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_1DA9")

    Jump("loc_26C4")

    label("loc_1DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1EAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E68")

    ChrTalk(
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Guess the Anniversary Festival is coming up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should probably make something in commemoration.\x01",
            "It IS the 70th anniversary, after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1EA7")

    label("loc_1E68")


    ChrTalk(
        0xFE,
        (
            "I should already be thinking about\x01",
            "how to prepare for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA7")

    Jump("loc_26C4")

    label("loc_1EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2068")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FD0")

    ChrTalk(
        0xFE,
        "So, I just had myself a teensy little accident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was trying to move this chest and ended up dropping\x01",
            "it on my feet when I was going down those stairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* It's not really a big deal, though.\x01",
            "I'm not going to get taken down by a silly little box.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2063")

    label("loc_1FD0")


    ChrTalk(
        0xFE,
        (
            "Us craftsmen are always one misstep away\x01",
            "from injuring ourselves, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't just moan and complain over\x01",
            "every little injury.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2063")

    Jump("loc_26C4")

    label("loc_2068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2141")

    ChrTalk(
        0xFE,
        (
            "I've been having some pretty steady\x01",
            "sales lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I sure am glad people are enjoying my works.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, I may have cut the heck outta my hands\x01",
            "making all this stuff, but it sure was worth it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C4")

    label("loc_2141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_22EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2282")

    ChrTalk(
        0xFE,
        "Yeowch... Hurt my dang fingers again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd ask for a break, but Aidios would probably\x01",
            "prank me by breaking a couple of my bones.\x02",
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
            "Hey, now. I swear I'm not nearly as clumsy\x01",
            "as I make myself out to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even veterans manage to get hurt\x01",
            "every once in a while, you know!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_22E5")

    label("loc_2282")


    ChrTalk(
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Injuries are bound to happen no matter\x01",
            "what I do, so I'm not going to sweat it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E5")

    Jump("loc_26C4")

    label("loc_22EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_247F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C1")

    ChrTalk(
        0xFE,
        (
            "Those hooligans in the Downtown District sure\x01",
            "love to come up here and cause a huge ruckus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just put up some rather unique items, too...\x01",
            "Argh. They're really pissing me off...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_247A")

    label("loc_23C1")


    ChrTalk(
        0xFE,
        (
            "Those hooligans in the Downtown District sure\x01",
            "love to come up here and cause a huge ruckus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I end up losing customers whenever they pull\x01",
            "that crap. It really pisses me off...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_247A")

    Jump("loc_26C4")

    label("loc_247F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_26C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_264F")

    ChrTalk(
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you interested in handicrafts made by\x01",
            "yours truly? Then look no further!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWow. They've even got stores like this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FUmm... Might I ask what this\x01",
            "revolving object is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha. Glad you asked, kid!\x01",
            "This here's called a 'pinwheel.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These babies are used as a good luck\x01",
            "charm out in the East.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to take one, if you'd like.\x01",
            "Who knows, it might even bring you\x01",
            "some good fortune!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_26C4")

    label("loc_264F")


    ChrTalk(
        0xFE,
        "I've got plenty of other items besides pinwheels!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everything's handmade, of course,\x01",
            "so take a look around!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26C4")

    Jump("loc_10B2")

    label("loc_26C9")

    TalkEnd(0xFE)
    Return()

    # Function_10_10A5 end

    def Function_11_26CD(): pass

    label("Function_11_26CD")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4069")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_272B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_272B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_274B")
    OP_AF(0x38)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4064")

    label("loc_274B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_275F")
    Jump("loc_4064")

    label("loc_275F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4064")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_281E")

    ChrTalk(
        0x101,
        (
            "#0003F(Hmm... Tront said he walked around\x01",
            "East Street's marketplace. He might\x01",
            "have dropped something here.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_281E")


    ChrTalk(
        0x101,
        (
            "#0000FExcuse me. Have you picked up any\x01",
            "items off the ground recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Welcome!\x01",
            "What's that? You lost something?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sorry, pal. I haven't picked anything up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We start working at the crack of dawn, so\x01",
            "I figure I woulda noticed a doohickey or two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's pretty important, then why don't you check\x01",
            "to see if somebody brought it to the police?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(I've got a pretty funny story for you...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F(I suppose we still have yet to build\x01",
            "up a reputation.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2A6F")

    label("loc_2A0C")


    ChrTalk(
        0xFE,
        (
            "You lost something?\x01",
            "I haven't seen anything around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sorry, I wish I could help you.\x02",
    )

    CloseMessageWindow()

    label("loc_2A6F")

    Jump("loc_4064")

    label("loc_2A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2B30")

    ChrTalk(
        0xFE,
        (
            "Hey there, folks! Keep standing there\x01",
            "and the day's going to be over before\x01",
            "you know it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come on over and buy something!\x01",
            "We're holding our last bargain of the day!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4064")

    label("loc_2B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2D20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA1")

    ChrTalk(
        0xFE,
        (
            "I have nothing but respect for the old guys\x01",
            "over at the Business Owners' Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the end of the day, they're always the ones\x01",
            "throwing out their backs for us merchants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, uh... I'm not exactly smart when it comes\x01",
            "to anything complicated!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I totally lack all the qualities needed to be\x01",
            "some kinda fancy executive!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2D1B")

    label("loc_2CA1")


    ChrTalk(
        0xFE,
        (
            "Welcome! What are you just\x01",
            "standing there for?! Buy something!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep. I should definitely stick to\x01",
            "my usual flow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D1B")

    Jump("loc_4064")

    label("loc_2D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2DE2")

    ChrTalk(
        0xFE,
        (
            "Welcome, folks! Thanks for shopping at\x01",
            "Dinz Fresh!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Business has been booming all day, so I figured,\x01",
            "hey, why not put on a little sale?! C'mon over and\x01",
            "take a quick look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4064")

    label("loc_2DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2EF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E9E")

    ChrTalk(
        0xFE,
        (
            "Man, screw Revache! Those jackasses\x01",
            "are way too violent!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rough me up all ya want, but I won't let you off\x01",
            "easy if you cause problems for my customers!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2EF4")

    label("loc_2E9E")


    ChrTalk(
        0xFE,
        (
            "I'm not going to let those jackasses over in\x01",
            "Revache get off the hook so easily!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF4")

    Jump("loc_4064")

    label("loc_2EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3105")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306E")

    ChrTalk(
        0xFE,
        (
            "Those guys from the Business Owners' Association\x01",
            "have been asking me to hang out with them lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guess I caught their attention.\x01",
            "They keep inviting me out for lunch\x01",
            "and whatnot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heh. It almost feels like they were born to do business.\x01",
            "I always end up learning something new every time they\x01",
            "tell one of their interesting stories.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3100")

    label("loc_306E")


    ChrTalk(
        0xFE,
        (
            "I've gone to lunch with some guys from the\x01",
            "Business Owners' Association a few times now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They're some of the nicest folk I've ever met.\x02",
    )

    CloseMessageWindow()

    label("loc_3100")

    Jump("loc_4064")

    label("loc_3105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_32C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_321F")

    ChrTalk(
        0xFE,
        (
            "The chairman of the Business Owners' Association\x01",
            "always compliments me for all the hard work\x01",
            "I've done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I'm glad to know I've got someone like\x01",
            "him looking out for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've actually invited me out for drinks\x01",
            "a couple of times, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_32BE")

    label("loc_321F")


    ChrTalk(
        0xFE,
        (
            "The chairman of the Business Owners' Association\x01",
            "complimented me for my hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's nothing better in life than working\x01",
            "as a street merchant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32BE")

    Jump("loc_4064")

    label("loc_32C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_34E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3461")

    ChrTalk(
        0xFE,
        (
            "It's always kinda hard to figure out how much to stock\x01",
            "up for the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't care what anyone says, I'd better not catch\x01",
            "them overstocking on veggies. Get that gross stale\x01",
            "stuff out of my sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I also need to make sure I stock enough\x01",
            "so that I don't run out too quickly and cause\x01",
            "double the trouble for my customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's a constant struggle.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_34E0")

    label("loc_3461")


    ChrTalk(
        0xFE,
        (
            "It's always kinda hard to figure out when to stock\x01",
            "up for the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* It's a constant struggle.\x02",
    )

    CloseMessageWindow()

    label("loc_34E0")

    Jump("loc_4064")

    label("loc_34E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3583")

    ChrTalk(
        0xFE,
        "Welcome, friends!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got a special little something\x01",
            "to give out to our valued regulars!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wanna take a quick peek at our wares?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4064")

    label("loc_3583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_375E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36CD")

    ChrTalk(
        0xFE,
        (
            "Anything I order from Armorica Village\x01",
            "gets delivered here by orbal truck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, back when I started up this stall,\x01",
            "we didn't have anything NEARLY\x01",
            "as convenient as that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now we can get fresh veggies in a fraction\x01",
            "of the time! The world's moving so friggin'\x01",
            "fast that I can hardly keep up!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3759")

    label("loc_36CD")


    ChrTalk(
        0xFE,
        (
            "Looks like a lotta stores are relying on\x01",
            "orbal truck delivery these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, it's pretty insane how convenient\x01",
            "life has gotten!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3759")

    Jump("loc_4064")

    label("loc_375E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3884")

    ChrTalk(
        0xFE,
        (
            "The chairman of the Business Owners' Association\x01",
            "called out to me in the middle of the street this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gosh darn it, that sure was embarrassing...\x01",
            "Didn't think he'd actually remember me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, let's do this. I'd better get some\x01",
            "hefty sales today!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3900")

    label("loc_3884")


    ChrTalk(
        0xFE,
        "Welcome to Dinz Fresh, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Need fresh produce? We got you covered,\x01",
            "whether it be breakfast, lunch, or dinz!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3900")

    Jump("loc_4064")

    label("loc_3905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3A7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A0A")

    ChrTalk(
        0xFE,
        (
            "Welcome, folks! We've got the finest\x01",
            "produce available today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not to brag or anything, but I haven't\x01",
            "taken a single day of vacation ever\x01",
            "since I set up this stall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can't leave our valuable customers\x01",
            "waiting, after all!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3A7A")

    label("loc_3A0A")


    ChrTalk(
        0xFE,
        (
            "Welcome one, welcome all!\x01",
            "While we're not open 24 hours a day, we ARE\x01",
            "open 7 days a week, 52 weeks a year!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A7A")

    Jump("loc_4064")

    label("loc_3A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3CB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BD4")

    ChrTalk(
        0xFE,
        "Greetings, fellow Crossbellans!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had this real energetic girl stop by the\x01",
            "stall this morning, and we got to talking.\x01",
            "We ended up going at it for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y'know, she had chestnut hair done up in twintails.\x01",
            "I've never seen her around these parts before.\x01",
            "You think she just moved into town recently?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3CAF")

    label("loc_3BD4")


    ChrTalk(
        0xFE,
        (
            "This energetic girl stopped by the stall this\x01",
            "morning. We got to talking, and I ended up\x01",
            "feeling pretty lively, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've never seen her around these parts before.\x01",
            "You think she just moved into town recently?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CAF")

    Jump("loc_4064")

    label("loc_3CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D79")

    ChrTalk(
        0xFE,
        "Howdy. Welcome to Dinz Fresh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can count on us to sell you freshly\x01",
            "harvested vegetables at a great price!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Don't miss your chance at some great veggies!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3DFC")

    label("loc_3D79")


    ChrTalk(
        0xFE,
        (
            "We're offering our vegetables at dirt-cheap\x01",
            "prices at all times!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't just stand there, people!\x01",
            "Buy everything you can!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DFC")

    Jump("loc_4064")

    label("loc_3E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4064")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FD5")

    ChrTalk(
        0xFE,
        "Welcome, folks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, haven't seen your faces around these parts.\x01",
            "How 'bout I throw you guys a lil' extra, for free!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FMan, this dude musta gone through a ton of trouble\x01",
            "to get all these veggies on display like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FI feel like it'd almost be rude to NOT buy something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha! You folks have a good eye on you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These bad boys were delivered straight from\x01",
            "Armorica Village! Come pick out your favorites!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4064")

    label("loc_3FD5")


    ChrTalk(
        0xFE,
        (
            "That's right, we even have produce delivered\x01",
            "straight from Armorica Village!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Buy some, or else I won't be able to pay\x01",
            "my water bill!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4064")

    Jump("loc_26DA")

    label("loc_4069")

    TalkEnd(0xFE)
    Return()

    # Function_11_26CD end

    def Function_12_406D(): pass

    label("Function_12_406D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_424D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4116")

    ChrTalk(
        0x101,
        (
            "#0003F(Hmm... Tront said he walked around\x01",
            "East Street's marketplace. He might\x01",
            "have dropped something here.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_4116")


    ChrTalk(
        0x101,
        (
            "#0000FExcuse me, do you know if the marketplace\x01",
            "has anything like a lost and found?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, did you lose something? I can't\x01",
            "say we do, sadly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not too surprising, though.\x01",
            "People lose stuff here all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Have you tried asking anyone else?\x01",
            "Somebody may have already picked it up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_42CF")

    label("loc_424D")


    ChrTalk(
        0xFE,
        (
            "You should try asking other people around here.\x01",
            "They might be able to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Someone might have picked it up by now.\x02",
    )

    CloseMessageWindow()

    label("loc_42CF")

    Jump("loc_5790")

    label("loc_42D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_44BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43E8")

    ChrTalk(
        0xFE,
        "How can Dinz act so pleased with himself?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He flat out rejected the Business Owners'\x01",
            "Association's offer and continues to happily\x01",
            "work his stall like he normally does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I swear, he has such a one-track\x01",
            "mind and isn't afraid to show it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_44BA")

    label("loc_43E8")


    ChrTalk(
        0xFE,
        (
            "How simpleminded can he be?\x01",
            "He's going to end up getting tricked\x01",
            "by some bad people if he's not careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seriously... What would he ever do without me?\x01",
            "I can't take my eyes off him for even a second.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44BA")

    Jump("loc_5790")

    label("loc_44BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_46D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_460E")

    ChrTalk(
        0xFE,
        (
            "It looks like Dinz had a serious meeting with the\x01",
            "chairman of the Business Owners' Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think Dinz has a difficult offer on his hands,\x01",
            "because his face sure shows it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come on, already! Why won't you hurry up\x01",
            "and accept the offer? Sheesh!\x01",
            "It'd be a huge step forward for your career.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_46CD")

    label("loc_460E")


    ChrTalk(
        0xFE,
        (
            "You'll get a ton of assistance from all the veterans\x01",
            "if you join the Business Owners' Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He needs to learn how to accept the offer.\x01",
            "There's plenty for him to learn there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46CD")

    Jump("loc_5790")

    label("loc_46D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4862")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47C6")

    ChrTalk(
        0xFE,
        "Hi there! Are you interested in my goods?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everybody's up in arms over some incident,\x01",
            "but we've just been minding our own business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no point in worrying about it,\x01",
            "so wanna buy some of my goods?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_485D")

    label("loc_47C6")


    ChrTalk(
        0xFE,
        (
            "Still, though... Dinz seems totally\x01",
            "unfazed by the whole thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do you think he doesn't worry about rumors,\x01",
            "or is he just totally oblivious?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_485D")

    Jump("loc_5790")

    label("loc_4862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_49AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4936")

    ChrTalk(
        0xFE,
        (
            "I can't believe Dinz got attacked yesterday...\x01",
            "He even got sent to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Argh! I'm so mad!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I'm not exactly in a position where\x01",
            "I can do something about it...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_49A6")

    label("loc_4936")


    ChrTalk(
        0xFE,
        (
            "If I had a bit more muscle on these arms,\x01",
            "they'd be getting paid a visit by the CEO of\x01",
            "knuckle sandwiches.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A6")

    Jump("loc_5790")

    label("loc_49AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4ACC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AA0")

    ChrTalk(
        0xFE,
        (
            "Dinz received an invitation to join the\x01",
            "Business Owners' Association recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess the old guys figured out\x01",
            "how hard of a worker he is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, if only that numbskull would\x01",
            "figure it out for himself...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4AC7")

    label("loc_4AA0")


    ChrTalk(
        0xFE,
        "Oh, what will I ever do with him?\x02",
    )

    CloseMessageWindow()

    label("loc_4AC7")

    Jump("loc_5790")

    label("loc_4ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4CA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C10")

    ChrTalk(
        0xFE,
        "Ugh. Dinz is such a numbskull.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think he realizes how huge an honor it is to receive\x01",
            "an invitation to the Business Owners' Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish I could do something to make him understand\x01",
            "how big a deal it is, but I'm not sure he has the\x01",
            "mental capacity to really understand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4CA3")

    label("loc_4C10")


    ChrTalk(
        0xFE,
        (
            "It's a huge honor to be able to join the\x01",
            "Business Owners' Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But unfortunately, that invite is wasted on\x01",
            "a moron like himself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CA3")

    Jump("loc_5790")

    label("loc_4CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4D60")

    ChrTalk(
        0xFE,
        "Hello there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everybody sure loves offering discounts during\x01",
            "the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're no exception, obviously, so come on over\x01",
            "and buy some produce!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5790")

    label("loc_4D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4EE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E62")

    ChrTalk(
        0xFE,
        (
            "Didn't Arc en Ciel recruit a new member recently?\x01",
            "I think her name was Rixia, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Speaking of which, I feel like I've seen her around here\x01",
            "a few times before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wouldn't be surprised if she lives around here.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4EE1")

    label("loc_4E62")


    ChrTalk(
        0xFE,
        (
            "I've seen that Rixia girl shopping at the marketplace\x01",
            "a few times before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do you think she lives around these parts?\x02",
    )

    CloseMessageWindow()

    label("loc_4EE1")

    Jump("loc_5790")

    label("loc_4EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_508F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FFE")

    ChrTalk(
        0xFE,
        (
            "Maaaan... I really wanted to get a ticket to\x01",
            "Arc en Ciel's new show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would have loved to go for a little post-show\x01",
            "shopping at Times afterwards...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Crap! I need to snap out of it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "W-Welcome to Dinz Fresh.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_508A")

    label("loc_4FFE")


    ChrTalk(
        0xFE,
        (
            "I can't believe I started pouting in the\x01",
            "middle of the street like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I gotta chill out. Can't let greed get\x01",
            "the best of me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_508A")

    Jump("loc_5790")

    label("loc_508F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5162")

    ChrTalk(
        0xFE,
        "Hi there, welcome to Dinz Fresh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our owner may be a touch too naive, but we\x01",
            "still have the customer's best interests in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's veggies you need, then it's\x01",
            "Dinz Fresh, indeed!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5790")

    label("loc_5162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_52F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_525E")

    ChrTalk(
        0xFE,
        (
            "I can't tell if Dinz is even interested in running\x01",
            "a serious business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've seen him go around handing out unsold vegetables\x01",
            "for free around the neighborhood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He can be way too nice for his own good, at times.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_52F2")

    label("loc_525E")


    ChrTalk(
        0xFE,
        (
            "Dinz is SO sincere that it ends up\x01",
            "making him naive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've known each other ever since we were kids,\x01",
            "so it's hard not to worry about him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52F2")

    Jump("loc_5790")

    label("loc_52F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_557D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54AB")

    ChrTalk(
        0xFE,
        (
            "East Street is home to an organization known as\x01",
            "the Business Owners' Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They used to negotiate for the shopkeepers here,\x01",
            "but now they're essentially representatives for\x01",
            "the entire area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Many Crossbellan traders make their fortunes\x01",
            "by participating in international trade and\x01",
            "speculation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I doubt you'd find anybody on East Street that\x01",
            "approves of those kinds of methods, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5578")

    label("loc_54AB")


    ChrTalk(
        0xFE,
        (
            "All the old guys in the Business Owners' Association\x01",
            "used to run stalls themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They formed a union in an attempt to\x01",
            "oppose unfair business practices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They've got all of our backs here.\x02",
    )

    CloseMessageWindow()

    label("loc_5578")

    Jump("loc_5790")

    label("loc_557D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5732")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5681")

    ChrTalk(
        0xFE,
        (
            "There's no stopping Dinz when he sets his mind\x01",
            "on accomplishing a goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only that, but he's naive, so he might get\x01",
            "taken advantage of one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So imagine my shock when he told me\x01",
            "he wanted to own his own business.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_572D")

    label("loc_5681")


    ChrTalk(
        0xFE,
        (
            "There's no stopping Dinz when he sets his mind\x01",
            "on accomplishing a goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess the customers like that about him,\x01",
            "so maybe I should stop worrying so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_572D")

    Jump("loc_5790")

    label("loc_5732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5790")

    ChrTalk(
        0xFE,
        "Oh, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our veggies are extra fresh today,\x01",
            "so I hope you'll buy some!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5790")

    TalkEnd(0xFE)
    Return()

    # Function_12_406D end

    def Function_13_5794(): pass

    label("Function_13_5794")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57C1")
    TurnDirection(0x0, 0xB, 0)
    OP_4B(0xB, 0xFF)
    Call(0, 34)
    Return()

    label("loc_57C1")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x2, 3)
    Call(0, 15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5964")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_595C")

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
    SetScenarioFlags(0x2, 2)
    TalkEnd(0xFE)
    Return()

    label("loc_595C")

    Call(0, 14)
    Jump("loc_75E3")

    label("loc_5964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_75E0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5977")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75DB")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "Talk")
    MenuCmd(1, 1, "Give Fish")
    MenuCmd(1, 1, "Leave")
    ClearScenarioFlags(0x2, 3)
    Call(0, 15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59C5")
    MenuCmd(3, 1, 0x1)

    label("loc_59C5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59F7")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_59F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75A6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7597")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A7E")
    MenuCmd(1, 1, "Snow Crab (for earth x10)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A74")
    Call(0, 16)

    label("loc_5A74")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5A7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5AD5")
    MenuCmd(1, 1, "Armorican Carp (for water x10)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ACB")
    Call(0, 16)

    label("loc_5ACB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5AD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B2B")
    MenuCmd(1, 1, "Tiger Rockfish (for fire x10)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B21")
    Call(0, 16)

    label("loc_5B21")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5B2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B7C")
    MenuCmd(1, 1, "Rockeater (for wind x10)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B72")
    Call(0, 16)

    label("loc_5B72")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5B7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5BC8")
    MenuCmd(1, 1, "Carp (for time x10)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BBE")
    Call(0, 16)

    label("loc_5BBE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5BC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C1B")
    MenuCmd(1, 1, "Raineater (for mirage x10)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C11")
    Call(0, 16)

    label("loc_5C11")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5C1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C6C")
    MenuCmd(1, 1, "Azelfish (for earth x20)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C62")
    Call(0, 16)

    label("loc_5C62")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5C6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5CBC")
    MenuCmd(1, 1, "Kasagin (for water x20)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CB2")
    Call(0, 16)

    label("loc_5CB2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5CBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D11")
    MenuCmd(1, 1, "Rainbow Trout (for fire x20)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D07")
    Call(0, 16)

    label("loc_5D07")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5D11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D5E")
    MenuCmd(1, 1, "Trout (for wind x20)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D54")
    Call(0, 16)

    label("loc_5D54")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5D5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5DAC")
    MenuCmd(1, 1, "Salmon (for time x20)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DA2")
    Call(0, 16)

    label("loc_5DA2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5DAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5DF9")
    MenuCmd(1, 1, "Eel (for mirage x20)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DEF")
    Call(0, 16)

    label("loc_5DEF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5DF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E4C")
    MenuCmd(1, 1, "Pearlglass (for space x20)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E42")
    Call(0, 16)

    label("loc_5E42")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5E4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5EA4")
    MenuCmd(1, 1, "Gluttonous Bass (for earth x40)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E9A")
    Call(0, 16)

    label("loc_5E9A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5EA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5EF6")
    MenuCmd(1, 1, "Viperfish (for water x40)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EEC")
    Call(0, 16)

    label("loc_5EEC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5EF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F48")
    MenuCmd(1, 1, "Pythonhead (for fire x40)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F3E")
    Call(0, 16)

    label("loc_5F3E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F97")
    MenuCmd(1, 1, "Catfish (for wind x40)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F8D")
    Call(0, 16)

    label("loc_5F8D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5FE9")
    MenuCmd(1, 1, "Queen Crab (for time x50)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FDF")
    Call(0, 16)

    label("loc_5FDF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5FE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_603F")
    MenuCmd(1, 1, "Electric Eel (for mirage x50)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6035")
    Call(0, 16)

    label("loc_6035")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_603F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6094")
    MenuCmd(1, 1, "Demon Catfish (for time x50)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_608A")
    Call(0, 16)

    label("loc_608A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6094")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_60E6")
    MenuCmd(1, 1, "Arch Crab (for space x50)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60DC")
    Call(0, 16)

    label("loc_60DC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_60E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_613A")
    MenuCmd(1, 1, "Gold Salmon (for time x100)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6130")
    Call(0, 16)

    label("loc_6130")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_613A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_618E")
    MenuCmd(1, 1, "Noble Carp (for space x100)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6184")
    Call(0, 16)

    label("loc_6184")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_618E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_61E4")
    MenuCmd(1, 1, "Serpenthead (for mirage x100)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61DA")
    Call(0, 16)

    label("loc_61DA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_61E4")

    MenuCmd(1, 1, "Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6225")
    Jump("loc_7592")

    label("loc_6225")

    FadeToBright(300, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_62C3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62B9")
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


    label("loc_62B9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_62C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6344")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_633A")
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


    label("loc_633A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6344")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_63C4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63BA")
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


    label("loc_63BA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_63C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6444")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_643A")
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


    label("loc_643A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6444")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_64C4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64BA")
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


    label("loc_64BA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_64C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6546")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_653C")
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


    label("loc_653C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6546")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_65C7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65BD")
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


    label("loc_65BD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_65C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6648")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_663E")
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


    label("loc_663E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6648")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_66C8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66BE")
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


    label("loc_66BE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_66C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6748")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_673E")
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


    label("loc_673E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6748")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_67C8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67BE")
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


    label("loc_67BE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_67C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_684A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6840")
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


    label("loc_6840")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_684A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_68CB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68C1")
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


    label("loc_68C1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_68CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_694C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6942")
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


    label("loc_6942")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_694C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_69CD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69C3")
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


    label("loc_69C3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_69CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A4D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A43")
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


    label("loc_6A43")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6A4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6ACD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AC3")
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


    label("loc_6AC3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6ACD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6B4D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B43")
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


    label("loc_6B43")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6B4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6BCF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BC5")
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


    label("loc_6BC5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6C4F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C45")
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


    label("loc_6C45")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CD0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CC6")
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


    label("loc_6CC6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6D51")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D47")
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


    label("loc_6D47")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6DD3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DC9")
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


    label("loc_6DC9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E56")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E4C")
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


    label("loc_6E4C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E56")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7592")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F81")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F81")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6F81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7588")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sleep(300)
    Sound(17, 0, 100, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_7048"),
        (1, "loc_707F"),
        (2, "loc_70B6"),
        (3, "loc_70EC"),
        (4, "loc_7122"),
        (5, "loc_7158"),
        (6, "loc_7190"),
        (7, "loc_71C7"),
        (8, "loc_71FE"),
        (9, "loc_7234"),
        (10, "loc_726A"),
        (11, "loc_72A0"),
        (12, "loc_72D8"),
        (13, "loc_730F"),
        (14, "loc_7346"),
        (15, "loc_737D"),
        (16, "loc_73B3"),
        (17, "loc_73E9"),
        (18, "loc_741F"),
        (19, "loc_7457"),
        (20, "loc_748D"),
        (21, "loc_74C4"),
        (22, "loc_74FB"),
        (23, "loc_7533"),
        (SWITCH_DEFAULT, "loc_756C"),
    )


    label("loc_7048")


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
    Jump("loc_756C")

    label("loc_707F")


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
    Jump("loc_756C")

    label("loc_70B6")


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
    Jump("loc_756C")

    label("loc_70EC")


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
    Jump("loc_756C")

    label("loc_7122")


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
    Jump("loc_756C")

    label("loc_7158")


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
    Jump("loc_756C")

    label("loc_7190")


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
    Jump("loc_756C")

    label("loc_71C7")


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
    Jump("loc_756C")

    label("loc_71FE")


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
    Jump("loc_756C")

    label("loc_7234")


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
    Jump("loc_756C")

    label("loc_726A")


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
    Jump("loc_756C")

    label("loc_72A0")


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
    Jump("loc_756C")

    label("loc_72D8")


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
    Jump("loc_756C")

    label("loc_730F")


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
    Jump("loc_756C")

    label("loc_7346")


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
    Jump("loc_756C")

    label("loc_737D")


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
    Jump("loc_756C")

    label("loc_73B3")


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
    Jump("loc_756C")

    label("loc_73E9")


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
    Jump("loc_756C")

    label("loc_741F")


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
    Jump("loc_756C")

    label("loc_7457")


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
    Jump("loc_756C")

    label("loc_748D")


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
    Jump("loc_756C")

    label("loc_74C4")


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
    Jump("loc_756C")

    label("loc_74FB")


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
    Jump("loc_756C")

    label("loc_7533")


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
    Jump("loc_756C")

    label("loc_756C")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7592")

    label("loc_7588")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7592")

    Jump("loc_5A10")

    label("loc_7597")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_75D6")

    label("loc_75A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75BA")
    Jump("loc_75D6")

    label("loc_75BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75D6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_75D6")

    Jump("loc_5977")

    label("loc_75DB")

    Jump("loc_75E3")

    label("loc_75E0")

    Call(0, 14)

    label("loc_75E3")

    TalkEnd(0xB)
    Return()

    # Function_13_5794 end

    def Function_14_75E7(): pass

    label("Function_14_75E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_76EE")

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
    Jump("loc_8D83")

    label("loc_76EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_77EC")

    ChrTalk(
        0xB,
        (
            "I can't say I ever expected the police\x01",
            "to go on a scavenger hunt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, whatever. Just make sure that thing\x01",
            "makes it back to its owner safely, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYeah, you can count on us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FThank you for your cooperation.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D83")

    label("loc_77EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_793A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78E0")

    ChrTalk(
        0xB,
        (
            "Some journalists from the Crossbell Times have been\x01",
            "frantically running around all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "The bracers seem like they're in a tizzy, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What the heck is everybody freaking out about\x01",
            "that's so important?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7935")

    label("loc_78E0")


    ChrTalk(
        0xB,
        (
            "It's like the whole city feels restless today.\x01",
            "The heck's going on around here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7935")

    Jump("loc_8D83")

    label("loc_793A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7A94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A45")

    ChrTalk(
        0xB,
        (
            "Some of those delinquents from downtown came up\x01",
            "to me this morning looking all worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Wonder if they got into a fight or something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "They asked me if I knew where one of their members\x01",
            "was, but I can't say I was much help...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7A8F")

    label("loc_7A45")


    ChrTalk(
        0xB,
        (
            "You think those delinquents from downtown got\x01",
            "into some kinda brawl?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A8F")

    Jump("loc_8D83")

    label("loc_7A94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7C3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BBA")

    ChrTalk(
        0xB,
        "I DID hear that something went down pretty recently...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Not my problem, though. Not a chance in Gehenna\x01",
            "I'd close up shop over something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm no chicken. Crossbellan merchants back in the day\x01",
            "used to conduct trades even in the middle of wars.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7C36")

    label("loc_7BBA")


    ChrTalk(
        0xB,
        (
            "I'm just a simple little merchant, so nothing short of\x01",
            "the literal end of the world is going to make me close\x01",
            "up shop!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C36")

    Jump("loc_8D83")

    label("loc_7C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7E07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D65")

    ChrTalk(
        0xB,
        (
            "I swear, if those ruffians from Revache show\x01",
            "their faces around here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Y'know, some Calvardian mafia has been creeping\x01",
            "their way into Crossbell...and you know what?\x01",
            "I kinda like them better than Revache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Meh. Not like I have a choice in the matter, do I?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7E02")

    label("loc_7D65")


    ChrTalk(
        0xB,
        (
            "Oh, yeah... What's with all the dangerous stuff\x01",
            "happening around here lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You guys better watch each other's backs\x01",
            "out in the street, capisce?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E02")

    Jump("loc_8D83")

    label("loc_7E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7ED0")

    ChrTalk(
        0xB,
        "Mornin', friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The Anniversary Festival may be over,\x01",
            "but some travelers have stuck around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A whole week has already passed, yet my\x01",
            "sales are still lookin' pretty beefy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D83")

    label("loc_7ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8084")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FED")

    ChrTalk(
        0xFE,
        (
            "Looks like they finally managed to restore\x01",
            "the highway leading to Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They sure took their sweet time, considering\x01",
            "it was just a tiny accident involving a truck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Meh. As long as I get my fish in time,\x01",
            "I don't have any reason to complain.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_807F")

    label("loc_7FED")


    ChrTalk(
        0xFE,
        (
            "What's with all of the weird accidents that\x01",
            "keep happening?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Meh. As long as I get my fish in time,\x01",
            "I don't have any reason to complain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_807F")

    Jump("loc_8D83")

    label("loc_8084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8230")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8195")

    ChrTalk(
        0xFE,
        "Mornin', folks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the time being, I'm going to buy fish from\x01",
            "the Fisherman's Guild. They've got a hefty\x01",
            "supply, and they're plenty fresh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The delayed shipments have been a pain in my butt,\x01",
            "but I'll have to make do however I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_822B")

    label("loc_8195")


    ChrTalk(
        0xFE,
        (
            "The usual delivery truck got into an accident,\x01",
            "so shipments are currently postponed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I need to figure out a plan for how to deal with this.\x02",
    )

    CloseMessageWindow()

    label("loc_822B")

    Jump("loc_8D83")

    label("loc_8230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8301")

    ChrTalk(
        0xFE,
        "Sorry, guys. Runnin' a bit low on fish right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The highway into Calvard's still blocked\x01",
            "cause of that truck accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Any deliveries from Calvard are being put\x01",
            "on hold for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D83")

    label("loc_8301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_84AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8401")

    ChrTalk(
        0xFE,
        (
            "Actually... There's been a bunch of accidents\x01",
            "on the road connecting to Calvard recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It always ends up blocking the road, and\x01",
            "then my fish deliveries get delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* If it's not one thing, it's another...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_84A2")

    label("loc_8401")


    ChrTalk(
        0xFE,
        (
            "There's been a bunch of accidents on the road\x01",
            "connecting to Calvard recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A couple accidents actually happened last week.\x01",
            "The heck's up with that?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84A2")

    SetScenarioFlags(0x95, 1)
    Jump("loc_8D83")

    label("loc_84AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_86A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85F1")

    ChrTalk(
        0xB,
        (
            "The hubby's been pretty busy trying to refill our inventory,\x01",
            "so it's been kinda hard to see him these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, uh, never mind me. I should be focusing\x01",
            "on the store instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You, sir! You look like the type to buy our finest fish!\x01",
            "Pick whichever you like. Their quality is guaranteed!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_86A0")

    label("loc_85F1")


    ChrTalk(
        0xB,
        (
            "The hubby's been pretty busy trying to refill our inventory,\x01",
            "so it's been kinda hard to see him these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "It gets a little lonely around here without him, y'know?\x02",
    )

    CloseMessageWindow()

    label("loc_86A0")

    Jump("loc_8D83")

    label("loc_86A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_87E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8779")

    ChrTalk(
        0xB,
        (
            "You guys know about the Fisherman's Guild\x01",
            "just up the street, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Those guys always just stand there and\x01",
            "stare at my fish whenever they pass by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "What's their problem?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_87DD")

    label("loc_8779")


    ChrTalk(
        0xB,
        (
            "The guys from the Fisherman's Guild\x01",
            "always come by and stare at my fish.\x01",
            "What's their problem?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87DD")

    Jump("loc_8D83")

    label("loc_87E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8ADF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A26")

    ChrTalk(
        0xB,
        (
            "Them red tracksuit wearing delinquents haven't\x01",
            "shown their faces around here lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm glad they're not here picking fights in front\x01",
            "of my store anymore, but now it feels a bit too\x01",
            "quiet around here. I'm almost MORE worried now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder if they ate something bad. Food poisoning\x01",
            "would put 'em down for the count.\x02",
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
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#0300F(How 'bout we give that a try if they keep\x01",
            "causin' problems?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(A little excessive, don't you think?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8ADA")

    label("loc_8A26")


    ChrTalk(
        0xB,
        (
            "Them red tracksuit wearing delinquents haven't\x01",
            "shown their faces around here lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder if they ate something bad. Food poisoning\x01",
            "would put 'em down for the count.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8ADA")

    Jump("loc_8D83")

    label("loc_8ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8BB1")

    ChrTalk(
        0xB,
        (
            "A lot more of those delivery trucks have been\x01",
            "able to come through here lately. Much easier\x01",
            "to stock up on inventory now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "C'mon now, don't be shy! This one was\x01",
            "caught just this morning!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D83")

    label("loc_8BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_8D83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D2B")

    ChrTalk(
        0xB,
        (
            "Fish! Come get your fish! Lest ye be\x01",
            "sleeping with the fishies!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FThat is a large quantity of fish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FYeah, though I can't say I'm\x01",
            "familiar with these species...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Heh. These are saltwater fish preserved and\x01",
            "transported out from Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Whether you steam 'em or you fry 'em,\x01",
            "they'll still be delicious. Wanna buy some?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8D83")

    label("loc_8D2B")


    ChrTalk(
        0xB,
        "Fish! Come get your fish!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I just got a new delivery in,\x01",
            "so they're all fresh!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D83")

    Return()

    # Function_14_75E7 end

    def Function_15_8D84(): pass

    label("Function_15_8D84")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_8D92")
    SetScenarioFlags(0x2, 3)

    label("loc_8D92")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_8DA0")
    SetScenarioFlags(0x2, 3)

    label("loc_8DA0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_8DAE")
    SetScenarioFlags(0x2, 3)

    label("loc_8DAE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_8DBC")
    SetScenarioFlags(0x2, 3)

    label("loc_8DBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_8DCA")
    SetScenarioFlags(0x2, 3)

    label("loc_8DCA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_8DD8")
    SetScenarioFlags(0x2, 3)

    label("loc_8DD8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_8DE6")
    SetScenarioFlags(0x2, 3)

    label("loc_8DE6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_8DF4")
    SetScenarioFlags(0x2, 3)

    label("loc_8DF4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_8E02")
    SetScenarioFlags(0x2, 3)

    label("loc_8E02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_8E10")
    SetScenarioFlags(0x2, 3)

    label("loc_8E10")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_8E1E")
    SetScenarioFlags(0x2, 3)

    label("loc_8E1E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_8E2C")
    SetScenarioFlags(0x2, 3)

    label("loc_8E2C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_8E3A")
    SetScenarioFlags(0x2, 3)

    label("loc_8E3A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_8E48")
    SetScenarioFlags(0x2, 3)

    label("loc_8E48")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_8E56")
    SetScenarioFlags(0x2, 3)

    label("loc_8E56")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_8E64")
    SetScenarioFlags(0x2, 3)

    label("loc_8E64")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_8E72")
    SetScenarioFlags(0x2, 3)

    label("loc_8E72")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_8E80")
    SetScenarioFlags(0x2, 3)

    label("loc_8E80")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_8E8E")
    SetScenarioFlags(0x2, 3)

    label("loc_8E8E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_8E9C")
    SetScenarioFlags(0x2, 3)

    label("loc_8E9C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_8EAA")
    SetScenarioFlags(0x2, 3)

    label("loc_8EAA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_8EB8")
    SetScenarioFlags(0x2, 3)

    label("loc_8EB8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_8EC6")
    SetScenarioFlags(0x2, 3)

    label("loc_8EC6")

    Return()

    # Function_15_8D84 end

    def Function_16_8EC7(): pass

    label("Function_16_8EC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EDA")
    MenuCmd(3, 1, 0x0)

    label("loc_8EDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EED")
    MenuCmd(3, 1, 0x1)

    label("loc_8EED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F00")
    MenuCmd(3, 1, 0x2)

    label("loc_8F00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F13")
    MenuCmd(3, 1, 0x3)

    label("loc_8F13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F26")
    MenuCmd(3, 1, 0x4)

    label("loc_8F26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F39")
    MenuCmd(3, 1, 0x5)

    label("loc_8F39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F4C")
    MenuCmd(3, 1, 0x6)

    label("loc_8F4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F5F")
    MenuCmd(3, 1, 0x7)

    label("loc_8F5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F72")
    MenuCmd(3, 1, 0x8)

    label("loc_8F72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F85")
    MenuCmd(3, 1, 0x9)

    label("loc_8F85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F98")
    MenuCmd(3, 1, 0xA)

    label("loc_8F98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FAB")
    MenuCmd(3, 1, 0xB)

    label("loc_8FAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FBE")
    MenuCmd(3, 1, 0xC)

    label("loc_8FBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FD1")
    MenuCmd(3, 1, 0xD)

    label("loc_8FD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FE4")
    MenuCmd(3, 1, 0xE)

    label("loc_8FE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FF7")
    MenuCmd(3, 1, 0xF)

    label("loc_8FF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_900A")
    MenuCmd(3, 1, 0x10)

    label("loc_900A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_901D")
    MenuCmd(3, 1, 0x11)

    label("loc_901D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9030")
    MenuCmd(3, 1, 0x12)

    label("loc_9030")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9043")
    MenuCmd(3, 1, 0x13)

    label("loc_9043")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9056")
    MenuCmd(3, 1, 0x14)

    label("loc_9056")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9069")
    MenuCmd(3, 1, 0x15)

    label("loc_9069")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_907C")
    MenuCmd(3, 1, 0x16)

    label("loc_907C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_908F")
    MenuCmd(3, 1, 0x17)

    label("loc_908F")

    Return()

    # Function_16_8EC7 end

    def Function_17_9090(): pass

    label("Function_17_9090")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_91A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_911A")

    ChrTalk(
        0xFE,
        "Oh, wow. It's gotten pretty late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should probably finish up my shopping\x01",
            "so I can hurry on home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_919B")

    label("loc_911A")


    ChrTalk(
        0xFE,
        (
            "Luckily for me, there's a ton of discounts\x01",
            "happening at this hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should probably finish up\x01",
            "so I can hurry on home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_919B")

    Jump("loc_A379")

    label("loc_91A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_925E")

    ChrTalk(
        0xFE,
        (
            "The buses are undergoing an inspection today,\x01",
            "so service to Armorica Village will be suspended\x01",
            "at noon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should get going soon if you have any\x01",
            "business out there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A379")

    label("loc_925E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_93F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_932F")

    ChrTalk(
        0xFE,
        (
            "I heard the chairman of the Business Owners'\x01",
            "Association was going to meet with the diet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good luck to him! He's our representative,\x01",
            "so I hope he scores us a large budget!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_93EE")

    label("loc_932F")


    ChrTalk(
        0xFE,
        (
            "The chairman of the Business Owners' Association\x01",
            "essentially acts as East Street's representative.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's been attempting to gather up help from\x01",
            "all of the merchants around the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93EE")

    Jump("loc_A379")

    label("loc_93F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_959E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9510")

    ChrTalk(
        0xFE,
        (
            "Market conditions should be improving in about\x01",
            "a year's time, according to the Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the markets were to improve, then my husband's\x01",
            "salary would also improve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'd use that opportunity to\x01",
            "purchase some expensive clothing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9599")

    label("loc_9510")


    ChrTalk(
        0xFE,
        (
            "I'm excited over the thought of his\x01",
            "wallet fattening up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'd use that opportunity to\x01",
            "purchase some expensive clothing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9599")

    Jump("loc_A379")

    label("loc_959E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9716")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9684")

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival has concluded,\x01",
            "and with it, the city has calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that I think about it, the mafia have\x01",
            "calmed down, too, haven't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, from what I can tell anyway.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9711")

    label("loc_9684")


    ChrTalk(
        0xFE,
        (
            "I haven't heard any recent rumors\x01",
            "about Revache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I can finally relax for a bit, now\x01",
            "that they aren't causing any problems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9711")

    Jump("loc_A379")

    label("loc_9716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_97B7")

    ChrTalk(
        0xFE,
        (
            "The Business Owners' Association always holds\x01",
            "an event during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm interested to see what they'll do this year.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A379")

    label("loc_97B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_985D")

    ChrTalk(
        0xFE,
        (
            "At long last, the Anniversary Festival arrives\x01",
            "in one more month!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to work out my shopping budget\x01",
            "to make sure I can actually enjoy it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A379")

    label("loc_985D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9A21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9987")

    ChrTalk(
        0xFE,
        (
            "I seem to remember there being\x01",
            "a few shootouts between mafia\x01",
            "members around 7 or 8 years ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think there were some rumors about\x01",
            "an internal conflict in Revache at\x01",
            "the time, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph. Of course, the police idly sat by\x01",
            "and left us scared and helpless.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9A1C")

    label("loc_9987")


    ChrTalk(
        0xFE,
        (
            "I heard there's been plenty of gunshots\x01",
            "near the warehouses recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose the mafia is at it again.\x01",
            "A frightening thought, for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A1C")

    Jump("loc_A379")

    label("loc_9A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9BE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B32")

    ChrTalk(
        0xFE,
        (
            "Did you hear the news already?\x01",
            "There were gunshots near the\x01",
            "warehouse area last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The bracers were able to quickly dispatch,\x01",
            "but the culprits managed to escape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief. No matter the time or place,\x01",
            "peace is ever fleeting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9BDB")

    label("loc_9B32")


    ChrTalk(
        0xFE,
        (
            "There were gunshots near the\x01",
            "warehouse area last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if it's the usual suspects...\x01",
            "I swear... No matter the time or place,\x01",
            "peace is ever fleeting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BDB")

    SetScenarioFlags(0x95, 1)
    Jump("loc_A379")

    label("loc_9BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D0D")

    ChrTalk(
        0xFE,
        (
            "I've been reading about the CGF in\x01",
            "the Crossbell Times lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Their deputy commander is actually a woman.\x01",
            "I could tell by the fact that her name is Sonya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I sometimes see the CGF's vehicles around here.\x01",
            "It makes me feel some sort of camaraderie with her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9D70")

    label("loc_9D0D")


    ChrTalk(
        0xFE,
        (
            "The CGF's deputy commander is a woman, right?\x01",
            "That makes me feel a bit more connected to her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D70")

    Jump("loc_A379")

    label("loc_9D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9F52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EC2")

    ChrTalk(
        0xFE,
        (
            "Any resident of East Street can find\x01",
            "all of life's necessities here with ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you go down the street a bit, you'll find\x01",
            "all kinds of vendors. If you're looking for\x01",
            "special items, you can put in a request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, this is probably the most\x01",
            "convenient street to live on in the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9F4D")

    label("loc_9EC2")


    ChrTalk(
        0xFE,
        (
            "Any resident of East Street can find all of\x01",
            "life's necessities here. It's probably the most\x01",
            "convenient street to live on in the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F4D")

    Jump("loc_A379")

    label("loc_9F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A115")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A062")

    ChrTalk(
        0xFE,
        "Oh... Are you all planning to visit Armorica Village?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In that case, you should exit the city via the\x01",
            "eastern gate right over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you board the bus there, it'll take you all the\x01",
            "way there, so it's a fairly easy trip to make.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A110")

    label("loc_A062")


    ChrTalk(
        0xFE,
        (
            "You'll be able to find a bus stop if you take\x01",
            "the eastern exit out of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just wait for the bus to come, and you'll\x01",
            "be in Armorica Village in no time at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A110")

    Jump("loc_A379")

    label("loc_A115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A1CC")

    ChrTalk(
        0xFE,
        (
            "Those gangs from the Downtown District\x01",
            "are stirring up trouble once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they drag their fights up here again,\x01",
            "will the police even do anything about it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A379")

    label("loc_A1CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_A379")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2E4")

    ChrTalk(
        0xFE,
        "Oh! Are you tourists?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should watch yourselves around here.\x01",
            "We're pretty close to the Downtown District,\x01",
            "so it can get a little dangerous at times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're ever in trouble and need help, just\x01",
            "know you can always rely on the bracers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A379")

    label("loc_A2E4")


    ChrTalk(
        0xFE,
        (
            "It can get a little dangerous around here\x01",
            "at times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're ever in trouble and need help, just\x01",
            "know you can always rely on the bracers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A379")

    TalkEnd(0xFE)
    Return()

    # Function_17_9090 end

    def Function_18_A37D(): pass

    label("Function_18_A37D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A58F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4B8")

    ChrTalk(
        0xFE,
        (
            "Revache's don has always been\x01",
            "cunning. He can't keep gettin'\x01",
            "away with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they were to hold a proper trial for him,\x01",
            "his sentence would be 200 back-breaking\x01",
            "years of grueling labor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I cannot believe he hasn't been arrested yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Just what has this world come to?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A58A")

    label("loc_A4B8")


    ChrTalk(
        0xFE,
        (
            "If they were to arrest Revache's don, I'm sure\x01",
            "his sentence would be 200 back-breaking years\x01",
            "of grueling labor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I cannot believe the police haven't arrested him yet.\x01",
            "Just what has this world come to?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A58A")

    Jump("loc_BCB8")

    label("loc_A58F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A65B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A61B")

    ChrTalk(
        0xFE,
        (
            "Apparently, all international flights were\x01",
            "suspended this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What's the issue? Another incident?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A656")

    label("loc_A61B")


    ChrTalk(
        0xFE,
        (
            "There's been plenty of inexplicable\x01",
            "incidents lately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A656")

    Jump("loc_BCB8")

    label("loc_A65B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A7C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A780")

    ChrTalk(
        0xFE,
        (
            "Why, just last night, a black orbal car\x01",
            "crashed right into the park in the\x01",
            "Harbor District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only that, but people supposedly heard\x01",
            "the sound of numerous gunshots, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. Who else could it have been other\x01",
            "than Revache? It's SO obviously them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A7BB")

    label("loc_A780")


    ChrTalk(
        0xFE,
        (
            "Damn Revache. It's one thing after another\x01",
            "with them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7BB")

    Jump("loc_BCB8")

    label("loc_A7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A9F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A93D")

    ChrTalk(
        0xFE,
        "Okay, seriously. What is it with Revache?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They drove into town with an\x01",
            "orbal transport truck yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guess what happened next? They took\x01",
            "over the marketplace and decided we\x01",
            "'NEED' to pay them protection money.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    Sound(25, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Luckily, the bracers managed to drive them away.\x01",
            "But seriously, what a bunch of sick freaks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A9F2")

    label("loc_A93D")


    ChrTalk(
        0xFE,
        (
            "How barbaric does Revache have to be to think\x01",
            "they could just prance here and step all over\x01",
            "everything we've cultivated for generations?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Seriously, what a bunch of fools.\x02",
    )

    CloseMessageWindow()

    label("loc_A9F2")

    Jump("loc_BCB8")

    label("loc_A9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_ABCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB2E")

    ChrTalk(
        0xFE,
        (
            "Seems like a lot of people decided to permanently\x01",
            "stay here after the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are even a few of them who are interested\x01",
            "in starting their own businesses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sounds like we're about to have a new wave of\x01",
            "merchants on East Street. Pretty exciting stuff.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_ABC5")

    label("loc_AB2E")


    ChrTalk(
        0xFE,
        (
            "East Street is the gathering place\x01",
            "for merchants alike.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho. I'm a veteran in this business, so I should\x01",
            "give them the warmest of welcomes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABC5")

    Jump("loc_BCB8")

    label("loc_ABCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_ADE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD0C")

    ChrTalk(
        0xFE,
        (
            "I've been hearing the daughter of the\x01",
            "IBC CEO is an exceptional lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's still young, yet she manages to hold a position\x01",
            "on the IBC's board of directors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho. She's the spitting image of her father\x01",
            "back when he was her age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She may actually be more talented than he was!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_ADDB")

    label("loc_AD0C")


    ChrTalk(
        0xFE,
        (
            "The Crois family must have been blessed with fantastic\x01",
            "genes, considering how talented the both of them are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They may already be big shots, but I'm looking forward\x01",
            "to what more they have in store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADDB")

    Jump("loc_BCB8")

    label("loc_ADE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_B029")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF56")

    ChrTalk(
        0xFE,
        (
            "The IBC's very own CEO Crois always\x01",
            "shows expertise in the many jobs he has\x01",
            "undertaken over the years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's always had great sense when it comes\x01",
            "to business, but he's really become a big shot\x01",
            "in the business world now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And despite all of his successes, no one can\x01",
            "really come to hate him. It's probably because\x01",
            "he's a virtuous man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B024")

    label("loc_AF56")


    ChrTalk(
        0xFE,
        (
            "Mr. Crois, the CEO of the IBC, has always shown\x01",
            "aptitude in any task he undertakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And despite that, he still remains virtuous.\x01",
            "As a result, all of us merchants have come\x01",
            "to respect him greatly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B024")

    Jump("loc_BCB8")

    label("loc_B029")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_B206")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B186")

    ChrTalk(
        0xFE,
        (
            "You know, I've been hearing about more and more\x01",
            "cases of assault these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yet somehow, the police can't seem to make\x01",
            "any headway at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wow, what a surprise. Our only hope is the\x01",
            "Bracer Guild whenever anything goes wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(Ouch. Definitely stings to hear someone\x01",
            "say it straight to my face.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B201")

    label("loc_B186")


    ChrTalk(
        0xFE,
        "The police always conduct shoddy investigations.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our only hope is the Bracer Guild whenever\x01",
            "anything goes wrong.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B201")

    Jump("loc_BCB8")

    label("loc_B206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B3BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B334")

    ChrTalk(
        0xFE,
        (
            "The Business Owners' Association always\x01",
            "holds a special event during the annual\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're thinking of holding an event that any\x01",
            "citizen can participate in this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho. I definitely look forward to seeing\x01",
            "what they have in store for us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B3B6")

    label("loc_B334")


    ChrTalk(
        0xFE,
        (
            "The Business Owners' Association always\x01",
            "holds a special event during the annual\x01",
            "Anniversary Festival, so I'm excited for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3B6")

    Jump("loc_BCB8")

    label("loc_B3BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_B5A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4C3")

    ChrTalk(
        0xFE,
        (
            "I've been running my own shop on\x01",
            "East Street for a long time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am truly indebted to the Business Owners'\x01",
            "Association's chairman at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho. Long lasting bonds like this are\x01",
            "some of life's greatest treasures.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B59C")

    label("loc_B4C3")


    ChrTalk(
        0xFE,
        (
            "Even to this day, the chairman of the\x01",
            "Business Owners' Association comes\x01",
            "to check up on the marketplace at times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am willing to bet he's interested in all the\x01",
            "youngsters that have started their own shops.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B59C")

    Jump("loc_BCB8")

    label("loc_B5A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_B7B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B703")

    ChrTalk(
        0xFE,
        (
            "Those fancy orbal vehicles have become more\x01",
            "popular in the last few years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only that, but they're beginning to use them\x01",
            "to deliver goods from Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're definitely more convenient for small\x01",
            "deliveries than trains are, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You kids better watch both sides of the street\x01",
            "for cars, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B7AC")

    label("loc_B703")


    ChrTalk(
        0xFE,
        (
            "More and more merchants are beginning to\x01",
            "rely on delivery trucks these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Back in my day, we had to walk through\x01",
            "half an arge of snow both ways to restock.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7AC")

    Jump("loc_BCB8")

    label("loc_B7B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B9B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B917")

    ChrTalk(
        0xFE,
        "Crossbell has long been known as a trade city.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's in no small part thanks to the eastern and\x01",
            "western highways being such vital trade routes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those highways have carried international produce,\x01",
            "textiles, and even valuable information into the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've truly helped shape Crossbell\x01",
            "into what it is today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B9B1")

    label("loc_B917")


    ChrTalk(
        0xFE,
        (
            "Crossbell's been growing as a trade city\x01",
            "ever since the Middle Ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People these days like to call Crossbell\x01",
            "the 'Crossroads of Civilization.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9B1")

    Jump("loc_BCB8")

    label("loc_B9B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_BB15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA82")

    ChrTalk(
        0xFE,
        (
            "That journalist lady with the Crossbell Times\x01",
            "came through these parts a minute ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She's a real hardworking lass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I see her around here fairly often, actually.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_BB10")

    label("loc_BA82")


    ChrTalk(
        0xFE,
        (
            "I gather she came here to investigate\x01",
            "for another article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've lately noticed her trying to\x01",
            "flag down some bracers for\x01",
            "interviews.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB10")

    Jump("loc_BCB8")

    label("loc_BB15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_BCB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC22")

    ChrTalk(
        0xFE,
        (
            "Oh? I don't recognize you kids. Is this your\x01",
            "first time coming to East Street?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lots of merchants and immigrants live\x01",
            "around here, if you were curious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Foreigners have been welcomed\x01",
            "with open arms for as long as\x01",
            "I can remember.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_BCB8")

    label("loc_BC22")


    ChrTalk(
        0xFE,
        (
            "There's usually some kind of ruckus\x01",
            "happening, but we're all kind folk here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You might be out of your comfort zones,\x01",
            "but you can rest easy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCB8")

    TalkEnd(0xFE)
    Return()

    # Function_18_A37D end

    def Function_19_BCBC(): pass

    label("Function_19_BCBC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_BE65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDE9")
    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xE,
        (
            "Hey, Meiling... What do you think\x01",
            "I should do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Just be yoursewf! Now stop wowwying\x01",
            "and come pway with me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Hahaha... Yeah, I guess you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "C'mon, grab my hand. Let's\x01",
            "head back home now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    ChrTalk(
        0x10,
        "Okaaay!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0xEE, 0)
    Jump("loc_BE60")

    label("loc_BDE9")


    ChrTalk(
        0xFE,
        "Man, I should probably find myself a job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Starting to get pretty bored sitting around\x01",
            "doing nothing all day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE60")

    Jump("loc_CDC6")

    label("loc_BE65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BF82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF33")

    ChrTalk(
        0xFE,
        (
            "Arios just left the guild a couple\x01",
            "of minutes ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The other bracers look like they've been\x01",
            "super busy with work, too. Man, those guys\x01",
            "don't have easy lives, do they?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_BF7D")

    label("loc_BF33")


    ChrTalk(
        0xFE,
        (
            "*sigh* Maaan... Should I really be lazying\x01",
            "around like this all day?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF7D")

    Jump("loc_CDC6")

    label("loc_BF82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C0F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C052")

    ChrTalk(
        0xFE,
        (
            "My grandpa came up to me this morning\x01",
            "and told me to keep a close eye on\x01",
            "Meiling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, there WAS another accident earlier,\x01",
            "so I should probably be a little more careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C0EB")

    label("loc_C052")


    ChrTalk(
        0xFE,
        (
            "Looks like Grandpa got called over\x01",
            "to City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sounds like they wanted him to give some kinda\x01",
            "statement. Guess things are hectic there, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C0EB")

    Jump("loc_CDC6")

    label("loc_C0F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C21C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C18B")

    ChrTalk(
        0xFE,
        (
            "Y'know, I actually had a part-time job\x01",
            "during the Anniversary Festival.\x02",
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
        "Maybe I should have stuck with it...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C217")

    label("loc_C18B")


    ChrTalk(
        0xFE,
        (
            "I'm not busy anyway, so it might be\x01",
            "a waste to not have a job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but feel like I'd just\x01",
            "get swept into the flow again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C217")

    Jump("loc_CDC6")

    label("loc_C21C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C3AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C371")

    ChrTalk(
        0xFE,
        (
            "Man, what a pain in my ass. They made me help\x01",
            "clean up after the Anniversary Festival ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On top of that, some members of the BOA\x01",
            "were praising me and saying how 'gifted'\x01",
            "I should be as the chairman's grandson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The worst part was that I had to fork over\x01",
            "all of my earnings from my part-time job.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C3A7")

    label("loc_C371")


    ChrTalk(
        0xFE,
        (
            "*sigh* I don't even care about\x01",
            "being a merchant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3A7")

    Jump("loc_CDC6")

    label("loc_C3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_C51C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C49A")

    ChrTalk(
        0xFE,
        (
            "C-Crap... I just saw Dad coming\x01",
            "down the street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did he come to meet Grandpa,\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is bad... Really bad. If he finds me,\x01",
            "I'm friggin' toast. I can't handle another\x01",
            "long-ass lecture.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C517")

    label("loc_C49A")


    ChrTalk(
        0xFE,
        (
            "Dad's always nagging me to\x01",
            "get a job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If he finds me, I'm friggin' toast. I can't\x01",
            "handle another long-ass lecture.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C517")

    Jump("loc_CDC6")

    label("loc_C51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C68A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C61E")

    ChrTalk(
        0xFE,
        (
            "'Operation: Teach Meiling Manners'\x01",
            "ended in complete failure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All I wanted was for her to not be\x01",
            "so dang spoiled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wasn't expecting her to turn on\x01",
            "the waterworks, though... I kinda\x01",
            "screwed up, didn't I?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x87, 0x0)
    SetChrFlags(0xE, 0x10)
    SetScenarioFlags(0x1, 1)
    Jump("loc_C685")

    label("loc_C61E")


    ChrTalk(
        0xFE,
        "Hey, c'mon... It's my fault, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll buy ya whatever you want today,\x01",
            "so cheer up? Please?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C685")

    Jump("loc_CDC6")

    label("loc_C68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_C850")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C775")

    ChrTalk(
        0xFE,
        (
            "I'm thinking I should teach\x01",
            "Meiling some manners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mom and I have been coddling her,\x01",
            "so she's become really spoiled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She starts Sunday School next year,\x01",
            "so I need to straighten her out\x01",
            "by then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C84B")

    label("loc_C775")


    ChrTalk(
        0xFE,
        (
            "Well, not like I'm one to talk. I'm just a\x01",
            "jobless bum, haha. Still, if things continue\x01",
            "this way, her future's going to suck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's my job as her older brother to give her\x01",
            "the proper discipline she needs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C84B")

    Jump("loc_CDC6")

    label("loc_C850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_C986")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C915")

    ChrTalk(
        0xFE,
        "Man, Meiling's a little TOO spoiled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She starts Sunday School next year.\x01",
            "I need to make sure to straighten her out,\x01",
            "or she's going to pay for it down the line.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C981")

    label("loc_C915")


    ChrTalk(
        0xFE,
        "Man, Meiling's a little TOO spoiled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She needs to straighten up, or\x01",
            "her future could be in peril.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C981")

    Jump("loc_CDC6")

    label("loc_C986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_CAE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA6A")

    ChrTalk(
        0xFE,
        (
            "Dude, my parents keep nagging at me\x01",
            "to get a job. It's so annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish they'd piss off and give me\x01",
            "some freedom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't need them to nag at me.\x01",
            "I'll find a job when I want to work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_CAE3")

    label("loc_CA6A")


    ChrTalk(
        0xFE,
        (
            "I can barely stay at home with how much\x01",
            "my parents nag at me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish they'd piss off and give me\x01",
            "some freedom.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAE3")

    Jump("loc_CDC6")

    label("loc_CAE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_CB40")

    ChrTalk(
        0xFE,
        "I'm friggin' starved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Think I'll hit up Long Lao for some grub.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CDC6")

    label("loc_CB40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_CC79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC35")

    ChrTalk(
        0xFE,
        (
            "My family has been working\x01",
            "as merchants for generations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dad runs a trading company, and Grandpa\x01",
            "is chairman of the Business Owners'\x01",
            "Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not that I really give a damn about\x01",
            "any of that, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_CC74")

    label("loc_CC35")


    ChrTalk(
        0xFE,
        "Man, I'm beat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think I'll take another lazy day.\x02",
    )

    CloseMessageWindow()

    label("loc_CC74")

    Jump("loc_CDC6")

    label("loc_CC79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_CD5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD26")

    ChrTalk(
        0xFE,
        "I have way too much free time on my hands.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not really looking forward to being an\x01",
            "adult. I'm usually alone, so I don't have\x01",
            "much to do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_CD56")

    label("loc_CD26")


    ChrTalk(
        0xFE,
        "I have way too much free time on my hands.\x02",
    )

    CloseMessageWindow()

    label("loc_CD56")

    Jump("loc_CDC6")

    label("loc_CD5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_CDC6")

    ChrTalk(
        0xFE,
        (
            "My mom and dad keep making me\x01",
            "babysit Meiling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Holy heck, I wish they'd leave me alone.\x02",
    )

    CloseMessageWindow()

    label("loc_CDC6")

    TalkEnd(0xFE)
    Return()

    # Function_19_BCBC end

    def Function_20_CDCA(): pass

    label("Function_20_CDCA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_CE19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDE8")
    Call(0, 19)
    Jump("loc_CE14")

    label("loc_CDE8")


    ChrTalk(
        0xFE,
        "Yaaay! Big bwother finally cheewed up!\x02",
    )

    CloseMessageWindow()

    label("loc_CE14")

    Jump("loc_D617")

    label("loc_CE19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_CEB7")

    ChrTalk(
        0xFE,
        (
            "My bwother keeps stawing at some of\x01",
            "the people wawking down the stweets\x01",
            "for some weason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's been acting weally weird...\x01",
            "Is he okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D617")

    label("loc_CEB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_CF91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF67")

    ChrTalk(
        0xFE,
        (
            "Woy said he'd pway with me today,\x01",
            "I'm super-duper happy!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0xFE,
        "Huwway!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Me and my big bwother will\x01",
            "be together fowever!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_CF8C")

    label("loc_CF67")


    ChrTalk(
        0xFE,
        "We're gonna play a whole bunch!\x02",
    )

    CloseMessageWindow()

    label("loc_CF8C")

    Jump("loc_D617")

    label("loc_CF91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D09F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D051")
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xFE,
        "Hey, Woy! Wisten to this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I saw this huge doggie eawlier today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It had white fuw, and it was THIS big!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Oh, yeah? I'm happy for you.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x1, 2)
    Jump("loc_D09A")

    label("loc_D051")


    ChrTalk(
        0xFE,
        "Woy keeps spacing out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He's not even wistening to me at all...\x02",
    )

    CloseMessageWindow()

    label("loc_D09A")

    Jump("loc_D617")

    label("loc_D09F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_D10D")

    ChrTalk(
        0xFE,
        "The festivaw was super-duper fun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Me and my bwother went to sooo\x01",
            "many shops together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D617")

    label("loc_D10D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_D163")

    ChrTalk(
        0xFE,
        "Where'd you go, Woy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I told you not to weave me by mysewf!\x02",
    )

    CloseMessageWindow()
    Jump("loc_D617")

    label("loc_D163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_D1C9")

    ChrTalk(
        0xFE,
        "Don't weave me alone, Woy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mommy said you have to take\x01",
            "good cawe of me today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D617")

    label("loc_D1C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_D261")

    ChrTalk(
        0xFE,
        "La-la-la-la... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm going to play with my bwother again today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My bwother is the bestest! He pways with me\x01",
            "all the time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D617")

    label("loc_D261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_D2D4")

    ChrTalk(
        0xFE,
        (
            "My bwother bought me some tasty-wooking\x01",
            "candy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*munch* *munch* Omigosh!\x01",
            "That's sooo tasty!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D617")

    label("loc_D2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_D31E")

    ChrTalk(
        0xFE,
        "Daddy yelled at Woy a lot today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Cheer up, Woy!\x02",
    )

    CloseMessageWindow()
    Jump("loc_D617")

    label("loc_D31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_D39E")

    ChrTalk(
        0xFE,
        "Woy doesn't weally want to wun a stowe at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He towd me he's charging his 'life battewies'\x01",
            "wight now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D617")

    label("loc_D39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_D484")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D449")

    ChrTalk(
        0xFE,
        "Did you guys know Daddy is super impowtant?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's the pwesident of a hyuuuge\x01",
            "trading company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But, but... My bwother hates Daddy.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_D47F")

    label("loc_D449")


    ChrTalk(
        0xFE,
        "Woy hates Daddy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sniff*... I'm so sad...\x02",
    )

    CloseMessageWindow()

    label("loc_D47F")

    Jump("loc_D617")

    label("loc_D484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_D514")

    ChrTalk(
        0xFE,
        "La-la-la-la... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That wed building is the Bwacer Guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The bwacers are super nice and say\x01",
            "hi to me all the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D617")

    label("loc_D514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_D617")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5D2")
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xE,
        "Listen up, Meiling.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Your brother wants to be a\x01",
            "lazy nobody today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Feel free to stick around, but you\x01",
            "gotta be quiet, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Okays!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x1, 2)
    Jump("loc_D617")

    label("loc_D5D2")


    ChrTalk(
        0xFE,
        (
            "I'm weally, weally, excited to hang\x01",
            "out with my big bwother! ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D617")

    TalkEnd(0xFE)
    Return()

    # Function_20_CDCA end

    def Function_21_D61B(): pass

    label("Function_21_D61B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D62C")
    Jump("loc_E3C7")

    label("loc_D62C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D77A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D72B")

    ChrTalk(
        0xFE,
        (
            "I made sure to let my family\x01",
            "know I'd be cooking dinner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And yet they still came home\x01",
            "in the middle of the night!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They tried to play it off by saying\x01",
            "their manager wasn't on-site.\x01",
            "Like I'd believe that rubbish!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_D775")

    label("loc_D72B")


    ChrTalk(
        0xFE,
        "Now I'm really mad!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, THEY can\x01",
            "do all the housework!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D775")

    Jump("loc_E3C7")

    label("loc_D77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_D86B")

    ChrTalk(
        0xFE,
        "Oh, the men in my household...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They all came home together yesterday and\x01",
            "started immediately nagging me about dinner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I swear, the only time they're ever in agreement\x01",
            "with each other is when they're complaining!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3C7")

    label("loc_D86B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D947")

    ChrTalk(
        0xFE,
        (
            "I heard that Arios MacLaine is heading out\x01",
            "on a long business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm a little worried that criminals might get\x01",
            "a big head with him gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish he'd stay in Crossbell\x01",
            "as much as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3C7")

    label("loc_D947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_DA56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9F9")

    ChrTalk(
        0xFE,
        (
            "My boys have been lazing around at home\x01",
            "all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They APPARENTLY have the 'day off.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not like us housewives ever get\x01",
            "days off... *sigh*\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_DA51")

    label("loc_D9F9")


    ChrTalk(
        0xFE,
        (
            "If they have the day off, then couldn't they\x01",
            "at least try to help with the chores?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA51")

    Jump("loc_E3C7")

    label("loc_DA56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_DB43")

    ChrTalk(
        0xFE,
        (
            "Oh, barnacles! It's noon already?\x01",
            "I have to head home and get the\x01",
            "laundry going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Between cleaning, laundry, cooking, and shopping,\x01",
            "there's always a million things to do a day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Will somebody EVER help me out?\x02",
    )

    CloseMessageWindow()
    Jump("loc_E3C7")

    label("loc_DB43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_DC87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBFA")

    ChrTalk(
        0xFE,
        "All of my boys work at a construction site.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's fine and all, but all they do is complain about\x01",
            "how hard their jobs are whenever they're home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_DC82")

    label("loc_DBFA")


    ChrTalk(
        0xFE,
        (
            "And yet I'm the one who has a boatload of\x01",
            "chores to deal with, and they still act like\x01",
            "they're the only hard workers in the house.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC82")

    Jump("loc_E3C7")

    label("loc_DC87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_DCFA")

    ChrTalk(
        0xFE,
        (
            "Hmm... Is it just me, or has the selection\x01",
            "of fish been poor lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder why that is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E3C7")

    label("loc_DCFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_DEA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE1B")

    ChrTalk(
        0xFE,
        (
            "Did you hear that tickets to Arc en Ciel's\x01",
            "newest show have already sold out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Argh... If only I didn't have all these\x01",
            "chores to deal with all the time.\x01",
            "I would have loved to buy tickets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everybody in my family is a professional\x01",
            "at pissing me off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_DE9D")

    label("loc_DE1B")


    ChrTalk(
        0xFE,
        (
            "It'd be a total miracle if I could get any of\x01",
            "the men in the house to help with chores.\x01",
            "Argh... I'm so pissed off right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE9D")

    Jump("loc_E3C7")

    label("loc_DEA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_DF95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF34")

    ChrTalk(
        0xFE,
        (
            "I have a giant pile of dirty laundry\x01",
            "to wash when I get home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Having a large family can be painful at times.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_DF90")

    label("loc_DF34")


    ChrTalk(
        0xFE,
        (
            "My life would be much easier if I could\x01",
            "get the boys to help me out with the chores...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF90")

    Jump("loc_E3C7")

    label("loc_DF95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_E05B")

    ChrTalk(
        0xFE,
        (
            "The marketplace is pretty useful for\x01",
            "talking to various store owners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Some of the ladies here taught me a simple\x01",
            "and useful way to prepare fish when I'm\x01",
            "running low on time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3C7")

    label("loc_E05B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_E1EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E16D")

    ChrTalk(
        0xFE,
        (
            "We have not one, not two, but FIVE\x01",
            "big boys at our household.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've got all this brute strength, but it's totally\x01",
            "wasted on their lazy butts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do you know how amazing it'd be if I could get\x01",
            "ANY of them to help me with the chores?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_E1E6")

    label("loc_E16D")


    ChrTalk(
        0xFE,
        (
            "We have not one, not two, but FIVE\x01",
            "big boys at our household.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How tragic is it that I only gave birth to boys?\x02",
    )

    CloseMessageWindow()

    label("loc_E1E6")

    Jump("loc_E3C7")

    label("loc_E1EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_E320")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E298")

    ChrTalk(
        0xFE,
        (
            "Let's see... Eight carrots, twelve onions,\x01",
            "and fifteen salmon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhh, and then after that...I, uh...\x01",
            "Wait, what else did I need to buy?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_E31B")

    label("loc_E298")


    ChrTalk(
        0xFE,
        (
            "I sometimes forget what I'm thinking about\x01",
            "when I walk around the marketplace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhh... What was I supposed to buy, again?\x02",
    )

    CloseMessageWindow()

    label("loc_E31B")

    Jump("loc_E3C7")

    label("loc_E320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_E3C7")

    ChrTalk(
        0xFE,
        "Okay... Fishies...fishies...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All the boys in my house are\x01",
            "hefty eaters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a total pain in my behind to prepare\x01",
            "enough food for all of them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3C7")

    TalkEnd(0xFE)
    Return()

    # Function_21_D61B end

    def Function_22_E3CB(): pass

    label("Function_22_E3CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_E4A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E460")

    ChrTalk(
        0xFE,
        (
            "My mom didn't feel like shopping, so\x01",
            "she made me do it instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mom's always spending her whole day at home.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_E4A0")

    label("loc_E460")


    ChrTalk(
        0xFE,
        (
            "My mom always gets easily annoyed\x01",
            "by pretty much anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4A0")

    TalkEnd(0xFE)
    Return()

    # Function_22_E3CB end

    def Function_23_E4A4(): pass

    label("Function_23_E4A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_E5DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E555")

    ChrTalk(
        0xFE,
        (
            "I thought I managed to find the\x01",
            "cheapest shopping route...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like there's still plenty about this\x01",
            "world that I've yet to understand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_E5D5")

    label("loc_E555")


    ChrTalk(
        0xFE,
        (
            "I thought I managed to devise the\x01",
            "optimal shopping route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've decided to go and learn the quirks\x01",
            "of each shop again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5D5")

    Jump("loc_F4C7")

    label("loc_E5DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_E6F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E66A")

    ChrTalk(
        0xFE,
        (
            "Vegetables are starting to\x01",
            "become more expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What's up with that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This shouldn't be happening...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_E6F2")

    label("loc_E66A")


    ChrTalk(
        0xFE,
        (
            "Vegetables and fish seem to be getting\x01",
            "more expensive for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's up with that? It doesn't\x01",
            "make any sense at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6F2")

    Jump("loc_F4C7")

    label("loc_E6F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E8A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7DF")

    ChrTalk(
        0xFE,
        (
            "I was able to recently figure out\x01",
            "the optimal shopping route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I made sure to remember the\x01",
            "quirks of each and every shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe... It always makes me giddy\x01",
            "when I manage to save some mira. ♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_E89F")

    label("loc_E7DF")


    ChrTalk(
        0xFE,
        (
            "I figured out every shop's quirks, and with them,\x01",
            "the optimal shopping route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew... It feels like I just managed to solve a\x01",
            "difficult math problem. I'm so happy, I could\x01",
            "kiss you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E89F")

    Jump("loc_F4C7")

    label("loc_E8A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_E8B2")
    Jump("loc_F4C7")

    label("loc_E8B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_EA1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E998")

    ChrTalk(
        0xFE,
        (
            "I totally forgot because of\x01",
            "the Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xFE,
        "I need to finish my Sunday School homework, and fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Otherwise, the sister's going to be furious with me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_EA19")

    label("loc_E998")


    ChrTalk(
        0xFE,
        (
            "They had assigned us a bunch of homework\x01",
            "just before the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I gotta get home and finish it quickly.\x02",
    )

    CloseMessageWindow()

    label("loc_EA19")

    Jump("loc_F4C7")

    label("loc_EA1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_EC0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB5C")

    ChrTalk(
        0xFE,
        (
            "The chairman of the Business Owners' Association\x01",
            "is a great man and happens to be friends with\x01",
            "the mayor, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He started out as a simple street merchant,\x01",
            "but now he acts as a mediator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's actually incredibly kind. Believe it or not,\x01",
            "he's even stopped to talk to me before.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_EC09")

    label("loc_EB5C")


    ChrTalk(
        0xFE,
        (
            "The chairman of the Business Owners'\x01",
            "Association is an incredibly kind man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He even gave me a friendly little greeting when\x01",
            "we passed by each other earlier today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC09")

    Jump("loc_F4C7")

    label("loc_EC0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_ED0C")

    ChrTalk(
        0xFE,
        (
            "I managed to save even more mira\x01",
            "than I thought I would today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't let it get to my head, though.\x01",
            "I'll probably end up blowing it on\x01",
            "a bunch of dumb stuff, otherwise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've gotta do a better job of\x01",
            "saving up my allowance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F4C7")

    label("loc_ED0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_EDA5")

    ChrTalk(
        0xFE,
        (
            "Is it just me, or are Cronk's hands always\x01",
            "covered with bandages?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a little worrying, isn't it?\x01",
            "Is he going to be all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F4C7")

    label("loc_EDA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_EF07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE9A")

    ChrTalk(
        0xFE,
        (
            "Mom gave me a bunch of mira along\x01",
            "with the shopping list.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I really use my brain when I shop, I should\x01",
            "have some leftover cash.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to keep my eyes peeled for deals and\x01",
            "spend as little as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_EF02")

    label("loc_EE9A")


    ChrTalk(
        0xFE,
        (
            "Let's see, the prices on fish\x01",
            "change depending on the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This is tougher than I expected...\x02",
    )

    CloseMessageWindow()

    label("loc_EF02")

    Jump("loc_F4C7")

    label("loc_EF07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_EF7C")

    ChrTalk(
        0xFE,
        "Oh, yeah. I have Sunday School today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to finish up shopping so I can\x01",
            "head over there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F4C7")

    label("loc_EF7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_F0D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F095")

    ChrTalk(
        0xFE,
        (
            "Hmm... I'm pretty sure it's cheapest to\x01",
            "buy from Dinz Fresh in bulk right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the other hand, the key to vegetables\x01",
            "is to keep them fresh, so maybe I should\x01",
            "only buy a few of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll think on it while I check out some other stores.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_F0CD")

    label("loc_F095")


    ChrTalk(
        0xFE,
        (
            "It's actually pretty hard to buy stuff\x01",
            "cheap, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F0CD")

    Jump("loc_F4C7")

    label("loc_F0D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_F22D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1A9")

    ChrTalk(
        0xFE,
        (
            "I saw some bracers hanging out in the\x01",
            "marketplace this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They always look like they're ultra busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They usually come rushing out of the guild\x01",
            "whenever trouble calls.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_F228")

    label("loc_F1A9")


    ChrTalk(
        0xFE,
        (
            "Funnily enough, they looked pretty relaxed\x01",
            "this morning...for once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bought myself some vegetables\x01",
            "from Dinz Fresh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F228")

    Jump("loc_F4C7")

    label("loc_F22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_F382")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F30B")

    ChrTalk(
        0xFE,
        (
            "Dinz was having a sale, so I may have bought\x01",
            "myself a little more than I was planning to...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "I was trying to save some money, but\x01",
            "look at how that turned out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_F37D")

    label("loc_F30B")


    ChrTalk(
        0xFE,
        (
            "Trading's actually pretty deep when you think about it.\x01",
            "Shopping isn't exactly a walk in the market, either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F37D")

    Jump("loc_F4C7")

    label("loc_F382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_F4C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F42F")

    ChrTalk(
        0xFE,
        (
            "Hmm. This shop looks like it's a\x01",
            "little cheaper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, hold on. I'm pretty sure I heard\x01",
            "this other store lets you haggle with them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_F4C7")

    label("loc_F42F")


    ChrTalk(
        0xFE,
        (
            "All of the produce vendors run a limited time\x01",
            "sale during the evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I figure I should wait a little while\x01",
            "before I buy anything from them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F4C7")

    TalkEnd(0xFE)
    Return()

    # Function_23_E4A4 end

    def Function_24_F4CB(): pass

    label("Function_24_F4CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_F53E")

    ChrTalk(
        0xFE,
        (
            "What's with all the commotion coming\x01",
            "from the bridge over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Was there an accident?\x02",
    )

    CloseMessageWindow()
    Jump("loc_F6F6")

    label("loc_F53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_F6F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F623")

    ChrTalk(
        0xFE,
        (
            "You know you can always count on the\x01",
            "Bracer Guild, wherever you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what country you may find\x01",
            "yourself in, people know who to turn to.\x01",
            "It definitely makes traveling less stressful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_F6F6")

    label("loc_F623")


    ChrTalk(
        0xFE,
        (
            "You know you can always count on the\x01",
            "Bracer Guild, wherever you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That goes double for Crossbell. I've heard\x01",
            "nothing but incredible things about the\x01",
            "branch here, so I've got nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6F6")

    TalkEnd(0xFE)
    Return()

    # Function_24_F4CB end

    def Function_25_F6FA(): pass

    label("Function_25_F6FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_F843")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F719")
    Call(0, 26)
    Jump("loc_F843")

    label("loc_F719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7B3")

    ChrTalk(
        0xFE,
        "Welcome, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come grab a bite. I'm begging you.\x01",
            "I'm one failure away from the chewing\x01",
            "out of a lifetime from my boss.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_F843")

    label("loc_F7B3")


    ChrTalk(
        0xFE,
        "Could my boss be any more intimidating?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, maybe I should have found myself\x01",
            "part-time work at literally any other shop\x01",
            "in the area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F843")

    TalkEnd(0xFE)
    Return()

    # Function_25_F6FA end

    def Function_26_F847(): pass

    label("Function_26_F847")


    ChrTalk(
        0xFE,
        (
            "I managed to come up with this\x01",
            "genius mapo tofu recipe while\x01",
            "working here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You guys wanna learn something cool?\x02",
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
            "Received the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x194),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x194),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x2)
    Return()

    # Function_26_F847 end

    def Function_27_F940(): pass

    label("Function_27_F940")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_FA7C")
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)
    OP_4B(0x17, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F96A")
    Call(0, 28)
    Jump("loc_FA70")

    label("loc_F96A")


    ChrTalk(
        0x17,
        (
            "#6002FI can hear the sound of the breeze...\x02\x03",
            "Thank you so much, Estelle\x01",
            "and Joshua!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#0809FAww, Shizuku. You're such a sweetie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#0902FI'm just happy that you're happy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004F(I'd be lying if I said I wasn't at least\x01",
            "a little jealous of them.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA70")

    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    OP_4C(0x17, 0xFF)

    label("loc_FA7C")

    TalkEnd(0xFE)
    Return()

    # Function_27_F940 end

    def Function_28_FA80(): pass

    label("Function_28_FA80")

    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_68(-24130, -1400, 4220, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -19520, -3000, 5040, 270)
    SetChrPos(0x102, -19520, -3000, 3780, 270)
    SetChrPos(0x103, -18270, -3000, 3780, 270)
    SetChrPos(0x104, -18270, -3000, 5040, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FB28")
    SetChrPos(0x10A, -18500, -3000, 2490, 270)

    label("loc_FB28")

    OP_0D()
    Sleep(250)

    ChrTalk(
        0x17,
        (
            "#6000FPinwheels are really interesting.\x02\x03",
            "While I can't see them, I can certainly\x01",
            "feel them moving through the air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#0800FOh, yeah? So you can use 'em to\x01",
            "hear and feel the flow of the wind?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x8, 500)

    ChrTalk(
        0x16,
        (
            "#0900FExcuse me, sir. I'd like one of\x01",
            "the pink ones, please.\x02\x03",
            "Could you gift wrap it,\x01",
            "if possible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Of course!\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x17)

    ChrTalk(
        0x17,
        "#6008FJ-Joshua...?\x02",
    )

    CloseMessageWindow()
    OP_93(0x16, 0x5A, 0x1F4)

    ChrTalk(
        0x15,
        (
            "#0800FDon't you worry your pretty little head,\x01",
            "Shizuku. It's just a little something from us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0904FRight. And besides, Arios is always\x01",
            "looking out for us.\x02\x03",
            "#0902FThat's not exactly why we're buying you\x01",
            "a gift, but we'd be elated if you accepted\x01",
            "it, regardless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#6002FTh-Thank you so much...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-19140, -1400, 3950, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    Sleep(100)

    ChrTalk(
        0x104,
        "#0300F(Haha. Warms your heart, don't it?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Yeah. We probably shouldn't interrupt\x01",
            "their fun, though.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD0, 1)
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_FA80 end

    def Function_29_FE9C(): pass

    label("Function_29_FE9C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-16810, 1440, 25050, 0)
    MoveCamera(49, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26970, 0)
    OP_68(-1670, 1440, 2470, 7000)
    MoveCamera(25, 17, 0, 7000)
    OP_6E(600, 7000)
    SetCameraDistance(21920, 7000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(5230, -200, -13420, 0)
    MoveCamera(54, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    OP_68(-26250, 1500, -2620, 6000)
    MoveCamera(22, 22, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(14290, 6000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0xB, 0x8000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-6850, 1440, -820, 0)
    MoveCamera(35, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31810, 0)
    SetCameraDistance(37810, 5000)
    OP_0D()
    PlaceName2(340, 40, "c_plac04", 0x0, 0)
    OP_6F(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1023F")

    AnonymousTalk(
        0x104,
        "#0305FWowza. Talk about an exotic-lookin' street, eh?\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#0202FI believe this style is referred to as 'Eastern-inspired.'\x01",
            "I have some knowledge of the area, but it pales in\x01",
            "comparison to seeing it in person.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#0102FI haven't had the chance to properly look at all\x01",
            "of the stalls at the marketplace, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        "#0309FYeah? Why don't we check it out, then?\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#0006FIs this the part where I remind everybody\x01",
            "that we aren't here to shop?\x02\x03",
            "#0008F(And besides, I think the Bracer Guild is\x01",
            "located somewhere around here.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1023F")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "East Street is an Eastern-inspired district\x01",
            "on the east side of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The marketplace is filled with street vendors,\x01",
            "and is popular among shoppers.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Additionally, the Crossbell branch of the Bracer Guild is\x01",
            "located in the area and provides support to the citizenry.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10416")
    OP_68(-29790, 1420, 13830, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)
    Jump("loc_10463")

    label("loc_10416")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10463")
    SetChrPos(0x0, -20550, -310, 29980, 180)
    OP_68(-20550, 1440, 29980, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)

    label("loc_10463")

    SetScenarioFlags(0x44, 5)
    EventEnd(0x5)
    Return()

    # Function_29_FE9C end

    def Function_30_10469(): pass

    label("Function_30_10469")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-10500, 2000, -1000, 0)
    MoveCamera(65, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 27600, -300, -2700, 0)
    SetChrPos(0x1, 27600, -300, -2700, 0)
    SetChrPos(0x2, 27600, -300, -2700, 0)
    SetChrPos(0x3, 27600, -300, -2700, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_4B(0x10, 0xFF)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0x10, -19900, -320, 18140, 90)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrPos(0xC, -16300, -300, 12700, 135)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrPos(0xD, -4900, -300, 4000, 315)
    SetChrFlags(0xD, 0x8000)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KThe same day, 3:00PM...\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7103", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_105D9():
        OP_98(0xFE, 0x32C8, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_105D9)

    def lambda_105F3():
        OP_98(0xFE, 0xFFFFCD38, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_105F3)
    OP_68(-10500, 1000, -1000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-7500, 2100, 14100, 0)
    MoveCamera(75, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(17500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    ClearScenarioFlags(0x2, 4)
    SetScenarioFlags(0x5C, 1)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_10469 end

    def Function_31_10681(): pass

    label("Function_31_10681")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-7800, 1300, 13600, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    SetChrPos(0x101, -7000, 300, 14400, 225)
    SetChrPos(0x102, -7000, 300, 14400, 225)
    SetChrPos(0x103, -7000, 300, 14400, 225)
    SetChrPos(0x104, -7000, 300, 14400, 225)
    OP_4B(0x17, 0xFF)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrPos(0x17, -7000, 300, 14400, 225)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_4B(0x10, 0xFF)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0x10, -19900, -320, 18140, 90)
    SetChrFlags(0x10, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x2)
    OP_68(-11000, 700, 10250, 4500)

    def lambda_107D6():
        OP_95(0xFE, -12000, -300, 9400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_107D6)

    def lambda_107F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_107F0)
    Sleep(500)

    def lambda_10804():
        OP_95(0xFE, -10600, -300, 10800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10804)

    def lambda_1081E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1081E)
    Sleep(500)

    def lambda_10832():
        OP_95(0xFE, -10600, -300, 10800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10832)

    def lambda_1084C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1084C)
    Sleep(500)

    def lambda_10860():
        OP_95(0xFE, -10600, -300, 10800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10860)

    def lambda_1087A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1087A)
    Sleep(700)

    def lambda_1088E():
        OP_95(0xFE, -9600, -300, 11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1088E)

    def lambda_108A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_108A8)
    WaitChrThread(0x103, 1)

    def lambda_108BD():
        OP_95(0xFE, -11000, -300, 9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_108BD)

    def lambda_108D7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_108D7)
    WaitChrThread(0x102, 1)

    def lambda_108EC():
        OP_95(0xFE, -11600, -300, 11200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_108EC)

    def lambda_10906():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10906)
    WaitChrThread(0x104, 1)

    def lambda_1091B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1091B)
    WaitChrThread(0x103, 1)

    def lambda_1092C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1092C)
    WaitChrThread(0x102, 1)

    def lambda_1093D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1093D)
    WaitChrThread(0x101, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x102, 2)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5100177V#0006F#11PMan... I feel a little overwhelmed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100178V#6P#0204FI anticipated Arios' proficiency, but\x01",
            "Estelle and Joshua show promise, too.\x02\x03",
            "#5100179V#0202FOnce you factor in all of the other members,\x01",
            "everybody appears to be highly skilled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100180V#6P#0300FI'm willin' to bet a few mira that they're all\x01",
            "B-rank or higher, but...\x02\x03",
            "#5100181V...ain't it kinda rare for a branch to have\x01",
            "THIS many budding bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100182V#5P#0102FAll this means is that the guild realizes\x01",
            "the importance of Crossbell, right?\x02\x03",
            "#5100183V#0106FHowever, they know they have the upper hand,\x01",
            "since they can act in ways the police can't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100184V#0006F#11PYeah, all that means is that we'll just have to\x01",
            "work twice as hard.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-10100, 700, 11300, 1200)

    def lambda_10C81():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10C81)
    Sleep(150)

    def lambda_10C91():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10C91)
    Sleep(50)
    TurnDirection(0x102, 0x17, 500)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#5100185V#6P#0012FSorry, Shizuku. It's not exactly professional\x01",
            "of us to discuss this in front of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5100186V#6002F#11POh, please. I don't mind at all.\x02\x03",
            "#5100187V#6008FOf course, I've heard that my father was\x01",
            "a police officer a long time ago...\x02\x03",
            "#5100188VI know there are plenty of complicated\x01",
            "problems happening right now.\x02\x03",
            "#5100189V#6000FBut this time, everybody's going to work\x01",
            "together to fix it, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F2E")

    ChrTalk(
        0x101,
        (
            "#5100193V#6P#0004FYeah, though I think we're receiving more\x01",
            "help than we're providing.\x02\x03",
            "#5100205V#0002FAnyway, we'll lead you to the SSS now,\x01",
            "if that's okay with you.\x02\x03",
            "#5100206VMind holding on to my hand?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1133B")

    label("loc_10F2E")


    ChrTalk(
        0x101,
        (
            "#5100190V#6P#0004FYeah, though I think we're receiving more\x01",
            "help than we're providing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5100194V#6P#0000FOh, yeah. I just remembered that handmade\x01",
            "pendant from the other day.\x02\x03",
            "#5100195VWere you able to give it to your dad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5100196V#6005F#11POh, yes. I did.\x02\x03",
            "#5100197V#6000FHeheh... The truth is, Father came\x01",
            "to visit me last night.\x02\x03",
            "#5100198V#6010FI managed to give him the present, but I can\x01",
            "only wonder about the look on his face.\x02\x03",
            "#5100199VHe went silent for a bit before he awkwardly\x01",
            "thanked me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100200V#6P#0302FHaha. I bet he said somethin' like\x01",
            "'I'll hold on to this.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#5100201V#6002F#11PYes, essentially.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100202V#6P#0204FA man of few words, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100203V#6P#0109FIt sounds like even somebody like Arios\x01",
            "manages to get embarrassed by dear\x01",
            "little Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100204V#6P#0004FYeah, and I think that's a testament to\x01",
            "how important you are to him.\x02\x03",
            "#5100191V#0002FAnyway, we'll lead you to the SSS now,\x01",
            "if that's okay with you.\x02\x03",
            "#5100192VMind holding on to my hand?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1133B")


    ChrTalk(
        0x17,
        (
            "#5100207V#6000F#11PO-Okay. Thank you for the assistance.\x02\x03",
            "#5100208V#6005FNow that I think about it,\x01",
            "KeA's there, isn't she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100209V#0102FYes, she is. I think she's probably\x01",
            "playing with Zeit right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100210V#6P#0202FI am sure KeA would be delighted to have\x01",
            "you participate in the fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#5100211V#6002F#11PI'm glad to hear that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100212V#6P#0302FRighto. Think it's about time we\x01",
            "escort the princess to our castle!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16650, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetChrPos(0x101, -17500, -300, 14300, 270)
    SetChrPos(0x102, -17400, -300, 13000, 270)
    SetChrPos(0x103, -16000, -300, 13200, 270)
    SetChrPos(0x104, -15800, -300, 14500, 270)
    SetChrPos(0x17, -17500, -300, 13700, 270)
    OP_68(-22000, 500, 13700, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(15500, 0)

    def lambda_1159B():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1159B)
    Sleep(15)

    def lambda_115B8():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_115B8)
    Sleep(15)

    def lambda_115D5():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_115D5)
    Sleep(15)

    def lambda_115F2():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_115F2)
    Sleep(15)

    def lambda_1160F():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1160F)
    BeginChrThread(0x101, 3, 0, 32)
    OP_68(-27000, 500, 13700, 10000)
    MoveCamera(54, 18, 0, 10000)
    SetCameraDistance(19500, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(700)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_63(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -40000, -340, 16000, 90)
    SetChrFlags(0xD, 0x8000)

    def lambda_116E7():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_116E7)
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(700)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_63(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5D, 7)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_10681 end

    def Function_32_1179C(): pass

    label("Function_32_1179C")

    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, -10000, -300, 6500, 315)
    SetChrFlags(0xC, 0x8000)

    def lambda_117C1():
        OP_95(0xFE, -16000, -300, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_117C1)
    WaitChrThread(0xC, 1)

    def lambda_117DF():
        OP_95(0xFE, -36000, -300, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_117DF)
    WaitChrThread(0xC, 1)
    Return()

    # Function_32_1179C end

    def Function_33_117F9(): pass

    label("Function_33_117F9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
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
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")

    def lambda_118CD():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_118CD)
    Sleep(50)

    def lambda_118EA():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_118EA)
    Sleep(50)

    def lambda_11907():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11907)
    Sleep(50)

    def lambda_11924():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11924)
    SetCameraDistance(20500, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sound(806, 2, 100, 0)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)
    Sleep(250)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_11987():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11987)
    Sleep(50)

    def lambda_11997():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11997)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(1084, 255, 90, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#2100266V#0001FThis is Lloyd Bannings of the\x01",
            "SSS speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(2083, 255, 100, 0)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100267V\x07\x05",
            "Oh, Lloyd!\x02\x03",
            "#2100268VOh, what a relief! The call went through.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#2100269V\x07\x00",
            "#0005FWhat's up, Fran? It's not like you\x01",
            "to directly contact us.\x02\x03",
            "#2100270V#0000FAre there urgent matters to tend to?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100271V\x07\x05",
            "S-So, actually...\x02\x03",
            "#2100272VA citizen would like to speak with the\x01",
            "Special Support Section.\x02\x03",
            "#2100273VAre you okay with a face-to-face meeting?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#2100274V\x07\x00",
            "#0001FYeah, that shouldn't be a problem.\x02\x03",
            "#2100275VOne question, though. Why didn't you send\x01",
            "the request through the terminal like you\x01",
            "normally would?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100276V\x07\x05",
            "So, about that... It sounds like the request\x01",
            "is a bit more serious than usual.\x02\x03",
            "#2100277VNot to mention, it's rare to have somebody\x01",
            "specifically ask for you.\x02\x03",
            "#2100278VI figured you guys would be okay with it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#2100279V\x07\x00",
            "#0012FG-Got'cha...\x02\x03",
            "#2100280V#0000FI think I understand the situation.\x01",
            "Should we return to the SSS?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100281V\x07\x05",
            "That'd be perfect! I'll tell the client to meet you\x01",
            "there.\x02\x03",
            "#2100282VDo you have any idea when you'll be back?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#2100283V\x07\x00",
            "#0003FHmm, let me think...\x02\x03",
            "#2100284V#0000FWe're a ways away, so let them know they're\x01",
            "free to wait inside if they manage to get there\x01",
            "first.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100285V\x07\x05",
            "Okay, sounds like a plan!\x02\x03",
            "#2100286VThanks, Lloyd. I hope your meeting\x01",
            "goes well!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(825, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2100287V\x07\x00",
            "#0105F#5PWhat's wrong? It sounded urgent.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    OP_0D()
    Sleep(150)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#2100288V#6P#0003FYeah, well...Fran was being a little vague,\x01",
            "but it looks like we've got a serious request.\x02\x03",
            "#2100289V#0000FLet's finish up any unfinished business\x01",
            "and head back to the SSS, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100290V#0202F#11PRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100291V#5P#0309FYo, Lloyd. Is our client a sexy lady this time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100292V#6P#0006FHow do you expect me to know that, Randy?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0x0, 24700, -300, 500, 270)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x80, 1)
    OP_29(0x41, 0x1, 0x2)
    OP_24(0x326)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_33_117F9 end

    def Function_34_12263(): pass

    label("Function_34_12263")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5890, -1400, -10830, 0)
    MoveCamera(53, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14300, 0)
    SetChrPos(0x101, -5200, -3000, -10840, 0)
    SetChrPos(0x102, -3950, -3000, -12150, 0)
    SetChrPos(0x103, -5040, -3000, -11950, 0)
    SetChrPos(0x104, -3970, -3000, -10800, 0)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12377")

    ChrTalk(
        0x101,
        (
            "#6P#0003F(Hmm... Tront said he walked around\x01",
            "East Street's marketplace. He might\x01",
            "have dropped something here.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_12377")


    ChrTalk(
        0x101,
        (
            "#6P#0000FExcuse me. Have you picked up any\x01",
            "items off the ground recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PDropped something, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PActually, wait a sec... I remember some guy\x01",
            "wandering around here yesterday trying to\x01",
            "find something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PDidn't stop him from making a dull\x01",
            "joke when he saw my stall, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PI don't think he noticed the gaping hole\x01",
            "in his bag because a package fell out of\x01",
            "it when he wasn't paying attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PI tried catching up to him, but it was too late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0300FJackpot, baby.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5POh? You the folks the police\x01",
            "sent to pick it up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PGuess I'll leave it with you, then.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x338),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x338, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x337, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x338, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x339, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_126D5")

    ChrTalk(
        0x101,
        (
            "#0006FPhew... This should wrap\x01",
            "up our search, I think.\x02\x03",
            "#0000FWe should report the good news to Tront.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FSounds like a good plan to me.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_126D5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-4630, -1400, -10720, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, -4630, -3000, -10720, 0)
    SetChrPos(0x1, -4630, -3000, -10720, 0)
    SetChrPos(0x2, -4630, -3000, -10720, 0)
    SetChrPos(0x3, -4630, -3000, -10720, 0)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    OP_29(0x2, 0x1, 0x2)
    SetScenarioFlags(0x2, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1278C")
    OP_29(0x2, 0x1, 0x1F)

    label("loc_1278C")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_34_12263 end

    def Function_35_12792(): pass

    label("Function_35_12792")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1286D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12838")

    ChrTalk(
        0x101,
        (
            "#0000FThis is the city's east exit.\x02\x03",
            "We have no reason to leave right now, though.\x01",
            "Let's knock out our work in the city first.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1286D")

    label("loc_12838")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's no reason to leave the city now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1286D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12929")

    ChrTalk(
        0x101,
        (
            "#0000FWe'll need to leave via the city's southern gate if\x01",
            "we want to get to St. Ursula Medical College.\x02\x03",
            "We should head down towards Station Street\x01",
            "from Central Square.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_129BD")

    ChrTalk(
        0x101,
        (
            "#0000FWe'll need to leave via the city's northern gate\x01",
            "if we want to get to Mainz.\x02\x03",
            "Let's head over to the Residential District.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_129BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12AA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A64")

    ChrTalk(
        0x101,
        (
            "#0005FWe aren't supposed to leave the city.\x02\x03",
            "#0000FKeA's safety is our top priority, and we can't\x01",
            "do anything to jeopardize that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12AA0")

    label("loc_12A64")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's no reason to leave via the highway now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_12AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12B79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B3E")

    ChrTalk(
        0x101,
        (
            "#0003FThis is the city's east exit.\x02\x03",
            "We already have our hands full with the\x01",
            "Heiyue case, so let's deal with that first.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12B79")

    label("loc_12B3E")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's no reason to leave the city right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_12B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_12C2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12BE3")

    ChrTalk(
        0x101,
        (
            "#0000FThe city's eastern gate is this way.\x01",
            "We should hurry to St. Ursula!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12C2E")

    label("loc_12BE3")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's no reason to leave via the\x01",
            "East Crossbell Highway now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_12C2E")

    SetChrPos(0x0, 29390, -300, 500, 270)
    EventEnd(0x4)
    Return()

    # Function_35_12792 end

    def Function_36_12C42(): pass

    label("Function_36_12C42")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12DF9")

    ChrTalk(
        0x10A,
        "#0603F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FIs something bothering you, Dudley?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12CBE")

    ChrTalk(
        0x10A,
        "#0601FThe damned guild...\x02",
    )

    CloseMessageWindow()
    Jump("loc_12D0A")

    label("loc_12CBE")


    ChrTalk(
        0x10A,
        (
            "#0601F*glare* You guys aren't seriously\x01",
            "planning on going in, are you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D0A")

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
        (
            "#0005F(Oh, that's right. Dudley hates\x01",
            "the guild, doesn't he?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(Probably a good idea to peace\x01",
            "outta here for today.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x47, 6)
    Jump("loc_12EC0")

    label("loc_12DF9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E5D")

    ChrTalk(
        0x10A,
        (
            "#0603F...\x02\x03",
            "#0600FWe have absolutely no reason to be here.\x01",
            "Let's get moving.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EC0")

    label("loc_12E5D")


    ChrTalk(
        0x10A,
        "#0600F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(Dudley is shooting daggers at us...\x01",
            "We should avoid the guild for now.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EC0")

    Sleep(50)
    SetChrPos(0x0, -9300, -300, 12060, 225)
    EventEnd(0x4)
    Return()

    # Function_36_12C42 end

    def Function_37_12ED7(): pass

    label("Function_37_12ED7")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F9F")

    ChrTalk(
        0x101,
        (
            "#0005FWait...\x02\x03",
            "That restaurant over there is the one\x01",
            "the reporter told us about.\x02\x03",
            "#0003FWe'll need to get information one way or another,\x01",
            "so let's hear her out this one time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_13001")

    label("loc_12F9F")


    ChrTalk(
        0x101,
        (
            "#0003FWe'll need to get information one way or another,\x01",
            "so let's hear her out this one time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13001")

    Sleep(50)
    SetChrPos(0x0, -6210, -3000, -9790, 135)
    EventEnd(0x4)
    Return()

    # Function_37_12ED7 end

    def Function_38_13018(): pass

    label("Function_38_13018")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_130E0")

    ChrTalk(
        0x101,
        (
            "#0005FWait...\x02\x03",
            "That restaurant over there is the one\x01",
            "the reporter told us about.\x02\x03",
            "#0003FWe'll need to get information one way or another,\x01",
            "so let's hear her out this one time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_13142")

    label("loc_130E0")


    ChrTalk(
        0x101,
        (
            "#0003FWe'll need to get information one way or another,\x01",
            "so let's hear her out this one time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13142")

    Sleep(50)
    SetChrPos(0x0, 2100, -1350, -5490, 180)
    EventEnd(0x4)
    Return()

    # Function_38_13018 end

    def Function_39_13159(): pass

    label("Function_39_13159")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 7)), scpexpr(EXPR_END)), "loc_13198")
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
    Jump("loc_15355")

    label("loc_13198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13793")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_134FC")

    ChrTalk(
        0x153,
        "#1110FWhoooa... What is this thingy?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1329E")

    ChrTalk(
        0x102,
        (
            "#0105FI never thought I'd see a Jizo hiding here.\x01",
            "I've passed through here more times than I\x01",
            "can count, but I've never noticed it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1337D")

    label("loc_1329E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_13322")

    ChrTalk(
        0x103,
        (
            "#0205FThis statue has quite the...enormous face, does it not?\x01",
            "I have never encountered anything quite like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1337D")

    label("loc_13322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1337D")

    ChrTalk(
        0x104,
        (
            "#0305FYo, check out this Jizo. Kinda surprised\x01",
            "I've never noticed it before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1337D")


    ChrTalk(
        0x153,
        "#1111F...Jizo statue?\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x153,
        (
            "#1105FOooh, look at this thingy! It's like,\x01",
            "some kinda platform, I think?\x02\x03",
            "#1110FHe might be hungry, so we should\x01",
            "bring him some tasty food!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, I'm pretty sure this is a pedestal\x01",
            "meant to present offerings.\x02\x03",
            "#0000FThat's a good idea. Next time we make some\x01",
            "exceptional dishes, we should try bringing\x01",
            "them here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1378B")

    label("loc_134FC")


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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135F4")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    label("loc_135F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13617")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    label("loc_13617")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1363A")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    label("loc_1363A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1365D")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    label("loc_1365D")


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

    label("loc_1378B")

    SetScenarioFlags(0x98, 0)
    Jump("loc_15355")

    label("loc_13793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_137CF")
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
    Jump("loc_15355")

    label("loc_137CF")

    Call(0, 40)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13881")
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

    label("loc_13881")

    Call(0, 41)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B21")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a letter accompanied with a\x01",
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
    Jump("loc_15355")

    label("loc_13B21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13D38")
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
    Jump("loc_15355")

    label("loc_13D38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13F68")
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
    Jump("loc_15355")

    label("loc_13F68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14169")
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
    Jump("loc_15355")

    label("loc_14169")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_142DA")
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
    Jump("loc_15355")

    label("loc_142DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14405")
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
    Jump("loc_15355")

    label("loc_14405")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an Eastern-looking Jizo.\x02\x03",
            "Offer a supreme dish?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14454")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15355")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_144A8")
    MenuCmd(1, 1, "Dynasty Noodles")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_END)), "loc_1449E")
    Call(0, 16)

    label("loc_1449E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_144A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_144E4")
    MenuCmd(1, 1, "Huanglong Mapo Tofu")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_END)), "loc_144DA")
    Call(0, 16)

    label("loc_144DA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_144E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1451B")
    MenuCmd(1, 1, "Baihu Chao Fan")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_END)), "loc_14511")
    Call(0, 16)

    label("loc_14511")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1451B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14551")
    MenuCmd(1, 1, "Elegant Steak")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_END)), "loc_14547")
    Call(0, 16)

    label("loc_14547")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14587")
    MenuCmd(1, 1, "Aromatic Stew")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_END)), "loc_1457D")
    Call(0, 16)

    label("loc_1457D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_145BF")
    MenuCmd(1, 1, "Gorgeous Hotpot")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_END)), "loc_145B5")
    Call(0, 16)

    label("loc_145B5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_145BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_145F9")
    MenuCmd(1, 1, "Expressive Hotpot")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_END)), "loc_145EF")
    Call(0, 16)

    label("loc_145EF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_145F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14632")
    MenuCmd(1, 1, "Resurrection Fry")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_END)), "loc_14628")
    Call(0, 16)

    label("loc_14628")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1466E")
    MenuCmd(1, 1, "Radiant Omelet Rice")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_END)), "loc_14664")
    Call(0, 16)

    label("loc_14664")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1466E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_146A8")
    MenuCmd(1, 1, "Radiant Carbonara")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_END)), "loc_1469E")
    Call(0, 16)

    label("loc_1469E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_146A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_146DC")
    MenuCmd(1, 1, "King Burger")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_END)), "loc_146D2")
    Call(0, 16)

    label("loc_146D2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_146DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14710")
    MenuCmd(1, 1, "Queen Pizza")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_END)), "loc_14706")
    Call(0, 16)

    label("loc_14706")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1474B")
    MenuCmd(1, 1, "Partners' Sandwich")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_END)), "loc_14741")
    Call(0, 16)

    label("loc_14741")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1474B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14785")
    MenuCmd(1, 1, "Mother's Lunchbox")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_END)), "loc_1477B")
    Call(0, 16)

    label("loc_1477B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_147BC")
    MenuCmd(1, 1, "Full Moon Soup")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_END)), "loc_147B2")
    Call(0, 16)

    label("loc_147B2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_147BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_147F7")
    MenuCmd(1, 1, "Crescent Moon Soup")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_END)), "loc_147ED")
    Call(0, 16)

    label("loc_147ED")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_147F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1482D")
    MenuCmd(1, 1, "Pure Cut Cake")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_END)), "loc_14823")
    Call(0, 16)

    label("loc_14823")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1482D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14861")
    MenuCmd(1, 1, "Deep Yellow")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_END)), "loc_14857")
    Call(0, 16)

    label("loc_14857")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14897")
    MenuCmd(1, 1, "Powdered Snow")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_END)), "loc_1488D")
    Call(0, 16)

    label("loc_1488D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_148CE")
    MenuCmd(1, 1, "Drifting Cloud")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_END)), "loc_148C4")
    Call(0, 16)

    label("loc_148C4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_148CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14904")
    MenuCmd(1, 1, "Supreme Latte")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_END)), "loc_148FA")
    Call(0, 16)

    label("loc_148FA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14939")
    MenuCmd(1, 1, "Ultimate Mix")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_END)), "loc_1492F")
    Call(0, 16)

    label("loc_1492F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14972")
    MenuCmd(1, 1, "Nightmare Killer")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_END)), "loc_14968")
    Call(0, 16)

    label("loc_14968")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_149B0")
    MenuCmd(1, 1, "Moonlight Butterflies")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_END)), "loc_149A6")
    Call(0, 16)

    label("loc_149A6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_149B0")

    MenuCmd(1, 1, "Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_149F1")
    Jump("loc_15350")

    label("loc_149F1")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14A5D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A53")
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


    label("loc_14A53")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14AAA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AA0")
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


    label("loc_14AA0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14AF7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AED")
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


    label("loc_14AED")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14B44")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B3A")
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


    label("loc_14B3A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14B91")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B87")
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


    label("loc_14B87")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14BDE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BD4")
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


    label("loc_14BD4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14C2B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C21")
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


    label("loc_14C21")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14C78")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C6E")
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


    label("loc_14C6E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14CC5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14CBB")
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


    label("loc_14CBB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14D12")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D08")
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


    label("loc_14D08")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14D5F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D55")
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


    label("loc_14D55")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14DAC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DA2")
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


    label("loc_14DA2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14DF9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DEF")
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


    label("loc_14DEF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14E46")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E3C")
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


    label("loc_14E3C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14E93")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E89")
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


    label("loc_14E89")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14EE0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14ED6")
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


    label("loc_14ED6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14F2D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F23")
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


    label("loc_14F23")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14F7A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F70")
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


    label("loc_14F70")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14FC7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FBD")
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


    label("loc_14FBD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15014")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1500A")
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


    label("loc_1500A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15061")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15057")
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


    label("loc_15057")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_150AE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_150A4")
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


    label("loc_150A4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_150AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_150FB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_150F1")
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


    label("loc_150F1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_150FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15148")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1513E")
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


    label("loc_1513E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15148")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15350")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1534D")

    ChrTalk(
        0x101,
        (
            "#0000FAll right. Let's try bringing a different\x01",
            "dish next time.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1522E")

    ChrTalk(
        0x102,
        (
            "#0100FWe should avoid bringing any repeat\x01",
            "dishes, Lloyd. One of each kind should\x01",
            "suffice, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15325")

    label("loc_1522E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_152AF")

    ChrTalk(
        0x103,
        (
            "#0200FIt may be impolite of us to offer the\x01",
            "same dish twice. I recommend\x01",
            "providing a variety of meals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15325")

    label("loc_152AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15325")

    ChrTalk(
        0x104,
        (
            "#0300FBit rude to bring the guy the\x01",
            "same grub every time, eh?\x01",
            "Let's try to shake it up a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15325")


    ChrTalk(
        0x101,
        "#0000FOkay. Sounds like a plan.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x98, 1)

    label("loc_1534D")

    SetScenarioFlags(0x2, 5)

    label("loc_15350")

    Jump("loc_14454")

    label("loc_15355")

    TalkEnd(0xFF)
    Return()

    # Function_39_13159 end

    def Function_40_15359(): pass

    label("Function_40_15359")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1537C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1537C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15395")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_153AE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_153AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_153C7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_153C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_153E0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_153E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_153F9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_153F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15412")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1542B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1542B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15444")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1545D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1545D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15476")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1548F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1548F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_154A8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_154A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_154C1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_154C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_154DA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_154DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_154F3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_154F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1550C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1550C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15525")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1553E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1553E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15557")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15570")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15589")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_155A2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_155A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_155BB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_155BB")

    Return()

    # Function_40_15359 end

    def Function_41_155BC(): pass

    label("Function_41_155BC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_END)), "loc_155D9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_155D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_END)), "loc_155EC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_155EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_END)), "loc_155FF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_155FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_END)), "loc_15612")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_END)), "loc_15625")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_END)), "loc_15638")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_END)), "loc_1564B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1564B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_END)), "loc_1565E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1565E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_END)), "loc_15671")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_END)), "loc_15684")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_END)), "loc_15697")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_END)), "loc_156AA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_156AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_END)), "loc_156BD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_156BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_END)), "loc_156D0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_156D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_END)), "loc_156E3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_156E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_END)), "loc_156F6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_156F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_END)), "loc_15709")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_END)), "loc_1571C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1571C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_END)), "loc_1572F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1572F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_END)), "loc_15742")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_END)), "loc_15755")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_END)), "loc_15768")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_15768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_END)), "loc_1577B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1577B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_END)), "loc_1578E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1578E")

    Return()

    # Function_41_155BC end

    SaveToFile()

Try(main)
