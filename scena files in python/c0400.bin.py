from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0400.bin",                # FileName
        "c0400",                    # MapName
        "c0400",                    # Location
        0x0022,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 34, 0, 6, 0, 7],
    )

    BuildStringList((
        "c0400",                  # 0
        "Sophie",                 # 1
        "Barker Pym",             # 2
        "Portia",                 # 3
        "Tap",                    # 4
        "Ramanda",                # 5
        "Tejo",                   # 6
        "Bunny Girl",             # 7
        "Officer Kate",           # 8
        "Chief Roberts",          # 9
        "Estelle",                # 10
        "Joshua",                 # 11
        "Shizuku",                # 12
        "Elie",                   # 13
        "Mayor MacDowell",        # 14
        "Secretary Ernest",       # 15
        "市長車",                 # 16
        "Rixia",                  # 17
        "Ilya",                   # 18
        "Yin",                    # 19
        "Guide",                  # 20
        "Tourist",                # 21
        "Tourist",                # 22
        "Tourist",                # 23
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
        "chr/ch20400.itc",                   # 00
        "chr/ch36300.itc",                   # 01
        "chr/ch21900.itc",                   # 02
        "chr/ch34500.itc",                   # 03
        "chr/ch25900.itc",                   # 04
        "chr/ch27100.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch30600.itc",                   # 08
        "chr/ch29300.itc",                   # 09
        "chr/ch00600.itc",                   # 0A
        "chr/ch00700.itc",                   # 0B
        "chr/ch08700.itc",                   # 0C
        "chr/ch00102.itc",                   # 0D
        "chr/ch24400.itc",                   # 0E
    ))

    DeclNpc(-10750,  1759,    24469,   175,  261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4360,    0,       -10960,  310,  261,  0x0, 0,   4,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(379,     1769,    28049,   315,  261,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(1830,    1769,    27899,   315,  261,  0x0, 0,   14,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-50000,  9,       12069,   220,  257,  0x0, 0,   2,   0,   0,   2,   0,   16,  255,  0)
    DeclNpc(15439,   0,       10340,   45,   261,  0x0, 0,   0,   0,   0,   3,   0,   17,  255,  0)
    DeclNpc(-22049,  0,       12489,   175,  261,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-2380,   1990,    18079,   225,  389,  0x0, 0,   8,   0,   0,   4,   0,   19,  255,  0)
    DeclNpc(-9439,   1759,    22709,   0,    389,  0x0, 0,   9,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-9149,   1759,    24250,   90,   405,  0x0, 0,   10,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-7849,   1799,    23100,   315,  405,  0x0, 0,   11,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-7650,   1759,    24250,   270,  405,  0x0, 0,   12,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-12699,  1899,    26899,   180,  405,  0x0, 0,   13,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 44,  -2.0,                  19.0,                  1.0,                   2626.5625,             [0.04878048598766327,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.09756097197532654,   -3.799999952316284,    -0.20000000298023224,  1.0])
    DeclEvent(0x0000, 0, 46,  -2.0,                  19.0,                  1.0,                   2626.5625,             [0.04878048598766327,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.09756097197532654,   -3.799999952316284,    -0.20000000298023224,  1.0])
    DeclEvent(0x0000, 0, 60,  -2.0,                  35.0,                  1.0,                   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.3999999761581421,    -17.5,                 -0.19999998807907104,  1.0])
    DeclEvent(0x0000, 0, 61,  -26.5,                 16.739999771118164,    -0.5,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   8.833333969116211,     -8.369999885559082,    0.10000000894069672,   1.0])
    DeclEvent(0x0000, 0, 22,  -8.279999732971191,    24.030000686645508,    1.7599999904632568,    1640.25,               [0.07856739312410355,  0.07856745272874832,   -0.0,                  0.0,                   -0.07856745272874832,  0.07856739312410355,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.5385138988494873,    -1.237436056137085,    -0.35199999809265137,  1.0])
    DeclEvent(0x0000, 0, 44,  7.0,                   22.0,                  1.0,                   612.5625,              [0.222222238779068,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.09090909361839294,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.5555557012557983,   -2.0,                  -0.20000000298023224,  1.0])
    DeclEvent(0x0000, 0, 46,  7.0,                   22.0,                  1.0,                   612.5625,              [0.222222238779068,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.09090909361839294,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.5555557012557983,   -2.0,                  -0.20000000298023224,  1.0])

    DeclActor(-8160,   1770,    13680,   4000,    -8160,   2270,    13680,   0x007C, 0,  29, 0x0000)
    DeclActor(9850,    1760,    27000,   3500,    9850,    3260,    27000,   0x007C, 0,  30, 0x0000)
    DeclActor(16850,   0,       3030,    3500,    16850,   1500,    3030,    0x007C, 0,  31, 0x0000)
    DeclActor(-7810,   1760,    24750,   2500,    -7810,   3260,    24750,   0x007C, 0,  32, 0x0000)
    DeclActor(-4370,   0,       2950,    3500,    -4370,   500,     2950,    0x007C, 0,  33, 0x0000)

    PlaceName(90.5999984741211, 0.0, -111.88999938964844, 0x0000, 0x0000, "Central Square")
    PlaceName(-19.209999084472656, 0.0, -104.37999725341797, 0x0000, 0x0000, "West Street")
    PlaceName(135.69000244140625, 0.0, 36.7400016784668, 0x0000, 0x0000, "Administrative District")
    PlaceName(-121.08000183105469, 0.0, 20.040000915527344, 0x0000, 0x0000, "Residential District")
    PlaceName(0.8399999737739563, 0.0, 6.679999828338623, 0x0000, 0x0000, "Entertainment District")
    PlaceName(226.2899932861328, 0.0, -150.3000030517578, 0x0000, 0x0000, "East Street")
    PlaceName(285.57000732421875, 0.0, -242.14999389648438, 0x0000, 0x0000, "Downtown District")
    PlaceName(273.04998779296875, 0.0, -40.08000183105469, 0x0000, 0x0000, "Harbor District")
    PlaceName(229.6300048828125, 0.0, 116.9000015258789, 0x0000, 0x0000, "IBC")
    PlaceName(109.38999938964844, 0.0, -227.1199951171875, 0x0000, 0x0000, "Station Street")
    PlaceName(30.899999618530273, 0.0, -53.439998626708984, 0x0000, 0x0000, "Back Alley")
    PlaceName(104.37999725341797, 0.0, -278.8900146484375, 0x0000, 0x0000, "Ursula Road")
    PlaceName(316.4700012207031, 0.0, -126.91999816894531, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-104.37999725341797, 0.0, -106.87999725341797, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-94.36000061035156, 0.0, 60.119998931884766, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(53.86000061035156, 0.0, -135.27000427246094, 0x0000, 0x0051, "")
    PlaceName(143.6199951171875, 0.0, -91.8499984741211, 0x0000, 0x0054, "")
    PlaceName(94.7699966430664, 0.0, -148.6300048828125, 0x0000, 0x0057, "")
    PlaceName(52.61000061035156, 0.0, -86.83999633789062, 0x0000, 0x0053, "")
    PlaceName(86.83999633789062, 0.0, -46.7599983215332, 0x0000, 0x0053, "")
    PlaceName(2.0899999141693115, 0.0, -95.19000244140625, 0x0000, 0x0053, "")
    PlaceName(-14.199999809265137, 0.0, -60.119998931884766, 0x0000, 0x0053, "")
    PlaceName(25.889999389648438, 0.0, -6.679999828338623, 0x0000, 0x0052, "")
    PlaceName(33.81999969482422, 0.0, -28.389999389648438, 0x0000, 0x0053, "")
    PlaceName(48.43000030517578, 0.0, -42.59000015258789, 0x0000, 0x0053, "")
    PlaceName(96.02999877929688, 0.0, 75.98999786376953, 0x0000, 0x0051, "")
    PlaceName(283.07000732421875, 0.0, -150.3000030517578, 0x0000, 0x0052, "")
    PlaceName(254.67999267578125, 0.0, -301.44000244140625, 0x0000, 0x0053, "")
    PlaceName(232.97000122070312, 0.0, -270.5400085449219, 0x0000, 0x0053, "")
    PlaceName(109.38999938964844, 0.0, -131.92999267578125, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_A04",          # 00, 0
        "Function_1_ABC",          # 01, 1
        "Function_2_AE7",          # 02, 2
        "Function_3_C74",          # 03, 3
        "Function_4_DFB",          # 04, 4
        "Function_5_E26",          # 05, 5
        "Function_6_E70",          # 06, 6
        "Function_7_13BE",         # 07, 7
        "Function_8_178F",         # 08, 8
        "Function_9_2B92",         # 09, 9
        "Function_10_2C30",        # 0A, 10
        "Function_11_2CE9",        # 0B, 11
        "Function_12_2E4D",        # 0C, 12
        "Function_13_4556",        # 0D, 13
        "Function_14_56B8",        # 0E, 14
        "Function_15_5880",        # 0F, 15
        "Function_16_6931",        # 10, 16
        "Function_17_7AA5",        # 11, 17
        "Function_18_8CB5",        # 12, 18
        "Function_19_8F4B",        # 13, 19
        "Function_20_9219",        # 14, 20
        "Function_21_9629",        # 15, 21
        "Function_22_979B",        # 16, 22
        "Function_23_9CFF",        # 17, 23
        "Function_24_A5A8",        # 18, 24
        "Function_25_A629",        # 19, 25
        "Function_26_ABAF",        # 1A, 26
        "Function_27_B696",        # 1B, 27
        "Function_28_B706",        # 1C, 28
        "Function_29_B721",        # 1D, 29
        "Function_30_B7AB",        # 1E, 30
        "Function_31_B84F",        # 1F, 31
        "Function_32_B8E9",        # 20, 32
        "Function_33_B965",        # 21, 33
        "Function_34_B9DE",        # 22, 34
        "Function_35_BABB",        # 23, 35
        "Function_36_BAD7",        # 24, 36
        "Function_37_BAF3",        # 25, 37
        "Function_38_BB0F",        # 26, 38
        "Function_39_BB2B",        # 27, 39
        "Function_40_BB47",        # 28, 40
        "Function_41_BB63",        # 29, 41
        "Function_42_BBD6",        # 2A, 42
        "Function_43_BE76",        # 2B, 43
        "Function_44_C948",        # 2C, 44
        "Function_45_CD7B",        # 2D, 45
        "Function_46_DA79",        # 2E, 46
        "Function_47_F601",        # 2F, 47
        "Function_48_F647",        # 30, 48
        "Function_49_10332",       # 31, 49
        "Function_50_112D3",       # 32, 50
        "Function_51_11365",       # 33, 51
        "Function_52_113A2",       # 34, 52
        "Function_53_113FF",       # 35, 53
        "Function_54_11415",       # 36, 54
        "Function_55_11630",       # 37, 55
        "Function_56_1166D",       # 38, 56
        "Function_57_116AA",       # 39, 57
        "Function_58_116E7",       # 3A, 58
        "Function_59_11724",       # 3B, 59
        "Function_60_127A8",       # 3C, 60
        "Function_61_12D8A",       # 3D, 61
        "Function_62_130A0",       # 3E, 62
        "Function_63_130BC",       # 3F, 63
        "Function_64_130D8",       # 40, 64
    ))


    def Function_0_A04(): pass

    label("Function_0_A04")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_A44"),
        (1, "loc_A50"),
        (2, "loc_A5C"),
        (3, "loc_A68"),
        (4, "loc_A74"),
        (5, "loc_A80"),
        (6, "loc_A8C"),
        (SWITCH_DEFAULT, "loc_A98"),
    )


    label("loc_A44")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_A50")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_A5C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_A68")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_A74")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_A80")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_A8C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_A98")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_AA4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ABB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_ABB")

    Return()

    # Function_0_A04 end

    def Function_1_ABC(): pass

    label("Function_1_ABC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AE6")
    OP_94(0xFE, 0xED8, 0xFFFFEC96, 0x1AE0, 0xFFFFDE22, 0x3E8)
    Sleep(300)
    Jump("Function_1_ABC")

    label("loc_AE6")

    Return()

    # Function_1_ABC end

    def Function_2_AE7(): pass

    label("Function_2_AE7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C73")
    SetChrPos(0xFE, -50000, 10, 12070, 220)
    OP_95(0xFE, -18740, 10, 10280, 1500, 0x0)
    OP_95(0xFE, -2040, 1770, 9880, 1500, 0x0)
    OP_95(0xFE, 30970, 0, 12150, 1500, 0x0)
    Sleep(1500)
    SetChrPos(0xFE, 30210, 0, 8600, 270)
    OP_95(0xFE, 17210, 0, 8600, 1500, 0x0)
    OP_95(0xFE, 15010, 0, 6790, 1500, 0x0)
    OP_95(0xFE, 10210, 0, -960, 1500, 0x0)
    OP_95(0xFE, 8450, 0, -7690, 1500, 0x0)
    OP_95(0xFE, 10100, 0, -11960, 1500, 0x0)
    OP_95(0xFE, 28170, 0, -38880, 1500, 0x0)
    Sleep(1500)
    SetChrPos(0xFE, 28170, 0, -38880, 315)
    OP_95(0xFE, 9370, 0, -17000, 1500, 0x0)
    OP_95(0xFE, 4280, 0, -11560, 1500, 0x0)
    OP_95(0xFE, -4810, 0, -3900, 1500, 0x0)
    OP_95(0xFE, -13140, 0, 1410, 1500, 0x0)
    OP_95(0xFE, -21060, 0, 5360, 1500, 0x0)
    OP_95(0xFE, -26790, 0, 8090, 1500, 0x0)
    OP_95(0xFE, -50000, 10, 12070, 1500, 0x0)
    Sleep(1500)
    Jump("Function_2_AE7")

    label("loc_C73")

    Return()

    # Function_2_AE7 end

    def Function_3_C74(): pass

    label("Function_3_C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF4")

    label("loc_C82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CEF")
    OP_95(0xFE, 4650, 0, 3100, 1000, 0x0)
    OP_95(0xFE, -450, 0, 800, 1000, 0x0)
    OP_93(0xFE, 0x119, 0x0)
    Sleep(1500)
    OP_95(0xFE, 4150, 0, 3130, 1000, 0x0)
    OP_95(0xFE, 11400, 0, 7650, 1000, 0x0)
    Sleep(1500)
    Jump("loc_C82")

    label("loc_CEF")

    Jump("loc_DFA")

    label("loc_CF4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DFA")
    OP_95(0xFE, 8780, 0, 6460, 1000, 0x0)
    OP_95(0xFE, 2270, 0, 3060, 1000, 0x0)
    OP_95(0xFE, -5460, 0, 2360, 1000, 0x0)
    OP_95(0xFE, -14070, 0, 5650, 1000, 0x0)
    OP_95(0xFE, -19800, 0, 8020, 1000, 0x0)
    OP_95(0xFE, -26870, 0, 10100, 1000, 0x0)
    Sleep(1500)
    OP_95(0xFE, -19800, 0, 8020, 1000, 0x0)
    OP_95(0xFE, -14070, 0, 5650, 1000, 0x0)
    OP_95(0xFE, -5460, 0, 2360, 1000, 0x0)
    OP_95(0xFE, 2270, 0, 3060, 1000, 0x0)
    OP_95(0xFE, 8780, 0, 6460, 1000, 0x0)
    OP_95(0xFE, 11400, 0, 7650, 1000, 0x0)
    Sleep(1500)
    Jump("loc_CF4")

    label("loc_DFA")

    Return()

    # Function_3_C74 end

    def Function_4_DFB(): pass

    label("Function_4_DFB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E25")
    OP_94(0xFE, 0xFFFFEA7A, 0x4E98, 0x118, 0x4682, 0x3E8)
    Sleep(300)
    Jump("Function_4_DFB")

    label("loc_E25")

    Return()

    # Function_4_DFB end

    def Function_5_E26(): pass

    label("Function_5_E26")

    ClearChrFlags(0x17, 0x80)
    OP_78(0x4, 0x17)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x17, -5300, 0, 1800, 100)
    OP_D3(0x17, 0x0, 0x186A0, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_70(0x4, 0x0)
    Return()

    # Function_5_E26 end

    def Function_6_E70(): pass

    label("Function_6_E70")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A2")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F44")
    SetChrPos(0x0, 21040, 0, 11840, 270)
    SetChrPos(0x1, 21040, 0, 11840, 270)
    SetChrPos(0x2, 21040, 0, 11840, 270)
    SetChrPos(0x3, 21040, 0, 11840, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F17")
    SetChrPos(0x4, 21040, 0, 11840, 270)
    SetChrPos(0x5, 21040, 0, 11840, 270)
    Jump("loc_F36")

    label("loc_F17")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F36")
    SetChrPos(0x4, 21040, 0, 11840, 270)

    label("loc_F36")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10A2")

    label("loc_F44")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1001")
    SetChrPos(0x0, -39280, 0, 12420, 90)
    SetChrPos(0x1, -39280, 0, 12420, 90)
    SetChrPos(0x2, -39280, 0, 12420, 90)
    SetChrPos(0x3, -39280, 0, 12420, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FD4")
    SetChrPos(0x4, -39280, 0, 12420, 90)
    SetChrPos(0x5, -39280, 0, 12420, 90)
    Jump("loc_FF3")

    label("loc_FD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF3")
    SetChrPos(0x4, -39280, 0, 12420, 90)

    label("loc_FF3")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10A2")

    label("loc_1001")

    SetChrPos(0x0, 13270, 0, -19100, 315)
    SetChrPos(0x1, 13270, 0, -19100, 315)
    SetChrPos(0x2, 13270, 0, -19100, 315)
    SetChrPos(0x3, 13270, 0, -19100, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_107A")
    SetChrPos(0x4, 13270, 0, -19100, 315)
    SetChrPos(0x5, 13270, 0, -19100, 315)
    Jump("loc_1099")

    label("loc_107A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1099")
    SetChrPos(0x4, 13270, 0, -19100, 315)

    label("loc_1099")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10A2")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C1")
    Event(0, 45)
    Jump("loc_10DA")

    label("loc_10C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10DA")
    Event(0, 59)

    label("loc_10DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_10EE")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 48)
    Jump("loc_114D")

    label("loc_10EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1102")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 49)
    Jump("loc_114D")

    label("loc_1102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_1116")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 54)
    Jump("loc_114D")

    label("loc_1116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_112A")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 23)
    Jump("loc_114D")

    label("loc_112A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_113E")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 24)
    Jump("loc_114D")

    label("loc_113E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_114D")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 26)

    label("loc_114D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1160")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_134B")

    label("loc_1160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1196")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1178")
    SetChrFlags(0xA, 0x10)

    label("loc_1178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1191")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)

    label("loc_1191")

    Jump("loc_134B")

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_11B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_11AD")
    SetChrFlags(0xA, 0x10)

    label("loc_11AD")

    Jump("loc_134B")

    label("loc_11B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_11C0")
    Jump("loc_134B")

    label("loc_11C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_11F1")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jump("loc_134B")

    label("loc_11F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1212")
    ClearChrFlags(0xF, 0x80)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)
    Jump("loc_134B")

    label("loc_1212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1220")
    Jump("loc_134B")

    label("loc_1220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1251")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jump("loc_134B")

    label("loc_1251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_12B2")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_127C")
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)

    label("loc_127C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A8")
    ClearChrFlags(0x14, 0x80)
    Jump("loc_12AD")

    label("loc_12A8")

    ClearChrFlags(0x10, 0x80)

    label("loc_12AD")

    Jump("loc_134B")

    label("loc_12B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1302")
    SetChrPos(0x8, -9610, 1770, 24250, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12DD")
    Jump("loc_12FD")

    label("loc_12DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_12EB")
    Jump("loc_12FD")

    label("loc_12EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_12FD")
    ClearChrFlags(0x14, 0x80)

    label("loc_12FD")

    Jump("loc_134B")

    label("loc_1302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1315")
    SetChrFlags(0xA, 0x10)
    Jump("loc_134B")

    label("loc_1315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1323")
    Jump("loc_134B")

    label("loc_1323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_133D")
    TurnDirection(0xB, 0xA, 0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_134B")

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_134B")
    Jump("loc_134B")

    label("loc_134B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1362")
    SetMapFlags(0x10000000)
    Event(0, 43)

    label("loc_1362")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13BD")
    SetChrPos(0x0, -9950, 0, 3770, 220)
    SetChrPos(0x1, -9950, 0, 3770, 220)
    SetChrPos(0x2, -9950, 0, 3770, 220)
    SetChrPos(0x3, -9950, 0, 3770, 220)

    label("loc_13BD")

    Return()

    # Function_6_E70 end

    def Function_7_13BE(): pass

    label("Function_7_13BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13DA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_145A")

    label("loc_13DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13F6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_145A")

    label("loc_13F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1412")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_145A")

    label("loc_1412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_142E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_145A")

    label("loc_142E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_1445")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_145A")

    label("loc_1445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 0)), scpexpr(EXPR_END)), "loc_145A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x5F, 0)

    label("loc_145A")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 6, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_148B")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 5, 0x80)

    label("loc_148B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14A3")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 6, 0x80)

    label("loc_14A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14F4")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFE, 0xCB, 0xC0, 0x2C, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_1565")

    label("loc_14F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1540")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFE, 0xCB, 0xC0, 0x2C, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_1565")

    label("loc_1540")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_1565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_158B")
    SetMapObjFrame(0xFF, "ka01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ka02", 0x1, 0x1)
    Jump("loc_15A3")

    label("loc_158B")

    SetMapObjFrame(0xFF, "ka01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ka02", 0x0, 0x1)

    label("loc_15A3")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15BF")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_15BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15D6")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_15D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15ED")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_15ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1600")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1617")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1629")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1629")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1641")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1641")

    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1663")
    OP_1B(0x1, 0x0, 0x3E)
    OP_1B(0x2, 0x0, 0x3F)

    label("loc_1663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_167B")
    OP_1B(0x1, 0x0, 0x3E)
    OP_1B(0x2, 0x0, 0x3F)

    label("loc_167B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_168F")
    BeginChrThread(0x17, 0, 0, 5)

    label("loc_168F")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_16B1")
    Jump("loc_176D")

    label("loc_16B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_176D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_16CB")
    Jump("loc_176D")

    label("loc_16CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_16D9")
    Jump("loc_176D")

    label("loc_16D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_1713")
    OP_1B(0x1, 0x0, 0x24)
    OP_1B(0x2, 0x0, 0x25)
    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x4, 0x0, 0x27)
    OP_1B(0x5, 0x0, 0x28)
    OP_1B(0x6, 0x0, 0x29)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    Jump("loc_176D")

    label("loc_1713")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_176D")
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    OP_1B(0x0, 0x0, 0x23)
    OP_1B(0x1, 0x0, 0x24)
    OP_1B(0x2, 0x0, 0x25)
    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x5, 0x0, 0x28)
    OP_1B(0x6, 0x0, 0x29)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176D")
    Event(0, 42)

    label("loc_176D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1789")
    Jump("loc_178E")

    label("loc_1789")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_178E")

    Return()

    # Function_7_13BE end

    def Function_8_178F(): pass

    label("Function_8_178F")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_179C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B8E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17ED")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_17ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_180D")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B89")

    label("loc_180D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1821")
    Jump("loc_2B89")

    label("loc_1821")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B89")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1994")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18CC")

    ChrTalk(
        0x8,
        "Hey there! Want some handmade ice cream?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Come on, give it a try. Some delicious, smooth\x01",
            "ice cream won't harm ya.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_198F")

    label("loc_18CC")


    ChrTalk(
        0x8,
        (
            "Hey, did you know my ice cream's\x01",
            "handmade?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh. I bet you're thinking this ice cream\x01",
            "looks super delish!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You know it's good, right? It's time to buy some.\x01",
            "You know you want it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_198F")

    Jump("loc_2B89")

    label("loc_1994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1B34")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A08")

    ChrTalk(
        0x8,
        (
            "Man, everybody needs to chill out!\x01",
            "People freak out so easily these days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7F")

    label("loc_1A08")


    ChrTalk(
        0x8,
        (
            "Hey there, youngster. Er, I mean...fine sir!\x01",
            "Care for some tasty ice cream?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#0603FExcuse me? I'm only 27!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A7F")

    Jump("loc_1B2F")

    label("loc_1A84")


    ChrTalk(
        0x8,
        "Ice cream! Get your ice cream!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hey, mister! Yeah, you!\x01",
            "Come try my ice cream!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've even got a brandy-flavored sample\x01",
            "for adults with sophisticated palates!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B2F")

    Jump("loc_2B89")

    label("loc_1B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1C61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B93")

    ChrTalk(
        0x8,
        (
            "I'd say that eating ice cream with an\x01",
            "upset stomach is a bad idea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5C")

    label("loc_1B93")


    ChrTalk(
        0x8,
        (
            "Someone from Arc en Ciel told me\x01",
            "something interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They said one of their members has\x01",
            "been acting like a weirdo recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What's up with them? Oh, maybe\x01",
            "he has an upset stomach!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1C5C")

    Jump("loc_2B89")

    label("loc_1C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C9C")

    ChrTalk(
        0x8,
        "Ice cream! Get your ice cream!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D5B")

    label("loc_1C9C")


    ChrTalk(
        0x8,
        (
            "Business still hasn't slowed down, despite\x01",
            "the Anniversary Festival ending.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Phew! What a relief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You can leave your mira here after you've\x01",
            "purchased your ice cream. Thanks!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D5B")

    Jump("loc_2B89")

    label("loc_1D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E90")

    ChrTalk(
        0x8,
        (
            "Some other stall was selling ice cream over in\x01",
            "the Harbor District during the festival. Man, I was\x01",
            "sweating bullets for a second there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...until I was graciously crowned the\x01",
            "MVP of food stalls for the month!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is all thanks to each and every one\x01",
            "of my patrons!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F81")

    label("loc_1E90")


    ChrTalk(
        0x8,
        "Ice cream! Get your ice cream!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wow, my sales during the Anniversary\x01",
            "Festival kicked butt! That had to have been\x01",
            "twenty times more than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can only imagine that I clean sweeped\x01",
            "the competition in terms of total sales.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F81")

    Jump("loc_2B89")

    label("loc_1F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2291")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2109")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2033")

    ChrTalk(
        0x8,
        "Ice cream! Get your ice cream!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x11C, 500)

    ChrTalk(
        0x8,
        (
            "Hey there, cute doggie! You want\x01",
            "some ice cream? You know it's\x01",
            "good, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2105")

    label("loc_2033")


    ChrTalk(
        0x8,
        "Ice cream! Get your ice cream!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x11C, 500)

    ChrTalk(
        0x8,
        (
            "Hey there, cute doggie! You want\x01",
            "some ice cream? You know it's\x01",
            "good, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11C,
        "#1200FGrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(He claims that he 'does not have\x01",
            "a sweet fang.')\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2105")

    TalkEnd(0x8)
    Return()

    label("loc_2109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21B7")

    ChrTalk(
        0x8,
        (
            "Even members of the troupe are ranting\x01",
            "and raving over my ice cream!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Who knows? If I can get my ice cream to\x01",
            "a distributor, I'll get even more sales!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228C")

    label("loc_21B7")


    ChrTalk(
        0x8,
        (
            "My ice cream's so delicious that even\x01",
            "members of the troupe love it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's gotta be great if the wondrous\x01",
            "Ilya and Plie are regulars, right?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope I sell so much ice cream that\x01",
            "I become famous!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_228C")

    Jump("loc_2B89")

    label("loc_2291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2371")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_22F9")

    ChrTalk(
        0x8,
        (
            "Hello, my noble customers. You are\x01",
            "like kings, and your wish is my command.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_236C")

    label("loc_22F9")


    ChrTalk(
        0x8,
        "Hey, good morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We're not open yet...but hey, what the heck!\x01",
            "You wanna eat some ice cream anyway?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_236C")

    Jump("loc_2B89")

    label("loc_2371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_24E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2417")

    ChrTalk(
        0x8,
        (
            "You better hurry it up if you wanna try the\x01",
            "troupe's favorite flavors!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Try it out while you still can, or you're\x01",
            "going to regret it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E3")

    label("loc_2417")


    ChrTalk(
        0x8,
        "Ice cream! Get your ice cream!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Only a few more short moments until\x01",
            "Arc en Ciel's most popular flavors are\x01",
            "totally sold out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Try it out while you still can, or you're\x01",
            "going to regret it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_24E3")

    Jump("loc_2B89")

    label("loc_24E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_260D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_256C")

    ChrTalk(
        0x8,
        (
            "Fans of Arc en Ciel all love\x01",
            "buying our ice cream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Come on, join the hivemind.\x01",
            "You know you wanna.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2608")

    label("loc_256C")


    ChrTalk(
        0x8,
        "You guys all fans of Arc en Ciel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You are? Well, then, what are you waiting for?\x01",
            "Buy the ice cream...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Don't be shy. You know you want it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2608")

    Jump("loc_2B89")

    label("loc_260D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2772")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_269E")

    ChrTalk(
        0x8,
        (
            "I managed to get crowned as this month's\x01",
            "MVP among all the food stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "This is all thanks to my loyal patrons!\x02",
    )

    CloseMessageWindow()
    Jump("loc_276D")

    label("loc_269E")


    ChrTalk(
        0x8,
        "Wahoo! I kicked everybody's butts in sales!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, thank the dairy angels above!\x01",
            "I beat everybody else's sales numbers\x01",
            "this month!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks, everyone! I couldn't have\x01",
            "pulled it off without you!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_276D")

    Jump("loc_2B89")

    label("loc_2772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_28C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_27B9")

    ChrTalk(
        0x8,
        (
            "Boy, I really do love fans of\x01",
            "Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28BB")

    label("loc_27B9")


    ChrTalk(
        0x8,
        (
            "Those two are always out here bright\x01",
            "and early to cheer on Arc en Ciel. You\x01",
            "know what that means, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As soon as they all need their midday snacks,\x01",
            "I'm out here, waiting with some tasty ice cream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'm super grateful for their patronage.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_28BB")

    Jump("loc_2B89")

    label("loc_28C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_29AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2932")

    ChrTalk(
        0x8,
        (
            "Man, if only there was a juice stall out here.\x01",
            "I'd love to trade them some ice cream.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A7")

    label("loc_2932")


    ChrTalk(
        0x8,
        "Ice cream! Get your ice cream!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, boy. I'm super thirsty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Are there any juice stalls around here?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_29A7")

    Jump("loc_2B89")

    label("loc_29AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2A65")

    ChrTalk(
        0x8,
        (
            "Hey, listen to this cool recommendation!\x01",
            "Try out Sophie's Ice Cream!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You don't want to dilly-dally for too long.\x01",
            "I'm usually sold out by the afternoon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B28")

    label("loc_2A65")


    ChrTalk(
        0x8,
        "Ice cream! Get your ice cream!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hey, mister! Yeah, you!\x01",
            "Come try my ice cream!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Today's going to be a scorcher! I won't care\x01",
            "if you come crying to me later when I'm\x01",
            "all sold out!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2B28")

    Jump("loc_2B89")

    label("loc_2B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2B62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_END)), "loc_2B5A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x15)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B52")
    Call(0, 11)
    Jump("loc_2B55")

    label("loc_2B52")

    Call(0, 9)

    label("loc_2B55")

    Jump("loc_2B5D")

    label("loc_2B5A")

    Call(0, 9)

    label("loc_2B5D")

    Jump("loc_2B89")

    label("loc_2B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_END)), "loc_2B86")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x15)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7E")
    Call(0, 11)
    Jump("loc_2B81")

    label("loc_2B7E")

    Call(0, 10)

    label("loc_2B81")

    Jump("loc_2B89")

    label("loc_2B86")

    Call(0, 10)

    label("loc_2B89")

    Jump("loc_179C")

    label("loc_2B8E")

    TalkEnd(0xFE)
    Return()

    # Function_8_178F end

    def Function_9_2B92(): pass

    label("Function_9_2B92")


    ChrTalk(
        0x8,
        (
            "You guys know that Arc en Ciel's putting on\x01",
            "a public show later today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My sales have been growing at a remarkable\x01",
            "pace, but that's to be expected.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_9_2B92 end

    def Function_10_2C30(): pass

    label("Function_10_2C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2C8D")

    ChrTalk(
        0x8,
        (
            "My ice cream rocks! It'll be the most\x01",
            "delicious thing you've ever tasted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CE8")

    label("loc_2C8D")


    ChrTalk(
        0x8,
        "Ice cream! Get your ice cream!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hey, mister! Yeah, you!\x01",
            "Come try my ice cream!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2CE8")

    Return()

    # Function_10_2C30 end

    def Function_11_2CE9(): pass

    label("Function_11_2CE9")


    ChrTalk(
        0xFE,
        "Ice cream! Get your ice cream!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey there, mister! We're having a\x01",
            "free giveaway today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're handing out recipes for some\x01",
            "delicious vanilla au lait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's simply fabulous, so you gotta\x01",
            "try it out at least once.\x02",
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
            "Received the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1CD),
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
            scpstr(SCPSTR_CODE_ITEM, 0x1CD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x15)
    Return()

    # Function_11_2CE9 end

    def Function_12_2E4D(): pass

    label("Function_12_2E4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3002")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F60")

    ChrTalk(
        0xFE,
        (
            "Oh, hey there.\x01",
            "You fine folk free right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Interested in some drinks? How about\x01",
            "the finest women you've ever seen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heh heh heh. We've got a hell of a shop\x01",
            "that even the CGF's commander is fond\x01",
            "of. I promise you won't regret it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FFD")

    label("loc_2F60")


    ChrTalk(
        0xFE,
        (
            "Heh heh heh. We've got a hell of a shop that\x01",
            "even the CGF's commander is fond of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come in and have some fun. I promise\x01",
            "ya won't regret it one bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FFD")

    Jump("loc_4552")

    label("loc_3002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3163")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3099")

    ChrTalk(
        0x9,
        (
            "Been seeing cops come in and out of that\x01",
            "hotel for the last couple of days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Damn cops. They're screwing our business.\x02",
    )

    CloseMessageWindow()
    Jump("loc_315E")

    label("loc_3099")


    ChrTalk(
        0x9,
        (
            "Heard cops have been coming in and out of\x01",
            "that hotel for the last couple of days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "What are they going on about now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They gotta cut it out already.\x01",
            "It's weirding out my customers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_315E")

    Jump("loc_4552")

    label("loc_3163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_32B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_31DB")

    ChrTalk(
        0x9,
        "Yep. Today's definitely a weird one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I don't even feel like reeling in more customers.\x02",
    )

    CloseMessageWindow()
    Jump("loc_32B3")

    label("loc_31DB")


    ChrTalk(
        0x9,
        (
            "This district feels like it's been caught\x01",
            "up in a sticky situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I smell something fishy in the air.\x01",
            "The cops about to raid someone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I figure I should get the hell outta\x01",
            "here earlier than usual.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_32B3")

    Jump("loc_4552")

    label("loc_32B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3423")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3360")

    ChrTalk(
        0x9,
        (
            "Lotta people been coming back ever since\x01",
            "the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm pretty happy, bro. I'm inviting them\x01",
            "all to the special course!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_341E")

    label("loc_3360")


    ChrTalk(
        0x9,
        (
            "Lotta people been sticking around still,\x01",
            "even though the festival ended a\x01",
            "month ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I've gotta say, bro. I'm moved to tears.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's almost like they want me to\x01",
            "reel 'em in.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_341E")

    Jump("loc_4552")

    label("loc_3423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_35C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_34E6")

    ChrTalk(
        0x9,
        (
            "It's such a pain in the ass to entertain the\x01",
            "diet members when their sessions start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Heh heh heh... Back to business, baby.\x01",
            "Gotta get me a bunch of reservations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BD")

    label("loc_34E6")


    ChrTalk(
        0x9,
        "The diet session's starting pretty soon here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Heh heh heh. Our store is pretty damn good\x01",
            "at entertaining those types of people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "My store's way better than all of those\x01",
            "other flashy-looking places.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_35BD")

    Jump("loc_4552")

    label("loc_35C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_391C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3760")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3677")
    TurnDirection(0x9, 0x11C, 0)

    ChrTalk(
        0x9,
        "Heh. Mighty fine-looking pup you've got there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He yours? Must be nice having him around.\x01",
            "I'm real jealous of ya...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_375C")

    label("loc_3677")

    TurnDirection(0x9, 0x11C, 0)

    ChrTalk(
        0x9,
        "Heh. Mighty-fine looking pup you've got there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He yours? Must be nice having him around.\x01",
            "I'm real jealous of ya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11C,
        "#1203FGrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F(He claims that he is 'not interested in\x01",
            "the likes of you.')\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_375C")

    TalkEnd(0x9)
    Return()

    label("loc_3760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_37FA")

    ChrTalk(
        0x9,
        (
            "Man. Business has already been crappy,\x01",
            "and now a bracer walks in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm freaking out over here. I swear\x01",
            "I'm not a bad person, guys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3917")

    label("loc_37FA")


    ChrTalk(
        0x9,
        (
            "Definitely felt a chill go down my spine\x01",
            "when that bracer walked in earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, guess it was all for nothing. He just\x01",
            "had some work-related business here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Not gonna lie... Even though I don't\x01",
            "think we do anythin' shady here, I\x01",
            "was still freakin' out a little bit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3917")

    Jump("loc_4552")

    label("loc_391C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3A48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3994")

    ChrTalk(
        0x9,
        "Phew... I'm in the ZONE today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Man, there's nothing like being\x01",
            "able to outwit someone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A43")

    label("loc_3994")


    ChrTalk(
        0x9,
        (
            "Managed to drag a chick over from\x01",
            "Bishy's place to my store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Heh. Not like it'll hurt him too badly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Man, there's nothing like being\x01",
            "able to outwit someone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3A43")

    Jump("loc_4552")

    label("loc_3A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3B8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3AC2")

    ChrTalk(
        0x9,
        (
            "Heh heh heh. Customers should be\x01",
            "coming any minute now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Can't afford to slack off today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B87")

    label("loc_3AC2")


    ChrTalk(
        0x9,
        (
            "You there, bro. You've just found\x01",
            "yourself a nice spot to hang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Whaddaya say, bro? You wanna\x01",
            "have some fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I bet you're pretty stressed, too.\x01",
            "Come in, it'll be hella refreshing!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3B87")

    Jump("loc_4552")

    label("loc_3B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3CD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3BEC")

    ChrTalk(
        0x9,
        (
            "Revache & Co. ain't the kind of\x01",
            "folks you should get involved with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CCC")

    label("loc_3BEC")


    ChrTalk(
        0x9,
        (
            "Some group called Heiyue's been\x01",
            "trying to widen their reach lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Revache, by and large, still leads\x01",
            "Crossbell's underworld.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anybody who's ever tried to go against\x01",
            "them has had a less than pleasant time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3CCC")

    Jump("loc_4552")

    label("loc_3CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3E64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3D94")

    ChrTalk(
        0x9,
        (
            "All the best dining spots are gonna be packed\x01",
            "with the diet session starting soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll be making sure all of those big shots\x01",
            "know they can get good drinks here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E5F")

    label("loc_3D94")


    ChrTalk(
        0x9,
        (
            "Hey, bro. You wanna come in and\x01",
            "have some fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Man, we've been seeing a record number\x01",
            "of customers lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I bet it's cause the diet session's coming up.\x01",
            "Ain't that just the best news?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3E5F")

    Jump("loc_4552")

    label("loc_3E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3FFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F4E")

    ChrTalk(
        0xFE,
        (
            "The cops have been questioning\x01",
            "a bunch of people these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had a pair of detectives ask me\x01",
            "all kindsa stuff earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Give me a break. I'm just a barker.\x01",
            "I ain't gonna know anything crazy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3FF8")

    label("loc_3F4E")


    ChrTalk(
        0xFE,
        (
            "This district's been through a lot lately, so the\x01",
            "cops are trying to figure out what's going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No way in Gehenna someone like\x01",
            "me would know anything, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF8")

    Jump("loc_4552")

    label("loc_3FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4133")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_407D")

    ChrTalk(
        0x9,
        (
            "That chick running the ice cream stall is cute.\x01",
            "I'd get her a job if she ever goes out\x01",
            "of business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_412E")

    label("loc_407D")


    ChrTalk(
        0x9,
        "*lick*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Just stocked up on some ice cream from\x01",
            "the stall down that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The girl there is really cute. I'd get her a job\x01",
            "here if she ever went out of business.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_412E")

    Jump("loc_4552")

    label("loc_4133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_423E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_41A4")

    ChrTalk(
        0x9,
        (
            "Don't let Bishy worm his way into your head.\x01",
            "Our place is way better for having fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4239")

    label("loc_41A4")


    ChrTalk(
        0x9,
        (
            "You ever seen that Bishy guy\x01",
            "from the Back Alley?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You could call him my business rival.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't let him worm his\x01",
            "way into your head.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4239")

    Jump("loc_4552")

    label("loc_423E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_435B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4291")

    ChrTalk(
        0x9,
        (
            "Ya think there are any prime customers\x01",
            "out here today?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4356")

    label("loc_4291")


    ChrTalk(
        0x9,
        (
            "Oh, it's almost noon. Figure customers\x01",
            "should be coming pretty soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We have so many patrons, you can\x01",
            "hardly count 'em all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Heh heh. Time for some fun.\x01",
            "Who's gonna come in today?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4356")

    Jump("loc_4552")

    label("loc_435B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_43BE")

    ChrTalk(
        0x9,
        "Our store's pretty close by.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Heh heh. How bout it, bro?\x01",
            "Want some service?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4552")

    label("loc_43BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_444A")

    ChrTalk(
        0xFE,
        (
            "Heh heh. You've come to\x01",
            "the right place, my man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got the booze and girls,\x01",
            "now we just need you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44F0")

    label("loc_444A")


    ChrTalk(
        0x9,
        (
            "Hey, girlie. Get lost. You're crampin'\x01",
            "my style here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 750)

    ChrTalk(
        0xFE,
        (
            "You there, bro. You lookin' for some fun?\x01",
            "We've got the booze and girls, now we\x01",
            "just need you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44F0")


    ChrTalk(
        0x9,
        (
            "Heh heh. Come in and enjoy the\x01",
            "time of your life for the low price\x01",
            "of 1,000 mira an hour.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4552")

    TalkEnd(0xFE)
    Return()

    # Function_12_2E4D end

    def Function_13_4556(): pass

    label("Function_13_4556")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_46A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_45F6")

    ChrTalk(
        0xA,
        (
            "You can't trick me! I'm a true fan!\x01",
            "I know something happened!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I tried asking the receptionist, but\x01",
            "they wouldn't humor me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46A3")

    label("loc_45F6")


    ChrTalk(
        0xA,
        "The troupe's been acting weird since morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I tried asking the receptionist, but\x01",
            "they wouldn't humor me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Why was the afternoon show delayed\x01",
            "for so long?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_46A3")

    Jump("loc_56B4")

    label("loc_46A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_479E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4740")

    ChrTalk(
        0xA,
        (
            "I can usually hear Ilya's heart speak to me,\x01",
            "but it seems to have disappeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "What if something's happened to her?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4799")

    label("loc_4740")


    ChrTalk(
        0xA,
        "#4SMiss Ilya?! Miss Ilyaaa?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Huh, weird. I can't hear anything at all.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_4799")

    Jump("loc_56B4")

    label("loc_479E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4878")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_47E5")

    ChrTalk(
        0xA,
        (
            "Good luck with the performance,\x01",
            "Lady Ilya!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4873")

    label("loc_47E5")


    ChrTalk(
        0xA,
        "Today's show has finally begun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't have a ticket, but that won't stop\x01",
            "me from cheering for Lady Ilya from afar!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x13B, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_4873")

    Jump("loc_56B4")

    label("loc_4878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_48D0")

    ChrTalk(
        0xA,
        (
            "Please come out and bestow upon us\x01",
            "your magnificent wave, Lady Ilya!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56B4")

    label("loc_48D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4A7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4955")

    ChrTalk(
        0xA,
        (
            "The 'Golden Sun, Silver Moon' photo\x01",
            "collection is going on sale today.\x01",
            "I wouldn't miss it for the world!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A75")

    label("loc_4955")


    ChrTalk(
        0xA,
        (
            "Did you guys know? The 'Golden Sun,\x01",
            "Silver Moon' photo collection is going\x01",
            "on sale today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I heard it's supposed to have photos from\x01",
            "the real show-stopping moments and all\x01",
            "kinds of other scenes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I...gotta go. I need to go to Times Department\x01",
            "Store and buy it. Right now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4A75")

    Jump("loc_56B4")

    label("loc_4A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4B55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4ACB")

    ChrTalk(
        0xA,
        "*sigh* I wonder what Lady Ilya is doing right now...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B50")

    label("loc_4ACB")


    ChrTalk(
        0xA,
        "Arc en Ciel's taking a break today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Everyone came out for free practice anyway,\x01",
            "but...Lady Ilya is nowhere to be found!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4B50")

    Jump("loc_56B4")

    label("loc_4B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4BB1")

    ChrTalk(
        0xA,
        (
            "#4SGood luck with practice, Lady Ilya!\x01",
            "I'll be rooting for you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BB4")

    label("loc_4BB1")

    Call(0, 14)

    label("loc_4BB4")

    Jump("loc_56B4")

    label("loc_4BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4C3E")

    ChrTalk(
        0xA,
        "Huh. Lady Ilya slept through practice today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This is a rare event! I'll have to write this\x01",
            "down in my diary!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56B4")

    label("loc_4C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4C8E")

    ChrTalk(
        0xA,
        (
            "Good luck with practice, Lady Ilya!\x01",
            "I'll be rooting for you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56B4")

    label("loc_4C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4E32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4D18")

    ChrTalk(
        0xA,
        "*staaare* I'll be keeping my eye on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm going to flip out on you if I catch\x01",
            "you trying to sneak in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E2D")

    label("loc_4D18")


    ChrTalk(
        0xA,
        (
            "Excuse me...\x01",
            "What were you doing at Arc en Ciel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You're not related to the troupe, right?\x01",
            "You've piqued my interest a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FOh, please don't mind us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FWe're acquainted with a few of the employees.\x01",
            "(Hey, we're technically not lying...right?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4E2D")

    Jump("loc_56B4")

    label("loc_4E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4FEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4ED7")

    ChrTalk(
        0xA,
        (
            "Aww... I thought I'd once again be able\x01",
            "to gaze upon Lady Ilya's visage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've been waiting patiently for this\x01",
            "day to come, and yet!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FE7")

    label("loc_4ED7")


    ChrTalk(
        0xA,
        "#4SAAAARGH! How could I be so stupid?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I accidentally slept through the opening\x01",
            "sales for their newest show!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I rushed out the second I woke up, but it\x01",
            "sold out just ONE person before me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Waaah... You stupid idiot, me!\x01",
            "Now I can't watch Lady Ilya...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4FE7")

    Jump("loc_56B4")

    label("loc_4FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5097")

    ChrTalk(
        0xA,
        (
            "Looks like tickets for Arc en Ciel's new show\x01",
            "are going on sale next week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Heheheheh... I'm drooling just thinking about\x01",
            "getting my hands on them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56B4")

    label("loc_5097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_52A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_517E")

    ChrTalk(
        0xA,
        (
            "Sweet merciful Aidios, Ilya in her training clothes...\x01",
            "All I need now are some great angles of her\x01",
            "new stage dress. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hehehe... I've gotta find an opportunity to\x01",
            "snap some fantastic photos of her!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52A4")

    label("loc_517E")


    ChrTalk(
        0xA,
        "Lady Ilya! Lady Ilyaaa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I now have in my possession...photos of her in\x01",
            "street clothes, her stage dresses, and the\x01",
            "gown she wears in her dressing room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And now, she's got her training clothes on...\x01",
            "I must find the opportunity to take some\x01",
            "photos and add them to my collection!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_52A4")

    Jump("loc_56B4")

    label("loc_52A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_545E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_535C")

    ChrTalk(
        0xA,
        (
            "Lady Ilya will be starring in Arc en Ciel's\x01",
            "latest production!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Aaah! Watch, as I feast upon Lady Ilya's\x01",
            "majestic and gallant figure in the flesh!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5459")

    label("loc_535C")

    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Hey! Did you hear?! Did you hear the\x01",
            "big news?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Arc en Ciel's newest production is going\x01",
            "to be announced soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The tickets are supposedly going on sale\x01",
            "immediately following the announcement!\x01",
            "I HAVE to get me one!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_5459")

    Jump("loc_56B4")

    label("loc_545E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_55E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5500")
    OP_63(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "Wh-Where's Lady Ilya? Is she not coming out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "O-Or maybe, just maybe...she went through\x01",
            "the back exit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55DB")

    label("loc_5500")


    ChrTalk(
        0xA,
        "Lady Ilya has yet to come out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's been my dream to take a picture of\x01",
            "Lady Ilya moments after she finishes\x01",
            "practicing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've thrown down 20,000 whole mira for an orbal\x01",
            "camera to help realize my dream!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_55DB")

    Jump("loc_56B4")

    label("loc_55E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_END)), "loc_5661")

    ChrTalk(
        0xA,
        (
            "Hey, you! Did you happen to see\x01",
            "Lady Ilya inside?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You little sneak! I wanted to cop a look at\x01",
            "her, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56B4")

    label("loc_5661")

    OP_93(0xFE, 0x13B, 0x0)

    ChrTalk(
        0xA,
        (
            "Will I ever get the chance to see Lady Ilya\x01",
            "in her practice outfit...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56B4")

    TalkEnd(0xFE)
    Return()

    # Function_13_4556 end

    def Function_14_56B8(): pass

    label("Function_14_56B8")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "Did you manage to get your hands on\x01",
            "those tickets, Tap?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Nope, no luck. I tried asking some friends\x01",
            "for help, too, but none of them managed\x01",
            "to get any, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, there's only one thing to do during the\x01",
            "Anniversary Festival, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yep, the only thing we CAN do.\x02",
    )

    CloseMessageWindow()

    def lambda_57E1():
        OP_93(0xA, 0x13B, 0x2EE)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_57E1)

    def lambda_57EE():
        OP_93(0xB, 0x13B, 0x2EE)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_57EE)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)

    ChrTalk(
        0xA,
        (
            "#4SWe'll always be thinking about you,\x01",
            "Lady Ilyaaa!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#4SI'll be dreaming about you night and day,\x01",
            "Lady Ilya!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_14_56B8 end

    def Function_15_5880(): pass

    label("Function_15_5880")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_594E")

    ChrTalk(
        0xB,
        (
            "Today's show started awfully late.\x01",
            "Must've been after 4PM by then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The troupe leader and the manager keep\x01",
            "scrambling in and out of the place.\x01",
            "What the heck's going on in there?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_692D")

    label("loc_594E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5A34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_59B7")

    ChrTalk(
        0xB,
        (
            "Today's afternoon show's been delayed\x01",
            "for some odd reason. What's the issue?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A2F")

    label("loc_59B7")


    ChrTalk(
        0xB,
        "Hmm. The troupe's strangely quiet...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Isn't it almost time for the show to start?\x01",
            "What are they even doing?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5A2F")

    Jump("loc_692D")

    label("loc_5A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5B83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5ADA")

    ChrTalk(
        0xB,
        (
            "That one girl was glaring at me while\x01",
            "I was watching Lady Ilya this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Why'd the troupe go and hire such an\x01",
            "unfriendly weirdo?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B7E")

    label("loc_5ADA")


    ChrTalk(
        0xB,
        (
            "I think Arc en Ciel hired a new assistant\x01",
            "sometime recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I get the impression that she's pretty unfriendly,\x01",
            "given that she usually glares at me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5B7E")

    Jump("loc_692D")

    label("loc_5B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5D0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5C13")

    ChrTalk(
        0xB,
        (
            "Isn't it about time they started selling Rixia's\x01",
            "photo collections? I've been waiting for this\x01",
            "day for so, so long!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D05")

    label("loc_5C13")


    ChrTalk(
        0xB,
        (
            "It makes sense that Lady Ilya is nothing short of\x01",
            "perfection, but Rixia is pretty amazing, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I bet if they'd release a solo collection only\x01",
            "featuring Rixia, it'd still sell out crazy fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Can't they put one out already?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5D05")

    Jump("loc_692D")

    label("loc_5D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5EA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5D98")

    ChrTalk(
        0xFE,
        (
            "I'd heard that Rixia Mao's been\x01",
            "performing admirably alongside\x01",
            "Lady Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maaaan! I wanna see her live, too!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EA2")

    label("loc_5D98")


    ChrTalk(
        0xFE,
        (
            "Some girl named Rixia Mao recently\x01",
            "debuted as Lady Ilya's co-star.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From what I've heard, it sounds like she's\x01",
            "pretty darn amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's unlike Lady Ilya, and has a more\x01",
            "lovely, yet refined style of dancing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maaaan! I wanna see her live, too!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5EA2")

    Jump("loc_692D")

    label("loc_5EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5EF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5EEA")

    ChrTalk(
        0xB,
        "#4SWe're your biggest fans, Lady Ilya!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EED")

    label("loc_5EEA")

    Call(0, 14)

    label("loc_5EED")

    Jump("loc_692D")

    label("loc_5EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5FE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5F3F")

    ChrTalk(
        0xB,
        (
            "Who are you guys? Are you new\x01",
            "fans of Lady Ilya?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FDF")

    label("loc_5F3F")


    ChrTalk(
        0xB,
        (
            "Some people in suits went to talk to\x01",
            "the troupe this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think they may have had some business\x01",
            "with them. Their eyes seemed pretty serious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5FDF")

    Jump("loc_692D")

    label("loc_5FE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_6189")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_60C6")

    ChrTalk(
        0xB,
        (
            "Well, even if they do put on shows, I think\x01",
            "a poor student like myself will never have\x01",
            "the chance to watch it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm fine, honest. I'm just happy to marvel at\x01",
            "the theater all lit up in the dark!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6184")

    label("loc_60C6")


    ChrTalk(
        0xB,
        (
            "Arc en Ciel won't be performing a show today.\x01",
            "They're still rehearsing for their newest\x01",
            "production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Don't you just get excited from admiring\x01",
            "the theater all lit up in the dark?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_6184")

    Jump("loc_692D")

    label("loc_6189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6213")

    ChrTalk(
        0xB,
        (
            "That new girl, Rixia, keeps leaving and\x01",
            "coming back for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You think she left a bunch of stuff at home?\x02",
    )

    CloseMessageWindow()
    Jump("loc_692D")

    label("loc_6213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_63F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_635A")

    ChrTalk(
        0xFE,
        (
            "Tickets for Arc en Ciel are going to be\x01",
            "hard to get. Even the B section\x01",
            "seats are really expensive now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hate to say it, but I think I'd better give up\x01",
            "on trying to watch a show this time around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think it's possible for a student like me to\x01",
            "be able to afford those tickets.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_63EB")

    label("loc_635A")


    ChrTalk(
        0xFE,
        (
            "Damn it! I even tried to ask my parents to\x01",
            "help me pay for them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess a student like me can't afford\x01",
            "to go see every performance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63EB")

    Jump("loc_692D")

    label("loc_63F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6438")

    ChrTalk(
        0xB,
        "Hey, Portia. You've got a bit of a dribble going on.\x02",
    )

    CloseMessageWindow()
    Jump("loc_692D")

    label("loc_6438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_64D3")

    ChrTalk(
        0xB,
        (
            "Damn! I sure wish I owned an orbal camera\x01",
            "right about now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Something like that is way too pricey\x01",
            "for a poor student like myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_692D")

    label("loc_64D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_65D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6569")

    ChrTalk(
        0xFE,
        "I come here every morning without fail.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It feels like I may as well pitch up a tent\x01",
            "and camp out here at this point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65CD")

    label("loc_6569")


    ChrTalk(
        0xB,
        (
            "You guys here to get your morning\x01",
            "fill of Lady Ilya, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I'm pretty much her groupie!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_65CD")

    Jump("loc_692D")

    label("loc_65D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_67DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_66B1")

    ChrTalk(
        0xFE,
        (
            "Portia is a fellow comrade in arms over our\x01",
            "love of Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We 'coincidentally' first watched Lady Ilya\x01",
            "dance on stage on that very same day.\x01",
            "We were instantly captivated by her moves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67D5")

    label("loc_66B1")


    ChrTalk(
        0xB,
        (
            "Arc en Ciel's famous even on the\x01",
            "international stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "All of the artists that perform for them\x01",
            "are top notch actors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And above all of them rests Ilya Platiere.\x01",
            "A genius dancer like her only comes\x01",
            "once a century.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I can completely relate to Portia's\x01",
            "enthusiasm over her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_67D5")

    Jump("loc_692D")

    label("loc_67DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_685C")

    ChrTalk(
        0xB,
        (
            "Arc en Ciel usually doesn't let fans\x01",
            "come inside to watch them practice.\x01",
            "All you can do is watch from outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_692D")

    label("loc_685C")


    ChrTalk(
        0xB,
        (
            "Did you guys come to check out the troupe's\x01",
            "practice session as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Fans aren't allowed inside, but you can watch\x01",
            "them for free from the outside. Anyway...\x01",
            "Nice to meet you, my fellow comrades.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_692D")

    TalkEnd(0xFE)
    Return()

    # Function_15_5880 end

    def Function_16_6931(): pass

    label("Function_16_6931")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_69B2")

    ChrTalk(
        0xC,
        (
            "I'm going out for dinner with my family\x01",
            "tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ahaha. It's probably about time for\x01",
            "me to get ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AA1")

    label("loc_69B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6A2C")

    ChrTalk(
        0xC,
        "The main road's pretty quiet today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I get the feeling that there are fewer\x01",
            "orbal cars than usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AA1")

    label("loc_6A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6BDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6AE4")

    ChrTalk(
        0xC,
        (
            "Speaker Hartmann's main opponent is\x01",
            "Representative Campbell...for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I struggle to imagine anyone being able to\x01",
            "overpower Speaker Hartmann for long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BD6")

    label("loc_6AE4")


    ChrTalk(
        0xC,
        (
            "Speaker Hartmann is definitely\x01",
            "a corrupt sleazeball.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Not only is he demeaning to his staff,\x01",
            "he also has connections to Revache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Heh. What an utterly frightening man.\x01",
            "I'd be shaking in my boots if I had to\x01",
            "go up against him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6BD6")

    Jump("loc_7AA1")

    label("loc_6BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6CB0")

    ChrTalk(
        0xC,
        (
            "I heard some rumors about an androgynous-\x01",
            "looking host having worked at the club for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He seems to have disappeared without a trace\x01",
            "after the festival ended, unfortunately...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D9F")

    label("loc_6CB0")


    ChrTalk(
        0xC,
        (
            "I haven't heard much about that young gentleman\x01",
            "these days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "His fashion sense paired with his androgynous\x01",
            "looks immediately shot him up into stardom.\x01",
            "I've never seen a host with cool eyes like his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "*sigh* What a shame.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6D9F")

    Jump("loc_7AA1")

    label("loc_6DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6EC9")

    ChrTalk(
        0xC,
        (
            "Those five long days during the Anniversary\x01",
            "Festival must have worked all of the stall\x01",
            "owners to the bone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ahaha. I guess that also means that\x01",
            "tourists probably spent a ton of money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Crossbell has once again managed to accumulate\x01",
            "mira from all over the continent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AA1")

    label("loc_6EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6F9D")

    ChrTalk(
        0xFE,
        (
            "Between all of the parties, the casinos, watching\x01",
            "live shows, and visiting Mishelam Wonderland...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Holy moly. I've got one heck of a busy festival\x01",
            "ahead of me. Better get a schedule ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AA1")

    label("loc_6F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7058")

    ChrTalk(
        0xC,
        (
            "The Anniversary Festival hasn't even started,\x01",
            "yet tourists are already here to sightsee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I heard that all of the local hotels have\x01",
            "already been completely booked.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AA1")

    label("loc_7058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_70BD")

    ChrTalk(
        0xC,
        "I got invited to go to a party tonight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'd better hurry up and get dressed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AA1")

    label("loc_70BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_71DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7141")

    ChrTalk(
        0xC,
        (
            "I haven't heard much churning in the rumor\x01",
            "mill lately, but I think the crime rate has\x01",
            "increased a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71D7")

    label("loc_7141")


    ChrTalk(
        0xC,
        (
            "I had some police officers stop me to\x01",
            "ask a few questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, boy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I suppose yet another incident has occurred.\x01",
            "What a surprise.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_71D7")

    Jump("loc_7AA1")

    label("loc_71DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_72F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_726F")

    ChrTalk(
        0xC,
        (
            "The power of Arc en Ciel fans never ceases\x01",
            "to amaze me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even I couldn't get my hands on\x01",
            "tickets for the new show.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72F3")

    label("loc_726F")


    ChrTalk(
        0xC,
        (
            "The crowds were insane the day tickets\x01",
            "went up for sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "*sigh* I wasn't able to purchase a ticket.\x01",
            "How disappointing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_72F3")

    Jump("loc_7AA1")

    label("loc_72F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_73AD")

    ChrTalk(
        0xC,
        "Hmm... Where should I have some fun today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Dealing with absurd crowds is a\x01",
            "staple of the Entertainment District.\x01",
            "You can't let the little things bother you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AA1")

    label("loc_73AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_75BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7474")

    ChrTalk(
        0xC,
        (
            "Armorica and Mainz Village are in the\x01",
            "boonies, but St. Ursula Medical College\x01",
            "is different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's a well-renowned medical college that\x01",
            "Crossbellans are familiar with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75B7")

    label("loc_7474")


    ChrTalk(
        0xC,
        (
            "St. Ursula Medical College is a state-of-the-art\x01",
            "medical facility located south of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The difference between St. Ursula and\x01",
            "one of those villages is that it's renowned\x01",
            "among all Crossbellans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It makes sense, though. If you've ever been\x01",
            "badly injured, you were probably treated\x01",
            "at St. Ursula.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_75B7")

    Jump("loc_7AA1")

    label("loc_75BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_76FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_763A")

    ChrTalk(
        0xC,
        "Be wary of barkers like him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "They'll scam you out of your mira if\x01",
            "you get reeled in by them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76F5")

    label("loc_763A")


    ChrTalk(
        0xC,
        (
            "The Back Alley is filled with shady\x01",
            "men like Pim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Try and keep up your guard around them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You slip up for one second, and you're\x01",
            "already on the road to getting scammed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_76F5")

    Jump("loc_7AA1")

    label("loc_76FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_78D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_77C0")

    ChrTalk(
        0xC,
        (
            "The Entertainment District is a popular\x01",
            "international hub for social gatherings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There's a seemingly endless amount of tourists\x01",
            "that come out here to have some fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78D4")

    label("loc_77C0")


    ChrTalk(
        0xC,
        (
            "The Entertainment District is a popular\x01",
            "international hub for social gatherings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "From the casual casino spot, to luxurious\x01",
            "entertainment for the upper echelons of society...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There's a seemingly endless amount of tourists\x01",
            "that come out here to have some fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_78D4")

    Jump("loc_7AA1")

    label("loc_78D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7983")

    ChrTalk(
        0xC,
        (
            "This area conveniently has many casinos,\x01",
            "hotels, and restaurants close by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Are you tourists? You should try and visit\x01",
            "all the sights around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AA1")

    label("loc_7983")


    ChrTalk(
        0xC,
        (
            "Oh, I haven't seen your faces around here\x01",
            "before. Are you tourists?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Are you looking to gamble? There's a casino\x01",
            "nearby. Otherwise, I'd recommend watching\x01",
            "an Arc en Ciel performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There's plenty of good shops in the area.\x01",
            "You should take a look through all of them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7AA1")

    TalkEnd(0xFE)
    Return()

    # Function_16_6931 end

    def Function_17_7AA5(): pass

    label("Function_17_7AA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7B05")

    ChrTalk(
        0xD,
        "Hell yeah! It's nighttime, baby!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I'm gonna party my ass off tonight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CB1")

    label("loc_7B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7B4E")

    ChrTalk(
        0xD,
        "Catching some z's sounds like a good idea...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7BB4")

    label("loc_7B4E")


    ChrTalk(
        0xD,
        (
            "I stayed up all night playing the\x01",
            "slot machine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Urk. Not too surprising I'm this hungry.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7BB4")

    Jump("loc_8CB1")

    label("loc_7BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7CC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7BF2")

    ChrTalk(
        0xD,
        "If only I were that lucky...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CC0")

    label("loc_7BF2")


    ChrTalk(
        0xD,
        (
            "Some guy had an insane stroke of luck\x01",
            "at the casino, and now they say he's\x01",
            "surrounded by riches and bitches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I'm pretty damn jealous of him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I can't believe the level of success\x01",
            "he's had.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7CC0")

    Jump("loc_8CB1")

    label("loc_7CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7DCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7D30")

    ChrTalk(
        0xD,
        (
            "It's impossible to win as much as he has,\x01",
            "but the madman pulled it off anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DC5")

    label("loc_7D30")


    ChrTalk(
        0xD,
        (
            "You guys hear about this yet? Some\x01",
            "guy's been winning a ton of money\x01",
            "at the casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Don't have a clue who he is, but damn,\x01",
            "he's good...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7DC5")

    Jump("loc_8CB1")

    label("loc_7DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7F24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7E43")

    ChrTalk(
        0xD,
        (
            "I feel like hitting up the slot machines today.\x01",
            "Aren't there any DECENT casinos around here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F1F")

    label("loc_7E43")


    ChrTalk(
        0xD,
        "This place is festering with lust and greed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The Anniversary Festival might be over, but the\x01",
            "Entertainment District will always be the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "There's really only one thing you can\x01",
            "do when you come here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7F1F")

    Jump("loc_8CB1")

    label("loc_7F24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_80B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7FBD")

    ChrTalk(
        0xD,
        (
            "Most of Arc en Ciel's sponsors are influential\x01",
            "people and foreign affluents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Everybody's got some fancy-ass orbal cars.\x02",
    )

    CloseMessageWindow()
    Jump("loc_80AC")

    label("loc_7FBD")


    ChrTalk(
        0xD,
        (
            "Sounds like Arc en Ciel's private performance\x01",
            "is happening pretty soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You can catch the occasional glimpse of\x01",
            "their sponsors, and I've gotta say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...they've all got some fancy-ass orbal cars.\x01",
            "I am seething with envy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_80AC")

    Jump("loc_8CB1")

    label("loc_80B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8234")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8145")

    ChrTalk(
        0xD,
        "That Rixia chick sure is a total cutie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "She may have just joined the troupe,\x01",
            "but I can tell she works her ass off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_822F")

    label("loc_8145")


    ChrTalk(
        0xD,
        (
            "Some girl named Rixia is a part of that batch\x01",
            "of people Arc en Ciel just recently hired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "That chick is totally cute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I see her headed to work sometimes, and I can\x01",
            "tell she's busting her ass off to overcome all odds.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_822F")

    Jump("loc_8CB1")

    label("loc_8234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_82C9")

    ChrTalk(
        0xD,
        (
            "The cathedral's bell rings at this hour\x01",
            "every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's pretty common for tourists to come and\x01",
            "listen to its solemn tolling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CB1")

    label("loc_82C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8578")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_83DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8391")

    ChrTalk(
        0xFE,
        (
            "Hey, that limousine... Doesn't it stop by\x01",
            "Arc en Ciel every once in a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I noticed it there last week, too. Sped off\x01",
            "as soon as I noticed it, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_83D8")

    label("loc_8391")


    ChrTalk(
        0xFE,
        (
            "Wonder who owns that thing, 'cause\x01",
            "limousines cost a ton of mira.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83D8")

    Jump("loc_8573")

    label("loc_83DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_END)), "loc_8452")

    ChrTalk(
        0xFE,
        "*whistle* That's one fancy looking ride.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How rich do you have to be to own a limo\x01",
            "like that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8573")

    label("loc_8452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_84DD")

    ChrTalk(
        0xD,
        (
            "That applies to you, too. You should have\x01",
            "booked a hotel way earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "It's probably too late to get one this year.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8573")

    label("loc_84DD")


    ChrTalk(
        0xD,
        (
            "Pretty sure every hotel around here\x01",
            "is already fully booked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Damn, no wonder. It's 'cause the Anniversary\x01",
            "Festival is around the corner.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_8573")

    Jump("loc_8CB1")

    label("loc_8578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_86BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_860F")

    ChrTalk(
        0xD,
        "I wanted to pick up some tickets, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Heh. Definitely don't have the stones to\x01",
            "push my way through those rabid fans.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86B5")

    label("loc_860F")


    ChrTalk(
        0xD,
        (
            "Arc en Ciel's new play is called 'Golden\x01",
            "Sun, Silver Moon.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Tons of fans gathered here for the\x01",
            "announcement. You shoulda seen\x01",
            "how crazy they were going.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_86B5")

    Jump("loc_8CB1")

    label("loc_86BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_86FC")

    ChrTalk(
        0xD,
        "Soooooo... Where am I going to have fun today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CB1")

    label("loc_86FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_88DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_87CF")

    ChrTalk(
        0xD,
        (
            "So apparently, the new management at\x01",
            "Hotel Millennium has made that place\x01",
            "even richer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I think I'll stay in one of their luxury suites\x01",
            "for a night when I go from rags to riches.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88D6")

    label("loc_87CF")


    ChrTalk(
        0xD,
        (
            "You guys hear? Hotel Millennium's\x01",
            "management got changed a couple\x01",
            "years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, apparently, that already-luxury hotel\x01",
            "is raking in even more cash now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I think I'll stay in one of their luxury suites\x01",
            "for a night when I go from rags to riches.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_88D6")

    Jump("loc_8CB1")

    label("loc_88DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8A36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8950")

    ChrTalk(
        0xD,
        (
            "I think Barca's got some pretty good service.\x01",
            "Owner's a bit of a gloomy old man, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A31")

    label("loc_8950")


    ChrTalk(
        0xD,
        "You see Barca Casino over there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Those guys know how to treat a customer right.\x01",
            "The owner bought me some drinks when I\x01",
            "was down in the dumps from losing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You interested? You should check it out,\x01",
            "if you are.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_8A31")

    Jump("loc_8CB1")

    label("loc_8A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8B10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8AAC")

    ChrTalk(
        0xD,
        (
            "Think I'll head to some bar in the Back Alley.\x01",
            "Not many places to eat on the main street.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B0B")

    label("loc_8AAC")


    ChrTalk(
        0xD,
        "Man, I'm friggin' starving.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I usually forget to eat when I'm too busy\x01",
            "having fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_8B0B")

    Jump("loc_8CB1")

    label("loc_8B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8BD3")

    ChrTalk(
        0xD,
        (
            "Crossbell definitely isn't lacking when it\x01",
            "comes to entertainment. That's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I bet you could spend your whole life playing\x01",
            "around, and you'd still never get bored.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CB1")

    label("loc_8BD3")


    ChrTalk(
        0xD,
        "Hell yeah, I'm pumped! It's time to play again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Am I going to challenge the casino? Or, will\x01",
            "I hit up a bar and drink with a hot chick?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No matter what I choose, tonight's going to be\x01",
            "one hell of a night!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_8CB1")

    TalkEnd(0xFE)
    Return()

    # Function_17_7AA5 end

    def Function_18_8CB5(): pass

    label("Function_18_8CB5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8D49")

    ChrTalk(
        0xE,
        "Heeey theeere! Wanna play? ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hmm... What happened to that miner\x01",
            "that usually comes by here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Isn't he coming today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F47")

    label("loc_8D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8DB9")

    ChrTalk(
        0xE,
        "Heeey theeere! Wanna play? ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The Barca Casino is here to\x01",
            "provide you the best service!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F47")

    label("loc_8DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8E39")

    ChrTalk(
        0xE,
        "Heeey theeere! Wanna play? ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh! Will your child be joining you?\x01",
            "Here's a warm welcome to you, too. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F47")

    label("loc_8E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8E97")

    ChrTalk(
        0xE,
        "Heeey theeere! Wanna play? ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "We're offering nice discounts today! ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F47")

    label("loc_8E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8EFA")

    ChrTalk(
        0xE,
        "Heeey theeere! Wanna play? ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Thank you for coming to\x01",
            "the Barca Casino. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F47")

    label("loc_8EFA")


    ChrTalk(
        0xE,
        "Heeey theeere! Wanna play? ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I hope you have a wonderful time. ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_8F47")

    TalkEnd(0xFE)
    Return()

    # Function_18_8CB5 end

    def Function_19_8F4B(): pass

    label("Function_19_8F4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9175")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90DC")

    ChrTalk(
        0xFE,
        (
            "I've gotta work the graveyard shift tonight.\x01",
            "I'm going to head back to headquarters\x01",
            "and take a quick nap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You guys in the middle of an investigation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah. We're going to go to St. Ursula\x01",
            "Medical College for a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sounds like they've got you running everywhere...\x01",
            "Well, I hope we can support each other!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FI hope so, too, Kate.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9170")

    label("loc_90DC")


    ChrTalk(
        0xFE,
        (
            "I've gotta work the graveyard shift tonight.\x01",
            "Uh... Guess I'll go back to headquarters for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I need to pick up dinner, while I'm at it.\x02",
    )

    CloseMessageWindow()

    label("loc_9170")

    Jump("loc_9215")

    label("loc_9175")


    ChrTalk(
        0xFE,
        (
            "What's with all the incidents in the\x01",
            "Entertainment District these days?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if it's because the economy's booming...\x01",
            "We'd better up the patrols.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9215")

    TalkEnd(0xFE)
    Return()

    # Function_19_8F4B end

    def Function_20_9219(): pass

    label("Function_20_9219")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_950C")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        "Hello there, Tio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard this place offers a scrumptious\x01",
            "gelato, but I have my doubts.\x02",
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
        (
            "#0005F(Isn't he from the foundation, Tio?)\x02\x03",
            "(You think we should tell him about Jona?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F(No need. We should keep his secret\x01",
            "hidden for now.)\x02\x03",
            "#0200F(After all, it serves as perfect\x01",
            "blackmail material.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#0303F(Damn, Tio Tot! You just gonna throw him\x01",
            "under the bus if he refuses your every whim?\x01",
            "That's cold. Ice cold.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(There's no question that the children at the\x01",
            "Epstein Foundation are bold. Tio's a\x01",
            "testament to that.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 7)
    Jump("loc_9625")

    label("loc_950C")


    ChrTalk(
        0xFE,
        (
            "I'm currently in the delicate process of\x01",
            "inspecting whether or not this gelato's\x01",
            "quality is as marvelous as I'm told.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But alas, they fail to serve peach...\x01",
            "How will I survive without my peach?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0211F(You appear to have far too much extra\x01",
            "time on your hands, Chief.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9625")

    TalkEnd(0xFE)
    Return()

    # Function_20_9219 end

    def Function_21_9629(): pass

    label("Function_21_9629")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9797")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9647")
    Call(0, 22)
    Jump("loc_9797")

    label("loc_9647")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x13,
        "#6002FO-Oh, wow! This is delicious!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0809FI know, right?!\x01",
            "This stuff's my favorite!\x02\x03",
            "#0806FThere were so many other good\x01",
            "stalls during the festival, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0900FTrue. We really wanted to take\x01",
            "you out to eat then as well.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9788")

    ChrTalk(
        0x101,
        (
            "#0000F(Haha. Sure looks like they're\x01",
            "having a great time.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9788")

    SetScenarioFlags(0x0, 7)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)

    label("loc_9797")

    TalkEnd(0xFE)
    Return()

    # Function_21_9629 end

    def Function_22_979B(): pass

    label("Function_22_979B")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_68(-9790, 3700, 23610, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17250, 0)
    SetChrPos(0x101, -5470, 1990, 19030, 315)
    SetChrPos(0x102, -4390, 1990, 19310, 315)
    SetChrPos(0x103, -4670, 1990, 17970, 315)
    SetChrPos(0x104, -3730, 1990, 18070, 315)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    TurnDirection(0x8, 0x11, 0)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "#0800FOkay, Shizuku. Which flavors do\x01",
            "you want to try?\x02\x03",
            "It's my treat, so order whatever\x01",
            "you want, sweetie!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#6010FN-No, you don't have to pay for me.\x02\x03",
            "You were already nice enough to take\x01",
            "me around while Father's busy, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0809FC'mon, girl! It's fine! Trust me, we love\x01",
            "hanging out with you, so we woulda\x01",
            "done this no matter what!\x02\x03",
            "#0800FIf you're not going to pick anything, then\x01",
            "I'll just order my favorites, 'kay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x8, 500)

    ChrTalk(
        0x11,
        (
            "#0809FExcuse me, miss!\x02\x03",
            "I'll take three! One caramel crunch,\x01",
            "one strawberry cheesecake, and...\x01",
            "one raisin rum!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Here you are. I hope you're ready for\x01",
            "some delicious ice cream!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x13, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x12, 0x13, 350)

    ChrTalk(
        0x12,
        (
            "#0906FSorry about that, Shizuku. Estelle\x01",
            "can be pretty pushy at times.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)

    ChrTalk(
        0x13,
        "#6000FN-No, that's not it. I'm just...so happy.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-7590, 3940, 20060, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19390, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    OP_93(0x11, 0x5A, 0x0)
    OP_93(0x13, 0x10E, 0x0)
    OP_93(0x12, 0x13B, 0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0005F(What's Shizuku doing with\x01",
            "Estelle and Joshua?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100F(It would be rude to interrupt them.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(Indeed. Where has Arios gone, though?\x01",
            "I would have expected him to be in\x01",
            "their position.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -4470, 1990, 19030, 315)
    ModifyEventFlags(0, 4, 0x80)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0xD0, 0)
    EventEnd(0x5)
    Return()

    # Function_22_979B end

    def Function_23_9CFF(): pass

    label("Function_23_9CFF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05200.itc", 0x1E)
    OP_68(-2100, 4610, 34300, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -2000, 2660, 37550, 180)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -1510, 2660, 36550, 180)
    SetChrPos(0x102, -2710, 2660, 36550, 180)
    SetChrPos(0x103, -1310, 2660, 37550, 180)
    SetChrPos(0x104, -2910, 2660, 37550, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01800.itp")
    SetMapObjFlags(0x5, 0x1000)
    FadeToBright(1000, 0)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_68(-2100, 4610, 31380, 4000)
    MoveCamera(34, 29, 0, 4000)
    SetCameraDistance(18000, 4000)

    def lambda_9E66():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E66)

    def lambda_9E80():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9E80)
    Sleep(50)

    def lambda_9E94():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9E94)

    def lambda_9EAE():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9EAE)
    Sleep(50)

    def lambda_9EC2():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFED72, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9EC2)

    def lambda_9EDC():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9EDC)
    Sleep(50)

    def lambda_9EF0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFED72, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9EF0)

    def lambda_9F0A():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9F0A)
    WaitChrThread(0x101, 1)

    def lambda_9F1F():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F1F)
    WaitChrThread(0x102, 1)

    def lambda_9F30():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9F30)
    WaitChrThread(0x103, 1)

    def lambda_9F41():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9F41)
    WaitChrThread(0x104, 1)
    TurnDirection(0x104, 0x101, 500)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#0006F#12PBoy, was that embarrassing. I thought we\x01",
            "could go in there without any issues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F#5PExcuse me, but who exactly is this\x01",
            "Ilya Platiere?\x02\x03",
            "She is stunning.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#0305F#5PWhat?! How could you NOT know who\x01",
            "Ilya Platiere is?!\x02\x03",
            "#0309FMan, you been livin' under a rock all\x01",
            "these years?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F#5PSay that again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102F#6PCalm down, you two. To answer your\x01",
            "question, Tio, she's a bit of a celebrity.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Girl's Voice",
        "#2S#11PThanks. I'll see you tomorrow.\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)

    def lambda_A185():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF15A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A185)

    def lambda_A19F():
        OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_A19F)
    WaitChrThread(0x18, 1)

    def lambda_A1B4():
        TurnDirection(0x101, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A1B4)

    def lambda_A1C1():
        TurnDirection(0x102, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A1C1)

    def lambda_A1CE():
        TurnDirection(0x103, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A1CE)

    def lambda_A1DB():
        TurnDirection(0x104, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A1DB)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("Purple-Haired Girl")

    AnonymousTalk(
        0xFF,
        "Oh, pardon me!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#0002F#12PNo, it was our fault. We shouldn't have\x01",
            "been standing in your way.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A2D5():
        OP_98(0x101, 0xFA, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A2D5)

    def lambda_A2EF():
        OP_98(0x102, 0xFFFFFF06, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A2EF)

    def lambda_A309():
        OP_98(0x103, 0xFA, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A309)

    def lambda_A323():
        OP_98(0x104, 0xFFFFFF06, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A323)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    NpcTalk(
        0x18,
        "Purple-Haired Girl",
        "#1804F#5PIt's okay. Have a nice day.\x02",
    )

    CloseMessageWindow()

    def lambda_A38A():

        label("loc_A38A")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_A38A")

    QueueWorkItem2(0x0, 1, lambda_A38A)

    def lambda_A39C():

        label("loc_A39C")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_A39C")

    QueueWorkItem2(0x1, 1, lambda_A39C)

    def lambda_A3AE():

        label("loc_A3AE")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_A3AE")

    QueueWorkItem2(0x2, 1, lambda_A3AE)

    def lambda_A3C0():

        label("loc_A3C0")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_A3C0")

    QueueWorkItem2(0x3, 1, lambda_A3C0)
    OP_95(0x18, -2110, 1760, 28460, 3000, 0x0)
    Fade(500)
    OP_68(430, 4610, 28350, 0)
    MoveCamera(53, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(28910, 0)
    OP_95(0x18, -1750, 1990, 23060, 3000, 0x0)
    OP_95(0x18, 7100, 1770, 15210, 3000, 0x0)
    Fade(800)
    OP_68(-2100, 4610, 31380, 0)
    MoveCamera(34, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    OP_0D()
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)

    ChrTalk(
        0x104,
        "#0300F#5PHuh. She from the troupe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F#5PI've never seen her face before, though.\x01",
            "Is she a new member?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x1000)
    OP_68(-2110, 4610, 31550, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x0, -2110, 2660, 31550, 180)
    SetChrPos(0x1, -2110, 2660, 31550, 180)
    SetChrPos(0x2, -2110, 2660, 31550, 180)
    SetChrPos(0x3, -2110, 2660, 31550, 180)
    ModifyEventFlags(1, 2, 0x80)
    SetScenarioFlags(0x46, 4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_23_9CFF end

    def Function_24_A5A8(): pass

    label("Function_24_A5A8")

    EventBegin(0x0)
    Fade(500)
    OP_68(-2110, 4610, 31550, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x0, -2110, 2660, 31550, 180)
    SetChrPos(0x1, -2110, 2660, 31550, 180)
    SetChrPos(0x2, -2110, 2660, 31550, 180)
    SetChrPos(0x3, -2110, 2660, 31550, 180)
    ModifyEventFlags(1, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_24_A5A8 end

    def Function_25_A629(): pass

    label("Function_25_A629")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A6BD")
    Jump("loc_A707")

    label("loc_A6BD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A6DD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A707")

    label("loc_A6DD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6FD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A707")

    label("loc_A6FD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A707")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_A8AA")

    ChrTalk(
        0x14,
        (
            "#0106FMy experiences with the vice commissioner have\x01",
            "been less than pleasant, much like the words\x01",
            "that come out of his mouth.\x02\x03",
            "#0100FAnyway, I can't imagine he's in a good state\x01",
            "right now. Between being henpecked, and being\x01",
            "prone to getting blackout drunk, he must have\x01",
            "a lot on his plate.\x02\x03",
            "#0105FYou two aren't too tired, are you? We can\x01",
            "stop searching for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA13")

    label("loc_A8AA")


    ChrTalk(
        0x14,
        "#0100FSo, how's the investigation treating you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha... It's going.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FZeit's nose is accurate as always, but the\x01",
            "unpredictability of the vice commissioner\x01",
            "is making the search nigh impossible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#0106FThen it's as we feared. This very well\x01",
            "may take a long time.\x02\x03",
            "#0100FI think it's fine to stop if you're too\x01",
            "tired to continue.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_AA13")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Continue searching.]\x01",      # 0
            "[Stop for now.]\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB73")

    ChrTalk(
        0x101,
        "#0006FI'm beat. How about we pick this up later?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FAn agreeable decision.\x02\x03",
            "#0200FLet us once again rely on Zeit when\x01",
            "we resume the search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#0100FOkay. Let's grab Randy and head back\x01",
            "to the SSS building.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x95, 7)
    OP_29(0x15, 0x1, 0x2)
    SetScenarioFlags(0x5E, 1)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_ABA7")

    label("loc_AB73")


    ChrTalk(
        0x14,
        "#0100FI see. Well, try not to overdo it, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_ABA7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_A629 end

    def Function_26_ABAF(): pass

    label("Function_26_ABAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-26820, 1750, 11890, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17650, 0)
    SetChrPos(0x103, -26000, 0, 12000, 180)
    SetChrPos(0x11C, -25000, 0, 11000, 180)
    SetChrPos(0x101, -27000, 0, 12250, 180)
    SetChrPos(0x102, -26000, 0, 13500, 180)
    SetChrPos(0x104, -27000, 0, 13750, 180)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_AE68")

    def lambda_AC68():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AC68)

    def lambda_AC75():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AC75)

    def lambda_AC82():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AC82)

    def lambda_AC8F():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AC8F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#6P#0000FAll right, let's pick up where we left off!\x02\x03",
            "Elie, Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309FNo worries! I'll be on standby.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 1, 0, 27)

    def lambda_AD25():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD25)

    def lambda_AD32():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD32)

    def lambda_AD3F():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AD3F)

    def lambda_AD4C():
        OP_93(0x11C, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11C, 1, lambda_AD4C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x11C, 1)
    WaitChrThread(0x104, 1)
    Sleep(400)

    def lambda_AD70():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD70)

    def lambda_AD7D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD7D)

    def lambda_AD8A():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AD8A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x102,
        (
            "#0100FI'll be waiting on standby over by\x01",
            "that food cart.\x02\x03",
            "Good luck, you two.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_AE21")
    OP_1B(0x1, 0x0, 0x24)
    OP_1B(0x2, 0x0, 0x25)
    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x4, 0x0, 0x27)
    OP_1B(0x5, 0x0, 0x28)
    OP_1B(0x6, 0x0, 0x29)
    Jump("loc_AE60")

    label("loc_AE21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_AE60")
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    OP_1B(0x0, 0x0, 0x23)
    OP_1B(0x1, 0x0, 0x24)
    OP_1B(0x2, 0x0, 0x25)
    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x5, 0x0, 0x28)
    OP_1B(0x6, 0x0, 0x29)

    label("loc_AE60")

    ClearScenarioFlags(0x95, 7)
    Jump("loc_B5C4")

    label("loc_AE68")


    ChrTalk(
        0x101,
        (
            "#6P#0001FOkay... Which direction did the\x01",
            "vice commissioner go from here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11C,
        "#11P#1200F*sniff* *sniff*...\x02",
    )

    CloseMessageWindow()
    OP_93(0x11C, 0x5A, 0x1F4)

    ChrTalk(
        0x11C,
        "#11P#1200FGrrrrr...\x02",
    )

    CloseMessageWindow()

    def lambda_AEFD():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AEFD)
    Sleep(50)

    def lambda_AF0D():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF0D)
    Sleep(50)

    def lambda_AF1D():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AF1D)
    Sleep(50)

    def lambda_AF2D():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AF2D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x103,
        "#11P#0200FEast, he says.\x02",
    )

    CloseMessageWindow()

    def lambda_AF68():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF68)

    def lambda_AF75():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF75)

    def lambda_AF82():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AF82)

    def lambda_AF8F():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AF8F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#12P#0004FGreat. Let's try retracing his steps\x01",
            "using Zeit's nose.\x02\x03",
            "#0000FWe have to be careful not to miss\x01",
            "his ring while we're walking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0105FHey, Lloyd. Don't you think it's inefficient for the\x01",
            "four of us to search together?\x02\x03",
            "#0100FWe're talking about the entire district, here.\x01",
            "Wouldn't it make more sense to have Zeit narrow\x01",
            "down the location first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FAh, yeah. Wouldn't want to waste our energy.\x02\x03",
            "#0000FElie, Randy. You two mind waiting on standby\x01",
            "for now?\x02\x03",
            "After Tio and I have narrowed down the\x01",
            "ring's location, we'll come get you.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x0, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#5P#0304FSounds like a plan to me, my man.\x02\x03",
            "Now... What's this place got in store for\x01",
            "#0309FRandy today?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 1, 0, 27)

    def lambda_B25D():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B25D)

    def lambda_B26A():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B26A)

    def lambda_B277():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B277)

    def lambda_B284():
        OP_93(0x11C, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11C, 1, lambda_B284)

    ChrTalk(
        0x101,
        "#12P#0005FW-Wait...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x11C, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x103,
        "#11P#0211FHe immediately seized the opportunity.\x02",
    )

    CloseMessageWindow()

    def lambda_B2F4():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B2F4)

    def lambda_B301():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B301)

    def lambda_B30E():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B30E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x102,
        (
            "#11P#0106FThere's no point in trying to change him...\x02\x03",
            "#0100FAnyway, just give me a ring on the Enigma\x01",
            "once you're ready, okay?\x02\x03",
            "I'll be waiting on standby over by\x01",
            "that food cart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FThanks, Elie.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    ChrTalk(
        0x102,
        "#5P#0100FOf course. See you later, everyone.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 28)
    BeginChrThread(0x103, 1, 0, 28)
    BeginChrThread(0x11C, 1, 0, 28)
    OP_97(0x102, 0x7D0, 0x0, 0x0, 0x7D0, 0x1)
    OP_97(0x102, 0x7D0, 0x0, 0xFFFFF830, 0x7D0, 0x1)
    OP_97(0x102, 0xBB8, 0x0, 0x0, 0x7D0, 0x1)
    OP_97(0x102, 0x1F40, 0x0, 0x1770, 0x7D0, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x11C, 0x1)

    def lambda_B4A3():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B4A3)

    def lambda_B4B0():
        OP_93(0x11C, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11C, 1, lambda_B4B0)
    Sleep(50)

    def lambda_B4C0():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B4C0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x11C, 1)

    ChrTalk(
        0x103,
        "#11P#0200FShall we begin, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FYep. Let's do this.\x02\x03",
            "Remember, Zeit. We'll be walking ahead\x01",
            "of you, so make sure we don't take any\x01",
            "wrong turns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11C,
        "#11P#1200FWoof!\x02",
    )

    CloseMessageWindow()
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    OP_1B(0x0, 0x0, 0x23)
    OP_1B(0x1, 0x0, 0x24)
    OP_1B(0x2, 0x0, 0x25)
    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x5, 0x0, 0x28)
    OP_1B(0x6, 0x0, 0x29)
    OP_29(0x15, 0x1, 0x1)

    label("loc_B5C4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    OP_49()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)
    OP_68(-26500, 1950, 12000, 0)
    MoveCamera(40, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -26500, 0, 12000, 180)
    SetChrPos(0x103, -26500, 0, 12000, 180)
    SetChrPos(0x11C, -26500, 0, 12000, 180)
    ClearChrFlags(0x14, 0x80)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x10, 0x80)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_26_ABAF end

    def Function_27_B696(): pass

    label("Function_27_B696")

    OP_97(0x104, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x1)

    def lambda_B6CA():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B6CA)
    OP_97(0x104, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    Return()

    # Function_27_B696 end

    def Function_28_B706(): pass

    label("Function_28_B706")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B720")
    TurnDirection(0xFE, 0x102, 500)
    Sleep(100)
    Jump("Function_28_B706")

    label("loc_B720")

    Return()

    # Function_28_B706 end

    def Function_29_B721(): pass

    label("Function_29_B721")

    TalkBegin(0xFF)

    ChrTalk(
        0x11C,
        (
            "#1200F*sniff*...*sniff*\x02\x03",
            "Woof!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FAre we going the right way, Zeit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FIt appears so.\x02\x03",
            "Let us continue.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x15, 0x1, 0x3)
    TalkEnd(0xFF)
    Return()

    # Function_29_B721 end

    def Function_30_B7AB(): pass

    label("Function_30_B7AB")

    TalkBegin(0xFF)

    ChrTalk(
        0x11C,
        (
            "#1200F*sniff*...*sniff*\x02\x03",
            "Woof!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FYou smell something, Zeit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FIt appears the vice commissioner briefly\x01",
            "stopped here for a rest.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x15, 0x1, 0x4)
    TalkEnd(0xFF)
    Return()

    # Function_30_B7AB end

    def Function_31_B84F(): pass

    label("Function_31_B84F")

    TalkBegin(0xFF)

    ChrTalk(
        0x11C,
        (
            "#1200F*sniff*...*sniff*\x02\x03",
            "Grrrrr...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FIs this way a bust, Zeit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FCorrect. The scent appears to trail off\x01",
            "in that direction.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_31_B84F end

    def Function_32_B8E9(): pass

    label("Function_32_B8E9")

    TalkBegin(0xFF)

    ChrTalk(
        0x11C,
        (
            "#1200F*sniff*...*sniff*\x02\x03",
            "Grrrrr...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FNo good?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FZeit does not seem to think he went\x01",
            "that way.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_32_B8E9 end

    def Function_33_B965(): pass

    label("Function_33_B965")

    TalkBegin(0xFF)

    ChrTalk(
        0x11C,
        (
            "#1200F*sniff*...*sniff*\x02\x03",
            "Grrrrr...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FIsn't this...the wrong way?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FZeit seems to think so.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_33_B965 end

    def Function_34_B9DE(): pass

    label("Function_34_B9DE")

    TurnDirection(0x11C, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_BA40")

    ChrTalk(
        0x11C,
        "#1200FWoof! Woof!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(Doesn't look like this is the right way.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_BABA")

    label("loc_BA40")


    ChrTalk(
        0x11C,
        "#1200FWoof! Woof!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FNot this way, either?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FZeit agrees.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_BABA")

    Return()

    # Function_34_B9DE end

    def Function_35_BABB(): pass

    label("Function_35_BABB")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, 13270, 0, -19100, 315)
    EventEnd(0x4)
    Return()

    # Function_35_BABB end

    def Function_36_BAD7(): pass

    label("Function_36_BAD7")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, 20770, 0, 12930, 270)
    EventEnd(0x4)
    Return()

    # Function_36_BAD7 end

    def Function_37_BAF3(): pass

    label("Function_37_BAF3")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, -39280, 0, 12420, 90)
    EventEnd(0x4)
    Return()

    # Function_37_BAF3 end

    def Function_38_BB0F(): pass

    label("Function_38_BB0F")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, -2110, 2660, 34550, 180)
    EventEnd(0x4)
    Return()

    # Function_38_BB0F end

    def Function_39_BB2B(): pass

    label("Function_39_BB2B")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, 17100, 2060, 23000, 270)
    EventEnd(0x4)
    Return()

    # Function_39_BB2B end

    def Function_40_BB47(): pass

    label("Function_40_BB47")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, 13690, 90, -6130, 270)
    EventEnd(0x4)
    Return()

    # Function_40_BB47 end

    def Function_41_BB63(): pass

    label("Function_41_BB63")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0003FWe have no reason to be at the casino\x01",
            "right now. Let's try our luck elsewhere.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -26470, 300, 16370, 180)
    EventEnd(0x4)
    Return()

    # Function_41_BB63 end

    def Function_42_BBD6(): pass

    label("Function_42_BBD6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(12420, 1000, -5920, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x11C, 11520, 0, -5920, 270)
    SetChrPos(0x103, 12100, 0, -5140, 270)
    SetChrPos(0x101, 12680, 0, -6570, 270)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x103)

    ChrTalk(
        0x101,
        (
            "#11P#0005FThe vice commissioner cut through the hotel\x01",
            "after getting drunk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#0206FTypical behavior for a drunkard.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#11P#0000FYeah, but it doesn't look like he\x01",
            "dropped anything in there.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11C, 0xB4, 0x1F4)

    ChrTalk(
        0x11C,
        "#6P#1200FGrrrrr... Woof!\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_93(0x103, 0xB4, 0x2EE)
    Sleep(750)

    ChrTalk(
        0x103,
        "#5P#0200FZeit claims that he went south next.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x2EE)

    ChrTalk(
        0x101,
        "#11P#0000FSouth we go, then.\x02",
    )

    CloseMessageWindow()
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0x0, 0x24)
    OP_1B(0x2, 0x0, 0x25)
    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x4, 0x0, 0x27)
    OP_1B(0x5, 0x0, 0x28)
    OP_1B(0x6, 0x0, 0x29)
    SetChrPos(0x0, 11520, 0, -5920, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_29(0x15, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_42_BBD6 end

    def Function_43_BE76(): pass

    label("Function_43_BE76")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    LoadChrToIndex("chr/ch34600.itc", 0x1E)
    LoadChrToIndex("chr/ch32400.itc", 0x1F)
    LoadChrToIndex("chr/ch34300.itc", 0x20)
    LoadChrToIndex("chr/ch32200.itc", 0x21)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x1B, -1900, 1990, 20550, 180)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    SetChrPos(0x1C, -1900, 1990, 17860, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, -3280, 1990, 18520, 45)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -590, 1990, 18520, 315)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetMapObjFlags(0x5, 0x1000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-26220, 4050, 12750, 0)
    MoveCamera(32, 14, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15680, 0)
    FadeToBright(1000, 0)
    OP_68(13510, 1950, -6620, 7000)
    MoveCamera(56, 21, 0, 7000)
    OP_6E(800, 7000)
    SetCameraDistance(16000, 7000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-1890, 8610, 32520, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(25500, 0)
    OP_68(-2990, 3940, 18300, 8000)
    MoveCamera(41, 29, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(39500, 8000)
    PlaceName2(340, 200, "c_plac07", 0x0, 4000)
    OP_6F(0x79)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C680")

    AnonymousTalk(
        0x101,
        "#0005FHmm? What's that over there?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetCameraDistance(15000, 0)
    OP_0D()

    ChrTalk(
        0x1C,
        "#12POh, wow! This is amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#6PThis is home to the continent-renowned\x01",
            "theatre troupe, Arc en Ciel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#11POh, yeah. I've heard their tickets can\x01",
            "be ridiculously expensive, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5PIs everybody enjoying themselves? \x01",
            "Time for the next stop on our tour!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x5A, 0x1F4)
    OP_63(0x1D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_C1D1():
        OP_95(0xFE, -160, 1990, 19900, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_C1D1)
    Sleep(500)

    ChrTalk(
        0x1D,
        (
            "#6PAw, man. Can't we go inside and watch\x01",
            "one of their performances?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1B, 1)
    OP_93(0x1B, 0xE1, 0x1F4)

    ChrTalk(
        0x1B,
        (
            "#11PSorry to burst your bubble, but their\x01",
            "only show today is later in the evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11PYou can spend the night however you'd like.\x01",
            "If you're a fan or simply interested, I would\x01",
            "wholeheartedly recommend you stop by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#11POkay, everyone. Allow me to lead\x01",
            "you to our next destination.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C36A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_C36A)

    def lambda_C377():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_C377)

    def lambda_C384():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_C384)

    def lambda_C391():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_C391)
    WaitChrThread(0x1B, 1)

    def lambda_C3A2():
        OP_95(0xFE, 6940, 1760, 13750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_C3A2)
    Sleep(1000)
    WaitChrThread(0x1E, 1)

    def lambda_C3C3():
        OP_95(0xFE, 6940, 1760, 13750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_C3C3)
    Sleep(500)
    WaitChrThread(0x1C, 1)

    def lambda_C3E4():
        OP_95(0xFE, 6940, 1760, 13750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_C3E4)
    Sleep(300)
    WaitChrThread(0x1D, 1)

    def lambda_C405():
        OP_95(0xFE, 6940, 1760, 13750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_C405)
    WaitChrThread(0x1B, 1)

    def lambda_C423():
        OP_95(0xFE, 22200, 0, 12150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_C423)
    WaitChrThread(0x1E, 1)

    def lambda_C441():
        OP_95(0xFE, 22200, 0, 12150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_C441)
    WaitChrThread(0x1C, 1)

    def lambda_C45F():
        OP_95(0xFE, 22200, 0, 12150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_C45F)
    WaitChrThread(0x1D, 1)

    def lambda_C47D():
        OP_95(0xFE, 22200, 0, 12150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_C47D)

    AnonymousTalk(
        0x104,
        (
            "#0300FI like comin' out here to chill. Been a helluva\x01",
            "lot of tourists lately, though.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#0000FMore tourists have been coming here thanks\x01",
            "to how convenient the bus lines are.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#0104FThe Entertainment District has a lot to offer,\x01",
            "so that makes it one of the more popular\x01",
            "spots for them to visit.\x02\x03",
            "#0100FThat's why our work is of such importance.\x01",
            "If something were to happen to them,\x01",
            "it could snowball into an international crisis.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        "#0200FA suboptimal situation, I would think.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C680")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Entertainment District is a commercial\x01",
            "area in the northern part of the city.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Its various casinos, hotels, and theaters\x01",
            "attract an incredible amount of tourists.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Though not all of them may be accessible yet,\x01",
            "you should try visiting them as you progress\x01",
            "through the story.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearMapObjFlags(0x5, 0x1000)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrPos(0xC, -50000, 10, 12070, 220)
    BeginChrThread(0xC, 0, 0, 2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8C5")
    OP_68(21040, 1950, 11840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17500, 0)
    Jump("loc_C942")

    label("loc_C8C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C906")
    OP_68(13270, 1950, -19100, 0)
    MoveCamera(40, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)
    Jump("loc_C942")

    label("loc_C906")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C942")
    OP_68(-39280, 1950, 12420, 0)
    MoveCamera(40, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)

    label("loc_C942")

    SetScenarioFlags(0x45, 0)
    EventEnd(0x5)
    Return()

    # Function_43_BE76 end

    def Function_44_C948(): pass

    label("Function_44_C948")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-13000, 7940, 33500, 0)
    MoveCamera(40, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -2700, 1990, 21500, 0)
    SetChrPos(0x104, -1300, 1990, 21500, 0)
    SetChrPos(0x103, -2700, 1990, 20300, 0)
    SetChrPos(0x102, -1300, 1990, 20300, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_68(4000, 7940, 33500, 6000)
    MoveCamera(40, 13, 0, 6000)
    SetCameraDistance(30000, 6000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(-2000, 11940, 34000, 0)
    MoveCamera(31, -13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(28000, 0)
    MoveCamera(21, -13, 0, 9000)
    SetCameraDistance(37000, 9000)
    PlaceName2(340, 200, "c_plac11", 0x0, 5000)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(-2000, 2740, 24500, 0)
    MoveCamera(32, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(19950, 0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#2100387V#4P#0202FUpon further inspection, the architecture\x01",
            "of this building is magnificent.\x02\x03",
            "#2100388VIts appearance is quite modern, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100389V#0104FThat's because it was built in\x01",
            "the last twenty years.\x02\x03",
            "#2100390V#0100FIt's fairly new compared to some of\x01",
            "our older buildings, like City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100391V#6P#0003F(Arc en Ciel...)\x02\x03",
            "#2100392V#0008F(Back when I was a kid, Guy and Cecile would\x01",
            "bring me here every so often.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        "#2100393V#0305F#11PMajesty of it gettin' to you, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100394V#6P#0004FNo, not really.\x02\x03",
            "#2100395V#0000FSo, are we all ready to head inside?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -2000, 1990, 19500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    SetScenarioFlags(0x80, 3)
    EventEnd(0x5)
    Return()

    # Function_44_C948 end

    def Function_45_CD7B(): pass

    label("Function_45_CD7B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-2000, 3760, 35000, 0)
    MoveCamera(25, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -2700, 2660, 35500, 180)
    SetChrPos(0x102, -1300, 2660, 35500, 180)
    SetChrPos(0x103, -2700, 2660, 36900, 180)
    SetChrPos(0x104, -1300, 2660, 36900, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetMapObjFlags(0x5, 0x1000)
    FadeToBright(1000, 0)
    Sleep(500)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_68(-2000, 2860, 27500, 5000)
    MoveCamera(45, 27, 0, 5000)
    SetCameraDistance(18000, 5000)

    def lambda_CE90():
        OP_96(0xFE, 0xFFFFF574, 0x6E0, 0x68B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CE90)

    def lambda_CEAA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CEAA)
    Sleep(250)

    def lambda_CEBE():
        OP_96(0xFE, 0xFFFFFAEC, 0x6E0, 0x68B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CEBE)

    def lambda_CED8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CED8)
    Sleep(100)

    def lambda_CEEC():
        OP_96(0xFE, 0xFFFFF574, 0x6E0, 0x6E28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CEEC)

    def lambda_CF06():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CF06)
    Sleep(250)

    def lambda_CF1A():
        OP_96(0xFE, 0xFFFFFAEC, 0x6E0, 0x6E28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CF1A)

    def lambda_CF34():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CF34)
    Sleep(1000)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    WaitChrThread(0x101, 1)

    def lambda_CF67():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CF67)
    WaitChrThread(0x102, 1)

    def lambda_CF78():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CF78)
    WaitChrThread(0x103, 1)

    def lambda_CF89():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CF89)
    WaitChrThread(0x104, 1)

    def lambda_CF9A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CF9A)
    WaitChrThread(0x104, 2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#2100611V#5P#0303FWhat's the plan, then?\x02\x03",
            "#2100612V#0301FAt least Revache is lookin' like\x01",
            "a potential lead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100613V#0200FYin appears to bear some\x01",
            "significance as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100614V#6P#0008F...I have an idea.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#2100615V#6P#0003FHear me out, everyone.\x02\x03",
            "#2100616V#0013FWhy don't we pay Revache & Co.\x01",
            "a little visit?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_D162():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D162)
    Sleep(50)

    def lambda_D172():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D172)
    Sleep(50)

    def lambda_D182():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D182)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x102,
        "#2100617V#0105F#11PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100618V#5P#0301FYou feelin' all right, buddy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100619V#6P#0000FIsn't it our obligation as police officers to\x01",
            "question any possible lead?\x02\x03",
            "#2100620V#0003FWe still don't know if Revache's don is\x01",
            "responsible for sending the letter, but...\x02\x03",
            "#2100621V#0001F...I know for a fact that we'll never reach the\x01",
            "truth if we shy away from potential trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100622V#5P#0303FWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100623V#0201F#5PYou make a valid point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100624V#6P#0006FNot only that, but I think it'll be a\x01",
            "good opportunity.\x02\x03",
            "#2100625V#0008FThey're a group of criminals that think\x01",
            "they're above the law.\x02\x03",
            "#2100626V#0013FThis is a chance to see the true nature\x01",
            "of Crossbell's underworld for ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100627V#5P#0302FThat makes sense.\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D4E4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D4E4)
    Sleep(50)

    def lambda_D4F4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D4F4)
    Sleep(50)

    def lambda_D504():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D504)
    Sleep(300)
    OP_64(0x102)

    ChrTalk(
        0x101,
        (
            "#2100628V#6P#0005FUh, are you worried or something?\x02\x03",
            "#2100629V#0000FWell, Randy and I could always go alo--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        "#2100630V#0211F#5PWhat are you implying, Lloyd?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#2100631V#6P#0011FI-I wasn't implying anything!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100632V#0104F#11PWe'd love to join you. And besides,\x01",
            "I'm not particularly worried.\x02\x03",
            "#2100633V#0108FI don't see the harm in going to\x01",
            "ask them a few questions.\x02\x03",
            "#2100634VJust who are the people that make up\x01",
            "the city's infamous mafia?\x02\x03",
            "#2100635V#0102FI'm interested in finding out.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D72C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D72C)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x101,
        "#2100636V#6P#0005FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100637V#5P#0305FYou're soundin' pretty eager there,\x01",
            "Mademois-Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100638V#0104F#11PYou're imagining it.\x02\x03",
            "#2100639V#0100FAfter all, life is full of surprises. Doubly\x01",
            "so for our current case. Who knows what\x01",
            "information we'll unveil about the letter?\x02\x03",
            "#2100640VWe should go visit them right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100641V#6P#0000FAgreed!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100642V#0203F#5PAccording to the database...\x02\x03",
            "#2100643V#0201F...Revache's headquarters lies deep within the\x01",
            "Back Alley. There is a narrower alleyway halfway\x01",
            "down the street that leads to its front doors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100644V#5P#0304FThat shady-lookin' place, right?\x02\x03",
            "#2100645V#0300FYeah, pretty sure some mean-lookin' dudes\x01",
            "stand guard down there. Heh. All makes\x01",
            "sense now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18150, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -2000, 1760, 26500, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearMapObjFlags(0x5, 0x1000)
    SetScenarioFlags(0x80, 6)
    OP_29(0x42, 0x1, 0x3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_45_CD7B end

    def Function_46_DA79(): pass

    label("Function_46_DA79")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02500.itp")
    OP_68(-2000, 3000, 20500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -1500, 1990, 16500, 0)
    SetChrPos(0x102, -2700, 1990, 16500, 0)
    SetChrPos(0x103, -2700, 1990, 15300, 0)
    SetChrPos(0x104, -1500, 1990, 15300, 0)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, -2000, 2660, 36000, 180)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x16, -2600, 2660, 36000, 180)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x4, 0x17)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x17, -5300, 0, 1800, 100)
    OP_D3(0x17, 0x0, 0x186A0, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_70(0x4, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    SetMapObjFlags(0x5, 0x1000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)

    def lambda_DC40():
        OP_96(0xFE, 0xFFFFF574, 0x7C6, 0x5014, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DC40)
    Sleep(50)

    def lambda_DC5D():
        OP_96(0xFE, 0xFFFFFA24, 0x7C6, 0x5014, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DC5D)
    Sleep(50)

    def lambda_DC7A():
        OP_96(0xFE, 0xFFFFF574, 0x7C6, 0x4B64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DC7A)
    Sleep(50)

    def lambda_DC97():
        OP_96(0xFE, 0xFFFFFA24, 0x7C6, 0x4B64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DC97)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2101235V#11P#0005F...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_68(-2000, 3600, 32000, 2000)
    OP_6F(0x1)

    def lambda_DD63():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_DD63)

    def lambda_DD74():
        OP_95(0xFE, -2000, 2660, 31800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_DD74)
    Sleep(500)

    def lambda_DD91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_DD91)

    def lambda_DDA2():
        OP_95(0xFE, -2600, 2660, 32500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_DDA2)
    Sleep(700)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)

    ChrTalk(
        0x102,
        "#2101236V#0105F#1P(Oh, no...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Elderly Man",
        "#2101237V#2505F#5POh? What a surprise!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x16,
        "Young Man",
        "#2101238V#2605F#5PGood afternoon, Elie!\x02",
    )

    CloseMessageWindow()

    def lambda_DE9E():
        OP_95(0xFE, -2000, 1990, 24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_DE9E)
    Sleep(250)

    def lambda_DEBB():
        OP_96(0xFE, 0xFFFFF574, 0x7C6, 0x607C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_DEBB)
    Sleep(2000)
    Fade(500)
    OP_68(-2000, 3000, 22800, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x102, -2000, 1990, 21000, 0)
    SetChrPos(0x101, 100, 1990, 21200, 315)
    SetChrPos(0x103, -1500, 1990, 20200, 0)
    SetChrPos(0x104, -700, 1990, 19600, 0)
    SetCameraDistance(19000, 2000)
    OP_0D()
    Sleep(600)

    def lambda_DF5C():
        OP_95(0xFE, -2000, 1990, 21700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DF5C)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x102, 1)
    OP_6F(0x10)

    ChrTalk(
        0x102,
        "#2101239V#0105F#12PHello, Grandfather. Ernest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101240V#0005F(Did I hear her right?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101241V#0205F#4P(This man is Elie's grandfather?)\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Elderly Man")

    AnonymousTalk(
        0xFF,
        (
            "#2101242VIt's a shame that I haven't seen\x01",
            "you recently. You look well.\x02\x03",
            "#2101243VHow is work?\x02",
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
        0x102,
        (
            "#2101244V#12P#0108FW-Well...\x02\x03",
            "#2101245V#0103FI'm still new to everything, so we've made a\x01",
            "few missteps along the way.\x02\x03",
            "#2101246V#0102FBut I assure you, I don't intend to bring any\x01",
            "shame upon the MacDowell name.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Elderly Man",
        (
            "#2101247V#5P#2503FOh, Elie. I've told you, haven't I? Don't\x01",
            "worry yourself with name or pedigree.\x02\x03",
            "#2101248V#2500FAre these your colleagues, by chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101249V#12P#0100FY-Yes. They are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101250V#0003F#12PIt's nice to meet you, sir.\x02\x03",
            "#2101251V#0000FMy name is Lloyd Bannings, and I'm with\x01",
            "the CPD's Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101252V#12P#0204FTio Plato. How do you do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2101253V#12P#0300FHow's it goin'? Name's Randy Orlando.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Elderly Man",
        (
            "#2101254V#5P#2503FMy name is Henry MacDowell. It's a\x01",
            "pleasure to meet the three of you.\x02\x03",
            "#2101255V#2500FI must thank you for taking care of my\x01",
            "granddaughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101256V#0012F#12PNo, sir. I think you're mistaken.\x02\x03",
            "#2101257V#0000FElie's the one that's always looking\x01",
            "after us.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#2101258V#12P#0304FMademois-Elie's a bona fide genius when\x01",
            "it comes to takin' care of reports and all\x01",
            "that jazz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101259V#6P#0211FThat does not excuse your utter lack\x01",
            "of assistance, Randy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x102,
        "#2101260V#12P#0109FD-Don't worry about it. It's okay.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Old Man MacDowell",
        (
            "#2101261V#5P#2500FIs that so? Well, what IS important is\x01",
            "that you're content with your post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#2101262V#2606F#5PYou know, Elie...\x02\x03",
            "#2101263V#2601FIt wouldn't hurt to stop by your\x01",
            "home every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101264V#12P#0108FMy apologies.\x02\x03",
            "#2101265V#0106FI've been hesitant to rely on anyone\x01",
            "ever since I became independent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#2101266V#2601F#5PEven so, don't you--\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x190)

    NpcTalk(
        0x15,
        "Old Man MacDowell",
        (
            "#2101267V#11P#2503FIt's fine, Ernest.\x02\x03",
            "#2101268V#2500FElie wishes to stand by her decision.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x102, 400)
    Sleep(300)

    NpcTalk(
        0x15,
        "Old Man MacDowell",
        (
            "#2101269V#5P#2500FListen, dear. Continue down the path\x01",
            "you've chosen until you're satisfied.\x02\x03",
            "#2101270VI cannot mix business with personal\x01",
            "affairs, but know that I will cooperate\x01",
            "with you to the best of my ability.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101271V#12P#0104FI know. Thank you, Grandfather.\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x190)
    Sleep(300)

    NpcTalk(
        0x15,
        "Old Man MacDowell",
        (
            "#2101272V#11P#2500FNow, then. Shall we go, Ernest?\x02\x03",
            "#2101273VI have a meeting with the Business Owners'\x01",
            "Association next, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#2101274V#2600F#5PYes, sir. It's scheduled for 5PM.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_EA38():

        label("loc_EA38")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_EA38")

    QueueWorkItem2(0x101, 2, lambda_EA38)

    def lambda_EA4A():

        label("loc_EA4A")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_EA4A")

    QueueWorkItem2(0x102, 2, lambda_EA4A)

    def lambda_EA5C():

        label("loc_EA5C")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_EA5C")

    QueueWorkItem2(0x103, 2, lambda_EA5C)

    def lambda_EA6E():

        label("loc_EA6E")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_EA6E")

    QueueWorkItem2(0x104, 2, lambda_EA6E)
    OP_92(0x15, 0xFFFFE890, 0x4650, 0x1F4)

    def lambda_EA8D():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_EA8D)
    Sleep(150)
    OP_92(0x16, 0xFFFFE5D4, 0x490C, 0x1F4)

    def lambda_EAB7():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_EAB7)
    Sleep(4000)
    Fade(500)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    SetChrPos(0x15, -4900, 1770, 9000, 180)
    SetChrPos(0x16, -4900, 1770, 10400, 180)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x102, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    OP_68(-3000, 2000, 1800, 0)
    MoveCamera(328, 10, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(13000, 0)

    def lambda_EB5D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_EB5D)
    Sleep(50)

    def lambda_EB7A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_EB7A)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    Sound(462, 0, 100, 0)
    OP_71(0x4, 0xF1, 0x10E, 0x0, 0x0)
    OP_79(0x4)

    def lambda_EBB1():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_EBB1)

    def lambda_EBCB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_EBCB)
    Sleep(150)

    def lambda_EBDF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_EBDF)
    Sleep(500)

    def lambda_EBFC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_EBFC)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x16, 2)
    Sound(461, 0, 100, 0)
    OP_71(0x4, 0x10F, 0x12C, 0x0, 0x0)
    OP_79(0x4)
    OP_71(0x4, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x4)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)
    Sound(470, 0, 100, 0)
    BeginChrThread(0x17, 3, 0, 47)
    Sleep(300)
    Sound(457, 0, 100, 0)
    Sleep(1700)
    EndChrThread(0x17, 0xFF)
    Fade(500)
    OP_68(2500, 2000, -500, 0)
    MoveCamera(50, 13, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x17, -5300, 0, 1800, 100)
    OP_D3(0x17, 0x0, 0x186A0, 0x0, 0x0)
    OP_68(12500, 2000, 6500, 5000)
    MoveCamera(36, 13, 0, 5000)
    OP_9F(0x0, 0x17)
    OP_9F(0x1, 7500, 0, 3500)
    OP_9F(0x1, 17500, 0, 9500)
    OP_9F(0x1, 31500, 0, 10500)
    OP_9F(0x2, 0x17, 6500, 0x6)
    SetChrFlags(0x17, 0x80)
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x1000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    Fade(500)
    OP_68(-700, 3000, 20800, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19000, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#2101275V#5P#0305F*whistle*\x02\x03",
            "#2101276VAin't that a bitchin' ride? I KNEW your\x01",
            "family was loaded, Mademois-Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101277V#0109F#5PU-Um, I wouldn't really--\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(600)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#2101278V#5P#0005F#4SWAIT!\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_EE77():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_EE77)
    Sleep(50)
    OP_93(0x103, 0x2D, 0x1F4)

    ChrTalk(
        0x104,
        "#2101279V#12P#0305FHoly smokes, dude! You okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101280V#6P#0205FWhat seems to be the issue, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101281V#5P#0007FHe said Henry MacDowell, right?\x02\x03",
            "#2101282VAs in, the MAYOR of Crossbell City?!\x01",
            "THAT Henry MacDowell?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#2101283V#12P#0301FWell, I'll be damned...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101284V#6P#0201FHe is?\x02\x03",
            "#2101285V#0205F...That's right. I believe I saw that\x01",
            "name and position recorded in the\x01",
            "database.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#2101286V#0106F#5P*sigh* Oh, dear...\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x87, 0x190)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2101287V#0102F#5PHonestly, it's a miracle that you\x01",
            "hadn't noticed until now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F102():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F102)
    Sleep(100)

    def lambda_F112():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F112)
    Sleep(50)
    OP_93(0x104, 0x13B, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#2101288V#11P#0002FThere was always something about your\x01",
            "surname that bothered me, but I couldn't\x01",
            "for the life of me figure out what it was.\x02\x03",
            "#2101289VThe mayor's name must have totally\x01",
            "slipped my mind, I guess.\x02\x03",
            "#2101290V#0006FGeez. And I call myself a detective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101291V#0104F#5PWell, I don't particularly mind if you know.\x02\x03",
            "#2101292VMy grandfather's position has nothing to\x01",
            "do with me, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101293V#11P#0005F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101294V#0106F#5PWe should get back to the task at hand.\x02\x03",
            "#2101295V#0101FIt pains me to admit it, but we have to\x01",
            "tell Ilya and the others about the First\x01",
            "Division taking over the case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101296V#11P#0001FY-Yeah. Unfortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101297V#12P#0305FYo, Mademois-Elie. Why do ya think your\x01",
            "granddad stopped by Arc en Ciel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101298V#0105F#5POh, that?\x02\x03",
            "#2101299V#0103FArc en Ciel's first public performance of their\x01",
            "new production is being held alongside this\x01",
            "year's Anniversary Festival.\x02\x03",
            "#2101300V#0100FI can only assume he was here for a business\x01",
            "meeting regarding that.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(-2000, 3940, 21500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x0, -2000, 1990, 21500, 0)
    SetChrPos(0x1, -2000, 1990, 21500, 0)
    SetChrPos(0x2, -2000, 1990, 21500, 0)
    SetChrPos(0x3, -2000, 1990, 21500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 6, 0x80)
    ClearMapObjFlags(0x5, 0x1000)
    SetScenarioFlags(0x81, 4)
    EndChrThread(0xD, 0x0)
    BeginChrThread(0xD, 0, 0, 3)
    EventEnd(0x5)
    Return()

    # Function_46_DA79 end

    def Function_47_F601(): pass

    label("Function_47_F601")


    def lambda_F606():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x1194, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_F606)
    Sleep(600)

    def lambda_F61E():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x157C, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_F61E)
    Sleep(600)

    def lambda_F636():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_F636)
    Return()

    # Function_47_F601 end

    def Function_48_F647(): pass

    label("Function_48_F647")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05200.itc", 0x1E)
    OP_68(-2000, 2800, 29800, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -2600, 1850, 25800, 0)
    SetChrPos(0x102, -1400, 1850, 25800, 0)
    SetChrPos(0x103, -2600, 1990, 24400, 0)
    SetChrPos(0x104, -1400, 1990, 24400, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -2000, 1760, 27800, 180)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFE, 0xCB, 0xC0, 0x2C, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFlags(0x5, 0x1000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SubItemNumber(0x324, 1)
    OP_68(-2000, 2800, 26800, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sound(1637, 255, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x18,
        (
            "#2101379V#1806F#5PI'm so sorry, everyone. I've caused you\x01",
            "nothing but trouble...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101380V#12P#0012FDon't worry about it, Rixia.\x02\x03",
            "#2101381V#0000FAfter all, wasted efforts are just another\x01",
            "part of the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101382V#12P#0202FSuch is the nature of crime prevention.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101383V#0302F#12PYup. No worries, Rixia.\x02\x03",
            "#2101384V#0309FForget about us and focus on\x01",
            "the private performance, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#2101385V#1802F#5PIf you guys say so, then I will.\x01",
            "Thank you, everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#2101386V#6P#0005FPrivate performance?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#2101387V#0305F#11PThe hell? You dunno 'bout it already?\x02\x03",
            "#2101388V#0300FArc en Ciel puts on a lil' sneak peek of their\x01",
            "new show before it's available to the public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#2101389V#1804F#5PThat's correct. This'll be my first time\x01",
            "performing in one...\x02\x03",
            "#2101390V#1802FPeople from the media and other select\x01",
            "individuals, home and abroad, have\x01",
            "been invited to attend.\x02\x03",
            "#2101391VI can only assume that lots of celebrities\x01",
            "will come, too, and boost awareness of\x01",
            "our new production.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FB95():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FB95)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#2101392V#12P#0000FWow. That's pretty crazy.\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#2101393V#0105F#12PBy any chance...was Mayor MacDowell\x01",
            "invited as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#2101394V#1805F#5POh, yes. He's our guest of honor.\x02\x03",
            "#2101395V#1804FThe others have told me that he plans to\x01",
            "publically support it in conjunction with\x01",
            "the Anniversary Festival.\x02\x03",
            "#2101396V#1802FHe's quite kind. Despite his busy schedule,\x01",
            "he made time to stop by and encourage us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101397V#0100F#12PHow very much like him.\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#2101398V#0104F#12PGood luck with the private performance,\x01",
            "Rixia.\x02\x03",
            "#2101399V#0102FIt may be your first time, but I'm sure you'll\x01",
            "perform wonderfully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#2101400V#1805F#5PYou think so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101401V#12P#0002FAbsolutely. Considering all the training\x01",
            "you've put in, I doubt you have anything\x01",
            "to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2101402V#0309F#12PHell yeah! This play's gonna be sick!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101403V#12P#0204FI am quite looking forward to it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#2101404V#1809F#5PI appreciate the vote of confidence.\x02\x03",
            "#2101405V#1802FI'll return to practice, then.\x02\x03",
            "#2101406VThank you for your help, everyone.\x02",
        )
    )

    CloseMessageWindow()
    Sound(1638, 255, 100, 0)
    Sleep(1000)
    OP_93(0x18, 0x0, 0x1F4)
    OP_68(-2000, 3800, 31800, 3500)

    def lambda_1000F():
        OP_95(0xFE, -2000, 2660, 34200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1000F)
    WaitChrThread(0x18, 1)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_6F(0x79)

    def lambda_1004A():
        OP_95(0xFE, -2000, 2660, 36000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1004A)
    Sleep(500)

    def lambda_10067():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_10067)
    WaitChrThread(0x18, 2)
    WaitChrThread(0x18, 1)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    Sleep(500)
    Fade(500)
    OP_68(-2000, 3000, 25100, 0)
    MoveCamera(40, 27, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    def lambda_10133():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10133)
    Sleep(50)

    def lambda_10143():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10143)
    Sleep(50)

    def lambda_10153():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10153)
    Sleep(50)

    def lambda_10163():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10163)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x101,
        (
            "#2101407V#0006F#5P*sigh*\x02\x03",
            "#2101408V#0000FReady to head back, guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2101409V#0306F#11PNothin' better to do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101410V#6P#0206FI feel exhausted. Both mentally and physically.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101411V#0103F#5PI can relate...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_D5(0x1E)
    OP_68(-2000, 3710, 26800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -2000, 1760, 26800, 180)
    SetChrPos(0x102, -2000, 1760, 26800, 180)
    SetChrPos(0x103, -2000, 1760, 26800, 180)
    SetChrPos(0x104, -2000, 1760, 26800, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearMapObjFlags(0x5, 0x1000)
    SetScenarioFlags(0x81, 5)
    OP_C7(0x0, 0x1000)
    OP_29(0x42, 0x1, 0x9)
    OP_1B(0x1, 0x0, 0x3E)
    OP_1B(0x2, 0x0, 0x3F)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7000")
    ReplaceBGM("ed7101", "ed7000")
    ReplaceBGM("ed7100", "ed7102")
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_48_F647 end

    def Function_49_10332(): pass

    label("Function_49_10332")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00500.itc", 0x1E)
    LoadChrToIndex("chr/ch05200.itc", 0x1F)
    LoadChrToIndex("chr/ch05100.itc", 0x20)
    LoadChrToIndex("apl/ch50219.itc", 0x21)
    LoadChrToIndex("apl/ch50220.itc", 0x22)
    LoadChrToIndex("apl/ch50238.itc", 0x23)
    LoadChrToIndex("apl/ch50239.itc", 0x24)
    OP_68(15000, 14100, 24500, 0)
    MoveCamera(320, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x0, 15000, 0, 15000, 0)
    SetChrPos(0x1, 15000, 0, 15000, 0)
    SetChrPos(0x2, 15000, 0, 15000, 0)
    SetChrPos(0x3, 15000, 0, 15000, 0)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 26300, 14100, 24500, 270)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x8000)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x18, 19300, 13100, 24500, 270)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01801.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01700.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis155.itp")
    LoadEffect(0x0, "event\\eva04_00.eff")
    OP_68(17000, 14100, 24500, 3000)
    SetCameraDistance(15500, 3000)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_52(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x0)
    SetChrChip(0x0, 0x1A, 0x1E, 0x12C)

    def lambda_10565():
        OP_9D(0xFE, 0x4B64, 0x332C, 0x5FB4, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_10565)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x1A, 1)
    PlayEffect(0x0, 0xFF, 0x1A, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x1A, 0x1)
    Sound(42, 0, 100, 0)
    Sleep(10)
    Sound(31, 0, 100, 0)
    Sleep(500)
    SetChrChip(0x1, 0x1A, 0x0, 0x0)
    OP_52(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(250)
    SetChrChipByIndex(0x1A, 0x21)
    SetChrSubChip(0x1A, 0x0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x1A,
        (
            "#2201825V\x07\x03",
            "#0700F#11P#40W...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(19300, 13900, 24500, 0)
    MoveCamera(50, 31, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrFlags(0x1A, 0x20)
    SetChrFlags(0x1A, 0x2)
    SetChrChipByIndex(0x1A, 0x23)
    SetChrSubChip(0x1A, 0x7)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x0)
    Sleep(1000)
    Sound(534, 0, 90, 0)
    StopBGM(0x1388)
    MoveCamera(40, 31, 0, 2000)
    SetCameraDistance(20500, 2000)
    BeginChrThread(0x1A, 3, 0, 53)

    def lambda_106A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_106A0)

    def lambda_106B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_106B1)
    Sleep(600)
    SetChrSubChip(0x18, 0x1)
    Sleep(130)
    SetChrSubChip(0x18, 0x2)
    Sleep(130)
    SetChrSubChip(0x18, 0x3)
    Sleep(400)
    WaitChrThread(0x1A, 2)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    Sound(1640, 255, 100, 0)
    Sleep(1600)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x18,
        (
            "#2201827V\x07\x00",
            "#40W...\x02",
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
    ClearChrFlags(0x18, 0x20)
    ClearChrFlags(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    OP_93(0x18, 0x0, 0x190)
    Sleep(300)
    SetCameraDistance(21500, 3000)

    def lambda_10792():
        OP_96(0xFE, 0x4B64, 0x332C, 0x7788, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_10792)
    WaitChrThread(0x18, 1)
    PlayEffect(0x0, 0xFF, 0x18, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x4)
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_10804():
        OP_9D(0xFE, 0x4B64, 0x13EC, 0x8B10, 0x514, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_10804)
    Sound(814, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x18, 1)
    OP_6F(0x10)
    ClearChrFlags(0x18, 0x20)
    ClearChrFlags(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    OP_68(-2000, 2700, 28500, 0)
    MoveCamera(320, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    ClearChrFlags(0x18, 0x4)
    SetChrPos(0x18, 6000, 1760, 26000, 270)
    ClearChrFlags(0x19, 0x4)
    SetChrPos(0x19, -2000, 1990, 18600, 0)
    MoveCamera(330, 17, 0, 3500)
    SetCameraDistance(17000, 3500)

    def lambda_108D4():
        OP_96(0xFE, 0xFFFFF830, 0x6E0, 0x6F54, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_108D4)
    FadeToBright(1000, 0)
    WaitChrThread(0x18, 1)
    OP_93(0x18, 0x0, 0x1F4)
    OP_6F(0x50)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)

    NpcTalk(
        0x19,
        "Woman's Voice",
        "#2201828VYou're early, Rixia.\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(1635, 255, 100, 0)
    OP_68(-2000, 2700, 27600, 3000)

    def lambda_1096B():
        OP_96(0xFE, 0xFFFFF830, 0x6E0, 0x67E8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1096B)

    def lambda_10985():
        TurnDirection(0xFE, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_10985)
    WaitChrThread(0x19, 1)
    OP_6F(0x1)

    ChrTalk(
        0x18,
        "#2201830V#1805F#11PIlya?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x19,
        (
            "#2201831VWhat? You looking forward to\x01",
            "practice that badly?\x02\x03",
            "#2201832VGeez, and I call myself a dance\x01",
            "freak.\x02\x03",
            "#2201833VWere you always this dedicated?\x02",
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
        0x18,
        (
            "#2201834V#1809F#11PAhaha. I'm still nowhere near your level...\x02\x03",
            "#2201835VAnd I doubt I ever will be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#2201836V#6P#1704FYou say that, but your actions paint a different\x01",
            "picture. You were just as excited for the private\x01",
            "performance as I was.\x02\x03",
            "#2201837V#1702FAnd c'mon, Rixia. Your acting is top-notch.\x02\x03",
            "#2201838VYou've finally become a genuine rival\x01",
            "for yours truly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#2201839V#1802F#11PReally?\x02\x03",
            "#2201840V#1804FWell, true or not, I still owe everything to\x01",
            "you, Ilya.\x02\x03",
            "#2201841VYou showed me the light, opening my eyes\x01",
            "to a path straying from the one I inherited.\x02\x03",
            "#2201842V#1802FThough, I suppose I should be grateful to\x01",
            "the SSS this time, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#2201843V#6P#1705FOh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#2201844V#1804F#11PDon't worry about it. It's nothing.\x02\x03",
            "#2201845V#1800FToday's schedule is perfecting the\x01",
            "third act, right?\x02\x03",
            "#2201846VI'll do my best to keep up with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#2201847V#6P#1702FOh? You sure you're up for it?\x02\x03",
            "#2201848V#1700FWell, who am I to turn down a challenge?\x01",
            "ESPECIALLY from you.\x02\x03",
            "#2201849V#1709FAll righty, then! Until it's time for the\x01",
            "public performance, I'll improve this\x01",
            "scene a hundred times over!\x02\x03",
            "#2201850VFollow me, Rixia!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#2201851V#1809F#11POf course!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 6000)
    BeginChrThread(0x101, 3, 0, 50)
    Sleep(2000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    StopBGM(0x1388)
    WaitBGM()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10F93")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10F93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10FAD")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10FAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10FC7")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10FC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10FE1")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10FE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10FFB")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10FFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11015")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11015")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1102F")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1102F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11049")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11049")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11069")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_110A4")

    label("loc_11069")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11089")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_110A4")

    label("loc_11089")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_110A4")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_110A4")

    OP_29(0x41, 0x4, 0x10)
    OP_29(0x42, 0x4, 0x10)
    OP_29(0x43, 0x4, 0x10)
    OP_29(0x41, 0x4, 0x20)
    OP_29(0x43, 0x4, 0x20)
    SubItemNumber(0x325, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_110E0")
    OP_29(0xE, 0x4, 0x40)
    Jump("loc_110F2")

    label("loc_110E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110F2")
    OP_29(0xE, 0x4, 0x40)

    label("loc_110F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11104")
    OP_29(0x10, 0x4, 0x40)

    label("loc_11104")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11122")
    OP_29(0x11, 0x4, 0x40)
    Jump("loc_11134")

    label("loc_11122")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11134")
    OP_29(0x11, 0x4, 0x40)

    label("loc_11134")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11152")
    OP_29(0x12, 0x4, 0x40)
    Jump("loc_11164")

    label("loc_11152")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11164")
    OP_29(0x12, 0x4, 0x40)

    label("loc_11164")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11182")
    OP_29(0x13, 0x4, 0x40)
    Jump("loc_11194")

    label("loc_11182")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11194")
    OP_29(0x13, 0x4, 0x40)

    label("loc_11194")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_111B2")
    OP_29(0x14, 0x4, 0x40)
    Jump("loc_111C4")

    label("loc_111B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111C4")
    OP_29(0x14, 0x4, 0x40)

    label("loc_111C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_111E2")
    OP_29(0x15, 0x4, 0x40)
    Jump("loc_111F4")

    label("loc_111E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111F4")
    OP_29(0x15, 0x4, 0x40)

    label("loc_111F4")

    SubItemNumber(0x341, 1)
    SubItemNumber(0x33D, 1)
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_DE(0x26, 0x0)
    OP_DE(0x1E, 0x0)
    OP_DE(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5F, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x5F, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    OP_E3(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 1)
    NewScene("c1120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_49_10332 end

    def Function_50_112D3(): pass

    label("Function_50_112D3")

    BeginChrThread(0x19, 3, 0, 51)
    Sleep(100)
    BeginChrThread(0x18, 3, 0, 52)
    WaitChrThread(0x19, 3)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    WaitChrThread(0x18, 3)

    def lambda_1130A():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1130A)
    Sleep(50)

    def lambda_11327():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_11327)
    Sleep(300)

    def lambda_11344():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_11344)
    Sleep(50)

    def lambda_11358():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_11358)
    Return()

    # Function_50_112D3 end

    def Function_51_11365(): pass

    label("Function_51_11365")


    def lambda_1136A():
        OP_96(0xFE, 0xFFFFF63C, 0x6E0, 0x73A0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1136A)
    WaitChrThread(0x19, 1)

    def lambda_11388():
        OP_96(0xFE, 0xFFFFF63C, 0xA64, 0x8340, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_11388)
    WaitChrThread(0x19, 1)
    Return()

    # Function_51_11365 end

    def Function_52_113A2(): pass

    label("Function_52_113A2")


    def lambda_113A7():

        label("loc_113A7")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_113A7")

    QueueWorkItem2(0x18, 2, lambda_113A7)

    def lambda_113B9():
        OP_96(0xFE, 0xFFFFFA88, 0x6E0, 0x7080, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_113B9)
    WaitChrThread(0x18, 1)
    Sleep(600)
    EndChrThread(0x18, 0x2)
    OP_93(0x18, 0x0, 0x1F4)

    def lambda_113E5():
        OP_95(0xFE, -1400, 2660, 32800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_113E5)
    WaitChrThread(0x18, 1)
    Return()

    # Function_52_113A2 end

    def Function_53_113FF(): pass

    label("Function_53_113FF")

    OP_A1(0xFE, 0x7D0, 0x8, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_53_113FF end

    def Function_54_11415(): pass

    label("Function_54_11415")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-23500, 1000, 10000, 0)
    MoveCamera(75, 27, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(11000, 0)
    SetChrPos(0x101, -16000, 0, 5500, 300)
    SetChrPos(0x102, -16000, 0, 4300, 300)
    SetChrPos(0x104, -14600, 0, 4500, 300)
    SetChrPos(0x103, -14600, 0, 3300, 300)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFE, 0xCB, 0xC0, 0x2C, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    BeginChrThread(0x102, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 55)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 58)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 56)
    OP_68(-26500, 2500, 16000, 10000)
    MoveCamera(30, 11, 0, 10000)
    SetCameraDistance(19000, 10000)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 3)
    FadeToDark(2000, 0, -1)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x103, 3)

    def lambda_11596():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11596)
    Sleep(50)

    def lambda_115B3():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_115B3)
    Sleep(50)

    def lambda_115D0():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_115D0)
    Sleep(50)

    def lambda_115ED():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_115ED)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7000", "ed7000")
    SetScenarioFlags(0x5C, 0)
    NewScene("c0470", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_54_11415 end

    def Function_55_11630(): pass

    label("Function_55_11630")


    def lambda_11635():
        OP_95(0xFE, -26000, 0, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11635)
    WaitChrThread(0xFE, 1)

    def lambda_11653():
        OP_95(0xFE, -26000, 300, 16500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11653)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_55_11630 end

    def Function_56_1166D(): pass

    label("Function_56_1166D")


    def lambda_11672():
        OP_95(0xFE, -26000, 0, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11672)
    WaitChrThread(0xFE, 1)

    def lambda_11690():
        OP_95(0xFE, -26000, 300, 15000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11690)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_1166D end

    def Function_57_116AA(): pass

    label("Function_57_116AA")


    def lambda_116AF():
        OP_95(0xFE, -27200, 0, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_116AF)
    WaitChrThread(0xFE, 1)

    def lambda_116CD():
        OP_95(0xFE, -27200, 300, 16100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_116CD)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_57_116AA end

    def Function_58_116E7(): pass

    label("Function_58_116E7")


    def lambda_116EC():
        OP_95(0xFE, -27200, 0, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_116EC)
    WaitChrThread(0xFE, 1)

    def lambda_1170A():
        OP_95(0xFE, -27200, 300, 14600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1170A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_58_116E7 end

    def Function_59_11724(): pass

    label("Function_59_11724")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-2000, 2760, 27500, 0)
    MoveCamera(55, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -2700, 1760, 26800, 45)
    SetChrPos(0x102, -1300, 1760, 26800, 315)
    SetChrPos(0x103, -2700, 1760, 28200, 135)
    SetChrPos(0x104, -1300, 1760, 28200, 225)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    MoveCamera(45, 27, 0, 3000)
    SetCameraDistance(20000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#4300073V#0106FI can't believe how many people are\x01",
            "missing at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300074V#5P#0303FDamn it. That bad feeling was right on the money.\x02\x03",
            "#4300075V#0301FHow the hell do so many people up and disappear?\x01",
            "They get kidnapped, or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300076V#0206FThere is too little information to come to a conclusion.\x01",
            "All we can do is hypothesize at the moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_END)), "loc_11A5E")

    ChrTalk(
        0x101,
        (
            "#4300077V#6P#0003FThe five people missing may only be the tip\x01",
            "of the iceberg.\x02\x03",
            "#4300079V#0001FOdds are, several people living in Crossbell City\x01",
            "have already disappeared...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B0F")

    label("loc_11A5E")


    ChrTalk(
        0x101,
        (
            "#4300078V#6P#0003FThe four people missing may only be the tip\x01",
            "of the iceberg.\x02\x03",
            "#4300079V#0001FOdds are, several people living in Crossbell City\x01",
            "have already disappeared...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B0F")


    ChrTalk(
        0x102,
        (
            "#4300080V#0108FAs much as I hate to admit it, you might be right...\x01",
            "How many people have gone missing at this point?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300081V#5P#0301FWhat's the plan, Lloyd?\x02\x03",
            "#4300082VIt'd probably be a bit of a pain in the ass to\x01",
            "search for them one at a time, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300083V#6P#0006FYeah, we're going to need a stronger\x01",
            "effort than just the four of us.\x02\x03",
            "#4300084V#0008FAnd since the First Division is being pressured\x01",
            "by the top brass, they won't be able to help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300085V#0202FWould it be possible to consult with Inspector\x01",
            "Donovan from the Second Division?\x02\x03",
            "#4300086VHe has lent his assistance in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300087V#6P#0003FNo, I don't think that'll work, either.\x02\x03",
            "#4300088V#0001FI can only imagine that the Second Division\x01",
            "is being pressured as well, given Detective\x01",
            "Dudley came to us for help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4300089V#0206FI see. That certainly makes sense...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300090V#0108FSo, the circumstances in the Metropolitan\x01",
            "Division should be about the same...\x02\x03",
            "#4300091V#0106FBeing able to utilize that division's manpower\x01",
            "would have been a great asset...\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_11F92():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11F92)
    Sleep(50)

    def lambda_11FA2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_11FA2)
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
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4300092V\x07\x00",
            "#0001FYes, Special Support Section,\x01",
            "Lloyd Bannings speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4300093V\x07\x05",
            "Hey, rookies!\x02\x03",
            "#4300094VWhat the hell have you four\x01",
            "been up to?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4300095V\x07\x00",
            "#0011FOh...\x02\x03",
            "#4300096V#0001FIs that you, Detective Dudley?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4300097V\x07\x05",
            "You're damn right it's me!\x02\x03",
            "#4300098VYou guys didn't go sticking your noses into\x01",
            "Revache's business, did you?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4300099V\x07\x00",
            "#0005FN-No, not exactly...\x02\x03",
            "#4300100V#0003FWe're focused on the drug investigation\x01",
            "right now.\x02\x03",
            "#4300101V#0001FWhy? Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4300102V\x07\x05",
            "Why else would I be calling?!\x01",
            "Their office is--\x02\x03",
            "#4300103VAhem! Forget I said anything.\x02\x03",
            "#4300104VIf it doesn't concern you, then don't do anything\x01",
            "rash. Carry on with your investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(825, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4300105V\x07\x00",
            "#0005FAh...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(807, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#4300106V#6P#0013F...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#4300107V#0101FWas that Detective Dudley on the\x01",
            "other end? What's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300108V#6P#0006FWell...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd told Elie and the others about\x01",
            "his conversation with Dudley.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0x104,
        "#4300109V#5P#0301FWhat's poindexter's deal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300110V#0206FHis change in demeanor is suspicious.\x02\x03",
            "#4300111V#0201FClearly something must have happened\x01",
            "with Revache, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300112V#6P#0003FYeah, most likely.\x02",
    )

    CloseMessageWindow()
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
        0x104,
        (
            "#4300113V#5P#0300FWe'd better go check it out, then. Better than\x01",
            "standin' around here twiddlin' our thumbs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300114V#0103FTrue, but we were told to not interfere in\x01",
            "the conflict. Our hands are tied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300115V#0202FIf the mafia is connected to the missing persons\x01",
            "case, then that is our probable cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300116V#6P#0001FI agree. Let's hurry to Revache & Co.!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0x0, -2000, 1760, 26500, 180)
    SetScenarioFlags(0xC3, 7)
    OP_29(0x4C, 0x1, 0xC)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_59_11724 end

    def Function_60_127A8(): pass

    label("Function_60_127A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1285A")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FIt looks like only people with the proper\x01",
            "authorization are allowed inside right now.\x01",
            "Let's refrain from entering uninvited.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_1285A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1290C")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FIt looks like only people with the proper\x01",
            "authorization are allowed inside right now.\x01",
            "Let's refrain from entering uninvited.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_1290C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12990")
    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Arc en Ciel is currently in session. It would be\x01",
            "best to not intrude on them.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_12990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12B51")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AE0")

    ChrTalk(
        0x13D,
        (
            "#2105FTrying to get inside?\x02\x03",
            "#2109FNice, guys! You can do it! Heck, with ties\x01",
            "to Ilya Platiere, you can do anything!\x02\x03",
            "Fly, my friends! To the promised land!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FWhat's got you so enthusiastic today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FShall we hurry to the casino? Something\x01",
            "about the mayor's story has me worried.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_12B3B")

    label("loc_12AE0")


    ChrTalk(
        0x101,
        (
            "#0001FWe can't neglect what Mayor Bickson told\x01",
            "us... Let's hurry to the casino, guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B3B")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_12B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12BD5")
    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Arc en Ciel is currently in session. It would be\x01",
            "best to not intrude on them.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_12BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12D89")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D19")

    ChrTalk(
        0x101,
        (
            "#0005FWhoops. Arc en Ciel's in the middle of\x01",
            "a performance right now, aren't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FLet's leave the actin' to the\x01",
            "actors, eh?\x02\x03",
            "#0300FWe've got more important stuff\x01",
            "to be dealin' with right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, you're right. Let's hurry on over to\x01",
            "St. Ursula Medical College.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_12D73")

    label("loc_12D19")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Arc en Ciel is currently in session. It would be\x01",
            "best to not intrude on them.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_12D73")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_12D89")

    Return()

    # Function_60_127A8 end

    def Function_61_12D8A(): pass

    label("Function_61_12D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1309F")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F6D")

    ChrTalk(
        0x103,
        "#0200FIs this...a casino?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FSure is. The illustrious Barca Casino!\x01",
            "It's my go-to place in Crossbell City.\x02\x03",
            "#0309FSo how 'bout it, guys? Lil' casino action\x01",
            "to celebrate our newfound division?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0111FPlease try to use your brain, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FC'mon, Mademois-Elie! Gimme one good\x01",
            "reason why we shouldn't?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FWell, for one, we're in the middle of training\x01",
            "today. Sorry, Randy. You're just going to have\x01",
            "to deal with it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x46, 5)
    Jump("loc_13089")

    label("loc_12F6D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13039")

    ChrTalk(
        0x104,
        "#0300FLet's see what I'm playin' today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FUh, Randy? Correct me if I'm wrong,\x01",
            "but didn't I say no to the casino?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301FDamn. I'm surrounded by a bunch of killjoys.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13089")

    label("loc_13039")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This is Barca Casino. It would be wise\x01",
            "to avoid visiting for today.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_13089")

    Sleep(50)
    SetChrPos(0x0, -26500, 300, 15360, 175)
    EventEnd(0x4)

    label("loc_1309F")

    Return()

    # Function_61_12D8A end

    def Function_62_130A0(): pass

    label("Function_62_130A0")

    EventBegin(0x1)
    Call(0, 64)
    Sleep(50)
    SetChrPos(0x0, 20770, 0, 12930, 270)
    EventEnd(0x4)
    Return()

    # Function_62_130A0 end

    def Function_63_130BC(): pass

    label("Function_63_130BC")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 64)
    SetChrPos(0x0, -39280, 0, 12420, 90)
    EventEnd(0x4)
    Return()

    # Function_63_130BC end

    def Function_64_130D8(): pass

    label("Function_64_130D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1319F")

    ChrTalk(
        0x101,
        (
            "#0006FToday sure wore us out... Let's avoid\x01",
            "any unnecessary detours and head\x01",
            "back to the SSS.\x02\x03",
            "#0000FCutting through the Back Alley should\x01",
            "be the quickest way back from here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13208")

    label("loc_1319F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13208")

    ChrTalk(
        0x101,
        (
            "#0001FWe can't neglect what Mayor Bickson told\x01",
            "us... Let's hurry to the casino, guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13208")

    Return()

    # Function_64_130D8 end

    SaveToFile()

Try(main)
