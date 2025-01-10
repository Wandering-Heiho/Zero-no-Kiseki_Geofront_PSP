from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0000.bin",                # FileName
        "c0000",                    # MapName
        "c0000",                    # Location
        0x0002,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 2, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0000",                  # 0
        "Billy",                  # 1
        "Lyd",                    # 2
        "Felicia",                # 3
        "Letina",                 # 4
        "Marsha",                 # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Tourist",                # 10
        "Tourist",                # 11
        "Tourist",                # 12
        "Tourist",                # 13
        "Tourist",                # 14
        "Tourist",                # 15
        "Tourist",                # 16
        "Businessman",            # 17
        "Businessman",            # 18
        "Tourist",                # 19
        "Tourist",                # 20
        "Tourist",                # 21
        "Tourist",                # 22
        "Tourist",                # 23
        "Tourist",                # 24
        "Tourist",                # 25
        "Tourist",                # 26
        "Tourist",                # 27
        "Chief Sergei",           # 28
        "Old Man",                # 29
        "Old Lady",               # 30
        "Grace",                  # 31
        "Arios",                  # 32
        "列車",                   # 33
        "Tourist",                # 34
        "Tourist",                # 35
        "Tourist",                # 36
        "車00",                   # 37
        "Chroma",                 # 38
        "Central Square",         # 39
        "West Street",            # 40
        "Administrative District",# 41
        "Residential District",   # 42
        "Entertainment District", # 43
        "East Street",            # 44
        "Downtown District",      # 45
        "Harbor District",        # 46
        "IBC",                    # 47
        "Station Street",         # 48
        "Back Alley",             # 49
        "Ursula Road",            # 50
        "East Crossbell Highway", # 51
        "West Crossbell Highway", # 52
        "Mainz Mountain Path",    # 53
    ))

    AddCharChip((
        "chr/ch23600.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch21000.itc",                   # 02
        "chr/ch21100.itc",                   # 03
        "chr/ch21600.itc",                   # 04
        "chr/ch21700.itc",                   # 05
        "chr/ch22800.itc",                   # 06
        "chr/ch24400.itc",                   # 07
        "chr/ch21300.itc",                   # 08
        "chr/ch21800.itc",                   # 09
        "chr/ch21900.itc",                   # 0A
        "chr/ch21200.itc",                   # 0B
        "chr/ch27700.itc",                   # 0C
        "chr/ch27800.itc",                   # 0D
        "chr/ch22100.itc",                   # 0E
        "chr/ch22000.itc",                   # 0F
        "chr/ch32200.itc",                   # 10
        "chr/ch32300.itc",                   # 11
        "chr/ch20200.itc",                   # 12
        "chr/ch20300.itc",                   # 13
        "chr/ch33300.itc",                   # 14
        "chr/ch34500.itc",                   # 15
        "chr/ch24900.itc",                   # 16
    ))

    DeclNpc(4000,    0,       -7000,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-1830,   0,       13000,   180,  261,  0x0, 0,   1,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(5849,    0,       1759,    315,  389,  0x0, 0,   20,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4650,    0,       2950,    135,  389,  0x0, 0,   21,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4389,    0,       -4900,   90,   389,  0x0, 0,   21,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4880,    0,       2930,    35,   389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(6039,    0,       2779,    292,  389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4940,    0,       3049,    111,  389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(5920,    0,       2700,    291,  405,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4750,    0,       3109,    111,  389,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(5909,    0,       2680,    291,  389,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(5239,    0,       2819,    286,  389,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(6539,    0,       1690,    81,   389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(6320,    0,       2339,    177,  389,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(5130,    0,       2099,    290,  389,  0x0, 0,   11,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(4079,    0,       2480,    110,  389,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(3369,    0,       1950,    180,  389,  0x0, 0,   12,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(3480,    0,       529,     0,    389,  0x0, 0,   13,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4369,    0,       2119,    101,  389,  0x0, 0,   16,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(5940,    0,       1970,    281,  389,  0x0, 0,   17,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(4539,    0,       3069,    45,   389,  0x0, 0,   18,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(5880,    0,       2589,    315,  389,  0x0, 0,   19,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(5110,    0,       3750,    112,  389,  0x0, 0,   14,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(5909,    0,       3420,    292,  389,  0x0, 0,   15,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(6360,    0,       2480,    225,  389,  0x0, 0,   2,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(5239,    0,       2789,    180,  389,  0x0, 0,   3,   0,   0,   0,   0,   31,  255,  0)
    DeclNpc(4579,    0,       1519,    252,  389,  0x0, 0,   4,   0,   0,   0,   0,   32,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(699,     0,       13149,   270,  389,  0x0, 0,   22,  0,   0,   0,   0,   33,  255,  0)

    DeclEvent(0x0000, 0, 56,  -11.670000076293945,   17.1200008392334,      -5.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   5.835000038146973,     -8.5600004196167,      1.100000023841858,     1.0])
    DeclEvent(0x0000, 0, 58,  8.5,                   -2.0,                  -0.5,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -4.25,                 0.5,                   0.10000000149011612,   1.0])

    DeclActor(-22300,  -5000,   20700,   2000,    -21950,  -4000,   21360,   0x007C, 0,  35, 0x0000)

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
    PlaceName(2.0, 0.0, 55.0, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_940",          # 00, 0
        "Function_1_9F8",          # 01, 1
        "Function_2_A4B",          # 02, 2
        "Function_3_A84",          # 03, 3
        "Function_4_D88",          # 04, 4
        "Function_5_1040",         # 05, 5
        "Function_6_1CD3",         # 06, 6
        "Function_7_2E27",         # 07, 7
        "Function_8_303A",         # 08, 8
        "Function_9_3267",         # 09, 9
        "Function_10_3456",        # 0A, 10
        "Function_11_3686",        # 0B, 11
        "Function_12_36FA",        # 0C, 12
        "Function_13_3764",        # 0D, 13
        "Function_14_37F4",        # 0E, 14
        "Function_15_3857",        # 0F, 15
        "Function_16_390D",        # 10, 16
        "Function_17_39B5",        # 11, 17
        "Function_18_3A2F",        # 12, 18
        "Function_19_3A8E",        # 13, 19
        "Function_20_3B1D",        # 14, 20
        "Function_21_3BC3",        # 15, 21
        "Function_22_3C59",        # 16, 22
        "Function_23_3CAC",        # 17, 23
        "Function_24_3CE6",        # 18, 24
        "Function_25_3DA3",        # 19, 25
        "Function_26_3DF1",        # 1A, 26
        "Function_27_3E5E",        # 1B, 27
        "Function_28_3EBC",        # 1C, 28
        "Function_29_3F40",        # 1D, 29
        "Function_30_403A",        # 1E, 30
        "Function_31_40C9",        # 1F, 31
        "Function_32_4128",        # 20, 32
        "Function_33_41CC",        # 21, 33
        "Function_34_4432",        # 22, 34
        "Function_35_5D06",        # 23, 35
        "Function_36_5F23",        # 24, 36
        "Function_37_62DB",        # 25, 37
        "Function_38_6315",        # 26, 38
        "Function_39_6352",        # 27, 39
        "Function_40_6397",        # 28, 40
        "Function_41_63D8",        # 29, 41
        "Function_42_641D",        # 2A, 42
        "Function_43_645E",        # 2B, 43
        "Function_44_A6D2",        # 2C, 44
        "Function_45_BBCC",        # 2D, 45
        "Function_46_BCC2",        # 2E, 46
        "Function_47_BDB8",        # 2F, 47
        "Function_48_BE0D",        # 30, 48
        "Function_49_BE62",        # 31, 49
        "Function_50_BEB7",        # 32, 50
        "Function_51_BF18",        # 33, 51
        "Function_52_BF55",        # 34, 52
        "Function_53_BF92",        # 35, 53
        "Function_54_C1F4",        # 36, 54
        "Function_55_C213",        # 37, 55
        "Function_56_D06B",        # 38, 56
        "Function_57_D1BC",        # 39, 57
        "Function_58_D5DD",        # 3A, 58
    ))


    def Function_0_940(): pass

    label("Function_0_940")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_980"),
        (1, "loc_98C"),
        (2, "loc_998"),
        (3, "loc_9A4"),
        (4, "loc_9B0"),
        (5, "loc_9BC"),
        (6, "loc_9C8"),
        (SWITCH_DEFAULT, "loc_9D4"),
    )


    label("loc_980")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_98C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_998")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_9A4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_9B0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_9BC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_9C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_9D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_9E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9F7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_9F7")

    Return()

    # Function_0_940 end

    def Function_1_9F8(): pass

    label("Function_1_9F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A4A")
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1830, 0, -9000, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1830, 0, 13000, 2000, 0x0)
    Sleep(300)
    Jump("Function_1_9F8")

    label("loc_A4A")

    Return()

    # Function_1_9F8 end

    def Function_2_A4B(): pass

    label("Function_2_A4B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A83")
    OP_95(0xFE, -1830, 0, -23430, 2000, 0x0)
    Sleep(800)
    SetChrPos(0xFE, -1830, 0, 25870, 180)
    Jump("Function_2_A4B")

    label("loc_A83")

    Return()

    # Function_2_A4B end

    def Function_3_A84(): pass

    label("Function_3_A84")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B33")
    SetChrPos(0x0, 0, 0, 21840, 180)
    SetChrPos(0x1, 0, 0, 21840, 180)
    SetChrPos(0x2, 0, 0, 21840, 180)
    SetChrPos(0x3, 0, 0, 21840, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B0B")
    SetChrPos(0x4, 0, 0, 21840, 180)
    SetChrPos(0x5, 0, 0, 21840, 180)
    Jump("loc_B2A")

    label("loc_B0B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2A")
    SetChrPos(0x4, 0, 0, 21840, 180)

    label("loc_B2A")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B33")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_B48")
    SetScenarioFlags(0x53, 7)

    label("loc_B48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B5C")
    Event(0, 55)

    label("loc_B5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_B70")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 36)
    Jump("loc_BA7")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_B84")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 43)
    Jump("loc_BA7")

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_B98")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 44)
    Jump("loc_BA7")

    label("loc_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_BA7")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 53)

    label("loc_BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_BDE")
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x8, 3030, 0, -8220, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD9")
    ClearChrFlags(0xC, 0x80)

    label("loc_BD9")

    Jump("loc_D65")

    label("loc_BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BF6")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_D65")

    label("loc_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C0E")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_D65")

    label("loc_C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_C26")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_D65")

    label("loc_C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C43")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x10)
    Jump("loc_D65")

    label("loc_C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C6D")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_C68")
    ClearChrFlags(0x2D, 0x80)

    label("loc_C68")

    Jump("loc_D65")

    label("loc_C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_C8F")
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x10)
    SetChrFlags(0x8, 0x80)
    Jump("loc_D65")

    label("loc_C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_CAC")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_D65")

    label("loc_CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_CDF")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x15, 0x10)
    SetChrPos(0x8, 1990, 0, -10980, 180)
    Jump("loc_D65")

    label("loc_CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_CF2")
    ClearChrFlags(0x13, 0x80)
    Jump("loc_D65")

    label("loc_CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_D0A")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_D65")

    label("loc_D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_D22")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_D65")

    label("loc_D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_D44")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    Jump("loc_D65")

    label("loc_D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_D52")
    Jump("loc_D65")

    label("loc_D52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_D65")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_D65")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D87")
    OP_C7(0x1, 0x1000)

    label("loc_D87")

    Return()

    # Function_3_A84 end

    def Function_4_D88(): pass

    label("Function_4_D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA4")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DD7")

    label("loc_DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DD7")

    label("loc_DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD7")
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DD7")

    SetMapObjFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF2")
    ClearMapObjFlags(0x0, 0x10)
    Jump("loc_DF6")

    label("loc_DF2")

    OP_65(0x0, 0x1)

    label("loc_DF6")

    SetMapObjFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_E0A")
    Jump("loc_E53")

    label("loc_E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_E31")
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x2)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    Jump("loc_E53")

    label("loc_E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_E53")
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x2)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)

    label("loc_E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E94")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_EF5")

    label("loc_E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_ED0")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_EF5")

    label("loc_ED0")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_EF5")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F09")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_F09")

    OP_1B(0x3, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F21")
    OP_1B(0x3, 0x0, 0x39)

    label("loc_F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F34")
    OP_1B(0x3, 0x0, 0x39)

    label("loc_F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F47")
    OP_1B(0x3, 0x0, 0x39)

    label("loc_F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F5A")
    OP_1B(0x3, 0x0, 0x39)

    label("loc_F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F6D")
    OP_1B(0x3, 0x0, 0x39)

    label("loc_F6D")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F8D")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FA9")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_FB7")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_FB7")

    OP_78(0xD, 0x2C)
    SetMapObjFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_FCF")
    Jump("loc_100F")

    label("loc_FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_100F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_100F")
    ClearMapObjFlags(0xD, 0x4)
    SetChrPos(0x2C, 2250, 0, 12500, 180)
    OP_D3(0x2C, 0x0, 0x2BF20, 0x0, 0x0)

    label("loc_100F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_101E")
    SetScenarioFlags(0xD3, 0)

    label("loc_101E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_103A")
    Jump("loc_103F")

    label("loc_103A")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_103F")

    Return()

    # Function_4_D88 end

    def Function_5_1040(): pass

    label("Function_5_1040")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_115B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F8")

    ChrTalk(
        0xFE,
        (
            "There it is! Boy, that package sure\x01",
            "took its sweet, sweet time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Starting to run real low on time here,\x01",
            "so I'd better get this show on the road.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1156")

    label("loc_10F8")


    ChrTalk(
        0xFE,
        (
            "I don't have the time to daydream.\x01",
            "I need to hurry up if I want these\x01",
            "delivered on time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1156")

    Jump("loc_1CCF")

    label("loc_115B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_121F")

    ChrTalk(
        0xFE,
        (
            "I heard the station's currently on\x01",
            "high alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Inspections of both the freight trains\x01",
            "and passenger cars seem to be\x01",
            "falling behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, this isn't good for business.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_121F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_131D")

    ChrTalk(
        0xFE,
        (
            "It's a never-ending cycle. Here I am\x01",
            "again, waiting for more packages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The sad thing is, I think I'm actually\x01",
            "getting used to all these late arrivals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I suppose being able to savor\x01",
            "the wait is the mark of a pro, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_131D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_139F")

    ChrTalk(
        0xFE,
        (
            "I received my packages fairly\x01",
            "early today, amazingly enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "All right! Time to transport these bad boys!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_139F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1469")

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival may have ended,\x01",
            "but I'm as busy as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Deliverymen like myself can't catch a break.\x01",
            "My old man just HAD to go start this\x01",
            "grueling business, didn't he?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_1469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1477")
    Jump("loc_1CCF")

    label("loc_1477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1485")
    Jump("loc_1CCF")

    label("loc_1485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_16A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C4")

    ChrTalk(
        0xFE,
        (
            "I finally finished loading the packages\x01",
            "onto our truck. Now, if only I could take\x01",
            "a break...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to deliver some packages to\x01",
            "Bellguard Gate tomorrow, too. This\x01",
            "is too much to deal with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The freight train runs by there, so it sure\x01",
            "would be nice if it'd drop them off for me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_169E")

    label("loc_15C4")


    ChrTalk(
        0xFE,
        (
            "Members of the Guardian Force live at\x01",
            "their posts, so a few of their families will\x01",
            "send over meals and the like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The freight train runs right by there,\x01",
            "so it sure would be nice if it dropped\x01",
            "them off for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_169E")

    Jump("loc_1CCF")

    label("loc_16A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_178A")

    ChrTalk(
        0xFE,
        (
            "Over there is the truck our\x01",
            "transport company uses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The amount of units in this shipment\x01",
            "is ridiculous, so we're busting out\x01",
            "the truck to handle it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, do I really have to load all this?\x01",
            "What a pain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_178A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1837")

    ChrTalk(
        0xFE,
        (
            "Cargo from other countries\x01",
            "arrives late most of the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I don't deliver them quickly,\x01",
            "I get nagged at by my old man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maaaan, I'm so tired.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_1837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_199E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190A")

    ChrTalk(
        0xFE,
        (
            "I just received cargo from the\x01",
            "Republic a few moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be delivered to...\x01",
            "Whoa! All the way to Mainz?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I'll have to speed up\x01",
            "or else the sun'll set on me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1999")

    label("loc_190A")


    ChrTalk(
        0xFE,
        (
            "I'll have to drive up that narrow\x01",
            "mountain road to get to Mainz,\x01",
            "won't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I'll have to speed up\x01",
            "or else the sun'll set on me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1999")

    Jump("loc_1CCF")

    label("loc_199E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1A57")

    ChrTalk(
        0xFE,
        (
            "Cargo from the Republic is\x01",
            "scheduled for delivery today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not sure why I came early.\x01",
            "The cargo's never on time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should have just slept in,\x01",
            "to be honest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_1A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1B33")

    ChrTalk(
        0xFE,
        "At long last, the cargo has arrived.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Need to deliver these quick,\x01",
            "or else my old man's going\x01",
            "to chew me out again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Geez. If he's always going to complain,\x01",
            "then maybe he should do it himself!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_1B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1F")

    ChrTalk(
        0xFE,
        (
            "Rhimes Deliveries is a start-up\x01",
            "specialized in delivery services.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We deliver goods from foreign countries\x01",
            "to citizens of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I came here to pick up some\x01",
            "cargo, but it hasn't arrived yet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CCF")

    label("loc_1C1F")


    ChrTalk(
        0xFE,
        (
            "Rhimes Deliveries is a start-up\x01",
            "that specializes in delivery services.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I came here to pick up some\x01",
            "cargo, but it's not here yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's really trying my patience.\x02",
    )

    CloseMessageWindow()

    label("loc_1CCF")

    TalkEnd(0xFE)
    Return()

    # Function_5_1040 end

    def Function_6_1CD3(): pass

    label("Function_6_1CD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1DA3")

    ChrTalk(
        0xFE,
        (
            "I hear they beefed up security for both\x01",
            "the airport and the station in order to\x01",
            "minimize potential threats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who in their right mind would\x01",
            "dare to put my precious trains\x01",
            "in danger?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E23")

    label("loc_1DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E2D")

    ChrTalk(
        0xFE,
        (
            "It feels like there haven't been many\x01",
            "train departures today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did they all get delayed or something?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E67")

    label("loc_1E2D")


    ChrTalk(
        0xFE,
        (
            "Strange that there'd be this many\x01",
            "delays in one day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E67")

    Jump("loc_2E23")

    label("loc_1E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_204E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F84")

    ChrTalk(
        0xFE,
        (
            "I'm grateful to the Empire for\x01",
            "blessing the world with so\x01",
            "many beautiful trains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's just... I can't forgive them for\x01",
            "developing those railway guns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You could say that trains transport\x01",
            "people as well as the dreams of\x01",
            "train fans like me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2049")

    label("loc_1F84")


    ChrTalk(
        0xFE,
        (
            "I dislike the Empire's railway\x01",
            "guns, even if they're on rails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Railways aren't meant to be instruments of war.\x01",
            "They're noble creations meant for transporting\x01",
            "people, freight, and dreams.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2049")

    Jump("loc_2E23")

    label("loc_204E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_21C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_211B")

    ChrTalk(
        0xFE,
        (
            "I'd kill to get my hands on\x01",
            "an orbal camera right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why? To take pictures\x01",
            "of trains, of course!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Common folk like myself simply\x01",
            "don't have the funds to buy one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21C4")

    label("loc_211B")


    ChrTalk(
        0xFE,
        (
            "I even applied to become a\x01",
            "cameraman at the Crossbell\x01",
            "News Service once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Obviously, they had no interest\x01",
            "in someone who only wanted to\x01",
            "take shots of railways.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C4")

    Jump("loc_2E23")

    label("loc_21C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2267")

    ChrTalk(
        0xFE,
        (
            "Now that the Anniversary Festival is\x01",
            "over, the trains have returned to their\x01",
            "normal operations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* I feel lonely all of a sudden.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E23")

    label("loc_2267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2313")

    ChrTalk(
        0xFE,
        (
            "Next month's Anniversary Festival\x01",
            "will attract a lot of tourists who\x01",
            "come here by train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All those trains lining up will\x01",
            "be a real sight to behold.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E23")

    label("loc_2313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_246A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A7")

    ChrTalk(
        0xFE,
        (
            "I heard that some enthusiasts\x01",
            "in the Empire collect railway\x01",
            "models.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, the envy! If only\x01",
            "I were born a noble!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2465")

    label("loc_23A7")


    ChrTalk(
        0xFE,
        (
            "Since the models are handmade\x01",
            "by artisans, they tend to get\x01",
            "unbelievably expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I ever became rich, I would retire\x01",
            "early and gaze at railway models for\x01",
            "the rest of my life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2465")

    Jump("loc_2E23")

    label("loc_246A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2539")

    ChrTalk(
        0xFE,
        (
            "The best part of the Anniversary\x01",
            "Festival is the surge in trains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like swarms of insects crawling out of the\x01",
            "woodwork, the sight of people getting off\x01",
            "trains never fails to amaze me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E23")

    label("loc_2539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2742")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2667")

    ChrTalk(
        0xFE,
        (
            "The Transcontinental Railroad was built\x01",
            "over a period of many, many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Constructing such an enormous track\x01",
            "without incident must've taken some\x01",
            "meticulous planning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It truly is the greatest gift from our ancestors.\x01",
            "Someday, I want to become just like them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_273D")

    label("loc_2667")


    ChrTalk(
        0xFE,
        (
            "Meticulously laying down a track the length of the\x01",
            "Transcontinental Railroad took years and years of\x01",
            "hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It truly is the greatest gift from our ancestors.\x01",
            "Someday, I want to become just like them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_273D")

    Jump("loc_2E23")

    label("loc_2742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_27F5")

    ChrTalk(
        0xFE,
        (
            "Why don't people understand the\x01",
            "irresistible charm of railways?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can't discuss Crossbell's history and its\x01",
            "emphasis on trade without mentioning trains.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E23")

    label("loc_27F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2968")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B4")

    ChrTalk(
        0xFE,
        (
            "As a child, I always dreamed of becoming a\x01",
            "railway engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But one day, I decided to stick to admiration\x01",
            "instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's why I'm a train buff now!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2963")

    label("loc_28B4")


    ChrTalk(
        0xFE,
        "Appreciating trains makes me feel good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a child, I always wanted to become a\x01",
            "railway engineer. But if I had to pick now,\x01",
            "I'd opt for being a mere station worker.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2963")

    Jump("loc_2E23")

    label("loc_2968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2AD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A1A")

    ChrTalk(
        0xFE,
        (
            "The Transcontinental Railroad opened\x01",
            "for public use around 20 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now you can travel directly to Eastern Zemuria\x01",
            "on a single railway.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2ACE")

    label("loc_2A1A")


    ChrTalk(
        0xFE,
        (
            "Now you can travel directly to Eastern Zemuria\x01",
            "on a single railway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though it'll be a long and expensive\x01",
            "trip, I feel obliged to make it someday as\x01",
            "a train fanatic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ACE")

    Jump("loc_2E23")

    label("loc_2AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2CA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C13")

    ChrTalk(
        0xFE,
        "Airships, trains, cars...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They all cruise freely through the sky\x01",
            "or across land at amazing speeds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We tend to take technology for granted\x01",
            "nowadays, but if you really think about\x01",
            "it, it's all so incredible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do you feel the same love, the same\x01",
            "romance I'm feeling right now?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C9D")

    label("loc_2C13")


    ChrTalk(
        0xFE,
        "Airships, trains, cars...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I prefer trains, but there must be plenty\x01",
            "of people out there who feel strongly\x01",
            "about other vehicles.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C9D")

    Jump("loc_2E23")

    label("loc_2CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7C")

    ChrTalk(
        0xFE,
        "Are you on your way to the station?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My sources say the train bound for the\x01",
            "Republic should be arriving soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's fairly crowded during this time\x01",
            "of day, so please be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E23")

    label("loc_2D7C")


    ChrTalk(
        0xFE,
        (
            "The train bound for the Republic\x01",
            "should be arriving soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If time allowed it, I would stick around\x01",
            "and listen to the beautiful whistle of a\x01",
            "departing train.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E23")

    TalkEnd(0xFE)
    Return()

    # Function_6_1CD3 end

    def Function_7_2E27(): pass

    label("Function_7_2E27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2ECC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E45")
    Call(0, 9)
    Jump("loc_2EC7")

    label("loc_2E45")


    ChrTalk(
        0xFE,
        (
            "Why must Letina make a fuss\x01",
            "over every little detail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whatever. I can't wait until\x01",
            "I'm back at the mansion again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC7")

    Jump("loc_3036")

    label("loc_2ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FAB")

    ChrTalk(
        0xFE,
        "Phew. Here we are, at last.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell, home of the septium industry.\x01",
            "Just thinking about it gets me all tingly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll definitely get my hands on loads and\x01",
            "loads of precious septium crystals!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3036")

    label("loc_2FAB")


    ChrTalk(
        0xFE,
        (
            "I'll definitely get my hands on loads and\x01",
            "loads of precious septium crystals!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But first, I need to find myself a place to\x01",
            "sleep.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3036")

    TalkEnd(0xFE)
    Return()

    # Function_7_2E27 end

    def Function_8_303A(): pass

    label("Function_8_303A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3107")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3058")
    Call(0, 9)
    Jump("loc_3102")

    label("loc_3058")


    ChrTalk(
        0xFE,
        (
            "Ugh. Just thinking of what they'll say once\x01",
            "I return to the mansion depresses me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Aidios! Grant me divine protection for\x01",
            "the scolding they'll throw my way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3102")

    Jump("loc_3263")

    label("loc_3107")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3206")

    ChrTalk(
        0xFE,
        (
            "Lady Felicia and I came here from Erebonia\x01",
            "to purchase septium crystals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since we practically had to run away to find\x01",
            "our way here, I can only assume our sudden\x01",
            "disappearance caused a great stir at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I feel awful.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3263")

    label("loc_3206")


    ChrTalk(
        0xFE,
        (
            "To end up all the way over here in a\x01",
            "completely different country... I think\x01",
            "I may cry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3263")

    TalkEnd(0xFE)
    Return()

    # Function_8_303A end

    def Function_9_3267(): pass

    label("Function_9_3267")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xA,
        (
            "I managed to get my hands on some of those\x01",
            "glorious septium crystals. With that, I can now\x01",
            "finally return to Erebonia happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't wait to see the surprised look on\x01",
            "Father's face when he takes a gander\x01",
            "at this giant carnelia crystal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's been close to four months since we\x01",
            "ran away with a small fortune.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think anyone would be surprised if\x01",
            "we were to suddenly reappear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "S-Silence, you useless maid!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "So heartless, my lady...\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_9_3267 end

    def Function_10_3456(): pass

    label("Function_10_3456")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_362F")

    ChrTalk(
        0xFE,
        "I've decided to chase after Lady Felicia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't allow her go somewhere\x01",
            "so far away all by herself.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3624")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_3592")

    ChrTalk(
        0x101,
        "#0005FHaven't we met this maid before?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FI think she's employed at Representative\x01",
            "Campbell's mansion.\x02\x03",
            "#0106FIt looks like something's bothering her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3624")

    label("loc_3592")


    ChrTalk(
        0x101,
        "#0005FIs that a maid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FI'm guessing she must be employed\x01",
            "at someones mansion.\x02\x03",
            "(I can't shake the feeling we've met her\x01",
            "before...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3624")

    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0xEF, 5)
    Jump("loc_3682")

    label("loc_362F")


    ChrTalk(
        0xFE,
        (
            "Please forgive me, Master...\x01",
            "...but I feel obligated to be by my lady's\x01",
            "side!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3682")

    TalkEnd(0xFE)
    Return()

    # Function_10_3456 end

    def Function_11_3686(): pass

    label("Function_11_3686")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "This must be it! Crossbell Station!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Glad I managed to make it out of\x01",
            "that enormous maze of a city.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_3686 end

    def Function_12_36FA(): pass

    label("Function_12_36FA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Come on, dear. We're going\x01",
            "to miss the train at this rate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If we're late, that's on you!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_36FA end

    def Function_13_3764(): pass

    label("Function_13_3764")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "There sure are lots of interesting things\x01",
            "going on in Crossbell, aren't there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It sure makes this old heart\x01",
            "run rampant again.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_3764 end

    def Function_14_37F4(): pass

    label("Function_14_37F4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Sheesh, your eyes are beaming\x01",
            "like a little kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Try to calm down a little, okay?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_37F4 end

    def Function_15_3857(): pass

    label("Function_15_3857")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "When I tried to venture out onto the\x01",
            "highway, a local stopped me. Said it\x01",
            "was way too dangerous for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess I'll just rely on the bus\x01",
            "for sightseeing now.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_3857 end

    def Function_16_390D(): pass

    label("Function_16_390D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I can relate with the urge to step out on\x01",
            "the open highway and explore aimlessly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All these skyscrapers can make a country\x01",
            "boy like me claustrophobic.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_390D end

    def Function_17_39B5(): pass

    label("Function_17_39B5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm, Central Square should be right\x01",
            "down this road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew! I knew buying this map was the\x01",
            "right decision!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_39B5 end

    def Function_18_3A2F(): pass

    label("Function_18_3A2F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The swaying of the train has made\x01",
            "me a tad bit nauseous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ugh, this is horrid.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_3A2F end

    def Function_19_3A8E(): pass

    label("Function_19_3A8E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, honey. You're always so quick\x01",
            "to get motion sickness!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We won't be able to go anywhere\x01",
            "if you keep getting sick like this.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_3A8E end

    def Function_20_3B1D(): pass

    label("Function_20_3B1D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "We originally planned to visit next month\x01",
            "during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't handle crowds, though, so we\x01",
            "came to relax before it gets packed.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_3B1D end

    def Function_21_3BC3(): pass

    label("Function_21_3BC3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Dear, why did we come at the only time\x01",
            "there are no tourists wandering about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Roaming among the bustle of the city is\x01",
            "the best part.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_3BC3 end

    def Function_22_3C59(): pass

    label("Function_22_3C59")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I have business at the IBC today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, then, shall we get going?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_3C59 end

    def Function_23_3CAC(): pass

    label("Function_23_3CAC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Don't worry! I'll accompany you there, Chief!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_3CAC end

    def Function_24_3CE6(): pass

    label("Function_24_3CE6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The Crossbell Anniversary Festival\x01",
            "has already come to a close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good, I say! This is a shining opportunity\x01",
            "to really focus and build up our business!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Don't you think?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_3CE6 end

    def Function_25_3DA3(): pass

    label("Function_25_3DA3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "You're right, boss! Let's go appraise\x01",
            "the merchandise right away!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_3DA3 end

    def Function_26_3DF1(): pass

    label("Function_26_3DF1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Looks like the sun's about to set.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely there'll be rooms available\x01",
            "at one of the hotels.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_3DF1 end

    def Function_27_3E5E(): pass

    label("Function_27_3E5E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The long journey did a number\x01",
            "on my stomach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I need to find some grub, fast.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_3E5E end

    def Function_28_3EBC(): pass

    label("Function_28_3EBC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "My beloved and I have escaped the\x01",
            "Empire, far from my father's reach!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We can finally live our lives without worry!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_3EBC end

    def Function_29_3F40(): pass

    label("Function_29_3F40")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "If I had fallen in love with a woman of the\x01",
            "same social class, my dear wouldn't have\x01",
            "had to cut ties with her family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm the worst, aren't I?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, when I see her radiant smile, my fears\x01",
            "and guilt are washed away by her love.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_3F40 end

    def Function_30_403A(): pass

    label("Function_30_403A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The inspector's examination was\x01",
            "strangely thorough today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He kept muttering something about\x01",
            "dangerous goods. What's going on?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_403A end

    def Function_31_40C9(): pass

    label("Function_31_40C9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Something about the station felt\x01",
            "unusually tense today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did something happen?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_40C9 end

    def Function_32_4128(): pass

    label("Function_32_4128")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I think I may pass out. The station workers\x01",
            "have kept me waiting for almost an hour now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Has Crossbell always been this particular\x01",
            "about security?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_4128 end

    def Function_33_41CC(): pass

    label("Function_33_41CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_439F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_42CF")

    ChrTalk(
        0x2D,
        (
            "The acerbic tomato shake is a bit\x01",
            "special, so I can't normally\x01",
            "serve it that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "Besides, it costs a lot to make\x01",
            "and it barely sells on top of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "Most days, I make only a few shakes,\x01",
            "exclusively for the mayor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_439A")

    label("loc_42CF")


    ChrTalk(
        0x2D,
        (
            "Back already? Does that mean you\x01",
            "were able to deliver the shake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYep, we were. I'm sure he's probably\x01",
            "sipping on it as we speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FThank youuu!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "Why, you're very welcome!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_439A")

    Jump("loc_442E")

    label("loc_439F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_442B")

    ChrTalk(
        0x2D,
        (
            "Give him this shake as a token of my\x01",
            "gratitude, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "I'm forever thankful for his continued\x01",
            "patronage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_442E")

    label("loc_442B")

    Call(0, 34)

    label("loc_442E")

    TalkEnd(0xFE)
    Return()

    # Function_33_41CC end

    def Function_34_4432(): pass

    label("Function_34_4432")

    EventBegin(0x0)
    Fade(500)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_68(-530, 1300, 12810, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17490, 0)
    SetChrPos(0x101, -700, 0, 13150, 90)
    SetChrPos(0x153, -850, 0, 11920, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44B9")
    SetChrPos(0x102, -960, 0, 14520, 135)
    Jump("loc_4500")

    label("loc_44B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44DF")
    SetChrPos(0x103, -960, 0, 14520, 135)
    Jump("loc_4500")

    label("loc_44DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4500")
    SetChrPos(0x104, -960, 0, 14520, 135)

    label("loc_4500")

    OP_93(0x2D, 0x10E, 0x0)
    SetChrSubChip(0x2D, 0x0)
    OP_0D()

    ChrTalk(
        0x2D,
        "#11PWelcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "#11PCome for a refreshing drink?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#1110FLook! It's the juice lady!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FYou're usually set up around the fountain\x01",
            "in the Administrative District, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#11PWell, yes, but I like to switch things up\x01",
            "every now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#11PNothing beats a little change of scenery...\x01",
            "With the exception of paying customers,\x01",
            "of course! What would you like?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46D0")

    ChrTalk(
        0x102,
        "#6P#0102FSorry to disappoint, but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_474E")

    label("loc_46D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_471F")

    ChrTalk(
        0x103,
        "#6P#0200FI apologize, but the order is not for us...\x02",
    )

    CloseMessageWindow()
    Jump("loc_474E")

    label("loc_471F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_474E")

    ChrTalk(
        0x104,
        "#6P#0300FTempting, but...\x02",
    )

    CloseMessageWindow()

    label("loc_474E")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They explained that they dropped by to pick up\x01",
            "the mayor's usual order.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x2D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x2D,
        "#11POh, I see. You're here on behalf of the mayor!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#11PIn that case, give me a minute to whip\x01",
            "up his favorite.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadEffect(0x0, "battle\\it002_00.eff")
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x2D,
        "#11PHere you go!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x358),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x358, 1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_490B")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_4960")

    label("loc_490B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4938")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_4960")

    label("loc_4938")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4960")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4960")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#0005FWhat IS this?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49F0")

    ChrTalk(
        0x102,
        (
            "#6P#0105FI do know that my grandfather loves\x01",
            "bitter flavors, but this is a bit much...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AAA")

    label("loc_49F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A4F")

    ChrTalk(
        0x103,
        (
            "#6P#0206FJust the sight of it is enough to make\x01",
            "my mouth shrivel up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AAA")

    label("loc_4A4F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AAA")

    ChrTalk(
        0x104,
        (
            "#6P#0306FThe mayor has some interesting tastes,\x01",
            "that's for damn sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AAA")


    ChrTalk(
        0x2D,
        (
            "#11PThis particular shake eliminates fatigue in no time\x01",
            "flat, but people complained about the bitterness.\x01",
            "That's why it's not listed on the menu anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#11PYou know, I made extra. Would you like\x01",
            "to give it a taste?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0011FUmm, well...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Aidios, protect me.\x01",      # 0
            "Politely decline.\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5974")

    ChrTalk(
        0x101,
        "#6P#0012FO-Okay. Just a sip, though.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D22")

    ChrTalk(
        0x102,
        (
            "#6P#0106FThere's no harm in it.\x01",
            "(And I suppose I am curious as to why\x01",
            "Grandfather enjoys it as much as he does.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Nervously, Lloyd and Elie put samples of the\x01",
            "acerbic tomato shake to their lips and took\x01",
            "a little sip.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4E8B")

    label("loc_4D22")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DC2")

    ChrTalk(
        0x103,
        "#6P#0206FSeriously?\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Nervously, Lloyd and Tio put samples of the\x01",
            "acerbic tomato shake to their lips and took\x01",
            "a little sip.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4E8B")

    label("loc_4DC2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E8B")

    ChrTalk(
        0x104,
        (
            "#6P#0306FEh, might as well. I'm prepared to meet my\x01",
            "bitter end.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Nervously, Lloyd and Randy put samples of the\x01",
            "acerbic tomato shake to their lips and took\x01",
            "a little sip.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4E8B")

    Sound(887, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F0C")
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_4FC7")

    label("loc_4F0C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F6C")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_4FC7")

    label("loc_4F6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FC7")
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4FC7")

    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A liquid, bitter as death, slowly crawled down\x01",
            "their throats.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x0, 0x0, 0x101, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(228, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_509D")
    PlayEffect(0x0, 0x1, 0x102, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_5130")

    label("loc_509D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50E9")
    PlayEffect(0x0, 0x1, 0x103, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_5130")

    label("loc_50E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5130")
    PlayEffect(0x0, 0x1, 0x104, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_5130")

    OP_89(0x0, 0x0)
    OP_89(0x1, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Everyone's CP is restored!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_32(0x0, 0x5, 0xC8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_517C")
    OP_32(0x1, 0x5, 0xC8)
    Jump("loc_51AB")

    label("loc_517C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5196")
    OP_32(0x2, 0x5, 0xC8)
    Jump("loc_51AB")

    label("loc_5196")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51AB")
    OP_32(0x3, 0x5, 0xC8)

    label("loc_51AB")


    ChrTalk(
        0x101,
        (
            "#6P#0010F*cough* *cough*\x02\x03",
            "#0006FW-Wow. I've never felt this, uh, refreshed\x01",
            "before. Still not sure if that's good or bad,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5294")

    ChrTalk(
        0x102,
        (
            "#6P#0110FThis intense bitterness must be...*cough*\x01",
            "...an acquired taste.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5343")

    label("loc_5294")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52E3")

    ChrTalk(
        0x103,
        "#6P#0208FH-How is this level of bitterness possible?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5343")

    label("loc_52E3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5343")

    ChrTalk(
        0x104,
        (
            "#6P#0310FOkay, yeah. I was expectin' it to be bitter,\x01",
            "but not THAT bitter!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5343")


    ChrTalk(
        0x2D,
        "#11PHahaha! I know, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#1111FOooh, I wanna try it, too.\x02",
    )

    CloseMessageWindow()
    OP_93(0x153, 0x5A, 0x1F4)
    OP_96(0x153, 0x2BC, 0x0, 0x2E90, 0x3E8, 0x0)
    Sleep(500)
    OP_93(0x153, 0x0, 0x1F4)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "KeA grabbed what was left of the acerbic tomato\x01",
            "shake and put the straw in her mouth.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5431():
        TurnDirection(0x101, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5431)

    def lambda_543E():
        TurnDirection(0x2D, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_543E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_547A")
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x102, 0x153, 500)
    Jump("loc_54DD")

    label("loc_547A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54AE")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x103, 0x153, 500)
    Jump("loc_54DD")

    label("loc_54AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54DD")
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x104, 0x153, 500)

    label("loc_54DD")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#0011FWait! Stop!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_552F")

    ChrTalk(
        0x102,
        "#6P#0105FDon't do it, KeA!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5595")

    label("loc_552F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_555B")

    ChrTalk(
        0x103,
        "#6P#0205FKeA, no!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5595")

    label("loc_555B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5595")

    ChrTalk(
        0x104,
        "#6P#0305FYou sure about this, KeDo?!\x02",
    )

    CloseMessageWindow()

    label("loc_5595")


    ChrTalk(
        0x153,
        (
            "#12P#1103F*sluuuurp*\x02\x03",
            "#1100F*glug* *glug*\x02\x03",
            "#1109FAaaaah! Sooo goood!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5624")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_5679")

    label("loc_5624")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5651")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_5679")

    label("loc_5651")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5679")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5679")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#0011FD-Did she just finish it off?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56F3")

    ChrTalk(
        0x102,
        "#6P#0105FShe made it look like it was nothing...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5775")

    label("loc_56F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5739")

    ChrTalk(
        0x103,
        "#6P#0205FYou are much tougher than me, KeA.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5775")

    label("loc_5739")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5775")

    ChrTalk(
        0x104,
        "#6P#0302FFull of surprises, this girl.\x02",
    )

    CloseMessageWindow()

    label("loc_5775")

    TurnDirection(0x153, 0x101, 500)

    ChrTalk(
        0x153,
        (
            "#12P#1101FHuh? Why?\x02\x03",
            "#1100FIt's a little bitter, but\x01",
            "it's still good, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006FAs long as you like it, there's\x01",
            "nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#11PImpressive. You're a brave one,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_584E():
        TurnDirection(0x101, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_584E)

    def lambda_585B():
        TurnDirection(0x153, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_585B)

    def lambda_5868():
        TurnDirection(0x2D, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_5868)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_588C")
    TurnDirection(0x102, 0x2D, 500)
    Jump("loc_58BF")

    label("loc_588C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58A8")
    TurnDirection(0x103, 0x2D, 500)
    Jump("loc_58BF")

    label("loc_58A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58BF")
    TurnDirection(0x104, 0x2D, 500)

    label("loc_58BF")


    ChrTalk(
        0x101,
        (
            "#6P#0000FIsn't that the truth? Anyway, thanks for\x01",
            "everything. I'm sure the mayor will be\x01",
            "happy, too.\x02\x03",
            "Oh, and we'll pay you for our samples.\x01",
            "How much do we owe you?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x26, 0x1, 0x3)
    Jump("loc_5B24")

    label("loc_5974")


    ChrTalk(
        0x101,
        "#6P#0006FThanks, but I have to pass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#1105FAw, why?\x02\x03",
            "#1107FI wanted to try it!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A44")

    ChrTalk(
        0x102,
        (
            "#6P#0102FSorry, KeA, but I think you might\x01",
            "be a bit too young for something\x01",
            "this strong.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AF8")

    label("loc_5A44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A99")

    ChrTalk(
        0x103,
        (
            "#6P#0200FYou are too young for something\x01",
            "that strong, KeA.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AF8")

    label("loc_5A99")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5AF8")

    ChrTalk(
        0x104,
        (
            "#6P#0300FDon't do it, KeDo. Your tastebuds\x01",
            "would never be the same again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AF8")


    ChrTalk(
        0x101,
        "#6P#0000FHow much do we owe you?\x02",
    )

    CloseMessageWindow()
    OP_29(0x26, 0x1, 0x4)

    label("loc_5B24")


    ChrTalk(
        0x2D,
        (
            "#11PZilch. Today's special, so it's on the\x01",
            "house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#11PIt's the least I can do for my favorite\x01",
            "regular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#11PGive him this shake as a token of my\x01",
            "gratitude, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FYou're sure?\x02\x03",
            "#0000FAll right, then. Thank you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C68")

    ChrTalk(
        0x102,
        (
            "#6P#0102FWe'll make sure to pass\x01",
            "along the kind words, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CE8")

    label("loc_5C68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5CAA")

    ChrTalk(
        0x103,
        "#6P#0202FWe will make sure to tell him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CE8")

    label("loc_5CAA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5CE8")

    ChrTalk(
        0x104,
        "#6P#0302FNo worries! We'll let him know.\x02",
    )

    CloseMessageWindow()

    label("loc_5CE8")

    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x0, -700, 0, 13150, 90)
    EventEnd(0x5)
    Return()

    # Function_34_4432 end

    def Function_35_5D06(): pass

    label("Function_35_5D06")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 0)), scpexpr(EXPR_END)), "loc_5E2C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BD(0x0, 0x63)"), scpexpr(EXPR_EXEC_OP, "OP_BD(0x3, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BD(0x2, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BD(0x1, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D2F")
    Jump("loc_5E2C")

    label("loc_5D2F")


    ChrTalk(
        0x103,
        (
            "#0203FNot all of us have quartz set in our\x01",
            "orbments yet.\x02\x03",
            "#0200FWe should do that before entering.\x02",
        )
    )

    CloseMessageWindow()
    Sound(828, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please set a quartz for each party member.\x02\x03",
            "Open [ORBMENT] in the Camp Menu and then select\x01",
            "[QUARTZ] to set available quartz.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_5E2C")

    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x02\x03",
            "The door can be unlocked with the Geofront A Sector key.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Unlock\x01",      # 0
            "Don't\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5ED5"),
        (1, "loc_5F1B"),
        (SWITCH_DEFAULT, "loc_5F20"),
    )


    label("loc_5ED5")

    Sound(809, 0, 100, 0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door was unlocked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMapObjFlags(0x0, 0x10)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x46, 0)
    OP_C7(0x1, 0x80000)
    Jump("loc_5F20")

    label("loc_5F1B")

    Jump("loc_5F20")

    label("loc_5F20")

    EventEnd(0x3)
    Return()

    # Function_35_5D06 end

    def Function_36_5F23(): pass

    label("Function_36_5F23")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20800.itc", 0x1E)
    LoadChrToIndex("chr/ch20900.itc", 0x1F)
    LoadChrToIndex("chr/ch21400.itc", 0x20)
    LoadChrToIndex("apl/ch50003.itc", 0x21)
    OP_68(4200, 3100, -1900, 0)
    MoveCamera(90, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 10000, 500, -1900, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x24, 0x4)
    ClearChrFlags(0x25, 0x4)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x24, 10000, 500, -2800, 270)
    SetChrPos(0x25, 10000, 500, -1000, 270)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x40)
    SetChrChipByIndex(0x29, 0xF)
    SetChrSubChip(0x29, 0x0)
    SetChrFlags(0x29, 0x8000)
    SetChrChipByIndex(0x2A, 0x8)
    SetChrSubChip(0x2A, 0x0)
    SetChrFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2B, 0x20)
    SetChrSubChip(0x2B, 0x0)
    SetChrFlags(0x2B, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x2A, 900, 0, -8000, 0)
    SetChrPos(0x29, 4600, 0, 3300, 45)
    SetChrPos(0x2B, -4100, 0, -700, 315)
    SetChrPos(0x9, -1100, 0, 11000, 180)
    OP_E5()
    FadeToBright(1000, 0)
    OP_0D()
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)

    def lambda_60B7():
        OP_95(0xFE, 900, 0, 40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_60B7)

    def lambda_60D1():
        OP_95(0xFE, -1100, 0, -40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_60D1)
    OP_68(1200, 1100, -1900, 6000)
    MoveCamera(90, 12, 0, 6000)
    SetCameraDistance(22000, 6000)
    BeginChrThread(0x101, 3, 0, 37)
    Sleep(800)
    BeginChrThread(0x24, 3, 0, 39)
    Sleep(500)
    BeginChrThread(0x25, 3, 0, 41)
    Sleep(2000)
    Sound(101, 0, 100, 0)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    Sleep(2000)
    Fade(1000)
    OP_68(1200, 1100, -1900, 0)
    MoveCamera(48, 14, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(24000, 0)
    MoveCamera(42, 14, 0, 8000)
    SetCameraDistance(30000, 8000)
    OP_0D()
    PlaceName2(100, 200, "c_plac01", 0x0, 2000)
    BeginChrThread(0x101, 3, 0, 38)
    Sleep(400)
    BeginChrThread(0x24, 3, 0, 40)
    Sleep(1100)
    BeginChrThread(0x25, 3, 0, 42)
    OP_6F(0x40)
    OP_6F(0x10)
    Sleep(1000)
    Fade(500)
    OP_68(-700, 700, 12800, 0)
    MoveCamera(41, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x25, 0x1)
    SetChrPos(0x101, -700, 0, 10000, 0)
    SetChrPos(0x24, -1000, 0, 7800, 0)
    SetChrPos(0x25, 0, 0, 7400, 0)

    def lambda_624D():
        OP_97(0xFE, 0x0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_624D)

    def lambda_6267():
        OP_97(0xFE, 0x0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_6267)

    def lambda_6281():
        OP_97(0xFE, 0x0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_6281)
    OP_68(1400, 2700, 17000, 8000)
    MoveCamera(41, 5, 0, 8000)
    SetCameraDistance(19500, 8000)
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    OP_E6()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_5F23 end

    def Function_37_62DB(): pass

    label("Function_37_62DB")


    def lambda_62E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_62E0)

    def lambda_62F1():
        OP_95(0xFE, 600, 0, -1900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62F1)
    WaitChrThread(0x101, 1)
    Sleep(500)
    OP_93(0x101, 0x5A, 0x3E8)
    Return()

    # Function_37_62DB end

    def Function_38_6315(): pass

    label("Function_38_6315")


    def lambda_631A():
        OP_95(0xFE, -200, 0, -1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_631A)
    WaitChrThread(0x101, 1)

    def lambda_6338():
        OP_95(0xFE, -200, 0, 40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6338)
    WaitChrThread(0x101, 1)
    Return()

    # Function_38_6315 end

    def Function_39_6352(): pass

    label("Function_39_6352")


    def lambda_6357():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_6357)

    def lambda_6368():
        OP_95(0xFE, 1800, 0, -2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_6368)
    WaitChrThread(0x24, 1)
    Sleep(500)

    def lambda_6389():

        label("loc_6389")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6389")

    QueueWorkItem2(0xFE, 2, lambda_6389)
    Return()

    # Function_39_6352 end

    def Function_40_6397(): pass

    label("Function_40_6397")

    EndChrThread(0x24, 0x2)

    def lambda_63A0():
        OP_95(0xFE, -600, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_63A0)
    WaitChrThread(0x24, 1)

    def lambda_63BE():
        OP_95(0xFE, -600, 0, 40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_63BE)
    WaitChrThread(0x24, 1)
    Return()

    # Function_40_6397 end

    def Function_41_63D8(): pass

    label("Function_41_63D8")


    def lambda_63DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_63DD)

    def lambda_63EE():
        OP_95(0xFE, 2000, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_63EE)
    WaitChrThread(0x25, 1)
    Sleep(300)

    def lambda_640F():

        label("loc_640F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_640F")

    QueueWorkItem2(0xFE, 2, lambda_640F)
    Return()

    # Function_41_63D8 end

    def Function_42_641D(): pass

    label("Function_42_641D")

    EndChrThread(0x25, 0x2)

    def lambda_6426():
        OP_95(0xFE, 400, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_6426)
    WaitChrThread(0x25, 1)

    def lambda_6444():
        OP_95(0xFE, 400, 0, 40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_6444)
    WaitChrThread(0x25, 1)
    Return()

    # Function_42_641D end

    def Function_43_645E(): pass

    label("Function_43_645E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    OP_68(-500, 3000, 18800, 0)
    MoveCamera(30, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x23, 0x4)
    SetChrPos(0x23, -500, 0, 22000, 180)
    SetChrPos(0x101, -1300, 0, 25000, 180)
    SetChrPos(0x102, 300, 0, 25000, 180)
    SetChrPos(0x103, -1300, 0, 26600, 180)
    SetChrPos(0x104, 300, 0, 26600, 180)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis001.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis002.itp")
    CreatePortrait(2, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis003.itp")
    CreatePortrait(3, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis004.itp")

    def lambda_65E0():
        OP_95(0xFE, -500, 0, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_65E0)
    Sleep(500)

    def lambda_65FD():
        OP_95(0xFE, -1300, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65FD)
    Sleep(50)

    def lambda_661A():
        OP_95(0xFE, 300, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_661A)
    Sleep(50)

    def lambda_6637():
        OP_95(0xFE, -1300, 0, 19600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6637)
    Sleep(50)

    def lambda_6654():
        OP_95(0xFE, 300, 0, 19600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6654)
    OP_68(-500, 1000, 18800, 4000)
    FadeToBright(2000, 0)
    WaitChrThread(0x23, 1)

    def lambda_668C():
        OP_95(0xFE, -8500, -2800, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_668C)
    WaitChrThread(0x101, 1)

    def lambda_66AA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_66AA)
    WaitChrThread(0x102, 1)

    def lambda_66BB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_66BB)
    WaitChrThread(0x104, 1)

    def lambda_66CC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_66CC)
    WaitChrThread(0x103, 1)

    def lambda_66DD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_66DD)
    WaitChrThread(0x103, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#0100268V#12P#0005FDown there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100269V#12P#0105FWhy the underside of Station Street?\x01",
            "What could possibly be here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100270V#11P#0306FSounded like he had something lined\x01",
            "up for us to do.\x02\x03",
            "#0100271V#0301FDon't tell me he's expectin' us to\x01",
            "clean this place up or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100272V#5P#0200F...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x23, 1)
    Fade(1000)
    OP_68(-15500, -3900, 17500, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x23, -10500, -4000, 17500, 270)
    SetChrPos(0x101, -8500, -2300, 17000, 270)
    SetChrPos(0x102, -7540, -1800, 16100, 270)
    SetChrPos(0x103, -6900, -1500, 17800, 270)
    SetChrPos(0x104, -5900, -1300, 16700, 270)
    OP_68(-22500, -3900, 17500, 6000)
    MoveCamera(38, 16, 0, 6000)
    SetCameraDistance(17000, 6000)

    def lambda_68DF():
        OP_95(0x23, -19500, -5000, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_68DF)
    Sleep(300)

    def lambda_68FC():
        OP_95(0x101, -22500, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_68FC)
    Sleep(50)

    def lambda_6919():
        OP_95(0x102, -21540, -5000, 16100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6919)
    Sleep(50)

    def lambda_6936():
        OP_95(0x103, -20900, -5000, 17800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6936)
    Sleep(50)

    def lambda_6953():
        OP_95(0x104, -19900, -5000, 16700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6953)
    WaitChrThread(0x23, 1)

    def lambda_6971():
        OP_95(0xFE, -22500, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6971)
    WaitChrThread(0x23, 1)
    OP_93(0x23, 0x0, 0x2BC)
    WaitChrThread(0x101, 1)

    def lambda_699A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_699A)
    WaitChrThread(0x102, 1)

    def lambda_69AB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_69AB)
    WaitChrThread(0x103, 1)

    def lambda_69BC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_69BC)
    WaitChrThread(0x104, 1)

    def lambda_69CD():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_69CD)
    OP_93(0x23, 0xB4, 0x1F4)

    def lambda_69E1():

        label("loc_69E1")

        TurnDirection(0x101, 0x23, 500)
        Yield()
        Jump("loc_69E1")

    QueueWorkItem2(0x101, 2, lambda_69E1)

    def lambda_69F3():

        label("loc_69F3")

        TurnDirection(0x102, 0x23, 500)
        Yield()
        Jump("loc_69F3")

    QueueWorkItem2(0x102, 2, lambda_69F3)

    def lambda_6A05():

        label("loc_6A05")

        TurnDirection(0x103, 0x23, 500)
        Yield()
        Jump("loc_6A05")

    QueueWorkItem2(0x103, 2, lambda_6A05)

    def lambda_6A17():

        label("loc_6A17")

        TurnDirection(0x104, 0x23, 500)
        Yield()
        Jump("loc_6A17")

    QueueWorkItem2(0x104, 2, lambda_6A17)
    OP_6F(0x51)

    ChrTalk(
        0x23,
        (
            "#0100273V#5P#1003FBehind that door is the Geofront,\x01",
            "a vast network of tunnels running\x01",
            "underneath Crossbell City.\x02\x03",
            "#0100274V#1000FYour mission is to make your way\x01",
            "through it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#0100275V#12P#0005FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100276V#12P#0105FYou want us to go in there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100277V#11P#0301FYeah. What's this have to do with anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#0100278V#5P#1004FFor starters, it'll serve as a test to evaluate\x01",
            "your combat skills and overall aptitude.\x02\x03",
            "#0100279V#1002FThe Geofront is home to some pretty weak\x01",
            "monsters.\x02\x03",
            "#0100280VIt's your job to dispose of them and reach\x01",
            "its deepest section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100281V#12P#0100FThat makes more sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100282V#11P#0304FA combat test, huh? Fine by me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0100283V#12P#0011FW-Wait a second!\x02\x03",
            "#0100284V#0003FTest or not, why are WE the ones going\x01",
            "into an area infested with monsters?\x02\x03",
            "#0100285V#0001FIsn't that a job for the Guardian Force?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#0100286V#5P#1004FHeh. I'll admit that this isn't your typical\x01",
            "outing as a detective.\x02\x03",
            "#0100287V#1001FBut you're members of the SSS, making it\x01",
            "a different story altogether.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100288V#12P#0011FCome again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#0100289V#5P#1000FWe'll talk details later.\x02\x03",
            "#0100290VFirst things first.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x23, -22500, -5000, 18000, 2000, 0x0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Sergei handed over some kind of portable device\x01",
            "to Lloyd and the others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#0100291V#0005FWould this be...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#0100292V#0105FA new tactical orbment model, perhaps?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#0100293V#0305FDamn, it's pretty slick. I like it.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#0100294V#0203FA fifth-generation tactical orbment...\x01",
            "The Enigma.\x02\x03",
            "#0100295V#0200FIs it finally ready for combat?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    TurnDirection(0x23, 0x103, 250)
    OP_CA(0x1, 0x0, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis005.itp")

    ChrTalk(
        0x23,
        (
            "#0100296V#6P#1002FI guess so. The foundation shipped 'em\x01",
            "out a couple of days ago.\x02\x03",
            "#0100297VAnd they've already been adjusted to fit\x01",
            "your individual aptitudes.\x02\x03",
            "#0100298V#1004FAs for how to use them... Tio, you're up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100299V#11P#0203FIf I must.\x02\x03",
            "#0100300V#0200FWere you also supplied with quartz\x01",
            "for this particular model?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#0100301V#6P#1002FYeah. It's not much, but here you go.\x02",
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
            "Received \x07\x02",
            "quartz of each type\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TurnDirection(0x23, 0x101, 500)

    ChrTalk(
        0x23,
        "#0100302V#5P#1000FAlso, you won't get far without this.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x321),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x321, 1)

    ChrTalk(
        0x23,
        (
            "#0100303V#5P#1003FCome back to headquarters once you've\x01",
            "taken care of the monsters.\x02\x03",
            "#0100304VWe'll talk more after that.\x02\x03",
            "#0100305V#1005FOh, right. I better hand these over to\x01",
            "you, too.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(300)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "About the Detective Notebook:\x02\x03",
            "The Special Support Section automatically\x01",
            "records events that happen throughout\x01",
            "the game in the Detective Notebook.\x02\x03",
            "Check the contents by selecting\x01",
            "'Detective Notebook' after opening [ITEMS]\x01",
            "from the Camp Menu, or by pressing\x01",
            "[#165I + Left] on the field.\x02\x03",
            "You can also read the manual, so please\x01",
            "check it out.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "About the Combat Notebook:\x02\x03",
            "The Special Support Section automatically\x01",
            "records the data of each enemy you fight\x01",
            "in the Combat Notebook.\x02\x03",
            "Like the Detective Notebook, you can view\x01",
            "its contents by selecting 'Combat Notebook'\x01",
            "under [ITEMS], or by pressing\x01",
            "[#165I + Right] on the field.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1, 1)
    AddItemNumber(0x4, 1)
    OP_68(-19500, -3900, 17500, 3000)

    def lambda_77C1():
        OP_95(0xFE, -20000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_77C1)
    WaitChrThread(0x23, 1)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_77F1():
        OP_95(0xFE, -17500, -5000, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_77F1)
    Sound(1082, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0100306V#6P#0011FW-Wait! You're leaving, Chief?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x23, 1)
    OP_6F(0x1)
    TurnDirection(0x23, 0x101, 500)

    ChrTalk(
        0x23,
        (
            "#0100307V#11P#1002FOh, that reminds me, Lloyd.\x02\x03",
            "#0100308VI'm making you the leader of the team\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100309V#6P#0005FMe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#0100310V#11P#1004FYou're the only certified detective\x01",
            "here, so...\x02\x03",
            "#0100311VGood luck, kids.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x23, 0x5A, 0x1F4)

    def lambda_7947():
        OP_95(0xFE, -8500, -2800, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_7947)
    Sleep(2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitChrThread(0x23, 1)
    Fade(1000)
    OP_68(-21200, -3900, 17300, 0)
    MoveCamera(335, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrPos(0x101, -22500, -5000, 17300, 90)
    SetChrPos(0x102, -20900, -5000, 16000, 90)
    SetChrPos(0x103, -21500, -5000, 18600, 90)
    SetChrPos(0x104, -19900, -5000, 17300, 90)
    SetChrFlags(0x23, 0x80)
    OP_0D()

    def lambda_7A0D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7A0D)
    Sleep(50)

    def lambda_7A1D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A1D)
    Sleep(50)

    def lambda_7A2D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7A2D)
    WaitChrThread(0x103, 1)
    Sound(1362, 255, 100, 0)

    ChrTalk(
        0x104,
        (
            "#0100312V#12P#0309FHaha. Guess you drew the short\x01",
            "end of the stick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100313V#12P#0104FI do find it reassuring to have a\x01",
            "proper detective on the team.\x02\x03",
            "#0100314V#0102FPleasure to make your acquaintance,\x01",
            "Detective Bannings.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0100315V#0000F#5PSame...but could we maybe drop\x01",
            "the formalities?\x02\x03",
            "#0100316VI think we're about the same age,\x01",
            "and we are both rookies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100317V#12P#0100FI suppose so. I'm 18 myself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100318V#0000F#5PI had a feeling. So am I.\x02\x03",
            "#0100319V#0005FWhat about you two?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100320V#12P#0304FI'm 21, but you wouldn't ever catch me\x01",
            "caring about formalities.\x02\x03",
            "#0100321V#0300FNice to meet ya, Lloyd. Elie.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#0100322V#6P#0102FIt's a pleasure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100390V#0002F#5PYeah, likewise.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0100324V#6P#0001FI suppose that leaves you...\x01",
            "Would you mind telling us?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7D86():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7D86)
    Sleep(50)

    def lambda_7D96():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7D96)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x103,
        "#0100325V#11P#0203FFourteen. Will that be a problem?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#0100326V#6P#0012FNo, no. Of course not.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(1081, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0100327V#6P#0011F#4SF-FOURTEEN?!#3S\x02",
    )

    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100328V#12P#0309FSo you DO have a problem with it.\x01",
            "She looks the part, doesn't she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100329V#6P#0105FIt's hard to believe you're already\x01",
            "a police officer at that age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100330V#6P#0011FNo, back up! This doesn't make any sense,\x01",
            "no matter how you look at it!\x02\x03",
            "#0100331V#0006FYou have to be at least 16 before you can\x01",
            "join the police force.\x02\x03",
            "#0100332V#0001FHow can someone who's barely graduated\x01",
            "from Sunday School become a police off--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100333V#11P#0200FBecause I am not one, strictly speaking.\x02\x03",
            "#0100334VI was transferred here by the Epstein\x01",
            "Foundation for testing purposes.\x02",
        )
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0100335V#6P#0005FCome again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100336V#12P#0305FDidn't Epstein make these orbments\x01",
            "we just got?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100337V#6P#0104FOh, I think I understand.\x02\x03",
            "#0100338V#0100FI've heard that Crossbell City has been\x01",
            "cooperating with the foundation on a\x01",
            "large-scale project for several years.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#0100339V#5P#0200FCorrect. The Orbal Network Project.\x02\x03",
            "#0100340VWhile I do have some connection to\x01",
            "that, the real reason for my transfer\x01",
            "is this.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, -21500, -5000, 18800, 180)
    OP_0D()
    Sound(1268, 255, 100, 0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    Sleep(1000)

    AnonymousTalk(
        0x101,
        "#0100341V#0005FAnd that's...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#0100342V#0105FA mechanical...staff?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#0100343V#0204FIt is called an orbal staff.\x02\x03",
            "#0100344VI was transferred to test this weapon's\x01",
            "effectiveness in real combat scenarios.\x02\x03",
            "#0100345V#0200FDo you understand now, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    ChrTalk(
        0x101,
        (
            "#0100346V#6P#0001FBack up just a moment.\x02\x03",
            "#0100347VYou're telling me you're going to fight\x01",
            "with this thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100348V#11P#0203FFor a 'certified detective,' you are\x01",
            "exceptionally slow.\x02\x03",
            "#0100349V#0211FI believe I made myself clear.\x01",
            "What do you fail to comprehend?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100350V#6P#0011FUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100351V#12P#0304FC'mon, guys. Bickerin' like this won't\x01",
            "get us anywhere.\x02\x03",
            "#0100352V#0300FI dunno exactly how dangerous this\x01",
            "Geofront thing will be...\x02\x03",
            "#0100353V...so how about we come up with a\x01",
            "strategy before we head in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100354V#6P#0103FI'm still not sure how to feel about all of\x01",
            "this, but we should focus on our mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100355V#6P#0006FYou're right. Arguing is pointless.\x02\x03",
            "#0100356V#0000FI'm sorry, Tio. If I offended you in any\x01",
            "way, please accept my apologies.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Sound(804, 0, 100, 0)
    SetChrPos(0x103, -21500, -5000, 18600, 180)
    TurnDirection(0x103, 0x101, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#0100357V#11P#0203FIt is fine. Your reaction was justified,\x01",
            "given the situation.\x02\x03",
            "#0100358V#0200FNow, back on topic. As I said, I will\x01",
            "be utilizing my orbal staff to fight.\x02\x03",
            "#0100359VWhat weapons do you three use?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100360V#6P#0005FMy weapon of choice?\x02\x03",
            "#0100361V#0000FWell, I specialize in these.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 80, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -22700, -5000, 17300, 90)
    OP_0D()

    def lambda_891B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_891B)
    Sleep(50)

    def lambda_892B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_892B)
    Sleep(50)

    def lambda_893B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_893B)
    WaitChrThread(0x102, 1)
    Sound(1083, 255, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(1000)

    AnonymousTalk(
        0x102,
        "#0100362V#0105FSome sort of police batons?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#0100363V#0300FTonfas, eh? That's an Eastern weapon.\x02\x03",
            "#0100364VHeard they're specifically designed for\x01",
            "self-defense and suppression, rather\x01",
            "than offense.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
        "#0100365V#0102FI see. A fitting choice for\x01",
        "a police officer, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    SetChrPos(0x101, -22500, -5000, 17300, 90)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0100366V#0004F#5PI tried out other weapons, but\x01",
            "these felt the most natural.\x02\x03",
            "#0100367V#0000FSo, what about you, Elie? Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100368V#12P#0100FI'll be using this.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    OP_93(0x102, 0x0, 0x0)
    OP_0D()

    def lambda_8BB4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8BB4)
    Sleep(50)

    def lambda_8BC4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8BC4)
    Sleep(50)

    def lambda_8BD4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8BD4)
    WaitChrThread(0x103, 1)
    Sound(1173, 255, 100, 0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    Sleep(1000)

    AnonymousTalk(
        0x103,
        "#0100369V#0205FAn orbal gun. It appears slightly dated, though.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#0100370V#0005FMaybe, but you can't deny its charm.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#0100371V#0102FIt's something I continue to have\x01",
            "customized for competitive purposes.\x02\x03",
            "#0100372VIt may be an oldie, but its\x01",
            "precision is unparalleled.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#0100373V#11P#0302FNot bad, not bad.\x02\x03",
            "#0100374V#0300FNow, let me introduce you to my\x01",
            "partner in crime.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, -19500, -5000, 17300, 270)
    OP_0D()

    def lambda_8E05():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8E05)
    Sleep(50)

    def lambda_8E15():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8E15)
    Sleep(50)

    def lambda_8E25():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8E25)
    WaitChrThread(0x102, 1)
    Sound(1363, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(1000)

    AnonymousTalk(
        0x101,
        "#0100375V#0001FThat's...quite the large weapon.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#0100376V#0101FIt looks similar to the halberds used by\x01",
            "knights during the Middle Ages.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#0100377V#0200FI have seen them in the foundation's factories.\x02\x03",
            "#0100378VIt is equipped with a unit that converts orbal\x01",
            "energy into shockwaves.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#0100379V#0304FBingo. This baby's called a stun halberd.\x02\x03",
            "#0100380V#0300FIts weight can make it difficult to get\x01",
            "the hang of, but it's unmatched in\x01",
            "terms of raw power.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Fade(250)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    SetChrPos(0x104, -19900, -5000, 17300, 270)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0100381V#0003F#5PImpressive.\x02\x03",
            "#0100382V#0000FWhile I still don't quite know how\x01",
            "Tio's staff works yet...\x02\x03",
            "#0100383V...I think, overall, we make a pretty\x01",
            "balanced team.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9141():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9141)
    Sleep(50)

    def lambda_9151():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9151)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x102,
        "#0100384V#12P#0100FI think so, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100385V#12P#0300FThat's probably the reason the four of us\x01",
            "were put on this team in the first place.\x02\x03",
            "#0100386VThe chief may look like a bum, but there's\x01",
            "more to him than meets the eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100387V#11P#0203FI concur.\x02\x03",
            "#0100388V#0200FBefore I explain how it is my orbal\x01",
            "staff functions...\x02\x03",
            "#0100389V...should I first explain how our tactical\x01",
            "orbments work?\x02",
        )
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
            "Let her explain\x01",      # 0
            "Decline\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9346"),
        (1, "loc_A072"),
        (SWITCH_DEFAULT, "loc_A3CE"),
    )


    label("loc_9346")


    def lambda_934B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_934B)
    Sleep(50)

    def lambda_935B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_935B)
    Sleep(50)

    def lambda_936B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_936B)
    Sleep(50)

    ChrTalk(
        0x101,
        "#0100323V#0002F#5PThat'd be great\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100391V#11P#0203FVery well.\x02\x03",
            "#0100392V#0200FBasically, an orbment is a device that uses orbal\x01",
            "energy to generate various phenomena.\x02\x03",
            "#0100393VFrom simple lighting, cooling, and heating systems\x01",
            "to engines that power cars and trains--all of them\x01",
            "require energy output by orbments.\x02\x03",
            "#0100394VThe so-called tactical orbment is essentially a small,\x01",
            "portable orbment that is specifically designed to be\x01",
            "used in combat.\x02\x03",
            "#0100395V#0203FThe ones we received are the newest models, which\x01",
            "were developed by the Epstein Foundation.\x02\x03",
            "#0100396VLike its predecessors, it functions by drawing power\x01",
            "from crystal circuits called quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100397V#6P#0105FQuartz are created by processing septium fragments\x01",
            "known as sepith. Once made, they can be placed into\x01",
            "the actual orbments.\x02\x03",
            "#0100398V#0100FDidn't Chief Sergei hand you some before he left?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100399V#11P#0200FIndeed. All we have to do is set them\x01",
            "into the slots in our orbments.\x02\x03",
            "#0100400VThe elemental value and combination\x01",
            "of quartz will determine which orbal\x01",
            "arts are available to the user.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100401V#5P#0004FArts can be more effective than melee attacks,\x01",
            "depending on the monster.\x02\x03",
            "#0100402V#0000FThat's why we should properly configure each\x01",
            "of our orbments before tackling the Geofront.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100403V#6P#0100FThat's something to keep in mind\x01",
            "while we're engaged in combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100404V#12P#0304FEven the Bracer Guild and Guardian Force\x01",
            "use 'em. No reason why we shouldn't, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100405V#11P#0208FOne more thing.\x02\x03",
            "#0100406V#0200FTactical orbments are fine-tuned to each\x01",
            "individual user, meaning that the circuit\x01",
            "layout varies from person to person.\x02\x03",
            "#0100407VFor example, some slots are restricted to\x01",
            "quartz with a specific elemental attribute.\x01",
            "The sepith lines may differ as well.\x02\x03",
            "#0100408V#0203FIf we opened our orbments, we could see\x01",
            "that they are not identical.\x02\x03",
            "#0100409V#0200FAs for arts, it will be better to learn about\x01",
            "those during actual combat, so I will stop\x01",
            "my explanation here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100410V#6P#0102FThanks, Tio. That really cleared things up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100411V#11P#0203FYou are welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100412V#12P#0305FI got a quick question. These newer orbments\x01",
            "are pretty much just fancy older models, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100413V#11P#0203FCrude, but yes. If you are familiar with\x01",
            "older generation models, there should\x01",
            "not be much of a difference.\x02\x03",
            "#0100426V#0200FThe only major difference from the older\x01",
            "model is an additional function.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0100427V#5P#0005FAnd that would be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100428V#11P#0204FIt is unnecessary for this job, so explaining\x01",
            "would be a waste of time and energy.\x02\x03",
            "#0100417V#0200FLet us instead focus on the task at hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100418V#5P#0000FA-All right, then...\x01",
            "(That just makes me even more curious.)\x02\x03",
            "#0100419V#0004FOkay. Let's make sure our orbments\x01",
            "are ready before heading into the\x01",
            "Geofront.\x02\x03",
            "#0100420V#0000FOnce all of us have set our quartz,\x01",
            "we'll get our first mission underway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100432V#12P#0100FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100422V#12P#0300FTime to pop in some quartz!\x02",
    )

    CloseMessageWindow()
    AddItemNumber(0x64, 1)
    AddItemNumber(0x6A, 1)
    AddItemNumber(0x6D, 1)
    AddItemNumber(0x79, 1)
    FadeToDark(300, 0, 100)
    Sleep(300)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please set quartz for each party member's orbment.\x02\x03",
            "You can do this by selecting [ORBMENT] from the\x01",
            "Camp Menu and then selecting [QUARTZ].\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x44, 0)
    OP_C7(0x0, 0x80000)
    Jump("loc_A3CE")

    label("loc_A072")


    def lambda_A077():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A077)
    Sleep(50)

    def lambda_A087():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A087)
    Sleep(50)

    def lambda_A097():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A097)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#0100423V#5P#0000FI think we're good.\x02\x03",
            "#0100424VThey don't look too different from the\x01",
            "ones I'm familiar with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100425V#11P#0203FCorrect. Well, mostly.\x02\x03",
            "#0100414V#0200FThe only major difference from the older\x01",
            "model is an additional function.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0100415V#5P#0005FAnd that would be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100416V#11P#0204FIt is unnecessary for this job, so explaining\x01",
            "would be a waste of time and energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100429V#5P#0006F(That just makes me even more curious.)\x02\x03",
            "#0100430V#0000FWell, if everyone's ready, let's begin our\x01",
            "descent into the Geofront!\x02\x03",
            "#0100431VAnd remember: safety first!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100421V#12P#0100FOf course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100433V#11P#0200FRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100434V#12P#0300FLet's get this show on the road!\x02",
    )

    CloseMessageWindow()
    OP_42(0x0, 0x6D, 0x0)
    OP_42(0x1, 0x79, 0x0)
    OP_42(0x2, 0x64, 0x0)
    OP_42(0x3, 0x6A, 0x0)
    Jump("loc_A3CE")

    label("loc_A3CE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0x1, 0x0, 0x3)
    RemoveCraft(0x1, 0xFFFF)
    OP_38(0x1, 0x80, 0x1)
    OP_42(0x1, 0x3FC, 0xFF)
    OP_42(0x1, 0x5DC, 0xFF)
    OP_42(0x1, 0x640, 0xFF)
    AddCraft(0x1, 0xA0)
    AddCraft(0x1, 0xFF)
    SetChrChipPat(0x1, 0x6, 0xFF)
    OP_32(0x2, 0x0, 0x3)
    RemoveCraft(0x2, 0xFFFF)
    OP_38(0x2, 0x80, 0x1)
    OP_42(0x2, 0x410, 0xFF)
    OP_42(0x2, 0x5DC, 0xFF)
    OP_42(0x2, 0x640, 0xFF)
    AddCraft(0x2, 0xAA)
    AddCraft(0x2, 0x104)
    SetChrChipPat(0x2, 0x6, 0x104)
    OP_32(0x3, 0x0, 0x3)
    RemoveCraft(0x3, 0xFFFF)
    OP_38(0x3, 0x80, 0x1)
    OP_42(0x3, 0x424, 0xFF)
    OP_42(0x3, 0x5DC, 0xFF)
    OP_42(0x3, 0x640, 0xFF)
    AddCraft(0x3, 0xB4)
    AddCraft(0x3, 0x109)
    SetChrChipPat(0x3, 0x6, 0x109)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_68(-21000, -2800, 17500, 0)
    MoveCamera(45, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x0, -21000, -5000, 17500, 270)
    SetChrPos(0x1, -21000, -5000, 17500, 270)
    SetChrPos(0x2, -21000, -5000, 17500, 270)
    SetChrPos(0x3, -21000, -5000, 17500, 270)
    SetScenarioFlags(0x40, 2)
    OP_29(0x3C, 0x4, 0x2)
    OP_29(0x3C, 0x1, 0x0)
    OP_C5(0x1, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DE(0x0, 0x0)"), scpexpr(EXPR_END)), "loc_A6CF")
    Sleep(1500)
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You have earned the 'Noteworthy Beginning'\x01",
            "achievement for receiving the Detective Notebook.\x02\x03",
            "As you can see, during the game, you may unlock\x01",
            "'achievements' when fulfilling certain conditions.\x02\x03",
            "Unlocking achievements will net you points that you\x01",
            "can use to unlock various features after clearing the\x01",
            "game.\x02\x03",
            "You can check your achievements by selecting\x01",
            "[RECORD] under the [SYSTEM] menu in the\x01",
            "Camp Menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToBright(300, 0)

    label("loc_A6CF")

    EventEnd(0x5)
    Return()

    # Function_43_645E end

    def Function_44_A6D2(): pass

    label("Function_44_A6D2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("chr/ch02400.itc", 0x1F)
    LoadChrToIndex("apl/ch50010.itc", 0x20)
    LoadChrToIndex("apl/ch50011.itc", 0x21)
    SoundLoad(806)
    OP_68(-22500, -4100, 17300, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x102, -22000, -5000, 21000, 180)
    SetChrPos(0x101, -22000, -5000, 21000, 180)
    SetChrPos(0x103, -22000, -5000, 21000, 180)
    SetChrPos(0x104, -22000, -5000, 21000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x198, -17100, -5000, 19300, 135)
    SetChrPos(0x197, -18000, -5000, 19300, 135)

    def lambda_A7BE():

        label("loc_A7BE")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_A7BE")

    QueueWorkItem2(0x198, 2, lambda_A7BE)

    def lambda_A7D0():

        label("loc_A7D0")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_A7D0")

    QueueWorkItem2(0x197, 2, lambda_A7D0)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    SetChrChipByIndex(0x27, 0x1F)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x26, 0x4)
    ClearChrFlags(0x27, 0x4)
    SetChrPos(0x26, -16000, -5000, 17300, 270)
    SetChrPos(0x27, -18000, -5000, 17300, 90)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFC, 0xC3, 0xB6, 0x28, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis001.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")
    CreatePortrait(2, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    LoadEffect(0x0, "event\\eva02_00.eff")
    ClearMapObjFlags(0x0, 0x10)
    BeginChrThread(0x26, 3, 0, 45)
    SetCameraDistance(19500, 2000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x0)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 48)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 49)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 50)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#0100753V#6P#0005FWhat's going on?\x02",
    )

    CloseMessageWindow()
    OP_68(-16500, -4100, 17300, 2000)
    SetCameraDistance(19000, 2000)
    OP_6F(0x1)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("Woman")

    AnonymousTalk(
        0xFF,
        (
            "#0100754VWell, well, well, Arios! Accomplishing yet another\x01",
            "astounding feat, are we?\x02\x03",
            "#0100755VSaving these young boys from the jaws of mortal\x01",
            "danger, no thanks to our city's sloppy management\x01",
            "system? Brilliant!\x02\x03",
            "#0100756VIt's the perfect scoop for our next issue!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    ChrTalk(
        0x198,
        (
            "#0100757V#5PAwesome! Are we going\x01",
            "to be in the newspaper?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        (
            "#0100758V#1PI don't think this will end well for\x01",
            "us if our parents find out, Ryu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#0100759V#6P#1403FPlease don't make a scene, Grace.\x02\x03",
            "#0100760V#1400FWhile I can't deny the city's shoddy facility\x01",
            "management, these two children were in\x01",
            "the wrong as well.\x02\x03",
            "#0100761VAnd I don't appreciate biased news stories.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x26,
        "Woman",
        (
            "#0100762V#11P#2109FYou have the wrong idea, Arios. I'm merely\x01",
            "living up to my readers' lofty expectations! ♪\x02\x03",
            "#0100763V#2102FMy, oh, my. It looks like we have some new\x01",
            "contenders entering the ring, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100764V#0001F#5P...?!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x26, 0x3)
    OP_68(-20080, -4100, 17580, 2500)
    SetCameraDistance(19500, 2500)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)

    def lambda_ADCC():
        OP_96(0xFE, 0xFFFFB9B0, 0xFFFFEC78, 0x3E80, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_ADCC)
    WaitChrThread(0x26, 1)

    def lambda_ADEA():
        OP_96(0xFE, 0xFFFFB118, 0xFFFFEC78, 0x44C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_ADEA)
    Sleep(500)

    def lambda_AE07():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_AE07)
    WaitChrThread(0x26, 1)
    OP_6F(0x11)
    BeginChrThread(0x26, 3, 0, 46)

    NpcTalk(
        0x26,
        "Woman",
        (
            "#0100765V#11P#2104FThe first mission of the team that carries\x01",
            "the CPD's future on its back: the Special\x01",
            "Support Section!\x02\x03",
            "#0100766VAlas, these fledglings were unable to complete\x01",
            "their mission and had to rely, as per usual, on\x01",
            "the power of the heroic Bracer Guild!\x02\x03",
            "#0100767V#2110FWill this budding team, now aware of their\x01",
            "utter lack of experience, be able to overcome\x01",
            "the trials in store for them?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100768V#6P#0011FWh-What are you talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100769V#6P#0301F(Is this chick okay? All I hear is gibberish.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100770V#6P#0200F(Her demeanor suggests she is\x01",
            "a part of the mass media.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100771V#6P#0106F(She must be a journalist with\x01",
            "the Crossbell Times.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#0100772V#11P#1403FI'd appreciate it if you didn't disregard\x01",
            "their role in this, Grace.\x02\x03",
            "#0100773VThey were the ones who initially saved\x01",
            "the children, not me.\x02\x03",
            "#0100774V#1400FThough it's true that they failed to see\x01",
            "things through to the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100775V#6P#0001F...!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x26,
        "Woman",
        (
            "#0100776V#11P#2106FJust like I thought.\x02\x03",
            "#0100777V#2100FI can already taste the juicy tidbits waiting to\x01",
            "grace this article! Don't let the final product get\x01",
            "you down, though.\x02\x03",
            "#0100778V#2109FThink of it as motivation to improve yourselves!\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x26, 0x3)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    NpcTalk(
        0x26,
        "Woman",
        (
            "#0100779V#6P#2110FWell, then, Arios. How about an exclusive\x01",
            "one-on-one interview? For old times' sake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#0100780V#11P#1403FI'll pass. I've already told you\x01",
            "I'm not interested.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x27, 0x5A, 0x1F4)
    EndChrThread(0x198, 0x2)
    EndChrThread(0x197, 0x2)

    def lambda_B3C6():
        OP_97(0xFE, 0x2EE0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_B3C6)

    def lambda_B3E0():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_B3E0)

    def lambda_B3ED():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_B3ED)
    Sleep(400)
    BeginChrThread(0x198, 3, 0, 51)
    Sleep(400)
    BeginChrThread(0x197, 3, 0, 52)
    Sleep(400)

    def lambda_B40F():
        OP_97(0xFE, 0x3A98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_B40F)
    Sleep(4000)
    OP_68(-22500, -4000, 17300, 2000)
    MoveCamera(40, 23, 0, 2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(50)
    OP_64(0x102)
    Sleep(50)
    OP_64(0x103)
    Sleep(50)
    OP_64(0x104)
    OP_6F(0x1)
    WaitChrThread(0x27, 1)
    WaitChrThread(0x198, 3)
    WaitChrThread(0x197, 3)
    WaitChrThread(0x26, 1)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)

    ChrTalk(
        0x103,
        "#0100781V#6P#0211FWhat just happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100782V#0301F#6PY'know, making us out to be fools\x01",
            "really pisses me off.\x02\x03",
            "#0100783V#0306FThat said, she's definitely my type,\x01",
            "quirkiness aside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100784V#0106F#6PThat's not really the issue here.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#0100785V#0101F#5PSo, Lloyd. What do we do next?\x02",
    )

    CloseMessageWindow()

    def lambda_B611():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B611)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0100786V#11P#0005FOh, right.\x02\x03",
            "#0100787V#0006FWell, we technically accomplished the\x01",
            "mission Chief Sergei gave us, so let's\x01",
            "head back to the department for now.\x02\x03",
            "#0100788V#0008FWe'll have to file a report about the\x01",
            "kids while we're at it.\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0100789V#11P#0011FWhat's that sound?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0100790V#0005F#11PThe new orbment we were given?\x02\x03",
            "#0100791V#0001FDo these have communications\x01",
            "built in, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100792V#0203F#6PIs it not obvious?\x02\x03",
            "#0100793V#0200FPress the red button to switch to communication\x01",
            "mode. That will accept the incoming call, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100794V#0000F#11PThis one right here?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x2, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0100795V#0001FUmm. This is Lloyd Bannings.\x02\x03",
            "#0100796VChief Sergei, is that you?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2083, 255, 100, 0)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0100797V\x07\x05",
            "Ah, Lloyd!\x02\x03",
            "#0100798VIt's me! The receptionist you met at the\x01",
            "police department earlier today, that is.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0100799V\x07\x00",
            "#0005FOh, the one from this morning.\x02\x03",
            "#0100800V#0000FWhat's up? Is something wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Receptionist's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0100801V\x07\x05",
            "Well, the thing is...\x02\x03",
            "#0100802V...I'm going to need you to return\x01",
            "here as soon as possible.\x02\x03",
            "#0100803VThe vice commissioner wants to\x01",
            "have a word with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0100804V\x07\x00",
            "#0011FTh-The vice commissioner?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_CA(0x0, 0x2, 0x3)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    RemoveParty(0x96, 0x0)
    RemoveParty(0x97, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x326)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1160", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_A6D2 end

    def Function_45_BBCC(): pass

    label("Function_45_BBCC")

    Sleep(1000)

    label("loc_BBCF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BCC1")
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)

    def lambda_BBE7():
        OP_96(0xFE, 0xFFFFC180, 0xFFFFEC78, 0x4268, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_BBE7)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    Sleep(50)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x26, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)

    def lambda_BC58():
        OP_96(0xFE, 0xFFFFC180, 0xFFFFEC78, 0x44C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_BC58)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    Sleep(50)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x26, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_BBCF")

    label("loc_BCC1")

    Return()

    # Function_45_BBCC end

    def Function_46_BCC2(): pass

    label("Function_46_BCC2")

    Sleep(1000)

    label("loc_BCC5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BDB7")
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)

    def lambda_BCDD():
        OP_96(0xFE, 0xFFFFB118, 0xFFFFEC78, 0x4394, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_BCDD)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    Sleep(50)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x26, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)

    def lambda_BD4E():
        OP_96(0xFE, 0xFFFFB118, 0xFFFFEC78, 0x45EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_BD4E)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    Sleep(50)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x26, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_BCC5")

    label("loc_BDB7")

    Return()

    # Function_46_BCC2 end

    def Function_47_BDB8(): pass

    label("Function_47_BDB8")


    def lambda_BDBD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BDBD)

    def lambda_BDCE():
        OP_95(0xFE, -22000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BDCE)
    WaitChrThread(0x101, 1)

    def lambda_BDEC():
        OP_95(0xFE, -21700, -5000, 17100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BDEC)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_47_BDB8 end

    def Function_48_BE0D(): pass

    label("Function_48_BE0D")


    def lambda_BE12():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BE12)

    def lambda_BE23():
        OP_95(0xFE, -22000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE23)
    WaitChrThread(0x102, 1)

    def lambda_BE41():
        OP_95(0xFE, -22500, -5000, 17700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE41)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_48_BE0D end

    def Function_49_BE62(): pass

    label("Function_49_BE62")


    def lambda_BE67():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BE67)

    def lambda_BE78():
        OP_95(0xFE, -22000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BE78)
    WaitChrThread(0x103, 1)

    def lambda_BE96():
        OP_95(0xFE, -23900, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BE96)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_49_BE62 end

    def Function_50_BEB7(): pass

    label("Function_50_BEB7")


    def lambda_BEBC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BEBC)

    def lambda_BECD():
        OP_95(0xFE, -22000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BECD)
    WaitChrThread(0x104, 1)

    def lambda_BEEB():
        OP_95(0xFE, -22700, -5000, 19100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BEEB)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x5A, 0x1F4)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Return()

    # Function_50_BEB7 end

    def Function_51_BF18(): pass

    label("Function_51_BF18")


    def lambda_BF1D():
        OP_95(0xFE, -16000, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF1D)
    WaitChrThread(0xFE, 1)

    def lambda_BF3B():
        OP_97(0xFE, 0x2EE0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF3B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_51_BF18 end

    def Function_52_BF55(): pass

    label("Function_52_BF55")


    def lambda_BF5A():
        OP_95(0xFE, -16900, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF5A)
    WaitChrThread(0xFE, 1)

    def lambda_BF78():
        OP_97(0xFE, 0x2EE0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF78)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_52_BF55 end

    def Function_53_BF92(): pass

    label("Function_53_BF92")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28300.itc", 0x1E)
    LoadChrToIndex("chr/ch28400.itc", 0x1F)
    OP_68(10000, -2500, 2000, 0)
    MoveCamera(55, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(43000, 0)
    SetChrPos(0x101, -4500, -10300, -1900, 0)
    SetChrPos(0x102, -4500, -10300, -1900, 0)
    SetChrPos(0x103, -4500, -10300, -1900, 0)
    SetChrPos(0x104, -4500, -10300, -1900, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x28, 0x80)
    OP_78(0xB, 0x28)
    OP_49()
    SetChrPos(0x28, 40000, -11500, -11500, 0)
    OP_D3(0x28, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetChrChipByIndex(0x29, 0x1E)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)
    SetChrPos(0x29, 5000, 0, 0, 180)
    SetChrFlags(0x29, 0x8000)
    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    SetChrPos(0x2A, 5000, 0, -1800, 0)
    SetChrFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2B, 0x10)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    SetChrPos(0x2B, 0, 0, 22000, 180)
    SetChrFlags(0x2B, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -2400, 0, -8000, 270)
    SetChrFlags(0x9, 0x8000)
    BeginChrThread(0x9, 0, 0, 0)
    OP_11(0xF0, 0xF2, 0xFC, 0x14, 0x64, 0x0)
    OP_7D(0xC8, 0xDC, 0xE6, 0x0, 0x0)
    OP_11(0xF0, 0xF2, 0xFC, 0x1E, 0x6E, 0x1F40)
    OP_7D(0xDC, 0xF0, 0xFF, 0x0, 0x1F40)
    Sound(829, 0, 100, 0)
    OP_68(-5000, -2500, 2000, 10000)
    SetCameraDistance(48000, 10000)

    def lambda_C17B():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_C17B)
    FadeToBright(2000, 0)
    OP_0D()
    BeginChrThread(0x28, 3, 0, 54)
    Sleep(2000)
    Sound(451, 0, 100, 0)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0x28, 3)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 2)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_BF92 end

    def Function_54_C1F4(): pass

    label("Function_54_C1F4")


    def lambda_C1F9():
        OP_96(0xFE, 0xFFFEC780, 0xFFFFD314, 0xFFFFD314, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_C1F9)
    WaitChrThread(0x28, 1)
    Return()

    # Function_54_C1F4 end

    def Function_55_C213(): pass

    label("Function_55_C213")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-21900, -3900, 19000, 0)
    MoveCamera(37, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -21900, -5000, 22000, 180)
    SetChrPos(0x102, -21900, -5000, 22000, 180)
    SetChrPos(0x103, -21900, -5000, 22000, 180)
    SetChrPos(0x104, -21900, -5000, 22000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    SetCameraDistance(18000, 2000)
    FadeToBright(1000, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_C31E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C31E)

    def lambda_C32F():
        OP_96(0xFE, 0xFFFFA7B8, 0xFFFFEC78, 0x477C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C32F)
    Sleep(400)

    def lambda_C34C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C34C)

    def lambda_C35D():
        OP_96(0xFE, 0xFFFFACCC, 0xFFFFEC78, 0x477C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C35D)
    Sleep(400)

    def lambda_C37A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C37A)

    def lambda_C38B():
        OP_96(0xFE, 0xFFFFA7B8, 0xFFFFEC78, 0x4C90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C38B)
    Sleep(400)

    def lambda_C3A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C3A8)

    def lambda_C3B9():
        OP_96(0xFE, 0xFFFFACCC, 0xFFFFEC78, 0x4C90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C3B9)
    WaitChrThread(0x101, 1)
    OP_6F(0x10)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    Sleep(500)
    Sound(806, 2, 100, 0)
    Sleep(1000)

    def lambda_C3F7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C3F7)
    Sleep(50)

    def lambda_C407():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C407)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
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
        (
            "#0300113V#0005FLloyd Bannings of the Special Support\x01",
            "Section speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0300114V\x07\x05",
            "It's me.\x02\x03",
            "#0300115VHow are things going?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0300116V\x07\x00",
            "#0000FChief Sergei!\x02\x03",
            "#0300117V#0000FActually, we just eliminated the monster.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0300118V\x07\x05",
            "Perfect.\x02\x03",
            "#0300119VWhere are you now?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0300120V\x07\x00",
            "#0005FNear the exit of the Geofront. Why?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0300121V\x07\x05",
            "Heh. That's not too far away.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0300122V\x07\x00",
            "#0011FWhat?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0300123V\x07\x05",
            "I need you guys to investigate something\x01",
            "immediately.\x02\x03",
            "#0300124VDrop your support requests for now and\x01",
            "make it your top priority.\x02",
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
            "#0300125V\x07\x00",
            "#0001FGot it!\x02\x03",
            "#0300126VSo, uh, what is it that needs investigating?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0300127V\x07\x05",
            "Head over to the Downtown District on the double.\x01",
            "It's in the southeastern part of the city.\x02\x03",
            "#0300128VSome residents there contacted the police.\x02\x03",
            "#0300129VApparently, two delinquent gangs are at each\x01",
            "other's throats and are about to start a brawl.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0300130V\x07\x00",
            "#0005FWhat?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0300131V\x07\x05",
            "Stop them before there's trouble. Good luck.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(825, 0, 100, 0)
    Sleep(200)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0300132V\x07\x00",
            "#6P#0011FH-Hold on!\x02\x03",
            "#0300133VStopping a fight isn't exactly what I'd\x01",
            "call an investigati--\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x6)
    Sleep(200)

    ChrTalk(
        0x101,
        "#0300134V#6P#0013FHe hung up on me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0300135V#0105FThat was the chief? What'd he say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300136V#0302FI can tell it ain't gonna be fun, judging\x01",
            "by the look on your face.\x02",
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
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        "#0300137V#6P#0006FYou could say that.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd briefly explained what Sergei tasked\x01",
            "them with doing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0x102,
        "#0300138V#0101FDelinquent gangs in the Downtown District...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_END)), "loc_CC56")

    ChrTalk(
        0x104,
        (
            "#0300139V#0301FDidn't we run into some of those brats\x01",
            "when we were down there earlier?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCF9")

    label("loc_CC56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_END)), "loc_CCBB")

    ChrTalk(
        0x104,
        (
            "#0300140V#0301FWe went there earlier. Did you guys see\x01",
            "anyone that fits the bill?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCF9")

    label("loc_CCBB")


    ChrTalk(
        0x104,
        "#0300141V#0301FThe Downtown District? Never heard of it.\x02",
    )

    CloseMessageWindow()

    label("loc_CCF9")


    ChrTalk(
        0x103,
        (
            "#0300142V#0203F#5PAccording to the database...\x02\x03",
            "#0300143V#0200F...two rival gangs known as the Saber Vipers\x01",
            "and the Testaments recently formed downtown.\x02\x03",
            "#0300144VSkirmishes between the two of them are daily\x01",
            "occurrences now, it says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0300145V#6P#0005FReally? A whole lot has changed in the three\x01",
            "years I was gone, I guess.\x02\x03",
            "#0300146V#0003FWell, whatever. We should hurry there and\x01",
            "assess the situation.\x02\x03",
            "#0300147V#0001FWe have to find a way to calm them down\x01",
            "before the situation escalates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0300148V#0101FAgreed.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D00A")

    ChrTalk(
        0x104,
        "#0300149V#0305FWhere's this Downtown District at, anyway?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0300150V#6P#0000FAh, sorry. It's beyond that little bridge you\x01",
            "find at the southern tip of East Street.\x02\x03",
            "#0300151VWe should head there first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300152V#0300FGot'cha.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D03D")

    label("loc_D00A")


    ChrTalk(
        0x104,
        "#0300153V#0300FDowntown District it is, then!\x02",
    )

    CloseMessageWindow()

    label("loc_D03D")

    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -21900, -5000, 18000, 180)
    SetScenarioFlags(0x41, 7)
    OP_29(0x3E, 0x4, 0x2)
    OP_29(0x3E, 0x1, 0x0)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_55_C213 end

    def Function_56_D06B(): pass

    label("Function_56_D06B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1BB")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FOur first assignment is basically\x01",
            "your standard combat test.\x02\x03",
            "All right, everyone! Let's head into\x01",
            "the Geofront until we can't go any\x01",
            "deeper!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D151")

    ChrTalk(
        0x102,
        "#0100FUnderstood! Let's give it our all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D1A5")

    label("loc_D151")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D180")

    ChrTalk(
        0x103,
        "#0200FFocus, everyone.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D1A5")

    label("loc_D180")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1A5")

    ChrTalk(
        0x104,
        "#0300FYou got it!\x02",
    )

    CloseMessageWindow()

    label("loc_D1A5")

    Sleep(50)
    SetChrPos(0x0, -13150, -5000, 17120, 270)
    EventEnd(0x4)

    label("loc_D1BB")

    Return()

    # Function_56_D06B end

    def Function_57_D1BC(): pass

    label("Function_57_D1BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D2A9")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D25E")

    ChrTalk(
        0x101,
        (
            "#0000FThis is the city's south exit.\x02\x03",
            "We have work to finish inside the city,\x01",
            "so let's focus on that before anything\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_D293")

    label("loc_D25E")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's no reason to leave the city now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D293")

    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_D2A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D350")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FWe'll need to leave through the east exit\x01",
            "to get to Armorica Village.\x02\x03",
            "Let's turn around and head toward East Street.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_D350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D3EA")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FWe'll have to leave through the north exit\x01",
            "to get to Mainz.\x02\x03",
            "Let's head toward the Residential District.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_D3EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D4DF")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D48D")

    ChrTalk(
        0x101,
        (
            "#0000FWe aren't supposed to leave the city.\x02\x03",
            "KeA's safety is our top priority, and we can't\x01",
            "do anything to jeopardize that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_D4C9")

    label("loc_D48D")

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

    label("loc_D4C9")

    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_D4DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5DC")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D58B")

    ChrTalk(
        0x101,
        (
            "#0003FWe don't have time to leave the city now.\x02\x03",
            "We already have our hands full with the\x01",
            "Heiyue case, so let's deal with that first.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_D5C6")

    label("loc_D58B")

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

    label("loc_D5C6")

    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_D5DC")

    Return()

    # Function_57_D1BC end

    def Function_58_D5DD(): pass

    label("Function_58_D5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D663")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FThis is Crossbell Station. I don't think\x01",
            "we need to catch a train right now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_D663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D6EA")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FThis is Crossbell Station. I don't think\x01",
            "we need to catch a train right now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_D6EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D763")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FThis is Crossbell Station. I don't think\x01",
            "we need to catch a train right now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_D763")

    Return()

    # Function_58_D5DD end

    SaveToFile()

Try(main)
