from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0100.bin",                # FileName
        "c0100",                    # MapName
        "c0100",                    # Location
        0x0004,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("c0100", "c0100_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 5, 0, 6],
    )

    BuildStringList((
        "c0100",                  # 0
        "Gina",                   # 1
        "Old Man Conte",          # 2
        "Abel",                   # 3
        "Mimi",                   # 4
        "Pruna",                  # 5
        "Lenalee",                # 6
        "Haas",                   # 7
        "Arona",                  # 8
        "Officer Kate",           # 9
        "Reins",                  # 10
        "車１",                   # 11
        "Coppe",                  # 12
        "Zeit",                   # 13
        "KeA",                    # 14
        "Old Man",                # 15
        "Old Lady",               # 16
        "車１",                   # 17
        "車２",                   # 18
        "Harold",                 # 19
        "Chief Sergei",           # 20
        "Secretary Ernest",       # 21
        "Zeit",                   # 22
        "イベント用ＮＰＣ",       # 23
        "イベント用ＮＰＣ",       # 24
        "イベント用ＮＰＣ",       # 25
        "イベント用ＮＰＣ",       # 26
        "イベント用ＮＰＣ",       # 27
        "SE制御",                 # 28
        " ",                      # 29
        "Central Square",         # 30
        "West Street",            # 31
        "Administrative District",# 32
        "Residential District",   # 33
        "Entertainment District", # 34
        "East Street",            # 35
        "Downtown District",      # 36
        "Harbor District",        # 37
        "IBC",                    # 38
        "Station Street",         # 39
        "Back Alley",             # 40
        "Ursula Road",            # 41
        "East Crossbell Highway", # 42
        "West Crossbell Highway", # 43
        "Mainz Mountain Path",    # 44
    ))

    AddCharChip((
        "chr/ch21300.itc",                   # 00
        "chr/ch20002.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20700.itc",                   # 03
        "chr/ch20400.itc",                   # 04
        "chr/ch22100.itc",                   # 05
        "chr/ch28100.itc",                   # 06
        "chr/ch24900.itc",                   # 07
        "chr/ch21800.itc",                   # 08
        "chr/ch20600.itc",                   # 09
        "chr/ch21200.itc",                   # 0A
        "chr/ch20800.itc",                   # 0B
        "chr/ch20100.itc",                   # 0C
        "chr/ch21900.itc",                   # 0D
        "chr/ch27800.itc",                   # 0E
        "chr/ch20500.itc",                   # 0F
        "chr/ch26000.itc",                   # 10
        "chr/ch20900.itc",                   # 11
        "chr/ch39200.itc",                   # 12
        "chr/ch02708.itc",                   # 13
        "chr/ch20300.itc",                   # 14
        "chr/ch08200.itc",                   # 15
        "chr/ch30600.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(30000,   0,       -1799,   270,  261,  0x0, 0,   0,   0,   0,   1,   1,   0,   255,  0)
    DeclNpc(-6090,   150,     4449,    270,  341,  0x0, 0,   1,   0,   255, 255, 1,   1,   255,  0)
    DeclNpc(-6099,   0,       -9409,   90,   261,  0x0, 0,   2,   0,   0,   0,   1,   2,   255,  0)
    DeclNpc(-289,    0,       -10319,  225,  261,  0x0, 0,   3,   0,   0,   2,   1,   3,   255,  0)
    DeclNpc(850,     0,       17969,   90,   277,  0x0, 0,   15,  0,   0,   0,   1,   4,   255,  0)
    DeclNpc(2539,    0,       17870,   270,  277,  0x0, 0,   5,   0,   0,   0,   1,   5,   255,  0)
    DeclNpc(14130,   0,       340,     270,  261,  0x0, 0,   16,  0,   0,   0,   1,   6,   255,  0)
    DeclNpc(2650,    0,       -2960,   315,  389,  0x0, 0,   20,  0,   0,   0,   1,   7,   255,  0)
    DeclNpc(-1210,   0,       -2390,   180,  389,  0x0, 0,   22,  0,   0,   0,   1,   8,   255,  0)
    DeclNpc(-16760,  29,      6889,    315,  389,  0x0, 0,   6,   0,   0,   4,   1,   14,  255,  0)
    DeclNpc(-8010,   0,       16229,   225,  197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-22809,  1299,    -18829,  180,  261,  0x0, 0,   18,  0,   0,   3,   1,   9,   255,  0)
    DeclNpc(-25440,  1299,    -17040,  180,  404,  0x0, 0,   19,  0,   0,   0,   1,   12,  255,  0)
    DeclNpc(-25440,  1299,    -18170,  0,    389,  0x0, 0,   21,  0,   0,   0,   1,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 29,  -19.200000762939453,   -23.0,                 -9.199999809265137,    625.0,                 [0.07071065902709961,  0.14142140746116638,   -0.0,                  0.0,                   -0.07071070373058319,  0.14142131805419922,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.2687014639377594,   5.967981338500977,     1.840000033378601,     1.0])
    DeclEvent(0x0000, 0, 32,  0.0,                   -17.0,                 -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  3.4000000953674316,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 1, 15,  0.0,                   -17.0,                 -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  3.4000000953674316,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 1, 16,  -5.900000095367432,    -17.1299991607666,     -3.2799999713897705,   56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.9666666984558105,    3.425999879837036,     0.656000018119812,     1.0])

    DeclActor(1740,    -950,    3070,    1100,    1740,    550,     3070,    0x007C, 0,  7,  0x0000)
    DeclActor(-290,    -1000,   4400,    600,     -290,    -1000,   4400,    0x007C, 0,  9,  0x0000)
    DeclActor(-270,    0,       -980,    800,     130,     1500,    -10,     0x007C, 0,  8,  0x0000)
    DeclActor(4090,    0,       -16900,  1200,    4090,    2000,    -16900,  0x007C, 0,  12, 0x0000)

    PlaceName(-5.449999809265137, 0.0, -2.7200000286102295, 0x0000, 0x0000, "Central Square")
    PlaceName(-70.54000091552734, 0.0, 1.7300000190734863, 0x0000, 0x0000, "West Street")
    PlaceName(21.290000915527344, 0.0, 85.38999938964844, 0x0000, 0x0000, "Administrative District")
    PlaceName(-130.92999267578125, 0.0, 75.48999786376953, 0x0000, 0x0000, "Residential District")
    PlaceName(-58.65999984741211, 0.0, 67.56999969482422, 0x0000, 0x0000, "Entertainment District")
    PlaceName(74.98999786376953, 0.0, -25.489999771118164, 0x0000, 0x0000, "East Street")
    PlaceName(110.13999938964844, 0.0, -79.94000244140625, 0x0000, 0x0000, "Downtown District")
    PlaceName(102.70999908447266, 0.0, 39.849998474121094, 0x0000, 0x0000, "Harbor District")
    PlaceName(76.97000122070312, 0.0, 132.91000366210938, 0x0000, 0x0000, "IBC")
    PlaceName(5.690000057220459, 0.0, -71.02999877929688, 0x0000, 0x0000, "Station Street")
    PlaceName(-40.84000015258789, 0.0, 31.93000030517578, 0x0000, 0x0000, "Back Alley")
    PlaceName(2.7200000286102295, 0.0, -101.72000122070312, 0x0000, 0x0000, "Ursula Road")
    PlaceName(128.4499969482422, 0.0, -11.630000114440918, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-121.02999877929688, 0.0, 0.25, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-115.08999633789062, 0.0, 99.25, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-27.229999542236328, 0.0, -16.579999923706055, 0x0000, 0x0051, "")
    PlaceName(25.989999771118164, 0.0, 9.15999984741211, 0x0000, 0x0054, "")
    PlaceName(-2.9700000286102295, 0.0, -24.5, 0x0000, 0x0057, "")
    PlaceName(-27.969999313354492, 0.0, 12.130000114440918, 0x0000, 0x0053, "")
    PlaceName(-7.670000076293945, 0.0, 35.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-57.91999816894531, 0.0, 7.179999828338623, 0x0000, 0x0053, "")
    PlaceName(-67.56999969482422, 0.0, 27.969999313354492, 0x0000, 0x0053, "")
    PlaceName(-43.810001373291016, 0.0, 59.650001525878906, 0x0000, 0x0052, "")
    PlaceName(-39.11000061035156, 0.0, 46.779998779296875, 0x0000, 0x0053, "")
    PlaceName(-30.440000534057617, 0.0, 38.36000061035156, 0x0000, 0x0053, "")
    PlaceName(-2.2300000190734863, 0.0, 108.6500015258789, 0x0000, 0x0051, "")
    PlaceName(108.6500015258789, 0.0, -25.489999771118164, 0x0000, 0x0052, "")
    PlaceName(91.81999969482422, 0.0, -115.08999633789062, 0x0000, 0x0053, "")
    PlaceName(78.94999694824219, 0.0, -96.7699966430664, 0x0000, 0x0053, "")
    PlaceName(5.690000057220459, 0.0, -14.600000381469727, 0x0000, 0x0056, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(5000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1

    ScpFunction((
        "Function_0_980",          # 00, 0
        "Function_1_A38",          # 01, 1
        "Function_2_A85",          # 02, 2
        "Function_3_AB0",          # 03, 3
        "Function_4_ADB",          # 04, 4
        "Function_5_B06",          # 05, 5
        "Function_6_149E",         # 06, 6
        "Function_7_1738",         # 07, 7
        "Function_8_1962",         # 08, 8
        "Function_9_1B0F",         # 09, 9
        "Function_10_1B6D",        # 0A, 10
        "Function_11_2146",        # 0B, 11
        "Function_12_2235",        # 0C, 12
        "Function_13_2243",        # 0D, 13
        "Function_14_36B1",        # 0E, 14
        "Function_15_3725",        # 0F, 15
        "Function_16_3797",        # 10, 16
        "Function_17_3822",        # 11, 17
        "Function_18_382C",        # 12, 18
        "Function_19_3B64",        # 13, 19
        "Function_20_3BB0",        # 14, 20
        "Function_21_5112",        # 15, 21
        "Function_22_5159",        # 16, 22
        "Function_23_51A7",        # 17, 23
        "Function_24_64C4",        # 18, 24
        "Function_25_657E",        # 19, 25
        "Function_26_6817",        # 1A, 26
        "Function_27_68A1",        # 1B, 27
        "Function_28_68F2",        # 1C, 28
        "Function_29_693E",        # 1D, 29
        "Function_30_845F",        # 1E, 30
        "Function_31_8814",        # 1F, 31
        "Function_32_94C4",        # 20, 32
        "Function_33_A211",        # 21, 33
        "Function_34_A738",        # 22, 34
        "Function_35_A7C2",        # 23, 35
        "Function_36_A813",        # 24, 36
        "Function_37_A864",        # 25, 37
        "Function_38_A8B5",        # 26, 38
        "Function_39_A901",        # 27, 39
        "Function_40_B033",        # 28, 40
        "Function_41_B098",        # 29, 41
        "Function_42_B0FD",        # 2A, 42
        "Function_43_B162",        # 2B, 43
        "Function_44_B1C7",        # 2C, 44
        "Function_45_BCFA",        # 2D, 45
        "Function_46_C018",        # 2E, 46
        "Function_47_C394",        # 2F, 47
        "Function_48_C6D9",        # 30, 48
        "Function_49_C731",        # 31, 49
        "Function_50_C789",        # 32, 50
        "Function_51_C7E1",        # 33, 51
        "Function_52_C80B",        # 34, 52
        "Function_53_C863",        # 35, 53
        "Function_54_C98F",        # 36, 54
        "Function_55_C9F4",        # 37, 55
        "Function_56_CA3F",        # 38, 56
    ))


    def Function_0_980(): pass

    label("Function_0_980")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_9C0"),
        (1, "loc_9CC"),
        (2, "loc_9D8"),
        (3, "loc_9E4"),
        (4, "loc_9F0"),
        (5, "loc_9FC"),
        (6, "loc_A08"),
        (SWITCH_DEFAULT, "loc_A14"),
    )


    label("loc_9C0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A20")

    label("loc_9CC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A20")

    label("loc_9D8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A20")

    label("loc_9E4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A20")

    label("loc_9F0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A20")

    label("loc_9FC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A20")

    label("loc_A08")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A20")

    label("loc_A14")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A20")

    label("loc_A20")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A37")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A20")

    label("loc_A37")

    Return()

    # Function_0_980 end

    def Function_1_A38(): pass

    label("Function_1_A38")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A84")
    OP_95(0xFE, 11850, 0, -1800, 2000, 0x0)
    OP_95(0xFE, 11850, 0, 39440, 2000, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 30000, 0, -3010, 270)
    Jump("Function_1_A38")

    label("loc_A84")

    Return()

    # Function_1_A38 end

    def Function_2_A85(): pass

    label("Function_2_A85")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AAF")
    OP_94(0xFE, 0x366, 0xFFFFE296, 0xFFFFF236, 0xFFFFD166, 0x3E8)
    Sleep(300)
    Jump("Function_2_A85")

    label("loc_AAF")

    Return()

    # Function_2_A85 end

    def Function_3_AB0(): pass

    label("Function_3_AB0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ADA")
    OP_94(0xFE, 0xFFFFA484, 0xFFFFB348, 0xFFFFA722, 0xFFFFB9BA, 0x3E8)
    Sleep(300)
    Jump("Function_3_AB0")

    label("loc_ADA")

    Return()

    # Function_3_AB0 end

    def Function_4_ADB(): pass

    label("Function_4_ADB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B05")
    OP_94(0xFE, 0xFFFFBE2E, 0x2184, 0xFFFFB38E, 0x1054, 0x3E8)
    Sleep(300)
    Jump("Function_4_ADB")

    label("loc_B05")

    Return()

    # Function_4_ADB end

    def Function_5_B06(): pass

    label("Function_5_B06")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1217")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC8")
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    SetChrPos(0x1, -26950, -1160, -4340, 90)
    SetChrPos(0x2, -26950, -1160, -4340, 90)
    SetChrPos(0x3, -26950, -1160, -4340, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9B")
    SetChrPos(0x4, -26950, -1160, -4340, 90)
    SetChrPos(0x5, -26950, -1160, -4340, 90)
    Jump("loc_BBA")

    label("loc_B9B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBA")
    SetChrPos(0x4, -26950, -1160, -4340, 90)

    label("loc_BBA")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1217")

    label("loc_BC8")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7C")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C4F")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_C6E")

    label("loc_C4F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C6E")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_C6E")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1217")

    label("loc_C7C")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D30")
    SetChrPos(0x0, 11850, 0, 28440, 180)
    SetChrPos(0x1, 11850, 0, 28440, 180)
    SetChrPos(0x2, 11850, 0, 28440, 180)
    SetChrPos(0x3, 11850, 0, 28440, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D03")
    SetChrPos(0x4, 11850, 0, 28440, 180)
    SetChrPos(0x5, 11850, 0, 28440, 180)
    Jump("loc_D22")

    label("loc_D03")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D22")
    SetChrPos(0x4, 11850, 0, 28440, 180)

    label("loc_D22")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1217")

    label("loc_D30")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE4")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB7")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_DD6")

    label("loc_DB7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD6")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_DD6")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1217")

    label("loc_DE4")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E98")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E6B")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_E8A")

    label("loc_E6B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E8A")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_E8A")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1217")

    label("loc_E98")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4C")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F1F")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_F3E")

    label("loc_F1F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F3E")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_F3E")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1217")

    label("loc_F4C")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1000")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FD3")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_FF2")

    label("loc_FD3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF2")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_FF2")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1217")

    label("loc_1000")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B4")
    SetChrPos(0x0, 4040, 0, -21980, 0)
    SetChrPos(0x1, 4040, 0, -21980, 0)
    SetChrPos(0x2, 4040, 0, -21980, 0)
    SetChrPos(0x3, 4040, 0, -21980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1087")
    SetChrPos(0x4, 4040, 0, -21980, 0)
    SetChrPos(0x5, 4040, 0, -21980, 0)
    Jump("loc_10A6")

    label("loc_1087")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A6")
    SetChrPos(0x4, 4040, 0, -21980, 0)

    label("loc_10A6")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1217")

    label("loc_10B4")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1168")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_113B")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_115A")

    label("loc_113B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_115A")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_115A")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1217")

    label("loc_1168")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1217")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11EF")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_120E")

    label("loc_11EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_120E")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_120E")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1217")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_122E")
    Jump("loc_133C")

    label("loc_122E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1241")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_133C")

    label("loc_1241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_124F")
    Jump("loc_133C")

    label("loc_124F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_125D")
    Jump("loc_133C")

    label("loc_125D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1275")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_133C")

    label("loc_1275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1288")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_133C")

    label("loc_1288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_12A0")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_133C")

    label("loc_12A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_12B8")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_133C")

    label("loc_12B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_12C6")
    Jump("loc_133C")

    label("loc_12C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_12D9")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_133C")

    label("loc_12D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_12EC")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_133C")

    label("loc_12EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_12FF")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_133C")

    label("loc_12FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_130D")
    Jump("loc_133C")

    label("loc_130D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_131B")
    Jump("loc_133C")

    label("loc_131B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_132E")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_133C")

    label("loc_132E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_133C")
    ClearChrFlags(0x11, 0x80)

    label("loc_133C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1350")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)
    Jump("loc_1485")

    label("loc_1350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1361")
    ClearScenarioFlags(0x5C, 1)
    Jump("loc_1485")

    label("loc_1361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_1375")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 18)
    Jump("loc_1485")

    label("loc_1375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_1389")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 20)
    Jump("loc_1485")

    label("loc_1389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_139D")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 23)
    Jump("loc_1485")

    label("loc_139D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_13B1")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 25)
    Jump("loc_1485")

    label("loc_13B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 6)), scpexpr(EXPR_END)), "loc_13C2")
    ClearScenarioFlags(0x5C, 6)
    Jump("loc_1485")

    label("loc_13C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 7)), scpexpr(EXPR_END)), "loc_13D6")
    ClearScenarioFlags(0x5C, 7)
    Event(0, 30)
    Jump("loc_1485")

    label("loc_13D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 0)), scpexpr(EXPR_END)), "loc_13EA")
    ClearScenarioFlags(0x5D, 0)
    Event(0, 31)
    Jump("loc_1485")

    label("loc_13EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 1)), scpexpr(EXPR_END)), "loc_13FE")
    ClearScenarioFlags(0x5D, 1)
    Event(0, 33)
    Jump("loc_1485")

    label("loc_13FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 2)), scpexpr(EXPR_END)), "loc_1412")
    ClearScenarioFlags(0x5D, 2)
    Event(0, 39)
    Jump("loc_1485")

    label("loc_1412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 3)), scpexpr(EXPR_END)), "loc_1426")
    ClearScenarioFlags(0x5D, 3)
    Event(0, 44)
    Jump("loc_1485")

    label("loc_1426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 4)), scpexpr(EXPR_END)), "loc_143A")
    ClearScenarioFlags(0x5D, 4)
    Event(0, 45)
    Jump("loc_1485")

    label("loc_143A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 5)), scpexpr(EXPR_END)), "loc_144E")
    ClearScenarioFlags(0x5D, 5)
    Event(0, 46)
    Jump("loc_1485")

    label("loc_144E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 6)), scpexpr(EXPR_END)), "loc_145F")
    ClearScenarioFlags(0x5D, 6)
    Jump("loc_1485")

    label("loc_145F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 7)), scpexpr(EXPR_END)), "loc_1476")
    ClearScenarioFlags(0x5D, 7)
    SetScenarioFlags(0x1, 5)
    Event(0, 47)
    Jump("loc_1485")

    label("loc_1476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 0)), scpexpr(EXPR_END)), "loc_1485")
    ClearScenarioFlags(0x5E, 0)
    Event(1, 17)

    label("loc_1485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_149D")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)

    label("loc_149D")

    Return()

    # Function_5_B06 end

    def Function_6_149E(): pass

    label("Function_6_149E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14ED")

    label("loc_14BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14D6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14ED")

    label("loc_14D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14ED")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14ED")

    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_78(0x9, 0x12)
    OP_D3(0x12, 0x0, 0x3BD08, 0x0, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1542")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1555")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1555")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1569")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15BA")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_162B")

    label("loc_15BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1606")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_162B")

    label("loc_1606")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_162B")

    OP_10(0xB, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1641")
    OP_70(0xA, 0x0)
    Jump("loc_1645")

    label("loc_1641")

    OP_70(0xA, 0x1E)

    label("loc_1645")

    SetMapObjFlags(0xB, 0x4)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16B8")
    ClearMapObjFlags(0xB, 0x4)
    OP_78(0xB, 0x18)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    SetChrPos(0x18, 6000, 0, -16200, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    OP_74(0xB, 0x1E)
    OP_70(0xB, 0x0)
    OP_66(0x3, 0x1)
    Jump("loc_16BD")

    label("loc_16B8")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_16BD")

    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    OP_1B(0x3, 0xFF, 0xFFFF)
    OP_1B(0x4, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16FD")
    OP_1B(0x0, 0x0, 0x30)
    OP_1B(0x1, 0x0, 0x31)
    OP_1B(0x2, 0x0, 0x32)
    OP_1B(0x3, 0x0, 0x33)
    OP_1B(0x4, 0x0, 0x34)

    label("loc_16FD")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1715")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1737")
    OP_1B(0x0, 0x0, 0x30)
    OP_1B(0x1, 0x0, 0x31)
    OP_1B(0x2, 0x0, 0x32)
    OP_1B(0x4, 0x0, 0x34)

    label("loc_1737")

    Return()

    # Function_6_149E end

    def Function_7_1738(): pass

    label("Function_7_1738")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186C")
    Sound(14, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xA, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 30)
    AddSepith(0x1, 30)
    AddSepith(0x2, 30)
    AddSepith(0x3, 30)
    AddSepith(0x4, 30)
    AddSepith(0x5, 30)
    AddSepith(0x6, 30)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x30\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x30\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x30\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x30\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x30\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x30\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x30.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x111, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1950")

    label("loc_186C")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Did you know? The Bell of Crossbell was recovered in S1185,\x01",
            "but it was known of long before researchers relocated it.\x02\x03",
            "Its documented history dates back to the Middle Ages, and\x01",
            "it helped inspire the name 'Crossbell'.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1950")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1738 end

    def Function_8_1962(): pass

    label("Function_8_1962")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　              Bell of Crossbell\x01",
            "This enormous bell was excavated in\x01",
            "Crossbell State in S1185. It is estimated to\x01",
            "have been forged during the Middle Ages,\x01",
            "using multiple metal alloys. When struck,\x01",
            "it emits a low, yet pleasant ring.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is theorized that the bell was created by\x01",
            "some influential person of the times, but its\x01",
            "true purpose remains shrouded in mystery.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_1962 end

    def Function_9_1B0F(): pass

    label("Function_9_1B0F")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a ladder.\x01",
            "Climb down?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B6A")
    EventEnd(0x5)
    NewScene("m0000", 125, 0, 0)
    IdleLoop()
    Jump("loc_1B6C")

    label("loc_1B6A")

    EventEnd(0x5)

    label("loc_1B6C")

    Return()

    # Function_9_1B0F end

    def Function_10_1B6D(): pass

    label("Function_10_1B6D")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_213E")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20DB")
    Sound(1500, 255, 100, 0)
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C13")
    MenuCmd(1, 1, "★City - Central Square")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1C2E")

    label("loc_1C13")

    MenuCmd(1, 1, "　City - Central Square")

    label("loc_1C2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C5C")
    MenuCmd(1, 1, "★City - East Exit")
    MenuCmd(3, 1, 0x1)
    Jump("loc_1C72")

    label("loc_1C5C")

    MenuCmd(1, 1, "　City - East Exit")

    label("loc_1C72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA0")
    MenuCmd(1, 1, "★City - West Exit")
    MenuCmd(3, 1, 0x2)
    Jump("loc_1CB6")

    label("loc_1CA0")

    MenuCmd(1, 1, "　City - West Exit")

    label("loc_1CB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE5")
    MenuCmd(1, 1, "★City - South Exit")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1CFC")

    label("loc_1CE5")

    MenuCmd(1, 1, "　City - South Exit")

    label("loc_1CFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D2B")
    MenuCmd(1, 1, "★City - North Exit")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1D42")

    label("loc_1D2B")

    MenuCmd(1, 1, "　City - North Exit")

    label("loc_1D42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D6C")
    MenuCmd(1, 1, "★Tangram Gate")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1D7E")

    label("loc_1D6C")

    MenuCmd(1, 1, "　Tangram Gate")

    label("loc_1D7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DAA")
    MenuCmd(1, 1, "★Bellguard Gate")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1DBE")

    label("loc_1DAA")

    MenuCmd(1, 1, "　Bellguard Gate")

    label("loc_1DBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DF6")
    MenuCmd(1, 1, "★St. Ursula Medical College")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1E16")

    label("loc_1DF6")

    MenuCmd(1, 1, "　St. Ursula Medical College")

    label("loc_1E16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E44")
    MenuCmd(1, 1, "★Armorica Village")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1E5A")

    label("loc_1E44")

    MenuCmd(1, 1, "　Armorica Village")

    label("loc_1E5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E8C")
    MenuCmd(1, 1, "★Mainz Mining Village")
    MenuCmd(3, 1, 0x9)
    Jump("loc_1EA6")

    label("loc_1E8C")

    MenuCmd(1, 1, "　Mainz Mining Village")

    label("loc_1EA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EE0")
    MenuCmd(1, 1, "★Mainz Mountain Path - Tunnel")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1F02")

    label("loc_1EE0")

    MenuCmd(1, 1, "　Mainz Mountain Path - Tunnel")

    label("loc_1F02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F31")
    MenuCmd(1, 1, "★Stargazer's Tower")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1F48")

    label("loc_1F31")

    MenuCmd(1, 1, "　Stargazer's Tower")

    label("loc_1F48")

    MenuCmd(1, 1, "　Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20CC")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0xB)
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
        (0, "loc_201F"),
        (1, "loc_202D"),
        (2, "loc_203B"),
        (3, "loc_2049"),
        (4, "loc_2057"),
        (5, "loc_2065"),
        (6, "loc_2073"),
        (7, "loc_2081"),
        (8, "loc_208F"),
        (9, "loc_209D"),
        (10, "loc_20AB"),
        (11, "loc_20B9"),
        (SWITCH_DEFAULT, "loc_20C7"),
    )


    label("loc_201F")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_20C7")

    label("loc_202D")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_20C7")

    label("loc_203B")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_20C7")

    label("loc_2049")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_20C7")

    label("loc_2057")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_20C7")

    label("loc_2065")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_20C7")

    label("loc_2073")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_20C7")

    label("loc_2081")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_20C7")

    label("loc_208F")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_20C7")

    label("loc_209D")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_20C7")

    label("loc_20AB")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_20C7")

    label("loc_20B9")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_20C7")

    label("loc_20C7")

    Jump("loc_20D6")

    label("loc_20CC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20D6")

    Jump("loc_2139")

    label("loc_20DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2126")
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
    Jump("loc_2139")

    label("loc_2126")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2139")

    Jump("loc_1B87")

    label("loc_213E")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1B6D end

    def Function_11_2146(): pass

    label("Function_11_2146")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 2400, 0, -16530, 270)
    SetChrPos(0x1, 2400, 0, -16530, 270)
    SetChrPos(0x2, 2400, 0, -16530, 270)
    SetChrPos(0x3, 2400, 0, -16530, 270)
    SetChrPos(0x4, 2400, 0, -16530, 270)
    SetChrPos(0x5, 2400, 0, -16530, 270)
    Sleep(1)
    OP_68(2400, 1900, -16530, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(21500, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_221A")
    Sound(1502, 255, 100, 0)
    Jump("loc_2220")

    label("loc_221A")

    Sound(1503, 255, 100, 0)

    label("loc_2220")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_2146 end

    def Function_12_2235(): pass

    label("Function_12_2235")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Return()

    # Function_12_2235 end

    def Function_13_2243(): pass

    label("Function_13_2243")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50003.itc", 0x1E)
    LoadChrToIndex("apl/ch50004.itc", 0x1F)
    LoadChrToIndex("apl/ch50005.itc", 0x20)
    LoadChrToIndex("chr/ch20800.itc", 0x21)
    LoadChrToIndex("chr/ch20900.itc", 0x22)
    LoadChrToIndex("chr/ch21100.itc", 0x23)
    SoundLoad(803)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_68(-18000, 2000, 7500, 0)
    MoveCamera(28, 9, 0, 0)
    OP_6E(820, 0)
    SetCameraDistance(13000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 2900, 0, -21300, 0)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x16, 2600, 0, -23600, 0)
    SetChrPos(0x17, 3700, 0, -23800, 0)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -16700, 0, 2500, 315)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 7100, 0, -16600, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 200, 0, -2300, 270)
    SetChrPos(0xB, -1100, 0, -2300, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, -6300, 0, -9200, 135)
    SetChrPos(0x10, -5300, 0, -10200, 315)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, -4300, 0, 17300, 270)
    SetChrPos(0xD, -6200, 0, 17300, 90)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -6300, 100, 4300, 270)
    OP_4B(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 0)
    OP_4B(0xB, 0xFF)
    BeginChrThread(0xB, 0, 0, 0)
    OP_4B(0x11, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x8, 0x18)
    OP_78(0x9, 0x19)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    SetMapObjFlags(0x8, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x18, 0x4)
    ClearChrFlags(0x19, 0x4)
    OP_49()
    SetChrPos(0x18, 11500, 0, 19500, 0)
    OP_D3(0x18, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x19, 0, 0, 14000, 0)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    OP_70(0x9, 0x1E)
    OP_E5()
    Sound(803, 2, 0, 0)
    BeginChrThread(0x23, 1, 0, 55)
    OP_68(-17000, 2000, 7000, 9000)
    MoveCamera(18, 9, 0, 9000)
    SetCameraDistance(17000, 9000)
    BeginChrThread(0x11, 3, 0, 16)
    FadeToBright(2000, 0)
    OP_0D()
    BeginChrThread(0x19, 3, 0, 14)
    BeginChrThread(0x23, 2, 0, 17)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)
    Sleep(300)
    Fade(500)
    OP_68(2500, 1900, -1600, 0)
    MoveCamera(42, 5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(27000, 0)
    ClearMapObjFlags(0x8, 0x4)
    SetCameraDistance(32000, 8000)
    BeginChrThread(0x18, 3, 0, 15)
    OP_6F(0x10)
    Fade(1000)
    PlaceName2(340, 200, "c_plac02", 0x0, 1500)
    OP_68(0, 800, 4000, 0)
    MoveCamera(18, 22, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(28000, 0)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    MoveCamera(42, 22, 0, 9000)
    SetCameraDistance(33000, 9000)
    OP_6F(0x40)
    OP_6F(0x10)
    Fade(500)
    OP_68(3400, 800, -12300, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    Sleep(1)
    SetCameraDistance(19000, 5000)
    EndChrThread(0x23, 0x1)
    BeginChrThread(0x23, 1, 0, 56)

    def lambda_2693():
        OP_95(0xFE, 2900, 0, -11300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2693)
    Sleep(100)

    def lambda_26B0():
        OP_95(0xFE, 2600, 0, -13600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_26B0)
    Sleep(50)

    def lambda_26CD():
        OP_95(0xFE, 3700, 0, -13800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_26CD)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x50, 0x1F4)
    Sleep(500)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x23, 0x2)
    OP_E6()
    Sound(1080, 255, 90, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0100122V#0005F#5PWow. Things really have changed.\x02\x03",
            "#0100123V#0012FI can hardly even recognize the shops.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    ChrTalk(
        0x101,
        "#0100124V#0005F#5POh? What's that building over there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0100125V#12PThat's the orbal store.\x01",
            "It reopened just last year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0100126V#12PThey handle everything, from the\x01",
            "latest orbal devices to orbal cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0100127V#12PThey got doodads from Erebonia,\x01",
            "Calvard, Liberl...even Epstein.\x01",
            "You name it, they've got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#0100128V#0006F#5PThat's pretty impressive.\x02\x03",
            "#0100129V#0000FYou know, I've also noticed a lot more cars\x01",
            "on the streets.\x02\x03",
            "#0100130VYou would hardly see them three years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#0100131VYou're sharp, you. But, even now,\x01",
            "they're only ever used by rich folk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#0100132VLucky for us, public transportation has\x01",
            "improved dramatically over the years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#0100133VIt only takes 30 minutes to reach\x01",
            "the hospital to the south by bus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100134V#0002F#5PHow convenient.\x02\x03",
            "#0100135V#0004FIt's amazing how much can change\x01",
            "in just three years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#0100136V#12PWell, let's say our goodbyes here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#0100137V#12PYou still have to report in for your job, right?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#0100138V#0005F#5POh, right.\x02\x03",
            "#0100139VLet me carry your luggage home,\x01",
            "at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#0100140VOh, no. We could never\x01",
            "ask you to do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#0100141VThe last thing we want is for you\x01",
            "to be late to your first day of work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0100142V#12PShe's right. No matter what you do, first\x01",
            "impressions last. Remember that, son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100143V#0012F#5POkay, I give up. You make a good point.\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 2700, 0, -12500, 2000, 0x0)
    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    OP_96(0x101, 0xB54, 0x0, 0xFFFFD3DC, 0x7D0, 0x0)

    ChrTalk(
        0x16,
        (
            "#0100144V#12PAh, that reminds me. Seeing as you just\x01",
            "returned, do you have a place to stay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0100145V#12PIf you don't, I can introduce you to the\x01",
            "inn over on East Street. Lovely place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100146V#0002F#5PI appreciate the offer, but I already have\x01",
            "accomodations set up.\x02\x03",
            "#0100147VMy things have probably already arrived\x01",
            "there by now, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#0100148V#12POh, you don't say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#0100149VWell, the two of us live near\x01",
            "the end of East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#0100150VFeel free to drop by in case you need anything.\x01",
            "We'd be more than happy to lend you a hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100151V#0009F#5PThanks. I'll remember that.\x02\x03",
            "#0100152V#0002FOnce I'm settled in, I'll make sure\x01",
            "to stop by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#0100153V#12POf course. Take care, lad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#0100154VHope to see you soon, dear.\x02",
    )

    CloseMessageWindow()
    OP_92(0x16, 0x2E18, 0xFFFFEB4C, 0x1F4)

    def lambda_3054():
        OP_95(0xFE, 11800, 0, -5300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3054)
    Sleep(300)

    def lambda_3071():

        label("loc_3071")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_3071")

    QueueWorkItem2(0x101, 2, lambda_3071)
    Sleep(200)
    OP_92(0x17, 0x2C24, 0xFFFFE4A8, 0x1F4)

    def lambda_3093():
        OP_95(0xFE, 11300, 0, -7000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3093)
    WaitChrThread(0x16, 1)

    def lambda_30B1():
        OP_95(0xFE, 21800, 0, -5300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_30B1)
    WaitChrThread(0x17, 1)

    def lambda_30CF():
        OP_95(0xFE, 21300, 0, -7000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_30CF)
    Sleep(1000)
    EndChrThread(0x101, 0x2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        "#0100155V#0005F#11PWait a minute...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    OP_68(-25800, -1600, -16400, 3500)
    MoveCamera(45, 14, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(30500, 3500)
    OP_6F(0x79)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#0100156V#0000FSo it's still in one piece?\x02\x03",
            "#0100157VI wonder if the Crossbell Times moved into\x01",
            "something less decrepit by now.\x02\x03",
            "#0100158V#0012FSure brings back memories. It really sticks out\x01",
            "next to all these new buildings, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(3120, 800, -11310, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0100159V#0003F#11PWell, then, better get a move on.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd took out a letter from his pocket.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Officer Lloyd Bannings,\x01",
            "You are assigned to the Crossbell Police\x01",
            "Department's Special Support Section. Please\x01",
            "report in for duty on the designated date.\x01",
            "                                   - CPD HR Department\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        (
            "#0100160V#0001F#11PSpecial Support Section? I don't remember that\x01",
            "name ever popping up during my time at the\x01",
            "police academy.\x02\x03",
            "#0100161VI wasn't even sent a uniform. I wonder what kind\x01",
            "of division it's supposed to be...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0100162V#0004F#11POh, well. I guess I'll find out soon enough.\x02\x03",
            "#0100163VGood thing the police department hasn't\x01",
            "moved since I was here last.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)
    Sound(1000, 255, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#0100164V#0000F#11PAll right! Let's do this!\x02",
    )

    CloseMessageWindow()

    def lambda_3641():
        OP_95(0xFE, 9000, 0, 4000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3641)
    Sleep(2000)
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    OP_6F(0x10)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2243 end

    def Function_14_36B1(): pass

    label("Function_14_36B1")

    Sleep(1000)
    Sound(461, 0, 70, 0)
    OP_71(0x9, 0x1F, 0x3C, 0x0, 0x0)
    OP_79(0x9)
    Sleep(1000)
    OP_71(0x9, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x9)

    def lambda_36E0():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_36E0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    WaitChrThread(0x19, 2)

    def lambda_370B():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_370B)
    WaitChrThread(0x19, 1)
    Return()

    # Function_14_36B1 end

    def Function_15_3725(): pass

    label("Function_15_3725")


    def lambda_372A():
        OP_96(0xFE, 0x2CEC, 0x0, 0x1964, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_372A)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    WaitChrThread(0x18, 1)
    WaitChrThread(0x19, 2)
    Sound(458, 0, 100, 0)

    def lambda_375E():
        OP_9E(0xFE, 0x0, 0x1964, 0x15F90, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_375E)
    WaitChrThread(0x18, 1)

    def lambda_377D():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_377D)
    WaitChrThread(0x18, 1)
    Return()

    # Function_15_3725 end

    def Function_16_3797(): pass

    label("Function_16_3797")


    def lambda_379C():
        OP_95(0xFE, -21700, 100, 7500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_379C)
    WaitChrThread(0x11, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x6, 0x10)
    OP_71(0x6, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x6)

    def lambda_37D5():
        OP_95(0xFE, -22700, 0, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_37D5)

    def lambda_37EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_37EF)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x11, 2)
    Sleep(500)
    Sound(104, 0, 100, 0)
    OP_71(0x6, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x6)
    SetMapObjFlags(0x6, 0x10)
    Return()

    # Function_16_3797 end

    def Function_17_3822(): pass

    label("Function_17_3822")

    Sleep(4000)
    Sound(457, 0, 100, 0)
    Return()

    # Function_17_3822 end

    def Function_18_382C(): pass

    label("Function_18_382C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28100.itc", 0x1E)
    LoadChrToIndex("chr/ch21200.itc", 0x1F)
    LoadChrToIndex("chr/ch21400.itc", 0x20)
    LoadChrToIndex("chr/ch20000.itc", 0x21)
    LoadChrToIndex("chr/ch23600.itc", 0x22)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xB4, 0xD7, 0xE6, 0xF, 0x82, 0x0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x9, 0x18)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, 15000, 0, -3000, 0)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, -15000, 0, -6300, 90)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -6800, 0, 4000, 270)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -8300, 0, 2500, 90)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -19300, 0, 19400, 180)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, 7000, 0, 12000, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)

    def lambda_3A6B():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3A6B)

    def lambda_3A85():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3A85)

    def lambda_3A9F():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_3A9F)
    Sound(458, 0, 100, 0)

    def lambda_3AC0():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3AC0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 19)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x23, 0x1)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 2)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_382C end

    def Function_19_3B64(): pass

    label("Function_19_3B64")

    Sound(803, 2, 100, 0)
    Sleep(4000)
    OP_25(0x323, 0x5A)
    Sleep(100)
    OP_25(0x323, 0x50)
    Sleep(100)
    OP_25(0x323, 0x46)
    Sleep(100)
    OP_25(0x323, 0x3C)
    Sleep(100)
    OP_25(0x323, 0x32)
    Sleep(100)
    OP_25(0x323, 0x28)
    Sleep(100)
    OP_25(0x323, 0x1E)
    Sleep(100)
    OP_25(0x323, 0x14)
    Sleep(100)
    OP_25(0x323, 0xA)
    Sleep(100)
    OP_24(0x323)
    Return()

    # Function_19_3B64 end

    def Function_20_3BB0(): pass

    label("Function_20_3BB0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09300.itc", 0x1E)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    OP_78(0x8, 0x18)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x18, 25000, 0, -2600, 270)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1F, 0x3)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -9300, 0, -7200, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x2)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -9700, 0, -5500, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0xF)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -14500, 0, -500, 90)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, -15500, 0, 1000, 90)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)

    def lambda_3D6D():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3D6D)

    def lambda_3D87():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_3D87)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 19)
    FadeToBright(2000, 0)

    def lambda_3DC1():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF5D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3DC1)
    Sleep(2000)

    def lambda_3DDE():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF5D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3DDE)
    Sleep(1000)
    Sound(456, 0, 100, 0)

    def lambda_3E01():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF5D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3E01)
    Sleep(1000)

    def lambda_3E1E():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF5D8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3E1E)
    WaitChrThread(0x18, 1)
    OP_6F(0x79)
    OP_71(0x8, 0x5B, 0x78, 0x1, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_79(0x8)
    OP_68(0, 1000, -6600, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -600, 0, -7800, 0)
    SetChrPos(0x102, 700, 0, -7800, 0)
    SetChrPos(0x103, -600, 0, -9100, 0)
    SetChrPos(0x104, 700, 0, -9100, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    SetChrPos(0x1A, 0, 0, -5500, 180)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrPos(0x18, 0, 0, -2600, 270)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    ClearChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    OP_70(0x8, 0x1E)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#1100721V#12P#0002FThanks for driving us all the way back\x01",
            "to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#1100722V#3609F#5POh, it was nothing. It was on the way,\x01",
            "so why not travel in good company?\x02\x03",
            "#1100723V#3600FWell, best of luck with your investigation.\x02\x03",
            "#1100724VYou have my full support!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100725V#0102FThank you very much, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100726V#12P#0202FIf you're rooting for us, then please consider\x01",
            "the SSS for any hired help you may need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100727V#0309FWhat she said. Remember us before\x01",
            "you turn to the Bracer Guild, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_419F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_419F)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_41C1():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_41C1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(500)
    OP_64(0x101)
    OP_64(0x102)

    ChrTalk(
        0x101,
        "#1100728V#1P#0011FStay professional, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100729V#5P#0106FHow subtle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100730V#0302FWhat? Someone's gotta do the PR\x01",
            "for us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100731V#12P#0204FAdvertising is crucial.\x02",
    )

    CloseMessageWindow()

    def lambda_429E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_429E)
    Sleep(50)

    def lambda_42AE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_42AE)

    ChrTalk(
        0x1A,
        (
            "#1100732V#3609F#5PI won't argue that.\x02\x03",
            "#1100733V#3600FIf something comes up, I know where to\x01",
            "find you.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A,
        (
            "#1100734V#3605F#5POh, I have something that might come in handy.\x02\x03",
            "#1100735V#3600FThen again, as police officers, you might find it\x01",
            "unnecessary.\x02",
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
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x6, 1)
    OP_C7(0x1, 0x1000)

    ChrTalk(
        0x102,
        "#1100736V#0105FA map of the city?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#1100737V#3600F#5PIt's something I put together last month to\x01",
            "guide tourists around the city. So, I figure\x01",
            "it might be useful as a city map, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100738V#12P#0002FThis will be really nice to have when\x01",
            "we're patrolling the city.\x02\x03",
            "#1100739V#0004FThanks a lot, Mr. Hayworth. We'll put\x01",
            "it to good use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#1100740V#3609F#5PI'm glad to hear!\x02\x03",
            "#1100741V#3600FWell, then, until we meet again.\x01",
            "Good luck, all of you!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_92(0x1A, 0x0, 0xFFFFEF98, 0x1F4)

    def lambda_4607():
        OP_95(0xFE, 0, 0, -4200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4607)
    WaitChrThread(0x1A, 1)

    def lambda_4625():
        OP_95(0xFE, 0, 0, -3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4625)

    def lambda_463F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_463F)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1A, 2)
    Sound(461, 0, 100, 0)
    OP_71(0x8, 0x1F, 0x3C, 0x0, 0x0)
    OP_79(0x8)

    def lambda_466D():

        label("loc_466D")

        TurnDirection(0x101, 0x18, 500)
        Yield()
        Jump("loc_466D")

    QueueWorkItem2(0x101, 1, lambda_466D)

    def lambda_467F():

        label("loc_467F")

        TurnDirection(0x102, 0x18, 500)
        Yield()
        Jump("loc_467F")

    QueueWorkItem2(0x102, 1, lambda_467F)

    def lambda_4691():

        label("loc_4691")

        TurnDirection(0x103, 0x18, 500)
        Yield()
        Jump("loc_4691")

    QueueWorkItem2(0x103, 1, lambda_4691)

    def lambda_46A3():

        label("loc_46A3")

        TurnDirection(0x104, 0x18, 500)
        Yield()
        Jump("loc_46A3")

    QueueWorkItem2(0x104, 1, lambda_46A3)
    Fade(1000)
    OP_68(0, 500, -2600, 0)
    MoveCamera(30, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    Sound(457, 0, 100, 0)
    OP_71(0x8, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x8)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-10000, 500, -2600, 3000)
    SetCameraDistance(18500, 3000)
    MoveCamera(0, 30, 0, 3000)

    def lambda_472F():
        OP_98(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_472F)
    WaitChrThread(0x18, 1)
    OP_6F(0x11)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x8000)
    ClearMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x8, 0x4)
    Fade(500)
    OP_68(190, 1000, -8370, 0)
    MoveCamera(337, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17580, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#1100742V#11P#0000FWhat a great man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100743V#6P#0204FI agree.\x02\x03",
            "#1100744V#0202FI never thought we would find someone\x01",
            "as altruistic as Lloyd, but here we are.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#1100745V#11P#0006FI'm standing right here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100746V#0303F#12PRemember, he's a trader.\x02\x03",
            "#1100747V#0300FI bet it takes more than bein' nice to run\x01",
            "a successful business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100748V#0104F#2PWell, Mr. Hayworth and his business seem\x01",
            "to be prospering, all while maintaining\x01",
            "cooperation with the locals.\x02\x03",
            "#1100749V#0100FHe really stands out. Most Crossbellan\x01",
            "traders tend to trade abroad.\x02\x03",
            "#1100750VWe need more traders like that, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100751V#0305F#12PDamn. He really is something else, isn't he?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1100752V#11P#0003FWhile he runs an honest business, groups\x01",
            "like Revache are as dirty as they come.\x02\x03",
            "#1100753V#0000FThat's just how Crossbell is nowadays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100754V#0103F#2POf course, there's always the flip side...\x02\x03",
            "#1100755V#0100F...but people like Mr. Hayworth show that\x01",
            "Crossbell isn't all bad. He gives me hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100756V#11P#0004FYeah. I think so, too.\x02",
    )

    CloseMessageWindow()

    def lambda_4BE7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BE7)
    Sleep(100)

    def lambda_4BF7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4BF7)
    Sleep(50)

    def lambda_4C07():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4C07)
    Sleep(50)

    def lambda_4C17():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4C17)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#1100757V#5P#0000FAnyway, it's already past noon.\x02\x03",
            "#1100758VHow about we head to the next place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100759V#0100F#2PWe might as well. St. Ursula Medical\x01",
            "College, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100760V#6P#0203F...\x02\x03",
            "#1100761V#0200FThen we will be heading to the\x01",
            "south exit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100762V#5P#0000FRight. We can take the bus there.\x02\x03",
            "#1100763VI hear it stops by every 30 minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100764V#0305F#12PHey, that's handy dandy!\x02\x03",
            "#1100765V#0300FLet's take a look at the bus stop, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100766V#5P#0000FSounds good.\x02\x03",
            "#1100767V#0004F(St. Ursula... I guess I'm finally going\x01",
            "to see Cecile.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis203.itp")
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Crossbell City map can now be opened.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "While inside the city, press #172I#173I to bring up\x01",
            "a map of the city. (Press #172I#173I again for a map\x01",
            "of the state.)\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you are inside the city, you can use the\x01",
            "map as a shortcut to travel around quickly.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can fast travel to the areas listed on the\x01",
            "left side of the screen.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Be aware that in some situations, fast travel\x01",
            "will be unavailable.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_D5(0x1E)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 0, 0, -7800, 0)
    SetScenarioFlags(0x61, 1)
    OP_29(0x3F, 0x1, 0x5)
    EndChrThread(0x23, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_20_3BB0 end

    def Function_21_5112(): pass

    label("Function_21_5112")

    OP_9F(0x0, 0x18)
    OP_9F(0x1, 17420, 0, -4780)
    OP_9F(0x1, 9540, 0, -2690)
    OP_9F(0x1, 1040, 0, -2580)
    OP_9F(0x2, 0x18, 6000, 0x6)
    OP_71(0x8, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x8)
    Return()

    # Function_21_5112 end

    def Function_22_5159(): pass

    label("Function_22_5159")

    OP_93(0xFE, 0x104, 0x32)
    OP_9F(0x0, 0x18)
    OP_9F(0x1, -5850, 0, -3450)
    OP_9F(0x1, -16290, 0, -3810)
    OP_9F(0x1, -28280, -1380, -3420)
    OP_9F(0x2, 0x18, 6000, 0x6)
    OP_71(0x8, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x8)
    Return()

    # Function_22_5159 end

    def Function_23_51A7(): pass

    label("Function_23_51A7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    LoadChrToIndex("chr/ch28100.itc", 0x1F)
    LoadChrToIndex("chr/ch21200.itc", 0x20)
    LoadChrToIndex("chr/ch21400.itc", 0x21)
    LoadChrToIndex("chr/ch20000.itc", 0x22)
    LoadChrToIndex("chr/ch23600.itc", 0x23)
    LoadEffect(0x0, "event\\eva05_00.eff")
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -30600, -8200, -24900, 270)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x9, 0x18)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, 15000, 0, -3000, 0)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, -15000, 0, -6300, 90)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -6800, 0, 4000, 270)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -8300, 0, 2500, 90)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x22)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -19300, 0, 19400, 180)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x23)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, 7000, 0, 12000, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)

    def lambda_53D9():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_53D9)

    def lambda_53F3():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_53F3)

    def lambda_540D():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_540D)
    Sound(458, 0, 100, 0)

    def lambda_542E():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_542E)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 19)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    SetChrPos(0x101, 10600, 0, 24000, 180)
    SetChrPos(0x102, 12000, 0, 24000, 180)
    SetChrPos(0x103, 10600, 0, 25400, 180)
    SetChrPos(0x104, 12000, 0, 25400, 180)

    def lambda_54BB():
        OP_95(0xFE, 10600, 0, 19000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54BB)
    Sleep(100)

    def lambda_54D8():
        OP_95(0xFE, 12000, 0, 19000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54D8)
    Sleep(100)

    def lambda_54F5():
        OP_96(0xFE, 0x2968, 0x0, 0x4FB0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_54F5)
    Sleep(100)

    def lambda_5512():
        OP_95(0xFE, 12000, 0, 20400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5512)
    Sound(829, 0, 100, 0)
    Fade(1000)
    OP_68(11300, 1000, 19700, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(20500, 3000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetMapObjFlags(0x9, 0x4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#1201009V#6P#0006F*yawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1201010V#0106F#5PSo...sleepy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1201011V#5P#0306FI'll say. We practically pulled an\x01",
            "all-nighter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1201012V#0206FLimit reached. Considering standby.\x02",
    )

    CloseMessageWindow()

    def lambda_56B4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_56B4)
    Sleep(150)

    def lambda_56C4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_56C4)
    Sleep(50)

    def lambda_56D4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_56D4)
    Sleep(50)

    def lambda_56E4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_56E4)
    WaitChrThread(0x104, 2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1201013V#6P#0004FOnce we get back to the SSS building,\x01",
            "we're going to have a good, long rest.\x02\x03",
            "#1201014V#0000FThe chief's report can wait until after\x01",
            "we've recharged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1201015V#0100FA nap sounds lovely right about now.\x02",
    )

    CloseMessageWindow()

    def lambda_57DE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_57DE)
    Sleep(200)

    def lambda_57EE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_57EE)
    Sleep(100)

    def lambda_57FE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_57FE)
    Sleep(100)

    def lambda_580E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_580E)
    WaitChrThread(0x101, 2)

    def lambda_581F():
        OP_95(0xFE, 10600, 0, 8800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_581F)
    WaitChrThread(0x102, 2)

    def lambda_583D():
        OP_95(0xFE, 12000, 0, 8800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_583D)
    WaitChrThread(0x103, 2)

    def lambda_585B():
        OP_96(0xFE, 0x2968, 0x0, 0x27D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_585B)
    WaitChrThread(0x104, 2)

    def lambda_5879():
        OP_95(0xFE, 12000, 0, 10200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5879)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_6F(0x10)
    EndChrThread(0x23, 0x1)
    OP_68(-19000, -7100, -22800, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    OP_90(0x101, -16400, -6350, -19400, 225)
    OP_90(0x102, -15600, -6350, -20200, 225)
    OP_90(0x104, -15200, -5350, -18200, 225)
    OP_90(0x103, -14400, -5350, -19000, 225)
    PlayEffect(0x0, 0x0, 0x1B, 0x140, 0, 1300, 350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_595D():
        OP_95(0xFE, -19700, -8200, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_595D)
    Sleep(50)

    def lambda_597A():
        OP_96(0xFE, 0xFFFFB62C, 0xFFFFDFF8, 0xFFFFA434, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_597A)
    Sleep(50)

    def lambda_5997():
        OP_95(0xFE, -20900, -8200, -23900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5997)
    Sleep(50)

    def lambda_59B4():
        OP_95(0xFE, -20100, -8200, -24700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_59B4)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_59DC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_59DC)
    WaitChrThread(0x102, 1)

    def lambda_59ED():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_59ED)
    WaitChrThread(0x103, 1)

    def lambda_59FE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_59FE)
    WaitChrThread(0x104, 1)

    def lambda_5A0F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5A0F)
    OP_6F(0x11)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#1201016V#11P#0105FOh?\x02",
    )

    CloseMessageWindow()
    OP_68(-28620, -7100, -24980, 2000)
    MoveCamera(35, 23, 0, 2000)
    SetCameraDistance(17000, 2000)
    OP_6F(0x79)
    OP_93(0x1B, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1B,
        "#1201017V#6P#1002FYo. Job well done.\x02",
    )

    CloseMessageWindow()
    OP_68(-29600, -7100, -24900, 2000)

    def lambda_5AF1():
        OP_96(0xFE, 0xFFFF9048, 0xFFFFDFF8, 0xFFFFA0B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5AF1)
    Sleep(50)

    def lambda_5B0E():
        OP_96(0xFE, 0xFFFF9048, 0xFFFFDFF8, 0xFFFF9C64, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B0E)
    Sleep(50)

    def lambda_5B2B():
        OP_96(0xFE, 0xFFFF95C0, 0xFFFFDFF8, 0xFFFFA0B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B2B)
    Sleep(50)

    def lambda_5B48():
        OP_96(0xFE, 0xFFFF95C0, 0xFFFFDFF8, 0xFFFF9C64, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B48)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#1201018V#11P#0011FChief? Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1201019V#0302FDon't tell me you went out of your way\x01",
            "to welcome us back. How adorable.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5D3E")

    ChrTalk(
        0x1B,
        (
            "#1201020V#6P#1011FHah! As if I would do something as sappy as\x01",
            "that.\x02\x03",
            "#1201021V#1002FSonya just gave me a call and filled me in on\x01",
            "what happened.\x02\x03",
            "#1201022VSounds like you didn't do too shabby on your\x01",
            "first job outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1201023V#11P#0000FTh-Thanks?\x01",
            "(That WAS a compliment, right?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6016")

    label("loc_5D3E")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5EA8")

    ChrTalk(
        0x1B,
        (
            "#1201020V#6P#1011FHah! As if I would do something as sappy as\x01",
            "that.\x02\x03",
            "#1201021V#1002FSonya just gave me a call and filled me in on\x01",
            "what happened.\x02\x03",
            "#1201024V#1004FSounds to me like Lady Luck played a major\x01",
            "part in your success today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1201025V#11P#0005FYou could say that. (He's right. In the end, we\x01",
            "couldn't finish what we started.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6016")

    label("loc_5EA8")


    ChrTalk(
        0x1B,
        (
            "#1201020V#6P#1011FHah! As if I would do something as sappy as\x01",
            "that.\x02\x03",
            "#1201021V#1002FSonya just gave me a call and filled me in on\x01",
            "what happened.\x02\x03",
            "#1201026V#1003FSounds like you relied on Lady Luck a bit too\x01",
            "much. But hey, it's the result that counts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1201027V#11P#0006FSorry, Chief. (I want to defend us, but I can't\x01",
            "come up with any legitimate excuses.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6016")

    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x102,
        (
            "#1201028V#11P#0100FIf you weren't waiting for us, what were you\x01",
            "doing out here, Chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1201029V#11P#0200FIt is quite the unusual location for your\x01",
            "post-breakfast smoke, is it not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#1201030V#6P#1011FI can't help it, okay?\x02\x03",
            "#1201031V#1001FHe showed up out of nowhere, so can you\x01",
            "blame me for wanting to take the edge off?\x02",
        )
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
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#1201032V#11P#0005F'He' showed up? Who are you\x01",
            "talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1201033V#0305FYou've got me curious. Spill the beans.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#1201034V#6P#1000FHell if I know. Something just tells me that\x01",
            "he's here for you.\x02\x03",
            "#1201035VHe seems like he's friendly,\x01",
            "but kind of brazen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1201036V#11P#0001FWell...okay, then. So he's waiting\x01",
            "for us inside?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        "#1201037V#12P#0101FTime to see who our mystery guest is.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(400)

    def lambda_6384():

        label("loc_6384")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6384")

    QueueWorkItem2(0x1B, 2, lambda_6384)

    def lambda_6396():

        label("loc_6396")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6396")

    QueueWorkItem2(0x103, 2, lambda_6396)

    def lambda_63A8():

        label("loc_63A8")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_63A8")

    QueueWorkItem2(0x104, 2, lambda_63A8)
    BeginChrThread(0x102, 3, 0, 24)

    def lambda_63C0():
        OP_95(0xFE, -28600, -8200, -22600, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63C0)
    WaitChrThread(0x101, 1)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_63F9():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63F9)
    Sleep(1200)

    def lambda_6411():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6411)
    WaitChrThread(0x101, 2)
    Sleep(300)

    def lambda_6429():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6429)
    WaitChrThread(0x102, 2)
    Sleep(300)

    def lambda_6441():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6441)
    WaitChrThread(0x104, 2)
    FadeToDark(1000, 0, -1)
    Sleep(300)

    def lambda_6463():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6463)
    OP_0D()
    WaitChrThread(0x103, 2)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0x1B, 0x2)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    StopEffect(0x0, 0x0)
    SetScenarioFlags(0x5C, 5)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_51A7 end

    def Function_24_64C4(): pass

    label("Function_24_64C4")

    Sleep(600)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x103, 0x2)

    def lambda_64D4():
        OP_95(0xFE, -29300, -8200, -23000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_64D4)
    Sleep(800)

    def lambda_64F1():
        OP_95(0xFE, -28600, -8200, -24000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_64F1)
    Sleep(100)

    def lambda_650E():
        OP_95(0xFE, -29300, -8200, -24400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_650E)
    WaitChrThread(0x102, 1)

    def lambda_652C():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_652C)
    WaitChrThread(0x104, 1)

    def lambda_654A():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_654A)
    WaitChrThread(0x103, 1)

    def lambda_6568():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6568)
    Return()

    # Function_24_64C4 end

    def Function_25_657E(): pass

    label("Function_25_657E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrPos(0x101, -23800, -8200, -23800, 270)
    SetChrPos(0x104, -23000, -8200, -24600, 270)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x8, 0x18)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    ClearMapObjFlags(0x8, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, -1500, 0, -5500, 0)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    OP_70(0x8, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1F, 0x3)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -9300, 0, -7200, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x2)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -9700, 0, -5500, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0xF)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -14500, 0, -500, 90)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, -15500, 0, 1000, 90)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)

    def lambda_672C():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_672C)

    def lambda_6746():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_6746)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 28)
    FadeToBright(2000, 0)
    Sleep(4850)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 27)
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    EndChrThread(0x23, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 6)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_657E end

    def Function_26_6817(): pass

    label("Function_26_6817")


    def lambda_681C():
        OP_95(0xFE, -28400, -8200, -23800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_681C)
    WaitChrThread(0x101, 1)

    def lambda_683A():
        OP_95(0xFE, -28400, -8200, -22300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_683A)
    WaitChrThread(0x101, 1)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_6873():
        OP_95(0xFE, -28400, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6873)
    Sleep(500)

    def lambda_6890():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6890)
    WaitChrThread(0x101, 1)
    Return()

    # Function_26_6817 end

    def Function_27_68A1(): pass

    label("Function_27_68A1")


    def lambda_68A6():
        OP_95(0xFE, -28800, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_68A6)
    WaitChrThread(0x104, 1)

    def lambda_68C4():
        OP_95(0xFE, -28800, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_68C4)
    Sleep(1500)

    def lambda_68E1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_68E1)
    WaitChrThread(0x104, 1)
    Return()

    # Function_27_68A1 end

    def Function_28_68F2(): pass

    label("Function_28_68F2")

    Sound(803, 2, 100, 0)
    Sleep(5000)
    OP_25(0x323, 0x5A)
    Sleep(200)
    OP_25(0x323, 0x50)
    Sleep(200)
    OP_25(0x323, 0x46)
    Sleep(200)
    OP_25(0x323, 0x3C)
    Sleep(200)
    OP_25(0x323, 0x32)
    Sleep(200)
    OP_25(0x323, 0x28)
    Sleep(200)
    OP_25(0x323, 0x1E)
    Sleep(200)
    OP_25(0x323, 0x14)
    Sleep(200)
    OP_25(0x323, 0xA)
    Sleep(200)
    OP_24(0x323)
    Return()

    # Function_28_68F2 end

    def Function_29_693E(): pass

    label("Function_29_693E")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch02300.itc", 0x1E)
    OP_68(-21100, -7100, -24900, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -20800, -8200, -25500, 270)
    SetChrPos(0x102, -20800, -8200, -24300, 270)
    SetChrPos(0x103, -19400, -8200, -25700, 270)
    SetChrPos(0x104, -19400, -8200, -24500, 270)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -29000, -8200, -24900, 0)
    ModifyEventFlags(0, 0, 0x80)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02600.itp")
    FadeToBright(1000, 0)
    Sleep(600)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#2101412V#11P#0105FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101413V#11P#0005FWait, isn't that...?\x02",
    )

    CloseMessageWindow()
    OP_68(-27700, -7100, -24900, 2500)
    OP_6F(0x1)
    Fade(500)
    OP_68(-27960, -7100, -24530, 0)
    MoveCamera(318, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15420, 0)

    def lambda_6B29():
        OP_95(0xFE, -26800, -8200, -24300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B29)
    Sleep(100)

    def lambda_6B46():
        OP_95(0xFE, -26800, -8200, -25500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B46)
    Sleep(100)

    def lambda_6B63():
        OP_95(0xFE, -25400, -8200, -25700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B63)
    Sleep(100)

    def lambda_6B80():
        OP_95(0xFE, -25400, -8200, -24500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6B80)
    Sleep(500)
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x1C, 0x5A, 0x1F4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x1C,
        (
            "#2101414VOh, thank goodness!\x02\x03",
            "#2101415VI was just starting to wonder if I came\x01",
            "to the wrong place.\x02",
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
            "#2101416V#12P#0105FErnest?\x02\x03",
            "#2101417V#0100FDid you come to see me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#2101418V#5P#2600FYes, I did. I had business to attend to\x01",
            "at the office, so I decided to stop by.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1C,
        (
            "#2101419V#5P#2605FElie?\x02\x03",
            "#2101420V#2601FWhat's wrong? You don't look too great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101421V#12P#0108FWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#2101422V#5P#2603FSo you've gone to see Arc en Ciel\x01",
            "recently...\x02\x03",
            "#2101423V#2601FRelated to your police work, I take it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101424V#12P#0106FW-Well, sort of.\x02\x03",
            "#2101425V#0108FSomeone in the troupe was asking\x01",
            "us for advice, and, um...\x02\x03",
            "#2101426V#0102F...we went to report what we found.\x01",
            "That's all.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1C)

    ChrTalk(
        0x1C,
        (
            "#2101427V#5P#2606FYou know, Elie, I wasn't sure whether\x01",
            "I wanted to come here today or not...\x02\x03",
            "#2101428V#2600F...but I know I made the right decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101429V#12P#0105FWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#2101430V#5P#2603FAllow me to be brutally honest with you.\x02\x03",
            "#2101431V#2601FElie, I want you to quit the force\x01",
            "and return to us.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
        "#2101432V#12P#0105FQuit the force?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101433V#6P#0011F(He wants her to do WHAT?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101434V#12P#0301F(Whoa there, buddy! That came\x01",
            "outta left field!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101435V#12P#0205F(It does not appear to stem from\x01",
            "feelings of love, at least.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#2101436V#5P#2603FI know it was your idea to join\x01",
            "the CPD, Elie.\x02\x03",
            "#2101437V#2601FBut, you have the eyes of a lost lamb.\x01",
            "You look so...exhausted.\x02\x03",
            "#2101438VAsk yourself: Is this really the path you\x01",
            "should be walking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101439V#12P#0108FWh-What are you saying, Ernest?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#2101440V#5P#2603FListen to me. I know you understand the current\x01",
            "political climate, and the despair that comes with\x01",
            "it, better than anyone.\x02\x03",
            "#2101441VAnd that's likely where your initial urge to join\x01",
            "the police originated from.\x02\x03",
            "#2101442V#2601FBut just try to think about the torment and pain\x01",
            "the mayor is going through--how he feels in the\x01",
            "current situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101443V#12P#0105FI never meant for Grandfather to...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#2101444V#5P#2601FThe Anniversary Festival draws nearer with\x01",
            "every passing day, and Mayor MacDowell is\x01",
            "up to his neck with work.\x02\x03",
            "#2101445VAnd after that, it's right back to arguing with\x01",
            "the Imperial and Republican factions over\x01",
            "the budget.\x02\x03",
            "#2101446V#2603FThen, the very next month, he'll be up\x01",
            "for re-election.\x02\x03",
            "#2101447VAs I'm sure you know, Mayor MacDowell has\x01",
            "had plans to retire, but without a suitable\x01",
            "successor, he remains undecided.\x02\x03",
            "#2101448V#2600FI'm sure that if you were by his side, he would\x01",
            "feel much more confident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101449V#12P#0106F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#2101450V#5P#2606FI'm sorry, Elie. Perhaps this was uncalled for.\x02\x03",
            "#2101451VHowever, I can't ignore the issue any longer.\x02\x03",
            "#2101452V#2600FAs someone who respects Mayor MacDowell,\x01",
            "and as your friend, I cannot stand idle any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101453V#12P#0108FErnest...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#2101454V#5P#2604FObviously, what path you choose to follow is\x01",
            "entirely up to you.\x02\x03",
            "#2101455V#2600FAll I want is for you to not regret your decision.\x01",
            "Follow what you know to be right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101456V#12P#0108F#30W...\x02\x03",
            "#2101457V#0106F#40WJust...give me time to think about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2101458V#5P#0102FExcuse me, everyone.\x02\x03",
            "#2101459V#0103FI'm tired, so I'll retire to my room for now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_795F():
        TurnDirection(0xFE, 0x102, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_795F)
    Sleep(50)
    TurnDirection(0x103, 0x102, 300)

    ChrTalk(
        0x101,
        "#2101460V#6P#0005FS-Sure.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)

    def lambda_799C():

        label("loc_799C")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_799C")

    QueueWorkItem2(0x1C, 2, lambda_799C)

    def lambda_79AE():
        OP_95(0xFE, -28600, -8200, -23000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_79AE)
    WaitChrThread(0x102, 1)

    def lambda_79CC():
        OP_95(0xFE, -28600, -8200, -21800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_79CC)
    Sleep(300)

    def lambda_79E9():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_79E9)
    WaitChrThread(0x102, 1)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_7A15():
        OP_95(0xFE, -28600, -8200, -20000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A15)
    Sleep(300)

    def lambda_7A32():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7A32)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x102, 1)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    EndChrThread(0x1C, 0x2)
    Sleep(500)
    OP_93(0x1C, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "#2101461V#5P#2603FMy apologies. I know suddenly showing\x01",
            "up out of the blue wasn't exactly tactful.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7ADF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7ADF)
    Sleep(150)

    def lambda_7AEF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7AEF)
    Sleep(50)
    OP_93(0x104, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#2101462V#6P#0006FIt's okay. It sounds like Elie's situation is\x01",
            "more complicated than we thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101463V#12P#0301FAs long as you stop bothering Mademois-Elie,\x01",
            "we're cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101464V#12P#0203FSeconded.\x02\x03",
            "#2101465V#0211FPersonally, it feels like you are attempting\x01",
            "to take Elie away from us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#2101466V#5P#2604FReally? That wasn't my intention.\x02\x03",
            "#2101467V#2600FStill, you are aware that she wanted to become\x01",
            "a politician before a police officer, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2101468V#6P#0005FA politician? Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2101469V#12P#0305FYou don't say? Our Mademois-Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101470V#12P#0205FThat would explain her seemingly boundless\x01",
            "knowledge of politics and economics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#2101471V#5P#2600FAs the heir of our current mayor, it was only\x01",
            "natural for her to pursue a career in politics.\x02\x03",
            "#2101472V#2603FHer years as an exchange student in so many\x01",
            "nations should've contributed to her talent for\x01",
            "international relations and politics.\x02\x03",
            "#2101473V#2601FHowever, when she returned home last year,\x01",
            "she was dead set on joining the CPD.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101474V#6P#0001FSo that's how it happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101475V#12P#0206FI was unaware.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101476V#12P#0306FI did always wonder why a fancy lady like\x01",
            "herself was workin' for the CPD.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#2101477V#5P#2603FWould you keep an eye on her until she\x01",
            "makes her decision?\x02\x03",
            "#2101478V#2601FShe's too talented--too skilled--to simply\x01",
            "flounder about like this.\x02",
        )
    )

    CloseMessageWindow()
    Sound(856, 0, 100, 0)
    Sleep(1500)
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1C,
        (
            "#2101479V#5P#2605FGoodness, it's already gotten so late.\x02\x03",
            "#2101480V#2600FI'm sorry for taking up so much of your\x01",
            "time. I'll get out of your hair now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101481V#6P#0000FS-See you.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-26080, -6900, -25260, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_68(-23700, -7100, -24900, 6000)

    def lambda_81F2():

        label("loc_81F2")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_81F2")

    QueueWorkItem2(0x101, 2, lambda_81F2)

    def lambda_8204():

        label("loc_8204")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_8204")

    QueueWorkItem2(0x103, 2, lambda_8204)

    def lambda_8216():

        label("loc_8216")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_8216")

    QueueWorkItem2(0x104, 2, lambda_8216)

    def lambda_8228():
        OP_95(0xFE, -27600, -8200, -23500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_8228)
    WaitChrThread(0x1C, 1)

    def lambda_8246():
        OP_95(0xFE, -20600, -8200, -23500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_8246)
    WaitChrThread(0x1C, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    def lambda_8270():
        OP_95(0xFE, -13800, -4200, -16600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_8270)
    WaitChrThread(0x1C, 1)
    OP_6F(0x1)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    OP_68(-26080, -6900, -25260, 1500)
    SetCameraDistance(15000, 1500)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#2101482V#6P#0006F*sigh*\x02",
    )

    CloseMessageWindow()

    def lambda_82DC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_82DC)
    Sleep(50)

    def lambda_82EC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_82EC)
    Sleep(300)

    ChrTalk(
        0x103,
        "#2101483V#0206F#11PYes. Today has been full of such sighs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101484V#5P#0306FWith the wringer we went through today?\x01",
            "Hell, I'd say they're warranted.\x02\x03",
            "#2101485V#0301FMy brain's fried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101486V#6P#0003FYours and mine both, Randy.\x02\x03",
            "#2101487V#0000FAnyway, let's report back to the chief\x01",
            "and call it a day.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetScenarioFlags(0x5D, 0)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_693E end

    def Function_30_845F(): pass

    label("Function_30_845F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02707.itc", 0x1E)
    LoadChrToIndex("chr/ch28100.itc", 0x1F)
    LoadChrToIndex("chr/ch21200.itc", 0x20)
    LoadChrToIndex("chr/ch21400.itc", 0x21)
    LoadChrToIndex("chr/ch20000.itc", 0x22)
    LoadChrToIndex("chr/ch23600.itc", 0x23)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -29000, -8150, -24000, 180)
    BeginChrThread(0x1D, 3, 0, 0)
    OP_52(0x1D, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1D, 0x1)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xB4, 0xD7, 0xE6, 0xF, 0x82, 0x0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x9, 0x18)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, 15000, 0, -3000, 0)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, -15000, 0, -6300, 90)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -6800, 0, 4000, 270)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -8300, 0, 2500, 90)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x22)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -19300, 0, 19400, 180)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x23)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, 7000, 0, 12000, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)

    def lambda_86F5():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_86F5)

    def lambda_870F():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_870F)

    def lambda_8729():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_8729)

    def lambda_8744():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8744)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 19)
    FadeToBright(2000, 0)
    Sleep(500)
    Sound(458, 0, 100, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x23, 0x1)
    OP_52(0x1D, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1D, 0x1)
    SetScenarioFlags(0x5D, 1)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_845F end

    def Function_31_8814(): pass

    label("Function_31_8814")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50109.itc", 0x1E)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x101, 1000, 0, -16800, 90)
    SetChrPos(0x102, 1000, 0, -15600, 90)
    SetChrPos(0x103, -200, 0, -16800, 90)
    SetChrPos(0x104, -200, 0, -15600, 90)
    SetChrPos(0x109, 3200, 0, -16200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_78(0xB, 0x18)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    ClearMapObjFlags(0xB, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, 6000, 0, -16200, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    OP_74(0xB, 0x1E)
    OP_70(0xB, 0x0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x0)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, 0, 0, -5000, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x3)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -9300, 0, -7200, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x2)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -9700, 0, -5500, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0xF)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -4500, 0, 11500, 270)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, -5500, 0, 13000, 270)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    def lambda_8A7D():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8A7D)

    def lambda_8A98():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8A98)

    def lambda_8AB2():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_8AB2)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 28)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(2700, 900, -14200, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    OP_68(2700, 900, -16200, 3000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#2201354V#11P#0500FGood work, everyone!\x02\x03",
            "#2201355V#0506FI just wish I could've been more help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201356V#0102F#6PYou supporting us throughout the tower\x01",
            "was more than enough!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2201357V#0300F#6PAgreed. You helped us out big time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201358V#6P#0204FYou were even gracious enough to\x01",
            "drive us back to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201359V#6P#0002FWe appreciate it, Sergeant Major.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#2201360V#11P#0509FReally? You're very welcome, then.\x02\x03",
            "#2201361V#0501FRemember, you can contact the guardsmen at\x01",
            "Tangram Gate if anything ever comes up.\x02\x03",
            "#2201362VI'll give a report of what happened once\x01",
            "I return to the deputy commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201363V#6P#0000FPerfect. We'd appreciate that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2201364V#0300F#6PSee ya later!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#2201365V#11P#0502FRoger!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    Sleep(150)
    Sound(1483, 255, 90, 0)
    Sleep(1800)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_92(0x109, 0xE74, 0xFFFFBEC4, 0x1F4)

    def lambda_8E58():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFBEC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8E58)
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0x5A, 0x1F4)
    OP_71(0xB, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0xB)
    SetChrFlags(0x109, 0x4)

    def lambda_8E97():
        OP_96(0xFE, 0x125C, 0x1F4, 0xFFFFBEC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8E97)

    def lambda_8EB1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8EB1)
    WaitChrThread(0x109, 1)
    ClearChrFlags(0x109, 0x4)
    OP_71(0xB, 0x1F, 0x3C, 0x0, 0x0)
    Sound(463, 0, 100, 0)
    OP_79(0xB)
    Fade(500)
    OP_68(6000, 1000, -16200, 0)
    MoveCamera(25, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    Sound(470, 0, 100, 0)
    OP_71(0xB, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0xB)
    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    OP_68(12000, 1000, -4400, 4000)
    MoveCamera(60, 11, 0, 4000)
    SetCameraDistance(19500, 4000)

    def lambda_8F59():
        OP_96(0xFE, 0x1770, 0x0, 0xFFFFDC10, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8F59)
    Sound(486, 0, 100, 0)
    Sleep(1500)

    def lambda_8F7C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8F7C)

    def lambda_8F89():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8F89)
    Sleep(300)

    def lambda_8F99():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8F99)

    def lambda_8FA6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8FA6)
    WaitChrThread(0x18, 1)
    Sound(471, 0, 100, 0)

    def lambda_8FBD():
        OP_9E(0xFE, 0x2EE0, 0xFFFFDC10, 0x15F90, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8FBD)
    WaitChrThread(0x18, 1)

    def lambda_8FDC():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8FDC)
    Sleep(3000)
    OP_6F(0x79)
    Fade(500)
    OP_68(400, 1000, -16200, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    EndChrThread(0x18, 0x1)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x8000)
    ClearMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xB, 0x4)
    OP_0D()

    def lambda_9049():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9049)
    Sleep(150)

    def lambda_9059():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9059)
    Sleep(50)

    def lambda_9069():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9069)
    Sleep(50)

    def lambda_9079():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9079)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x101,
        (
            "#2201367V#0003F#11PNext on the agenda...\x02\x03",
            "#2201368V#0001F...we'll be providing security for Arc en Ciel's\x01",
            "private performance this weekend, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201369V#5P#0103FShall we return to the SSS and figure out\x01",
            "our plan of attack?\x02\x03",
            "#2201370V#0100FWe need to contact the troupe, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201371V#6P#0203FFirst, we will need to ascertain how the First\x01",
            "Division intends to handle security detail.\x02\x03",
            "#2201372V#0202FThe chief could probably do some research\x01",
            "if we were to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2201373V#0302F#5PSounds like we're gonna be busy, eh?\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x23, 0x1)
    StopBGM(0x1388)
    WaitBGM()
    ReplaceBGM("ed7100", "ed7000")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Soon after, the Special Support Section contacted\x01",
            "Arc en Ciel and figured out their plans for security\x01",
            "at the private performance.\x02\x03",
            "It was decided that Lloyd and Elie would take care\x01",
            "of the theater's interior, keeping an eye out for any\x01",
            "suspicious individuals or happenings.\x02\x03",
            "And as for Randy and Tio, they would be stationed\x01",
            "outside of the theater, conducting surveillance.\x02\x03",
            "Finally, on the day of the private performance...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_BA(0x8)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 0)
    NewScene("c040B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_8814 end

    def Function_32_94C4(): pass

    label("Function_32_94C4")

    EventBegin(0x0)
    Fade(1000)
    OP_68(0, 800, 4000, 0)
    MoveCamera(18, 22, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(28000, 0)
    Sound(803, 2, 0, 0)
    BeginChrThread(0x23, 1, 0, 55)
    SetChrPos(0x101, 2600, 0, -16600, 0)
    SetChrPos(0xEF, 3700, 0, -16800, 0)
    SetChrPos(0x153, 2900, 0, -14300, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_78(0x9, 0x12)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFlags(0x9, 0x4)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x4)
    OP_49()
    SetChrPos(0x12, 16000, 0, -6000, 270)
    OP_D3(0x12, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    MoveCamera(42, 22, 0, 9000)
    SetCameraDistance(33000, 9000)
    OP_6F(0x40)
    OP_6F(0x10)
    OP_0D()
    Fade(500)
    OP_68(3400, 800, -10300, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_966C():
        OP_95(0xFE, 2900, 0, -9300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_966C)
    Sleep(100)

    def lambda_9689():
        OP_95(0xFE, 2600, 0, -11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9689)
    Sleep(50)

    def lambda_96A6():
        OP_95(0xFE, 3700, 0, -11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_96A6)
    WaitChrThread(0x153, 1)
    OP_93(0x153, 0x50, 0x2BC)
    Sleep(750)
    OP_93(0x153, 0x10E, 0x2BC)
    Sleep(500)
    EndChrThread(0x23, 0x1)

    ChrTalk(
        0x153,
        (
            "#3600221V#1109F#11PWooow! There's so many people!\x02\x03",
            "#3600222V#1110FHey, Lloyd! Are all these people your\x01",
            "friends?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3600223V#12P#0012FN-No, I'm afraid not. That'd be impossible.\x02\x03",
            "#3600224V#0000FBesides, this is nothing compared to how\x01",
            "it was during the Anniversary Festival...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_9888")

    ChrTalk(
        0x102,
        (
            "#3600225V#12P#0108FDoes this mean she's not from\x01",
            "Crossbell City after all?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9950")

    label("loc_9888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_98F8")

    ChrTalk(
        0x103,
        (
            "#3600226V#12P#0208FHer surprise seems to indicate that\x01",
            "she is not from Crossbell, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9950")

    label("loc_98F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9950")

    ChrTalk(
        0x104,
        (
            "#3600227V#12P#0308FHuh? Guess she might not be from\x01",
            "Crossbell, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9950")

    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x153, 0x50, 0x1F4)
    Sound(2032, 255, 100, 0)
    Sleep(800)
    Fade(500)
    OP_68(9000, 1200, -6000, 0)
    MoveCamera(75, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    ClearMapObjFlags(0x9, 0x4)

    def lambda_99B3():

        label("loc_99B3")

        TurnDirection(0xFE, 0x12, 100)
        Yield()
        Jump("loc_99B3")

    QueueWorkItem2(0x153, 2, lambda_99B3)
    OP_68(-2000, 1200, -6000, 4000)
    MoveCamera(45, 20, 0, 4000)
    SetCameraDistance(16000, 4000)

    def lambda_99EA():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_99EA)
    Sound(458, 0, 100, 0)
    Sleep(2000)
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(2033, 255, 100, 0)
    WaitChrThread(0x12, 1)
    EndChrThread(0x153, 0x2)
    ClearMapObjFlags(0x9, 0x1000)
    ClearChrFlags(0x12, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    BeginChrThread(0x23, 1, 0, 56)
    Fade(500)
    OP_68(3400, 800, -10300, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()
    SetChrPos(0x12, -8010, 0, 16230, 225)
    OP_D3(0x12, 0x0, 0x3BD08, 0x0, 0x0)
    OP_70(0x9, 0x0)
    OP_63(0x153, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_9C(0x153, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(100)
    OP_9C(0x153, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(300)

    ChrTalk(
        0x153,
        (
            "#3600228V#1107F#11PWhat the heck is that big metal box?! All\x01",
            "it did was move and go vroom-vroom!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600229V#12P#0014FThat's a car, KeA.\x02\x03",
            "#3600230V#0002FIs that the first time you've seen one?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x153, 0xB4, 0x1F4)

    ChrTalk(
        0x153,
        (
            "#3600231V#1109F#5PI think so, but I'm not sure!\x02\x03",
            "#3600232V#1100FHehe! So it's a car? Vroom-vroom!\x02\x03",
            "#3600233V#1110FYou guys have one, too, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#3600234V#12P#0012FSadly, we don't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600235V#1100F#5PAw, okay.\x02\x03",
            "#3600236VI just thought it would be a lot of fun\x01",
            "if we could ride in one together.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_9DD8")

    ChrTalk(
        0x102,
        (
            "#3600237V#12P#0106FMe, too. I REALLY envy the First Division.\x02\x03",
            "#3600238V#0101FBut I suppose we can discard the possibility\x01",
            "of her being Crossbellan, now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F45")

    label("loc_9DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_9EAA")

    ChrTalk(
        0x103,
        (
            "#3600239V#12P#0206FStrong feelings of envy toward the First\x01",
            "Division are beginning to sprout.\x02\x03",
            "#3600240V#0201FDoes this confirm that she is not Crossbellan\x01",
            "like we initially thought, though?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F45")

    label("loc_9EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9F45")

    ChrTalk(
        0x104,
        (
            "#3600241V#12P#0306FThose lucky First Division dogs...\x02\x03",
            "#3600242V#0301FBut anyway, it's startin' to look like she's\x01",
            "not actually Crossbellan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F45")


    ChrTalk(
        0x101,
        (
            "#3600243V#6P#0006FYeah. You can't grow up in Crossbell and\x01",
            "NOT know what a car is.\x02\x03",
            "#3600244V#0001F(Then again, it's not like the concept of a\x01",
            "car is completely alien to her.)\x02\x03",
            "#3600245V(But what does that mean?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        (
            "#3600246V#1100F#5PWhat's wrong, Lloyd?\x02\x03",
            "#3600247VAren't we going to say hello to the\x01",
            "braces people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600248V#12P#0000FYou mean the bracers? If so, yes.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_A127")

    ChrTalk(
        0x102,
        "#3600249V#12P#0100FShall we head to East Street, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A198")

    label("loc_A127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_A163")

    ChrTalk(
        0x103,
        "#3600250V#12P#0202FTo East Street, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A198")

    label("loc_A163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_A198")

    ChrTalk(
        0x104,
        "#3600251V#12P#0300FSounds like a plan!\x02",
    )

    CloseMessageWindow()

    label("loc_A198")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 3400, 0, -10300, 0)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0xA7, 7)
    OP_C7(0x1, 0x1000)
    EndChrThread(0x23, 0x1)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_32_94C4 end

    def Function_33_A211(): pass

    label("Function_33_A211")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x101, -24800, -8200, -23800, 270)
    SetChrPos(0x102, -24000, -8200, -24600, 270)
    SetChrPos(0x103, -22400, -8200, -23800, 270)
    SetChrPos(0x104, -21600, -8200, -24600, 270)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x0)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, 9000, 0, 5000, 180)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x3)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -9300, 0, -7200, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x2)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -9700, 0, -5500, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0xF)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -14500, 0, -500, 90)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, -15500, 0, 1000, 90)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Three weeks later...\x02\x03",
            "There was still no sign of KeA's memories returning,\x01",
            "and even with the Bracer Guild's help, the team still\x01",
            "couldn't verify her identity.\x02\x03",
            "With the Anniversary Festival over and the mayoral\x01",
            "election still one month away, Crossbell had become\x01",
            "fairly quiet.\x02\x03",
            "The Special Support Section had adjusted to living\x01",
            "with the young, rambunctious girl and returned to\x01",
            "their regular duties.\x02\x03",
            "Being a quick learner, KeA understood that the team\x01",
            "worked during the day, so she offered to watch over\x01",
            "the SSS building while they're out.\x02\x03",
            "And then...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7201", 0)
    ReplaceBGM("ed7100", "ed7201")

    def lambda_A60C():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A60C)

    def lambda_A627():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A627)

    def lambda_A641():
        OP_98(0xFE, 0x2710, 0x0, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_A641)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 38)
    FadeToBright(2000, 0)
    Sleep(4750)
    BeginChrThread(0x101, 3, 0, 34)
    Sleep(150)
    BeginChrThread(0x102, 3, 0, 35)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 36)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 37)
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    WaitChrThread(0x23, 1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_24(0x323)
    SetScenarioFlags(0x5D, 4)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_A211 end

    def Function_34_A738(): pass

    label("Function_34_A738")


    def lambda_A73D():
        OP_95(0xFE, -28400, -8200, -23800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A73D)
    WaitChrThread(0x101, 1)

    def lambda_A75B():
        OP_95(0xFE, -28400, -8200, -22300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A75B)
    WaitChrThread(0x101, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_A794():
        OP_95(0xFE, -28400, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A794)
    Sleep(500)

    def lambda_A7B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A7B1)
    WaitChrThread(0x101, 1)
    Return()

    # Function_34_A738 end

    def Function_35_A7C2(): pass

    label("Function_35_A7C2")


    def lambda_A7C7():
        OP_95(0xFE, -28800, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A7C7)
    WaitChrThread(0x102, 1)

    def lambda_A7E5():
        OP_95(0xFE, -28800, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A7E5)
    Sleep(1500)

    def lambda_A802():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A802)
    WaitChrThread(0x102, 1)
    Return()

    # Function_35_A7C2 end

    def Function_36_A813(): pass

    label("Function_36_A813")


    def lambda_A818():
        OP_95(0xFE, -28400, -8200, -23800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A818)
    WaitChrThread(0x103, 1)

    def lambda_A836():
        OP_95(0xFE, -28400, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A836)
    Sleep(1500)

    def lambda_A853():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A853)
    WaitChrThread(0x103, 1)
    Return()

    # Function_36_A813 end

    def Function_37_A864(): pass

    label("Function_37_A864")


    def lambda_A869():
        OP_95(0xFE, -28800, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A869)
    WaitChrThread(0x104, 1)

    def lambda_A887():
        OP_95(0xFE, -28800, -8200, -20300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A887)
    Sleep(1500)

    def lambda_A8A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A8A4)
    WaitChrThread(0x104, 1)
    Return()

    # Function_37_A864 end

    def Function_38_A8B5(): pass

    label("Function_38_A8B5")

    Sound(803, 2, 100, 0)
    Sleep(7000)
    OP_25(0x323, 0x5A)
    Sleep(200)
    OP_25(0x323, 0x50)
    Sleep(200)
    OP_25(0x323, 0x46)
    Sleep(200)
    OP_25(0x323, 0x3C)
    Sleep(200)
    OP_25(0x323, 0x32)
    Sleep(200)
    OP_25(0x323, 0x28)
    Sleep(200)
    OP_25(0x323, 0x1E)
    Sleep(200)
    OP_25(0x323, 0x14)
    Sleep(200)
    OP_25(0x323, 0xA)
    Sleep(200)
    OP_24(0x323)
    Return()

    # Function_38_A8B5 end

    def Function_39_A901(): pass

    label("Function_39_A901")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-28700, -7200, -21900, 0)
    MoveCamera(50, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -28700, -8200, -19500, 180)
    SetChrPos(0x102, -28700, -8200, -19500, 180)
    SetChrPos(0x103, -28700, -8200, -19500, 180)
    SetChrPos(0x104, -28700, -8200, -19500, 180)
    SetChrPos(0x109, -28700, -8200, -19500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(-28700, -7200, -24900, 6000)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 41)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 43)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 42)
    Sleep(1500)

    def lambda_AA32():
        OP_95(0xFE, -28700, -8200, -23500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AA32)

    def lambda_AA4C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AA4C)
    Sleep(1500)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    ChrTalk(
        0x109,
        (
            "#4100236V#5P#0500FMy car's parked over near the north exit.\x02\x03",
            "#4100237VI'd be happy to give you a ride, as long as\x01",
            "we stay within state borders. Just let me\x01",
            "know, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_END)), "loc_AC7D")

    ChrTalk(
        0x101,
        (
            "#4100245V#12P#0004FThat'd be great. Thanks.\x02\x03",
            "#4100239V#0000FSo, just to clarify, we're talking about the\x01",
            "ruins beyond the fork that's halfway into\x01",
            "the mountain path, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100240V#6P#0203FWe hiked down that path some time ago.\x02\x03",
            "#4100241V#0200FThat time, however, it was barricaded off\x01",
            "by the CGF.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AEB9")

    label("loc_AC7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 7)), scpexpr(EXPR_END)), "loc_AD9D")

    ChrTalk(
        0x101,
        (
            "#4100242V#12P#0004FThat'd be great. Thanks.\x02\x03",
            "#4100246V#0000FSo, just to clarify, we're talking about the\x01",
            "ruins beyond the fork that's halfway into\x01",
            "the mountain path, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100244V#6P#0202FI believe so. It should be somewhere in\x01",
            "the village's general proximity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AEB9")

    label("loc_AD9D")


    ChrTalk(
        0x101,
        (
            "#4100238V#12P#0004FThat'd be great. Thanks.\x02\x03",
            "#4100243V#0000FSo, just to clarify, we're talking about the\x01",
            "ruins beyond the fork that's halfway into\x01",
            "the mountain path, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100247V#6P#0202FYes. I'm positive that there was a narrow\x01",
            "path branching off in the path's tunnel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEB9")


    ChrTalk(
        0x109,
        (
            "#4100248V#5P#0500FThat's the one. The road is pretty\x01",
            "rough, so you'll have to tackle the\x01",
            "mountain path on foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100249V#11P#0309FTime to wrap things up here and have\x01",
            "ourselves a hike, then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100250V#12P#0108F(Ruins...infested with ghosts? Aidios,\x01",
            "protect me.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -28700, -8200, -25000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC0, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_29(0x48, 0x1, 0x9)
    OP_29(0x49, 0x4, 0x2)
    OP_29(0x49, 0x1, 0x0)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_39_A901 end

    def Function_40_B033(): pass

    label("Function_40_B033")


    def lambda_B038():
        OP_95(0xFE, -28700, -8200, -23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B038)

    def lambda_B052():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B052)
    WaitChrThread(0xFE, 1)

    def lambda_B067():
        OP_95(0xFE, -28100, -8200, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B067)
    WaitChrThread(0x101, 1)

    def lambda_B085():
        OP_92(0xFE, 0xFFFF8FE4, 0xFFFFA434, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B085)
    WaitChrThread(0x101, 2)
    Return()

    # Function_40_B033 end

    def Function_41_B098(): pass

    label("Function_41_B098")


    def lambda_B09D():
        OP_95(0xFE, -28700, -8200, -23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B09D)

    def lambda_B0B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B0B7)
    WaitChrThread(0xFE, 1)

    def lambda_B0CC():
        OP_95(0xFE, -29400, -8200, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B0CC)
    WaitChrThread(0x102, 1)

    def lambda_B0EA():
        OP_92(0xFE, 0xFFFF8FE4, 0xFFFFA434, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B0EA)
    WaitChrThread(0x102, 2)
    Return()

    # Function_41_B098 end

    def Function_42_B0FD(): pass

    label("Function_42_B0FD")


    def lambda_B102():
        OP_95(0xFE, -28700, -8200, -23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B102)

    def lambda_B11C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B11C)
    WaitChrThread(0xFE, 1)

    def lambda_B131():
        OP_95(0xFE, -30400, -8200, -25300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B131)
    WaitChrThread(0x103, 1)

    def lambda_B14F():
        OP_92(0xFE, 0xFFFF8FE4, 0xFFFFA434, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B14F)
    WaitChrThread(0x103, 2)
    Return()

    # Function_42_B0FD end

    def Function_43_B162(): pass

    label("Function_43_B162")


    def lambda_B167():
        OP_95(0xFE, -28700, -8200, -23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B167)

    def lambda_B181():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B181)
    WaitChrThread(0xFE, 1)

    def lambda_B196():
        OP_95(0xFE, -27000, -8200, -25300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B196)
    WaitChrThread(0x104, 1)

    def lambda_B1B4():
        OP_92(0xFE, 0xFFFF8FE4, 0xFFFFA434, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B1B4)
    WaitChrThread(0x104, 2)
    Return()

    # Function_43_B162 end

    def Function_44_B1C7(): pass

    label("Function_44_B1C7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50109.itc", 0x1E)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x101, 1000, 0, -16800, 90)
    SetChrPos(0x102, 1000, 0, -15600, 90)
    SetChrPos(0x103, -200, 0, -16800, 90)
    SetChrPos(0x104, -200, 0, -15600, 90)
    SetChrPos(0x109, 3200, 0, -16200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_78(0xB, 0x18)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    ClearMapObjFlags(0xB, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, 6000, 0, -16200, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    OP_74(0xB, 0x1E)
    OP_70(0xB, 0x0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x0)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, 0, 0, -5000, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x3)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -9300, 0, -7200, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x2)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -9700, 0, -5500, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0xF)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -4500, 0, 11500, 270)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, -5500, 0, 13000, 270)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    def lambda_B412():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_B412)

    def lambda_B42D():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_B42D)

    def lambda_B447():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_B447)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 28)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(2700, 900, -14200, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    OP_68(2700, 900, -16200, 3000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#4100559V#11P#0509FThanks for your help today, everyone!\x02\x03",
            "#4100560V#0502FTrust me, I plan to return the favor as\x01",
            "soon as I can!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100561V#6P#0002FI think you're giving us too much credit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100562V#0304F#6PYeah, dude. We should be thankin' YOU\x01",
            "for inviting us on this crazy adventure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100563V#0106F#6PGuys, about what happened in the temple...\x02\x03",
            "#4100564V#0108FI think we should contact Crossbell Cathedral\x01",
            "and have them sort things out from here on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100565V#6P#0206FI concur.\x02\x03",
            "#4100566VIf the ruins are, in fact, related to an artifact,\x01",
            "our hands are tied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4100567V#11P#0503FGood point...\x02\x03",
            "#4100568V#0500FEither way, I'll discuss things with the deputy\x01",
            "commander and figure out what to do.\x02\x03",
            "#4100569V#0505FSo, are you guys going to start asking around\x01",
            "the city now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100570V#6P#0004FYep. Starting with the casino.\x02\x03",
            "#4100571V#0000FCould you contact us if the CGF learns\x01",
            "anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#4100572V#11P#0500FAbout Gantz, you mean? Of course.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#4100573V#2P#0502F#11PAnyway, I'll let you guys get back to work.\x01",
            "Good luck!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100574V#0302F#6PHeh. You, too, Noel.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_92(0x109, 0xE74, 0xFFFFBEC4, 0x1F4)

    def lambda_B94A():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFBEC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B94A)
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0x5A, 0x1F4)
    OP_71(0xB, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0xB)
    SetChrFlags(0x109, 0x4)

    def lambda_B989():
        OP_96(0xFE, 0x125C, 0x1F4, 0xFFFFBEC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B989)

    def lambda_B9A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B9A3)
    WaitChrThread(0x109, 1)
    ClearChrFlags(0x109, 0x4)
    OP_71(0xB, 0x1F, 0x3C, 0x0, 0x0)
    Sound(463, 0, 100, 0)
    OP_79(0xB)
    Fade(500)
    OP_68(6000, 1000, -16200, 0)
    MoveCamera(25, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    Sound(470, 0, 100, 0)
    OP_71(0xB, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0xB)
    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    OP_68(12000, 1000, -4400, 4000)
    MoveCamera(60, 11, 0, 4000)
    SetCameraDistance(19500, 4000)
    Sound(486, 0, 100, 0)

    def lambda_BA51():
        OP_96(0xFE, 0x1770, 0x0, 0xFFFFDC10, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_BA51)
    Sleep(1500)

    def lambda_BA6E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BA6E)

    def lambda_BA7B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BA7B)
    Sleep(300)

    def lambda_BA8B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BA8B)

    def lambda_BA98():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BA98)
    WaitChrThread(0x18, 1)
    Sound(471, 0, 100, 0)

    def lambda_BAAF():
        OP_9E(0xFE, 0x2EE0, 0xFFFFDC10, 0x15F90, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_BAAF)
    WaitChrThread(0x18, 1)

    def lambda_BACE():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_BACE)
    Sleep(3000)
    OP_6F(0x79)
    Fade(500)
    OP_68(400, 1000, -16200, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    EndChrThread(0x18, 0x1)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x8000)
    ClearMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xB, 0x4)
    OP_0D()

    def lambda_BB3B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BB3B)
    Sleep(150)

    def lambda_BB4B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BB4B)
    Sleep(50)

    def lambda_BB5B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BB5B)
    Sleep(50)

    def lambda_BB6B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BB6B)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x101,
        (
            "#4100575V#0000FWell, then. Ready to stop by the casino?\x01",
            "Remember, we don't have too much time\x01",
            "to waste.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102)

    ChrTalk(
        0x102,
        (
            "#4100576V#5P#0100FLet's go. There's still a lot we don't know\x01",
            "about Gantz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100577V#0309FWell, what are we waiting for? To the\x01",
            "Entertainment District!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_BA(0x8)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    SetScenarioFlags(0xC1, 4)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_29(0x4A, 0x1, 0x3)
    EndChrThread(0x23, 0x1)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 2)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_B1C7 end

    def Function_45_BCFA(): pass

    label("Function_45_BCFA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28100.itc", 0x1E)
    LoadChrToIndex("chr/ch21200.itc", 0x1F)
    LoadChrToIndex("chr/ch21400.itc", 0x20)
    LoadChrToIndex("chr/ch20000.itc", 0x21)
    LoadChrToIndex("chr/ch23600.itc", 0x22)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xB4, 0xD7, 0xE6, 0xF, 0x82, 0x0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x9, 0x18)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, 15000, 0, -3000, 0)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, -15000, 0, -6300, 90)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -6800, 0, 4000, 270)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -8300, 0, 2500, 90)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -19300, 0, 19400, 180)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, 7000, 0, 12000, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)

    def lambda_BF22():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_BF22)

    def lambda_BF3C():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_BF3C)

    def lambda_BF56():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_BF56)
    Sound(458, 0, 100, 0)

    def lambda_BF77():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_BF77)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 19)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x23, 0x1)
    SetScenarioFlags(0x5D, 5)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_BCFA end

    def Function_46_C018(): pass

    label("Function_46_C018")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28100.itc", 0x1E)
    LoadChrToIndex("chr/ch21200.itc", 0x1F)
    LoadChrToIndex("chr/ch21400.itc", 0x20)
    LoadChrToIndex("chr/ch20000.itc", 0x21)
    LoadChrToIndex("chr/ch23600.itc", 0x22)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xB4, 0xD7, 0xE6, 0xF, 0x82, 0x0)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x9, 0x18)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_49()
    SetChrPos(0x18, 15000, 0, -3000, 0)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, -15000, 0, -6300, 90)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -6800, 0, 4000, 270)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -8300, 0, 2500, 90)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -19300, 0, 19400, 180)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, 7000, 0, 12000, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KThe next day, 8:00AM...\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7001", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_C2A2():
        OP_96(0xFE, 0x1388, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_C2A2)

    def lambda_C2BC():
        OP_98(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_C2BC)

    def lambda_C2D6():
        OP_9E(0xFE, 0x0, 0x1388, 0x2BF20, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_C2D6)

    def lambda_C2F1():
        OP_96(0xFE, 0xFFFF9A70, 0x3E8, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_C2F1)
    Sound(458, 0, 100, 0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 19)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5D, 6)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_46_C018 end

    def Function_47_C394(): pass

    label("Function_47_C394")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x1E, 0x0)
    SetChrSubChip(0x1E, 0x0)
    OP_4B(0x1E, 0xFF)
    SetChrPos(0x1E, 0, 0, -5000, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x3)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -9300, 0, -7200, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x2)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -9700, 0, -5500, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0xF)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, -4500, 0, 11500, 270)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x22, -5500, 0, 13000, 270)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KThe same day, 5:00PM...\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7100", 0)

    def lambda_C5C3():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_C5C3)

    def lambda_C5DE():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_C5DE)

    def lambda_C5F8():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD120, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_C5F8)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x23, 1, 0, 28)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    ClearScenarioFlags(0x1, 5)
    EndChrThread(0x23, 0x1)
    OP_24(0x323)
    SetScenarioFlags(0x5D, 7)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_47_C394 end

    def Function_48_C6D9(): pass

    label("Function_48_C6D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C707")
    EventBegin(0x1)
    Call(0, 54)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)
    Jump("loc_C730")

    label("loc_C707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C730")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)

    label("loc_C730")

    Return()

    # Function_48_C6D9 end

    def Function_49_C731(): pass

    label("Function_49_C731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C75F")
    EventBegin(0x1)
    Call(0, 54)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)
    Jump("loc_C788")

    label("loc_C75F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C788")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_C788")

    Return()

    # Function_49_C731 end

    def Function_50_C789(): pass

    label("Function_50_C789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C7B7")
    EventBegin(0x1)
    Call(0, 54)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)
    Jump("loc_C7E0")

    label("loc_C7B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C7E0")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)

    label("loc_C7E0")

    Return()

    # Function_50_C789 end

    def Function_51_C7E1(): pass

    label("Function_51_C7E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C80A")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, -13380, 0, 14530, 135)
    EventEnd(0x4)

    label("loc_C80A")

    Return()

    # Function_51_C7E1 end

    def Function_52_C80B(): pass

    label("Function_52_C80B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C839")
    EventBegin(0x1)
    Call(0, 54)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)
    Jump("loc_C862")

    label("loc_C839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C862")
    EventBegin(0x1)
    Call(0, 53)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)

    label("loc_C862")

    Return()

    # Function_52_C80B end

    def Function_53_C863(): pass

    label("Function_53_C863")


    ChrTalk(
        0x101,
        (
            "#0005FWait. We should stop by the orbal\x01",
            "store before exploring the city.\x02\x03",
            "#0000FI'm pretty sure it's on the northeast\x01",
            "corner of Central Square.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C931")

    ChrTalk(
        0x103,
        "#0200FRoger. Ready when you are.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C98E")

    label("loc_C931")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C964")

    ChrTalk(
        0x104,
        "#0300FGot'cha. Let's roll!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C98E")

    label("loc_C964")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C98E")

    ChrTalk(
        0x102,
        "#0100FOff we go, then.\x02",
    )

    CloseMessageWindow()

    label("loc_C98E")

    Return()

    # Function_53_C863 end

    def Function_54_C98F(): pass

    label("Function_54_C98F")


    ChrTalk(
        0x101,
        (
            "#0000F*sigh* Today was brutal. How about\x01",
            "we DON'T take any detours on the\x01",
            "way back to the SSS?\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_54_C98F end

    def Function_55_C9F4(): pass

    label("Function_55_C9F4")

    OP_25(0x323, 0x0)
    Sleep(200)
    OP_25(0x323, 0xA)
    Sleep(200)
    OP_25(0x323, 0x14)
    Sleep(200)
    OP_25(0x323, 0x1E)
    Sleep(200)
    OP_25(0x323, 0x28)
    Sleep(200)
    OP_25(0x323, 0x32)
    Sleep(200)
    OP_25(0x323, 0x3C)
    Sleep(200)
    OP_25(0x323, 0x46)
    Sleep(200)
    OP_25(0x323, 0x50)
    Sleep(200)
    OP_25(0x323, 0x5A)
    Sleep(200)
    OP_25(0x323, 0x64)
    Return()

    # Function_55_C9F4 end

    def Function_56_CA3F(): pass

    label("Function_56_CA3F")

    OP_25(0x323, 0x64)
    Sleep(100)
    OP_25(0x323, 0x5A)
    Sleep(100)
    OP_25(0x323, 0x50)
    Sleep(100)
    OP_25(0x323, 0x46)
    Sleep(100)
    OP_25(0x323, 0x3C)
    Sleep(100)
    OP_25(0x323, 0x32)
    Sleep(100)
    OP_25(0x323, 0x28)
    Sleep(100)
    OP_25(0x323, 0x1E)
    Sleep(100)
    OP_25(0x323, 0x14)
    Sleep(100)
    OP_25(0x323, 0xA)
    Sleep(100)
    OP_25(0x323, 0x0)
    OP_24(0x323)
    Return()

    # Function_56_CA3F end

    SaveToFile()

Try(main)
