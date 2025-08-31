from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0200.bin",                # FileName
        "c0200",                    # MapName
        "c0200",                    # Location
        0x000A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 10, 0, 9, 0, 10],
    )

    BuildStringList((
        "c0200",                  # 0
        "Ryu",                    # 1
        "Anri",                   # 2
        "Ponce",                  # 3
        "Burik",                  # 4
        "Momo",                   # 5
        "Bennet",                 # 6
        "Old Man Levick",         # 7
        "Elsa",                   # 8
        "Zeit",                   # 9
        "Detective Dudley",       # 10
        "Zeit",                   # 11
        "車１",                   # 12
        "群衆１",                 # 13
        "群衆２",                 # 14
        "群衆３",                 # 15
        "群衆４",                 # 16
        "群衆５",                 # 17
        "Oscar",                  # 18
        "Central Square",         # 19
        "West Street",            # 20
        "Administrative District",# 21
        "Residential District",   # 22
        "Entertainment District", # 23
        "East Street",            # 24
        "Downtown District",      # 25
        "Harbor District",        # 26
        "IBC",                    # 27
        "Station Street",         # 28
        "Back Alley",             # 29
        "Ursula Road",            # 30
        "East Crossbell Highway", # 31
        "West Crossbell Highway", # 32
        "Mainz Mountain Path",    # 33
    ))

    AddCharChip((
        "chr/ch20600.itc",                   # 00
        "chr/ch22200.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20402.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch34300.itc",                   # 05
        "chr/ch21600.itc",                   # 06
        "chr/ch10400.itc",                   # 07
        "chr/ch02707.itc",                   # 08
        "chr/ch00000.itc",                   # 09
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

    DeclNpc(449,     0,       610,     90,   257,  0x0, 0,   0,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(-1000,   0,       610,     90,   257,  0x0, 0,   1,   0,   0,   1,   0,   16,  255,  0)
    DeclNpc(-15119,  0,       5829,    270,  261,  0x0, 0,   2,   0,   0,   2,   0,   17,  255,  0)
    DeclNpc(6570,    -150,    5119,    90,   341,  0x0, 0,   3,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(5360,    3000,    17690,   0,    257,  0x0, 0,   4,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(3240,    -300,    4559,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-14420,  0,       4199,    0,    389,  0x0, 0,   6,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5360,    3000,    17690,   0,    261,  0x0, 0,   7,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(29809,   -4000,   -18139,  225,  404,  0x0, 0,   8,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       180,  453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 24,  11.5,                  15.5,                  2.0,                   49.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.75,                 -2.2142858505249023,   -0.4000000059604645,   1.0])
    DeclEvent(0x0000, 0, 32,  39.5,                  -19.0,                 -4.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -19.75,                9.5,                   0.9000000357627869,    1.0])

    DeclActor(14410,   -6500,   -13590,  1200,    14410,   -5500,   -13590,  0x007C, 0,  11, 0x0000)
    DeclActor(-32070,  -1000,   11050,   1200,    -32070,  0,       11050,   0x007C, 0,  12, 0x0000)

    PlaceName(70.75, 0.0, -7.0, 0x0000, 0x0000, "Central Square")
    PlaceName(5.0, 0.0, -2.5, 0x0000, 0x0000, "West Street")
    PlaceName(97.75, 0.0, 82.0, 0x0000, 0x0000, "Administrative District")
    PlaceName(-56.0, 0.0, 72.0, 0x0000, 0x0000, "Residential District")
    PlaceName(17.0, 0.0, 64.0, 0x0000, 0x0000, "Entertainment District")
    PlaceName(152.0, 0.0, -30.0, 0x0000, 0x0000, "East Street")
    PlaceName(187.5, 0.0, -85.0, 0x0000, 0x0000, "Downtown District")
    PlaceName(180.0, 0.0, 36.0, 0x0000, 0x0000, "Harbor District")
    PlaceName(154.0, 0.0, 130.0, 0x0000, 0x0000, "IBC")
    PlaceName(82.0, 0.0, -76.0, 0x0000, 0x0000, "Station Street")
    PlaceName(35.0, 0.0, 28.0, 0x0000, 0x0000, "Back Alley")
    PlaceName(79.0, 0.0, -107.0, 0x0000, 0x0000, "Ursula Road")
    PlaceName(206.0, 0.0, -16.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-46.0, 0.0, -4.0, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-40.0, 0.0, 96.0, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(48.75, 0.0, -21.0, 0x0000, 0x0051, "")
    PlaceName(102.5, 0.0, 5.0, 0x0000, 0x0054, "")
    PlaceName(73.25, 0.0, -29.0, 0x0000, 0x0057, "")
    PlaceName(48.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(68.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(17.75, 0.0, 3.0, 0x0000, 0x0053, "")
    PlaceName(8.0, 0.0, 24.0, 0x0000, 0x0053, "")
    PlaceName(32.0, 0.0, 56.0, 0x0000, 0x0052, "")
    PlaceName(36.75, 0.0, 43.0, 0x0000, 0x0053, "")
    PlaceName(45.5, 0.0, 34.5, 0x0000, 0x0053, "")
    PlaceName(74.0, 0.0, 105.5, 0x0000, 0x0051, "")
    PlaceName(186.0, 0.0, -30.0, 0x0000, 0x0052, "")
    PlaceName(169.0, 0.0, -120.5, 0x0000, 0x0053, "")
    PlaceName(156.0, 0.0, -102.0, 0x0000, 0x0053, "")
    PlaceName(82.0, 0.0, -19.0, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_6EC",          # 00, 0
        "Function_1_7A4",          # 01, 1
        "Function_2_805",          # 02, 2
        "Function_3_866",          # 03, 3
        "Function_4_891",          # 04, 4
        "Function_5_965",          # 05, 5
        "Function_6_A39",          # 06, 6
        "Function_7_B0D",          # 07, 7
        "Function_8_BE1",          # 08, 8
        "Function_9_CB5",          # 09, 9
        "Function_10_11C3",        # 0A, 10
        "Function_11_13EE",        # 0B, 11
        "Function_12_1557",        # 0C, 12
        "Function_13_16AE",        # 0D, 13
        "Function_14_2164",        # 0E, 14
        "Function_15_2887",        # 0F, 15
        "Function_16_29ED",        # 10, 16
        "Function_17_356E",        # 11, 17
        "Function_18_4AB0",        # 12, 18
        "Function_19_5F21",        # 13, 19
        "Function_20_66AC",        # 14, 20
        "Function_21_68E0",        # 15, 21
        "Function_22_6A46",        # 16, 22
        "Function_23_6F03",        # 17, 23
        "Function_24_7088",        # 18, 24
        "Function_25_7F09",        # 19, 25
        "Function_26_9378",        # 1A, 26
        "Function_27_96AC",        # 1B, 27
        "Function_28_9BA9",        # 1C, 28
        "Function_29_A277",        # 1D, 29
        "Function_30_A80B",        # 1E, 30
        "Function_31_A8E4",        # 1F, 31
        "Function_32_A900",        # 20, 32
        "Function_33_A91C",        # 21, 33
    ))


    def Function_0_6EC(): pass

    label("Function_0_6EC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_72C"),
        (1, "loc_738"),
        (2, "loc_744"),
        (3, "loc_750"),
        (4, "loc_75C"),
        (5, "loc_768"),
        (6, "loc_774"),
        (SWITCH_DEFAULT, "loc_780"),
    )


    label("loc_72C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_738")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_744")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_750")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_75C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_768")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_774")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_780")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_78C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_7A3")

    Return()

    # Function_0_6EC end

    def Function_1_7A4(): pass

    label("Function_1_7A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_804")
    OP_95(0xFE, 7000, -300, 610, 6000, 0x0)
    OP_95(0xFE, 7000, 0, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, -10, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, 0, 610, 6000, 0x0)
    Jump("Function_1_7A4")

    label("loc_804")

    Return()

    # Function_1_7A4 end

    def Function_2_805(): pass

    label("Function_2_805")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_865")
    OP_95(0xFE, -5160, 0, 5750, 800, 0x0)
    OP_95(0xFE, -5160, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 5750, 800, 0x0)
    Jump("Function_2_805")

    label("loc_865")

    Return()

    # Function_2_805 end

    def Function_3_866(): pass

    label("Function_3_866")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_890")
    OP_94(0xFE, 0xFFFF8F3A, 0x9EC, 0xFFFFAD9E, 0x18EC, 0x3E8)
    Sleep(300)
    Jump("Function_3_866")

    label("loc_890")

    Return()

    # Function_3_866 end

    def Function_4_891(): pass

    label("Function_4_891")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_964")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8D0")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF40C, 0x12C, 0x0)
    Jump("loc_95C")

    label("loc_8D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8F8")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF3A8, 0x12C, 0x0)
    Jump("loc_95C")

    label("loc_8F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_920")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF344, 0x12C, 0x0)
    Jump("loc_95C")

    label("loc_920")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_948")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF2E0, 0x12C, 0x0)
    Jump("loc_95C")

    label("loc_948")

    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF27C, 0x12C, 0x0)

    label("loc_95C")

    Sleep(500)
    Jump("Function_4_891")

    label("loc_964")

    Return()

    # Function_4_891 end

    def Function_5_965(): pass

    label("Function_5_965")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A38")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9A4")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF40C, 0xC8, 0x0)
    Jump("loc_A30")

    label("loc_9A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9CC")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF3A8, 0xC8, 0x0)
    Jump("loc_A30")

    label("loc_9CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9F4")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF344, 0xC8, 0x0)
    Jump("loc_A30")

    label("loc_9F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A1C")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF2E0, 0xC8, 0x0)
    Jump("loc_A30")

    label("loc_A1C")

    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF27C, 0xC8, 0x0)

    label("loc_A30")

    Sleep(600)
    Jump("Function_5_965")

    label("loc_A38")

    Return()

    # Function_5_965 end

    def Function_6_A39(): pass

    label("Function_6_A39")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B0C")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A78")
    OP_96(0xFE, 0x11A8, 0x0, 0xFFFFF1AA, 0x12C, 0x0)
    Jump("loc_B04")

    label("loc_A78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AA0")
    OP_96(0xFE, 0x11DA, 0x0, 0xFFFFF1DC, 0x12C, 0x0)
    Jump("loc_B04")

    label("loc_AA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AC8")
    OP_96(0xFE, 0x120C, 0x0, 0xFFFFF20E, 0x12C, 0x0)
    Jump("loc_B04")

    label("loc_AC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AF0")
    OP_96(0xFE, 0x123E, 0x0, 0xFFFFF240, 0x12C, 0x0)
    Jump("loc_B04")

    label("loc_AF0")

    OP_96(0xFE, 0x1270, 0x0, 0xFFFFF272, 0x12C, 0x0)

    label("loc_B04")

    Sleep(500)
    Jump("Function_6_A39")

    label("loc_B0C")

    Return()

    # Function_6_A39 end

    def Function_7_B0D(): pass

    label("Function_7_B0D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BE0")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B4C")
    OP_96(0xFE, 0xE24, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_BD8")

    label("loc_B4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B74")
    OP_96(0xFE, 0xDF2, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_BD8")

    label("loc_B74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B9C")
    OP_96(0xFE, 0xDC0, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_BD8")

    label("loc_B9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BC4")
    OP_96(0xFE, 0xD8E, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_BD8")

    label("loc_BC4")

    OP_96(0xFE, 0xD5C, 0x0, 0xFFFFF92A, 0xFA, 0x0)

    label("loc_BD8")

    Sleep(550)
    Jump("Function_7_B0D")

    label("loc_BE0")

    Return()

    # Function_7_B0D end

    def Function_8_BE1(): pass

    label("Function_8_BE1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CB4")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C20")
    OP_96(0xFE, 0x910, 0x0, 0xFFFFF272, 0xC8, 0x0)
    Jump("loc_CAC")

    label("loc_C20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C48")
    OP_96(0xFE, 0x942, 0x0, 0xFFFFF240, 0xC8, 0x0)
    Jump("loc_CAC")

    label("loc_C48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C70")
    OP_96(0xFE, 0x974, 0x0, 0xFFFFF20E, 0xC8, 0x0)
    Jump("loc_CAC")

    label("loc_C70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C98")
    OP_96(0xFE, 0x9A6, 0x0, 0xFFFFF1DC, 0xC8, 0x0)
    Jump("loc_CAC")

    label("loc_C98")

    OP_96(0xFE, 0x9D8, 0x0, 0xFFFFF1AA, 0xC8, 0x0)

    label("loc_CAC")

    Sleep(600)
    Jump("Function_8_BE1")

    label("loc_CB4")

    Return()

    # Function_8_BE1 end

    def Function_9_CB5(): pass

    label("Function_9_CB5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E21")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D80")
    SetChrPos(0x0, 110, 3000, 22760, 180)
    SetChrPos(0x1, 110, 3000, 22760, 180)
    SetChrPos(0x2, 110, 3000, 22760, 180)
    SetChrPos(0x3, 110, 3000, 22760, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D53")
    SetChrPos(0x4, 110, 3000, 22760, 180)
    SetChrPos(0x5, 110, 3000, 22760, 180)
    Jump("loc_D72")

    label("loc_D53")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D72")
    SetChrPos(0x4, 110, 3000, 22760, 180)

    label("loc_D72")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E21")

    label("loc_D80")

    SetChrPos(0x0, 24460, 0, -8180, 270)
    SetChrPos(0x1, 24460, 0, -8180, 270)
    SetChrPos(0x2, 24460, 0, -8180, 270)
    SetChrPos(0x3, 24460, 0, -8180, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF9")
    SetChrPos(0x4, 24460, 0, -8180, 270)
    SetChrPos(0x5, 24460, 0, -8180, 270)
    Jump("loc_E18")

    label("loc_DF9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E18")
    SetChrPos(0x4, 24460, 0, -8180, 270)

    label("loc_E18")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E21")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_E91")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0xA, -25120, 0, 4140, 180)
    BeginChrThread(0xA, 0, 0, 3)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_EE3")
    SetChrPos(0x9, 8670, 0, -5340, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0x8, -1000, 0, 610, 90)
    SetChrPos(0xC, 450, 0, 610, 90)
    BeginChrThread(0xC, 0, 0, 1)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_F3B")
    SetChrPos(0x8, 4620, 0, -3570, 315)
    BeginChrThread(0x8, 0, 0, 6)
    SetChrPos(0x9, 3520, 0, -1750, 180)
    BeginChrThread(0x9, 0, 0, 7)
    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 8)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_F81")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 4)
    SetChrPos(0xC, 2580, 0, -3260, 90)
    BeginChrThread(0xC, 0, 0, 5)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_FDA")
    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_FA7")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_FD5")

    label("loc_FA7")

    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)

    label("loc_FD5")

    Jump("loc_1177")

    label("loc_FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1020")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_1020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1038")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_1038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1083")
    SetChrPos(0x8, 29770, -4000, -19580, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 27640, -4000, -18980, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_1177")

    label("loc_1083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_10CE")
    SetChrPos(0x8, 29770, -4000, -19580, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 27640, -4000, -18980, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_1177")

    label("loc_10CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_111C")
    SetChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1117")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)

    label("loc_1117")

    Jump("loc_1177")

    label("loc_111C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1139")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_1139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1156")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_1156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1169")
    SetChrFlags(0xC, 0x80)
    Jump("loc_1177")

    label("loc_1169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1177")
    SetChrFlags(0xC, 0x80)

    label("loc_1177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1188")
    Event(0, 27)

    label("loc_1188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_119C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 25)
    Jump("loc_11AB")

    label("loc_119C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_11AB")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 26)

    label("loc_11AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11C2")
    SetMapFlags(0x10000000)
    Event(0, 28)

    label("loc_11C2")

    Return()

    # Function_9_CB5 end

    def Function_10_11C3(): pass

    label("Function_10_11C3")

    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_11F9")
    ClearMapObjFlags(0xD, 0x4)

    label("loc_11F9")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1211")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1211")

    SetMapObjFrame(0xFF, "br02", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_126E")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_12DF")

    label("loc_126E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_12BA")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_12DF")

    label("loc_12BA")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_12DF")

    ClearMapObjFlags(0x9, 0x10)
    OP_70(0x9, 0x1E)
    OP_1B(0x8, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1301")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_1301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1314")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_1314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1327")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_1327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133A")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_133A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1348")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_1348")

    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1374")
    OP_1B(0x0, 0x0, 0x1E)
    OP_1B(0x1, 0x0, 0x1F)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1374")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_139E")
    OP_1B(0x0, 0x0, 0x1E)

    label("loc_139E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B1")
    OP_70(0x7, 0x0)
    Jump("loc_13B5")

    label("loc_13B1")

    OP_70(0x7, 0x1E)

    label("loc_13B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C8")
    OP_70(0x8, 0x0)
    Jump("loc_13CC")

    label("loc_13C8")

    OP_70(0x8, 0x1E)

    label("loc_13CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E8")
    Jump("loc_13ED")

    label("loc_13E8")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_13ED")

    Return()

    # Function_10_11C3 end

    def Function_11_13EE(): pass

    label("Function_11_13EE")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1522")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x7, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 80)
    AddSepith(0x1, 80)
    AddSepith(0x2, 80)
    AddSepith(0x3, 80)
    AddSepith(0x4, 80)
    AddSepith(0x5, 80)
    AddSepith(0x6, 80)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x80.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x110, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1545")

    label("loc_1522")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Kept you waiting, huh?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1545")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_13EE end

    def Function_12_1557(): pass

    label("Function_12_1557")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1641")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA7, 1)"), scpexpr(EXPR_END)), "loc_15D7")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_163C")

    label("loc_15D7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_163C")

    Jump("loc_16A2")

    label("loc_1641")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wait, you don't live in Villa-Raisins.\x01",
            "Get outta here!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_16A2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1557 end

    def Function_13_16AE(): pass

    label("Function_13_16AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1762")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16CC")
    Call(0, 14)
    Jump("loc_175D")

    label("loc_16CC")


    ChrTalk(
        0xFE,
        (
            "Momo always runs away bawling her eyes out\x01",
            "whenever she gets the slightest bit scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, I knew playing with girls\x01",
            "would be a drag.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175D")

    Jump("loc_2160")

    label("loc_1762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_17CF")

    ChrTalk(
        0xFE,
        "Hey, hey! ROAAAR!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Better hurry up! If you're too slow,\x01",
            "I'm gonna end up catchin' ya!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2160")

    label("loc_17CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_17E0")
    Call(0, 15)
    Jump("loc_2160")

    label("loc_17E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1938")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18B9")
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Heh, trust me. I'm a professional\x01",
            "when it comes to hopscotch!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "Hey, Momo! Go grab\x01",
            "the bag over there!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        "Okay!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_1933")

    label("loc_18B9")


    ChrTalk(
        0xFE,
        "Where the heck is Anri? He's late!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whatever, he's the one who's missing out.\x01",
            "Momo and I are gonna have a blast!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1933")

    Jump("loc_2160")

    label("loc_1938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_19C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1953")
    Call(0, 14)
    Jump("loc_19BB")

    label("loc_1953")


    ChrTalk(
        0xFE,
        "*sigh* I'd rather keel over than study.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anri's a goody two shoes. He never\x01",
            "angers the sister.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19BB")

    Jump("loc_2160")

    label("loc_19C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1A84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19DB")
    Call(0, 14)
    Jump("loc_1A7F")

    label("loc_19DB")


    ChrTalk(
        0xFE,
        (
            "Darn it, you're all so rude for a bunch of\x01",
            "police officers.\x02",
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

    label("loc_1A7F")

    Jump("loc_2160")

    label("loc_1A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1ACC")

    ChrTalk(
        0xFE,
        (
            "Hehe, I'm gonna find an awesome\x01",
            "place to play today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2160")

    label("loc_1ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1C42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE5")
    OP_93(0x8, 0x0, 0x0)

    ChrTalk(
        0xFE,
        (
            "Zeit likes to patrol this area pretty\x01",
            "often, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's fine, but you gotta take\x01",
            "me with you today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#1200FGrrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(He says 'Maybe later, if I feel like it.')\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(Man, it's like their roles are reversed...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C3D")

    label("loc_1BE5")


    ChrTalk(
        0xFE,
        (
            "Zeit likes to patrol this area pretty\x01",
            "often, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Police dogs are so cool!!\x02",
    )

    CloseMessageWindow()

    label("loc_1C3D")

    Jump("loc_2160")

    label("loc_1C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1D98")
    SetScenarioFlags(0x90, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D32")

    ChrTalk(
        0xFE,
        (
            "I wish I had a dog as huge\x01",
            "and awesome as Zeit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He's always so composed!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FZeit sure knows how to earn the hero treatment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FI can hardly blame the boys for\x01",
            "being enamored with him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D93")

    label("loc_1D32")

    OP_93(0x8, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "Zeit! Come here, boy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Whoa, his fangs are ginormous!\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    label("loc_1D93")

    Jump("loc_2160")

    label("loc_1D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1F22")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC0")
    Call(0, 14)
    Jump("loc_1E3D")

    label("loc_1DC0")


    ChrTalk(
        0xFE,
        (
            "There's no point in relying in our\x01",
            "city's police department, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "At least we've got reliable bracers on our side!\x02",
    )

    CloseMessageWindow()

    label("loc_1E3D")

    Jump("loc_1F1D")

    label("loc_1E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF7")

    ChrTalk(
        0xFE,
        "Oh, I didn't notice you guys there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, whatever. Good luck with your work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha, thanks...\x01",
            "(Were we actually acknowledged a little there?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F1D")

    label("loc_1EF7")


    ChrTalk(
        0xFE,
        "Keep up the good work, everyone!\x02",
    )

    CloseMessageWindow()

    label("loc_1F1D")

    Jump("loc_2160")

    label("loc_1F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1F30")
    Jump("loc_2160")

    label("loc_1F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1F3E")
    Jump("loc_2160")

    label("loc_1F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1F8A")

    ChrTalk(
        0xFE,
        (
            "Take this! The greatest bracer to ever live\x01",
            "has arrived!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2160")

    label("loc_1F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2160")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2135")

    ChrTalk(
        0xFE,
        "Hey, you're the guys from the other day!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On patrol or something? Are the police really so\x01",
            "short-staffed that they need you to do it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FBeing a police officer is a busy job, Ryu.\x01",
            "And besides, patrolling is one of our duties.\x02\x03",
            "#0000FPutting that aside, you guys really need to\x01",
            "cut it out with the dangerous stunts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Erk...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "W-Weird.\x01",
            "I have no clue what you're talking about!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2160")

    label("loc_2135")


    ChrTalk(
        0xFE,
        "Have no fear, Arios MacLaine is here!\x02",
    )

    CloseMessageWindow()

    label("loc_2160")

    TalkEnd(0xFE)
    Return()

    # Function_13_16AE end

    def Function_14_2164(): pass

    label("Function_14_2164")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_223D")
    TurnDirection(0x8, 0x9, 0)
    TurnDirection(0x9, 0x8, 0)

    ChrTalk(
        0x8,
        (
            "What's the big deal? We're just\x01",
            "playing a game of tag.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I told you that you went too far\x01",
            "this time, Ryu!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't worry. I'll make sure he\x01",
            "gives a real apology tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2878")

    label("loc_223D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2349")
    TurnDirection(0x8, 0x9, 0)
    TurnDirection(0x9, 0x8, 0)

    ChrTalk(
        0x8,
        (
            "Lame. We have to go to Sunday School today.\x01",
            "Psh, let's just play hooky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't think that's a good idea, Ryu. You\x01",
            "need to start taking school more seriously...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hey, how about we invite Momo\x01",
            "to come with us to the cathedral?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2878")

    label("loc_2349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_254D")
    TurnDirection(0x8, 0x9, 0)
    TurnDirection(0x9, 0x8, 0)

    ChrTalk(
        0x8,
        (
            "Forget her, Anri. How 'bout we just\x01",
            "go hang out on the highway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, you see, my pops has been\x01",
            "crazy busy lately. We'd be able to\x01",
            "slip outside the city with ease!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "U-Uh, Ryu...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Hmm, what's with that face?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FY o u   g u y s... Did you honestly think it'd be\x01",
            "a good idea for a bunch of kids to go waltzing\x01",
            "out onto the highway by themselves?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        (
            "Crap! It's that guy from the SSS!\x01",
            "D-Damn it!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 0)
    Jump("loc_2878")

    label("loc_254D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_255B")
    Jump("loc_2878")

    label("loc_255B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2878")
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0x8,
        "Ah, you're the guys from the SSS.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hahaha! Sorry, but you were too slow!\x02",
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FWhat are you talking about?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_269A")

    ChrTalk(
        0x9,
        (
            "Well, we found a kitten that was\x01",
            "was lost earlier...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D0")

    label("loc_269A")


    ChrTalk(
        0x9,
        (
            "Well, we found a kitten that was\x01",
            "lost yesterday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D0")


    ChrTalk(
        0x9,
        (
            "But this bracer girl that was passing by happened\x01",
            "to see what was going on and solved it like it was\x01",
            "nothing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She was with this black-haired guy, and they\x01",
            "managed to find its owner in no time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, that's a bracer for you! I've\x01",
            "never seen a girl that cool before!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FTh-Those two...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FEstelle and Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FThey sure managed to pull the rug out\x01",
            "from under our feet.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0x9, 0x5A, 0x0)

    label("loc_2878")

    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_14_2164 end

    def Function_15_2887(): pass

    label("Function_15_2887")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0x8, 0xC, 0)
    TurnDirection(0xC, 0x8, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_295F")

    ChrTalk(
        0x8,
        (
            "Huh, it was actually worth it to play\x01",
            "in a group of three.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "All right, Momo! From now on,\x01",
            "you're a part of the squad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, let's keep playing together!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_29D3")

    label("loc_295F")


    ChrTalk(
        0x8,
        (
            "Here, Momo, I'm going to pass it to you!\x01",
            "Get ready to catch it, okay?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        "I'm ready!\x02",
    )

    CloseMessageWindow()

    label("loc_29D3")

    OP_93(0x8, 0x13B, 0x0)
    OP_93(0xC, 0x2D, 0x0)
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_15_2887 end

    def Function_16_29ED(): pass

    label("Function_16_29ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2A52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0B")
    Call(0, 14)
    Jump("loc_2A4D")

    label("loc_2A0B")


    ChrTalk(
        0xFE,
        (
            "You'd better go and give an apology\x01",
            "for real tomorrow, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A4D")

    Jump("loc_356A")

    label("loc_2A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2A93")
    OP_93(0xFE, 0x10E, 0x0)

    ChrTalk(
        0xFE,
        "H-Hey, Ryu!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, you suck at tag!\x02",
    )

    CloseMessageWindow()
    Jump("loc_356A")

    label("loc_2A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2B0D")

    ChrTalk(
        0xFE,
        "Us three are hanging out today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe... Didn't you know? It's more fun to play\x01",
            "in a larger group.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_356A")

    label("loc_2B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2B1B")
    Jump("loc_356A")

    label("loc_2B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2BA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B36")
    Call(0, 14)
    Jump("loc_2BA4")

    label("loc_2B36")


    ChrTalk(
        0xFE,
        "We have to go to Sunday School today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ryu always wants to skip class, and it's\x01",
            "causing me problems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA4")

    Jump("loc_356A")

    label("loc_2BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2C78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC4")
    Call(0, 14)
    Jump("loc_2C73")

    label("loc_2BC4")


    ChrTalk(
        0xFE,
        (
            "S-Sorry, but that's actually the reason you all\x01",
            "had to come rescue us in the first place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to give Ryu a real piece of my\x01",
            "mind before he messes up again!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C73")

    Jump("loc_356A")

    label("loc_2C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2E04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA5")

    ChrTalk(
        0xFE,
        (
            "My father's really going to let me have it if he\x01",
            "catches me skipping any more classes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You wouldn't believe how mad he was when\x01",
            "he found out about the Geofront thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know, my father's had a shorter temper\x01",
            "ever since I started hanging out with Ryu...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DFF")

    label("loc_2DA5")


    ChrTalk(
        0xFE,
        (
            "Hey, Ryu! Wouldn't it be a good idea to actually\x01",
            "reflect on all of your dumb ideas?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DFF")

    Jump("loc_356A")

    label("loc_2E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2F56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE6")

    ChrTalk(
        0xFE,
        "Ryu constantly bad-mouths the police...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He really admires them, though.\x01",
            "Not that he admits it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't blame him, though.\x01",
            "The CPD has cool people like\x01",
            "you working for them, after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F51")

    label("loc_2EE6")


    ChrTalk(
        0xFE,
        (
            "In reality, Ryu really admires\x01",
            "the Crossbell police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's too stubborn to ever admit\x01",
            "it, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F51")

    Jump("loc_356A")

    label("loc_2F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_31F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C5")

    ChrTalk(
        0xFE,
        (
            "It looks like the SSS saved\x01",
            "Ryu yet again.\x01",
            "Really, thank you so much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, Zeit's pretty awesome,\x01",
            "isn't he?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't believe you guys own a police dog!\x01",
            "That's so cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHaha, sorry, kid. 'Own' is a lil'\x01",
            "off the mark in Zeit's case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FWe are not Zeit's owners. He merely stays\x01",
            "with us because he wishes to.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31EC")

    label("loc_30C5")

    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        "Ah, but...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "Shouldn't we head over to the cathedral, Ryu?\x01",
            "The sisters are going to have our heads if we skip!\x02",
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
        "#0012FYeah, you shouldn't skip school, Ryu.\x02",
    )

    CloseMessageWindow()

    label("loc_31EC")

    Jump("loc_356A")

    label("loc_31F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_336C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3219")
    Call(0, 14)
    Jump("loc_32DF")

    label("loc_3219")


    ChrTalk(
        0xFE,
        "That bracer girl was sooo cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She told us that 'A lost kitty is nothing!\x01",
            "I've saved a few of them in my time!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FR-Really? I suppose a request like that\x01",
            "is normal for a bracer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32DF")

    Jump("loc_3367")

    label("loc_32E4")


    ChrTalk(
        0xFE,
        "Thanks for all of the help yesterday, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be sure to come knock on your door if\x01",
            "I ever run into any more trouble!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3367")

    Jump("loc_356A")

    label("loc_336C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_337A")
    Jump("loc_356A")

    label("loc_337A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3388")
    Jump("loc_356A")

    label("loc_3388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_33FB")

    ChrTalk(
        0xFE,
        "*pant* *pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come on, Ryu! Why can't you follow\x01",
            "the rules for just once in your life?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_356A")

    label("loc_33FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_356A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3538")

    ChrTalk(
        0xFE,
        (
            "Oh, it's the Special Support Section guys.\x01",
            "Thanks for helping us out the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our dads were soooo mad. I thought we\x01",
            "were going to get grounded for life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI can't say I'm too surprised.\x01",
            "I'm just glad you're both safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope you all have a good day at work!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_356A")

    label("loc_3538")


    ChrTalk(
        0xFE,
        (
            "Hold on, Ryu! That's not how\x01",
            "the rules work!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_356A")

    TalkEnd(0xFE)
    Return()

    # Function_16_29ED end

    def Function_17_356E(): pass

    label("Function_17_356E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3727")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_368F")

    ChrTalk(
        0xFE,
        (
            "Hmm, this sunset is making me feel\x01",
            "melancholic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I have my time right, the Crossbell Cathedral\x01",
            "should be ringing its bell any second now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had this genius idea of snapping a photo of the\x01",
            "cathedral, with the sunset serving as a backdrop.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3722")

    label("loc_368F")


    ChrTalk(
        0xFE,
        "Wow, today's sunset really is exceptional...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like the setting sun is going to perfectly\x01",
            "complement the grandeur of the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3722")

    Jump("loc_4AAC")

    label("loc_3727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_37EA")

    ChrTalk(
        0xFE,
        (
            "There's been chatter about a shootout that happened\x01",
            "over at the harbor yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't believe something that insane would happen\x01",
            "in the middle of a business district.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AAC")

    label("loc_37EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3947")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38BB")

    ChrTalk(
        0xFE,
        (
            "Somebody told me that there are massive\x01",
            "ruins somewhere around Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a place I've been dying to visit, since I've\x01",
            "been focusing on taking landscape shots.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3942")

    label("loc_38BB")


    ChrTalk(
        0xFE,
        (
            "There are apparently many unexplored\x01",
            "ruins all over Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's so much to miss out on if you only\x01",
            "stick to the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3942")

    Jump("loc_4AAC")

    label("loc_3947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3BBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ADD")

    ChrTalk(
        0xFE,
        (
            "I'm willing to bet the ruins in the middle of the\x01",
            "Mainz Mountain Path are perfect for photography.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been running all over the place, since I've been\x01",
            "focusing on taking landscape photos. I managed to find\x01",
            "a place that really stood out to me, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Silence hung in the air. Not a word could\x01",
            "be heard in that dark, solemn ruin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Granted, I didn't go in.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BB8")

    label("loc_3ADD")


    ChrTalk(
        0xFE,
        (
            "I felt like the ruins in the middle of Mainz Mountain Path\x01",
            "would be a good place for someone to calm down and relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I haven't actually taken a look inside thanks to\x01",
            "the Guardian Force setting up a barricade.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BB8")

    Jump("loc_4AAC")

    label("loc_3BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3D0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C82")

    ChrTalk(
        0xFE,
        (
            "Man, I took enough photos during the\x01",
            "festival to fill an entire scrapbook!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Every place was lively and full of smiles...\x01",
            "Haha, I'm already pumped for next year!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D06")

    label("loc_3C82")


    ChrTalk(
        0xFE,
        (
            "I wonder what kind of photos I'll be able to\x01",
            "snap at next year's Anniversary Festival?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, I'm already so pumped for it.\x02",
    )

    CloseMessageWindow()

    label("loc_3D06")

    Jump("loc_4AAC")

    label("loc_3D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3EE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E36")

    ChrTalk(
        0xFE,
        (
            "There are many ruins scattered around Crossbell\x01",
            "that date all the way back to the Middle Ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The most popular ones can be read about in\x01",
            "tourist guidebooks, but most of them have\x01",
            "yet to be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I personally cannot wait until they've all\x01",
            "been discovered.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3EDD")

    label("loc_3E36")


    ChrTalk(
        0xFE,
        (
            "There are many ruins scattered around Crossbell\x01",
            "that date all the way back to the Middle Ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We still don't know who built them\x01",
            "or what their purpose was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EDD")

    Jump("loc_4AAC")

    label("loc_3EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3F9F")

    ChrTalk(
        0xFE,
        (
            "Phew, I'm glad the weather is nice today.\x01",
            "Now I can proceed with my little expedition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All right, time to pack up my camera and\x01",
            "photo-quartz and head out somewhere!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AAC")

    label("loc_3F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4042")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood seems a lot busier\x01",
            "than usual these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He mentioned how work was starting to pile up\x01",
            "on his desk last time I ran into him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AAC")

    label("loc_4042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4237")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4140")

    ChrTalk(
        0xFE,
        (
            "You'll reach Crossbell's western gate\x01",
            "if you continue along this road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bellguard Gate is at the end of the road, right\x01",
            "beside our border with the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'll often find transport trucks passing\x01",
            "through there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4232")

    label("loc_4140")


    ChrTalk(
        0xFE,
        (
            "If you continue along this road, you'll find\x01",
            "yourself on the West Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Only places you'll find down that way are Bellguard\x01",
            "Gate and the police academy. You'll often find\x01",
            "transport trucks passing through there, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4232")

    Jump("loc_4AAC")

    label("loc_4237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4466")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4380")

    ChrTalk(
        0xFE,
        (
            "Did you know that orbal cameras come in all different\x01",
            "shapes and sizes? There are even different brands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they happen to pique your interest,\x01",
            "I'd recommend the ZCF series.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've got a practical and easy-to-use design,\x01",
            "so those babies are a solid choice for beginners\x01",
            "and pros alike.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4461")

    label("loc_4380")


    ChrTalk(
        0xFE,
        (
            "If they happen to pique your interest,\x01",
            "I'd recommend the ZCF series.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Their design has advanced with each iteration\x01",
            "ever since its inception back in 1180. Their older\x01",
            "models are a prized item for any collector, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4461")

    Jump("loc_4AAC")

    label("loc_4466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4644")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4582")

    ChrTalk(
        0xFE,
        (
            "Have you guys heard about this?\x01",
            "There's apparently an enormous\x01",
            "ancient ruin along Ursula Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's a tower that dates back to the Middle Ages, supposedly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'd be wise to bring a camera with you if you\x01",
            "plan to go somewhere that incredible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_463F")

    label("loc_4582")


    ChrTalk(
        0xFE,
        (
            "I heard that there's a massive tower built in the\x01",
            "Middle Ages along Ursula Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd recommend bringing your camera, along with an\x01",
            "extra photo-quartz if you like taking pictures.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_463F")

    Jump("loc_4AAC")

    label("loc_4644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_47CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_472F")

    ChrTalk(
        0xFE,
        (
            "Word is the police stopped a major incident\x01",
            "in the Downtown District recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You don't hear a story like that often.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a little shocking. I'd heard the police\x01",
            "stopped patrolling downtown.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_47C7")

    label("loc_472F")


    ChrTalk(
        0xFE,
        (
            "There have been some unusual people in\x01",
            "the police force as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a citizen of Crossbell, I would be\x01",
            "interested to hear more about them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47C7")

    Jump("loc_4AAC")

    label("loc_47CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4987")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48E1")

    ChrTalk(
        0xFE,
        (
            "An uptight-looking man dressed in a suit passed by\x01",
            "here a few moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If my eyes aren't deceiving me, I could have\x01",
            "sworn he was wearing a CPD badge...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What business does a police officer have in a\x01",
            "peaceful neighborhood like this?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4982")

    label("loc_48E1")


    ChrTalk(
        0xFE,
        (
            "I can't help but feel that I've seen him\x01",
            "somewhere before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of business a police officer has\x01",
            "in a peaceful neighborhood like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4982")

    Jump("loc_4AAC")

    label("loc_4987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A53")

    ChrTalk(
        0xFE,
        (
            "I think more people have been purchasing\x01",
            "orbal cars lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I love taking photos, so being able to drive\x01",
            "out of the city for some nice shots would be\x01",
            "very convenient.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4AAC")

    label("loc_4A53")


    ChrTalk(
        0xFE,
        (
            "I'd really like to own an orbal car someday.\x01",
            "I sure wish they were cheaper, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AAC")

    TalkEnd(0xFE)
    Return()

    # Function_17_356E end

    def Function_18_4AB0(): pass

    label("Function_18_4AB0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B44")
    Jump("loc_4B8E")

    label("loc_4B44")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B64")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B8E")

    label("loc_4B64")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B84")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B8E")

    label("loc_4B84")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B8E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4D2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C91")

    ChrTalk(
        0xFE,
        (
            "Whoa, it's already evening? I've\x01",
            "gotta get going soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Talk around town is that the diet's budget\x01",
            "meeting has finally adjourned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe it'll finally be peaceful around here again.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4D28")

    label("loc_4C91")


    ChrTalk(
        0xFE,
        "Everything usually calms down once the diet finishes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, all these years I've\x01",
            "lived in Crossbell, and it still\x01",
            "hasn't changed a hair.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D28")

    Jump("loc_5F19")

    label("loc_4D2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4EAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DFD")

    ChrTalk(
        0xFE,
        (
            "Have you guys heard that even more people\x01",
            "in the city have gone missing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not to mention all the commotion\x01",
            "the mafia continues to cause. It's\x01",
            "just one thing after another.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4EA8")

    label("loc_4DFD")


    ChrTalk(
        0xFE,
        "Still, if everything stays peaceful, that'd be great...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As police, surely you've noticed that public order has\x01",
            "been getting worse. Will everything be all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EA8")

    Jump("loc_5F19")

    label("loc_4EAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_500A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F84")

    ChrTalk(
        0xFE,
        "The latest issue of the Crossbell Times was postponed?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No way... My beloved breakfast companion...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How am I going to know what ended up\x01",
            "happening during the diet session?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5005")

    label("loc_4F84")


    ChrTalk(
        0xFE,
        (
            "I don't even remember the last time the\x01",
            "Crossbell Times had to be delayed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What in the world could have caused that?\x02",
    )

    CloseMessageWindow()

    label("loc_5005")

    Jump("loc_5F19")

    label("loc_500A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_513A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50C2")

    ChrTalk(
        0xFE,
        (
            "Apparently, City Hall is like a warzone due\x01",
            "to the diet's ongoing budget meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's like this every year, but this is the\x01",
            "worst it's ever been.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5135")

    label("loc_50C2")


    ChrTalk(
        0xFE,
        (
            "Sounds like the diet's budget meeting is as\x01",
            "rough as ever. I'll be shocked if they come\x01",
            "to an easy agreement.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5135")

    Jump("loc_5F19")

    label("loc_513A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_53B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52EF")

    ChrTalk(
        0xFE,
        (
            "So, the Crossbell Diet's budget meeting\x01",
            "has finally begun, has it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you weren't aware, this annual meeting is when\x01",
            "Crossbell's budget plan for the next year is decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It all comes down to mira. Mira, mira, mira...\x01",
            "The diet's just tangled in foreign interests now,\x01",
            "with members only caring for their own factions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How's this year going to turn out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it is what it is, I guess.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_53AB")

    label("loc_52EF")


    ChrTalk(
        0xFE,
        (
            "Every year, the diet's budget meeting\x01",
            "just becomes stormier and stormier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be frank, all we citizens can do\x01",
            "is sit back and watch their petty,\x01",
            "factional feuds from a distance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53AB")

    Jump("loc_5F19")

    label("loc_53B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_54C6")

    ChrTalk(
        0xFE,
        (
            "I can't help but wonder if Mayor MacDowell is\x01",
            "planning to retire once his current term ends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's already served as Crossbell's mayor\x01",
            "for over a decade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Truth be told, I don't really want him to retire\x01",
            "just yet. He has a good head on his shoulders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F19")

    label("loc_54C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_56CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5604")

    ChrTalk(
        0xFE,
        (
            "The IBC has invested a fortune into the\x01",
            "Epstein Foundation's Orbal Network\x01",
            "Project, for whatever reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard that the project will be able\x01",
            "to connect every single IBC branch\x01",
            "across Zemuria with each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's the IBC for you...\x01",
            "The scale of this project is insane.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_56C9")

    label("loc_5604")


    ChrTalk(
        0xFE,
        (
            "I imagine the Orbal Network Project requires\x01",
            "an extraordinary amount of mira...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To already be setting their eyes on the future like this...\x01",
            "The IBC is really in a whole different league.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56C9")

    Jump("loc_5F19")

    label("loc_56CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_585F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5799")

    ChrTalk(
        0xFE,
        (
            "By the way, I haven't seen that\x01",
            "Crossbell Times reporter lady\x01",
            "around here lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'd be surprised how many times she'd\x01",
            "come through here, sniffing for interviews.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_585A")

    label("loc_5799")


    ChrTalk(
        0xFE,
        (
            "Occasionally, that Crossbell Times reporter lady\x01",
            "would come through here, looking for interviews.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She follows the police like a lost puppy,\x01",
            "sniffing out material for her big stories.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_585A")

    Jump("loc_5F19")

    label("loc_585F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5980")

    ChrTalk(
        0xFE,
        (
            "You can feel the city becoming more cheery,\x01",
            "now that the Anniversary Festival is nearing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did you guys know that this year marks\x01",
            "Crossbell's 70th anniversary as a state?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm willing to bet that they're going to pull out\x01",
            "all the stops for this year's festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F19")

    label("loc_5980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5A3D")

    ChrTalk(
        0xFE,
        (
            "I heard that the Guardian Force was mobilizing\x01",
            "their troops, but why?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Has there been turmoil at the border?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oddly enough, the news hasn't bothered\x01",
            "to cover it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F19")

    label("loc_5A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5ADD")

    ChrTalk(
        0xFE,
        (
            "Mmm, the croissants baked here\x01",
            "are a dream come true!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've made it a routine to grab one and chow\x01",
            "it down with a nice, steamy espresso!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F19")

    label("loc_5ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5C2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BA9")

    ChrTalk(
        0xFE,
        (
            "Oh, yeah, did you hear that the Bracer Guild\x01",
            "picked up a couple of new members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Most of the bracers I know are amazing, so\x01",
            "I'm curious to see how good these guys are.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5C26")

    label("loc_5BA9")


    ChrTalk(
        0xFE,
        (
            "Supposedly the Bracer Guild had a couple of\x01",
            "members transfer over to our branch.\x01",
            "I wonder what kind of people they are?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C26")

    Jump("loc_5F19")

    label("loc_5C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5CF5")

    ChrTalk(
        0xFE,
        (
            "The Crossbell Times has a spunky gal putting in\x01",
            "good work as a reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's been reporting on one major event\x01",
            "after another, so she's starting to become\x01",
            "the talk of the town.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F19")

    label("loc_5CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5F19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E3F")

    ChrTalk(
        0xFE,
        "So the bracers saved some kids?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Leave it to the guild to perform\x01",
            "an amazing feat like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This really goes to show how sloppy our\x01",
            "city's management system is, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we had the appropriate countermeasures set in stone,\x01",
            "this would have never even happened in the first place!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5F19")

    label("loc_5E3F")


    ChrTalk(
        0xFE,
        (
            "Can't go a day without hearing about\x01",
            "some accident or crime in the paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bracers are capable of handling most of the problems\x01",
            "on their own, but I wish the city would develop a\x01",
            "plan to prevent them entirely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F19")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_4AB0 end

    def Function_19_5F21(): pass

    label("Function_19_5F21")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_629B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61AF")

    ChrTalk(
        0x101,
        (
            "#0000FDo you mind if we borrow a minute of your time?\x02\x03",
            "Do you own a cat, by any chance?\x01",
            "We found a stray kitten, and we're\x01",
            "trying to find its owner.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "No, I don't, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can I have the kitty?\x01",
            "I've always wanted to own a cat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, my parents run a store inside\x01",
            "of our house, so I don't think they would\x01",
            "let me keep a kitty inside there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FSorry about that. We've gotta find\x01",
            "this kitten's rightful owner, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aw...I wanted the kitty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What am I saying? Please find the poor\x01",
            "kitty's owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FAnother dead end.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8, 0x1, 0x4)
    Jump("loc_6296")

    label("loc_61AF")


    ChrTalk(
        0xFE,
        "I wish we had any kind of information to work with.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, I think I remember Ryu and Anri talking\x01",
            "about a kitty they found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's exciting for them, I guess.\x01",
            "I wish I was able to have my own kitty, too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6296")

    Jump("loc_66A8")

    label("loc_629B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_62A9")
    Jump("loc_66A8")

    label("loc_62A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6390")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6353")
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "Stoooop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ryu, you're too fast!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FUh, running with your eyes closed\x01",
            "isn't the brightest idea, is it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_638B")

    label("loc_6353")


    ChrTalk(
        0xFE,
        (
            "That's incredible, Ryu! How\x01",
            "do you run that fast?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_638B")

    Jump("loc_66A8")

    label("loc_6390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_63A1")
    Call(0, 15)
    Jump("loc_66A8")

    label("loc_63A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6405")

    ChrTalk(
        0xFE,
        (
            "Ryu invited me to play with him\x01",
            "and Anri.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "H-Hooray!\x02",
    )

    CloseMessageWindow()
    Jump("loc_66A8")

    label("loc_6405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6413")
    Jump("loc_66A8")

    label("loc_6413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6421")
    Jump("loc_66A8")

    label("loc_6421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_642F")
    Jump("loc_66A8")

    label("loc_642F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_643D")
    Jump("loc_66A8")

    label("loc_643D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_644B")
    Jump("loc_66A8")

    label("loc_644B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6459")
    Jump("loc_66A8")

    label("loc_6459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_64CD")

    ChrTalk(
        0xFE,
        (
            "Ryu and Anri are always\x01",
            "so full of energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if they'd let me play\x01",
            "with them, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66A8")

    label("loc_64CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6586")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_654B")

    ChrTalk(
        0xFE,
        (
            "Ryu and Anri haven't been coming to\x01",
            "play with me lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if everything is okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6581")

    label("loc_654B")


    ChrTalk(
        0xFE,
        "I wanted to help them look after a kitty, too...\x02",
    )

    CloseMessageWindow()

    label("loc_6581")

    Jump("loc_66A8")

    label("loc_6586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6691")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_664F")

    ChrTalk(
        0xFE,
        (
            "Ryu and Anri haven't been around\x01",
            "here lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They told me that they were on\x01",
            "a super secret mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That sounds fun... I wish I could be\x01",
            "their friend, too...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_668C")

    label("loc_664F")


    ChrTalk(
        0xFE,
        (
            "*sniffle*\x01",
            "They wouldn't tell me what they were doing...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_668C")

    Jump("loc_66A8")

    label("loc_6691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_669F")
    Jump("loc_66A8")

    label("loc_669F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_66A8")

    label("loc_66A8")

    TalkEnd(0xFE)
    Return()

    # Function_19_5F21 end

    def Function_20_66AC(): pass

    label("Function_20_66AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6800")

    ChrTalk(
        0xFE,
        (
            "I forced Oscar to try a bite of my masterpiece\x01",
            "of a baked delicacy, my magnum opus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He took one bite and said, 'Wow, this is delicious!'\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I swear... No sane person just goes and\x01",
            "compliments their rival's creations like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oscar thinks he can trick me so easily?\x01",
            "Think again, buddy!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67F8")
    SetScenarioFlags(0xED, 1)

    label("loc_67F8")

    SetScenarioFlags(0x0, 7)
    Jump("loc_68DC")

    label("loc_6800")


    ChrTalk(
        0xFE,
        (
            "If he really thought the bread was that great,\x01",
            "his reaction would have been priceless...\x01",
            "Yep, he must have tried to fool me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn that Oscar! I'll keep training, baking,\x01",
            "and one day, I'll leave him speechless!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68DC")

    TalkEnd(0xFE)
    Return()

    # Function_20_66AC end

    def Function_21_68E0(): pass

    label("Function_21_68E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69B4")

    ChrTalk(
        0xFE,
        (
            "I finally bit the bullet and purchased\x01",
            "my very own orbal car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll treat myself to my first\x01",
            "little joyride in this baby tomorrow.\x01",
            "The truth is, I'm shaking with excitement.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6A42")

    label("loc_69B4")


    ChrTalk(
        0xFE,
        (
            "I finally bit the bullet and purchased\x01",
            "my very own orbal car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to enjoy my retirement\x01",
            "to the fullest. You best believe it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A42")

    TalkEnd(0xFE)
    Return()

    # Function_21_68E0 end

    def Function_22_6A46(): pass

    label("Function_22_6A46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6BCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B4E")

    ChrTalk(
        0xFE,
        (
            "Good day, everyone!\x01",
            "Welcome to Tallys' General Store!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What an adorable girl you got with you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey there, would you like to be\x01",
            "friends with our little Momo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1110FYeah, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FAlways the popular one.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6BC7")

    label("loc_6B4E")


    ChrTalk(
        0xFE,
        (
            "Our Momo is quite the reserved girl,\x01",
            "but she has a big heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd be grateful if you could get along with her.\x02",
    )

    CloseMessageWindow()

    label("loc_6BC7")

    Jump("loc_6EFF")

    label("loc_6BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6BDA")
    Jump("loc_6EFF")

    label("loc_6BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6DB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_END)), "loc_6CDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C81")

    ChrTalk(
        0xFE,
        (
            "Pete is on his way over now. He told us that\x01",
            "he handles all of Mr. Grimwood's meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope he manages to hang in there.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6CD7")

    label("loc_6C81")


    ChrTalk(
        0xFE,
        (
            "I'd like for Momo to keep observing so\x01",
            "she can learn the ropes for a bit longer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CD7")

    Jump("loc_6DB2")

    label("loc_6CDC")


    ChrTalk(
        0xFE,
        (
            "Have you heard about those rival gangs that\x01",
            "are always having scuffles downtown?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've only heard rumors about them, but they\x01",
            "sound frightening. I don't want Momo going\x01",
            "anywhere near them. She's too pure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DB2")

    Jump("loc_6EFF")

    label("loc_6DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6EFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E77")

    ChrTalk(
        0xFE,
        (
            "Good morning to you all.\x01",
            "Welcome to Tallys' General Store!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tallys' is in its tenth year of doing business.\x01",
            "Thank you for your continued support, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6EFF")

    label("loc_6E77")


    ChrTalk(
        0xFE,
        (
            "It's all thanks to the support of the people in this\x01",
            "neighborhood that we've been able to stay in\x01",
            "business for as long as we have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EFF")

    TalkEnd(0xFE)
    Return()

    # Function_22_6A46 end

    def Function_23_6F03(): pass

    label("Function_23_6F03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_706D")

    ChrTalk(
        0x10,
        "#1200FGrrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHey, Tio, what's he saying?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F'The sun's warmth feels pleasant on my back.'\x01",
            "He seems to be enjoying himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FMan, what's this mutt's deal? I thought he'd\x01",
            "be pissed we're makin' him chase after some\x01",
            "kiddos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FIt looks like Zeit's way of doing things\x01",
            "is to take it slow and easy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 3)
    Jump("loc_7084")

    label("loc_706D")


    ChrTalk(
        0x10,
        "#1200FGrrrrowl...\x02",
    )

    CloseMessageWindow()

    label("loc_7084")

    TalkEnd(0xFE)
    Return()

    # Function_23_6F03 end

    def Function_24_7088(): pass

    label("Function_24_7088")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    OP_4B(0xF, 0xFF)
    SetChrFlags(0xF, 0x80)
    OP_68(16500, 6000, 15500, 0)
    MoveCamera(66, 2, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, 10500, 3000, 14800, 90)
    SetChrPos(0x102, 10500, 3000, 16200, 90)
    SetChrPos(0x103, 9300, 3000, 14800, 90)
    SetChrPos(0x104, 9300, 3000, 16200, 90)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, 21000, 3000, 15500, 270)
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00600.itp")
    OP_68(14500, 6000, 15500, 6000)
    MoveCamera(56, 2, 0, 6000)
    SetCameraDistance(18500, 6000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#0400806V#0100FGrimwood Law Office...\x02\x03",
            "#0400807VI believe this is the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400808V#5P#0000FYeah. I've seen the lawyer who runs it in\x01",
            "the neighborhood before.\x02\x03",
            "#0400809VI had no idea he was well known, though...\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x3)
    Sleep(300)

    NpcTalk(
        0x11,
        "Man's Voice",
        (
            "#0400810V#1P#2SThanks for your time, Ian. I'm sure\x01",
            "we'll speak again in the near future.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    NpcTalk(
        0x11,
        "Man's Voice",
        (
            "#0400811V#11P#2SOf course. I'll be here any time you need me.\x02\x03",
            "#0400812V#2SShouldn't your division try to do something\x01",
            "to solve the situation, though?\x02\x03",
            "#0400813V#2SThink about the impact that this will have on\x01",
            "the citizens.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x11,
        "Man's Voice",
        (
            "#0400814V#1P#2SKissing the asses of the populace isn't my job,\x01",
            "nor do I intend on it ever being.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1553, 255, 90, 0)
    Sleep(1000)
    Fade(500)
    OP_68(13070, 3700, 15860, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23790, 0)
    OP_0D()

    def lambda_753F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_753F)

    def lambda_7550():
        OP_95(0xFE, 14000, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7550)
    WaitChrThread(0x11, 2)
    Sleep(800)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    WaitChrThread(0x11, 1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sound(1554, 255, 100, 0)
    SetChrName("Bespectacled Man")

    AnonymousTalk(
        0xFF,
        (
            "#0400815VYou four are...\x02\x03",
            "#0400816V...\x02",
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
        "#0400817V#6P#0005FCome again...?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1555, 255, 100, 0)
    Sleep(500)

    NpcTalk(
        0x11,
        "Bespectacled Man",
        (
            "#0400818V#0604F#11PThat's right.\x02\x03",
            "#0400819V#0602FYou're those pups that Sergei decided\x01",
            "to adopt.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0400820V#6P#0011FHuh?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0400821V#6P#0001FHold on. That badge... You work for the\x01",
            "CPD, too?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1556, 255, 100, 0)
    Sleep(500)

    NpcTalk(
        0x11,
        "Bespectacled Man",
        (
            "#0400822V#0603F#11PWho I am isn't important to you.\x02\x03",
            "#0400823V#0601FI imagine you're here to speak with\x01",
            "Ian about something...\x02\x03",
            "#0400824VA word of advice: Try not to waste\x01",
            "his time.\x02\x03",
            "#0400825VUnlike you useless rookies, he's a\x01",
            "busy man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400826V#6P#0013FWh-What?!\x02",
    )

    CloseMessageWindow()

    def lambda_7909():

        label("loc_7909")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_7909")

    QueueWorkItem2(0x101, 2, lambda_7909)

    def lambda_791B():

        label("loc_791B")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_791B")

    QueueWorkItem2(0x102, 2, lambda_791B)

    def lambda_792D():

        label("loc_792D")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_792D")

    QueueWorkItem2(0x103, 2, lambda_792D)

    def lambda_793F():

        label("loc_793F")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_793F")

    QueueWorkItem2(0x104, 2, lambda_793F)

    def lambda_7951():
        OP_95(0xFE, 2100, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7951)
    Sleep(600)
    OP_68(11850, 3700, 16440, 3000)

    def lambda_797F():
        OP_96(0xFE, 0x2904, 0xBB8, 0x3840, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_797F)
    Sleep(400)

    def lambda_799C():
        OP_96(0xFE, 0x2454, 0xBB8, 0x3840, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_799C)
    Sleep(2500)

    def lambda_79B9():
        OP_96(0xFE, 0x2904, 0xBB8, 0x39D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_79B9)
    Sleep(400)

    def lambda_79D6():
        OP_96(0xFE, 0x2454, 0xBB8, 0x39D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_79D6)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    ClearChrFlags(0x11, 0x8000)
    SetChrFlags(0x11, 0x80)
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
        0x101,
        "#0400827V#11P#0007FWhat's his problem?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400828V#11P#0101FHe looked like a detective from one of\x01",
            "the investigative divisions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400829V#12P#0211FHis ego is overbearing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400830V#0303F#5PGlasses definitely ain't a greenhorn,\x01",
            "that's for sure.\x02\x03",
            "#0400831V#0301FYou can tell by the weapon strapped\x01",
            "to his left hip.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#0400832V#11P#0005FS-Seriously? I didn't even notice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400833V#11P#0105FYou were able to notice it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400834V#12P#0203FI detected it with my sensors.\x02\x03",
            "#0400835V#0200FA specialized military-grade handgun...\x01",
            "Or so it seemed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400836V#0300F#5PYeah, sounds 'bout right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400837V#11P#0000FWow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400838V#11P#0100FYou two are amazing.\x02",
    )

    CloseMessageWindow()

    def lambda_7D60():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7D60)
    Sleep(50)

    def lambda_7D70():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7D70)
    Sleep(300)

    ChrTalk(
        0x104,
        "#0400839V#0304F#6PHaha, it was nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400840V#6P#0200FMore importantly, should we not\x01",
            "head inside and greet the lawyer?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#0400841V#11P#0005FOh, right.\x02",
    )

    CloseMessageWindow()

    def lambda_7E30():
        OP_93(0xFE, 0x59, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7E30)
    Sleep(100)

    def lambda_7E40():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7E40)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0400842V#6P#0001FI'd feel kind of bad bothering him if he's as\x01",
            "busy as that man said, but let's go in and\x01",
            "introduce ourselves.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x0, 10200, 3000, 15500, 90)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0x42, 7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_24_7088 end

    def Function_25_7F09(): pass

    label("Function_25_7F09")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(17100, 4000, 15500, 0)
    MoveCamera(57, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    OP_4B(0xF, 0xFF)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0x101, 20500, 3000, 15500, 270)
    SetChrPos(0x102, 20500, 3000, 15500, 270)
    SetChrPos(0x103, 20500, 3000, 15500, 270)
    SetChrPos(0x104, 20500, 3000, 15500, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8000")
    LoadChrToIndex("chr/ch07000.itc", 0x1E)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    SetChrPos(0x19, 8000, 3300, 21000, 180)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_8000")

    FadeToBright(1000, 0)
    Sleep(500)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x3)
    OP_68(11900, 4000, 15500, 5500)
    MoveCamera(45, 27, 0, 5500)
    SetCameraDistance(20500, 5500)

    def lambda_804B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_804B)

    def lambda_805C():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_805C)
    Sleep(700)

    def lambda_8079():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8079)

    def lambda_808A():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_808A)
    Sleep(700)

    def lambda_80A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_80A7)

    def lambda_80B8():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_80B8)
    Sleep(700)

    def lambda_80D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_80D5)

    def lambda_80E6():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_80E6)
    WaitChrThread(0x101, 1)

    def lambda_8104():
        OP_95(0xFE, 11200, 3000, 14800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8104)
    WaitChrThread(0x102, 1)

    def lambda_8122():
        OP_95(0xFE, 11200, 3000, 16200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8122)
    WaitChrThread(0x103, 1)

    def lambda_8140():
        OP_95(0xFE, 12600, 3000, 14800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8140)
    WaitChrThread(0x104, 1)

    def lambda_815E():
        OP_95(0xFE, 12600, 3000, 16200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_815E)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x101, 1)

    def lambda_818E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_818E)
    WaitChrThread(0x102, 1)

    def lambda_819F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_819F)
    WaitChrThread(0x103, 1)

    def lambda_81B0():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_81B0)
    WaitChrThread(0x104, 1)

    def lambda_81C1():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_81C1)
    WaitChrThread(0x104, 2)
    OP_79(0x3)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#0400969V#0100FSo, what's the next course of action?\x02\x03",
            "#0400970VShould we go back and sort through\x01",
            "all the information we've gathered?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400971V#6P#0008FGood idea.\x02\x03",
            "#0400972V#0003FBut before we do that, now's the time to\x01",
            "wrap up any unfinished business we still\x01",
            "have to take care of.\x02\x03",
            "#0400973V#0001FBesides, if what I'm thinking is the truth\x01",
            "behind all these incidents... Let's just say\x01",
            "we're in for a bumpy ride, all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400974V#5P#0309FI appreciate the modesty, but your face is\x01",
            "givin' away your confidence.\x02\x03",
            "#0400975V#0300FAnyhow, let's head back to the SSS buildin'\x01",
            "once we've crossed off everything on our\x01",
            "bucket list. Sound good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400976V#0202FYes, it does. Let us make haste.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9333")
    OP_68(11050, 4000, 15990, 3000)
    MoveCamera(45, 27, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(20500, 3000)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    Sleep(500)

    def lambda_84EF():
        OP_95(0xFE, 8000, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_84EF)

    def lambda_8509():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_8509)
    Sleep(1000)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x2)
    Sleep(500)
    WaitChrThread(0x19, 1)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_854B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_854B)
    Sleep(1000)

    NpcTalk(
        0x19,
        "Young Man",
        "Huh? Well, if it ain't Lloyd.\x02",
    )

    CloseMessageWindow()

    def lambda_8588():
        OP_95(0xFE, 9500, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8588)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_85EA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_85EA)
    Sleep(60)

    def lambda_85FA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_85FA)
    Sleep(60)

    def lambda_860A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_860A)
    Sleep(60)

    def lambda_861A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_861A)
    Sleep(60)
    WaitChrThread(0x19, 1)

    ChrTalk(
        0x101,
        "#0005F#11PWait, Oscar?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "No way! It's been too long, man.\x01",
            "When did you get back to Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "You haven't shown your face once during these\x01",
            "past three years! I was worried about ya!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004F#11PSorry about that. I was planning\x01",
            "on coming to see you a bit earlier.\x02\x03",
            "#0002FWork ended up getting busy faster\x01",
            "than I was expecting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Right, it DOES look like you're working right now...\x01",
            "Er, are you in the middle of an investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F#11PHuh? Yeah, we are.\x02\x03",
            "#0006FHow'd you manage to figure that out?\x01",
            "Man, three years and I still can't tell\x01",
            "whether you're sharp or oblivious, Oscar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "It must have been that serious look\x01",
            "on your face that tipped me off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Oh, right. Here, take this. It's on me.\x01",
            "To our reunion, Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_891C():
        OP_98(0xFE, 0x1F4, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_891C)
    WaitChrThread(0x19, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    AddItemNumber(0x2, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B38")
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Wrote down the recipe for\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x1B5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " in the notebook.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xD)

    def lambda_89FD():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_89FD)
    WaitChrThread(0x19, 1)

    ChrTalk(
        0x19,
        "You were always decent at cooking, weren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "You'll have lots of space to jot down recipes\x01",
            "that you and your friends can try together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "It only has a single recipe written in it, though.\x01",
            "It's a simple sandwich that I like to make for myself.\x01",
            "Well, knock yourself out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BFD")

    label("loc_8B38")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    def lambda_8B50():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8B50)
    WaitChrThread(0x19, 1)

    ChrTalk(
        0x19,
        "You were always decent at cooking, weren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "You'll have lots of space to jot down recipes that\x01",
            "you and your friends can try together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BFD")


    ChrTalk(
        0x101,
        (
            "#0002F#11PWow, this'll be pretty handy to have...\x02\x03",
            "#0009FThanks, Oscar. I appreciate it.\x01",
            "Time to break out the oven mitts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Anyway, I'll catch you guys later.\x02",
    )

    CloseMessageWindow()

    def lambda_8CAA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8CAA)
    WaitChrThread(0x19, 1)
    Sleep(300)

    ChrTalk(
        0x19,
        (
            "I actually started working as a baker over\x01",
            "at Morges Bakery. Stop by if you're ever\x01",
            "feeling hungry for a snack!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004F#11PThat's right. I remember you writing that\x01",
            "in one of your letters.\x02\x03",
            "#0000FAll right. We'll drop by when we find the time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8DBB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8DBB)
    WaitChrThread(0x19, 1)

    ChrTalk(
        0x19,
        "Awesome. Don't go too crazy with your job, okay?\x02",
    )

    CloseMessageWindow()

    def lambda_8E02():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8E02)
    WaitChrThread(0x19, 1)

    def lambda_8E13():
        OP_95(0xFE, 1000, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8E13)
    Sleep(3000)

    ChrTalk(
        0x103,
        "#0202F#11PA friend of yours, I presume?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004F#11PYeah. That's Oscar, one of my\x01",
            "closest childhood friends.\x02\x03",
            "#0002FWe kept in touch via letters, but man,\x01",
            "that guy really hasn't changed one bit.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8EFB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8EFB)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#0100FWhy don't you spend some more time with\x01",
            "him, Lloyd? We'd be fine with it.\x02\x03",
            "I'm sure you two have some catching up to do.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8F90():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F90)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#0006FNo, it's okay. I'm still busy trying to digest\x01",
            "all the information Ian told us.\x02\x03",
            "#0000FBut I suppose it wouldn't hurt to drop by\x01",
            "the bakery every now and then while doing\x01",
            "our rounds.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9063():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9063)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        (
            "#0304F#5PSounds tasty to me.\x02\x03",
            "#0302FAnyway, once we knock off the rest of these chores,\x01",
            "let's skedaddle on back to the SSS building.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(150)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    OP_49()
    OP_D5(0x1E)
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you talk to people or examine certain things,\x01",
            "you can sometimes learn cooking recipes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Recipes are recorded in the Recipe Notebook.\x01",
            "If you use the Recipe Notebook, you can prepare\x01",
            "dishes with various effects at any time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When cooking recipes, there is a set chance to\x01",
            "get a 'supreme' or 'peculiar' variant of each dish.\x01",
            "(Cooking can sometimes result in a 'failure,' too.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Most ingredients used in cooking are sold\x01",
            "at the general stores and various shops.\x01",
            "Monsters may drop them, as well.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x46, 1)
    SetScenarioFlags(0x4A, 7)

    label("loc_9333")

    SetChrPos(0x0, 11500, 3000, 15500, 270)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetMapObjFlags(0x3, 0x10)
    SetScenarioFlags(0x43, 0)
    OP_29(0x3E, 0x1, 0x7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9375")
    OP_1B(0x0, 0x0, 0x1E)
    OP_1B(0x1, 0x0, 0x1F)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_9375")

    EventEnd(0x5)
    Return()

    # Function_25_7F09 end

    def Function_26_9378(): pass

    label("Function_26_9378")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02702.itc", 0x1E)
    LoadChrToIndex("chr/ch05900.itc", 0x1F)
    LoadChrToIndex("chr/ch07000.itc", 0x20)
    LoadChrToIndex("chr/ch24500.itc", 0x21)
    LoadChrToIndex("chr/ch20700.itc", 0x22)
    LoadChrToIndex("chr/ch25000.itc", 0x23)
    OP_68(6600, 1400, -11300, 0)
    MoveCamera(27, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 11700, 0, -9200, 270)
    SetChrPos(0x102, 11900, 0, -10200, 270)
    SetChrPos(0x103, 13300, 0, -10200, 270)
    SetChrPos(0x104, 13100, 0, -9200, 270)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, 8200, 0, -9400, 270)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 6800, 0, -9900, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 6600, 0, -8800, 125)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 10510, 0, -7890, 243)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 8940, 0, -4080, 210)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 7260, 0, -5600, 157)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 8900, 0, -6230, 217)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 4310, 0, -7050, 127)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 12470, 0, -6780, 240)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 5760, 0, -4940, 178)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xC, 0x4)
    OP_78(0xC, 0x13)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x13, 1500, 0, -13500, 0)
    OP_D3(0x13, 0x0, 0x29810, 0x4E20, 0x0)
    OP_70(0xC, 0x0)
    SetMapObjFrame(0xFF, "br02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "br00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "br01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "br_mul", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "◆No input.\x01",
            "West Street sepia flashback scene.\x01",
            "Zeit saves the kids from an accident.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    SetScenarioFlags(0x5C, 7)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_9378 end

    def Function_27_96AC(): pass

    label("Function_27_96AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(17100, 4000, 15500, 0)
    MoveCamera(57, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 20500, 3000, 15500, 270)
    SetChrPos(0x102, 20500, 3000, 15500, 270)
    SetChrPos(0x103, 20500, 3000, 15500, 270)
    SetChrPos(0x104, 20500, 3000, 15500, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x3)
    OP_68(11900, 4000, 15500, 5500)
    MoveCamera(45, 27, 0, 5500)
    SetCameraDistance(20500, 5500)

    def lambda_97A5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_97A5)

    def lambda_97B6():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_97B6)
    Sleep(700)

    def lambda_97D3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_97D3)

    def lambda_97E4():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_97E4)
    Sleep(700)

    def lambda_9801():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9801)

    def lambda_9812():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9812)
    Sleep(700)

    def lambda_982F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_982F)

    def lambda_9840():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9840)
    WaitChrThread(0x101, 1)

    def lambda_985E():
        OP_95(0xFE, 11200, 3000, 14800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_985E)
    WaitChrThread(0x102, 1)

    def lambda_987C():
        OP_95(0xFE, 11200, 3000, 16200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_987C)
    WaitChrThread(0x103, 1)

    def lambda_989A():
        OP_95(0xFE, 12600, 3000, 14800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_989A)
    WaitChrThread(0x104, 1)

    def lambda_98B8():
        OP_95(0xFE, 12600, 3000, 16200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_98B8)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x101, 1)

    def lambda_98E8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_98E8)
    WaitChrThread(0x102, 1)

    def lambda_98F9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_98F9)
    WaitChrThread(0x103, 1)

    def lambda_990A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_990A)
    WaitChrThread(0x104, 1)

    def lambda_991B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_991B)
    WaitChrThread(0x104, 2)
    OP_79(0x3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#2100955V#6P#0003FAll right. Let's make our way to\x01",
            "Heiyue Trading, Ltd.\x02\x03",
            "#2100956V#0000FI think they're somewhere by the pier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100957V#0203FCorrect. Our destination should be in the\x01",
            "northeast corner of the Harbor District.\x02\x03",
            "#2100958V#0200FThey are apparently located right by the river.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100959V#5P#0300FOh, we talkin' about that red, Eastern\x01",
            "lookin' building?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100960V#0106FThe IBC and Crossbell Times buildings are\x01",
            "right in that area, so you would think that\x01",
            "they'd be an upstanding establishment...\x02\x03",
            "#2100961V#0101FI suppose it's no matter.\x01",
            "Let's try paying them a visit.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 11500, 3000, 15500, 270)
    SetMapObjFlags(0x3, 0x10)
    SetScenarioFlags(0x81, 1)
    OP_29(0x42, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_27_96AC end

    def Function_28_9BA9(): pass

    label("Function_28_9BA9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(8000, 5000, 15590, 0)
    MoveCamera(37, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15560, 0)
    OP_68(16710, 5000, 15520, 4000)
    MoveCamera(70, 18, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(18910, 4000)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-14910, 2400, -11820, 0)
    MoveCamera(29, 26, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(7830, 0)
    OP_68(-9970, 3700, 9790, 5000)
    MoveCamera(23, 15, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(16270, 5000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(10660, 3700, 2040, 0)
    MoveCamera(59, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18420, 0)
    OP_68(6220, 1660, 5470, 5000)
    MoveCamera(45, 37, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(44100, 5000)
    PlaceName2(340, 200, "c_plac03", 0x0, 1000)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FE3")

    AnonymousTalk(
        0x103,
        "#0205FI believe this area is known as West Street.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#0004FYep. It's one of the larger residential areas\x01",
            "in the city. Just look at all of the apartments.\x02\x03",
            "#0000FI'm actually familiar with most of the people\x01",
            "in the area... Is it okay if I take some time to\x01",
            "catch up with them when we get the chance?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#0300FSo I take it you grew up around these parts?\x02\x03",
            "#0304FHell, we're already here. May as well do some\x01",
            "meetin' and greetin' before we head out!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#0102FI'm sure you've been longing to see your friends\x01",
            "and family. We can accompany you, too.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#0002FThanks, guys.\x02\x03",
            "#0004F(I should swing by Bellheim to visit Auntie.\x01",
            "I can probably find Oscar working\x01",
            "at Morges, too.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_9FE3")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "West Street is a residential area in\x01",
            "the western part of the city.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The streets are lined with homes and apartments,\x01",
            "along with the occasional shop.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Our main protagonist, Lloyd, was born\x01",
            "and raised in this district.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_END)), "loc_A209")
    FadeToBright(300, 0)
    OP_0D()

    AnonymousTalk(
        0x101,
        (
            "#0005F(That reminds me. I still need to pay Auntie\x01",
            "and Uncle a visit. Oscar, too, while I'm at it.)\x02\x03",
            "#0008F(They should still live at Bellheim, and Oscar\x01",
            "is probably busy working at the bakery.)\x02\x03",
            "#0000F(I'll pay them a visit, if I can find the time.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_A209")

    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A271")
    OP_68(110, 5000, 22760, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)

    label("loc_A271")

    SetScenarioFlags(0x44, 6)
    EventEnd(0x5)
    Return()

    # Function_28_9BA9 end

    def Function_29_A277(): pass

    label("Function_29_A277")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A333")
    EventBegin(0x1)
    Sound(823, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0000FWhoops... We have the kitten with us.\x02\x03",
            "It's probably not the best idea to leave\x01",
            "the city with her in tow.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_A333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A433")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3E2")

    ChrTalk(
        0x101,
        (
            "#0000FThis is the city's west exit.\x02\x03",
            "We have no reason to leave the city at the moment.\x01",
            "Let's knock out our work inside the city first.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A41D")

    label("loc_A3E2")

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

    label("loc_A41D")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_A433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A547")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4F4")

    ChrTalk(
        0x101,
        (
            "#0000FThis is the city's west exit. Just past here\x01",
            "is West Crossbell Highway.\x02\x03",
            "There shouldn't be anything there pertaining\x01",
            "to our current investigation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A531")

    label("loc_A4F4")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "We can venture onto the highway some other time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A531")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_A547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A63F")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5ED")

    ChrTalk(
        0x101,
        (
            "#0000FWe should avoid the west gate for today.\x02\x03",
            "KeA's safety is our top priority, and we can't\x01",
            "do anything to jeopardize that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A629")

    label("loc_A5ED")

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

    label("loc_A629")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_A63F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A73E")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6ED")

    ChrTalk(
        0x101,
        (
            "#0003FThis is the city's west exit.\x02\x03",
            "We've got the Heiyue incident on our hands, still.\x01",
            "There's no reason to leave the city right now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A728")

    label("loc_A6ED")

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

    label("loc_A728")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_A73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A80A")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7A9")

    ChrTalk(
        0x101,
        (
            "#0000FThis is the city's west exit.\x01",
            "...We've gotta hurry to Ursula Road!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A7F4")

    label("loc_A7A9")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's no reason to leave via the\x01",
            "West Crossbell Highway now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A7F4")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_A80A")

    Return()

    # Function_29_A277 end

    def Function_30_A80B(): pass

    label("Function_30_A80B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8C8")
    EventBegin(0x1)
    Sound(823, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0000FWhoops... We have the kitten with us.\x02\x03",
            "It's probably not the best idea to wander\x01",
            "the city with her in tow.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 24460, 0, -8180, 270)
    EventEnd(0x4)
    Return()

    label("loc_A8C8")

    EventBegin(0x1)
    Call(0, 33)
    Sleep(50)
    SetChrPos(0x0, 24460, 0, -8180, 270)
    EventEnd(0x4)
    Return()

    # Function_30_A80B end

    def Function_31_A8E4(): pass

    label("Function_31_A8E4")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 33)
    SetChrPos(0x0, 110, 3000, 22760, 180)
    EventEnd(0x4)
    Return()

    # Function_31_A8E4 end

    def Function_32_A900(): pass

    label("Function_32_A900")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 33)
    SetChrPos(0x0, 36500, -4000, -19000, 270)
    EventEnd(0x4)
    Return()

    # Function_32_A900 end

    def Function_33_A91C(): pass

    label("Function_33_A91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB45")

    ChrTalk(
        0x101,
        "#0000FOh, that's right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FHmm, what's up, man?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI have a childhood friend name Oscar who actually\x01",
            "lives on this street. I kinda promised him that\x01",
            "I'd drop by when I got back to Crossbell...\x02\x03",
            "Would you guys be okay with me stopping\x01",
            "by to say hello real quick?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FOf course, that shouldn't be\x01",
            "an issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FIs he in the area?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWell, I imagine he's working at\x01",
            "Morges Bakery right about now.\x02\x03",
            "I remember him mentioning that it faces\x01",
            "the main road, but I'm not sure on\x01",
            "its exact location.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_ABBE")

    label("loc_AB45")


    ChrTalk(
        0x101,
        (
            "#0000FOscar should be working at Morges\x01",
            "Bakery right about now.\x02\x03",
            "Man, it's been too long. I should pay him a visit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABBE")

    Return()

    # Function_33_A91C end

    SaveToFile()

Try(main)
