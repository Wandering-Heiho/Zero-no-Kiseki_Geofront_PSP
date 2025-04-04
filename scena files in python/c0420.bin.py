from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0420.bin",                # FileName
        "c0420",                    # MapName
        "c0420",                    # Location
        0x0023,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 35, 0, 5, 0, 6],
    )

    BuildStringList((
        "c0420",                  # 0
        "Ilya",                   # 1
        "Rixia",                  # 2
        "Manager Balsamo",        # 3
        "Receptionist Rowland",   # 4
        "Troupe Leader Avan",     # 5
        "Heinz",                  # 6
        "Eugene",                 # 7
        "Theodor",                # 8
        "Nikolai",                # 9
        "Plie",                   # 10
        "Selene",                 # 11
        "Detective Dudley",       # 12
        "Detective Emma",         # 13
        "Lechter",                # 14
        "Sully",                  # 15
        "Detective",              # 16
        "Detective",              # 17
        "Spectator",              # 18
        "Spectator",              # 19
        "Spectator",              # 20
        "Spectator",              # 21
        "Girl",                   # 22
        "Spectator",              # 23
        "Spectator",              # 24
        "Spectator",              # 25
        "Spectator",              # 26
        "Mayor MacDowell",        # 27
        "Secretary Ernest",       # 28
    ))

    AddCharChip((
        "chr/ch05100.itc",                   # 00
        "chr/ch05200.itc",                   # 01
        "chr/ch25800.itc",                   # 02
        "chr/ch25900.itc",                   # 03
        "chr/ch27500.itc",                   # 04
        "chr/ch24200.itc",                   # 05
        "chr/ch28700.itc",                   # 06
        "chr/ch28800.itc",                   # 07
        "chr/ch28900.itc",                   # 08
        "chr/ch29000.itc",                   # 09
        "chr/ch29100.itc",                   # 0A
        "chr/ch36600.itc",                   # 0B
        "chr/ch36700.itc",                   # 0C
        "chr/ch36800.itc",                   # 0D
        "chr/ch09800.itc",                   # 0E
        "chr/ch00900.itc",                   # 0F
        "chr/ch30500.itc",                   # 10
        "chr/ch07400.itc",                   # 11
        "chr/ch10100.itc",                   # 12
        "chr/ch27600.itc",                   # 13
        "chr/ch27700.itc",                   # 14
        "chr/ch21600.itc",                   # 15
        "chr/ch21700.itc",                   # 16
        "chr/ch21900.itc",                   # 17
        "chr/ch33102.itc",                   # 18
        "chr/ch22302.itc",                   # 19
        "chr/ch33002.itc",                   # 1A
        "chr/ch33302.itc",                   # 1B
        "chr/ch22000.itc",                   # 1C
        "chr/ch32300.itc",                   # 1D
    ))

    DeclNpc(-209,    0,       15550,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-209,    0,       13819,   360,  261,  0x0, 0,   1,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(769,     15199,   -6840,   270,  389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(3710,    1799,    6079,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-1879,   9,       15239,   135,  261,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-66489,  0,       7329,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(64750,   0,       3480,    135,  389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-2549,   1250,    19700,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(64750,   0,       3480,    135,  261,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(2250,    0,       14750,   270,  389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-68129,  0,       2140,    270,  389,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(209,     0,       15229,   270,  389,  0x0, 0,   15,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(1019,    0,       14640,   270,  389,  0x0, 0,   16,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-22120,  15199,   6940,    45,   389,  0x0, 0,   17,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(67370,   0,       2470,    90,   389,  0x0, 0,   18,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-21100,  15199,   5230,    0,    389,  0x0, 0,   19,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-26899,  15199,   6300,    0,    389,  0x0, 0,   20,  0,   0,   4,   0,   29,  255,  0)
    DeclNpc(-2690,   15199,   -7989,   0,    389,  0x0, 0,   21,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(-3779,   15199,   -8229,   0,    389,  0x0, 0,   22,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(-3450,   15199,   -3289,   0,    389,  0x0, 0,   23,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(-8149,   15350,   -3289,   45,   469,  0x0, 0,   24,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(-7150,   15350,   -3680,   0,    469,  0x0, 0,   25,  0,   255, 255, 0,   34,  255,  0)
    DeclNpc(2069,    15350,   -4349,   0,    469,  0x0, 0,   26,  0,   255, 255, 0,   35,  255,  0)
    DeclNpc(3170,    15350,   -4349,   0,    469,  0x0, 0,   27,  0,   255, 255, 0,   36,  255,  0)
    DeclNpc(8800,    15199,   -6800,   315,  405,  0x0, 0,   29,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(7789,    15199,   -5789,   135,  389,  0x0, 0,   28,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 39,  0.0,                   11.880000114440918,    0.0,                   14.0625,               [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.4000000059604645,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -4.752000331878662,    -0.0,                  1.0])

    ScpFunction((
        "Function_0_594",          # 00, 0
        "Function_1_64C",          # 01, 1
        "Function_2_677",          # 02, 2
        "Function_3_774",          # 03, 3
        "Function_4_7C7",          # 04, 4
        "Function_5_7F2",          # 05, 5
        "Function_6_C4C",          # 06, 6
        "Function_7_D5B",          # 07, 7
        "Function_8_1A7C",         # 08, 8
        "Function_9_1C5D",         # 09, 9
        "Function_10_1DD0",        # 0A, 10
        "Function_11_1F47",        # 0B, 11
        "Function_12_2A54",        # 0C, 12
        "Function_13_2DFB",        # 0D, 13
        "Function_14_2FE1",        # 0E, 14
        "Function_15_3464",        # 0F, 15
        "Function_16_358A",        # 10, 16
        "Function_17_3B48",        # 11, 17
        "Function_18_3CE1",        # 12, 18
        "Function_19_3DFB",        # 13, 19
        "Function_20_3F61",        # 14, 20
        "Function_21_43DA",        # 15, 21
        "Function_22_50B0",        # 16, 22
        "Function_23_534D",        # 17, 23
        "Function_24_5499",        # 18, 24
        "Function_25_55DC",        # 19, 25
        "Function_26_58F1",        # 1A, 26
        "Function_27_5F51",        # 1B, 27
        "Function_28_6099",        # 1C, 28
        "Function_29_6160",        # 1D, 29
        "Function_30_6390",        # 1E, 30
        "Function_31_63F5",        # 1F, 31
        "Function_32_6489",        # 20, 32
        "Function_33_64D2",        # 21, 33
        "Function_34_667E",        # 22, 34
        "Function_35_66D1",        # 23, 35
        "Function_36_6888",        # 24, 36
        "Function_37_6A28",        # 25, 37
        "Function_38_6AD4",        # 26, 38
        "Function_39_6B57",        # 27, 39
        "Function_40_79B1",        # 28, 40
        "Function_41_79DE",        # 29, 41
        "Function_42_7A0B",        # 2A, 42
        "Function_43_7A22",        # 2B, 43
        "Function_44_7A39",        # 2C, 44
        "Function_45_7A42",        # 2D, 45
        "Function_46_7A4B",        # 2E, 46
        "Function_47_7A54",        # 2F, 47
        "Function_48_7A5D",        # 30, 48
        "Function_49_7A8A",        # 31, 49
        "Function_50_7AB7",        # 32, 50
        "Function_51_7ACE",        # 33, 51
        "Function_52_7AE5",        # 34, 52
        "Function_53_7B04",        # 35, 53
        "Function_54_7B23",        # 36, 54
        "Function_55_7B42",        # 37, 55
        "Function_56_7B61",        # 38, 56
        "Function_57_7B9A",        # 39, 57
        "Function_58_7BD3",        # 3A, 58
        "Function_59_7E09",        # 3B, 59
        "Function_60_7E32",        # 3C, 60
        "Function_61_9BEB",        # 3D, 61
        "Function_62_9C36",        # 3E, 62
        "Function_63_9EE9",        # 3F, 63
        "Function_64_9F10",        # 40, 64
        "Function_65_B739",        # 41, 65
        "Function_66_B970",        # 42, 66
        "Function_67_BBDE",        # 43, 67
        "Function_68_BC09",        # 44, 68
        "Function_69_BC34",        # 45, 69
    ))


    def Function_0_594(): pass

    label("Function_0_594")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5D4"),
        (1, "loc_5E0"),
        (2, "loc_5EC"),
        (3, "loc_5F8"),
        (4, "loc_604"),
        (5, "loc_610"),
        (6, "loc_61C"),
        (SWITCH_DEFAULT, "loc_628"),
    )


    label("loc_5D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_5E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_5EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_5F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_604")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_610")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_61C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_628")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_634")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_64B")

    Return()

    # Function_0_594 end

    def Function_1_64C(): pass

    label("Function_1_64C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_676")
    OP_94(0xFE, 0xF4D8, 0x532, 0x1054A, 0x15AE, 0x3E8)
    Sleep(300)
    Jump("Function_1_64C")

    label("loc_676")

    Return()

    # Function_1_64C end

    def Function_2_677(): pass

    label("Function_2_677")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_773")
    OP_95(0xFE, -2550, 1250, 19700, 5000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x2EE)
    Sleep(300)
    BeginChrThread(0xFE, 1, 0, 53)
    OP_9D(0xFE, 0xFFFFF830, 0x4E2, 0x4CF4, 0x12C, 0x5DC)
    OP_9D(0xFE, 0xFFFFFC18, 0x4E2, 0x4CF4, 0x1F4, 0x3E8)
    BeginChrThread(0xFE, 1, 0, 52)
    OP_9D(0xFE, 0x7D0, 0x4E2, 0x4CF4, 0x2BC, 0x2BC)
    EndChrThread(0xFE, 0x1)
    OP_95(0xFE, 2550, 1250, 19700, 5000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x2EE)
    Sleep(300)
    BeginChrThread(0xFE, 1, 0, 53)
    OP_9D(0xFE, 0x7D0, 0x4E2, 0x4CF4, 0x12C, 0x5DC)
    OP_9D(0xFE, 0x3E8, 0x4E2, 0x4CF4, 0x1F4, 0x3E8)
    BeginChrThread(0xFE, 1, 0, 52)
    OP_9D(0xFE, 0xFFFFF830, 0x4E2, 0x4CF4, 0x2BC, 0x2BC)
    EndChrThread(0xFE, 0x1)
    Jump("Function_2_677")

    label("loc_773")

    Return()

    # Function_2_677 end

    def Function_3_774(): pass

    label("Function_3_774")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C6")
    OP_95(0xFE, 61750, 0, 3480, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x2EE)
    Sleep(300)
    OP_95(0xFE, 66750, 0, 3480, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x2EE)
    Sleep(300)
    Jump("Function_3_774")

    label("loc_7C6")

    Return()

    # Function_3_774 end

    def Function_4_7C7(): pass

    label("Function_4_7C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7F1")
    OP_94(0xFE, 0xFFFF9C32, 0x1C0C, 0xFFFF8F8A, 0x1108, 0x3E8)
    Sleep(300)
    Jump("Function_4_7C7")

    label("loc_7F1")

    Return()

    # Function_4_7C7 end

    def Function_5_7F2(): pass

    label("Function_5_7F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_808")
    Event(0, 64)
    Jump("loc_819")

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_819")
    Event(0, 69)

    label("loc_819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_828")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 60)

    label("loc_828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_880")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0xD, -65800, 0, 6680, 0)
    SetChrPos(0x16, -66490, 0, 7330, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87B")
    SetChrFlags(0xD, 0x10)

    label("loc_87B")

    Jump("loc_C4B")

    label("loc_880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_901")
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x9, 0, 0, 14000, 0)
    SetChrPos(0x8, 750, 0, 15500, 225)
    SetChrPos(0xC, -750, 0, 15500, 135)
    SetChrPos(0x16, -68150, 0, 2150, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FC")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -2250, 0, 14250, 90)

    label("loc_8FC")

    Jump("loc_C4B")

    label("loc_901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_93B")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x16, 0x80)
    TurnDirection(0xC, 0x8, 0)
    TurnDirection(0x8, 0xC, 0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x8, 0x10)
    Jump("loc_C4B")

    label("loc_93B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_9AF")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0xC, -21940, 15200, 4850, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97D")
    SetChrFlags(0xC, 0x10)

    label("loc_97D")

    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_C4B")

    label("loc_9AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A2E")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xA, -20, 0, 14380, 315)
    SetChrPos(0xE, -910, 1250, 25550, 90)
    SetChrPos(0xF, 940, 1250, 25550, 270)
    SetChrPos(0x10, 66420, 0, 1580, 90)
    SetChrFlags(0xC, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A29")
    SetChrFlags(0xE, 0x10)

    label("loc_A29")

    Jump("loc_C4B")

    label("loc_A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A55")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_C4B")

    label("loc_A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_A63")
    Jump("loc_C4B")

    label("loc_A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_B32")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0xC, -1940, 900, 10160, 0)
    SetChrPos(0x8, 1860, 900, 10150, 0)
    SetChrPos(0xE, -5140, 1350, 8470, 0)
    SetChrPos(0x10, 0, 1250, 22620, 180)
    SetChrPos(0xD, 960, 1800, 6150, 0)
    SetChrPos(0x13, 2670, 15200, -7100, 0)
    SetChrPos(0x14, 1690, 15200, -8109, 0)
    SetChrChipByIndex(0xF, 0xC)
    SetChrChipByIndex(0x10, 0xD)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x14, 0x10)
    BeginChrThread(0xF, 0, 0, 2)
    Jump("loc_C4B")

    label("loc_B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_B8A")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    TurnDirection(0xC, 0x13, 0)
    SetChrPos(0x9, -68120, 0, 2180, 270)
    SetChrChipByIndex(0xE, 0xB)
    BeginChrThread(0xE, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B85")
    SetChrFlags(0xE, 0x10)

    label("loc_B85")

    Jump("loc_C4B")

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_BDB")
    SetChrFlags(0x10, 0x80)
    TurnDirection(0xC, 0x8, 0)
    TurnDirection(0x8, 0xC, 0)
    SetChrChipByIndex(0x9, 0xE)
    SetChrPos(0x9, 4150, 1250, 24490, 225)
    SetChrPos(0xD, 3170, 1250, 23150, 45)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_C4B")

    label("loc_BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_C31")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xC, -700, 15200, -6830, 90)
    SetChrPos(0x8, 650, 1250, 25470, 270)
    SetChrPos(0xD, -650, 1250, 25470, 90)
    SetChrFlags(0x10, 0x10)
    BeginChrThread(0x10, 0, 0, 3)
    Jump("loc_C4B")

    label("loc_C31")

    BeginChrThread(0x10, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4B")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_C4B")

    Return()

    # Function_5_7F2 end

    def Function_6_C4C(): pass

    label("Function_6_C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C64")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C7B")

    label("loc_C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C7B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x213), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_CA3")
    SetMapObjFrame(0xFF, "pos01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pos02", 0x1, 0x1)
    Jump("loc_CBD")

    label("loc_CA3")

    SetMapObjFrame(0xFF, "pos01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "pos02", 0x0, 0x1)

    label("loc_CBD")

    SetMapObjFlags(0x1C, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD7")
    ClearMapObjFlags(0x1C, 0x4)

    label("loc_CD7")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_CEA")
    Jump("loc_D02")

    label("loc_CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D02")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D3A")
    OP_52(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xF, -2550, 1250, 19700, 0)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x1)
    BeginChrThread(0xF, 0, 0, 2)

    label("loc_D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5A")
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_D5A")

    Return()

    # Function_6_C4C end

    def Function_7_D5B(): pass

    label("Function_7_D5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DFB")

    ChrTalk(
        0xC,
        (
            "I think we'll manage to scrape by\x01",
            "on today's performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Nikolai returning right about now would\x01",
            "be the best-case scenario, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A78")

    label("loc_DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E0C")
    Call(0, 12)
    Jump("loc_1A78")

    label("loc_E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_FDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EE8")

    ChrTalk(
        0xC,
        (
            "I'm showing one of our special guests\x01",
            "to their seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I have to say, he's a bit of a strange one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What kind of connections does he\x01",
            "have to be considered a 'special\x01",
            "guest' at his age?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD5")

    label("loc_EE8")

    OP_4B(0x15, 0xFF)

    ChrTalk(
        0x15,
        (
            "#3509FOh, man! This view is pretty sick,\x01",
            "don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hahaha... There's still ten minutes until\x01",
            "the performance starts, so sit tight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hope you enjoy 'Golden Sun, Silver\x01",
            "Moon' to your heart's content.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 0)
    OP_4C(0x15, 0xFF)

    label("loc_FD5")

    Jump("loc_1A78")

    label("loc_FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1196")
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1080")

    ChrTalk(
        0xC,
        (
            "I'm not particularly against performing\x01",
            "internationally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sorry about that, Balsamo. Could you\x01",
            "look into it for me one more time?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118D")

    label("loc_1080")


    ChrTalk(
        0xC,
        "Speaking of business...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...I was touched by Kilika's story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's clear that she understands the\x01",
            "artistry that goes into Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm sorry, Balsamo, but could you\x01",
            "look into it for me one more time?\x01",
            "I apologize for making you do all the work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_118D")

    OP_4C(0xA, 0xFF)
    Jump("loc_1A78")

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1362")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_124E")

    ChrTalk(
        0xC,
        (
            "Ilya's guidance has been fostering\x01",
            "Rixia's rapid improvement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We'll be able to put on an amazing show if\x01",
            "the rest of the members follow their example.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_135D")

    label("loc_124E")


    ChrTalk(
        0xC,
        "Oh, you've all come.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We've been running into one problem\x01",
            "after another, but as they say in\x01",
            "showbiz...the show must go on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Rixia's acting skills have been\x01",
            "growing at a steady rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hope that everybody else continues\x01",
            "to strive to improve like her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_135D")

    Jump("loc_1A78")

    label("loc_1362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_15DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1443")

    ChrTalk(
        0xC,
        (
            "(These First Division detectives made\x01",
            "it out here pretty quickly to start their\x01",
            "investigation this morning.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "(Why'd Ilya have to sleep in today\x01",
            "of all days? She's making my\x01",
            "anxiety flare up.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D9")

    label("loc_1443")

    OP_4B(0x13, 0xFF)
    TurnDirection(0xC, 0x13, 0)

    ChrTalk(
        0xC,
        "You want floor plans for the theater?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There should be one inside of our\x01",
            "information pamphlets...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#0603FThat won't do. I need the floor plans from when\x01",
            "the theater was built.\x02\x03",
            "#0600FAny entrances, loading docks, storage rooms,\x01",
            "the stage design, and even the placement of\x01",
            "the ventilation ducts... All of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I-I understand, sir. I'll start looking for\x01",
            "them immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x0, 0)

    label("loc_15D9")

    Jump("loc_1A78")

    label("loc_15DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_16C2")

    ChrTalk(
        0xC,
        (
            "At any rate, identifying the veracity of\x01",
            "these claims has been helpful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I appreciate your collaboration in the matter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll have the tickets delivered to you\x01",
            "later. I hope you'll look forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A78")

    label("loc_16C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_18B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_177D")

    ChrTalk(
        0xC,
        (
            "I get overloaded with administrative work\x01",
            "as we get ready to perform our new play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hope that threat letter was nothing\x01",
            "more than a mere childish prank.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B3")

    label("loc_177D")


    ChrTalk(
        0xC,
        (
            "Our new show is absurdly popular.\x01",
            "We're anticipating the theater to be\x01",
            "even more packed than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And for that reason, I want to be prepared\x01",
            "to welcome all customers while with\x01",
            "everything running smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We can't even complete any basic tasks\x01",
            "without calling an over complicated meeting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_18B3")

    Jump("loc_1A78")

    label("loc_18B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_194F")

    ChrTalk(
        0xC,
        (
            "I feel reassured knowing the police have\x01",
            "agreed to investigate the matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll leave the threat letter in your\x01",
            "capable hands.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A78")

    label("loc_194F")


    ChrTalk(
        0xC,
        (
            "I wish Ilya would treat this situation just a\x01",
            "little more seriously, considering the letter\x01",
            "is targeting her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ahem! Regardless, we'll leave the matter\x01",
            "in your capable hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm counting on you to see this through\x01",
            "to the end. Please contact me if you\x01",
            "find out any information.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A78")

    TalkEnd(0xFE)
    Return()

    # Function_7_D5B end

    def Function_8_1A7C(): pass

    label("Function_8_1A7C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1B8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9A")
    Call(0, 9)
    Jump("loc_1B85")

    label("loc_1A9A")


    ChrTalk(
        0xA,
        (
            "I've actually been looking into holding\x01",
            "a performance in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Kilika came to visit us from the Republic\x01",
            "and gave us a persuasive proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm going to look into it one more time.\x01",
            "It might be worth considering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B85")

    Jump("loc_1C59")

    label("loc_1B8A")


    ChrTalk(
        0xA,
        (
            "I don't know if that letter was the real\x01",
            "deal. But as the manager, it's my\x01",
            "duty to ensure everyone's safety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It may be a smart idea to bolster\x01",
            "the patrolling efforts before the\x01",
            "performance starts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C59")

    TalkEnd(0xFE)
    Return()

    # Function_8_1A7C end

    def Function_9_1C5D(): pass

    label("Function_9_1C5D")


    ChrTalk(
        0xFE,
        "Oh, have you met our new assistant yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Her name is Sully. Please treat her as\x01",
            "you would any of our other members.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1DCC")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D40")

    ChrTalk(
        0x102,
        (
            "#0100FIt looks like she's managing\x01",
            "to handle herself just fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCC")

    label("loc_1D40")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D82")

    ChrTalk(
        0x103,
        "#0200FShe appears to be adjusting well.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DCC")

    label("loc_1D82")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DCC")

    ChrTalk(
        0x104,
        "#0300FHeh. Looks like she's doin' a swell job to me.\x02",
    )

    CloseMessageWindow()

    label("loc_1DCC")

    SetScenarioFlags(0xD1, 6)
    Return()

    # Function_9_1C5D end

    def Function_10_1DD0(): pass

    label("Function_10_1DD0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E9A")

    ChrTalk(
        0xB,
        (
            "I help out with the preparations needed\x01",
            "to run practice sessions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We have less than two weeks left until\x01",
            "the private performance. Everyone's\x01",
            "working on the finishing touches.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F43")

    label("loc_1E9A")


    ChrTalk(
        0xB,
        "Let's see... The lighting for the next scene...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Not good. The First Division's investigation\x01",
            "is disrupting our work and causing us to\x01",
            "fall behind schedule.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1F43")

    TalkEnd(0xFE)
    Return()

    # Function_10_1DD0 end

    def Function_11_1F47(): pass

    label("Function_11_1F47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2215")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1FE6")

    ChrTalk(
        0x8,
        (
            "#1701FCome to think of it, Nikolai WAS acting\x01",
            "kinda weird last night.\x02\x03",
            "#1706FYeah, the pieces are starting to fit\x01",
            "together now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2210")

    label("loc_1FE6")


    ChrTalk(
        0x8,
        (
            "#1706FCome to think of it, Nikolai WAS acting\x01",
            "kinda weird last night.\x02\x03",
            "#1701FAlmost like he was high or something...\x01",
            "Gave me a pretty nasty glare, too.\x02\x03",
            "#1709FYou'd better believe I shot an equally\x01",
            "nasty one right back at him!\x02",
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
        (
            "#0012FI'm not sure what else I was expecting\x01",
            "you to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108FIt's a bit surprising that he'd give Ilya\x01",
            "such attitude, considering who she is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FYeah. Doesn't sound like much of a\x01",
            "rookie to me at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2210")

    Jump("loc_2A50")

    label("loc_2215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2226")
    Call(0, 12)
    Jump("loc_2A50")

    label("loc_2226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_22A0")

    ChrTalk(
        0x8,
        (
            "#1701F#11PThere we go! Put more spunk\x01",
            "into it!\x02\x03",
            "Yeah, feel the rhythm! Get some bounce\x01",
            "into your step!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A50")

    label("loc_22A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_239F")

    ChrTalk(
        0x8,
        (
            "#1703FIt's a shame I can't put my favorite\x01",
            "little guy in charge, though.\x02\x03",
            "#1700FEh, whatever. Not much I can do about it.\x02\x03",
            "#1706F*sigh* I was expecting it to be a minor\x01",
            "annoyance, but this thing's growing to\x01",
            "be a real pain in the butt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A50")

    label("loc_239F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2760")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2450")

    ChrTalk(
        0x8,
        (
            "#1704FRixia's still growing as an artist, but\x01",
            "I'm expecting greatness outta her.\x02\x03",
            "#1702FHaha. I'll have to up my efforts and\x01",
            "reach new heights, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_275B")

    label("loc_2450")


    ChrTalk(
        0x8,
        (
            "#1703FI'm sure one of my solo performances could\x01",
            "easily leave the entire audience stunned.\x02\x03",
            "#1700FBut seriously, Rixia's acting has its own\x01",
            "qualities that deserve to be seen.\x02\x03",
            "She pushes me to raise the bar for myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FWhoa... Is she seriously that good?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FCan't say she really gives me the\x01",
            "impression of a celebrity, despite\x01",
            "gettin' picked to co-star.\x02\x03",
            "#0309FActually, I'd say she's soothing,\x01",
            "and I kinda like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1702FHeh, you got that right. That girl\x01",
            "is a top-tier piece of work.\x02\x03",
            "#1704FI don't think she's realized it, but\x01",
            "she's got as much potential as I.\x02\x03",
            "#1701FWho knows? Maybe she'll even end up\x01",
            "dethroning me some day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FSh-She's that talented?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0204FRixia has piqued my interest. I would\x01",
            "like to watch her perform once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_275B")

    Jump("loc_2A50")

    label("loc_2760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2A4D")

    ChrTalk(
        0x8,
        (
            "#1704FOur new play's going to rock\x01",
            "your socks off, my friends.\x02\x03",
            "#1702FIt contrasts me, symbolizing the sun,\x01",
            "and Rixia, who symbolizes the moon.\x02\x03",
            "Our two lights have an intense clash,\x01",
            "but soon join together and become\x01",
            "as one on the stage.\x02\x03",
            "#1709FThere's not much time until we debut,\x01",
            "so we gotta hurry it up!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A48")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2906")

    ChrTalk(
        0x101,
        (
            "#0012F(Well, looks like her mind's drifted\x01",
            "off into theatreland.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A45")

    label("loc_2906")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2967")

    ChrTalk(
        0x102,
        (
            "#0102F(Her mind must be filled with nothing\x01",
            "other than the performance.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A45")

    label("loc_2967")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B8")

    ChrTalk(
        0x103,
        (
            "#0202F(Her focus must be entirely on\x01",
            "the upcoming play.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A45")

    label("loc_29B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A45")

    ChrTalk(
        0x104,
        (
            "#0309F(Totally unsurprised that our dear Ilya\x01",
            "has probably gone and forgotten all\x01",
            "about that threatenin' letter already.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A45")

    SetScenarioFlags(0x0, 3)

    label("loc_2A48")

    Jump("loc_2A50")

    label("loc_2A4D")

    Call(0, 13)

    label("loc_2A50")

    TalkEnd(0xFE)
    Return()

    # Function_11_1F47 end

    def Function_12_2A54(): pass

    label("Function_12_2A54")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2BA5")

    ChrTalk(
        0xC,
        "Oh, yeah. About our earlier conversation...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1705F#11PYou mean the one about Nikolai?\x02\x03",
            "#1706FHe was definitely being a weirdo,\x01",
            "but I do think that his role in the\x01",
            "play's a tad unbalanced.\x02\x03",
            "#1709FOh, I know! Why don't we add a fight\x01",
            "scene between him and Theodor?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "*sigh* Cut me some slack, will you?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DF2")

    label("loc_2BA5")


    ChrTalk(
        0x8,
        (
            "#1703F#11PUh, I don't think I can pull off that\x01",
            "kind of acting.\x02\x03",
            "#1701FIf we're going to add a scene, it should\x01",
            "be something that's going to win over\x01",
            "our dear audience's hearts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Be that as it may, I don't want the\x01",
            "play to get sidetracked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I understand where you're coming from,\x01",
            "but could you think about it some more?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1706F#11PNot a chance.\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "I thought you might say that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(I believe they are holding a discussion\x01",
            "regarding the play...and the troupe\x01",
            "leader is distressed.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(I think we'd better leave them alone.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2DF2")

    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_12_2A54 end

    def Function_13_2DFB(): pass

    label("Function_13_2DFB")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x8,
        (
            "#1702FLet's continue where we left off, Rixia.\x02\x03",
            "#1704FYou have to try and go with the flow when\x01",
            "you perform with another person.\x02\x03",
            "It won't go well if you try too hard to force your\x01",
            "own pace or match your partner's pace.\x02\x03",
            "#1700FAll you can really do is let it all happen\x01",
            "naturally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "She's right, you know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We don't have much time left, so you might\x01",
            "as well try it out together on stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1800FO-Okay! Please let me know how I do.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_2DFB end

    def Function_14_2FE1(): pass

    label("Function_14_2FE1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3152")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3080")

    ChrTalk(
        0x9,
        (
            "#1806FNikolai's been giving off some strange\x01",
            "vibes lately... It's almost as if his\x01",
            "personality has suddenly changed.\x02\x03",
            "#1808F...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_314D")

    label("loc_3080")


    ChrTalk(
        0x9,
        (
            "#1806FNikolai's been giving off some strange\x01",
            "vibes lately...\x02\x03",
            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI know you're worried, Rixia. We'll get\x01",
            "to the bottom of this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1810FRight... Thank you for trying\x01",
            "to reassure me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_314D")

    Jump("loc_3460")

    label("loc_3152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3385")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3223")

    ChrTalk(
        0x9,
        (
            "#1806FWith the private performance closing in,\x01",
            "I get all flustered and anxious if I don't\x01",
            "constantly practice.\x02\x03",
            "#1810FIlya showed up late today, so I can't help\x01",
            "but feel impatient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3380")

    label("loc_3223")


    ChrTalk(
        0x9,
        (
            "#1802FGood morning, everyone.\x02\x03",
            "#1804FThank you so much for conducting\x01",
            "the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FNot a problem. It's our job, after all.\x02\x03",
            "#0000FLooks like the First Division's\x01",
            "already on the case, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1809FAhaha... Yeah, they ended up\x01",
            "asking me questions, too.\x02\x03",
            "#1810FIlya showed up late today, so I can't help\x01",
            "but feel impatient.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3380")

    Jump("loc_3460")

    label("loc_3385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3396")
    Call(0, 15)
    Jump("loc_3460")

    label("loc_3396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_345D")

    ChrTalk(
        0x9,
        (
            "#1806FSorry, everyone. I have to get back\x01",
            "to practice soon.\x02\x03",
            "#1802FStill, though. I'm glad I decided to\x01",
            "consult with you.\x02\x03",
            "Good luck investigating the origin\x01",
            "of the threat letter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3460")

    label("loc_345D")

    Call(0, 13)

    label("loc_3460")

    TalkEnd(0xFE)
    Return()

    # Function_14_2FE1 end

    def Function_15_3464(): pass

    label("Function_15_3464")

    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "Okay. Let's take it from the top of\x01",
            "scene 18.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Give me a moment. I need to set\x01",
            "the stage up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6201FGreat, thank you!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3581")

    ChrTalk(
        0x101,
        "#0005F(They look pretty busy...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304F(Probably not cool of us to distract\x01",
            "'em during crunch time. Let's get\x01",
            "outta here.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3581")

    OP_4C(0x9, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_15_3464 end

    def Function_16_358A(): pass

    label("Function_16_358A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_371C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3613")

    ChrTalk(
        0xE,
        "Do not speak with me, for I am practicing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If you would like to observe, then do so\x01",
            "from the stands.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3717")

    label("loc_3613")

    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xE,
        "Okay, let us now proceed to the final act!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hah! Dost thou think thou have matched\x01",
            "me, awoken warrior?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Final act...check. No problems here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Was that a scene with the Moon Princess?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Could you please take this seriously?!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 5)
    OP_4C(0xF, 0xFF)

    label("loc_3717")

    Jump("loc_3B44")

    label("loc_371C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_384B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3799")

    ChrTalk(
        0xE,
        "Our problems all stem from Nikolai...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "He may work hard, but his skills are\x01",
            "not up to snuff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3846")

    label("loc_3799")


    ChrTalk(
        0xE,
        (
            "Theodor's acting skills are phenomenal.\x01",
            "Frighteningly so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The man is at the height of his performance.\x01",
            "Even a top-tier star like myself has gotten\x01",
            "the shivers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_3846")

    Jump("loc_3B44")

    label("loc_384B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_38C9")

    ChrTalk(
        0xE,
        (
            "O-Oh, I must note to you... Do not\x01",
            "utter a word about this to anyone,\x01",
            "for I am engaged in secret training.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B44")

    label("loc_38C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3999")

    ChrTalk(
        0xE,
        (
            "Rixia has my sympathies. She must\x01",
            "be faced with great difficulty right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "She's partnered up with Ilya. Even I have\x01",
            "my moments of trouble with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Egads! That was a secret.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3B44")

    label("loc_3999")


    ChrTalk(
        0xE,
        "*sigh* Shall I break for recess?\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xE, 0x0, 750)
    Sleep(750)

    ChrTalk(
        0xE,
        (
            "Wh-Whoa! Oh, it's just the officers.\x01",
            "Please refrain from startling me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FSorry about that. Were you practicing\x01",
            "back here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Indeed. I must face off with Ilya\x01",
            "during a scene in this play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I don't wish to be obscured and completely\x01",
            "outclassed by her radiant light.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I must do everything I can to perfect\x01",
            "these finishing touches.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_3B44")

    TalkEnd(0xFE)
    Return()

    # Function_16_358A end

    def Function_17_3B48(): pass

    label("Function_17_3B48")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3BFF")

    ChrTalk(
        0xF,
        (
            "Oh, by the way. We recently hired\x01",
            "a new assistant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "She might have some talent for the\x01",
            "performing arts. I'm impressed at how\x01",
            "gracefully she carries herself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CDD")

    label("loc_3BFF")


    ChrTalk(
        0xF,
        (
            "I'm supposed to have the day off,\x01",
            "but Eugene called me in.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        "*yaawn* I'm still waking up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(I'll never get used to how different these\x01",
            "guys are when they aren't performing.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_3CDD")

    TalkEnd(0xFE)
    Return()

    # Function_17_3B48 end

    def Function_18_3CE1(): pass

    label("Function_18_3CE1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3D86")

    ChrTalk(
        0x11,
        (
            "Nikolai seemed pretty troubled. I'd know,\x01",
            "as he's always such a worrywart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "*sigh* Where could he have ran off to?\x01",
            "What could he be doing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF7")

    label("loc_3D86")


    ChrTalk(
        0x11,
        (
            "Adjusting the scenario will mean\x01",
            "adjusting the acting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "*sigh* I've been worried sick\x01",
            "about Nikolai.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_3DF7")

    TalkEnd(0xFE)
    Return()

    # Function_18_3CE1 end

    def Function_19_3DFB(): pass

    label("Function_19_3DFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3E6C")

    ChrTalk(
        0x12,
        (
            "First Rixia, and now Nikolai?! I'm going\x01",
            "to be left behind if I don't start trying\x01",
            "harder!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F5D")

    label("loc_3E6C")


    ChrTalk(
        0x12,
        (
            "N-Nikolai's been in perfect form\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I can't believe how well he performed\x01",
            "during today's rehearsal.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x12)

    ChrTalk(
        0x12,
        (
            "C-Crap. First Rixia, and now Nikolai?!\x01",
            "Everyone's just leaving me in the dust\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_3F5D")

    TalkEnd(0xFE)
    Return()

    # Function_19_3DFB end

    def Function_20_3F61(): pass

    label("Function_20_3F61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_40FE")
    OP_64(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3FF5")

    ChrTalk(
        0x10,
        (
            "*sigh* Things aren't going to go\x01",
            "well for me. I just know it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Rixia's already widely recognized\x01",
            "by everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40E7")

    label("loc_3FF5")


    ChrTalk(
        0x10,
        (
            "I made a huge blunder during\x01",
            "yesterday's performance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I've been making all these careless mistakes\x01",
            "even during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I wanted to get a good practice session in,\x01",
            "but I'm just too depressed to do anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_40E7")

    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_43D6")

    label("loc_40FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_41D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_414B")

    ChrTalk(
        0xFE,
        "*sigh* Why doesn't anything ever go well for me?\x02",
    )

    CloseMessageWindow()
    Jump("loc_41D2")

    label("loc_414B")


    ChrTalk(
        0x10,
        (
            "Okay... So this part goes into a spin\x01",
            "like...this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huh. Something feels off. None of it goes\x01",
            "well together, like, at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_41D2")

    Jump("loc_43D6")

    label("loc_41D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4345")

    ChrTalk(
        0xFE,
        "I managed to get a role for this play.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's one of the most minor roles, but it's\x01",
            "still for an Arc en Ciel play. That's cause\x01",
            "for celebration for someone like me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the other hand, Rixia managed to\x01",
            "become the co-star. And she joined\x01",
            "the troupe after I did...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ugh. I'm being too impatient here.\x01",
            "Maybe we're on different levels.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_43D6")

    label("loc_4345")


    ChrTalk(
        0xFE,
        (
            "Rixia's skills are the real deal. She just\x01",
            "got here, yet she has a major role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Compared to her, I'm just--\x01",
            "No! I mustn't be impatient.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43D6")

    TalkEnd(0xFE)
    Return()

    # Function_20_3F61 end

    def Function_21_43DA(): pass

    label("Function_21_43DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_45D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4518")
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0xD,
        (
            "Let's see... Okay, the curtain needs to\x01",
            "roll up at a different speed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Change the stage lift to 'B.' Now, follow\x01",
            "the timing of the lighting and music...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Understood. Am I doing it right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, that's perfect. Do it the exact\x01",
            "same way during the real thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x16, 0xFF)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x1, 3)
    Jump("loc_45D0")

    label("loc_4518")


    ChrTalk(
        0xD,
        (
            "The scenario was changed at the last\x01",
            "moment, so things are pretty hectic\x01",
            "for us stagehands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "*sigh* At least I have Sully helping me.\x01",
            "Maybe I'll let her control the curtains.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45D0")

    Jump("loc_50AC")

    label("loc_45D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4728")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4688")

    ChrTalk(
        0xD,
        (
            "Nikolai's been brooding over his Anniversary\x01",
            "Festival blunder pretty badly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We've been worried that his nerves\x01",
            "have been getting the best of him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4723")

    label("loc_4688")


    ChrTalk(
        0xD,
        "Nikolai's gone missing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I wonder if it's because of all of the recent\x01",
            "stress he's been dealing with. I could see\x01",
            "the tension during practice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_4723")

    Jump("loc_50AC")

    label("loc_4728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_48A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_47AB")

    ChrTalk(
        0xD,
        "Will Nikolai ever take a break?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Pretty sure he's been exerting himself\x01",
            "a bit too much these days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48A1")

    label("loc_47AB")


    ChrTalk(
        0xD,
        (
            "Just last night, Nikolai was operating the\x01",
            "stage controls on his own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Sounds like he pulled another all-nighter\x01",
            "so he could practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's fine that he's putting his heart and\x01",
            "soul into it, but isn't this going a bit\x01",
            "overboard?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_48A1")

    Jump("loc_50AC")

    label("loc_48A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4A0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_496D")

    ChrTalk(
        0xFE,
        (
            "Actually, I visited an acquaintance's\x01",
            "studio the other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was welcomed in by the loveliest\x01",
            "little girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't know the old man had a\x01",
            "granddaughter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_4A08")

    label("loc_496D")


    ChrTalk(
        0xFE,
        (
            "I know a place where we can get help\x01",
            "with Arc en Ciel's stage design.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He surprised me, though. I didn't know\x01",
            "he had such a lovely granddaughter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A08")

    Jump("loc_50AC")

    label("loc_4A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4BAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4AAE")

    ChrTalk(
        0xD,
        (
            "Detectives will be posted throughout the\x01",
            "theater during the performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh, how I'd love for them to not\x01",
            "mess up the lighting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BA8")

    label("loc_4AAE")


    ChrTalk(
        0xD,
        (
            "Hmm... We could change the angle of\x01",
            "the lighting for this scene like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "However, we'll need to account for any\x01",
            "detectives posted through the theater\x01",
            "during the performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm worried that they might end up\x01",
            "blocking the lights.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_4BA8")

    Jump("loc_50AC")

    label("loc_4BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4D71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CAA")

    ChrTalk(
        0xFE,
        (
            "All of our stage designs need to be subtle,\x01",
            "yet bold and powerful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not something we can just set up\x01",
            "in a single day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stage design has been moving along smoothly\x01",
            "thanks to the help of a studio we work with.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_4D6C")

    label("loc_4CAA")


    ChrTalk(
        0xFE,
        (
            "Stage design should be considered an\x01",
            "artform. It supports Arc en Ciel's artists\x01",
            "with its bold visuals and props.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our stage design is almost finished\x01",
            "thanks to the studio we work with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D6C")

    Jump("loc_50AC")

    label("loc_4D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4D82")
    Call(0, 15)
    Jump("loc_50AC")

    label("loc_4D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4E3A")

    ChrTalk(
        0xD,
        (
            "Oh, boy. Yet another ridiculous request from\x01",
            "our queen. I don't think I'll be able to modify\x01",
            "the stage for what she has in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I'll try my damnedest, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_50AC")

    label("loc_4E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4EDA")

    ChrTalk(
        0xD,
        (
            "The energy Ilya puts into performing\x01",
            "always impresses me to no end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "She has the power to influence our troupe\x01",
            "leader with her opinions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50AC")

    label("loc_4EDA")


    ChrTalk(
        0xD,
        (
            "Oh, you're those officers the troupe leader\x01",
            "told us about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I don't mind you watching, but please\x01",
            "don't touch anything, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FIs this the stage design you'll be\x01",
            "using for the performance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It sure is. That design carries the\x01",
            "hopes and dreams of Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Ilya requested some adjustments, so\x01",
            "I'm in the process of applying them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "With all these difficult orders, she's giving\x01",
            "the troupe leader's enthusiasm a run for\x01",
            "his money.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_50AC")

    TalkEnd(0xFE)
    Return()

    # Function_21_43DA end

    def Function_22_50B0(): pass

    label("Function_22_50B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_518B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50CE")
    Call(0, 24)
    Jump("loc_5186")

    label("loc_50CE")


    ChrTalk(
        0xFE,
        (
            "#0603FI thought I told you to not wander around!\x02\x03",
            "Did I stutter, or do you have trouble hearing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FN-No, sir. Sorry for that.\x01",
            "(Yeah, I figured we were pushing our luck.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5186")

    Jump("loc_5349")

    label("loc_518B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5294")
    OP_4B(0x14, 0xFF)
    TurnDirection(0xFE, 0xC, 0)

    ChrTalk(
        0xFE,
        (
            "#0600FOkay, I understand the situation.\x02\x03",
            "#0603FEmma, have the letter in question\x01",
            "analyzed.\x02\x03",
            "#0601FI doubt we'll find any fingerprints, but there\x01",
            "might be other important clues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Yes, sir. I'll have it analyzed immediately.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    OP_4C(0x14, 0xFF)
    Jump("loc_5349")

    label("loc_5294")


    ChrTalk(
        0xFE,
        (
            "#0600FHey, you. You've wrapped up your work\x01",
            "here, right?\x02\x03",
            "#0603FStop resisting the inevitable and return\x01",
            "to your own work already. This case is\x01",
            "already under our jurisdiction.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5349")

    TalkEnd(0xFE)
    Return()

    # Function_22_50B0 end

    def Function_23_534D(): pass

    label("Function_23_534D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_53CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_536B")
    Call(0, 24)
    Jump("loc_53C6")

    label("loc_536B")


    ChrTalk(
        0xFE,
        (
            "The private performance is fast approaching...\x01",
            "I'll prepare the documents right away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53C6")

    Jump("loc_5495")

    label("loc_53CB")


    ChrTalk(
        0xFE,
        (
            "Do us a favor and don't get in\x01",
            "the way of our work, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Or perhaps it's the SSS's hobby to\x01",
            "sniff around where they don't belong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F(O-Ouch. Always hitting us right\x01",
            "where it hurts.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5495")

    TalkEnd(0xFE)
    Return()

    # Function_23_534D end

    def Function_24_5499(): pass

    label("Function_24_5499")

    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_93(0x13, 0x0, 0x0)
    OP_93(0x14, 0x2D, 0x0)

    ChrTalk(
        0x14,
        "This looks like the ideal spot for a sniper.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#0601FThe way this theater was built gives it\x01",
            "far too many openings for my liking.\x02\x03",
            "#0600FI'll keep watch over here, Emma. Let's\x01",
            "switch over to pattern B.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Understood, sir. I'll have the men change\x01",
            "their positions immediately.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 5)
    OP_4C(0x13, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_24_5499 end

    def Function_25_55DC(): pass

    label("Function_25_55DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_584C")

    ChrTalk(
        0x101,
        (
            "#0005FWh-What the heck? What are you doing\x01",
            "here, Lechter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#3502FHahaha! Isn't it obvious? I'm here\x01",
            "to watch Arc en Ciel!\x02\x03",
            "#3504FBoy, I thought I wasn't gonna make it\x01",
            "on time, so I started sprinting here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FHeh. I feel you there, man.\x02\x03",
            "#0307FWait! Hold on just a damn sec here.\x01",
            "Aren't these seats for special guests?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FThese seats shouldn't be available\x01",
            "to the average person, no.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#3507FWeeell...about that. The chanc--*cough*\x02\x03",
            "#3509FI mean... Can't I use Gramps' sweet\x01",
            "benefits for my own enjoyment every\x01",
            "once in a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F(His behavior is incomprehensible.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 4)
    Jump("loc_58ED")

    label("loc_584C")


    ChrTalk(
        0x15,
        (
            "#3504FHey, this looks like one comfy couch\x01",
            "to me.\x02\x03",
            "#3510FThink I'll snooze until the show starts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0206F(His behavior is absolutely\x01",
            "incomprehensible.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58ED")

    TalkEnd(0xFE)
    Return()

    # Function_25_55DC end

    def Function_26_58F1(): pass

    label("Function_26_58F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_590E")
    Call(0, 27)
    Jump("loc_5F4D")

    label("loc_590E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5CB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 1)), scpexpr(EXPR_END)), "loc_59AC")

    ChrTalk(
        0xFE,
        (
            "Rixia said she was going home to grab\x01",
            "a few things, but she sure is late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose I'll have to go and pick\x01",
            "her up later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CAB")

    label("loc_59AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C55")

    ChrTalk(
        0xFE,
        (
            "We've adjusted the script, so the troupe is\x01",
            "hard at work practicing the changes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Try not to wander around too much, will you?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5C4D")

    ChrTalk(
        0x101,
        (
            "#0006FSorry. We'll try. I'm a bit worried about\x01",
            "the whole situation.\x02\x03",
            "#0000FBut with how hard you guys work,\x01",
            "I'm sure you'll pull through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah, I sure hope so. I'm doing my part, too.\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "We'll push through it with pure willpower\x01",
            "and make it a great success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, I think you should stop worrying\x01",
            "about it and go back to doing your\x01",
            "own job!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FSurprisingly reliable words comin' from you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThanks. We'll heed your words.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good luck to you guys\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 1)

    label("loc_5C4D")

    SetScenarioFlags(0x1, 7)
    Jump("loc_5CAB")

    label("loc_5C55")


    ChrTalk(
        0xFE,
        "What's your guys' problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're too busy to deal with your\x01",
            "dilly-dallying!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CAB")

    Jump("loc_5F4D")

    label("loc_5CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5E5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D91")

    ChrTalk(
        0xFE,
        (
            "That Nikolai guy's been acting like a\x01",
            "total weirdo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He got into a fight with Rixia and even\x01",
            "shot dirty looks at Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was about to punch him square in the\x01",
            "jaw, but Ilya stopped me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_5E59")

    label("loc_5D91")


    ChrTalk(
        0xFE,
        (
            "Come to think of it, he made some careless\x01",
            "mistakes during the Anniversary Festival\x01",
            "and has been kinda down ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guess he's been acting pretty weird\x01",
            "since that whole thing went down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E59")

    Jump("loc_5F4D")

    label("loc_5E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5F4D")

    ChrTalk(
        0xFE,
        "Rixia's far too kind, to be honest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's such a jackass! She didn't have\x01",
            "to leave just 'cause he told her to.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F4A")

    ChrTalk(
        0x101,
        "#0000FHey, is something the matter?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 500)

    ChrTalk(
        0xFE,
        "Nope. None of your business, anyway.\x02",
    )

    CloseMessageWindow()

    label("loc_5F4A")

    SetScenarioFlags(0x1, 7)

    label("loc_5F4D")

    TalkEnd(0xFE)
    Return()

    # Function_26_58F1 end

    def Function_27_5F51(): pass

    label("Function_27_5F51")


    ChrTalk(
        0x101,
        (
            "#0005FWas this kid always a part\x01",
            "of the troupe?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FCE")

    ChrTalk(
        0xFE,
        (
            "The heck? You guys Ilya's\x01",
            "friends or something?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6003")

    label("loc_5FCE")


    ChrTalk(
        0xFE,
        (
            "The heck? You guys Ilya's\x01",
            "friends or something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6003")


    ChrTalk(
        0xFE,
        (
            "Hmph. The theater isn't open to\x01",
            "the public right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just because you're friends, doesn't mean\x01",
            "I'll let you come and go as you please.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 0)
    Return()

    # Function_27_5F51 end

    def Function_28_6099(): pass

    label("Function_28_6099")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This building truly has far too many\x01",
            "openings. You could take aim at the\x01",
            "stage from just about anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Grr... Talk about a guy who knows how\x01",
            "to take advantage of his surroundings.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_6099 end

    def Function_29_6160(): pass

    label("Function_29_6160")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6304")

    ChrTalk(
        0xFE,
        (
            "We'll have to adjust our patrol into a\x01",
            "perfect formation until the very end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anything were to happen to Ilya Platiere,\x01",
            "it'd be a serious blow to our government's\x01",
            "credibility. It'd be a huge political scandal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(Do you think that's true, Elie?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103F(It's possible... Ilya is internationally\x01",
            "famous.)\x02\x03",
            "#0101F(If word gets out, I doubt our politicians\x01",
            "would idly sit by.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_638C")

    label("loc_6304")


    ChrTalk(
        0xFE,
        (
            "Hey, you useless SSS guys. You're no\x01",
            "longer in charge, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to ask you outsiders to\x01",
            "exit the premises immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_638C")

    TalkEnd(0xFE)
    Return()

    # Function_29_6160 end

    def Function_30_6390(): pass

    label("Function_30_6390")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I came all the way out from the Empire\x01",
            "just for this day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't wait to see this.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_6390 end

    def Function_31_63F5(): pass

    label("Function_31_63F5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This is my first time watching\x01",
            "Arc en Ciel perform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard their new production is super\x01",
            "popular, so my expectations are high.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_63F5 end

    def Function_32_6489(): pass

    label("Function_32_6489")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Arc en Ciel's play is finally here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#4SWooo, Lady Ilya!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_6489 end

    def Function_33_64D2(): pass

    label("Function_33_64D2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6566")
    Jump("loc_65B0")

    label("loc_6566")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6586")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_65B0")

    label("loc_6586")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65A6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_65B0")

    label("loc_65A6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65B0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I'm also interested in that rising\x01",
            "star of theirs, Rixia Mao.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's got quite the reputation, so I'm\x01",
            "excited to see whether she lives\x01",
            "up to it or not.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_64D2 end

    def Function_34_667E(): pass

    label("Function_34_667E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Daaaaaad... When's it going to start?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm soooo bored of waiting.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_667E end

    def Function_35_66D1(): pass

    label("Function_35_66D1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6765")
    Jump("loc_67AF")

    label("loc_6765")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6785")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67AF")

    label("loc_6785")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67A5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67AF")

    label("loc_67A5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_67AF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I watched them perform on the opening day,\x01",
            "but the excitement from it never went away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been buying tickets nonstop because\x01",
            "I can't stop thinking about them.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_66D1 end

    def Function_36_6888(): pass

    label("Function_36_6888")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_691C")
    Jump("loc_6966")

    label("loc_691C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_693C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6966")

    label("loc_693C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_695C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6966")

    label("loc_695C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6966")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Hahaha... These S section seats are fantastic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no better way to fully appreciate the\x01",
            "artistry, other than to sit in the S section.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_36_6888 end

    def Function_37_6A28(): pass

    label("Function_37_6A28")

    TalkBegin(0xFE)
    OP_4B(0x21, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Oh. I need to excuse myself to the\x01",
            "restroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm sorry, but could you watch my seat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "What are you talking about? Aren't\x01",
            "those seats reserved?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x21, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_37_6A28 end

    def Function_38_6AD4(): pass

    label("Function_38_6AD4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I unexpectedly received tickets from my\x01",
            "job, so we get to come watch the show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aren't we just the luckiest bunch?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_6AD4 end

    def Function_39_6B57(): pass

    label("Function_39_6B57")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_68(0, 1500, 13250, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -750, 450, 11500, 0)
    SetChrPos(0x102, 250, 450, 11250, 0)
    SetChrPos(0x103, -750, 900, 10000, 0)
    SetChrPos(0x104, 250, 900, 9750, 0)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0x11, 0xE1, 0x0)
    OP_93(0xA, 0x87, 0x0)
    OP_0D()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#5POh, the Special Support Section!\x01",
            "Perfect timing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FHas something happened, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PA-Actually...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIf you could, please keep what I'm about\x01",
            "to tell you a secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PWe discovered that one of our artists\x01",
            "went missing this morning.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_END)), "loc_6E35")

    ChrTalk(
        0x9,
        (
            "#1806F#5PI'm pretty sure we've mentioned\x01",
            "him before. His name is Nikolai...\x02\x03",
            "#1801FAnyway, he apparently never showed\x01",
            "up at home yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EA2")

    label("loc_6E35")


    ChrTalk(
        0x9,
        (
            "#1806F#5PNikolai and I are both rookies...\x02\x03",
            "#1801FAnd, he apparently never showed up\x01",
            "at home yesterday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EA2")


    ChrTalk(
        0x11,
        (
            "#11PWe were told his family's searching for him,\x01",
            "but they haven't had any luck yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI tried to reach out to all of my contacts,\x01",
            "but no one has seen him anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0201FNikolai? Is he not the man who was\x01",
            "behaving oddly?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#5PY-Yeah, that's him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PHe was timid and would make all sorts of\x01",
            "mistakes, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P...right after the Anniversary Festival, he\x01",
            "started to demonstrate incredible talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FIs that right...?\x02\x03",
            "#0001FYou say talent, but could you be a little\x01",
            "more specific, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PWell, his physical prowess skyrocketed.\x01",
            "He improved to the point where he could\x01",
            "handle the most passionate scenes with ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1706F#5PIt was pretty weird... Almost as if he was\x01",
            "possessed by someone or something.\x02\x03",
            "#1701FThere's no way Nikolai would be able to\x01",
            "pull off the moves I saw.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1806F#5PHonestly, it felt as if he were delirious.\x02\x03",
            "#1808FIt was as if he had turned into a different person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0303FThat...ain't good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108FA disappearance is never good, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FMr. Avan, would you mind leaving this\x01",
            "case with the Special Support Section?\x02\x03",
            "#0001FWe might be able to find him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PTruly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PWe would greatly appreciate your\x01",
            "assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1702F#5PThat's probably our best bet. We can rest\x01",
            "easy with Lloyd and the crew on the case.\x02\x03",
            "#1706FBesides, we still need to rearrange today's\x01",
            "programme.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(12)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(13)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#0305FWhoa! Hold your horses! You seriously\x01",
            "still plan on doin' today's performance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PYes. We were just in the middle of\x01",
            "discussing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PEven if Nikolai doesn't return in time,\x01",
            "we can't just cancel the show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PWe'll likely have to rearrange the roles.\x01",
            "Either way, we'll manage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PArc en Ciel won't simply walk off the\x01",
            "stage because of a setback.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PWe'll have to take some time to adjust\x01",
            "the roles, script, and even the scenes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, we can always delay the start\x01",
            "of the show. We just want to make it\x01",
            "happen, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202FI am amazed by the tenacity\x01",
            "you apply to your craft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0109FIsn't that the truth? We shouldn't have\x01",
            "expected otherwise from them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004FAll right, then. Best of luck with your show.\x02\x03",
            "#0001FIf you could, keep an eye on the dressing\x01",
            "rooms and auditorium. Nikolai may come\x01",
            "back later.\x02\x03",
            "And if you do spot him, contact the SSS\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5POf course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1808F#5PI'm sorry, everyone. If I had just been\x01",
            "more careful, this would have never\x01",
            "happened.\x02\x03",
            "#1801FPlease find Nikolai, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FDon't worry. We will.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_794D")
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x102,
        "#0101FWe'd better hurry, Lloyd.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#0001F#6PYou're right. We need to check on the\x01",
            "others as soon as we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_794D")

    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 0, 450, 11500, 360)
    OP_93(0x8, 0xE1, 0x0)
    OP_93(0x9, 0x168, 0x0)
    OP_93(0x11, 0x10E, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetScenarioFlags(0xC8, 0)
    OP_29(0x4C, 0x1, 0x7)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0x11, 0xFF)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_39_6B57 end

    def Function_40_79B1(): pass

    label("Function_40_79B1")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_40_79B1 end

    def Function_41_79DE(): pass

    label("Function_41_79DE")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_41_79DE end

    def Function_42_7A0B(): pass

    label("Function_42_7A0B")

    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_42_7A0B end

    def Function_43_7A22(): pass

    label("Function_43_7A22")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(33)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_43_7A22 end

    def Function_44_7A39(): pass

    label("Function_44_7A39")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_44_7A39 end

    def Function_45_7A42(): pass

    label("Function_45_7A42")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_45_7A42 end

    def Function_46_7A4B(): pass

    label("Function_46_7A4B")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_46_7A4B end

    def Function_47_7A54(): pass

    label("Function_47_7A54")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_47_7A54 end

    def Function_48_7A5D(): pass

    label("Function_48_7A5D")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_48_7A5D end

    def Function_49_7A8A(): pass

    label("Function_49_7A8A")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_49_7A8A end

    def Function_50_7AB7(): pass

    label("Function_50_7AB7")

    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_7AB7 end

    def Function_51_7ACE(): pass

    label("Function_51_7ACE")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(33)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_51_7ACE end

    def Function_52_7AE5(): pass

    label("Function_52_7AE5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B03")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_52_7AE5")

    label("loc_7B03")

    Return()

    # Function_52_7AE5 end

    def Function_53_7B04(): pass

    label("Function_53_7B04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B22")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(66)
    Jump("Function_53_7B04")

    label("loc_7B22")

    Return()

    # Function_53_7B04 end

    def Function_54_7B23(): pass

    label("Function_54_7B23")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B41")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_54_7B23")

    label("loc_7B41")

    Return()

    # Function_54_7B23 end

    def Function_55_7B42(): pass

    label("Function_55_7B42")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B60")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(66)
    Jump("Function_55_7B42")

    label("loc_7B60")

    Return()

    # Function_55_7B42 end

    def Function_56_7B61(): pass

    label("Function_56_7B61")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_D3(0xFE, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D3(0xFE, 0x0, 0x0, 0x57E40, 0x3E8)
    SetChrFlags(0xFE, 0x100)
    Return()

    # Function_56_7B61 end

    def Function_57_7B9A(): pass

    label("Function_57_7B9A")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    OP_D3(0xFE, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D3(0xFE, 0x0, 0x0, 0xFFFA81C0, 0x3E8)
    SetChrFlags(0xFE, 0x100)
    Return()

    # Function_57_7B9A end

    def Function_58_7BD3(): pass

    label("Function_58_7BD3")

    Sleep(1500)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1F)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    OP_95(0x9, -2110, 1250, 20950, 4500, 0x0)
    BeginChrThread(0x9, 2, 0, 41)

    def lambda_7C07():
        OP_9E(0x9, 0x0, 0x5AB4, 0xFFFEA070, 0x898, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7C07)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    Sleep(1)
    Sound(820, 0, 100, 0)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x578, 0x2BC)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1E)
    Sound(50, 0, 100, 0)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    Sleep(700)
    BeginChrThread(0x9, 2, 0, 43)
    BeginChrThread(0x9, 3, 0, 54)
    Sound(820, 0, 100, 0)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x2BC)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1F)
    Sound(50, 0, 100, 0)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)

    def lambda_7CA8():
        OP_93(0x9, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_7CA8)
    BeginChrThread(0x9, 2, 0, 41)
    OP_9D(0x9, 0xFFFFF9FC, 0x4E2, 0x5E38, 0xBB8, 0x4B0)
    SetChrChipByIndex(0x9, 0x21)
    Sound(50, 0, 100, 0)
    SetChrSubChip(0x9, 0x1)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1E)
    BeginChrThread(0x9, 2, 0, 41)

    def lambda_7CEE():
        OP_93(0x9, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_7CEE)
    OP_9D(0x9, 0xFFFFF3C6, 0x4E2, 0x62F2, 0x3E8, 0x6A4)
    SetChrChipByIndex(0x9, 0x21)
    Sound(50, 0, 100, 0)
    SetChrSubChip(0x9, 0x2)
    Sleep(1500)

    def lambda_7D23():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_7D23)
    BeginChrThread(0x9, 2, 0, 41)
    OP_9D(0x9, 0xFFFFFA74, 0x4E2, 0x6496, 0x7D0, 0xA28)
    Sound(50, 0, 100, 0)
    BeginChrThread(0x9, 2, 0, 43)
    BeginChrThread(0x9, 3, 0, 54)
    OP_9D(0x9, 0x58C, 0x4E2, 0x6496, 0x7D0, 0xA28)
    Sound(50, 0, 100, 0)
    BeginChrThread(0x9, 2, 0, 44)
    BeginChrThread(0x9, 3, 0, 54)
    OP_9D(0x9, 0xF28, 0x4E2, 0x6496, 0x7D0, 0xA28)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x21)
    Sound(50, 0, 100, 0)
    SetChrSubChip(0x9, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    OP_9E(0x9, 0xF28, 0x55F0, 0xFFFEA070, 0xBB8, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    BeginChrThread(0x9, 3, 0, 55)
    Sleep(700)
    BeginChrThread(0x9, 2, 0, 43)
    BeginChrThread(0x9, 3, 0, 54)
    Sleep(1800)
    EndChrThread(0x9, 0x3)
    Sound(820, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x1)
    Return()

    # Function_58_7BD3 end

    def Function_59_7E09(): pass

    label("Function_59_7E09")

    OP_95(0xFE, -5500, 1250, 24300, 3000, 0x0)
    OP_95(0xFE, -10500, 1250, 25300, 3000, 0x0)
    Return()

    # Function_59_7E09 end

    def Function_60_7E32(): pass

    label("Function_60_7E32")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0xC, 0xFF)
    ClearMapObjFlags(0x1A, 0x4)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0x14, 0x1E, 0x0)
    OP_7D(0xC8, 0xC8, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0x1A, "02back", 0x0, 0x1)
    SetMapObjFrame(0x1A, "02moon_add", 0x0, 0x1)
    SetMapObjFrame(0x1A, "02water01", 0x0, 0x1)
    SetMapObjFrame(0x1A, "02water02_add", 0x0, 0x1)
    SetMapObjFrame(0x1A, "main02", 0x0, 0x1)
    LoadChrToIndex("apl/ch50265.itc", 0x1E)
    LoadChrToIndex("apl/ch50266.itc", 0x1F)
    LoadChrToIndex("apl/ch50267.itc", 0x20)
    LoadChrToIndex("apl/ch50268.itc", 0x21)
    LoadChrToIndex("apl/ch50269.itc", 0x22)
    LoadChrToIndex("apl/ch50270.itc", 0x23)
    LoadChrToIndex("chr/ch09800.itc", 0x24)
    LoadChrToIndex("apl/ch50200.itc", 0x28)
    LoadChrToIndex("apl/ch50201.itc", 0x29)
    LoadChrToIndex("apl/ch50202.itc", 0x2A)
    LoadChrToIndex("apl/ch50549.itc", 0x2B)
    EndChrThread(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x1)
    SetChrPos(0x9, 0, 1250, 23220, 225)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01700.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06200.itp")
    OP_68(-70, 2500, 24310, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20500, 0)
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x2, 0x0, 0x0, 0x1388, 0x0)
    OP_C9(0x2, 0x1, 0x3E8, 0x44C, 0x0)
    OP_E5()
    PlayBGM("ed7501", 1)
    Sleep(1000)
    FadeToBright(8000, 0)
    OP_6E(620, 25000)
    Sleep(5700)
    OP_C9(0x2, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x2328)
    OP_C9(0x2, 0x1, 0xBB8, 0xBB8, 0x2328)
    Sleep(900)
    BeginChrThread(0x101, 3, 0, 58)
    WaitChrThread(0x101, 3)
    StopBGM(0x1770)
    Sleep(3000)
    Fade(500)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x1)
    OP_0D()
    Sleep(300)
    OP_E6()
    Sound(1632, 255, 80, 0)

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        "#2100042V#6206F#5P#100W*pant* *pant*... *pant*...\x02",
    )

    CloseMessageWindow()
    OP_11(0x0, 0x0, 0x0, 0x32, 0xC8, 0x3E8)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(800)
    SetChrName("Purple-Haired Girl")

    AnonymousTalk(
        0xFF,
        (
            "#2100043V#30WThank Aidios. I finally managed to\x01",
            "pull it off...\x02",
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
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -9000, 1250, 24230, 270)

    NpcTalk(
        0x8,
        "Woman's Voice",
        "#2100044V#2PYep. That was a good showing.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(1635, 255, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7513", 0)
    TurnDirection(0x9, 0x8, 300)
    Fade(1000)
    OP_68(-6200, 3200, 23140, 0)
    MoveCamera(336, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_68(-1330, 2500, 22900, 5000)
    OP_95(0x8, -1730, 1250, 23430, 2000, 0x0)
    TurnDirection(0x8, 0x9, 500)
    OP_6F(0x1)

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        "#2100045V#6205F#30WTh-Thank you, Ilya.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Blonde-Haired Woman")

    AnonymousTalk(
        0xFF,
        (
            "#2100046VYour speed and timing are great.\x02\x03",
            "#2100047VAll you need to work on is adjusting\x01",
            "to the rhythm during each interval.\x02\x03",
            "#2100048VDon't just get into the swing of the\x01",
            "music. Control it with your dancing\x01",
            "and acting till the very end.\x02\x03",
            "#2100049VDo it quietly, purely, and with\x01",
            "the majesty that's exclusive to the\x01",
            "Moon Princess.\x02",
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

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        (
            "#2100050V#6202F#30WYes, I'll focus on doing that.\x02\x03",
            "#2100051V#6208F#50WAh...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_68(-1330, 2400, 22900, 800)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(1300)

    NpcTalk(
        0x8,
        "Blonde-Haired Woman",
        (
            "#2100052V#1706FWell, I suppose it'd be heartless of me to\x01",
            "call you sloppy.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(170, 3020, 21070, 2000)
    SetCameraDistance(16500, 2000)
    SetChrFlags(0x8, 0x8000)
    OP_95(0x8, -750, 1250, 22350, 1000, 0x0)
    TurnDirection(0x8, 0x9, 500)
    Fade(250)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    NpcTalk(
        0x8,
        "Blonde-Haired Woman",
        (
            "#2100053V#1702F#5PTo be honest, I'm pretty dang impressed.\x02\x03",
            "#2100054VNot a single person has been able to keep\x01",
            "up with me during practice until now.\x02\x03",
            "#2100055V#1709FYou're going all out on this, aren't you? ♪\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        (
            "#2100056V#6202F#2PThank you. That means a lot.\x02\x03",
            "#2100057V#6203FStill, I can't shake my anxiety.\x02\x03",
            "#2100058VWhat if I end up holding you back\x01",
            "during a performance?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Blonde-Haired Woman",
        (
            "#2100059V#1704F#5PDon't sweat it. You have talent to spare.\x02\x03",
            "#2100060V#1702FHeck, I bet you've got a good chance\x01",
            "of surpassing me one of these days.\x02\x03",
            "#2100061V#1709FC'mon, just trust in my judgment!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        (
            "#2100062V#6209F#2PI really don't see that happening.\x02\x03",
            "#2100063V#6202FI mean, surpassing you? That's impossible.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Blonde-Haired Woman",
        (
            "#2100064V#1702F#5PWell, I don't exactly intend on making\x01",
            "it a walk in the park for you.\x02\x03",
            "#2100065V#1704FSo, you'd better hurry up and get\x01",
            "on my level while you still can.\x02\x03",
            "#2100066V#1701FYou'll be my rival, Rixia! A performer\x01",
            "who I can finally compete with!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        (
            "#2100067V#6203F#2P*sigh* Please try to refrain from making\x01",
            "impossible demands...\x02\x03",
            "#2100068V#6208FGeez. How did I even end up here?\x02\x03",
            "#2100069VI should already be back home and far\x01",
            "away from Crossbell by now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Blonde-Haired Woman",
        (
            "#2100070V#1709F#5PHeh heh heh... Pretty simple, if you ask me.\x02\x03",
            "#2100071VThe moment I caught you watching\x01",
            "me practice, your fate was sealed.\x02\x03",
            "#2100072VI'm never going to let you go. Got it?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        (
            "#2100073V#6206F#2PGoddess help me... I've been\x01",
            "kidnapped by a crazy dancer...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Blonde-Haired Woman",
        "#2100074V#1700F#5POh, dear. Are you that exhausted?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        (
            "#2100075V#6202F#2PNo, I'm okay.\x02\x03",
            "#2100076V#6203FIt's just, you know...\x02\x03",
            "#2100077V#6208FI'm still worried about not being good\x01",
            "enough, and there's that letter we\x01",
            "have to deal with...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Blonde-Haired Woman",
        (
            "#2100078V#1705F#5PLetter?\x02\x03",
            "#2100079VWhat was up with that again?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        (
            "#2100080V#6201F#2PThe letter that was addressed to you!\x02\x03",
            "#2100081VYou know, the one from that Yin person.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Blonde-Haired Woman",
        (
            "#2100082V#1705F#5POoooh, that one?\x02\x03",
            "#2100083V#1704FWhat a load of garbage. Isn't it\x01",
            "just some stupid prank?\x02\x03",
            "#2100084V#1702FIf I let every one of those get under\x01",
            "my skin, I wouldn't be the star I am.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        "#2100085V#6208F#2PB-But, Ilya...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Blonde-Haired Woman",
        (
            "#2100086V#1702F#5PListen, girly. After your debut, you're going\x01",
            "to start getting mountains of fan letters.\x02\x03",
            "#2100087VThere's definitely going to be some weird\x01",
            "ones in there, so just toss those in the bin.\x02\x03",
            "#2100088V#1709FIt might even be worse for you. With that\x01",
            "chest, I bet the boys will hardly be able to\x01",
            "take their eyes off you.\x02",
        )
    )

    CloseMessageWindow()
    MoveCamera(350, 20, 0, 1000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_96(0x8, 0xFFFFFE02, 0x4B0, 0x5528, 0x320, 0x0)
    Fade(250)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x8, 0x1)
    Sound(858, 0, 100, 0)
    Sleep(250)
    SetChrSubChip(0x8, 0x0)
    Sleep(250)
    SetChrSubChip(0x8, 0x1)
    Sound(858, 0, 100, 0)
    Sleep(250)
    SetChrSubChip(0x8, 0x0)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(800)
    Sound(1633, 255, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    OP_63(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        "#2100090V#6201F#2PW-Wait a minute! Ilya, please! Stop!\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#2100091V#1705FSorry about that. I lost control for a sec.\x02\x03",
            "#2100092V#1702FBut c'mon, Rixia. Lemme get a little up\x01",
            "close and personal with them for a bit.\x02\x03",
            "#2100093V#1709FIt won't hurt, I swear. It'll be the opposite!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        "#2100094V#6206F#2PUgh... Aidios!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, -9000, 1250, 24230, 270)

    NpcTalk(
        0xC,
        "Man's Voice",
        "#2100095V#2P*cough* *cough* Ahem!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xC, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-530, 3200, 22200, 3000)
    MoveCamera(340, 24, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(18000, 3000)

    def lambda_93E2():
        OP_95(0xFE, -1310, 1250, 24690, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_93E2)
    Sleep(300)
    Fade(250)

    def lambda_9404():

        label("loc_9404")

        TurnDirection(0xFE, 0xC, 300)
        Yield()
        Jump("loc_9404")

    QueueWorkItem2(0x8, 0, lambda_9404)

    def lambda_9416():

        label("loc_9416")

        TurnDirection(0xFE, 0xC, 300)
        Yield()
        Jump("loc_9416")

    QueueWorkItem2(0x9, 0, lambda_9416)
    SetChrChipByIndex(0x8, 0x0)
    Sleep(1000)

    def lambda_942F():
        OP_96(0xFE, 0xFFFFFC18, 0x4E2, 0x5640, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_942F)
    WaitChrThread(0xC, 1)
    TurnDirection(0xC, 0x8, 500)
    Fade(500)
    SetChrChipByIndex(0x9, 0x24)
    OP_0D()

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        "#2100096V#6205F#12PM-Mr. Avan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100097V#1705F#6POh... The heck? Were you here for\x01",
            "that whole thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#2100098VYes, and you should watch yourself, Ilya.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2100099VIt's quite clear you're dedicated, but\x01",
            "could you spare us the inappropriate\x01",
            "and unnecessary conduct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100100V#1709F#6PI'm her acting coach, silly! That's all.\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#2100101V#1700F#5POh, Rixia. Since it's already this late, I want\x01",
            "you to spend the night at my apartment.\x02\x03",
            "#2100102VI won't have you walking over to that part of\x01",
            "town when it's this dark out.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x0)
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#2100103V#6205FI promise it's not as dangerous as you\x01",
            "make it out to be.\x02\x03",
            "#2100104V#6209FEveryone there has been incredibly\x01",
            "kind to me ever since I moved in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100105V#1701F#5PPish posh! They all have ulterior motives.\x02\x03",
            "#2100106V#1706FEven on the best of nights, the city has\x01",
            "libidinous guys roaming the streets...\x02\x03",
            "#2100107VIf they got a glimpse of that hot bod of\x01",
            "yours, what would they do?\x02\x03",
            "#2100108V#1701FProbably throw themselves at you, that's\x01",
            "what!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#2100109VDescribing yourself, are we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#2100110VAh, that's right. There's a call for you, Ilya.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0xC, 500)

    ChrTalk(
        0x8,
        "#2100111V#1705F#6PReally? Is it from a woman, by any chance?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#2100112VYes. Will you take it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100113V#1709F#6PBut of course!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        "#2100114V#1702F#5PSorry, I'll be back in a bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2100115V#6202FOkay. I'll be here.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x13B, 0x1F4)
    OP_68(-1480, 3200, 22170, 2000)

    def lambda_9A0C():

        label("loc_9A0C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_9A0C")

    QueueWorkItem2(0xC, 0, lambda_9A0C)

    def lambda_9A1E():

        label("loc_9A1E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_9A1E")

    QueueWorkItem2(0x9, 0, lambda_9A1E)
    BeginChrThread(0x8, 0, 0, 59)
    Sleep(500)
    Sleep(1000)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#2100116V#11P*sigh* That woman never changes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2100117V#11PI thought she would be the slightest bit\x01",
            "disturbed by the letter, but I guess not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2100118V#6202F#11PWe ARE talking about Ilya.\x02\x03",
            "#2100119V#6204FIn everything she does, she dazzles like a\x01",
            "beautiful, golden sun...\x02\x03",
            "#2100120V#6208FStill, that just means she needs to be\x01",
            "even more cautious of others.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x201), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_60_7E32 end

    def Function_61_9BEB(): pass

    label("Function_61_9BEB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C35")
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_61_9BEB")

    label("loc_9C35")

    Return()

    # Function_61_9BEB end

    def Function_62_9C36(): pass

    label("Function_62_9C36")

    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 1, 0, 61)
    SetChrFlags(0x8, 0x4)
    BeginChrThread(0x8, 2, 0, 40)
    Sound(814, 0, 80, 0)
    Sleep(100)
    OP_9D(0x8, 0xA, 0x4E2, 0x636A, 0xFA0, 0x3E8)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    BeginChrThread(0x8, 2, 0, 43)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 53)

    def lambda_9C9C():
        OP_9E(0x8, 0x0, 0x5DC0, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_9C9C)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 40)
    Sleep(100)

    def lambda_9CEA():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_9CEA)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    EndChrThread(0x8, 0x0)

    def lambda_9D2F():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_9D2F)
    BeginChrThread(0x8, 2, 0, 40)
    Sleep(100)

    def lambda_9D45():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_9D45)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    Sound(854, 0, 80, 0)
    Sound(50, 0, 100, 0)
    EndChrThread(0x8, 0x0)

    def lambda_9D8A():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_9D8A)
    BeginChrThread(0x8, 2, 0, 40)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 52)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    BeginChrThread(0x8, 2, 0, 40)
    Sleep(100)

    def lambda_9DD2():
        OP_9E(0x8, 0x0, 0x636A, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_9DD2)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x320)
    Sound(854, 0, 80, 0)
    Sound(50, 0, 100, 0)
    BeginChrThread(0x8, 2, 0, 40)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 52)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x8, 0x0)

    def lambda_9E4D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_9E4D)
    BeginChrThread(0x8, 2, 0, 41)
    OP_9D(0x8, 0x0, 0x4E2, 0x639C, 0x7D0, 0x7D0)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    BeginChrThread(0x8, 3, 0, 52)
    BeginChrThread(0x8, 2, 0, 43)
    OP_9D(0x8, 0x0, 0x4E2, 0x639C, 0xBB8, 0x9C4)
    Sound(50, 0, 100, 0)
    Sound(51, 0, 100, 0)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    OP_82(0x0, 0x64, 0x5DC, 0x96)
    EndChrThread(0x8, 0x1)
    Sleep(1000)
    Return()

    # Function_62_9C36 end

    def Function_63_9EE9(): pass

    label("Function_63_9EE9")

    OP_95(0x9, 1300, 0, 15400, 1000, 0x0)

    def lambda_9F02():

        label("loc_9F02")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_9F02")

    QueueWorkItem2(0x9, 0, lambda_9F02)
    Return()

    # Function_63_9EE9 end

    def Function_64_9F10(): pass

    label("Function_64_9F10")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0xC, 0xFF)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFrame(0x19, "01back", 0x0, 0x1)
    LoadEffect(0x0, "event\\ev290_01.eff")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x2, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x2, 0x1, 0xBB8, 0xBB8, 0x0)
    LoadChrToIndex("apl/ch50250.itc", 0x1E)
    LoadChrToIndex("apl/ch50251.itc", 0x1F)
    LoadChrToIndex("apl/ch50252.itc", 0x20)
    LoadChrToIndex("apl/ch50253.itc", 0x21)
    LoadChrToIndex("apl/ch50254.itc", 0x22)
    LoadChrToIndex("apl/ch50255.itc", 0x23)
    LoadChrToIndex("chr/ch09700.itc", 0x24)
    LoadChrToIndex("apl/ch50207.itc", 0x28)
    SetChrPos(0x8, 10, 1250, 25450, 225)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06100.itp")
    SetChrPos(0x101, 650, 2700, -1530, 0)
    SetChrPos(0x102, -520, 2700, -1410, 0)
    SetChrPos(0x104, 570, 2700, -2900, 0)
    SetChrPos(0x103, -600, 2700, -2900, 0)

    def lambda_A06A():
        OP_95(0xFE, 650, 2700, 530, 1400, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A06A)

    def lambda_A084():
        OP_95(0xFE, -520, 2700, 410, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A084)

    def lambda_A09E():
        OP_95(0xFE, 570, 2700, -900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A09E)

    def lambda_A0B8():
        OP_95(0xFE, -600, 2700, -900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A0B8)
    SetChrPos(0xC, -3230, 0, 13720, 0)
    SetChrPos(0x9, 2160, 0, 13710, 0)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0x9, 0xFF)
    OP_68(650, 4000, 530, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(730, 0)
    SetCameraDistance(14000, 0)
    VolumeBGM(0x64, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)

    ChrTalk(
        0x101,
        "#2100417V#0005F#11P(Whoa...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100418V#0205F#11P(W-Well, there she is.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100419V#0105F#11P(Wow. She's absolutely incredible.)\x02",
    )

    CloseMessageWindow()
    OP_68(650, 4000, 2530, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-70, 4000, 24310, 0)
    MoveCamera(0, -5, -5, 0)
    OP_6E(900, 0)
    SetCameraDistance(13000, 0)
    OP_68(510, 3200, 24660, 17000)
    MoveCamera(312, 21, -10, 17000)
    OP_6E(800, 17000)
    SetCameraDistance(11000, 17000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    FadeToBright(1000, 0)
    BeginChrThread(0x101, 3, 0, 62)
    WaitChrThread(0x101, 3)
    SetChrPos(0x101, -650, 700, 10950, 0)
    SetChrPos(0x102, 490, 900, 10470, 0)
    SetChrPos(0x103, -600, 1350, 8220, 0)
    SetChrPos(0x104, 500, 1350, 8220, 0)
    StopBGM(0xFA0)
    Sleep(1500)
    Sound(853, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0x9, 1, 0, 63)

    def lambda_A2BA():

        label("loc_A2BA")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_A2BA")

    QueueWorkItem2(0xC, 0, lambda_A2BA)

    def lambda_A2CC():
        OP_96(0xFE, 0xFFFFF632, 0x0, 0x3714, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A2CC)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#2100458V#6105FOh?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)

    def lambda_A32B():
        OP_95(0xFE, 0, 1250, 18500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_A32B)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_68(60, 1500, 15290, 0)
    MoveCamera(63, 24, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(16000, 0)

    def lambda_A382():

        label("loc_A382")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_A382")

    QueueWorkItem2(0x101, 0, lambda_A382)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_A3A5():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A3A5)
    Sleep(100)

    def lambda_A3BD():
        OP_9B(0x1, 0xFE, 0x0, 0xD48, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A3BD)
    Sleep(50)

    def lambda_A3D5():
        OP_9B(0x1, 0xFE, 0x0, 0xF3C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A3D5)
    Sleep(80)

    def lambda_A3ED():
        OP_9B(0x1, 0xFE, 0x0, 0xED8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A3ED)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#2100421V#1809F#5PThank you for coming, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100422V#0006FS-Sorry. We didn't mean to bother you.\x02\x03",
            "#2100423V#0002FY-Yeah, you were... Just, wow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100424V#0206FUh... Um...\x02\x03",
            "#2100425V#0201FTh-That...was completely breathtaking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100426V#0302FI think I died and went to heaven for a\x01",
            "second there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100427V#0104FI'm blessed to have witnessed\x01",
            "something so extraordinary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100428V#6109FYou guys flatter me.\x02",
    )

    CloseMessageWindow()
    OP_68(-730, 1650, 13990, 2000)
    MoveCamera(47, 29, 0, 2000)
    OP_6E(730, 2000)
    SetCameraDistance(11500, 2000)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sound(814, 0, 60, 0)

    def lambda_A5F8():
        OP_9D(0xFE, 0x0, 0x0, 0x3E80, 0x5DC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A5F8)
    Sleep(450)
    SetChrSubChip(0x8, 0x3)
    WaitChrThread(0x8, 1)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    Sound(43, 0, 100, 0)
    OP_95(0x8, 0, 0, 15800, 1500, 0x0)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        "#2100429V#6106F#5PStill, it's nowhere near finished.\x02",
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

    ChrTalk(
        0x101,
        "#2100430V#0011F#6PSeriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100431V#0205F#12PYou intend to improve it even further?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100432V#6100F#5PWhy, of course.\x02\x03",
            "#2100433V#6104FThat particular routine was from one\x01",
            "of the Sun Princess' first scenes.\x02\x03",
            "#2100434VIt'll be even better once we add the\x01",
            "Moon Princess into the mix.\x02\x03",
            "#2100435V#6102FAs for the climax... Well, let's just say\x01",
            "this was NOTHING compared to what\x01",
            "that'll be like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100436V#0013F#6PWow, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100437V#0301F#12PGotta say, that's pretty damn amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100438V#0106F#12PIsn't it? I can't even imagine what it will\x01",
            "end up looking like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100439V#6104F#5PLook forward to it.\x02\x03",
            "#2100440V#6100FSo, Rixia. Are these the people you\x01",
            "were telling me about?\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x0)
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#2100441V#1802F#11PYes, that's right. This is the Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100442V#6100F#5PReally? You sure don't give off any\x01",
            "'cop' vibes, though.\x02\x03",
            "#2100443V#6106FAnyway, you want to investigate this\x01",
            "letter business?\x02\x03",
            "#2100444VYou know, I'd feel bad if you wasted\x01",
            "your time looking into a dumb prank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#2100445V#6PCome, now, Ilya.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2100446V#6PEveryone is worried about you. Why\x01",
            "don't you indulge us? Just a tad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100447V#6103F#5PWell, I dunno about that...\x02\x03",
            "#2100448VIt's never been my style to try and\x01",
            "reduce the pressure before a show.\x02\x03",
            "#2100449V#6102FBuuuut...if Rixia lets me give her\x01",
            "a special 'massage,' I'll consider it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x9,
        "#2100450V#1801F#11PN-No! Absolutely not!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2100451V#6P*sigh* I swear, what am I going to do\x01",
            "with you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#2100452V#0012F#6P(She's, uh, pretty different from her\x01",
            "stage persona.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100453V#0211F#12P(Reminds me of a creepy old lecher.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100454V#0106F#12P(I heard she had an...interesting personality,\x01",
            "but not to this extent.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100455V#0302F#12P(Kinda intense, ain't she?)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#2100456V#1806F#5PI'm so sorry, everyone.\x02\x03",
            "#2100457V#1801FLloyd, would you and the others mind\x01",
            "waiting in the lobby? I'll try my best to\x01",
            "persuade her somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AF1B():

        label("loc_AF1B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_AF1B")

    QueueWorkItem2(0x8, 0, lambda_AF1B)

    ChrTalk(
        0x8,
        "#2100420V#6105F#5PWhat was that?\x02",
    )

    CloseMessageWindow()
    OP_68(-1030, 1650, 13570, 1300)
    OP_96(0x8, 0xFFFFFE5C, 0x0, 0x39D0, 0x5DC, 0x0)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#2100459V#0005F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2100460V#1805F#5PWhat do you mean, Ilya?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100461V#6101F#5PYou said...'Lloyd,' right?\x02\x03",
            "#2100462VThat's you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100463V#0011F#6PY-Yes, I'm him. (Too close! Way too close!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100464V#6100F#5PAnd what's your last name?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100465V#0000F#6PUh... Bannings. My name's Lloyd Bannings.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0x8, 0x40)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#2100466V#6109F#5P#4SAhaha! I knew it!\x02",
    )

    CloseMessageWindow()
    OP_9A(0x8, 0x101, 0x190, 0x708, 0x0)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x20)
    Sound(804, 0, 100, 0)
    Sound(864, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(-440, 1450, 14120, 0)
    MoveCamera(123, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12500, 0)
    TurnDirection(0x102, 0x8, 0)
    TurnDirection(0x9, 0xC, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#2100467V#0011F#11PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100468V#0205F#11P...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100469V#0105FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100470V#0301F#11PYeah! What the hell, Lloyd?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2100471V#1801F#5PIlya, stop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#2100472V#12PWh-What is the meaning of this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100473V#6109FHooo boy, it's a small world!\x02\x03",
            "#2100474VWho woulda thought this'd be the day\x01",
            "I met the infamous little brother!\x02\x03",
            "#2100475V#6102FWell, now that I think about it, I'm pretty\x01",
            "sure she mentioned that you had joined\x01",
            "the police department...\x02\x03",
            "#2100476VHeehee! You're EXACTLY how I imagined\x01",
            "you'd be!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100477V#0011F#11PW-Wait a second. Does that mean...\x02\x03",
            "#2100478V...you're a friend of Cecile's or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100479V#6104FYep! Cecile's my best friend.\x02\x03",
            "#2100480VI've known her for about ten years now.\x01",
            "We met in Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100481V#0012F#11PI-I had no idea...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-780, 1650, 13530, 0)
    MoveCamera(47, 29, 0, 0)
    OP_6E(730, 0)
    SetCameraDistance(11500, 0)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x20)
    OP_96(0x8, 0xFFFFFD1C, 0x0, 0x3B9C, 0x3E8, 0x0)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#2100482VAllow me to introduce myself, then.\x02\x03",
            "#2100483VI'm Ilya Platiere, the figurehead\x01",
            "of Arc en Ciel, so to speak.\x02\x03",
            "#2100484VHappy to finally meet you, Lloyd!\x01",
            "And that goes for the rest of\x01",
            "you, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    SetCameraDistance(12000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x87, 3)
    SetScenarioFlags(0x5C, 1)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_64_9F10 end

    def Function_65_B739(): pass

    label("Function_65_B739")

    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 0, 0, 61)
    BeginChrThread(0x9, 2, 0, 49)

    def lambda_B754():
        OP_9D(0x9, 0xFA, 0xCB2, 0x5C58, 0x7D0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B754)
    Sleep(200)
    BeginChrThread(0x9, 2, 0, 51)
    BeginChrThread(0x9, 3, 0, 54)
    WaitChrThread(0x9, 1)
    OP_9D(0x9, 0x726, 0x4E2, 0x5C58, 0x1F4, 0x5DC)
    EndChrThread(0x9, 0x3)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x29)
    OP_9E(0x9, 0x0, 0x5DC0, 0x20F58, 0x1770, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)

    def lambda_B7CC():
        OP_9E(0x9, 0x0, 0x5DC0, 0x1B7740, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B7CC)
    Sleep(33)

    def lambda_B7EA():

        label("loc_B7EA")

        TurnDirection(0x9, 0x8, 0)
        Yield()
        Jump("loc_B7EA")

    QueueWorkItem2(0x9, 3, lambda_B7EA)
    BeginChrThread(0x9, 2, 0, 49)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x9, 2, 0, 49)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x9, 3, 0, 54)
    BeginChrThread(0x9, 2, 0, 51)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xBB8, 0x3E8)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x29)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x9, 0x3)
    OP_9E(0x9, 0x0, 0x5DC0, 0x50910, 0x1388, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 48)

    def lambda_B894():

        label("loc_B894")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_B894")

    QueueWorkItem2(0x9, 3, lambda_B894)
    OP_9D(0x9, 0xFFFFEFF2, 0x4E2, 0x5DDE, 0xBB8, 0x3E8)
    EndChrThread(0x9, 0x3)
    EndChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    Sleep(150)
    SetChrSubChip(0x9, 0x1)
    Sleep(150)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x0)
    Sleep(900)
    SetChrChipByIndex(0x9, 0x29)
    OP_95(0x9, -1420, 1250, 24000, 6000, 0x0)
    BeginChrThread(0x9, 2, 0, 47)
    BeginChrThread(0x9, 3, 0, 54)
    BeginChrThread(0x9, 0, 0, 61)
    OP_9D(0x9, 0x384, 0x4E2, 0x5BC2, 0x7D0, 0xDAC)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 57)

    def lambda_B933():
        OP_9D(0x9, 0xF28, 0x4E2, 0x5BC2, 0xDAC, 0x384)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B933)
    Sleep(1000)
    BeginChrThread(0x9, 2, 0, 51)
    BeginChrThread(0x9, 3, 0, 54)
    WaitChrThread(0x9, 1)
    EndChrThread(0x9, 0x0)

    def lambda_B967():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_B967)
    Return()

    # Function_65_B739 end

    def Function_66_B970(): pass

    label("Function_66_B970")

    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 0, 0, 61)
    BeginChrThread(0x8, 2, 0, 41)

    def lambda_B98B():
        OP_9D(0x8, 0xFFFFFF06, 0xCB2, 0x5C58, 0x7D0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B98B)
    Sleep(200)
    BeginChrThread(0x8, 2, 0, 43)
    BeginChrThread(0x8, 3, 0, 52)
    WaitChrThread(0x8, 1)
    OP_9D(0x8, 0xFFFFF8DA, 0x4E2, 0x5C58, 0x1F4, 0x5DC)
    EndChrThread(0x8, 0x3)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    OP_9E(0x8, 0x0, 0x5DC0, 0x20F58, 0x1770, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 3, 0, 52)

    def lambda_BA09():
        OP_9E(0x8, 0x0, 0x5DC0, 0x1B7740, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BA09)
    Sleep(33)

    def lambda_BA27():

        label("loc_BA27")

        TurnDirection(0x8, 0x9, 0)
        Yield()
        Jump("loc_BA27")

    QueueWorkItem2(0x8, 3, lambda_BA27)
    BeginChrThread(0x8, 2, 0, 41)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x8, 2, 0, 41)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x8, 3, 0, 52)
    BeginChrThread(0x8, 2, 0, 43)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xBB8, 0x3E8)
    CancelBlur(0)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x3)
    OP_9E(0x8, 0x0, 0x5DC0, 0x50910, 0x1388, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 40)

    def lambda_BAE8():

        label("loc_BAE8")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_BAE8")

    QueueWorkItem2(0x8, 3, lambda_BAE8)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_9D(0x8, 0x100E, 0x4E2, 0x5DDE, 0xBB8, 0x3E8)
    CancelBlur(0)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(150)
    SetChrSubChip(0x8, 0x1)
    Sleep(150)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(900)
    SetChrChipByIndex(0x8, 0x1F)
    OP_95(0x8, 1420, 1250, 23000, 6000, 0x0)
    BeginChrThread(0x8, 2, 0, 44)
    BeginChrThread(0x8, 3, 0, 52)
    BeginChrThread(0x8, 0, 0, 61)
    OP_9D(0x8, 0xFFFFFC7C, 0x4E2, 0x5BC2, 0x7D0, 0xDAC)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 56)

    def lambda_BB9E():
        OP_9D(0x8, 0xFFFFF0D8, 0x4E2, 0x5BC2, 0xDAC, 0x384)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BB9E)
    Sleep(1000)
    BeginChrThread(0x8, 2, 0, 43)
    BeginChrThread(0x8, 3, 0, 52)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)

    def lambda_BBD2():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_BBD2)
    Sleep(700)
    Return()

    # Function_66_B970 end

    def Function_67_BBDE(): pass

    label("Function_67_BBDE")

    OP_9B(0x1, 0xFE, 0x0, 0x1324, 0x7D0, 0x1)
    OP_95(0xFE, -1550, 0, 14280, 2000, 0x0)
    OP_93(0xFE, 0x168, 0x0)
    Return()

    # Function_67_BBDE end

    def Function_68_BC09(): pass

    label("Function_68_BC09")

    OP_9B(0x1, 0xFE, 0x0, 0x12C0, 0x7D0, 0x1)
    OP_95(0xFE, 1550, 0, 14280, 2000, 0x0)
    OP_93(0xFE, 0x168, 0x0)
    Return()

    # Function_68_BC09 end

    def Function_69_BC34(): pass

    label("Function_69_BC34")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0xC, 0xFF)
    LoadEffect(0x0, "event\\ev290_01.eff")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x2, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x2, 0x1, 0xBB8, 0xBB8, 0x0)
    ClearMapObjFlags(0x1B, 0x4)
    SetMapObjFrame(0x1B, "04Bback", 0x0, 0x1)
    SetMapObjFrame(0x1B, "04light_add", 0x0, 0x1)
    SetMapObjFrame(0x1B, "04Aback", 0x0, 0x1)
    SetMapObjFrame(0x1B, "04moon_add", 0x0, 0x1)
    SetMapObjFrame(0x1B, "04main2", 0x0, 0x1)
    SetMapObjFrame(0x1B, "02water01", 0x0, 0x1)
    SetMapObjFrame(0x1B, "02water02_add", 0x0, 0x1)
    SetMapObjFrame(0x1B, "ball", 0x0, 0x1)
    LoadChrToIndex("apl/ch50250.itc", 0x1E)
    LoadChrToIndex("apl/ch50251.itc", 0x1F)
    LoadChrToIndex("apl/ch50252.itc", 0x20)
    LoadChrToIndex("apl/ch50253.itc", 0x21)
    LoadChrToIndex("apl/ch50254.itc", 0x22)
    LoadChrToIndex("apl/ch50255.itc", 0x23)
    LoadChrToIndex("chr/ch09700.itc", 0x24)
    LoadChrToIndex("apl/ch50265.itc", 0x28)
    LoadChrToIndex("apl/ch50266.itc", 0x29)
    LoadChrToIndex("apl/ch50267.itc", 0x2A)
    LoadChrToIndex("apl/ch50268.itc", 0x2B)
    LoadChrToIndex("apl/ch50269.itc", 0x2C)
    LoadChrToIndex("apl/ch50270.itc", 0x2D)
    LoadChrToIndex("chr/ch09800.itc", 0x2E)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrPos(0x8, -2000, 1250, 24200, 90)
    SetChrPos(0x9, 2000, 1250, 24200, 270)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, 650, 2700, -1530, 0)
    SetChrPos(0x102, -520, 2700, -1410, 0)
    SetChrPos(0x104, 570, 2700, -2900, 0)
    SetChrPos(0x103, -600, 2700, -2900, 0)

    def lambda_BE54():
        OP_95(0xFE, 650, 2700, 530, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE54)

    def lambda_BE6E():
        OP_95(0xFE, -520, 2700, 410, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE6E)

    def lambda_BE88():
        OP_95(0xFE, 570, 2700, -900, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BE88)

    def lambda_BEA2():
        OP_95(0xFE, -600, 2700, -900, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BEA2)
    OP_68(1010, 3000, 740, 0)
    MoveCamera(49, 26, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22000, 0)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
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

    ChrTalk(
        0x101,
        "#2101301V#0011F#11P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101302V#0105F#11P*gasp*\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-70, 3200, 24310, 0)
    MoveCamera(0, 38, 0, 0)
    OP_6E(790, 0)
    SetCameraDistance(10500, 0)
    OP_68(470, 3200, 23470, 17000)
    MoveCamera(345, 21, -10, 17000)
    OP_6E(600, 17000)
    SetCameraDistance(17000, 17000)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    PlayBGM("ed7530", 1)
    BeginChrThread(0x101, 0, 0, 66)
    BeginChrThread(0x101, 1, 0, 65)
    WaitChrThread(0x101, 0)
    StopBGM(0xFA0)
    Sleep(2000)
    Fade(500)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x2)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x2)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        "#2101303V#6104F#40WPhew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2101304V#6206F#40W*pant* *pant*\x02",
    )

    CloseMessageWindow()
    Sound(853, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    Fade(500)
    SetChrPos(0x8, -1390, 1250, 21930, 180)
    SetChrPos(0x9, 1390, 1250, 21930, 180)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x101, -650, 0, 14950, 0)
    SetChrPos(0x102, 360, 0, 14950, 0)
    SetChrPos(0x103, -1410, 0, 14460, 0)
    SetChrPos(0x104, 1200, 0, 14370, 0)
    OP_68(160, 2200, 16370, 0)
    MoveCamera(0, 8, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(13470, 0)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        "#2101305V#6105F#5POh, look...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2101306V#6202F#11PYou're back.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x1000)
    ClearChrFlags(0x9, 0x1000)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x9, 0x20)

    def lambda_C1AC():
        OP_96(0x8, 0xFFFFFB64, 0x4E2, 0x4948, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C1AC)
    Sleep(200)

    def lambda_C1C9():
        OP_96(0x9, 0x4BA, 0x4E2, 0x4948, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C1C9)

    ChrTalk(
        0x104,
        "#2101307V#0309F#12P#NHot damn! Lucky us!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#2101308V#0002F#6P#NYou two are incredible!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#2101309V#0204F#6P#NIndeed. I have never experienced\x01",
            "anything quite like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x8, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#2101310V#6104F#5PYou think? Sounds like if we start ironing\x01",
            "out the kinks, this might become a crowd\x01",
            "favorite.\x02\x03",
            "#2101311V#6100FOh, that gives me an idea. How about we\x01",
            "put a little delay on the Moon Princess'\x01",
            "spin, Rixia?\x02\x03",
            "#2101312VThat way the Sun Princess will have to\x01",
            "respond in a way that should really wow\x01",
            "the audience.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    ChrTalk(
        0x9,
        "#2101313V#6200F#11PThat's perfect!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101314V#0104F#12P#NYour dancing isn't the only thing that's\x01",
            "amazing...\x02\x03",
            "#2101315V#0102FYou're building upon a finished scene,\x01",
            "even though you don't have to.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#2101316V#6109F#5PHow's that amazing? If we have the ability to\x01",
            "do it, we might as well strive for perfection till\x01",
            "it's time to perform.\x02\x03",
            "#2101317V#6100FBut enough about that. Any developments in\x01",
            "the investigation?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x9,
        "#2101318V#6205F#11POh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101319V#0108F#12P#NYes, actually.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#2101320V#0006F#6P#NIt's, uh, not exactly good news.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x9,
        "#2101321V#6201F#11PWh-What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101322V#6103F#5PHmm? All right, then.\x02\x03",
            "#2101323V#6100FLet me go grab Avan and then you\x01",
            "can fill us in on everything, 'kay?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    OP_93(0x8, 0x13B, 0x190)

    def lambda_C6FB():
        OP_95(0xFE, -6050, 1250, 24120, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C6FB)
    TurnDirection(0x9, 0x8, 500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_68(110, 1000, 17000, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(28500, 0)
    OP_68(110, 1000, 17000, 7000)
    MoveCamera(25, 24, 0, 13000)
    OP_6E(420, 13000)
    SetCameraDistance(22000, 13000)
    EndChrThread(0x8, 0xFF)
    OP_93(0x9, 0xE1, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -1180, 1250, 18760, 180)
    SetChrPos(0xC, -3170, 0, 16329, 60)
    TurnDirection(0xC, 0x101, 0)
    EndChrThread(0xC, 0xFF)
    FadeToBright(4000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#2101324V#5PThis Yin character sounds like he's quite\x01",
            "dangerous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2101325V#6205FYou can't be serious...\x02\x03",
            "#2101326V#6201FHe's really somewhere in the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101327V#6105FWowza! Ain't that a kicker?!\x02\x03",
            "#2101328V#6102FA shadowy, immortal assassin that the\x01",
            "Eastern Quarter sings legends about...?\x02\x03",
            "#2101329V#6109FOh, I love it! That character will play a\x01",
            "HUGE role in our next production!\x02\x03",
            "#2101330V#6102FActually, let's just throw him in! Couldn't\x01",
            "we use those white robes from the third\x01",
            "act as a costume?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_CA6A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_CA6A)
    Sleep(50)
    TurnDirection(0xC, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        "#2101331V#6P*sigh* Oh, Ilya...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2101332V#6206F#12PYou should probably try and take this\x01",
            "a little more seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101333V#0103F#12PAccording to our intel, a group known as\x01",
            "Heiyue appears to be employing a criminal\x01",
            "named Yin.\x02\x03",
            "#2101334V#0108FWe still don't quite understand why Yin sent\x01",
            "Ilya the threat letter in the first place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101335V#0001F#6PBut one thing is certain: The possibility that this\x01",
            "is just a prank has decreased exponentially.\x02\x03",
            "#2101336VIs there any chance you could postpone or--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101337V#6104FNot a chance, buddy.\x02\x03",
            "#2101338VWe wouldn't walk off the stage even\x01",
            "if a bomb was about to go off.\x02\x03",
            "#2101339V#6100FIsn't that right, Avan?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0xC,
        "#2101340VWell...I suppose so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2101341VThough we aren't all as rabid as Ilya, the truth\x01",
            "is that all members of Arc en Ciel are possessed\x01",
            "by the monster known as the stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2101342VYou wouldn't find one member of the troupe\x01",
            "who would refuse to appear on stage when\x01",
            "faced with the opportunity.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#2101343V#6206FU-Umm... I may be new to all this,\x01",
            "but I feel the same way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2101344V#0306F#12PI swear, you guys are obsessed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101345V#0200F#12PIf you intend to proceed with the show, would\x01",
            "you care if we handed over security duties to\x01",
            "someone else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101346V#6103FWell, I mean, it's pretty annoying. Buuut,\x01",
            "we all have to make sacrifices.\x02\x03",
            "#2101347V#6100FThose First Division guys... What kind of\x01",
            "people are they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101348V#0011F#6PGood question.\x02\x03",
            "#2101349V#0012FWell, they're definitely qualified. But, uh,\x01",
            "they might act a little TOO qualified at\x01",
            "times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101350V#0103F#12PObjectively speaking, they're excellent at\x01",
            "what they do.\x02\x03",
            "#2101351V#0100FThe First Division are an elite group that\x01",
            "lives up to their name.\x02\x03",
            "#2101352VThey should be able to protect you and\x01",
            "your show with the utmost discretion\x01",
            "until curtain call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101353V#6106FYuck. Just my luck.\x02\x03",
            "#2101354V#6101FThen again, we will have a full house.\x01",
            "Better safe than sorry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 500)
    Sleep(150)

    ChrTalk(
        0xC,
        "#2101355V#6PPatience, Ilya. Patience.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2101356V#6PAnyway, we ARE talking about you here,\x01",
            "Ilya. Once the play starts, I doubt you will\x01",
            "care much about what they do. Right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 500)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#2101357V#6101FHow rude! I'll have you know that I always\x01",
            "pay close attention to my audience.\x02\x03",
            "#2101358V#6104F'The show begins only when the audience\x01",
            "and play become as one.'\x02\x03",
            "#2101359V#6100FIsn't that one of your famous sayings?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2101360V#6PFor anyone else's case, yes. In yours,\x01",
            "however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2101361V#6PI'd say forcibly dragging everyone along\x01",
            "to your own rhythm is a bit more accurate.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2101362V#0012F#6P(He's not mincing his words at all, is he?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101363V#0202F#12P(Indeed. All the evidence indicates that Ilya\x01",
            "has a remarkable obsession with performing.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x9)
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "#2101364V#6201FE-Excuse me, Lloyd.\x02\x03",
            "#2101365VWhat will happen to your investigation?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    def lambda_D634():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D634)
    Sleep(50)

    def lambda_D644():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D644)
    Sleep(50)

    def lambda_D654():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D654)
    Sleep(50)

    def lambda_D664():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D664)
    Sleep(50)
    TurnDirection(0xC, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#2101366V#0006F#6PI'm really sorry, Rixia. We don't have much\x01",
            "wiggle room here.\x02\x03",
            "#2101367V#0000FThe First Division is most likely going to\x01",
            "take over the case. Good news is that I\x01",
            "doubt you have anything to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2101368V#6206FYou're officially off the case, then...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101369V#6100FWell, that's a bummer. Only reason I agreed\x01",
            "to all this was because you were leading the\x01",
            "show, Lloyd.\x02\x03",
            "#2101370VStill, I appreciate you looking into\x01",
            "things for us.\x02\x03",
            "#2101371V#6109FI'll send some tickets your way as thanks, so\x01",
            "be sure to come and see the play next time\x01",
            "you're free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2101372VHmm, I'm sure we can arrange something.\x01",
            "Though, I'm afraid you might have to wait\x01",
            "until after the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2101373VIf you're okay with tickets for next month,\x01",
            "I can have them sent to you as gifts.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 500)

    def lambda_D9B6():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D9B6)
    Sleep(50)

    def lambda_D9C6():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D9C6)
    Sleep(50)

    def lambda_D9D6():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D9D6)
    Sleep(50)

    def lambda_D9E6():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D9E6)
    TurnDirection(0x9, 0xC, 500)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#2101374V#0305F#11PSeriously?!\x02\x03",
            "#2101375V#0309FHell yes! And here I was thinkin' that I'd\x01",
            "have to wait TWO months to see it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101376V#0202F#11PIt is quite generous. Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101377V#0108F#11P#40W...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#2101378V#0001F#6P(Elie...?)\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_69_BC34 end

    SaveToFile()

Try(main)
