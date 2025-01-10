from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c010c.bin",                # FileName
        "c010c",                    # MapName
        "c010c",                    # Location
        0x0004,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 5, 0, 6],
    )

    BuildStringList((
        "c010c",                  # 0
        "Abel",                   # 1
        "Mimi",                   # 2
        "Gina",                   # 3
        "Old Man Conte",          # 4
        "Pruna",                  # 5
        "Lenalee",                # 6
        "Haas",                   # 7
        "Arona",                  # 8
        "Nardol",                 # 9
        "Mazie",                  # 10
        "Nonno",                  # 11
        "Ryu",                    # 12
        "Koken",                  # 13
        "Fay",                    # 14
        "Pansy",                  # 15
        "Nurse Cirone",           # 16
        "Nurse Meifa",            # 17
        "Officer Kate",           # 18
        "Tourist",                # 19
        "Tourist",                # 20
        "Tourist",                # 21
        "Tourist",                # 22
        "Zeit",                   # 23
        "Coppe",                  # 24
        "Guest",                  # 25
        "Guest",                  # 26
        "Guest",                  # 27
        "Young Man",              # 28
        "Young Man",              # 29
        "SE制御",                 # 30
        "Central Square",         # 31
        "West Street",            # 32
        "Administrative District",# 33
        "Residential District",   # 34
        "Entertainment District", # 35
        "East Street",            # 36
        "Downtown District",      # 37
        "Harbor District",        # 38
        "IBC",                    # 39
        "Station Street",         # 40
        "Back Alley",             # 41
        "Ursula Road",            # 42
        "East Crossbell Highway", # 43
        "West Crossbell Highway", # 44
        "Mainz Mountain Path",    # 45
    ))

    AddCharChip((
        "chr/ch20200.itc",                   # 00
        "chr/ch20700.itc",                   # 01
        "chr/ch21300.itc",                   # 02
        "chr/ch20002.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch22100.itc",                   # 05
        "chr/ch20300.itc",                   # 06
        "chr/ch26000.itc",                   # 07
        "chr/ch24500.itc",                   # 08
        "chr/ch25600.itc",                   # 09
        "chr/ch02707.itc",                   # 0A
        "chr/ch39200.itc",                   # 0B
        "chr/ch32300.itc",                   # 0C
        "chr/ch32400.itc",                   # 0D
        "chr/ch32200.itc",                   # 0E
        "chr/ch21600.itc",                   # 0F
        "chr/ch20600.itc",                   # 10
        "chr/ch21000.itc",                   # 11
        "chr/ch32700.itc",                   # 12
        "chr/ch22300.itc",                   # 13
        "chr/ch36500.itc",                   # 14
        "chr/ch36400.itc",                   # 15
        "chr/ch30600.itc",                   # 16
        "chr/ch26900.itc",                   # 17
    ))

    DeclNpc(-6099,   0,       -9409,   90,   261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-289,    0,       -10319,  225,  261,  0x0, 0,   1,   0,   0,   2,   0,   10,  255,  0)
    DeclNpc(30000,   0,       -1799,   270,  261,  0x0, 0,   2,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(-6090,   150,     4449,    270,  341,  0x0, 0,   3,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(850,     0,       17969,   90,   277,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(2539,    0,       17870,   270,  277,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(8310,    0,       -9510,   315,  261,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(1879,    0,       -4300,   180,  261,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(12420,   0,       2730,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-7400,   0,       15560,   180,  261,  0x0, 0,   8,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-17479,  0,       610,     135,  389,  0x0, 0,   9,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-15449,  0,       -2259,   90,   261,  0x0, 0,   16,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-14100,  0,       -2259,   270,  261,  0x0, 0,   17,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-3519,   0,       9729,    225,  405,  0x0, 0,   18,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-4710,   0,       8529,    45,   405,  0x0, 0,   19,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-11829,  0,       -2779,   90,   405,  0x0, 0,   20,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-12090,  0,       -1389,   135,  405,  0x0, 0,   21,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-2579,   0,       -2119,   197,  261,  0x0, 0,   22,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(7300,    0,       -16639,  0,    261,  0x0, 0,   12,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(7300,    0,       -15159,  180,  261,  0x0, 0,   23,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(0,       0,       15109,   0,    261,  0x0, 0,   14,  0,   0,   4,   0,   30,  255,  0)
    DeclNpc(-15829,  0,       7170,    180,  261,  0x0, 0,   15,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(-25440,  1299,    -17040,  225,  276,  0x0, 0,   10,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(-22450,  1299,    -20010,  315,  261,  0x0, 0,   11,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 67,  -28.5,                 -21.5,                 -9.199999809265137,    4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.25,                 10.75,                 1.840000033378601,     1.0])

    DeclActor(-270,    0,       -980,    800,     130,     1500,    -10,     0x007C, 0,  37, 0x0000)
    DeclActor(-290,    -1000,   4400,    600,     -290,    -1000,   4400,    0x007C, 0,  38, 0x0000)
    DeclActor(-20,     -1000,   4760,    800,     800,     1800,    4570,    0x007C, 0,  61, 0x0000)
    DeclActor(1740,    -950,    3070,    1100,    1740,    550,     3070,    0x007C, 0,  8,  0x0000)

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

    ScpFunction((
        "Function_0_89C",          # 00, 0
        "Function_1_954",          # 01, 1
        "Function_2_9A1",          # 02, 2
        "Function_3_9CC",          # 03, 3
        "Function_4_9F7",          # 04, 4
        "Function_5_A80",          # 05, 5
        "Function_6_1327",         # 06, 6
        "Function_7_1428",         # 07, 7
        "Function_8_14D3",         # 08, 8
        "Function_9_16B3",         # 09, 9
        "Function_10_1C57",        # 0A, 10
        "Function_11_24C3",        # 0B, 11
        "Function_12_2A41",        # 0C, 12
        "Function_13_31C1",        # 0D, 13
        "Function_14_34D3",        # 0E, 14
        "Function_15_37CD",        # 0F, 15
        "Function_16_3BE6",        # 10, 16
        "Function_17_4537",        # 11, 17
        "Function_18_4656",        # 12, 18
        "Function_19_4E29",        # 13, 19
        "Function_20_5AC6",        # 14, 20
        "Function_21_5BE2",        # 15, 21
        "Function_22_65B3",        # 16, 22
        "Function_23_6866",        # 17, 23
        "Function_24_692A",        # 18, 24
        "Function_25_6982",        # 19, 25
        "Function_26_6A50",        # 1A, 26
        "Function_27_6BF3",        # 1B, 27
        "Function_28_72F8",        # 1C, 28
        "Function_29_7552",        # 1D, 29
        "Function_30_768C",        # 1E, 30
        "Function_31_78BB",        # 1F, 31
        "Function_32_7B98",        # 20, 32
        "Function_33_7DC8",        # 21, 33
        "Function_34_905A",        # 22, 34
        "Function_35_9261",        # 23, 35
        "Function_36_93B2",        # 24, 36
        "Function_37_947F",        # 25, 37
        "Function_38_97D0",        # 26, 38
        "Function_39_982E",        # 27, 39
        "Function_40_9EAE",        # 28, 40
        "Function_41_A9F2",        # 29, 41
        "Function_42_ABB4",        # 2A, 42
        "Function_43_AC00",        # 2B, 43
        "Function_44_ADBE",        # 2C, 44
        "Function_45_B656",        # 2D, 45
        "Function_46_BDC8",        # 2E, 46
        "Function_47_BDEE",        # 2F, 47
        "Function_48_BE35",        # 30, 48
        "Function_49_BED1",        # 31, 49
        "Function_50_BF6D",        # 32, 50
        "Function_51_C00E",        # 33, 51
        "Function_52_C037",        # 34, 52
        "Function_53_C06F",        # 35, 53
        "Function_54_C098",        # 36, 54
        "Function_55_C0C5",        # 37, 55
        "Function_56_C0F2",        # 38, 56
        "Function_57_C10E",        # 39, 57
        "Function_58_C12A",        # 3A, 58
        "Function_59_C142",        # 3B, 59
        "Function_60_C171",        # 3C, 60
        "Function_61_C774",        # 3D, 61
        "Function_62_CC65",        # 3E, 62
        "Function_63_CCB8",        # 3F, 63
        "Function_64_CD34",        # 40, 64
        "Function_65_CDB0",        # 41, 65
        "Function_66_CE03",        # 42, 66
        "Function_67_CE7F",        # 43, 67
        "Function_68_CE9B",        # 44, 68
        "Function_69_CFC0",        # 45, 69
        "Function_70_D047",        # 46, 70
        "Function_71_D0CB",        # 47, 71
        "Function_72_D13A",        # 48, 72
        "Function_73_D190",        # 49, 73
        "Function_74_D201",        # 4A, 74
    ))


    def Function_0_89C(): pass

    label("Function_0_89C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_8DC"),
        (1, "loc_8E8"),
        (2, "loc_8F4"),
        (3, "loc_900"),
        (4, "loc_90C"),
        (5, "loc_918"),
        (6, "loc_924"),
        (SWITCH_DEFAULT, "loc_930"),
    )


    label("loc_8DC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_8E8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_8F4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_900")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_90C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_918")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_924")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_930")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_93C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_953")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_93C")

    label("loc_953")

    Return()

    # Function_0_89C end

    def Function_1_954(): pass

    label("Function_1_954")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9A0")
    OP_95(0xFE, 10430, 0, -1800, 2000, 0x0)
    OP_95(0xFE, 10430, 0, 39440, 2000, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 30000, 0, -3010, 270)
    Jump("Function_1_954")

    label("loc_9A0")

    Return()

    # Function_1_954 end

    def Function_2_9A1(): pass

    label("Function_2_9A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9CB")
    OP_94(0xFE, 0x366, 0xFFFFE296, 0xFFFFF236, 0xFFFFD166, 0x3E8)
    Sleep(300)
    Jump("Function_2_9A1")

    label("loc_9CB")

    Return()

    # Function_2_9A1 end

    def Function_3_9CC(): pass

    label("Function_3_9CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9F6")
    OP_94(0xFE, 0xFFFFA9C0, 0xFFFFBD34, 0xFFFF9D36, 0xFFFFB0AA, 0x3E8)
    Sleep(300)
    Jump("Function_3_9CC")

    label("loc_9F6")

    Return()

    # Function_3_9CC end

    def Function_4_9F7(): pass

    label("Function_4_9F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A7F")
    OP_95(0xFE, -7290, 0, 11150, 2000, 0x0)
    OP_95(0xFE, -13960, 0, 1780, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x168, 0x190)
    Sleep(100)
    OP_95(0xFE, -7290, 0, 11150, 2000, 0x0)
    OP_95(0xFE, 0, 0, 15110, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    Jump("Function_4_9F7")

    label("loc_A7F")

    Return()

    # Function_4_9F7 end

    def Function_5_A80(): pass

    label("Function_5_A80")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1191")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B42")
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    SetChrPos(0x1, -26950, -1160, -4340, 90)
    SetChrPos(0x2, -26950, -1160, -4340, 90)
    SetChrPos(0x3, -26950, -1160, -4340, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B15")
    SetChrPos(0x4, -26950, -1160, -4340, 90)
    SetChrPos(0x5, -26950, -1160, -4340, 90)
    Jump("loc_B34")

    label("loc_B15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B34")
    SetChrPos(0x4, -26950, -1160, -4340, 90)

    label("loc_B34")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_B42")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF6")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC9")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_BE8")

    label("loc_BC9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE8")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_BE8")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_BF6")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAA")
    SetChrPos(0x0, 11850, 0, 28440, 180)
    SetChrPos(0x1, 11850, 0, 28440, 180)
    SetChrPos(0x2, 11850, 0, 28440, 180)
    SetChrPos(0x3, 11850, 0, 28440, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7D")
    SetChrPos(0x4, 11850, 0, 28440, 180)
    SetChrPos(0x5, 11850, 0, 28440, 180)
    Jump("loc_C9C")

    label("loc_C7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9C")
    SetChrPos(0x4, 11850, 0, 28440, 180)

    label("loc_C9C")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_CAA")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5E")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D31")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_D50")

    label("loc_D31")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D50")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_D50")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_D5E")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E12")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE5")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_E04")

    label("loc_DE5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E04")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_E04")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_E12")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC6")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E99")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_EB8")

    label("loc_E99")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB8")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_EB8")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_EC6")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7A")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F4D")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_F6C")

    label("loc_F4D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F6C")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_F6C")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_F7A")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102E")
    SetChrPos(0x0, 4040, 0, -21980, 0)
    SetChrPos(0x1, 4040, 0, -21980, 0)
    SetChrPos(0x2, 4040, 0, -21980, 0)
    SetChrPos(0x3, 4040, 0, -21980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1001")
    SetChrPos(0x4, 4040, 0, -21980, 0)
    SetChrPos(0x5, 4040, 0, -21980, 0)
    Jump("loc_1020")

    label("loc_1001")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1020")
    SetChrPos(0x4, 4040, 0, -21980, 0)

    label("loc_1020")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_102E")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E2")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10B5")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_10D4")

    label("loc_10B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D4")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_10D4")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1191")

    label("loc_10E2")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1191")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1169")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_1188")

    label("loc_1169")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1188")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_1188")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1191")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_11C3")
    SetChrPos(0x1F, -26850, 1300, -17520, 89)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_1285")

    label("loc_11C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_11E0")
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_1285")

    label("loc_11E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1204")
    SetChrPos(0x1F, -25480, 1300, -18700, 0)
    SetChrFlags(0x19, 0x80)
    Jump("loc_1285")

    label("loc_1204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1236")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x1F, -28010, 1300, -19360, 45)
    OP_93(0x13, 0x0, 0x0)
    OP_93(0x14, 0x0, 0x0)
    Jump("loc_1285")

    label("loc_1236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1268")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x1F, -28010, 1300, -19360, 45)
    OP_93(0x13, 0x0, 0x0)
    OP_93(0x14, 0x0, 0x0)
    Jump("loc_1285")

    label("loc_1268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1285")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_1285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A0")
    SetMapFlags(0x10000000)
    Event(0, 39)
    Jump("loc_12B6")

    label("loc_12A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12B6")
    SetMapFlags(0x10000000)
    Event(0, 40)

    label("loc_12B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_12C7")
    ClearScenarioFlags(0x5C, 0)
    Jump("loc_1326")

    label("loc_12C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_12D8")
    ClearScenarioFlags(0x5C, 1)
    Jump("loc_1326")

    label("loc_12D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_12EC")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 41)
    Jump("loc_1326")

    label("loc_12EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_1300")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 43)
    Jump("loc_1326")

    label("loc_1300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_1317")
    ClearScenarioFlags(0x5C, 4)
    SetScenarioFlags(0x1, 5)
    Event(0, 45)
    Jump("loc_1326")

    label("loc_1317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_1326")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 60)

    label("loc_1326")

    Return()

    # Function_5_A80 end

    def Function_6_1327(): pass

    label("Function_6_1327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_133C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 5)

    label("loc_133C")

    OP_52(0x1E, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)
    OP_10(0xB, 0x0)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_138D")
    OP_65(0x1, 0x1)
    OP_66(0x2, 0x1)

    label("loc_138D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A0")
    OP_70(0xC, 0x0)
    Jump("loc_13A4")

    label("loc_13A0")

    OP_70(0xC, 0x1E)

    label("loc_13A4")

    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 10000, -4000, 5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -10000, -4000, 5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_6_1327 end

    def Function_7_1428(): pass

    label("Function_7_1428")

    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    OP_1B(0x3, 0xFF, 0xFFFF)
    OP_1B(0x4, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1468")
    OP_1B(0x1, 0x0, 0x3F)
    OP_1B(0x2, 0x0, 0x40)
    OP_1B(0x3, 0x0, 0x41)
    OP_1B(0x4, 0x0, 0x42)

    label("loc_1468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1485")
    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x1, 0x0, 0x3F)
    OP_1B(0x2, 0x0, 0x40)

    label("loc_1485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_149D")
    OP_1B(0x0, 0x0, 0x3E)
    OP_1B(0x4, 0x0, 0x42)

    label("loc_149D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14B0")
    OP_1B(0x4, 0x0, 0x42)

    label("loc_14B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14D2")
    OP_1B(0x0, 0x0, 0x3E)
    OP_1B(0x1, 0x0, 0x3F)
    OP_1B(0x2, 0x0, 0x40)
    OP_1B(0x3, 0x0, 0x41)

    label("loc_14D2")

    Return()

    # Function_7_1428 end

    def Function_8_14D3(): pass

    label("Function_8_14D3")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1607")
    Sound(14, 0, 100, 0)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xC, 0x1E)
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
    Jump("loc_16A1")

    label("loc_1607")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Is celebrating the Anniversary Festival underneath\x01",
            "the Bell of Crossbell weird or the most appropriate\x01",
            "way to celebrate Crossbell imaginable?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_16A1")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_14D3 end

    def Function_9_16B3(): pass

    label("Function_9_16B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_175F")

    ChrTalk(
        0xFE,
        (
            "I had the entire festival, and I still couldn't\x01",
            "give anything special to Mimi...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, she had a great time, so that's all I\x01",
            "can really ask for.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C53")

    label("loc_175F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1821")

    ChrTalk(
        0xFE,
        "I'm glad that the parade went smoothly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's the largest event of the Anniversary\x01",
            "Festival, so it looks like they had to pay\x01",
            "close attention to traffic while it went on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C53")

    label("loc_1821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1914")

    ChrTalk(
        0xFE,
        (
            "For some reason, the city feels a lot more\x01",
            "energetic today than yesterday. Maybe it's\x01",
            "because of the parade?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The whole thing will be ruined if there's\x01",
            "a car accident, so they must be heavily\x01",
            "regulating the roads today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C53")

    label("loc_1914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1A1F")

    ChrTalk(
        0xFE,
        (
            "That concert down in the Harbor District\x01",
            "was pretty awesome. Mimi thought\x01",
            "so, too, which I'm happy about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "According to the festival schedule, all sorts\x01",
            "of events like it are going to be thrown during\x01",
            "the five days. Maybe we should go to some.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C53")

    label("loc_1A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1AFA")

    ChrTalk(
        0xFE,
        (
            "I've been touring all of the city's food stalls\x01",
            "with Mimi since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After I messed up getting those Arc en Ciel\x01",
            "tickets she really wanted, this is the least\x01",
            "I can do to make it up to her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C53")

    label("loc_1AFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1C53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB8")

    ChrTalk(
        0xFE,
        (
            "Wow, it's as if the highway entrances\x01",
            "changed overnight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I noticed a lot of foreign cars parked outside\x01",
            "of them, but do they really all have permits...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C53")

    label("loc_1BB8")


    ChrTalk(
        0xFE,
        (
            "Wow, it's as if the highway entrances\x01",
            "changed overnight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not to mention, it looks like there's a ton\x01",
            "of illegally parked cars outside of them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C53")

    TalkEnd(0xFE)
    Return()

    # Function_9_16B3 end

    def Function_10_1C57(): pass

    label("Function_10_1C57")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1CD8")

    ChrTalk(
        0xFE,
        (
            "Daddy couldn't take me to Mishelam\x01",
            "or Arc en Ciel, but that's okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We both had lots and lots of fun!\x02",
    )

    CloseMessageWindow()
    Jump("loc_24BF")

    label("loc_1CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_1D24")

    ChrTalk(
        0xFE,
        "The parade was sooo cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did you guys see it, too?\x02",
    )

    CloseMessageWindow()
    Jump("loc_24BF")

    label("loc_1D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F6E")

    ChrTalk(
        0x101,
        (
            "#0000F(If she was at the parade, she might\x01",
            "have noticed something...)\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked if she knew\x01",
            "anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xFE,
        "Have I seen this boy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Umm, actually, I think I might have saw\x01",
            "him following the parade!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FSeriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep! He was at the veeery end, trying\x01",
            "to keep up with the rest of the floats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pretty sure he's the same boy in your\x01",
            "photo, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FGot'cha...\x01",
            "(That lines up with what Elie told me, too.)\x02\x03",
            "#0000FThanks, Mimi. You were a lot of help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 36)
    Jump("loc_2042")

    label("loc_1F6E")


    ChrTalk(
        0xFE,
        (
            "I only remembered him because I was\x01",
            "watching the parade reeeally closely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was at the very end, trying to keep\x01",
            "up with all the floats!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3300FWe must be dealing with quite the\x01",
            "curious little boy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2042")

    Jump("loc_24BF")

    label("loc_2047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_20AC")

    ChrTalk(
        0xFE,
        "The parade was the coolest thing ever!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You were able to see it, right, guys?\x02",
    )

    CloseMessageWindow()
    Jump("loc_24BF")

    label("loc_20AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_20FF")

    ChrTalk(
        0xFE,
        (
            "I get to go see the parade with\x01",
            "Daddy today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't wait!\x02",
    )

    CloseMessageWindow()
    Jump("loc_24BF")

    label("loc_20FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2198")

    ChrTalk(
        0xFE,
        (
            "It might have made me pretty dizzy,\x01",
            "but seeing the concert was awesome!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The whole stage was going boom!\x01",
            "Bang! Badadadadadaaa! ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24BF")

    label("loc_2198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2264")

    ChrTalk(
        0xFE,
        "*munch* *munch* Mmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had popcorn yesterday, too, but I just\x01",
            "can't get enough of it. It's so tasty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Daddy even told me they make it from\x01",
            "corn on the cob! Isn't that crazy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24BF")

    label("loc_2264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_24BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2455")

    ChrTalk(
        0xFE,
        "Hiya, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you going to do stuff at the festival?\x01",
            "Wanna play with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThanks for the invite, Mimi, but we're a\x01",
            "little preoccupied with work right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aw, really? Being the Special Support\x01",
            "Suction must be tough...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FM-Mimi, sweetie, it's touching that you\x01",
            "remembered our name, but you're just\x01",
            "a bit off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FThe Special Support Suction? I suppose\x01",
            "the job can suck on occasion, yes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FYou're a riot, Tio Tot...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24BF")

    label("loc_2455")


    ChrTalk(
        0xFE,
        (
            "Our plan is to visit every single one\x01",
            "of the food stalls now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Have fun with suction work, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_24BF")

    TalkEnd(0xFE)
    Return()

    # Function_10_1C57 end

    def Function_11_24C3(): pass

    label("Function_11_24C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2631")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25B1")

    ChrTalk(
        0xFE,
        (
            "After hanging out in the Entertainment District,\x01",
            "I'll hit up the Harbor District's food stalls, then\x01",
            "wrap the day up with Mishelam's fireworks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm going to enjoy this festival till the bitter end!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_262C")

    label("loc_25B1")


    ChrTalk(
        0xFE,
        "I intend to take my family with me today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what, I can't waste the majesty\x01",
            "of the Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_262C")

    Jump("loc_2A3D")

    label("loc_2631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_26B9")

    ChrTalk(
        0xFE,
        "Ah, that parade was absolutely superb.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes! This year's Anniversary Festival\x01",
            "has been an incredible success! ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3D")

    label("loc_26B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2802")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2770")

    ChrTalk(
        0xFE,
        (
            "Whew, I'm still full from all the food\x01",
            "we had this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the rate things are going, I may not\x01",
            "have the strength to try all the food stalls.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27FD")

    label("loc_2770")


    ChrTalk(
        0xFE,
        (
            "No matter where I look, I keep seeing\x01",
            "all these different food stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, eating at all of them must be\x01",
            "pretty much impossible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27FD")

    Jump("loc_2A3D")

    label("loc_2802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_28B3")

    ChrTalk(
        0xFE,
        (
            "Some random tourist spilled all of his\x01",
            "juice on me! Sheesh, can't people\x01",
            "watch where they're going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Darn it! It'll leave a stain if I\x01",
            "don't wash it out!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3D")

    label("loc_28B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2954")

    ChrTalk(
        0xFE,
        (
            "Yesterday, I stayed over at a friend's\x01",
            "house, and we had pillow fights all night!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gee, that was so much fun. I really love\x01",
            "the festival!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3D")

    label("loc_2954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A19")

    ChrTalk(
        0xFE,
        (
            "*munch* *munch* I hear that\x01",
            "the Harbor District has a bunch of\x01",
            "food stalls, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should check them out if you\x01",
            "have the time. This definitely hits\x01",
            "the spot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A3D")

    label("loc_2A19")


    ChrTalk(
        0xFE,
        "Now, next on the list is... ♪\x02",
    )

    CloseMessageWindow()

    label("loc_2A3D")

    TalkEnd(0xFE)
    Return()

    # Function_11_24C3 end

    def Function_12_2A41(): pass

    label("Function_12_2A41")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AD5")
    Jump("loc_2B1F")

    label("loc_2AD5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2AF5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B1F")

    label("loc_2AF5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B15")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B1F")

    label("loc_2B15")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B1F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2D22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C53")

    ChrTalk(
        0xFE,
        (
            "On the last day of the Anniversary\x01",
            "Festival, Mishelam throws their big,\x01",
            "annual fireworks show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I spent the last year's closing day\x01",
            "there, and boy, lemme tell you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You haven't seen a fireworks show\x01",
            "until you've seen Mishelam's.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2D1D")

    label("loc_2C53")


    ChrTalk(
        0xFE,
        (
            "C'mon, it's the Anniversary Festival,\x01",
            "for crying out loud! Go be kids and\x01",
            "have some fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys should definitely go see the\x01",
            "big fireworks bonanza that's thrown on\x01",
            "the last day at Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D1D")

    Jump("loc_31B9")

    label("loc_2D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2E2C")

    ChrTalk(
        0xFE,
        (
            "This year's parade looked quite a bit\x01",
            "longer than last year's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet the guys running it wanted as many\x01",
            "people as possible to be able to watch it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, I wouldn't be surprised if it was\x01",
            "the event that they put the most effort into.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B9")

    label("loc_2E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2F08")

    ChrTalk(
        0xFE,
        "I mainly came to see all the floats.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People tell me that they added another\x01",
            "this year, bringing the total to seven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With that many, I have no doubt this\x01",
            "parade will be something to remember.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B9")

    label("loc_2F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2FAD")

    ChrTalk(
        0xFE,
        "Having fun yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know you're on duty and all, but it'll be\x01",
            "a waste if you don't enjoy yourselves.\x01",
            "This only happens once a year, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B9")

    label("loc_2FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3053")

    ChrTalk(
        0xFE,
        (
            "This year's festival is much more\x01",
            "gorgeous than previous years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd say it's representative of Crossbell's\x01",
            "flourishing economy, wouldn't you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B9")

    label("loc_3053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_31B9")

    ChrTalk(
        0xFE,
        (
            "Yesterday, Mayor MacDowell stood tall\x01",
            "on the opening ceremony's stage and\x01",
            "gave his address, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I hear there was an assassination attempt\x01",
            "made by his secretary. Fortunately, he seems\x01",
            "to be in higher spirits than I thought he'd be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He has quite the mental fortitude for someone\x01",
            "his age. Well, that's old Mayor MacDowell for\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B9")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_2A41 end

    def Function_13_31C1(): pass

    label("Function_13_31C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3247")

    ChrTalk(
        0xFE,
        (
            "We totally ended up eating at every\x01",
            "single food stall, didn't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I'm sorta scared to weigh myself now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_34CF")

    label("loc_3247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_32EC")

    ChrTalk(
        0xFE,
        (
            "Hmm, it's been a tight race, and that ice\x01",
            "cream is SO good, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I think the popcorn from that stall is just\x01",
            "as totally lit as it gets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34CF")

    label("loc_32EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_338E")

    ChrTalk(
        0xFE,
        (
            "Hey, which stall did you think was the \x01",
            "most fire today? Like, what's tops to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Personally, hamburgers are just, like,\x01",
            "bae to the max.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34CF")

    label("loc_338E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_33FA")

    ChrTalk(
        0xFE,
        (
            "...Hey, wouldn't you rather hang out\x01",
            "with a boyfriend or something instead\x01",
            "of, like, me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34CF")

    label("loc_33FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_346D")

    ChrTalk(
        0xFE,
        "*munch* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* If all I do is eat festival food,\x01",
            "I'm, like, totally gonna get fat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34CF")

    label("loc_346D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_34CF")

    ChrTalk(
        0xFE,
        "Hey, hey. Where to next?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Chilling in Central Square is getting kinda\x01",
            "old, TBH.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34CF")

    TalkEnd(0xFE)
    Return()

    # Function_13_31C1 end

    def Function_14_34D3(): pass

    label("Function_14_34D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_354C")

    ChrTalk(
        0xFE,
        "Moooood...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, like, I think it'd be scarier if\x01",
            "you kept gaining weight and didn't\x01",
            "know why.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C9")

    label("loc_354C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_35D6")

    ChrTalk(
        0xFE,
        (
            "Hold on. What happened to hamburgers\x01",
            "being 'bae to the max'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anything is bae, it's gotta be ice cream,\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C9")

    label("loc_35D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_364E")

    ChrTalk(
        0xFE,
        "Pssh! The ice cream is WAY better!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll just have to load up on both\x01",
            "later to decide for sure!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C9")

    label("loc_364E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_367D")

    ChrTalk(
        0xFE,
        "Ugh, like, don't remind me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37C9")

    label("loc_367D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_373F")

    ChrTalk(
        0xFE,
        (
            "We can chillax, though. After the festival\x01",
            "ends, we'll just hit up those squad goals\x01",
            "and start dieting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You only live once, so we've got to snack\x01",
            "now while we still can!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C9")

    label("loc_373F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_37C9")

    ChrTalk(
        0xFE,
        "Same here... Off to the Harbor District, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We could peep on that concert thing they've\x01",
            "been doing since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37C9")

    TalkEnd(0xFE)
    Return()

    # Function_14_34D3 end

    def Function_15_37CD(): pass

    label("Function_15_37CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3862")

    ChrTalk(
        0xFE,
        (
            "I sure hope I hand out all of my\x01",
            "balloons today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was told if I manage to hand them all\x01",
            "out, I'd probably get a bonus.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BE2")

    label("loc_3862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_391B")

    ChrTalk(
        0xFE,
        (
            "Whoops... I totally zoned out while thinking\x01",
            "about where all the balloons in the sky\x01",
            "fly off to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the air runs out eventually, so\x01",
            "they must fall somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BE2")

    label("loc_391B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3A70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39FF")

    ChrTalk(
        0xFE,
        (
            "Occasionally, I can see the balloons I\x01",
            "hand out fly far out into the horizon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Flying, flying, flying... Will they manage\x01",
            "to reach Aidios in the end?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Bit of a depressing sight, isn't it?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3A6B")

    label("loc_39FF")


    ChrTalk(
        0xFE,
        (
            "Occasionally, I can see balloons\x01",
            "fly far out into the horizon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do they end up seeing the Goddess?\x02",
    )

    CloseMessageWindow()

    label("loc_3A6B")

    Jump("loc_3BE2")

    label("loc_3A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_3AD1")

    ChrTalk(
        0xFE,
        "Balloons! Come get your balloons!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They're fun, colorful, and even float!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BE2")

    label("loc_3AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B52")

    ChrTalk(
        0xFE,
        (
            "Ugh, all these freakin' couples walking\x01",
            "everywhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just take a balloon and stop holding\x01",
            "hands, okay?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BE2")

    label("loc_3B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3BE2")

    ChrTalk(
        0xFE,
        "Here, have a balloon! They're free!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "During the Anniversary Festival, even\x01",
            "part-timers like me can get bonuses.\x01",
            "I'm fired up!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BE2")

    TalkEnd(0xFE)
    Return()

    # Function_15_37CD end

    def Function_16_3BE6(): pass

    label("Function_16_3BE6")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4533")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C44")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3C44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C64")
    OP_AF(0x7A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_452E")

    label("loc_3C64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C78")
    Jump("loc_452E")

    label("loc_3C78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_452E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4050")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC3")

    ChrTalk(
        0x101,
        (
            "#0001FExcuse me, but mind if I ask you a\x01",
            "few questions?\x02\x03",
            "We're conducting an investigation\x01",
            "on the recent thefts, you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're talking about the stalls that\x01",
            "have been robbed all across the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No worries. I think I'll be okay here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, I'm right in the middle of Central\x01",
            "Square. With this many people walking\x01",
            "around, I'm practically untouchable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FThen again, it's not as if the tourists are\x01",
            "paying much attention to anything.\x02\x03",
            "On the contrary, the likelihood of our thief\x01",
            "using the crowd to avoid detection is\x01",
            "quite high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Psh, everything's fine. Just leave it to\x01",
            "me, guys!\x02",
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
    Sleep(1200)

    ChrTalk(
        0x102,
        "#0104F(Well, she doesn't SEEM nervous...)\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x7)
    Jump("loc_404B")

    label("loc_3FC3")


    ChrTalk(
        0xFE,
        (
            "Even one of the stalls in the middle of\x01",
            "Central Square was hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe that stall near East Street just\x01",
            "wasn't careful enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_404B")

    Jump("loc_452E")

    label("loc_4050")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4063")
    Call(0, 17)
    Jump("loc_452E")

    label("loc_4063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_40FD")

    ChrTalk(
        0xFE,
        (
            "In the mood for some scrumptious,\x01",
            "fluffy popcorn?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to catch the last bus home,\x01",
            "so if you want some, lemme know\x01",
            "quick, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_452E")

    label("loc_40FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4196")

    ChrTalk(
        0xFE,
        (
            "Oh, darn. It seems that I've run out\x01",
            "of all my supplies already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good thing the department store\x01",
            "is right there. How convenient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_452E")

    label("loc_4196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_431B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4257")

    ChrTalk(
        0xFE,
        "People say that the thief was caught!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, good! What goes around,\x01",
            "comes around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you want mira THAT much, just\x01",
            "open up your own stall or something!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4316")

    label("loc_4257")


    ChrTalk(
        0xFE,
        (
            "Crossbellans sure are reckless\x01",
            "when it comes to their wallets...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Back when I ran a shop in the Empire,\x01",
            "business was slooooow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep, I think coming to Crossbell was\x01",
            "a good call.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4316")

    Jump("loc_452E")

    label("loc_431B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_43BC")

    ChrTalk(
        0xFE,
        (
            "Looks like I won't have any time to\x01",
            "go sightseeing today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's only because business is\x01",
            "booming, so I can't be too angry\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_452E")

    label("loc_43BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4466")

    ChrTalk(
        0xFE,
        (
            "It's hard to resist the tempting smell\x01",
            "of popcorn, so sales are up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please be careful not to tip over the\x01",
            "bag, okay? It'll all come spilling out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_452E")

    label("loc_4466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_452E")

    ChrTalk(
        0xFE,
        (
            "How about some popcorn, folks? It'll\x01",
            "be the tastiest thing you'll have all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whether you're going to see a play\x01",
            "or a concert, there's no better snack\x01",
            "to munch on while watching.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_452E")

    Jump("loc_3BF3")

    label("loc_4533")

    TalkEnd(0xFE)
    Return()

    # Function_16_3BE6 end

    def Function_17_4537(): pass

    label("Function_17_4537")


    ChrTalk(
        0xFE,
        "How about some popcorn, folks?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'd be surprised how much effort\x01",
            "I put into making my popcorn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why it's so dang tasty. Want\x01",
            "to try some?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1CA),
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
            scpstr(SCPSTR_CODE_ITEM, 0x1CA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x14)
    Return()

    # Function_17_4537 end

    def Function_18_4656(): pass

    label("Function_18_4656")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4680")
    Call(0, 44)
    Return()

    label("loc_4680")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_468D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E25")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46DE")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_46DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46FE")
    OP_AF(0x78)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E20")

    label("loc_46FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4712")
    Jump("loc_4E20")

    label("loc_4712")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E20")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4995")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47BE")

    ChrTalk(
        0xFE,
        "You're with the CPD, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard the story... The thieves\x01",
            "have been arrested already?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4824")

    label("loc_47BE")


    ChrTalk(
        0xFE,
        "You're with the CPD, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard the story... The thieves\x01",
            "have been arrested already?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4824")


    ChrTalk(
        0xFE,
        (
            "Awesome. Now I don't have to worry\x01",
            "about my entire profit getting stolen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you don't mind, would you take this?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1AE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1AE, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_491C")

    ChrTalk(
        0x101,
        "#0002FWow, thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4947")

    label("loc_491C")


    ChrTalk(
        0x103,
        "#0203FThank you. We will use it well.\x02",
    )

    CloseMessageWindow()

    label("loc_4947")


    ChrTalk(
        0xFE,
        (
            "No, I should be the one thanking\x01",
            "you for catching that criminal.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBC, 6)
    Jump("loc_4E20")

    label("loc_4995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4A0E")

    ChrTalk(
        0xFE,
        "Hamburgers...are pretty good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're good leftover food, so buy\x01",
            "as much as you'd like...please.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E20")

    label("loc_4A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4A9A")

    ChrTalk(
        0xFE,
        (
            "Prime rib sandwiches and donairs have\x01",
            "been becoming more popular in Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Personally, I prefer a good hamburger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E20")

    label("loc_4A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4C90")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B01")

    ChrTalk(
        0xFE,
        (
            "Finally, I can sell my hamburgers\x01",
            "in peace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thank you, everyone.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C8B")

    label("loc_4B01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C0C")

    ChrTalk(
        0xFE,
        (
            "This is the first time I've run a food stall\x01",
            "in a big metropolis like Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's also the first time I've been robbed,\x01",
            "actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When exactly was I robbed? I keep thinking\x01",
            "about it, but it's still a mystery.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C8B")

    label("loc_4C0C")


    ChrTalk(
        0xFE,
        "Hamburgers... Want some?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They aren't too complicated to make.\x01",
            "If you think you could do it, then you\x01",
            "probably could.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C8B")

    Jump("loc_4E20")

    label("loc_4C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_4D1A")

    ChrTalk(
        0xFE,
        (
            "Crossbell has been great for business\x01",
            "so far...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even an awkward person like me is\x01",
            "able to get a lot of customers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E20")

    label("loc_4D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4D9A")

    ChrTalk(
        0xFE,
        "Would you like some...hamburgers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't feel pressured, though. But if\x01",
            "you want some, just let me know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E20")

    label("loc_4D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4E20")

    ChrTalk(
        0xFE,
        "Are you in the mood for...hamburgers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's the perfect harmony of meat, veggies,\x01",
            "and carbs... A miracle junk food.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E20")

    Jump("loc_468D")

    label("loc_4E25")

    TalkEnd(0xFE)
    Return()

    # Function_18_4656 end

    def Function_19_4E29(): pass

    label("Function_19_4E29")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AC2")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E87")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4E87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EA7")
    OP_AF(0x79)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5ABD")

    label("loc_4EA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EBB")
    Jump("loc_5ABD")

    label("loc_4EBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ABD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51CB")

    ChrTalk(
        0xFE,
        (
            "Oh, aren't you those police officers\x01",
            "that helped me out earlier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thanks to you, I dodged a bullet! ㈱\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FF3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_4FC2")

    ChrTalk(
        0x101,
        (
            "#0002FIt was dangerous, but I'm glad\x01",
            "it worked out in the end.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FEE")

    label("loc_4FC2")


    ChrTalk(
        0x101,
        "#0012FIt was a little dangerous, yeah.\x02",
    )

    CloseMessageWindow()

    label("loc_4FEE")

    Jump("loc_508F")

    label("loc_4FF3")


    ChrTalk(
        0x101,
        "#0000FIt was a close call, that's for sure.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_5062")

    ChrTalk(
        0x104,
        "#0304FWe saw through their every move!\x02",
    )

    CloseMessageWindow()
    Jump("loc_508F")

    label("loc_5062")


    ChrTalk(
        0x104,
        "#0303FNegligence is our greatest enemy.\x02",
    )

    CloseMessageWindow()

    label("loc_508F")


    ChrTalk(
        0xFE,
        (
            "Here, take this. You can call it a\x01",
            "token of my appreciation. ㈱\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1C0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1C0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_515A")

    ChrTalk(
        0x101,
        "#0000FWe'll take good care of it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_517A")

    label("loc_515A")


    ChrTalk(
        0x102,
        "#0100FThank you very much.\x02",
    )

    CloseMessageWindow()

    label("loc_517A")


    ChrTalk(
        0xFE,
        (
            "Police officers have to do their best\x01",
            "while working, same as me. ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 0)
    Jump("loc_5ABD")

    label("loc_51CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_527E")

    ChrTalk(
        0xFE,
        (
            "Aw, it's already the last day of the\x01",
            "festival? I'm going to cry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, you better believe I'll be here next\x01",
            "year with my sweets, so don't forget me! ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ABD")

    label("loc_527E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_530D")

    ChrTalk(
        0xFE,
        "Low calorie food is a fad!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And honestly, if you really like your\x01",
            "sweets, you're going to end up eating\x01",
            "them anyway. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ABD")

    label("loc_530D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_58C6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_53B1")

    ChrTalk(
        0xFE,
        (
            "Thanks for before, everyone. I was\x01",
            "able to make it through unscathed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The police can be pretty reliable.\x01",
            "Surprise, surprise! ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C1")

    label("loc_53B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5825")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_574C")

    ChrTalk(
        0x101,
        (
            "#0001FExcuse me, do you have a moment?\x02\x03",
            "We're conducting an investigation\x01",
            "on the recent thefts, you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, that? Someone from the Business Owners'\x01",
            "Association came by earlier to tell me to\x01",
            "keep an eye out for anyone shady...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FThey already hit one of the square's stalls.\x02\x03",
            "So, any ideas? Seen the thief runnin'\x01",
            "around or anything like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nope! ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been getting a lot of customers,\x01",
            "so I can't spare the energy to look\x01",
            "at what's happening at other stands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FWell, that's a valid excuse.\x02",
    )

    CloseMessageWindow()
    OP_92(0x101, 0xFFFFFF2E, 0x56C2, 0x1F4)
    Sleep(500)
    OP_92(0x101, 0xFFFFCC16, 0x36BA, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0008FNow that you mention it, you ARE right in\x01",
            "front of Times and near the Back Alley...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep! And you're also forgetting that the\x01",
            "Administrative District is right down there! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Most of our customers today came into\x01",
            "the city to watch the parade. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0103FY-You certainly seem busy.\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x8)
    Jump("loc_5820")

    label("loc_574C")


    ChrTalk(
        0xFE,
        "Oh, I have no clue about those thefts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, if they want to come at me,\x01",
            "come at me! I'll catch 'em for you! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FUm, yeah. We don't support or condone\x01",
            "civilians doing anything rash, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5820")

    Jump("loc_58C1")

    label("loc_5825")


    ChrTalk(
        0xFE,
        (
            "Looking for sweets, sweets, and more\x01",
            "sweets?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're getting tired of walking around\x01",
            "the festival and wanna reenergize, grab\x01",
            "a bagful to go! ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58C1")

    Jump("loc_5ABD")

    label("loc_58C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_5968")

    ChrTalk(
        0xFE,
        (
            "I may be running a sweets stall, but I\x01",
            "don't have a very big sweet tooth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, they're nothing more than\x01",
            "sugar-filled pastries, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ABD")

    label("loc_5968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5A04")

    ChrTalk(
        0xFE,
        (
            "You'd be surprised how many of\x01",
            "my customers are young ladies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In most cases, girls really, really\x01",
            "like the taste of sweet stuff! ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ABD")

    label("loc_5A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5ABD")

    ChrTalk(
        0xFE,
        (
            "Good morning, everyone! Welcome\x01",
            "to my lovely little sweets stall. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Two men and two girls...? Are you\x01",
            "in the middle of a double date?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* I'm so jealous. ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_5ABD")

    Jump("loc_4E36")

    label("loc_5AC2")

    TalkEnd(0xFE)
    Return()

    # Function_19_4E29 end

    def Function_20_5AC6(): pass

    label("Function_20_5AC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5AD7")
    Jump("loc_5BDE")

    label("loc_5AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_5B0A")

    ChrTalk(
        0xFE,
        "Welcome! Want something to eat?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BDE")

    label("loc_5B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5BD5")

    ChrTalk(
        0xFE,
        (
            "Good morning! If you're looking for\x01",
            "some breakfast, try eating here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've started to be more aggressive\x01",
            "in pulling in customers, so hopefully\x01",
            "things'll be getting busier for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BDE")

    label("loc_5BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5BDE")

    label("loc_5BDE")

    TalkEnd(0xFE)
    Return()

    # Function_20_5AC6 end

    def Function_21_5BE2(): pass

    label("Function_21_5BE2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5DDC")
    OP_93(0xFE, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D31")
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0xFE,
        "C'mon, let's go to Mishelam!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can spend the night at the hotel\x01",
            "and play in the theme park!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "A-Are you crazy?! How much do you\x01",
            "think it costs to stay there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "We're going to see the closing ceremony\x01",
            "today, and that's final, Ryu! You better\x01",
            "not go wandering off now, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    SetScenarioFlags(0x0, 6)
    Jump("loc_5DD7")

    label("loc_5D31")


    ChrTalk(
        0xFE,
        (
            "Aw, this sucks. The closing ceremony\x01",
            "is so freakin' boring!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I say we ask Sis where she wants to go,\x01",
            "'cause she'd probably say Mishelam.\x01",
            "How about it, Pops?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DD7")

    Jump("loc_65AF")

    label("loc_5DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_5ED3")
    OP_93(0xFE, 0x5A, 0x0)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0xFE,
        "Hey, Pops, buy me this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And then let's get some juice and popcorn!\x01",
            "We're goin' all out for the festival, after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Ahaha! That's not a bad idea...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Hold on now! Try to show a bit\x01",
            "of restraint, son!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    Jump("loc_65AF")

    label("loc_5ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_6314")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61B2")

    ChrTalk(
        0x101,
        (
            "#0003F(Might as well try asking Ryu about\x01",
            "Colin since I'm here...)\x02\x03",
            "#0000FRyu, got a moment? We're looking\x01",
            "for this little kid...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked if he knew\x01",
            "anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xFE,
        "Huh? This kid got lost?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lemme think. I definitely feel like I've\x01",
            "seen him before, but then again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3306FHow exceedingly vague.\x02\x03",
            "#3300FYou're a boy, are you not?\x01",
            "You should act like one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ouch... Harsh much?\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "W-Well, I think I might have seen\x01",
            "him for a sec.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was kinda focused on the parade,\x01",
            "so I wasn't looking at the other kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI can't blame you there. Thanks anyway,\x01",
            "Ryu. You were a big help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 36)
    Jump("loc_630F")

    label("loc_61B2")


    ChrTalk(
        0xFE,
        (
            "I was kinda focused on the parade,\x01",
            "so I wasn't lookin' at the other kids.\x01",
            "I have a feeling I saw him, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, Lloyd, who's this girl\x01",
            "hanging out with you? She sounds\x01",
            "like a know-it-all, if you ask me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3302FNow, is that any way to\x01",
            "speak to a lady?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012F(Etiquette is probably the last\x01",
            "thing on Ryu's mind, Renne.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_630F")

    Jump("loc_65AF")

    label("loc_6314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6394")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Woohooooo! That was SICK!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, man, I wish Sis could've\x01",
            "been able to see it, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65AF")

    label("loc_6394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_63E3")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "I can't freakin' wait for this parade!\x02",
    )

    CloseMessageWindow()
    Jump("loc_65AF")

    label("loc_63E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_648C")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        (
            "C'mon, Pops! Let's check out the\x01",
            "department store while we wait!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, business comes first! This\x01",
            "is what they call market research!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65AF")

    label("loc_648C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_64ED")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        (
            "Oh, the department store is having a\x01",
            "sale! Pops, let's go have a look!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65AF")

    label("loc_64ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_65AF")

    ChrTalk(
        0xFE,
        "Yo, Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You gotta patrol on the last day of the\x01",
            "festival? Hehe, sucks for you guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, yeah.\x01",
            "Don't get too out of control now,\x01",
            "you hear me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65AF")

    TalkEnd(0xFE)
    Return()

    # Function_21_5BE2 end

    def Function_22_65B3(): pass

    label("Function_22_65B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6665")

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival's closing ceremony\x01",
            "is going to be held this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a Crossbellan, I feel compelled to see\x01",
            "out the festival to its end!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6862")

    label("loc_6665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_66F9")

    ChrTalk(
        0xFE,
        "Ahaha! Festivals really are the best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The parade was spectacular. It was as if\x01",
            "it represented the heart of us Crossbellans.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6862")

    label("loc_66F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6785")

    ChrTalk(
        0xFE,
        (
            "Ryu, listen. When the floats come around,\x01",
            "strike a pose with the peace sign!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll take a picture of you, all right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6862")

    label("loc_6785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_67D3")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        (
            "You have quite the impressive\x01",
            "vocabulary, huh, Ryu?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6862")

    label("loc_67D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_682B")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        (
            "I'd rather avoid thinking about business\x01",
            "during the festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6862")

    label("loc_682B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6862")

    ChrTalk(
        0xFE,
        "Ahahaha! I'm having the time of my life!\x02",
    )

    CloseMessageWindow()

    label("loc_6862")

    TalkEnd(0xFE)
    Return()

    # Function_22_65B3 end

    def Function_23_6866(): pass

    label("Function_23_6866")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68DA")

    ChrTalk(
        0xFE,
        (
            "Wendy works in this part of the city,\x01",
            "doesn't she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why don't we find her and say hi?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6926")

    label("loc_68DA")


    ChrTalk(
        0xFE,
        (
            "Umm, would it be rude to say hello\x01",
            "to my daughter while she's working?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6926")

    TalkEnd(0xFE)
    Return()

    # Function_23_6866 end

    def Function_24_692A(): pass

    label("Function_24_692A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I wanna go to the department store!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We can see Wendy whenever we want!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_692A end

    def Function_25_6982(): pass

    label("Function_25_6982")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A13")
    OP_4B(0x18, 0xFF)

    ChrTalk(
        0xFE,
        "Meifa, look! Food stalls...everywhere!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I HAVE to eat some of that! C'mon,\x01",
            "buy some!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "Buy it yourself!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    OP_4C(0x18, 0xFF)
    Jump("loc_6A4C")

    label("loc_6A13")


    ChrTalk(
        0xFE,
        (
            "Hey, Meifa. Wanna do me a favor\x01",
            "and buy me this...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A4C")

    TalkEnd(0xFE)
    Return()

    # Function_25_6982 end

    def Function_26_6A50(): pass

    label("Function_26_6A50")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B27")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "I took the day off from the hospital\x01",
            "to have some fun at the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to get rid of all that pent-up\x01",
            "stress I've built up while working as\x01",
            "a St. Ursula nurse!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x87, 0x0)
    SetScenarioFlags(0x1, 1)
    Jump("loc_6BEF")

    label("loc_6B27")


    ChrTalk(
        0xFE,
        (
            "Can't you be quiet for, like, one minute?!\x01",
            "You're acting like a giddy child!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness gracious, it's the Anniversary\x01",
            "Festival. Why do I still have to look after\x01",
            "Cirone? She's a grown woman!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BEF")

    TalkEnd(0xFE)
    Return()

    # Function_26_6A50 end

    def Function_27_6BF3(): pass

    label("Function_27_6BF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6D48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CA4")

    ChrTalk(
        0xFE,
        (
            "I saw one of the bracers headed\x01",
            "toward Crossbell Airport earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Was he heading out of town for a job?\x01",
            "Those folks really do work hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_6D43")

    label("loc_6CA4")


    ChrTalk(
        0xFE,
        (
            "Bracers are efficient, reliable, and they\x01",
            "make sure to put citizens first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only are they dependable, but they\x01",
            "can also be tough like detectives.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D43")

    Jump("loc_72F4")

    label("loc_6D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6D56")
    Jump("loc_72F4")

    label("loc_6D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6D64")
    Jump("loc_72F4")

    label("loc_6D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6E05")
    OP_93(0xFE, 0xC5, 0x0)

    ChrTalk(
        0xFE,
        (
            "*whistle* All orbal vehicles must keep\x01",
            "their speed to a minimum!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pedestrians, please make way for\x01",
            "vehicles to ensure your safety!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72F4")

    label("loc_6E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_72F4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6F04")

    ChrTalk(
        0xFE,
        "Keep up the good work, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad today isn't as crazy as the first\x01",
            "day with the opening ceremony, but...\x01",
            "the crowd is really something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should've tried to request \x01",
            "backup from headquarters...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72F4")

    label("loc_6F04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_7209")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7039")

    ChrTalk(
        0x19,
        (
            "The parked vehicles in question seem\x01",
            "to be concentrated around the eastern\x01",
            "and western exits of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Once you've checked all of them,\x01",
            "please contact Rebecca back at\x01",
            "headquarters, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Since we're about to get busy, I doubt\x01",
            "we'll be able to provide much backup.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7204")

    label("loc_7039")


    ChrTalk(
        0x19,
        (
            "Truth be told, this illegal parking thing\x01",
            "should've already been dealt with\x01",
            "by us rookies, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "...we're swamped right now. Sorry, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FDon't worry about it, Kate. We're the ones\x01",
            "who accepted the request, remember?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Thanks, everyone. And one other thing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Once you attach a warning sticker to a\x01",
            "vehicle, you can't take it off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "So try not to attach them to the wrong\x01",
            "ones, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FRoger. Just leave it to us!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_7204")

    Jump("loc_72F4")

    label("loc_7209")


    ChrTalk(
        0xFE,
        "Keep up the good work, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad today isn't as crazy as the first\x01",
            "day, with the opening ceremony, but...\x01",
            "the crowd is really something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should've tried to request the\x01",
            "department for more backup...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72F4")

    TalkEnd(0xFE)
    Return()

    # Function_27_6BF3 end

    def Function_28_72F8(): pass

    label("Function_28_72F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_73AC")

    ChrTalk(
        0xFE,
        (
            "Since I realized there's still so much\x01",
            "left to see in Crossbell, I extended\x01",
            "our stay by four days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now we'll be able to enjoy ourselves\x01",
            "at our own pace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_754E")

    label("loc_73AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7431")

    ChrTalk(
        0xFE,
        (
            "Now that I've toured around haphazardly,\x01",
            "I have absolutely no idea what to do next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What should we do today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_754E")

    label("loc_7431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_74E8")

    ChrTalk(
        0xFE,
        (
            "Yesterday, the two of us went and walked\x01",
            "around the festive Harbor District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite those vulgar delinquents causing\x01",
            "some trouble, it was a pretty good time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_754E")

    label("loc_74E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_754E")

    ChrTalk(
        0xFE,
        "My wife and I are here on our honeymoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just hope we can make lots of memories.\x02",
    )

    CloseMessageWindow()

    label("loc_754E")

    TalkEnd(0xFE)
    Return()

    # Function_28_72F8 end

    def Function_29_7552(): pass

    label("Function_29_7552")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_75C2")

    ChrTalk(
        0xFE,
        (
            "We might be here a while, but this\x01",
            "is a once-in-a-lifetime honeymoon.\x01",
            "I want to savor it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7688")

    label("loc_75C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7613")

    ChrTalk(
        0xFE,
        (
            "Geez, didn't I say we should have\x01",
            "made some kind of schedule?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7688")

    label("loc_7613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7643")

    ChrTalk(
        0xFE,
        "Men love that kind of stuff.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7688")

    label("loc_7643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7688")

    ChrTalk(
        0xFE,
        (
            "I'm so excited. I've always\x01",
            "wanted to visit Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7688")

    TalkEnd(0xFE)
    Return()

    # Function_29_7552 end

    def Function_30_768C(): pass

    label("Function_30_768C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_770F")

    ChrTalk(
        0xFE,
        "My train home is about to leave!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But...I still want to see the city!\x01",
            "Can't I stay just a little longer?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78B7")

    label("loc_770F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_77A0")

    ChrTalk(
        0xFE,
        "That orbal store is so unique!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The way all those different orbments\x01",
            "were elegantly displayed was downright\x01",
            "breathtaking!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78B7")

    label("loc_77A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7841")

    ChrTalk(
        0xFE,
        (
            "That department store was the coolest\x01",
            "thing in the world!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been to my fair share of stores, but\x01",
            "I've never been in one that massive!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78B7")

    label("loc_7841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_78B7")

    ChrTalk(
        0xFE,
        "This city is full of one-of-a-kind shops.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm having a hard time choosing which\x01",
            "one to go to next.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78B7")

    TalkEnd(0xFE)
    Return()

    # Function_30_768C end

    def Function_31_78BB(): pass

    label("Function_31_78BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7965")

    ChrTalk(
        0xFE,
        (
            "I think I've eaten at most of Crossbell's\x01",
            "restaurants now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, now what? Should I make my\x01",
            "way to the fabled Mishelam and try\x01",
            "my luck there?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B94")

    label("loc_7965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7A3F")

    ChrTalk(
        0xFE,
        (
            "I went to an Eastern restaurant over\x01",
            "on East Street, and...it was incredible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think there would be such authentic\x01",
            "Eastern dishes here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just the thought of it is\x01",
            "enough to make me drool.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B94")

    label("loc_7A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7ACD")

    ChrTalk(
        0xFE,
        (
            "I may have eaten here yesterday, too,\x01",
            "but it was just as delicious the second time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Should I try some junk food next?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B94")

    label("loc_7ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7B94")

    ChrTalk(
        0xFE,
        (
            "Crossbell State, the biggest melting\x01",
            "pot in all of Zemuria...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps this will be where I meet that\x01",
            "fateful dish that makes my taste buds\x01",
            "go wild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, let's get to eating!\x02",
    )

    CloseMessageWindow()

    label("loc_7B94")

    TalkEnd(0xFE)
    Return()

    # Function_31_78BB end

    def Function_32_7B98(): pass

    label("Function_32_7B98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7BC1")

    ChrTalk(
        0xFE,
        "#1200FGrrrrrowl...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7DC4")

    label("loc_7BC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7BCF")
    Jump("loc_7DC4")

    label("loc_7BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7BF2")

    ChrTalk(
        0xFE,
        "#1200FGrrrrr...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7DC4")

    label("loc_7BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7C18")

    ChrTalk(
        0xFE,
        "#1200FGrrrrrowl...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7DC4")

    label("loc_7C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7DC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D63")

    ChrTalk(
        0xFE,
        "#1200FGrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0202F*pet* *pet*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0102F*gently caresses*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FEverything's so peaceful.\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#0306FFor whatever reason, everyone goes into\x01",
            "dummy mode when Zeit's around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0204FIt's unavoidable. When Zeit sunbathes,\x01",
            "his fur turns all soft and fluffy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7DC4")

    label("loc_7D63")


    ChrTalk(
        0xFE,
        "#1200FGrrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202F(Maybe I should go buy some bones\x01",
            "for him to snack on later...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DC4")

    TalkEnd(0xFE)
    Return()

    # Function_32_7B98 end

    def Function_33_7DC8(): pass

    label("Function_33_7DC8")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x1, 3)
    Call(0, 35)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E53")

    ChrTalk(
        0x101,
        (
            "#0004F(I might have something Coppe\x01",
            "would enjoy...)\x02\x03",
            "#0000F(I'm sure it'll be okay giving this to him.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x52, 0)

    label("loc_7E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9053")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7EC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_904E")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "Talk")
    MenuCmd(1, 1, "Give Food")
    MenuCmd(1, 1, "Leave")
    ClearScenarioFlags(0x1, 3)
    Call(0, 35)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F16")
    MenuCmd(3, 1, 0x1)

    label("loc_7F16")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F48")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_7F48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9019")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_7F86")
    MenuCmd(1, 1, "Snow Crab")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7F86")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_7FAD")
    MenuCmd(1, 1, "Armorican Carp")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7FAD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_7FD4")
    MenuCmd(1, 1, "Tiger Rockfish")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7FD4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_7FF6")
    MenuCmd(1, 1, "Rockeater")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7FF6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_8013")
    MenuCmd(1, 1, "Carp")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8013")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_8035")
    MenuCmd(1, 1, "Raineater")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8035")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_8056")
    MenuCmd(1, 1, "Azelfish")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8056")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_8076")
    MenuCmd(1, 1, "Kasagin")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8076")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_809C")
    MenuCmd(1, 1, "Rainbow Trout")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_809C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_80BA")
    MenuCmd(1, 1, "Trout")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_80D9")
    MenuCmd(1, 1, "Salmon")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_80F5")
    MenuCmd(1, 1, "Eel")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_8118")
    MenuCmd(1, 1, "Pearlglass")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8118")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_8140")
    MenuCmd(1, 1, "Gluttonous Bass")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8140")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_8162")
    MenuCmd(1, 1, "Viperhead")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8162")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_8185")
    MenuCmd(1, 1, "Pythonhead")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8185")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_81A5")
    MenuCmd(1, 1, "Catfish")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_81A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_81C8")
    MenuCmd(1, 1, "Queen Crab")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_81C8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_81ED")
    MenuCmd(1, 1, "Electric Eel")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_81ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_8213")
    MenuCmd(1, 1, "Demon Catfish")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8213")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_8235")
    MenuCmd(1, 1, "Arch Crab")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8235")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_8259")
    MenuCmd(1, 1, "Gold Salmon")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8259")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_827C")
    MenuCmd(1, 1, "Noble Carp")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_827C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_82A0")
    MenuCmd(1, 1, "Serpenthead")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_82A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_82C1")
    MenuCmd(1, 1, "Cat Food")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_82C1")

    MenuCmd(1, 1, "Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_830B")
    Jump("loc_900A")

    label("loc_830B")

    EventBegin(0x1)
    Fade(500)
    SetChrPos(0x1F, -21980, 1300, -19300, 270)
    SetChrPos(0x0, -23900, 1300, -19070, 89)
    SetChrPos(0x1, -23540, 1300, -20210, 89)
    SetChrPos(0x2, -25020, 1300, -19860, 89)
    SetChrPos(0x3, -25130, 1300, -18930, 89)
    SetChrPos(0x4, -26200, 1300, -19870, 89)
    SetChrPos(0x5, -26790, 1300, -19180, 89)
    OP_68(-23130, 3900, -19610, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    ChrTalk(
        0xFE,
        "Nyannyan... ㈱\x02",
    )

    CloseMessageWindow()

    def lambda_83D1():

        label("loc_83D1")

        TurnDirection(0x0, 0x1F, 0)
        Yield()
        Jump("loc_83D1")

    QueueWorkItem2(0x0, 1, lambda_83D1)

    def lambda_83E3():

        label("loc_83E3")

        TurnDirection(0x1, 0x1F, 0)
        Yield()
        Jump("loc_83E3")

    QueueWorkItem2(0x1, 1, lambda_83E3)

    def lambda_83F5():

        label("loc_83F5")

        TurnDirection(0x2, 0x1F, 0)
        Yield()
        Jump("loc_83F5")

    QueueWorkItem2(0x2, 1, lambda_83F5)

    def lambda_8407():

        label("loc_8407")

        TurnDirection(0x3, 0x1F, 0)
        Yield()
        Jump("loc_8407")

    QueueWorkItem2(0x3, 1, lambda_8407)

    def lambda_8419():

        label("loc_8419")

        TurnDirection(0x4, 0x1F, 0)
        Yield()
        Jump("loc_8419")

    QueueWorkItem2(0x4, 1, lambda_8419)

    def lambda_842B():

        label("loc_842B")

        TurnDirection(0x5, 0x1F, 0)
        Yield()
        Jump("loc_842B")

    QueueWorkItem2(0x5, 1, lambda_842B)
    SetChrFlags(0x1F, 0x8000)
    OP_93(0x1F, 0x0, 0x1F4)
    Sleep(50)
    ClearChrFlags(0x1F, 0x1)
    Sound(814, 0, 80, 0)

    def lambda_8457():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x708, 0x1F40)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_8457)
    WaitChrThread(0x1F, 1)
    Sound(814, 0, 80, 0)

    def lambda_847E():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1130, 0x1388)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_847E)
    WaitChrThread(0x1F, 1)
    Sound(854, 0, 80, 0)

    def lambda_84A5():
        OP_9D(0xFE, 0xFFFFA75E, 0x514, 0xFFFFDFBC, 0x708, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_84A5)
    WaitChrThread(0x1F, 1)
    Sleep(2000)
    OP_93(0x1F, 0xB4, 0x1F4)
    Sound(814, 0, 80, 0)

    def lambda_84D6():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1194, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_84D6)
    WaitChrThread(0x1F, 1)
    Sound(814, 0, 80, 0)

    def lambda_84FD():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_84FD)
    WaitChrThread(0x1F, 1)
    Sound(854, 0, 80, 0)

    def lambda_8524():
        OP_9D(0xFE, 0xFFFFAA24, 0x514, 0xFFFFB49C, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_8524)
    WaitChrThread(0x1F, 1)
    SetChrFlags(0x1F, 0x1)
    OP_93(0x1F, 0x10E, 0x1F4)
    ClearChrFlags(0x1F, 0x8000)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x4, 0x1)
    EndChrThread(0x5, 0x1)

    ChrTalk(
        0xFE,
        "Funya～...\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_85F4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85EA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x15E, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x70),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x70, 1)

    label("loc_85EA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_85F4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_8640")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8636")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x15F, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x79),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x79, 1)

    label("loc_8636")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8640")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_868C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8682")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x160, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x6A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x6A, 1)

    label("loc_8682")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_868C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_86D8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86CE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x161, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x6D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x6D, 1)

    label("loc_86CE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_86D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_8724")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_871A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x162, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x73),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x73, 1)

    label("loc_871A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8724")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_8770")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8766")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x163, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x67),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x67, 1)

    label("loc_8766")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8770")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_87BC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87B2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x164, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x8A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x8A, 1)

    label("loc_87B2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_8808")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87FE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x165, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x85),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x85, 1)

    label("loc_87FE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8808")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_8854")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_884A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x166, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x99),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x99, 1)

    label("loc_884A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8854")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_88A0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8896")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x167, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x82, 1)

    label("loc_8896")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_88EC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88E2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x168, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x92),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x92, 1)

    label("loc_88E2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_8938")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_892E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x169, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x7F, 1)

    label("loc_892E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8938")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_8984")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_897A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16A, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x76),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x76, 1)

    label("loc_897A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8984")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_89D0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89C6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16B, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x7C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x7C, 1)

    label("loc_89C6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_89D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_8A1C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A12")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16C, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x8B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x8B, 1)

    label("loc_8A12")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A1C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_8A68")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A5E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16D, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x8D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x8D, 1)

    label("loc_8A5E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_8AB4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AAA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16E, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x8E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x8E, 1)

    label("loc_8AAA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AB4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_8B00")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AF6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16F, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x83),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x83, 1)

    label("loc_8AF6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_8B4C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B42")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x170, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0xA9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0xA9, 1)

    label("loc_8B42")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_8B98")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B8E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x171, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x81),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x81, 1)

    label("loc_8B8E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B98")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_8BE4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BDA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x172, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x72, 1)

    label("loc_8BDA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BE4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_8C30")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C26")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x173, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x9A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x9A, 1)

    label("loc_8C26")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C30")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_8C7C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C72")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x174, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x95),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x95, 1)

    label("loc_8C72")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C7C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_8CC8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CBE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x175, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0xA0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0xA0, 1)

    label("loc_8CBE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8CC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_8D17")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D0D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D9, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x12D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3.\x02",
        )
    )

    AddItemNumber(0x12D, 3)

    label("loc_8D0D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D17")

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D3E")
    SetScenarioFlags(0x4B, 3)

    label("loc_8D3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D4F")
    SetScenarioFlags(0x52, 1)

    label("loc_8D4F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D60")
    SetScenarioFlags(0x52, 2)

    label("loc_8D60")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D71")
    SetScenarioFlags(0x52, 3)

    label("loc_8D71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D82")
    SetScenarioFlags(0x52, 4)

    label("loc_8D82")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D93")
    SetScenarioFlags(0x52, 5)

    label("loc_8D93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DA4")
    SetScenarioFlags(0x52, 6)

    label("loc_8DA4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 1)), scpexpr(EXPR_END)), "loc_8DC1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 2)), scpexpr(EXPR_END)), "loc_8DD4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_END)), "loc_8DE7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 4)), scpexpr(EXPR_END)), "loc_8DFA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 5)), scpexpr(EXPR_END)), "loc_8E0D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 6)), scpexpr(EXPR_END)), "loc_8E20")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E95")

    ChrTalk(
        0xFE,
        "Nyannyannya～n... ♪\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0xA6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0xA6, 1)
    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_8E95")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EDA")

    ChrTalk(
        0x102,
        "#0105FOh? You want me to have this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F8D")

    label("loc_8EDA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F1C")

    ChrTalk(
        0x103,
        "#0205FAre you giving this to me?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F8D")

    label("loc_8F1C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F8D")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F6C")

    ChrTalk(
        0x104,
        "#0305FGivin' us a gift, buddy?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F8D")

    label("loc_8F6C")


    ChrTalk(
        0x101,
        "#0005FWant me to have this?\x02",
    )

    CloseMessageWindow()

    label("loc_8F8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FBB")

    ChrTalk(
        0x101,
        "#0000FThanks, Coppe.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9004")

    label("loc_8FBB")


    ChrTalk(
        0x101,
        (
            "#0000FThanks, Coppe. But, uh, where\x01",
            "the heck did you get this from?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9004")

    TalkEnd(0xFE)
    EventEnd(0x4)
    Return()

    label("loc_900A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9049")

    label("loc_9019")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_902D")
    Jump("loc_9049")

    label("loc_902D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9049")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 34)

    label("loc_9049")

    Jump("loc_7EC8")

    label("loc_904E")

    Jump("loc_9056")

    label("loc_9053")

    Call(0, 34)

    label("loc_9056")

    TalkEnd(0x1F)
    Return()

    # Function_33_7DC8 end

    def Function_34_905A(): pass

    label("Function_34_905A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90ED")

    ChrTalk(
        0x1F,
        "Funyaya～～go...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F...Shush. Zeit is sleeping. That is not\x01",
            "any of your concern, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Funyan...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 4)
    Jump("loc_9260")

    label("loc_90ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_910E")

    ChrTalk(
        0x1F,
        "...Nyaaoo～n.\x02",
    )

    CloseMessageWindow()
    Jump("loc_919A")

    label("loc_910E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_911C")
    Jump("loc_919A")

    label("loc_911C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9138")

    ChrTalk(
        0x1F,
        "Nyaon...\x02",
    )

    CloseMessageWindow()
    Jump("loc_919A")

    label("loc_9138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_915C")

    ChrTalk(
        0x1F,
        "Fumyaya～～go...\x02",
    )

    CloseMessageWindow()
    Jump("loc_919A")

    label("loc_915C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9180")

    ChrTalk(
        0x1F,
        "Fumyaya～～go...\x02",
    )

    CloseMessageWindow()
    Jump("loc_919A")

    label("loc_9180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_919A")

    ChrTalk(
        0x1F,
        "...Nyaon...\x02",
    )

    CloseMessageWindow()

    label("loc_919A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9260")

    ChrTalk(
        0x101,
        (
            "#0004F(Coppe has been a resident of the SSS\x01",
            "building far longer than any of us...)\x02\x03",
            "#0000F(He's definitely a stubborn guy, but\x01",
            "it won't hurt to bring him food every\x01",
            "now and then.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 3)

    label("loc_9260")

    Return()

    # Function_34_905A end

    def Function_35_9261(): pass

    label("Function_35_9261")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_926F")
    SetScenarioFlags(0x1, 3)

    label("loc_926F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_927D")
    SetScenarioFlags(0x1, 3)

    label("loc_927D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_928B")
    SetScenarioFlags(0x1, 3)

    label("loc_928B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_9299")
    SetScenarioFlags(0x1, 3)

    label("loc_9299")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_92A7")
    SetScenarioFlags(0x1, 3)

    label("loc_92A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_92B5")
    SetScenarioFlags(0x1, 3)

    label("loc_92B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_92C3")
    SetScenarioFlags(0x1, 3)

    label("loc_92C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_92D1")
    SetScenarioFlags(0x1, 3)

    label("loc_92D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_92DF")
    SetScenarioFlags(0x1, 3)

    label("loc_92DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_92ED")
    SetScenarioFlags(0x1, 3)

    label("loc_92ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_92FB")
    SetScenarioFlags(0x1, 3)

    label("loc_92FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_9309")
    SetScenarioFlags(0x1, 3)

    label("loc_9309")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_9317")
    SetScenarioFlags(0x1, 3)

    label("loc_9317")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_9325")
    SetScenarioFlags(0x1, 3)

    label("loc_9325")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_9333")
    SetScenarioFlags(0x1, 3)

    label("loc_9333")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_9341")
    SetScenarioFlags(0x1, 3)

    label("loc_9341")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_934F")
    SetScenarioFlags(0x1, 3)

    label("loc_934F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_935D")
    SetScenarioFlags(0x1, 3)

    label("loc_935D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_936B")
    SetScenarioFlags(0x1, 3)

    label("loc_936B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_9379")
    SetScenarioFlags(0x1, 3)

    label("loc_9379")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_9387")
    SetScenarioFlags(0x1, 3)

    label("loc_9387")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_9395")
    SetScenarioFlags(0x1, 3)

    label("loc_9395")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_93A3")
    SetScenarioFlags(0x1, 3)

    label("loc_93A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_93B1")
    SetScenarioFlags(0x1, 3)

    label("loc_93B1")

    Return()

    # Function_35_9261 end

    def Function_36_93B2(): pass

    label("Function_36_93B2")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_947E")

    ChrTalk(
        0x160,
        (
            "#3300F(Should we conclude our investigation\x01",
            "of Central Square here?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Yeah. I think we've covered enough ground.)\x02\x03",
            "(Let's head for Station Street next.)\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 5)
    OP_29(0x46, 0x1, 0x7)
    Call(0, 7)

    label("loc_947E")

    Return()

    # Function_36_93B2 end

    def Function_37_947F(): pass

    label("Function_37_947F")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_97CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_972E")

    ChrTalk(
        0x101,
        (
            "#0003FThe Bell of Crossbell. You could\x01",
            "make the argument that it's the true\x01",
            "symbol of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FHey, Lloyd. What if...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYou read my mind, Elie. You think there's\x01",
            "a way we can check inside of it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_97CC")

    label("loc_972E")


    ChrTalk(
        0x101,
        (
            "#0001FYou could make the argument that it's\x01",
            "the true symbol of Crossbell.\x02\x03",
            "#0003FHmm... What if we tried going through\x01",
            "the Geofront to check the inside?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97CC")

    TalkEnd(0xFF)
    Return()

    # Function_37_947F end

    def Function_38_97D0(): pass

    label("Function_38_97D0")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_982B")
    EventEnd(0x5)
    NewScene("m0000", 125, 0, 0)
    IdleLoop()
    Jump("loc_982D")

    label("loc_982B")

    EventEnd(0x5)

    label("loc_982D")

    Return()

    # Function_38_97D0 end

    def Function_39_982E(): pass

    label("Function_39_982E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-12000, 1000, 13000, 0)
    MoveCamera(350, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -16000, 0, 17000, 135)
    SetChrPos(0x160, -17300, 0, 16800, 135)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")

    def lambda_98C4():
        OP_96(0xFE, 0xFFFFD120, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_98C4)
    Sleep(50)

    def lambda_98E1():
        OP_96(0xFE, 0xFFFFCC0C, 0x0, 0x3200, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_98E1)
    SetCameraDistance(17500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x101, 1)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_9938():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_9938)
    Sleep(500)
    WaitChrThread(0x160, 1)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(1085, 255, 100, 0)

    def lambda_99A0():
        OP_9A(0xFE, 0x101, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_99A0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3400352V#0005FHello?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1189, 255, 100, 0)
    Sleep(1200)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Elie's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400353V\x07\x05",
            "Lloyd, it's Elie.\x01",
            "I just finished my search of the\x01",
            "Administrative District.\x02\x03",
            "#3400354VI couldn't find Colin, but I found\x01",
            "someone who might have...\x02\x03",
            "#3400355VHe says he saw a similar-looking\x01",
            "boy following the parade from the\x01",
            "rear, unaccompanied.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400356V\x07\x00",
            "#0003FReally? That's a solid lead.\x02\x03",
            "#3400357V#0001FIf you don't mind, can I leave the\x01",
            "Harbor District's investigation to you,\x01",
            "Elie?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Elie's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400358V\x07\x05",
            "Of course. I'll keep you posted.\x02",
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
    WaitChrThread(0x160, 1)

    def lambda_9C18():
        OP_96(0xFE, 0xFFFFCC0C, 0x0, 0x3200, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_9C18)
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    WaitChrThread(0x160, 1)
    Sleep(300)

    ChrTalk(
        0x160,
        (
            "#3400359V\x07\x00",
            "#5P#3304FThe parade's rear...? He must have\x01",
            "been following that float, then.\x02",
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
    Sound(804, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x160, 500)

    ChrTalk(
        0x101,
        (
            "#3400360V#11P#0012FWait, you know something?\x02\x03",
            "#3400361V#0000FWhich float are you talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400362V#5P#3302FThe one that had that silly little\x01",
            "mascot Mishy riding on top.\x02\x03",
            "#3400363VIts design was quite amusing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400364V#11P#0008FWell, that would definitely be the kind\x01",
            "of thing to catch a kid's attention.\x02\x03",
            "#3400365V#0003F(So should I ditch questioning the\x01",
            "food stalls and go straight for kids\x01",
            "and receptionists?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -12400, 0, 13500, 135)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA2, 2)
    OP_29(0x46, 0x1, 0x6)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_39_982E end

    def Function_40_9EAE(): pass

    label("Function_40_9EAE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(4000, 1000, -20000, 0)
    MoveCamera(47, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 4600, 0, -23500, 0)
    SetChrPos(0x160, 3400, 0, -23700, 0)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")

    def lambda_9F44():
        OP_96(0xFE, 0x11F8, 0x0, 0xFFFFB9B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F44)
    Sleep(50)

    def lambda_9F61():
        OP_96(0xFE, 0xD48, 0x0, 0xFFFFB8E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_9F61)
    OP_68(4000, 1000, -18000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sound(806, 2, 100, 0)
    Sleep(500)
    WaitChrThread(0x160, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_9FC2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_9FC2)
    Sleep(500)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x3)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)

    def lambda_A020():
        OP_9A(0xFE, 0x101, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_A020)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3400407V#0001FHello?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Randy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400408V\x07\x05",
            "Yo, it's Randy. I'm checkin' out the\x01",
            "Downtown District as we speak.\x02\x03",
            "#3400409VIt sounds like our kid Colin was\x01",
            "hangin' around here, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400410V\x07\x00",
            "#0011FSeriously?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Randy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400411V\x07\x05",
            "While he was watchin' the parade,\x01",
            "the Downtown District scamps invited him\x01",
            "to play for a little bit.\x02\x03",
            "#3400412VThey said he suddenly left to go\x01",
            "back to East Street...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400413V\x07\x00",
            "#0008FThat's another confirmed sighting.\x02\x03",
            "#3400414V#0006FIt's obvious that Colin's filled with\x01",
            "curiosity... Or maybe it's bravery?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Randy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400415V\x07\x05",
            "Tell me about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(806, 2, 100, 0)
    Sleep(1200)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400416V\x07\x05",
            "It's Tio. I apologize for the\x01",
            "interruption.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400417V\x07\x00",
            "#0005FTio?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Randy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400418V\x07\x05",
            "The hell? Our Enigmas have\x01",
            "group calling?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400419V\x07\x05",
            "They do indeed.\x02\x03",
            "#3400420VI'm currently at the east exit, but Zeit\x01",
            "cannot find any trace of his scent.\x02\x03",
            "#3400421VNow, I'm passing through the Harbor District,\x01",
            "heading up toward the north exit.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400422V\x07\x00",
            "#0000FGood call, Tio.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Randy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400423V\x07\x05",
            "Should I try going 'round East Street\x01",
            "one more time, just in case?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400424V\x07\x00",
            "#0003FYeah, he probably passed through\x01",
            "there at some point.\x02\x03",
            "#3400425V#0001FAnother lap won't hurt.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Randy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400426V\x07\x05",
            "Leave it to me, bossman!\x02",
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
    WaitChrThread(0x160, 1)

    def lambda_A66F():
        OP_96(0xFE, 0xD48, 0x0, 0xFFFFB8E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_A66F)
    SetChrSubChip(0x101, 0x2)
    Sound(807, 0, 100, 0)
    WaitChrThread(0x160, 1)
    Sleep(300)

    ChrTalk(
        0x160,
        (
            "#3400427V\x07\x00",
            "#6P#3302FTeehee. Our elusive boy is quite adept at\x01",
            "playing tag, isn't he?\x02\x03",
            "#3400428V#3304FAfter all, he followed the parade from the\x01",
            "Administrative District, Entertainment\x01",
            "District, Back Alley, Central Square...\x02\x03",
            "#3400429V...East Street, and then Downtown District.\x01",
            "Then, we know he returned to East\x01",
            "Street, heading to the Harbor District.\x02\x03",
            "#3400430V#3300FThat appears to be his route, yes?\x02",
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
    Sound(804, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x160, 400)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#3400431V#0004F#11PWell, yeah. You took the words right out\x01",
            "of my mouth, Renne.\x02\x03",
            "#3400432V#0000FFor the time being, I'll leave those areas\x01",
            "to the rest of the team, since they're closer.\x02\x03",
            "#3400433VNext, I'd like to check out West Street.\x01",
            "You okay with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400434V#6P#3300FI don't see why I wouldn't be. Eliminating\x01",
            "leads is always worthwhile.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    ClearMapFlags(0x10000000)
    SetChrPos(0x0, 4000, 0, -17500, 0)
    SetScenarioFlags(0xA2, 6)
    OP_29(0x46, 0x1, 0xA)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_40_9EAE end

    def Function_41_A9F2(): pass

    label("Function_41_A9F2")

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
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x25, 1, 0, 42)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -4200, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x8000)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x25, 1)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 4)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_A9F2 end

    def Function_42_ABB4(): pass

    label("Function_42_ABB4")

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

    # Function_42_ABB4 end

    def Function_43_AC00(): pass

    label("Function_43_AC00")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(885)
    LoadEffect(0x7, "event\\ev308_00.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 12260, -4000, -5860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 2420, -4000, -4019, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -14490, -4000, -1370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x0, 400, 0, -2630, 75)
    SetChrPos(0x1, 400, 0, -2630, 75)
    SetChrPos(0x2, 400, 0, -2630, 75)
    SetChrPos(0x3, 400, 0, -2630, 75)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    Sound(885, 2, 90, 0)
    FadeToBright(2000, 0)
    OP_68(9110, 1900, -4010, 0)
    MoveCamera(351, 38, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(22500, 0)
    OP_68(-11370, 1900, -100, 10000)
    MoveCamera(335, 20, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(17000, 10000)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x375)
    SetScenarioFlags(0x5C, 0)
    NewScene("c100C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_43_AC00 end

    def Function_44_ADBE(): pass

    label("Function_44_ADBE")

    EventBegin(0x0)
    OP_4B(0x10, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(10960, 1900, 3910, 0)
    MoveCamera(140, 25, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(12830, 0)
    SetChrPos(0x101, 10600, 0, 3200, 90)
    SetChrPos(0x102, 10600, 0, 2100, 90)
    SetChrPos(0x103, 9100, 0, 3100, 90)
    SetChrPos(0x104, 9290, 0, 1920, 90)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#11P#0100FNardol's Burgers... This is one of\x01",
            "the food stalls that was robbed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0001FExcuse me, do you have a minute?\x01",
            "We're conducting an investigation\x01",
            "on the recent thefts...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#5PA-Are you those police officers the guy\x01",
            "from the Business Owners' Association\x01",
            "told me about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P*sigh* I'm sure you know, but my stall\x01",
            "was hit just this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FOur condolences.\x02\x03",
            "Please, try to recall what occurred\x01",
            "at the time of the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5PO-Oh, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PThe problem with that is that I don't\x01",
            "exactly know when I was robbed.\x02",
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
    Sleep(1200)

    ChrTalk(
        0x104,
        "#12P#0305FHow's that even possible?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PWell, it might have been when I was\x01",
            "busy chatting away with this talkative\x01",
            "young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PI think he was an eager tourist who\x01",
            "came to enjoy the festival. Anyway,\x01",
            "he was quite the loose-lipped guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PWhen I finally got him his order, I swear\x01",
            "I heard some rustling from behind me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PConfused, I quickly spun around, but\x01",
            "there was no one there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PThen, after a while, I opened up my\x01",
            "register, and lo and behold, all my\x01",
            "mira was gone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0101FSo it's possible that your mira was\x01",
            "stolen while you were busy talking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PThat's the only thing I can think of.\x01",
            "I'm as boggled as you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0003FThat definitely sounds odd...\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B633")
    OP_68(9490, 1900, 3320, 1200)
    MoveCamera(140, 32, 0, 1200)
    SetCameraDistance(14000, 1200)

    def lambda_B419():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B419)

    def lambda_B426():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B426)

    def lambda_B433():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B433)

    def lambda_B440():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B440)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#6P#0000FShould we wrap up our questioning here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0300FWe should be good. Let's head on back\x01",
            "and shuffle through all our info.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B62D")

    ChrTalk(
        0x102,
        (
            "#11P#0100FWe haven't heard from the Business Owners'\x01",
            "Association, so we can assume that no other\x01",
            "stalls have been victimized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FThat should be the case, yes.\x02\x03",
            "#0200FThough, perhaps it would be prudent\x01",
            "to conduct one more round of the food\x01",
            "stalls, just to be sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B62D")

    OP_29(0x20, 0x1, 0xD)

    label("loc_B633")

    OP_5A()
    SetChrPos(0x0, 11180, 0, 2990, 90)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_44_ADBE end

    def Function_45_B656(): pass

    label("Function_45_B656")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch20000.itc", 0x1F)
    LoadChrToIndex("chr/ch00301.itc", 0x20)
    OP_68(-6670, 1900, 14740, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(26840, 0)
    SetChrPos(0x101, -21900, -320, -910, 0)
    SetChrPos(0x102, 10980, 0, 26470, 355)
    SetChrPos(0x103, 11010, 0, 5140, 175)
    SetChrPos(0x104, -23280, -550, -950, 45)
    SetChrPos(0x20, -7420, 0, 13730, 0)
    SetChrPos(0x23, -16170, 0, 18920, 315)
    SetChrPos(0x24, -270, 800, 28250, 355)
    SetChrChipByIndex(0x20, 0x0)
    SetChrSubChip(0x20, 0x0)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0xD)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0xC)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The members of the SSS traveled to the designated\x01",
            "district to conduct their stakeout.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-6670, 1000, 14740, 2800)
    PlayBGM("ed7111", 0)
    FadeToBright(2000, 0)
    BeginChrThread(0x11, 1, 0, 46)
    Sleep(150)
    BeginChrThread(0x20, 1, 0, 46)
    OP_0D()
    OP_6F(0x1)

    AnonymousTalk(
        0x101,
        (
            "#0001F...\x02\x03",
            "Looks like he's a bust.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(500)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x20, 0x1)
    OP_64(0x11)
    OP_64(0x20)
    Sleep(200)
    BeginChrThread(0x20, 1, 0, 47)
    Sleep(1800)
    BeginChrThread(0x21, 1, 0, 48)
    Sleep(200)
    BeginChrThread(0x22, 1, 0, 49)
    Sleep(8000)
    OP_95(0x23, -11360, 0, 14110, 1500, 0x0)
    OP_95(0x23, -7480, 0, 13910, 1500, 0x0)
    OP_93(0x23, 0x0, 0x190)
    BeginChrThread(0x23, 1, 0, 46)
    Sleep(150)
    BeginChrThread(0x11, 1, 0, 46)
    Sleep(500)
    SetScenarioFlags(0x1, 4)
    BeginChrThread(0x24, 1, 0, 50)

    AnonymousTalk(
        0x101,
        (
            "#0001FThis customer's pretty young. Just\x01",
            "looks like your run-of-the-mill tourist.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#0305FHold your horses, Lloyd. We got\x01",
            "another bite...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B94B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_B95C")
    Sleep(500)
    Jump("loc_B94B")

    label("loc_B95C")

    Sleep(500)
    EndChrThread(0x24, 0x1)
    Sleep(500)
    OP_95(0x24, -3540, 0, 16830, 1500, 0x0)
    Sleep(800)
    OP_95(0x24, -4360, 0, 17140, 2200, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The youth subtly reached his hand into the food\x01",
            "stall's register.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x7D0)
    OP_68(-20140, 1000, 1410, 1200)
    Sleep(1200)

    ChrTalk(
        0x104,
        "#6P#0301FThat's our cue!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0001FGo, go, go!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7401", 0)
    BeginChrThread(0x101, 1, 0, 51)
    BeginChrThread(0x104, 1, 0, 52)

    ChrTalk(
        0x101,
        "#0007F#10APolice! Freeze!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-6320, 1900, 14400, 0)
    MoveCamera(286, 29, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(23340, 0)
    OP_0D()
    OP_4B(0x11, 0xFF)
    EndChrThread(0x11, 0xFF)
    EndChrThread(0x23, 0xFF)
    OP_64(0x11)
    OP_64(0x23)
    OP_63(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(300)

    def lambda_BACC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_BACC)

    def lambda_BAD9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_BAD9)
    Sleep(200)

    ChrTalk(
        0x23,
        "#5PTch, damn it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "#11PQuick, let's scram!\x02",
    )

    CloseMessageWindow()
    OP_68(-680, 1900, 16400, 800)
    MoveCamera(326, 38, 0, 800)
    OP_6E(480, 800)
    SetCameraDistance(20960, 800)

    def lambda_BB4A():

        label("loc_BB4A")

        TurnDirection(0xFE, 0x23, 300)
        Yield()
        Jump("loc_BB4A")

    QueueWorkItem2(0x11, 1, lambda_BB4A)
    BeginChrThread(0x23, 1, 0, 53)
    OP_95(0x24, 410, 0, 17550, 7000, 0x0)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    def lambda_BB7E():
        OP_95(0xFE, -390, 0, 17340, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_BB7E)

    def lambda_BB98():
        OP_95(0xFE, 870, 0, 19220, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_BB98)
    Sound(819, 0, 100, 0)
    OP_63(0x24, 0x0, 1900, 0x30, 0x32, 0x96, 0x0)
    Sound(24, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(
        0x24,
        "#6P#15AWhoa!\x02",
    )


    ChrTalk(
        0xC,
        "#11P#15AHuh?!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 54)
    BeginChrThread(0x104, 1, 0, 55)
    WaitChrThread(0x104, 1)
    Sleep(400)
    WaitChrThread(0x101, 1)
    OP_93(0x104, 0x5A, 0x190)

    ChrTalk(
        0x104,
        "#11P#0307FMademois-Elie, Tio Tot! You're up!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(300)
    OP_68(8360, 2200, 14220, 0)
    MoveCamera(64, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12970, 0)
    SetChrPos(0x23, 3440, 0, 16440, 90)
    BeginChrThread(0x102, 1, 0, 56)
    BeginChrThread(0x103, 1, 0, 57)
    OP_95(0x23, 8700, 0, 16500, 5000, 0x0)
    BeginChrThread(0x23, 0, 0, 58)
    Sleep(300)
    OP_63(0x23, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(
        0x102,
        "#0100F#11PYou DO know this is a dead end, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0201F#12PGame, set, match.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x23, 1, 0, 59)
    Sleep(800)

    ChrTalk(
        0x23,
        "#6PC-C-Cr...\x02",
    )

    Sleep(1000)
    OP_57(0x0)
    SetCameraDistance(13500, 1800)
    OP_82(0x64, 0xC8, 0xBB8, 0x320)

    ChrTalk(
        0x23,
        "#6P#30A#4SCRAAAAAP!\x02",
    )

    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    CloseMessageWindow()
    Sleep(400)
    SetMapObjFlags(0x4, 0x10)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 1)
    NewScene("c120C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_B656 end

    def Function_46_BDC8(): pass

    label("Function_46_BDC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BDED")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_46_BDC8")

    label("loc_BDED")

    Return()

    # Function_46_BDC8 end

    def Function_47_BDEE(): pass

    label("Function_47_BDEE")

    OP_95(0xFE, -3920, 0, 14640, 1500, 0x0)
    OP_95(0xFE, 1060, 0, 15050, 1500, 0x0)
    OP_95(0xFE, 5750, 0, 9900, 1500, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_47_BDEE end

    def Function_48_BE35(): pass

    label("Function_48_BE35")

    SetChrPos(0xFE, 4800, 0, 11810, 270)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_BE60():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BE60)
    OP_95(0xFE, -100, 0, 12810, 1500, 0x0)
    OP_95(0xFE, -5290, 0, 10890, 1500, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Sleep(2800)
    OP_95(0xFE, -9280, 0, 9400, 1500, 0x0)
    OP_95(0xFE, -17320, 0, 16450, 1500, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_48_BE35 end

    def Function_49_BED1(): pass

    label("Function_49_BED1")

    SetChrPos(0xFE, 4800, 0, 12810, 270)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_BEFC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BEFC)
    OP_95(0xFE, -100, 0, 13810, 1500, 0x0)
    OP_95(0xFE, -5290, 0, 11890, 1500, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Sleep(2800)
    OP_95(0xFE, -9280, 0, 10400, 1500, 0x0)
    OP_95(0xFE, -17320, 0, 17450, 1500, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_49_BED1 end

    def Function_50_BF6D(): pass

    label("Function_50_BF6D")

    Sleep(2500)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(100, 0, 100, 0)
    OP_79(0x4)

    def lambda_BF90():
        OP_95(0xFE, -280, 800, 23120, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BF90)
    Sleep(1000)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    Sound(100, 0, 100, 0)
    WaitChrThread(0xFE, 2)
    OP_95(0xFE, -1680, 0, 18230, 2000, 0x0)

    label("loc_BFD2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C00D")
    Sleep(800)
    OP_93(0xFE, 0x87, 0x190)
    Sleep(800)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(800)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(800)
    OP_93(0xFE, 0xE1, 0x190)
    ClearScenarioFlags(0x1, 4)
    Jump("loc_BFD2")

    label("loc_C00D")

    Return()

    # Function_50_BF6D end

    def Function_51_C00E(): pass

    label("Function_51_C00E")

    OP_95(0xFE, -19540, 0, -1160, 4000, 0x0)
    OP_95(0xFE, -13740, 0, 4530, 4000, 0x0)
    Return()

    # Function_51_C00E end

    def Function_52_C037(): pass

    label("Function_52_C037")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFAA6A, 0x0, 0x46A, 0x320, 0x9C4)
    SetChrChipByIndex(0xFE, 0xFF)
    OP_95(0xFE, -18470, 0, 4490, 4000, 0x0)
    Return()

    # Function_52_C037 end

    def Function_53_C06F(): pass

    label("Function_53_C06F")

    OP_95(0xFE, -300, 0, 15200, 7000, 0x0)
    OP_95(0xFE, 8700, 0, 16500, 7000, 0x0)
    Return()

    # Function_53_C06F end

    def Function_54_C098(): pass

    label("Function_54_C098")

    SetChrPos(0xFE, -10000, 0, 9420, 318)
    OP_95(0xFE, -1300, 0, 17110, 7000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_54_C098 end

    def Function_55_C0C5(): pass

    label("Function_55_C0C5")

    SetChrPos(0xFE, -6890, 0, 11470, 48)
    OP_95(0xFE, 690, 0, 16880, 7000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_55_C0C5 end

    def Function_56_C0F2(): pass

    label("Function_56_C0F2")

    OP_95(0xFE, 11800, 0, 19560, 5000, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_56_C0F2 end

    def Function_57_C10E(): pass

    label("Function_57_C10E")

    OP_95(0xFE, 10450, 0, 11630, 5000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_57_C10E end

    def Function_58_C12A(): pass

    label("Function_58_C12A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C141")
    OP_A0(0xFE, 3000, 0x0, 0xFB)
    Jump("Function_58_C12A")

    label("loc_C141")

    Return()

    # Function_58_C12A end

    def Function_59_C142(): pass

    label("Function_59_C142")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C170")
    OP_93(0xFE, 0x87, 0x190)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(500)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1200)
    Jump("Function_59_C142")

    label("loc_C170")

    Return()

    # Function_59_C142 end

    def Function_60_C171(): pass

    label("Function_60_C171")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("apl/ch50379.itc", 0x1F)
    LoadChrToIndex("chr/ch02708.itc", 0x20)
    OP_4B(0x11, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_68(3680, 1900, 13710, 0)
    MoveCamera(35, 35, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 8770, 0, 14220, 270)
    SetChrPos(0x102, 10300, 0, 15450, 270)
    SetChrPos(0x103, 8870, 0, 15450, 270)
    SetChrPos(0x104, 10200, 0, 14220, 270)
    SetChrPos(0x23, -3470, 200, 15260, 294)
    SetChrPos(0x24, -2120, 0, 16490, 242)
    SetChrPos(0x1E, -3570, 400, 15260, 90)
    SetChrPos(0x11, -5920, 0, 15070, 100)
    SetChrPos(0xD, 1100, 0, 19090, 242)
    SetChrPos(0xC, 2110, 0, 17600, 242)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x23, 0x2)
    SetChrFlags(0x23, 0x20)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x23, 0x1)
    ClearChrFlags(0x1E, 0x1)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)

    def lambda_C2D6():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C2D6)

    def lambda_C2EB():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C2EB)

    def lambda_C300():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C300)

    def lambda_C315():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C315)
    FadeToBright(1000, 0)
    OP_0D()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    ChrTalk(
        0x101,
        "#0011FOh, no.\x02",
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_68(-1500, 2100, 13860, 3000)
    MoveCamera(337, 42, 0, 3000)
    OP_6E(580, 3000)
    SetCameraDistance(15750, 3000)
    Sleep(3000)

    ChrTalk(
        0x24,
        "#11PS-Save meee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#12PWh-What the heck is this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#5P#1201FGRRRR...!\x02",
    )

    CloseMessageWindow()

    def lambda_C3EB():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C3EB)

    def lambda_C400():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C400)

    def lambda_C415():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C415)

    def lambda_C42A():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C42A)
    Sleep(2600)

    ChrTalk(
        0x104,
        "#12P#0305FSwoopin' in to save the day, Zeit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FDoes this indicate that these two\x01",
            "are indeed our culprits?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#5P#1203FWoof!\x02",
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
            "#6P#0000FNo way. Did he watch the crime all\x01",
            "the way from the SSS roof?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100F*sigh* I shouldn't even be surprised.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PE-Excuse me, whose doggie is this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PGee, he really gave me a shock!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0002FHaha, sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FUnderneath that rugged appearance,\x01",
            "he's a big ol' softy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106FSaved by Zeit, once again. I think we\x01",
            "owe him some treats...\x02\x03",
            "#0100FAnyway, I'm just relieved that we\x01",
            "were able to apprehend the culprits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0202FThank you, Zeit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#5P#1200FGrrrr, woof!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1E, 0x1)
    SetScenarioFlags(0x5C, 1)
    NewScene("c120C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_60_C171 end

    def Function_61_C774(): pass

    label("Function_61_C774")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(50, 4000, 4040, 0)
    MoveCamera(33, 28, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(15130, 0)
    SetChrPos(0x101, -750, -1000, 4560, 135)
    SetChrPos(0x102, -370, -1000, 5710, 180)
    SetChrPos(0x103, -1310, -1000, 5220, 135)
    SetChrPos(0x104, 170, -1000, 4860, 180)
    OP_68(50, 1100, 4040, 3000)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(886, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x104,
        "#12P#0306FOuch! I dinged my head.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FWow, it's pitch black inside of the bell.\x01",
            "I can hardly see a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FPerhaps this is the 'dark sky' the riddle was\x01",
            "referencing. That would also make the\x01",
            "Bell of Crossbell the symbol we're looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FI think I see a card inside of the bell, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FOh, I think you're right. Give me a moment\x01",
            "while I reach for it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x4)
    Sleep(300)
    OP_9D(0x101, 0x136, 0xFFFFFC18, 0xCE4, 0x190, 0x9C4)
    Sleep(700)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A card was affixed up near the top of the bell.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(200)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　For the next key, seek the oasis of\x01",
            "　pristine water, known only to the\x01",
            "　dazzling ones!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#12P#0005FThis must be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0305F...another riddle, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0103FPhantom Thief B truly is a fan of\x01",
            "unconventional methods, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FAn 'oasis of pristine water'? What\x01",
            "could that mean?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -110, -1000, 5480, 135)
    OP_CA(0x1, 0xFF, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    OP_66(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_29(0x22, 0x1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_61_C774 end

    def Function_62_CC65(): pass

    label("Function_62_CC65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC8E")
    EventBegin(0x1)
    Call(0, 72)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)

    label("loc_CC8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCB7")
    EventBegin(0x1)
    Call(0, 69)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)

    label("loc_CCB7")

    Return()

    # Function_62_CC65 end

    def Function_63_CCB8(): pass

    label("Function_63_CCB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCE1")
    EventBegin(0x1)
    Call(0, 72)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_CCE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD0A")
    EventBegin(0x1)
    Call(0, 71)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_CD0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD33")
    EventBegin(0x1)
    Call(0, 68)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_CD33")

    Return()

    # Function_63_CCB8 end

    def Function_64_CD34(): pass

    label("Function_64_CD34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD5D")
    EventBegin(0x1)
    Call(0, 72)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)

    label("loc_CD5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD86")
    EventBegin(0x1)
    Call(0, 73)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)

    label("loc_CD86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDAF")
    EventBegin(0x1)
    Call(0, 68)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)

    label("loc_CDAF")

    Return()

    # Function_64_CD34 end

    def Function_65_CDB0(): pass

    label("Function_65_CDB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDD9")
    EventBegin(0x1)
    Call(0, 72)
    Sleep(50)
    SetChrPos(0x0, -13380, 0, 14530, 135)
    EventEnd(0x4)

    label("loc_CDD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE02")
    EventBegin(0x1)
    Call(0, 68)
    Sleep(50)
    SetChrPos(0x0, -13380, 0, 14530, 135)
    EventEnd(0x4)

    label("loc_CE02")

    Return()

    # Function_65_CDB0 end

    def Function_66_CE03(): pass

    label("Function_66_CE03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE2C")
    EventBegin(0x1)
    Call(0, 70)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)

    label("loc_CE2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE55")
    EventBegin(0x1)
    Call(0, 69)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)

    label("loc_CE55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE7E")
    EventBegin(0x1)
    Call(0, 68)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)

    label("loc_CE7E")

    Return()

    # Function_66_CE03 end

    def Function_67_CE7F(): pass

    label("Function_67_CE7F")

    EventBegin(0x1)
    Call(0, 74)
    Sleep(50)
    SetChrPos(0x0, -28500, -8200, -25010, 180)
    EventEnd(0x4)
    Return()

    # Function_67_CE7F end

    def Function_68_CE9B(): pass

    label("Function_68_CE9B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF4E")

    ChrTalk(
        0x103,
        (
            "#0200FRemember, Jona may contact us.\x02\x03",
            "We should not stray too far away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FGood point. Well, once we're ready,\x01",
            "let's head on over to the Geofront!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFBF")

    label("loc_CF4E")


    ChrTalk(
        0x103,
        (
            "#0200FJona may still contact us.\x02\x03",
            "We should travel to the Geofront after\x01",
            "making the necessary preparations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFBF")

    Return()

    # Function_68_CE9B end

    def Function_69_CFC0(): pass

    label("Function_69_CFC0")


    ChrTalk(
        0x101,
        (
            "#0000FNo, we still haven't questioned\x01",
            "enough people yet...\x02\x03",
            "Let's try to scrounge up a little\x01",
            "more info before wrapping up\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_69_CFC0 end

    def Function_70_D047(): pass

    label("Function_70_D047")


    ChrTalk(
        0x101,
        (
            "#0000FLet's try asking around Station Street\x01",
            "for now.\x02\x03",
            "After all, it'd be bad news if he ended\x01",
            "up wandering outside the city.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_70_D047 end

    def Function_71_D0CB(): pass

    label("Function_71_D0CB")


    ChrTalk(
        0x101,
        (
            "#0000FRandy should be investigating\x01",
            "over that way.\x02\x03",
            "It'd be best to keep searching\x01",
            "our designated areas.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_71_D0CB end

    def Function_72_D13A(): pass

    label("Function_72_D13A")


    ChrTalk(
        0x101,
        (
            "#0000FNo time for detours...\x02\x03",
            "Let's hurry over to West Crossbell\x01",
            "Highway, ASAP!\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_72_D13A end

    def Function_73_D190(): pass

    label("Function_73_D190")


    ChrTalk(
        0x101,
        (
            "#0000FElie should be investigating\x01",
            "over that way.\x02\x03",
            "It'd be best to keep searching\x01",
            "in our designated areas.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_73_D190 end

    def Function_74_D201(): pass

    label("Function_74_D201")


    ChrTalk(
        0x101,
        (
            "#0001FI have no reason to return to the SSS\x01",
            "right now, so let's focus on finding Colin!\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_74_D201 end

    SaveToFile()

Try(main)
