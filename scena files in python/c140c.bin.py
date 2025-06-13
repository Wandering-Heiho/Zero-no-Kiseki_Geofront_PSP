from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c140c.bin",                # FileName
        "c140c",                    # MapName
        "c140c",                    # Location
        0x002E,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 46, 0, 3, 0, 4],
    )

    BuildStringList((
        "c140c",                  # 0
        "Dino",                   # 1
        "Old Lady Paola",         # 2
        "Vaan",                   # 3
        "Ruze",                   # 4
        "Canon",                  # 5
        "Huey",                   # 6
        "Koki",                   # 7
        "Kienz",                  # 8
        "Vesse",                  # 9
        "Corona",                 # 10
        "Lima",                   # 11
        "Melson",                 # 12
        "Tourist",                # 13
        "Tourist",                # 14
        "Estelle",                # 15
        "Joshua",                 # 16
        "Wazy",                   # 17
        "Wald",                   # 18
        "Abbas",                  # 19
        "Grace",                  # 20
        "Cameraman",              # 21
        "Saber Viper",            # 22
        "Saber Viper",            # 23
        "Saber Viper",            # 24
        "Saber Viper",            # 25
        "Saber Viper",            # 26
        "Testament",              # 27
        "Testament",              # 28
        "Testament",              # 29
        "Testament",              # 30
        "Event Old Man Tantz",    # 31
        "Event Geithner",         # 32
        "Event Tourist",          # 33
        "Event Tourist",          # 34
        "Lloyd",                  # 35
        "Randy",                  # 36
        "Elie",                   # 37
        "Tio",                    # 38
        "Objet d'art",            # 39
        "Central Square",         # 40
        "West Street",            # 41
        "Administrative District",# 42
        "Residential District",   # 43
        "Entertainment District", # 44
        "East Street",            # 45
        "Downtown District",      # 46
        "Harbor District",        # 47
        "IBC",                    # 48
        "Station Street",         # 49
        "Back Alley",             # 50
        "Ursula Road",            # 51
        "East Crossbell Highway", # 52
        "West Crossbell Highway", # 53
        "Mainz Mountain Path",    # 54
    ))

    AddCharChip((
        "chr/ch06800.itc",                   # 00
        "chr/ch23302.itc",                   # 01
        "chr/ch23000.itc",                   # 02
        "chr/ch24700.itc",                   # 03
        "chr/ch23800.itc",                   # 04
        "chr/ch31700.itc",                   # 05
        "chr/ch22700.itc",                   # 06
        "chr/ch20700.itc",                   # 07
        "chr/ch26200.itc",                   # 08
        "chr/ch23700.itc",                   # 09
        "chr/ch23600.itc",                   # 0A
        "chr/ch31800.itc",                   # 0B
        "chr/ch30900.itc",                   # 0C
        "chr/ch30800.itc",                   # 0D
    ))

    DeclNpc(44880,   -2500,   -20090,  225,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(15449,   100,     -19,     270,  261,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(9640,    0,       850,     180,  261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(10279,   0,       -550,    315,  261,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(34080,   -6500,   -38270,  45,   261,  0x0, 0,   4,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(2339,    0,       -2940,   315,  405,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(43650,   -2500,   -19120,  135,  389,  0x0, 0,   13,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-140,    0,       3740,    135,  405,  0x0, 0,   11,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(920,     0,       2680,    315,  389,  0x0, 0,   12,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(9449,    0,       3140,    0,    277,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(8350,    0,       4110,    90,   261,  0x0, 0,   7,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(9560,    0,       4400,    225,  261,  0x0, 0,   8,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-19489,  0,       -9409,   0,    261,  0x0, 0,   9,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(1950,    0,       140,     180,  261,  0x0, 0,   10,  0,   0,   0,   0,   24,  255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-28460,  2800,    -29590,  1200,    -28460,  3800,    -29590,  0x007C, 0,  5,  0x0000)
    DeclActor(34830,   2450,    -19780,  1500,    34830,   3950,    -19780,  0x007C, 0,  81, 0x0000)

    PlaceName(-110.69000244140625, 0.0, 106.94999694824219, 0x0000, 0x0000, "Central Square")
    PlaceName(-186.3000030517578, 0.0, 112.12999725341797, 0x0000, 0x0000, "West Street")
    PlaceName(-79.63999938964844, 0.0, 209.3000030517578, 0x0000, 0x0000, "Administrative District")
    PlaceName(-256.45001220703125, 0.0, 197.8000030517578, 0x0000, 0x0000, "Residential District")
    PlaceName(-172.5, 0.0, 188.60000610351562, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-17.25, 0.0, 80.5, 0x0000, 0x0000, "East Street")
    PlaceName(23.579999923706055, 0.0, 17.25, 0x0000, 0x0000, "Downtown District")
    PlaceName(14.949999809265137, 0.0, 156.39999389648438, 0x0000, 0x0000, "Harbor District")
    PlaceName(-14.949999809265137, 0.0, 264.5, 0x0000, 0x0000, "IBC")
    PlaceName(-97.75, 0.0, 27.600000381469727, 0x0000, 0x0000, "Station Street")
    PlaceName(-151.8000030517578, 0.0, 147.1999969482422, 0x0000, 0x0000, "Back Alley")
    PlaceName(-101.19999694824219, 0.0, -8.050000190734863, 0x0000, 0x0000, "Ursula Road")
    PlaceName(44.849998474121094, 0.0, 96.5999984741211, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-244.9499969482422, 0.0, 110.4000015258789, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-238.0500030517578, 0.0, 225.39999389648438, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-135.99000549316406, 0.0, 90.8499984741211, 0x0000, 0x0051, "")
    PlaceName(-74.18000030517578, 0.0, 120.75, 0x0000, 0x0054, "")
    PlaceName(-107.80999755859375, 0.0, 81.6500015258789, 0x0000, 0x0057, "")
    PlaceName(-136.85000610351562, 0.0, 124.19999694824219, 0x0000, 0x0053, "")
    PlaceName(-113.27999877929688, 0.0, 151.8000030517578, 0x0000, 0x0053, "")
    PlaceName(-171.63999938964844, 0.0, 118.44999694824219, 0x0000, 0x0053, "")
    PlaceName(-182.85000610351562, 0.0, 142.60000610351562, 0x0000, 0x0053, "")
    PlaceName(-155.25, 0.0, 179.39999389648438, 0x0000, 0x0052, "")
    PlaceName(-149.7899932861328, 0.0, 164.4499969482422, 0x0000, 0x0053, "")
    PlaceName(-139.72999572753906, 0.0, 154.67999267578125, 0x0000, 0x0053, "")
    PlaceName(-106.94999694824219, 0.0, 236.3300018310547, 0x0000, 0x0051, "")
    PlaceName(21.850000381469727, 0.0, 80.5, 0x0000, 0x0052, "")
    PlaceName(2.299999952316284, 0.0, -23.579999923706055, 0x0000, 0x0053, "")
    PlaceName(-12.649999618530273, 0.0, -2.299999952316284, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_8E4",          # 00, 0
        "Function_1_99C",          # 01, 1
        "Function_2_9C7",          # 02, 2
        "Function_3_AA0",          # 03, 3
        "Function_4_DFE",          # 04, 4
        "Function_5_E70",          # 05, 5
        "Function_6_FC8",          # 06, 6
        "Function_7_134E",         # 07, 7
        "Function_8_173F",         # 08, 8
        "Function_9_1A13",         # 09, 9
        "Function_10_1ACC",        # 0A, 10
        "Function_11_1B95",        # 0B, 11
        "Function_12_1DB9",        # 0C, 12
        "Function_13_249B",        # 0D, 13
        "Function_14_24A5",        # 0E, 14
        "Function_15_263C",        # 0F, 15
        "Function_16_27BF",        # 10, 16
        "Function_17_2886",        # 11, 17
        "Function_18_29E4",        # 12, 18
        "Function_19_2B0C",        # 13, 19
        "Function_20_2D27",        # 14, 20
        "Function_21_2EF0",        # 15, 21
        "Function_22_2FAD",        # 16, 22
        "Function_23_32DF",        # 17, 23
        "Function_24_33C0",        # 18, 24
        "Function_25_363C",        # 19, 25
        "Function_26_65D2",        # 1A, 26
        "Function_27_6660",        # 1B, 27
        "Function_28_66C8",        # 1C, 28
        "Function_29_675A",        # 1D, 29
        "Function_30_67C6",        # 1E, 30
        "Function_31_6869",        # 1F, 31
        "Function_32_68E6",        # 20, 32
        "Function_33_6999",        # 21, 33
        "Function_34_6A13",        # 22, 34
        "Function_35_6A65",        # 23, 35
        "Function_36_6AB7",        # 24, 36
        "Function_37_6AE4",        # 25, 37
        "Function_38_6B28",        # 26, 38
        "Function_39_6B92",        # 27, 39
        "Function_40_6C15",        # 28, 40
        "Function_41_6C63",        # 29, 41
        "Function_42_6CB1",        # 2A, 42
        "Function_43_6CE2",        # 2B, 43
        "Function_44_6D35",        # 2C, 44
        "Function_45_6E7B",        # 2D, 45
        "Function_46_6F3E",        # 2E, 46
        "Function_47_6F8C",        # 2F, 47
        "Function_48_6FDA",        # 30, 48
        "Function_49_702C",        # 31, 49
        "Function_50_7089",        # 32, 50
        "Function_51_7135",        # 33, 51
        "Function_52_7181",        # 34, 52
        "Function_53_71EC",        # 35, 53
        "Function_54_725A",        # 36, 54
        "Function_55_72B7",        # 37, 55
        "Function_56_72D7",        # 38, 56
        "Function_57_7331",        # 39, 57
        "Function_58_738C",        # 3A, 58
        "Function_59_73C9",        # 3B, 59
        "Function_60_7452",        # 3C, 60
        "Function_61_74E1",        # 3D, 61
        "Function_62_7570",        # 3E, 62
        "Function_63_75F9",        # 3F, 63
        "Function_64_7629",        # 40, 64
        "Function_65_76DB",        # 41, 65
        "Function_66_78C6",        # 42, 66
        "Function_67_79A6",        # 43, 67
        "Function_68_79B3",        # 44, 68
        "Function_69_79BE",        # 45, 69
        "Function_70_79C9",        # 46, 70
        "Function_71_79D3",        # 47, 71
        "Function_72_D025",        # 48, 72
        "Function_73_D134",        # 49, 73
        "Function_74_D167",        # 4A, 74
        "Function_75_D19A",        # 4B, 75
        "Function_76_D1B6",        # 4C, 76
        "Function_77_D1D2",        # 4D, 77
        "Function_78_D1FE",        # 4E, 78
        "Function_79_D22A",        # 4F, 79
        "Function_80_D2B7",        # 50, 80
        "Function_81_11380",       # 51, 81
    ))


    def Function_0_8E4(): pass

    label("Function_0_8E4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_924"),
        (1, "loc_930"),
        (2, "loc_93C"),
        (3, "loc_948"),
        (4, "loc_954"),
        (5, "loc_960"),
        (6, "loc_96C"),
        (SWITCH_DEFAULT, "loc_978"),
    )


    label("loc_924")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_930")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_93C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_948")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_954")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_960")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_96C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_978")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_984")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_99B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_99B")

    Return()

    # Function_0_8E4 end

    def Function_1_99C(): pass

    label("Function_1_99C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C6")
    OP_94(0xFE, 0x8D04, 0xFFFF6E7E, 0x7800, 0xFFFF612C, 0x3E8)
    Sleep(300)
    Jump("Function_1_99C")

    label("loc_9C6")

    Return()

    # Function_1_99C end

    def Function_2_9C7(): pass

    label("Function_2_9C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A9F")
    OP_95(0xFE, 5840, 0, -6890, 5000, 0x0)
    OP_95(0xFE, 13450, -1420, -18510, 5000, 0x0)
    OP_95(0xFE, 21750, -2500, -24790, 5000, 0x0)
    OP_95(0xFE, 21750, -6500, -38390, 5000, 0x0)
    OP_95(0xFE, 7790, -6320, -37990, 5000, 0x0)
    OP_95(0xFE, -3730, -3830, -27600, 5000, 0x0)
    OP_95(0xFE, -12250, -3030, -23600, 5000, 0x0)
    OP_95(0xFE, -12250, 0, -12120, 5000, 0x0)
    OP_95(0xFE, -10970, 0, -11360, 5000, 0x0)
    OP_95(0xFE, -5510, 0, -7900, 5000, 0x0)
    Jump("Function_2_9C7")

    label("loc_A9F")

    Return()

    # Function_2_9C7 end

    def Function_3_AA0(): pass

    label("Function_3_AA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7D")
    SetChrPos(0x0, 2050, 0, 14590, 180)
    SetChrPos(0x1, 2050, 0, 14590, 180)
    SetChrPos(0x2, 2050, 0, 14590, 180)
    SetChrPos(0x3, 2050, 0, 14590, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B27")
    SetChrPos(0x4, 2050, 0, 14590, 180)
    SetChrPos(0x5, 2050, 0, 14590, 180)
    Jump("loc_B46")

    label("loc_B27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B46")
    SetChrPos(0x4, 2050, 0, 14590, 180)

    label("loc_B46")

    OP_68(2050, 2000, 14590, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B7D")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_B9A")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 25)
    Jump("loc_BBD")

    label("loc_B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_BAE")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 71)
    Jump("loc_BBD")

    label("loc_BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_BBD")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 80)

    label("loc_BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_C71")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x8, 4620, 0, -5320, 315)
    SetChrPos(0xF, 1100, 0, -1620, 135)
    SetChrPos(0x10, -310, 50, -1500, 135)
    SetChrPos(0xE, 44880, -2500, -20090, 225)
    OP_93(0x11, 0xE1, 0x0)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_DFD")

    label("loc_C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_CB5")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrPos(0xA, 1810, 0, 4550, 315)
    SetChrPos(0xB, 610, 0, 5750, 135)
    ClearChrFlags(0x11, 0x10)
    Jump("loc_DFD")

    label("loc_CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_CEF")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    TurnDirection(0x11, 0x12, 0)
    TurnDirection(0x12, 0x11, 0)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_DFD")

    label("loc_CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_DA3")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xA, 4670, 0, -5500, 180)
    SetChrPos(0xB, 4710, 0, -7160, 0)
    SetChrPos(0x14, 43330, -2500, -20060, 90)
    SetChrPos(0x15, 42420, -2500, -19200, 135)
    OP_93(0x8, 0x10E, 0x0)
    TurnDirection(0x13, 0x12, 0)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x15, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7C")
    SetChrFlags(0x8, 0x10)

    label("loc_D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D8F")
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)

    label("loc_D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9E")
    SetChrFlags(0x12, 0x10)

    label("loc_D9E")

    Jump("loc_DFD")

    label("loc_DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_DC7")
    SetChrPos(0x15, -18810, 0, -10220, 315)
    SetChrFlags(0x8, 0x80)
    Jump("loc_DFD")

    label("loc_DC7")

    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xA, 2740, 0, -770, 315)
    SetChrPos(0xB, 960, 0, 870, 135)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_DFD")

    Return()

    # Function_3_AA0 end

    def Function_4_DFE(): pass

    label("Function_4_DFE")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4D")
    OP_70(0x7, 0x0)
    Jump("loc_E51")

    label("loc_E4D")

    OP_70(0x7, 0x1E)

    label("loc_E51")

    OP_65(0x1, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6F")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_E6F")

    Return()

    # Function_4_DFE end

    def Function_5_E70(): pass

    label("Function_5_E70")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5A")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x642, 1)"), scpexpr(EXPR_END)), "loc_EF0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_F55")

    label("loc_EF0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F55")

    Jump("loc_FBC")

    label("loc_F5A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Happy birthday, Crossbell! It's Usher! *Xbox 360 sound*\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_FBC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_E70 end

    def Function_6_FC8(): pass

    label("Function_6_FC8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_105F")

    ChrTalk(
        0x8,
        (
            "Hahaha. To think I'd meet the Testaments in\x01",
            "a place like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Th-They lookin' for a fight?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I-I...\x01",
            "What should I do?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_134A")

    label("loc_105F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_112F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10D7")

    ChrTalk(
        0x8,
        (
            "A bunch of tourists have been wanderin'\x01",
            "around here all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Man, they're so annoying!\x02",
    )

    CloseMessageWindow()
    Jump("loc_112A")

    label("loc_10D7")

    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x8,
        "C'mon! This place ain't some attraction!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Get outta here!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x14, 0xFF)

    label("loc_112A")

    Jump("loc_134A")

    label("loc_112F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11D2")

    ChrTalk(
        0x8,
        (
            "Wald and the boys are about to go\x01",
            "screw around in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Geez! I asked 'em if they wanted to go,\x01",
            "and nobody seemed interested at all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_134A")

    label("loc_11D2")


    ChrTalk(
        0x8,
        (
            "Wald and the boys are about to go\x01",
            "screw around in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everybody loves the festival, so they hit up the\x01",
            "food stalls every year.\x02",
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
            "#0106FS-So, they left you here to watch\x01",
            "over the base?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Like I could do much about it!\x01",
            "I'm the lowest rung on the ladder!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_134A")

    TalkEnd(0xFE)
    Return()

    # Function_6_FC8 end

    def Function_7_134E(): pass

    label("Function_7_134E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13E2")
    Jump("loc_142C")

    label("loc_13E2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1402")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_142C")

    label("loc_1402")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1422")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_142C")

    label("loc_1422")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_142C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_148F")

    ChrTalk(
        0x9,
        "Oh, dearie. Are those boys still fighting?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1737")

    label("loc_148F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1507")

    ChrTalk(
        0x9,
        "I heard the parade was a sight to behold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Now, I think I'll whip up a delicious\x01",
            "meal for lunch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1737")

    label("loc_1507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_15C4")

    ChrTalk(
        0x9,
        (
            "With old age comes weak knees, so\x01",
            "I can no longer walk with crowds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't worry about me, dearies.\x01",
            "At least I'm able to soak in the sounds\x01",
            "of the parade every year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1737")

    label("loc_15C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1677")

    ChrTalk(
        0x9,
        (
            "I'm surprised tourists would come downtown\x01",
            "to enrich their sightseeing experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm happy that my district is becoming\x01",
            "easier on the eyes for visitors.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1737")

    label("loc_1677")


    ChrTalk(
        0x9,
        (
            "This confetti is absolutely charming...\x01",
            "The Anniversary Festival never fails to\x01",
            "make this old heart leap every year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm content with just watching\x01",
            "everyone enjoy it to the fullest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1737")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_134E end

    def Function_8_173F(): pass

    label("Function_8_173F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_17DC")

    ChrTalk(
        0xA,
        (
            "I woke up my stinkin' old man and managed\x01",
            "to con a wad of mira outta him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Heheh... Time to treat myself to somethin'\x01",
            "tasty today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0F")

    label("loc_17DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_18C2")

    ChrTalk(
        0xA,
        (
            "Dang. There were too many people around,\x01",
            "so I couldn't get a good look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's just like I thought it was going to be.\x01",
            "The parade is a no-go for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Unfortunately, looking at it doesn't fill your belly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A0F")

    label("loc_18C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1932")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_192A")

    ChrTalk(
        0xA,
        (
            "My old man's nothin' more than a drunkard\x01",
            "these days, so we're goin' alone!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_192D")

    label("loc_192A")

    Call(0, 9)

    label("loc_192D")

    Jump("loc_1A0F")

    label("loc_1932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1998")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1990")

    ChrTalk(
        0xA,
        "All right! Bring it on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "My special craft will take you down!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1993")

    label("loc_1990")

    Call(0, 10)

    label("loc_1993")

    Jump("loc_1A0F")

    label("loc_1998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_19D7")

    ChrTalk(
        0xA,
        "Did those hoodrats run off somewhere today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A0F")

    label("loc_19D7")

    OP_4B(0x15, 0xFF)

    ChrTalk(
        0xA,
        "Yo, tourist!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Spare me some mira, pal!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)

    label("loc_1A0F")

    TalkEnd(0xFE)
    Return()

    # Function_8_173F end

    def Function_9_1A13(): pass

    label("Function_9_1A13")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        "Did you hear, Ruze?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I heard the parade's goin' through\x01",
            "East Street!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Parade?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "What's that? Does it taste good?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "You dumbo. It's not food.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 4)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_9_1A13 end

    def Function_10_1ACC(): pass

    label("Function_10_1ACC")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        "All right! Bring it on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll take you down with\x01",
            "my special craft!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Fine, then I'll be the bracer girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Wanna see what I got? Too slow!\x01",
            "Come forth, Wheel of Time!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_10_1ACC end

    def Function_11_1B95(): pass

    label("Function_11_1B95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1BCA")

    ChrTalk(
        0xB,
        (
            "Hahaha!\x01",
            "There's a feast today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB5")

    label("loc_1BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1C32")

    ChrTalk(
        0xB,
        "I bumped into some old guy and hit my head...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehehe.\x01",
            "Well, at least I had fun!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB5")

    label("loc_1C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1C95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1C8D")

    ChrTalk(
        0xB,
        "What's a parade?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehehe...\x01",
            "Do ya eat it? Is it delicious?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C90")

    label("loc_1C8D")

    Call(0, 9)

    label("loc_1C90")

    Jump("loc_1DB5")

    label("loc_1C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1CFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1CF5")

    ChrTalk(
        0xB,
        "Fine, then I'll be the bracer girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Come forth, Wheel of Time!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CF8")

    label("loc_1CF5")

    Call(0, 10)

    label("loc_1CF8")

    Jump("loc_1DB5")

    label("loc_1CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_1D65")

    ChrTalk(
        0xB,
        (
            "Heehee...\x01",
            "I got my hands on some cotton candy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I think I'll split it with Vaan.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DB5")

    label("loc_1D65")


    ChrTalk(
        0xB,
        "Hey, tourist guy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If ya don't spare me some mira,\x01",
            "I'm gonna prank ya!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB5")

    TalkEnd(0xFE)
    Return()

    # Function_11_1B95 end

    def Function_12_1DB9(): pass

    label("Function_12_1DB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1F14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1E67")

    ChrTalk(
        0xC,
        (
            "I saw a super pretty bird fly east through\x01",
            "the blue sky this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Heheh. Hopefully, it's a sign that'll\x01",
            "bring happiness to all of us!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F0F")

    label("loc_1E67")


    ChrTalk(
        0xC,
        (
            "I saw a super pretty bird fly east through\x01",
            "the blue sky this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Heheh. I hope it's a sign of bigger profits to come.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I hope today's a nice one.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_1F0F")

    Jump("loc_2497")

    label("loc_1F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1FBF")

    ChrTalk(
        0xC,
        "Phew... That cleaning took everything outta me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I gotta wake up early tomorrow, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I gotta get home before it turns dark\x01",
            "and hit the hay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2497")

    label("loc_1FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2106")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2033")

    ChrTalk(
        0xC,
        "*sweep* *sweep*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "All this confetti kinda looks like\x01",
            "pretty snowflakes, don't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2101")

    label("loc_2033")


    ChrTalk(
        0xC,
        "*sweep* *sweep*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I had to sweep the heck outta the streets today\x01",
            "thanks to all this confetti piling up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Still, though. I like watching the confetti.\x01",
            "It reminds me of falling snowflakes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_2101")

    Jump("loc_2497")

    label("loc_2106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_22EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2196")

    ChrTalk(
        0xC,
        "I gotta hurry up and clean these up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Seeing people fight just makes me sad.\x01",
            "I wish they would just make peace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_2196")


    ChrTalk(
        0xC,
        (
            "Looks like those two groups started fightin'\x01",
            "again when I wasn't here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I gotta hurry up and clean these up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "This area looks like it got hit pretty hard...\x02",
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
        "#0006FS-Sorry about that...\x02",
    )


    ChrTalk(
        0x104,
        "#0306F#6PY-Yeah. Our bad...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_22E9")

    Jump("loc_2497")

    label("loc_22EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_239D")

    ChrTalk(
        0xC,
        (
            "If I can get this place squeaky clean, I bet the\x01",
            "tourists will enjoy exploring this area!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I need to clean my butt off during the\x01",
            "Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2497")

    label("loc_239D")


    ChrTalk(
        0xC,
        (
            "Ah, do you guys mind helping me pick\x01",
            "up any trash you see?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If I can get this place squeaky clean, I bet the\x01",
            "tourists will enjoy exploring this area!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'd be pretty gosh darn happy if I saw other\x01",
            "people appreciating how clean it was.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_2497")

    TalkEnd(0xFE)
    Return()

    # Function_12_1DB9 end

    def Function_13_249B(): pass

    label("Function_13_249B")

    TalkBegin(0xFE)
    Call(0, 14)
    TalkEnd(0xFE)
    Return()

    # Function_13_249B end

    def Function_14_24A5(): pass

    label("Function_14_24A5")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xD,
        (
            "When the hell'd this become your turf,\x01",
            "ya jackasses?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "When'd you get so easygoing, huh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "We tried to pass by here earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "You should try to learn your place!\x02",
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
        "#0106FSome people just never learn, do they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FAll right, we should break this up.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_14_24A5 end

    def Function_15_263C(): pass

    label("Function_15_263C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_273C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_26BE")

    ChrTalk(
        0xE,
        "I took over guard duty for the day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Here's to hopin' Dino enjoys his day off\x01",
            "at the festival!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2737")

    label("loc_26BE")


    ChrTalk(
        0xE,
        (
            "I cut Dino some slack today and let\x01",
            "him have a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Heh. Just one of my roles as a dude lookin' over him.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2737")

    Jump("loc_27BB")

    label("loc_273C")

    OP_4B(0xE, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xE,
        "Oh, yeah. I gotta head outta here soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Stay sharp, Dino!\x01",
            "Try not to miss us too much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "R-Right!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0x8, 0xFF)

    label("loc_27BB")

    TalkEnd(0xFE)
    Return()

    # Function_15_263C end

    def Function_16_27BF(): pass

    label("Function_16_27BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_27D3")
    Call(0, 14)
    Jump("loc_2882")

    label("loc_27D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_287F")

    ChrTalk(
        0xF,
        (
            "My family snagged some tickets to Arc en Ciel,\x01",
            "so I'm gonna catch a show on the last day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Hmph. I hope I don't run into any Vipers\x01",
            "along the way...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2882")

    label("loc_287F")

    Call(0, 17)

    label("loc_2882")

    TalkEnd(0xFE)
    Return()

    # Function_16_27BF end

    def Function_17_2886(): pass

    label("Function_17_2886")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        (
            "I-I thought you had tickets\x01",
            "to Arc en Ciel, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Yeah, too bad they're for a show on the\x01",
            "last day of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I can't say I enjoy using my old man's\x01",
            "leftovers like this, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "D-Don't say that, man.\x01",
            "I'm super pumped!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "We'll chill and catch the show together\x01",
            "on the last day.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_17_2886 end

    def Function_18_29E4(): pass

    label("Function_18_29E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2A61")

    ChrTalk(
        0x10,
        "W-We picked a fight with the Vipers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "O-Obviously we aren't going to\x01",
            "back down from the challenge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B08")

    label("loc_2A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2B05")

    ChrTalk(
        0x10,
        "Kienz's family is loaded.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "H-His father's actually a doctor\x01",
            "at St. Ursula Medical College.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Heh, it pays to have a good friend\x01",
            "like him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B08")

    label("loc_2B05")

    Call(0, 17)

    label("loc_2B08")

    TalkEnd(0xFE)
    Return()

    # Function_18_29E4 end

    def Function_19_2B0C(): pass

    label("Function_19_2B0C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2B85")

    ChrTalk(
        0x11,
        "Oh, dear. What a bother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Perhaps we shouldn't try to make our\x01",
            "way through with brute force...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D23")

    label("loc_2B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2C05")

    ChrTalk(
        0x11,
        "Heehee. My daughter was thrilled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I'm glad I could spend time at the festival\x01",
            "with my family this year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D23")

    label("loc_2C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2C66")
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x11,
        (
            "Make sure to hold my hand tight, Lima.\x01",
            "Don't ever let go. Okay, dear?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    Jump("loc_2D23")

    label("loc_2C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2CF2")
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x11,
        (
            "Darling, please. How about we slow\x01",
            "down our pace a little today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Lima's a small girl, so she can't keep up.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)
    Jump("loc_2D23")

    label("loc_2CF2")

    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x11,
        "Where should we head next, darling?\x02",
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)

    label("loc_2D23")

    TalkEnd(0xFE)
    Return()

    # Function_19_2B0C end

    def Function_20_2D27(): pass

    label("Function_20_2D27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2D71")
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x12,
        "What's wrong, Daddy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Let's go already!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)
    Jump("loc_2EEC")

    label("loc_2D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2DC9")

    ChrTalk(
        0x12,
        (
            "Sooo many shiny cars!\x01",
            "They were moving so slow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "That's amazing!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EEC")

    label("loc_2DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2E2B")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x12,
        (
            "Hey, hey! Why are pretty flowers\x01",
            "falling from the sky?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Jump("loc_2EEC")

    label("loc_2E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2E8A")

    ChrTalk(
        0x12,
        "Anywhere's fine with me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "If I'm with Daddy, I'll go anywhere!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E8D")

    label("loc_2E8A")

    Call(0, 21)

    label("loc_2E8D")

    Jump("loc_2EEC")

    label("loc_2E92")


    ChrTalk(
        0x12,
        (
            "I get to go outside with\x01",
            "Mommy AND Daddy today!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x12)

    ChrTalk(
        0x12,
        "Hurray!\x02",
    )

    CloseMessageWindow()

    label("loc_2EEC")

    TalkEnd(0xFE)
    Return()

    # Function_20_2D27 end

    def Function_21_2EF0(): pass

    label("Function_21_2EF0")

    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x13,
        (
            "Is there anywhere you want to\x01",
            "go today, Lima?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x12)

    ChrTalk(
        0x12,
        "Hmm... There!\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x13,
        "Over there...? So, the highway, then?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 3)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_21_2EF0 end

    def Function_22_2FAD(): pass

    label("Function_22_2FAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3029")

    ChrTalk(
        0x13,
        (
            "Right when we left, those hoodlums\x01",
            "started brewing up trouble...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "*sigh* Those guys are hopeless.\x02",
    )

    CloseMessageWindow()
    Jump("loc_32DB")

    label("loc_3029")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_30BD")

    ChrTalk(
        0x13,
        "You must watch the parade, if you can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "It's simply the most magnificent occasion\x01",
            "for creating new memories with the family!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32DB")

    label("loc_30BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3191")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x13,
        (
            "Don't worry. The parade makes sure to travel\x01",
            "through all of the major roads in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "We still have plenty of time, since it\x01",
            "supposedly visits East Street last.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Jump("loc_32DB")

    label("loc_3191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_321C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3214")
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x13,
        (
            "Lima, let's go explore East Street\x01",
            "today, shall we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "I'm sure you'll love the marketplace!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    Jump("loc_3217")

    label("loc_3214")

    Call(0, 21)

    label("loc_3217")

    Jump("loc_32DB")

    label("loc_321C")


    ChrTalk(
        0x13,
        (
            "I usually have to work all day long...\x01",
            "Now I see the sadness my little girl\x01",
            "feels while I'm away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "All right! We'll explore the festival today\x01",
            "and have the most fun you've ever had!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32DB")

    TalkEnd(0xFE)
    Return()

    # Function_22_2FAD end

    def Function_23_32DF(): pass

    label("Function_23_32DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3346")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x14,
        "Hey, what is this place supposed to be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Any idea what they do here?\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_33BC")

    label("loc_3346")


    ChrTalk(
        0x14,
        (
            "I was considering checking out\x01",
            "this bar here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Oh, the sign says they're closed for the day.\x01",
            "That's a shame.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33BC")

    TalkEnd(0xFE)
    Return()

    # Function_23_32DF end

    def Function_24_33C0(): pass

    label("Function_24_33C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3458")
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x15,
        "Whoa, whoa! That's dangerous!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I've told you over and over again. Don't mess\x01",
            "with the folks in the Downtown District.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    Jump("loc_3638")

    label("loc_3458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_3503")

    ChrTalk(
        0x15,
        (
            "I told you it wasn't a good idea to\x01",
            "check out the Downtown District...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "All the main attractions are going to be\x01",
            "out on the main streets, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3638")

    label("loc_3503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_35A1")

    ChrTalk(
        0x15,
        (
            "Have you seen my girlfriend\x01",
            "around this neighborhood?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Not really sure why, but she charged off\x01",
            "into the Downtown District on her own!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3638")

    label("loc_35A1")


    ChrTalk(
        0x15,
        (
            "Man, I accidentally ended up getting\x01",
            "involved with some delinquents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Damn it! Why'd I take my eyes off of her?\x01",
            "Today's just not my day...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_3638")

    TalkEnd(0xFE)
    Return()

    # Function_24_33C0 end

    def Function_25_363C(): pass

    label("Function_25_363C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00000.itc", 0x2D)
    LoadChrToIndex("chr/ch00100.itc", 0x2E)
    LoadChrToIndex("chr/ch00200.itc", 0x2F)
    LoadChrToIndex("chr/ch00300.itc", 0x30)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    LoadChrToIndex("chr/ch00400.itc", 0x20)
    LoadChrToIndex("chr/ch02100.itc", 0x21)
    LoadChrToIndex("chr/ch06700.itc", 0x22)
    LoadChrToIndex("chr/ch24000.itc", 0x23)
    LoadChrToIndex("chr/ch21000.itc", 0x24)
    LoadChrToIndex("chr/ch24500.itc", 0x25)
    LoadChrToIndex("chr/ch21300.itc", 0x26)
    ClearMapObjFlags(0x8, 0x20)
    ClearMapObjFlags(0x8, 0x4)
    OP_70(0x8, 0x0)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
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
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xA, 9150, 0, -7800, 275)
    SetChrPos(0xB, 9350, 0, -8700, 275)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x14, 8000, 0, -12000, 310)
    SetChrPos(0x15, 8600, 0, -11200, 310)
    SetChrChipByIndex(0x26, 0x23)
    SetChrSubChip(0x26, 0x0)
    SetChrChipByIndex(0x27, 0x24)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x26, 12000, 0, -5900, 270)
    SetChrPos(0x27, 11700, 0, -4750, 270)
    SetChrChipByIndex(0x28, 0x25)
    SetChrSubChip(0x28, 0x0)
    SetChrChipByIndex(0x29, 0x26)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)
    SetChrFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x28, 7500, 0, 400, 230)
    SetChrPos(0x29, 8050, 0, -400, 230)
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x2A, 0x4)
    ClearChrFlags(0x2B, 0x4)
    ClearChrFlags(0x2C, 0x4)
    ClearChrFlags(0x2D, 0x4)
    SetChrFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x8000)
    SetChrChipByIndex(0x2A, 0x2D)
    SetChrChipByIndex(0x2B, 0x30)
    SetChrChipByIndex(0x2C, 0x2E)
    SetChrChipByIndex(0x2D, 0x2F)
    SetChrSubChip(0x2A, 0x0)
    SetChrSubChip(0x2B, 0x0)
    SetChrSubChip(0x2C, 0x0)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)
    SetChrPos(0x2B, 1820, 0, -7540, 359)
    SetChrPos(0x2A, 480, 0, -6970, 116)
    SetChrPos(0x2C, 4750, 0, -8590, 291)
    SetChrPos(0x2D, 4320, 0, -9580, 309)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, 3500, 0, -4840, 214)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x17, 4070, 0, -5920, 235)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 350, 0, -4510, 162)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    SetChrPos(0x19, 1980, 0, -2970, 183)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x0)
    SetChrPos(0x1A, -1100, 0, -4400, 125)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0xD)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, 3900, 0, -1750, 225)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x5)
    SetChrPos(0x1E, 2100, 0, -1550, 170)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x1F, 0x5)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, 5000, 0, -2900, 250)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x20, 0xD)
    SetChrPos(0x20, 1400, 0, -650, 170)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x21, 0xD)
    SetChrSubChip(0x21, 0x0)
    SetChrPos(0x21, 4400, 0, -200, 225)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    SetChrPos(0x22, -2100, 0, -5550, 80)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x4)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x23, 0xB)
    SetChrSubChip(0x23, 0x0)
    SetChrPos(0x23, -2100, 0, -3250, 125)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x24, 0xC)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -3250, 0, -3000, 125)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x25, 0xC)
    SetChrSubChip(0x25, 0x0)
    SetChrPos(0x25, -3000, 0, -4600, 85)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    OP_68(1850, 1000, -5600, 0)
    MoveCamera(70, 31, 0, 0)
    OP_6E(670, 0)
    SetCameraDistance(17310, 0)
    FadeToBright(5000, 0)
    MoveCamera(110, 31, 0, 60000)
    SetCameraDistance(12810, 30000)
    OP_0D()

    ChrTalk(
        0x18,
        (
            "#3200217V#6P#0404FHeh. I see...\x02\x03",
            "#3200218VA chase battle utilizing downtown's\x01",
            "rugged terrain, huh?\x02\x03",
            "#3200219V#0402FSounds like a grand ol' time, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#3200220V#5P#1602FHah. Isn't this great?!\x02\x03",
            "#3200221VA chase battle where anythin' goes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#3200222V#5P#0903F#NSpeed, power, technique, and strategy...\x02\x03",
            "#3200223V#0900FWe'll need to consider all of them for this battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#3200224V#5P#0802F#NHeeey, this sounds super interesting!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x2B,
        "#3200225V#11P#0309FHaha. I know, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200226V#6P#0006FDon't toot your own horn so easily, Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#3200227V#5P#0106F#NWhile I'm glad that this isn't necessarily a fight...\x02\x03",
            "#3200228V#0101F...won't we still end up bothering all of the\x01",
            "locals in the area?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#3200229V#11P#0202F#NI do not necessarily agree. I would imagine the\x01",
            "locals are excited for an event of this nature.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x18,
        (
            "#3200230V#6P#0404FIsn't this fantastic? It's like we're our very\x01",
            "own festival attraction.\x02\x03",
            "#3200231V#0400FAnd, besides...\x01",
            "Aren't you guys planning to participate?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x18, 500)

    ChrTalk(
        0x2A,
        (
            "#3200232V#11P#0003FDon't have much of a choice now, do we?\x02\x03",
            "#3200233V#0001FWe're already this deep in, so I don't think we\x01",
            "can back down now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#3200234V#11P#0302FSheesh! You need to relax, my friend.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 800)
    TurnDirection(0x17, 0x2A, 500)

    ChrTalk(
        0x2A,
        (
            "#3200235V#6P#0011FWasn't this your idea, Randy?!\x02\x03",
            "#3200236V#0003FOkay, fine. But you guys better not use this as a\x01",
            "chance to deviate from the rules of a normal match!\x02\x03",
            "#3200237V#0013FOnce this is all over, there won't be any more\x01",
            "disputes, and no grudges will be held!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#3200238V#5P#0806F#NYeah, I don't think Joshua or I are going to\x01",
            "complain about that.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4245():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4245)
    Sleep(50)

    def lambda_4255():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_4255)
    Sleep(50)

    def lambda_4265():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4265)
    Sleep(50)

    def lambda_4275():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_4275)
    Sleep(50)

    def lambda_4285():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4285)
    Sleep(300)

    ChrTalk(
        0x19,
        (
            "#3200239V#6P#1604FHeh. Fine by me, too.\x02\x03",
            "#3200240V#1602FCan't pass an opportunity to show the police\x01",
            "and the bracers that they ain't jack...\x02\x03",
            "#3200241V#1607FI'll show you who's really the boss around here!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x19, 500)
    Sleep(150)

    ChrTalk(
        0x16,
        (
            "#3200242V#11P#0802FHaha. Bring it on, buster! I'll fight you to the\x01",
            "bitter end, fair and square!\x02\x03",
            "#3200243V#0806FBuuuut, I may have been just a touch\x01",
            "bit too rude earlier.\x02\x03",
            "#3200244V#0800FSo... Sorry about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#3200245V#1605F#6PHuh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x16, 800)
    TurnDirection(0x2C, 0x16, 800)
    TurnDirection(0x2D, 0x16, 800)
    OP_63(0x2A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x2A,
        "#3200246V#12P#0012F(Sh-She's at it again...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#3200247V#12P#0302F(This gal never ceases to amaze me.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#3200248V#6P#0409FHahaha! This girl's so full of surprises!\x02\x03",
            "#3200249V#0402FCome on. If you apologize now, then the\x01",
            "race will have lost all meaning, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x18, 500)

    ChrTalk(
        0x16,
        (
            "#3200250V#5P#0805FI mean, now that it's a friendly match,\x01",
            "I thought it'd be good to get out of the\x01",
            "way.\x02\x03",
            "#3200251V#0809FI hope we all push ourselves as hard as\x01",
            "we can and have a heck of a good time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#3200252V#11P#0906F#N*sigh* You never change, do you?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x2B, 500)

    ChrTalk(
        0x19,
        (
            "#3200253V#5P#1603FYou're definitely one strange chick.\x02\x03",
            "#3200254V#1601FWhat do I care, though?\x01",
            "'Splain the rules, Red.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#3200255V#11P#0301FWho you callin' Red?!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_47E5():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_47E5)

    def lambda_47F2():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_47F2)

    def lambda_47FF():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_47FF)

    def lambda_480C():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_480C)

    def lambda_4819():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4819)

    def lambda_4826():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4826)
    Fade(500)
    OP_68(1830, 1100, -6450, 0)
    MoveCamera(179, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17810, 0)
    SetChrPos(0x2A, 260, 0, -6350, 128)
    SetChrPos(0x2C, 3370, 0, -9330, 319)
    SetChrPos(0x2D, 2520, 0, -9890, 1)
    SetChrPos(0x19, 1190, 0, -3490, 172)
    TurnDirection(0x2B, 0x19, 0)
    Sleep(1000)

    ChrTalk(
        0x2B,
        (
            "#3200256V#5P#0300FANYWAY! As I was saying earlier, the premise\x01",
            "of this race is to 'chase each other down.'\x02\x03",
            "#3200257V#0304FWazy and Wald are Team Downtown.\x02\x03",
            "#3200258VEstelle and Joshua are Team Bracer.\x02\x03",
            "#3200259V#0300FAnd Lloyd and I are Team SSS.\x02\x03",
            "#3200260VOutta these three teams, the one that\x01",
            "completes three laps 'round downtown\x01",
            "the fastest will be crowned champ.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-21270, 1380, -10450, 0)
    MoveCamera(313, 42, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(21500, 0)
    MoveCamera(313, 29, 0, 10000)
    OP_6E(340, 10000)
    Sleep(500)
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x2B,
        (
            "#3200261V#0301FIt ain't that simple, though. There are three\x01",
            "checkpoints that'll hold up each team with every\x01",
            "passin' lap.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(44450, -1060, -22490, 0)
    MoveCamera(53, 26, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(24500, 0)
    MoveCamera(53, 14, 0, 10000)
    OP_6E(460, 10000)
    SetCameraDistance(16000, 10000)
    Sleep(300)

    AnonymousTalk(
        0x2B,
        (
            "#3200262V#0303FThe checkpoints are gonna get placed in each\x01",
            "alleyway around the district. The tech's made\x01",
            "to light up when you give 'em a good smack.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(36420, -5060, -38470, 0)
    MoveCamera(28, 26, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(24500, 0)
    MoveCamera(53, 26, 0, 10000)
    OP_6E(300, 10000)
    Sleep(300)

    AnonymousTalk(
        0x2B,
        (
            "#3200263V#0302FYou gotta light up all three checkpoints\x01",
            "for it to count as a valid lap.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1820, 1100, -6000, 0)
    MoveCamera(180, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17810, 0)
    MoveCamera(160, 21, 0, 30000)
    Sleep(1000)

    ChrTalk(
        0x2B,
        (
            "#3200264V#5P#0303FDon't expect to make a quick getaway\x01",
            "in a terrain like this.\x02\x03",
            "#3200265V#0300FAnd feel free to mess with the other teams\x01",
            "however ya like during the race...\x02\x03",
            "#3200266VBasically, you'll probably wanna interfere\x01",
            "with the other teams a lil' bit to gain ground\x01",
            "if you aren't in the lead.\x02\x03",
            "#3200267V#0304FHow ya avoid said interference will be left\x01",
            "to your team's discretion. Got all that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#3200268V#12P#0405FHmm...\x01",
            "These are some pretty thorough rules.\x02\x03",
            "#3200269V#0400FHey, just curious. Are traps allowed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#3200270V#5P#0303FThat they are, my friend.\x02\x03",
            "#3200271V#0300FNot only can you fight each other head-on,\x01",
            "but also use the terrain to impede your\x01",
            "opponents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200272V#12P#0001FGot'cha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#3200273V#6P#0905F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x16, 0x17, 500)

    ChrTalk(
        0x16,
        "#3200274V#6P#0805FWhat's up, Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#3200275V#6P#0903FNo, it's just...\x01",
            "I get the gist of the rules, but...\x02\x03",
            "#3200276V#0900F...how do we determine the starting order?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x2B, 500)

    ChrTalk(
        0x2B,
        (
            "#3200277V#5P#0300FWe'll settle it by the flip of a coin.\x02\x03",
            "#3200278VLloyd, Wald, and Estelle.\x01",
            "Each of you get out a one-mira coin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200279V#12P#0005FOkay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#3200280V#6P#1602FHmph...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#3200281V#6P#0804FGot it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#3200282V#5P#0304FNow, flip the coin onto the back of your hand.\x02\x03",
            "#3200283V#0300FWhoever flips a unique side gets\x01",
            "to go first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200284V#0000F#12PHey, that's a smart idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#3200285V#0800F#6PWell, here goes nothing.\x02",
    )

    CloseMessageWindow()

    def lambda_5263():
        OP_A6(0xFE, 0x0, 0x64, 0xFA, 0x5DC)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_5263)

    def lambda_527C():
        OP_A6(0xFE, 0x0, 0x64, 0xFA, 0x5DC)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_527C)

    def lambda_5295():
        OP_A6(0xFE, 0x0, 0x64, 0xFA, 0x5DC)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5295)
    Sound(860, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd, Estelle, and Wald\x01",
            "each flipped their coin.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_6E(470, 5000)
    Sleep(1800)

    ChrTalk(
        0x2A,
        "#3200286V#0001F#12PHeads.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#3200287V#0800F#6PAlso heads.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#3200288V#6P#1604FTails...\x01",
            "Heh. Looks like we're up first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200289V#0001F#12PCrap...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#3200290V#0801F#6PArgh! Darn it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#3200291V#5P#0300FCongrats. Wazy, do me a solid\x01",
            "and flip another coin, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#3200292V#12P#0404FSure.\x02",
    )

    CloseMessageWindow()

    def lambda_544D():
        OP_A6(0xFE, 0x0, 0x64, 0xFA, 0x5DC)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_544D)
    Sound(860, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wazy flipped the coin.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    TurnDirection(0x2B, 0x16, 500)
    Sleep(300)

    ChrTalk(
        0x2B,
        (
            "#3200293V#11P#0300FLloyd, Estelle.\x02\x03",
            "#3200294VHeads or tails?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x2A, 500)

    ChrTalk(
        0x16,
        "#3200295V#0805F#5PUmm...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x16, 500)

    ChrTalk(
        0x2A,
        "#3200296V#0002F#11PDon't worry about it. You pick first, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#3200297V#0809F#5PThanks, I'll take you up on that offer.\x01",
            "Okay, heads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200298V#0000F#11PSounds like I'm tails, then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wazy opened his hand.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sleep(1000)

    ChrTalk(
        0x18,
        "#3200299V#12P#0404FTails... Team SSS starts second.\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x16, 0x17, 500)

    ChrTalk(
        0x16,
        (
            "#3200300V#0806F#6PNot again...\x01",
            "Sorry, Joshua.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x16, 500)

    ChrTalk(
        0x17,
        (
            "#3200301V#0904F#5PHaha. It's not a big deal.\x02\x03",
            "#3200302V#0900FThe starting order doesn't matter too much\x01",
            "with rules like these.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x2C, 3540, 0, -7660, 2000, 0x0)
    TurnDirection(0x2C, 0x18, 500)

    ChrTalk(
        0x2C,
        (
            "#3200303V#0100F#5PWell, then. Now that we've gotten that out\x01",
            "of the way, is everybody ready to begin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#3200304V#0304F#11PYep. Sure seems that way.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x19, 500)

    def lambda_57F7():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_57F7)
    Sleep(50)

    def lambda_5807():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5807)
    Sleep(50)

    def lambda_5817():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_5817)
    Sleep(500)

    ChrTalk(
        0x2B,
        (
            "#3200305V#0300F#5PEach team should get together and have\x01",
            "a lil' strategy meetin' before we begin.\x02\x03",
            "#3200306VWon't be much time for chattin' once\x01",
            "the race starts, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#3200307V#0809F#6PHaha. That's a pretty good point.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x19, 500)

    ChrTalk(
        0x18,
        (
            "#3200308V#0409F#11PLet's get to it then, Wald. Shall we have\x01",
            "ourselves a lovely pregame meeting?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 500)

    ChrTalk(
        0x19,
        "#3200309V#1601F#5PYa never fail to give me the creeps.\x02",
    )

    CloseMessageWindow()

    def lambda_59BF():
        OP_95(0xFE, 9480, 0, -3490, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_59BF)
    Sleep(50)

    def lambda_59DC():
        OP_95(0xFE, 2900, 0, -8940, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_59DC)
    Sleep(50)

    def lambda_59F9():

        label("loc_59F9")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_59F9")

    QueueWorkItem2(0x1D, 2, lambda_59F9)

    def lambda_5A0B():

        label("loc_5A0B")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_5A0B")

    QueueWorkItem2(0x1E, 2, lambda_5A0B)

    def lambda_5A1D():

        label("loc_5A1D")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_5A1D")

    QueueWorkItem2(0x1F, 2, lambda_5A1D)

    def lambda_5A2F():

        label("loc_5A2F")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_5A2F")

    QueueWorkItem2(0x20, 2, lambda_5A2F)

    def lambda_5A41():

        label("loc_5A41")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_5A41")

    QueueWorkItem2(0x21, 2, lambda_5A41)

    def lambda_5A53():
        OP_95(0xFE, -800, 0, 1900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_5A53)
    Sleep(100)

    def lambda_5A70():
        OP_95(0xFE, 9180, 50, -2440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5A70)
    Sleep(50)

    def lambda_5A8D():

        label("loc_5A8D")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_5A8D")

    QueueWorkItem2(0x22, 2, lambda_5A8D)

    def lambda_5A9F():

        label("loc_5A9F")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_5A9F")

    QueueWorkItem2(0x23, 2, lambda_5A9F)

    def lambda_5AB1():

        label("loc_5AB1")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_5AB1")

    QueueWorkItem2(0x24, 2, lambda_5AB1)

    def lambda_5AC3():

        label("loc_5AC3")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_5AC3")

    QueueWorkItem2(0x25, 2, lambda_5AC3)

    def lambda_5AD5():

        label("loc_5AD5")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_5AD5")

    QueueWorkItem2(0x1A, 2, lambda_5AD5)

    def lambda_5AE7():
        OP_95(0xFE, -1540, 0, 790, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5AE7)
    Sleep(50)

    def lambda_5B04():
        OP_95(0xFE, -4280, 0, -10520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_5B04)
    Sleep(50)

    def lambda_5B21():
        OP_95(0xFE, -3260, 0, -10950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_5B21)
    Sleep(1000)
    Fade(500)
    OP_68(-4510, 3150, -11210, 0)
    MoveCamera(57, 21, 0, 0)
    OP_6E(280, 0)
    SetCameraDistance(29500, 0)
    OP_68(-4510, 1750, -11210, 3000)
    MoveCamera(74, 29, 0, 3000)
    OP_6E(280, 3000)
    SetCameraDistance(29500, 3000)
    Sleep(3000)

    ChrTalk(
        0x2B,
        (
            "#3200310V#11P#0303FI'm sure you've already noticed it, Lloyd...\x02\x03",
            "#3200311V#0301F...but we're easily the most disadvantaged\x01",
            "in this race.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "#3200312V#0006F#5PYeah, you're probably right.\x02\x03",
            "#3200313V#0013FWazy and Wald know the Downtown District\x01",
            "like the back of their hands.\x02\x03",
            "#3200314VOn the other hand, I feel like Estelle and Joshua\x01",
            "are more formidable than they let on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#3200315V#11P#0306FPretty much.\x02\x03",
            "#3200316V#0301FIt'll be a shot in the dark, but dependin' on our\x01",
            "luck and teamwork, we might pull this off.\x02\x03",
            "#3200317V#0300FI'll cover the rear, so I'll leave the vanguard\x01",
            "in your hands, eh?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(150)

    ChrTalk(
        0x2A,
        (
            "#3200318V#0005F#6PNo complaints here, but...aren't\x01",
            "you way faster than I am?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2A, 500)

    ChrTalk(
        0x2B,
        (
            "#3200319V#11P#0304FWhen workin' in pairs, it's easier to coordinate\x01",
            "if the faster one is giving support from the back.\x02\x03",
            "#3200320V#0300FAnd, your tonfas are gonna be handier than my\x01",
            "halberd when it comes to wardin' off attacks.\x02\x03",
            "#3200321VThat quick brain of yours is better for makin' snap\x01",
            "decisions, like whether to counterattack or dodge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "#3200322V#0003F#6PHmm... Well, it's now or never.\x01",
            "Let's give it a shot, Randy.\x02\x03",
            "#3200323V#0000FOur opponents are no walk in the park, but if\x01",
            "we stick to the plan, we'll come out victorious!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#3200324V#0309F#11PHaha. That's the spirit!\x02",
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x2B,
        (
            "#3200325V#11P#0305FOh, yeah. That reminds me.\x02\x03",
            "#3200326V#0300FIt's a kinda rare opportunity, so how\x01",
            "'bout we try out a combo craft during\x01",
            "the race?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x2A,
        (
            "#3200327V#0005F#6PUh, sure. You think it'll be a good idea\x01",
            "without practicing first, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#3200328V#11P#0304FWell, I'd reckon we understand each\x01",
            "other's movements pretty well by now.\x02\x03",
            "#3200329V#0300FLet's get it done, Lloyd! No rehearsal needed!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 4)), scpexpr(EXPR_END)), "loc_63BE")
    AddCraft(0x0, 0x156)
    AddCraft(0x3, 0x156)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Randy learned \x07\x02",
            "[Burning Rage 2]\x07\x05",
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By spending 100 CP each, a powerful\x01",
            "combination attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In this chase battle, you can choose\x01",
            "to use it against the enemy teams.\x01",
            "(There's no need to worry about spending CP.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_64DF")

    label("loc_63BE")

    AddCraft(0x0, 0x14C)
    AddCraft(0x3, 0x14C)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Randy learned \x07\x02",
            "[Burning Rage]\x07\x05",
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By spending 100 CP each, a powerful\x01",
            "combination attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In this chase battle, you can choose\x01",
            "to use it against the enemy teams.\x01",
            "(There's no need to worry about spending CP.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_64DF")

    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x1E, 0xFF)
    EndChrThread(0x1F, 0xFF)
    EndChrThread(0x20, 0xFF)
    EndChrThread(0x21, 0xFF)
    EndChrThread(0x22, 0xFF)
    EndChrThread(0x23, 0xFF)
    EndChrThread(0x24, 0xFF)
    EndChrThread(0x25, 0xFF)
    EndChrThread(0x1A, 0xFF)
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
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
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
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    Call(0, 71)
    Return()

    # Function_25_363C end

    def Function_26_65D2(): pass

    label("Function_26_65D2")

    OP_95(0xFE, -8980, 0, -10190, 7000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x2A)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 7000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 7000, 0x0)
    Return()

    # Function_26_65D2 end

    def Function_27_6660(): pass

    label("Function_27_6660")

    OP_95(0xFE, -8740, 0, -11240, 6000, 0x0)
    OP_95(0xFE, -17490, 0, -11470, 6000, 0x0)
    Sleep(500)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 6000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 6000, 0x0)
    Return()

    # Function_27_6660 end

    def Function_28_66C8(): pass

    label("Function_28_66C8")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, -8980, 0, -10190, 7000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x32)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, -14710, 0, -11410, 7000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 7000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 7000, 0x0)
    Return()

    # Function_28_66C8 end

    def Function_29_675A(): pass

    label("Function_29_675A")

    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, -8740, 0, -11240, 6000, 0x0)
    OP_95(0xFE, -17490, 0, -11470, 6000, 0x0)
    Sleep(500)
    OP_95(0xFE, -14710, 0, -11410, 5000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 6000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 6000, 0x0)
    Return()

    # Function_29_675A end

    def Function_30_67C6(): pass

    label("Function_30_67C6")

    SetChrPos(0xFE, -980, 0, -8050, 272)
    SetChrChipByIndex(0xFE, 0x30)
    OP_95(0xFE, -8980, 0, -10190, 7000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x30)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 7000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 7000, 0x0)
    Return()

    # Function_30_67C6 end

    def Function_31_6869(): pass

    label("Function_31_6869")

    SetChrPos(0xFE, -1210, 0, -9240, 256)
    SetChrChipByIndex(0xFE, 0x2D)
    OP_95(0xFE, -8740, 0, -11240, 6000, 0x0)
    OP_95(0xFE, -17490, 0, -11470, 6000, 0x0)
    Sleep(500)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 6000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 6000, 0x0)
    Return()

    # Function_31_6869 end

    def Function_32_68E6(): pass

    label("Function_32_68E6")

    SetChrPos(0xFE, -980, 0, -8050, 272)
    SetChrChipByIndex(0xFE, 0x30)
    OP_95(0xFE, -8980, 0, -10190, 6000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -14710, 0, -11410, 5000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 6000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 6000, 0x0)
    Return()

    # Function_32_68E6 end

    def Function_33_6999(): pass

    label("Function_33_6999")

    SetChrPos(0xFE, -1210, 0, -9240, 256)
    SetChrChipByIndex(0xFE, 0x2D)
    OP_95(0xFE, -8740, 0, -11240, 5000, 0x0)
    OP_95(0xFE, -18490, 0, -11470, 4000, 0x0)
    OP_95(0xFE, -14710, 0, -11410, 5000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 5000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 5000, 0x0)
    Return()

    # Function_33_6999 end

    def Function_34_6A13(): pass

    label("Function_34_6A13")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrPos(0xFE, -9470, -3280, -24010, 7000)
    OP_95(0xFE, -3020, -3880, -27130, 7000, 0x0)
    OP_95(0xFE, 8500, -6390, -35860, 6000, 0x0)
    OP_95(0xFE, 26760, -6490, -37430, 6000, 0x0)
    Return()

    # Function_34_6A13 end

    def Function_35_6A65(): pass

    label("Function_35_6A65")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrPos(0xFE, -11390, -3080, -24680, 6000)
    OP_95(0xFE, -4560, -3800, -27110, 6000, 0x0)
    OP_95(0xFE, 5280, -5590, -36320, 6000, 0x0)
    OP_95(0xFE, 26700, -6490, -39330, 6000, 0x0)
    Return()

    # Function_35_6A65 end

    def Function_36_6AB7(): pass

    label("Function_36_6AB7")

    SetChrChipByIndex(0xFE, 0x27)
    OP_95(0xFE, 22720, -6500, -37590, 7000, 0x0)
    OP_95(0xFE, 21220, -2500, -25410, 7000, 0x0)
    Return()

    # Function_36_6AB7 end

    def Function_37_6AE4(): pass

    label("Function_37_6AE4")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 30470, -6500, -37950, 6000, 0x0)
    OP_95(0xFE, 21840, -6500, -37170, 5000, 0x0)
    OP_95(0xFE, 22440, -2550, -25860, 6000, 0x0)
    Return()

    # Function_37_6AE4 end

    def Function_38_6B28(): pass

    label("Function_38_6B28")

    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, 32280, -6500, -38450, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x35)
    OP_71(0xA, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, 21840, -6500, -37170, 5000, 0x0)
    OP_95(0xFE, 22440, -2550, -25860, 6000, 0x0)
    Return()

    # Function_38_6B28 end

    def Function_39_6B92(): pass

    label("Function_39_6B92")

    Sound(532, 0, 100, 0)
    OP_71(0xF, 0xA, 0x28, 0x0, 0x20)
    OP_9D(0x2E, 0x66BC, 0xFFFFE890, 0xFFFF6A96, 0x3E8, 0xFA0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(826, 0, 100, 0)
    OP_9D(0x2E, 0x61A8, 0xFFFFE890, 0xFFFF6A96, 0x190, 0xFA0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_95(0x2E, 8840, -6430, -36090, 6000, 0x0)
    SetMapObjFlags(0xF, 0x4)
    Return()

    # Function_39_6B92 end

    def Function_40_6C15(): pass

    label("Function_40_6C15")

    SetChrPos(0xFE, 21840, -6500, -37170, 0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -24770, 5000, 0x0)
    OP_95(0xFE, 41360, -2510, -23000, 6000, 0x0)
    Return()

    # Function_40_6C15 end

    def Function_41_6C63(): pass

    label("Function_41_6C63")

    SetChrPos(0xFE, 21840, -6500, -40170, 0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -24770, 5000, 0x0)
    OP_95(0xFE, 41360, -2510, -23000, 6000, 0x0)
    Return()

    # Function_41_6C63 end

    def Function_42_6CB1(): pass

    label("Function_42_6CB1")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrPos(0xFE, 25590, -2500, -24700, 340)
    OP_95(0xFE, 41840, -2500, -24090, 7000, 0x0)
    TurnDirection(0xFE, 0x2A, 500)
    Return()

    # Function_42_6CB1 end

    def Function_43_6CE2(): pass

    label("Function_43_6CE2")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrPos(0xFE, 27000, -2500, -23420, 0)
    OP_95(0xFE, 43180, -2500, -22300, 5000, 0x0)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x29)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    TurnDirection(0xFE, 0x2A, 500)
    Return()

    # Function_43_6CE2 end

    def Function_44_6D35(): pass

    label("Function_44_6D35")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 43240, -2500, -22630, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x32)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 37240, -2500, -22750, 7000, 0x0)
    OP_95(0xFE, 19890, -2500, -22930, 7000, 0x0)
    OP_95(0xFE, 8740, 0, -11540, 6000, 0x0)
    OP_95(0xFE, 4170, -10, -8870, 7000, 0x0)
    OP_95(0xFE, -4930, -10, -8640, 7000, 0x0)
    OP_95(0xFE, -10890, -10, -11230, 7000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 7000, 0x0)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x32)
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, -18070, 0, -10380, 6000, 0x0)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 5000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 5000, 0x0)
    Return()

    # Function_44_6D35 end

    def Function_45_6E7B(): pass

    label("Function_45_6E7B")

    Sleep(500)
    OP_95(0xFE, 34760, -2500, -23810, 5000, 0x0)
    OP_95(0xFE, 19890, -2500, -22930, 6000, 0x0)
    OP_95(0xFE, 8740, 0, -11540, 7000, 0x0)
    OP_95(0xFE, 4170, -10, -8870, 7000, 0x0)
    OP_95(0xFE, -4930, -10, -8640, 7000, 0x0)
    OP_95(0xFE, -10890, -10, -11230, 6000, 0x0)
    OP_95(0xFE, -18320, 0, -11470, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, -12880, 0, -13440, 5000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 5000, 0x0)
    Return()

    # Function_45_6E7B end

    def Function_46_6F3E(): pass

    label("Function_46_6F3E")

    SetChrPos(0xFE, 21840, -6500, -37170, 0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -24770, 5000, 0x0)
    OP_95(0xFE, 41360, -2510, -23000, 6000, 0x0)
    Return()

    # Function_46_6F3E end

    def Function_47_6F8C(): pass

    label("Function_47_6F8C")

    SetChrPos(0xFE, 21840, -6500, -40170, 0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -24770, 5000, 0x0)
    OP_95(0xFE, 41360, -2510, -23000, 6000, 0x0)
    Return()

    # Function_47_6F8C end

    def Function_48_6FDA(): pass

    label("Function_48_6FDA")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrPos(0xFE, -9470, -3280, -24010, 9000)
    OP_95(0xFE, -3020, -3880, -27130, 9000, 0x0)
    OP_95(0xFE, 8500, -6390, -35860, 9000, 0x0)
    OP_95(0xFE, 35200, -6490, -38160, 9000, 0x0)
    Return()

    # Function_48_6FDA end

    def Function_49_702C(): pass

    label("Function_49_702C")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrPos(0xFE, -11390, -3080, -24680, 9000)
    OP_95(0xFE, -4560, -3800, -27110, 9000, 0x0)
    OP_95(0xFE, 5280, -5590, -36320, 9000, 0x0)
    OP_95(0xFE, 33860, -6490, -39150, 9000, 0x0)
    SetChrChipByIndex(0xFE, 0x34)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_49_702C end

    def Function_50_7089(): pass

    label("Function_50_7089")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrPos(0xFE, 23260, -6490, -37200, 99)
    OP_95(0xFE, 32750, -6490, -37340, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x2C)

    def lambda_70BB():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_70BB)
    SetChrFlags(0xFE, 0x4)
    Sound(854, 0, 100, 0)
    OP_9D(0xFE, 0x8EB2, 0xFFFFEC78, 0xFFFF69C4, 0x7D0, 0xFA0)
    OP_71(0xA, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_9D(0xFE, 0x7FEE, 0xFFFFE6A6, 0xFFFF6E24, 0x1F4, 0xFA0)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x2D)
    Sound(326, 0, 100, 0)
    Sleep(300)
    OP_95(0xFE, 22640, -6490, -36980, 7000, 0x0)
    Return()

    # Function_50_7089 end

    def Function_51_7135(): pass

    label("Function_51_7135")

    SetChrPos(0xFE, 22340, -6490, -38660, 94)
    Sleep(500)
    OP_95(0xFE, 31530, -6490, -39340, 7000, 0x0)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x0)
    Sleep(1300)
    SetChrChipByIndex(0x17, 0x30)
    OP_95(0xFE, 22640, -6490, -36980, 7000, 0x0)
    Return()

    # Function_51_7135 end

    def Function_52_7181(): pass

    label("Function_52_7181")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 21840, -6500, -37170, 6000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 7000, 0x0)
    OP_95(0xFE, 22800, -2510, -24500, 6000, 0x0)
    OP_95(0xFE, 31620, -2500, -22500, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x31)

    def lambda_71DE():

        label("loc_71DE")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_71DE")

    QueueWorkItem2(0xFE, 2, lambda_71DE)
    Return()

    # Function_52_7181 end

    def Function_53_71EC(): pass

    label("Function_53_71EC")

    Sleep(400)
    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, 21840, -6500, -38170, 5000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 7000, 0x0)
    OP_95(0xFE, 22800, -2510, -25000, 7000, 0x0)
    OP_95(0xFE, 30970, -2500, -24000, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x34)

    def lambda_724C():

        label("loc_724C")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_724C")

    QueueWorkItem2(0xFE, 2, lambda_724C)
    Return()

    # Function_53_71EC end

    def Function_54_725A(): pass

    label("Function_54_725A")

    SetChrChipByIndex(0xFE, 0x27)
    EndChrThread(0xFE, 0x2)
    OP_95(0xFE, 42800, -2500, -23020, 7000, 0x0)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x26)
    Sound(532, 0, 100, 0)
    OP_A1(0xFE, 0xFA0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    SetChrChipByIndex(0xFE, 0x27)
    OP_95(0xFE, 23080, -2500, -23890, 7000, 0x0)
    Return()

    # Function_54_725A end

    def Function_55_72B7(): pass

    label("Function_55_72B7")

    Sleep(2400)
    SetChrChipByIndex(0xFE, 0x2A)
    EndChrThread(0xFE, 0x2)
    OP_95(0xFE, 23080, -2500, -23890, 7000, 0x0)
    Return()

    # Function_55_72B7 end

    def Function_56_72D7(): pass

    label("Function_56_72D7")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrFlags(0xFE, 0x4)
    Sound(814, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFCB8A, 0x10CC, 0xFFFFE049, 0x3E8, 0xFA0)
    SetChrChipByIndex(0xFE, 0x29)

    def lambda_7306():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7306)
    Sound(854, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFB438, 0x7D0, 0xFFFFD7A6, 0x7D0, 0xFA0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_56_72D7 end

    def Function_57_7331(): pass

    label("Function_57_7331")

    OP_93(0xFE, 0x10E, 0x320)
    SetChrChipByIndex(0xFE, 0x29)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x2A)
    OP_95(0xFE, -14710, 0, -11410, 7000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 7000, 0x0)
    Return()

    # Function_57_7331 end

    def Function_58_738C(): pass

    label("Function_58_738C")

    OP_95(0xFE, -14710, 0, -11410, 5000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 5000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 5000, 0x0)
    Return()

    # Function_58_738C end

    def Function_59_73C9(): pass

    label("Function_59_73C9")

    SetChrPos(0xFE, 30590, -6500, -36930, 45)
    OP_95(0xFE, 21840, -6500, -37170, 5000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 5000, 0x0)
    OP_95(0xFE, 22800, -2510, -24000, 6000, 0x0)
    OP_95(0xFE, 33880, -2500, -23450, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x38)
    BeginChrThread(0xFE, 2, 0, 70)
    OP_9C(0xFE, 0x3E8, 0x0, 0x0, 0x64, 0xBB8)
    Sound(514, 0, 100, 0)
    Return()

    # Function_59_73C9 end

    def Function_60_7452(): pass

    label("Function_60_7452")

    SetChrPos(0xFE, 32990, -6500, -39280, 315)
    OP_95(0xFE, 21840, -6500, -38170, 5000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 7000, 0x0)
    OP_95(0xFE, 22800, -2510, -25000, 6000, 0x0)
    OP_95(0xFE, 33550, -2500, -25230, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x37)
    BeginChrThread(0xFE, 2, 0, 70)
    Sound(590, 0, 100, 0)
    OP_9C(0xFE, 0x960, 0x0, 0x0, 0x64, 0xFA0)
    Sound(819, 0, 100, 0)
    Return()

    # Function_60_7452 end

    def Function_61_74E1(): pass

    label("Function_61_74E1")

    SetChrPos(0xFE, 27350, -6500, -39590, 210)
    OP_95(0xFE, 21840, -6500, -37170, 6000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 5000, 0x0)
    OP_95(0xFE, 22800, -2510, -24500, 6000, 0x0)
    OP_95(0xFE, 33770, -2500, -22910, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x39)
    BeginChrThread(0xFE, 2, 0, 70)
    Sound(590, 0, 100, 0)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x64, 0xBB8)
    Sound(819, 0, 100, 0)
    Return()

    # Function_61_74E1 end

    def Function_62_7570(): pass

    label("Function_62_7570")

    SetChrPos(0xFE, 29850, -6500, -40680, 135)
    OP_95(0xFE, 21840, -6500, -38170, 6000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -25000, 6000, 0x0)
    OP_95(0xFE, 33350, -2500, -24540, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x3A)
    BeginChrThread(0xFE, 2, 0, 70)
    OP_9C(0xFE, 0x4E2, 0x0, 0x0, 0x64, 0xFA0)
    Sound(514, 0, 100, 0)
    Return()

    # Function_62_7570 end

    def Function_63_75F9(): pass

    label("Function_63_75F9")

    OP_95(0xFE, 30930, 2390, -21190, 6000, 0x0)
    OP_95(0xFE, 34310, 2450, -21190, 6000, 0x0)
    OP_93(0xFE, 0xB4, 0x2BC)
    Return()

    # Function_63_75F9 end

    def Function_64_7629(): pass

    label("Function_64_7629")

    OP_95(0x2A, 40240, -1000, -27180, 7000, 0x0)
    Sound(814, 0, 100, 0)
    OP_9D(0x2A, 0xA028, 0xFFFFF63C, 0xFFFFA07E, 0x3E8, 0xFA0)
    Sound(42, 0, 100, 0)
    Sound(31, 0, 100, 0)
    OP_95(0x2A, 43620, -2500, -22910, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x32)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x33)
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x0, 0x0, 0x0)
    Sleep(150)
    OP_95(0x2A, 41240, -2490, -22980, 4000, 0x0)
    SetChrChipByIndex(0xFE, 0x31)

    def lambda_76CD():

        label("loc_76CD")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_76CD")

    QueueWorkItem2(0xFE, 2, lambda_76CD)
    Return()

    # Function_64_7629 end

    def Function_65_76DB(): pass

    label("Function_65_76DB")

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
    OP_D5(0x0)
    OP_D5(0x1)
    OP_D5(0x2)
    OP_D5(0x3)
    OP_D5(0x4)
    OP_D5(0x6)
    OP_D5(0x7)
    OP_D5(0x8)
    OP_D5(0x9)
    OP_D5(0xA)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    LoadChrToIndex("chr/ch00400.itc", 0x20)
    LoadChrToIndex("chr/ch02100.itc", 0x21)
    LoadChrToIndex("chr/ch06700.itc", 0x22)
    LoadChrToIndex("chr/ch06000.itc", 0x23)
    LoadChrToIndex("apl/ch50378.itc", 0x24)
    LoadChrToIndex("chr/ch02150.itc", 0x25)
    LoadChrToIndex("chr/ch02152.itc", 0x26)
    LoadChrToIndex("chr/ch02151.itc", 0x27)
    LoadChrToIndex("chr/ch00450.itc", 0x28)
    LoadChrToIndex("chr/ch00452.itc", 0x29)
    LoadChrToIndex("chr/ch00451.itc", 0x2A)
    LoadChrToIndex("chr/ch00650.itc", 0x2B)
    LoadChrToIndex("chr/ch00652.itc", 0x2C)
    LoadChrToIndex("chr/ch00651.itc", 0x2D)
    LoadChrToIndex("chr/ch00750.itc", 0x2E)
    LoadChrToIndex("chr/ch00752.itc", 0x2F)
    LoadChrToIndex("chr/ch00751.itc", 0x30)
    LoadChrToIndex("chr/ch00050.itc", 0x31)
    LoadChrToIndex("chr/ch00052.itc", 0x32)
    LoadChrToIndex("chr/ch00051.itc", 0x33)
    LoadChrToIndex("chr/ch00350.itc", 0x34)
    LoadChrToIndex("chr/ch00352.itc", 0x35)
    LoadChrToIndex("chr/ch00351.itc", 0x36)
    LoadChrToIndex("chr/ch02153.itc", 0x37)
    LoadChrToIndex("chr/ch00453.itc", 0x38)
    LoadChrToIndex("chr/ch00653.itc", 0x39)
    LoadChrToIndex("chr/ch00753.itc", 0x3A)
    LoadChrToIndex("chr/ch00053.itc", 0x3B)
    LoadChrToIndex("chr/ch00353.itc", 0x3C)
    LoadChrToIndex("chr/ch00357.itc", 0x3D)
    LoadChrToIndex("apl/ch50311.itc", 0x3E)
    LoadChrToIndex("apl/ch50314.itc", 0x3F)
    LoadChrToIndex("chr/ch00155.itc", 0x40)
    LoadChrToIndex("apl/ch50312.itc", 0x41)
    ClearMapObjFlags(0x8, 0x20)
    ClearMapObjFlags(0x8, 0x4)
    OP_70(0x8, 0x0)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
    OP_52(0x2A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_65_76DB end

    def Function_66_78C6(): pass

    label("Function_66_78C6")

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
    SetChrFlags(0x2A, 0x80)
    SetChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x80)
    SetChrBattleFlags(0x2B, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    OP_D5(0x2F)
    OP_D5(0x30)
    OP_D5(0x31)
    OP_D5(0x32)
    OP_D5(0x33)
    OP_D5(0x34)
    OP_D5(0x35)
    OP_D5(0x36)
    OP_D5(0x37)
    OP_D5(0x38)
    OP_D5(0x39)
    OP_D5(0x3A)
    OP_D5(0x3B)
    OP_D5(0x3C)
    OP_D5(0x3D)
    OP_D5(0x3E)
    OP_D5(0x3F)
    OP_D5(0x40)
    OP_D5(0x41)
    Return()

    # Function_66_78C6 end

    def Function_67_79A6(): pass

    label("Function_67_79A6")

    OP_A1(0xFE, 0x6A4, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Return()

    # Function_67_79A6 end

    def Function_68_79B3(): pass

    label("Function_68_79B3")

    OP_A1(0xFE, 0x6A4, 0x4, 0x0, 0x1, 0x2, 0x3)
    Return()

    # Function_68_79B3 end

    def Function_69_79BE(): pass

    label("Function_69_79BE")

    OP_A1(0xFE, 0x6A4, 0x4, 0x3, 0x2, 0x1, 0x0)
    Return()

    # Function_69_79BE end

    def Function_70_79C9(): pass

    label("Function_70_79C9")

    OP_A1(0xFE, 0x6A4, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_70_79C9 end

    def Function_71_79D3(): pass

    label("Function_71_79D3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x2A, 0x80)
    SetChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x80)
    SetChrBattleFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    OP_49()
    Call(0, 65)
    LoadChrToIndex("chr/ch00000.itc", 0x37)
    LoadChrToIndex("chr/ch00100.itc", 0x38)
    LoadChrToIndex("chr/ch00200.itc", 0x39)
    LoadChrToIndex("chr/ch00300.itc", 0x3A)
    ClearChrFlags(0x2A, 0x4)
    ClearChrFlags(0x2B, 0x4)
    ClearChrFlags(0x2C, 0x4)
    ClearChrFlags(0x2D, 0x4)
    SetChrFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x8000)
    SetChrChipByIndex(0x2A, 0x37)
    SetChrChipByIndex(0x2B, 0x3A)
    SetChrChipByIndex(0x2C, 0x38)
    SetChrChipByIndex(0x2D, 0x39)
    SetChrSubChip(0x2A, 0x0)
    SetChrSubChip(0x2B, 0x0)
    SetChrSubChip(0x2C, 0x0)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x23)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x0)
    SetChrPos(0x2C, -5340, 0, -6550, 122)
    SetChrPos(0x2D, -4410, 0, -5830, 122)
    SetChrPos(0x18, -3140, 0, -8130, 302)
    SetChrPos(0x19, -3080, 0, -9580, 302)
    SetChrPos(0x2A, -980, 0, -8050, 302)
    SetChrPos(0x2B, -1210, 0, -9240, 302)
    SetChrPos(0x16, 1080, 0, -9140, 302)
    SetChrPos(0x17, 1580, 0, -7990, 302)
    SetChrPos(0x1A, -3500, 0, -4500, 170)
    SetChrPos(0x1C, 2240, 0, 6890, 180)
    SetChrPos(0x1B, 1050, 0, 7050, 180)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0xD)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, 1950, 0, -4050, 240)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x5)
    SetChrPos(0x1E, 3400, 0, -5700, 275)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x1F, 0x5)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, 3600, 0, -3700, 240)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x20, 0xD)
    SetChrPos(0x20, 2850, 0, -2050, 220)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x21, 0xD)
    SetChrSubChip(0x21, 0x0)
    SetChrPos(0x21, 4850, 0, -4050, 240)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    SetChrPos(0x22, -4350, 0, -1800, 160)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x4)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x23, 0xB)
    SetChrSubChip(0x23, 0x0)
    SetChrPos(0x23, -4900, 0, -3800, 140)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x24, 0xC)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -2700, 0, -3200, 160)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x25, 0xC)
    SetChrSubChip(0x25, 0x0)
    SetChrPos(0x25, -6000, 0, -2600, 140)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    FadeToBright(4000, 0)
    OP_68(1350, 2000, -8800, 0)
    MoveCamera(358, 31, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(16000, 0)
    OP_68(-2710, 1320, -6940, 5000)
    MoveCamera(348, 30, 0, 5000)
    OP_6E(540, 5000)
    SetCameraDistance(15740, 5000)
    Sleep(5000)

    ChrTalk(
        0x2C,
        (
            "#3200330V#5P#0104FAll right, then. Allow me to fire the\x01",
            "starting signal.\x02\x03",
            "#3200331V#0100FOn my first shot, Team Downtown will start.\x02\x03",
            "#3200332VI will fire a second shot five seconds later, and\x01",
            "Team SSS will start.\x02\x03",
            "#3200333VAnd five seconds after that, Team Bracer\x01",
            "will be the last to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "#3200334V#5P#0204FI will handle the countdown.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#3200335V#5PWe will make sure to keep any spectators\x01",
            "out of your way.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x18,
        "#3200336V#5P#0404FAnd with that, the stage is finally set.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 10, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        "#3200337VBut, wait! The star has yet to arrive!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8118():

        label("loc_8118")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_8118")

    QueueWorkItem2(0x2A, 0, lambda_8118)
    Sleep(50)

    def lambda_812D():

        label("loc_812D")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_812D")

    QueueWorkItem2(0x2D, 0, lambda_812D)
    Sleep(50)

    def lambda_8142():

        label("loc_8142")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_8142")

    QueueWorkItem2(0x19, 0, lambda_8142)

    def lambda_8154():

        label("loc_8154")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_8154")

    QueueWorkItem2(0x16, 0, lambda_8154)
    Sleep(50)

    def lambda_8169():

        label("loc_8169")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_8169")

    QueueWorkItem2(0x17, 0, lambda_8169)
    Sleep(50)

    def lambda_817E():

        label("loc_817E")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_817E")

    QueueWorkItem2(0x1A, 0, lambda_817E)
    Sleep(50)

    def lambda_8193():

        label("loc_8193")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_8193")

    QueueWorkItem2(0x2C, 0, lambda_8193)
    Sleep(50)

    def lambda_81A8():

        label("loc_81A8")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_81A8")

    QueueWorkItem2(0x2B, 0, lambda_81A8)

    def lambda_81BA():

        label("loc_81BA")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_81BA")

    QueueWorkItem2(0x18, 0, lambda_81BA)
    Sleep(50)

    def lambda_81CF():

        label("loc_81CF")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_81CF")

    QueueWorkItem2(0x1D, 2, lambda_81CF)

    def lambda_81E1():

        label("loc_81E1")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_81E1")

    QueueWorkItem2(0x1E, 2, lambda_81E1)

    def lambda_81F3():

        label("loc_81F3")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_81F3")

    QueueWorkItem2(0x1F, 2, lambda_81F3)

    def lambda_8205():

        label("loc_8205")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_8205")

    QueueWorkItem2(0x20, 2, lambda_8205)

    def lambda_8217():

        label("loc_8217")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_8217")

    QueueWorkItem2(0x21, 2, lambda_8217)

    def lambda_8229():

        label("loc_8229")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_8229")

    QueueWorkItem2(0x22, 2, lambda_8229)

    def lambda_823B():

        label("loc_823B")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_823B")

    QueueWorkItem2(0x23, 2, lambda_823B)

    def lambda_824D():

        label("loc_824D")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_824D")

    QueueWorkItem2(0x24, 2, lambda_824D)

    def lambda_825F():

        label("loc_825F")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_825F")

    QueueWorkItem2(0x25, 2, lambda_825F)

    def lambda_8271():
        OP_95(0xFE, -1220, 0, -4550, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_8271)

    def lambda_828B():
        OP_95(0xFE, -50, 0, -4300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_828B)
    Sleep(500)
    Fade(500)
    OP_68(130, 620, -370, 0)
    MoveCamera(0, 38, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(12500, 0)
    OP_68(-1140, 1860, -7560, 5000)
    MoveCamera(0, 31, 0, 5000)
    OP_6E(620, 5000)
    SetCameraDistance(12500, 5000)
    Sleep(5000)

    ChrTalk(
        0x2A,
        "#3200338V#6P#0005FG-Grace?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#3200339V#12P#0905FIsn't she with the Crossbell Times?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#3200340V#5P#2109FHow ya doing, ladies and gentlemen?!\x02\x03",
            "#3200341V#2102FSome birdies told me about an exciting\x01",
            "event that's about to go down here.\x02\x03",
            "#3200342VI couldn't help but sink my teeth into this scoop!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200343V#6P#0011F'Sink your teeth into'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#3200344V#6P#1600F#NThe hell you schemin', lady?!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x1B,
        "#3200345V#5P#2101FThe answer, my dear delinquent...is this!\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x50, 0xC8)
    Sleep(100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0xF)
    OP_68(-1210, 2000, -6530, 500)
    OP_6E(580, 500)
    SetCameraDistance(10500, 500)
    OP_93(0x1B, 0xA, 0x2BC)
    OP_93(0x1B, 0xB4, 0x2BC)
    Sound(534, 0, 100, 0)
    Sound(882, 0, 100, 0)
    CancelBlur(100)
    Sound(896, 0, 100, 0)
    SetChrChipByIndex(0x1B, 0x3E)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x3F)
    SetChrSubChip(0x1C, 0x0)
    Sleep(1600)
    VolumeBGM(0x64, 0xC8)

    ChrTalk(
        0x1B,
        (
            "#3200346V#5P#2110FAn electrifying chase battle, covered live\x01",
            "from downtown!\x02\x03",
            "#3200347V#2109FI even brought my cameraman along,\x01",
            "so let's show some energy out there!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x1C, -6880, 1800, -14620, 45)
    SetChrPos(0x1B, -5740, 1800, -14060, 45)
    OP_68(-3900, 2000, -10810, 0)
    MoveCamera(87, 29, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(16000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x2A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-4080, 2000, -8980, 5000)
    MoveCamera(65, 29, 0, 5000)
    SetCameraDistance(16000, 5000)
    Sleep(1000)
    EndChrThread(0x2A, 0x0)
    EndChrThread(0x2C, 0x0)
    EndChrThread(0x2D, 0x0)
    EndChrThread(0x2B, 0x0)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x1A, 0x0)
    EndChrThread(0x1D, 0x2)
    EndChrThread(0x1E, 0x2)
    EndChrThread(0x1F, 0x2)
    EndChrThread(0x20, 0x2)
    EndChrThread(0x21, 0x2)
    EndChrThread(0x22, 0x2)
    EndChrThread(0x23, 0x2)
    EndChrThread(0x24, 0x2)
    EndChrThread(0x25, 0x2)

    ChrTalk(
        0x2D,
        (
            "#3200348V#5P#0211FI get the impression that she is trying to\x01",
            "turn this spectacle into a publicity stunt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#3200349V#11P#0809F#NAhaha. It's fine, isn't it?\x01",
            "This is way more interesting\x01",
            "than a brawl, I'd say! ♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2C, 500)
    Sleep(300)

    ChrTalk(
        0x2B,
        (
            "#3200350V#11P#0304FSheesh, this gal...\x01",
            "At least you're rarin' to go.\x02\x03",
            "#3200351V#0300FWell, 'bout time we get this show on the road.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_88F8():
        TurnDirection(0xFE, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_88F8)

    def lambda_8905():
        TurnDirection(0xFE, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_8905)
    Sleep(100)

    def lambda_8915():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_8915)

    def lambda_8922():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_8922)
    Sleep(100)

    def lambda_8932():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_8932)

    def lambda_893F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_893F)
    Sleep(100)

    def lambda_894F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_894F)

    def lambda_895C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_895C)

    def lambda_8969():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_8969)

    def lambda_8976():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_8976)

    def lambda_8983():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_8983)

    def lambda_8990():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_8990)

    def lambda_899D():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_899D)

    def lambda_89AA():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_89AA)

    def lambda_89B7():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_89B7)

    def lambda_89C4():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_89C4)

    def lambda_89D1():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_89D1)

    ChrTalk(
        0x18,
        (
            "#3200352V#0404F#5PYeah, I'd be inclined to agree.\x02\x03",
            "#3200353V#0402FAre you prepared, Wald?\x02",
        )
    )

    CloseMessageWindow()
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x19, 0x25)
    OP_A0(0x19, 2000, 0x0, 0xFB)

    ChrTalk(
        0x19,
        "#3200354V#1602F#11PHell yes. I'm ready any time.\x02",
    )

    CloseMessageWindow()
    OP_68(-5100, 1610, -9070, 3000)
    MoveCamera(72, 29, 0, 3000)
    OP_6E(540, 3000)
    SetCameraDistance(16000, 3000)
    SetChrChipByIndex(0x18, 0x2A)

    def lambda_8AB6():

        label("loc_8AB6")

        TurnDirection(0xFE, 0x18, 400)
        Yield()
        Jump("loc_8AB6")

    QueueWorkItem2(0x2D, 2, lambda_8AB6)

    def lambda_8AC8():
        OP_95(0xFE, -5130, 0, -8590, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8AC8)
    Sleep(100)
    SetChrChipByIndex(0x19, 0x27)
    OP_95(0x19, -5050, 0, -9830, 2000, 0x0)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_8B01():

        label("loc_8B01")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_8B01")

    QueueWorkItem2(0x19, 2, lambda_8B01)
    Sleep(1000)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_8B1A():

        label("loc_8B1A")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_8B1A")

    QueueWorkItem2(0x18, 2, lambda_8B1A)
    Sleep(1000)

    def lambda_8B2F():
        OP_96(0xFE, 0xFFFFEB60, 0x0, 0xFFFFE8D6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_8B2F)
    WaitChrThread(0x2C, 1)
    SetChrChipByIndex(0x2C, 0x40)
    SetChrSubChip(0x2C, 0x0)
    Sound(531, 0, 100, 0)
    SetChrFlags(0x2C, 0x2)
    OP_A0(0x2C, 1500, 0x6, 0x0)
    Fade(250)
    ClearChrFlags(0x2C, 0x2)
    SetChrChipByIndex(0x2C, 0x41)
    SetChrSubChip(0x2C, 0x0)
    Sound(804, 0, 100, 0)
    EndChrThread(0x2D, 0x2)
    OP_0D()

    ChrTalk(
        0x2D,
        (
            "#3200355V#0202F#5PAll right, then. I will begin\x01",
            "the countdown.\x02",
        )
    )

    CloseMessageWindow()
    OP_E5()
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6E(500, 6000)
    SetCameraDistance(13210, 6000)
    Sound(844, 0, 100, 0)

    ChrTalk(
        0x2D,
        "#3200356V#0203F#10ADrei...\x02",
    )

    Sleep(1000)
    Sound(844, 0, 100, 0)

    ChrTalk(
        0x2D,
        "#3200357V#0203F#10AZwei...\x02",
    )

    Sleep(1000)
    Sound(844, 0, 100, 0)

    ChrTalk(
        0x2D,
        "#3200358V#0203F#10AEins...\x02",
    )

    Sleep(1000)
    FadeToDark(0, 16777215, -1)
    FadeToBright(500, 16777215)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayBGM("ed7507", 0)
    EndChrThread(0x18, 0x2)
    EndChrThread(0x19, 0x2)
    SetChrChipByIndex(0x19, 0x27)
    SetChrChipByIndex(0x18, 0x2A)
    BeginChrThread(0x18, 3, 0, 26)
    BeginChrThread(0x19, 3, 0, 27)
    Fade(500)
    OP_67(0x1)
    OP_68(-6020, 2000, -9720, 0)
    MoveCamera(74, 9, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(27150, 0)
    Sound(845, 0, 100, 0)
    Sound(901, 0, 100, 0)

    NpcTalk(
        0x2D,
        "Tio",
        "#3200359V#0207F#5A#NNull!\x02",
    )

    Sleep(1000)
    OP_5A()
    SetMessageWindowPos(14, -10, -1, 3)

    AnonymousTalk(
        0x1B,
        "#3200360V#4A#30W#2110FThe heart throbbing race has begun, everyone!\x02",
    )

    Sleep(1400)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_93(0x1B, 0x12C, 0x0)
    OP_93(0x1C, 0x12C, 0x0)
    SetChrPos(0x18, -3140, 0, -8130, 302)
    SetChrPos(0x19, -3080, 0, -9580, 302)
    SetChrChipByIndex(0x19, 0x27)
    SetChrChipByIndex(0x18, 0x2A)
    BeginChrThread(0x18, 3, 0, 26)
    BeginChrThread(0x19, 3, 0, 27)
    OP_67(0x1)
    OP_68(-17450, 2000, -12010, 2500)
    MoveCamera(296, 19, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(27150, 0)

    AnonymousTalk(
        0x1B,
        (
            "#3200361V#6A#30W#2110FThe first team, consisting of Wazy and Wald,\x01",
            "is off to a sensational start!\x02",
        )
    )

    Sleep(3400)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        (
            "#3200362V#6A#30W#2110FIncredible! They've already tagged the first\x01",
            "checkpoint and are fast approaching the second!\x02",
        )
    )

    Sleep(3600)
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    SetChrChipByIndex(0x2C, 0x38)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x2)
    Sound(845, 0, 100, 0)
    Fade(500)
    BeginChrThread(0x2A, 3, 0, 28)
    BeginChrThread(0x2B, 3, 0, 29)
    OP_67(0x1)
    OP_68(-4540, 2000, -9070, 0)
    MoveCamera(83, 10, -1, 0)
    OP_6E(320, 0)
    SetCameraDistance(27150, 0)
    SetMessageWindowPos(14, -10, -1, 3)

    AnonymousTalk(
        0x1B,
        (
            "#3200363V#6A#30W#2100FLook here! Lloyd and Randy of Team SSS\x01",
            "have charged from the starting line!\x02",
        )
    )

    Sleep(3200)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x2A, -980, 0, -8050, 302)
    SetChrPos(0x2B, -1210, 0, -9240, 302)
    BeginChrThread(0x2A, 3, 0, 28)
    BeginChrThread(0x2B, 3, 0, 29)
    OP_6B(0xFF)
    OP_67(0x1)
    OP_68(-20730, 2000, -11460, 0)
    MoveCamera(59, 32, 0, 2500)
    OP_6E(340, 0)
    SetCameraDistance(25650, 0)

    AnonymousTalk(
        0x1B,
        (
            "#3200364V#6A#30W#2100FRandy's time in the CGF must have made\x01",
            "him nimble! Lloyd's no slowpoke, either!\x02",
        )
    )

    Sleep(4000)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        "#3200365V#8A#30W#2100FThey're now passing the first checkpoint!\x02",
    )

    Sleep(1800)
    OP_57(0x0)
    OP_5A()
    Sound(845, 0, 100, 0)
    Fade(500)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrChipByIndex(0x16, 0x27)
    BeginChrThread(0x17, 3, 0, 30)
    BeginChrThread(0x16, 3, 0, 31)
    OP_6B(0xFF)
    OP_67(0x1)
    OP_68(-4720, 2000, -6290, 0)
    MoveCamera(211, 26, -1, 0)
    OP_6E(340, 0)
    SetCameraDistance(25650, 0)
    SetMessageWindowPos(290, 145, -1, -1)

    AnonymousTalk(
        0x1B,
        (
            "#3200366V#6A#30W#2104FThe final team, made up of Estelle and Joshua\x01",
            "Bright, has exploded from the start!\x02",
        )
    )

    Sleep(3200)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x16, 1080, 0, -9140, 302)
    SetChrPos(0x17, 1580, 0, -7990, 302)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrChipByIndex(0x16, 0x27)
    BeginChrThread(0x17, 3, 0, 30)
    BeginChrThread(0x16, 3, 0, 31)
    OP_67(0x1)
    OP_68(-10660, 2000, -12350, 0)
    MoveCamera(53, 36, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(12970, 0)
    OP_68(-10660, 2000, -12350, 0)
    MoveCamera(316, 36, 0, 3500)
    OP_6E(620, 0)
    SetCameraDistance(12970, 0)

    AnonymousTalk(
        0x1B,
        (
            "#3200367V#6A#30W#2100FThese two are a bona fide tag team!\x01",
            "True top-class bracers!\x02",
        )
    )

    Sleep(3400)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        (
            "#3200368V#6A#30W#2100FThey're now completing the first checkpoint,\x01",
            "while hot on the tracks of the other teams!\x02",
        )
    )

    Sleep(3400)
    OP_57(0x0)
    OP_5A()
    Fade(1500)
    OP_6B(0x2A)
    BeginChrThread(0x2A, 3, 0, 34)
    BeginChrThread(0x2B, 3, 0, 35)
    OP_67(0x1)
    OP_68(-9470, -3280, -24010, 0)
    MoveCamera(20, 18, 0, 0)
    OP_6E(880, 0)
    SetCameraDistance(11000, 0)
    MoveCamera(65, 18, 0, 4000)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_9340():

        label("loc_9340")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9340")

    QueueWorkItem2(0x18, 2, lambda_9340)
    SetChrPos(0x18, 33790, -6490, -39680, 270)
    SetChrPos(0x19, 32409, -6490, -38140, 270)
    SetChrPos(0x16, 1080, 0, -9140, 272)
    SetChrPos(0x17, 1580, 0, -7990, 267)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x17, 0x3)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    OP_93(0x1D, 0xB4, 0x0)
    OP_93(0x1E, 0xB4, 0x0)
    OP_93(0x1F, 0xB4, 0x0)
    OP_93(0x20, 0xB4, 0x0)
    OP_93(0x21, 0xB4, 0x0)
    SetChrPos(0x2E, 32409, -4800, -38140, 180)
    SetMapObjFlags(0xF, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    OP_78(0xF, 0x2E)
    OP_D3(0x2E, 0x0, 0x15F90, 0x0, 0x0)
    OP_49()
    OP_74(0xF, 0xF)
    OP_70(0xF, 0xA)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x1)
    Sleep(3500)
    OP_63(0x2A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6B(0xFF)
    Fade(1000)
    OP_68(33490, -4540, -38270, 1000)
    MoveCamera(70, 18, 0, 1000)
    OP_6E(360, 1000)
    SetCameraDistance(22500, 1000)
    SetMessageWindowPos(14, -10, -1, 3)

    AnonymousTalk(
        0x1B,
        "#3200369V#7A#30W#2105FOh, what's this?! A bold move by Wald Wales!\x02",
    )

    Sleep(3200)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        "#3200370V#8A#30W#2101FHow will Team SSS react?!\x02",
    )

    Sleep(1800)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x2A, 13000, -6490, -37180, 78)

    def lambda_9574():
        OP_95(0x2A, 23760, -6490, -37430, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 3, lambda_9574)
    SetChrPos(0x2B, 12600, -6490, -39220, 315)

    def lambda_959F():
        OP_95(0x2B, 23700, -6490, -39330, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 3, lambda_959F)
    OP_68(21660, -5040, -38440, 0)
    MoveCamera(80, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    OP_68(29470, -5040, -38330, 2500)
    MoveCamera(83, 10, 0, 2500)
    OP_6E(420, 2500)
    SetCameraDistance(21000, 2500)

    ChrTalk(
        0x2A,
        "#3200371V#5P#8A#30W#0001F(Crap!)\x02",
    )

    Sleep(1000)

    ChrTalk(
        0x2B,
        "#3200372V#11P#12A#30W#0301F(It's your call!)\x02",
    )

    Sleep(1800)
    OP_E6()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Try to dodge]\x01",       # 0
            "[Break through]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_96D0"),
        (1, "loc_98D1"),
        (SWITCH_DEFAULT, "loc_9BD7"),
    )


    label("loc_96D0")


    ChrTalk(
        0x19,
        "#3200373V#6A#30W#1607F#4S#5P#NHaaahhh!!\x02",
    )

    BeginChrThread(0x2E, 3, 0, 39)
    SetChrChipByIndex(0x19, 0x26)
    BeginChrThread(0x19, 3, 0, 67)
    Sleep(400)

    def lambda_9714():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_9714)

    def lambda_9721():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_9721)

    def lambda_972E():
        OP_9D(0xFE, 0x6428, 0xFFFFE69C, 0xFFFF728E, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_972E)

    def lambda_974B():
        OP_9D(0xFE, 0x6554, 0xFFFFE69C, 0xFFFF60DC, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_974B)
    Sound(814, 0, 100, 0)
    Sleep(600)

    ChrTalk(
        0x18,
        "#3200374V#9A#30W#0402F#5PCiao! We're going on ahead!\x02",
    )

    EndChrThread(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x2A)
    OP_9D(0x18, 0x76CA, 0xFFFFE69C, 0xFFFF6AB4, 0x320, 0x1770)
    Sound(814, 0, 100, 0)
    BeginChrThread(0x19, 3, 0, 36)
    OP_95(0x18, 22720, -6500, -37590, 7000, 0x0)
    SetMessageWindowPos(14, -10, -1, 3)

    AnonymousTalk(
        0x1B,
        (
            "#3200375V#4A#30W#2103FLloyd and Randy barely managed to\x01",
            "avoid the barrel!\x02",
        )
    )

    BeginChrThread(0x2A, 3, 0, 37)
    BeginChrThread(0x2B, 3, 0, 38)
    OP_95(0x18, 21220, -2500, -25410, 7000, 0x0)
    Sleep(1400)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        (
            "#3200376V#4A#30W#2101FBut, their formation has been broken!\x01",
            "Will their time suffer as a result?!\x02",
        )
    )

    Sleep(2000)
    OP_57(0x0)
    OP_5A()
    Jump("loc_9BD7")

    label("loc_98D1")

    OP_2C(0x44, 0x1)
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x19,
        "#3200377V#6A#30W#1607F#4S#5P#NHaaahhh!!\x02",
    )

    BeginChrThread(0x2E, 3, 0, 39)
    SetChrChipByIndex(0x19, 0x26)
    BeginChrThread(0x19, 3, 0, 67)
    Sleep(300)
    SetChrChip(0x0, 0x2A, 0x64, 0x1F4)
    SetChrChip(0x0, 0x2B, 0x64, 0x1F4)

    def lambda_9938():
        OP_9D(0xFE, 0x6978, 0xFFFFE69C, 0xFFFF6C58, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9938)

    def lambda_9955():
        OP_9D(0xFE, 0x6978, 0xFFFFE69C, 0xFFFF66E0, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_9955)
    Sound(250, 0, 100, 0)
    Sleep(100)
    EndChrThread(0x18, 0x2)

    def lambda_997F():
        OP_9D(0xFE, 0x76CA, 0xFFFFE69C, 0xFFFF6AB4, 0x320, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_997F)
    Sound(814, 0, 100, 0)
    OP_68(31000, -5040, -38330, 1500)
    MoveCamera(59, 6, 0, 1500)
    OP_6E(420, 1500)
    SetCameraDistance(21000, 1500)
    Sleep(600)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_99D7():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_99D7)
    Sleep(600)
    SetChrChipByIndex(0x18, 0x29)

    def lambda_99EB():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_99EB)
    Sleep(200)
    SetChrChip(0x0, 0x18, 0x64, 0x1F4)

    def lambda_9A03():
        OP_9D(0xFE, 0x6860, 0xFFFFE69C, 0xFFFF6D2A, 0x64, 0x2BC)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9A03)
    Sound(250, 0, 100, 0)
    Sound(541, 0, 100, 0)

    def lambda_9A2C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_9A2C)

    def lambda_9A39():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_9A39)

    def lambda_9A46():
        OP_9D(0xFE, 0x7530, 0xFFFFE69C, 0xFFFF7040, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9A46)

    def lambda_9A63():
        OP_9D(0xFE, 0x7530, 0xFFFFE69C, 0xFFFF62F8, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_9A63)
    Sound(814, 0, 100, 0)
    Sleep(200)
    TurnDirection(0x18, 0x2A, 500)
    SetChrChip(0x1, 0x18, 0x0, 0x0)
    SetChrChip(0x1, 0x2A, 0x0, 0x0)
    SetChrChip(0x1, 0x2B, 0x0, 0x0)
    BeginChrThread(0x19, 3, 0, 36)

    ChrTalk(
        0x18,
        "#3200378V#5A#30W#0402F#5PHaha. Well done!\x02",
    )

    SetChrChipByIndex(0x18, 0x2A)
    Sleep(700)
    SetChrChip(0x1, 0x2A, 0x0, 0x0)
    SetChrChip(0x1, 0x2B, 0x0, 0x0)
    BeginChrThread(0x2A, 3, 0, 37)
    BeginChrThread(0x2B, 3, 0, 38)
    OP_95(0x18, 21220, -2500, -25410, 7000, 0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, -10, -1, 3)

    AnonymousTalk(
        0x1B,
        (
            "#3200379V#8A#30W#2104FLloyd and Randy managed to evade Team\x01",
            "Downtown's assault! Marvelous!\x02",
        )
    )

    Sleep(4000)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        (
            "#3200380V#8A#30W#2100FThey've fended off Wazy! To the second\x01",
            "checkpoint!\x02",
        )
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    Jump("loc_9BD7")

    label("loc_9BD7")

    Fade(500)
    BeginChrThread(0x2A, 3, 0, 40)
    BeginChrThread(0x2B, 3, 0, 41)
    SetChrPos(0x19, 43020, -2500, -21880, 135)
    SetChrPos(0x18, 42830, -2500, -23790, 45)
    OP_6B(0x2A)
    OP_68(21840, -4500, -37170, 0)
    MoveCamera(1, 20, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(14500, 0)
    MoveCamera(67, 12, 0, 5000)
    Sleep(1000)
    BeginChrThread(0x19, 3, 0, 42)
    BeginChrThread(0x18, 3, 0, 43)
    Sleep(1500)
    Sleep(500)

    ChrTalk(
        0x2B,
        "#3200381V#5P#6A#30W#0301F(What's the plan?!)\x02",
    )

    Sleep(800)

    ChrTalk(
        0x2A,
        "#3200382V#5P#8A#30W#0007F(Let's counterattack!)\x02",
    )

    Sleep(1200)
    EndChrThread(0x2B, 0x3)
    EndChrThread(0x2A, 0x3)
    OP_6B(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Fight separately]\x01",      # 0
            "[Combo craft]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9D2C"),
        (1, "loc_9FA7"),
        (SWITCH_DEFAULT, "loc_A23D"),
    )


    label("loc_9D2C")

    OP_68(42290, -500, -23200, 700)

    def lambda_9D42():
        OP_95(0xFE, 42100, -2500, -22410, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9D42)

    def lambda_9D5C():
        OP_9D(0xFE, 0xA154, 0xFFFFFE0C, 0xFFFFA20E, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_9D5C)
    Sound(854, 0, 100, 0)
    Sleep(700)
    ClearScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200001, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    Call(0, 65)
    LoadEffect(0x3, "event\\ev301_00.eff")
    EventBegin(0x0)
    SetChrChipByIndex(0x2A, 0x31)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_9DF2():

        label("loc_9DF2")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9DF2")

    QueueWorkItem2(0x2A, 2, lambda_9DF2)

    def lambda_9E04():

        label("loc_9E04")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9E04")

    QueueWorkItem2(0x2B, 2, lambda_9E04)
    SetChrPos(0x2A, 40970, -2500, -22390, 21)
    SetChrPos(0x2B, 41410, -2500, -24040, 135)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    SetChrChipByIndex(0x18, 0x28)
    SetChrChipByIndex(0x19, 0x37)

    def lambda_9E62():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_9E62)
    BeginChrThread(0x19, 3, 0, 68)
    Sound(514, 0, 100, 0)
    SetChrPos(0x18, 42120, -2500, -20350, 180)
    SetChrPos(0x19, 43290, -2500, -24680, 331)
    OP_6B(0x2A)
    OP_68(41050, -500, -22430, 0)
    MoveCamera(44, 30, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(14500, 0)
    OP_E5()
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x19,
        "#3200383V#11P#8A#30W#1607FGah?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#3200384V#5P#12A#30W#0404FHaha. Not bad.\x02",
    )

    Sleep(2000)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x2A,
        "#3200385V#5P#8A#30W#0000FSee you later!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x2A, 3, 0, 44)

    ChrTalk(
        0x2B,
        "#3200386V#5P#8A#30W#0309FTry not to hate us, fools!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x2B, 0x36)
    BeginChrThread(0x2B, 3, 0, 45)
    Jump("loc_A23D")

    label("loc_9FA7")

    OP_2C(0x44, 0x1)
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(42290, -500, -23200, 700)

    def lambda_9FD0():
        OP_95(0xFE, 42100, -2500, -22410, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9FD0)

    def lambda_9FEA():
        OP_9D(0xFE, 0xA154, 0xFFFFFE0C, 0xFFFFA20E, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_9FEA)
    Sound(854, 0, 100, 0)
    Sleep(700)
    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200001, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Call(0, 65)
    LoadEffect(0x3, "event\\ev301_00.eff")
    SetChrChipByIndex(0x2A, 0x31)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_A080():

        label("loc_A080")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_A080")

    QueueWorkItem2(0x2A, 2, lambda_A080)

    def lambda_A092():

        label("loc_A092")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_A092")

    QueueWorkItem2(0x2B, 2, lambda_A092)
    SetChrPos(0x2A, 40970, -2500, -22390, 21)
    SetChrPos(0x2B, 41410, -2500, -24040, 135)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    SetChrChipByIndex(0x18, 0x38)
    SetChrChipByIndex(0x19, 0x37)
    BeginChrThread(0x18, 3, 0, 68)
    BeginChrThread(0x19, 3, 0, 68)
    SetChrPos(0x18, 42120, -2500, -20350, 180)
    SetChrPos(0x19, 43290, -2500, -24680, 331)
    OP_6B(0x2A)
    OP_68(41050, -500, -22430, 0)
    MoveCamera(44, 30, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(14500, 0)
    OP_E5()
    Sound(514, 0, 100, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x19,
        "#3200387V#8A#30W#1605F#11PThe hell?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#3200388V#8A#30W#0410F#5PYou got us good...\x02",
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x2A,
        "#3200389V#8A#30W#0001F#5PSorry about that!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x2A, 3, 0, 44)

    ChrTalk(
        0x2B,
        "#3200390V#8A#30W#0300F#5PWe'll see ya up ahead! Or not!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x2B, 0x36)
    BeginChrThread(0x2B, 3, 0, 45)
    Jump("loc_A23D")

    label("loc_A23D")

    Sleep(1000)
    BeginChrThread(0x16, 3, 0, 46)
    BeginChrThread(0x17, 3, 0, 47)
    Sleep(2000)
    OP_57(0x0)
    OP_5A()
    Sleep(3000)
    Fade(1000)
    OP_6B(0xFF)
    OP_67(0x1)
    OP_68(9060, 1990, -12040, 0)
    MoveCamera(44, 31, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22150, 0)
    OP_67(0x0)
    OP_6B(0x2A)
    SetMessageWindowPos(14, -10, -1, 3)

    AnonymousTalk(
        0x1B,
        "#3200391V#18A#30W#2100FSecond lap here we go!\x02",
    )

    Sleep(1000)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        (
            "#3200392V#20A#50W#2100FLloyd and Randy have taken\x01",
            "a decisive lead and...\x02",
        )
    )

    Sleep(2400)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        "#3200393V#6A#20W#2109F...they've passed the first checkpoint!\x02",
    )

    SetChrPos(0x16, 1080, 0, -9140, 272)
    SetChrPos(0x17, 1580, 0, -7990, 267)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrChipByIndex(0x16, 0x27)
    BeginChrThread(0x17, 3, 0, 32)
    BeginChrThread(0x16, 3, 0, 33)
    Sleep(2200)
    OP_57(0x0)
    OP_5A()
    OP_6B(0xFF)
    OP_67(0x1)

    AnonymousTalk(
        0x1B,
        (
            "#3200394V#15A#20W#2105FHold on, folks! What's this?!\x01",
            "Estelle and Joshua are approaching\x01",
            "Team SSS at an incredible speed!\x02",
        )
    )

    Sleep(4000)
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-4680, -1840, -26700, 0)
    MoveCamera(51, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    BeginChrThread(0x2A, 3, 0, 48)
    BeginChrThread(0x2B, 3, 0, 49)
    OP_6B(0x2A)
    MoveCamera(359, 18, 0, 5000)
    Sleep(1000)

    ChrTalk(
        0x2A,
        "#3200395V#6A#30W#0008F#5PTch!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#3200396V#8A#30W#0301F#5PDamn it! They managed to catch up!\x02",
    )

    CloseMessageWindow()
    Sleep(2300)
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    EndChrThread(0x2A, 0x3)
    OP_95(0x2A, 35200, -6490, -38160, 7000, 0x0)

    ChrTalk(
        0x2B,
        "#3200397V#6A#30W#0307F#5PHey, Lloyd!\x02",
    )

    OP_71(0xA, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    SetChrChipByIndex(0x2A, 0x32)
    OP_A1(0x2A, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    SetChrChipByIndex(0x2A, 0x31)

    def lambda_A56A():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_A56A)
    Sleep(300)

    ChrTalk(
        0x2A,
        "#3200398V#6A#30W#0005F#5PHuh?\x02",
    )

    CloseMessageWindow()
    OP_6B(0xFF)
    OP_68(36410, -4540, -38600, 5000)
    MoveCamera(339, 31, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(22500, 5000)
    PlayEffect(0x3, 0xFF, 0xFF, 0x40, 34000, -7000, -36000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(898, 0, 100, 0)
    OP_71(0x8, 0x0, 0x14, 0x0, 0x8)
    FadeToDark(300, 16777215, 100)
    Sleep(500)

    ChrTalk(
        0x2A,
        "#3200399V#8A#30W#0007F#5PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#3200400V#8A#30W#0310FQuicklime?!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, -10, -1, 3)

    AnonymousTalk(
        0x1B,
        (
            "#3200401V#8A#30W#2105FWhat a shocking development!\x01",
            "What's with this white smoke?!\x02",
        )
    )

    Sleep(2800)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        (
            "#3200402V#8A#30W#2110FIs this a trap laid by\x01",
            "Team Bracer?!\x02",
        )
    )

    Sleep(3200)
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x16, 3, 0, 50)
    BeginChrThread(0x17, 3, 0, 51)

    ChrTalk(
        0x16,
        "#3200403V#6A#30W#0802F#5P#NSorry about that, losers!\x02",
    )

    CloseMessageWindow()
    Sleep(1500)

    ChrTalk(
        0x17,
        "#3200404V#6A#30W#0900F#5PTry not to breathe in too much!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200405V#9A#30W#0013F#5PCrap...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#3200406V#9A#30W#0307FC'mon! We gotta go after 'em!\x02",
    )

    CloseMessageWindow()
    FadeToBright(1300, 16777215)
    SetChrChipByIndex(0x16, 0x2B)

    def lambda_A80F():

        label("loc_A80F")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_A80F")

    QueueWorkItem2(0x16, 2, lambda_A80F)
    SetChrChipByIndex(0x17, 0x2E)

    def lambda_A825():

        label("loc_A825")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_A825")

    QueueWorkItem2(0x17, 2, lambda_A825)
    SetChrPos(0x17, 37300, -2500, -22500, 270)
    SetChrPos(0x16, 37800, -2500, -24000, 270)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrPos(0x19, 28020, -2500, -23450, 308)
    SetChrPos(0x18, 28260, -2500, -24990, 128)
    BeginChrThread(0x2A, 3, 0, 52)
    BeginChrThread(0x2B, 3, 0, 53)
    Sleep(1500)
    OP_68(23210, -4540, -36350, 0)
    MoveCamera(48, 16, 0, 0)
    OP_6E(960, 0)
    SetCameraDistance(10000, 0)
    Sleep(2400)
    OP_68(22810, -500, -24060, 0)
    MoveCamera(120, 35, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(26000, 0)
    Sleep(1500)
    OP_68(34300, 50, -22710, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(840, 0)
    SetCameraDistance(11000, 0)
    Sleep(50)
    OP_E6()

    ChrTalk(
        0x16,
        "#3200407V#0800F#11PHere they come!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#3200408V#0901F#11PWe're breaking through!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200409V#0013F#5P(Think, Lloyd!)\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x16, 0x2D)
    SetChrChipByIndex(0x17, 0x30)
    SetChrChipByIndex(0x2B, 0x36)
    SetChrChipByIndex(0x2A, 0x33)

    def lambda_A9C1():
        OP_99(0xFE, 0x2B, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_A9C1)

    def lambda_A9D5():
        OP_99(0xFE, 0x2A, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A9D5)

    def lambda_A9E9():
        OP_99(0xFE, 0x16, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_A9E9)

    def lambda_A9FD():
        OP_99(0xFE, 0x17, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A9FD)
    Sleep(150)
    EndChrThread(0x2B, 0x1)
    EndChrThread(0x2A, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x2B, 0x2)
    EndChrThread(0x2A, 0x2)
    EndChrThread(0x16, 0x2)
    EndChrThread(0x17, 0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Fight separately]\x01",      # 0
            "[Combo craft]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    def lambda_AA79():
        OP_99(0xFE, 0x2B, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_AA79)

    def lambda_AA8D():
        OP_99(0xFE, 0x2A, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_AA8D)

    def lambda_AAA1():
        OP_99(0xFE, 0x16, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_AAA1)

    def lambda_AAB5():
        OP_99(0xFE, 0x17, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_AAB5)
    Sleep(150)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AADD"),
        (1, "loc_B0D4"),
        (SWITCH_DEFAULT, "loc_B5BD"),
    )


    label("loc_AADD")

    OP_2C(0x44, 0x1)
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x2B, 0x1)
    EndChrThread(0x2A, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    ClearScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200000, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000600, 0x30000700, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Call(0, 65)
    LoadEffect(0x0, "battle\\cr003300.eff")
    LoadEffect(0x1, "event\\ev302_01.eff")
    LoadEffect(0x2, "event\\ev302_00.eff")
    OP_68(35610, -500, -24250, 0)
    MoveCamera(38, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x2A, 0x31)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_ABCE():

        label("loc_ABCE")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_ABCE")

    QueueWorkItem2(0x2A, 2, lambda_ABCE)

    def lambda_ABE0():

        label("loc_ABE0")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_ABE0")

    QueueWorkItem2(0x2B, 2, lambda_ABE0)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrChipByIndex(0x16, 0x2B)

    def lambda_ABFA():

        label("loc_ABFA")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_ABFA")

    QueueWorkItem2(0x17, 2, lambda_ABFA)

    def lambda_AC0C():

        label("loc_AC0C")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_AC0C")

    QueueWorkItem2(0x16, 2, lambda_AC0C)
    SetChrPos(0x17, 34690, -2500, -22950, 89)
    SetChrPos(0x16, 33910, -2500, -24380, 89)
    SetChrPos(0x2A, 36880, -2500, -23410, 270)
    SetChrPos(0x2B, 37460, -2500, -24500, 270)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x16,
        "#3200410V#1P#30W#0809FHeeey, nice try!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#3200411V#5P#30W#0902FBut we'll still be going on ahead!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x16, 0x2D)

    def lambda_ACFC():
        OP_95(0xFE, 17660, -2500, -22500, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_ACFC)
    Sleep(300)
    SetChrChipByIndex(0x17, 0x30)

    def lambda_AD1D():
        OP_95(0xFE, 17660, -2500, -22500, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_AD1D)

    ChrTalk(
        0x2A,
        "#3200412V#30W#0013F#11PGah!\x02",
    )

    CloseMessageWindow()
    OP_93(0x2B, 0x5A, 0x1F4)
    OP_68(36790, -500, -24050, 1000)

    ChrTalk(
        0x2B,
        (
            "#3200413V#30W#0307F#5POnce we get to the next checkpoint,\x01",
            "we gotta make sure to--\x02",
        )
    )

    Sleep(500)
    OP_93(0x2A, 0x5A, 0x1F4)
    CloseMessageWindow()
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    Sound(1431, 255, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x18,
        "#3200414V#8A#30W#0402F#2PDon't get distracted now, boys!\x02",
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_93(0x2B, 0x10E, 0x320)
    Sleep(500)
    EndChrThread(0x2B, 0x2)
    MoveCamera(320, 27, 0, 2000)
    OP_93(0x2A, 0x10E, 0x320)
    OP_63(0x2A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    EndChrThread(0x2A, 0x2)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrChipByIndex(0x19, 0x27)

    def lambda_AE88():
        OP_99(0xFE, 0x2B, 0xFFFFFC18, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_AE88)

    def lambda_AE9C():
        OP_99(0xFE, 0x2A, 0xFFFFFC18, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_AE9C)
    Sound(1791, 255, 100, 2)
    Sleep(1050)
    OP_49()
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    Sound(834, 0, 100, 0)
    OP_68(38120, -500, -23640, 500)
    MoveCamera(358, 27, 0, 500)
    OP_6E(400, 500)
    SetCameraDistance(24500, 500)
    OP_49()
    Sleep(30)
    SetChrChipByIndex(0x2A, 0x3B)
    BeginChrThread(0x2A, 3, 0, 68)
    Sound(514, 0, 100, 0)

    def lambda_AF13():
        OP_9D(0xFE, 0x9CC2, 0xFFFFF63C, 0xFFFFA9D4, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_AF13)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_AF34():

        label("loc_AF34")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_AF34")

    QueueWorkItem2(0x18, 2, lambda_AF34)
    SetChrChipByIndex(0x2B, 0x3C)
    BeginChrThread(0x2B, 3, 0, 68)

    def lambda_AF50():
        OP_9D(0xFE, 0x9D4E, 0xFFFFF63C, 0xFFFFA04C, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_AF50)

    ChrTalk(
        0x2A,
        "#3200416V#11P#6A#30W#0010FGah...\x02",
    )


    ChrTalk(
        0x2B,
        "#12P#6A#30W#0310FDamn it...\x02",
    )

    Sleep(200)
    BeginChrThread(0x19, 3, 0, 54)
    Sleep(200)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_AFC2():

        label("loc_AFC2")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_AFC2")

    QueueWorkItem2(0x18, 2, lambda_AFC2)
    BeginChrThread(0x18, 3, 0, 55)
    Sleep(1000)
    SetMessageWindowPos(14, -10, -1, 3)

    AnonymousTalk(
        0x1B,
        (
            "#3200418V#16A#30W#2105FPhenomenal! Wazy and Wald\x01",
            "have launched a surprise attack\x01",
            "on Team SSS!\x02",
        )
    )

    Sleep(5200)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        (
            "#3200419V#16A#30W#2110FThey've now managed to pass the third\x01",
            "checkpoint, putting them in hot pursuit\x01",
            "of Estelle and Joshua!\x02",
        )
    )

    Sleep(3200)
    OP_57(0x0)
    OP_5A()
    Jump("loc_B5BD")

    label("loc_B0D4")

    EndChrThread(0x2B, 0x1)
    EndChrThread(0x2A, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200000, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000600, 0x30000700, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Call(0, 65)
    LoadEffect(0x0, "battle\\cr003300.eff")
    LoadEffect(0x1, "event\\ev302_01.eff")
    LoadEffect(0x2, "event\\ev302_00.eff")
    OP_68(35610, -500, -24250, 0)
    MoveCamera(38, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x2A, 0x3B)
    SetChrChipByIndex(0x2B, 0x3C)
    BeginChrThread(0x2A, 3, 0, 68)
    BeginChrThread(0x2B, 3, 0, 68)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrChipByIndex(0x19, 0x27)
    SetChrPos(0x17, 34690, -2500, -22950, 89)
    SetChrPos(0x16, 33910, -2500, -24380, 89)
    SetChrPos(0x2A, 40130, -2500, -22060, 270)
    SetChrPos(0x2B, 40270, -2500, -24500, 270)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    Sound(514, 0, 100, 0)
    OP_68(36790, -500, -24050, 1500)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x16,
        "#3200420V#0800F#1PSee ya later, suckers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#3200421V#0901F#5PLet's keep up this pace, Estelle!\x02",
    )

    CloseMessageWindow()

    def lambda_B2B7():
        OP_95(0xFE, 17660, -2500, -22500, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_B2B7)
    Sleep(300)

    def lambda_B2D4():
        OP_95(0xFE, 17660, -2500, -22500, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B2D4)

    ChrTalk(
        0x2A,
        "#3200422V#0010F#11PCrap...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#3200423V#0310F#11PDamn. They got us good...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    Sound(1431, 255, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x18,
        "#3200424V#0409F#2PThings are starting to heat up nicely!\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_B3D1():
        OP_99(0xFE, 0x2B, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B3D1)
    OP_68(38120, -500, -23640, 3500)
    MoveCamera(358, 27, 0, 3500)
    OP_6E(400, 3500)
    SetCameraDistance(24500, 3500)
    ClearChrFlags(0x2A, 0x1000)
    ClearChrFlags(0x2B, 0x1000)
    OP_99(0x19, 0x2A, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_B42F():

        label("loc_B42F")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_B42F")

    QueueWorkItem2(0x19, 2, lambda_B42F)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_B445():

        label("loc_B445")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_B445")

    QueueWorkItem2(0x18, 2, lambda_B445)

    ChrTalk(
        0x19,
        "#3200425V#5P#1602FHaha... You morons are lookin' a bit clumsy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#3200426V#5P#0402FWell, we managed to get our revenge!\x02",
    )

    CloseMessageWindow()
    Sound(1809, 255, 100, 1)
    BeginChrThread(0x19, 3, 0, 54)
    Sleep(200)
    BeginChrThread(0x18, 3, 0, 55)
    Sleep(500)
    SetMessageWindowPos(14, -10, -1, 3)

    AnonymousTalk(
        0x1B,
        (
            "#3200427V#8A#30W#2100FWazy and Wald have overtaken the\x01",
            "crestfallen Team SSS and have\x01",
            "made it to the third checkpoint!\x02",
        )
    )

    Sleep(5200)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        "#3200428V#8A#30W#2100FThey're now gunning for Team Bracer!\x02",
    )

    Sleep(2400)
    OP_57(0x0)
    OP_5A()
    Jump("loc_B5BD")

    label("loc_B5BD")

    Sound(804, 0, 100, 0)
    OP_A1(0x2A, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    SetChrChipByIndex(0x2A, 0x31)

    def lambda_B5D5():

        label("loc_B5D5")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_B5D5")

    QueueWorkItem2(0x2A, 2, lambda_B5D5)
    Sound(804, 0, 100, 0)
    OP_A1(0x2B, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_B5FA():

        label("loc_B5FA")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_B5FA")

    QueueWorkItem2(0x2B, 2, lambda_B5FA)

    ChrTalk(
        0x2A,
        (
            "#3200429V#0010F#11PNo...\x02\x03",
            "#3200430V#0008FDamn it, at this rate...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B653():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x2B, 3, lambda_B653)
    Sleep(300)
    Sound(1370, 255, 100, 0)
    Sleep(150)
    EndChrThread(0x2B, 0x2)
    Sleep(1500)
    Sleep(100)

    ChrTalk(
        0x2B,
        "#3200431V#0312F#11P#60W#12AHahahahahaha!\x02",
    )

    Sleep(1000)

    def lambda_B6B2():
        TurnDirection(0xFE, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_B6B2)
    Sleep(2000)
    Sound(1310, 255, 100, 0)
    SetChrChipByIndex(0x2B, 0x3D)
    OP_A1(0x2B, 0x7D0, 0x4, 0x0, 0x0, 0x0, 0x0)

    def lambda_B6D6():
        OP_A6(0xFE, 0x64, 0x0, 0x320, 0x5DC)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_B6D6)
    CloseMessageWindow()
    PlayEffect(0x0, 0xFF, 0x2B, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(197, 0, 100, 0)
    Sound(183, 0, 100, 0)
    OP_68(40200, -500, -24500, 1500)
    MoveCamera(45, 27, 0, 1500)
    OP_6E(240, 1500)
    SetCameraDistance(24500, 1500)
    Sleep(1500)
    OP_6E(350, 0)
    PlayEffect(0x1, 0xFF, 0x2B, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(256, 0, 100, 0)
    Sound(325, 0, 100, 0)
    OP_A1(0x2B, 0x7D0, 0x1, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sleep(800)

    ChrTalk(
        0x2A,
        "#3200432V#0011F#5PR-Randy?\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_B7F4():

        label("loc_B7F4")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_B7F4")

    QueueWorkItem2(0x2B, 2, lambda_B7F4)
    Sleep(500)

    ChrTalk(
        0x2B,
        (
            "#3200433V#0312F#11PIsn't this great?! I'm gettin' PUMPED!\x02\x03",
            "#3200434VI'm gonna have to pull out all the stops,\x01",
            "so let's enjoy the hell outta this!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrChipByIndex(0x16, 0x2B)
    BeginChrThread(0x17, 3, 0, 32)
    BeginChrThread(0x16, 3, 0, 33)
    OP_68(-7310, 2000, -9830, 0)
    MoveCamera(317, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    OP_68(-19630, 2000, -10660, 4000)
    MoveCamera(297, 27, 0, 4000)
    OP_6E(400, 4000)
    SetCameraDistance(23270, 4000)
    SetMessageWindowPos(14, -10, -1, 3)

    AnonymousTalk(
        0x1B,
        (
            "#3200435V#16A#30W#2103FTeam Bracer is sprinting through the square,\x01",
            "almost reaching the beginning of the third lap!\x02",
        )
    )

    Sleep(3600)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        (
            "#3200436V#20A#30W#2101FIf the two other teams let Team Bracer keep\x01",
            "this firm lead, the match is as good as over...\x02",
        )
    )

    Sleep(400)
    EndChrThread(0x16, 0x3)
    OP_93(0x16, 0x5A, 0x1F4)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x16, 0x2B)

    def lambda_BA3A():

        label("loc_BA3A")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_BA3A")

    QueueWorkItem2(0x16, 2, lambda_BA3A)
    Sleep(300)
    EndChrThread(0x17, 0x3)
    SetChrChipByIndex(0x17, 0x2E)

    def lambda_BA57():

        label("loc_BA57")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_BA57")

    QueueWorkItem2(0x17, 2, lambda_BA57)
    OP_93(0x17, 0x5A, 0x1F4)
    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x19, 0x25)

    def lambda_BA7A():

        label("loc_BA7A")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_BA7A")

    QueueWorkItem2(0x19, 2, lambda_BA7A)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_BA90():

        label("loc_BA90")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_BA90")

    QueueWorkItem2(0x18, 2, lambda_BA90)
    SetChrPos(0x19, -13190, 0, -10450, 270)
    SetChrPos(0x18, -10130, 4300, -7240, 270)
    OP_68(-15530, 2000, -10670, 700)
    OP_6E(380, 700)
    SetCameraDistance(23500, 700)

    AnonymousTalk(
        0x1B,
        (
            "#3200437V#20A#30W#2105FAnd there it is! Nobody thought it'd be that\x01",
            "simple for our dear bracers!\x02",
        )
    )

    Sleep(3600)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x16,
        "#3200438V#0801F#5PHeads-up!\x02",
    )

    CloseMessageWindow()
    Sleep(700)

    ChrTalk(
        0x16,
        "#3200439V#0805F#5PHuh? Why are you alone?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x17,
        "#3200440V#0907F#5P#NIt couldn't be...!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-13540, 3200, -8170, 0)
    MoveCamera(312, 32, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    Sleep(500)

    ChrTalk(
        0x18,
        "#3200441V#0402F#16AGot'cha.\x02",
    )

    Sleep(1500)
    OP_68(-19160, 1990, -9840, 2000)
    MoveCamera(312, 55, 0, 2000)
    OP_6E(1080, 2000)
    SetCameraDistance(9000, 2000)
    EndChrThread(0x18, 0x2)
    BeginChrThread(0x18, 3, 0, 56)
    EndChrThread(0x18, 0x2)
    SetChrChipByIndex(0x19, 0x27)

    def lambda_BC86():
        OP_99(0xFE, 0x17, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_BC86)
    Sleep(1400)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x18, 0xFF)
    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200002, "", 0x30000600, 0x30000700, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x4, "event\\ev303_00.eff")
    LoadEffect(0x2, "event\\ev302_00.eff")
    LoadEffect(0x5, "event\\ev311_00.eff")
    LoadEffect(0x6, "event\\eva01_00.eff")
    EventBegin(0x0)
    Call(0, 65)
    OP_68(-18550, 1810, -10400, 0)
    MoveCamera(37, 33, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_BD7E():

        label("loc_BD7E")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_BD7E")

    QueueWorkItem2(0x19, 2, lambda_BD7E)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_BD94():

        label("loc_BD94")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_BD94")

    QueueWorkItem2(0x18, 2, lambda_BD94)
    SetChrPos(0x16, -16760, 0, -9580, 270)
    SetChrPos(0x17, -16400, 0, -11240, 270)
    SetChrPos(0x19, -19960, 0, -11410, 90)
    SetChrPos(0x18, -20100, 0, -9630, 90)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x16,
        "#3200442V#0802F#11PWow! Nice moves!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#3200443V#1602F#6P#NHah. Right back at you, girlie!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x18,
        (
            "#3200444V#0402F#5PHehe...\x01",
            "Spectacular performance, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#3200445V#0904F#11PLikewise...\x02\x03",
            "#3200446V#0901FLet's go, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#3200447V#0801F#5PYeah!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x16, 0x2)
    SetChrChipByIndex(0x16, 0x2D)

    def lambda_BF22():
        OP_95(0xFE, -11620, 0, -14190, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_BF22)
    Sleep(400)
    EndChrThread(0x17, 0x2)
    SetChrChipByIndex(0x17, 0x30)

    def lambda_BF47():
        OP_95(0xFE, -11250, -540, -15070, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_BF47)

    ChrTalk(
        0x18,
        "#3200448V#0407F#5PLet's chase them down, Wald!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#3200449V#1607F#6P#NYa didn't need to tell me that!\x02",
    )

    CloseMessageWindow()
    OP_E5()
    EndChrThread(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x2A)
    BeginChrThread(0x18, 3, 0, 57)
    Sleep(100)
    EndChrThread(0x19, 0x2)
    SetChrChipByIndex(0x19, 0x27)
    BeginChrThread(0x19, 3, 0, 58)
    SetMessageWindowPos(14, -10, -1, 3)

    AnonymousTalk(
        0x1B,
        "#3200450V#8A#30W#2100FWe've got a dead heat between these two teams!\x02",
    )

    Sleep(2400)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        (
            "#3200451V#8A#30W#2100FWhich of these two fabulous teams\x01",
            "will be the one to seize victory?\x02",
        )
    )

    Sleep(3200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x2A, 0x2)
    SetChrChipByIndex(0x2B, 0x36)
    SetChrChipByIndex(0x2A, 0x33)
    SetChrPos(0x2B, -6110, 0, -10730, 127)
    SetChrPos(0x2A, -6110, 0, -10730, 5)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x2B,
        "#3200452V#12A#30W#0307F#4SHaaaaaaaaaah!\x02",
    )

    CloseMessageWindow()
    OP_95(0x2B, -16000, 0, -10700, 11000, 0x0)
    Sound(1295, 255, 100, 0)

    def lambda_C130():
        OP_95(0xFE, -15720, 0, -10810, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_C130)
    SetChrChipByIndex(0x2B, 0x35)
    SetChrFlags(0x2B, 0x1000)

    def lambda_C153():
        OP_A0(0xFE, 4000, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_C153)
    Sound(532, 0, 100, 0)
    OP_96(0x2B, 0xFFFFADF8, 0x0, 0xFFFFD544, 0x4E20, 0x0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -21800, 1200, -10600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -21300, 1200, -10600, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_71(0xB, 0x10, 0x19, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    Sound(899, 0, 100, 0)
    SetChrChipByIndex(0x2B, 0x36)
    OP_96(0x2B, 0xFFFFB5C8, 0x0, 0xFFFFD634, 0x2EE0, 0x0)

    def lambda_C229():
        OP_95(0xFE, -11250, -540, -15070, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_C229)
    Sleep(700)

    def lambda_C246():
        OP_95(0xFE, -11620, 0, -14190, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_C246)
    SetMessageWindowPos(14, -10, -1, 3)

    AnonymousTalk(
        0x1B,
        (
            "#3200453V#8A#30W#2105FU-Unbelievable! What's this intense\x01",
            "power radiating from Randy?!\x02",
        )
    )

    Sleep(4200)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        (
            "#3200454V#8A#30W#2106FW-Wait... Won't all the equipment get destroyed\x01",
            "if he keeps this up?\x02",
        )
    )

    Sleep(3200)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    ClearMapObjFlags(0xC, 0x4)
    OP_68(30200, -4540, -39130, 0)
    MoveCamera(330, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    OP_6B(0x17)
    MoveCamera(60, 27, 0, 5000)
    BeginChrThread(0x18, 3, 0, 59)
    BeginChrThread(0x19, 3, 0, 60)
    BeginChrThread(0x16, 3, 0, 61)
    BeginChrThread(0x17, 3, 0, 62)
    Sleep(5000)
    OP_6B(0xFF)
    OP_68(33400, -500, -24080, 0)
    MoveCamera(91, 25, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(14000, 3000)
    MoveCamera(91, 25, 5, 3000)
    Sleep(1000)
    SetChrFlags(0x2A, 0x4)
    SetChrPos(0x2A, 25000, -1000, -27210, 90)

    ChrTalk(
        0x19,
        "#3200455V#8A#30W#1605F#11PTh-The hell's this?!\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x17,
        "#3200456V#8A#30W#0901F#12PA wire trap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200457V#5P#8A#30W#0007F...We caught you!\x02",
    )

    CloseMessageWindow()
    OP_68(41380, -500, -22950, 3000)
    MoveCamera(80, 16, 5, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(16000, 3000)
    BeginChrThread(0x2A, 3, 0, 64)
    Sleep(4000)
    OP_68(37090, -500, -23670, 3000)
    MoveCamera(72, 30, 5, 7000)

    ChrTalk(
        0x16,
        "#3200458V#10A#30W#0801F#6P#NArgh. Darn it!\x02",
    )

    OP_A1(0x16, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x16, 0x2D)
    OP_95(0x16, 38410, -2490, -22860, 6000, 0x0)
    SetChrChipByIndex(0x16, 0x2B)

    def lambda_C531():

        label("loc_C531")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_C531")

    QueueWorkItem2(0x16, 2, lambda_C531)
    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#3200459V#8A#1607F#12P#NAs if we'll let you get away!\x02",
    )

    OP_A1(0x19, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x19, 0x27)
    OP_95(0x19, 38260, -2490, -24380, 6000, 0x0)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_C5A9():

        label("loc_C5A9")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_C5A9")

    QueueWorkItem2(0x19, 2, lambda_C5A9)
    CloseMessageWindow()
    OP_E6()
    Sound(804, 0, 100, 0)
    OP_A1(0x17, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    SetChrChipByIndex(0x17, 0x2E)

    ChrTalk(
        0x17,
        "#3200460V#0907F#11PWait!\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_A1(0x18, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    SetChrChipByIndex(0x18, 0x28)

    ChrTalk(
        0x18,
        "#3200461V#0410F#5PWhere's the other one?!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1373, 255, 100, 0)
    Sleep(1000)

    def lambda_C63C():

        label("loc_C63C")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_C63C")

    QueueWorkItem2(0x19, 0, lambda_C63C)
    Sleep(50)

    def lambda_C651():

        label("loc_C651")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_C651")

    QueueWorkItem2(0x16, 0, lambda_C651)
    Sleep(100)

    def lambda_C666():

        label("loc_C666")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_C666")

    QueueWorkItem2(0x17, 0, lambda_C666)
    Sleep(50)

    def lambda_C67B():

        label("loc_C67B")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_C67B")

    QueueWorkItem2(0x18, 0, lambda_C67B)
    OP_68(33430, -500, -22930, 4000)
    MoveCamera(56, 30, 5, 4000)
    SetChrPos(0x2B, 24970, -2400, -21190, 0)

    ChrTalk(
        0x2B,
        "#3200462V#14A#30W#0312F#5P#NYou're wide open!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x2B, 3, 0, 63)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)
    Fade(500)
    OP_68(34310, 4450, -21190, 0)
    MoveCamera(39, 10, 5, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    Sleep(700)
    OP_6B(0x2B)
    SetChrChip(0x0, 0x2B, 0x64, 0x3E8)
    SetChrChipByIndex(0x2B, 0x35)

    def lambda_C76E():
        OP_A0(0xFE, 500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_C76E)
    SetChrFlags(0x2B, 0x4)
    MoveCamera(317, 48, 5, 1000)
    OP_6E(700, 1000)
    SetCameraDistance(16000, 1000)
    Sound(1297, 255, 100, 0)
    Sound(854, 0, 100, 0)
    OP_9D(0x2B, 0x8E94, 0xFFFFF63C, 0xFFFFA236, 0xFA0, 0xFA0)
    Sound(808, 0, 100, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    SetMapObjFlags(0xC, 0x4)
    PlayEffect(0x4, 0xFF, 0x2B, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(834, 0, 100, 0)
    Sound(813, 0, 100, 0)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x18, 0x0)
    TurnDirection(0x17, 0x2B, 0)
    TurnDirection(0x18, 0x2B, 0)
    TurnDirection(0x16, 0x2B, 0)
    TurnDirection(0x19, 0x2B, 0)
    SetChrChipByIndex(0x17, 0x3A)
    SetChrChipByIndex(0x18, 0x38)
    SetChrChipByIndex(0x16, 0x39)
    SetChrChipByIndex(0x19, 0x37)
    Sound(514, 0, 100, 0)
    BeginChrThread(0x17, 3, 0, 68)
    BeginChrThread(0x18, 3, 0, 68)
    BeginChrThread(0x16, 3, 0, 68)
    BeginChrThread(0x19, 3, 0, 68)
    Sound(1741, 255, 100, 1)

    def lambda_C880():
        OP_9D(0xFE, 0x8340, 0xFFFFF63C, 0xFFFF9EBC, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_C880)
    Sound(1404, 255, 100, 2)

    def lambda_C8A3():
        OP_9D(0xFE, 0x8322, 0xFFFFF63C, 0xFFFFA6D2, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_C8A3)
    Sound(1669, 255, 100, 3)

    def lambda_C8C6():
        OP_9D(0xFE, 0x9970, 0xFFFFF63C, 0xFFFFA93E, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_C8C6)
    Sound(1800, 255, 100, 4)

    def lambda_C8E9():
        OP_9D(0xFE, 0x9A6A, 0xFFFFF63C, 0xFFFF9F52, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_C8E9)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(100)
    SetChrChipByIndex(0x2B, 0x36)
    SetChrChip(0x1, 0x2B, 0x0, 0x0)
    Sleep(500)
    CancelBlur(1000)
    Sleep(1500)
    OP_6B(0xFF)
    OP_6E(500, 3000)
    EndChrThread(0x2A, 0x2)
    SetChrChipByIndex(0x2A, 0x33)
    OP_95(0x2A, 38500, -2500, -23850, 5000, 0x0)
    SetChrChipByIndex(0x2A, 0x31)

    def lambda_C95E():

        label("loc_C95E")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_C95E")

    QueueWorkItem2(0x2A, 2, lambda_C95E)

    ChrTalk(
        0x2A,
        "#3200463V#0000FNice one, Randy!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_C999():

        label("loc_C999")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_C999")

    QueueWorkItem2(0x2B, 2, lambda_C999)
    TurnDirection(0x2B, 0x2A, 500)

    ChrTalk(
        0x2B,
        (
            "#3200464V#0307F#5PDamn straight! Let's keep going!\x01",
            "We're almost at the finish line!\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x2B, 0x2)
    ClearChrFlags(0x2B, 0x4)
    ClearChrFlags(0x2A, 0x4)
    SetChrChipByIndex(0x2B, 0x36)

    def lambda_CA1D():
        OP_95(0xFE, 21840, -2500, -24140, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_CA1D)
    Sleep(300)
    SetChrChipByIndex(0x2A, 0x33)

    def lambda_CA3E():
        OP_95(0xFE, 21840, -2500, -24140, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_CA3E)
    Sleep(1500)
    Fade(500)
    OP_68(8660, 1940, -13150, 0)
    MoveCamera(51, 27, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(7500, 0)
    SetChrPos(0x1D, 11600, -10, -9000, 135)
    SetChrPos(0x1E, 12950, -10, -8500, 135)
    SetChrPos(0x1F, 12350, -10, -7600, 135)
    SetChrPos(0x20, 11800, -10, -6250, 135)
    SetChrPos(0x21, 11200, -10, -7700, 135)
    SetChrPos(0x22, 7900, -10, -6300, 135)
    SetChrPos(0x23, 8700, -10, -6800, 135)
    SetChrPos(0x24, 10250, -10, -6200, 135)
    SetChrPos(0x25, 9500, -10, -5100, 135)
    SetChrPos(0x1A, 8700, -10, -8100, 135)
    SetChrPos(0x102, 10750, 0, -11000, 135)
    SetChrPos(0x103, 10100, 0, -10600, 135)

    def lambda_CB5A():

        label("loc_CB5A")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_CB5A")

    QueueWorkItem2(0x1D, 2, lambda_CB5A)

    def lambda_CB6C():

        label("loc_CB6C")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_CB6C")

    QueueWorkItem2(0x1E, 2, lambda_CB6C)

    def lambda_CB7E():

        label("loc_CB7E")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_CB7E")

    QueueWorkItem2(0x1F, 2, lambda_CB7E)

    def lambda_CB90():

        label("loc_CB90")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_CB90")

    QueueWorkItem2(0x20, 2, lambda_CB90)

    def lambda_CBA2():

        label("loc_CBA2")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_CBA2")

    QueueWorkItem2(0x21, 2, lambda_CBA2)

    def lambda_CBB4():

        label("loc_CBB4")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_CBB4")

    QueueWorkItem2(0x22, 2, lambda_CBB4)

    def lambda_CBC6():

        label("loc_CBC6")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_CBC6")

    QueueWorkItem2(0x23, 2, lambda_CBC6)

    def lambda_CBD8():

        label("loc_CBD8")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_CBD8")

    QueueWorkItem2(0x24, 2, lambda_CBD8)

    def lambda_CBEA():

        label("loc_CBEA")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_CBEA")

    QueueWorkItem2(0x25, 2, lambda_CBEA)

    def lambda_CBFC():

        label("loc_CBFC")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_CBFC")

    QueueWorkItem2(0x1A, 2, lambda_CBFC)

    def lambda_CC0E():

        label("loc_CC0E")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_CC0E")

    QueueWorkItem2(0x102, 2, lambda_CC0E)

    def lambda_CC20():

        label("loc_CC20")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_CC20")

    QueueWorkItem2(0x103, 2, lambda_CC20)
    SetChrChipByIndex(0x17, 0x30)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrChipByIndex(0x16, 0x2D)
    SetChrChipByIndex(0x19, 0x27)
    ClearMapObjFlags(0xD, 0x4)
    SetChrPos(0x1B, 4500, 1800, -14300, 90)
    SetChrPos(0x1C, 4059, 1800, -13820, 90)
    SetChrPos(0x2A, 16940, -2170, -20310, 0)

    def lambda_CC7B():
        OP_95(0xFE, 4080, 0, -5300, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_CC7B)
    SetChrPos(0x2B, 16290, -2310, -21940, 0)

    def lambda_CCA6():
        OP_95(0xFE, 2660, 0, -6540, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_CCA6)
    BeginChrThread(0x101, 3, 0, 75)
    Sleep(1500)
    Sound(874, 0, 100, 0)
    Sound(881, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(14, -10, -1, 3)

    AnonymousTalk(
        0x1B,
        "#3200465V#12A#30W#2110F#4SGoal!!!#3S\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        (
            "#3200466V#16A#30W#2102FThe SSS has managed to make an\x01",
            "unprecedented comeback, overcoming\x01",
            "the trials of this violent race!\x02",
        )
    )

    Sleep(2100)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x16, 0x4)
    SetChrPos(0x18, 16940, -2170, -20310, 0)

    def lambda_CDBA():
        OP_95(0xFE, 4080, 0, -5300, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_CDBA)
    Sleep(200)
    SetChrPos(0x17, 16290, -2310, -21940, 0)

    def lambda_CDE8():
        OP_95(0xFE, 2660, 0, -6540, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_CDE8)
    Sleep(200)
    SetChrPos(0x19, 16620, -2270, -21350, 0)

    def lambda_CE16():
        OP_95(0xFE, 3270, 0, -5970, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_CE16)
    SetChrPos(0x16, 16290, -2310, -21940, 0)

    def lambda_CE41():
        OP_95(0xFE, 2660, 0, -6540, 6800, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_CE41)
    Sleep(2100)
    OP_57(0x0)
    OP_5A()
    Sound(876, 0, 100, 0)
    SetMessageWindowPos(14, -10, -1, 3)

    AnonymousTalk(
        0x1B,
        "#3200467V#16A#30W#2100FThe other two teams have reached the finish line!\x02",
    )

    Sleep(1800)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        "#3200468V#16A#30W#2105FOh, my. Which of them arrived first?\x02",
    )

    Sleep(1800)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        (
            "#3200469V#2109FWho cares?! Anyway, give yourselves\x01",
            "#16A#30Wa pat on the back, everyone!\x02",
        )
    )

    Sleep(3400)
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x1B,
        (
            "#3200470V#24A#30W#2109FLet's hear that round of applause from\x01",
            "our audience members!\x02",
        )
    )

    Sleep(3600)
    OP_57(0x0)
    OP_5A()
    Sound(900, 0, 100, 0)
    Sound(874, 0, 100, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    WaitChrThread(0x101, 3)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x1D, 0x2)
    EndChrThread(0x1E, 0x2)
    EndChrThread(0x1F, 0x2)
    EndChrThread(0x20, 0x2)
    EndChrThread(0x21, 0x2)
    EndChrThread(0x22, 0x2)
    EndChrThread(0x23, 0x2)
    EndChrThread(0x24, 0x2)
    EndChrThread(0x25, 0x2)
    EndChrThread(0x1A, 0x2)
    Call(0, 66)
    Call(0, 80)
    Return()

    # Function_71_79D3 end

    def Function_72_D025(): pass

    label("Function_72_D025")

    Sleep(1800)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x1D, 0x2)
    EndChrThread(0x1E, 0x2)
    EndChrThread(0x1F, 0x2)
    EndChrThread(0x20, 0x2)
    EndChrThread(0x21, 0x2)
    EndChrThread(0x22, 0x2)
    EndChrThread(0x23, 0x2)
    EndChrThread(0x24, 0x2)
    EndChrThread(0x25, 0x2)
    EndChrThread(0x1A, 0x2)
    Sleep(4200)

    def lambda_D060():

        label("loc_D060")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_D060")

    QueueWorkItem2(0x1D, 2, lambda_D060)

    def lambda_D072():

        label("loc_D072")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_D072")

    QueueWorkItem2(0x1E, 2, lambda_D072)

    def lambda_D084():

        label("loc_D084")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_D084")

    QueueWorkItem2(0x1F, 2, lambda_D084)

    def lambda_D096():

        label("loc_D096")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_D096")

    QueueWorkItem2(0x20, 2, lambda_D096)

    def lambda_D0A8():

        label("loc_D0A8")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_D0A8")

    QueueWorkItem2(0x21, 2, lambda_D0A8)

    def lambda_D0BA():

        label("loc_D0BA")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_D0BA")

    QueueWorkItem2(0x22, 2, lambda_D0BA)

    def lambda_D0CC():

        label("loc_D0CC")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_D0CC")

    QueueWorkItem2(0x23, 2, lambda_D0CC)

    def lambda_D0DE():

        label("loc_D0DE")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_D0DE")

    QueueWorkItem2(0x24, 2, lambda_D0DE)

    def lambda_D0F0():

        label("loc_D0F0")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_D0F0")

    QueueWorkItem2(0x25, 2, lambda_D0F0)

    def lambda_D102():

        label("loc_D102")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_D102")

    QueueWorkItem2(0x1A, 2, lambda_D102)

    def lambda_D114():

        label("loc_D114")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_D114")

    QueueWorkItem2(0x102, 2, lambda_D114)

    def lambda_D126():

        label("loc_D126")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_D126")

    QueueWorkItem2(0x103, 2, lambda_D126)
    Return()

    # Function_72_D025 end

    def Function_73_D134(): pass

    label("Function_73_D134")

    OP_95(0xFE, 1490, 0, 7480, 2000, 0x0)
    OP_95(0xFE, 1490, 0, 30000, 2000, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_73_D134 end

    def Function_74_D167(): pass

    label("Function_74_D167")

    OP_95(0xFE, 2460, 0, 6790, 2000, 0x0)
    OP_95(0xFE, 2460, 0, 30000, 2000, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_74_D167 end

    def Function_75_D19A(): pass

    label("Function_75_D19A")

    OP_95(0xFE, 7050, 0, 3670, 2000, 0x0)
    TurnDirection(0xFE, 0x2A, 500)
    Return()

    # Function_75_D19A end

    def Function_76_D1B6(): pass

    label("Function_76_D1B6")

    OP_95(0xFE, 7380, 0, 2610, 2000, 0x0)
    TurnDirection(0xFE, 0x2B, 500)
    Return()

    # Function_76_D1B6 end

    def Function_77_D1D2(): pass

    label("Function_77_D1D2")

    OP_92(0xFE, 0x251C, 0xFFFFC392, 0x1F4)
    OP_95(0xFE, 9500, -300, -15470, 3000, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_77_D1D2 end

    def Function_78_D1FE(): pass

    label("Function_78_D1FE")

    OP_92(0xFE, 0xFFFFF038, 0xC10CA3D7, 0x1F4)
    OP_95(0xFE, -4040, 0, -8790, 2000, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_78_D1FE end

    def Function_79_D22A(): pass

    label("Function_79_D22A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D2B6")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D266")
    Sleep(50)
    Jump("loc_D2AE")

    label("loc_D266")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D27D")
    Sleep(150)
    Jump("loc_D2AE")

    label("loc_D27D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D294")
    Sleep(200)
    Jump("loc_D2AE")

    label("loc_D294")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D2AB")
    Sleep(300)
    Jump("loc_D2AE")

    label("loc_D2AB")

    Sleep(400)

    label("loc_D2AE")

    Sleep(50)
    Jump("Function_79_D22A")

    label("loc_D2B6")

    Return()

    # Function_79_D22A end

    def Function_80_D2B7(): pass

    label("Function_80_D2B7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
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
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
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
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    LoadChrToIndex("chr/ch00000.itc", 0x37)
    LoadChrToIndex("chr/ch00100.itc", 0x38)
    LoadChrToIndex("chr/ch00200.itc", 0x39)
    LoadChrToIndex("chr/ch00300.itc", 0x3A)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    LoadChrToIndex("chr/ch00400.itc", 0x20)
    LoadChrToIndex("chr/ch02100.itc", 0x21)
    LoadChrToIndex("chr/ch06700.itc", 0x22)
    LoadChrToIndex("apl/ch50317.itc", 0x23)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x2A, 0x4)
    ClearChrFlags(0x2B, 0x4)
    ClearChrFlags(0x2C, 0x4)
    ClearChrFlags(0x2D, 0x4)
    SetChrFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x8000)
    SetChrChipByIndex(0x2A, 0x37)
    SetChrChipByIndex(0x2B, 0x3A)
    SetChrChipByIndex(0x2C, 0x38)
    SetChrChipByIndex(0x2D, 0x39)
    SetChrSubChip(0x2A, 0x0)
    SetChrSubChip(0x2B, 0x0)
    SetChrSubChip(0x2C, 0x0)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrPos(0x2A, 8400, 0, 3900, 0)
    SetChrChipByIndex(0x2A, 0x23)
    SetChrSubChip(0x2A, 0x0)
    SetChrFlags(0x2A, 0x2)
    SetChrPos(0x2B, 9170, 0, 3280, 224)
    SetChrFlags(0x2B, 0x8)
    SetChrPos(0x2D, 8600, 0, 6160, 185)
    SetChrPos(0x2C, 7740, 0, 6270, 161)
    SetChrPos(0x18, 8610, 0, -7590, 68)
    SetChrPos(0x19, 7270, 0, -9110, 178)
    SetChrPos(0x16, -4080, 0, -8100, 195)
    SetChrPos(0x17, -3180, 0, -9070, 287)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_68(8800, 2000, 4470, 0)
    MoveCamera(79, 19, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(24500, 0)
    Sleep(1000)
    Sleep(1000)
    PlayBGM("ed7514", 0)
    OP_6E(400, 10000)
    BeginChrThread(0x2A, 2, 0, 79)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrPos(0x101, 8400, -700, 4570, 0)
    SetChrPos(0x104, 8890, -700, 3750, 0)

    ChrTalk(
        0x101,
        "#3200471V#0006F#5P#50W*pant* *pant* *pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3200472V#0303F#11P#50W*pant* *pant* *pant* *pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#3200473V#0102FHeehee.\x01",
            "Great race, you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#3200474V#0202F#5PI was on the edge of my seat.\x01",
            "Congratulations on being victorious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200475V#0002F#5P#40WIt was all...thanks to Randy's...\x01",
            "strategy and traps...*pant* *pant*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200476V#0302F#11P#40WNah, man... If ya weren't there...\x01",
            "I would have never...managed to\x01",
            "pull off that last trick...\x02\x03",
            "#3200477V#0306FI need a break.\x01",
            "L-Lloyd, I think we went a lil' too fast...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x2C,
        "#3200478V#0106F*sigh* I swear, you boys are all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#3200479V#0203F#5P...simpleminded? Or stubborn?\x02\x03",
            "#3200480V#0202FWell, I suppose there was also a girl participating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#3200481V#0109FOh, you're right.\x02\x03",
            "#3200482V#0102FYou two sit tight for a minute.\x01",
            "I'll go buy some cold drinks, okay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2D, 0x2C, 500)

    ChrTalk(
        0x2D,
        (
            "#3200483V#0202F#11PAh. I shall accompany you.\x02\x03",
            "#3200484VThe marketplace on East Street is\x01",
            "adequate, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#3200485V#0104FYes. You read my mind, Tio.\x02\x03",
            "#3200486V#0100FWait for just a bit, you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2C, 0xE1, 0x1F4)
    BeginChrThread(0x2C, 3, 0, 73)
    Sleep(400)
    BeginChrThread(0x2D, 3, 0, 74)
    Sleep(3000)
    Fade(500)
    OP_68(8660, 2000, 3480, 0)
    MoveCamera(104, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    Sleep(500)
    OP_68(8660, 2000, 3480, 40000)
    MoveCamera(88, 10, 0, 40000)
    OP_6E(520, 40000)
    SetCameraDistance(15500, 40000)
    EndChrThread(0x2A, 0xFF)
    SetChrSubChip(0x2A, 0x8)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#3200487V#0006F#30WAh...ugh...\x02\x03",
            "#3200488V#0008FNow that I think about it...why the hell did we\x01",
            "even sign up for this in the first place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200489V#0304F#30WHaha. S'pose it wasn't the wisest\x01",
            "move in the playbook.\x02\x03",
            "#3200490V#0308F#40W...\x02",
        )
    )

    CloseMessageWindow()
    Sound(820, 0, 100, 0)
    OP_A0(0x2A, 1200, 0x8, 0xA)
    OP_63(0x2B, 0xFFFFFE3E, 1000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x2B)
    OP_63(0x2A, 0xFFFFFDA8, 1100, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)
    OP_A1(0x2A, 0x4B0, 0x3, 0xA, 0xD, 0xE)

    ChrTalk(
        0x101,
        "#3200491V#0005F#30WRandy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200492V#0303F#30WI'm sure you've been wonderin'...\x02\x03",
            "#3200493V...why'd I go and lose my temper like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200494V#0005F#30WAh...\x02\x03",
            "#3200495V#0001F#30W...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1500)

    ChrTalk(
        0x104,
        (
            "#3200496V#0308F#30WI...I just don't get it.\x02\x03",
            "#3200497VIs the me who's always smilin' and laughin'\x01",
            "now the real me?\x02\x03",
            "#3200498V#0308FOr, is the monster who lost his cool during\x01",
            "a fun little game who I really am?\x02\x03",
            "#3200499V#0303FThe answer has become totally muddled\x01",
            "these past two years...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3200500V#0001F#30WRandy...\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0xFFFFFDA8, 1100, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x2A)

    ChrTalk(
        0x101,
        (
            "#3200501V#0008FHey, where were you before you\x01",
            "joined the Guardian Force?\x02\x03",
            "#3200502VI've heard you say that you aren't\x01",
            "from Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200503V#0304F#30WHaha. Where was I, he asks?\x02\x03",
            "#3200504V#0312F...A place as hot as Gehenna,\x01",
            "and as cold as the underworld.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3200505V#0005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200506V#0311F#30WWhere both blood and soul boil...\x01",
            "A world frozen over...\x02\x03",
            "#3200507VA place where the brightness of life\x01",
            "and the dirtiest filth of human nature\x01",
            "mix into an unholy fusion of suffering...\x02\x03",
            "#3200508V#0303FThat's where I was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3200509V#0001FRandy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3200510V#0300FI'm just messin' with ya.\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_A1(0x2A, 0x5DC, 0x3, 0xE, 0xF, 0x10)
    Sleep(1000)
    Sound(820, 0, 100, 0)
    OP_A1(0x2A, 0x5DC, 0x5, 0x11, 0x12, 0x13, 0x14, 0x15)
    Sleep(1000)
    SetChrPos(0x101, 8240, -400, 3940, 0)
    SetChrPos(0x104, 8490, -300, 3110, 0)

    ChrTalk(
        0x104,
        (
            "#3200511V#0309F#5PWell, I s'pose that ain't too far off.\x02\x03",
            "#3200512V#0302FMy past, or whatever you wanna call it, isn't\x01",
            "somethin' for the history books, y'know.\x02\x03",
            "#3200513VI'm just livin' life in the present. I'm a suave,\x01",
            "good-lookin' dude who loves the nightlife.\x02\x03",
            "#3200514V#0304FNothin' more, nothin' less.\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_A1(0x2A, 0x5DC, 0x3, 0x15, 0x16, 0x17)
    OP_A1(0x2A, 0x5DC, 0x2, 0x19, 0x1A)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3200515V#0008F#5P...\x02\x03",
            "#3200516V#0006FYou know, Randy.\x02\x03",
            "#3200517V#0002FI've mentioned it before, but I had\x01",
            "an older brother.\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x2A, 0x5DC, 0x2, 0x1A, 0x19)
    OP_A1(0x2A, 0x5DC, 0x5, 0x19, 0x1B, 0x1C, 0x1D, 0x1E)

    ChrTalk(
        0x104,
        "#3200518V#0305F#11PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200519V#0004F#5PGuy Bannings... An ace detective from the\x01",
            "CPD's First Division.\x02\x03",
            "#3200520VHe was unbelievably optimistic, almost to\x01",
            "an unhealthy degree.\x02\x03",
            "#3200521VAfter we lost our parents to an accident,\x01",
            "he worked hard to support me on his own.\x02\x03",
            "#3200522VHe was the kind of guy who wouldn't even\x01",
            "let things like heartbreak or jealousy faze\x01",
            "him...\x02\x03",
            "#3200523V#0000FAnyway, my brother was an amazing man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3200524V#0300F#11PHuh. Dude sounds like a real character.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_A1(0x2A, 0x4B0, 0x5, 0x17, 0x18, 0x19, 0x18, 0x17)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#3200525V#0304F#5PHaha. Guess your life hasn't exactly been\x01",
            "all sunshine and rainbows, either.\x02\x03",
            "#3200526VSo you've been tryin' to follow in your\x01",
            "bro's footsteps this entire time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200527V#0012F#5PYeah, something like that.\x02\x03",
            "#3200528V#0008FActually, I have a confession to make.\x02\x03",
            "#3200529V#0002FYou know, Randy... You kinda remind me\x01",
            "of my brother.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x96, 1600, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_A1(0x2A, 0x708, 0x5, 0x19, 0x1B, 0x1C, 0x1D, 0x1E)

    ChrTalk(
        0x104,
        "#3200530V#0305F#11PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200531V#0004F#5PI mean, it's not like your appearances are similar.\x01",
            "They aren't. Not in the slightest, but...\x02\x03",
            "#3200532VYou know how you support Elie, Tio, and me,\x01",
            "no matter what we're up against?\x02\x03",
            "#3200533V#0002FThat part of you reminds me of Guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200534V#0305F#11PH-Hey, now... Cool it with the sappy speech,\x01",
            "my man.\x02\x03",
            "#3200535V#0309FYa want my face to turn as red as my hair?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200536V#0009F#5PHaha. Even the way you try to hide your\x01",
            "embarrassment reminds me of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3200537V#0301F#11PDude...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200538V#0004F#5PThat's why...a part of me really respects\x01",
            "you, Randy.\x02\x03",
            "#3200539VYou know yourself well enough that you\x01",
            "can work to take care of others.\x02\x03",
            "#3200540V#0000FNot just as a colleague, but as an adult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3200541V#0305F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200542V#0008F#5PTo be honest, I still have a long way to go.\x02\x03",
            "#3200543VIf you laid your past bare right here and\x01",
            "now, I probably wouldn't be able to help\x01",
            "you at all.\x02\x03",
            "#3200544V#0004FSo, I have a proposal.\x02\x03",
            "#3200545V#0000FSomeday, when I'm able to stand tall and proud,\x01",
            "walking alongside you and my brother...\x02\x03",
            "#3200546V...will you let me hear your story then, Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3200547V#0302F#11PLloyd...\x02",
    )

    CloseMessageWindow()
    OP_A1(0x2A, 0x4B0, 0x3, 0x1E, 0x1F, 0x20)
    OP_63(0x2B, 0x96, 1600, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x2B)
    Sleep(300)
    Sound(1374, 255, 85, 0)
    Sleep(1200)
    OP_A1(0x2A, 0x4B0, 0x5, 0x20, 0x21, 0x22, 0x23, 0x24)
    Sound(820, 0, 100, 0)
    OP_A1(0x2A, 0x5DC, 0x5, 0x24, 0x25, 0x26, 0x25, 0x24)

    ChrTalk(
        0x101,
        "#3200548V#0011F#5PR-Randy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200549V#0304F#11PMan, I give up. I surrender!\x02\x03",
            "#3200550V#0300FGeez, and you've already made Mademois-Elie cry...\x01",
            "You might just be a natural-born ladykiller.\x02\x03",
            "#3200551V#0305FWait, wouldn't this make you a ladykiller-killer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200552V#0011F#5PWh-What's with you?\x02\x03",
            "#3200553V#0013FAnd let's not forget that I'm already an adult,\x01",
            "so please stop treating me like I'm some child.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1376, 255, 100, 0)
    Sleep(150)
    OP_82(0x64, 0x0, 0x7D0, 0x12C)

    ChrTalk(
        0x104,
        (
            "#3200554V#0309F#11PHaha...\x01",
            "#4SHahahahahaha!\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x2A, 0x5DC, 0x4, 0x24, 0x25, 0x26, 0x25)
    OP_A1(0x2A, 0x5DC, 0x4, 0x24, 0x25, 0x26, 0x25)
    OP_A1(0x2A, 0x5DC, 0x5, 0x24, 0x25, 0x26, 0x25, 0x24)
    SetChrPos(0x2C, 2300, 0, 7050, 194)
    SetChrPos(0x2D, 1700, 0, 5650, 135)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)

    NpcTalk(
        0x2C,
        "Elie's Voice",
        "#3200555V*sigh* What are you two doing?\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 1500, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x64, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(8240, 1500, 2820, 0)
    MoveCamera(22, 27, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24500, 0)
    BeginChrThread(0x2C, 3, 0, 75)
    Sleep(600)
    BeginChrThread(0x2D, 3, 0, 76)
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0x2A, 0x2)
    SetChrPos(0x2A, 8440, 0, 4040, 240)
    SetChrPos(0x2B, 9170, 0, 3280, 240)
    SetChrChipByIndex(0x2A, 0x37)
    SetChrChipByIndex(0x2B, 0x3A)
    SetChrSubChip(0x2A, 0x0)
    SetChrSubChip(0x2B, 0x0)
    Sound(804, 0, 100, 0)
    ClearChrFlags(0x2B, 0x8)
    Sleep(1500)

    ChrTalk(
        0x2C,
        "#3200556V#0106F#6PHere, cold refreshments. Drink up.\x02",
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x2C, 0x0, 0x320, 0x5DC, 0x0)
    Sleep(100)
    OP_96(0x2C, 0x1B8A, 0x0, 0xE56, 0x4B0, 0x0)
    WaitChrThread(0x2D, 3)

    ChrTalk(
        0x2D,
        (
            "#3200557V#0202F#6PThere was a stall selling soft drinks,\x01",
            "so we bought some for you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x2D, 0x0, 0x44C, 0x5DC, 0x0)
    Sleep(100)
    OP_96(0x2D, 0x1CD4, 0x0, 0xA32, 0x4B0, 0x0)

    ChrTalk(
        0x2B,
        "#3200558V#0302F#11PAh, thanks a ton.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200559V#0002F#5PYeah, I can't thank you enough.\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x2A,
        "#0003F#11P#10A#70W*glug* *glug* *glug*...\x02",
    )


    ChrTalk(
        0x2B,
        "#3200560V#0303F#12P#10A#70W*glug* *glug* *glug*...\x02",
    )

    Sound(887, 0, 100, 0)
    Sleep(800)
    Sound(887, 0, 100, 0)
    Sleep(800)
    Sound(887, 0, 100, 0)
    Sleep(900)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x2A,
        "#0014F#11P#1K#4SAaaaaaaah!\x02",
    )


    ChrTalk(
        0x2B,
        "#3200562V#0309F#12P#1K#4SAaaaaaaah!\x02",
    )

    OP_57(0x1)
    OP_5A()
    Sleep(500)

    ChrTalk(
        0x2C,
        (
            "#3200564V#0113F#6PI seriously don't get boys sometimes.\x02\x03",
            "#3200565V#0111FYou just wore yourselves out in that race, so\x01",
            "don't fool around too much when you're tired.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2D, 0x2C, 500)

    ChrTalk(
        0x2D,
        "#3200566V#0202F#12PDo I detect hints of jealousy, Elie?\x02",
    )

    CloseMessageWindow()
    OP_63(0x2C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(800)
    TurnDirection(0x2C, 0x2D, 800)
    OP_63(0x2C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_96(0x2C, 0x1AC2, 0x0, 0x100E, 0xBB8, 0x0)
    Sleep(500)

    ChrTalk(
        0x2C,
        (
            "#3200567V#0112F#5PWh-What? N-No, why would I ever be jealous\x01",
            "over something like this?!\x02\x03",
            "#3200568VAnd, more importantly... They're both boys,\x01",
            "so why should I be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#3200569V#0204F#12PWhile I may be inexperienced, I have\x01",
            "heard it is a popular genre.\x02\x03",
            "#3200570V#0202FThis scenario may serve to act as a flag.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        "#3200571V#0112F#5PY-You think so?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2C, 500)

    ChrTalk(
        0x2B,
        (
            "#3200572V#0302F#11PSorry, Mademois-Elie!\x02\x03",
            "#3200573V#0309FLove is a battlefield, y'know?!\x01",
            "All's fair, as they say.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2C, 0x2B, 500)

    ChrTalk(
        0x2C,
        "#3200574V#0111F#5PY-You...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200575V#0006F#11P*sigh* What are you guys even talking about?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Young Man's Voice",
        "#3200576VLively as always.\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_F551():

        label("loc_F551")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_F551")

    QueueWorkItem2(0x2A, 0, lambda_F551)

    def lambda_F563():

        label("loc_F563")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_F563")

    QueueWorkItem2(0x2C, 0, lambda_F563)

    def lambda_F575():

        label("loc_F575")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_F575")

    QueueWorkItem2(0x2D, 0, lambda_F575)

    def lambda_F587():

        label("loc_F587")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_F587")

    QueueWorkItem2(0x2B, 0, lambda_F587)
    Fade(500)
    SetChrPos(0x2D, 6090, 0, 3190, 230)
    OP_68(7880, 1710, 1510, 0)
    MoveCamera(127, 30, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18500, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x4)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x23, 0xB)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x24, 0xC)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x25, 0xC)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrPos(0x18, 7000, 0, -5000, 0)
    SetChrPos(0x1A, 6200, 0, -6000, 0)
    SetChrPos(0x22, 7000, 0, -7000, 0)
    SetChrPos(0x23, 7600, 0, -6000, 0)
    SetChrPos(0x24, 6700, 0, -8350, 0)
    SetChrPos(0x25, 5200, 0, -6900, 0)

    def lambda_F6D9():
        OP_95(0xFE, 7000, 0, -180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_F6D9)

    def lambda_F6F3():
        OP_95(0xFE, 6200, 0, -1180, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_F6F3)

    def lambda_F70D():
        OP_95(0xFE, 7000, 0, -2180, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 3, lambda_F70D)

    def lambda_F727():
        OP_95(0xFE, 7600, 0, -1180, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_F727)

    def lambda_F741():
        OP_95(0xFE, 6700, 0, -3350, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_F741)

    def lambda_F75B():
        OP_95(0xFE, 5200, 0, -1900, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 3, lambda_F75B)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0xD)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x5)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x1F, 0xD)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x20, 0x5)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x21, 0xD)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x19, 9500, 0, -5300, 0)
    SetChrPos(0x1D, 8700, 0, -6300, 0)
    SetChrPos(0x1E, 10300, 0, -6300, 0)
    SetChrPos(0x1F, 10300, 0, -7900, 0)
    SetChrPos(0x20, 8700, 0, -7900, 0)
    SetChrPos(0x21, 11400, 0, -7800, 0)

    def lambda_F871():
        OP_95(0xFE, 9500, 0, -500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_F871)

    def lambda_F88B():
        OP_95(0xFE, 8700, 0, -1500, 1100, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_F88B)

    def lambda_F8A5():
        OP_95(0xFE, 10300, 0, -1500, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_F8A5)

    def lambda_F8BF():
        OP_95(0xFE, 10300, 0, -3100, 1100, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_F8BF)

    def lambda_F8D9():
        OP_95(0xFE, 8700, 0, -3100, 1100, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_F8D9)

    def lambda_F8F3():
        OP_95(0xFE, 11400, 0, -3000, 1100, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_F8F3)
    Sleep(1500)

    ChrTalk(
        0x2A,
        "#3200577V#0000F#6PHey, you guys. Already recovered?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x18, 3)

    ChrTalk(
        0x18,
        (
            "#3200578V#0404F#11PPretty much.\x02\x03",
            "#3200579V#0402FUnfortunately, I must declare our\x01",
            "earnest defeat by your hands.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x19, 3)
    TurnDirection(0x19, 0x2B, 500)

    ChrTalk(
        0x19,
        (
            "#3200580V#1603F#11PDamn. What a crappy ending.\x02\x03",
            "#3200581V#1601FHey, Red. How 'bout you and I go at it\x01",
            "for real next time?\x02\x03",
            "#3200582VThat last spurt of explosive power you had...\x01",
            "Had your claws sheathed, did ya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#3200583V#0306F#6PAh... Well, I wouldn't say sheathed.\x01",
            "Bit more to it than that.\x02\x03",
            "#3200584V#0300FIf I try usin' that much power all at\x01",
            "once, I usually end up dog-tired.\x02\x03",
            "#3200585VI like to think of it as my trump card,\x01",
            "so I don't like showin' it off that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#3200586V#1600F#11PBoth you and that damn black-haired dude...\x02\x03",
            "#3200587V#1604FEh, screw it. I'm too tired to think 'bout it.\x02\x03",
            "#3200588VSaber Vipers, we're rollin' out.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(260, 20, -1, -1)
    SetChrName("Saber Vipers")

    AnonymousTalk(
        0xFF,
        "#3200589V#4SRIGHT!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_FCAD():

        label("loc_FCAD")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_FCAD")

    QueueWorkItem2(0x1D, 2, lambda_FCAD)

    def lambda_FCBF():

        label("loc_FCBF")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_FCBF")

    QueueWorkItem2(0x1E, 2, lambda_FCBF)

    def lambda_FCD1():

        label("loc_FCD1")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_FCD1")

    QueueWorkItem2(0x1F, 2, lambda_FCD1)

    def lambda_FCE3():

        label("loc_FCE3")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_FCE3")

    QueueWorkItem2(0x20, 2, lambda_FCE3)

    def lambda_FCF5():

        label("loc_FCF5")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_FCF5")

    QueueWorkItem2(0x21, 2, lambda_FCF5)
    BeginChrThread(0x19, 3, 0, 77)
    Sleep(1500)
    EndChrThread(0x1F, 0x2)
    BeginChrThread(0x1F, 3, 0, 77)
    Sleep(150)
    EndChrThread(0x20, 0x2)
    BeginChrThread(0x20, 3, 0, 77)
    Sleep(150)
    EndChrThread(0x1D, 0x2)
    BeginChrThread(0x1D, 3, 0, 77)
    Sleep(150)
    EndChrThread(0x21, 0x2)
    BeginChrThread(0x21, 3, 0, 77)
    Sleep(150)
    EndChrThread(0x1E, 0x2)
    BeginChrThread(0x1E, 3, 0, 77)

    ChrTalk(
        0x18,
        (
            "#3200591V#0402F#11PHeh. We'll use this opportunity to take\x01",
            "our leave as well...\x02\x03",
            "#3200592V#0409FAdios. I appreciate the entertainment.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x1A,
        "#3200593V#11PLet us withdraw.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(320, 60, -1, -1)
    SetChrName("Testaments")

    AnonymousTalk(
        0xFF,
        "#3200594V#4SJA!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    BeginChrThread(0x24, 3, 0, 78)
    Sleep(150)
    BeginChrThread(0x25, 3, 0, 78)
    Sleep(150)
    BeginChrThread(0x22, 3, 0, 78)
    Sleep(150)
    BeginChrThread(0x1A, 3, 0, 78)
    Sleep(150)
    BeginChrThread(0x23, 3, 0, 78)
    Sleep(500)
    BeginChrThread(0x18, 3, 0, 78)
    Sleep(1000)

    NpcTalk(
        0x16,
        "Girl's Voice",
        (
            "#3200596VWow... At least these guys have better\x01",
            "leadership than the Ravens, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_FF2B():

        label("loc_FF2B")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_FF2B")

    QueueWorkItem2(0x2A, 0, lambda_FF2B)

    def lambda_FF3D():

        label("loc_FF3D")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_FF3D")

    QueueWorkItem2(0x2C, 0, lambda_FF3D)

    def lambda_FF4F():

        label("loc_FF4F")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_FF4F")

    QueueWorkItem2(0x2D, 0, lambda_FF4F)

    def lambda_FF61():

        label("loc_FF61")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_FF61")

    QueueWorkItem2(0x2B, 0, lambda_FF61)
    Sleep(1000)
    Fade(500)
    OP_68(3990, 1500, 2440, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrPos(0x16, 3140, 0, 1400, 225)
    SetChrPos(0x17, 1830, 0, 1460, 90)

    def lambda_FFDF():
        OP_95(0xFE, 8300, 0, 1510, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_FFDF)

    def lambda_FFF9():
        OP_95(0xFE, 6790, 0, 1680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_FFF9)
    OP_68(7460, 1500, 2790, 2000)
    Sleep(2000)

    def lambda_10027():

        label("loc_10027")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_10027")

    QueueWorkItem2(0x16, 0, lambda_10027)

    def lambda_10039():

        label("loc_10039")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_10039")

    QueueWorkItem2(0x17, 0, lambda_10039)

    ChrTalk(
        0x16,
        "#3200597V#0809F#12PHeehee. Congrats again, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200598V#0002F#5PYou two weren't so bad yourselves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#3200599V#0300F#5PHuh? You guys headin' back already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#3200600V#0902F#6PYeah, we were in the middle of a job before\x01",
            "we got tangled up in this mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "#3200601V#0203F#5PInterestingly enough, we were in a similar situation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        "#3200602V#0106F#5P*sigh* It's already evening, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#3200603V#0809F#12PAhaha. What's the big deal?\x01",
            "We had a ton of fun!\x02\x03",
            "#3200604V#0802FC'mon, you gotta live a little\x01",
            "during the festivities, right?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200605V#0012F#5PSh-She's too bright...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#3200606V#0909F#6PHaha. Trust me, that's one of Estelle's\x01",
            "best qualities.\x02\x03",
            "#3200607V#0908FHey, Randy.\x02\x03",
            "#3200608V#0901FIs your body holding up okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x2A,
        "#3200609V#0005F#5PEh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#3200610V#0305F#5PHuh?\x02\x03",
            "#3200611V#0300FI didn't peg ya for having the same\x01",
            "background, but maybe I was off?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#3200612V#0903F#6PNo, my circumstances are little different.\x02\x03",
            "#3200613V#0901FBut I do have a good idea of what you did\x01",
            "back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#3200614V#0300F#5PYeah?\x02\x03",
            "#3200615V#0304FWell, I've been usin' it ever since I was\x01",
            "a little kid, so...\x02\x03",
            "#3200616VI should hold up just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#3200617V#0904F#6POh, really?\x02\x03",
            "#3200618V#0900FI apologize if I said anything uncalled for, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#3200619V#0302F#5PDon't worry 'bout it, man.\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x2A,
        "#3200620V#0001F#5PRandy?\x02",
    )

    CloseMessageWindow()

    def lambda_1061C():

        label("loc_1061C")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_1061C")

    QueueWorkItem2(0x16, 0, lambda_1061C)
    Sleep(300)

    ChrTalk(
        0x16,
        (
            "#3200621V#0801F#11PHold on a second here. Why are you two\x01",
            "on the same wavelength?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10688():

        label("loc_10688")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_10688")

    QueueWorkItem2(0x17, 0, lambda_10688)
    Sleep(200)

    ChrTalk(
        0x17,
        (
            "#3200622V#0904F#6PHaha. Don't worry about it, Estelle.\x02\x03",
            "#3200623V#0900FShouldn't it be about time to leave, anyway?\x01",
            "Arios should be returning soon, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#3200624V#0805F#11POh, yeah.\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#3200625V#0801F#11PActually, I just remembered something.\x01",
            "Let's run it by them, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#3200626V#0905F#6POh... All right.\x02\x03",
            "#3200627V#0901FMight as well, since we're all here.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_10891():

        label("loc_10891")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_10891")

    QueueWorkItem2(0x17, 0, lambda_10891)

    def lambda_108A3():

        label("loc_108A3")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_108A3")

    QueueWorkItem2(0x16, 0, lambda_108A3)
    Fade(1000)
    OP_68(7700, 1730, 3080, 0)
    MoveCamera(102, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    OP_68(7280, 1730, 3440, 30000)
    MoveCamera(125, 32, 0, 30000)
    OP_6E(500, 30000)
    SetCameraDistance(16000, 30000)
    Sleep(1000)

    ChrTalk(
        0x2A,
        "#3200628V#0005F#5P'Run it by them'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#3200629V#0305F#5PSomethin' up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#3200630V#0806F#11PYeah, actually...\x02\x03",
            "#3200631V#0801FYou guys ever hear about this\x01",
            "'Schwarze Auction'?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x2C,
        "#3200632V#0105F#6PSchwarze...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "#3200633V#0205F#6P#NIs that...a real auction?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x16,
        (
            "#3200634V#0806F#11PYeah, it's apparently some fancy-schmancy\x01",
            "auction that's held somewhere in Crossbell.\x02\x03",
            "#3200635VOur intel tells us that they run it every year\x01",
            "during the Anniversary Festival.\x02\x03",
            "#3200636V#0801FThe kicker? They totally deal in stolen goods.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x2C,
        "#3200637V#0101F#6PS-Stolen goods?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200638V#0013F#6PAre you serious?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#3200639V#0903F#11PWell, it's still a rumor...for the time being.\x02\x03",
            "#3200640V#0908FThe story goes that only the most lavish of\x01",
            "items whose origins remain a mystery are\x01",
            "put up for auction there.\x02\x03",
            "#3200641V#0901FJudging by your reaction, it's safe to assume\x01",
            "you've never heard of it before, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200642V#0006F#6PYeah, first I've heard of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#3200643V#0201F#6P#NI cannot locate anything like that\x01",
            "in the police database, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x2B,
        (
            "#3200644V#0303F#5PThe Schwarze Auction... Pretty fancy\x01",
            "name, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        "#3200645V#0108F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#3200646V#0806F#11PSeriously? Dang, I was hoping you guys\x01",
            "knew a thing or two about it.\x02\x03",
            "#3200647V#0800FMaybe it really IS just a rumor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#3200648V#0903F#11PHmm, it's possible.\x02\x03",
            "#3200649V#0908FHowever, given that Nial was our source,\x01",
            "there may still be something to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200650V#0001F#6P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#3200651V#0809F#11PHahaha... Sorry to make you guys listen\x01",
            "to our weird ramblings.\x02\x03",
            "#3200652V#0802FAnyway, today was awesome!\x01",
            "Still a little ticked we lost, though.\x02\x03",
            "#3200653VBut, hey! We still got to work on the\x01",
            "same case. I hope we team up again\x01",
            "sometime!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3200654V#0002F#6PHaha. I feel the same way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#3200655V#0904F#11PWell, if you'll excuse us.\x02\x03",
            "#3200656V#0900FThanks for today, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#3200657V#0302F#5PRight back at ya.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The second day of the Anniversary Festival came to a close.\x02\x03",
            "Lloyd and the others returned to the SSS building.\x01",
            "After having wrapped up their reports, they decided\x01",
            "to eat dinner and go to bed a little earlier than usual.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x104, 0x4)
    Sleep(500)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11338")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11373")

    label("loc_11338")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11358")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11373")

    label("loc_11358")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11373")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11373")

    SetScenarioFlags(0x5C, 0)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_80_D2B7 end

    def Function_81_11380(): pass

    label("Function_81_11380")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "           Maison Imelda\x01",
            "～ Currently Unmanaged ～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11453")

    ChrTalk(
        0x101,
        (
            "#0000FEverything's covered in dust...\x01",
            "Doesn't look like anybody's lived\x01",
            "here for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_11453")

    TalkEnd(0xFF)
    Return()

    # Function_81_11380 end

    SaveToFile()

Try(main)
