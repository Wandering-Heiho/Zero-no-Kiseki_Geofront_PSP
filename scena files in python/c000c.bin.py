from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c000c.bin",                # FileName
        "c000c",                    # MapName
        "c000c",                    # Location
        0x0002,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 2, 0, 7, 0, 8],
    )

    BuildStringList((
        "c000c",                  # 0
        "Billy",                  # 1
        "Lyd",                    # 2
        "Tourist",                # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Tourist",                # 10
        "Tourist",                # 11
        "Girl",                   # 12
        "Tourist",                # 13
        "Tourist",                # 14
        "Tourist",                # 15
        "Tourist",                # 16
        "Central Square",         # 17
        "West Street",            # 18
        "Administrative District",# 19
        "Residential District",   # 20
        "Entertainment District", # 21
        "East Street",            # 22
        "Downtown District",      # 23
        "Harbor District",        # 24
        "IBC",                    # 25
        "Station Street",         # 26
        "Back Alley",             # 27
        "Ursula Road",            # 28
        "East Crossbell Highway", # 29
        "West Crossbell Highway", # 30
        "Mainz Mountain Path",    # 31
    ))

    AddCharChip((
        "chr/ch23600.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch33100.itc",                   # 02
        "chr/ch34300.itc",                   # 03
        "chr/ch32400.itc",                   # 04
        "chr/ch33000.itc",                   # 05
        "chr/ch21200.itc",                   # 06
        "chr/ch33000.itc",                   # 07
        "chr/ch32200.itc",                   # 08
        "chr/ch23900.itc",                   # 09
        "chr/ch21300.itc",                   # 0A
        "chr/ch20200.itc",                   # 0B
        "chr/ch33100.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
    ))

    DeclNpc(4000,    0,       -7000,   270,  257,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-1830,   0,       13000,   180,  257,  0x0, 0,   1,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(4420,    0,       2450,    276,  385,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(750,     0,       -7000,   0,    385,  0x0, 0,   3,   0,   0,   2,   0,   12,  255,  0)
    DeclNpc(3809,    0,       509,     136,  385,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(5489,    0,       409,     267,  385,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4590,    0,       3660,    45,   385,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(6139,    0,       2970,    308,  385,  0x0, 0,   0,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(750,     0,       3000,    0,    385,  0x0, 0,   6,   0,   0,   3,   0,   17,  255,  0)
    DeclNpc(-2970,   0,       10220,   269,  385,  0x0, 0,   7,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(3450,    0,       -1350,   270,  385,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(3450,    0,       -2150,   0,    385,  0x0, 0,   9,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(750,     0,       -3000,   0,    385,  0x0, 0,   10,  0,   0,   4,   0,   19,  255,  0)
    DeclNpc(4800,    0,       3000,    180,  385,  0x0, 0,   11,  0,   0,   5,   0,   20,  255,  0)
    DeclNpc(3829,    0,       1169,    270,  385,  0x0, 0,   6,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(750,     0,       1000,    180,  385,  0x0, 0,   12,  0,   0,   6,   0,   24,  255,  0)

    DeclEvent(0x0000, 0, 34,  8.5,                   -2.0,                  -0.5,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -4.25,                 0.5,                   0.10000000149011612,   1.0])

    DeclActor(-22300,  -5000,   20700,   2000,    -22300,  -4000,   20700,   0x007C, 0,  26, 0x0000)

    PlaceName(-9.25, 0.0, 67.0, 0x0000, 0x0000, "Central Square")
    PlaceName(-75.0, 0.0, 71.5, 0x0000, 0x0000, "West Street")
    PlaceName(17.75, 0.0, 156.0, 0x0000, 0x0000, "Administrative District")
    PlaceName(-136.0, 0.0, 146.0, 0x0000, 0x0000, "Residential District")
    PlaceName(-63.0, 0.0, 138.0, 0x0000, 0x0000, "Entertainment District")
    PlaceName(72.0, 0.0, 44.0, 0x0000, 0x0000, "East Street")
    PlaceName(107.5, 0.0, -11.0, 0x0000, 0x0000, "Downtown District")
    PlaceName(100.0, 0.0, 110.0, 0x0000, 0x0000, "Harbor District")
    PlaceName(74.0, 0.0, 204.0, 0x0000, 0x0000, "IBC")
    PlaceName(2.0, 0.0, -2.0, 0x0000, 0x0000, "Station Street")
    PlaceName(-45.0, 0.0, 102.0, 0x0000, 0x0000, "Back Alley")
    PlaceName(-1.0, 0.0, -33.0, 0x0000, 0x0000, "Ursula Road")
    PlaceName(126.0, 0.0, 58.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-126.0, 0.0, 70.0, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-120.0, 0.0, 170.0, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-31.25, 0.0, 53.0, 0x0000, 0x0051, "")
    PlaceName(22.5, 0.0, 79.0, 0x0000, 0x0054, "")
    PlaceName(-6.75, 0.0, 45.0, 0x0000, 0x0057, "")
    PlaceName(-32.0, 0.0, 82.0, 0x0000, 0x0053, "")
    PlaceName(-11.5, 0.0, 106.0, 0x0000, 0x0053, "")
    PlaceName(-62.25, 0.0, 77.0, 0x0000, 0x0053, "")
    PlaceName(-72.0, 0.0, 98.0, 0x0000, 0x0053, "")
    PlaceName(-48.0, 0.0, 130.0, 0x0000, 0x0052, "")
    PlaceName(-43.25, 0.0, 117.0, 0x0000, 0x0053, "")
    PlaceName(-34.5, 0.0, 108.5, 0x0000, 0x0053, "")
    PlaceName(-6.0, 0.0, 179.5, 0x0000, 0x0051, "")
    PlaceName(106.0, 0.0, 44.0, 0x0000, 0x0052, "")
    PlaceName(89.0, 0.0, -46.5, 0x0000, 0x0053, "")
    PlaceName(76.0, 0.0, -28.0, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_5E8",          # 00, 0
        "Function_1_6A0",          # 01, 1
        "Function_2_6F3",          # 02, 2
        "Function_3_72C",          # 03, 3
        "Function_4_765",          # 04, 4
        "Function_5_79E",          # 05, 5
        "Function_6_7C9",          # 06, 6
        "Function_7_802",          # 07, 7
        "Function_8_A47",          # 08, 8
        "Function_9_B96",          # 09, 9
        "Function_10_E39",         # 0A, 10
        "Function_11_1805",        # 0B, 11
        "Function_12_187D",        # 0C, 12
        "Function_13_1915",        # 0D, 13
        "Function_14_199C",        # 0E, 14
        "Function_15_1A70",        # 0F, 15
        "Function_16_1AED",        # 10, 16
        "Function_17_1BAA",        # 11, 17
        "Function_18_1C3A",        # 12, 18
        "Function_19_1D0D",        # 13, 19
        "Function_20_1D7D",        # 14, 20
        "Function_21_1E64",        # 15, 21
        "Function_22_1FB6",        # 16, 22
        "Function_23_22E1",        # 17, 23
        "Function_24_2358",        # 18, 24
        "Function_25_2428",        # 19, 25
        "Function_26_2527",        # 1A, 26
        "Function_27_258F",        # 1B, 27
        "Function_28_2951",        # 1C, 28
        "Function_29_30CF",        # 1D, 29
        "Function_30_378E",        # 1E, 30
        "Function_31_4517",        # 1F, 31
        "Function_32_45E5",        # 20, 32
        "Function_33_4682",        # 21, 33
        "Function_34_46F5",        # 22, 34
        "Function_35_48E3",        # 23, 35
        "Function_36_4ACA",        # 24, 36
    ))


    def Function_0_5E8(): pass

    label("Function_0_5E8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_628"),
        (1, "loc_634"),
        (2, "loc_640"),
        (3, "loc_64C"),
        (4, "loc_658"),
        (5, "loc_664"),
        (6, "loc_670"),
        (SWITCH_DEFAULT, "loc_67C"),
    )


    label("loc_628")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_634")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_640")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_64C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_658")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_664")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_670")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_67C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_688")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_69F")

    Return()

    # Function_0_5E8 end

    def Function_1_6A0(): pass

    label("Function_1_6A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F2")
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1830, 0, -9000, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1830, 0, 13000, 2000, 0x0)
    Sleep(300)
    Jump("Function_1_6A0")

    label("loc_6F2")

    Return()

    # Function_1_6A0 end

    def Function_2_6F3(): pass

    label("Function_2_6F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72B")
    OP_95(0xFE, 750, 0, 33000, 1000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 750, 0, -25000, 0)
    Jump("Function_2_6F3")

    label("loc_72B")

    Return()

    # Function_2_6F3 end

    def Function_3_72C(): pass

    label("Function_3_72C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_764")
    OP_95(0xFE, 750, 0, 33000, 1000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 750, 0, -25000, 0)
    Jump("Function_3_72C")

    label("loc_764")

    Return()

    # Function_3_72C end

    def Function_4_765(): pass

    label("Function_4_765")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_79D")
    OP_95(0xFE, 750, 0, 33000, 2000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 750, 0, -25000, 0)
    Jump("Function_4_765")

    label("loc_79D")

    Return()

    # Function_4_765 end

    def Function_5_79E(): pass

    label("Function_5_79E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C8")
    OP_94(0xFE, 0x189C, 0xFA0, 0xCE4, 0x834, 0x3E8)
    Sleep(300)
    Jump("Function_5_79E")

    label("loc_7C8")

    Return()

    # Function_5_79E end

    def Function_6_7C9(): pass

    label("Function_6_7C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_801")
    OP_95(0xFE, 750, 0, 33000, 1000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 750, 0, -25000, 0)
    Jump("Function_6_7C9")

    label("loc_801")

    Return()

    # Function_6_7C9 end

    def Function_7_802(): pass

    label("Function_7_802")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B1")
    SetChrPos(0x0, 0, 0, 21840, 180)
    SetChrPos(0x1, 0, 0, 21840, 180)
    SetChrPos(0x2, 0, 0, 21840, 180)
    SetChrPos(0x3, 0, 0, 21840, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_889")
    SetChrPos(0x4, 0, 0, 21840, 180)
    SetChrPos(0x5, 0, 0, 21840, 180)
    Jump("loc_8A8")

    label("loc_889")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A8")
    SetChrPos(0x4, 0, 0, 21840, 180)

    label("loc_8A8")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B1")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D0")
    Event(0, 27)
    Jump("loc_904")

    label("loc_8D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EB")
    SetMapFlags(0x10000000)
    Event(0, 28)
    Jump("loc_904")

    label("loc_8EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_904")
    SetMapFlags(0x10000000)
    Event(0, 30)

    label("loc_904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_915")
    ClearScenarioFlags(0x5C, 0)
    Jump("loc_924")

    label("loc_915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_924")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 31)

    label("loc_924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_941")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_A24")

    label("loc_941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_97B")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x10)
    OP_93(0x12, 0x0, 0x0)
    SetChrPos(0x13, 2650, 0, -2050, 0)
    Jump("loc_A24")

    label("loc_97B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9B5")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x10)
    OP_93(0x12, 0x0, 0x0)
    SetChrPos(0x13, 2650, 0, -2050, 0)
    SetChrFlags(0x8, 0x80)
    Jump("loc_A24")

    label("loc_9B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9D7")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x13, 0x10)
    Jump("loc_A24")

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_9F9")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xF, 0x10)
    Jump("loc_A24")

    label("loc_9F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A11")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_A24")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A24")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_A24")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A46")
    OP_C7(0x1, 0x1000)

    label("loc_A46")

    Return()

    # Function_7_802 end

    def Function_8_A47(): pass

    label("Function_8_A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A6C")
    Jump("loc_A75")

    label("loc_A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_A75")

    label("loc_A75")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A91")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x0, 0x10)

    label("loc_A91")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA9")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABC")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACF")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_ACF")

    OP_1B(0x3, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE7")
    OP_1B(0x3, 0x0, 0x23)

    label("loc_AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFA")
    OP_1B(0x3, 0x0, 0x23)

    label("loc_AFA")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B12")
    OP_1B(0x0, 0x0, 0x24)

    label("loc_B12")

    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, -4000, 15000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, -4000, -10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_8_A47 end

    def Function_9_B96(): pass

    label("Function_9_B96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_BA7")
    Jump("loc_E35")

    label("loc_BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C52")

    ChrTalk(
        0xFE,
        (
            "I have to make yet another delivery\x01",
            "to Bellguard Gate tomorrow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I always need to deliver 'em\x01",
            "stuff by the truckloads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What a drag...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E35")

    label("loc_C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_CF4")

    ChrTalk(
        0xFE,
        "Phew. Finally got all the packages I needed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crap! It's this late already? I'd better kick it\x01",
            "into high gear, or I won't make it in time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E35")

    label("loc_CF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_DAF")

    ChrTalk(
        0xFE,
        (
            "There are way more tourists coming through\x01",
            "Crossbell than usual, but freight traffic has\x01",
            "stayed about the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sadly, that means my schedule hasn't freed\x01",
            "up any.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E35")

    label("loc_DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_E35")

    ChrTalk(
        0xFE,
        (
            "Whew. The train station's getting pretty\x01",
            "crowded now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be lucky if I can get all the packages\x01",
            "delivered today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E35")

    TalkEnd(0xFE)
    Return()

    # Function_9_B96 end

    def Function_10_E39(): pass

    label("Function_10_E39")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_EEB")

    ChrTalk(
        0xFE,
        (
            "Today's the last day of the adjusted\x01",
            "train schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once I wrap up work, should I try to find\x01",
            "a spot near the bridge to sit and watch\x01",
            "all the trains?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1801")

    label("loc_EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1020")

    ChrTalk(
        0xFE,
        (
            "Did you know that there's a book on\x01",
            "railways at the library?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "AND did you know that I contributed to it?\x01",
            "That's right! My submission took up quite\x01",
            "a few pages of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, my original contribution took up about\x01",
            "300 pages, so it ended up being abridged by\x01",
            "the editor...greatly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1801")

    label("loc_1020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_112E")

    ChrTalk(
        0xFE,
        (
            "You'd be surprised how many people out\x01",
            "there adore the beauty of the railway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That being said, I've yet to find a fellow\x01",
            "Crossbellan who shares my passion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I can't help but wonder if I'll ever\x01",
            "have a friend to talk with about trains.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1801")

    label("loc_112E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1349")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A7")

    ChrTalk(
        0xFE,
        (
            "Once you become a tried-and-true train buff,\x01",
            "the thrill of seeing a train morphs into\x01",
            "something more akin to love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I try to give every train that stops at the\x01",
            "station a girl's name. It helps me admire\x01",
            "their beauty even more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FThe world truly is filled with all\x01",
            "sorts of strange people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(It sure is, Tio. It sure is...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1344")

    label("loc_12A7")


    ChrTalk(
        0xFE,
        (
            "I've actually already given two Transcontinental\x01",
            "Railroad trains their own personal names. Want\x01",
            "to know what they are?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You don't? Well, your loss.\x02",
    )

    CloseMessageWindow()

    label("loc_1344")

    Jump("loc_1801")

    label("loc_1349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_142B")

    ChrTalk(
        0xFE,
        (
            "There's a private freight line running between\x01",
            "Bellguard and Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Members of the Guardian Force and police\x01",
            "department can use it, but only after they\x01",
            "submit an application. Oh, I'm so jealous!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1801")

    label("loc_142B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1605")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156F")

    ChrTalk(
        0xFE,
        (
            "The Zemurian Railroad Corporation is\x01",
            "organizing some kind of stamp rally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, you don't know about it? It's an event\x01",
            "where you travel across the continent and\x01",
            "gather stamps at the designated locations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's the railroad corporation for you,\x01",
            "always pleasing my train-loving heart.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1600")

    label("loc_156F")


    ChrTalk(
        0xFE,
        (
            "I really want to participate in the stamp\x01",
            "rally one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, doesn't playing a game while on\x01",
            "vacation help you appreciate it more?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1600")

    Jump("loc_1801")

    label("loc_1605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1801")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1748")

    ChrTalk(
        0xFE,
        (
            "More and more trains are up and running,\x01",
            "thanks to the increase in tourism.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard people predict that there'll be\x01",
            "more tourists than usual this year, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You know what that means: more trains!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For a train buff like myself, there's no\x01",
            "greater joy in the world than that!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1801")

    label("loc_1748")


    ChrTalk(
        0xFE,
        (
            "If the service frequency increases, I'll get\x01",
            "even more sneak peeks at Zemuria's\x01",
            "beautiful trains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For a train buff like myself, there's no\x01",
            "greater joy in the world than that!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1801")

    TalkEnd(0xFE)
    Return()

    # Function_10_E39 end

    def Function_11_1805(): pass

    label("Function_11_1805")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Excuse me, are you a local?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's no trouble, could you recommend\x01",
            "me some popular sightseeing spots?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1805 end

    def Function_12_187D(): pass

    label("Function_12_187D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "So, the bustling Central Square is\x01",
            "right over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't miss my chance to see it in the\x01",
            "limelight while the festival is going on!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_187D end

    def Function_13_1915(): pass

    label("Function_13_1915")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm not sure if I can handle much\x01",
            "more of this walking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We should have at least hired a\x01",
            "chauffeur to drive us around.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1915 end

    def Function_14_199C(): pass

    label("Function_14_199C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, no. My wife's starting to get cranky\x01",
            "again. Isn't walking around one of the\x01",
            "charms of a festival like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I doubt we could even use a\x01",
            "car right now, seeing how cramped the\x01",
            "city is.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_199C end

    def Function_15_1A70(): pass

    label("Function_15_1A70")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Heeey, where to next?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Make sure we have time for every popular spot!\x01",
            "We have to make the most of this trip!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1A70 end

    def Function_16_1AED(): pass

    label("Function_16_1AED")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "It'll be quite the feat if we're able to make it\x01",
            "to all the big spots during the commotion\x01",
            "of the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Narrowing down the spots we REALLY want\x01",
            "to see is our best bet.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_1AED end

    def Function_17_1BAA(): pass

    label("Function_17_1BAA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "We might as well go with the parade today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, it's sort of the big finale of the day.\x01",
            "There's no way we can pass that up!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1BAA end

    def Function_18_1C3A(): pass

    label("Function_18_1C3A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "On our way to the city, we tried to stop\x01",
            "by St. Ursula Medical College.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought it'd be cool, considering all the\x01",
            "state-of-the-art medical research they're\x01",
            "working with. You know what I mean?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1C3A end

    def Function_19_1D0D(): pass

    label("Function_19_1D0D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Apparently, the parade's about to begin.\x01",
            "You better hurry if you want a good spot\x01",
            "to watch it from!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_1D0D end

    def Function_20_1D7D(): pass

    label("Function_20_1D7D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "*hic* You all having a shwell time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Didn't take me long to get lil' tipshy.\x01",
            "Worth it, though! *hic* Hahaha.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely the Goddesh will take pity on good\x01",
            "ol' me, eh? Ish the Anniversary Feshtival\x01",
            "afta' all! *hic*\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_1D7D end

    def Function_21_1E64(): pass

    label("Function_21_1E64")

    TalkBegin(0xFE)
    OP_4B(0x13, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1F1D")

    ChrTalk(
        0xFE,
        "Has the parade already passed?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "No way! Is it possible...that this\x01",
            "street isn't a part of its route?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, please no! Where are you, parade?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FAE")

    label("loc_1F1D")


    ChrTalk(
        0xFE,
        "Oh, sweet Aidios... We missed the parade!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please forgive your failure of a father, dear!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Calm down, Dad! Your watch is just fast.\x02",
    )

    CloseMessageWindow()

    label("loc_1FAE")

    OP_4C(0x13, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_21_1E64 end

    def Function_22_1FB6(): pass

    label("Function_22_1FB6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2152")

    ChrTalk(
        0x101,
        (
            "#0003F(It's possible that this kid might know\x01",
            "something about Colin.)\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked if she\x01",
            "knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Um, I don't think I've seen him before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was here all day, so I would've\x01",
            "remembered someone like him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FI see. Well, thanks for your help.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB1, 0)
    SetScenarioFlags(0xAC, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    Jump("loc_21A1")

    label("loc_2152")


    ChrTalk(
        0xFE,
        (
            "I've been here all day, but I've never\x01",
            "seen that boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sorry, mister.\x02",
    )

    CloseMessageWindow()

    label("loc_21A1")

    Jump("loc_22DD")

    label("loc_21A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2246")

    ChrTalk(
        0xFE,
        (
            "It's possible that the music I heard a few\x01",
            "blocks over could have been the parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been a long time since I last\x01",
            "heard it, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22DD")

    label("loc_2246")

    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x12,
        "Oh, sweet Aidios. We missed the parade!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Please forgive your failure of a father, dear!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Calm down, Dad! Your watch is just fast.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)

    label("loc_22DD")

    TalkEnd(0xFE)
    Return()

    # Function_22_1FB6 end

    def Function_23_22E1(): pass

    label("Function_23_22E1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I'd better head straight back to Calvard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd rather not have my mood soiled by\x01",
            "these massive crowds.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_22E1 end

    def Function_24_2358(): pass

    label("Function_24_2358")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "People keep talking about how great this\x01",
            "theme park at Mishelam is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My wallet says no, but my mind keeps telling\x01",
            "me yes. I mean, with the festival going on, I'm\x01",
            "sure it'll be worth the mira!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_2358 end

    def Function_25_2428(): pass

    label("Function_25_2428")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2526")

    ChrTalk(
        0x160,
        "#3300F(Is that it for this area?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Yeah, Zeit already combed through\x01",
            "here and couldn't find anything.)\x02\x03",
            "#0001F(For now, we should just head back to\x01",
            "Central Square and start investigating\x01",
            "West Street.)\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 6)
    OP_29(0x46, 0x1, 0x9)
    OP_1B(0x0, 0xFF, 0xFFFF)

    label("loc_2526")

    Return()

    # Function_25_2428 end

    def Function_26_2527(): pass

    label("Function_26_2527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_253D")
    Call(0, 29)
    Jump("loc_258E")

    label("loc_253D")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked. There is no reason\x01",
            "to open it right now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_258E")

    Return()

    # Function_26_2527 end

    def Function_27_258F(): pass

    label("Function_27_258F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-22000, -3900, 18700, 0)
    MoveCamera(32, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -22000, -5000, 22000, 180)
    SetChrPos(0x103, -22000, -5000, 22000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFC, 0xC3, 0xB6, 0x28, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetCameraDistance(19000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x0)

    def lambda_2672():
        OP_96(0xFE, 0xFFFFAA10, 0xFFFFEC78, 0x45EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2672)

    def lambda_268C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_268C)
    Sleep(900)

    def lambda_26A0():
        OP_96(0xFE, 0xFFFFAA10, 0xFFFFEC78, 0x4C90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_26A0)

    def lambda_26BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_26BA)
    Sleep(1000)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        (
            "#3300585V#0005F#5PWow, the sun's already setting?\x02\x03",
            "#3300586V#0000FGuess we spent more time in the Geofront\x01",
            "than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300587V#0204F#5PIt seems that way.\x02\x03",
            "#3300588V#0202F...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#3300589V#12P#0005FWhat's the matter, Tio?\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#3300590V#0201F#5PNothing.\x02\x03",
            "#3300591V#0203FWe should hurry back to Jona and\x01",
            "retrieve the memory quartz.\x02\x03",
            "#3300592V#0202FFurthermore, I am still worried about\x01",
            "Kitty's true identity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300593V#12P#0000FMe, too. Hopefully, this will lead us\x01",
            "somewhere.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x209), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    SetScenarioFlags(0x5C, 1)
    NewScene("m0101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_258F end

    def Function_28_2951(): pass

    label("Function_28_2951")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(0, 1100, 20000, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 200, 0, 25500, 180)
    SetChrPos(0x160, -1000, 0, 25800, 180)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")

    def lambda_29E7():
        OP_96(0xFE, 0xC8, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29E7)
    Sleep(50)

    def lambda_2A04():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x4EE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2A04)
    SetCameraDistance(17500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x101, 1)
    Sound(806, 2, 100, 0)
    Sleep(500)
    WaitChrThread(0x160, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_2A5F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_2A5F)
    Sleep(500)
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
    Sound(1084, 255, 100, 0)

    def lambda_2AC3():
        OP_9A(0xFE, 0x101, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2AC3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3400373V#0001FLloyd speaking.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1267, 255, 100, 0)
    Sleep(800)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400374V\x07\x05",
            "It's Tio.\x02\x03",
            "#3400375VZeit and I have been following Colin's scent.\x02\x03",
            "#3400376VHowever, given the abundance of people here,\x01",
            "we have not discovered a definitive trail.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400377V\x07\x00",
            "#0006FI was afraid of that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400378V\x07\x05",
            "The trails we HAVE do not go past the\x01",
            "south exit, nor inside the train station.\x02\x03",
            "#3400379VAt least, that is what Zeit concluded after\x01",
            "investigating those locations.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(2054, 255, 90, 0)
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Zeit's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400380V\x07\x05",
            "Woof!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400381V\x07\x00",
            "#0003FGot it.\x02\x03",
            "#3400382V#0000FCould you check the other exits to see\x01",
            "if he may have left through those?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400383V\x07\x05",
            "Affirmative.\x02\x03",
            "#3400384VWe will proceed with our investigation\x01",
            "heading counterclockwise, making our\x01",
            "way toward the east exit.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400385V\x07\x00",
            "#0002FThanks, you two.\x02",
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

    def lambda_2EA0():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x4F4C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2EA0)
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    WaitChrThread(0x160, 1)
    Sleep(300)

    ChrTalk(
        0x160,
        (
            "#3400386V#6P#3309FTeehee. So she chose to tag along\x01",
            "with the big bad wolf, then?\x02\x03",
            "#3400387V#3302FStill, turning him into a police dog?\x01",
            "You guys come up with some\x01",
            "interesting ideas.\x02",
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
            "#3400388V#11P#0006FWell, we didn't have much of a\x01",
            "choice. He walked right into the\x01",
            "SSS building, and that was that.\x02\x03",
            "#3400389V#0005FBut, wait a minute... How do you\x01",
            "know so much about us, Renne?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3400390V#6P#3304FHeehee. Who's to say?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, 0, 0, 20000, 180)
    SetScenarioFlags(0xA2, 4)
    OP_29(0x46, 0x1, 0x8)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_28_2951 end

    def Function_29_30CF(): pass

    label("Function_29_30CF")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-22100, -4000, 20500, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -22700, -5000, 19200, 0)
    SetChrPos(0x160, -21600, -5000, 19200, 315)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis123.itp")
    CreatePortrait(1, 112, 64, 368, 192, 0, 0, 256, 128, 0, 0, 256, 128, 0xFFFFFF, 0x1, "c_vis050.itp")
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked. There is no reason\x01",
            "to open it right now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0x160,
        (
            "#3400391V#3305FCrossbell's very own den of monsters, the\x01",
            "Geofront.\x02\x03",
            "#3400392V#3304FYou can't go inside without a key from City Hall,\x01",
            "so you can scratch it off your list.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400393V#12P#0012FGood point.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x160, 500)

    ChrTalk(
        0x101,
        (
            "#3400394V#6P#0011FHold on, how could you possibly know that?\x02\x03",
            "#3400395V#0013FSure, someone could have told you about\x01",
            "the monsters, but the thing about City Hall?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3400396V#3302FHeehee...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x160, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0x160,
        (
            "#3400397V#3309F#11PI fail to understand your confusion.\x02\x03",
            "#3400398VI'm no stranger to Crossbell, after all.\x02\x03",
            "#3400399V#3302FIt's just another one of my playgrounds, so\x01",
            "I know every nook and cranny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400400V#6P#0005FAnother playground?\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x32, 0x12C)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x1, 0x3)
    VolumeBGM(0x64, 0x12C)

    ChrTalk(
        0x101,
        "#3400401V#6P#0013F(She can't be...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400402V#3304F#11PShall we continue, Detective?\x02\x03",
            "#3400403V#3302FWe still have to return that poor child to\x01",
            "his kind papa and mama, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400404V#6P#0001FRenne, are you...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3400405V#6P#0003FYeah, you're right. Let's keep searching.\x02\x03",
            "#3400406V#0001FColin's safety should be our top priority.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_376D")
    OP_93(0x101, 0xB4, 0x190)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0008F#5P(It looks like Colin didn't wander into this\x01",
            "part of town.)\x02\x03",
            "#0001F(For now, we should just head back to\x01",
            "Central Square and start investigating\x01",
            "West Street.)\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 6)
    OP_29(0x46, 0x1, 0x9)
    OP_1B(0x0, 0xFF, 0xFFFF)

    label("loc_376D")

    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -22500, -5000, 18000, 180)
    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xAC, 5)
    EventEnd(0x5)
    Return()

    # Function_29_30CF end

    def Function_30_378E(): pass

    label("Function_30_378E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(0, 1000, -14200, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, -600, 0, -18500, 0)
    SetChrPos(0x102, 600, 0, -18500, 0)
    SetChrPos(0x103, -600, 0, -19900, 0)
    SetChrPos(0x104, 600, 0, -19900, 0)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")

    def lambda_3862():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3862)
    Sleep(50)

    def lambda_387F():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_387F)
    Sleep(50)

    def lambda_389C():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_389C)
    Sleep(50)

    def lambda_38B9():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_38B9)
    SetCameraDistance(20500, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
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

    def lambda_394C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_394C)
    Sleep(50)

    def lambda_395C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_395C)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3200048V#5P#0005FA call?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3200049V#0305FOh, boy. More trouble?\x02",
    )

    CloseMessageWindow()
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
    Sound(1084, 255, 100, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3200050V#0001FLloyd speaking.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Sound(2083, 255, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D2D")
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3200051V\x07\x05",
            "Heya! Working hard as always, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3200060V\x07\x00",
            "#0005FFran? How's it going?\x02\x03",
            "#3200053V#0002FI've been meaning to thank you for\x01",
            "inviting me out yesterday.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3200054V\x07\x05",
            "No big deal! You know, Noey really had\x01",
            "a wonderful time with you.\x02\x03",
            "#3200055VAnd I did, too, of course!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3200056V\x07\x00",
            "#0009FGlad to hear I was good company.\x02\x03",
            "#3200057V#0001FSo, what's up? Someone submit a\x01",
            "request or something?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3200058V\x07\x05",
            "Ah, yes. Something's come up.\x02\x03",
            "#3200063VI'm sure you're familiar with the two\x01",
            "gangs downtown?\x02\x03",
            "#3200064VWell, there's been reports that they're\x01",
            "currently fighting over in the Harbor District.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3EDD")

    label("loc_3D2D")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3200059V\x07\x05",
            "Heya! Working hard as always, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3200052V\x07\x00",
            "#0005FOh, Fran? Hey.\x02\x03",
            "#3200061V#0001FSo, what's up? Someone submit\x01",
            "a request or something?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3200062V\x07\x05",
            "Ah, yes. Something's come up.\x02\x03",
            "#3200063VI'm sure you're familiar with the two\x01",
            "gangs downtown?\x02\x03",
            "#3200064VWell, there's been reports that they're\x01",
            "currently fighting over in the Harbor District.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3EDD")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3200065V\x07\x00",
            "#0001FSeriously?\x02\x03",
            "#3200066V#0006FWhat are they thinking, pulling a stunt\x01",
            "like this with all these tourists around?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3200067V\x07\x05",
            "We thought the same thing, actually.\x02\x03",
            "#3200068VQuite a few people called the police, but it\x01",
            "seems all of our patrols are preoccupied at\x01",
            "the moment.\x02\x03",
            "#3200069VSince you've dealt with them before, could\x01",
            "we leave this to the Special Support Section?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3200070V\x07\x00",
            "#0000FOf course. You said the Harbor District,\x01",
            "didn't you?\x02\x03",
            "#3200071VWe'll head there right away.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3200072V\x07\x05",
            "Please be careful!\x02",
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
    SetChrSubChip(0x101, 0x2)
    Sound(807, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#3200073V\x07\x00",
            "#11P#0101FSomething happen over in the Harbor District?\x02",
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
    OP_0D()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#3200074V#5P#0006FYeah. Our two favorite gangs are having a\x01",
            "spat, apparently.\x02\x03",
            "#3200075V#0001FWald and Wazy must've thought it was a\x01",
            "great idea to settle it in the middle of the\x01",
            "crowded street.\x02",
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
        0x102,
        "#3200076V#11P#0105FOh, my.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3200077V#12P#0206FThose imbeciles again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200078V#0302FGeez. Did the enthusiasm of the festival\x01",
            "go to their heads or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200079V#5P#0001FEven so, they're putting innocent people\x01",
            "in danger with a stunt like this.\x02\x03",
            "#3200080VWe should head there ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3200081V#11P#0100FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200082V#0304FSounds to me like those troublemakers\x01",
            "need a good old-fashioned spankin'.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, 0, 0, -13500, 0)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA0, 1)
    OP_29(0x44, 0x1, 0x1)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_30_378E end

    def Function_31_4517(): pass

    label("Function_31_4517")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-20000, -4000, 17000, 0)
    MoveCamera(45, 40, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(26000, 0)
    OP_90(0x101, -10000, -3800, 17000, 270)
    OP_90(0x103, -8500, -2800, 17000, 270)
    MoveCamera(35, 25, 0, 10000)
    SetCameraDistance(17500, 10000)
    BeginChrThread(0x101, 3, 0, 32)
    BeginChrThread(0x103, 3, 0, 33)
    FadeToBright(2000, 0)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x103, 0x1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 0)
    NewScene("m0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_4517 end

    def Function_32_45E5(): pass

    label("Function_32_45E5")


    def lambda_45EA():
        OP_95(0xFE, -19000, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45EA)
    WaitChrThread(0xFE, 1)

    def lambda_4608():
        OP_95(0xFE, -22000, -5000, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4608)
    WaitChrThread(0xFE, 1)
    OP_4B(0x103, 0xFF)
    OP_93(0xFE, 0x0, 0x1F4)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x0)
    OP_4C(0x103, 0xFF)

    def lambda_4650():
        OP_95(0xFE, -22000, -5000, 23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4650)
    Sleep(200)

    def lambda_466D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_466D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_32_45E5 end

    def Function_33_4682(): pass

    label("Function_33_4682")


    def lambda_4687():
        OP_95(0xFE, -19000, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4687)
    WaitChrThread(0xFE, 1)

    def lambda_46A5():
        OP_95(0xFE, -22000, -5000, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_46A5)
    WaitChrThread(0xFE, 1)

    def lambda_46C3():
        OP_95(0xFE, -22000, -5000, 23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_46C3)
    Sleep(200)

    def lambda_46E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_46E0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_33_4682 end

    def Function_34_46F5(): pass

    label("Function_34_46F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4798")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FThis is Crossbell Station. The traffic must be\x01",
            "crazy right now.\x02\x03",
            "Luckily, we don't have any business there\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_4798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4839")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FAccording to Zeit, Colin didn't head toward\x01",
            "Crossbell Station.\x02\x03",
            "We should be able to scratch that off our list.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_4839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48E2")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FThat way leads to Crossbell Station. Good\x01",
            "thing we don't have any business there.\x02\x03",
            "The traffic must be crazy right now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_48E2")

    Return()

    # Function_34_46F5 end

    def Function_35_48E3(): pass

    label("Function_35_48E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A33")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49A6")

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
    Jump("loc_4A1D")

    label("loc_49A6")


    ChrTalk(
        0x103,
        (
            "#0203FJona may still contact us.\x02\x03",
            "#0200FWe should travel to the Geofront after\x01",
            "making the necessary preparations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A1D")

    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_4A33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AC9")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FAccording to Zeit, Colin didn't leave\x01",
            "via the south exit.\x02\x03",
            "We can scratch that off our list for now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_4AC9")

    Return()

    # Function_35_48E3 end

    def Function_36_4ACA(): pass

    label("Function_36_4ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B7B")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FLet's wrap up our investigation of Station\x01",
            "Street.\x02\x03",
            "Now, we just have to figure out what other\x01",
            "places Colin might be hiding in.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 0, 0, 21840, 180)
    EventEnd(0x4)

    label("loc_4B7B")

    Return()

    # Function_36_4ACA end

    SaveToFile()

Try(main)
