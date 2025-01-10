from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1100.bin",                # FileName
        "c1100",                    # MapName
        "c1100",                    # Location
        0x0016,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 4210, 2500, 8930, 0, 0, 1, 22, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1100",                  # 0
        "Chroma",                 # 1
        "Otto",                   # 2
        "Tajik",                  # 3
        "Officer Franz",          # 4
        "Detective Dudley",       # 5
        "Detective Emma",         # 6
        "Shannah",                # 7
        "Abby",                   # 8
        "Inspector Donovan",      # 9
        "Detective Raymond",      # 10
        "Yin",                    # 11
        "Central Square",         # 12
        "West Street",            # 13
        "Administrative District",# 14
        "Residential District",   # 15
        "Entertainment District", # 16
        "East Street",            # 17
        "Downtown District",      # 18
        "Harbor District",        # 19
        "IBC",                    # 20
        "Station Street",         # 21
        "Back Alley",             # 22
        "Ursula Road",            # 23
        "East Crossbell Highway", # 24
        "West Crossbell Highway", # 25
        "Mainz Mountain Path",    # 26
    ))

    AddCharChip((
        "chr/ch24900.itc",                   # 00
        "chr/ch20800.itc",                   # 01
        "chr/ch28100.itc",                   # 02
        "chr/ch00900.itc",                   # 03
        "chr/ch30500.itc",                   # 04
        "chr/ch20300.itc",                   # 05
        "chr/ch34200.itc",                   # 06
        "chr/ch30000.itc",                   # 07
        "chr/ch30300.itc",                   # 08
        "chr/ch30200.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
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

    DeclNpc(6929,    2490,    -6650,   225,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(8369,    2390,    -14850,  90,   261,  0x0, 0,   1,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(-8739,   2500,    6070,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-15050,  2500,    27399,   180,  261,  0x0, 0,   7,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-22500,  2500,    24280,   270,  389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-23659,  2500,    24280,   90,   389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(6530,    2500,    -8260,   45,   389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(6969,    2500,    -9149,   45,   389,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-21790,  2500,    27280,   180,  389,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-21100,  2500,    26180,   270,  389,  0x0, 0,   9,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 17,  8.539999961853027,     -5.630000114440918,    2.450000047683716,     68.0625,               [0.12856481969356537,  0.23570233583450317,   -0.0,                  0.0,                   -0.12856490910053253,  0.23570217192173004,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -1.8217639923095703,   -0.6858946681022644,   -0.4899999797344208,   1.0])

    DeclActor(-5890,   2500,    31840,   1200,    -5890,   4000,    31840,   0x007C, 0,  24, 0x0000)

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
    PlaceName(-16.899999618530273, 0.0, -123.5, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_580",          # 00, 0
        "Function_1_638",          # 01, 1
        "Function_2_711",          # 02, 2
        "Function_3_73C",          # 03, 3
        "Function_4_B06",          # 04, 4
        "Function_5_C7C",          # 05, 5
        "Function_6_1C62",         # 06, 6
        "Function_7_1D97",         # 07, 7
        "Function_8_2EAC",         # 08, 8
        "Function_9_4607",         # 09, 9
        "Function_10_6064",        # 0A, 10
        "Function_11_60FB",        # 0B, 11
        "Function_12_61E9",        # 0C, 12
        "Function_13_6322",        # 0D, 13
        "Function_14_636F",        # 0E, 14
        "Function_15_63B2",        # 0F, 15
        "Function_16_6920",        # 10, 16
        "Function_17_6A55",        # 11, 17
        "Function_18_6E3D",        # 12, 18
        "Function_19_6E62",        # 13, 19
        "Function_20_6E87",        # 14, 20
        "Function_21_74F0",        # 15, 21
        "Function_22_764E",        # 16, 22
        "Function_23_76D6",        # 17, 23
        "Function_24_7AE4",        # 18, 24
    ))


    def Function_0_580(): pass

    label("Function_0_580")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5C0"),
        (1, "loc_5CC"),
        (2, "loc_5D8"),
        (3, "loc_5E4"),
        (4, "loc_5F0"),
        (5, "loc_5FC"),
        (6, "loc_608"),
        (SWITCH_DEFAULT, "loc_614"),
    )


    label("loc_5C0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5CC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5D8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5E4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5F0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5FC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_608")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_614")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_620")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_637")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_637")

    Return()

    # Function_0_580 end

    def Function_1_638(): pass

    label("Function_1_638")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_710")
    OP_95(0xFE, 17250, 2500, -14850, 1000, 0x0)
    OP_95(0xFE, 17250, 2500, -70, 1000, 0x0)
    OP_95(0xFE, 3810, 2500, 8270, 1000, 0x0)
    OP_95(0xFE, -6210, 2500, 23860, 1000, 0x0)
    OP_95(0xFE, -18440, 2500, 23260, 1000, 0x0)
    OP_95(0xFE, -20840, 2450, 19170, 1000, 0x0)
    OP_95(0xFE, -18240, 2500, 6490, 1000, 0x0)
    OP_95(0xFE, -18430, 2500, -3620, 1000, 0x0)
    OP_95(0xFE, -7420, 2500, -14630, 1000, 0x0)
    OP_95(0xFE, 8370, 2390, -14850, 1000, 0x0)
    Jump("Function_1_638")

    label("loc_710")

    Return()

    # Function_1_638 end

    def Function_2_711(): pass

    label("Function_2_711")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_73B")
    OP_94(0xFE, 0x1F72, 0xFFFFEAD4, 0x109A, 0xFFFFD8AA, 0x7D0)
    Sleep(200)
    Jump("Function_2_711")

    label("loc_73B")

    Return()

    # Function_2_711 end

    def Function_3_73C(): pass

    label("Function_3_73C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96E")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_807")
    SetChrPos(0x0, 30170, 2500, -90, 270)
    SetChrPos(0x1, 30170, 2500, -90, 270)
    SetChrPos(0x2, 30170, 2500, -90, 270)
    SetChrPos(0x3, 30170, 2500, -90, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DA")
    SetChrPos(0x4, 30170, 2500, -90, 270)
    SetChrPos(0x5, 30170, 2500, -90, 270)
    Jump("loc_7F9")

    label("loc_7DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F9")
    SetChrPos(0x4, 30170, 2500, -90, 270)

    label("loc_7F9")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96E")

    label("loc_807")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8CD")
    SetChrPos(0x0, -40390, 0, 24150, 90)
    SetChrPos(0x1, -40390, 0, 24150, 90)
    SetChrPos(0x2, -40390, 0, 24150, 90)
    SetChrPos(0x3, -40390, 0, 24150, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A0")
    SetChrPos(0x4, -40390, 0, 24150, 90)
    SetChrPos(0x5, -40390, 0, 24150, 90)
    Jump("loc_8BF")

    label("loc_8A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8BF")
    SetChrPos(0x4, -40390, 0, 24150, 90)

    label("loc_8BF")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96E")

    label("loc_8CD")

    SetChrPos(0x0, 19940, 0, -37920, 0)
    SetChrPos(0x1, 19940, 0, -37920, 0)
    SetChrPos(0x2, 19940, 0, -37920, 0)
    SetChrPos(0x3, 19940, 0, -37920, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_946")
    SetChrPos(0x4, 19940, 0, -37920, 0)
    SetChrPos(0x5, 19940, 0, -37920, 0)
    Jump("loc_965")

    label("loc_946")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_965")
    SetChrPos(0x4, 19940, 0, -37920, 0)

    label("loc_965")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_96E")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_991")
    OP_93(0x8, 0x2D, 0x0)
    SetChrFlags(0xB, 0x80)
    Jump("loc_AAD")

    label("loc_991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_99F")
    Jump("loc_AAD")

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9B2")
    SetChrFlags(0xB, 0x80)
    Jump("loc_AAD")

    label("loc_9B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9C0")
    Jump("loc_AAD")

    label("loc_9C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9DF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_9DA")
    SetChrFlags(0x8, 0x80)

    label("loc_9DA")

    Jump("loc_AAD")

    label("loc_9DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_A08")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -22770, 2500, 26320, 90)
    Jump("loc_AAD")

    label("loc_A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A25")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_AAD")

    label("loc_A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_A33")
    Jump("loc_AAD")

    label("loc_A33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_A41")
    Jump("loc_AAD")

    label("loc_A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A4F")
    Jump("loc_AAD")

    label("loc_A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A5D")
    Jump("loc_AAD")

    label("loc_A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A6B")
    Jump("loc_AAD")

    label("loc_A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A7E")
    SetChrFlags(0xB, 0x80)
    Jump("loc_AAD")

    label("loc_A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_A96")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_AAD")

    label("loc_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_AA4")
    Jump("loc_AAD")

    label("loc_AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_AAD")

    label("loc_AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_AC4")
    ClearScenarioFlags(0x5C, 0)
    SetScenarioFlags(0x1, 1)
    Event(0, 21)
    Jump("loc_AEA")

    label("loc_AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_ADB")
    ClearScenarioFlags(0x5C, 1)
    SetScenarioFlags(0x1, 1)
    Event(0, 22)
    Jump("loc_AEA")

    label("loc_ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_AEA")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 23)

    label("loc_AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B05")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_B05")

    Return()

    # Function_3_73C end

    def Function_4_B06(): pass

    label("Function_4_B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B1D")

    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B31")
    Jump("loc_B40")

    label("loc_B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_B40")
    ClearMapObjFlags(0x6, 0x4)

    label("loc_B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B81")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_BE2")

    label("loc_B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_BBD")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_BE2")

    label("loc_BBD")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_BF3")
    OP_24(0x7B)
    Jump("loc_C0F")

    label("loc_BF3")

    SoundDistance(0x7B, 0xFFFFB32A, 0x99C, 0xFFFFC324, 0x2710, 0x186A0, 0x64, 0x0)

    label("loc_C0F")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C22")
    Jump("loc_C5A")

    label("loc_C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C5A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_C43")
    SetMapObjFlags(0x4, 0x4)
    Jump("loc_C5A")

    label("loc_C43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_C5A")
    ModifyEventFlags(1, 0, 0x80)
    SetMapObjFlags(0x4, 0x4)

    label("loc_C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C76")
    Jump("loc_C7B")

    label("loc_C76")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_C7B")

    Return()

    # Function_4_B06 end

    def Function_5_C7C(): pass

    label("Function_5_C7C")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C5E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CDA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_CDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFA")
    OP_AF(0x80)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C59")

    label("loc_CFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0E")
    Jump("loc_1C59")

    label("loc_D0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C59")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_DF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBD")

    ChrTalk(
        0xFE,
        "I'm going to be closing up shop here pretty soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Better order while you still can.\x01",
            "This will be the final call.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DF0")

    label("loc_DBD")


    ChrTalk(
        0xFE,
        (
            "Final call. Better order while\x01",
            "you still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF0")

    Jump("loc_1C59")

    label("loc_DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_E81")

    ChrTalk(
        0xFE,
        (
            "Some police officers were making a lot\x01",
            "of noise around here earlier this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what that was all about.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C59")

    label("loc_E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_F8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F27")

    ChrTalk(
        0xFE,
        "We're having some lovely weather, aren't we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Weather like today's my saving grace, considering\x01",
            "I can't stay open on a rainy day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F85")

    label("loc_F27")


    ChrTalk(
        0xFE,
        (
            "I anticipate people will be crawling to me for\x01",
            "refreshments, considering how warm it is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F85")

    Jump("loc_1C59")

    label("loc_F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_10CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1043")

    ChrTalk(
        0xFE,
        (
            "Things have gotten a lot more lively\x01",
            "since the diet started their session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Too bad neither members of the diet nor\x01",
            "the press stop by my shop often.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10C5")

    label("loc_1043")


    ChrTalk(
        0xFE,
        "I liked the Anniversary Festival much more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wouldn't be able to tell you the first thing\x01",
            "about how the diet operates.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C5")

    Jump("loc_1C59")

    label("loc_10CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1245")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1181")

    ChrTalk(
        0xFE,
        "I think it's about time I pack up and try another location.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to focus on attracting tourists who'll\x01",
            "spread word of my juice after they go home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1240")

    label("loc_1181")


    ChrTalk(
        0xFE,
        (
            "Hey there. You're looking thirsty!\x01",
            "Care to try some fresh juice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're tired of sightseeing,\x01",
            "why not try some juice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My delicious juice will rejuvenate\x01",
            "you, guaranteed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1240")

    Jump("loc_1C59")

    label("loc_1245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_13E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1336")

    ChrTalk(
        0xFE,
        (
            "I bet the price of fruit is going to increase\x01",
            "as the Anniversary Festival draws near.\x01",
            "I'd better act fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come to think, didn't Mom give\x01",
            "me a similar warning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've gotta continue to give it my all.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13E1")

    label("loc_1336")


    ChrTalk(
        0xFE,
        (
            "My mom actually runs the grocery store\x01",
            "inside of Times Department Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maintaining inventory is her speciality.\x01",
            "Maybe I should ask her to teach me her ways...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E1")

    Jump("loc_1C59")

    label("loc_13E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1437")

    ChrTalk(
        0xFE,
        (
            "Welcome to my stall.\x01",
            "Would any of you like to place an order?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C59")

    label("loc_1437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_15F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153F")

    ChrTalk(
        0xFE,
        (
            "My mom actually runs the grocery store\x01",
            "inside of Times Department Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's managed to build up a good reputation\x01",
            "with how long she's been in the food industry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's all thanks to my mom that I decided\x01",
            "to open up shop.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15ED")

    label("loc_153F")


    ChrTalk(
        0xFE,
        (
            "My mom actually runs the grocery store\x01",
            "inside of Times Department Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's managed to build up a good reputation\x01",
            "with how long she's been in the food industry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15ED")

    Jump("loc_1C59")

    label("loc_15F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_17DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E2")

    ChrTalk(
        0xFE,
        (
            "I figured I'd follow my mom's footsteps and try running\x01",
            "my own business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Only problem is, I had to take out a\x01",
            "hefty loan just to purchase this cart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's why I'm working so hard to make a profit.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17D7")

    label("loc_16E2")


    ChrTalk(
        0xFE,
        (
            "I wanted to see how far I could get on my own,\x01",
            "so I settled for a loan. Can't always rely\x01",
            "on Mommy, can we now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm gonna do it! I'll run a profit, pay back the\x01",
            "loan, and become a hotshot merchant!\x01",
            "I'm ready to hit the ground running!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D7")

    Jump("loc_1C59")

    label("loc_17DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1927")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x16)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F8")
    Call(0, 6)
    Jump("loc_1922")

    label("loc_17F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D5")

    ChrTalk(
        0xFE,
        (
            "Good day, everyone.\x01",
            "Care for a tall, cold glass of tasty juice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A few bracers just struck up a conversation\x01",
            "with me, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I gotta hand it to them, they're pretty\x01",
            "cool and friendly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1922")

    label("loc_18D5")


    ChrTalk(
        0xFE,
        (
            "Y-You gotta hand it to those bracers.\x01",
            "They're pretty cool and friendly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1922")

    Jump("loc_1C59")

    label("loc_1927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_19FB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x16)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1943")
    Call(0, 6)
    Jump("loc_19F6")

    label("loc_1943")


    ChrTalk(
        0xFE,
        "My shop is a big hit with tourists.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nothing beats a tall glass of juice to recover\x01",
            "from post-sightseeing exhaustion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm so glad I decided to invest in this stall.\x02",
    )

    CloseMessageWindow()

    label("loc_19F6")

    Jump("loc_1C59")

    label("loc_19FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1B2E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x16)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A17")
    Call(0, 6)
    Jump("loc_1B29")

    label("loc_1A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A95")

    ChrTalk(
        0xFE,
        "Woohoo! The weather's on my side today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nothing pairs well with this scorching sun\x01",
            "like my juice!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B29")

    label("loc_1A95")


    ChrTalk(
        0xFE,
        (
            "Welcome!\x01",
            "Would you like to try some orange juice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Leave it up to some cold, delicious orange\x01",
            "juice to put the spring back into your step!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B29")

    Jump("loc_1C59")

    label("loc_1B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1BEA")

    ChrTalk(
        0xFE,
        "Who wants some fresh juice?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you tired from walking around this massive\x01",
            "city all day? Come try our juice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Look no further if you want to feel revitalized!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C59")

    label("loc_1BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1C59")

    ChrTalk(
        0xFE,
        "Howdy, folks. Care to try some fresh juice?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Orange, melon, apple... You name it, we got it!\x02",
    )

    CloseMessageWindow()

    label("loc_1C59")

    Jump("loc_C89")

    label("loc_1C5E")

    TalkEnd(0xFE)
    Return()

    # Function_5_C7C end

    def Function_6_1C62(): pass

    label("Function_6_1C62")


    ChrTalk(
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to teach you guys how to\x01",
            "make some delicious juice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's important that you rehydrate your body with\x01",
            "water after a long walk or an intense workout.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1D0),
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
            scpstr(SCPSTR_CODE_ITEM, 0x1D0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x16)
    Return()

    # Function_6_1C62 end

    def Function_7_1D97(): pass

    label("Function_7_1D97")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1F38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E98")

    ChrTalk(
        0xFE,
        (
            "I'm not sure why, but this sunset is\x01",
            "tinged with a slight drop of sorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The sorrowful sunset, the chill of the wind,\x01",
            "and the quiet toll of the evening bell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They all are representative of Crossbell's beauty!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F33")

    label("loc_1E98")


    ChrTalk(
        0xFE,
        (
            "Isn't it about time for you guys\x01",
            "to call it a day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope you're not headed to the Entertainment District.\x01",
            "It can get pretty dangerous at night!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F33")

    Jump("loc_2EA8")

    label("loc_1F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2049")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FFD")

    ChrTalk(
        0xFE,
        (
            "The arguments heated up even more\x01",
            "during today's diet session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do you think they'll ever grow tired of it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Today marks the third extension of the session.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2044")

    label("loc_1FFD")


    ChrTalk(
        0xFE,
        (
            "Diet meetings only grow longer and longer\x01",
            "with each passing year!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2044")

    Jump("loc_2EA8")

    label("loc_2049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_21A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2156")

    ChrTalk(
        0xFE,
        (
            "I'm not sure why, but the latest issue of the\x01",
            "Crossbell Times was postponed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been to a few stores that carry their\x01",
            "publication, but none of them have the latest one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's with the hold up?\x01",
            "I demand a proper explanation!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_219E")

    label("loc_2156")


    ChrTalk(
        0xFE,
        (
            "It's inconceivable for the Crossbell Times\x01",
            "to delay a publication!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219E")

    Jump("loc_2EA8")

    label("loc_21A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2223")

    ChrTalk(
        0xFE,
        "Surely there wasn't an accident, was there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is it just me, or has the city been getting\x01",
            "more dangerous?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA8")

    label("loc_2223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_22C0")

    ChrTalk(
        0xFE,
        (
            "The streets have gone back to normal now\x01",
            "that the Anniversary Festival is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah, this beautiful tranquility, how I've missed you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EA8")

    label("loc_22C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_231A")

    ChrTalk(
        0xFE,
        "#4SI'm so excited, Ilya!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Isn't the weather magnificent today?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EA8")

    label("loc_231A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2459")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23DC")

    ChrTalk(
        0xFE,
        (
            "It may just be a rumor, but apparently\x01",
            "Arc en Ciel is putting on a private show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How unfair!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Us common folk have been waiting\x01",
            "for it with bated breath.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2454")

    label("loc_23DC")


    ChrTalk(
        0xFE,
        (
            "Arc en Ciel is putting on a private performance\x01",
            "for some esteemed guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How unfair!\x01",
            "Where's my invitation?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2454")

    Jump("loc_2EA8")

    label("loc_2459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_25D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2557")

    ChrTalk(
        0xFE,
        (
            "It's almost time to discuss the budget\x01",
            "at City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I imagine the diet members will constantly\x01",
            "interrupt proceedings, as per usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, no matter. We have to keep trying\x01",
            "our hardest for the good of Crossbell!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25D2")

    label("loc_2557")


    ChrTalk(
        0xFE,
        (
            "As citizens of Crossbell, it is our duty to do so!\x01",
            "We must make the lives of the mayor and\x01",
            "government workers easier!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D2")

    Jump("loc_2EA8")

    label("loc_25D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_270E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_269C")

    ChrTalk(
        0xFE,
        (
            "Are you guys looking forward to\x01",
            "Arc en Ciel's new show?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I know I am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I managed to get my hands on some B section\x01",
            "seats, so I finally get to see them live!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2709")

    label("loc_269C")


    ChrTalk(
        0xFE,
        "I'm so excited, Ilya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not a day goes by where Ilya's fans don't\x01",
            "shout her name out on the streets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2709")

    Jump("loc_2EA8")

    label("loc_270E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_28BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_281D")

    ChrTalk(
        0xFE,
        (
            "Are you looking for the CPD's vice commissioner?\x01",
            "I see him around these parts pretty often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Between his face and his slender build,\x01",
            "I'd say he reminds me of a fox.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's always restlessly pacing around here\x01",
            "during my lunch break!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28B6")

    label("loc_281D")


    ChrTalk(
        0xFE,
        "The vice commissioner has a face that's easy to read.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can tell from a selge away that he's not someone\x01",
            "I'd want to have a conversation with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28B6")

    Jump("loc_2EA8")

    label("loc_28BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2A42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B7")

    ChrTalk(
        0xFE,
        (
            "It's been about fifty years since the\x01",
            "City Hall building was constructed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was designed by the hands\x01",
            "of the famous architect, J. Kendall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its majesty and refined air perfectly\x01",
            "represent Crossbell as a whole!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A3D")

    label("loc_29B7")


    ChrTalk(
        0xFE,
        (
            "The City Hall building was designed\x01",
            "by a famous architect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surprisingly enough, it's one of the most\x01",
            "popular tourist spots!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A3D")

    Jump("loc_2EA8")

    label("loc_2A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2AFE")

    ChrTalk(
        0xFE,
        (
            "The mayor manages to handle constant\x01",
            "meetings and business trips, despite his old age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can only assume that he's doing a fantastic\x01",
            "job of maintaining his health.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA8")

    label("loc_2AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C01")

    ChrTalk(
        0xFE,
        "Have you ever heard Crossbell City Hall's slogan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I believe it was...'The administration welcomes\x01",
            "each and every one of its citizens with open arms.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope they're taking the proper steps to\x01",
            "uphold their own values.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CDA")

    label("loc_2C01")


    ChrTalk(
        0xFE,
        (
            "The slogan 'The administration welcomes each and\x01",
            "every one of its citizens with open arms' is printed\x01",
            "at Crossbell City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although, not many citizens visit City Hall,\x01",
            "so it's usually pretty quiet there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CDA")

    Jump("loc_2EA8")

    label("loc_2CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2EA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF3")

    ChrTalk(
        0xFE,
        "Good morning...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get the impression that you're all\x01",
            "citizens of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd give you some details about the area if\x01",
            "you were tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering you're locals, I doubt it's necessary.\x01",
            "Surely you don't need a guide, do you?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EA8")

    label("loc_2DF3")


    ChrTalk(
        0xFE,
        (
            "This area mostly has administrative offices.\x01",
            "Not a whole lot of civilians hang around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahem! What I'm trying to say is this place is\x01",
            "fantastic for an afternoon walk!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA8")

    TalkEnd(0xFE)
    Return()

    # Function_7_1D97 end

    def Function_8_2EAC(): pass

    label("Function_8_2EAC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3042")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FBA")

    ChrTalk(
        0xFE,
        (
            "Listen up! At long last, the diet's budget session\x01",
            "is finally over!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew... I can finally return home without any\x01",
            "lingering regrets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite what people may think, determining\x01",
            "the budget is crucial to Crossbell's prosperity.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_303D")

    label("loc_2FBA")


    ChrTalk(
        0xFE,
        (
            "You'd figure I'd get burnt out from working too hard,\x01",
            "but I really do enjoy my work with Financial Affairs\x01",
            "for the most part.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_303D")

    Jump("loc_4603")

    label("loc_3042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_31B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311E")

    ChrTalk(
        0xFE,
        (
            "A reporter just came by and fired off one\x01",
            "question after another at me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heh. He asked if I knew the outcome of\x01",
            "the diet session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's what I've been wondering this whole time!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31B2")

    label("loc_311E")


    ChrTalk(
        0xFE,
        (
            "The diet's budget meeting is still in session.\x01",
            "As a member of Financial Affairs, I'm interested\x01",
            "in what the final budget draft will look like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B2")

    Jump("loc_4603")

    label("loc_31B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_33F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E3")

    ChrTalk(
        0xFE,
        (
            "The diet has been at it all morning trying to\x01",
            "decide on the budget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Too bad it's a diet in name only. It's nothing\x01",
            "more than a futile shouting match between\x01",
            "the Imperial and Republican factions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*\x01",
            "Mayor MacDowell's a glorified babysitter at this point.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33EC")

    label("loc_32E3")


    ChrTalk(
        0xFE,
        (
            "I'd avoid City Hall today, if I were you.\x01",
            "All you'll find are the Imperial and Republican\x01",
            "factions hurling insults at each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Speaker Hartmann is supposed to be the mediator,\x01",
            "yet he supports the Imperial Faction...\x01",
            "Mayor MacDowell must have it rough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33EC")

    Jump("loc_4603")

    label("loc_33F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3479")

    ChrTalk(
        0xFE,
        "Man, I'm bored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about how the diet budget meeting\x01",
            "is progressing, but I can't do anything about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4603")

    label("loc_3479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_37CF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_353C")

    ChrTalk(
        0xFE,
        (
            "I just noticed that the juice stall relocated\x01",
            "in front of the station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I AM feeling a little thirsty...\x01",
            "I think I'll grab myself a drink later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37CA")

    label("loc_353C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_364B")

    ChrTalk(
        0xFE,
        "Huh, where'd the juice stall run off to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I noticed some food carts headed over\x01",
            "to the south entrance a second ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're constantly relocating around\x01",
            "the city to increase their visibility.\x01",
            "Not much else they can do to get more popular.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37CA")

    label("loc_364B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_371D")

    ChrTalk(
        0xFE,
        (
            "The diet's budget session is finally\x01",
            "beginning tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A draft of the budget has already been submitted,\x01",
            "so it's the diet members' turn to make demands.\x01",
            "I've been feeling on edge.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37CA")

    label("loc_371D")


    ChrTalk(
        0xFE,
        (
            "The diet's budget session is finally\x01",
            "beginning tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how much of my work is thrown out,\x01",
            "I'm proud of what I accomplished. I've been feeling\x01",
            "on edge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37CA")

    Jump("loc_4603")

    label("loc_37CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_398F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38CF")

    ChrTalk(
        0xFE,
        (
            "I caught a glimpse of Speaker Hartmann's face\x01",
            "during negotiations earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The expression he was wearing made me\x01",
            "believe he was as extraordinary as he lets on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's almost as if he has an air of majesty about him.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_398A")

    label("loc_38CF")


    ChrTalk(
        0xFE,
        (
            "Speaker Hartmann was hardly contributing\x01",
            "to the discussion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He had a strange aura around him, though.\x01",
            "I suppose that's to be expected of a prominent\x01",
            "politician such as himself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_398A")

    Jump("loc_4603")

    label("loc_398F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3A91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4C")

    ChrTalk(
        0xFE,
        "*sigh* I'm so tired...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I feel like skipping today's meeting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to grit my teeth and not let the diet\x01",
            "members' outbursts get under my skin.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A8C")

    label("loc_3A4C")


    ChrTalk(
        0xFE,
        "This is one of the worst times to be in Financial Affairs.\x02",
    )

    CloseMessageWindow()

    label("loc_3A8C")

    Jump("loc_4603")

    label("loc_3A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3D3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C15")

    ChrTalk(
        0xFE,
        (
            "The Imperial Faction currently holds\x01",
            "a majority in the diet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're not quite at the two-thirds majority\x01",
            "needed to steamroll the minority opposition, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's why things are starting to heat up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Discussions regarding the budget always get\x01",
            "sidetracked by Imperial and Republican diet\x01",
            "members arguing, making it impossible to progress.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D39")

    label("loc_3C15")


    ChrTalk(
        0xFE,
        (
            "Take the construction of the new City Hall,\x01",
            "for example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've already managed to allocate the funds\x01",
            "accordingly in the new plan, yet they've not\x01",
            "decided on who will lead the project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Construction was in progress but has since been\x01",
            "put on ice... Who knows when it'll resume?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D39")

    Jump("loc_4603")

    label("loc_3D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3F49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EBE")

    ChrTalk(
        0xFE,
        (
            "We're about to start arranging a draft of the\x01",
            "budget in a conference room at City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm a part of the team creating a budget outline that'll\x01",
            "be sent to the diet's budget session next month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The conference is only meant for members of\x01",
            "Financial Affairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But of course, diet members are already\x01",
            "sticking their noses into our business.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F44")

    label("loc_3EBE")


    ChrTalk(
        0xFE,
        (
            "*sigh* I have to go there again\x01",
            "for the afternoon session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder how many more of them\x01",
            "will come interrupt us this time?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F44")

    Jump("loc_4603")

    label("loc_3F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_403A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FF9")

    ChrTalk(
        0xFE,
        (
            "I heard that it's Crime Prevention Week\x01",
            "over at the CPD.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Explains why it feels like the police have\x01",
            "been stepping up their patrol efforts.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4035")

    label("loc_3FF9")


    ChrTalk(
        0xFE,
        (
            "I wish they would have given us proper\x01",
            "notice, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4035")

    Jump("loc_4603")

    label("loc_403A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_41F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4134")

    ChrTalk(
        0xFE,
        (
            "It won't be much longer until we need to\x01",
            "put together the draft for the next budget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I'm sure, once again, the diet members\x01",
            "will be clawing at us to make it benefit them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ugh, I've got a killer headache.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_41F2")

    label("loc_4134")


    ChrTalk(
        0xFE,
        (
            "I was an ambitious young man filled with hopes\x01",
            "and dreams when I got hired at City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It only took a couple of years for the cold,\x01",
            "cruel reality of a government job to kick in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41F2")

    Jump("loc_4603")

    label("loc_41F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_435E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4311")

    ChrTalk(
        0xFE,
        (
            "The Transportation Division manages all of the\x01",
            "buses that run within the state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been about five years since it was created,\x01",
            "and there hasn't been a moment of rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, it's thanks to them that the buses\x01",
            "run as efficiently as they do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4359")

    label("loc_4311")


    ChrTalk(
        0xFE,
        (
            "My work tends to slowly trickle in,\x01",
            "so I feel pretty bad for them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4359")

    Jump("loc_4603")

    label("loc_435E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4496")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4448")

    ChrTalk(
        0xFE,
        (
            "I think my boss has it out for me.\x01",
            "I get scolded way too often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I find it hard to concentrate when all he does\x01",
            "is shove all the worthless jobs onto me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, I don't want to go back to work...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4491")

    label("loc_4448")


    ChrTalk(
        0xFE,
        (
            "We're paid well, but I honestly despise\x01",
            "working for the government.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4491")

    Jump("loc_4603")

    label("loc_4496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4603")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4523")

    ChrTalk(
        0xFE,
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everybody's been lighting a fire under\x01",
            "Financial Affairs' behinds.\x01",
            "I'm at my wits' end, here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4603")

    label("loc_4523")


    ChrTalk(
        0xFE,
        (
            "Financial Affairs keeps track of the city's mira.\x01",
            "From diet members to high-ranking officials,\x01",
            "there's always someone pressuring us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew... I need a break. I'll suffocate if I don't\x01",
            "get a little breathing room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4603")

    TalkEnd(0xFE)
    Return()

    # Function_8_2EAC end

    def Function_9_4607(): pass

    label("Function_9_4607")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4923")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0005FIs that you, Franz? I haven't seen you\x01",
            "in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whoa, good to see you, Lloyd!\x01",
            "Been about a month since police\x01",
            "academy graduation, hasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, didn't you pass the detective\x01",
            "qualification exam?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you happy with your assignment? Wait,\x01",
            "don't tell me... Were you assigned to one of\x01",
            "the investigative divisions right off the bat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FWell... Not exactly.\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "What's with the halfhearted reply?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's no big deal. It won't be much longer until\x01",
            "your pal Franz here becomes a detective, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be counting on you to help explain anything\x01",
            "I don't understand in the textbooks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FY-Yeah, leave it to me.\x01",
            "(I'll need to clear the air with Franz later...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_491F")
    SetScenarioFlags(0x1, 2)

    label("loc_491F")

    TalkEnd(0xFE)
    Return()

    label("loc_4923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4931")
    Jump("loc_6060")

    label("loc_4931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4A50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49EE")

    ChrTalk(
        0xFE,
        (
            "Something's up at the airport.\x01",
            "We received instructions from above to\x01",
            "exercise caution, and all that jazz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What exactly am I supposed to be careful of?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4A4B")

    label("loc_49EE")


    ChrTalk(
        0xFE,
        (
            "Those were some pretty vague instructions.\x01",
            "Did they really come from our section chief?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A4B")

    Jump("loc_6060")

    label("loc_4A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4A5E")
    Jump("loc_6060")

    label("loc_4A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4D3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CBD")

    ChrTalk(
        0xFE,
        "Ah, hey, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gotta tell you something... I think I'm going\x01",
            "to take the detective exam for real this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FNice, Franz. You finally made up your mind?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, yeah, but the amount I study still isn't enough.\x01",
            "Even if you ignore the practical exam, I'm still\x01",
            "pretty bad at classwork.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm thinking I might get a better grasp on what\x01",
            "I should study if I take the exam once, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Only problem is, they've strengthened patrols\x01",
            "lately, which has been sucking up my free time.\x01",
            "What's with the chain of incidents recently?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4D37")

    label("loc_4CBD")


    ChrTalk(
        0xFE,
        (
            "Our section chief has been working us to\x01",
            "the bone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dang it... More and more of my study time\x01",
            "is being eaten up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D37")

    Jump("loc_6060")

    label("loc_4D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4F88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EEC")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if it isn't Lloyd!\x01",
            "Good to see you're safe, buddy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I heard Revache was gunning for you,\x01",
            "I thought to myself, 'What have they gotten\x01",
            "themselves into this time?'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha, I'm glad they were just overblown rumors.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Officers were spreading them around HQ.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I heard you reached a deal with them.\x01",
            "You can finally take it easy now, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 6)
    Jump("loc_4F83")

    label("loc_4EEC")


    ChrTalk(
        0xFE,
        (
            "People in the CPD have been spreading\x01",
            "all kinds of rumors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I heard you reached a deal with them.\x01",
            "You can finally take it easy now, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F83")

    Jump("loc_6060")

    label("loc_4F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5196")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50EB")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        (
            "Umm, the seven tools of a detective\x01",
            "should be used whenever--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Whoops, sorry. I was just going over some\x01",
            "of the study material for the detective exam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FSounds like you're hard at work, Franz.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, you guys in the middle of an investigation?\x01",
            "I appreciate all the hard work you guys put in!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5191")

    label("loc_50EB")


    ChrTalk(
        0xFE,
        (
            "Everyone in the investigative divisions\x01",
            "has been crazy busy as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I gotta keep up the hard work and earn\x01",
            "my detective qualification as soon as I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5191")

    Jump("loc_6060")

    label("loc_5196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_533D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52AC")

    ChrTalk(
        0xFE,
        (
            "Dudley carries the hope of the First Division\x01",
            "on his shoulders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's the ace of the younger detectives,\x01",
            "and the older ones tip their hat to him.\x01",
            "He's kind of a role model of mine, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Though, he's kinda difficult to approach.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5338")

    label("loc_52AC")


    ChrTalk(
        0xFE,
        (
            "Don't get me wrong. He's a helluva guy,\x01",
            "but I can't even talk to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A formal greeting is about all I can\x01",
            "muster when I see him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5338")

    Jump("loc_6060")

    label("loc_533D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5559")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54A1")

    ChrTalk(
        0xFE,
        (
            "Dealing with the citizens' complaints is probably\x01",
            "the most painful thing about being an officer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not like we can prevent every single crime from\x01",
            "happening, y'know? We're not being lazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* It's my sworn duty to protect the citizens,\x01",
            "but some things are just outta my control.\x01",
            "That's the part that stings.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5554")

    label("loc_54A1")


    ChrTalk(
        0xFE,
        (
            "As a member of the CPD, there's just\x01",
            "so many restrictions placed on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Having a sense of justice and knowing there's\x01",
            "so much you can't accomplish... It hurts, y'know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5554")

    Jump("loc_6060")

    label("loc_5559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5984")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57AD")

    ChrTalk(
        0xFE,
        (
            "Oh, it's you guys.\x01",
            "Keep up the hard work, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHow are things going for you lately, Franz?\x01",
            "I know you told me you've been having\x01",
            "a hard time finding time to study, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha, you mean the qualification exam?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'm going to focus on my everyday duties,\x01",
            "for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That doesn't mean I've given up on my dream\x01",
            "of becoming a detective, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FSounds like you've got yourself in a complicated\x01",
            "situation. Don't overwork yourself, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can count on me, buddy.\x01",
            "You hang in there, too.\x01",
            "All right, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 1)
    Jump("loc_597F")

    label("loc_57AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58CD")

    ChrTalk(
        0xFE,
        (
            "Oh, it's you guys...\x01",
            "I try to strike up a conversation with the receptionist\x01",
            "whenever I get the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think her name was Rebecca?\x01",
            "Man, she's a pretty girl...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Don't mind me, it's not like I've got any\x01",
            "ulterior motives or anything!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_597F")

    label("loc_58CD")


    ChrTalk(
        0xFE,
        "That receptionist, Rebecca, is a stunning beauty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't get me wrong, Fran is cute, too,\x01",
            "but Rebecca is just mesmerizing...\x01",
            "Wait, what the hell am I telling you guys?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_597F")

    Jump("loc_6060")

    label("loc_5984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5AD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A1E")

    ChrTalk(
        0xFE,
        "Good morning, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One of the detectives from the First Division\x01",
            "just left. Phew... Those guys make me nervous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5AD3")

    label("loc_5A1E")


    ChrTalk(
        0xFE,
        (
            "Can you blame me, though?\x01",
            "You've seen how cool they are, right?\x01",
            "They're detectives, through and through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanna hurry up and take my qualification exam\x01",
            "as soon as I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AD3")

    Jump("loc_6060")

    label("loc_5AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5C8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C11")

    ChrTalk(
        0xFE,
        (
            "As one of the city's patrol officers, I chose\x01",
            "to make this location my regular beat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It may look like a dull place to watch, but a\x01",
            "lot of detectives come through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I'm aiming to earn my detective license,\x01",
            "don't you think studying them is the perfect\x01",
            "reference?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C86")

    label("loc_5C11")


    ChrTalk(
        0xFE,
        (
            "If I work here, I can start to understand\x01",
            "how detectives think and act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You've got to learn from the best!\x02",
    )

    CloseMessageWindow()

    label("loc_5C86")

    Jump("loc_6060")

    label("loc_5C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5C99")
    Jump("loc_6060")

    label("loc_5C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5F8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_5D8E")

    ChrTalk(
        0xFE,
        (
            "(Hey, check it out. I'm pretty sure those two\x01",
            "over there are from the First Division!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(B-Being in the presence of their greatness\x01",
            "is making me feel overwhelmed.\x01",
            "I'd probably pass out just standing near them...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F85")

    label("loc_5D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_5E67")

    ChrTalk(
        0xFE,
        (
            "(I'm pretty sure those two over there\x01",
            "are from the First Division!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(B-Being in the presence of their greatness\x01",
            "is making me feel overwhelmed.\x01",
            "I'd probably pass out just standing near them...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F85")

    label("loc_5E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EE8")

    ChrTalk(
        0xFE,
        "Good work, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "First day on the job? I'm in the same boat.\x01",
            "Phew... I'm feeling pretty nervous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5F85")

    label("loc_5EE8")


    ChrTalk(
        0xFE,
        (
            "Well, this is just another step I have to take to\x01",
            "become a detective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what kind of work is thrown\x01",
            "my way, I can't start cutting corners.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F85")

    Jump("loc_6060")

    label("loc_5F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6060")

    ChrTalk(
        0xFE,
        (
            "I'm aiming to become an inspector for\x01",
            "the First Division, so I'm working towards\x01",
            "my detective qualification.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All the members of the First Division are\x01",
            "just as respectable as I thought they'd be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6060")

    TalkEnd(0xFE)
    Return()

    # Function_9_4607 end

    def Function_10_6064(): pass

    label("Function_10_6064")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6079")
    Call(0, 11)
    Jump("loc_60F7")

    label("loc_6079")


    ChrTalk(
        0xFE,
        (
            "#0603FHmph...\x01",
            "I have nothing to say to the lot of you.\x02\x03",
            "#0600FHurry up and make yourself scarce,\x01",
            "do I make myself clear?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60F7")

    TalkEnd(0xFE)
    Return()

    # Function_10_6064 end

    def Function_11_60FB(): pass

    label("Function_11_60FB")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0xD, 0x5A, 0x0)

    ChrTalk(
        0xC,
        (
            "#0603FYes, I'll attempt to gather information in the\x01",
            "Republic for the time being.\x02\x03",
            "#0603FI'll leave the investigation to you, Emma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Understood. I'll rendezvous with\x01",
            "surveillance team K ASAP.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_11_60FB end

    def Function_12_61E9(): pass

    label("Function_12_61E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61FE")
    Call(0, 11)
    Jump("loc_631E")

    label("loc_61FE")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "The Special Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, don't go impeding my investigation.\x01",
            "You've only just joined us, after all.\x02",
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
        "#0006F(That was awfully rude of them.)\x02",
    )

    CloseMessageWindow()

    label("loc_631E")

    TalkEnd(0xFE)
    Return()

    # Function_12_61E9 end

    def Function_13_6322(): pass

    label("Function_13_6322")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Oh, good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We've got clear skies on our hands today.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_6322 end

    def Function_14_636F(): pass

    label("Function_14_636F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I get to go to the library later\x01",
            "today with Mom again!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_636F end

    def Function_15_63B2(): pass

    label("Function_15_63B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_649C")

    ChrTalk(
        0xFE,
        (
            "I've got assault, hit-and-run, and fraud\x01",
            "investigations on my plate today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gotta hurry up and clean up this damn mess,\x01",
            "or else the sun's going to set on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThe Second Division looks pretty busy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_691C")

    label("loc_649C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_691C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6781")

    ChrTalk(
        0xFE,
        (
            "*puff* I heard your case got snatched up by\x01",
            "the First Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I'm sure it wasn't an important case.\x02",
    )


    ChrTalk(
        0xFE,
        (
            "You should be glad that they let you off with just\x01",
            "a little warning for meddling in their business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FIs that how people are seeing the situation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep, not that we expected anything\x01",
            "less from Sergei's kiddos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, try not to kick up too much dust, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My gut tells me that you're all going to get\x01",
            "another scolding from the vice commissioner\x01",
            "if you keep standing out.\x02",
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
        "#0200FWe cannot guarantee anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FThat doesn't sound like a good time, though...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_691C")

    label("loc_6781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6881")

    ChrTalk(
        0xFE,
        (
            "Sticking your noses into\x01",
            "First Division business...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, considering you're Sergei's kiddos, the\x01",
            "fox might actually have to yield to you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, try not to invoke the vice commissioner's\x01",
            "ire, got it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_691C")

    label("loc_6881")


    ChrTalk(
        0xFE,
        (
            "*puff* Anyway, where the hell is Raymond?\x01",
            "I bet he's slacking off somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm gonna burn through all of my cigs\x01",
            "before we go get that info...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_691C")

    TalkEnd(0xFE)
    Return()

    # Function_15_63B2 end

    def Function_16_6920(): pass

    label("Function_16_6920")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69EB")

    ChrTalk(
        0xFE,
        (
            "I really hope I score myself a girlfriend\x01",
            "during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd love to be able to enjoy a nice vacation\x01",
            "at Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's just a pipe dream, though.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6A51")

    label("loc_69EB")


    ChrTalk(
        0xFE,
        (
            "Hahaha...\x01",
            "There's no way a detective could ever take\x01",
            "a vacation during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A51")

    TalkEnd(0xFE)
    Return()

    # Function_16_6920 end

    def Function_17_6A55(): pass

    label("Function_17_6A55")

    EventBegin(0x0)
    Fade(500)
    OP_68(7330, 3500, -6700, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17970, 0)
    SetChrPos(0x101, 6820, 2390, -5850, 270)
    SetChrPos(0x153, 8100, 2390, -5930, 225)
    BeginChrThread(0x101, 1, 0, 18)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AE5")
    SetChrPos(0x102, 8160, 2390, -7190, 180)
    BeginChrThread(0x102, 1, 0, 19)
    Sleep(2000)
    EndChrThread(0x102, 0x1)
    Jump("loc_6B46")

    label("loc_6AE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B18")
    SetChrPos(0x103, 8160, 2390, -7190, 180)
    BeginChrThread(0x103, 1, 0, 19)
    Sleep(2000)
    EndChrThread(0x103, 0x1)
    Jump("loc_6B46")

    label("loc_6B18")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B46")
    SetChrPos(0x104, 8160, 2390, -7190, 180)
    BeginChrThread(0x104, 1, 0, 19)
    Sleep(2000)
    EndChrThread(0x104, 0x1)

    label("loc_6B46")

    EndChrThread(0x101, 0x1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0005FHuh, that's strange.\x02\x03",
            "Wasn't the juice stall around here before?\x01",
            "I could have sworn it was by the fountain.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C3D")
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#12P#0105FYes, you're definitely not imagining it.\x02\x03",
            "#0103FDo you think they relocated?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D44")

    label("loc_6C3D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CB8")
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#12P#0203FYou are not mistaken.\x02\x03",
            "#0200FI presume they have moved to\x01",
            "a different location.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D44")

    label("loc_6CB8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D44")
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#12P#0303FYeah, you aren't crazy. I stopped by\x01",
            "it during a date the other day.\x02\x03",
            "#0301FWhere the heck did it go?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D44")

    TurnDirection(0x153, 0x101, 500)

    ChrTalk(
        0x153,
        (
            "#11P#1112FDoes that mean we can't bring\x01",
            "Gramps a drink?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)

    ChrTalk(
        0x101,
        (
            "#5P#0003FI doubt they moved outside\x01",
            "of the city.\x02\x03",
            "#0000FI'm sure we'll run into it again\x01",
            "if we keep our eyes peeled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#11P#1100FOkay!\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 8100, 2390, -5930, 225)
    OP_29(0x26, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_17_6A55 end

    def Function_18_6E3D(): pass

    label("Function_18_6E3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E61")
    OP_93(0xFE, 0x0, 0x226)
    Sleep(500)
    OP_93(0xFE, 0x10E, 0x226)
    Sleep(500)
    Jump("Function_18_6E3D")

    label("loc_6E61")

    Return()

    # Function_18_6E3D end

    def Function_19_6E62(): pass

    label("Function_19_6E62")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E86")
    OP_93(0xFE, 0xB4, 0x258)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x258)
    Sleep(500)
    Jump("Function_19_6E62")

    label("loc_6E86")

    Return()

    # Function_19_6E62 end

    def Function_20_6E87(): pass

    label("Function_20_6E87")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-18580, 4730, 27420, 0)
    MoveCamera(46, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    FadeToBright(1000, 0)
    OP_68(9150, 6030, 14130, 5000)
    MoveCamera(46, 11, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(20160, 5000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(24420, 6330, -12770, 0)
    MoveCamera(71, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16379, 0)
    SetChrFlags(0x8, 0x8000)
    OP_68(-12250, 5080, -8260, 7000)
    MoveCamera(45, 4, 0, 7000)
    OP_6E(700, 7000)
    SetCameraDistance(19000, 7000)
    PlaceName2(340, 40, "c_plac05", 0x0, 6000)
    OP_6F(0x79)
    Sleep(3000)

    AnonymousTalk(
        0x102,
        (
            "#0103FThe City Hall, CPD headquarters, and the\x01",
            "City Library...\x02\x03",
            "#0100FIt certainly lives up to the name of the\x01",
            "Administrative District, since all of the\x01",
            "primary public offices operate here.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#0202FI appreciate the tranquility of this area.\x01",
            "I can see myself relaxing on those benches.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#0104FConsidering this is one of Crossbell's\x01",
            "prime locations, I'm surprised at how\x01",
            "unusually quiet it is around here.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#0000FWell, the department is right here, so I'm sure\x01",
            "we'll be visiting frequently.\x02\x03",
            "We definitely should try to remember the way\x01",
            "here from the SSS building.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#0304FRoger that, Leader.\x02\x03",
            "#0300FDidn't we receive one of them support requests\x01",
            "from HQ tellin' us to go there? May as well pop\x01",
            "in since we're already here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Administrative District is home to all\x01",
            "administrative affairs, and is situated in\x01",
            "the northern part of the city.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Many important government institutions and\x01",
            "the CPD headquarters can be found here,\x01",
            "so you'll be visiting the area often.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In addition to Crossbell City Hall, you may\x01",
            "browse an encyclopedia to broaden your\x01",
            "understanding of the world at the City Library.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearChrFlags(0x8, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74AE")
    OP_68(19940, 2240, -37920, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    Jump("loc_74EA")

    label("loc_74AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74EA")
    OP_68(-40390, 2240, 24150, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)

    label("loc_74EA")

    SetScenarioFlags(0x45, 3)
    EventEnd(0x5)
    Return()

    # Function_20_6E87 end

    def Function_21_74F0(): pass

    label("Function_21_74F0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-7500, 3600, 25000, 0)
    MoveCamera(65, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -5500, 2500, 25000, 270)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x8)
    ClearMapObjFlags(0x1, 0x10)

    def lambda_7556():
        OP_95(0xFE, -18500, 2500, 25000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7556)
    OP_68(-18500, 3600, 25000, 7000)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    OP_68(-18500, 4300, 27000, 2500)
    MoveCamera(44, 3, 0, 2500)
    OP_6F(0x41)
    Sleep(1000)

    def lambda_75B9():
        OP_95(0xFE, -18500, 2500, 28400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75B9)
    WaitChrThread(0x101, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)

    def lambda_75EC():
        OP_95(0xFE, -18500, 3100, 31400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75EC)
    Sleep(500)

    def lambda_7609():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7609)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearScenarioFlags(0x1, 1)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_74F0 end

    def Function_22_764E(): pass

    label("Function_22_764E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-18000, 5000, 30500, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27500, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetMapObjFlags(0x6, 0x4)
    MoveCamera(0, 10, 0, 7000)
    SetCameraDistance(17500, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    ClearScenarioFlags(0x1, 1)
    SetScenarioFlags(0x5C, 1)
    NewScene("c1160", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_764E end

    def Function_23_76D6(): pass

    label("Function_23_76D6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00501.itc", 0x1E)
    LoadChrToIndex("apl/ch50220.itc", 0x1F)
    LoadEffect(0x0, "event\\eva04_00.eff")
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 33000, 12200, 6000, 270)
    SetChrPos(0x12, 33000, 12200, 6000, 270)
    SetMapObjFlags(0x2, 0x1000)
    OP_68(15000, 11200, 20000, 0)
    MoveCamera(55, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(45000, 0)
    MoveCamera(35, 0, 0, 7500)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0x12, 0x1E, 0x12C)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)

    def lambda_77BB():
        OP_9D(0xFE, 0x61A8, 0x3B60, 0x1770, 0xFA0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_77BB)
    Sound(814, 0, 70, 0)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)

    def lambda_77F1():
        OP_95(0xFE, 25000, 15200, 19900, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_77F1)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    OP_93(0x12, 0x13B, 0x0)
    SetChrSubChip(0x12, 0x0)

    def lambda_7825():
        OP_9D(0xFE, 0x4E20, 0x4074, 0x6144, 0x8FC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7825)
    Sound(814, 0, 70, 0)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)

    def lambda_7857():
        OP_9D(0xFE, 0x3A98, 0x3B60, 0x74CC, 0x514, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7857)
    Sound(814, 0, 70, 0)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)

    def lambda_788D():
        OP_95(0xFE, 2500, 15200, 29900, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_788D)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    ClearChrFlags(0x12, 0x1)
    SetChrSubChip(0x12, 0x0)

    def lambda_78BF():
        OP_9D(0xFE, 0xFFFFFE0C, 0x4268, 0x74CC, 0x8FC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_78BF)
    Sound(814, 0, 70, 0)
    WaitChrThread(0x12, 1)

    def lambda_78E6():
        OP_9D(0xFE, 0xFFFFD6FC, 0x4268, 0x74CC, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_78E6)
    Sound(814, 0, 70, 0)
    WaitChrThread(0x12, 1)
    Fade(500)
    OP_68(-25800, 14500, 37000, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)
    OP_68(-40700, 10500, 37000, 2000)
    MoveCamera(50, 20, 0, 2000)
    SetChrPos(0x12, -15800, 15500, 37000, 270)
    SetChrFlags(0x12, 0x1)
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x12, 0x0)

    def lambda_7981():
        OP_9D(0xFE, 0xFFFF9B38, 0x34BC, 0x9088, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7981)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x12, 1)
    PlayEffect(0x0, 0xFF, 0x12, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x12, 0x1)
    Sound(31, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)

    def lambda_79F0():
        OP_9D(0xFE, 0xFFFF7EB4, 0x251C, 0x9088, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_79F0)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x12, 1)
    PlayEffect(0x0, 0xFF, 0x12, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    Sound(31, 0, 100, 0)
    Sound(42, 0, 100, 0)

    def lambda_7A69():
        OP_95(0xFE, -41700, 9500, 37000, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7A69)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)

    def lambda_7A96():
        OP_9D(0xFE, 0xFFFF360C, 0x251C, 0x9088, 0x76C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7A96)
    Sound(854, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x12, 1)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    SetScenarioFlags(0x5C, 1)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_76D6 end

    def Function_24_7AE4(): pass

    label("Function_24_7AE4")

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

    # Function_24_7AE4 end

    SaveToFile()

Try(main)
