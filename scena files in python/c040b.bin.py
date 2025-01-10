from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c040b.bin",                # FileName
        "c040b",                    # MapName
        "c040b",                    # Location
        0x0022,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 34, 0, 4, 0, 5],
    )

    BuildStringList((
        "c040b",                  # 0
        "Sophie",                 # 1
        "Barker Pym",             # 2
        "Portia",                 # 3
        "Tap",                    # 4
        "Ramanda",                # 5
        "Tejo",                   # 6
        "Bunny Girl",             # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Tourist",                # 10
        "Mayor MacDowell",        # 11
        "Secretary Ernest",       # 12
        "Zeit",                   # 13
        "Detective Dudley",       # 14
        "Chief Sergei",           # 15
        "Ilya",                   # 16
        "Rixia",                  # 17
        "CGF Guardsman",          # 18
        "CGF Guardsman",          # 19
        "CGF Guardsman",          # 20
        "CGF Guardsman",          # 21
        "車１",                   # 22
        "車２",                   # 23
        "Guest",                  # 24
        "Guest",                  # 25
        "Guest",                  # 26
        "Guest",                  # 27
        "Guest",                  # 28
        "Guest",                  # 29
        "Guest",                  # 30
        "Guest",                  # 31
        "Guest",                  # 32
        "Guest",                  # 33
        "SE制御",                 # 34
        "Central Square",         # 35
        "West Street",            # 36
        "Administrative District",# 37
        "Residential District",   # 38
        "Entertainment District", # 39
        "East Street",            # 40
        "Downtown District",      # 41
        "Harbor District",        # 42
        "IBC",                    # 43
        "Station Street",         # 44
        "Back Alley",             # 45
        "Ursula Road",            # 46
        "East Crossbell Highway", # 47
        "West Crossbell Highway", # 48
        "Mainz Mountain Path",    # 49
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch36300.itc",                   # 01
        "chr/ch21900.itc",                   # 02
        "chr/ch34500.itc",                   # 03
        "chr/ch25900.itc",                   # 04
        "chr/ch27100.itc",                   # 05
        "chr/ch32200.itc",                   # 06
        "chr/ch32300.itc",                   # 07
        "chr/ch24400.itc",                   # 08
        "chr/ch33100.itc",                   # 09
    ))

    DeclNpc(-10750,  1759,    24469,   175,  261,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(230,     0,       -1830,   175,  277,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(379,     1769,    28049,   315,  261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(1830,    1769,    27899,   315,  261,  0x0, 0,   8,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-50000,  9,       12069,   220,  257,  0x0, 0,   2,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(15439,   0,       10340,   45,   261,  0x0, 0,   0,   0,   0,   2,   0,   12,  255,  0)
    DeclNpc(-22049,  0,       12489,   175,  261,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(300,     0,       -3799,   355,  277,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(1149,    0,       -4409,   310,  277,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(14829,   0,       2670,    90,   261,  0x0, 0,   9,   0,   0,   0,   0,   16,  255,  0)
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 58,  -2.0,                  35.0,                  1.0,                   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.3999999761581421,    -17.5,                 -0.19999998807907104,  1.0])

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
        "Function_0_814",          # 00, 0
        "Function_1_8CC",          # 01, 1
        "Function_2_A59",          # 02, 2
        "Function_3_B60",          # 03, 3
        "Function_4_B7C",          # 04, 4
        "Function_5_DF8",          # 05, 5
        "Function_6_E89",          # 06, 6
        "Function_7_FF8",          # 07, 7
        "Function_8_10D8",         # 08, 8
        "Function_9_11B1",         # 09, 9
        "Function_10_120E",        # 0A, 10
        "Function_11_12BE",        # 0B, 11
        "Function_12_12F6",        # 0C, 12
        "Function_13_136E",        # 0D, 13
        "Function_14_13CF",        # 0E, 14
        "Function_15_141E",        # 0F, 15
        "Function_16_14A3",        # 10, 16
        "Function_17_1531",        # 11, 17
        "Function_18_1586",        # 12, 18
        "Function_19_15DB",        # 13, 19
        "Function_20_1644",        # 14, 20
        "Function_21_16AD",        # 15, 21
        "Function_22_1716",        # 16, 22
        "Function_23_177F",        # 17, 23
        "Function_24_17E8",        # 18, 24
        "Function_25_1851",        # 19, 25
        "Function_26_18BA",        # 1A, 26
        "Function_27_1923",        # 1B, 27
        "Function_28_1980",        # 1C, 28
        "Function_29_19BD",        # 1D, 29
        "Function_30_19F5",        # 1E, 30
        "Function_31_1A1B",        # 1F, 31
        "Function_32_1A41",        # 20, 32
        "Function_33_1A67",        # 21, 33
        "Function_34_1A8D",        # 22, 34
        "Function_35_1AC7",        # 23, 35
        "Function_36_1B01",        # 24, 36
        "Function_37_200B",        # 25, 37
        "Function_38_204A",        # 26, 38
        "Function_39_207F",        # 27, 39
        "Function_40_212A",        # 28, 40
        "Function_41_2164",        # 29, 41
        "Function_42_21B0",        # 2A, 42
        "Function_43_2A43",        # 2B, 43
        "Function_44_2E5B",        # 2C, 44
        "Function_45_4198",        # 2D, 45
        "Function_46_4201",        # 2E, 46
        "Function_47_4300",        # 2F, 47
        "Function_48_438F",        # 30, 48
        "Function_49_43D9",        # 31, 49
        "Function_50_4426",        # 32, 50
        "Function_51_448D",        # 33, 51
        "Function_52_44E6",        # 34, 52
        "Function_53_4636",        # 35, 53
        "Function_54_4683",        # 36, 54
        "Function_55_46D8",        # 37, 55
        "Function_56_472E",        # 38, 56
        "Function_57_4791",        # 39, 57
        "Function_58_47AB",        # 3A, 58
        "Function_59_48E7",        # 3B, 59
        "Function_60_4903",        # 3C, 60
        "Function_61_491F",        # 3D, 61
        "Function_62_493B",        # 3E, 62
    ))


    def Function_0_814(): pass

    label("Function_0_814")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_854"),
        (1, "loc_860"),
        (2, "loc_86C"),
        (3, "loc_878"),
        (4, "loc_884"),
        (5, "loc_890"),
        (6, "loc_89C"),
        (SWITCH_DEFAULT, "loc_8A8"),
    )


    label("loc_854")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_860")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_86C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_878")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_884")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_890")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_89C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_8A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_8B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_8CB")

    Return()

    # Function_0_814 end

    def Function_1_8CC(): pass

    label("Function_1_8CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A58")
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
    Jump("Function_1_8CC")

    label("loc_A58")

    Return()

    # Function_1_8CC end

    def Function_2_A59(): pass

    label("Function_2_A59")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B5F")
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
    Jump("Function_2_A59")

    label("loc_B5F")

    Return()

    # Function_2_A59 end

    def Function_3_B60(): pass

    label("Function_3_B60")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B7B")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_3_B60")

    label("loc_B7B")

    Return()

    # Function_3_B60 end

    def Function_4_B7C(): pass

    label("Function_4_B7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D93")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C47")
    SetChrPos(0x0, 21040, 0, 11840, 270)
    SetChrPos(0x1, 21040, 0, 11840, 270)
    SetChrPos(0x2, 21040, 0, 11840, 270)
    SetChrPos(0x3, 21040, 0, 11840, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C23")
    SetChrPos(0x4, 21040, 0, 11840, 270)
    SetChrPos(0x5, 21040, 0, 11840, 270)
    Jump("loc_C42")

    label("loc_C23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C42")
    SetChrPos(0x4, 21040, 0, 11840, 270)

    label("loc_C42")

    Jump("loc_D93")

    label("loc_C47")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CFB")
    SetChrPos(0x0, -39280, 0, 12420, 90)
    SetChrPos(0x1, -39280, 0, 12420, 90)
    SetChrPos(0x2, -39280, 0, 12420, 90)
    SetChrPos(0x3, -39280, 0, 12420, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD7")
    SetChrPos(0x4, -39280, 0, 12420, 90)
    SetChrPos(0x5, -39280, 0, 12420, 90)
    Jump("loc_CF6")

    label("loc_CD7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF6")
    SetChrPos(0x4, -39280, 0, 12420, 90)

    label("loc_CF6")

    Jump("loc_D93")

    label("loc_CFB")

    SetChrPos(0x0, 13270, 0, -19100, 315)
    SetChrPos(0x1, 13270, 0, -19100, 315)
    SetChrPos(0x2, 13270, 0, -19100, 315)
    SetChrPos(0x3, 13270, 0, -19100, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D74")
    SetChrPos(0x4, 13270, 0, -19100, 315)
    SetChrPos(0x5, 13270, 0, -19100, 315)
    Jump("loc_D93")

    label("loc_D74")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D93")
    SetChrPos(0x4, 13270, 0, -19100, 315)

    label("loc_D93")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAD")
    Event(0, 43)

    label("loc_DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_DC1")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 36)
    Jump("loc_DE4")

    label("loc_DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_DD5")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 42)
    Jump("loc_DE4")

    label("loc_DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_DE4")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 44)

    label("loc_DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DF7")
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xF, 0x10)

    label("loc_DF7")

    Return()

    # Function_4_B7C end

    def Function_5_DF8(): pass

    label("Function_5_DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_E1E")
    SetMapObjFrame(0xFF, "ka01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ka02", 0x1, 0x1)
    Jump("loc_E36")

    label("loc_E1E")

    SetMapObjFrame(0xFF, "ka01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ka02", 0x0, 0x1)

    label("loc_E36")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E4E")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E4E")

    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E70")
    OP_1B(0x1, 0x0, 0x3B)
    OP_1B(0x2, 0x0, 0x3C)

    label("loc_E70")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E88")
    OP_1B(0x0, 0x0, 0x3D)

    label("loc_E88")

    Return()

    # Function_5_DF8 end

    def Function_6_E89(): pass

    label("Function_6_E89")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF4")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_EE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F07")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FEF")

    label("loc_F07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F1B")
    Jump("loc_FEF")

    label("loc_F1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FEF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F7A")

    ChrTalk(
        0x8,
        (
            "Being a merchant is tough work...\x01",
            "Is this my fate?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FEF")

    label("loc_F7A")


    ChrTalk(
        0x8,
        "Crossbell is dazzling during nighttime.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd go out and enjoy myself if I didn't\x01",
            "have a business to run.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_FEF")

    Jump("loc_E96")

    label("loc_FF4")

    TalkEnd(0xFE)
    Return()

    # Function_6_E89 end

    def Function_7_FF8(): pass

    label("Function_7_FF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10D1")

    ChrTalk(
        0xFE,
        (
            "Out on the town for a night of fun?\x01",
            "Why not come in for some fantastic wine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heh. You're in a group of four, so you've\x01",
            "scored yourself a party discount.\x01",
            "Give it some thought, why don't you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D4")

    label("loc_10D1")

    Call(0, 8)

    label("loc_10D4")

    TalkEnd(0xFE)
    Return()

    # Function_7_FF8 end

    def Function_8_10D8(): pass

    label("Function_8_10D8")

    OP_4B(0x9, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        "Are you sure it's all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'm definitely interested, but I'm\x01",
            "a little nervous about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Bwahahaha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Come on, now. Do we look like\x01",
            "a bunch of crooked folks to you?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x9, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_8_10D8 end

    def Function_9_11B1(): pass

    label("Function_9_11B1")

    TalkBegin(0xFE)

    ChrTalk(
        0xA,
        (
            "It's almost time for the performance!\x01",
            "My heart feels like it's going to explode!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_11B1 end

    def Function_10_120E(): pass

    label("Function_10_120E")

    TalkBegin(0xFE)

    ChrTalk(
        0xB,
        (
            "The Entertainment District has a\x01",
            "crazy nightlife...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Damn, if only I had managed to snag me\x01",
            "some tickets. I'd be enjoying the new\x01",
            "Arc en Ciel show in a minute.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_120E end

    def Function_11_12BE(): pass

    label("Function_11_12BE")

    TalkBegin(0xFE)

    ChrTalk(
        0xC,
        "Where's the party going to take me tonight?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_12BE end

    def Function_12_12F6(): pass

    label("Function_12_12F6")

    TalkBegin(0xFE)

    ChrTalk(
        0xD,
        "Okay, it's time to play all night!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "First things first, it's time to hit up\x01",
            "the casino and try my luck!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_12F6 end

    def Function_13_136E(): pass

    label("Function_13_136E")

    TalkBegin(0xFE)

    ChrTalk(
        0xE,
        "Heeey theeere! Wanna play? ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Come on down to the Barca Casino\x01",
            "for a good time!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_136E end

    def Function_14_13CF(): pass

    label("Function_14_13CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1417")

    ChrTalk(
        0xF,
        (
            "A-Ahem!\x01",
            "Keep this a secret from my wife,\x01",
            "will ya?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141A")

    label("loc_1417")

    Call(0, 8)

    label("loc_141A")

    TalkEnd(0xFE)
    Return()

    # Function_14_13CF end

    def Function_15_141E(): pass

    label("Function_15_141E")

    TalkBegin(0xFE)
    OP_4B(0x9, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x10,
        "Oh, are you actually going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hehe. I'd be lying if I said I wasn't\x01",
            "at least a little bit interested.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xF, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_15_141E end

    def Function_16_14A3(): pass

    label("Function_16_14A3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "My daughter and wife still haven't\x01",
            "returned from shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* This sucks.\x01",
            "I think I'll head back to the hotel for now...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_14A3 end

    def Function_17_1531(): pass

    label("Function_17_1531")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -2550, 1860, 25760, 0)
    OP_95(0xFE, -2550, 2660, 35120, 1000, 0x0)

    def lambda_1565():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1565)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_17_1531 end

    def Function_18_1586(): pass

    label("Function_18_1586")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -1280, 1990, 24700, 0)
    OP_95(0xFE, -1390, 2660, 35120, 1000, 0x0)

    def lambda_15BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15BA)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_18_1586 end

    def Function_19_15DB(): pass

    label("Function_19_15DB")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, 4520, 1890, 19530, 333)
    OP_95(0xFE, -1330, 2150, 30540, 1000, 0x0)
    OP_95(0xFE, -1390, 2660, 35120, 1000, 0x0)

    def lambda_1623():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1623)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_19_15DB end

    def Function_20_1644(): pass

    label("Function_20_1644")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, 4040, 1950, 18100, 333)
    OP_95(0xFE, -2660, 2430, 31010, 1000, 0x0)
    OP_95(0xFE, -1390, 2660, 35120, 1000, 0x0)

    def lambda_168C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_168C)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_20_1644 end

    def Function_21_16AD(): pass

    label("Function_21_16AD")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -7760, 1920, 21240, 26)
    OP_95(0xFE, -2950, 1760, 29310, 1000, 0x0)
    OP_95(0xFE, -2800, 2660, 35080, 1000, 0x0)

    def lambda_16F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_16F5)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_21_16AD end

    def Function_22_1716(): pass

    label("Function_22_1716")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -7210, 1990, 19830, 26)
    OP_95(0xFE, -1240, 1760, 29900, 1000, 0x0)
    OP_95(0xFE, -1600, 2660, 35120, 1000, 0x0)

    def lambda_175E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_175E)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_22_1716 end

    def Function_23_177F(): pass

    label("Function_23_177F")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -30, 1810, 12140, 341)
    OP_95(0xFE, -2950, 1760, 29310, 1000, 0x0)
    OP_95(0xFE, -2800, 2660, 35080, 1000, 0x0)

    def lambda_17C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_17C7)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_23_177F end

    def Function_24_17E8(): pass

    label("Function_24_17E8")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, 1150, 1760, 11990, 341)
    OP_95(0xFE, -1240, 1760, 29900, 1000, 0x0)
    OP_95(0xFE, -1600, 2660, 35120, 1000, 0x0)

    def lambda_1830():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1830)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_24_17E8 end

    def Function_25_1851(): pass

    label("Function_25_1851")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -5550, 1990, 15680, 26)
    OP_95(0xFE, -2950, 1760, 29310, 1000, 0x0)
    OP_95(0xFE, -2800, 2660, 35080, 1000, 0x0)

    def lambda_1899():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1899)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_25_1851 end

    def Function_26_18BA(): pass

    label("Function_26_18BA")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -4270, 1990, 16100, 26)
    OP_95(0xFE, -1240, 1760, 29900, 1000, 0x0)
    OP_95(0xFE, -1600, 2660, 35120, 1000, 0x0)

    def lambda_1902():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1902)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_26_18BA end

    def Function_27_1923(): pass

    label("Function_27_1923")

    OP_95(0xFE, -8970, 330, 5920, 2000, 0x0)
    OP_93(0xFE, 0x109, 0x1F4)

    def lambda_1943():

        label("loc_1943")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_1943")

    QueueWorkItem2(0xFE, 2, lambda_1943)
    Sleep(2500)
    EndChrThread(0xFE, 0x2)
    OP_95(0xFE, -7220, 1770, 9000, 1200, 0x0)
    OP_95(0xFE, -2350, 1990, 19350, 1200, 0x0)
    Return()

    # Function_27_1923 end

    def Function_28_1980(): pass

    label("Function_28_1980")

    OP_95(0xFE, -10140, 250, 6390, 1200, 0x0)
    OP_95(0xFE, -8109, 1770, 9690, 1200, 0x0)
    OP_95(0xFE, -3180, 1990, 19840, 1200, 0x0)
    Return()

    # Function_28_1980 end

    def Function_29_19BD(): pass

    label("Function_29_19BD")

    OP_9F(0x0, 0x1D)
    OP_9F(0x1, -28630, 0, 10380)
    OP_9F(0x1, -19800, 0, 9100)
    OP_9F(0x1, -11600, 0, 3800)
    OP_9F(0x2, 0x1D, 5000, 0x6)
    Return()

    # Function_29_19BD end

    def Function_30_19F5(): pass

    label("Function_30_19F5")

    SetChrPos(0xFE, 470, 1770, 10040, 45)
    OP_95(0xFE, -3140, 1760, 29500, 1500, 0x0)
    Return()

    # Function_30_19F5 end

    def Function_31_1A1B(): pass

    label("Function_31_1A1B")

    SetChrPos(0xFE, 1910, 1770, 10160, 45)
    OP_95(0xFE, -1330, 1760, 29360, 1500, 0x0)
    Return()

    # Function_31_1A1B end

    def Function_32_1A41(): pass

    label("Function_32_1A41")

    SetChrPos(0xFE, -6160, 1590, 7540, 315)
    OP_95(0xFE, -3140, 1760, 29500, 1500, 0x0)
    Return()

    # Function_32_1A41 end

    def Function_33_1A67(): pass

    label("Function_33_1A67")

    SetChrPos(0xFE, -5150, 1640, 7470, 314)
    OP_95(0xFE, -1330, 1760, 29360, 1500, 0x0)
    Return()

    # Function_33_1A67 end

    def Function_34_1A8D(): pass

    label("Function_34_1A8D")

    SetChrPos(0xFE, -7000, 690, 5700, 314)
    OP_95(0xFE, -6030, 1770, 9130, 1200, 0x0)
    OP_95(0xFE, -3140, 1760, 29500, 1200, 0x0)
    Return()

    # Function_34_1A8D end

    def Function_35_1AC7(): pass

    label("Function_35_1AC7")

    SetChrPos(0xFE, -5600, 740, 5500, 44)
    OP_95(0xFE, -4950, 1770, 8820, 1200, 0x0)
    OP_95(0xFE, -1330, 1760, 29360, 1200, 0x0)
    Return()

    # Function_35_1AC7 end

    def Function_36_1B01(): pass

    label("Function_36_1B01")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(803)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    LoadChrToIndex("chr/ch02700.itc", 0x20)
    LoadChrToIndex("chr/ch33000.itc", 0x28)
    LoadChrToIndex("chr/ch33300.itc", 0x29)
    LoadChrToIndex("chr/ch27700.itc", 0x2A)
    LoadChrToIndex("chr/ch27600.itc", 0x2B)
    LoadChrToIndex("chr/ch33100.itc", 0x2C)
    LoadChrToIndex("chr/ch32400.itc", 0x2D)
    LoadChrToIndex("chr/ch22000.itc", 0x2E)
    LoadChrToIndex("chr/ch33200.itc", 0x2F)
    LoadChrToIndex("chr/ch27800.itc", 0x30)
    LoadChrToIndex("chr/ch27900.itc", 0x31)
    SetChrChipByIndex(0x1F, 0x28)
    SetChrChipByIndex(0x20, 0x29)
    SetChrChipByIndex(0x21, 0x2A)
    SetChrChipByIndex(0x22, 0x2B)
    SetChrChipByIndex(0x23, 0x2C)
    SetChrChipByIndex(0x24, 0x2D)
    SetChrChipByIndex(0x25, 0x2E)
    SetChrChipByIndex(0x26, 0x2F)
    SetChrChipByIndex(0x27, 0x30)
    SetChrChipByIndex(0x28, 0x31)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x8000)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x1F, 0x4)
    ClearChrFlags(0x20, 0x4)
    ClearChrFlags(0x21, 0x4)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    ClearChrFlags(0x24, 0x4)
    ClearChrFlags(0x25, 0x4)
    ClearChrFlags(0x26, 0x4)
    ClearChrFlags(0x27, 0x4)
    ClearChrFlags(0x28, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    OP_68(-14500, 1950, 7000, 0)
    MoveCamera(40, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, -3000, 1990, 20500, 180)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x13, -3000, 1990, 21500, 180)
    ClearChrFlags(0x1D, 0x80)
    OP_78(0x4, 0x1D)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1D, -28630, 0, 10380, 130)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)
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
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    SetMapObjFrame(0xFF, "ka01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ka02", 0x1, 0x1)
    BeginChrThread(0x29, 0, 0, 37)
    FadeToBright(3000, 0)
    OP_68(-2580, 10570, 29050, 0)
    MoveCamera(20, 3, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(36500, 0)
    OP_68(-2580, 10570, 29050, 14000)
    MoveCamera(345, -13, 0, 14000)
    OP_6E(800, 14000)
    SetCameraDistance(36500, 14000)
    BeginChrThread(0x1F, 0, 0, 17)
    BeginChrThread(0x20, 0, 0, 18)
    BeginChrThread(0x21, 0, 0, 19)
    BeginChrThread(0x22, 0, 0, 20)
    BeginChrThread(0x23, 0, 0, 21)
    BeginChrThread(0x24, 0, 0, 22)
    BeginChrThread(0x25, 0, 0, 23)
    BeginChrThread(0x26, 0, 0, 24)
    BeginChrThread(0x27, 0, 0, 25)
    BeginChrThread(0x28, 0, 0, 26)
    Sleep(6000)
    BeginChrThread(0x1D, 0, 0, 29)
    Sleep(2000)
    Fade(500)
    Fade(500)
    Sound(459, 0, 100, 0)
    EndChrThread(0x29, 0x0)
    BeginChrThread(0x1F, 0, 0, 30)
    BeginChrThread(0x20, 0, 0, 31)
    BeginChrThread(0x21, 0, 0, 32)
    BeginChrThread(0x22, 0, 0, 33)
    BeginChrThread(0x23, 0, 0, 34)
    BeginChrThread(0x24, 0, 0, 35)
    OP_68(-10140, 2050, 6000, 0)
    MoveCamera(12, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    OP_6E(600, 10000)
    WaitChrThread(0x1D, 0)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    OP_71(0x4, 0xF1, 0x10E, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0x4)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x12, -10990, 0, 4660, 208)
    SetChrPos(0x13, -10990, 0, 4660, 208)
    BeginChrThread(0x13, 0, 0, 27)
    Sleep(1500)
    BeginChrThread(0x12, 0, 0, 28)
    Sleep(1600)
    OP_71(0x4, 0x10F, 0x12C, 0x0, 0x0)
    Sound(461, 0, 100, 0)
    OP_79(0x4)
    Sleep(1500)
    Fade(500)
    OP_68(10490, 2380, 14240, 0)
    MoveCamera(359, 11, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(17000, 0)
    OP_68(10490, 2380, 14240, 6000)
    MoveCamera(19, 19, 0, 6000)
    OP_6E(580, 6000)
    SetCameraDistance(17000, 6000)
    SetChrPos(0x104, 13520, 0, 14590, 270)

    def lambda_1F41():
        OP_95(0xFE, 8590, 1770, 14770, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1F41)
    SetChrPos(0x103, 15170, 0, 14690, 270)

    def lambda_1F6C():
        OP_95(0xFE, 9760, 1400, 14890, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1F6C)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    ClearChrFlags(0x14, 0x4)
    SetChrPos(0x14, 15760, 0, 13260, 272)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)

    def lambda_1FB3():
        OP_95(0xFE, 9320, 1410, 13720, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1FB3)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sleep(3000)
    BeginChrThread(0x29, 0, 0, 38)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x29, 1)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x323)
    SetScenarioFlags(0x5C, 1)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_1B01 end

    def Function_37_200B(): pass

    label("Function_37_200B")

    Sound(803, 2, 0, 0)
    Sleep(100)
    OP_25(0x323, 0xA)
    Sleep(100)
    OP_25(0x323, 0x14)
    Sleep(100)
    OP_25(0x323, 0x1E)
    Sleep(100)
    OP_25(0x323, 0x28)
    Sleep(100)
    OP_25(0x323, 0x32)
    Sleep(100)
    OP_25(0x323, 0x3C)
    Sleep(100)
    OP_25(0x323, 0x46)
    Sleep(100)
    OP_25(0x323, 0x50)
    Return()

    # Function_37_200B end

    def Function_38_204A(): pass

    label("Function_38_204A")

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

    # Function_38_204A end

    def Function_39_207F(): pass

    label("Function_39_207F")

    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)

    def lambda_208C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_208C)
    OP_95(0xFE, -2210, 2660, 31430, 5000, 0x0)
    OP_95(0xFE, -2210, 1760, 27140, 5000, 0x0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 1000, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    SetChrFlags(0x13, 0x20)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    OP_95(0xFE, -2360, 1940, 25100, 5000, 0x0)
    Return()

    # Function_39_207F end

    def Function_40_212A(): pass

    label("Function_40_212A")


    def lambda_212F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_212F)
    OP_95(0xFE, -2720, 2660, 31430, 5000, 0x0)
    OP_95(0xFE, -2720, 1760, 29040, 5000, 0x0)
    Return()

    # Function_40_212A end

    def Function_41_2164(): pass

    label("Function_41_2164")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrChipByIndex(0xFE, 0x29)

    def lambda_2177():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2177)
    OP_95(0xFE, -1310, 2580, 31270, 5000, 0x0)
    OP_95(0xFE, -1170, 1760, 29010, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    Return()

    # Function_41_2164 end

    def Function_42_21B0(): pass

    label("Function_42_21B0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    LoadChrToIndex("apl/ch50229.itc", 0x20)
    LoadChrToIndex("apl/ch50230.itc", 0x21)
    LoadChrToIndex("apl/ch50232.itc", 0x22)
    LoadChrToIndex("apl/ch50233.itc", 0x23)
    LoadChrToIndex("chr/ch00950.itc", 0x28)
    LoadChrToIndex("chr/ch00951.itc", 0x29)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00051.itc", 0x2B)
    LoadChrToIndex("chr/ch00350.itc", 0x2D)
    LoadChrToIndex("chr/ch00356.itc", 0x2E)
    LoadChrToIndex("chr/ch00351.itc", 0x2F)
    LoadChrToIndex("chr/ch00250.itc", 0x30)
    LoadChrToIndex("chr/ch00251.itc", 0x31)
    LoadChrToIndex("chr/ch00252.itc", 0x32)
    LoadChrToIndex("apl/ch50231.itc", 0x33)
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0xA)
    SetChrChipByIndex(0x103, 0x30)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrPos(0x101, -2160, 2660, 36390, 180)
    SetChrPos(0x15, -2160, 2660, 36390, 180)
    SetChrPos(0x13, -2160, 2660, 36390, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x104, -2660, 1990, 18290, 0)
    SetChrPos(0x103, 3680, 1960, 17210, 135)
    LoadEffect(0x0, "event\\ev201_00.eff")
    LoadEffect(0x1, "battle\\ms00004.eff")
    OP_68(-2160, 4600, 35160, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(21500, 0)
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
    FadeToBright(1000, 0)
    BeginChrThread(0x13, 0, 0, 39)
    OP_68(-2040, 2800, 25190, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(480, 3000)
    SetCameraDistance(21500, 3000)
    Sleep(1000)
    Sound(1221, 255, 100, 0)
    Sleep(500)
    SetChrPos(0x1D, -2210, 1760, 25140, 0)
    PlayEffect(0x0, 0xFF, 0x103, 0x0, 0, 1600, 0, 0, 0, 0, 1000, 1000, 1000, 0x1D, 0, 1000, 0, 0)
    Sound(255, 0, 100, 0)
    Sleep(250)
    Sound(1876, 255, 100, 2)
    Sound(251, 0, 100, 0)
    WaitChrThread(0x13, 0)
    Sleep(500)

    def lambda_244B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_244B)
    SetChrChipByIndex(0x13, 0x33)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x2)
    Sound(1320, 255, 100, 1)
    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x104, 0x0)
    Sound(250, 0, 100, 0)
    Sleep(100)
    SetChrChip(0x0, 0x104, 0x32, 0x12C)
    SetChrSubChip(0x104, 0x1)
    OP_99(0x104, 0x13, 0x1F4, 0x2328, 0x0)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x2)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    Sound(1877, 255, 100, 2)
    SetChrSubChip(0x104, 0x2)
    Sound(814, 0, 100, 0)
    Sound(819, 0, 100, 0)
    Sound(830, 0, 100, 0)
    SetChrChip(0x1, 0x104, 0x0, 0x0)
    OP_9D(0x104, 0xFFFFF682, 0x7C6, 0x59EC, 0x3E8, 0x7D0)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    Sound(514, 0, 100, 0)
    SetChrSubChip(0x104, 0x0)
    Sound(31, 0, 100, 0)
    Sleep(100)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    Sound(30, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x104, 0x2F)
    ClearChrFlags(0x104, 0x20)
    OP_95(0x104, -2280, 1990, 24350, 5000, 0x0)
    SetChrChipByIndex(0x104, 0x2D)
    Sound(808, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x104,
        "#2201671V#0301F#11PPhew... Where do ya think you're going?\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x103, 0x30)
    OP_95(0x103, -840, 1990, 23150, 5000, 0x0)
    TurnDirection(0x103, 0x13, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#2201672V#0201F#11PThis man is the true culprit behind the\x01",
            "series of events...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201673VRandy, Tio!\x02",
    )

    CloseMessageWindow()
    OP_68(-2120, 2810, 27360, 3000)
    BeginChrThread(0x101, 0, 0, 40)
    Sleep(1000)
    BeginChrThread(0x15, 0, 0, 41)
    WaitChrThread(0x101, 0)
    Sleep(1500)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    Sound(804, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#2201674V#0002F#5POh, thank goodness...\x01",
            "You guys managed to catch him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201675V#0301F#12PYeah. It was lights out for him as\x01",
            "soon I saw him pull out a gun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201676V#0004F#5PGood call.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201677V#0205F#12PThat aside, why have you joined forces\x01",
            "with Four Eyes from the First Division?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "#2201678V#0607F#5PWh-Who do you think you're calling Four Eyes?!\x02\x03",
            "#2201679V#0603FExplain yourselves. Now.\x01",
            "What is the meaning of all of this?\x02\x03",
            "#2201680V#0601FYou've even brought backup...\x01",
            "What exactly were you planning?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201681V#0008F#5PWell, you see...\x02",
    )

    CloseMessageWindow()

    def lambda_28B8():

        label("loc_28B8")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_28B8")

    QueueWorkItem2(0x101, 2, lambda_28B8)

    def lambda_28CA():

        label("loc_28CA")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_28CA")

    QueueWorkItem2(0x104, 2, lambda_28CA)

    def lambda_28DC():

        label("loc_28DC")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_28DC")

    QueueWorkItem2(0x103, 2, lambda_28DC)

    def lambda_28EE():

        label("loc_28EE")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_28EE")

    QueueWorkItem2(0x15, 2, lambda_28EE)
    Sound(1901, 255, 100, 0)
    SetChrChipByIndex(0x13, 0x1F)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    Sound(804, 0, 100, 0)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x104, 0x2)
    OP_96(0x104, 0xFFFFF6AA, 0x7C6, 0x5B04, 0x1770, 0x0)
    SetChrChipByIndex(0x104, 0x2D)
    Sound(819, 0, 100, 0)
    Sound(808, 0, 100, 0)
    Sleep(1000)
    SetChrChip(0x0, 0x13, 0x32, 0x12C)
    SetChrChipByIndex(0x13, 0x20)
    ClearChrFlags(0x13, 0x20)

    def lambda_2966():
        OP_95(0xFE, 8780, 1760, 24750, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2966)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#2201683V#0307F#5PThe hell?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201684V#0007F#5PHe can still move?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c110B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_21B0 end

    def Function_43_2A43(): pass

    label("Function_43_2A43")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-21000, 6500, 7000, 0)
    MoveCamera(45, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x101, -26500, 300, 17500, 180)
    SetChrPos(0x102, -25800, 300, 17500, 180)
    SetChrPos(0x103, -27200, 300, 17500, 180)
    SetChrPos(0x104, -26500, 300, 17500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_68(-21000, 5000, 7000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_2B44():
        OP_96(0xFE, 0xFFFF987C, 0x0, 0x2A94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B44)

    def lambda_2B5E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B5E)
    Sleep(700)

    def lambda_2B72():
        OP_96(0xFE, 0xFFFF94F8, 0x0, 0x2E7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B72)

    def lambda_2B8C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2B8C)
    Sleep(700)

    def lambda_2BA0():
        OP_96(0xFE, 0xFFFF9C00, 0x0, 0x2F44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BA0)

    def lambda_2BBA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2BBA)
    Sleep(700)

    def lambda_2BCE():
        OP_96(0xFE, 0xFFFF987C, 0x0, 0x332C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BCE)

    def lambda_2BE8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2BE8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_6F(0x1)
    Fade(1000)
    OP_68(-26500, 1000, 12000, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#4100617V#5P#0001FIt's already nighttime...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#4100618V#12P#0000FWe need to go and speak with Gantz.\x02",
    )

    CloseMessageWindow()

    def lambda_2CCE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2CCE)
    Sleep(50)
    TurnDirection(0x103, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#4100619V#5P#0104FRight, let's head over to the hotel.\x02\x03",
            "#4100620V#0100FThe VIP rooms are on the top floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100621V#5P#0306FImagine hitting the jackpot and livin'\x01",
            "the baller life in a five-star hotel.\x02\x03",
            "#4100622V#0301FDamn, I'm jealous as hell.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)

    ChrTalk(
        0x103,
        "#4100623V#6P#0211FFocus on the problem at hand, Randy.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -26500, 0, 12000, 180)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetScenarioFlags(0xC1, 7)
    EventEnd(0x5)
    Return()

    # Function_43_2A43 end

    def Function_44_2E5B(): pass

    label("Function_44_2E5B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50506.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("chr/ch02751.itc", 0x21)
    LoadChrToIndex("chr/ch02752.itc", 0x22)
    LoadChrToIndex("chr/ch31250.itc", 0x23)
    LoadChrToIndex("chr/ch31251.itc", 0x24)
    LoadChrToIndex("chr/ch31350.itc", 0x25)
    LoadChrToIndex("chr/ch31351.itc", 0x26)
    LoadChrToIndex("chr/ch05100.itc", 0x27)
    LoadChrToIndex("chr/ch05200.itc", 0x28)
    LoadChrToIndex("chr/ch00150.itc", 0x29)
    LoadChrToIndex("chr/ch00151.itc", 0x2A)
    LoadChrToIndex("chr/ch00250.itc", 0x2B)
    LoadChrToIndex("chr/ch00251.itc", 0x2C)
    LoadChrToIndex("chr/ch00950.itc", 0x2D)
    LoadChrToIndex("chr/ch00951.itc", 0x2E)
    LoadChrToIndex("chr/ch00952.itc", 0x2F)
    LoadChrToIndex("apl/ch50509.itc", 0x30)
    LoadChrToIndex("chr/ch00152.itc", 0x31)
    LoadChrToIndex("chr/ch00254.itc", 0x32)
    OP_68(6100, 1000, -6300, 0)
    MoveCamera(35, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 9000, 0, -13700, 0)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 8600, 0, -15200, 0)
    SetChrChipByIndex(0x103, 0x2B)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 9800, 0, -15700, 0)
    SetChrPos(0x104, 10200, 0, -14200, 0)
    SetChrChipByIndex(0x10A, 0x2D)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x10A, 11000, 0, -13700, 0)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 9900, 0, -15000, 0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    ClearChrFlags(0x14, 0x4)
    SetChrPos(0x14, 5000, 0, -14500, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x19, 0x25)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x25)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x25)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x19, -22600, 500, 9200, 180)
    SetChrPos(0x1A, -22600, 500, 9200, 180)
    SetChrPos(0x1B, -22600, 500, 9200, 180)
    SetChrPos(0x1C, -22600, 500, 9200, 180)
    SetChrChipByIndex(0x17, 0x27)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    OP_90(0x17, 1600, 1770, 13000, 180)
    SetChrChipByIndex(0x18, 0x28)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_90(0x18, 600, 1770, 13400, 180)
    OP_78(0x8, 0x1D)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x8, 0x4)
    SetChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1D, 0x4)
    OP_49()
    SetChrPos(0x1D, -22000, 0, 10000, 0)
    OP_D3(0x1D, 0x0, 0x186A0, 0x0, 0x0)
    OP_74(0x8, 0x1E)
    OP_70(0x8, 0x0)
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
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "battle\\mgaria1.eff")
    LoadEffect(0x2, "battle\\mg030_00.eff")
    LoadEffect(0x4, "battle\\btgun00.eff")

    def lambda_31D5():
        OP_96(0xFE, 0xBB8, 0x0, 0xFFFFFD44, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31D5)
    Sleep(50)

    def lambda_31F2():
        OP_96(0xFE, 0x1068, 0x0, 0xFFFFFB50, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_31F2)
    Sleep(50)

    def lambda_320F():
        OP_96(0xFE, 0xA28, 0x0, 0xFFFFF768, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_320F)
    Sleep(50)

    def lambda_322C():
        OP_96(0xFE, 0xED8, 0x0, 0xFFFFF574, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_322C)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 3, 0, 3)

    def lambda_326A():
        OP_96(0xFE, 0x3E8, 0x0, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_326A)
    OP_68(3100, 1000, -1700, 3000)
    MoveCamera(45, 21, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15500, 3000)
    FadeToBright(2000, 0)
    BeginChrThread(0x29, 1, 0, 57)
    WaitChrThread(0x101, 1)

    def lambda_32C5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_32C5)
    WaitChrThread(0x104, 1)

    def lambda_32D6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_32D6)
    WaitChrThread(0x102, 1)

    def lambda_32E7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_32E7)
    WaitChrThread(0x103, 1)

    def lambda_32F8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_32F8)
    WaitChrThread(0x14, 1)
    EndChrThread(0x29, 0x1)
    EndChrThread(0x14, 0x3)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_332F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_332F)
    WaitChrThread(0x103, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5200163V#0006F#5P*huff* *huff*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200164V#0306F#5PI dunno 'bout you guys, but I'm gettin' tired.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        "#5200165V#6P#1112FAre you okay, Lloyd?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x104,
        "Shizuku",
        "#5200166V#6P#6001FI-I'll get down from you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200167V#0000F#5PNo, it's fine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200168V#0309F#5PHaha, you little ladies just leave this to us.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x17, 0x8)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)

    NpcTalk(
        0x17,
        "Woman's Voice",
        "#5200169V#4POh, if it isn't Lloyd and crew.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_353C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_353C)

    def lambda_3549():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3549)

    def lambda_3556():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3556)

    def lambda_3563():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3563)

    def lambda_3570():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3570)
    ClearChrFlags(0x17, 0x8)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    OP_68(3100, 1000, 200, 4000)

    def lambda_359D():
        OP_96(0xFE, 0xE10, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_359D)
    Sleep(100)

    def lambda_35BA():
        OP_96(0xFE, 0xA28, 0xA, 0x960, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_35BA)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x18, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#5200170V#12P#0011FIlya? Rixia?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#5200171V#1808F#5PE-Everyone...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3755")

    NpcTalk(
        0x101,
        "KeA",
        (
            "#5200172V#1105F#11PIt's Rixia and the lady that snores\x01",
            "really loud!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5200178V#5P#1705FSnores...?\x02\x03",
            "#5200179V#1702FAnyway, look at these two cuties.\x02\x03",
            "#5200181V#1709FYou've even got your big puppy with you.\x01",
            "I've gotta say, that's one interesting\x01",
            "troupe you're traveling with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A2F")

    label("loc_3755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3849")

    NpcTalk(
        0x101,
        "KeA",
        "#5200175V#1110F#11PAh! It's Rixia!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5200180V#5P#1705FHehe, look at these two cuties.\x02\x03",
            "#5200181V#1709FYou've even got your big puppy with you.\x01",
            "I've gotta say, that's one interesting\x01",
            "troupe you're traveling with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A2F")

    label("loc_3849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_397A")

    NpcTalk(
        0x101,
        "KeA",
        "#5200177V#1105F#11POh, it's the lady with the humongous snores!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5200173V#5P#1705FSnores...?\x02\x03",
            "#5200174V#1702FAnyway, what's with the cute kiddos?\x02\x03",
            "#5200181V#1709FYou've even got your big puppy with you.\x01",
            "I've gotta say, that's one interesting\x01",
            "troupe you're traveling with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A2F")

    label("loc_397A")


    ChrTalk(
        0x17,
        (
            "#5200176V#5P#1705FHehe, look at these two cuties.\x02\x03",
            "#5200181V#1709FYou've even got your big puppy with you.\x01",
            "I've gotta say, that's one interesting\x01",
            "troupe you're traveling with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A2F")


    ChrTalk(
        0x101,
        (
            "#5200182V#12P#0007FYou two, go back and hide in the\x01",
            "theater. And hurry!\x02\x03",
            "#5200183VThey'll be here any minu--\x02",
        )
    )

    CloseMessageWindow()
    Sound(489, 0, 100, 0)
    Sleep(1000)
    Sound(495, 0, 100, 0)
    Sleep(200)
    OP_24(0x1E9)
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
    ClearMapObjFlags(0x8, 0x4)
    OP_68(-22000, 1000, 10000, 2000)
    MoveCamera(345, 27, 0, 2000)
    SetCameraDistance(18500, 2000)

    def lambda_3B52():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B52)
    Sleep(50)

    def lambda_3B62():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3B62)

    def lambda_3B6F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3B6F)
    Sleep(50)

    def lambda_3B7F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3B7F)

    def lambda_3B8C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3B8C)
    Sleep(50)

    def lambda_3B9C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3B9C)

    def lambda_3BA9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3BA9)
    OP_6F(0x79)
    OP_71(0x8, 0xF1, 0x10E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x8)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    BeginChrThread(0x19, 3, 0, 55)
    Sleep(500)
    BeginChrThread(0x1A, 3, 0, 55)
    Sleep(500)
    BeginChrThread(0x1B, 3, 0, 55)
    Sleep(500)
    BeginChrThread(0x1C, 3, 0, 55)
    WaitChrThread(0x19, 3)
    Fade(500)
    OP_68(3100, 1000, 200, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    ClearScenarioFlags(0x0, 2)

    def lambda_3C50():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3C50)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x3)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x102, 3, 0, 47)
    BeginChrThread(0x103, 3, 0, 46)
    OP_0D()
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x1B, 0xFF)
    EndChrThread(0x1C, 0xFF)

    ChrTalk(
        0x104,
        (
            "#5200184V#0307F#11PDamn it! Just how many are they\x01",
            "settin' on us?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5200185V#11P#1705FH-Huh? What was that? Is this some\x01",
            "kind of new tourist thing?\x02\x03",
            "#5200186V#1709FIt sure looks like the real deal! Bravo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200187V#12P#0107FPlease, you all need to hide! Now!\x02",
    )

    CloseMessageWindow()
    OP_68(5600, 1000, -4800, 2000)
    MoveCamera(55, 21, 0, 2000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)

    def lambda_3DE6():
        OP_95(0xFE, 7000, 0, -5700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3DE6)
    Sleep(100)

    def lambda_3E03():
        OP_95(0xFE, 5900, 0, -7000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3E03)
    WaitChrThread(0x10A, 1)

    def lambda_3E21():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_3E21)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)

    def lambda_3E3A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_3E3A)
    WaitChrThread(0x16, 2)

    def lambda_3E4B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3E4B)
    OP_6F(0x41)

    ChrTalk(
        0x10A,
        "#5200188V#11P#0607FWhat the hell are you guys doing?!\x02",
    )

    CloseMessageWindow()

    def lambda_3E95():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E95)
    Sleep(50)

    def lambda_3EA5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3EA5)
    SetScenarioFlags(0x0, 2)

    ChrTalk(
        0x16,
        "#5200189V#11P#1007FHead to CPD headquarters, ASAP!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200190V#3P#0007FRoger!\x02",
    )

    CloseMessageWindow()
    OP_AD(0x3)
    OP_AD(0x4)
    OP_68(15500, 1000, 9700, 5000)
    MoveCamera(30, 21, 0, 5000)
    BeginChrThread(0x101, 3, 0, 48)
    BeginChrThread(0x104, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 50)
    BeginChrThread(0x103, 3, 0, 51)
    BeginChrThread(0x10A, 3, 0, 53)
    BeginChrThread(0x16, 3, 0, 54)
    BeginChrThread(0x14, 3, 0, 52)
    Sleep(1000)

    def lambda_3F5A():

        label("loc_3F5A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3F5A")

    QueueWorkItem2(0x17, 2, lambda_3F5A)

    def lambda_3F6C():

        label("loc_3F6C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3F6C")

    QueueWorkItem2(0x18, 2, lambda_3F6C)
    WaitChrThread(0x16, 3)
    EndChrThread(0x17, 0x2)
    EndChrThread(0x18, 0x2)
    OP_6F(0x41)
    EndChrThread(0x29, 0x1)
    Fade(500)
    OP_68(3100, 1000, 2200, 0)
    MoveCamera(10, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(14500, 1000)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x17,
        (
            "#5200191V#5P#1709FWow! It's like I've stepped straight into\x01",
            "an action novel!\x02\x03",
            "#5200192V#1702FSo be it. It's time for Ilya Platiere to\x01",
            "stand and fight!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_406C():
        OP_95(0xFE, 3200, 0, 2600, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_406C)
    WaitChrThread(0x18, 1)
    TurnDirection(0x18, 0x17, 500)

    ChrTalk(
        0x18,
        "#5200193V#1801F#5PIlya, don't be crazy! This isn't a game!\x02",
    )

    CloseMessageWindow()

    def lambda_40D1():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x3A98, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_40D1)
    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_40FD():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x3A98, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_40FD)
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 45)
    SetCameraDistance(17000, 5000)

    ChrTalk(
        0x17,
        (
            "#5200194V#6P#1705F#28ARixia, nooooo! This was my time to\x01",
            "shine...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetScenarioFlags(0x5C, 1)
    NewScene("c110B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_2E5B end

    def Function_45_4198(): pass

    label("Function_45_4198")

    SetChrPos(0x19, -7000, 0, 1500, 90)
    SetChrPos(0x1A, -7000, 0, 1500, 90)
    SetChrPos(0x1B, -7000, 0, 1500, 90)
    SetChrPos(0x1C, -7000, 0, 1500, 90)
    Sleep(500)
    BeginChrThread(0x19, 3, 0, 56)
    Sleep(500)
    BeginChrThread(0x1A, 3, 0, 56)
    Sleep(500)
    BeginChrThread(0x1B, 3, 0, 56)
    Sleep(500)
    BeginChrThread(0x1C, 3, 0, 56)
    Return()

    # Function_45_4198 end

    def Function_46_4201(): pass

    label("Function_46_4201")

    ClearScenarioFlags(0x0, 4)
    SetChrChipByIndex(0x103, 0x32)
    SetChrSubChip(0x103, 0x0)

    label("loc_420C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42FC")
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(831, 0, 100, 0)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    Sound(280, 0, 80, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x103, 0x3)
    Sleep(500)
    PlayEffect(0x2, 0x2, 0x103, 0x140, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0x19, 0, 0, 0, 0)
    SetChrSubChip(0x103, 0x4)
    Sleep(2000)
    StopEffect(0x2, 0x2)
    Jump("loc_420C")

    label("loc_42FC")

    SetScenarioFlags(0x0, 4)
    Return()

    # Function_46_4201 end

    def Function_47_4300(): pass

    label("Function_47_4300")

    ClearScenarioFlags(0x0, 3)
    SetChrChipByIndex(0x102, 0x31)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)

    label("loc_4319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_438B")
    Sleep(1500)
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    SetChrSubChip(0x102, 0x3)
    Sleep(150)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Jump("loc_4319")

    label("loc_438B")

    SetScenarioFlags(0x0, 3)
    Return()

    # Function_47_4300 end

    def Function_48_438F(): pass

    label("Function_48_438F")

    OP_92(0x101, 0x34BC, 0x25E4, 0x1F4)

    def lambda_43A1():
        OP_95(0xFE, 13500, 0, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43A1)
    WaitChrThread(0x101, 1)

    def lambda_43BF():
        OP_97(0xFE, 0x3A98, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43BF)
    WaitChrThread(0x101, 1)
    Return()

    # Function_48_438F end

    def Function_49_43D9(): pass

    label("Function_49_43D9")

    Sleep(600)
    OP_92(0x104, 0x396C, 0x21FC, 0x1F4)

    def lambda_43EE():
        OP_95(0xFE, 14700, 0, 8700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43EE)
    WaitChrThread(0x104, 1)

    def lambda_440C():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_440C)
    WaitChrThread(0x104, 1)
    Return()

    # Function_49_43D9 end

    def Function_50_4426(): pass

    label("Function_50_4426")

    SetChrSubChip(0x102, 0x2)
    Sleep(400)
    SetChrSubChip(0x102, 0x1)
    Sleep(100)
    SetChrSubChip(0x102, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    OP_92(0x102, 0x34BC, 0x25E4, 0x1F4)

    def lambda_4455():
        OP_95(0xFE, 13500, 0, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4455)
    WaitChrThread(0x102, 1)

    def lambda_4473():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4473)
    WaitChrThread(0x102, 1)
    Return()

    # Function_50_4426 end

    def Function_51_448D(): pass

    label("Function_51_448D")

    SetChrSubChip(0x103, 0x3)
    Sleep(1200)
    SetChrChipByIndex(0x103, 0x2B)
    SetChrSubChip(0x103, 0x0)
    OP_92(0x103, 0x396C, 0x21FC, 0x1F4)

    def lambda_44AE():
        OP_95(0xFE, 14700, 0, 8700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_44AE)
    WaitChrThread(0x103, 1)

    def lambda_44CC():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_44CC)
    WaitChrThread(0x103, 1)
    Return()

    # Function_51_448D end

    def Function_52_44E6(): pass

    label("Function_52_44E6")


    def lambda_44EB():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_44EB)
    WaitChrThread(0x14, 2)
    OP_92(0x14, 0x332C, 0x21FC, 0x1F4)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 0, 0, 3)
    BeginChrThread(0x29, 1, 0, 57)

    def lambda_453F():
        OP_96(0xFE, 0x3E8, 0x6EA, 0x25E4, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_453F)
    WaitChrThread(0x14, 1)

    def lambda_455D():
        OP_96(0xFE, 0x157C, 0x6EA, 0x319C, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_455D)
    WaitChrThread(0x14, 1)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x29, 0x1)

    def lambda_4583():
        OP_92(0xFE, 0x34BC, 0x319C, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_4583)
    SetChrSubChip(0x14, 0x2)
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    SetChrSubChip(0x14, 0x3)
    Sleep(50)
    SetChrSubChip(0x14, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_45C4():
        OP_9D(0xFE, 0x34BC, 0x0, 0x319C, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_45C4)
    Sleep(600)
    SetChrSubChip(0x14, 0x1)
    Sleep(50)
    SetChrSubChip(0x14, 0x2)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0x14, 0x3)
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    BeginChrThread(0x14, 0, 0, 3)
    BeginChrThread(0x29, 1, 0, 57)

    def lambda_461C():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_461C)
    WaitChrThread(0x14, 1)
    Return()

    # Function_52_44E6 end

    def Function_53_4636(): pass

    label("Function_53_4636")

    Sleep(2500)
    OP_92(0x10A, 0x4268, 0x21FC, 0x1F4)

    def lambda_464B():
        OP_95(0xFE, 17000, 0, 8700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_464B)
    WaitChrThread(0x10A, 1)

    def lambda_4669():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_4669)
    WaitChrThread(0x10A, 1)
    Return()

    # Function_53_4636 end

    def Function_54_4683(): pass

    label("Function_54_4683")

    Sleep(2800)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    OP_92(0x16, 0x4268, 0x21FC, 0x1F4)

    def lambda_46A0():
        OP_95(0xFE, 17000, 0, 8700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_46A0)
    WaitChrThread(0x16, 1)

    def lambda_46BE():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_46BE)
    WaitChrThread(0x16, 1)
    Return()

    # Function_54_4683 end

    def Function_55_46D8(): pass

    label("Function_55_46D8")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_46E5():
        OP_95(0xFE, -22800, 0, 7200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_46E5)

    def lambda_46FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_46FF)
    WaitChrThread(0xFE, 1)

    def lambda_4714():
        OP_95(0xFE, -13800, 0, 3200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4714)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_55_46D8 end

    def Function_56_472E(): pass

    label("Function_56_472E")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_473B():
        OP_95(0xFE, 3000, 0, 1500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_473B)
    WaitChrThread(0xFE, 1)

    def lambda_4759():
        OP_95(0xFE, 13000, 0, 9500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4759)
    WaitChrThread(0xFE, 1)

    def lambda_4777():
        OP_95(0xFE, 23000, 0, 9500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4777)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_472E end

    def Function_57_4791(): pass

    label("Function_57_4791")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47AA")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_57_4791")

    label("loc_47AA")

    Return()

    # Function_57_4791 end

    def Function_58_47AB(): pass

    label("Function_58_47AB")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4883")

    ChrTalk(
        0x104,
        "#0300FArc en Ciel's show is startin' any minute now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FIt's certainly tempting...\x02\x03",
            "#0001F...but I think we should check on Gantz first.\x01",
            "He should be staying at the hotel over there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_48D0")

    label("loc_4883")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tonight's performance has yet to begin.\x01",
            "Come by at a later time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_48D0")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Return()

    # Function_58_47AB end

    def Function_59_48E7(): pass

    label("Function_59_48E7")

    EventBegin(0x1)
    Call(0, 62)
    Sleep(50)
    SetChrPos(0x0, 20770, 0, 12930, 270)
    EventEnd(0x4)
    Return()

    # Function_59_48E7 end

    def Function_60_4903(): pass

    label("Function_60_4903")

    EventBegin(0x1)
    Call(0, 62)
    Sleep(50)
    SetChrPos(0x0, -39280, 0, 12420, 90)
    EventEnd(0x4)
    Return()

    # Function_60_4903 end

    def Function_61_491F(): pass

    label("Function_61_491F")

    EventBegin(0x1)
    Call(0, 62)
    Sleep(50)
    SetChrPos(0x0, 13270, 0, -19100, 315)
    EventEnd(0x4)
    Return()

    # Function_61_491F end

    def Function_62_493B(): pass

    label("Function_62_493B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49A5")

    ChrTalk(
        0x101,
        (
            "#0001FGantz should be staying in the fancy\x01",
            "hotel over there...\x02\x03",
            "Let's pay him a visit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B00")

    ChrTalk(
        0x101,
        (
            "#0000FIt's already nighttime...\x02\x03",
            "KeA's still waiting for us,\x01",
            "so let's head straight home.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A65")

    ChrTalk(
        0x102,
        (
            "#0100FAgreed. We've already finished\x01",
            "our work for the day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B00")

    label("loc_4A65")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AA4")

    ChrTalk(
        0x103,
        "#0200FCourse set for the SSS building.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B00")

    label("loc_4AA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B00")

    ChrTalk(
        0x104,
        (
            "#0300FAll right! Let's head home and get our\x01",
            "daily dose of KeDo's smile!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B00")

    Return()

    # Function_62_493B end

    SaveToFile()

Try(main)
