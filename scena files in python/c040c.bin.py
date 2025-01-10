from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c040c.bin",                # FileName
        "c040c",                    # MapName
        "c040c",                    # Location
        0x0022,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 34, 0, 4, 0, 5],
    )

    BuildStringList((
        "c040c",                  # 0
        "Sophie",                 # 1
        "Barker Pym",             # 2
        "Portia",                 # 3
        "Tap",                    # 4
        "Ramanda",                # 5
        "Tejo",                   # 6
        "Bunny Girl",             # 7
        "Lime",                   # 8
        "Ferrick",                # 9
        "Young Man",              # 10
        "Girl",                   # 11
        "Grace",                  # 12
        "Reins",                  # 13
        "Pansy",                  # 14
        "Fay",                    # 15
        "Sammie",                 # 16
        "Sully",                  # 17
        "Tourist",                # 18
        "Tourist",                # 19
        "車",                     # 20
        "Cecile",                 # 21
        "Noel",                   # 22
        "Fran",                   # 23
        "Philia",                 # 24
        "Lan",                    # 25
        "Ada",                    # 26
        "Guest",                  # 27
        "Guest",                  # 28
        "Guest",                  # 29
        "Guest",                  # 30
        "Guest",                  # 31
        "Guest",                  # 32
        "Guest",                  # 33
        "Guest",                  # 34
        "Guest",                  # 35
        "Guest",                  # 36
        "Central Square",         # 37
        "West Street",            # 38
        "Administrative District",# 39
        "Residential District",   # 40
        "Entertainment District", # 41
        "East Street",            # 42
        "Downtown District",      # 43
        "Harbor District",        # 44
        "IBC",                    # 45
        "Station Street",         # 46
        "Back Alley",             # 47
        "Ursula Road",            # 48
        "East Crossbell Highway", # 49
        "West Crossbell Highway", # 50
        "Mainz Mountain Path",    # 51
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch36300.itc",                   # 01
        "chr/ch21900.itc",                   # 02
        "chr/ch34500.itc",                   # 03
        "chr/ch24800.itc",                   # 04
        "chr/ch25900.itc",                   # 05
        "chr/ch27100.itc",                   # 06
        "chr/ch33100.itc",                   # 07
        "chr/ch33200.itc",                   # 08
        "chr/ch22000.itc",                   # 09
        "chr/ch24500.itc",                   # 0A
        "chr/ch32300.itc",                   # 0B
        "chr/ch06000.itc",                   # 0C
        "chr/ch28100.itc",                   # 0D
        "chr/ch22300.itc",                   # 0E
        "chr/ch32700.itc",                   # 0F
        "chr/ch25600.itc",                   # 10
        "chr/ch10100.itc",                   # 11
        "chr/ch24400.itc",                   # 12
    ))

    DeclNpc(-10750,  1759,    24469,   175,  261,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4360,    0,       -10960,  310,  261,  0x0, 0,   5,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(379,     1769,    28049,   315,  261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(1830,    1769,    27899,   315,  261,  0x0, 0,   18,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-50000,  9,       12069,   220,  257,  0x0, 0,   2,   0,   0,   2,   0,   12,  255,  0)
    DeclNpc(15439,   0,       10340,   45,   261,  0x0, 0,   0,   0,   0,   3,   0,   13,  255,  0)
    DeclNpc(-22049,  0,       12489,   175,  261,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-3779,   0,       500,     180,  261,  0x0, 0,   4,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-1679,   1990,    20069,   225,  277,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-1970,   1990,    18229,   0,    277,  0x0, 0,   11,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-3460,   1990,    19659,   90,   277,  0x0, 0,   10,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-4820,   1830,    12710,   0,    389,  0x0, 0,   12,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-6369,   1759,    12850,   90,   389,  0x0, 0,   13,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(6010,    1759,    20729,   340,  389,  0x0, 0,   14,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(5510,    1759,    22149,   160,  389,  0x0, 0,   15,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(2420,    1990,    22479,   326,  389,  0x0, 0,   16,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(-10770,  1769,    22969,   0,    389,  0x0, 0,   17,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(14810,   0,       2289,    270,  261,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(15250,   0,       1220,    315,  261,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-2500,   0,       2000,    265,  197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 39,  -2.0,                  35.0,                  1.0,                   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.3999999761581421,    -17.5,                 -0.19999998807907104,  1.0])

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

    ScpFunction((
        "Function_0_828",          # 00, 0
        "Function_1_8E0",          # 01, 1
        "Function_2_90B",          # 02, 2
        "Function_3_A98",          # 03, 3
        "Function_4_B9F",          # 04, 4
        "Function_5_FE7",          # 05, 5
        "Function_6_1173",         # 06, 6
        "Function_7_22AA",         # 07, 7
        "Function_8_298E",         # 08, 8
        "Function_9_2D18",         # 09, 9
        "Function_10_2EC4",        # 0A, 10
        "Function_11_2F8E",        # 0B, 11
        "Function_12_3399",        # 0C, 12
        "Function_13_3842",        # 0D, 13
        "Function_14_3C1E",        # 0E, 14
        "Function_15_3F6B",        # 0F, 15
        "Function_16_4D2D",        # 10, 16
        "Function_17_512B",        # 11, 17
        "Function_18_540A",        # 12, 18
        "Function_19_565B",        # 13, 19
        "Function_20_57E4",        # 14, 20
        "Function_21_58FA",        # 15, 21
        "Function_22_5A50",        # 16, 22
        "Function_23_5B87",        # 17, 23
        "Function_24_5E5A",        # 18, 24
        "Function_25_60C6",        # 19, 25
        "Function_26_6684",        # 1A, 26
        "Function_27_6767",        # 1B, 27
        "Function_28_6932",        # 1C, 28
        "Function_29_6B4E",        # 1D, 29
        "Function_30_6C7A",        # 1E, 30
        "Function_31_6D62",        # 1F, 31
        "Function_32_6F6E",        # 20, 32
        "Function_33_7039",        # 21, 33
        "Function_34_70BA",        # 22, 34
        "Function_35_734A",        # 23, 35
        "Function_36_A5EE",        # 24, 36
        "Function_37_ACB2",        # 25, 37
        "Function_38_B2AC",        # 26, 38
        "Function_39_B2D2",        # 27, 39
        "Function_40_B4A3",        # 28, 40
        "Function_41_B4BF",        # 29, 41
        "Function_42_B4DB",        # 2A, 42
        "Function_43_B4F7",        # 2B, 43
        "Function_44_B704",        # 2C, 44
    ))


    def Function_0_828(): pass

    label("Function_0_828")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_868"),
        (1, "loc_874"),
        (2, "loc_880"),
        (3, "loc_88C"),
        (4, "loc_898"),
        (5, "loc_8A4"),
        (6, "loc_8B0"),
        (SWITCH_DEFAULT, "loc_8BC"),
    )


    label("loc_868")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_874")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_880")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_88C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_898")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_8A4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_8B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_8BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_8C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8DF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_8DF")

    Return()

    # Function_0_828 end

    def Function_1_8E0(): pass

    label("Function_1_8E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_90A")
    OP_94(0xFE, 0x2148, 0xFFFFEA34, 0xB36, 0xFFFFCFFE, 0x3E8)
    Sleep(300)
    Jump("Function_1_8E0")

    label("loc_90A")

    Return()

    # Function_1_8E0 end

    def Function_2_90B(): pass

    label("Function_2_90B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A97")
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
    Jump("Function_2_90B")

    label("loc_A97")

    Return()

    # Function_2_90B end

    def Function_3_A98(): pass

    label("Function_3_A98")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B9E")
    OP_95(0xFE, 8780, 0, 6460, 1000, 0x0)
    OP_95(0xFE, 2270, 0, 60, 1000, 0x0)
    OP_95(0xFE, -5460, 0, -1360, 1000, 0x0)
    OP_95(0xFE, -14070, 0, 5650, 1000, 0x0)
    OP_95(0xFE, -19800, 0, 8020, 1000, 0x0)
    OP_95(0xFE, -26870, 0, 10100, 1000, 0x0)
    Sleep(1500)
    OP_95(0xFE, -19800, 0, 8020, 1000, 0x0)
    OP_95(0xFE, -14070, 0, 5650, 1000, 0x0)
    OP_95(0xFE, -5460, 0, -1360, 1000, 0x0)
    OP_95(0xFE, 2270, 0, 60, 1000, 0x0)
    OP_95(0xFE, 8780, 0, 6460, 1000, 0x0)
    OP_95(0xFE, 11400, 0, 7650, 1000, 0x0)
    Sleep(1500)
    Jump("Function_3_A98")

    label("loc_B9E")

    Return()

    # Function_3_A98 end

    def Function_4_B9F(): pass

    label("Function_4_B9F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD1")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C73")
    SetChrPos(0x0, 21040, 0, 11840, 270)
    SetChrPos(0x1, 21040, 0, 11840, 270)
    SetChrPos(0x2, 21040, 0, 11840, 270)
    SetChrPos(0x3, 21040, 0, 11840, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C46")
    SetChrPos(0x4, 21040, 0, 11840, 270)
    SetChrPos(0x5, 21040, 0, 11840, 270)
    Jump("loc_C65")

    label("loc_C46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C65")
    SetChrPos(0x4, 21040, 0, 11840, 270)

    label("loc_C65")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DD1")

    label("loc_C73")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D30")
    SetChrPos(0x0, -39280, 0, 12420, 90)
    SetChrPos(0x1, -39280, 0, 12420, 90)
    SetChrPos(0x2, -39280, 0, 12420, 90)
    SetChrPos(0x3, -39280, 0, 12420, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D03")
    SetChrPos(0x4, -39280, 0, 12420, 90)
    SetChrPos(0x5, -39280, 0, 12420, 90)
    Jump("loc_D22")

    label("loc_D03")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D22")
    SetChrPos(0x4, -39280, 0, 12420, 90)

    label("loc_D22")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DD1")

    label("loc_D30")

    SetChrPos(0x0, 13270, 0, -19100, 315)
    SetChrPos(0x1, 13270, 0, -19100, 315)
    SetChrPos(0x2, 13270, 0, -19100, 315)
    SetChrPos(0x3, 13270, 0, -19100, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA9")
    SetChrPos(0x4, 13270, 0, -19100, 315)
    SetChrPos(0x5, 13270, 0, -19100, 315)
    Jump("loc_DC8")

    label("loc_DA9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC8")
    SetChrPos(0x4, 13270, 0, -19100, 315)

    label("loc_DC8")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DD1")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_DEE")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 34)
    Jump("loc_E11")

    label("loc_DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_E02")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 35)
    Jump("loc_E11")

    label("loc_E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_E11")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 33)

    label("loc_E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E88")
    SetChrPos(0x19, -6530, 1990, 19910, 0)
    SetChrPos(0x1A, -5730, 1990, 19110, 315)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6D")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_E6D")

    ClearChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E83")
    ClearChrFlags(0x18, 0x80)

    label("loc_E83")

    Jump("loc_FD4")

    label("loc_E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_F2B")
    SetChrPos(0x19, -10110, 1760, 13270, 135)
    SetChrPos(0x1A, -9100, 1760, 12260, 315)
    SetChrPos(0x10, 1960, 1990, 21100, 180)
    SetChrPos(0x11, 3030, 1990, 19760, 315)
    SetChrPos(0x12, 680, 1990, 19830, 45)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x15, -6890, 1990, 20250, 45)
    SetChrPos(0x16, -5800, 1990, 21340, 225)
    SetChrFlags(0x15, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F26")
    SetChrFlags(0x16, 0x10)

    label("loc_F26")

    Jump("loc_FD4")

    label("loc_F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_F6F")
    SetChrPos(0x19, -10110, 1760, 13270, 135)
    SetChrPos(0x1A, -9100, 1760, 12260, 315)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_FD4")

    label("loc_F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_FBC")
    SetChrPos(0x19, 1000, 1760, 26100, 0)
    SetChrPos(0x1A, 1280, 1870, 24860, 0)
    TurnDirection(0xA, 0x19, 0)
    TurnDirection(0xB, 0x19, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x19, 0x10)
    Jump("loc_FD4")

    label("loc_FBC")

    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_FD4")
    ClearChrFlags(0x10, 0x10)

    label("loc_FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_FE6")
    ClearScenarioFlags(0x5C, 3)
    SetScenarioFlags(0x1, 7)
    Event(0, 37)

    label("loc_FE6")

    Return()

    # Function_4_B9F end

    def Function_5_FE7(): pass

    label("Function_5_FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_FFC")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 7)

    label("loc_FFC")

    OP_78(0x6, 0x1B)
    OP_D3(0x1B, 0x0, 0x15F90, 0x0, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_102F")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_102F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1046")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_105D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_105D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1074")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1074")

    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A0")
    OP_1B(0x0, 0x0, 0x2A)
    OP_1B(0x1, 0x0, 0x28)
    OP_1B(0x2, 0x0, 0x29)

    label("loc_10A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B8")
    OP_1B(0x1, 0x0, 0x28)
    OP_1B(0x2, 0x0, 0x29)

    label("loc_10B8")

    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -2500, -3000, 26000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -2500, -4000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -25000, -4000, 10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_5_FE7 end

    def Function_6_1173(): pass

    label("Function_6_1173")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1180")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22A6")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_11D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F1")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22A1")

    label("loc_11F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1205")
    Jump("loc_22A1")

    label("loc_1205")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22A1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_13A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12C4")

    ChrTalk(
        0x8,
        (
            "Get your ice cream now, or else\x01",
            "it'll all be sold out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You don't wanna have any regrets, right?\x01",
            "Better buy some while you still can!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A3")

    label("loc_12C4")


    ChrTalk(
        0x8,
        (
            "Hahaha! I sure am raking in the\x01",
            "dough today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You there! You look like you're dying for\x01",
            "some luscious ice cream!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's okay to splurge! Five scoops? No problem!\x01",
            "I mean, why stop there?! Go for seven scoops!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_13A3")

    Jump("loc_22A1")

    label("loc_13A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_14CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1400")

    ChrTalk(
        0x8,
        (
            "Maaan, what a shame.\x01",
            "This year's parade has come\x01",
            "to an end.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C9")

    label("loc_1400")


    ChrTalk(
        0x8,
        "You know, I was thinking...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...what if I'd followed the parade on its route?\x01",
            "I'd have been super popular with the crowds!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll have you know I can move this\x01",
            "stall around pretty well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_14C9")

    Jump("loc_22A1")

    label("loc_14CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1821")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_END)), "loc_15C1")

    ChrTalk(
        0x8,
        (
            "Besides, you can't expect me to remember.\x01",
            "People disappeared after the parade just\x01",
            "as quickly as they appeared!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Honestly, my head's spinning from how\x01",
            "crazy things have been lately. My poor\x01",
            "memory is suffering.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181C")

    label("loc_15C1")


    ChrTalk(
        0x101,
        (
            "#0001F(Yeah, this person might know\x01",
            "something about Colin...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked\x01",
            "if she knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "What the heck's up with this photo?\x01",
            "You want me to keep it for myself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FNo, I already explained that I'm looking\x01",
            "for this child... Have you seen him\x01",
            "around here before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Sorry, I can't say he's ringing any bells.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Besides, you can't expect me to remember.\x01",
            "People disappeared after the parade just\x01",
            "as quickly as they appeared!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, fair enough... Well, thank you for your\x01",
            "cooperation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 32)

    label("loc_181C")

    Jump("loc_22A1")

    label("loc_1821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_194A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1879")

    ChrTalk(
        0x8,
        (
            "Maaan, what a shame. This year's parade\x01",
            "has come to an end.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1945")

    label("loc_1879")


    ChrTalk(
        0x8,
        "You know, I was thinking...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...if my stall was near the parade, I'd have\x01",
            "been super popular with the crowds!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After all, isn't slowly lugging this cart around\x01",
            "town one of my specialties?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1945")

    Jump("loc_22A1")

    label("loc_194A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1FE6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1A61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E7")

    ChrTalk(
        0xFE,
        "Ice cream! Come get your cold ice cream!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't settle for an inferior pizza! Come\x01",
            "try my ice cream instead!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A5C")

    label("loc_19E7")


    ChrTalk(
        0xFE,
        (
            "Whether you caught the thief or not,\x01",
            "it doesn't make a difference to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyway, how about some ice cream?\x02",
    )

    CloseMessageWindow()

    label("loc_1A5C")

    Jump("loc_1FE1")

    label("loc_1A61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F10")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DDD")

    ChrTalk(
        0x101,
        (
            "#0001FExcuse me, could we ask\x01",
            "you a quick question?\x02\x03",
            "We're investigating the recent string\x01",
            "of thefts around the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, yeah, I've heard that the pizzeria\x01",
            "over there was one of the victims.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Heh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someone like me would never make\x01",
            "an amateur mistake like that!\x02",
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
        0x102,
        (
            "#0106FSo, were you able to catch a\x01",
            "glimpse of the culprit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Doubt it. Wasn't exactly paying attention.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although, based on my cunning intuition,\x01",
            "I have my suspicions that they'll be\x01",
            "committing a third crime pretty soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd be willing to bet our culprit is looking\x01",
            "for his next victim right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FS-Seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F...A slight correction. Four cases of theft\x01",
            "have been reported, so the next victim\x01",
            "will be the fifth.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xA)
    Jump("loc_1F0B")

    label("loc_1DDD")


    ChrTalk(
        0xFE,
        (
            "Based on my cunning intuition, I have\x01",
            "my suspicions that they'll be committing\x01",
            "another crime pretty soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're a serial thief, after all. You think\x01",
            "they'll claim another victim before the\x01",
            "end of the day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heheh... Don't worry about me.\x01",
            "I'm not about to get robbed by\x01",
            "some petty thief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F0B")

    Jump("loc_1FE1")

    label("loc_1F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F72")

    ChrTalk(
        0x8,
        "That pizzeria is my sworn rival.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Don't ever buy their crappy pizza, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FE1")

    label("loc_1F72")


    ChrTalk(
        0x8,
        "Ice cream! Get your ice cream!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Don't settle for an inferior pizza! Come\x01",
            "try my ice cream instead!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1FE1")

    Jump("loc_22A1")

    label("loc_1FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2149")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2083")

    ChrTalk(
        0x8,
        (
            "I hold the proud achievement of having the best\x01",
            "sales among all the food stalls in this district.\x01",
            "I'm not about to give that up!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2144")

    label("loc_2083")


    ChrTalk(
        0x8,
        (
            "The owner of that pizzeria is good...\x01",
            "TOO good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Palate Pizza has become famous around\x01",
            "the city for their fast delivery service...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Heh. I'm not going to give up that easily.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2144")

    Jump("loc_22A1")

    label("loc_2149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21F7")

    ChrTalk(
        0x8,
        (
            "I heard that another ice cream shop known\x01",
            "for selling spectacular flavors has popped\x01",
            "up in the Harbor District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Bring it on, buddy! I'll take you on!\x02",
    )

    CloseMessageWindow()
    Jump("loc_22A1")

    label("loc_21F7")


    ChrTalk(
        0x8,
        "Ice cream! Get your ice cream!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hey, mister! Yeah, you! When you think about\x01",
            "the festival, you think of ice cream, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "How do you NOT buy ice cream?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_22A1")

    Jump("loc_1180")

    label("loc_22A6")

    TalkEnd(0xFE)
    Return()

    # Function_6_1173 end

    def Function_7_22AA(): pass

    label("Function_7_22AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_233E")

    ChrTalk(
        0x9,
        (
            "The festival's ending today.\x01",
            "Damn. What a shame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wouldn't mind all this horseplay\x01",
            "continuing for the rest of the year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_298A")

    label("loc_233E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_23E7")

    ChrTalk(
        0x9,
        (
            "Heh heh. Caught myself a pretty hefty\x01",
            "haul of customers today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The festival putting everyone in a good mood\x01",
            "makes people more open to my offers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_298A")

    label("loc_23E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2671")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 7)), scpexpr(EXPR_END)), "loc_24A0")

    ChrTalk(
        0x9,
        (
            "Sorry, but I ain't interested in anybody other than\x01",
            "customers who wanna live a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sure, I mighta seen him somewhere.\x01",
            "Can't remember where, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_266C")

    label("loc_24A0")


    ChrTalk(
        0x101,
        (
            "#0001F(This questionable-looking man might\x01",
            "unfortunately know something about Colin...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked\x01",
            "if he knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        "A missing kid, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No idea, pal. I only take note of\x01",
            "any potential customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Besides, you think I'm gonna remember a\x01",
            "small kid with all the commotion from the\x01",
            "parade?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FNo, I guess not...\x01",
            "Well, thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAA, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 32)

    label("loc_266C")

    Jump("loc_298A")

    label("loc_2671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_271A")

    ChrTalk(
        0x9,
        (
            "Heh heh. Caught myself a pretty hefty\x01",
            "haul of customers today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The festival putting everyone in a good mood\x01",
            "makes people more open to my offers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_298A")

    label("loc_271A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_281E")

    ChrTalk(
        0xFE,
        (
            "This place is gonna get pretty crowded as soon\x01",
            "as Arc en Ciel's show ends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can't forget about that parade, either.\x01",
            "It's gonna get pretty chaotic around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heh heh. Gotta keep my eyes peeled for\x01",
            "guys looking to have a good time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_298A")

    label("loc_281E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2895")

    ChrTalk(
        0xFE,
        (
            "Man, I'm feeling hella happy.\x01",
            "Look at all the potential customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Okay... Who to target next?\x02",
    )

    CloseMessageWindow()
    Jump("loc_298A")

    label("loc_2895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_28CF")

    ChrTalk(
        0x9,
        "Time to look for some prime customers.\x02",
    )

    CloseMessageWindow()
    Jump("loc_298A")

    label("loc_28CF")


    ChrTalk(
        0x9,
        (
            "The Anniversary Festival, eh?\x01",
            "I get pretty happy during it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even a simple barker like myself\x01",
            "can't help but get a little giddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You there, bro. You wanna have\x01",
            "some fun?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_298A")

    TalkEnd(0xFE)
    Return()

    # Function_7_22AA end

    def Function_8_298E(): pass

    label("Function_8_298E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_29E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_29E0")

    ChrTalk(
        0xA,
        (
            "Stalkers are absolute cowards.\x01",
            "Truly unforgivable!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29E3")

    label("loc_29E0")

    Call(0, 9)

    label("loc_29E3")

    Jump("loc_2D14")

    label("loc_29E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2B18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2A5C")

    ChrTalk(
        0xA,
        (
            "I envy every last person that managed to get\x01",
            "their hands on tickets for today's show...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B13")

    label("loc_2A5C")


    ChrTalk(
        0xA,
        (
            "A few of the spectators told me how\x01",
            "phenomenal the show was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "One of them mentioned that Lady Ilya's\x01",
            "aura was even more sensational than usual!\x01",
            "Gah... Damned rich people!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2B13")

    Jump("loc_2D14")

    label("loc_2B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2B9B")

    ChrTalk(
        0xA,
        "Lady Ilya, wait for meee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Heheheh... She should be changing into\x01",
            "her performance outfit right about now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D14")

    label("loc_2B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2BAC")
    Call(0, 10)
    Jump("loc_2D14")

    label("loc_2BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2C45")

    ChrTalk(
        0xA,
        (
            "This autograph by Lady Ilya is now a family\x01",
            "heirloom. It shall be passed down to my son,\x01",
            "my grandson, my great-grandson, and so on...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D14")

    label("loc_2C45")


    ChrTalk(
        0xA,
        (
            "I GOT LADY ILYA'S\x01",
            "AUTOGRAPH!!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't believe this actually happened!!\x01",
            "Sh-She was RIGHT in front of me!!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "Oh, crap... I was so excited that\x01",
            "I couldn't say a word...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2D14")

    TalkEnd(0xFE)
    Return()

    # Function_8_298E end

    def Function_9_2D18(): pass

    label("Function_9_2D18")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "Tap, did you hear the news?!\x01",
            "Some sicko was stalking\x01",
            "Lady Ilya!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2DAA")

    ChrTalk(
        0xA,
        "I heard the police already caught him, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DDC")

    label("loc_2DAA")


    ChrTalk(
        0xA,
        "They may have caught him, but you know what?\x02",
    )

    CloseMessageWindow()

    label("loc_2DDC")


    ChrTalk(
        0xA,
        (
            "His actions are reprehensible! Truly unforgivable!\x01",
            "How DARE he do that to my DEAREST LADY ILYA?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If he thinks he can get out of this unscathed,\x01",
            "he's got another thing coming...for we will\x01",
            "FINISH HIM.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_9_2D18 end

    def Function_10_2EC4(): pass

    label("Function_10_2EC4")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)

    ChrTalk(
        0xA,
        (
            "Wait, what?! You have a ticket\x01",
            "to tomorrow's show?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Grrr... This crowd needs to GO AWAY!\x01",
            "I despise all of these tourists!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You said it! Buzz off! Shoo!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x19, 0xFF)
    OP_4C(0x1A, 0xFF)
    Return()

    # Function_10_2EC4 end

    def Function_11_2F8E(): pass

    label("Function_11_2F8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2FDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2FD7")

    ChrTalk(
        0xB,
        (
            "Who's responsible...?\x01",
            "We'll make him pay!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FDA")

    label("loc_2FD7")

    Call(0, 9)

    label("loc_2FDA")

    Jump("loc_3395")

    label("loc_2FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3074")

    ChrTalk(
        0xFE,
        (
            "Damn it! I haven't seen Lady Ilya a single time\x01",
            "ever since I miraculously got her autograph!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Jealousy runs through my veins!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3395")

    label("loc_3074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_313C")

    ChrTalk(
        0xB,
        (
            "Anybody looking for the parade should\x01",
            "head thataway! Go that way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What if I end up missing my chance\x01",
            "to see Lady Ilya because of you\x01",
            "guys and your silly parade, HUH?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3214")

    label("loc_313C")


    ChrTalk(
        0xB,
        "The parade...? Not interested.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Any true fan of Arc en Ciel and Lady Ilya\x01",
            "would be ready to pounce on the opportunity\x01",
            "to purchase a ticket at any given moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Even during the peak of this festival!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3214")

    Jump("loc_3395")

    label("loc_3219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_322A")
    Call(0, 10)
    Jump("loc_3395")

    label("loc_322A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_32A4")

    ChrTalk(
        0xB,
        (
            "I-I can't believe it... I got to see Lady Ilya\x01",
            "in the flesh. I'd never seen her up close\x01",
            "and personal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3395")

    label("loc_32A4")


    ChrTalk(
        0xB,
        (
            "Arc en Ciel held an autograph session to celebrate\x01",
            "the premiere of their newest production yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As their biggest fans, you bet we hauled\x01",
            "our butts into line for autographs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...We didn't watch the performance, though.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3395")

    TalkEnd(0xFE)
    Return()

    # Function_11_2F8E end

    def Function_12_3399(): pass

    label("Function_12_3399")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3475")

    ChrTalk(
        0xC,
        (
            "Maybe I'll try boarding one of those exclusive\x01",
            "sightseeing airships today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "After all, they're only available during the festival.\x01",
            "I'm sure there'll be open seats, too, given it's the\x01",
            "last day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_383E")

    label("loc_3475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3510")

    ChrTalk(
        0xC,
        (
            "I managed to watch the parade and try various\x01",
            "food stalls during this year's festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Needless to say, it's been a good few days.\x02",
    )

    CloseMessageWindow()
    Jump("loc_383E")

    label("loc_3510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_35CB")

    ChrTalk(
        0xC,
        (
            "According to its route, the parade should pass\x01",
            "through the Entertainment District first...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha. I definitely can't miss it.\x01",
            "I must secure myself a vantage point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_383E")

    label("loc_35CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_371D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3662")

    ChrTalk(
        0xC,
        "There are far too many people here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wonder what would happen if we were\x01",
            "stricken with disaster at a time like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3718")

    label("loc_3662")


    ChrTalk(
        0xC,
        (
            "We're already three days into the festival,\x01",
            "yet more tourists continue to pour into\x01",
            "the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Phew... I'm out of breath just from making my\x01",
            "way through the main street.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3718")

    Jump("loc_383E")

    label("loc_371D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_377E")

    ChrTalk(
        0xC,
        (
            "It's much harder to get around town with\x01",
            "so many people crowding the streets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_383E")

    label("loc_377E")


    ChrTalk(
        0xC,
        (
            "Ah. I'm sorry, but could you\x01",
            "give me some space?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...With so many people around,\x01",
            "merely walking takes an effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And now I must make my way across\x01",
            "the city to attend a party.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_383E")

    TalkEnd(0xFE)
    Return()

    # Function_12_3399 end

    def Function_13_3842(): pass

    label("Function_13_3842")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_38DA")

    ChrTalk(
        0xD,
        "Three cheers for the birth of Crossbell!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "All right, once I chant that little formality,\x01",
            "it'll be time to party all day long!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C1A")

    label("loc_38DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3986")

    ChrTalk(
        0xD,
        (
            "Floats covered in pure gold...\x01",
            "Geez. That's friggin' unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I guess they weren't kiddin' about how gaudy\x01",
            "this year's parade was going to be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C1A")

    label("loc_3986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3A92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3A04")

    ChrTalk(
        0xD,
        (
            "Nice. Looks like we've got some bracers\x01",
            "patrolling the streets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Heh. I can party safely now!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A8D")

    label("loc_3A04")


    ChrTalk(
        0xD,
        (
            "Good to see the bracers workin'\x01",
            "during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Looks like they do the occasional patrol\x01",
            "through the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_3A8D")

    Jump("loc_3C1A")

    label("loc_3A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B70")

    ChrTalk(
        0xD,
        (
            "Rumor has it casinos are lettin' people\x01",
            "win more easily right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What better time to go out and have some fun?\x01",
            "It's the Anniversary Festival. Live a little!\x01",
            "This bad boy only happens once a year!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C1A")

    label("loc_3B70")


    ChrTalk(
        0xD,
        (
            "Looks like a lotta the restaurants are runnin'\x01",
            "stalls for the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Heh. I bet they're makin' a killing right now.\x01",
            "I'd better enjoy this while I still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C1A")

    TalkEnd(0xFE)
    Return()

    # Function_13_3842 end

    def Function_14_3C1E(): pass

    label("Function_14_3C1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_3CA7")

    ChrTalk(
        0xE,
        "Heeey theeere! Wanna play? ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "What better time to come in and have some fun\x01",
            "than the Anniversary Festival? ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F67")

    label("loc_3CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3EEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 6)), scpexpr(EXPR_END)), "loc_3D3D")

    ChrTalk(
        0xE,
        (
            "Heehee. I try to only pay attention to our\x01",
            "dear customers' wallets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Sorry, I don't know anything about a child... ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EEA")

    label("loc_3D3D")


    ChrTalk(
        0x101,
        (
            "#0001F(It's a shot in the dark, but this bunny girl\x01",
            "might know something about Colin...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked\x01",
            "if she knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xE,
        (
            "Hmmmm? I can't help you. I've never\x01",
            "seen this boy before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I doubt I would have noticed him if he walked\x01",
            "past me with all of these people around. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FA-Ah, got'cha... Thank you for your cooperation.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAA, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 32)

    label("loc_3EEA")

    Jump("loc_3F67")

    label("loc_3EEF")


    ChrTalk(
        0xE,
        "Heeey theeere! Wanna play? ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "What better time to come in and have some fun\x01",
            "than the Anniversary Festival? ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F67")

    TalkEnd(0xFE)
    Return()

    # Function_14_3C1E end

    def Function_15_3F6B(): pass

    label("Function_15_3F6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F95")
    Call(0, 36)
    Return()

    label("loc_3F95")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3FA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D29")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FF3")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3FF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4013")
    OP_AF(0x7F)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D24")

    label("loc_4013")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4027")
    Jump("loc_4D24")

    label("loc_4027")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D24")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41B5")

    ChrTalk(
        0xFE,
        (
            "Hey, I heard you guys managed to catch\x01",
            "those damned thieves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd better show you my appreciation, then.\x01",
            "...Here, take this with you!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1B1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1B1, 1)

    ChrTalk(
        0x101,
        (
            "#0000FThanks for the generosity.\x01",
            "We appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not a problem, our esteemed officers!\x01",
            "Eat your hearts out!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBD, 0)
    Jump("loc_4D24")

    label("loc_41B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_42B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_422B")

    ChrTalk(
        0xF,
        (
            "Today's the last day we're running this stall,\x01",
            "so come and get your pizza while it's hot!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42B0")

    label("loc_422B")


    ChrTalk(
        0xF,
        (
            "Hey there, pal. You hungry for\x01",
            "a nice, toasty pizza?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The Palate Pizza food stall is open\x01",
            "for business for one last day!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_42B0")

    Jump("loc_4D24")

    label("loc_42B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_43BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_42FF")

    ChrTalk(
        0xF,
        (
            "Crap! Just when business was\x01",
            "really thriving!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43BA")

    label("loc_42FF")


    ChrTalk(
        0xF,
        (
            "Damn it! The parade passed through here,\x01",
            "so they forced me to shut down my stall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I can't believe they made me close up shop\x01",
            "during the most profitable time of the festival!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_43BA")

    Jump("loc_4D24")

    label("loc_43BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_46F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4479")

    ChrTalk(
        0xF,
        (
            "I was forced to move my stand\x01",
            "before the parade passed by.\x01",
            "It was pretty frantic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can at least tell you he probably\x01",
            "hasn't passed by in the last hour.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F3")

    label("loc_4479")


    ChrTalk(
        0x101,
        (
            "#0001F(Hmm, this man might know some\x01",
            "details regarding Colin...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked\x01",
            "if he knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xFE,
        (
            "A missing kid?\x01",
            "Actually, I think I've seen this kid somewhere before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FSeriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I was forced to pack up my bags\x01",
            "before the parade passed by. I was\x01",
            "frantically trying to get it done...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Sorry, my memory's a little fuzzy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can at least tell you he probably\x01",
            "hasn't passed by in the last hour. The crowd's\x01",
            "been gone for that long, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThank you for your cooperation.\x01",
            "You've been a great help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 32)

    label("loc_46F3")

    Jump("loc_4D24")

    label("loc_46F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4802")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4742")

    ChrTalk(
        0xF,
        (
            "Crap! Just when business was\x01",
            "really thriving!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47FD")

    label("loc_4742")


    ChrTalk(
        0xF,
        (
            "Damn it!\x01",
            "When the parade passed through here, I\x01",
            "was forced to shut down my stall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I can't believe they made me close up shop\x01",
            "during the most profitable time of the festival!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_47FD")

    Jump("loc_4D24")

    label("loc_4802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4AD9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_48B2")

    ChrTalk(
        0xFE,
        "All right, I should be able to make back my proceeds.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The parade should be starting soon...\x01",
            "It's just one good thing after another! Hahaha!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AD4")

    label("loc_48B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49D5")

    ChrTalk(
        0xFE,
        (
            "This incredibly chatty fellow asked me for\x01",
            "a tropical pizza. I was just about to give it\x01",
            "to him, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Judging by my past experience with customers,\x01",
            "I'm willing to bet he was a tourist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Sorry, but I've come to\x01",
            "dislike that fellow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AD4")

    label("loc_49D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4A31")

    ChrTalk(
        0xF,
        (
            "Well, he's a dangerous old geezer.\x01",
            "I'd rather not get involved with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AD4")

    label("loc_4A31")


    ChrTalk(
        0xF,
        (
            "That old guy loitering around over\x01",
            "there gives me the creeps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "He's been been talking to tourists\x01",
            "non-stop for a while now. I wonder\x01",
            "what his deal is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4AD4")

    Jump("loc_4D24")

    label("loc_4AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4BBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4B0C")

    ChrTalk(
        0xF,
        "Come and try a sample!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BBA")

    label("loc_4B0C")


    ChrTalk(
        0xF,
        (
            "Don't be shy, now! Let the smell of that\x01",
            "pizza sink in while you look at them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Everyone's favorite pizzeria, Palate Pizza,\x01",
            "has opened a food stall just for you!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4BBA")

    Jump("loc_4D24")

    label("loc_4BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4C62")

    ChrTalk(
        0xF,
        (
            "It's your friendly neighborhood\x01",
            "Palate Pizza!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We've opened a food stall for your convenience,\x01",
            "exclusively during the Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D24")

    label("loc_4C62")


    ChrTalk(
        0xF,
        (
            "Welcome!\x01",
            "It's your favorite pizzeria, Palate Pizza!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "You know us, you love us! Come get a slice!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We decided to open up a food stand\x01",
            "exclusively during the Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4D24")

    Jump("loc_3FA2")

    label("loc_4D29")

    TalkEnd(0xFE)
    Return()

    # Function_15_3F6B end

    def Function_16_4D2D(): pass

    label("Function_16_4D2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4DC4")

    ChrTalk(
        0x19,
        "Oh, wow... This is delicious!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "This place's gelato is out of this world.\x01",
            "This taste is perfect for wrapping up\x01",
            "the festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5127")

    label("loc_4DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4E67")

    ChrTalk(
        0xFE,
        (
            "The parade was absolutely\x01",
            "jaw-dropping!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell City seems to really be flourishing.\x01",
            "First time I've experienced an event of this scale.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5127")

    label("loc_4E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4F48")
    OP_4B(0x1A, 0xFF)

    ChrTalk(
        0x19,
        (
            "I read in a festival guidebook that there's\x01",
            "going to be a massive parade today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Hey, are you sure you're feeling all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "I'm really looking forward to this parade!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    Jump("loc_5127")

    label("loc_4F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4FF5")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)

    ChrTalk(
        0x19,
        (
            "Excuse me...\x01",
            "Am I in the right place? I'm trying\x01",
            "to find 'Arc en Ciel.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "What time does the morning\x01",
            "show start again?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x19, 0xFF)
    OP_4C(0x1A, 0xFF)
    Jump("loc_5127")

    label("loc_4FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_5047")

    ChrTalk(
        0x19,
        (
            "Well, then, should we take our\x01",
            "time to explore the city a bit?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5127")

    label("loc_5047")


    ChrTalk(
        0x19,
        (
            "Oh, this city is exceeding all of\x01",
            "my expectations so far...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Haha. Not sure what else you'd expect from\x01",
            "Zemuria's leader of trade, Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "The long journey from Remiferia\x01",
            "was definitely worth the effort.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_5127")

    TalkEnd(0xFE)
    Return()

    # Function_16_4D2D end

    def Function_17_512B(): pass

    label("Function_17_512B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5208")

    ChrTalk(
        0x1A,
        (
            "Today's actually our\x01",
            "wedding anniversary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I'm glad we were able to spend it\x01",
            "together in such a wonderful place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I would absolutely love to come to Crossbell's\x01",
            "Anniversary Festival again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5406")

    label("loc_5208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_52A8")

    ChrTalk(
        0xFE,
        (
            "We were able to make many irreplaceable\x01",
            "memories this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew picking Crossbell as our\x01",
            "vacation spot was going to be\x01",
            "a great idea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5406")

    label("loc_52A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5323")

    ChrTalk(
        0x1A,
        "I'm actually expecting a child soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I wanted to show the baby inside\x01",
            "of my belly the parade, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5406")

    label("loc_5323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5376")

    ChrTalk(
        0x1A,
        (
            "I don't understand why Crossbell got crowded\x01",
            "all of a sudden...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5406")

    label("loc_5376")


    ChrTalk(
        0x1A,
        (
            "Our anniversary coincides with the famous\x01",
            "Crossbell Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "What a wonderful opportunity\x01",
            "to enrich our own anniversary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5406")

    TalkEnd(0xFE)
    Return()

    # Function_17_512B end

    def Function_18_540A(): pass

    label("Function_18_540A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5468")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5460")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x10,
        (
            "Ah, really?\x01",
            "That girl was really nice.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_5463")

    label("loc_5460")

    Call(0, 19)

    label("loc_5463")

    Jump("loc_5657")

    label("loc_5468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_54F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_54F0")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x10,
        (
            "But for a person like myself,\x01",
            "the parade is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Wait, are you two even listening to me?\x02",
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_54F3")

    label("loc_54F0")

    Call(0, 20)

    label("loc_54F3")

    Jump("loc_5657")

    label("loc_54F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_55A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5598")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x10,
        (
            "Well...if you insist. I suppose\x01",
            "I could tag along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "We could probably crash at my\x01",
            "cousin Susie's house tonight.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_559B")

    label("loc_5598")

    Call(0, 21)

    label("loc_559B")

    Jump("loc_5657")

    label("loc_55A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5654")

    ChrTalk(
        0x10,
        (
            "Yep, nothin' better than spending your\x01",
            "time at a festival with all your buddies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I don't have a curfew during the festival,\x01",
            "so I'm going to play all night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5657")

    label("loc_5654")

    Call(0, 22)

    label("loc_5657")

    TalkEnd(0xFE)
    Return()

    # Function_18_540A end

    def Function_19_565B(): pass

    label("Function_19_565B")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x11,
        (
            "You really saved our hides\x01",
            "with those tickets, Ferrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Where the heck did you manage to find them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "My pops managed to get them through some\x01",
            "connections at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Well, they're just B section seats.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Hey, B section seats are fine in my book!\x01",
            "Lady Ilya was so brilliant!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Of course, let's not forget Theodor.\x01",
            "I'm a big fan of his, too. ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_19_565B end

    def Function_20_57E4(): pass

    label("Function_20_57E4")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x12,
        (
            "Tickets for Arc en Ciel?\x01",
            "You should've spoken up earlier!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "My bad, I forgot to mention them.\x01",
            "Besides, they're only valid for\x01",
            "today's morning show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "They're about to start the performance, right?\x01",
            "C'mon, let's see if we can still make it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_20_57E4 end

    def Function_21_58FA(): pass

    label("Function_21_58FA")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x10,
        "Mishelam?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Kinda cliche, isn't it? And besides,\x01",
            "isn't that place for rich kids?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Oh, don't worry about it. Let's go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Your cousin's place is there, right? Why don't\x01",
            "we hang out with her while we're there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yeah, sounds like a plan...\x01",
            "Let's check out the haunted house while\x01",
            "we're there, then!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_21_58FA end

    def Function_22_5A50(): pass

    label("Function_22_5A50")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x11,
        "Where do you wanna hang out today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Wasn't that super rich guy throwing\x01",
            "a party tonight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Let's party it up there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I don't think we can... I'm pretty sure\x01",
            "it's a private party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "When you start dabbling in high society,\x01",
            "you learn to respect your superiors.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x1, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_22_5A50 end

    def Function_23_5B87(): pass

    label("Function_23_5B87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5C65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5C5D")
    OP_4B(0x10, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x11,
        (
            "I was totally stunned by that girl performing\x01",
            "as the Moon Princess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I find it hard to believe that she's a rookie!\x01",
            "I think I might have become her biggest fan...\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_5C60")

    label("loc_5C5D")

    Call(0, 19)

    label("loc_5C60")

    Jump("loc_5E56")

    label("loc_5C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5CE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5CDE")
    OP_4B(0x10, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x11,
        (
            "Pssh. Parades are for babies.\x01",
            "Arc en Ciel is for mature adults, like myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_5CE1")

    label("loc_5CDE")

    Call(0, 20)

    label("loc_5CE1")

    Jump("loc_5E56")

    label("loc_5CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5DB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5DB0")
    OP_4B(0x10, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x11,
        (
            "Haha. Ferrick, didn't you go to the\x01",
            "theme park with your family before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Tsk, tsk. That place is for kids.\x01",
            "Why not relax in the resort like refined folk?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_5DB3")

    label("loc_5DB0")

    Call(0, 21)

    label("loc_5DB3")

    Jump("loc_5E56")

    label("loc_5DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5E53")
    OP_4B(0x10, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x11,
        "Here it comes! Ferrick's high society theory!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "So, what's the plan for today?\x01",
            "Want to try our hand at Barca Casino?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_5E56")

    label("loc_5E53")

    Call(0, 22)

    label("loc_5E56")

    TalkEnd(0xFE)
    Return()

    # Function_23_5B87 end

    def Function_24_5E5A(): pass

    label("Function_24_5E5A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5EDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5ED4")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x12,
        "Oh, you traitor!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "What happened to always staying\x01",
            "loyal to Lady Ilya?!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Jump("loc_5ED7")

    label("loc_5ED4")

    Call(0, 19)

    label("loc_5ED7")

    Jump("loc_60C2")

    label("loc_5EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5F7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5F77")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x12,
        "Hey, we'd better hurry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Our seats aren't reserved, right? We need\x01",
            "to find good seats before they're gone!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Jump("loc_5F7A")

    label("loc_5F77")

    Call(0, 20)

    label("loc_5F7A")

    Jump("loc_60C2")

    label("loc_5F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6041")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_6039")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x12,
        (
            "His cousin actually owns a villa\x01",
            "at Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "She's absolutely loaded! If it's just the three\x01",
            "of us, we can stay there with no problems.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Jump("loc_603C")

    label("loc_6039")

    Call(0, 21)

    label("loc_603C")

    Jump("loc_60C2")

    label("loc_6041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_60BF")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x12,
        "I wanna go to some fancy bar or restaurant!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Doesn't that make you feel like an adult?\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Jump("loc_60C2")

    label("loc_60BF")

    Call(0, 22)

    label("loc_60C2")

    TalkEnd(0xFE)
    Return()

    # Function_24_5E5A end

    def Function_25_60C6(): pass

    label("Function_25_60C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 1)), scpexpr(EXPR_END)), "loc_62A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6190")

    ChrTalk(
        0x13,
        (
            "#2100FOh, that reminds me. When you've taken\x01",
            "enough photos for the request, just scurry\x01",
            "on over to the CNS reception desk.\x02\x03",
            "You got this in the bag! ♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 1)
    Jump("loc_62A3")

    label("loc_6190")

    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x13,
        (
            "#2109FNow, then, time to uncover what the public\x01",
            "thinks about Arc en Ciel's new creation!\x02\x03",
            "#2100FIt's about time I ambush Ilya Platiere\x01",
            "and Rixia Mao for a jaw-dropping,\x01",
            "awe-inspiring interview!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 300)

    ChrTalk(
        0x13,
        "#2100FAway we go, Reins!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Y-Yes, ma'am!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    OP_4C(0x13, 0xFF)
    OP_4C(0x14, 0xFF)

    label("loc_62A3")

    Jump("loc_6680")

    label("loc_62A8")


    ChrTalk(
        0x13,
        (
            "#2100FWell, if it isn't my best friends?\x02\x03",
            "#2109FI love you guys so much! That scoop earlier\x01",
            "was exactly what I was looking for!\x02\x03",
            "I know I can always count on the valiant SSS!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F*sigh* Somebody's in a good mood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FYou do realize that our job is not to provide\x01",
            "you with stories, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FThings did become a little complicated\x01",
            "that night.\x02\x03",
            "I'm relieved that the article was primarily\x01",
            "sympathetic towards Grandfather's\x01",
            "struggles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#2104FWeeell, I'm kind of barred from writing pieces on\x01",
            "the Imperial Faction, so it wouldn't be fair if\x01",
            "I only criticized Mayor MacDowell, right?\x02\x03",
            "#2100FAnd besides, your grandfather's popularity with\x01",
            "the citizens is off the charts! Heck, I like the\x01",
            "old guy myself.\x02\x03",
            "I might be disqualified from saying this, considering\x01",
            "I'm a reporter, but...I really try to cut the guy some\x01",
            "slack, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0102FThank you, Grace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FCan't blame a reporter for having their\x01",
            "own opinions, right? I think it's all good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB5, 1)

    label("loc_6680")

    TalkEnd(0xFE)
    Return()

    # Function_25_60C6 end

    def Function_26_6684(): pass

    label("Function_26_6684")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_66F3")

    ChrTalk(
        0xFE,
        (
            "Getting dragged around like this has made me\x01",
            "painfully aware of how out of shape I am...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6763")

    label("loc_66F3")


    ChrTalk(
        0xFE,
        (
            "*pant* *pant*\x01",
            "I'm forced to run my butt off\x01",
            "in order to keep up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Phew... I need a minute...or two.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_6763")

    TalkEnd(0xFE)
    Return()

    # Function_26_6684 end

    def Function_27_6767(): pass

    label("Function_27_6767")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_6829")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6785")
    Call(0, 29)
    Jump("loc_6824")

    label("loc_6785")


    ChrTalk(
        0xFE,
        (
            "Stupid, idiot Dad!\x01",
            "You grease monkey!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And just when I thought I could enjoy\x01",
            "this festival's lovely atmosphere!\x01",
            "I've lost my appetite thanks to you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6824")

    Jump("loc_692E")

    label("loc_6829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6856")

    ChrTalk(
        0xFE,
        "They were all so amazing!\x02",
    )

    CloseMessageWindow()
    Jump("loc_692E")

    label("loc_6856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_692E")

    ChrTalk(
        0xFE,
        (
            "Let me preface this by saying,\x01",
            "I love Lady Ilya with all of my\x01",
            "heart. Don't misunderstand!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I can't forget Plie, Selene,\x01",
            "and Rixia, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What can I say? I have a\x01",
            "thing for beautiful women.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_692E")

    TalkEnd(0xFE)
    Return()

    # Function_27_6767 end

    def Function_28_6932(): pass

    label("Function_28_6932")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_69A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6950")
    Call(0, 29)
    Jump("loc_69A3")

    label("loc_6950")


    ChrTalk(
        0xFE,
        (
            "Hahaha. I can't believe how much fun\x01",
            "I had trying out all the different food.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69A3")

    Jump("loc_6B4A")

    label("loc_69A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6A1E")

    ChrTalk(
        0xFE,
        "Wow, that was super amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep! You definitely have to bow down to\x01",
            "the famed Ilya Platiere!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B4A")

    label("loc_6A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6B4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AFB")
    OP_4B(0x15, 0xFF)
    OP_93(0xFE, 0xA0, 0x0)

    ChrTalk(
        0x15,
        (
            "Geez! If you had Arc en Ciel tickets\x01",
            "all along, then why didn't you say\x01",
            "so sooner?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha! Sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I received them from a work acquaintance,\x01",
            "but I forgot about them.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    SetScenarioFlags(0x1, 4)
    Jump("loc_6B4A")

    label("loc_6AFB")


    ChrTalk(
        0xFE,
        (
            "Hahaha...\x01",
            "Pansy's a girl, so it's no wonder\x01",
            "that she admires Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B4A")

    TalkEnd(0xFE)
    Return()

    # Function_28_6932 end

    def Function_29_6B4E(): pass

    label("Function_29_6B4E")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)
    TurnDirection(0x15, 0x16, 0)
    TurnDirection(0x16, 0x15, 0)

    ChrTalk(
        0x15,
        (
            "Oh, yeah! I wanted to\x01",
            "eat some ice cream!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "What a wonderful idea! Let's buy some and\x01",
            "observe how it's produced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I wonder what sort of manufacturing\x01",
            "equipment is used in the process... ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You big dummy, Dad!\x01",
            "Why are you so weird?!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x2D, 0x0)
    OP_93(0x16, 0xE1, 0x0)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    Return()

    # Function_29_6B4E end

    def Function_30_6C7A(): pass

    label("Function_30_6C7A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CED")

    ChrTalk(
        0xFE,
        "Yes! The fated day has finally arrived!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm coming, Lady Ilya!\x01",
            "Wait for meeeeeeeee!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_6D5E")

    label("loc_6CED")


    ChrTalk(
        0xFE,
        (
            "I only managed to buy a B section\x01",
            "ticket for today's show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it's okay! I can finally\x01",
            "see Lady Ilya!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D5E")

    TalkEnd(0xFE)
    Return()

    # Function_30_6C7A end

    def Function_31_6D62(): pass

    label("Function_31_6D62")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EAA")

    ChrTalk(
        0x101,
        "#0005FOh, hey. What are you up to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ilya asked me to pick up some\x01",
            "ice cream.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)

    ChrTalk(
        0xFE,
        (
            "The next performance is about to start. I should\x01",
            "hurry up and get back to helping them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100F(She appears to be working hard.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(She finally seems to have found\x01",
            "the path she wishes to walk.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_6F6A")

    label("loc_6EAA")


    ChrTalk(
        0xFE,
        (
            "Ilya said if I wanted to start practicing\x01",
            "on stage, I could, but...\x01",
            "...no. Not yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll stay as her assistant for a bit longer.\x01",
            "I can still train by observing Ilya\x01",
            "during practice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F6A")

    TalkEnd(0xFE)
    Return()

    # Function_31_6D62 end

    def Function_32_6F6E(): pass

    label("Function_32_6F6E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7038")
    OP_29(0x46, 0x1, 0x2)

    ChrTalk(
        0x101,
        (
            "#0001F(All right, that's a wrap on the Entertainment\x01",
            "District's investigation.)\x02\x03",
            "(Looks like the Back Alley is next...\x01",
            "Let's continue the investigation there!)\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 3)
    OP_1B(0x0, 0xFF, 0xFFFF)

    label("loc_7038")

    Return()

    # Function_32_6F6E end

    def Function_33_7039(): pass

    label("Function_33_7039")

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
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_33_7039 end

    def Function_34_70BA(): pass

    label("Function_34_70BA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(21000, 1000, 11800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 27000, 0, 11800, 270)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetCameraDistance(16500, 3000)

    def lambda_712F():
        OP_96(0xFE, 0x5208, 0x0, 0x2E18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_712F)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    OP_6F(0x10)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3400236V#0003F#11P(Let's see... So I'm responsible for investigating the\x01",
            "Entertainment District, Back Alley, Central Square,\x01",
            "Station Street, and West Street, huh?)\x02\x03",
            "#3400237V#0000F(I have no idea where this kid could be,\x01",
            "so I'll just have to search every location\x01",
            "from top to bottom.)\x02\x03",
            "#3400238V(As for buildings, I'll stick to the receptionists.\x01",
            "Otherwise this is going to take forever.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 21000, 0, 11800, 270)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetScenarioFlags(0xA1, 6)
    OP_C7(0x0, 0x1000)
    ModifyEventFlags(0, 0, 0x80)
    ClearChrFlags(0x16, 0x10)
    OP_29(0x46, 0x4, 0x2)
    OP_29(0x46, 0x1, 0x0)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x0, 0x0, 0x2A)
    OP_1B(0x1, 0x0, 0x28)
    OP_1B(0x2, 0x0, 0x29)
    EventEnd(0x5)
    Return()

    # Function_34_70BA end

    def Function_35_734A(): pass

    label("Function_35_734A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07500.itc", 0x1E)
    LoadChrToIndex("chr/ch08400.itc", 0x1F)
    LoadChrToIndex("chr/ch08500.itc", 0x20)
    LoadChrToIndex("chr/ch36300.itc", 0x21)
    LoadChrToIndex("chr/ch36400.itc", 0x22)
    LoadChrToIndex("chr/ch36500.itc", 0x23)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06300.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06400.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05900.itp")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    LoadChrToIndex("chr/ch20000.itc", 0x28)
    LoadChrToIndex("chr/ch20100.itc", 0x29)
    LoadChrToIndex("chr/ch20200.itc", 0x2A)
    LoadChrToIndex("chr/ch20300.itc", 0x2B)
    LoadChrToIndex("chr/ch20800.itc", 0x2C)
    LoadChrToIndex("chr/ch20900.itc", 0x2D)
    LoadChrToIndex("chr/ch21200.itc", 0x2E)
    LoadChrToIndex("chr/ch21300.itc", 0x2F)
    LoadChrToIndex("chr/ch21800.itc", 0x30)
    LoadChrToIndex("chr/ch21900.itc", 0x31)
    SetChrChipByIndex(0x22, 0x28)
    SetChrChipByIndex(0x23, 0x29)
    SetChrChipByIndex(0x24, 0x2A)
    SetChrChipByIndex(0x25, 0x2B)
    SetChrChipByIndex(0x26, 0x2C)
    SetChrChipByIndex(0x27, 0x2D)
    SetChrChipByIndex(0x28, 0x2E)
    SetChrChipByIndex(0x29, 0x2F)
    SetChrChipByIndex(0x2A, 0x30)
    SetChrChipByIndex(0x2B, 0x31)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x8000)
    SetChrFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x8000)
    SetChrFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x8000)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    ClearChrFlags(0x24, 0x4)
    ClearChrFlags(0x25, 0x4)
    ClearChrFlags(0x26, 0x4)
    ClearChrFlags(0x27, 0x4)
    ClearChrFlags(0x28, 0x4)
    ClearChrFlags(0x29, 0x4)
    ClearChrFlags(0x2A, 0x4)
    ClearChrFlags(0x2B, 0x4)
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
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetMapObjFlags(0x5, 0x1000)
    SetChrPos(0x22, -2880, 2660, 33730, 315)
    SetChrPos(0x23, -1480, 2660, 33130, 315)
    SetChrPos(0x24, -2520, 2660, 31990, 315)
    SetChrPos(0x25, -2560, 1760, 29650, 135)
    SetChrPos(0x26, -1660, 1760, 28950, 225)

    def lambda_75FF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_75FF)

    def lambda_7619():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_7619)

    def lambda_7633():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_7633)

    def lambda_764D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 0, lambda_764D)

    def lambda_7667():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 0, lambda_7667)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    OP_68(-7600, 1950, 500, 0)
    MoveCamera(40, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, -5200, 0, -1600, 310)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -4300, 0, -2300, 310)
    SetChrChipByIndex(0x1F, 0x23)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -10700, 0, 2600, 130)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -11800, 0, 3500, 130)
    SetChrChipByIndex(0x21, 0x22)
    SetChrSubChip(0x21, 0x0)
    SetChrPos(0x21, -12900, 0, 4400, 130)
    FadeToBright(1000, 0)
    OP_68(-1960, 4040, 33450, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(18000, 3000)
    SetChrPos(0x27, -2500, 2660, 35600, 315)
    SetChrPos(0x28, -1500, 2660, 35600, 315)
    SetChrPos(0x29, -2500, 2660, 35600, 315)
    SetChrPos(0x2A, -1500, 2660, 35600, 135)
    SetChrPos(0x2B, -1500, 2660, 35600, 225)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -2500, 2660, 35600, 0)
    SetChrPos(0x1C, -1500, 2660, 35600, 0)
    Sleep(1000)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)

    def lambda_7898():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_7898)

    def lambda_78A9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_78A9)
    Sleep(500)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)

    def lambda_78D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_78D0)

    def lambda_78E1():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 0, lambda_78E1)
    Sleep(2000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)

    def lambda_7908():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7908)

    def lambda_7919():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7919)
    Sleep(300)

    def lambda_7936():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_7936)

    def lambda_7947():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_7947)
    Sleep(2000)
    FadeToDark(3000, 0, -1)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)

    def lambda_7978():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_7978)

    def lambda_7989():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_7989)
    Sleep(500)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)

    def lambda_79B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_79B0)

    def lambda_79C1():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_79C1)
    Sleep(1500)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)

    def lambda_79E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_79E8)

    def lambda_79F9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_79F9)
    OP_0D()
    OP_68(-11650, 2120, 3280, 0)
    MoveCamera(28, 16, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(12500, 0)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x80)
    SetChrBattleFlags(0x29, 0x8000)
    SetChrFlags(0x2A, 0x80)
    SetChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x80)
    SetChrBattleFlags(0x2B, 0x8000)
    EndChrThread(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    EndChrThread(0x1C, 0xFF)
    SetChrSubChip(0x1C, 0x0)
    SetChrPos(0x101, -7400, 0, -300, 220)
    SetChrPos(0x1C, -8700, 0, 800, 220)
    OP_68(-11650, 920, 3280, 4000)
    MoveCamera(41, 24, 0, 4000)
    OP_6E(740, 4000)
    SetCameraDistance(11000, 4000)
    SetChrPos(0x101, -11320, 0, 2530, 334)
    SetChrPos(0x1C, -11770, 0, 4110, 154)
    FadeToBright(3000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3100014V#0014F#12PPhew... That was incredible!\x02\x03",
            "#3100015VI finally understand why people get\x01",
            "so fanatical over them.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x1C,
        (
            "#3100016VI'm glad you enjoyed it.\x02\x03",
            "#3100017VIlya was obviously amazing, but\x01",
            "I was really impressed by Rixia!\x02\x03",
            "#3100018VI can tell Ilya put quite some time\x01",
            "into teaching her.\x02",
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
        (
            "#3100019V#0002F#12PHaha. Yeah, I agree.\x02\x03",
            "#3100020VThey were already in sync during the private\x01",
            "performance, but this was on another level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#3100021V#5902F#5POh, that's right. Your team was responsible for solving\x01",
            "that case, right?\x02\x03",
            "#3100022VLast time I spoke with Ilya, she couldn't stop praising\x01",
            "the efforts of the SSS.\x02\x03",
            "#3100023V#5909FAt this rate, she's planning to create a play based on\x01",
            "the incident. She even mentioned something about\x01",
            "giving you a special role in it, too...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3100024V#0012F#12PR-Really...? You're just messing with me,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#3100025V#5906F#5PIs that what you think?\x02\x03",
            "#3100026VI've known her most of my life...and I\x01",
            "assure you, she's quite serious.\x02\x03",
            "#3100027V#5900FThen again, she always changes her mind at\x01",
            "the drop of a hat. I'm sure you'll live, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3100028V#0006F#12PI sure hope so...\x02\x03",
            "#3100029V#0000FMy gut's warning me that if Ilya starts to\x01",
            "get pushy, there'll be no refusing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#3100030V#5904F#5PI wouldn't worry about it too much.\x01",
            "Ilya's not the inconsiderate type.\x02\x03",
            "#3100031V#5900FNow that I think about it... Did I offend\x01",
            "your friend Randy, somehow?\x02\x03",
            "#3100032VI could have invited him to join us if\x01",
            "we had another ticket...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3100033V#0004F#12PDon't worry about him, Cecile.\x02\x03",
            "#3100034V#0000FArc en Ciel was gracious enough to\x01",
            "provide us with special tickets.\x02\x03",
            "#3100035VMore importantly, wasn't Randy going to\x01",
            "keep your coworkers from St. Ursula\x01",
            "company today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#3100036V#5902F#5PIndeed he was.\x02\x03",
            "#3100037V#5904FThose girls are always busy, so I was\x01",
            "hoping they'd take a breather.\x02\x03",
            "#3100038V#5905FBy the way, Lloyd. The SSS only\x01",
            "gets this one day off, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3100039V#0000F#12PYep. You'd be surprised by how busy\x01",
            "it gets during the Anniversary Festival.\x02\x03",
            "#3100040VGetting the opening day off was our\x01",
            "reward for solving that last case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#3100041V#5909F#5PI would say you four earned it.\x02\x03",
            "#3100042V#5902FOh, right. Why don't you join me\x01",
            "for dinner at my place tonight?\x02\x03",
            "#3100043VMom and Dad were looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3100044V#0002F#12PSure, I appreciate the invite.\x02\x03",
            "#3100045V#0005FYou know, we still have some time\x01",
            "before dinner.\x02\x03",
            "#3100046V#0012FErr... Do you want to go look around\x01",
            "the festival together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#3100047V#5905F#5POh... I'm sorry, Lloyd.\x02\x03",
            "#3100048V#5906FI was planning to meet with\x01",
            "someone after the performance.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3100049V#0011F#12PHuh?!\x02\x03",
            "#3100050VYou're meeting someone... It couldn't be.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x1C,
        (
            "#3100051V#5900F#5PHmm? What's the matter?\x02\x03",
            "#3100052VI had promised Ilya that I'd go\x01",
            "to her place afterwards...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3100053V#0B#5Z#26B#53Z#64B#92Z#105B#117Z#0012F#0E#12PO-Oh, haha...\x02\x03",
            "#3100054V#0L#0013F(Geez! What am I getting all flustered for?!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#3100055V#5909F#5PShe was planning on introducing\x01",
            "me to Rixia.\x02\x03",
            "#3100056V#5902FWhy don't you tag along, Lloyd?\x01",
            "You two have already met, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#3100057V#0000F#12PN-No, that's okay. I'll pass on that.\x02\x03",
            "#3100058VI don't see any reason for a guy like\x01",
            "me to spoil your all-girls party.\x02\x03",
            "#3100059V#0006F(And I bet it would turn into a 'Let's mess\x01",
            "with Lloyd' party, given Ilya's personality.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#3100060V#5909F#5PWell, if you insist.\x02\x03",
            "#3100061V#5902FAnyway, thanks for spending your one\x01",
            "day off with me, Lloyd.\x02\x03",
            "#3100062VI'll be home before dinner, so I expect\x01",
            "you to be there before I arrive, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3100063V#0002F#12PYeah, no problem.\x02",
    )

    CloseMessageWindow()
    OP_68(-12750, 920, 4100, 5000)

    def lambda_8A5B():

        label("loc_8A5B")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_8A5B")

    QueueWorkItem2(0x101, 0, lambda_8A5B)
    OP_92(0x1C, 0xFFFFAC04, 0x1A2C, 0x1F4)

    def lambda_8A7A():
        OP_95(0xFE, -21500, 0, 6700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_8A7A)
    Sleep(2000)
    EndChrThread(0x101, 0xFF)
    OP_93(0x101, 0x10E, 0x0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sound(1092, 255, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3100064V#0006F#11P...Well, that was awkward.\x02\x03",
            "#3100065V#0008FI wish I was as outgoing as Guy was...\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0xFF)
    WaitChrThread(0x1C, 1)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8B61")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8B7B")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8B95")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8BAF")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8BAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8BC9")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8BC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8BE3")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8BE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8BFD")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8BFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C17")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C31")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xB, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C4B")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C65")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C7F")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C99")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8CB3")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8CB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8CCD")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8CCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8CE7")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8CE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8D01")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8D1B")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8D35")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8D47")
    SetScenarioFlags(0xAA, 1)

    label("loc_8D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DC1")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Quest completion rate is high\x01",      # 0
            "Quest completion rate is low\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8DB1"),
        (1, "loc_8DB9"),
        (SWITCH_DEFAULT, "loc_8DC1"),
    )


    label("loc_8DB1")

    SetScenarioFlags(0xAA, 1)
    Jump("loc_8DC1")

    label("loc_8DB9")

    ClearScenarioFlags(0xAA, 1)
    Jump("loc_8DC1")

    label("loc_8DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_9C56")
    SetChrPos(0x1D, -2840, 0, -3110, 306)
    SetChrPos(0x1E, -3460, 0, -4040, 306)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    Sleep(300)
    Sound(2084, 255, 100, 0)
    Sleep(150)

    NpcTalk(
        0x1E,
        "Girl's Voice",
        "#3100066V#1PIs that you, Lloyd?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x1D, 500)
    Fade(1000)
    OP_68(-7250, 1530, -700, 0)
    MoveCamera(81, 28, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(14500, 0)

    def lambda_8E92():
        OP_95(0xFE, -9840, 0, 660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_8E92)
    Sleep(100)

    def lambda_8EAF():
        OP_95(0xFE, -9220, 0, 1590, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_8EAF)
    OP_68(-10020, 1000, 1460, 4500)
    MoveCamera(81, 28, 0, 4500)
    OP_6E(680, 4500)
    SetCameraDistance(12500, 10000)
    WaitChrThread(0x1E, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x1E,
        "#3100067VHi, Lloyd!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    WaitChrThread(0x1D, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x1D,
        "#3100068VIt's nice to see you again.\x02",
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
            "#3100069V#0005F#6POh, hey. What's up, you two?\x02\x03",
            "#3100070V#0000FIt took me a second to recognize you\x01",
            "without your uniforms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#3100071V#6309FAhaha... Well, we wouldn't be in uniform\x01",
            "on our day off, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#3100072V#6400F#11POn the contrary, you haven't dressed\x01",
            "down at all, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3100073V#0004F#6POh, yeah. That's because we wear\x01",
            "our casual clothes while on duty.\x02\x03",
            "#3100074V#0000FAre the Seeker sisters out on a date?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#3100075V#6409F#11POf course we are, silly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#3100076V#6306F*sigh* I'd much rather be on a date with\x01",
            "a boyfriend than my little sister...\x02\x03",
            "#3100077V#6308FWell, it's not like I even have time to find one.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1D, 500)

    ChrTalk(
        0x1E,
        (
            "#3100078V#6401F#12PNoey?!\x02\x03",
            "#3100079VAll you ever do is complain about how\x01",
            "busy you are, so the least you could\x01",
            "do is hang out with me today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#3100080V#6302FYeah, yeah. I know.\x02\x03",
            "#3100081V#6300FSo, what are you doing out here, Lloyd?\x02\x03",
            "#3100082VAre you waiting for someone?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)

    ChrTalk(
        0x101,
        (
            "#3100083V#0005F#6POh, no. I'm not...\x02\x03",
            "#3100084V#0012FI was just with a friend, but she had\x01",
            "something else she needed to tend to.\x02\x03",
            "#3100085VI'm done with all of my plans for now, so I'm\x01",
            "actually at a bit of a loss as to what to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1E, 0x1D, 500)
    TurnDirection(0x1D, 0x1E, 500)

    ChrTalk(
        0x1E,
        "#3100086V#6401F#12P(You thinking what I'm thinking, Noey?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#3100087V#6308F#5P(Yeah... Poor guy probably got stood up.)\x02\x03",
            "#3100088V#6301F(He was looking pretty down in the\x01",
            "dumps when we called out to him.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#3100089V#6406F#12P(Th-There's only one thing to do, then...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1E)
    OP_64(0x1D)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#3100090V#0000F#6PUh...ladies?\x01",
            "(I think there's been a misunderstanding...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)
    TurnDirection(0x1D, 0x101, 500)

    ChrTalk(
        0x1E,
        (
            "#3100091V#6404F#11PHey, Lloyd...\x02\x03",
            "#3100092V#6402FSince you're already free, would you\x01",
            "like to accompany two lovely ladies?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3100093V#0005F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#3100094V#6302FThere's actually a live concert down\x01",
            "in the Harbor District.\x02\x03",
            "#3100095VWe were on our way there just now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3100096V#0005F#6PA concert?\x02\x03",
            "#3100097V#0002FThat sounds pretty interesting. I know you\x01",
            "two don't get to spend much time together.\x01",
            "Are you sure I wouldn't be imposing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#3100098V#6409F#11POh, of course we are! It's especially\x01",
            "okay if it's you, Lloyd!\x02\x03",
            "#3100099VAny other guy would have to face\x01",
            "my sisterly wrath!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#3100100V#6306FC-Calm down, Fran...\x02\x03",
            "#3100101V#6302FAnyway... This is a rare opportunity for\x01",
            "us, so you're welcome to join the team!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_998A():
        OP_95(0xFE, -10900, 0, 3030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_998A)

    def lambda_99A4():
        OP_95(0xFE, -11600, 0, 1990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_99A4)
    OP_68(-11320, 1360, 2530, 3000)
    WaitChrThread(0x1D, 0)

    def lambda_99D3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_99D3)
    Sound(804, 0, 100, 0)
    WaitChrThread(0x1E, 0)

    def lambda_99EA():
        OP_93(0xFE, 0x78, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_99EA)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#3100102V#0011F#5PH-Hold on, you two.\x02\x03",
            "#3100103VTrust me, I appreciate the offer,\x01",
            "but isn't this a little...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#3100104V#6309F#5PIt's okay, Lloyd. You don't need to worry so much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#3100105V#6400F#11PYou said it, Noey. Look at you, having\x01",
            "two beauties on your arms like this!\x02\x03",
            "#3100106V#6409FOkay, guys! Let's gooooo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3100107V#0012F#5PO-Okay...\x02\x03",
            "#3100108V(Yeah, they definitely misunderstood something...\x01",
            "Oh, well. Can't do anything about it now.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9BFD():
        OP_97(0xFE, 0x1C84, 0x0, 0xFFFFEF34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9BFD)

    def lambda_9C17():
        OP_97(0xFE, 0x1C84, 0x0, 0xFFFFEF34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_9C17)

    def lambda_9C31():
        OP_97(0xFE, 0x1C84, 0x0, 0xFFFFEF34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_9C31)
    FadeToDark(3000, 0, -1)
    OP_0D()
    Jump("loc_A507")

    label("loc_9C56")

    SetChrPos(0x104, -23440, 0, 8980, 1)
    SetChrPos(0x1F, -24390, 0, 8530, 126)
    SetChrPos(0x20, -23360, 0, 9820, 126)
    SetChrPos(0x21, -24780, 0, 9950, 126)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    Sleep(300)
    Sound(1369, 255, 100, 0)
    Sleep(150)

    NpcTalk(
        0x104,
        "Randy's Voice",
        "#3100109V#2PYo, Lloyd!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)
    Fade(1000)
    OP_68(-17230, 1000, 5390, 0)
    MoveCamera(349, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(-12210, 1000, 3240, 5000)
    MoveCamera(349, 31, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(13500, 5000)

    def lambda_9D7A():

        label("loc_9D7A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_9D7A")

    QueueWorkItem2(0x104, 1, lambda_9D7A)

    def lambda_9D8C():

        label("loc_9D8C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_9D8C")

    QueueWorkItem2(0x21, 1, lambda_9D8C)

    def lambda_9D9E():

        label("loc_9D9E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_9D9E")

    QueueWorkItem2(0x1F, 1, lambda_9D9E)

    def lambda_9DB0():
        OP_96(0xFE, 0xFFFFD3F0, 0x0, 0xF28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_9DB0)
    Sleep(150)

    def lambda_9DCD():
        OP_96(0xFE, 0xFFFFCF7C, 0x0, 0x73A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_9DCD)
    Sleep(150)

    def lambda_9DEA():
        OP_96(0xFE, 0xFFFFCC2A, 0x0, 0xA78, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_9DEA)

    def lambda_9E04():
        OP_96(0xFE, 0xFFFFCDF6, 0x0, 0xF6E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9E04)
    Sleep(4000)
    WaitChrThread(0x20, 0)

    def lambda_9E25():
        TurnDirection(0x20, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_9E25)
    Sleep(800)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x1F, 0xFF)
    EndChrThread(0x21, 0xFF)

    ChrTalk(
        0x101,
        (
            "#3100110V#0005F#12POh, it's Randy and...Cecile's\x01",
            "coworkers?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1F, 0)

    ChrTalk(
        0x1F,
        "#3100111V#5POh, it's Cecile's little brother! Heeey!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x20, 0)

    ChrTalk(
        0x20,
        (
            "#3100112V#11POooh? Weren't you just with Cecile\x01",
            "not too long ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3100113V#0000F#12PYeah, but she'd promised to meet up\x01",
            "with some friends after the show.\x02\x03",
            "#3100114VWe split up a moment ago, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#3100115V#5POh, so that's why.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#3100116V#5PTeehee.\x01",
            "A darn shame, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#3100117V#0012F#12PWh-What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3100118V#0305F#5PHey, hold on just a damn second here!\x02\x03",
            "#3100119V#0301FYou aren't tellin' me... Cecile went\x01",
            "to hang out with some other dude?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3100120V#0004F#12PNo, she's just meeting up with Ilya.\x02\x03",
            "#3100121V#0000FRixia, too, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3100122V#0304F#5PPhew... Man, almost had a heart attack.\x02\x03",
            "#3100123V#0301FEither way, I'm still jealous as hell!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A19F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_A19F)

    def lambda_A1AC():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_A1AC)
    TurnDirection(0x1F, 0x104, 500)

    ChrTalk(
        0x1F,
        "#3100124V#6POh? What's this, Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#3100125VAre you implying you'd rather spend\x01",
            "your day with Cecile and Ilya Platiere\x01",
            "instead of us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3100126V#0309F#5PNaaah. No way, baby.\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x21, 0x101, 500)

    ChrTalk(
        0x21,
        "#3100127V#5PHow would you like to join us, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#3100128V#5PWe were about to head to that concert\x01",
            "over in the Harbor District.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A324():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_A324)

    def lambda_A331():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_A331)

    def lambda_A33E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A33E)

    ChrTalk(
        0x101,
        (
            "#3100129V#0002F#12PHey, that sounds a little interesting.\x02\x03",
            "#3100130V#0000FAre you okay with me joining you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3100131V#0300F#5PHell yeah! This is what I'm talkin' about!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#3100132V#5PAnd so, Cecile's little brother has\x01",
            "joined the party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#3100133V#11PTo the Harbor District!\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x78, 0x258)

    def lambda_A476():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A476)
    Sleep(50)

    def lambda_A493():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A493)
    Sleep(100)

    def lambda_A4B0():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_A4B0)
    Sleep(100)

    def lambda_A4CD():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_A4CD)

    def lambda_A4E7():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_A4E7)
    FadeToDark(3000, 0, -1)
    OP_0D()

    label("loc_A507")

    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Thus, the Anniversary Festival's opening day went by\x01",
            "in the blink of an eye.\x02\x03",
            "That night, Lloyd dined at the Neues residence.\x02\x03",
            "They told stories of Guy and reminisced the night away.\x02\x03",
            "And then...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 6)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_734A end

    def Function_36_A5EE(): pass

    label("Function_36_A5EE")

    EventBegin(0x0)
    OP_4B(0xF, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-4770, 1950, -2080, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10500, 0)
    SetChrPos(0x101, -4210, 0, -1770, 355)
    SetChrPos(0x102, -3290, 0, -3440, 355)
    SetChrPos(0x103, -4520, 0, -3350, 355)
    SetChrPos(0x104, -3020, 0, -1890, 355)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#0001FRight. Palate Pizza is one of the\x01",
            "stalls that was robbed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FExcuse me, sir. Do you have a minute to talk?\x01",
            "We're investigating the recent string of thefts.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xFE,
        "#5PThat mess, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#5PGeez, what a day it's been. I was all\x01",
            "caught up dealing with a customer\x01",
            "when I let my guard down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0305F...Wait, dealin' with a customer?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#5PYeah, some chatty fellow was asking me\x01",
            "for a tropical pizza.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#5PJudging by my past experience with customers,\x01",
            "I'm willing to bet he was a tourist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#5P*sigh* Sorry, but I've come to\x01",
            "dislike that fellow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#5PIf my ears weren't deceiving me, I coulda sworn\x01",
            "I heard sounds coming from the back of the stall...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#5PNo, I'm positive it was the sound of the\x01",
            "register being wrenched open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5PDamn it! How could this happen to me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FI'm sorry for what you're going through.\x01",
            "Thank you for cooperating in our investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC8F")
    OP_68(-4460, 1950, -3230, 1200)

    def lambda_AA72():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA72)

    def lambda_AA7F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA7F)

    def lambda_AA8C():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AA8C)

    def lambda_AA99():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AA99)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#6P#0003FShould we wrap up our questioning here?\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AC89")

    ChrTalk(
        0x102,
        (
            "#12P#0100FWe haven't heard from the Business Owners'\x01",
            "Association, so we can assume that\x01",
            "no other stalls have been victimized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FThat should be the case, yes.\x02\x03",
            "#0200F...Though, perhaps it would be prudent\x01",
            "to conduct one more round of the food\x01",
            "stalls, just to be sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC89")

    OP_29(0x20, 0x1, 0xD)

    label("loc_AC8F")

    OP_5A()
    SetChrPos(0x0, -3450, 0, -1670, 0)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_36_A5EE end

    def Function_37_ACB2(): pass

    label("Function_37_ACB2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x28)
    LoadChrToIndex("chr/ch21300.itc", 0x29)
    SoundLoad(806)
    OP_68(-10760, 3710, 22590, 0)
    MoveCamera(40, 28, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14300, 0)
    SetChrPos(0x101, -13630, 1340, 14190, 0)
    SetChrPos(0x102, -13510, 1240, 13230, 0)
    SetChrPos(0x103, -14640, 980, 14590, 45)
    SetChrPos(0x104, -14440, 930, 13700, 45)
    SetChrPos(0x22, -10770, 1770, 22760, 0)
    SetChrPos(0x23, -7540, 1770, 14200, 315)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x22, 0x0)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x29)
    SetChrSubChip(0x23, 0x0)
    BeginChrThread(0x22, 0, 0, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
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
    OP_68(-10760, 2710, 22590, 2800)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    BeginChrThread(0x8, 1, 0, 38)
    Sleep(150)
    BeginChrThread(0x22, 1, 0, 38)
    OP_0D()
    OP_6F(0x1)

    AnonymousTalk(
        0x101,
        (
            "#0001F...\x02\x03",
            "It doesn't look like this is our guy.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x22, 0x1)
    OP_64(0x8)
    OP_64(0x22)
    Sleep(200)
    OP_95(0x22, -1540, 1990, 21840, 1500, 0x0)

    def lambda_AE8F():
        OP_95(0xFE, 2270, 1990, 18430, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_AE8F)
    Sleep(1000)
    OP_95(0x23, -10750, 1760, 22660, 2000, 0x0)
    OP_93(0x23, 0x0, 0x190)
    BeginChrThread(0x8, 1, 0, 38)
    Sleep(150)
    BeginChrThread(0x23, 1, 0, 38)
    Sleep(2500)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x23, 0x1)
    OP_64(0x8)
    OP_64(0x23)
    Sleep(200)
    OP_95(0x23, -7540, 1770, 14200, 2000, 0x0)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)

    AnonymousTalk(
        0x104,
        "#0306F'Fraid you're right.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        "#0211FAnd it has already been an hour...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#0001FI don't get it. If they were coming, they should\x01",
            "have shown up by now...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(806, 2, 100, 0)
    Sleep(800)
    Fade(300)
    OP_68(-14510, 3210, 13420, 0)
    MoveCamera(40, 28, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13550, 0)
    OP_0D()
    Sleep(500)
    OP_93(0x101, 0x5A, 0x190)
    Sleep(50)

    def lambda_AFFF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AFFF)

    def lambda_B00C():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B00C)

    def lambda_B019():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B019)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#0001FYes, sir! Lloyd Bannings spea--\x02\x03",
            "#0005FThe thief appeared?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(10)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(8)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#0005FC-Central Square? Got it!\x02\x03",
            "We'll be there right away!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 400)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#0003F#11PSorry, guys. It looks like my deductions\x01",
            "were a little off target.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0101FIt's fine. Let's hurry, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001F#11PR-Right. Let's go!\x02",
    )

    CloseMessageWindow()

    def lambda_B205():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B205)

    def lambda_B212():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B212)

    def lambda_B21F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B21F)

    def lambda_B22C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B22C)
    Sleep(300)
    WaitChrThread(0x102, 1)

    def lambda_B240():
        OP_9B(0x0, 0xFE, 0x14, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B240)

    def lambda_B255():
        OP_9B(0x0, 0xFE, 0x14, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B255)

    def lambda_B26A():
        OP_9B(0x0, 0xFE, 0x14, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B26A)

    def lambda_B27F():
        OP_9B(0x0, 0xFE, 0x14, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B27F)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x28)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 5)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_ACB2 end

    def Function_38_B2AC(): pass

    label("Function_38_B2AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B2D1")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_38_B2AC")

    label("loc_B2D1")

    Return()

    # Function_38_B2AC end

    def Function_39_B2D2(): pass

    label("Function_39_B2D2")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B340")
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

    label("loc_B340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3AC")
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

    label("loc_B3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B420")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Many audience members from the performance\x01",
            "still remain. Let's refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B48C")
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

    label("loc_B48C")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Return()

    # Function_39_B2D2 end

    def Function_40_B4A3(): pass

    label("Function_40_B4A3")

    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 20770, 0, 12930, 270)
    EventEnd(0x4)
    Return()

    # Function_40_B4A3 end

    def Function_41_B4BF(): pass

    label("Function_41_B4BF")

    EventBegin(0x1)
    Call(0, 44)
    Sleep(50)
    SetChrPos(0x0, -39280, 0, 12420, 90)
    EventEnd(0x4)
    Return()

    # Function_41_B4BF end

    def Function_42_B4DB(): pass

    label("Function_42_B4DB")

    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 13270, 0, -19100, 315)
    EventEnd(0x4)
    Return()

    # Function_42_B4DB end

    def Function_43_B4F7(): pass

    label("Function_43_B4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B669")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5E9")

    ChrTalk(
        0x101,
        (
            "#0001FI need to gather more witness\x01",
            "testimonies about Colin.\x02\x03",
            "#0003FI should start with the food stall vendors and\x01",
            "receptionists... Other than that, I should look\x01",
            "for whoever else that might catch my eye.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_B669")

    label("loc_B5E9")


    ChrTalk(
        0x101,
        (
            "#0001FI need to gather more witness\x01",
            "testimonies about Colin.\x02\x03",
            "I'll try questioning people who may\x01",
            "know Colin in this area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B703")

    ChrTalk(
        0x101,
        (
            "#0001FElie should've investigated\x01",
            "this area already...\x02\x03",
            "I should stick to the plan and focus my\x01",
            "investigation on the designated areas.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B703")

    Return()

    # Function_43_B4F7 end

    def Function_44_B704(): pass

    label("Function_44_B704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B876")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7F6")

    ChrTalk(
        0x101,
        (
            "#0001FI need to gather more witness\x01",
            "testimonies about Colin.\x02\x03",
            "#0003FI should start with the food stall vendors and\x01",
            "receptionists... Other than that, I should look\x01",
            "for whoever else that might catch my eye.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_B876")

    label("loc_B7F6")


    ChrTalk(
        0x101,
        (
            "#0001FI need to gather more witness\x01",
            "testimonies about Colin.\x02\x03",
            "I'll try questioning people who may\x01",
            "know Colin in this area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B9FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B967")

    ChrTalk(
        0x101,
        (
            "#0001FMr. Hayworth should have the Residential District\x01",
            "covered...\x02\x03",
            "If he manages to spot him, he'll contact me immediately.\x02\x03",
            "I'll stick to the plan for now, and continue to search for\x01",
            "clues in the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_B9FE")

    label("loc_B967")


    ChrTalk(
        0x101,
        (
            "#0001FMr. Hayworth should have the Residential District\x01",
            "covered...\x02\x03",
            "I'll stick to the plan for now, and continue to search for\x01",
            "clues in the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9FE")

    Return()

    # Function_44_B704 end

    SaveToFile()

Try(main)
