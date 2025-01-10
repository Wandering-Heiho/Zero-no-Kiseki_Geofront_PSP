from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1200.bin",                # FileName
        "c1200",                    # MapName
        "c1200",                    # Location
        0x001A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 26, 0, 10, 0, 11],
    )

    BuildStringList((
        "c1200",                  # 0
        "Cunha",                  # 1
        "Ozelle",                 # 2
        "Bishop",                 # 3
        "Old Man Quine",          # 4
        "Amisa",                  # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Tourist",                # 10
        "Tourist",                # 11
        "Citizen",                # 12
        "Citizen",                # 13
        "Citizen",                # 14
        "Citizen",                # 15
        "Citizen",                # 16
        "Cruise Ship Guide",      # 17
        "Heiyue Member",          # 18
        "Grace",                  # 19
        "Reins",                  # 20
        "Chief Roberts",          # 21
        "Bracer Scott",           # 22
        "Pearl",                  # 23
        "Nikolai",                # 24
        "Selene",                 # 25
        "Officer Franz",          # 26
        "Heiyue Member",          # 27
        "Heiyue Member",          # 28
        "Lau",                    # 29
        "Detective Dudley",       # 30
        "Yin",                    # 31
        "Dudley's Car",           # 32
        "Central Square",         # 33
        "West Street",            # 34
        "Administrative District",# 35
        "Residential District",   # 36
        "Entertainment District", # 37
        "East Street",            # 38
        "Downtown District",      # 39
        "Harbor District",        # 40
        "IBC",                    # 41
        "Station Street",         # 42
        "Back Alley",             # 43
        "Ursula Road",            # 44
        "East Crossbell Highway", # 45
        "West Crossbell Highway", # 46
        "Mainz Mountain Path",    # 47
    ))

    AddCharChip((
        "chr/ch22100.itc",                   # 00
        "chr/ch25200.itc",                   # 01
        "chr/ch26000.itc",                   # 02
        "apl/ch50168.itc",                   # 03
        "chr/ch21500.itc",                   # 04
        "chr/ch29300.itc",                   # 05
        "chr/ch31500.itc",                   # 06
        "chr/ch28100.itc",                   # 07
        "chr/ch06000.itc",                   # 08
        "chr/ch30000.itc",                   # 09
        "chr/ch21102.itc",                   # 0A
        "chr/ch20600.itc",                   # 0B
        "chr/ch20400.itc",                   # 0C
        "chr/ch21900.itc",                   # 0D
        "chr/ch20700.itc",                   # 0E
        "chr/ch20800.itc",                   # 0F
        "chr/ch26600.itc",                   # 10
        "chr/ch27200.itc",                   # 11
        "chr/ch26600.itc",                   # 12
        "chr/ch28900.itc",                   # 13
        "chr/ch29100.itc",                   # 14
        "chr/ch31400.itc",                   # 15
        "chr/ch24000.itc",                   # 16
        "chr/ch21300.itc",                   # 17
        "chr/ch24400.itc",                   # 18
        "chr/ch34200.itc",                   # 19
        "chr/ch21100.itc",                   # 1A
    ))

    DeclNpc(-13199,  0,       11500,   90,   257,  0x0, 0,   0,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(-10470,  0,       13340,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-52470,  2000,    21149,   90,   257,  0x0, 0,   2,   0,   0,   2,   0,   15,  255,  0)
    DeclNpc(39669,   -2500,   -19379,  180,  277,  0x0, 0,   3,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(38439,   -2490,   -18079,  135,  261,  0x0, 0,   4,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(7469,    -699,    3029,    180,  453,  0x0, 0,   10,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(9489,    -699,    129,     64,   389,  0x0, 0,   11,  0,   0,   9,   0,   25,  255,  0)
    DeclNpc(42000,   -2500,   0,       90,   389,  0x0, 0,   12,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(40000,   -2500,   0,       180,  389,  0x0, 0,   13,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(40000,   -2500,   -1250,   90,   389,  0x0, 0,   14,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(38000,   -2500,   0,       90,   389,  0x0, 0,   15,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(17629,   0,       -2130,   0,    389,  0x0, 0,   23,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(9409,    0,       13489,   90,   389,  0x0, 0,   12,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(22500,   0,       1019,    0,    389,  0x0, 0,   24,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(2900,    0,       9310,    90,   405,  0x0, 0,   25,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(3730,    0,       8510,    45,   389,  0x0, 0,   26,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(42450,   -2500,   2329,    235,  389,  0x0, 0,   16,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(18989,   9,       19649,   180,  389,  0x0, 0,   6,   0,   0,   0,   0,   35,  255,  0)
    DeclNpc(3069,    -699,    1110,    180,  389,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(21620,   0,       14909,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-9189,   -9,      12270,   315,  389,  0x0, 0,   5,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(3259,    -699,    1440,    90,   405,  0x0, 0,   17,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(5159,    -699,    1639,    270,  405,  0x0, 0,   18,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-18000,  0,       -5750,   90,   389,  0x0, 0,   19,  0,   0,   3,   0,   38,  255,  0)
    DeclNpc(-16979,  0,       -13449,  45,   389,  0x0, 0,   20,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(19100,   0,       16600,   0,    389,  0x0, 0,   9,   0,   0,   0,   0,   37,  255,  0)
    DeclNpc(22399,   0,       19500,   0,    453,  0x0, 0,   6,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(24000,   0,       17899,   45,   453,  0x0, 0,   6,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(19879,   0,       19629,   225,  389,  0x0, 0,   21,  0,   0,   0,   0,   40,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 54,  21.0,                  5.5,                   -1.5,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.4000000953674316,   -1.8333333730697632,   0.30000001192092896,   1.0])
    DeclEvent(0x0000, 0, 54,  13.5,                  11.5,                  -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -4.5,                  -1.149999976158142,    0.20000000298023224,   1.0])

    DeclActor(19200,   250,     20500,   2000,    19200,   1250,    20500,   0x007C, 0,  42, 0x0000)
    DeclActor(68620,   -2500,   15400,   1200,    68040,   -3500,   11820,   0x007C, 0,  41, 0x0000)
    DeclActor(34000,   -2500,   3400,    1500,    34000,   -1500,   3400,    0x007C, 0,  57, 0x0000)
    DeclActor(77440,   -2500,   19770,   1200,    77440,   -1000,   19770,   0x007C, 0,  58, 0x0000)

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "Central Square")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "West Street")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "Administrative District")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "Residential District")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "East Street")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "Downtown District")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "Harbor District")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "IBC")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "Station Street")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "Back Alley")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "Ursula Road")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-268.2200012207031, 0.0, 49.779998779296875, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-151.9600067138672, 0.0, -103.48999786376953, 0x0000, 0x0051, "")
    PlaceName(-81.55000305175781, 0.0, -69.43000030517578, 0x0000, 0x0054, "")
    PlaceName(-119.87000274658203, 0.0, -113.97000122070312, 0x0000, 0x0057, "")
    PlaceName(-152.94000244140625, 0.0, -65.5, 0x0000, 0x0053, "")
    PlaceName(-126.08999633789062, 0.0, -34.060001373291016, 0x0000, 0x0053, "")
    PlaceName(-192.57000732421875, 0.0, -72.05000305175781, 0x0000, 0x0053, "")
    PlaceName(-205.33999633789062, 0.0, -44.540000915527344, 0x0000, 0x0053, "")
    PlaceName(-173.89999389648438, 0.0, -2.619999885559082, 0x0000, 0x0052, "")
    PlaceName(-167.67999267578125, 0.0, -19.649999618530273, 0x0000, 0x0053, "")
    PlaceName(-156.22000122070312, 0.0, -30.790000915527344, 0x0000, 0x0053, "")
    PlaceName(-118.87999725341797, 0.0, 62.22999954223633, 0x0000, 0x0051, "")
    PlaceName(27.84000015258789, 0.0, -115.27999877929688, 0x0000, 0x0052, "")
    PlaceName(5.570000171661377, 0.0, -233.83999633789062, 0x0000, 0x0053, "")
    PlaceName(-11.460000038146973, 0.0, -209.60000610351562, 0x0000, 0x0053, "")
    PlaceName(-108.4000015258789, 0.0, -100.87000274658203, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_914",          # 00, 0
        "Function_1_9CC",          # 01, 1
        "Function_2_A7D",          # 02, 2
        "Function_3_BB7",          # 03, 3
        "Function_4_C68",          # 04, 4
        "Function_5_C93",          # 05, 5
        "Function_6_CBE",          # 06, 6
        "Function_7_CFE",          # 07, 7
        "Function_8_D3E",          # 08, 8
        "Function_9_D69",          # 09, 9
        "Function_10_D94",         # 0A, 10
        "Function_11_129E",        # 0B, 11
        "Function_12_1570",        # 0C, 12
        "Function_13_2810",        # 0D, 13
        "Function_14_4672",        # 0E, 14
        "Function_15_47B4",        # 0F, 15
        "Function_16_51AD",        # 10, 16
        "Function_17_5F77",        # 11, 17
        "Function_18_65EE",        # 12, 18
        "Function_19_670C",        # 13, 19
        "Function_20_682C",        # 14, 20
        "Function_21_6B8E",        # 15, 21
        "Function_22_71DC",        # 16, 22
        "Function_23_7520",        # 17, 23
        "Function_24_758E",        # 18, 24
        "Function_25_77C9",        # 19, 25
        "Function_26_7855",        # 1A, 26
        "Function_27_79D1",        # 1B, 27
        "Function_28_7A5C",        # 1C, 28
        "Function_29_7AAA",        # 1D, 29
        "Function_30_7B3E",        # 1E, 30
        "Function_31_7BB6",        # 1F, 31
        "Function_32_7C34",        # 20, 32
        "Function_33_7D99",        # 21, 33
        "Function_34_7DFF",        # 22, 34
        "Function_35_7E93",        # 23, 35
        "Function_36_7F27",        # 24, 36
        "Function_37_81DC",        # 25, 37
        "Function_38_8578",        # 26, 38
        "Function_39_8909",        # 27, 39
        "Function_40_8B4C",        # 28, 40
        "Function_41_8BA0",        # 29, 41
        "Function_42_8C8B",        # 2A, 42
        "Function_43_8DEB",        # 2B, 43
        "Function_44_91EE",        # 2C, 44
        "Function_45_9831",        # 2D, 45
        "Function_46_9F88",        # 2E, 46
        "Function_47_D8B1",        # 2F, 47
        "Function_48_D8EE",        # 30, 48
        "Function_49_D935",        # 31, 49
        "Function_50_D97C",        # 32, 50
        "Function_51_D9C3",        # 33, 51
        "Function_52_DA0A",        # 34, 52
        "Function_53_DBB1",        # 35, 53
        "Function_54_DFF8",        # 36, 54
        "Function_55_E6B3",        # 37, 55
        "Function_56_F588",        # 38, 56
        "Function_57_FAC8",        # 39, 57
        "Function_58_FBB0",        # 3A, 58
    ))


    def Function_0_914(): pass

    label("Function_0_914")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_954"),
        (1, "loc_960"),
        (2, "loc_96C"),
        (3, "loc_978"),
        (4, "loc_984"),
        (5, "loc_990"),
        (6, "loc_99C"),
        (SWITCH_DEFAULT, "loc_9A8"),
    )


    label("loc_954")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_960")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_96C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_978")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_984")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_990")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_99C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_9A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_9B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_9CB")

    Return()

    # Function_0_914 end

    def Function_1_9CC(): pass

    label("Function_1_9CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A7C")
    OP_95(0xFE, 14600, 0, 11500, 1000, 0x0)
    OP_95(0xFE, 20200, 0, 8200, 1000, 0x0)
    OP_95(0xFE, 20200, 0, -6200, 1000, 0x0)
    OP_95(0xFE, 14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -20000, 0, -6400, 1000, 0x0)
    OP_95(0xFE, -20000, 0, 6000, 1000, 0x0)
    OP_95(0xFE, -13200, 0, 11500, 1000, 0x0)
    Jump("Function_1_9CC")

    label("loc_A7C")

    Return()

    # Function_1_9CC end

    def Function_2_A7D(): pass

    label("Function_2_A7D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BB6")
    Sleep(3000)
    OP_95(0xFE, -13000, 2000, 21150, 5000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 5000, 0x0)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_95(0xFE, 1760, 2000, 24150, 5000, 0x0)
    OP_95(0xFE, 1760, 5080, 38700, 8000, 0x0)
    Sleep(3000)
    OP_95(0xFE, 1760, 2000, 24150, 5000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 5000, 0x0)
    OP_95(0xFE, -13000, 0, 14240, 5000, 0x0)
    OP_95(0xFE, -22130, 0, 5860, 5000, 0x0)
    OP_95(0xFE, -22020, 0, -46700, 5000, 0x0)
    Sleep(3000)
    OP_95(0xFE, -22130, 0, 5860, 5000, 0x0)
    OP_95(0xFE, -15540, 0, 14240, 5000, 0x0)
    OP_95(0xFE, -15540, 2000, 21150, 5000, 0x0)
    OP_95(0xFE, -52470, 2000, 21150, 5000, 0x0)
    Jump("Function_2_A7D")

    label("loc_BB6")

    Return()

    # Function_2_A7D end

    def Function_3_BB7(): pass

    label("Function_3_BB7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C67")
    OP_95(0xFE, -13000, 0, -10000, 4000, 0x0)
    OP_95(0xFE, 13000, 0, -10000, 4000, 0x0)
    OP_95(0xFE, 18000, 0, -4300, 4000, 0x0)
    OP_95(0xFE, 18000, 0, 7040, 4000, 0x0)
    OP_95(0xFE, 13000, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -12700, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -18000, 0, 5200, 4000, 0x0)
    OP_95(0xFE, -18000, 0, -5750, 4000, 0x0)
    Jump("Function_3_BB7")

    label("loc_C67")

    Return()

    # Function_3_BB7 end

    def Function_4_C68(): pass

    label("Function_4_C68")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C92")
    OP_94(0xFE, 0x708, 0xF32, 0xFFFFF9A2, 0xC3A, 0x3E8)
    Sleep(300)
    Jump("Function_4_C68")

    label("loc_C92")

    Return()

    # Function_4_C68 end

    def Function_5_C93(): pass

    label("Function_5_C93")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_5_C93 end

    def Function_6_CBE(): pass

    label("Function_6_CBE")

    OP_93(0xFE, 0xB4, 0x2BC)
    OP_93(0xFE, 0x5A, 0x2BC)
    OP_93(0xFE, 0x0, 0x2BC)
    OP_93(0xFE, 0x10E, 0x2BC)
    OP_93(0xFE, 0xB4, 0x2BC)
    OP_93(0xFE, 0x5A, 0x2BC)
    OP_93(0xFE, 0x0, 0x2BC)
    OP_93(0xFE, 0x10E, 0x2BC)
    OP_93(0xFE, 0xB4, 0x2BC)
    Return()

    # Function_6_CBE end

    def Function_7_CFE(): pass

    label("Function_7_CFE")

    OP_93(0xFE, 0x10E, 0x398)
    OP_93(0xFE, 0x0, 0x398)
    OP_93(0xFE, 0x5A, 0x398)
    OP_93(0xFE, 0xB4, 0x398)
    OP_93(0xFE, 0x10E, 0x398)
    OP_93(0xFE, 0x0, 0x398)
    OP_93(0xFE, 0x5A, 0x398)
    OP_93(0xFE, 0xB4, 0x398)
    OP_93(0xFE, 0x13B, 0x398)
    Return()

    # Function_7_CFE end

    def Function_8_D3E(): pass

    label("Function_8_D3E")

    OP_93(0xFE, 0x0, 0x28A)
    OP_93(0xFE, 0x5A, 0x28A)
    OP_93(0xFE, 0xB4, 0x28A)
    OP_93(0xFE, 0x10E, 0x28A)
    OP_93(0xFE, 0x0, 0x28A)
    OP_93(0xFE, 0x5A, 0x28A)
    Return()

    # Function_8_D3E end

    def Function_9_D69(): pass

    label("Function_9_D69")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D93")
    OP_94(0xFE, 0x1F22, 0x546, 0x7D9, 0xFFFFF7FE, 0x3E8)
    Sleep(300)
    Jump("Function_9_D69")

    label("loc_D93")

    Return()

    # Function_9_D69 end

    def Function_10_D94(): pass

    label("Function_10_D94")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC6")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E56")
    SetChrPos(0x0, 4870, 3350, 31570, 180)
    SetChrPos(0x1, 4870, 3350, 31570, 180)
    SetChrPos(0x2, 4870, 3350, 31570, 180)
    SetChrPos(0x3, 4870, 3350, 31570, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E29")
    SetChrPos(0x4, 4870, 3350, 31570, 180)
    SetChrPos(0x5, 4870, 3350, 31570, 180)
    Jump("loc_E48")

    label("loc_E29")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E48")
    SetChrPos(0x4, 4870, 3350, 31570, 180)

    label("loc_E48")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FC6")

    label("loc_E56")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F25")
    SetChrPos(0x0, -28110, 2000, 23520, 90)
    SetChrPos(0x1, -28110, 2000, 23520, 90)
    SetChrPos(0x2, -28110, 2000, 23520, 90)
    SetChrPos(0x3, -28110, 2000, 23520, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF8")
    SetChrPos(0x4, -28110, 2000, 23520, 90)
    SetChrPos(0x5, -28110, 2000, 23520, 90)
    Jump("loc_F17")

    label("loc_EF8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F17")
    SetChrPos(0x4, -28110, 2000, 23520, 90)

    label("loc_F17")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FC6")

    label("loc_F25")

    SetChrPos(0x0, -19600, 0, -27950, 0)
    SetChrPos(0x1, -19600, 0, -27950, 0)
    SetChrPos(0x2, -19600, 0, -27950, 0)
    SetChrPos(0x3, -19600, 0, -27950, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9E")
    SetChrPos(0x4, -19600, 0, -27950, 0)
    SetChrPos(0x5, -19600, 0, -27950, 0)
    Jump("loc_FBD")

    label("loc_F9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FBD")
    SetChrPos(0x4, -19600, 0, -27950, 0)

    label("loc_FBD")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FC6")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_FE3")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 46)
    Jump("loc_101A")

    label("loc_FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_FF7")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 52)
    Jump("loc_101A")

    label("loc_FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_100B")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 53)
    Jump("loc_101A")

    label("loc_100B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_101A")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 55)

    label("loc_101A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_105B")
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 2870, -700, -1190, 0)
    ClearChrFlags(0x1A, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1056")
    ClearChrFlags(0x1C, 0x80)
    OP_93(0x9, 0x87, 0x0)

    label("loc_1056")

    Jump("loc_1286")

    label("loc_105B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1073")
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_1286")

    label("loc_1073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1110")
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x8, 7270, 200, 16400, 135)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0xB, 17010, 0, -6810, 0)
    SetChrPos(0xC, 15600, 0, -7280, 45)
    SetChrChipByIndex(0xB, 0x16)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F1")
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)

    label("loc_10F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_110B")
    SetChrPos(0x21, 20500, 0, 15200, 180)

    label("loc_110B")

    Jump("loc_1286")

    label("loc_1110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1123")
    SetChrFlags(0xC, 0x10)
    Jump("loc_1286")

    label("loc_1123")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_113B")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_1286")

    label("loc_113B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1149")
    Jump("loc_1286")

    label("loc_1149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_115C")
    SetChrFlags(0xC, 0x10)
    Jump("loc_1286")

    label("loc_115C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1182")
    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_117D")
    ClearChrFlags(0x24, 0x80)

    label("loc_117D")

    Jump("loc_1286")

    label("loc_1182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1195")
    SetChrFlags(0xC, 0x80)
    Jump("loc_1286")

    label("loc_1195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_11CE")
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 800, -700, 3300, 270)
    BeginChrThread(0x20, 0, 0, 4)
    Jump("loc_1286")

    label("loc_11CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1204")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_1286")

    label("loc_1204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1232")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 33460, -2500, 1730, 0)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_1286")

    label("loc_1232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_125E")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    Jump("loc_1286")

    label("loc_125E")

    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)

    label("loc_1286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_129D")
    SetMapFlags(0x10000000)
    Event(0, 44)

    label("loc_129D")

    Return()

    # Function_10_D94 end

    def Function_11_129E(): pass

    label("Function_11_129E")

    OP_65(0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12C4")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_12C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12DC")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_12DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FD")
    SetMapObjFrame(0xFF, "kurotuki01", 0x0, 0x1)
    Jump("loc_130F")

    label("loc_12FD")

    SetMapObjFrame(0xFF, "kurotuki00", 0x0, 0x1)

    label("loc_130F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1327")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_1327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133F")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_133F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_END)), "loc_1352")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_1352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_136A")
    OP_65(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_136A")

    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13C1")
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_71(0x6, 0x12C, 0x12C, 0x0, 0x0)

    label("loc_13C1")

    SetMapObjFlags(0x5, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13DB")
    ClearMapObjFlags(0x5, 0x4)

    label("loc_13DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x32, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x37, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_142C")
    OP_65(0x1, 0x1)

    label("loc_142C")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 68040, -3500, 11820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundDistance(0x7E, 0x13E3E, 0x0, 0xFFFF8972, 0x13880, 0xC350, 0x64, 0x0)
    OP_E1(0x13DE4, 0x0, 0x71E8)
    OP_E1(0x13C54, 0x0, 0xD1B0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14ED")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_154E")

    label("loc_14ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1529")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_154E")

    label("loc_1529")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_154E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156A")
    Jump("loc_156F")

    label("loc_156A")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_156F")

    Return()

    # Function_11_129E end

    def Function_12_1570(): pass

    label("Function_12_1570")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159D")
    TurnDirection(0x0, 0x8, 0)
    OP_4B(0x8, 0xFF)
    Call(0, 56)
    Return()

    label("loc_159D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_164F")

    ChrTalk(
        0xFE,
        (
            "You'd have to be a pretty dumb tourist\x01",
            "to lose your train ticket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd feel bad if they had to search\x01",
            "all over town for it. Go on and\x01",
            "get this to them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_280C")

    label("loc_164F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1769")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_16CA")

    ChrTalk(
        0xFE,
        "Looks like the diet's finally over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm looking forward to hearing the\x01",
            "budget allocation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1764")

    label("loc_16CA")


    ChrTalk(
        0xFE,
        "Apparently, the diet just ended.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Boy, that sure was a lengthy one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hopefully, Mayor MacDowell was able\x01",
            "to stick up for us Crossbellans.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1764")

    Jump("loc_280C")

    label("loc_1769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1833")

    ChrTalk(
        0xFE,
        (
            "I just got questioned by a\x01",
            "Crossbell Times reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was a suave-looking young man\x01",
            "with a bit of a baby face... ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He shows promise, but he has a long\x01",
            "road ahead of him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_280C")

    label("loc_1833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_18B4")

    ChrTalk(
        0xFE,
        "You know, I was out on a walk earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It got cut short when an angry police\x01",
            "officer stopped me, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_280C")

    label("loc_18B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1983")

    ChrTalk(
        0xFE,
        (
            "Speaker Hartmann prefers to focus on\x01",
            "directing his lackeys instead of wasting\x01",
            "time appearing in the media.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The citizens of Crossbell deserve to know\x01",
            "the details of the diet!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A77")

    label("loc_1983")


    ChrTalk(
        0xFE,
        "Speaker Hartmann is far too composed to be tripped up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The media can't seem to get a peep out of him, either.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rumors say he's gunning to take Mayor MacDowell's\x01",
            "seat in the next election. It's making the citizens feel\x01",
            "anxious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1A77")

    Jump("loc_280C")

    label("loc_1A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1C59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1B40")

    ChrTalk(
        0xFE,
        (
            "Supposedly, some kind of accident occurred\x01",
            "at the Mishelam Center...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The strange thing is, it didn't make the news.\x01",
            "I've hardly heard any rumors about it, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C54")

    label("loc_1B40")


    ChrTalk(
        0xFE,
        (
            "I've only heard rumors, but apparently, there was\x01",
            "some sort of accident at the Mishelam Center?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It happened during the Anniversary Festival,\x01",
            "so naturally, there was an uproar about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's so weird, though. I haven't heard anything\x01",
            "about it from the media.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1C54")

    Jump("loc_280C")

    label("loc_1C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1D4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1CBA")

    ChrTalk(
        0xFE,
        (
            "What kind of cool entertainment do you think\x01",
            "they'll have this year?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4A")

    label("loc_1CBA")


    ChrTalk(
        0xFE,
        "One more month until the Anniversary Festival.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's apparently been extended to last for five\x01",
            "days, so I have to plan my time out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1D4A")

    Jump("loc_280C")

    label("loc_1D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1EC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1DAE")

    ChrTalk(
        0xFE,
        (
            "I've unfortunately only seen pictures of him\x01",
            "in magazines, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC4")

    label("loc_1DAE")


    ChrTalk(
        0xFE,
        (
            "You know the IBC's CEO, Dieter Crois?\x01",
            "He's already 40 years old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He clearly has business acumen. He's successfully\x01",
            "held multiple senior management positions for\x01",
            "businesses starting from a young age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And he's a total hottie, to boot!\x01",
            "Talk about a top tier man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1EC4")

    Jump("loc_280C")

    label("loc_1EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_207C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1F6B")

    ChrTalk(
        0xFE,
        (
            "There are all kinds of performers that work\x01",
            "for Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I love them all, but if I had to pick a favorite,\x01",
            "it'd be...Eugene.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2077")

    label("loc_1F6B")


    ChrTalk(
        0xFE,
        (
            "Two of the lead actors for Arc en Ciel\x01",
            "are pretty handsome, if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eugene, the Flaxen Prince, and\x01",
            "Theodor, the Silent Scion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heheheh... If I had to pick one, I think I'd\x01",
            "go with Team Eugene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He's got that princely charm, y'know?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2077")

    Jump("loc_280C")

    label("loc_207C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2212")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2121")

    ChrTalk(
        0xFE,
        (
            "I saw the mayor's secretary hanging\x01",
            "around here a bunch lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's kind and charming. He even went\x01",
            "out of his way to greet me! ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220D")

    label("loc_2121")


    ChrTalk(
        0xFE,
        (
            "There's been a well-dressed man\x01",
            "in the area as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think he was the mayor's secretary,\x01",
            "if I recall correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can tell he puts his heart and soul\x01",
            "into working. He was even nice enough\x01",
            "to give me a greeting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_220D")

    Jump("loc_280C")

    label("loc_2212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_236E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F3")

    ChrTalk(
        0xFE,
        (
            "Crossbell's in a hell of a messy political\x01",
            "situation, if you couldn't tell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The mayor's the only man that I feel has\x01",
            "our best interests at heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll be rooting for him all the way.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2369")

    label("loc_22F3")


    ChrTalk(
        0xFE,
        (
            "The mayor does a good job of presenting\x01",
            "himself in a dignified manner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll be rooting for him all the way.\x02",
    )

    CloseMessageWindow()

    label("loc_2369")

    Jump("loc_280C")

    label("loc_236E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_240F")

    ChrTalk(
        0xFE,
        (
            "What's with all the people exercising\x01",
            "in the park these days?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Probably just the trendy thing to do.\x01",
            "I think I'll give it a try sometime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_280C")

    label("loc_240F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2501")

    ChrTalk(
        0xFE,
        (
            "You ever see the ferris wheel at\x01",
            "Mishelam Wonderland? It's huge!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They have a bunch of other attractions,\x01",
            "like a roller coaster and haunted house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanna go on the roller coaster!\x01",
            "I've never ridden on one before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_280C")

    label("loc_2501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_26C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_25B9")

    ChrTalk(
        0xFE,
        (
            "Some Eastern-looking company opened\x01",
            "up an office around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hardly ever see their employees, though...\x01",
            "What kinda company are they supposed to be?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26BB")

    label("loc_25B9")


    ChrTalk(
        0xFE,
        (
            "Some Eastern-looking company opened\x01",
            "up an office around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to say, the Eastern-style aesthetics,\x01",
            "paired with that crimson exterior, is a\x01",
            "superb design choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When'd they even build it, though...?\x01",
            "I never saw a construction site.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_26BB")

    Jump("loc_280C")

    label("loc_26C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2792")

    ChrTalk(
        0xFE,
        (
            "Plenty of people in suits pass by here\x01",
            "in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You ever see them before? We call them\x01",
            "businessmen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have no problem admitting that a good\x01",
            "suit really makes the man. ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_280C")

    label("loc_2792")


    ChrTalk(
        0xFE,
        (
            "Doesn't a man in a good suit look\x01",
            "attractive?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I, uh...tend to get a little 'distracted' in\x01",
            "the morning by them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_280C")

    TalkEnd(0xFE)
    Return()

    # Function_12_1570 end

    def Function_13_2810(): pass

    label("Function_13_2810")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BEB")

    ChrTalk(
        0x101,
        (
            "#0000F(The Harbor District. Tront was in the\x01",
            "area for a bit, so he might have dropped\x01",
            "some of his belongings around here.)\x02",
        )
    )

    CloseMessageWindow()

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
        "Oh, are you looking for something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, now that you mention it...\x01",
            "There was some weirdo hanging out in\x01",
            "the park earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I remember him yelling about a hole in\x01",
            "his bag at some point. He started freaking\x01",
            "out pretty hard about it, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x103,
        "#0203FThat certainly sounds like him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I only saw it from a distance, so I have\x01",
            "no clue what he actually lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FThat's too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, hold on... One of my customers mentioned\x01",
            "finding something on the ground earlier today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She hangs out in the park around here pretty\x01",
            "often, so it shouldn't be hard to find her.\x01",
            "Why not try asking her for more details?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x2, 0x1, 0x3)
    TalkEnd(0xFE)
    Return()

    label("loc_2BEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CC7")

    ChrTalk(
        0xFE,
        (
            "One of my customers mentioned finding\x01",
            "something on the ground earlier today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's usually in the area. Might be worth\x01",
            "talking to her if you're looking for something\x01",
            "you lost.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_2CC7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_466E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D22")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2D22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D42")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4669")

    label("loc_2D42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D56")
    Jump("loc_4669")

    label("loc_2D56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4669")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3056")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D8B")
    Call(0, 14)
    Jump("loc_3051")

    label("loc_2D8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2ECF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2E25")

    ChrTalk(
        0xFE,
        "This is clearly a man of culture.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mustn't disappoint him. This batch will\x01",
            "bring him to the brink of noodle ecstasy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ECA")

    label("loc_2E25")


    ChrTalk(
        0xFE,
        (
            "This customer desires the finest firm\x01",
            "noodles in all the land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hah, leave it to me. I shall enlighten him and\x01",
            "bring him to the threshold of the noodle.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2ECA")

    Jump("loc_3051")

    label("loc_2ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2F4F")

    ChrTalk(
        0xFE,
        (
            "Isn't she that reporter with the Crossbell Times?\x01",
            "What's she doing out here? An investigation,\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3051")

    label("loc_2F4F")


    ChrTalk(
        0xFE,
        (
            "Some CNS journalists have been interviewing\x01",
            "people to try and get some information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They kept bugging me for one, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something about if I had any family or\x01",
            "friends that had been acting strange lately.\x01",
            "I dunno what the hell they're after.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3051")

    Jump("loc_4669")

    label("loc_3056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_31D4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3072")
    Call(0, 14)
    Jump("loc_31CF")

    label("loc_3072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_30FB")

    ChrTalk(
        0xFE,
        (
            "I gotta hand it to those guys from the trading\x01",
            "company; they've got nerves of steel.\x01",
            "They didn't budge a single rege.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31CF")

    label("loc_30FB")


    ChrTalk(
        0xFE,
        (
            "That trading company was raided the other day,\x01",
            "and yet they haven't said a single peep about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They don't seem to be fazed by the\x01",
            "bullet holes all over the walls.\x01",
            "Talk about total nerves of steel.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_31CF")

    Jump("loc_4669")

    label("loc_31D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_339A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31F0")
    Call(0, 14)
    Jump("loc_3395")

    label("loc_31F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_327A")

    ChrTalk(
        0xFE,
        (
            "If they think that I'm going to close down my\x01",
            "stall over something that little, then they've\x01",
            "got another thing coming.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3395")

    label("loc_327A")


    ChrTalk(
        0xFE,
        (
            "Something big happened last night.\x01",
            "The police have been freaking out\x01",
            "over it all morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What do I plan to do? Not close\x01",
            "my shop, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not so weak that I'd turn tail and run\x01",
            "from something so insignificant. The path\x01",
            "of the noodle waits for no man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3395")

    Jump("loc_4669")

    label("loc_339A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3557")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B6")
    Call(0, 14)
    Jump("loc_3552")

    label("loc_33B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3467")

    ChrTalk(
        0xFE,
        (
            "Just exactly how is sitting at a desk all day\x01",
            "writing documents supposed to be fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whatever boils their noodle.\x01",
            "I'll never understand it, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3552")

    label("loc_3467")


    ChrTalk(
        0xFE,
        (
            "My customers have been in an oddly\x01",
            "good mood, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somethin' about their company's work\x01",
            "progressing smoothly. Apparently, it's\x01",
            "rewarding to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whatever boils their noodle.\x01",
            "I'll never understand it, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3552")

    Jump("loc_4669")

    label("loc_3557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3707")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_35F1")

    ChrTalk(
        0xFE,
        (
            "That pronunciation... Eh, whatever.\x01",
            "But, I'll thank you to stop calling\x01",
            "it weird.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Stalls like these are common out East.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3702")

    label("loc_35F1")

    OP_63(0x153, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        "#1110FHeeey, is this a store? It looks so weird!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whaddaya mean it's weird?! It's\x01",
            "Eastern-style. Get it right!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1107FEast-urn style!\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "You're a little off there, kiddo.\x01",
            "Well, whatever. Close enough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3702")

    Jump("loc_4669")

    label("loc_3707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_385B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_376A")

    ChrTalk(
        0xFE,
        (
            "The world is vast... I must rededicate\x01",
            "my body and soul to the noodle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3856")

    label("loc_376A")


    ChrTalk(
        0xFE,
        (
            "I checked out the restaurant on East\x01",
            "Street the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The owner showed real finesse.\x01",
            "I had the pleasure of eating noodles\x01",
            "that were as good as my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmm... Wait. Doesn't that mean\x01",
            "that I require more training?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3856")

    Jump("loc_4669")

    label("loc_385B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3937")

    ChrTalk(
        0xFE,
        (
            "Did you know you can open up a food stall\x01",
            "in Crossbell by submitting an application to\x01",
            "the Business Owners' Association?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I connect with those guys way better than\x01",
            "those government snobs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A3E")

    label("loc_3937")


    ChrTalk(
        0xFE,
        (
            "Not much longer until the Anniversary\x01",
            "Festival comes knocking on our doors.\x01",
            "I'd better register my stall soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Crossbell Business Owners' Association\x01",
            "oversees any and all food stalls in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They understand us, and they're pretty fair.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3A3E")

    Jump("loc_4669")

    label("loc_3A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3D05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3B2E")

    ChrTalk(
        0xFE,
        (
            "I used to have this duo of bright, young\x01",
            "police officers come here pretty often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They used to prattle on about the future of\x01",
            "the CPD while slurping down my noodles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002F(Is he talking about...?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D00")

    label("loc_3B2E")


    ChrTalk(
        0xFE,
        (
            "I'm honored to have set so many regular\x01",
            "customers on the path of the noodle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There used to be a duo of bright, young\x01",
            "police officers amongst them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One of 'em was tall and composed, and the\x01",
            "other was a brown-haired lad filled with passion.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "Y'know, you remind me of the brown-haired\x01",
            "one an awful lot.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FWhat? Are you talking about me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, you. You even give off the same vibe\x01",
            "as each other.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 0)
    SetScenarioFlags(0x0, 3)

    label("loc_3D00")

    Jump("loc_4669")

    label("loc_3D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3EE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3DCC")

    ChrTalk(
        0xFE,
        (
            "I am always looking to further perfect\x01",
            "and hone my noodle craft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Give me your honest feedback on them after a taste.\x01",
            "My resolve is as firm as the noodles themselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EE1")

    label("loc_3DCC")


    ChrTalk(
        0xFE,
        "Today's noodles will defy your expectations!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're plump, but they've got good elasticity\x01",
            "and swim through the broth nicely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Made 'em with some water I gathered from\x01",
            "Mainz Mountain Path, I did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys should sit down and enjoy\x01",
            "my nice, firm noodles.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3EE1")

    Jump("loc_4669")

    label("loc_3EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4089")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3F95")

    ChrTalk(
        0xFE,
        "Hey, it ain't my job to listen to your complaints.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps you'd be happier at a job you love.\x01",
            "That's why I've devoted my life to the noodle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4084")

    label("loc_3F95")


    ChrTalk(
        0xFE,
        "Being a businessman seems pretty tiring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lotta customers eat on the way home from\x01",
            "work, and all of them moan and complain\x01",
            "in the exact same way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you want someone to cry to, go to a bar.\x01",
            "I'm here to serve noodles, pal.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4084")

    Jump("loc_4669")

    label("loc_4089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4267")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4139")

    ChrTalk(
        0xFE,
        (
            "Hmph. My standards for noodles are as\x01",
            "high as the IBC's stock prices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Try as they might, no other stall will ever\x01",
            "come CLOSE to these noodles.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4262")

    label("loc_4139")


    ChrTalk(
        0xFE,
        (
            "Judge my noodles not by the stall they're\x01",
            "served from, but by their quality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wake up at the crack of dawn to prepare\x01",
            "the noodles and let 'em rest. Once they're\x01",
            "ready, I bring them here and boil 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No other stall could hope to compare to\x01",
            "the mastery carried by THESE noodles!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4262")

    Jump("loc_4669")

    label("loc_4267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_43EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_42AA")

    ChrTalk(
        0xFE,
        "So, don't be frugal... Try my noodles.\x02",
    )

    CloseMessageWindow()
    Jump("loc_43E9")

    label("loc_42AA")


    ChrTalk(
        0xFE,
        (
            "I abandoned my grandfather's store\x01",
            "to walk the path of the noodle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had no choice if I wanted to fulfill my destiny\x01",
            "of reaching true noodle enlightenment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I am ever to accomplish that, I must continue\x01",
            "to broaden my noodle horizons. So, please...\x01",
            "Join me on this journey...and eat my damn noodles.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_43E9")

    Jump("loc_4669")

    label("loc_43EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4561")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_44AF")

    ChrTalk(
        0xFE,
        (
            "I always see those thugs from the Downtown\x01",
            "District pop up around these parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They just shovel my noodles into their mouths\x01",
            "without savoring 'em. Disgraceful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_455C")

    label("loc_44AF")


    ChrTalk(
        0xFE,
        (
            "I always see those thugs from the Downtown\x01",
            "District pop up around these parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All they ever do is cause a ruckus\x01",
            "late at night. Kind of a pain, if you\x01",
            "ask me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_455C")

    Jump("loc_4669")

    label("loc_4561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_45C7")

    ChrTalk(
        0xFE,
        (
            "My noodles are the mightiest in all the land.\x01",
            "Just one bite and you'll understand!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4669")

    label("loc_45C7")


    ChrTalk(
        0xFE,
        "Noodles must be firm, or else I'll make you squirm!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Your mind will be absolutely blown!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you just gonna stand there,\x01",
            "or will you eat a bowl?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4669")

    Jump("loc_2CD1")

    label("loc_466E")

    TalkEnd(0xFE)
    Return()

    # Function_13_2810 end

    def Function_14_4672(): pass

    label("Function_14_4672")


    ChrTalk(
        0xFE,
        (
            "I've been brainstorming a new flavor,\x01",
            "so I tried emulating Long Lao's\x01",
            "stir fry, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep. There are no shortcuts on the path of the noodle.\x01",
            "You guys can have the recipe, if you want.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x191),
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
            scpstr(SCPSTR_CODE_ITEM, 0x191),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x1)
    Return()

    # Function_14_4672 end

    def Function_15_47B4(): pass

    label("Function_15_47B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_497D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4877")

    ChrTalk(
        0xFE,
        (
            "The IBC has some of the strongest security\x01",
            "in all of Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet it costs a fortune to hire them...\x01",
            "Wouldn't be surprised if they were\x01",
            "better than the CPD.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4978")

    label("loc_4877")


    ChrTalk(
        0xFE,
        (
            "Doesn't the IBC have an amazing\x01",
            "security department?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've even got an orbal detector to scan\x01",
            "all the mail they receive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only are the guards skilled, but they're even\x01",
            "friendly! They're truly on a different level from\x01",
            "the rest of us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_4978")

    Jump("loc_51A9")

    label("loc_497D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4A09")

    ChrTalk(
        0xFE,
        (
            "The flight carrying the cargo has yet\x01",
            "to arrive...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A bit weird for it to run late...\x01",
            "I hope everything's all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A9")

    label("loc_4A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4A66")

    ChrTalk(
        0xFE,
        "What's with all the police cars today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You think something happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_51A9")

    label("loc_4A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4BD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4AE2")

    ChrTalk(
        0xFE,
        (
            "As you can see, Crossbell will continue\x01",
            "to grow and grow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...as will my workload, sadly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BD4")

    label("loc_4AE2")


    ChrTalk(
        0xFE,
        (
            "Many businesses have been thriving ever\x01",
            "since the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People thought it'd be a good idea to try\x01",
            "and take advantage of the wave to expand\x01",
            "their businesses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Too bad my workload is about to\x01",
            "grow again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_4BD4")

    Jump("loc_51A9")

    label("loc_4BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4C53")

    ChrTalk(
        0xFE,
        "Darn! I forgot the IBC was on holiday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Argh! I brought all of these packages\x01",
            "with me for nothing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A9")

    label("loc_4C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4DD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4D12")

    ChrTalk(
        0xFE,
        (
            "They've been laying the groundwork for\x01",
            "the orbal net or whatever. I think these\x01",
            "are parts they need for the project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I should probably handle them with care.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DD3")

    label("loc_4D12")


    ChrTalk(
        0xFE,
        (
            "I've been dealing with a lot more packages\x01",
            "that have 'fragile' written on 'em, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think they're quartz or something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Either way, I'd better handle them more carefully.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_4DD3")

    Jump("loc_51A9")

    label("loc_4DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4E50")

    ChrTalk(
        0xFE,
        (
            "I get decent tips from some of the companies\x01",
            "I deliver to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Boy, I sure love delivering to them.\x02",
    )

    CloseMessageWindow()
    Jump("loc_51A9")

    label("loc_4E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4E91")

    ChrTalk(
        0xFE,
        (
            "I wish my company'd buy me an\x01",
            "orbal car, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A9")

    label("loc_4E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4F56")

    ChrTalk(
        0xFE,
        (
            "I had to cancel my vacation a little while ago.\x01",
            "My plans got canned when I had a bunch of\x01",
            "work thrown at me out of nowhere!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Working in the service industry sure is painful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_51A9")

    label("loc_4F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4FD5")

    ChrTalk(
        0xFE,
        (
            "I've got my sights set on enjoying Mishelam\x01",
            "for my next vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't wait for the day it happens.\x02",
    )

    CloseMessageWindow()
    Jump("loc_51A9")

    label("loc_4FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5063")

    ChrTalk(
        0xFE,
        "Huh? Where's this place supposed to be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The addresses for these newly constructed\x01",
            "buildings make absolutely no sense.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A9")

    label("loc_5063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_50E6")

    ChrTalk(
        0xFE,
        (
            "You're telling me a fight broke out\x01",
            "in the Downtown District?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Scary stuff. I'd better watch my back there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_51A9")

    label("loc_50E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_515A")

    ChrTalk(
        0xFE,
        (
            "I can't deal with this area. All these businesses\x01",
            "means I'm at the mercy of a thousand packages.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A9")

    label("loc_515A")


    ChrTalk(
        0xFE,
        "*sigh* Okay, the next destination is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey, you! Get outta the way!\x02",
    )

    CloseMessageWindow()

    label("loc_51A9")

    TalkEnd(0xFE)
    Return()

    # Function_15_47B4 end

    def Function_16_51AD(): pass

    label("Function_16_51AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5299")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_522A")

    ChrTalk(
        0xFE,
        (
            "My granddaughter has been worried\x01",
            "about my well-being...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I may be acting too stubborn...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5294")

    label("loc_522A")


    ChrTalk(
        0xFE,
        "My granddaughter's a good kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She hasn't given an old man like me much\x01",
            "reason to worry her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_5294")

    Jump("loc_5F73")

    label("loc_5299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_53B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_530F")

    ChrTalk(
        0xFE,
        "She said she'd keep me company today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is it because she's worried about my health?\x02",
    )

    CloseMessageWindow()
    Jump("loc_53B1")

    label("loc_530F")


    ChrTalk(
        0xFE,
        "I tried to get her to go home, but she refused.\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "There was a shooting here yesterday, so\x01",
            "it's no place for children to be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_53B1")

    Jump("loc_5F73")

    label("loc_53B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5480")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        "Almighty Aidios, what an unsettling predicament.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd better send my granddaughter\x01",
            "back home today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'd kill me to get her caught up in\x01",
            "a dangerous situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    Jump("loc_5F73")

    label("loc_5480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_555E")

    ChrTalk(
        0xFE,
        (
            "My body is alive and kicking. I don't need to\x01",
            "take no stinking medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gimme a fishing rod paired with a quiet spot,\x01",
            "and I'm good to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is how I've decided to spend my\x01",
            "remaining years.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F73")

    label("loc_555E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_55F7")

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival spoiled any chance\x01",
            "I had to fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I couldn't get in any time while everyone else\x01",
            "was out being festive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F73")

    label("loc_55F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_56D0")

    ChrTalk(
        0xFE,
        (
            "I understand where my granddaughter's\x01",
            "coming from...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know she's a good kid with the right\x01",
            "intentions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, still. This old coot doesn't have many\x01",
            "years left. Just let me do as I please!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F73")

    label("loc_56D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_572C")

    ChrTalk(
        0xFE,
        "My granddaughter came to visit me today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sorry, but I'm busy today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F73")

    label("loc_572C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_57CE")

    ChrTalk(
        0xFE,
        "Fishing is the only thing I look forward to...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to spend the whole day fishing,\x01",
            "so you whippersnappers better not get\x01",
            "in my way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F73")

    label("loc_57CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_58A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_57FE")

    ChrTalk(
        0xFE,
        "Heh. I hate crowds.\x02",
    )

    CloseMessageWindow()
    Jump("loc_58A2")

    label("loc_57FE")


    ChrTalk(
        0xFE,
        (
            "Those whelps from the Fisherman's Guild\x01",
            "tried to get me to join their little group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Heh, I hate crowds.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What's 'pleasant fishing' supposed to be?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_58A2")

    Jump("loc_5F73")

    label("loc_58A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_594F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5947")

    ChrTalk(
        0xFE,
        (
            "I've decided to spend the rest of my life\x01",
            "focusing on fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel bad for my granddaughter, but I\x01",
            "don't need any medicine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_594A")

    label("loc_5947")

    Call(0, 18)

    label("loc_594A")

    Jump("loc_5F73")

    label("loc_594F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5A29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_599A")

    ChrTalk(
        0xFE,
        (
            "Damn it! How am I supposed to fish\x01",
            "like this?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A24")

    label("loc_599A")


    ChrTalk(
        0xFE,
        "So it's that damn cruise ship, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm getting right pissed off. The blasted thing\x01",
            "is getting in the way of my fishing...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_5A24")

    Jump("loc_5F73")

    label("loc_5A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5CAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5B3C")

    ChrTalk(
        0xFE,
        (
            "The most skilled detectives are all a part\x01",
            "of the First Investigative Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was a detective I met a few years ago\x01",
            "with a knack for it, despite being young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You've gotta be at least as capable as he was\x01",
            "if you want my approval.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CA9")

    label("loc_5B3C")


    ChrTalk(
        0xFE,
        "The state government is filled with dirty dogs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And don't even get me started on the police...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They don't bother seeing investigations through\x01",
            "to the end, and they're constantly bailing out\x01",
            "criminals due to political pressure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The whole lot of them are worthless.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Admittedly, the First Investigative Division\x01",
            "isn't completely worthless.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_5CA9")

    Jump("loc_5F73")

    label("loc_5CAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5EAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5D1D")

    ChrTalk(
        0xFE,
        "I can't stand the people in this city.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I could puke just thinking about them.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EA5")

    label("loc_5D1D")


    ChrTalk(
        0xFE,
        "I can't stand most of the people in this city.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone's always thinking about how to make money.\x01",
            "They don't care for rules or tradition anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not to mention, they get swept up in every\x01",
            "new fad and all their brainless gossip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You think they'd behave themselves at a\x01",
            "festival? Think again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though, who am I to judge? All I'm doing is\x01",
            "standing here complaining.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_5EA5")

    Jump("loc_5F73")

    label("loc_5EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5EEB")

    ChrTalk(
        0xFE,
        "(*grumble* You're all a bunch of failures...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F73")

    label("loc_5EEB")


    ChrTalk(
        0xFE,
        (
            "Whaddaya want, you whippersnapper?\x01",
            "Are you here to waste my time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Leave already! You're scaring the fish away!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    SetChrFlags(0xB, 0x10)
    OP_93(0xB, 0xB4, 0x0)

    label("loc_5F73")

    TalkEnd(0xFE)
    Return()

    # Function_16_51AD end

    def Function_17_5F77(): pass

    label("Function_17_5F77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_60DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6005")

    ChrTalk(
        0xFE,
        "I guess I'll leave Grandpa alone for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He does look healthy, so I won't bother\x01",
            "him about his medicine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60D7")

    label("loc_6005")


    ChrTalk(
        0xFE,
        (
            "I think I'll leave Grandpa alone for\x01",
            "the rest of the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just wanted him to go to the hospital\x01",
            "and take his medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've tried everything, but he always\x01",
            "ignores me and insists he's fine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_60D7")

    Jump("loc_65EA")

    label("loc_60DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_61D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6126")

    ChrTalk(
        0xFE,
        (
            "I hope Grandpa catches all of the\x01",
            "fish today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61CC")

    label("loc_6126")


    ChrTalk(
        0xFE,
        "I'm hanging out with Grandpa today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get worried thinking about an old man\x01",
            "like him being on his own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's okay, though. I like watching him fish.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_61CC")

    Jump("loc_65EA")

    label("loc_61D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_61F8")

    ChrTalk(
        0xFE,
        "Hmm? What happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_65EA")

    label("loc_61F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6295")

    ChrTalk(
        0xFE,
        (
            "Here, Grandpa. I brought you your\x01",
            "medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Will you please take it? For me?\x01",
            "You need to listen to what the\x01",
            "doctor tells you, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65EA")

    label("loc_6295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6364")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_62DF")

    ChrTalk(
        0xFE,
        "I hope I can go to it with Grandpa next year.\x02",
    )

    CloseMessageWindow()
    Jump("loc_635F")

    label("loc_62DF")


    ChrTalk(
        0xFE,
        "*sigh* The Anniversary Festival is over...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I ended up missing all of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wanted to spend it with Grandpa...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_635F")

    Jump("loc_65EA")

    label("loc_6364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_63AA")

    ChrTalk(
        0xFE,
        "*sigh* I wish he'd let me help him out...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6460")

    label("loc_63AA")


    ChrTalk(
        0xFE,
        (
            "My grandpa was in the hospital\x01",
            "until last year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He ran away, though. He doesn't\x01",
            "like hospitals too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I know how he feels,\x01",
            "but this isn't good for him...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_6460")

    Jump("loc_65EA")

    label("loc_6465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6569")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6506")

    ChrTalk(
        0xFE,
        (
            "Grandpa always looks really mad\x01",
            "when he's fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* He doesn't take his medicine, either.\x01",
            "What am I going to do with him?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6564")

    label("loc_6506")


    ChrTalk(
        0xFE,
        (
            "Hey, Grandpa. Why don't we go to\x01",
            "East Street together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "C'mon! Play with me!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xC, 0x10)

    label("loc_6564")

    Jump("loc_65EA")

    label("loc_6569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_65E7")

    ChrTalk(
        0xFE,
        "Grandpa is sooooo stubborn.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only that, but he hates hospitals...\x01",
            "*sigh* What am I supposed to do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65EA")

    label("loc_65E7")

    Call(0, 18)

    label("loc_65EA")

    TalkEnd(0xFE)
    Return()

    # Function_17_5F77 end

    def Function_18_65EE(): pass

    label("Function_18_65EE")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xC,
        "I'm here to give you your medicine, Grandpa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hey... You'll take it every day, won't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Quit nagging me, girlie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I don't need any medicine, so get\x01",
            "the heck outta here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Come on, Grandpa! You can't just\x01",
            "keep acting like a broken record!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xC, 0x10)
    Return()

    # Function_18_65EE end

    def Function_19_670C(): pass

    label("Function_19_670C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67DF")

    ChrTalk(
        0xFE,
        "Oh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where are you headed off to at\x01",
            "a time like this, Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being a police officer must be difficult.\x01",
            "Take good care of yourself, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FThank you. I will be sure to.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6828")

    label("loc_67DF")


    ChrTalk(
        0xFE,
        "Being a police officer must be difficult.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Take care, everyone!\x02",
    )

    CloseMessageWindow()

    label("loc_6828")

    TalkEnd(0xFE)
    Return()

    # Function_19_670C end

    def Function_20_682C(): pass

    label("Function_20_682C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_69B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_68AB")

    ChrTalk(
        0xFE,
        (
            "Grace has been fixated on this weird\x01",
            "rumor since morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is there really something to it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_69AD")

    label("loc_68AB")


    ChrTalk(
        0xFE,
        (
            "A strange rumor has been going around since morning.\x01",
            "Apparently, a bunch of people have gone missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're trying to investigate it right now,\x01",
            "but I'm not so sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Would this really make for a good article?\x01",
            "I guess it IS a little weird...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_69AD")

    Jump("loc_6B8A")

    label("loc_69B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_6A48")

    ChrTalk(
        0xFE,
        (
            "Man, I just wanna go home already.\x01",
            "I can't leave Grace behind like that, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ughhhh... What the heck am I supposed to do?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B8A")

    label("loc_6A48")


    ChrTalk(
        0xFE,
        "Ahhh... What do I do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Grace ditched me to go straight to the\x01",
            "source for information!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FW-Wait, seriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0205FHas she gone into Heiyue's office?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*nod*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cut me some slack, Grace...\x01",
            "I'm fallin' behind here!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    SetScenarioFlags(0xD0, 3)

    label("loc_6B8A")

    TalkEnd(0xFE)
    Return()

    # Function_20_682C end

    def Function_21_6B8E(): pass

    label("Function_21_6B8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 4)), scpexpr(EXPR_END)), "loc_6D38")

    ChrTalk(
        0x1A,
        (
            "#2103FBoth Revache's shenanigans and\x01",
            "missing people, eh?\x02\x03",
            "Yep. I'd say we've gotten ourselves into\x01",
            "quite the pickle.\x02\x03",
            "#2101FYou guys better watch your backs if you\x01",
            "plan on continuing the investigation.\x02\x03",
            "#2109FI can't have you dying on me when\x01",
            "my next big scoop hinges on your\x01",
            "success!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D33")

    ChrTalk(
        0x101,
        "#0002FHaha... Sure, we'll be more vigilant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FYou'd do well to heed your own\x01",
            "advice, Grace.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_6D33")

    Jump("loc_71D8")

    label("loc_6D38")


    ChrTalk(
        0x1A,
        (
            "#2105FWell, if it isn't my best friends.\x02\x03",
            "#2101FI overheard just the craziest thing...\x01",
            "Has the entire mafia seriously gone missing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FHow were you able to get your hands on\x01",
            "classified information like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#2103FImagine thinking us reporters don't have\x01",
            "access to our own information networks.\x02\x03",
            "But anyway! I heard Gantz went missing\x01",
            "after that big kerfuffle yesterday.\x02\x03",
            "#2101FNot only that, but more and more people\x01",
            "are suddenly vanishing into thin air.\x02\x03",
            "I dunno about you guys, but I've got a real\x01",
            "bad feeling about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0013FYeah, I'm pretty worried...\x01",
            "We'd better get a handle on what's going on,\x01",
            "and fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#2104FOh, so you guys ARE chasing them down?\x01",
            "Good to know!\x01",
            "*scritch scratch*\x02\x03",
            "#2110FOkay. I think I've got the gist of it. You'd better\x01",
            "hit me up with those juicy details if anything\x01",
            "else happens!\x02",
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
        0x103,
        (
            "#0211FYou may have divulged too much information,\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FYou don't need to tell me twice. I feel\x01",
            "like such an amateur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FYou screwed the pooch, but there's no\x01",
            "use in beatin' yourself up about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 4)

    label("loc_71D8")

    TalkEnd(0xFE)
    Return()

    # Function_21_6B8E end

    def Function_22_71DC(): pass

    label("Function_22_71DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_751C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74E0")
    OP_4B(0x1D, 0xFF)
    OP_4B(0x1E, 0xFF)

    ChrTalk(
        0x1D,
        (
            "H-Hey, Pearl. I haven't seen you in\x01",
            "a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "You're right. You haven't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I thought you had completely forgotten\x01",
            "about your dear wife-to-be.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x1D,
        (
            "O-Of course not! It's only because the\x01",
            "Bracer Guild has been working us like\x01",
            "a bunch of slaves lately!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Haha. I know, dear. I'm just toying with you. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I understand far better than anyone else the\x01",
            "hard work you put into being a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "Oh, my sweet Pearl! ㈱\x02",
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(20)
    OP_63(0x1E, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        "#1109FAww, they're so cute!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x153, 500)
    TurnDirection(0x1E, 0x153, 500)
    OP_63(0x1D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#0006F(K-KeA! Don't just butt into their conversation\x01",
            "like that!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "P-Pardon me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "H-Haha...\x02",
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x5A, 0x0)
    OP_93(0x1E, 0x10E, 0x0)
    OP_4C(0x1D, 0xFF)
    OP_4C(0x1E, 0xFF)
    SetScenarioFlags(0x1, 3)
    Jump("loc_751C")

    label("loc_74E0")


    ChrTalk(
        0xFE,
        (
            "How about we get back on track\x01",
            "and grab a bite to eat?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_751C")

    TalkEnd(0xFE)
    Return()

    # Function_22_71DC end

    def Function_23_7520(): pass

    label("Function_23_7520")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_758A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_753E")
    Call(0, 22)
    Jump("loc_758A")

    label("loc_753E")


    ChrTalk(
        0xFE,
        "Sounds like a plan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We might as well go for a little stroll, too.\x02",
    )

    CloseMessageWindow()

    label("loc_758A")

    TalkEnd(0xFE)
    Return()

    # Function_23_7520 end

    def Function_24_758E(): pass

    label("Function_24_758E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7622")
    Jump("loc_766C")

    label("loc_7622")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7642")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_766C")

    label("loc_7642")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7662")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_766C")

    label("loc_7662")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_766C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7725")

    ChrTalk(
        0xFE,
        "Oh, my. This dish is wonderful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, these flavors take me back. I got it from\x01",
            "that stall over there, if you're interested.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77C1")

    label("loc_7725")


    ChrTalk(
        0xFE,
        (
            "I'm glad we managed to find this park.\x01",
            "My feet are killing me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This place is massive. Bringing a child here\x01",
            "was just asking to get worn out fast.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77C1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_758E end

    def Function_25_77C9(): pass

    label("Function_25_77C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_77FF")

    ChrTalk(
        0xFE,
        "These soba noodles are amazing!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7851")

    label("loc_77FF")


    ChrTalk(
        0xFE,
        "I'm tired from walking around all day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I could go for some ice cream...\x02",
    )

    CloseMessageWindow()

    label("loc_7851")

    TalkEnd(0xFE)
    Return()

    # Function_25_77C9 end

    def Function_26_7855(): pass

    label("Function_26_7855")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_790A")

    ChrTalk(
        0xFE,
        (
            "I missed the ship 'cause I was too busy\x01",
            "eating my lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The next one's coming sooner than I thought.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe I didn't really need to hurry after all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_79CD")

    label("loc_790A")


    ChrTalk(
        0xFE,
        (
            "Oh, so this is where you board the\x01",
            "cruise ship to Mishelam?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been looking forward to this trip for\x01",
            "a while. I plan to hit up every one of those\x01",
            "fancy shops I've been hearing about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79CD")

    TalkEnd(0xFE)
    Return()

    # Function_26_7855 end

    def Function_27_79D1(): pass

    label("Function_27_79D1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I'm taking my daughter to Mishelam.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll be our first time riding on one of these\x01",
            "cruise ships, so we're pretty excited!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_79D1 end

    def Function_28_7A5C(): pass

    label("Function_28_7A5C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Whoaaa, this boat is huge!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've never been on a boat before!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_7A5C end

    def Function_29_7AAA(): pass

    label("Function_29_7AAA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I heard there are plenty of ways for anyone\x01",
            "to enjoy themselves at Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehehe... I'm looking forward to having\x01",
            "a bit of fun.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_7AAA end

    def Function_30_7B3E(): pass

    label("Function_30_7B3E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "(Psst... Revache is definitely responsible\x01",
            "for this mess.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "(This is why I'm so scared of the mafia...)\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_7B3E end

    def Function_31_7BB6(): pass

    label("Function_31_7BB6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Heiyue Trading...?\x01",
            "Never heard of 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did they do something to anger the mafia?\x01",
            "I hope nothing bad happens.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_7BB6 end

    def Function_32_7C34(): pass

    label("Function_32_7C34")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D0B")

    ChrTalk(
        0xFE,
        "The occasional dispute isn't particularly rare.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, this is the first time we've experienced\x01",
            "a company being the victim of a violent attack.\x01",
            "The whole situation's been an eye-opener.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_7D95")

    label("loc_7D0B")


    ChrTalk(
        0xFE,
        "And you wanna know what the police did?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Diddly squat. I bet you'd be able to detonate a\x01",
            "building, and they STILL wouldn't care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D95")

    TalkEnd(0xFE)
    Return()

    # Function_32_7C34 end

    def Function_33_7D99(): pass

    label("Function_33_7D99")

    TalkBegin(0xFE)
    OP_4B(0x17, 0xFF)

    ChrTalk(
        0xFE,
        "Wow, look at all of the holes!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0xFE, 500)
    Sleep(300)

    ChrTalk(
        0x17,
        "Shh! Be quiet and stay away!\x02",
    )

    CloseMessageWindow()
    OP_93(0x17, 0x2D, 0x0)
    OP_4C(0x17, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_33_7D99 end

    def Function_34_7DFF(): pass

    label("Function_34_7DFF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I like coming to the park to relax and unwind,\x01",
            "yet that somehow gets taken away from me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What the hell are the police good for?!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_7DFF end

    def Function_35_7E93(): pass

    label("Function_35_7E93")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Is there something I can help you with?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FNo, not particularly.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 3)), scpexpr(EXPR_END)), "loc_7F23")

    ChrTalk(
        0x102,
        "#0106F(Looks like even Grace is hard at work...)\x02",
    )

    CloseMessageWindow()

    label("loc_7F23")

    TalkEnd(0xFE)
    Return()

    # Function_35_7E93 end

    def Function_36_7F27(): pass

    label("Function_36_7F27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7FB7")

    ChrTalk(
        0xFE,
        (
            "We ask for the patience of any passengers\x01",
            "traveling to Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The ship will depart in approximately\x01",
            "five minutes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81D8")

    label("loc_7FB7")


    ChrTalk(
        0xFE,
        (
            "We ask for the patience of any passengers\x01",
            "traveling to Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The ship will depart in approximately\x01",
            "five minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FThis thing takes you to the famed Mishelam?\x01",
            "It's bigger than I was expecting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FMishelam is pretty sweet, my friend.\x01",
            "They've got an theme park and a bunch of\x01",
            "shops and fun places to chill out.\x02\x03",
            "#0305FYou ever been, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FNope, can't say I have. They built the\x01",
            "place while I was living abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FAt any rate, we don't have time to sit here\x01",
            "conversing about Mishelam all day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_81D8")

    TalkEnd(0xFE)
    Return()

    # Function_36_7F27 end

    def Function_37_81DC(): pass

    label("Function_37_81DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_END)), "loc_848D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_827C")

    ChrTalk(
        0xFE,
        (
            "Dudley and Emma were staring\x01",
            "daggers at me earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm tired of guarding this place. Those\x01",
            "Heiyue guys give me the creeps.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8488")

    label("loc_827C")


    ChrTalk(
        0xFE,
        (
            "*sigh* Heiyue's members have been\x01",
            "coming in and out of the place all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh... I guess they would be employees\x01",
            "rather than members, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They left for now, but it's only a matter of\x01",
            "time before they're back again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FSorry you're dealing with this, Franz.\x01",
            "We're counting on you to watch the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FI suspect they will not launch an assault\x01",
            "on you, so you will be fine.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Well, you're probably right... But, still.\x01",
            "I can hardly relax in this situation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)

    label("loc_8488")

    Jump("loc_8574")

    label("loc_848D")


    ChrTalk(
        0xFE,
        (
            "Who the heck's crazy enough to open\x01",
            "fire during the dead of night in a place\x01",
            "like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, make sure you come up\x01",
            "with an excuse or something for Dudley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to end up with him\x01",
            "keeping an eye on me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8574")

    TalkEnd(0xFE)
    Return()

    # Function_37_81DC end

    def Function_38_8578(): pass

    label("Function_38_8578")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_85C8")

    ChrTalk(
        0xFE,
        (
            "I swear I'm gonna get a big role this time!\x01",
            "*huff* *puff*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8905")

    label("loc_85C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_86B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_865D")

    ChrTalk(
        0xFE,
        "S-Selene's here, too?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess none of us can take things easy\x01",
            "with casting announcements being made\x01",
            "next week.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_86B2")

    label("loc_865D")


    ChrTalk(
        0xFE,
        (
            "Oh, man. Only one more week until the\x01",
            "announcement... The stress is killin' me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86B2")

    Jump("loc_8905")

    label("loc_86B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_879F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_875B")

    ChrTalk(
        0xFE,
        "I work up a mean appetite after my morning run.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The annoying part is that I'll lose jumping\x01",
            "power if I start gaining weight...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_879A")

    label("loc_875B")


    ChrTalk(
        0xFE,
        (
            "*sigh* Guess I've got no choice but to\x01",
            "train even harder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_879A")

    Jump("loc_8905")

    label("loc_879F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_885B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_883B")

    ChrTalk(
        0xFE,
        "*huff* *puff*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Need to resist the temptation to eat\x01",
            "at that new stall that opened up around\x01",
            "here. The menu looks great.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_8856")

    label("loc_883B")


    ChrTalk(
        0xFE,
        "I'm soooooo hungry...\x02",
    )

    CloseMessageWindow()

    label("loc_8856")

    Jump("loc_8905")

    label("loc_885B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_8905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88C9")

    ChrTalk(
        0xFE,
        "*huff* *puff*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*pant* *pant*\x01",
            "I...should probably work on my conditioning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_8905")

    label("loc_88C9")


    ChrTalk(
        0xFE,
        (
            "Wh-What are you lookin' at?\x01",
            "Don't get in my way, 'kay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8905")

    TalkEnd(0xFE)
    Return()

    # Function_38_8578 end

    def Function_39_8909(): pass

    label("Function_39_8909")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8A56")

    label("loc_8915")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_893F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_8932")
    OP_4C(0x20, 0xFF)
    Jump("loc_8937")

    label("loc_8932")

    Jump("loc_893F")

    label("loc_8937")

    Sleep(200)
    Jump("loc_8915")

    label("loc_893F")

    OP_4B(0x20, 0xFF)
    TurnDirection(0xFE, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89F0")

    ChrTalk(
        0xFE,
        (
            "How am I supposed to sit still when they're\x01",
            "about to announce the cast?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been training non-stop, even on days\x01",
            "we don't have practice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_8A4D")

    label("loc_89F0")


    ChrTalk(
        0xFE,
        "I hope I get casted for a supporting role.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I KNOW I'll get chosen for a good role!\x02",
    )

    CloseMessageWindow()

    label("loc_8A4D")

    OP_4C(0x20, 0xFF)
    Jump("loc_8B48")

    label("loc_8A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8B48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B1A")

    ChrTalk(
        0xFE,
        (
            "Nikolai's running all over the place like\x01",
            "a ball of energy, haha.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm not gonna let him outshine me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And to make matters worse, Rixia is...\x01",
            "...and yet...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_8B48")

    label("loc_8B1A")


    ChrTalk(
        0xFE,
        "Wahh! I'm not gonna lose to her, either!\x02",
    )

    CloseMessageWindow()

    label("loc_8B48")

    TalkEnd(0xFE)
    Return()

    # Function_39_8909 end

    def Function_40_8B4C(): pass

    label("Function_40_8B4C")

    TalkBegin(0xFE)

    NpcTalk(
        0x24,
        "Eastern Man",
        (
            "#5PThe branch manager will see you now.\x01",
            "Please step inside.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_8B4C end

    def Function_41_8BA0(): pass

    label("Function_41_8BA0")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FLook out, Lupinus River.\x01",
            "I'm going to catch some dinner!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(63790, 0, 7940, 1500)
    MoveCamera(45, 23, 0, 1500)
    OP_6E(280, 1500)
    SetCameraDistance(29000, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Try fishing?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C86")
    OP_E0(0x2)
    MiniGame(0x6, 0x1, 0x10BE4, 0xFFFFF63C, 0x4074, 0xB4, 0x109C8, 0xFFFFF254, 0x2E2C)

    label("loc_8C86")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_41_8BA0 end

    def Function_42_8C8B(): pass

    label("Function_42_8C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CA7")
    TalkBegin(0xFF)
    Call(0, 43)
    TalkEnd(0xFF)
    Jump("loc_8DEA")

    label("loc_8CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CBD")
    Call(0, 45)
    Jump("loc_8DEA")

    label("loc_8CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CD9")
    TalkBegin(0xFF)
    Call(0, 43)
    TalkEnd(0xFF)
    Jump("loc_8DEA")

    label("loc_8CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DE1")
    TalkBegin(0xFF)
    Call(0, 43)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DD9")

    ChrTalk(
        0x101,
        (
            "#0001F(Convincing them to let us in again\x01",
            "might be a little tricky.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103F(Indeed. Cao has likely begun to plan\x01",
            "out Heiyue's next move already.)\x02\x03",
            "#0101F(At least we were able to speak to\x01",
            "him in the first place.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_8DD9")

    TalkEnd(0xFF)
    Jump("loc_8DEA")

    label("loc_8DE1")

    TalkBegin(0xFF)
    Call(0, 43)
    TalkEnd(0xFF)

    label("loc_8DEA")

    Return()

    # Function_42_8C8B end

    def Function_43_8DEB(): pass

    label("Function_43_8DEB")

    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A sign is affixed to the locked door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   Heiyue Trading, Ltd. - Crossbell Branch\x01",
            "If you have business with us, please knock.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91EA")

    ChrTalk(
        0x101,
        (
            "#0001FHeiyue Trading...\x02\x03",
            "Is this the place Ian was telling us about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FMust be. Kinda crazy that a place like this\x01",
            "is a Republican mafia's stronghold.\x02\x03",
            "#0306FI gotta say, they did a bang-up job makin'\x01",
            "the place feel like a legit business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FIt's nothing more than a mere facade, though.\x01",
            "One they hope people will be deceived by.\x02\x03",
            "I hate the fact that we still have no clear\x01",
            "idea of how this organization operates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FWe should categorize them the same way we do\x01",
            "Revache. We cannot take action on either group\x01",
            "without taking the proper precautions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FTio's right. As of now, we have no evidence\x01",
            "implicating them in any crimes. We may know\x01",
            "their true nature, but we can't act just yet.\x02\x03",
            "#0003F(I hope we get the opportunity to properly\x01",
            "investigate these guys someday.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91EA")

    SetScenarioFlags(0x94, 0)
    Return()

    # Function_43_8DEB end

    def Function_44_91EE(): pass

    label("Function_44_91EE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(45480, 0, 3700, 0)
    MoveCamera(45, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(29000, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    FadeToBright(1000, 0)
    OP_68(1340, 1800, -380, 10000)
    MoveCamera(45, 24, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(26000, 10000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-7040, 4500, 24940, 0)
    MoveCamera(20, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26000, 0)
    OP_68(-2790, 2500, 5490, 8000)
    MoveCamera(35, 32, 0, 8000)
    OP_6E(600, 8000)
    SetCameraDistance(51580, 8000)
    PlaceName2(340, 200, "c_plac31", 0x0, 4000)
    OP_6F(0x79)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_962C")

    AnonymousTalk(
        0x102,
        (
            "#0104FAh, the Harbor District. It's connected to the\x01",
            "Lupinus River and Lake Elm just south of us.\x02\x03",
            "#0100FThis area is home to many different businesses.\x01",
            "If you look north, you'll see all sorts of\x01",
            "companies lined up next to each other.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#0309FCan't forget about that nice park in the middle,\x01",
            "though. Place is just right for a bit of relaxin'.\x02\x03",
            "#0302FI bet I could take a quick snooze there, easy.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#0203FThe database indicates this area is simply\x01",
            "named the Harbor District. Not exactly a\x01",
            "complex name, is it?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        "#0005FWait, is that...?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-13890, 5100, 25220, 0)
    MoveCamera(0, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26000, 0)
    OP_0D()
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#0000FThe Crossbell Times! I was wondering\x01",
            "where they moved their office to.\x02\x03",
            "#0003F(The city's gone through a lot of changes\x01",
            "these past three years.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_962C")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Harbor District serves as the business district,\x01",
            "and is located in the northeastern part of the city.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The park faces Crossbell's longest river, the\x01",
            "Lupinus River. Citizens and tourists alike visit\x01",
            "this scenic park for relaxation and fun.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's also home to some major businesses,\x01",
            "such as the famed Crossbell News Service.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_982B")
    OP_68(-19600, 2500, -27950, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)

    label("loc_982B")

    SetScenarioFlags(0x45, 2)
    EventEnd(0x5)
    Return()

    # Function_44_91EE end

    def Function_45_9831(): pass

    label("Function_45_9831")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 18600, 0, 17800, 0)
    SetChrPos(0x102, 19700, 0, 17800, 0)
    SetChrPos(0x103, 18600, 0, 16600, 0)
    SetChrPos(0x104, 19700, 0, 16600, 0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9939")
    OP_68(22000, 3700, 20500, 0)
    MoveCamera(24, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    MoveCamera(37, 6, 0, 6000)
    SetCameraDistance(18000, 6000)
    OP_0D()
    PlaceName2(340, 200, "c_plac13", 0x0, 1000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(22000, 1000, 21000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(21500, 0)
    OP_68(22000, 0, 21000, 2000)
    OP_6F(0x1)
    OP_0D()
    Jump("loc_9968")

    label("loc_9939")

    OP_68(22000, 0, 21000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(21500, 0)
    OP_0D()

    label("loc_9968")

    Call(0, 43)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99AD")

    ChrTalk(
        0x101,
        "#2100962V#12P#0001FI think this is the place...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x88, 3)

    label("loc_99AD")

    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#2100963V#11P#0101FHow do we proceed, Lloyd?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Knock\x01",                 # 0
            "Leave Them Alone\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9A37"),
        (1, "loc_9F61"),
        (SWITCH_DEFAULT, "loc_9F87"),
    )


    label("loc_9A37")


    def lambda_9A3C():

        label("loc_9A3C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_9A3C")

    QueueWorkItem2(0x102, 2, lambda_9A3C)

    def lambda_9A4E():
        OP_96(0xFE, 0x4A9C, 0x0, 0x4CF4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A4E)
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x2)
    Sleep(300)
    Sound(811, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#2100964V#11P#0001FExcuse me! Is anybody there?!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    VolumeBGM(0x3C, 0x12C)
    Sound(855, 0, 100, 0)
    Sleep(3000)
    SetChrPos(0x24, 19100, 350, 21500, 180)
    OP_4B(0x24, 0xFF)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)

    NpcTalk(
        0x24,
        "Man's Voice",
        "#2100965V#5P#2SAnd who might you all be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100966V#12P#0003FWe're from the Crossbell Police Department,\x01",
            "Special Support Section.\x02\x03",
            "#2100967V#0001FWe were hoping to ask your branch manager a few\x01",
            "questions regarding a certain incident, if possible.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x24,
        "Man's Voice",
        "#2100968V#5P#2S#40W...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x24,
        "Man's Voice",
        "#2100969V#5P#2SWait here for a moment.\x02",
    )

    CloseMessageWindow()
    Sound(855, 0, 100, 0)
    Sleep(3000)
    VolumeBGM(0x64, 0x12C)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        "#2100970V#0006F#5PAnd now we wait.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100971V#12P#0303FTakin' bets on who's gonna meet us...\x01",
            "A demon or a snake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100972V#6P#0201F#6PI look forward to seeing what awaits\x01",
            "us behind the door.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x24, 0x4)
    SetChrPos(0x24, 19100, 350, 21500, 180)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 18600, 0, 17800, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(809, 0, 100, 0)
    Sleep(500)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)

    def lambda_9DEE():
        OP_95(0xFE, 19100, 0, 19700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_9DEE)

    def lambda_9E08():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_9E08)
    WaitChrThread(0x24, 1)
    WaitChrThread(0x24, 2)
    Sleep(300)

    NpcTalk(
        0x24,
        "Eastern Man",
        "#2100973V#5PI apologize for the wait.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x24,
        "Eastern Man",
        (
            "#2100974V#5PThe branch manager will see you now.\x01",
            "Please step inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x24, 0xE1, 0x190)

    def lambda_9EB8():
        OP_96(0xFE, 0x4DA8, 0x0, 0x4CAE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_9EB8)
    WaitChrThread(0x24, 1)

    ChrTalk(
        0x101,
        "#2100975V#6P#0000FTh-Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100976V#12P#0103FIf you'll excuse us.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 19100, 0, 17200, 0)
    OP_4C(0x24, 0xFF)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x4, 0x2)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x81, 2)
    EventEnd(0x5)
    Jump("loc_9F87")

    label("loc_9F61")

    SetChrPos(0x0, 19100, 0, 17200, 0)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    EventEnd(0x5)
    Jump("loc_9F87")

    label("loc_9F87")

    Return()

    # Function_45_9831 end

    def Function_46_9F88(): pass

    label("Function_46_9F88")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    OP_68(22000, 0, 19000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 19100, 350, 21500, 180)
    SetChrPos(0x102, 19100, 350, 21500, 180)
    SetChrPos(0x103, 19100, 350, 21500, 180)
    SetChrPos(0x104, 19100, 350, 21500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x24, 0x4)
    SetChrPos(0x24, 19100, 350, 21500, 180)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x24, 0xFF)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x27, 0x80)
    OP_78(0x5, 0x27)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x27, 5300, 0, -12500, 270)
    OP_D3(0x27, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00600.itp")
    SetCameraDistance(20500, 6000)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)

    def lambda_A12E():
        OP_96(0xFE, 0x4CF4, 0x0, 0x3908, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A12E)

    def lambda_A148():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A148)
    Sleep(500)

    def lambda_A15C():
        OP_96(0xFE, 0x48A8, 0x0, 0x3908, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A15C)

    def lambda_A176():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A176)
    Sleep(600)

    def lambda_A18A():
        OP_96(0xFE, 0x4CF4, 0x0, 0x3DB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A18A)

    def lambda_A1A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A1A4)
    Sleep(500)

    def lambda_A1B8():
        OP_96(0xFE, 0x48A8, 0x0, 0x3DB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A1B8)

    def lambda_A1D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A1D2)
    WaitChrThread(0x104, 1)

    def lambda_A1E7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A1E7)
    WaitChrThread(0x103, 1)

    def lambda_A1F8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A1F8)
    WaitChrThread(0x102, 1)

    def lambda_A209():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A209)
    WaitChrThread(0x101, 1)

    def lambda_A21A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A21A)

    def lambda_A227():
        OP_95(0xFE, 19100, 0, 17700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_A227)

    def lambda_A241():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_A241)
    WaitChrThread(0x24, 1)
    WaitChrThread(0x24, 2)
    OP_6F(0x10)

    NpcTalk(
        0x24,
        "Eastern Man",
        "#2101080V#5PThank you for all you do, officers.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x24,
        "Eastern Man",
        (
            "#2101081V#5PThe branch manager told me to tell you\x01",
            "to contact us again if anything happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101082V#12P#0003FWe appreciate the hospitality.\x02",
    )

    CloseMessageWindow()
    OP_93(0x24, 0x0, 0x1F4)

    def lambda_A348():
        OP_95(0xFE, 19100, 0, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_A348)
    Sleep(1000)

    def lambda_A365():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_A365)
    WaitChrThread(0x24, 1)
    WaitChrThread(0x24, 2)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x4)
    ClearMapObjFlags(0x4, 0x10)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    Sleep(700)
    Sound(809, 0, 100, 0)
    Sleep(500)
    OP_68(22000, 0, 17870, 2000)
    MoveCamera(45, 20, 0, 2000)
    SetCameraDistance(18950, 2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2101083V#0006F#5PSo now we have to worry about these\x01",
            "guys on top of Revache...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101084V#0306F#12PI wanna say they at least seem a bit\x01",
            "friendlier than Revache.\x02\x03",
            "#2101085V#0301FYou think they're just doin' it to screw with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101086V#12P#0206F#6PThat is not out of the realm of possibility.\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_64(0x102)

    def lambda_A5BA():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A5BA)
    Sleep(50)

    def lambda_A5CA():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A5CA)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#2101087V#6P#0005FElie? You okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101088V#6P#0201FAre you feeling unwell?\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2101089V#5P#0104FNo, no. I'm fine.\x02\x03",
            "#2101090V#0108FMore importantly, we found out that the\x01",
            "legendary assassin, Yin, has managed to\x01",
            "infiltrate Crossbell State.\x02\x03",
            "#2101091V#0101FWe can likely work under this assumption.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101092V#6P#0001FYeah, it didn't seem like he was lying.\x02\x03",
            "#2101093V#0008FAlso, I find it hard to believe that Cao is\x01",
            "the one threatening Arc en Ciel and Ilya.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#2101094V#0301F#11PI was thinkin' the same thing.\x02\x03",
            "#2101095VOnly problem is, why'd he call attention to\x01",
            "himself and imply that they're connected to Yin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101096V#6P#0208FThen, would that mean...\x02\x03",
            "#2101097V#0201F...Yin's actions are not tied to his employer,\x01",
            "Heiyue, but rather he is acting of his own\x01",
            "accord.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#2101098V#0006F#5PWe might be out of options, if that's\x01",
            "the case.\x02\x03",
            "#2101099V#0001FLet's assume you're right. That means\x01",
            "Cao probably doesn't know Yin's true\x01",
            "identity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101100V#0301FSounds like our only option is to catch\x01",
            "a legendary assassin, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101101V#5P#0108FUnfortunately true.\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#2101102V#5P#0103FIf Yin is truly after Ilya's life, then...\x02\x03",
            "#2101103V...this case may be beyond our capabilities.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AB18():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AB18)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x101,
        "#2101212V#6P#0005F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101105V#5P#0100FThere's no guarantee that we'd be able\x01",
            "to apprehend a professional assassin\x01",
            "like Yin, anyway.\x02\x03",
            "#2101106VThat being the case, wouldn't it be better to\x01",
            "leave this to headquarters?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101107V#6P#0011FI'm not sure that's necessarily true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101108V#6P#0205FWould they not simply look the other way\x01",
            "like they did the incident downtown?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101109V#5P#0103FI doubt it. Arc en Ciel, and by extension, Ilya,\x01",
            "are incredibly important to the people of\x01",
            "Crossbell.\x02\x03",
            "#2101110V#0101FHeadquarters would definitely take action if\x01",
            "her life were in danger.\x02\x03",
            "#2101111VThey'd stake their pride on it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 19400, 0, 6200, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    Sound(1557, 255, 100, 0)

    NpcTalk(
        0x25,
        "Man's Voice",
        "#2101112VThat's correct.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(22000, 0, 16000, 2500)
    SetCameraDistance(20500, 2500)

    def lambda_AE6C():
        OP_96(0xFE, 0x4BC8, 0x0, 0x2BC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_AE6C)

    def lambda_AE86():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AE86)
    Sleep(100)

    def lambda_AE96():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AE96)
    Sleep(100)

    def lambda_AEA6():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AEA6)
    Sleep(100)

    def lambda_AEB6():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AEB6)
    WaitChrThread(0x25, 1)
    OP_6F(0x11)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2101113V#0011F#5PY-You're...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101114V#5P#0105FI believe you're with the First Investigative\x01",
            "Division, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101115V#11P#0603FI am. Alex Dudley, of the First Investigative\x01",
            "Division.\x02\x03",
            "#2101116V#0601FLet's relocate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101117V#0005F#5PHuh? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101118V#11P#0601FOnly an absolute buffoon would discuss\x01",
            "information here of all places.\x02\x03",
            "#2101119VWe don't have time to waste. Follow me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101120V#0011F#5PU-Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2101121V#5P#0301FWhat's with the 'tude, pal?\x02",
    )

    CloseMessageWindow()
    OP_93(0x25, 0xB4, 0x1F4)
    SetCameraDistance(21000, 1500)

    def lambda_B137():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_B137)
    Sleep(500)
    FadeToDark(1000, 0, -1)

    def lambda_B15E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B15E)
    Sleep(150)

    def lambda_B17B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B17B)
    Sleep(150)

    def lambda_B198():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B198)
    Sleep(150)

    def lambda_B1B5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B1B5)
    OP_0D()
    EndChrThread(0x25, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x101, 0x1)
    OP_6F(0x10)
    OP_68(12300, 900, -10300, 0)
    MoveCamera(310, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x25, 17600, 0, -6000, 225)
    SetChrPos(0x101, 19600, 0, -4000, 225)
    SetChrPos(0x102, 20600, 0, -3000, 225)
    SetChrPos(0x103, 21600, 0, -2000, 225)
    SetChrPos(0x104, 22600, 0, -1000, 225)
    BeginChrThread(0x25, 3, 0, 47)
    BeginChrThread(0x101, 3, 0, 48)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 3, 0, 50)
    BeginChrThread(0x104, 3, 0, 51)
    OP_68(8200, 900, -10300, 8000)
    MoveCamera(315, 25, 0, 8000)
    SetCameraDistance(19500, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x25, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    OP_93(0x25, 0x5A, 0x1F4)
    Sleep(150)
    Sound(1555, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x25,
        (
            "#2101122VAre you all insane?\x02\x03",
            "#2101123VI don't know what you were planning,\x01",
            "but to think you'd waltz right in there.\x02\x03",
            "#2101124VNot only that, you then decided to discuss the\x01",
            "results within earshot of their building!\x02",
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
        "#2101125V#6P#0006FSorry, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101126V#0108F#12PPerhaps we were too hasty with our\x01",
            "judgment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101127V#5P#0603FHmph.\x02\x03",
            "#2101128V#0600F...Well?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2101129V#6P#0005FWell...what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101130V#5P#0601FYou're going to explain to me what you\x01",
            "were babbling on about with Arc en Ciel...\x02\x03",
            "#2101131V...and, how this all relates to your little\x01",
            "visit to Heiyue.\x02\x03",
            "#2101132VYou'd better tell me everything you know.\x02",
        )
    )

    CloseMessageWindow()
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
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#2101133V#6P#0013FExcuse me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2101134V#12P#0301FWhere the hell is this comin' from?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101135V#12P#0211FIt is brazen of you to demand that\x01",
            "after showing up so suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101136V#5P#0604FHah. I wonder which one of us is\x01",
            "truly brazen.\x02\x03",
            "#2101137VThe First Division has been keeping tabs\x01",
            "on Heiyue for over a month already.\x02\x03",
            "#2101138V#0601FYou're the ones who barged into our\x01",
            "investigation without any notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101139V#6P#0011FIs that really the truth?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101140V#0101F#12PD-Does that mean...you're after\x01",
            "Yin, too?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101141V#5P#0603FOh? Aware of Yin's existence already,\x01",
            "are we?\x02\x03",
            "#2101142V#0601FWell, no matter. Tell me everything you know.\x02\x03",
            "#2101143VI won't hesitate to file a complaint to Sergei\x01",
            "claiming you're obstructing our investigation...\x01",
            "If you don't comply, that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101144V#6P#0008FDamn it... All right, fine. I understand.\x02\x03",
            "#2101145V#0013FHowever, this was a formal request\x01",
            "submitted to the SSS.\x02\x03",
            "#2101146VCan we ask that you don't tell anyone else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101147V#5P#0603FI'll be the one to decide that.\x02\x03",
            "#2101148V#0601FOn with the details, already. This is an order.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)
    OP_63(0x25, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    SetCameraDistance(19500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_64(0x25)
    OP_6F(0x10)

    ChrTalk(
        0x25,
        (
            "#2101149V#5P#0604FHmm... I understand the situation.\x02\x03",
            "#2101150VI didn't think there was anything concrete,\x01",
            "but it seems they've finally tipped their hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101151V#0101F#12PAre you referring to Yin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101152V#5P#0600FYes, I am.\x02\x03",
            "#2101153V#0603FHeiyue employed a legendary assassin\x01",
            "as a trump card in order to threaten\x01",
            "Revache's influence.\x02\x03",
            "#2101154VThe First Division received an anonymous\x01",
            "tip with information regarding Heiyue.\x01",
            "We've been surveilling them since.\x02\x03",
            "#2101155V#0601FI have to say, though. I'm impressed a group\x01",
            "of amateurs were able to jump right into\x01",
            "the thick of it and create an opening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101156V#12P#0304FWow. Mighty high praise comin'\x01",
            "from a guy like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101157V#12P#0201FI would like to inquire as to why you only had\x01",
            "Heiyue under your surveillance.\x02\x03",
            "#2101158VI am under the impression that your team is\x01",
            "leaving Revache unchecked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101159V#5P#0604FExcuse me? What are you implying?\x02\x03",
            "#2101160VThe First Division already understands\x01",
            "Revache's operating procedure.\x02\x03",
            "#2101161V#0602FWe're also fully aware of both the incident\x01",
            "downtown and how they've used war hounds.\x02\x03",
            "#2101162VDon't think for a second that we haven't kept tabs\x01",
            "on the cases you've been getting involved in.\x02",
        )
    )

    CloseMessageWindow()
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#2101192V#6P#0005F#4SWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101164V#12P#0201FWhy, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101165V#5P#0603FIf we jump on every little thing they did,\x01",
            "then we'd be running in circles.\x02\x03",
            "#2101166V#0600FIt's not like they committed a murder.\x01",
            "They were just petty crimes.\x02\x03",
            "#2101167VDo you think it's worth it to strain our limited\x01",
            "personnel and put off more important cases?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101168V#6P#0007FI understand that, but still!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101169V#5P#0601FDetectives of the First Division are different\x01",
            "from greenhorns like yourselves.\x02\x03",
            "#2101170V#0603FWe're charged with maintaining a certain degree of\x01",
            "order in a city where justice has an uphill battle as is.\x02\x03",
            "#2101171VWe're expected to suppress major crimes and protect\x01",
            "the public from criminal organizations and foreign\x01",
            "intelligence agencies...\x02\x03",
            "#2101172V#0601FCan you possibly fathom the work that goes into that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101173V#6P#0005F...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101174V#0108F#12PI knew it. I always had a feeling...\x02\x03",
            "#2101175V#0106FCrossbell's peace and prosperity are\x01",
            "hanging by a thread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101176V#5P#0606FYes, and most of the citizens fail to\x01",
            "realize it.\x02\x03",
            "#2101177V#0600FSure, it might be popular to read stories on\x01",
            "Revache's ties to Imperial Faction diet members.\x02\x03",
            "#2101178VMeanwhile, Heiyue is in the process of deepening\x01",
            "their relationship with the Republican Faction.\x02\x03",
            "#2101179V#0603FIf we allow it to progress any further, they'll\x01",
            "be untouchable.\x02\x03",
            "#2101180V#0601FOur laws against espionage are lax, as well.\x01",
            "Agents from foreign intelligence agencies are\x01",
            "free to enter and leave however they'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101181V#6P#0013FI never realized how dire the situation was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101182V#12P#0206FThis is unbelievable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101183V#12P#0306FSounds like Crossbell's always one step\x01",
            "away from all hell breakin' loose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101184V#0108F#40W#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101185V#5P#0603FWe're doing everything we can, despite\x01",
            "the desperate situation we're in.\x02\x03",
            "#2101186VWe assess how dangerous each case is,\x01",
            "and even if we can't solve the root cause\x01",
            "of it, we can at least lessen the impact.\x02\x03",
            "#2101187V#0600FHandling Yin is nothing more than solving\x01",
            "one part of a larger puzzle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101188V#6P#0005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101189V#5P#0600FWe haven't been able to keep a close watch\x01",
            "on the case regarding Arc en Ciel.\x02\x03",
            "#2101190VThank you for the valuable information.\x02\x03",
            "#2101191VThe First Division will handle it from here.\x01",
            "You may return to your usual positions.\x02",
        )
    )

    CloseMessageWindow()
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#2101163V#6P#0007F#4SWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101193V#12P#0307FThe hell you gettin' at?! Why are you\x01",
            "doin' this to us?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#2101194V#5P#0603FAfter carefully assessing the situation, I've\x01",
            "ascertained that Yin is more than a mere legend.\x02\x03",
            "#2101195VWe'll be observing Heiyue's movements\x01",
            "while protecting Ilya Platiere from falling\x01",
            "victim to our mysterious assassin.\x02\x03",
            "#2101196V#0602FTell me. Do you think you'd be able to handle it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101197V#6P#0010FD-Damn it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101198V#12P#0206FWith our lack of resources, it would prove\x01",
            "to be difficult.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x25, 0x10E, 0x1F4)
    OP_68(6890, 900, -9560, 2000)

    def lambda_CC83():
        OP_95(0xFE, 5000, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_CC83)
    WaitChrThread(0x25, 1)
    OP_93(0x25, 0xB4, 0x1F4)
    OP_71(0x5, 0xF1, 0x10E, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0x5)
    Sleep(500)

    ChrTalk(
        0x25,
        (
            "#2101199V#0603F#5PAt the very least, I can let you handle\x01",
            "contacting Arc en Ciel.\x02\x03",
            "#2101200VMake sure you tell them that their case has\x01",
            "been transferred to the First Division.\x02\x03",
            "#2101201V#0600FSee to it that they're given a proper explanation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CDB8():
        OP_95(0xFE, 5000, 0, -11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_CDB8)
    Sleep(100)

    def lambda_CDD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_CDD5)
    WaitChrThread(0x25, 1)
    WaitChrThread(0x25, 2)
    OP_71(0x5, 0x10F, 0x12C, 0x0, 0x0)
    Sound(461, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x5)
    Sound(457, 0, 100, 0)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)

    def lambda_CE24():
        OP_95(0xFE, -14000, 0, -12500, 6500, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_CE24)
    Sleep(1250)
    Sound(458, 0, 100, 0)
    Fade(500)
    OP_68(-14500, 1000, -12500, 0)
    MoveCamera(40, 35, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_68(-19500, 1000, -19500, 4000)
    MoveCamera(60, 25, 0, 4000)
    SetCameraDistance(16500, 4000)
    WaitChrThread(0x27, 1)

    def lambda_CEA3():
        OP_9E(0xFE, 0xFFFFC950, 0xFFFFB7BC, 0xFFFEA070, 0x1964, 0x1)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_CEA3)
    WaitChrThread(0x27, 1)

    def lambda_CEC2():
        OP_95(0xFE, -20000, 0, -33500, 6500, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_CEC2)
    WaitChrThread(0x27, 1)
    OP_6F(0x79)
    ClearChrFlags(0x25, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x5, 0x1000)
    StopBGM(0x1770)
    Fade(1000)
    OP_68(7700, 900, -10300, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_68(9810, 900, -10230, 3000)
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#2101202V#0301F#12PWhat the hell? He said his piece and\x01",
            "then peaced out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101203V#12P#0211FDriving away in his personal vehicle\x01",
            "frustrates me even more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101204V#0103F#11P#40W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101205V#0008F#5PAs frustrated as we all are, I understand\x01",
            "where he's coming from.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#2101206V#0105F#11PYou do?\x02",
    )

    CloseMessageWindow()

    def lambda_D0A9():
        OP_93(0xFE, 0x59, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D0A9)
    Sleep(50)

    def lambda_D0B9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D0B9)
    Sleep(50)
    OP_93(0x104, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2101207V#0006F#5PI actually agree with him. The scope of this\x01",
            "case has gone way beyond our level of\x01",
            "experience.\x02\x03",
            "#2101208VAll we can do now is inform the troupe and\x01",
            "offer our sincerest apologies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2101209V#0306FSo, that it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101210V#12P#0208FThere is...nothing more we can do.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#2101211V#0107F#11PW-Wait a moment, everyone!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D255():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D255)
    Sleep(50)

    def lambda_D265():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D265)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x101,
        "#2101104V#6P#0005FHuh?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)
    SetCameraDistance(19000, 20000)

    ChrTalk(
        0x102,
        (
            "#2101213V#0106F#11PLloyd, how can you...\x02\x03",
            "#2101214VHow can you say that?! You told us to overcome\x01",
            "#0101Four barriers... You said as long we're together,\x01",
            "then no barrier is too high, didn't you?!\x02\x03",
            "#2101215V#0107FSo...why? Why are you giving up so easily?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101216V#6P#0011FE-Elie...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101217V#12P#0305FWhy the total meltdown, Mademois-Elie?\x02\x03",
            "#2101218V#0301FDidn't ya already tell us it'd be\x01",
            "better to leave it to headquarters?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#2101219V#0105F#11P#40WOh...\x02\x03",
            "#2101220V#0108F#50WI did, didn't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101221V#6P#0205FElie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101222V#6P#0006FListen, Elie.\x02\x03",
            "#2101223VI don't like the situation we're in, either. I don't\x01",
            "want it to end this way... There has to be\x01",
            "something we can do.\x02\x03",
            "#2101224V#0000FIf you don't want us to give up, then we'll\x01",
            "find another way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101225V#0106F#11PNo, it's all right.\x02\x03",
            "#2101226V#0102FI'm sorry, everyone. I think we've just\x01",
            "had a rough day, is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101227V#6P#0001FElie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101228V#12P#0306FWell, we did spend our entire day runnin'\x01",
            "into one jackass after another.\x02\x03",
            "#2101229V#0300FLet's go report the news to Arc en Ciel.\x01",
            "We can head back to the SSS and\x01",
            "relax for a bit after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101230V#6P#0203FUnderstood. That sounds like a\x01",
            "reasonable plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101231V#6P#0003FSure. Fine by me.\x02\x03",
            "#2101232V#0000FIs that okay with you, Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101233V#0104F#11PYes... Thank you, everyone.\x02\x03",
            "#2101234V#0100FLet's be off to Arc en Ciel, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    StopBGM(0xBB8)
    SetChrPos(0x0, 9600, 0, -10300, 270)
    SetScenarioFlags(0x81, 3)
    OP_29(0x42, 0x1, 0x8)
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    EventEnd(0x5)
    Return()

    # Function_46_9F88 end

    def Function_47_D8B1(): pass

    label("Function_47_D8B1")


    def lambda_D8B6():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D8B6)
    WaitChrThread(0x25, 1)

    def lambda_D8D4():
        OP_95(0xFE, 6700, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_D8D4)
    WaitChrThread(0x25, 1)
    Return()

    # Function_47_D8B1 end

    def Function_48_D8EE(): pass

    label("Function_48_D8EE")

    Sleep(500)

    def lambda_D8F6():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D8F6)
    WaitChrThread(0x101, 1)

    def lambda_D914():
        OP_95(0xFE, 9600, 0, -11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D914)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_48_D8EE end

    def Function_49_D935(): pass

    label("Function_49_D935")

    Sleep(600)

    def lambda_D93D():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D93D)
    WaitChrThread(0x102, 1)

    def lambda_D95B():
        OP_95(0xFE, 9600, 0, -9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D95B)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x10E, 0x1F4)
    Return()

    # Function_49_D935 end

    def Function_50_D97C(): pass

    label("Function_50_D97C")

    Sleep(700)

    def lambda_D984():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D984)
    WaitChrThread(0x103, 1)

    def lambda_D9A2():
        OP_95(0xFE, 11000, 0, -11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D9A2)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x10E, 0x1F4)
    Return()

    # Function_50_D97C end

    def Function_51_D9C3(): pass

    label("Function_51_D9C3")

    Sleep(800)

    def lambda_D9CB():
        OP_95(0xFE, 13300, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D9CB)
    WaitChrThread(0x104, 1)

    def lambda_D9E9():
        OP_95(0xFE, 11000, 0, -9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D9E9)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_51_D9C3 end

    def Function_52_DA0A(): pass

    label("Function_52_DA0A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1600, 2500, 5600, 0)
    MoveCamera(55, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29000, 0)
    SetChrPos(0x0, -19600, 0, -28000, 0)
    SetChrPos(0x1, -19600, 0, -28000, 0)
    SetChrPos(0x2, -19600, 0, -28000, 0)
    SetChrPos(0x3, -19600, 0, -28000, 0)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, -10500, 0, 12000, 180)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, 8000, 0, 10000, 270)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, -18000, 0, 12500, 180)
    SetChrFlags(0xA, 0x8000)

    def lambda_DB09():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DB09)
    OP_68(-1600, 1500, 5600, 5000)
    FadeToBright(2000, 0)
    Sleep(1000)

    def lambda_DB40():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_DB40)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(22140, 2500, 20700, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(21000, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1210", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_DA0A end

    def Function_53_DBB1(): pass

    label("Function_53_DBB1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00500.itc", 0x1E)
    LoadChrToIndex("apl/ch50220.itc", 0x1F)
    LoadEffect(0x0, "event\\eva04_00.eff")
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(21500, 7900, 24500, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x26, 0x8000)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x26, 23000, 9500, 24500, 270)
    OP_52(0x26, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_68(21500, 10400, 24500, 5000)
    FadeToBright(2000, 0)
    Sleep(3000)
    PlayEffect(0x1, 0xFF, 0x26, 0x40, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrChip(0x0, 0x26, 0x1E, 0x12C)

    def lambda_DD02():
        OP_95(0xFE, 21500, 9500, 24500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_DD02)

    def lambda_DD1C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_DD1C)
    WaitChrThread(0x26, 1)
    WaitChrThread(0x26, 2)
    SetChrChip(0x1, 0x26, 0x0, 0x0)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x1)
    Sleep(500)
    OP_68(14000, 9400, 24500, 700)
    MoveCamera(40, 18, 0, 700)
    SetCameraDistance(17500, 700)
    SetChrChip(0x0, 0x26, 0x1E, 0x12C)
    SetChrSubChip(0x26, 0x0)

    def lambda_DD80():
        OP_9D(0xFE, 0x36B0, 0x2134, 0x5FB4, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_DD80)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x26, 1)
    PlayEffect(0x0, 0xFF, 0x26, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x26, 0x1)
    Sleep(50)
    OP_6F(0x79)
    OP_68(14000, 11800, 31000, 700)
    MoveCamera(35, 15, 0, 700)
    SetCameraDistance(18500, 700)
    SetChrSubChip(0x26, 0x0)

    def lambda_DE10():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_DE10)

    def lambda_DE1D():
        OP_9D(0xFE, 0x36B0, 0x2A30, 0x7918, 0xCE4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_DE1D)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x26, 1)
    PlayEffect(0x0, 0xFF, 0x26, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x26, 0x1)
    Sleep(50)
    OP_6F(0x79)
    OP_68(-4000, 11200, 31000, 2000)
    MoveCamera(45, 27, 0, 2000)
    SetCameraDistance(22500, 2000)
    SetChrSubChip(0x26, 0x0)

    def lambda_DEAD():
        OP_93(0xFE, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_DEAD)

    def lambda_DEBA():
        OP_9D(0xFE, 0x24B8, 0x2C24, 0x7918, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_DEBA)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x26, 1)
    SetChrSubChip(0x26, 0x1)
    Sleep(50)
    SetChrSubChip(0x26, 0x0)

    def lambda_DEEC():
        OP_9D(0xFE, 0xFFFFF448, 0x2648, 0x7918, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_DEEC)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x26, 1)
    PlayEffect(0x0, 0xFF, 0x26, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x26, 0x1)
    Sleep(50)
    SetChrSubChip(0x26, 0x0)

    def lambda_DF55():
        OP_9D(0xFE, 0xFFFFD314, 0x3458, 0x7918, 0x1324, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_DF55)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x26, 1)
    PlayEffect(0x0, 0xFF, 0x26, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x26, 0x1)
    Sleep(50)
    SetChrSubChip(0x26, 0x0)

    def lambda_DFBE():
        OP_9D(0xFE, 0xFFFFAC04, 0x3458, 0x7918, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_DFBE)
    Sound(854, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x26, 0x1)
    SetScenarioFlags(0x5C, 2)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_DBB1 end

    def Function_54_DFF8(): pass

    label("Function_54_DFF8")

    EventBegin(0x0)
    Fade(1000)
    OP_68(22000, 2000, 20100, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 18600, 0, 12400, 0)
    SetChrPos(0x102, 19600, 0, 12400, 0)
    SetChrPos(0x103, 18600, 0, 11000, 0)
    SetChrPos(0x104, 19600, 0, 11000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x21, 19100, 0, 16600, 0)
    MoveCamera(30, 30, 0, 5000)
    SetCameraDistance(17000, 5000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(19100, 1100, 13600, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#4200058V#12P#0013FThis place is a mess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200059V#12P#0201FA raid will do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200060V#0303FYep, this confirms it. I'm seein' traces of\x01",
            "heavy weaponry all over.\x02\x03",
            "#4200061V#0301F'Least they didn't resort to blowing 'em\x01",
            "up with explosives.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x21, 0xFF)
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x21, 0xB4, 0x1F4)

    ChrTalk(
        0x21,
        "#4200062V#5POh, I see you guys are on the scene, too.\x02",
    )

    CloseMessageWindow()
    OP_68(19100, 1100, 14000, 1200)

    def lambda_E2AB():
        OP_95(0xFE, 19100, 0, 14800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_E2AB)
    WaitChrThread(0x21, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#4200063V#12P#0001FHey, Franz...\x01",
            "How's the situation looking?\x02\x03",
            "#4200064VWe rushed out here as soon as we\x01",
            "heard the news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#4200065V#5PI don't know much, yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#4200066V#5PAll I've heard is that shots were fired\x01",
            "in the middle of the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#4200067V#5PDudley and the others are in the middle of\x01",
            "conducting an investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#4200068V#0106FIt sounds like the First Division beat us to\x01",
            "the punch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200069V#12P#0206FWell, they are highly coordinated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200070V#12P#0003FWe'd like to ask the members of Heiyue\x01",
            "some questions.\x02\x03",
            "#4200071V#0000FDo you mind letting us inside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#4200072V#5PUh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#4200073V#5PI suppose I could...? I was only told to not\x01",
            "let civilians pass through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#4200074V#5PYou'll have to make up an excuse\x01",
            "to Dudley for me, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200075V#12P#0002FOf course. Thanks for helping us out.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 19100, 0, 13000, 0)
    OP_4C(0x21, 0xFF)
    SetChrPos(0x21, 20500, 0, 15200, 180)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0xC2, 3)
    OP_29(0x4B, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_54_DFF8 end

    def Function_55_E6B3(): pass

    label("Function_55_E6B3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(22000, 0, 21000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 19100, 350, 21500, 180)
    SetChrPos(0x102, 19100, 350, 21500, 180)
    SetChrPos(0x103, 19100, 350, 21500, 180)
    SetChrPos(0x104, 19100, 350, 21500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x21, 20500, 0, 15200, 180)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetCameraDistance(22500, 4000)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x4)

    def lambda_E7DF():
        OP_96(0xFE, 0x4A9C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E7DF)

    def lambda_E7F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E7F9)
    Sleep(650)

    def lambda_E80D():
        OP_96(0xFE, 0x4A9C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E80D)

    def lambda_E827():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E827)
    Sleep(650)

    def lambda_E83B():
        OP_96(0xFE, 0x4A9C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E83B)

    def lambda_E855():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E855)
    Sleep(650)

    def lambda_E869():
        OP_96(0xFE, 0x4A9C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E869)

    def lambda_E883():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E883)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    OP_4B(0x101, 0xFF)
    OP_4B(0x102, 0xFF)
    OP_4B(0x103, 0xFF)
    OP_4B(0x104, 0xFF)

    def lambda_E8B9():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E8B9)

    def lambda_E8C6():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_E8C6)

    def lambda_E8D3():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_E8D3)

    def lambda_E8E0():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_E8E0)
    Sleep(100)
    OP_4B(0x21, 0xFF)
    TurnDirection(0x21, 0x101, 500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x21)

    def lambda_E92B():

        label("loc_E92B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E92B")

    QueueWorkItem2(0x21, 2, lambda_E92B)

    def lambda_E93D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E93D)

    def lambda_E94A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_E94A)

    def lambda_E957():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_E957)

    def lambda_E964():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_E964)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_4C(0x101, 0xFF)
    OP_4C(0x102, 0xFF)
    OP_4C(0x103, 0xFF)
    OP_4C(0x104, 0xFF)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    WaitChrThread(0x101, 1)
    Fade(1000)
    OP_68(21100, 1000, 1800, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    EndChrThread(0x21, 0x2)
    OP_4C(0x21, 0xFF)
    SetChrPos(0x21, 20500, 0, 15200, 180)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrPos(0x101, 21100, 0, 3800, 180)
    SetChrPos(0x102, 21600, 0, 5300, 180)
    SetChrPos(0x103, 20600, 0, 4800, 180)
    SetChrPos(0x104, 21100, 0, 6500, 180)
    OP_68(21100, 1000, -2200, 4000)

    def lambda_EA4F():
        OP_95(0xFE, 21100, 0, -3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EA4F)
    Sleep(50)

    def lambda_EA6C():
        OP_95(0xFE, 22100, 0, -1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EA6C)
    Sleep(50)

    def lambda_EA89():
        OP_95(0xFE, 20100, 0, -2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EA89)
    Sleep(50)

    def lambda_EAA6():
        OP_95(0xFE, 21100, 0, -900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EAA6)
    WaitChrThread(0x101, 1)

    def lambda_EAC4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EAC4)
    WaitChrThread(0x102, 1)

    def lambda_EAD5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EAD5)
    WaitChrThread(0x103, 1)

    def lambda_EAE6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_EAE6)
    WaitChrThread(0x104, 1)
    OP_6F(0x11)

    ChrTalk(
        0x101,
        "#4200231V#12P#0006FWell, that was something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200232V#5P#0106FThey gave us plenty of useful information\x01",
            "to work with, but...\x02\x03",
            "#4200233V#0101FI can't believe they suggested the high\x01",
            "possibility of a full-blown conflict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200234V#0303F#5PIf things keep heatin' up the way they have,\x01",
            "then it's about to get real messy.\x02\x03",
            "#4200235V#0301FWe're screwed if they decide to have a\x01",
            "firefight in the middle of town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200236V#6P#0206FAdditionally, we have to consider the possibility\x01",
            "that Heiyue may call for reinforcements.\x02\x03",
            "#4200237V#0211FThis is all sounding a bit too ominous.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#4200238V#12P#0003FIt sounds like we have a bit of time still,\x01",
            "judging by what Cao said.\x02\x03",
            "#4200239V#0013FAt any rate, we can't leave Revache unchecked\x01",
            "any longer.\x02\x03",
            "#4200240VWe need to start looking into it before Heiyue\x01",
            "mobilizes their forces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200241V#5P#0101FI agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200242V#6P#0205FShall we visit each of the districts and\x01",
            "question the citizens?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200243V#12P#0003FNo.\x02\x03",
            "#4200244V#0000FI think it's time we go straight to the source.\x01",
            "Let's go get our answers from Revache directly.\x02",
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

    ChrTalk(
        0x104,
        "#4200245V#0305F#5PYou're kiddin', right?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200246V#5P#0106FWe may have gone there once before,\x01",
            "but still...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200247V#6P#0201FThat was before the incident at the auction.\x01",
            "Are we not acting too recklessly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200248V#12P#0006FYeah... I can't imagine they'd overlook\x01",
            "anything outside of KeA's case.\x02\x03",
            "#4200249V#0008FThere's something else I'm concerned\x01",
            "about, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200250V#6P#0205FWhat might that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200251V#12P#0001FGarcia's movements.\x02\x03",
            "#4200252VWe've quarreled with him before, but he never\x01",
            "seemed the type to be reckless.\x02\x03",
            "#4200253VI was under the impression that he had a strong\x01",
            "command over his subordinates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200254V#0303F#5PGood eye. He used to be a well-known\x01",
            "jaeger commander, in fact.\x02\x03",
            "#4200255V#0301FDidn't think he'd order his men to launch an\x01",
            "assault on Heiyue like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200256V#5P#0103FWhile there's a chance he ordered the\x01",
            "attack on Heiyue, it's entirely possible\x01",
            "that his subordinates acted independently.\x02\x03",
            "#4200257V#0101FI'd certainly like to get to the bottom of this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200258V#12P#0000FI agree.\x02\x03",
            "#4200259VIt'd be a good idea to search for clues around\x01",
            "their base.\x02\x03",
            "#4200260VDo you guys want to head there now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200261V#5P#0102F*sigh* We don't have a choice, do we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200262V#6P#0202FAs long as we remain outside of the perimeter,\x01",
            "the level of risk will be low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200263V#0302F#5PLet's go have ourselves a little stakeout!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 21100, 0, -2500, 180)
    SetScenarioFlags(0xC2, 4)
    OP_29(0x4B, 0x1, 0x2)
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_55_E6B3 end

    def Function_56_F588(): pass

    label("Function_56_F588")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(18120, 2300, 5600, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(14010, 0)
    SetChrPos(0x8, 19940, 0, 9410, 180)
    SetChrPos(0x101, 19200, 0, 7270, 0)
    SetChrPos(0x102, 20640, 0, 7470, 0)
    SetChrPos(0x103, 19150, 0, 5850, 0)
    SetChrPos(0x104, 20640, 0, 6050, 0)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#0000FSorry to bother you, but have\x01",
            "you picked up anything lying\x01",
            "around here recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5POh, my. Lost something, have we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI actually found something stuck in the\x01",
            "grass on the outskirts of the park.\x01",
            "I was kinda curious, so I picked it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PIt was actually almost blown away by the wind.\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#0005FBlown away by the wind...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F#12POur client failed to identify what the\x01",
            "third lost item was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100F#11PWhat could blow away in the wind?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWere you guys looking for it? I suppose\x01",
            "I should give it to you, then.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x339),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x339, 1)

    ChrTalk(
        0x104,
        (
            "#11P#0305FA train ticket, eh?\x02\x03",
            "#0306FDoubt he's going anywhere without\x01",
            "this bad boy.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x337, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x338, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x339, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FA3F")

    ChrTalk(
        0x101,
        (
            "#6P#0003FA-Anyway, we were able to retrieve all\x01",
            "of his missing items. Good job, guys.\x02\x03",
            "#0000FLet's go back to Tront and tell him the\x01",
            "good news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100F#11PI'm sure he'll be glad to see his valuables again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_FA6C")

    label("loc_FA3F")


    ChrTalk(
        0x101,
        "#6P#0003FWe'll deliver it to him later.\x02",
    )

    CloseMessageWindow()

    label("loc_FA6C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 20110, 0, 7370, 225)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    OP_29(0x2, 0x1, 0x4)
    SetScenarioFlags(0x2, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FAC2")
    OP_29(0x2, 0x1, 0x1F)

    label("loc_FAC2")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_56_F588 end

    def Function_57_FAC8(): pass

    label("Function_57_FAC8")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell City Cruise Ship Schedule\x01\x01",
            "The pride of Mishelam, Mishelam Wonderland,\x01",
            "is now open for all to enjoy! Come on down and\x01",
            "experience the greatest theme park of all time!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_57_FAC8 end

    def Function_58_FBB0(): pass

    label("Function_58_FBB0")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "        Lupinus River - Lighthouse 1\x01\x01",
            "Unauthorized entry is strictly prohibited.\x01",
            "                                 - City Hall\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_58_FBB0 end

    SaveToFile()

Try(main)
