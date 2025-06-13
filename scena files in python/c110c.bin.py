from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c110c.bin",                # FileName
        "c110c",                    # MapName
        "c110c",                    # Location
        0x0016,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 22, 0, 2, 0, 3],
    )

    BuildStringList((
        "c110c",                  # 0
        "Officer Franz",          # 1
        "Shannah",                # 2
        "Abby",                   # 3
        "Chroma",                 # 4
        "Otto",                   # 5
        "Tajik",                  # 6
        "Derek",                  # 7
        "Sealy",                  # 8
        "Inspector Donovan",      # 9
        "Detective Raymond",      # 10
        "Chief Jolich",           # 11
        "Aretha",                 # 12
        "Stefan",                 # 13
        "Officer",                # 14
        "Chief Sergei",           # 15
        "Officer Kate",           # 16
        "Grace",                  # 17
        "Reins",                  # 18
        "Estelle",                # 19
        "Joshua",                 # 20
        "Bracer Lynn",            # 21
        "Bracer Aeolia",          # 22
        "Tourist",                # 23
        "Tourist",                # 24
        "Tourist",                # 25
        "Tourist",                # 26
        "Officer",                # 27
        "Harold",                 # 28
        "Sophia",                 # 29
        "Zeit",                   # 30
        "Guest",                  # 31
        "Guest",                  # 32
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
        "chr/ch30000.itc",                   # 00
        "chr/ch20300.itc",                   # 01
        "chr/ch20600.itc",                   # 02
        "chr/ch20800.itc",                   # 03
        "chr/ch28100.itc",                   # 04
        "chr/ch32300.itc",                   # 05
        "chr/ch24900.itc",                   # 06
        "chr/ch30300.itc",                   # 07
        "chr/ch30200.itc",                   # 08
        "chr/ch30100.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch20000.itc",                   # 0B
        "chr/ch20100.itc",                   # 0C
        "chr/ch23400.itc",                   # 0D
        "chr/ch23500.itc",                   # 0E
        "chr/ch30600.itc",                   # 0F
        "chr/ch09300.itc",                   # 10
        "chr/ch09402.itc",                   # 11
        "chr/ch06000.itc",                   # 12
        "chr/ch02500.itc",                   # 13
        "chr/ch00602.itc",                   # 14
        "chr/ch00702.itc",                   # 15
        "chr/ch32000.itc",                   # 16
        "chr/ch32100.itc",                   # 17
        "chr/ch24500.itc",                   # 18
        "chr/ch22700.itc",                   # 19
        "chr/ch34200.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-15050,  2500,    27399,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(23239,   2500,    -6429,   270,  261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(23340,   2500,    -7389,   270,  261,  0x0, 0,   26,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(6929,    2490,    -6650,   225,  261,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(8369,    2390,    -14850,  90,   261,  0x0, 0,   3,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(-8739,   2500,    6070,    180,  389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-11430,  2500,    10270,   190,  261,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-13659,  2500,    10739,   190,  261,  0x0, 0,   24,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-5829,   2500,    27989,   359,  389,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-4250,   2500,    27879,   359,  389,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-6500,   2500,    30750,   359,  405,  0x0, 0,   9,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-14069,  2500,    6230,    360,  389,  0x0, 0,   25,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-15340,  2500,    6219,    360,  389,  0x0, 0,   2,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(2450,    2500,    13770,   142,  389,  0x0, 0,   0,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-3559,   2500,    25170,   270,  389,  0x0, 0,   19,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-4869,   2500,    30729,   270,  389,  0x0, 0,   15,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-8229,   2500,    26780,   45,   389,  0x0, 0,   18,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-9369,   2500,    27190,   45,   389,  0x0, 0,   4,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(-3630,   2500,    -12920,  180,  469,  0x0, 0,   20,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(-4769,   2500,    -12920,  180,  469,  0x0, 0,   21,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(1470,    2500,    -12529,  0,    389,  0x0, 0,   22,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(1870,    2500,    -10829,  225,  389,  0x0, 0,   23,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(-9420,   2500,    -11609,  45,   261,  0x0, 0,   11,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-10239,  2500,    -10750,  45,   261,  0x0, 0,   12,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(14340,   2500,    4010,    112,  261,  0x0, 0,   13,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(15750,   2500,    3609,    292,  261,  0x0, 0,   14,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(3329,    2500,    12640,   322,  389,  0x0, 0,   0,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-17799,  2500,    800,     180,  389,  0x0, 0,   16,  0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-17219,  2599,    -400,    270,  468,  0x0, 0,   17,  0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-5890,   2500,    31840,   1200,    -5890,   4000,    31840,   0x007C, 0,  46, 0x0000)
    DeclActor(16550,   2410,    10660,   1200,    16550,   3910,    10660,   0x007C, 0,  47, 0x0000)

    PlaceName(-31.530000686645508, 0.0, -107.9000015258789, 0x0000, 0x0000, "Central Square")
    PlaceName(-117.0, 0.0, -102.05000305175781, 0x0000, 0x0000, "West Street")
    PlaceName(3.5799999237060547, 0.0, 7.800000190734863, 0x0000, 0x0000, "Administrative District")
    PlaceName(-196.3000030517578, 0.0, -5.199999809265137, 0x0000, 0x0000, "Residential District")
    PlaceName(-101.4000015258789, 0.0, -15.600000381469727, 0x0000, 0x0000, "Entertainment District")
    PlaceName(74.0999984741211, 0.0, -137.8000030517578, 0x0000, 0x0000, "East Street")
    PlaceName(120.25, 0.0, -209.3000030517578, 0x0000, 0x0000, "Downtown District")
    PlaceName(110.5, 0.0, -52.0, 0x0000, 0x0000, "Harbor District")
    PlaceName(76.69999694824219, 0.0, 70.19999694824219, 0x0000, 0x0000, "IBC")
    PlaceName(-16.899999618530273, 0.0, -197.60000610351562, 0x0000, 0x0000, "Station Street")
    PlaceName(-78.0, 0.0, -62.400001525878906, 0x0000, 0x0000, "Back Alley")
    PlaceName(-20.799999237060547, 0.0, -237.89999389648438, 0x0000, 0x0000, "Ursula Road")
    PlaceName(144.3000030517578, 0.0, -119.5999984741211, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-183.3000030517578, 0.0, -104.0, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-175.5, 0.0, 26.0, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-60.130001068115234, 0.0, -126.0999984741211, 0x0000, 0x0051, "")
    PlaceName(9.75, 0.0, -92.30000305175781, 0x0000, 0x0054, "")
    PlaceName(-28.280000686645508, 0.0, -136.5, 0x0000, 0x0057, "")
    PlaceName(-61.099998474121094, 0.0, -88.4000015258789, 0x0000, 0x0053, "")
    PlaceName(-34.45000076293945, 0.0, -57.20000076293945, 0x0000, 0x0053, "")
    PlaceName(-100.43000030517578, 0.0, -94.9000015258789, 0x0000, 0x0053, "")
    PlaceName(-113.0999984741211, 0.0, -67.5999984741211, 0x0000, 0x0053, "")
    PlaceName(-81.9000015258789, 0.0, -26.0, 0x0000, 0x0052, "")
    PlaceName(-75.7300033569336, 0.0, -42.900001525878906, 0x0000, 0x0053, "")
    PlaceName(-64.3499984741211, 0.0, -53.95000076293945, 0x0000, 0x0053, "")
    PlaceName(-27.299999237060547, 0.0, 38.349998474121094, 0x0000, 0x0051, "")
    PlaceName(118.30000305175781, 0.0, -137.8000030517578, 0x0000, 0x0052, "")
    PlaceName(96.19999694824219, 0.0, -255.4499969482422, 0x0000, 0x0053, "")
    PlaceName(79.30000305175781, 0.0, -231.39999389648438, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_7D8",          # 00, 0
        "Function_1_890",          # 01, 1
        "Function_2_969",          # 02, 2
        "Function_3_DB1",          # 03, 3
        "Function_4_EF4",          # 04, 4
        "Function_5_EF8",          # 05, 5
        "Function_6_EFC",          # 06, 6
        "Function_7_110A",         # 07, 7
        "Function_8_1481",         # 08, 8
        "Function_9_14F2",         # 09, 9
        "Function_10_15F6",        # 0A, 10
        "Function_11_1CD5",        # 0B, 11
        "Function_12_2213",        # 0C, 12
        "Function_13_2396",        # 0D, 13
        "Function_14_2F2E",        # 0E, 14
        "Function_15_37B0",        # 0F, 15
        "Function_16_39B5",        # 10, 16
        "Function_17_3E62",        # 11, 17
        "Function_18_3FA6",        # 12, 18
        "Function_19_409C",        # 13, 19
        "Function_20_4240",        # 14, 20
        "Function_21_435F",        # 15, 21
        "Function_22_45CB",        # 16, 22
        "Function_23_4668",        # 17, 23
        "Function_24_492D",        # 18, 24
        "Function_25_4B45",        # 19, 25
        "Function_26_4D9A",        # 1A, 26
        "Function_27_5012",        # 1B, 27
        "Function_28_52C5",        # 1C, 28
        "Function_29_53BF",        # 1D, 29
        "Function_30_5797",        # 1E, 30
        "Function_31_58AE",        # 1F, 31
        "Function_32_5A4F",        # 20, 32
        "Function_33_5C44",        # 21, 33
        "Function_34_5F04",        # 22, 34
        "Function_35_5F7A",        # 23, 35
        "Function_36_649A",        # 24, 36
        "Function_37_683B",        # 25, 37
        "Function_38_87C4",        # 26, 38
        "Function_39_87E3",        # 27, 39
        "Function_40_882D",        # 28, 40
        "Function_41_8A42",        # 29, 41
        "Function_42_9DED",        # 2A, 42
        "Function_43_9E02",        # 2B, 43
        "Function_44_A481",        # 2C, 44
        "Function_45_AAC4",        # 2D, 45
        "Function_46_AAEA",        # 2E, 46
        "Function_47_AB66",        # 2F, 47
    ))


    def Function_0_7D8(): pass

    label("Function_0_7D8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_818"),
        (1, "loc_824"),
        (2, "loc_830"),
        (3, "loc_83C"),
        (4, "loc_848"),
        (5, "loc_854"),
        (6, "loc_860"),
        (SWITCH_DEFAULT, "loc_86C"),
    )


    label("loc_818")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_824")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_830")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_83C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_848")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_854")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_860")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_86C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_878")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_88F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_88F")

    Return()

    # Function_0_7D8 end

    def Function_1_890(): pass

    label("Function_1_890")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_968")
    OP_95(0xFE, 17250, 2500, -14850, 1000, 0x0)
    OP_95(0xFE, 17250, 2500, -70, 1000, 0x0)
    OP_95(0xFE, 3810, 2500, 8270, 1000, 0x0)
    OP_95(0xFE, -6210, 2500, 23860, 1000, 0x0)
    OP_95(0xFE, -18440, 2500, 23260, 1000, 0x0)
    OP_95(0xFE, -20840, 2450, 19170, 1000, 0x0)
    OP_95(0xFE, -19000, 2500, 6490, 1000, 0x0)
    OP_95(0xFE, -19000, 2500, -3620, 1000, 0x0)
    OP_95(0xFE, -8180, 2500, -14970, 1000, 0x0)
    OP_95(0xFE, 8370, 2390, -14850, 1000, 0x0)
    Jump("Function_1_890")

    label("loc_968")

    Return()

    # Function_1_890 end

    def Function_2_969(): pass

    label("Function_2_969")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9B")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A34")
    SetChrPos(0x0, 30170, 2500, -90, 270)
    SetChrPos(0x1, 30170, 2500, -90, 270)
    SetChrPos(0x2, 30170, 2500, -90, 270)
    SetChrPos(0x3, 30170, 2500, -90, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A07")
    SetChrPos(0x4, 30170, 2500, -90, 270)
    SetChrPos(0x5, 30170, 2500, -90, 270)
    Jump("loc_A26")

    label("loc_A07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A26")
    SetChrPos(0x4, 30170, 2500, -90, 270)

    label("loc_A26")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B9B")

    label("loc_A34")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AFA")
    SetChrPos(0x0, -40390, 0, 24150, 90)
    SetChrPos(0x1, -40390, 0, 24150, 90)
    SetChrPos(0x2, -40390, 0, 24150, 90)
    SetChrPos(0x3, -40390, 0, 24150, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ACD")
    SetChrPos(0x4, -40390, 0, 24150, 90)
    SetChrPos(0x5, -40390, 0, 24150, 90)
    Jump("loc_AEC")

    label("loc_ACD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AEC")
    SetChrPos(0x4, -40390, 0, 24150, 90)

    label("loc_AEC")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B9B")

    label("loc_AFA")

    SetChrPos(0x0, 19940, 0, -37920, 0)
    SetChrPos(0x1, 19940, 0, -37920, 0)
    SetChrPos(0x2, 19940, 0, -37920, 0)
    SetChrPos(0x3, 19940, 0, -37920, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B73")
    SetChrPos(0x4, 19940, 0, -37920, 0)
    SetChrPos(0x5, 19940, 0, -37920, 0)
    Jump("loc_B92")

    label("loc_B73")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B92")
    SetChrPos(0x4, 19940, 0, -37920, 0)

    label("loc_B92")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B9B")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_BD9")
    ClearChrFlags(0x8, 0x80)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x20, 0x10)
    SetChrFlags(0x21, 0x10)
    Jump("loc_D76")

    label("loc_BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_BE7")
    Jump("loc_D76")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_END)), "loc_C45")
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x8, 0x80)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    TurnDirection(0x13, 0x14, 0)
    TurnDirection(0x14, 0x13, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 26270, 2500, 1570, 180)
    SetChrFlags(0x1E, 0x10)
    Jump("loc_D76")

    label("loc_C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_C99")
    ClearChrFlags(0x8, 0x80)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    TurnDirection(0x13, 0x14, 0)
    TurnDirection(0x14, 0x13, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 26270, 2500, 1570, 180)
    SetChrFlags(0x1E, 0x10)
    Jump("loc_D76")

    label("loc_C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_D02")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -9520, 2500, 29080, 40)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_93(0x20, 0xB4, 0x0)
    OP_93(0x21, 0xB4, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_D76")

    label("loc_D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_D2D")
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x21, 0x10)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_D76")

    label("loc_D2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D76")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 420, 2500, 9250, 326)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -470, 2500, 10590, 146)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_D76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8A")
    Event(0, 41)

    label("loc_D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_D9E")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 40)
    Jump("loc_DB0")

    label("loc_D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_DB0")
    ClearScenarioFlags(0x5C, 1)
    SetScenarioFlags(0x2, 0)
    Event(0, 44)

    label("loc_DB0")

    Return()

    # Function_2_969 end

    def Function_3_DB1(): pass

    label("Function_3_DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_DC3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DC3")

    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    SetMapObjFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_DF7")
    Jump("loc_E0C")

    label("loc_DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_E0C")
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)

    label("loc_E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_E1D")
    OP_24(0x7B)
    Jump("loc_E39")

    label("loc_E1D")

    SoundDistance(0x7B, 0xFFFFB32A, 0x99C, 0xFFFFC324, 0x2710, 0x186A0, 0x64, 0x0)

    label("loc_E39")

    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -16000, -1500, 16000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 12000, -1500, -12000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 12000, -1500, 16000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_3_DB1 end

    def Function_4_EF4(): pass

    label("Function_4_EF4")

    Call(0, 37)
    Return()

    # Function_4_EF4 end

    def Function_5_EF8(): pass

    label("Function_5_EF8")

    Call(0, 37)
    Return()

    # Function_5_EF8 end

    def Function_6_EFC(): pass

    label("Function_6_EFC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F99")

    ChrTalk(
        0xFE,
        "The station is currently experiencing heavy congestion.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please take care to not get separated from your\x01",
            "loved ones or belongings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1106")

    label("loc_F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_FFA")

    ChrTalk(
        0xFE,
        (
            "I led the parade through\x01",
            "the entire city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*huff* *huff* Man, I'm beat...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1106")

    label("loc_FFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_10B3")

    ChrTalk(
        0xFE,
        (
            "The Metropolitan Division has been tasked\x01",
            "with patrolling the parade all by themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's too darn crowded to act as any\x01",
            "sort of meaningful security, though!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1106")

    label("loc_10B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_10C1")
    Jump("loc_1106")

    label("loc_10C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1106")

    ChrTalk(
        0xFE,
        "Keep it moving! No pushing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Don't block any cars!\x02",
    )

    CloseMessageWindow()

    label("loc_1106")

    TalkEnd(0xFE)
    Return()

    # Function_6_EFC end

    def Function_7_110A(): pass

    label("Function_7_110A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1240")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B1")
    OP_4B(0xA, 0xFF)
    TurnDirection(0xFE, 0xA, 0)

    ChrTalk(
        0xFE,
        "Are you tired, Abby?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My poor child. Don't worry, Mom's\x01",
            "going to give you a piggyback ride!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Really?! Yaaay!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_123B")

    label("loc_11B1")


    ChrTalk(
        0xFE,
        (
            "Abby's wiped out from having played\x01",
            "at the festival all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can understand it, though.\x01",
            "I may have overindulged a bit myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123B")

    Jump("loc_147D")

    label("loc_1240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_12E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125B")
    Call(0, 8)
    Jump("loc_12DF")

    label("loc_125B")


    ChrTalk(
        0xFE,
        (
            "I'm glad we were able to make some\x01",
            "pleasant memories this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Isn't Crossbell's Anniversary Festival\x01",
            "utterly fantastic?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12DF")

    Jump("loc_147D")

    label("loc_12E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1361")
    TurnDirection(0xFE, 0xA, 0)

    ChrTalk(
        0xFE,
        "Hey, look over there! That's the parade.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It goes around the whole city while\x01",
            "they play music.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_147D")

    label("loc_1361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_13E9")
    OP_4B(0xA, 0xFF)
    TurnDirection(0xFE, 0xA, 0)

    ChrTalk(
        0xFE,
        "How does it taste, Abby?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "May I have some, too, dear?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Sure, Mom!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Let's eat it together!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_147D")

    label("loc_13E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_147D")

    ChrTalk(
        0xFE,
        (
            "I only recently moved to Crossbell,\x01",
            "so this is my first time experiencing the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to say, I'm incredibly impressed.\x02",
    )

    CloseMessageWindow()

    label("loc_147D")

    TalkEnd(0xFE)
    Return()

    # Function_7_110A end

    def Function_8_1481(): pass

    label("Function_8_1481")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)

    ChrTalk(
        0x9,
        "That was sooo much fun!\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xA,
        "Yeah, that was awesome!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_8_1481 end

    def Function_9_14F2(): pass

    label("Function_9_14F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_152A")
    TurnDirection(0xFE, 0x9, 0)

    ChrTalk(
        0xFE,
        "Mom, I'm getting sleepy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_15F2")

    label("loc_152A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_153B")
    Call(0, 8)
    Jump("loc_15F2")

    label("loc_153B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1562")

    ChrTalk(
        0xFE,
        "What's a 'pa-raid'?\x02",
    )

    CloseMessageWindow()
    Jump("loc_15F2")

    label("loc_1562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_15A7")

    ChrTalk(
        0xFE,
        "Mom bought me some ice cream.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's so tasty!\x02",
    )

    CloseMessageWindow()
    Jump("loc_15F2")

    label("loc_15A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_15F2")
    TurnDirection(0xFE, 0x9, 0)

    ChrTalk(
        0xFE,
        "Wow, look at all the confetti!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's so colorful!\x02",
    )

    CloseMessageWindow()

    label("loc_15F2")

    TalkEnd(0xFE)
    Return()

    # Function_9_14F2 end

    def Function_10_15F6(): pass

    label("Function_10_15F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1620")
    Call(0, 43)
    Return()

    label("loc_1620")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_162D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CD1")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_167E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_167E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169E")
    OP_AF(0x80)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CCC")

    label("loc_169E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B2")
    Jump("loc_1CCC")

    label("loc_16B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CCC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1873")

    ChrTalk(
        0xFE,
        "Hey, were you actually able to apprehend the thieves?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, thank Aidios!\x01",
            "I was worried I'd never see my mira again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like to give you this reward as a token\x01",
            "of my gratitude.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1CF, 1)

    ChrTalk(
        0x104,
        "#0300FThanks a bunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really can't thank you enough for your help.\x01",
            "I hope I'll be able to serve you next time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBC, 7)
    Jump("loc_1CCC")

    label("loc_1873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1981")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F2")

    ChrTalk(
        0xFE,
        "The police are out in full force today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, yeah. Today's the closing ceremony, isn't it?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_197C")

    label("loc_18F2")


    ChrTalk(
        0xFE,
        (
            "It's the last day of the festival,\x01",
            "yet the streets are packed with tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I bet everyone came to watch the closing ceremony.\x02",
    )

    CloseMessageWindow()

    label("loc_197C")

    Jump("loc_1CCC")

    label("loc_1981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1A6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A2A")

    ChrTalk(
        0xFE,
        (
            "Oh, crap. This isn't good...\x01",
            "I've totally run out of orange coffee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My apologies, but please have your order\x01",
            "ready before we speak!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A6A")

    label("loc_1A2A")


    ChrTalk(
        0xFE,
        (
            "The day's been jam-packed.\x01",
            "I haven't had a moment of rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6A")

    Jump("loc_1CCC")

    label("loc_1A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1BE6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B07")

    ChrTalk(
        0xFE,
        (
            "I was conversing with customers and managed\x01",
            "to drop my guard for a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* My poor sales...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BE1")

    label("loc_1B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B84")

    ChrTalk(
        0xFE,
        (
            "Doesn't look like it'll be much longer until the\x01",
            "cars for the parade arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm pretty excited.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BE1")

    label("loc_1B84")


    ChrTalk(
        0xFE,
        (
            "It's almost time for the parade to start...\x01",
            "I can feel my heart racing with excitement!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BE1")

    Jump("loc_1CCC")

    label("loc_1BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C72")

    ChrTalk(
        0xFE,
        "There's an event being run at City Hall today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I noticed some scholarly-looking people\x01",
            "gathering there all morning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCC")

    label("loc_1C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1CCC")

    ChrTalk(
        0xFE,
        "Welcome, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wow, I'm surprised at how many customers there are.\x02",
    )

    CloseMessageWindow()

    label("loc_1CCC")

    Jump("loc_162D")

    label("loc_1CD1")

    TalkEnd(0xFE)
    Return()

    # Function_10_15F6 end

    def Function_11_1CD5(): pass

    label("Function_11_1CD5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1D72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D34")

    ChrTalk(
        0xFE,
        "The festival's almost over...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...so I'm going all out!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D6D")

    label("loc_1D34")


    ChrTalk(
        0xFE,
        (
            "Where do I even begin?! I want to\x01",
            "visit EVERYTHING!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D6D")

    Jump("loc_220F")

    label("loc_1D72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1E67")

    ChrTalk(
        0xFE,
        "The mayor's speech was pleasant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Not to mention, Mishy was super nice, too!\x02",
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
        "#0003F(What's he even talking about...?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_220F")

    label("loc_1E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F41")

    ChrTalk(
        0xFE,
        (
            "I know it's fine to splurge during the festival period,\x01",
            "but you should remember to moderate yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's nothing wrong with a bit of self-control.\x01",
            "You'll thank yourself later!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F7F")

    label("loc_1F41")


    ChrTalk(
        0xFE,
        "Do you have a camera on you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The parade's starting!\x02",
    )

    CloseMessageWindow()

    label("loc_1F7F")

    Jump("loc_220F")

    label("loc_1F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_210E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207D")

    ChrTalk(
        0xFE,
        "Ahem... A symposium is being held at City Hall today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Scholars from all over the continent have\x01",
            "gathered at the mayor's request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Their discussions are bound to be enlightening,\x01",
            "so you won't want to miss it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2109")

    label("loc_207D")


    ChrTalk(
        0xFE,
        "A symposium is being held at City Hall today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not the biggest fan of formal events,\x01",
            "so I won't be checking it out for myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2109")

    Jump("loc_220F")

    label("loc_210E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_220F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2191")

    ChrTalk(
        0xFE,
        (
            "I heard of something called...Armorican\x01",
            "omelet rice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sounds good. I think I'll give it a try.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_220F")

    label("loc_2191")


    ChrTalk(
        0xFE,
        (
            "I can't stand hearing about something\x01",
            "and not going to check it out myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm definitely going to have to try it.\x02",
    )

    CloseMessageWindow()

    label("loc_220F")

    TalkEnd(0xFE)
    Return()

    # Function_11_1CD5 end

    def Function_12_2213(): pass

    label("Function_12_2213")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2224")
    Jump("loc_2392")

    label("loc_2224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2232")
    Jump("loc_2392")

    label("loc_2232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2240")
    Jump("loc_2392")

    label("loc_2240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_224E")
    Jump("loc_2392")

    label("loc_224E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233B")

    ChrTalk(
        0xFE,
        (
            "I managed to sneak in a little break\x01",
            "during work. Too bad it's so noisy\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The diet's budget meeting begins\x01",
            "the week after the Anniversary Festival.\x01",
            "Now's not the time to be fooling around.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2392")

    label("loc_233B")


    ChrTalk(
        0xFE,
        (
            "Ugh, I'm so frustrated. Now's not the time\x01",
            "to be fooling around, yet here we are.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2392")

    TalkEnd(0xFE)
    Return()

    # Function_12_2213 end

    def Function_13_2396(): pass

    label("Function_13_2396")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23F4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_23F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2414")
    OP_AF(0x81)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F25")

    label("loc_2414")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2428")
    Jump("loc_2F25")

    label("loc_2428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F25")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_253C")

    ChrTalk(
        0xFE,
        (
            "Hmm, doesn't look like we'll be attracting\x01",
            "any more customers to the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think this year's rush is already over.\x01",
            "It's probably time to close up shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's your last chance to purchase something\x01",
            "while you still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F25")

    label("loc_253C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_25FA")

    ChrTalk(
        0xFE,
        (
            "We've reached the home stretch. I'll try and\x01",
            "liquidate any inventory I still have left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Interested in anything you see?\x01",
            "I can help you out if you have any questions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F25")

    label("loc_25FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2B97")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_276A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E4")

    ChrTalk(
        0xFE,
        (
            "I just received word that the\x01",
            "thief was caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I've been giving the CPD\x01",
            "less credit than they deserve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, this is the first time I've ever\x01",
            "had any faith in them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2765")

    label("loc_26E4")


    ChrTalk(
        0xFE,
        "Now I can continue running my stall without worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to do everything I can to attract more\x01",
            "people to my village.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2765")

    Jump("loc_2B92")

    label("loc_276A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AE8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_299B")

    ChrTalk(
        0x101,
        (
            "#0001FExcuse me, may I borrow a moment of your time?\x02\x03",
            "We're currently investigating a chain of thefts\x01",
            "in the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*nervous sweating*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I'm not too worried about it.\x01",
            "I don't think anyone's stupid enough to\x01",
            "commit a crime right in front of CPD headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, maybe I'm a little nervous.\x01",
            "I heard one of the stalls nearby\x01",
            "got targeted by the thief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0101F(I think it's safe to say that he's on high alert.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(I doubt he knows anything about the culprit.\x01",
            "Let's move on.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x9)
    Jump("loc_2AE3")

    label("loc_299B")


    ChrTalk(
        0xFE,
        (
            "My heart won't stop racing, but I don't think\x01",
            "anyone's stupid enough to commit a crime\x01",
            "right in front of CPD headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I'm not too worried about it.\x01",
            "I'm sure I won't run into any problems, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(There's no way the culprit has the nerve to commit\x01",
            "a theft a few arge away from the department, right?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE3")

    Jump("loc_2B92")

    label("loc_2AE8")


    ChrTalk(
        0xFE,
        "I just received contact from Armorica Village.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've managed to reel in quite a few\x01",
            "tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'd be nice if this drives more traffic\x01",
            "to the village...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B92")

    Jump("loc_2F25")

    label("loc_2B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2D64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA5")

    ChrTalk(
        0xFE,
        "Armorica's speciality items are selling well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're even managing to drive some tourists\x01",
            "to the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like to think we've done a half-decent\x01",
            "job of revitalizing the village.\x01",
            "Not to mention, we've still got two days left.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2D5F")

    label("loc_2CA5")


    ChrTalk(
        0xFE,
        (
            "Between our speciality items selling well,\x01",
            "and tourists visiting the village, I'd say\x01",
            "it's a job well done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I managed to accomplish my goal,\x01",
            "despite there being two days left.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5F")

    Jump("loc_2F25")

    label("loc_2D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2F25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E57")

    ChrTalk(
        0xFE,
        (
            "Are you guys interested in trying\x01",
            "some pure Armorican Honey?\x01",
            "It's our village's speciality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The orbal bus near the east exit of\x01",
            "the city will take you to Armorica\x01",
            "Village, if you're interested in visiting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2F25")

    label("loc_2E57")


    ChrTalk(
        0xFE,
        (
            "Armorica is a peaceful village,\x01",
            "immersed in the beautiful surrounding nature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you tired of dealing with the hustle\x01",
            "and bustle of the festival?\x01",
            "Why not come for a visit? We'd love to have you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F25")

    Jump("loc_23A3")

    label("loc_2F2A")

    TalkEnd(0xFE)
    Return()

    # Function_13_2396 end

    def Function_14_2F2E(): pass

    label("Function_14_2F2E")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37AC")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F8C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2F8C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FAC")
    OP_AF(0x81)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37A7")

    label("loc_2FAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FC0")
    Jump("loc_37A7")

    label("loc_2FC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3180")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B3")

    ChrTalk(
        0xFE,
        (
            "Business has died down compared to yesterday,\x01",
            "but it's still pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can return to the village after I've\x01",
            "made it through the day. Just gotta\x01",
            "hang in there and deal with it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_317B")

    label("loc_30B3")


    ChrTalk(
        0xFE,
        (
            "I can't believe it's almost over...\x01",
            "My urban debut went by in an instant,\x01",
            "so it's back to the village life for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I regret not being able to check out Mishelam,\x01",
            "but that's okay. I'll live.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_317B")

    Jump("loc_37A7")

    label("loc_3180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3224")

    ChrTalk(
        0xFE,
        (
            "I guess I should forget about the\x01",
            "business back home for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They can handle their own problems.\x01",
            "I've got my own things to deal with here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A7")

    label("loc_3224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_350B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E5")

    ChrTalk(
        0xFE,
        (
            "Who wants to try some Armorican omelet rice?\x01",
            "It's our specialty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew... I've gotta up the advertising efforts\x01",
            "and sell more of these bad boys.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_334E")

    label("loc_32E5")


    ChrTalk(
        0xFE,
        (
            "I wonder how everybody back at the village\x01",
            "is doing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Keith is going to be there, as usual...\x02",
    )

    CloseMessageWindow()

    label("loc_334E")

    Jump("loc_3506")

    label("loc_3353")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_340A")

    ChrTalk(
        0xFE,
        "*stare*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys look pretty suspicious.\x01",
            "You know that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll boot you outta here so fast if I catch\x01",
            "you messing with my stall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3506")

    label("loc_340A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_349D")

    ChrTalk(
        0xFE,
        "I'm exhausted!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I managed to survive solely off of the\x01",
            "recipe my father taught me,\x01",
            "but doing this alone is really hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3506")

    label("loc_349D")


    ChrTalk(
        0xFE,
        (
            "I wonder how everybody back at the village\x01",
            "is doing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Keith is going to be there, as usual...\x02",
    )

    CloseMessageWindow()

    label("loc_3506")

    Jump("loc_37A7")

    label("loc_350B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_36A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3614")

    ChrTalk(
        0xFE,
        "Another day, another insane crowd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't even look away for more than\x01",
            "a few seconds without worrying about\x01",
            "another massive line forming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You city folk sure are strange...\x01",
            "Who'd line up all day just to eat a bowl of rice?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_369E")

    label("loc_3614")


    ChrTalk(
        0xFE,
        (
            "You city folk sure are strange...\x01",
            "Who'd line up all day just to eat a bowl of rice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd just give up and go eat something else.\x02",
    )

    CloseMessageWindow()

    label("loc_369E")

    Jump("loc_37A7")

    label("loc_36A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_37A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_373F")

    ChrTalk(
        0xFE,
        (
            "Here's a dish from the Ash Tree Inn\x01",
            "out in Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a rare chance to try something new,\x01",
            "so don't be shy!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_37A7")

    label("loc_373F")


    ChrTalk(
        0xFE,
        (
            "*sigh* I didn't think I'd get roped into\x01",
            "doing this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, whatever. At least I'm having fun.\x02",
    )

    CloseMessageWindow()

    label("loc_37A7")

    Jump("loc_2F3B")

    label("loc_37AC")

    TalkEnd(0xFE)
    Return()

    # Function_14_2F2E end

    def Function_15_37B0(): pass

    label("Function_15_37B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_37C1")
    Jump("loc_39B1")

    label("loc_37C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_37CF")
    Jump("loc_39B1")

    label("loc_37CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3946")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38AD")

    ChrTalk(
        0xFE,
        (
            "The bracers have been dispatched\x01",
            "around the city today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm... Not much we can do about it, I suppose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll have to get around this parade\x01",
            "without getting caught up in the chaos.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3941")

    label("loc_38AD")


    ChrTalk(
        0xFE,
        (
            "I don't want to embarrass ourselves\x01",
            "in front of the bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The police have to cooperate with the bracers\x01",
            "and get through this together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3941")

    Jump("loc_39B1")

    label("loc_3946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3954")
    Jump("loc_39B1")

    label("loc_3954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_39B1")

    ChrTalk(
        0xFE,
        "Wow, that's one big crowd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Be careful. There's bound to be trouble afoot.\x02",
    )

    CloseMessageWindow()

    label("loc_39B1")

    TalkEnd(0xFE)
    Return()

    # Function_15_37B0 end

    def Function_16_39B5(): pass

    label("Function_16_39B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_39C6")
    Jump("loc_3E5E")

    label("loc_39C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3A52")

    ChrTalk(
        0xFE,
        "I was in the Harbor District helping the parade escort.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, I'm tired.\x01",
            "Some juice would help wipe away my fatigue.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E5E")

    label("loc_3A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3C02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B6B")

    ChrTalk(
        0xFE,
        "Hey, thanks for the help yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wouldn't expect anything less from the\x01",
            "ones that managed to get the upper hand\x01",
            "on a case from the First Division!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FHaha, no. See, here's the thing--\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What are you getting all embarrassed for?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3BFD")

    label("loc_3B6B")


    ChrTalk(
        0xFE,
        (
            "We were recruited to help act as security\x01",
            "for the parade as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sheesh, don't think I'll be escaping\x01",
            "from these crowds any time soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BFD")

    Jump("loc_3E5E")

    label("loc_3C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3C10")
    Jump("loc_3E5E")

    label("loc_3C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3E5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D8C")

    ChrTalk(
        0xFE,
        (
            "We're in hot pursuit of a thief.\x01",
            "These scumbags take advantage of\x01",
            "poor festival goers every year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, when I get my hands on him...\x01",
            "I'm going to teach him a lesson or three.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FA-Aren't you enjoying this a bit too much?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha, I guess you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's somethin' about simple crimes\x01",
            "like theft that get me goin', y'know?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3E5E")

    label("loc_3D8C")


    ChrTalk(
        0xFE,
        (
            "I love dealing with them 'cause they're\x01",
            "easy enough for me to turn my brain off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't have to worry about stepping on any toes\x01",
            "due to a complex political climate, or any of that\x01",
            "other mumbo jumbo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E5E")

    TalkEnd(0xFE)
    Return()

    # Function_16_39B5 end

    def Function_17_3E62(): pass

    label("Function_17_3E62")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F3D")

    ChrTalk(
        0xFE,
        (
            "Oh, yeah. I forgot they were going to use\x01",
            "all of these cars for this year's parade.\x02",
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
            "Huh, I don't think this is all of them.\x01",
            "I could have sworn I saw seven of them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3FA2")

    label("loc_3F3D")


    ChrTalk(
        0xFE,
        (
            "The security team can't inspect the cars being\x01",
            "used for the parade if they aren't all lined up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FA2")

    TalkEnd(0xFE)
    Return()

    # Function_17_3E62 end

    def Function_18_3FA6(): pass

    label("Function_18_3FA6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4032")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC4")
    Call(0, 19)
    Jump("loc_402D")

    label("loc_3FC4")


    ChrTalk(
        0xFE,
        (
            "I'm thinking about ditching the festival early,\x01",
            "since the last day is bound to be insanely crowded.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402D")

    Jump("loc_4098")

    label("loc_4032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4098")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_404D")
    Call(0, 19)
    Jump("loc_4098")

    label("loc_404D")


    ChrTalk(
        0xFE,
        (
            "That Armorican honey was amazing!\x01",
            "I'll need to try it again sometime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4098")

    TalkEnd(0xFE)
    Return()

    # Function_18_3FA6 end

    def Function_19_409C(): pass

    label("Function_19_409C")

    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)
    TurnDirection(0x13, 0x14, 0)
    TurnDirection(0x14, 0x13, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4127")

    ChrTalk(
        0x13,
        (
            "The parade was very enjoyable, but it's\x01",
            "about time we return to the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "All right, Mom.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4231")

    label("loc_4127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4231")

    ChrTalk(
        0x13,
        (
            "Oh, wow! I'm surprised at how well our\x01",
            "village specialities sold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Hey, Stefan, look at this!\x01",
            "They sell this honey at the store by our house!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Huh? Oh, yeah. Cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Sheesh, this kid can't show\x01",
            "the slightest bit of enthusiasm.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0x0, 0x0)
    OP_93(0x14, 0x0, 0x0)

    label("loc_4231")

    OP_4C(0x13, 0xFF)
    OP_4C(0x14, 0xFF)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_19_409C end

    def Function_20_4240(): pass

    label("Function_20_4240")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_429A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_425E")
    Call(0, 19)
    Jump("loc_4295")

    label("loc_425E")


    ChrTalk(
        0xFE,
        (
            "This is making me want to go\x01",
            "back to the village.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4295")

    Jump("loc_435B")

    label("loc_429A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_435B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42B5")
    Call(0, 19)
    Jump("loc_435B")

    label("loc_42B5")


    ChrTalk(
        0xFE,
        (
            "I think this is the first time I've ever seen\x01",
            "that honey being sold before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've gotta say, looking at it from up close\x01",
            "is making me want to give it a try.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_435B")

    TalkEnd(0xFE)
    Return()

    # Function_20_4240 end

    def Function_21_435F(): pass

    label("Function_21_435F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_441A")

    ChrTalk(
        0xFE,
        (
            "The closing ceremony will be held\x01",
            "inside of the reception hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Security guards for the venue will usher folks\x01",
            "into the hall, so we've got a ton of work to do!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45C7")

    label("loc_441A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4428")
    Jump("loc_45C7")

    label("loc_4428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4516")

    ChrTalk(
        0xFE,
        (
            "We depart at 10:00 and arrive at the\x01",
            "Entertainment District at 10:30.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's going to be a large crowd\x01",
            "in front of Arc en Ciel, Chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please direct the pedestrians in a manner\x01",
            "that won't disrupt the parade.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45C7")

    label("loc_4516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_45BE")

    ChrTalk(
        0xFE,
        (
            "There's a symposium being held at\x01",
            "City Hall's reception hall today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mayor MacDowell will be participating,\x01",
            "so we've got to keep security tight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45C7")

    label("loc_45BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_45C7")

    label("loc_45C7")

    TalkEnd(0xFE)
    Return()

    # Function_21_435F end

    def Function_22_45CB(): pass

    label("Function_22_45CB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "The parade is happening today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It moves fairly slow, but it'll be cutting through the crowd.\x01",
            "I'd better make sure I don't lose my bearings.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_45CB end

    def Function_23_4668(): pass

    label("Function_23_4668")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4870")

    ChrTalk(
        0xFE,
        (
            "#1006FSonuva... What's the big idea?\x01",
            "Why'd they have to call me, too?\x02\x03",
            "#1000FHey. Do my work for me, thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FNo can do, Chief. We've got our own\x01",
            "requests to deal with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHow 'bout you get off your lazy ass\x01",
            "and do some work for once?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "#1000FYou kids are only running your mouths\x01",
            "'cause you don't know how much of\x01",
            "a pain in the ass it is to direct the parade.\x02\x03",
            "#1006FDamn it... I would have thought my rank\x01",
            "woulda put me way above doing chores.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_4929")

    label("loc_4870")


    ChrTalk(
        0xFE,
        (
            "#1003F*puff*...\x01",
            "I think I'll pull a fast one and disappear.\x02\x03",
            "It's too big a pain in my ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FPlease attempt to conduct yourself as an\x01",
            "adult every once in a while, Chief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4929")

    TalkEnd(0xFE)
    Return()

    # Function_23_4668 end

    def Function_24_492D(): pass

    label("Function_24_492D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_497C")

    ChrTalk(
        0xFE,
        (
            "Aw, it's the last day already.\x01",
            "I don't want this to end.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B41")

    label("loc_497C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_49E6")

    ChrTalk(
        0xFE,
        (
            "There are plenty of stores in\x01",
            "Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wouldn't worry too much about it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B41")

    label("loc_49E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4A5A")

    ChrTalk(
        0xFE,
        "There's a large event happening today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I came all the way from the countryside\x01",
            "to see this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B41")

    label("loc_4A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4AEC")

    ChrTalk(
        0xFE,
        (
            "I believe it's called 'Crossbell: One and\x01",
            "the Same.'\x01",
            "...Or something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like the symposium is\x01",
            "beginning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B41")

    label("loc_4AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4B41")

    ChrTalk(
        0xFE,
        (
            "Ah, a spectacle truly befitting of Crossbell's\x01",
            "City Hall. Magnificent!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B41")

    TalkEnd(0xFE)
    Return()

    # Function_24_492D end

    def Function_25_4B45(): pass

    label("Function_25_4B45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4BFD")

    ChrTalk(
        0xFE,
        (
            "The last thing I need to do is hit up all of\x01",
            "these delicious-looking food stalls!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "First on the menu is this delicious omelette\x01",
            "from Whatchamacallit Village!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D96")

    label("loc_4BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4C68")

    ChrTalk(
        0xFE,
        "Darn it. My photo-quartz broke.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can I purchase a replacement\x01",
            "anywhere around here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D96")

    label("loc_4C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4CD4")

    ChrTalk(
        0xFE,
        "The leading car has made its move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll need to take an amazing photograph of this!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D96")

    label("loc_4CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4D64")

    ChrTalk(
        0xFE,
        (
            "There's some kind of event going on\x01",
            "at City Hall today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Staff members have been frantically\x01",
            "running around all morning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D96")

    label("loc_4D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4D96")

    ChrTalk(
        0xFE,
        "I've gotta snap me a photo of this!\x02",
    )

    CloseMessageWindow()

    label("loc_4D96")

    TalkEnd(0xFE)
    Return()

    # Function_25_4B45 end

    def Function_26_4D9A(): pass

    label("Function_26_4D9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4E21")

    ChrTalk(
        0xFE,
        (
            "Actually, hold on a sec.\x01",
            "Do I even have any mira on me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, dangit. Guess I'll go withdraw some\x01",
            "at the IBC.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_500E")

    label("loc_4E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4E7D")

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival didn't fail to deliver\x01",
            "on my high expectations!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_500E")

    label("loc_4E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4EF4")

    ChrTalk(
        0xFE,
        (
            "I've got a gut feeling that the parade will\x01",
            "come through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey, you! Get the camera ready!\x02",
    )

    CloseMessageWindow()
    Jump("loc_500E")

    label("loc_4EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4F7D")

    ChrTalk(
        0xFE,
        (
            "All these police officers look like\x01",
            "they're on edge today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha! What's the matter with 'em?\x01",
            "Something going on?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_500E")

    label("loc_4F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_500E")

    ChrTalk(
        0xFE,
        (
            "Time to party my ass off like it's going\x01",
            "outta style!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm in Crossbell during the festival,\x01",
            "so of COURSE I'm gonna let loose!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_500E")

    TalkEnd(0xFE)
    Return()

    # Function_26_4D9A end

    def Function_27_5012(): pass

    label("Function_27_5012")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5078")

    ChrTalk(
        0xFE,
        "All right, I don't care if it kills me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm going shopping today, damn it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_52C1")

    label("loc_5078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_512E")

    ChrTalk(
        0xFE,
        (
            "I'm happy the festival's here, but\x01",
            "I haven't gone shopping a SINGLE time yet!\x01",
            "I won't stand for this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "CAN'T A GIRL GO SHOPPING?\x01",
            "IS THAT TOO MUCH TO ASK FOR?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52C1")

    label("loc_512E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_51B8")

    ChrTalk(
        0xFE,
        (
            "Aww, I wanted to check out the\x01",
            "department store in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're going to end up missing\x01",
            "the parade, though!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52C1")

    label("loc_51B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5247")

    ChrTalk(
        0xFE,
        (
            "Listen here, you.\x01",
            "You promised to take me shopping, didn't you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So why in the HELL are we only going\x01",
            "to food stalls?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52C1")

    label("loc_5247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_52C1")

    ChrTalk(
        0xFE,
        "I. Want. To. Go. Shopping.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm over it! No more sightseeing!\x01",
            "The only sights I'm seeing are the sales!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52C1")

    TalkEnd(0xFE)
    Return()

    # Function_27_5012 end

    def Function_28_52C5(): pass

    label("Function_28_52C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5329")

    ChrTalk(
        0xFE,
        "I've got so much work to do today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Good luck with your duties, everyone!\x02",
    )

    CloseMessageWindow()
    Jump("loc_53BB")

    label("loc_5329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5337")
    Jump("loc_53BB")

    label("loc_5337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5345")
    Jump("loc_53BB")

    label("loc_5345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_53B2")

    ChrTalk(
        0xFE,
        (
            "The senior officer and I are on\x01",
            "guard duty today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can feel the tension in the air!\x02",
    )

    CloseMessageWindow()
    Jump("loc_53BB")

    label("loc_53B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_53BB")

    label("loc_53BB")

    TalkEnd(0xFE)
    Return()

    # Function_28_52C5 end

    def Function_29_53BF(): pass

    label("Function_29_53BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_5575")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5472")

    ChrTalk(
        0x18,
        (
            "#2100FOh, yeah, that reminds me.\x01",
            "Don't forget to fork over the photos\x01",
            "after you've finished taking them.\x02\x03",
            "I'm counting on ya! ♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 4)
    Jump("loc_5570")

    label("loc_5472")


    ChrTalk(
        0x18,
        (
            "#2100FApparently, this year's parade is going\x01",
            "to have the largest attendance yet.\x02\x03",
            "#2104FI'm getting real fired up now!\x01",
            "I'll snap photos from angles unimaginable\x01",
            "and expose everything for what it's worth!\x02\x03",
            "#2109FReady or not, here I come, world!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)

    label("loc_5570")

    Jump("loc_5793")

    label("loc_5575")

    OP_4B(0x19, 0xFF)

    ChrTalk(
        0x101,
        (
            "#0000FHey, Grace.\x01",
            "Are you covering the parade?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#2100FYou know it! Apparently, this year's parade\x01",
            "is going to have the largest attendance yet,\x01",
            "so you know I gotta be there!\x02\x03",
            "#2104FI'm getting real fired up now!\x01",
            "I'll snap photos from angles unimaginable\x01",
            "and expose everything for what it's worth!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x19, 300)

    ChrTalk(
        0x18,
        (
            "#2109FAre you getting pumped, Reins?!\x01",
            "Tell me you're getting pumped!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 300)

    ChrTalk(
        0x19,
        "I'm getting pumped, ma'am!\x02",
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
    OP_93(0x19, 0x2D, 0x0)
    SetScenarioFlags(0x1, 3)
    OP_4C(0x19, 0xFF)

    label("loc_5793")

    TalkEnd(0xFE)
    Return()

    # Function_29_53BF end

    def Function_30_5797(): pass

    label("Function_30_5797")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_57FC")

    ChrTalk(
        0xFE,
        (
            "Oh, man! I can't contain myself!\x01",
            "There's only 30 minutes left until it starts!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58AA")

    label("loc_57FC")


    ChrTalk(
        0xFE,
        "F-Finally! The parade's finally starting!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think some of the photographs from today\x01",
            "might get featured in international newspapers,\x01",
            "and it's making me nervous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_58AA")

    TalkEnd(0xFE)
    Return()

    # Function_30_5797 end

    def Function_31_58AE(): pass

    label("Function_31_58AE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5942")
    Jump("loc_598C")

    label("loc_5942")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5962")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_598C")

    label("loc_5962")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5982")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_598C")

    label("loc_5982")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_598C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5A47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59CC")
    Call(0, 35)
    Jump("loc_5A47")

    label("loc_59CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59DE")
    Call(0, 36)
    Jump("loc_5A47")

    label("loc_59DE")


    ChrTalk(
        0x1A,
        (
            "#0804FLooks like the festival is in full swing.\x02\x03",
            "#0802FTime to join forces and kick butt, everyone!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A47")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_58AE end

    def Function_32_5A4F(): pass

    label("Function_32_5A4F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5AE3")
    Jump("loc_5B2D")

    label("loc_5AE3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B03")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B2D")

    label("loc_5B03")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B23")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B2D")

    label("loc_5B23")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5B2D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5C3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B6D")
    Call(0, 35)
    Jump("loc_5C3C")

    label("loc_5B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B7F")
    Call(0, 36)
    Jump("loc_5C3C")

    label("loc_5B7F")


    ChrTalk(
        0x1B,
        (
            "#0903FCrossbell's an international trade city,\x01",
            "so there's a lot of tourists from abroad.\x02\x03",
            "#0908FWe'll need to keep a close eye on things so we\x01",
            "can avoid any trouble before it happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C3C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_5A4F end

    def Function_33_5C44(): pass

    label("Function_33_5C44")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5F00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E42")

    ChrTalk(
        0xFE,
        (
            "We're a part of the parade's security detail.\x01",
            "It should be starting any moment now,\x01",
            "so keep your wits about you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a good thing we were mobilized.\x01",
            "I doubt anybody would think for a second\x01",
            "about messing with the show with us on guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FTrue that. You guys are real combat pros.\x02\x03",
            "#0309FI bet most sane people would piss their pants\x01",
            "after catchin' a bracer staring daggers at 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FY-Yeah. I can't deny that you're far more\x01",
            "intimidating than we are.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_5F00")

    label("loc_5E42")


    ChrTalk(
        0xFE,
        (
            "Well, it's not like we DON'T rely on you guys.\x01",
            "I feel like your team has gotten much more\x01",
            "reliable these past couple of months.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(O-Oh... I wasn't expecting praise from her.)\x02",
    )

    CloseMessageWindow()

    label("loc_5F00")

    TalkEnd(0xFE)
    Return()

    # Function_33_5C44 end

    def Function_34_5F04(): pass

    label("Function_34_5F04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5F76")

    ChrTalk(
        0xFE,
        "Working hard, officers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The crowd is especially large today,\x01",
            "so do try to be careful, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F76")

    TalkEnd(0xFE)
    Return()

    # Function_34_5F04 end

    def Function_35_5F7A(): pass

    label("Function_35_5F7A")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4450, 3750, -13280, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15650, 0)
    SetChrPos(0x101, -4650, 2500, -14600, 0)
    SetChrPos(0x102, -3800, 2500, -14700, 0)
    SetChrPos(0x103, -4650, 2500, -15750, 0)
    SetChrPos(0x104, -3800, 2500, -15850, 0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_0D()

    ChrTalk(
        0x1A,
        "#0809F#5PHeya, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#0902FHow's your day been?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FThe festival leaves us with little room\x01",
            "to breathe, but it hasn't been that bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0202FAre you two working today, as well?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#0804F#5PYeah, but we're just catching our breath.\x02\x03",
            "#0802FHoly moly, though! I wasn't expecting the\x01",
            "Anniversary Festival to be this huge!\x02\x03",
            "#0803FThis whole event might actually be\x01",
            "even more bombastic than the\x01",
            "queen's birthday celebration!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FThe queen's birthday celebration?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#0904FOh, she's referring to Queen Alicia II.\x01",
            "We celebrate her birthday every year\x01",
            "by holding a festival.\x02\x03",
            "#0900FIt's one of the largest annual events\x01",
            "in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FOh, that's right. I forgot you guys are Liberlian.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FI've actually been to it before, believe it or not.\x02\x03",
            "#0102FThe elegance and flashiness of the festival\x01",
            "was truly befitting of a monarch. It was an\x01",
            "unforgettable experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#0809F#5PGlad to hear you enjoyed yourself.\x02\x03",
            "#0802FIt's not just flashy, though! They even hold\x01",
            "a martial arts tournament at the arena!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FTournament, eh? Sounds like it's right\x01",
            "up my alley.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 2500, -14600, 0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    EndChrThread(0xC, 0x0)
    SetChrPos(0xC, 8370, 2390, -14850, 90)
    BeginChrThread(0xC, 0, 0, 1)
    SetScenarioFlags(0xB3, 7)
    EventEnd(0x5)
    Return()

    # Function_35_5F7A end

    def Function_36_649A(): pass

    label("Function_36_649A")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4450, 3750, -13280, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15650, 0)
    SetChrPos(0x101, -4650, 2500, -14600, 0)
    SetChrPos(0x102, -3800, 2500, -14700, 0)
    SetChrPos(0x103, -4650, 2500, -15750, 0)
    SetChrPos(0x104, -3800, 2500, -15850, 0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_0D()

    ChrTalk(
        0x1A,
        (
            "#0801F#5POh, yeah, I just remembered!\x02\x03",
            "#0802FCongrats, guys! You should be\x01",
            "really proud of yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FP-Proud...? Are you talking about the\x01",
            "assassination attempt?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FIt was more of a mountain of coincidences piling\x01",
            "up on top of each other. I'm afraid to think what\x01",
            "would've happened if we weren't as lucky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#0904FI wouldn't get hung up on that. Besides, if you\x01",
            "hadn't thwarted the assailant, I doubt we would\x01",
            "be here enjoying the festival like we are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#0809F#5PYeah, that's right! If you think about it, everyone\x01",
            "here owes you big time! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FHaha, thanks, you two.\x01",
            "(I'm not used to this much praise.\x01",
            "I don't look embarrassed, do I?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0304F(Red as an apple, my friend.)\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 2500, -14600, 0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    EndChrThread(0xC, 0x0)
    SetChrPos(0xC, 8370, 2390, -14850, 90)
    BeginChrThread(0xC, 0, 0, 1)
    SetScenarioFlags(0xB4, 1)
    EventEnd(0x5)
    Return()

    # Function_36_649A end

    def Function_37_683B(): pass

    label("Function_37_683B")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch02751.itc", 0x1E)
    LoadChrToIndex("chr/ch02702.itc", 0x1F)
    LoadChrToIndex("chr/ch09400.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00254.itc", 0x22)
    SoundLoad(840)
    OP_68(-18400, 3500, -300, 0)
    MoveCamera(90, 23, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -19000, 2500, -600, 45)
    SetChrPos(0x102, -18200, 2500, -1400, 45)
    SetChrPos(0x103, -20000, 2500, -1600, 45)
    SetChrPos(0x104, -19200, 2500, -2400, 45)
    OP_4B(0x23, 0xFF)
    SetChrFlags(0x23, 0x40)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -17700, 2500, 800, 180)
    OP_4B(0x24, 0xFF)
    SetChrFlags(0x24, 0x40)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -17150, 2600, 100, 270)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x0)
    SetChrPos(0x25, -17600, 500, -10200, 0)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis056.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis057.itp")
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    OP_0D()
    TurnDirection(0x23, 0x101, 300)

    ChrTalk(
        0x23,
        "#3400149V#3605F#5PYou came!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x1)
    Sleep(300)

    ChrTalk(
        0x24,
        "#3400150V#5P#3708FOh, thank Aidios!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    ChrTalk(
        0x101,
        (
            "#3400151V#12P#0001FGood afternoon, Mr. and Mrs. Hayworth.\x02\x03",
            "#3400152VIf I heard correctly, you guys were\x01",
            "watching the parade when you noticed\x01",
            "your son went missing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#3400153V#5P#3701FTh-That's right!\x02\x03",
            "#3400154V#3710FI should have paid more attention... It's all my\x01",
            "fault that he's...he's... Oh, Colin!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x24, 400)
    Sleep(150)

    ChrTalk(
        0x23,
        "#3400155V#3608FSophia, please. We have to stay calm.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x101, 500)

    ChrTalk(
        0x23,
        (
            "#3400156V#3603F#5PI apologize, everyone. She's just worried.\x02\x03",
            "#3400157V#3601FWe lost sight of Colin roughly three hours ago.\x02\x03",
            "#3400158VIt happened when we were watching\x01",
            "the parade pass through this district.\x02\x03",
            "#3400159VSophia noticed almost immediately. We both\x01",
            "searched around this area as hard as we\x01",
            "could, but to no avail.\x02\x03",
            "#3400160V#3610FThings being the way they are...we had no choice\x01",
            "but to call the CPD.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400161V#0102FI think that was a smart move, Mr. Hayworth.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#3400162V#0101F#11PShould we take this into our own hands\x01",
            "and conduct the search ourselves?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E2E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E2E)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x101,
        (
            "#3400163V#6P#0003FYeah. The rest of the force seems swamped\x01",
            "with patrolling the festival.\x02\x03",
            "#3400164V#0001FAnd if that's the case, we'll need to decide how\x01",
            "to divide ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400165V#12P#0203FThat IS the question.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3400166V#0300FWell, I'm thinkin' that we should probably go our\x01",
            "separate ways. We can always keep in contact\x01",
            "with our Enigmas, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#3400167V#5P#3707FP-Please, let me help as well! If I don't...\x02\x03",
            "#3400168V...who knows what might...happen to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#3400169V#3610F#5PSophia, it's going to be okay.\x02\x03",
            "#3400170V#3601FI'm going to escort my wife home for\x01",
            "the time being.\x02\x03",
            "#3400171VWe'll conduct a thorough search of the\x01",
            "neighborhood once we've arrived.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_70F7():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_70F7)
    Sleep(50)

    def lambda_7107():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7107)
    Sleep(50)
    OP_93(0x104, 0x2D, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#3400172V#12P#0000FThat would narrow down our list of places to\x01",
            "search. Good idea, Mr. Hayworth.\x02\x03",
            "#3400173V#0003FEveryone else, we'll split up and conduct our\x01",
            "own searches in the other districts.\x02\x03",
            "#3400174V#0001FNow, Mr. Hayworth, do you have anything that\x01",
            "might help us find him?\x02\x03",
            "#3400175VA clear photo of him would work best.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x23,
        (
            "#3400176V#3605F#5POh, really? We actually had a photo taken of him\x01",
            "during the festival!\x02\x03",
            "#3400177V#3608FHmmm, I have it here somewhere...\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Harold pulled an envelope out of his coat pocket.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x23,
        "#3400178V#3601F#5PHere you are!\x02",
    )

    CloseMessageWindow()

    def lambda_7393():
        OP_9A(0xFE, 0x101, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_7393)
    WaitChrThread(0x23, 1)

    def lambda_73AB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_73AB)

    def lambda_73B8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_73B8)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x327),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x327, 1)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x102,
        "#3400179V#0102FOh, how cute.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#3400180V#0202F#12PIndeed. I almost mistook him as their daughter.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    def lambda_74B3():
        OP_96(0xFE, 0xFFFFBADC, 0x9C4, 0x320, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_74B3)
    WaitChrThread(0x23, 1)
    Sleep(300)
    SetChrSubChip(0x24, 0x0)
    Sleep(300)

    ChrTalk(
        0x24,
        "#3400181V#5P#3710FM-My sweet boy...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x24, 500)

    ChrTalk(
        0x23,
        (
            "#3400182V#3600FCome, now, dear. Let's get out of the heat and\x01",
            "wait for Colin to come home.\x02\x03",
            "#3400183VWho knows? He may be waiting for us now...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x2)
    Sleep(300)

    ChrTalk(
        0x24,
        (
            "#3400184V#11P#3707FHarold! But, what if...?\x01",
            "What if it's happened again?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#3400185V#3601FIt won't! It will NEVER happen again, I swear it!\x02",
    )

    CloseMessageWindow()

    def lambda_763C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_763C)
    Sleep(50)
    OP_93(0x104, 0x2D, 0x1F4)

    ChrTalk(
        0x101,
        "#3400186V#12P#0005F(Did they say...again?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400187V#0108F(Perhaps there's something we're missing.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x101, 300)

    ChrTalk(
        0x23,
        (
            "#3400188V#3610F#5PExcuse us. The heat seems to have gotten\x01",
            "to our heads.\x02\x03",
            "#3400189V#3608FIt's just... This is a lot to deal with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400190V#12P#0004FNo, I completely understand.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3400191V#12P#0005FWhile you're here, do you have any\x01",
            "of Colin's possessions on hand?\x02\x03",
            "#3400192V#0000FOur police dog might be able to pick up\x01",
            "his scent.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x1)

    ChrTalk(
        0x23,
        "#3400193V#3605F#5POh, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "#3400194V#5P#3708FDoes this work? It's his stuffed animal!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x103,
        "#3400195V#0205F#12POh, a Mishy plush?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#3400196V#0103FWe'll make sure to return it once he's found.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x328, 1)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    ChrTalk(
        0x104,
        (
            "#3400197V#0303FWell, let's get a move on.\x02\x03",
            "#3400198V#0300FAs long as he's still in the city, he should be\x01",
            "relatively safe. Leave it to us, Hayworths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#3400199V#3604F#5PY-Yes, thank you.\x02\x03",
            "#3400200V#3601FI leave my son's safety in your hands.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x23, 3, 0, 39)
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x24, 0x20)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x1)
    SetChrPos(0x24, -17700, 2500, 100, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    BeginChrThread(0x24, 3, 0, 39)

    def lambda_7AE4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7AE4)
    Sleep(50)

    def lambda_7AF4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7AF4)
    Sleep(50)

    def lambda_7B04():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7B04)
    Sleep(50)

    def lambda_7B14():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7B14)
    Sleep(3000)
    OP_68(-18350, 3500, -1750, 1200)

    def lambda_7B35():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7B35)
    Sleep(100)

    def lambda_7B45():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7B45)

    def lambda_7B52():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7B52)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#3400201V#5P#0003FNow, how do we want to do this?\x02\x03",
            "#3400202V#0000FActually, we should call him first...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400203V#12P#0204FI can.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x23, 3)
    WaitChrThread(0x24, 3)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sound(831, 0, 100, 0)
    Sound(840, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sound(1205, 255, 95, 0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Sound(1206, 255, 95, 0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_24(0x348)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sound(911, 0, 100, 0)
    Sleep(600)
    Sound(2054, 255, 100, 0)
    Fade(500)
    OP_68(-18400, 3500, -2700, 0)
    MoveCamera(65, 29, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(18500, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    OP_52(0x25, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0x25, 0x1E, 0xC8)

    def lambda_7D86():
        OP_9D(0xFE, 0xFFFFB820, 0x9C4, 0xFFFFEF98, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_7D86)
    Sound(854, 0, 100, 0)
    Sleep(600)
    SetChrSubChip(0x25, 0x1)
    Sound(43, 0, 100, 0)
    Sound(832, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0x25, 0x2)
    WaitChrThread(0x25, 1)
    SetChrChip(0x1, 0x25, 0x0, 0x0)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrSubChip(0x25, 0x0)

    def lambda_7DD7():
        OP_93(0xFE, 0x154, 0x190)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_7DD7)

    def lambda_7DE4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7DE4)

    def lambda_7DF1():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7DF1)

    def lambda_7DFE():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7DFE)

    def lambda_7E0B():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7E0B)
    WaitChrThread(0x25, 2)
    BeginChrThread(0x25, 1, 0, 38)
    Sleep(500)
    Sound(2052, 255, 100, 0)
    Sleep(800)

    ChrTalk(
        0x25,
        "#3400204V#11P#1200FGrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400205V#5P#0002FZeit! Mind giving us a hand?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400206V#5P#0102FWhat a good boy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#3400207V#11P#1203FGrrr... Woof!\x02\x03",
            "#3400208V#1200FGrrrrr...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400209V#6P#0204F'You may rest assured, now that I've arrived.'\x02\x03",
            "#3400210V#2B#47Z#61B#119Z'Following this small child's scent will\x01",
            "be as simple as taking an afternoon nap.'\x02\x03",
            "#3400211V#0202FOr so he says.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3400212V#5P#0012FTh-Thanks, Zeit.\x02\x03",
            "#3400213V#0000FActually, how did he already know the\x01",
            "details of the case?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3400214V#5P#0300FEavesdroppin', I bet! This guy can never\x01",
            "pass the opportunity to show us up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400215V#5P#0104FWhatever the case, let's get back on topic.\x02",
    )

    CloseMessageWindow()
    OP_68(-19100, 3500, -1700, 1000)
    MoveCamera(75, 27, 0, 1000)
    Sleep(500)
    TurnDirection(0x102, 0x101, 500)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#3400216V#11P#0100FIn a city as large as this, how should we\x01",
            "divide and conquer?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_81A1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_81A1)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#3400217V#12P#0204FI will accompany Zeit, obviously.\x02\x03",
            "#3400218V#0202FIt would be illogical for someone that does\x01",
            "not understand him to go with him.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#3400219V#0003F#5PFair enough.\x02\x03",
            "#3400220V#0000FI'll leave the Mishy with you, then.\x02\x03",
            "#3400221VOnce Zeit finds the trail, follow it as far\x01",
            "as you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400222V#12P#0204FRoger.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3400223V#0003F#5PUs three will split up and search the\x01",
            "different districts.\x02\x03",
            "#3400224V#0000FI'll take care of the Entertainment District,\x01",
            "Back Alley, Central Square, Station Street,\x01",
            "and West Street.\x02\x03",
            "#3400225V#0004FRandy, you're in charge of East Street and the\x01",
            "Downtown District.\x02\x03",
            "#3400226VAnd, Elie, you can check out the Administrative\x01",
            "and Harbor Districts.\x02\x03",
            "#3400227V#0000FSound good to you guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3400228V#11P#0105FI mean, yes, but don't you have a lot of ground\x01",
            "to cover?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400229V#0002F#5PWell, think about it. The Administrative and Harbor\x01",
            "Districts are both large and have a lot of traffic\x01",
            "right now. The Downtown District, too, to an extent.\x02\x03",
            "#3400230VMy areas will be pretty easy to make my way through.\x01",
            "I think it's a fair distribution of work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400231V#11P#0102FIt makes sense when you put it that way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3400232V#0304FAll righty! Let's find ourselves a kid!\x02\x03",
            "#3400233V#0300FLet's use our nifty Enigmas to update each\x01",
            "other on our progress. Sound like a plan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400234V#0000F#5PYep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400235V#12P#0202FIf we are in agreement, shall we commence\x01",
            "the search for Colin Hayworth?\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM("ed7000", "ed7000")
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x348)
    SetScenarioFlags(0x5C, 0)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_683B end

    def Function_38_87C4(): pass

    label("Function_38_87C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87E2")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_38_87C4")

    label("loc_87E2")

    Return()

    # Function_38_87C4 end

    def Function_39_87E3(): pass

    label("Function_39_87E3")

    OP_92(0xFE, 0xFFFFB7BC, 0x9C4, 0x1F4)

    def lambda_87F5():
        OP_95(0xFE, -18500, 2500, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_87F5)
    WaitChrThread(0xFE, 1)

    def lambda_8813():
        OP_95(0xFE, -18500, 2500, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8813)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_39_87E3 end

    def Function_40_882D(): pass

    label("Function_40_882D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(885)
    Sound(885, 2, 90, 0)
    FadeToBright(2000, 0)
    LoadEffect(0x7, "event\\ev308_00.eff")
    LoadEffect(0x1, "event\\ev308_01.eff")
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 10930, 2500, 15620, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 4860, 2410, 19070, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 14320, 2410, 9830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 10930, 2500, 15620, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 4860, 2410, 19070, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 14320, 2410, 9830, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_68(-2080, 5260, 6650, 0)
    MoveCamera(58, -2, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(27500, 0)
    OP_68(-2080, 12900, 6650, 8000)
    MoveCamera(33, -15, 0, 8000)
    OP_6E(620, 8000)
    SetCameraDistance(27500, 8000)
    Sleep(1000)
    Sound(856, 0, 100, 0)
    Sleep(6000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x375)
    SetScenarioFlags(0x5C, 3)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_882D end

    def Function_41_8A42(): pass

    label("Function_41_8A42")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-18000, 3600, 26700, 0)
    MoveCamera(50, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -18400, 3100, 31000, 180)
    SetChrPos(0x102, -17600, 3100, 31000, 180)
    SetChrPos(0x103, -18400, 3100, 31000, 180)
    SetChrPos(0x104, -17600, 3100, 31000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    SetCameraDistance(20000, 3000)
    FadeToBright(1000, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x1)

    def lambda_8B61():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8B61)

    def lambda_8B72():
        OP_96(0xFE, 0xFFFFB758, 0x9C4, 0x6590, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B72)
    Sleep(400)

    def lambda_8B8F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8B8F)

    def lambda_8BA0():
        OP_96(0xFE, 0xFFFFBC08, 0x9C4, 0x6590, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8BA0)
    Sleep(400)

    def lambda_8BBD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8BBD)

    def lambda_8BCE():
        OP_96(0xFE, 0xFFFFB758, 0x9C4, 0x6B08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8BCE)
    Sleep(400)

    def lambda_8BEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8BEB)

    def lambda_8BFC():
        OP_96(0xFE, 0xFFFFBC08, 0x9C4, 0x6B08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8BFC)
    WaitChrThread(0x101, 1)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8C97():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8C97)
    Sleep(50)

    def lambda_8CA7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8CA7)

    ChrTalk(
        0x101,
        "#3300048V#5P#0005FA call?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3300049V#0105F#11PHopefully not another emergency.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300050V#5P#0001FYeah.\x02",
    )

    CloseMessageWindow()
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
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3300051V#0001FLloyd Bannings speaking.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300052V\x07\x05",
            "Hah, bingo!\x02\x03",
            "#3300053VWasn't sure if I was gonna reach you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3300054V\x07\x00",
            "#0005FUh... Who is this?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300055V\x07\x05",
            "What? You can't tell by my voice?\x01",
            "Some detective you are.\x02\x03",
            "#3300056VIt's Jona, dummy. Jona Sacred? Y'know,\x01",
            "the amazing, genius hacker?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 42)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3300057V\x07\x00",
            "#0014F#30WWait a second!\x02\x03",
            "#3300059V#3S#0007FHow'd you get this number?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300060V\x07\x05",
            "Pretty easily? All I had to do was run a quick\x01",
            "search of the police database.\x02\x03",
            "#3300061VMan, was the security a joke! I was like water\x01",
            "running through a freakin' strainer.\x02\x03",
            "#3300062VDon't worry, though. It's not like there was any\x01",
            "top secret information in there, anyway.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3300063V\x07\x00",
            "#0011FY-You're kidding me...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x104,
        "#3300064V#0305FWho is it, Lloyd?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3300065V#6P#0006FOur friend, the hacker.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3300066V#0105F#11PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300067V#0211F#5PHe never did know when to quit.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3300068V\x07\x00",
            "#0003FOkay, what do you want?\x02\x03",
            "#3300069V#0001FSurely you didn't call me just to show\x01",
            "off your skills, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300070V\x07\x05",
            "Yeah, I was getting to it.\x02\x03",
            "#3300071VI was actually wondering if I could submit\x01",
            "a request to you guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3300072V\x07\x00",
            "#0005FSeriously?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300073V\x07\x05",
            "Well, not you in particular. I need\x01",
            "Tio's help with something.\x02\x03",
            "#3300074VCould you pass on the message?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3300075V\x07\x00",
            "#0013FWe're already really busy, Jona...\x02\x03",
            "#3300076VIf this is just some private matter,\x01",
            "we can't deal with it right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300077V\x07\x05",
            "Well, private wouldn't be entirely\x01",
            "inaccurate...\x02\x03",
            "#3300078V...but what if I gave you a reward?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3300079V\x07\x00",
            "#0006FWe aren't bracers, you know.\x02\x03",
            "#3300080VIn other words, we don't intend on accepting\x01",
            "any direct compensation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300081V\x07\x05",
            "Oh, wow. Aren't you all high and mighty?\x02\x03",
            "#3300082VAnd I'm not talking about mira, dude.\x02\x03",
            "#3300083VI've got a memory quartz loaded with info\x01",
            "you guys might be interested in...\x02\x03",
            "#3300084VDoes that change things?\x02",
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
            "#3300085V\x07\x00",
            "#0001F...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300086V\x07\x05",
            "Hah! That's what I thought!\x02\x03",
            "#3300087VWell, anyway, just head on over to\x01",
            "my place when you can.\x02\x03",
            "#3300088VI'll fill you in on the details then.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3300089V\x07\x00",
            "#0006F...Fine.\x02",
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
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#3300090V#0105F#11PWhat was all of that about?\x02",
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
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#3300091V#6P#0003FWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained Jona's deal to the others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x102,
        "#3300092V#0103F#11PAn exchange, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3300093V#0306FSheesh, what a rascal.\x02\x03",
            "#3300094V#0301FHe's really tryin' to take advantage of the\x01",
            "cops, don'tcha think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300095V#0203F#5PBe that as it may, it might be smart to go\x01",
            "and at least hear what he has to say.\x02\x03",
            "#3300096V#0202FBesides, he wants my help. Why not flip the\x01",
            "table on Jona and take advantage of him?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9A1E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A1E)
    Sleep(50)

    def lambda_9A2E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9A2E)
    Sleep(50)

    def lambda_9A3E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9A3E)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3300097V#12P#0012FIt feels a little too unethical for my tastes...\x02\x03",
            "#3300098V#0005FBut really, I don't understand why he didn't\x01",
            "call you to begin with, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300099V#0204F#5PThere is a simple answer to that: fear.\x02\x03",
            "#3300100VHe is likely too afraid to face me after\x01",
            "I obliterated him in a puzzle game two\x01",
            "days ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3300101V#12P#0012FI-Is that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3300102V#0102F#11PI'm not sure what this 'puzzle game' is,\x01",
            "but that sounds impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3300103V#11P#0302FIt's clear that Jona's no match for our Tio Tot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300104V#0206F#5PBecause, at his core, he is a spoiled,\x01",
            "petulant child.\x02\x03",
            "#3300105V#0202FBut, if we have time, it would not hurt\x01",
            "to visit Jona.\x02\x03",
            "#3300106VI am interested in seeing what his\x01",
            "request entails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300107V#12P#0000FAll right, then. To the Geofront.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -18000, 2500, 26000, 180)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetScenarioFlags(0xA0, 3)
    OP_29(0x44, 0x1, 0x4)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_41_8A42 end

    def Function_42_9DED(): pass

    label("Function_42_9DED")

    Sleep(900)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Return()

    # Function_42_9DED end

    def Function_43_9E02(): pass

    label("Function_43_9E02")

    EventBegin(0x0)
    OP_4B(0xB, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(5880, 4740, -10040, 0)
    MoveCamera(7, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12150, 0)
    SetChrPos(0x101, 5420, 2500, -7460, 45)
    SetChrPos(0x102, 5120, 2500, -9330, 45)
    SetChrPos(0x103, 6250, 2500, -8390, 45)
    SetChrPos(0x104, 4250, 2500, -8350, 45)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#11PWelcome to Chroma's Juice Stand!\x01",
            "Feeling thirsty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FWasn't this the stand that was robbed?\x02\x03",
            "#0001FExcuse me, would you mind giving us a account\x01",
            "of how the robbery went down? In detail, please.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#11PS-Sure, I guess. It all happened when I let\x01",
            "my guard down for a second.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11P*sigh* My poor sales...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FDo you recall what the suspect looked like?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PNot really. It was really busy, so I wasn't\x01",
            "able to get a good look at everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PBut there was this slim, younger man. From\x01",
            "the looks of it, he was a foreign tourist. He\x01",
            "was hitting on me the entire time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PThen, as I was in the middle of rejecting him,\x01",
            "I heard these weird sounds from behind me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0303FAnd that was the thief's cue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PI think so. Darn it! I was being so careful, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0101F(Our thief is a crafty one.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A44A")
    OP_68(5210, 4740, -10040, 1200)
    MoveCamera(12, 25, 0, 1200)

    def lambda_A268():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A268)

    def lambda_A275():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A275)

    def lambda_A282():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A282)

    def lambda_A28F():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A28F)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#5P#0003FThat should be enough info for us. Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0300FGuess it's time to go back and sort through\x01",
            "the facts, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A444")

    ChrTalk(
        0x102,
        (
            "#12P#0100FGiven that the Business Owners' Association hasn't\x01",
            "contacted us yet, we can assume that the\x01",
            "next robbery hasn't happened yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FIndeed.\x02\x03",
            "#0200FIt would be wise of us to check\x01",
            "the stalls again on our way back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A444")

    OP_29(0x20, 0x1, 0xD)

    label("loc_A44A")

    OP_5A()
    SetChrPos(0x0, 5330, 2500, -8020, 56)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_43_9E02 end

    def Function_44_A481(): pass

    label("Function_44_A481")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x28)
    SoundLoad(806)
    OP_68(-11530, 4730, 9500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(14790, 0)
    SetChrPos(0x101, -15600, 2500, -6960, 0)
    SetChrPos(0x102, -14420, 2500, -7260, 0)
    SetChrPos(0x103, -15590, 2500, -8090, 0)
    SetChrPos(0x104, -14590, 2500, -8690, 0)
    SetChrPos(0x26, -11470, 2500, 8720, 0)
    SetChrPos(0x27, 6590, 2500, 4100, 135)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0x26, 0xC)
    SetChrSubChip(0x26, 0x0)
    SetChrChipByIndex(0x27, 0x4)
    SetChrSubChip(0x27, 0x0)
    BeginChrThread(0x26, 0, 0, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
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
    OP_68(-11530, 3730, 9500, 2800)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    BeginChrThread(0xE, 1, 0, 45)
    Sleep(150)
    BeginChrThread(0x26, 1, 0, 45)
    OP_0D()
    SoundDistance(0x7B, 0xFFFFB32A, 0x99C, 0xFFFFC324, 0x2710, 0x186A0, 0x64, 0x0)
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
    EndChrThread(0xE, 0x1)
    EndChrThread(0x26, 0x1)
    OP_64(0xE)
    OP_64(0x26)
    Sleep(200)
    OP_95(0x26, -6710, 2390, 7920, 1500, 0x0)

    def lambda_A679():
        OP_95(0xFE, 600, 2500, 1580, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_A679)
    OP_95(0x27, -4270, 2390, 9110, 2000, 0x0)
    OP_95(0x27, -11420, 2500, 8680, 2000, 0x0)
    OP_93(0x27, 0x0, 0x190)
    BeginChrThread(0xE, 1, 0, 45)
    Sleep(150)
    BeginChrThread(0x27, 1, 0, 45)
    Sleep(2500)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x27, 0x1)
    OP_64(0xE)
    OP_64(0x27)
    Sleep(200)
    OP_95(0x27, -19340, 2420, 12410, 2000, 0x0)
    OP_95(0x27, -23170, 2390, 16300, 2000, 0x0)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)

    AnonymousTalk(
        0x104,
        "#0306FAfraid you're right.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        "#0200FAnd it has already been an hour...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#0003FI don't get it. If they were coming, they should\x01",
            "have shown up by now...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(806, 2, 100, 0)
    Sleep(800)
    Fade(300)
    OP_68(-15360, 5070, -8180, 0)
    MoveCamera(37, 31, 0, 0)
    OP_6E(280, 0)
    SetCameraDistance(36070, 0)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_0D()
    Sleep(500)
    OP_93(0x101, 0x10E, 0x190)
    Sleep(50)

    def lambda_A818():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A818)

    def lambda_A825():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A825)

    def lambda_A832():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A832)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#0000FYes, sir! Lloyd Bannings spea--\x02\x03",
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
            "#5P#0001FC-Central Square? Got it!\x02\x03",
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
            "#5P#0003FSorry, guys. It looks like my deductions\x01",
            "were a little off target.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#0101FIt's fine. Let's hurry, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0001FR-Right. Let's go!\x02",
    )

    CloseMessageWindow()

    def lambda_AA1A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_AA1A)

    def lambda_AA27():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_AA27)

    def lambda_AA34():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_AA34)

    def lambda_AA41():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_AA41)
    Sleep(300)
    WaitChrThread(0x104, 1)

    def lambda_AA55():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_AA55)

    def lambda_AA6A():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_AA6A)

    def lambda_AA7F():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_AA7F)

    def lambda_AA94():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_AA94)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x28)
    ClearScenarioFlags(0x2, 0)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 5)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_A481 end

    def Function_45_AAC4(): pass

    label("Function_45_AAC4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AAE9")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_45_AAC4")

    label("loc_AAE9")

    Return()

    # Function_45_AAC4 end

    def Function_46_AAEA(): pass

    label("Function_46_AAEA")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　New City Hall Under Construction\x01",
            "       AUTHORIZED PERSONNEL ONLY\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_46_AAEA end

    def Function_47_AB66(): pass

    label("Function_47_AB66")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "           International Symposium\x01",
            "     - Crossbell: One and the Same -\x01",
            "    Listen to eight experts discuss the\x01",
            "    current state and future of Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "    Location: Crossbell City Hall\x01",
            "                    Reception Hall\x01",
            "    Meeting Time: Day 3\x01",
            "    Sponsor: Mayor Henry MacDowell\x01",
            "　 An RSVP is required to attend.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_47_AB66 end

    SaveToFile()

Try(main)
