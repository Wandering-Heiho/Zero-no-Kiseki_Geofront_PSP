from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1500.bin",                # FileName
        "t1500",                    # MapName
        "t1500",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1500",                  # 0
        "Security Guard Tony",    # 1
        "Nurse Ada",              # 2
        "Janitor Dyson",          # 3
        "Michael",                # 4
        "Inpatient",              # 5
        "Girl",                   # 6
        "Visitor",                # 7
        "Visitor",                # 8
        "Harold",                 # 9
        "Jed",                    # 10
        "Kienz",                  # 11
        "Officer Kate",           # 12
        "Peter",                  # 13
        "Master Fisherman Lloyd", # 14
        "Mariabell",              # 15
        "Doctor Gailey",          # 16
        "Doctor Guenter",         # 17
        "Tourist Oshiell",        # 18
        "Tourist Lapis",          # 19
        "Nurse Cirone",           # 20
        "Bus",                    # 21
        "Bus 2",                  # 22
        "Cecile",                 # 23
        "Shizuku",                # 24
        "KeA",                    # 25
        "Arios",                  # 26
        "Chief Robert",           # 27
        "Head Nurse Martha",      # 28
        "Staffer",                # 29
        "Bus Passenger",          # 30
        "Bus Passenger",          # 31
        "Bus Passenger",          # 32
        "Bus Passenger",          # 33
        "Bus Passenger",          # 34
        "Ursula Road",            # 35
    ))

    AddCharChip((
        "chr/ch33400.itc",                   # 00
        "chr/ch22300.itc",                   # 01
        "chr/ch28600.itc",                   # 02
        "chr/ch29800.itc",                   # 03
        "chr/ch20200.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch34002.itc",                   # 06
        "chr/ch20400.itc",                   # 07
        "chr/ch20500.itc",                   # 08
        "chr/ch09300.itc",                   # 09
        "chr/ch31700.itc",                   # 0A
        "apl/ch50385.itc",                   # 0B
        "chr/ch30600.itc",                   # 0C
        "apl/ch50165.itc",                   # 0D
        "apl/ch50169.itc",                   # 0E
        "chr/ch05500.itc",                   # 0F
        "chr/ch32702.itc",                   # 10
        "chr/ch07100.itc",                   # 11
        "chr/ch32302.itc",                   # 12
        "chr/ch34500.itc",                   # 13
        "chr/ch29900.itc",                   # 14
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

    DeclNpc(-47560,  0,       4000,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-23040,  -1000,   -25909,  0,    257,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-30000,  -1000,   -20299,  246,  389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-31450,  -899,    -16190,  180,  469,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-25180,  -1000,   -26069,  180,  389,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-22350,  0,       -1309,   90,   389,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-21309,  0,       2299,    90,   389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-28590,  0,       2440,    135,  389,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-52279,  0,       16629,   267,  389,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-18430,  0,       -11560,  180,  389,  0x0, 0,   10,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-16340,  0,       -330,    45,   389,  0x0, 0,   11,  0,   0,   2,   0,   16,  255,  0)
    DeclNpc(-52270,  0,       13590,   305,  389,  0x0, 0,   12,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-21770,  -1000,   -26059,  180,  405,  0x0, 0,   13,  0,   255, 255, 0,   18,  255,  0)
    DeclNpc(-24059,  -1000,   -26069,  180,  405,  0x0, 0,   14,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(-51279,  0,       15350,   270,  389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-16829,  -1000,   -16360,  180,  469,  0x0, 0,   16,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(-29469,  -990,    -26069,  180,  389,  0x0, 0,   17,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-21010,  150,     -9489,   270,  405,  0x0, 0,   18,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(-9789,   0,       6489,    90,   385,  0x0, 0,   19,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-27200,  6000,    20219,   0,    389,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   0,   3,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 36,  -42.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.166666984558105,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 55,  -25.0,                 0.0,                   -1.0,                  5625.0,                [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.03333333134651184,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   5.0,                   -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 57,  -24.0,                 -17.0,                 -2.0,                  76.5625,               [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142686843872,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.800000190734863,     4.857142448425293,     0.4000000059604645,    1.0])
    DeclEvent(0x0000, 0, 58,  -42.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.166666984558105,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 59,  -47.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.833333969116211,    -0.0,                  0.20000000298023224,   1.0])

    DeclActor(-58000,  0,       4000,    1500,    -58000,  1500,    4000,    0x007C, 0,  32, 0x0000)
    DeclActor(-35100,  3000,    17000,   2000,    -35100,  4000,    17000,   0x007C, 0,  33, 0x0000)
    DeclActor(-36600,  3000,    25600,   2000,    -36600,  4000,    25600,   0x007C, 0,  34, 0x0000)
    DeclActor(-42000,  3000,    20600,   2000,    -42000,  4000,    20600,   0x007C, 0,  35, 0x0000)
    DeclActor(-16830,  -1000,   -27510,  1200,    -17180,  -2000,   -32770,  0x007C, 0,  31, 0x0000)
    DeclActor(-7880,   0,       6560,    1200,    -7880,   1500,    6560,    0x007C, 0,  65, 0x0000)
    DeclActor(-36860,  0,       14360,   1200,    -36860,  1500,    14360,   0x007C, 0,  66, 0x0000)
    DeclActor(-49630,  0,       17190,   1200,    -49630,  2000,    17190,   0x007C, 0,  30, 0x0000)
    DeclActor(-35100,  3000,    17000,   2000,    -35100,  4000,    17000,   0x007C, 0,  63, 0x0000)

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "Ursula Road")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")
    PlaceName(-48.0, 0.0, 17.25, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_944",          # 00, 0
        "Function_1_9FC",          # 01, 1
        "Function_2_A5D",          # 02, 2
        "Function_3_A88",          # 03, 3
        "Function_4_AAE",          # 04, 4
        "Function_5_DBA",          # 05, 5
        "Function_6_1136",         # 06, 6
        "Function_7_2482",         # 07, 7
        "Function_8_3833",         # 08, 8
        "Function_9_3E9F",         # 09, 9
        "Function_10_40A5",        # 0A, 10
        "Function_11_4501",        # 0B, 11
        "Function_12_46E6",        # 0C, 12
        "Function_13_47BC",        # 0D, 13
        "Function_14_4860",        # 0E, 14
        "Function_15_4AD5",        # 0F, 15
        "Function_16_4BBC",        # 10, 16
        "Function_17_4C64",        # 11, 17
        "Function_18_500A",        # 12, 18
        "Function_19_50AE",        # 13, 19
        "Function_20_523C",        # 14, 20
        "Function_21_590D",        # 15, 21
        "Function_22_5D09",        # 16, 22
        "Function_23_5EE6",        # 17, 23
        "Function_24_6182",        # 18, 24
        "Function_25_6306",        # 19, 25
        "Function_26_63C4",        # 1A, 26
        "Function_27_64DD",        # 1B, 27
        "Function_28_6572",        # 1C, 28
        "Function_29_6B4B",        # 1D, 29
        "Function_30_6C3A",        # 1E, 30
        "Function_31_6C48",        # 1F, 31
        "Function_32_6D37",        # 20, 32
        "Function_33_6ED3",        # 21, 33
        "Function_34_6ED7",        # 22, 34
        "Function_35_6F4E",        # 23, 35
        "Function_36_6FF7",        # 24, 36
        "Function_37_7A0B",        # 25, 37
        "Function_38_8332",        # 26, 38
        "Function_39_83FD",        # 27, 39
        "Function_40_84D5",        # 28, 40
        "Function_41_8565",        # 29, 41
        "Function_42_85DE",        # 2A, 42
        "Function_43_88C1",        # 2B, 43
        "Function_44_8AF6",        # 2C, 44
        "Function_45_A024",        # 2D, 45
        "Function_46_A0B6",        # 2E, 46
        "Function_47_A123",        # 2F, 47
        "Function_48_A882",        # 30, 48
        "Function_49_B48D",        # 31, 49
        "Function_50_B52C",        # 32, 50
        "Function_51_B5BE",        # 33, 51
        "Function_52_B650",        # 34, 52
        "Function_53_B6E2",        # 35, 53
        "Function_54_B737",        # 36, 54
        "Function_55_B750",        # 37, 55
        "Function_56_C731",        # 38, 56
        "Function_57_D586",        # 39, 57
        "Function_58_F5AC",        # 3A, 58
        "Function_59_F81A",        # 3B, 59
        "Function_60_FEBC",        # 3C, 60
        "Function_61_FEE5",        # 3D, 61
        "Function_62_FEF0",        # 3E, 62
        "Function_63_108C8",       # 3F, 63
        "Function_64_10EBA",       # 40, 64
        "Function_65_113FC",       # 41, 65
        "Function_66_1144F",       # 42, 66
    ))


    def Function_0_944(): pass

    label("Function_0_944")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_984"),
        (1, "loc_990"),
        (2, "loc_99C"),
        (3, "loc_9A8"),
        (4, "loc_9B4"),
        (5, "loc_9C0"),
        (6, "loc_9CC"),
        (SWITCH_DEFAULT, "loc_9D8"),
    )


    label("loc_984")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_990")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_99C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_9A8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_9B4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_9C0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_9CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_9D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_9E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9FB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_9FB")

    Return()

    # Function_0_944 end

    def Function_1_9FC(): pass

    label("Function_1_9FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A5C")
    OP_95(0xFE, -23040, 0, -6950, 2000, 0x0)
    OP_95(0xFE, -24930, 0, -6950, 2000, 0x0)
    OP_95(0xFE, -24930, -1000, -23250, 2000, 0x0)
    OP_95(0xFE, -23040, -1000, -23250, 2000, 0x0)
    Jump("Function_1_9FC")

    label("loc_A5C")

    Return()

    # Function_1_9FC end

    def Function_2_A5D(): pass

    label("Function_2_A5D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A87")
    OP_94(0xFE, 0xFFFFB01E, 0xFFFFF8DA, 0xFFFFC9BE, 0x564, 0x3E8)
    Sleep(400)
    Jump("Function_2_A5D")

    label("loc_A87")

    Return()

    # Function_2_A5D end

    def Function_3_A88(): pass

    label("Function_3_A88")

    SetChrPos(0xFE, -58500, 0, 500, 4000)
    OP_97(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1388, 0x0)
    Return()

    # Function_3_A88 end

    def Function_4_AAE(): pass

    label("Function_4_AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AC2")
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_B00")

    label("loc_AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_AD0")
    Jump("loc_B00")

    label("loc_AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_ADE")
    Jump("loc_B00")

    label("loc_ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_AEC")
    Jump("loc_B00")

    label("loc_AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_AFA")
    Jump("loc_B00")

    label("loc_AFA")

    BeginChrThread(0x9, 0, 0, 1)

    label("loc_B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B0E")
    Jump("loc_D43")

    label("loc_B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B21")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_D43")

    label("loc_B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_B57")
    SetChrPos(0x8, -24640, 0, -1950, 135)
    SetChrPos(0x9, -23350, 0, -3110, 315)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_D43")

    label("loc_B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B74")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_D43")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B8C")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_D43")

    label("loc_B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_B9F")
    SetChrFlags(0x9, 0x80)
    Jump("loc_D43")

    label("loc_B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_BCF")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCA")
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)

    label("loc_BCA")

    Jump("loc_D43")

    label("loc_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_BE2")
    ClearChrFlags(0x12, 0x80)
    Jump("loc_D43")

    label("loc_BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_BF0")
    Jump("loc_D43")

    label("loc_BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C23")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x9, -30620, -1000, -17090, 317)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_D43")

    label("loc_C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C36")
    ClearChrFlags(0x16, 0x80)
    Jump("loc_D43")

    label("loc_C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_C49")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_D43")

    label("loc_C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C5D")
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_D43")

    label("loc_C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_C7B")
    ClearChrFlags(0x10, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0x18, 0x80)
    Jump("loc_D43")

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_C8E")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_D43")

    label("loc_C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_CD9")
    SetChrPos(0xA, -39100, 3000, 21560, 315)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xD, -26990, 0, 1930, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, -26490, -1000, -25270, 180)
    Jump("loc_D43")

    label("loc_CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_D02")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x9, -26490, -1000, -25270, 180)
    Jump("loc_D43")

    label("loc_D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_D2B")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x9, -26490, -1000, -25270, 180)
    Jump("loc_D43")

    label("loc_D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_D43")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5B")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)

    label("loc_D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_D6F")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 44)
    Jump("loc_D92")

    label("loc_D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_D83")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 48)
    Jump("loc_D92")

    label("loc_D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_D92")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 56)

    label("loc_D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_DA1")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 27)

    label("loc_DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_DB9")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 29)

    label("loc_DB9")

    Return()

    # Function_4_AAE end

    def Function_5_DBA(): pass

    label("Function_5_DBA")

    SetMapObjFlags(0x7, 0x4)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DEC")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DFF")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E12")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E25")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E38")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_E38")

    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E56")
    OP_66(0x1, 0x1)

    label("loc_E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E68")
    OP_66(0x2, 0x1)

    label("loc_E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E7A")
    OP_66(0x3, 0x1)

    label("loc_E7A")

    OP_65(0x8, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E98")
    OP_66(0x8, 0x1)

    label("loc_E98")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -17180, -2000, -32770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF0")

    label("loc_EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F1C")
    OP_11(0xFD, 0xD5, 0xC6, 0x19, 0xC8, 0x0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    Jump("loc_F6F")

    label("loc_F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F48")
    OP_11(0xFD, 0xD5, 0xC6, 0x19, 0xC8, 0x0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    Jump("loc_F6F")

    label("loc_F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F6F")
    OP_11(0xFD, 0xD5, 0xC6, 0x19, 0xC8, 0x0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)

    label("loc_F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_FB9")
    SetMapObjFrame(0xFF, "model6", 0x1, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x1, 0x2)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jump("loc_FED")

    label("loc_FB9")

    SetMapObjFrame(0xFF, "model6", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x2)

    label("loc_FED")

    SetMapObjFlags(0xB, 0x4)
    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_102A")
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    ClearMapObjFlags(0xB, 0x4)
    OP_66(0x7, 0x1)
    Jump("loc_102F")

    label("loc_102A")

    OP_16(0x3, 0x3, 0x1, 0x0)

    label("loc_102F")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1056")
    ClearMapObjFlags(0x8, 0x4)

    label("loc_1056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1069")
    ModifyEventFlags(1, 10, 0x80)

    label("loc_1069")

    SetMapObjFlags(0x9, 0x4)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    SetMapObjFrame(0xA, "patlight", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B3")
    ClearMapObjFlags(0x9, 0x4)

    label("loc_10B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C7")
    ClearMapObjFlags(0xA, 0x4)

    label("loc_10C7")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10DF")
    OP_1B(0x0, 0x0, 0x40)

    label("loc_10DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F2")
    OP_1B(0x0, 0x0, 0x40)

    label("loc_10F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1105")
    OP_1B(0x0, 0x0, 0x40)

    label("loc_1105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1118")
    OP_1B(0x0, 0x0, 0x40)

    label("loc_1118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_112B")
    OP_1B(0x0, 0x0, 0x40)

    label("loc_112B")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    Return()

    # Function_5_DBA end

    def Function_6_1136(): pass

    label("Function_6_1136")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_12A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1219")

    ChrTalk(
        0xFE,
        "Welcome to St. Ursula Hospital.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You, with the blue hair... Are you feeling\x01",
            "all right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0205FOh, yes. Thanks to the hospital staff, I am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm just glad to see you recovered.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_129C")

    label("loc_1219")


    ChrTalk(
        0xFE,
        (
            "I was a bit startled when your friend here\x01",
            "collapsed all of a sudden yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm glad to see she's recovered already.\x02",
    )

    CloseMessageWindow()

    label("loc_129C")

    Jump("loc_247E")

    label("loc_12A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1354")
    TurnDirection(0xFE, 0x9, 0)

    ChrTalk(
        0xFE,
        (
            "Those wolf attacks from a few months ago\x01",
            "ended up getting my shift extended, so I've\x01",
            "been a bit exhausted myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Looks like we both have it rough.\x02",
    )

    CloseMessageWindow()
    Jump("loc_247E")

    label("loc_1354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_140E")

    ChrTalk(
        0xFE,
        (
            "The hospital's been bringing in a lot\x01",
            "of scary-looking guys all morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't say I was expecting that when I woke\x01",
            "up today. Did something happen in the city?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247E")

    label("loc_140E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1471")

    ChrTalk(
        0xFE,
        "Good afternoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You didn't bring that adorable little girl\x01",
            "with you today?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247E")

    label("loc_1471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_14F8")

    ChrTalk(
        0xFE,
        "The green-haired girl?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think I've seen her out here.\x01",
            "Maybe she's still inside of the hospital grounds?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247E")

    label("loc_14F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_166C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DE")

    ChrTalk(
        0xFE,
        (
            "Hello there. Welcome to St. Ursula\x01",
            "Medical College.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FGood morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha. Full of energy, are we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As I'm sure you're aware, you can find the\x01",
            "reception desk in the hospital lobby.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1667")

    label("loc_15DE")


    ChrTalk(
        0xFE,
        (
            "The bus just left, so you're going to have\x01",
            "to wait a bit before the next one comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You'll find the receptionist in the lobby.\x02",
    )

    CloseMessageWindow()

    label("loc_1667")

    Jump("loc_247E")

    label("loc_166C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_188F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A2")

    ChrTalk(
        0xFE,
        (
            "A little while ago, I caught Doctor Guenter\x01",
            "trying to sneak onto the road with all of\x01",
            "his fishing gear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I stopped him and explained that the\x01",
            "road's dangerous, he tossed me one mira\x01",
            "and told me to let this be our little secret...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Pretty stingy guy, if you ask me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_188A")

    label("loc_17A2")


    ChrTalk(
        0xFE,
        (
            "Earlier, Doctor Guenter tried to sneak\x01",
            "away and go fishing. He even tossed me\x01",
            "one mira to stay quiet about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, a few nurses and interns caught\x01",
            "him and dragged him back inside, so I\x01",
            "guess all's well that ends well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_188A")

    Jump("loc_247E")

    label("loc_188F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_192D")

    ChrTalk(
        0xFE,
        "Good afternoon, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're not hurt or sick, are you?\x01",
            "Remember to not go overboard with things\x01",
            "during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247E")

    label("loc_192D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1AA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19FB")

    ChrTalk(
        0xFE,
        "Welcome to St. Ursula Hospital.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That car in the parking lot is amazing.\x01",
            "Isn't it one of those fancy limousines?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... I guess rich people have\x01",
            "to drive in luxury.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AA2")

    label("loc_19FB")


    ChrTalk(
        0xFE,
        (
            "Take a look at that limousine. If it really\x01",
            "is one of the newer models, I bet it\x01",
            "must have cost a fortune.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess rich people have\x01",
            "to drive in luxury, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA2")

    Jump("loc_247E")

    label("loc_1AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B53")

    ChrTalk(
        0xFE,
        "Hello, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The city is in the middle of celebrating the\x01",
            "Anniversary Festival. I'm sure you all are\x01",
            "looking forward to the festivities, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247E")

    label("loc_1B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1BFD")

    ChrTalk(
        0xFE,
        "Welcome to St. Ursula, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately, all I've been hearing about\x01",
            "is that Arc en Ciel troupe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I sort of want to see them, to be honest...\x02",
    )

    CloseMessageWindow()
    Jump("loc_247E")

    label("loc_1BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1E30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D6A")

    ChrTalk(
        0xFE,
        (
            "Recently, the hospital has been outfitted with a\x01",
            "special kind of orbal vehicle called an ambulance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now we can rush to wherever someone is\x01",
            "and stabilize them. It's much faster than the\x01",
            "bus service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When those gang members were attacked,\x01",
            "way back when, they managed to survive\x01",
            "because of the ambulance's fast response time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E2B")

    label("loc_1D6A")


    ChrTalk(
        0xFE,
        (
            "No matter where you are in the state, with\x01",
            "just one call, an ambulance will come\x01",
            "rushing to help you in an emergency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They even have the horsepower to\x01",
            "outrace your average orbal car.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E2B")

    Jump("loc_247E")

    label("loc_1E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1FA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F1D")

    ChrTalk(
        0xFE,
        "Heading back already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're returning to Crossbell City,\x01",
            "I recommend you wait at the bus\x01",
            "stop right over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No need to hurry, though. There will be\x01",
            "more buses coming before the day ends.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FA2")

    label("loc_1F1D")


    ChrTalk(
        0xFE,
        (
            "If you're aiming for Crossbell City,\x01",
            "I recommend you wait at the bus\x01",
            "stop right over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyway, how about this sunset?\x02",
    )

    CloseMessageWindow()

    label("loc_1FA2")

    Jump("loc_247E")

    label("loc_1FA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_21A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2123")

    ChrTalk(
        0xFE,
        (
            "On the evening one of our interns\x01",
            "was attacked, there was this really\x01",
            "annoying trader that visited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He kept trying to sell us some sheets and other\x01",
            "stuff at ridiculous prices. He wouldn't back down,\x01",
            "so I was asked to deal with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish I could be more help, but I was\x01",
            "in the middle of handling that nuisance\x01",
            "while the attack happened.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21A1")

    label("loc_2123")


    ChrTalk(
        0xFE,
        (
            "I was preoccupied that evening, busy\x01",
            "dealing with an irritating trader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sorry, but I didn't really notice anything.\x02",
    )

    CloseMessageWindow()

    label("loc_21A1")

    Jump("loc_247E")

    label("loc_21A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_23BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_236E")

    ChrTalk(
        0xFE,
        (
            "We just received a call from the bus that\x01",
            "was supposed to arrive earlier. Apparently\x01",
            "they were attacked by monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No need to worry, though. A pair of bracers\x01",
            "came and took care of them, no problem.\x01",
            "Always on the job, those bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FI guess we didn't leave a lasting impression.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011FI mean, I can't deny that Estelle and\x01",
            "Joshua were pretty impressive, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#1300FDon't let it bring you down.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23B9")

    label("loc_236E")


    ChrTalk(
        0xFE,
        (
            "Bracers sure are amazing. Maybe\x01",
            "I should learn a bit more about them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B9")

    Jump("loc_247E")

    label("loc_23BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_247E")

    ChrTalk(
        0xFE,
        (
            "Good morning. Welcome to St. Ursula\x01",
            "Medical College. Though, I'm sure you\x01",
            "know us as Crossbell's hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you outpatients? If so, just head\x01",
            "on into the hospital lobby.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_247E")

    TalkEnd(0xFE)
    Return()

    # Function_6_1136 end

    def Function_7_2482(): pass

    label("Function_7_2482")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2538")

    ChrTalk(
        0xFE,
        "A morning walk is good for your health, you know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And since I always have to accompany patients on\x01",
            "their walks, I'm able to kill two birds with one stone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382F")

    label("loc_2538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_25BC")

    ChrTalk(
        0xFE,
        "I'm on shift, today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's stressful being a nurse. We have to take care\x01",
            "of both our patients and ourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382F")

    label("loc_25BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_260F")

    ChrTalk(
        0xFE,
        (
            "I hope that patient that was carried\x01",
            "to the ICU will be okay...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382F")

    label("loc_260F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_26D0")

    ChrTalk(
        0xFE,
        (
            "The staff here tries to build relationships\x01",
            "with our patients, so you can't blame us\x01",
            "for being worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just need to cheer up and do my\x01",
            "job to the best of my ability.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382F")

    label("loc_26D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_276F")

    ChrTalk(
        0xFE,
        (
            "Oh, Cecile's little brother...?\x01",
            "Oh, my, isn't she a cutie!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Make sure she doesn't get lost, okay?\x01",
            "The hospital can get hectic at times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382F")

    label("loc_276F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_291F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_285F")

    ChrTalk(
        0xFE,
        "The festival ends today, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You all must have been swamped with\x01",
            "work these past few days. Hopefully,\x01",
            "everything starts to wind down now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're almost to the finish line,\x01",
            "so let's end it strong!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_291A")

    label("loc_285F")


    ChrTalk(
        0xFE,
        (
            "The festival ends today... Hopefully, that\x01",
            "means I'll be able to get some more sleep\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll just have to do my very best today;\x01",
            "then I can have a well-deserved rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_291A")

    Jump("loc_382F")

    label("loc_291F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A0D")

    ChrTalk(
        0xFE,
        (
            "Michael's condition has been good today,\x01",
            "so he's been allowed to come outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He still has to stay on the premises, though.\x01",
            "But since he's usually cooped up in a bed,\x01",
            "I think a change of scenery will do him good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382F")

    label("loc_2A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2B87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B1B")

    ChrTalk(
        0xFE,
        (
            "There are quite a lot of patients that\x01",
            "request leave from the hospital, if only\x01",
            "for the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Due to their illnesses and the fact that\x01",
            "they need to be periodically checked on\x01",
            "by the doctors, they're usually declined.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B82")

    label("loc_2B1B")


    ChrTalk(
        0xFE,
        (
            "I understand that they want to have fun\x01",
            "at the festival, but...I can't help\x01",
            "but worry about them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B82")

    Jump("loc_382F")

    label("loc_2B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2F5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F17")

    ChrTalk(
        0xFE,
        "Oh, good morning.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_2D26")

    ChrTalk(
        0xFE,
        (
            "The concert yesterday was great,\x01",
            "wasn't it, Randy? Thank you so\x01",
            "much for inviting me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know the other girls had a great\x01",
            "time, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FHeh. Showin' ladies a good time\x01",
            "is my life's mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FGoing on a date with three different\x01",
            "nurses is pretty daring, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FYou're telling me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211FWell, isn't someone popular?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F0F")

    label("loc_2D26")


    ChrTalk(
        0xFE,
        (
            "Oh, Randy, Lloyd! The concert yesterday was\x01",
            "SO fun, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Philia and Lan couldn't stop talking\x01",
            "about you two after we left, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FHeh. Showin' ladies a good time\x01",
            "is my life's mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI appreciated the invitation. I thought\x01",
            "it ended up being a great time, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FTh-The two of you went on a date\x01",
            "with three nurses? Randy, sure,\x01",
            "but you, too, Lloyd...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211FMy, someone is quite popular.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Spare me the death stare, Tio...)\x02",
    )

    CloseMessageWindow()

    label("loc_2F0F")

    SetScenarioFlags(0x0, 1)
    Jump("loc_2F59")

    label("loc_2F17")


    ChrTalk(
        0xFE,
        (
            "Well, yesterday was fun, but now\x01",
            "it's time to focus on work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F59")

    Jump("loc_382F")

    label("loc_2F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3149")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30AC")

    ChrTalk(
        0xFE,
        "The Anniversary Festival is only a month away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Philia invited me to come along, but I don't\x01",
            "know if I can take some time off yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309FHaha, I hope ya can! I'm pumped for it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    ChrTalk(
        0xFE,
        "Um...I'll try, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(It sounds like Randy invited her and her\x01",
            "friends to the festival...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3144")

    label("loc_30AC")


    ChrTalk(
        0xFE,
        (
            "I sure hope I can take some\x01",
            "time off for the festival...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if I keep working hard, I'm sure\x01",
            "I'll be able to negotiate for a little break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3144")

    Jump("loc_382F")

    label("loc_3149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3247")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_320D")

    ChrTalk(
        0xFE,
        (
            "Oh, you're Cecile's little brother,\x01",
            "aren't you? How have you been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FFor whatever reason, it feels like I've\x01",
            "become a celebrity among the nursing\x01",
            "staff...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3242")

    label("loc_320D")


    ChrTalk(
        0xFE,
        (
            "Oh, Cecile's little brother!\x01",
            "How have you been?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3242")

    Jump("loc_382F")

    label("loc_3247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_3332")

    ChrTalk(
        0xFE,
        (
            "The way the sunset reflects off of Lake Elm is\x01",
            "gorgeous. I'm telling you, that sight is strong\x01",
            "enough to make any stress disappear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, enough of that. It's time for me to\x01",
            "start preparing for tonight's watch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382F")

    label("loc_3332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_346B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3432")
    TurnDirection(0xFE, 0xC, 0)

    ChrTalk(
        0xFE,
        (
            "Come on, mister. The sun's already setting,\x01",
            "and you need to get back to your room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hohoho, right you are, dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I don't want to push myself too hard, with the\x01",
            "date of my hospital discharge fast approaching.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3466")

    label("loc_3432")


    ChrTalk(
        0xFE,
        "I need to get this gentleman back to his room.\x02",
    )

    CloseMessageWindow()

    label("loc_3466")

    Jump("loc_382F")

    label("loc_346B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_3679")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35AE")

    ChrTalk(
        0xFE,
        "Oh, Cecile... Wait, who are they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1300FThis is my little brother, Lloyd,\x01",
            "and his group of lovers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Th-That many...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011FC-Cut it out, Cecile! You're taking\x01",
            "this joke way too far now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#1309FOh, please. I'm just teasing you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You had me fooled for a second there...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3674")

    label("loc_35AE")


    ChrTalk(
        0xFE,
        (
            "I already knew about Lloyd because\x01",
            "Cecile talks about him a lot, but not\x01",
            "about the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whenever Cecile tells me something...\x01",
            "it's pretty hard to tell whether it's the\x01",
            "truth or a joke.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3674")

    Jump("loc_382F")

    label("loc_3679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_382F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37EA")

    ChrTalk(
        0xFE,
        (
            "Good morning, everyone. Are you\x01",
            "here to visit a patient?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FWow, nice...VERY nice!\x02\x03",
            "#0309FI knew it! Seein' the genuine article\x01",
            "is SO much better than pictures!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0205FGenuine? What on earth are you\x01",
            "talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0104FIt'd be best to just ignore him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I-I'm sorry...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FYou'll have to forgive him for us.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_382F")

    label("loc_37EA")


    ChrTalk(
        0xFE,
        (
            "Well, he's certainly lively. So, are\x01",
            "you here to visit someone?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_382F")

    TalkEnd(0xFE)
    Return()

    # Function_7_2482 end

    def Function_8_3833(): pass

    label("Function_8_3833")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3911")

    ChrTalk(
        0xFE,
        (
            "Sometimes I hear people say janitor\x01",
            "work is insignificant, but I don't see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have so many things to be responsible\x01",
            "for, and I'm proud to do them. I don't care\x01",
            "what people say. I like my job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E9B")

    label("loc_3911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_391F")
    Jump("loc_3E9B")

    label("loc_391F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_392D")
    Jump("loc_3E9B")

    label("loc_392D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_39C9")

    ChrTalk(
        0xFE,
        (
            "Doctor Gailey is constantly sulking\x01",
            "on that bench over there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess even big-time doctors like\x01",
            "him have their share of worries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E9B")

    label("loc_39C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_39D7")
    Jump("loc_3E9B")

    label("loc_39D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_39E5")
    Jump("loc_3E9B")

    label("loc_39E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_39F3")
    Jump("loc_3E9B")

    label("loc_39F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3A49")

    ChrTalk(
        0xFE,
        (
            "I have to water the flowers every day\x01",
            "so they don't begin to wilt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E9B")

    label("loc_3A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3A57")
    Jump("loc_3E9B")

    label("loc_3A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3B36")

    ChrTalk(
        0xFE,
        (
            "I genuinely feel at home here. Maybe it's\x01",
            "because of the view of Lake Elm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sure, the Anniversary Festival may be\x01",
            "going on, but to the patients who can't\x01",
            "travel, out here is like a beautiful oasis.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E9B")

    label("loc_3B36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3C18")

    ChrTalk(
        0xFE,
        (
            "I've even heard some of them talk about\x01",
            "how soothing all the greenery is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to bring a little peace of mind to\x01",
            "the patients, a bunch of flowers and greenery\x01",
            "were planted on the hospital grounds.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E9B")

    label("loc_3C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3C26")
    Jump("loc_3E9B")

    label("loc_3C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_3CB9")

    ChrTalk(
        0xFE,
        (
            "Installing that fence was a pretty\x01",
            "smart idea, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll do my part and be on\x01",
            "the lookout for monsters, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E9B")

    label("loc_3CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_3D58")

    ChrTalk(
        0xFE,
        (
            "Did you finish your investigation yet?\x01",
            "Find out anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If no one's on the roof right now, I guess\x01",
            "I'll go ahead and start cleaning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E9B")

    label("loc_3D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_3E13")

    ChrTalk(
        0xFE,
        (
            "I've been working in hospitals for a long\x01",
            "time now, and I can say, without a doubt,\x01",
            "that this place is the fanciest of them all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Now, if I move this over there...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E9B")

    label("loc_3E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3E9B")

    ChrTalk(
        0xFE,
        "You guys lost or something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're looking for the main part of the\x01",
            "hospital, it's that big building in the back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E9B")

    TalkEnd(0xFE)
    Return()

    # Function_8_3833 end

    def Function_9_3E9F(): pass

    label("Function_9_3E9F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F33")
    Jump("loc_3F7D")

    label("loc_3F33")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F53")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F7D")

    label("loc_3F53")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F73")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F7D")

    label("loc_3F73")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F7D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4033")

    ChrTalk(
        0xFE,
        (
            "Someone from the IBC came and\x01",
            "gave me a stuffed bear yesterday.\x01",
            "Haha... I love it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mr. Crois sure is nice, isn't he?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_409D")

    label("loc_4033")


    ChrTalk(
        0xFE,
        "The breeze feels so amazing today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time I go on a walk, I'll have to\x01",
            "take Shizuku with me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_409D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_3E9F end

    def Function_10_40A5(): pass

    label("Function_10_40A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_40B6")
    Jump("loc_44FD")

    label("loc_40B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_40C4")
    Jump("loc_44FD")

    label("loc_40C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_40D2")
    Jump("loc_44FD")

    label("loc_40D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_40E0")
    Jump("loc_44FD")

    label("loc_40E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_40EE")
    Jump("loc_44FD")

    label("loc_40EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_40FC")
    Jump("loc_44FD")

    label("loc_40FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_410A")
    Jump("loc_44FD")

    label("loc_410A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4118")
    Jump("loc_44FD")

    label("loc_4118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4126")
    Jump("loc_44FD")

    label("loc_4126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4134")
    Jump("loc_44FD")

    label("loc_4134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4142")
    Jump("loc_44FD")

    label("loc_4142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4150")
    Jump("loc_44FD")

    label("loc_4150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_415E")
    Jump("loc_44FD")

    label("loc_415E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_4208")

    ChrTalk(
        0xFE,
        (
            "Hoho, I suppose she's right.\x01",
            "I'll head on back inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm just about to be discharged, so I don't\x01",
            "want to go ruin it by pushing myself too\x01",
            "hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44FD")

    label("loc_4208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_43A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_436A")

    ChrTalk(
        0x136,
        "#1300FMister, how's your knee feeling today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It feels like I'm a youngster again.\x01",
            "I think getting treatment here was\x01",
            "the right decision after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1300FThat's wonderful to hear.\x02\x03",
            "Doctor Belldine said you would be able\x01",
            "to leave soon, so hang in there, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0004F(Cecile's really at home here, isn't she?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43A2")

    label("loc_436A")


    ChrTalk(
        0xFE,
        (
            "I get to leave soon, eh? Hohoho,\x01",
            "that's good news.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43A2")

    Jump("loc_44FD")

    label("loc_43A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_44FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4487")

    ChrTalk(
        0xFE,
        (
            "You know, I first came here because\x01",
            "I slipped in my bathroom and landed\x01",
            "on my knee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Only reason I'm able to take strolls\x01",
            "like this is due to all the doctors and\x01",
            "staff helping me recover.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44FD")

    label("loc_4487")


    ChrTalk(
        0xFE,
        (
            "Honestly, I didn't think I would be able\x01",
            "to walk this well for a long time... The\x01",
            "staff here are second to none.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44FD")

    TalkEnd(0xFE)
    Return()

    # Function_10_40A5 end

    def Function_11_4501(): pass

    label("Function_11_4501")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4512")
    Jump("loc_46E2")

    label("loc_4512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_4520")
    Jump("loc_46E2")

    label("loc_4520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_452E")
    Jump("loc_46E2")

    label("loc_452E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_453C")
    Jump("loc_46E2")

    label("loc_453C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_454A")
    Jump("loc_46E2")

    label("loc_454A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_4558")
    Jump("loc_46E2")

    label("loc_4558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4566")
    Jump("loc_46E2")

    label("loc_4566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4574")
    Jump("loc_46E2")

    label("loc_4574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4582")
    Jump("loc_46E2")

    label("loc_4582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4590")
    Jump("loc_46E2")

    label("loc_4590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_459E")
    Jump("loc_46E2")

    label("loc_459E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_45AC")
    Jump("loc_46E2")

    label("loc_45AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_4661")

    ChrTalk(
        0xFE,
        (
            "I'm glad Granny is doing all right. She\x01",
            "even gets to leave the hospital soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as she can leave, I'll get Papa\x01",
            "and Mama and we'll come take her home!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46E2")

    label("loc_4661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_466F")
    Jump("loc_46E2")

    label("loc_466F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_467D")
    Jump("loc_46E2")

    label("loc_467D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_46E2")

    ChrTalk(
        0xFE,
        (
            "Wow... I didn't know the hospital\x01",
            "was THIS big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I sure hope Granny is doing okay.\x02",
    )

    CloseMessageWindow()

    label("loc_46E2")

    TalkEnd(0xFE)
    Return()

    # Function_11_4501 end

    def Function_12_46E6(): pass

    label("Function_12_46E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_476E")

    ChrTalk(
        0xFE,
        (
            "I'm here to visit a friend who was\x01",
            "hospitalized after a big injury.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, where in the world is his room?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_47B8")

    label("loc_476E")


    ChrTalk(
        0xFE,
        (
            "Maybe if I keep on walking, I'll eventually\x01",
            "find my friend's room...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47B8")

    TalkEnd(0xFE)
    Return()

    # Function_12_46E6 end

    def Function_13_47BC(): pass

    label("Function_13_47BC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I came to visit my boyfriend today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You could call him a bit of a delinquent...\x01",
            "I just hope he doesn't cause the other\x01",
            "patients too many problems.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_47BC end

    def Function_14_4860(): pass

    label("Function_14_4860")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 6)), scpexpr(EXPR_END)), "loc_48E6")

    ChrTalk(
        0x10,
        (
            "#3600FNow, all that's left is to carry out\x01",
            "all of the equipment...\x02\x03",
            "Good luck with the rest\x01",
            "of today, everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AD1")

    label("loc_48E6")


    ChrTalk(
        0x101,
        "#0005FMr. Hayworth?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#3600FHello, everyone. It's been a while...\x01",
            "I wasn't expecting to meet you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWell, ever since that last case, we've been\x01",
            "getting a lot more jobs outside of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FAre you working right now, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#3600FIndeed. I came to St. Ursula today to sell\x01",
            "some equipment and non-perishables.\x02\x03",
            "I'm really starting to appreciate my orbal car.\x01",
            "It makes the trips remarkably easier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FI'm happy to see your business is doing well.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 6)

    label("loc_4AD1")

    TalkEnd(0xFE)
    Return()

    # Function_14_4860 end

    def Function_15_4AD5(): pass

    label("Function_15_4AD5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4B34")

    ChrTalk(
        0x11,
        (
            "What was with Dino...and that\x01",
            "crazy strength of his?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Damn it all...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BB8")

    label("loc_4B34")


    ChrTalk(
        0x11,
        (
            "Who does he think he is, playing\x01",
            "games with a Vipers leader?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Dino, when I come back...you're\x01",
            "gonna have hell to pay...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_4BB8")

    TalkEnd(0xFE)
    Return()

    # Function_15_4AD5 end

    def Function_16_4BBC(): pass

    label("Function_16_4BBC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4BFE")

    ChrTalk(
        0x12,
        "I never wanted to see his ugly mug again...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C60")

    label("loc_4BFE")


    ChrTalk(
        0x12,
        (
            "My mom told me to bring my\x01",
            "old man his lunch today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Damn it, where the hell is he?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4C60")

    TalkEnd(0xFE)
    Return()

    # Function_16_4BBC end

    def Function_17_4C64(): pass

    label("Function_17_4C64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EAB")

    ChrTalk(
        0x101,
        "#0005FKate? What are you doing here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FDid the department have a job to do\x01",
            "outside of Crossbell City?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I was just escorting some people here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You see, there's a few members of Heiyue\x01",
            "recovering at St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And since some of the Second Division detectives\x01",
            "wanted to question them, I was put in charge of\x01",
            "driving them here with one of the police cars.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "I don't think the department knows how bad\x01",
            "of a driver I am, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FGot'cha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FWhat matters is that you made it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 7)
    Jump("loc_5006")

    label("loc_4EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FD3")

    ChrTalk(
        0xFE,
        (
            "Thanks. But Heiyue...they're one of the\x01",
            "mafias, right? I didn't know about them\x01",
            "at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Second Division sure are taking\x01",
            "their time with the questioning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Last time I checked, it was already\x01",
            "past noon. I hope those Heiyue guys\x01",
            "aren't giving them a hard time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5006")

    label("loc_4FD3")


    ChrTalk(
        0xFE,
        "What's taking the Second Division so long...?\x02",
    )

    CloseMessageWindow()

    label("loc_5006")

    TalkEnd(0xFE)
    Return()

    # Function_17_4C64 end

    def Function_18_500A(): pass

    label("Function_18_500A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_50AA")

    ChrTalk(
        0xFE,
        (
            "One of our fellow members, Joachim,\x01",
            "is a doctor at the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I'll invite him to go fishing with\x01",
            "me later, if I have the chance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50AA")

    TalkEnd(0xFE)
    Return()

    # Function_18_500A end

    def Function_19_50AE(): pass

    label("Function_19_50AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5238")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51D2")

    ChrTalk(
        0xFE,
        (
            "Around two years ago, our president,\x01",
            "Mr. Fisher, established our branch\x01",
            "here in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And during those two years, we've been\x01",
            "slowly and surely expanding our events\x01",
            "and outreach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm pleased with how we've been\x01",
            "growing, to tell you the truth.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5238")

    label("loc_51D2")


    ChrTalk(
        0xFE,
        (
            "Being able to travel and fish together\x01",
            "with your fellow guild members...\x01",
            "There's nothing better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5238")

    TalkEnd(0xFE)
    Return()

    # Function_19_50AE end

    def Function_20_523C(): pass

    label("Function_20_523C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_52D0")
    Jump("loc_531A")

    label("loc_52D0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52F0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_531A")

    label("loc_52F0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5310")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_531A")

    label("loc_5310")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_531A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5406")

    ChrTalk(
        0xFE,
        (
            "I suppose it's about time to head\x01",
            "back to the examination room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite how tired I am, nothing would\x01",
            "be worse than getting laughed at by\x01",
            "Doctor Lago for leaving it empty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5905")

    label("loc_5406")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_55F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_54DF")

    ChrTalk(
        0xFE,
        (
            "And here I was hoping that you all\x01",
            "would take all of it off my hands...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* You know, throwing away dolls\x01",
            "that are supposed to ward off evil spirits\x01",
            "is harder than you'd think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55EE")

    label("loc_54DF")


    ChrTalk(
        0xFE,
        (
            "Did you find anything worthwhile among\x01",
            "the things on the terrace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A knitted leather string? Are you\x01",
            "positive that's all you need?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You could have taken everything...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(Can you really blame us for not wanting\x01",
            "to take those bulky dolls with us?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_55EE")

    Jump("loc_5905")

    label("loc_55F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_5718")

    ChrTalk(
        0xFE,
        (
            "You can find that container on the terrace\x01",
            "right outside of the men's dormitory on the\x01",
            "second floor of the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you see something that catches your\x01",
            "eye, by all means, take it with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been a pain trying to find someone\x01",
            "who'll take them off our hands.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5905")

    label("loc_5718")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_572C")
    Call(0, 62)
    Jump("loc_5905")

    label("loc_572C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_57C5")

    ChrTalk(
        0xFE,
        (
            "Keeping up with family and work\x01",
            "leaves me with no time for rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I may be a doctor and all, but\x01",
            "life just won't give me a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5905")

    label("loc_57C5")


    ChrTalk(
        0xFE,
        "I've been dead tired, lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "First, when I asked Cirone to order\x01",
            "new equipment, we were delivered\x01",
            "something entirely different...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...and on top of that, my son, Kienz,\x01",
            "still has no intentions of leaving that\x01",
            "foolish 'gang' he's in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I may be a doctor and all, but\x01",
            "life just won't give me a break.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_5905")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_523C end

    def Function_21_590D(): pass

    label("Function_21_590D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B03")
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        "#2900FElie! What a pleasant surprise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FBell? What are you doing at\x01",
            "St. Ursula?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#2900FNothing much. I just accompanied\x01",
            "my father here, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FMr. Crois...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FIs he sick?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0109FHaha, I doubt that's the case.\x02\x03",
            "#0100FHe's doing his usual thing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#2904FThat's right.\x02\x03",
            "#2900FIf you ask the receptionist, I'm sure you'll find\x01",
            "out what it is. Also, I'm sure my father would\x01",
            "appreciate a visit from you all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB4, 6)
    Jump("loc_5D05")

    label("loc_5B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_5BA0")

    ChrTalk(
        0x16,
        (
            "#2906FFather is far too late. What does he\x01",
            "think he's doing, making me wait?\x02\x03",
            "I even reminded him that we have\x01",
            "a meeting in 30 minutes...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D05")

    label("loc_5BA0")


    ChrTalk(
        0x16,
        (
            "#2906FEvery time meetings start to pile\x01",
            "up, he always... *sigh*\x02\x03",
            "#2900FI suppose this is one of his better\x01",
            "virtues, few as they are.\x02\x03",
            "And I'm not against indulging him,\x01",
            "as he's my father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102FYou may complain, but you still accompany\x01",
            "him every year, without fail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#2904FIt just so happens that I'm not busy\x01",
            "whenever he goes, that's all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_5D05")

    TalkEnd(0xFE)
    Return()

    # Function_21_590D end

    def Function_22_5D09(): pass

    label("Function_22_5D09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5EE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E1E")

    ChrTalk(
        0x18,
        (
            "#2400FLytton started working really hard once\x01",
            "he recovered.\x02\x03",
            "Not to mention, my plan of hiding my\x01",
            "own work in his was a massive success.\x01",
            "The boy ended up doing every bit of it.\x02\x03",
            "#2409FHahaha. Lucky me, being blessed\x01",
            "with such an eager pupil.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5EE2")

    label("loc_5E1E")


    ChrTalk(
        0x18,
        (
            "#2400FSince he was so willing, I tricked Lytton\x01",
            "into finishing up some of my work, too.\x02\x03",
            "#2409FNow that I have that out of the way,\x01",
            "maybe I can use this free time to go\x01",
            "fishing or something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EE2")

    TalkEnd(0xFE)
    Return()

    # Function_22_5D09 end

    def Function_23_5EE6(): pass

    label("Function_23_5EE6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F7A")
    Jump("loc_5FC4")

    label("loc_5F7A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F9A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FC4")

    label("loc_5F9A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5FBA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FC4")

    label("loc_5FBA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FC4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60CA")

    ChrTalk(
        0xFE,
        (
            "It's important to take in each country's\x01",
            "individual characteristics while on a trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For example, famous hospitals like this are\x01",
            "perfect sightseeing spots, with all their\x01",
            "research labs and people.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_617A")

    label("loc_60CA")


    ChrTalk(
        0xFE,
        (
            "It's important to take in each country's\x01",
            "individual characteristics while on a trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With so many things to see in Crossbell,\x01",
            "it can get a bit overwhelming at times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_617A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_5EE6 end

    def Function_24_6182(): pass

    label("Function_24_6182")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6266")

    ChrTalk(
        0xFE,
        (
            "I've heard this hospital has equipment\x01",
            "that can perform a health inspection\x01",
            "of sorts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, with the exhaustion I build up\x01",
            "by doing the housework day in, day out,\x01",
            "I'd love to have a checkup.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_6302")

    label("loc_6266")


    ChrTalk(
        0xFE,
        (
            "If the examination determined that I was\x01",
            "in poor health due to overexertion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I could use that as evidence to ask\x01",
            "Master for more vacation days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6302")

    TalkEnd(0xFE)
    Return()

    # Function_24_6182 end

    def Function_25_6306(): pass

    label("Function_25_6306")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x01",
            "Wait for a bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City - South Exit\x01",      # 0
            "Fork (Sandbar)\x01",                   # 1
            "Leave\x01",                            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_639C")
    Call(0, 26)
    ClearMapFlags(0x8000000)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_63BC")

    label("loc_639C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63BC")
    Call(0, 26)
    ClearMapFlags(0x8000000)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()

    label("loc_63BC")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_25_6306 end

    def Function_26_63C4(): pass

    label("Function_26_63C4")

    Fade(1000)
    OP_68(-59000, 1000, 2200, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -56600, 0, 3800, 180)
    SetChrPos(0x1, -56600, 0, 4900, 180)
    SetChrPos(0x2, -56600, 0, 6000, 180)
    SetChrPos(0x3, -56600, 0, 7200, 180)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x7, 0x1C)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1C, -75000, 0, 500, 90)
    OP_D3(0x1C, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)
    OP_0D()

    def lambda_649A():
        OP_95(0xFE, -59000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_649A)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x1C, 1)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x7)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_26_63C4 end

    def Function_27_64DD(): pass

    label("Function_27_64DD")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -56560, 0, 4080, 180)
    SetChrPos(0x1, -56560, 0, 4080, 180)
    SetChrPos(0x2, -56560, 0, 4080, 180)
    SetChrPos(0x3, -56560, 0, 4080, 180)
    OP_68(-56560, 1000, 4080, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_27_64DD end

    def Function_28_6572(): pass

    label("Function_28_6572")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_658C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B43")

    Menu(
        0,
        32,
        26,
        1,
        (
            "Ride in Guardian Force car\x01",      # 0
            "Rest\x01",                            # 1
            "Leave\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AE0")
    Sound(1500, 255, 100, 0)
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6618")
    MenuCmd(1, 1, "★City - Central Square")
    MenuCmd(3, 1, 0x0)
    Jump("loc_6633")

    label("loc_6618")

    MenuCmd(1, 1, "　City - Central Square")

    label("loc_6633")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6661")
    MenuCmd(1, 1, "★City - East Exit")
    MenuCmd(3, 1, 0x1)
    Jump("loc_6677")

    label("loc_6661")

    MenuCmd(1, 1, "　City - East Exit")

    label("loc_6677")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66A5")
    MenuCmd(1, 1, "★City - West Exit")
    MenuCmd(3, 1, 0x2)
    Jump("loc_66BB")

    label("loc_66A5")

    MenuCmd(1, 1, "　City - West Exit")

    label("loc_66BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66EA")
    MenuCmd(1, 1, "★City - South Exit")
    MenuCmd(3, 1, 0x3)
    Jump("loc_6701")

    label("loc_66EA")

    MenuCmd(1, 1, "　City - South Exit")

    label("loc_6701")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6730")
    MenuCmd(1, 1, "★City - North Exit")
    MenuCmd(3, 1, 0x4)
    Jump("loc_6747")

    label("loc_6730")

    MenuCmd(1, 1, "　City - North Exit")

    label("loc_6747")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6771")
    MenuCmd(1, 1, "★Tangram Gate")
    MenuCmd(3, 1, 0x5)
    Jump("loc_6783")

    label("loc_6771")

    MenuCmd(1, 1, "　Tangram Gate")

    label("loc_6783")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67AF")
    MenuCmd(1, 1, "★Bellguard Gate")
    MenuCmd(3, 1, 0x6)
    Jump("loc_67C3")

    label("loc_67AF")

    MenuCmd(1, 1, "　Bellguard Gate")

    label("loc_67C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67FB")
    MenuCmd(1, 1, "★St. Ursula Medical College")
    MenuCmd(3, 1, 0x7)
    Jump("loc_681B")

    label("loc_67FB")

    MenuCmd(1, 1, "　St. Ursula Medical College")

    label("loc_681B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6849")
    MenuCmd(1, 1, "★Armorica Village")
    MenuCmd(3, 1, 0x8)
    Jump("loc_685F")

    label("loc_6849")

    MenuCmd(1, 1, "　Armorica Village")

    label("loc_685F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6891")
    MenuCmd(1, 1, "★Mainz Mining Village")
    MenuCmd(3, 1, 0x9)
    Jump("loc_68AB")

    label("loc_6891")

    MenuCmd(1, 1, "　Mainz Mining Village")

    label("loc_68AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68E5")
    MenuCmd(1, 1, "★Mainz Mountain Path - Tunnel")
    MenuCmd(3, 1, 0xA)
    Jump("loc_6907")

    label("loc_68E5")

    MenuCmd(1, 1, "　Mainz Mountain Path - Tunnel")

    label("loc_6907")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6936")
    MenuCmd(1, 1, "★Stargazer's Tower")
    MenuCmd(3, 1, 0xB)
    Jump("loc_694D")

    label("loc_6936")

    MenuCmd(1, 1, "　Stargazer's Tower")

    label("loc_694D")

    MenuCmd(1, 1, "　Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AD1")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0xF1, 0x10E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0xB)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6A24"),
        (1, "loc_6A32"),
        (2, "loc_6A40"),
        (3, "loc_6A4E"),
        (4, "loc_6A5C"),
        (5, "loc_6A6A"),
        (6, "loc_6A78"),
        (7, "loc_6A86"),
        (8, "loc_6A94"),
        (9, "loc_6AA2"),
        (10, "loc_6AB0"),
        (11, "loc_6ABE"),
        (SWITCH_DEFAULT, "loc_6ACC"),
    )


    label("loc_6A24")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_6ACC")

    label("loc_6A32")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_6ACC")

    label("loc_6A40")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_6ACC")

    label("loc_6A4E")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_6ACC")

    label("loc_6A5C")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_6ACC")

    label("loc_6A6A")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_6ACC")

    label("loc_6A78")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_6ACC")

    label("loc_6A86")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_6ACC")

    label("loc_6A94")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_6ACC")

    label("loc_6AA2")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_6ACC")

    label("loc_6AB0")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_6ACC")

    label("loc_6ABE")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_6ACC")

    label("loc_6ACC")

    Jump("loc_6ADB")

    label("loc_6AD1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6ADB")

    Jump("loc_6B3E")

    label("loc_6AE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B2B")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_6B3E")

    label("loc_6B2B")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6B3E")

    Jump("loc_658C")

    label("loc_6B43")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_28_6572 end

    def Function_29_6B4B(): pass

    label("Function_29_6B4B")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -51320, 0, 17590, 270)
    SetChrPos(0x1, -51320, 0, 17590, 270)
    SetChrPos(0x2, -51320, 0, 17590, 270)
    SetChrPos(0x3, -51320, 0, 17590, 270)
    SetChrPos(0x4, -51320, 0, 17590, 270)
    SetChrPos(0x5, -51320, 0, 17590, 270)
    Sleep(1)
    OP_68(-51320, 1000, 17590, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6C1F")
    Sound(1502, 255, 100, 0)
    Jump("loc_6C25")

    label("loc_6C1F")

    Sound(1503, 255, 100, 0)

    label("loc_6C25")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_29_6B4B end

    def Function_30_6C3A(): pass

    label("Function_30_6C3A")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)
    Return()

    # Function_30_6C3A end

    def Function_31_6C48(): pass

    label("Function_31_6C48")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FIf fishing at a hospital is wrong,\x01",
            "I don't want to be right.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-17220, 0, -31290, 1500)
    MoveCamera(60, 36, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(22000, 1500)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D32")
    OP_E0(0x2)
    MiniGame(0x6, 0xE, 0xFFFFBFBE, 0xFFFFFC18, 0xFFFF9A5C, 0xB4, 0xFFFFBCE4, 0xFFFFF830, 0xFFFF7FFE)

    label("loc_6D32")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_31_6C48 end

    def Function_32_6D37(): pass

    label("Function_32_6D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D6F")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_6ED2")

    label("loc_6D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6DE8")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Wait for the Bus]\x01",      # 0
            "[Don't]\x01",                 # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6DD4"),
        (1, "loc_6DDC"),
        (SWITCH_DEFAULT, "loc_6DE1"),
    )


    label("loc_6DD4")

    Call(0, 47)
    Jump("loc_6DE1")

    label("loc_6DDC")

    Jump("loc_6DE1")

    label("loc_6DE1")

    EventEnd(0x3)
    Jump("loc_6ED2")

    label("loc_6DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6DF9")
    Call(0, 25)
    Jump("loc_6ED2")

    label("loc_6DF9")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_6E75")

    ChrTalk(
        0x101,
        (
            "#0000FBefore heading back, we need to\x01",
            "let Cecile know what's going on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ECF")

    label("loc_6E75")


    ChrTalk(
        0x101,
        (
            "#0000FWe can't go back to Crossbell City yet.\x01",
            "Our investigation isn't close to done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ECF")

    TalkEnd(0xFF)

    label("loc_6ED2")

    Return()

    # Function_32_6D37 end

    def Function_33_6ED3(): pass

    label("Function_33_6ED3")

    Call(0, 37)
    Return()

    # Function_33_6ED3 end

    def Function_34_6ED7(): pass

    label("Function_34_6ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EE9")
    Call(0, 42)
    Jump("loc_6F4D")

    label("loc_6EE9")

    TalkBegin(0xFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The box's lid is coated in a thick dust.\x02\x03",
            "It hasn't been touched for a long time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_6F4D")

    Return()

    # Function_34_6ED7 end

    def Function_35_6F4E(): pass

    label("Function_35_6F4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F60")
    Call(0, 43)
    Jump("loc_6FF6")

    label("loc_6F60")

    TalkBegin(0xFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "At various spots on the handrail, there are signs of paint\x01",
            "chipping.\x02\x03",
            "From the looks of it, the damage must have happened recently.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_6FF6")

    Return()

    # Function_35_6F4E end

    def Function_36_6FF7(): pass

    label("Function_36_6FF7")

    EventBegin(0x0)
    ModifyEventFlags(0, 0, 0x80)
    Fade(1000)
    SetChrPos(0x101, -37200, 0, -1000, 90)
    SetChrPos(0x102, -38600, 0, -1000, 90)
    SetChrPos(0x103, -38600, 0, 400, 90)
    SetChrPos(0x104, -37200, 0, 400, 90)
    OP_68(-27020, -500, 13870, 0)
    MoveCamera(53, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(47750, 0)
    PlaceName2(340, 200, "c_plac15", 0x0, 5000)
    OP_68(-16610, -500, 50, 10000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(-34620, 700, -20, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24700, 0)
    SetChrPos(0x101, -35740, 0, -950, 90)
    SetChrPos(0x102, -37220, 0, 560, 90)
    SetChrPos(0x103, -37220, 0, -950, 90)
    SetChrPos(0x104, -35740, 0, 560, 90)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#1101031V#0300F#5PWhew. I knew St. Ursula was pretty\x01",
            "impressive, but these buildings are\x01",
            "way bigger than I was expectin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101032V#0203F#6PSt. Ursula Medical College...\x02\x03",
            "#1101033V#0200FAs the most distinguished general hospital in\x01",
            "Zemuria, it is famous for its medical research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101034V#6P#0005FIt's that well known?\x02\x03",
            "#1101035V#0000FIt must get lots of visitors, with all the\x01",
            "bus trips scheduled to come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101036V#0104FI've heard that St. Ursula was originally\x01",
            "founded with help from the medically\x01",
            "advanced Principality of Remiferia.\x02\x03",
            "#1101037V#0100FWhat's more, they even accept patients\x01",
            "internationally.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#1101038V#0302F#5PHey, I'm just lookin' forward to seeing\x01",
            "all the nurses' uniforms!\x02\x03",
            "#1101039V#0309FThat's a sight for sore eyes, all right! ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_748D():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_748D)
    Sleep(50)

    def lambda_749D():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_749D)
    Sleep(50)

    def lambda_74AD():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_74AD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1101040V#0012F#12PSomeone's in a good mood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101041V#0103F#6PI've been here several times, but we\x01",
            "always traveled by car...\x02\x03",
            "#1101042V#0100FIt was quite the distance, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101043V#0208F#6P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_75C9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75C9)
    Sleep(50)

    def lambda_75D9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_75D9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_75EE():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_75EE)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1101044V#11P#0005FTio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101045V#0105FDo you need a break?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101046V#0203F#6PNo, I am perfectly fine.\x02\x03",
            "#1101047V#0200FBesides, it was a shorter walk\x01",
            "than it was to Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101048V#11P#0001FAll right. Just don't push yourself\x01",
            "too hard, okay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1101049V#0204F#6PI apologize for worrying you.\x02\x03",
            "#1101050V#0202FMore importantly, did you not intend\x01",
            "to see that lady you told us about,\x01",
            "Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101051V#0305F#5POh, I almost forgot about her!\x02",
    )

    CloseMessageWindow()

    def lambda_77E5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_77E5)
    WaitChrThread(0x104, 1)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#1101052V#0307F#5PLloyd! Let's find her, pronto!\x02",
    )

    CloseMessageWindow()

    def lambda_7840():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7840)

    def lambda_784D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_784D)

    def lambda_785A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_785A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x101,
        (
            "#1101053V#0006F#12PI'm afraid to ask why you're getting so\x01",
            "excited, Randy.\x02\x03",
            "#1101054V#0000FYour soon-to-be failed advances aside,\x01",
            "getting Cecile to show us around would\x01",
            "be the easiest course of action.\x02\x03",
            "#1101055VWe can ask about her at the reception\x01",
            "desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101056V#0309F#5PHell yeah!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#1101057V#0102FThen, shall we head to the hospital lobby?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -37900, 0, -300, 90)
    SetScenarioFlags(0x61, 6)
    OP_29(0x3F, 0x1, 0x8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_36_6FF7 end

    def Function_37_7A0B(): pass

    label("Function_37_7A0B")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00001.itc", 0x1E)
    LoadChrToIndex("chr/ch00301.itc", 0x1F)
    OP_68(-34930, 3900, 16980, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, -36910, 3000, 16290, 90)
    SetChrPos(0x102, -38300, 3000, 16300, 90)
    SetChrPos(0x103, -38300, 3000, 17300, 90)
    SetChrPos(0x104, -37000, 3000, 17300, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#1101320V#0000F#6PAll right, we should probably check\x01",
            "above here, just to be safe.\x02\x03",
            "#1101321VRandy, mind giving me a hand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101322V#0300F#5PHere we go.\x02",
    )

    CloseMessageWindow()
    OP_68(-34930, 4700, 16980, 2500)
    BeginChrThread(0x101, 3, 0, 38)
    Sleep(300)
    BeginChrThread(0x104, 3, 0, 39)
    OP_6F(0x1)
    Sleep(5300)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The tops of the boxes are covered in dust and strange\x01",
            "markings.\x02\x03",
            "Upon further inspection, it's clear that they are paw prints.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#1101323V#0004F#6PBingo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101324V#0300F#6PYeah, those are definitely from a\x01",
            "monster. A canine one, at that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#1101325V#0101F#5PThere's our lead.\x02",
    )

    CloseMessageWindow()

    def lambda_7CEA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7CEA)
    Sleep(50)

    def lambda_7CFA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7CFA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x103,
        "#1101326V#0203FAnd that means...\x02",
    )

    CloseMessageWindow()
    OP_68(-36200, 4000, 20200, 4000)
    MoveCamera(35, 16, 0, 4000)
    SetCameraDistance(34000, 4000)

    def lambda_7D5A():
        OP_95(0xFE, -36480, 3000, 20450, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7D5A)
    Sleep(500)

    def lambda_7D77():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D77)
    Sleep(300)

    def lambda_7D87():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7D87)
    Sleep(100)

    def lambda_7D97():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7D97)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    OP_6F(0x11)

    ChrTalk(
        0x103,
        (
            "#1101327V#0200F#6P...the probability that they used this as\x01",
            "their infiltration route is extremely high.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7E2A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E2A)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#1101328V#0000FYeah, I agree.\x02",
    )

    CloseMessageWindow()
    OP_68(-36930, 3900, 16980, 3000)
    SetCameraDistance(26500, 3000)
    BeginChrThread(0x101, 3, 0, 40)
    BeginChrThread(0x104, 3, 0, 41)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)

    def lambda_7E8C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E8C)

    def lambda_7E99():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E99)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#1101329V#0300F#6PThis spot doesn't look too high up\x01",
            "from the ground.\x02\x03",
            "#1101330VShould we come up with a plan\x01",
            "in case they show up again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101331V#0103F#6PMaybe so...\x02",
    )

    CloseMessageWindow()

    def lambda_7F65():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7F65)
    WaitChrThread(0x102, 1)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#1101332V#0100F#6PBut, is it really okay to end our\x01",
            "investigation here?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7FC6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7FC6)
    WaitChrThread(0x101, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1101333V#0001F#11PThere's still a lot of unanswered questions.\x02\x03",
            "#1101334V#0003FDid they intentionally choose a place like\x01",
            "this to enter from?\x02\x03",
            "#1101335VAnd why didn't they go all out when they\x01",
            "attacked Lytton?\x02\x03",
            "#1101336V#0001FWe have a lot to figure out.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_80DF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_80DF)
    Sleep(100)

    def lambda_80EF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_80EF)
    WaitChrThread(0x103, 1)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1101337V#0205F#5PI suppose only the wolves themselves\x01",
            "would know the answers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101338V#0302F#5PSounds 'bout right.\x02\x03",
            "#1101339VWhat we got should be enough to\x01",
            "round out the CGF's report, though.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_81D0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81D0)
    WaitChrThread(0x101, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1101340V#0004F#12PIt should be.\x02\x03",
            "#1101341V#0000FFor now, let's report back to Cecile\x01",
            "before we return to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101342V#0102F#6PWe still need to thank her, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101343V#0309F#5PBack to the nurses' station, then?\x01",
            "I'm down with that!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(26000, 2000)
    OP_6F(0x79)
    OP_0D()
    SetChrPos(0x0, -37600, 3000, 16800, 270)
    OP_65(0x1, 0x1)
    OP_66(0x2, 0x1)
    SetScenarioFlags(0x63, 1)
    OP_29(0x3F, 0x1, 0x10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7123", 0)
    EventEnd(0x5)
    Return()

    # Function_37_7A0B end

    def Function_38_8332(): pass

    label("Function_38_8332")

    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x101, 0xFFFF7748, 0xE42, 0x40B0, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x101, 0xFFFF7B30, 0x1036, 0x4092, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(55, 0, 100, 0)
    Sleep(300)

    def lambda_839C():
        OP_95(0xFE, -32689, 4150, 16470, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_839C)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(1000)
    OP_64(0x101)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Return()

    # Function_38_8332 end

    def Function_39_83FD(): pass

    label("Function_39_83FD")

    SetChrFlags(0x104, 0x4)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x104, 0xFFFF76BC, 0xE42, 0x4470, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(31, 0, 100, 0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x104, 0xFFFF7AAE, 0x1036, 0x44B6, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(54, 0, 100, 0)
    Sleep(1000)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_8479():
        OP_96(0xFE, 0xFFFF7AAE, 0x1036, 0x42C2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8479)
    WaitChrThread(0x104, 1)
    Sleep(2000)
    OP_64(0x104)

    def lambda_849D():
        OP_96(0xFE, 0xFFFF7AAE, 0x1036, 0x44B6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_849D)
    WaitChrThread(0x104, 1)
    Sleep(1050)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Return()

    # Function_39_83FD end

    def Function_40_84D5(): pass

    label("Function_40_84D5")


    def lambda_84DA():
        OP_95(0xFE, -34000, 4150, 16530, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84DA)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x101, 0xFFFF7748, 0xE42, 0x40B0, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(58, 0, 100, 0)
    Sound(30, 0, 100, 0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x101, 0xFFFF6FD2, 0xBB8, 0x3FA2, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(59, 0, 100, 0)
    Sound(30, 0, 100, 0)
    Sleep(300)
    ClearChrFlags(0x101, 0x4)
    Return()

    # Function_40_84D5 end

    def Function_41_8565(): pass

    label("Function_41_8565")

    OP_93(0x104, 0x10E, 0x1F4)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x104, 0xFFFF76BC, 0xE42, 0x4470, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(60, 0, 100, 0)
    Sound(30, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x104, 0xFFFF6F78, 0xBB8, 0x4394, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(61, 0, 100, 0)
    Sound(30, 0, 100, 0)
    Sleep(500)
    ClearChrFlags(0x104, 0x4)
    Return()

    # Function_41_8565 end

    def Function_42_85DE(): pass

    label("Function_42_85DE")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-37000, 4000, 24200, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -37000, 3000, 24200, 0)
    SetChrPos(0x102, -36800, 3000, 21670, 0)
    SetChrPos(0x103, -37670, 3000, 22640, 0)
    SetChrPos(0x104, -36210, 3000, 22900, 0)
    OP_0D()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The box's lid is coated in a thick dust.\x02\x03",
            "It must have been left alone for a long time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#1101344V#0005F#2P(Wait a second...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101345V#0105F#12PWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101346V#0003F#2PIt's nothing...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1101347V#0008F#2P(If they jumped up from over there, there\x01",
            "should be paw prints or something on top\x01",
            "of the box.)\x02\x03",
            "#1101348V(But considering the dust is undisturbed,\x01",
            "the boxes must have been left alone for\x01",
            "a long time now.)\x02\x03",
            "#1101349V#0000F(Am I missing something here?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -37000, 3000, 23200, 0)
    OP_68(-37000, 4000, 23200, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(26000, 0)
    OP_66(0x3, 0x1)
    SetScenarioFlags(0x63, 2)
    OP_29(0x3F, 0x1, 0x11)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_42_85DE end

    def Function_43_88C1(): pass

    label("Function_43_88C1")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-40800, 4200, 21500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -40800, 3000, 21500, 270)
    SetChrPos(0x102, -38230, 3000, 22130, 270)
    SetChrPos(0x103, -39000, 3000, 20760, 270)
    SetChrPos(0x104, -39000, 3000, 22800, 270)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1101350V#0001F#5P(What's this?)\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "At various spots on the handrail, there are signs of paint\x01",
            "chipping.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(300)

    ChrTalk(
        0x103,
        "#1101351V#0205F#11PLloyd, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101352V#0305F#11PFind somethin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101353V#0012F#5PNo, it's nothing important.\x02\x03",
            "#1101354V#0008F(Then again...this chipping looks\x01",
            "like it was done recently.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -39800, 3000, 21500, 270)
    OP_68(-39800, 4000, 21500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(26000, 0)
    SetScenarioFlags(0x63, 3)
    OP_29(0x3F, 0x1, 0x12)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_43_88C1 end

    def Function_44_8AF6(): pass

    label("Function_44_8AF6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
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
    OP_68(-34700, 4000, 20700, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, -35700, 3000, 20000, 270)
    SetChrPos(0x102, -35700, 3000, 21400, 270)
    SetChrPos(0x103, -34500, 3000, 20000, 270)
    SetChrPos(0x104, -34500, 3000, 21400, 270)
    SetChrPos(0x136, -37300, 3000, 20700, 270)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01300.itp")
    FadeToBright(1000, 0)
    OP_68(-35700, 4000, 20700, 3000)
    OP_0D()
    OP_6F(0x1)
    OP_93(0x136, 0xB4, 0x12C)
    Sleep(1000)
    OP_93(0x136, 0x15E, 0x1F4)
    Sleep(1000)

    ChrTalk(
        0x136,
        (
            "#1101577V#1301F#12PSo the monsters trespassed through\x01",
            "here, is that it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8C83():
        OP_95(0xFE, -37280, 3000, 23830, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_8C83)

    def lambda_8C9D():

        label("loc_8C9D")

        TurnDirection(0x101, 0x136, 500)
        Yield()
        Jump("loc_8C9D")

    QueueWorkItem2(0x101, 1, lambda_8C9D)

    def lambda_8CAF():

        label("loc_8CAF")

        TurnDirection(0x102, 0x136, 500)
        Yield()
        Jump("loc_8CAF")

    QueueWorkItem2(0x102, 1, lambda_8CAF)

    def lambda_8CC1():

        label("loc_8CC1")

        TurnDirection(0x103, 0x136, 500)
        Yield()
        Jump("loc_8CC1")

    QueueWorkItem2(0x103, 1, lambda_8CC1)

    def lambda_8CD3():

        label("loc_8CD3")

        TurnDirection(0x104, 0x136, 500)
        Yield()
        Jump("loc_8CD3")

    QueueWorkItem2(0x104, 1, lambda_8CD3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#1101578V#0001F#12PRight. We still don't know what compelled\x01",
            "them to do it...\x02\x03",
            "#1101579V...but the hospital should take some\x01",
            "precautions for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1101580V#1308F#5PI agree. We'll have to improvise...\x02\x03",
            "#1101581V#1301FIt may be possible to set up some sort of\x01",
            "fence to keep monsters away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101582V#0300F#11PYeah, that should do the trick.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x136, 1)

    ChrTalk(
        0x103,
        (
            "#1101583V#0200F#11PYou would need something sturdy\x01",
            "but also relatively mobile...\x02\x03",
            "#1101584VDo you have anything like that here?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x136, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x136,
        (
            "#1101585V#1304F#5PI believe we have something amongst\x01",
            "our outdoor equipment that would work.\x02\x03",
            "#1101586V#1300FI'll talk to the chief and see if we can\x01",
            "get it installed soon.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_68(-36180, 4000, 30470, 0)
    MoveCamera(36, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30450, 0)
    OP_68(-37360, 4000, 21820, 10000)
    SetMapObjFrame(0xFF, "model6", 0x1, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    LoadChrToIndex("chr/ch28000.itc", 0x1E)
    LoadChrToIndex("chr/ch29600.itc", 0x1F)
    LoadChrToIndex("chr/ch26000.itc", 0x20)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x22, 0x1E)
    SetChrSubChip(0x22, 0x0)
    SetChrPos(0x22, -34230, 3000, 24220, 90)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x0)
    SetChrPos(0x23, -32750, 3000, 24110, 270)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x24, 0x20)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -36060, 3390, 24850, 0)
    SetChrFlags(0x24, 0x8000)
    BeginChrThread(0x24, 0, 0, 46)
    SetChrPos(0x101, -11300, 0, -700, 90)
    SetChrPos(0x102, -11300, 0, 700, 90)
    SetChrPos(0x103, -12700, 0, -700, 90)
    SetChrPos(0x104, -12700, 0, 700, 90)
    SetChrPos(0x136, -9000, 0, 0, 270)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFD, 0xD5, 0xC6, 0x19, 0xC8, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    EndChrThread(0x24, 0x3)
    Fade(2000)
    OP_68(-10300, 2000, 0, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    OP_68(-10300, 1000, 0, 4000)
    OP_6F(0x1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x136,
        (
            "#1101587VGood work.\x02\x03",
            "#1101588VThanks to you all, everyone at the\x01",
            "hospital can work worry-free.\x02",
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
        0x104,
        "#1101589V#0309F#6PNothin' to it! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101590V#0004F#6PWe didn't do anything too special.\x02\x03",
            "#1101591V#0000FAll we did was pinpoint how exactly\x01",
            "the wolves entered the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1101592V#1304F#11PThat's not true! If you didn't come investigate,\x01",
            "we never would have known how to prevent\x01",
            "something like this from happening again.\x02\x03",
            "#1101593V#1300FI think if you work hard, the SSS will be on\x01",
            "Arios' level in no time.\x02\x03",
            "#1101594V#1309FI guarantee it! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101595V#0005F#6PYou think?\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#1101596V#0301F#6PI'm moved!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101597V#0109F#6PThank you for the kind words, Cecile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101598V#0202F#6PWe will do our best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1101599V#1309F#11PHeehee. I'm glad.\x02\x03",
            "#1101600V#1302FLloyd, when we both have some free time,\x01",
            "let's meet up and chat for a while.\x02\x03",
            "#1101601VAlso, I'd like to go visit his grave together,\x01",
            "if you don't mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101602V#0002F#6PYeah, we should do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1101603V#1304F#11POh, one last thing!\x02\x03",
            "#1101604V#1302FWhen I see you next, make sure to tell me\x01",
            "whether you're dating Elie or Tio, okay?\x02\x03",
            "#1101605V#1309FI'll have to congratulate you on getting your\x01",
            "first girlfriend! ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#1101606V#0011F#6PI told you it wasn't like that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1101607V#1306F#11PI guess Randy would be okay, too.\x01",
            "I'm not one to judge...\x02\x03",
            "#1101608V#1301FJust touch base with me, okay?\x01",
            "I'm not completely unfamiliar with\x01",
            "the genre, so I won't be surprised!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101609V#0006F#6PAnd what genre is that, exactly...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101610V#0309F#6PHey, if it'll make Cecile happy,\x01",
            "I don't mind givin' it a try!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 1000)
    Sleep(300)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#1101611V#0011F#4S#11PWell, I'd mind!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x136,
        (
            "#1101612V#1309F#11PI'd love to talk more, but I'll\x01",
            "have to excuse myself here.\x02\x03",
            "#1101613V#1302FTake care on the way back, everyone!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9928():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9928)
    WaitChrThread(0x101, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1101614V#0002F#6PWe will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101615V#0102F#6PThank you for everything.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x136, 3, 0, 45)
    Sleep(3000)
    OP_68(-12000, 1000, 0, 4000)
    WaitChrThread(0x136, 3)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        "#1101616V#0309F#6POh, I think I'm in love...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101617V#0104F#6PWarm, reliable, open-minded...\x02\x03",
            "#1101618V#0102FShe seems like an amazing person, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101619V#0009F#6PHaha. I'm glad you think so, too.\x02\x03",
            "#1101620V#0002FWe may not be real siblings, but\x01",
            "she's family, in my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101621V#0204F#6PThat reminds me, Lloyd.\x02\x03",
            "#1101622V#0202FWhat exactly IS your\x01",
            "relationship with her?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 600)

    ChrTalk(
        0x101,
        "#1101623V#0011F#11PHuh?\x02",
    )

    CloseMessageWindow()

    def lambda_9B7C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B7C)
    Sleep(50)

    def lambda_9B8C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9B8C)
    WaitChrThread(0x102, 1)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#1101624V#0104F#5PI'm a little curious, too.\x02\x03",
            "#1101625V#0102FI was definitely getting more than the\x01",
            "standard 'siblings' vibe from you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101626V#0001F#11PWhat are you implying...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101627V#0310F#5PLloyd, you traitor!\x02\x03",
            "#1101628VYou've been slammin' a babe like\x01",
            "her this entire time?!\x02\x03",
            "#1101629V#0307FArgh! What I wouldn't give to\x01",
            "switch bodies with you right now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101630V#0006F#11PYou know that isn't possible.\x02\x03",
            "#1101631V#0001FActually, I think it's about time we dropped\x01",
            "this nonsensical conversation and headed\x01",
            "back to Crossbell City.\x02\x03",
            "#1101632VIt's already evening, and we still have to put\x01",
            "together a report of today's investigation\x01",
            "before we go to sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101633V#0211F#6P(He dodged the question.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101634V#0111F#5P(Yes, quite blatantly at that.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101635V#0310F#5P(Curse you, Lloyd! She's totally my type, too!)\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_9F18():
        OP_93(0xFE, 0x13B, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F18)
    WaitChrThread(0x101, 1)
    Sleep(300)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        (
            "#1101636V#0003F#4S#11PI don't know what you're whispering\x01",
            "about, but I'm sure it's nothing good!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    RemoveParty(0x35, 0x0)
    SetChrPos(0x0, -11510, 0, -140, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -26990, 0, 1930, 270)
    SetScenarioFlags(0x63, 7)
    OP_29(0x3F, 0x1, 0x14)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_44_8AF6 end

    def Function_45_A024(): pass

    label("Function_45_A024")

    OP_93(0xFE, 0x5A, 0x12C)

    def lambda_A030():
        OP_95(0xFE, 1500, 1000, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A030)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    def lambda_A069():
        OP_95(0xFE, 4500, 1000, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A069)
    Sleep(500)

    def lambda_A086():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A086)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    Return()

    # Function_45_A024 end

    def Function_46_A0B6(): pass

    label("Function_46_A0B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A122")
    OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(1000)
    OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(1000)
    OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(1000)
    OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(1000)
    Jump("Function_46_A0B6")

    label("loc_A122")

    Return()

    # Function_46_A0B6 end

    def Function_47_A123(): pass

    label("Function_47_A123")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch20400.itc", 0x1E)
    LoadChrToIndex("chr/ch20300.itc", 0x1F)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x0)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x0)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xD, 0x40)
    EventBegin(0x0)
    OP_68(-59370, 1400, 2570, 0)
    MoveCamera(49, 15, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -58140, 0, 2890, 0)
    SetChrPos(0x102, -57140, 0, 1620, 0)
    SetChrPos(0x103, -59300, 0, 1290, 0)
    SetChrPos(0x104, -58230, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#1101637V#0000F#6PSo, should we wait for the bus?\x02\x03",
            "#1101638VAccording to the schedule, one's supposed\x01",
            "to come in 15 minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101639V#0305F#4PDang, that's convenient.\x02\x03",
            "#1101640VAnd it runs all the way up to 11PM?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101641V#0203F#6PThe fare is really cheap, too.\x02\x03",
            "#1101642V#0200FThe city manages it, correct? Does\x01",
            "that mean they do not make a profit\x01",
            "from it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#1101643V#0102FYou have to remember that the hospital\x01",
            "is important to everyone in Crossbell State.\x02\x03",
            "#1101644VGiven the high demand and room in the\x01",
            "state's budget, they must have enough\x01",
            "mira to fund the service.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        "#1101645V#0202F#6PThat makes sense.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#1101646V#0000F#5PBeing able to visit the hospital as easily\x01",
            "as you can is definitely something to be\x01",
            "thankful for.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-59000, 1000, 2200, 0)
    MoveCamera(66, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrPos(0x101, -56600, 0, 3800, 180)
    SetChrPos(0x102, -56600, 0, 4900, 180)
    SetChrPos(0x103, -56600, 0, 6000, 180)
    SetChrPos(0x104, -56600, 0, 7100, 180)
    SetChrPos(0x25, -56600, 0, 8200, 180)
    SetChrPos(0x26, -56600, 0, 9300, 180)
    SetChrPos(0xD, -56600, 0, 10400, 180)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x7, 0x1C)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1C, -75000, 0, 500, 90)
    OP_D3(0x1C, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_A605():
        OP_95(0xFE, -59000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A605)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x1C, 1)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x7)
    Sleep(300)
    OP_71(0x7, 0x1, 0x1E, 0x1, 0x0)
    OP_79(0x7)
    Sound(464, 0, 100, 0)
    Sleep(1000)

    def lambda_A659():
        OP_9B(0x0, 0xFE, 0x0, 0xED8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A659)
    Sleep(100)

    def lambda_A671():
        OP_9B(0x0, 0xFE, 0x0, 0x1324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A671)
    Sleep(80)

    def lambda_A689():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A689)
    Sleep(0)

    def lambda_A6A1():
        OP_9B(0x0, 0xFE, 0x0, 0x1BBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A6A1)
    Sleep(200)

    def lambda_A6B9():
        OP_9B(0x0, 0xFE, 0x0, 0x2008, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_A6B9)
    Sleep(100)

    def lambda_A6D1():
        OP_9B(0x0, 0xFE, 0x0, 0x2454, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_A6D1)
    Sleep(150)

    def lambda_A6E9():
        OP_9B(0x0, 0xFE, 0x0, 0x28A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A6E9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x25, 1)
    WaitChrThread(0x26, 1)
    Sound(463, 0, 100, 0)
    WaitChrThread(0xD, 1)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-58690, 1000, 2150, 0)
    MoveCamera(75, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23360, 0)
    SetChrPos(0x1C, -59000, 0, 500, 270)
    OP_D3(0x1C, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_70(0x7, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x7, 0x3C, 0x5A, 0x0, 0x0)
    Sound(467, 0, 100, 0)
    Sound(465, 0, 100, 0)
    OP_79(0x7)
    OP_68(-62690, 1000, 2150, 4000)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)

    def lambda_A810():
        OP_95(0xFE, -75000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A810)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM("ed7000", "ed7000")
    OP_6F(0x1)
    EndChrThread(0x1C, 0x1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetScenarioFlags(0x5C, 0)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_47_A123 end

    def Function_48_A882(): pass

    label("Function_48_A882")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch21100.itc", 0x1E)
    LoadChrToIndex("chr/ch21600.itc", 0x1F)
    LoadChrToIndex("chr/ch21800.itc", 0x20)
    LoadChrToIndex("chr/ch21900.itc", 0x21)
    OP_68(-51620, 2800, 4480, 0)
    MoveCamera(86, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23730, 0)
    SetChrPos(0x101, -50500, 0, -800, 270)
    SetChrPos(0xEF, -51500, 0, -800, 270)
    SetChrPos(0x153, -52500, 0, -800, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x0)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x0)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x7)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrChipByIndex(0x28, 0x20)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    SetChrChipByIndex(0x29, 0x21)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)
    SetChrPos(0x27, -56040, 0, 5750, 180)
    SetChrPos(0x28, -56040, 0, 6950, 180)
    SetChrPos(0x29, -56040, 0, 8150, 180)
    OP_4B(0x1D, 0xFF)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x1D, 0x80)
    OP_78(0x7, 0x1D)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1D, -75000, 0, 500, 90)
    OP_D3(0x1D, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)

    def lambda_AA2B():
        OP_95(0xFE, -56000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_AA2B)
    Sound(466, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_68(-51620, 200, 4480, 6000)
    OP_6F(0x1)
    OP_0D()
    WaitChrThread(0x1D, 1)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x7)
    OP_71(0x7, 0x1, 0x1E, 0x1, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x7)
    BeginChrThread(0x25, 3, 0, 49)
    Sleep(750)
    BeginChrThread(0x26, 3, 0, 49)
    Sleep(750)
    BeginChrThread(0x101, 3, 0, 50)
    Sleep(750)
    BeginChrThread(0x153, 3, 0, 52)
    Sleep(750)
    BeginChrThread(0xEF, 3, 0, 51)
    Sleep(750)
    Sleep(1500)
    BeginChrThread(0x27, 3, 0, 53)
    Sleep(350)
    BeginChrThread(0x28, 3, 0, 53)
    Sleep(350)
    BeginChrThread(0x29, 3, 0, 53)
    Sleep(350)
    Sleep(1500)
    EndChrThread(0x27, 0x3)
    EndChrThread(0x28, 0x3)
    EndChrThread(0x29, 0x3)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x80)
    SetChrBattleFlags(0x29, 0x8000)
    Fade(1000)
    OP_68(-46640, 200, 360, 0)
    MoveCamera(40, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21360, 0)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x153, 3)
    WaitChrThread(0xEF, 3)
    OP_0D()

    ChrTalk(
        0x153,
        (
            "#3600689V#1109F#6PThat was amazing! Hehehe!\x02\x03",
            "#3600690V#1110FWalking might be kinda fun, but\x01",
            "buses are SUPER-DUPER fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600691V#0014F#11PYou think so?\x02\x03",
            "#3600692V#0008F(From what she's saying, this must have\x01",
            "been her first time riding in a vehicle...)\x02\x03",
            "#3600693V#0001F(Does that mean she's never been in an\x01",
            "airship or train before?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600694V#1105F#6PWhat'd you say this place was?\x01",
            "A hos-pi-tal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600695V#0004F#11PYep, but it's also a medical college.\x01",
            "There's even a research lab here, too.\x02\x03",
            "#3600696V#0000FIt's possible that they'll be able to help\x01",
            "you with recovering your memory, KeA.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_AE5B")

    ChrTalk(
        0x153,
        (
            "#3600697V#1106F#6PHmm... Is it really that big a deal if I\x01",
            "remember things or not?\x02\x03",
            "#3600698V#1100FLloyd, Elie. Would it make you happy\x01",
            "if I remembered everything?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFC4")

    label("loc_AE5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_AF11")

    ChrTalk(
        0x153,
        (
            "#3600697V#1106F#6PHmm... Is it really that big a deal if I\x01",
            "remember things or not?\x02\x03",
            "#3600699V#1100FLloyd, Tio. Would it make you happy\x01",
            "if I remembered everything?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFC4")

    label("loc_AF11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_AFC4")

    ChrTalk(
        0x153,
        (
            "#3600697V#1106F#6PHmm... Is it really that big a deal if I\x01",
            "remember things or not?\x02\x03",
            "#3600700V#1100FLloyd, Randy. Would it make you happy\x01",
            "if I remembered everything?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFC4")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3600701V#0002F#11POf course.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_B0BE")

    ChrTalk(
        0x102,
        (
            "#3600702V#0104F#5PI'm sure you're missing a lot of\x01",
            "really precious memories, KeA.\x02\x03",
            "#3600703V#0102FTry to do your best to remember\x01",
            "them, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1F5")

    label("loc_B0BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_B163")

    ChrTalk(
        0x103,
        (
            "#3600704V#0203F#5PYou probably have quite a lot of precious\x01",
            "memories stored in your brain.\x02\x03",
            "#3600705V#0202FPlease try to recover them, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1F5")

    label("loc_B163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_B1F5")

    ChrTalk(
        0x104,
        (
            "#3600706V#0306F#5PI'm sure you got a lot of great\x01",
            "memories stored in your noggin.\x02\x03",
            "#3600707V#0300FDon't wanna just lose 'em, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1F5")


    ChrTalk(
        0x153,
        (
            "#3600708V#1104F#6PHmm, okay.\x02\x03",
            "#3600709V#1110FI'll do my bestest to remember\x01",
            "everything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600710V#0004F#11PThat's the spirit.\x02\x03",
            "#3600711V#0000FHowever, don't overwork yourself\x01",
            "trying to remember, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600712V#1109F#6PGot it!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_B34D")

    ChrTalk(
        0x102,
        (
            "#3600713V#0102F#5PWe should ask about the Neurology Department\x01",
            "in the lobby, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B423")

    label("loc_B34D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_B3B1")

    ChrTalk(
        0x103,
        (
            "#3600714V#0202F#5PShould we ask the receptionist about the\x01",
            "Neurology Department?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B423")

    label("loc_B3B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_B423")

    ChrTalk(
        0x104,
        (
            "#3600715V#0302F#5PAll righty. Let's hit up the receptionist and\x01",
            "ask about the Neurology Department.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B423")

    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(471, 0, 100, 0)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetChrPos(0x0, -48100, 0, -400, 90)
    ModifyEventFlags(1, 1, 0x80)
    SetScenarioFlags(0xA8, 4)
    OP_29(0x48, 0x1, 0x6)
    Sleep(500)
    EventEnd(0x5)
    OP_70(0x7, 0x0)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)
    OP_4C(0x1D, 0xFF)
    Return()

    # Function_48_A882 end

    def Function_49_B48D(): pass

    label("Function_49_B48D")

    SetChrPos(0xFE, -55990, 600, 1320, 270)

    def lambda_B4A3():
        OP_95(0xFE, -56010, 0, 4180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4A3)

    def lambda_B4BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B4BD)
    WaitChrThread(0xFE, 1)

    def lambda_B4D2():
        OP_95(0xFE, -50520, 0, 3410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4D2)
    WaitChrThread(0xFE, 1)

    def lambda_B4F0():
        OP_95(0xFE, -46150, 0, 30, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4F0)
    WaitChrThread(0xFE, 1)

    def lambda_B50E():
        OP_95(0xFE, -33950, 0, -50, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B50E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_49_B48D end

    def Function_50_B52C(): pass

    label("Function_50_B52C")

    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -55990, 600, 1320, 270)

    def lambda_B547():
        OP_95(0xFE, -56010, 0, 4180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B547)

    def lambda_B561():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B561)
    WaitChrThread(0xFE, 1)

    def lambda_B576():
        OP_95(0xFE, -50520, 0, 3410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B576)
    WaitChrThread(0xFE, 1)

    def lambda_B594():
        OP_95(0xFE, -47080, 0, -1280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B594)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x10E, 0x1F4)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_50_B52C end

    def Function_51_B5BE(): pass

    label("Function_51_B5BE")

    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -55990, 600, 1320, 270)

    def lambda_B5D9():
        OP_95(0xFE, -56010, 0, 4180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B5D9)

    def lambda_B5F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B5F3)
    WaitChrThread(0xFE, 1)

    def lambda_B608():
        OP_95(0xFE, -50520, 0, 3410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B608)
    WaitChrThread(0xFE, 1)

    def lambda_B626():
        OP_95(0xFE, -47530, 0, 180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B626)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xE1, 0x1F4)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_51_B5BE end

    def Function_52_B650(): pass

    label("Function_52_B650")

    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -55990, 600, 1320, 270)

    def lambda_B66B():
        OP_95(0xFE, -56010, 0, 4180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B66B)

    def lambda_B685():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B685)
    WaitChrThread(0xFE, 1)

    def lambda_B69A():
        OP_95(0xFE, -50520, 0, 3410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B69A)
    WaitChrThread(0xFE, 1)

    def lambda_B6B8():
        OP_95(0xFE, -48510, 0, -1230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6B8)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x1F4)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_52_B650 end

    def Function_53_B6E2(): pass

    label("Function_53_B6E2")


    def lambda_B6E7():
        OP_95(0xFE, -56060, 0, 3950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6E7)
    WaitChrThread(0xFE, 1)

    def lambda_B705():
        OP_95(0xFE, -55990, 600, 1320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B705)
    Sleep(1200)

    def lambda_B722():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B722)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_53_B6E2 end

    def Function_54_B737(): pass

    label("Function_54_B737")

    Sleep(7000)
    ClearMapObjFlags(0x6, 0x10)
    OP_71(0x6, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x6)
    Return()

    # Function_54_B737 end

    def Function_55_B750(): pass

    label("Function_55_B750")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    OP_68(-22700, 1000, -500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, -26700, 0, -1100, 90)
    SetChrPos(0x153, -28000, 0, -500, 90)
    SetChrPos(0xEF, -26700, 0, 100, 90)
    SetChrPos(0x1E, -9000, 0, -500, 270)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    OP_4B(0x1E, 0xFF)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01300.itp")
    ModifyEventFlags(0, 1, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    FadeToBright(1000, 0)

    def lambda_B84C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B84C)
    Sleep(100)

    def lambda_B864():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_B864)
    Sleep(150)

    def lambda_B87C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_B87C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)
    OP_0D()

    NpcTalk(
        0x1E,
        "Woman's Voice",
        "#3600716VLloyd...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3600717V#0002F#6P...!\x02",
    )

    CloseMessageWindow()
    OP_68(-14700, 1000, -500, 3000)
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(-21000, 1000, -500, 0)
    SetCameraDistance(23000, 0)
    OP_98(0x1E, 0xFFFFE890, 0x0, 0x0, 0x0, 0x0)

    def lambda_B962():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_B962)

    def lambda_B977():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B977)
    Sleep(100)

    def lambda_B98F():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_B98F)
    Sleep(150)

    def lambda_B9A7():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_B9A7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x1E, 1)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        "#3600718V#0000F#6PCecile!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_BA3A")

    ChrTalk(
        0x102,
        (
            "#3600719V#0102F#6PNice to see you, Cecile.\x01",
            "It's been a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BACD")

    label("loc_BA3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_BA76")

    ChrTalk(
        0x103,
        "#3600720V#0202F#6PNice to see you again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BACD")

    label("loc_BA76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_BACD")

    ChrTalk(
        0x104,
        (
            "#3600721V#0309F#6POh, Cecile! You have no idea\x01",
            "how much I've missed you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BACD")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 36, 3)
    Sleep(500)

    AnonymousTalk(
        0x1E,
        (
            "#3600722VIt looks like you two are doing well.\x02\x03",
            "#3600723VI'm sure you worked hard during the\x01",
            "festival. Has the department been\x01",
            "keeping you busy?\x02",
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
        (
            "#3600724V#0012F#6PYou could say that.\x02\x03",
            "#3600725V#0006FHonestly, those five days were\x01",
            "the busiest days of my life.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_BCA3")

    ChrTalk(
        0x102,
        (
            "#3600726V#0106F#6PAnd the week afterwards wasn't\x01",
            "anything to scoff about, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD5A")

    label("loc_BCA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_BD00")

    ChrTalk(
        0x103,
        (
            "#3600727V#0206F#6PAnd the following week was just\x01",
            "as busy, if not more...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD5A")

    label("loc_BD00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_BD5A")

    ChrTalk(
        0x104,
        (
            "#3600728V#0306F#6PAnd the week after 'em wasn't\x01",
            "a walk in the park, either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD5A")


    ChrTalk(
        0x1E,
        (
            "#3600729V#1302F#11PDespite all that, it looks like you\x01",
            "managed to survive.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1E,
        "#3600730V#1305F#11PHold on. That girl...\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    def lambda_BE07():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_BE07)
    WaitChrThread(0x153, 1)

    ChrTalk(
        0x153,
        (
            "#3600731V#1110F#6PHey, Lloyd!\x02\x03",
            "#3600732VDo you know this lady, too?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BE69():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE69)
    Sleep(50)

    def lambda_BE79():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_BE79)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3600733V#0000F#11PThat's right.\x02\x03",
            "#3600734VHer name's Cecile. She's basically\x01",
            "my big sister, and she--\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1E)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "#3600735V#1303F#11P#40WN-No way...\x02\x03",
            "#3600736V#1308F#40WI-I can't believe you'd do something\x01",
            "like this and keep it a secret from me...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BF86():
        TurnDirection(0xFE, 0x1E, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF86)

    def lambda_BF93():
        TurnDirection(0xFE, 0x1E, 300)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_BF93)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    ChrTalk(
        0x101,
        "#3600737V#0005F#6PWhat?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x1E,
        (
            "#3600738V#1306F#11PYou went and got married without telling me!\x01",
            "#4SHow could you not invite me?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        "#3600739V#0011F#4S#6PHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#3600740V#1303F#11PI can't believe it. You DID!\x02\x03",
            "#3600741V#1301FHey, you. What's your name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600742V#1110F#6PKeA!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_C212")

    ChrTalk(
        0x1E,
        (
            "#3600743V#1309F#11PKeA...? Heehee. What a cute name.\x02\x03",
            "#3600744V#1308FYou don't look like Lloyd, though...\x01",
            "Maybe you take after your mom?\x02\x03",
            "#3600745VWait, you don't look like Elie, either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3600746V#0112F#6PC-Cecile...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C40B")

    label("loc_C212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_C31C")

    ChrTalk(
        0x1E,
        (
            "#3600743V#1309F#11PKeA...? Heehee. What a cute name.\x02\x03",
            "#3600744V#1308FYou don't look like Lloyd, though...\x01",
            "Maybe you take after your mom?\x02\x03",
            "#3600747VWait, you don't look like Tio, either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3600748V#0211F#6PCecile, what are you getting at...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C40B")

    label("loc_C31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_C40B")

    ChrTalk(
        0x1E,
        (
            "#3600743V#1309F#11PKeA...? Heehee. What a cute name.\x02\x03",
            "#3600744V#1308FYou don't look like Lloyd, though...\x01",
            "Maybe you take after your mom?\x02\x03",
            "#3600749V#1301FOr maybe you're Randy's daughter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3600750V#0305F#6PWhoa, Cecile?!\x02",
    )

    CloseMessageWindow()

    label("loc_C40B")


    ChrTalk(
        0x101,
        (
            "#3600751V#0012F#6PPlease, calm down and think\x01",
            "about this rationally!\x02\x03",
            "#3600752V#0011FMe? KeA's dad? You know I'm not old\x01",
            "enough for that to be the case, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1100)
    OP_63(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1E)

    ChrTalk(
        0x1E,
        (
            "#3600753V#1305F#11POh, now that I think about it...\x02\x03",
            "#3600754V#1309FI guess that makes sense.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#3600755V#0012F#6PDoes it really require that\x01",
            "much thought...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_C616")

    ChrTalk(
        0x102,
        (
            "#3600756V#0106F#6PYou can be quite the airhead\x01",
            "at times, can't you, Cecile?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C6C9")

    label("loc_C616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_C676")

    ChrTalk(
        0x103,
        (
            "#3600757V#0206F#6PCecile, have people ever called\x01",
            "you a scatterbrain before?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C6C9")

    label("loc_C676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_C6C9")

    ChrTalk(
        0x104,
        (
            "#3600758V#0309F#6PCecile, your scatterbrain is as\x01",
            "endearing as ever!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C6C9")


    ChrTalk(
        0x153,
        "#3600759V#1105F#6PI don't get it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(24000, 2000)
    OP_6F(0x10)
    OP_0D()
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetScenarioFlags(0x5C, 1)
    NewScene("t1510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_55_B750 end

    def Function_56_C731(): pass

    label("Function_56_C731")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    StopEffect(0x8, 0x0)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch05400.itc", 0x1F)
    OP_68(1400, 1700, 530, 0)
    MoveCamera(46, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(31300, 0)
    SetChrPos(0x101, 100000, 0, 0, 0)
    SetChrPos(0xEF, 100000, 0, 0, 0)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, 4000, 1000, 0, 270)
    OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -23770, -1000, -26000, 180)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(29800, 2500)
    OP_6F(0x10)
    OP_0D()
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    def lambda_C836():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_C836)

    def lambda_C84B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_C84B)
    WaitChrThread(0x20, 1)
    WaitChrThread(0x20, 2)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)

    ChrTalk(
        0x20,
        (
            "#3600987V#1101F#11PDumb Lloyd. You don't get it at\x01",
            "all, do you?\x02\x03",
            "#3600988V#1108FI'd be perfectly fine without my\x01",
            "memories...\x02\x03",
            "#3600989V#1106FSo why is everyone so worried\x01",
            "about them?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(-1400, 1700, 530, 5000)

    def lambda_C94F():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_C94F)
    Sleep(3000)
    Fade(1000)
    OP_68(-24820, 1700, -1120, 0)
    MoveCamera(46, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(29800, 0)
    SetCameraDistance(25490, 3500)
    EndChrThread(0x20, 0x1)
    SetChrPos(0x20, -17660, 0, -310, 270)

    def lambda_C9B8():
        OP_9B(0x0, 0xFE, 0x0, 0x189C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_C9B8)
    WaitChrThread(0x20, 1)
    OP_63(0x20, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    OP_93(0x20, 0xB4, 0x12C)
    Sleep(750)
    OP_93(0x20, 0x10E, 0x1F4)
    OP_93(0x20, 0x0, 0x1F4)
    Sleep(750)
    OP_93(0x20, 0x10E, 0x12C)
    Sleep(750)

    ChrTalk(
        0x20,
        (
            "#3600990V#1105F#11PUhhhhhh...\x02\x03",
            "#3600991VWhere am I?\x02\x03",
            "#3600992V...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x20)
    OP_93(0x20, 0xB4, 0x12C)
    Sleep(500)

    ChrTalk(
        0x20,
        (
            "#3600993V#1114F#5PHmmm...\x02\x03",
            "#3600994V#1101FYup, I think I'm lost.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x20,
        "#3600995V#1105F#5P...\x02",
    )

    CloseMessageWindow()
    OP_68(-24820, 1700, -4120, 3000)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)
    OP_68(-24150, 0, -34360, 0)
    MoveCamera(46, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22830, 0)
    FadeToBright(1000, 0)
    OP_68(-24020, 0, -26990, 6000)
    SetCameraDistance(20600, 6000)
    OP_6F(0x1)
    Sleep(300)

    ChrTalk(
        0x1F,
        (
            "#3600996V#1502F#5PThe breeze is so nice...\x02\x03",
            "#3600997VI wonder when Father will be\x01",
            "coming today...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x20, -24000, 0, -14410, 180)
    Sleep(300)
    Sound(2035, 255, 100, 0)
    Sleep(150)

    ChrTalk(
        0x20,
        "#3600998VHey, you!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x1F, 0x0, 0x190)
    OP_68(-23780, 0, -25230, 2500)

    def lambda_CC46():
        OP_95(0xFE, -23770, -1000, -24500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_CC46)
    WaitChrThread(0x20, 1)

    ChrTalk(
        0x1F,
        "#3600999V#1505F#12PUm, you're...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#3601000V#1110F#5PAre you looking at something?\x02\x03",
            "#3601001V#1109FIs it all the fishies?! I wanna\x01",
            "look at them, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#3601002V#1500F#12PHeehee...\x02\x03",
            "#3601003VI can't see them, but I'm sure\x01",
            "they're swimming in the water,\x01",
            "all the same.\x02\x03",
            "#3601004VWhenever they jump from time\x01",
            "to time, I can hear the splashes...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    MoveCamera(46, 14, 0, 1500)
    OP_68(-24970, 0, -26730, 1500)

    def lambda_CDFD():
        OP_95(0xFE, -24860, -1000, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_CDFD)

    def lambda_CE17():

        label("loc_CE17")

        TurnDirection(0xFE, 0x20, 400)
        Yield()
        Jump("loc_CE17")

    QueueWorkItem2(0x1F, 1, lambda_CE17)
    WaitChrThread(0x20, 1)
    EndChrThread(0x1F, 0x1)
    OP_93(0x20, 0xB4, 0x1F4)
    Sleep(500)
    OP_63(0x20, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x20,
        (
            "#3601005V#1105F#5PWow, you're right! There's so many\x01",
            "of them right here!\x02\x03",
            "#3601006V#1109FI wish I had a fishing rod! I'd catch\x01",
            "'em all, or my name isn't KeA!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x10E, 0x190)

    ChrTalk(
        0x1F,
        (
            "#3601007V#1500F#11PSo, your name is KeA.\x02\x03",
            "#3601008VMy name is Shizuku MacLaine.\x01",
            "It's nice to meet you.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x20,
        (
            "#3601009V#1111F#5PShizuku...?\x02\x03",
            "#3601010V#1109FI like it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#3601011V#1500F#11PThank you.\x02\x03",
            "#3601012VI think you have a pretty name, too.\x02\x03",
            "#3601013VAre you here to visit someone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#3601014V#1105F#5PNope.\x02\x03",
            "#3601015V#1108FI came here to see if someone could\x01",
            "bring back my memories, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "#3601016V#1505F#11PMemories? What do you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#3601017V#1101F#5PWhen that weird doctor with glasses\x01",
            "said I had to leave Lloyd and everyone\x01",
            "else, I ran away.\x02\x03",
            "#3601018V#1104FA 'strategic retreat,' or whatever you\x01",
            "call it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1F,
        (
            "#3601019V#1508F#11PYou ran away?\x02\x03",
            "#3601020V#1505F(When she said Lloyd and everyone,\x01",
            "was she talking about...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#3601021V#1110F#5PShizuku! I have a question!\x02\x03",
            "#3601022VWhy do you keep your eyes closed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#3601023V#1500F#11POh, right...\x02\x03",
            "#3601024VI'm blind. That's why I stay here\x01",
            "at the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#3601025V#1105F#5PReally?\x02\x03",
            "#3601026V#1100FWell, I don't know who I am, so\x01",
            "I guess we're kinda the same.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1F,
        (
            "#3601027V#1505F#11POh, your memories...\x02\x03",
            "#3601028V#1508FYou mentioned that earlier.\x02\x03",
            "#3601029VYou don't remember anything?\x01",
            "Not even your mother or father?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#3601030V#1100F#5PNope. Nothing at all.\x02\x03",
            "#3601031V#1109FBut because I have Lloyd and the\x01",
            "others, I don't have to feel lonely!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#3601032V#1500F#11PIs that so?\x02\x03",
            "#3601033V#1508FMy mother isn't with us anymore,\x01",
            "but I still have my father...\x02\x03",
            "#3601034V#1510F...and everyone at the hospital is\x01",
            "really kind, so I guess I'm not very\x01",
            "lonely, either.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19600, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetScenarioFlags(0xA9, 0)
    SetScenarioFlags(0xA9, 7)
    StopBGM(0x1388)
    WaitBGM()
    EventEnd(0x5)
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_56_C731 end

    def Function_57_D586(): pass

    label("Function_57_D586")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch05400.itc", 0x1F)
    LoadChrToIndex("chr/ch02400.itc", 0x20)
    LoadChrToIndex("apl/ch50384.itc", 0x21)
    OP_68(-23910, 800, -12480, 0)
    MoveCamera(41, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23640, 0)
    SetChrPos(0x101, -23500, 0, -15070, 180)
    SetChrPos(0xEF, -24520, 0, -14530, 180)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -24570, -1000, -26000, 90)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -23240, -1000, -26000, 270)
    SetChrChipByIndex(0x21, 0x20)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x21, -23910, 0, -2470, 180)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ModifyEventFlags(0, 2, 0x80)
    StopBGM(0xFA0)
    FadeToBright(1000, 0)
    OP_68(-23910, 800, -15480, 2500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#3601035V#0000F#5PThere you are!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_D6F3")

    ChrTalk(
        0x102,
        "#3601036V#0102F#5PThank goodness!\x02",
    )

    CloseMessageWindow()
    Jump("loc_D75E")

    label("loc_D6F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_D723")

    ChrTalk(
        0x103,
        "#3601037V#0202F#5PFinally...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D75E")

    label("loc_D723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_D75E")

    ChrTalk(
        0x104,
        "#3601038V#0300F#5PSo this is where you went.\x02",
    )

    CloseMessageWindow()

    label("loc_D75E")

    OP_5A()
    Fade(1000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-24970, 0, -26730, 0)
    MoveCamera(46, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20600, 0)
    SetCameraDistance(20000, 20000)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)

    ChrTalk(
        0x20,
        (
            "#3601039V#1110F#5POh! And, and...!\x02\x03",
            "#3601040VOur dog, Zeit, is sooo big!\x02\x03",
            "#3601041VHe acts like he's better than everyone\x01",
            "else, but he's the softest thing I've ever\x01",
            "touched, you know?\x02\x03",
            "#3601042V#1109FAnd he loooves it when you scratch his\x01",
            "back really hard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#3601043V#1500F#11PHe does?\x02\x03",
            "#3601044V#1502FZeit sounds like quite the fluffy dog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#3601045V#1110F#5PYou probably come to the city every\x01",
            "now and then, right?\x02\x03",
            "#3601046VNext time you do, do you wanna play\x01",
            "with Zeit and me?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#3601047V#1500F#11PI would love to. Maybe I should ask\x01",
            "Father next time he visits.\x02\x03",
            "#3601048V#1505FIf I asked Estelle and Joshua, maybe\x01",
            "they would play with us, too...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x20,
        (
            "#3601049V#1105F#5PEstelle? Wasn't she that bracer girl?\x02\x03",
            "#3601050V#1100FI didn't know you knew her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#3601051V#1500F#11PWhen I go to the city, I like to\x01",
            "go shopping with them.\x02\x03",
            "#3601052VFather's usually busy, so...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(-23930, 900, -16040, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23640, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#3601053V#0002F#5PYou became quick friends\x01",
            "with Shizuku, huh, KeA?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_DC3B")

    ChrTalk(
        0x102,
        (
            "#3601054V#0109F#5PThey almost look like sisters,\x01",
            "chatting away like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DCE9")

    label("loc_DC3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_DCA0")

    ChrTalk(
        0x103,
        (
            "#3601055V#0204F#5PI'm impressed they got this close\x01",
            "in such a short span of time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DCE9")

    label("loc_DCA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_DCE9")

    ChrTalk(
        0x104,
        "#3601056V#0309F#5PThey're chattin' up a storm, ain't they?\x02",
    )

    CloseMessageWindow()

    label("loc_DCE9")


    NpcTalk(
        0x21,
        "Man's Voice",
        (
            "#3601057V#4PChildren are prone to become fast\x01",
            "friends, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_DD77():
        OP_93(0xFE, 0x167, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DD77)
    Sleep(50)

    def lambda_DD87():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_DD87)
    OP_68(-23930, 900, -14040, 5000)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_DDB0():
        OP_95(0xFE, -23910, 0, -12470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_DDB0)
    WaitChrThread(0x21, 1)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    ChrTalk(
        0x101,
        "#3601058V#0005F#12PA-Arios?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_DE58")

    ChrTalk(
        0x102,
        (
            "#3601059V#0104F#12PUm, we wanted to thank you for\x01",
            "helping us all the time, sir.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEFE")

    label("loc_DE58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_DEB0")

    ChrTalk(
        0x103,
        (
            "#3601060V#0204F#12PWe appreciate the assistance you\x01",
            "provide us, sir.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEFE")

    label("loc_DEB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_DEFE")

    ChrTalk(
        0x104,
        (
            "#3601061V#0303F#12PThanks for helpin' us out all the\x01",
            "time, man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEFE")


    ChrTalk(
        0x21,
        (
            "#3601062V#1404F#5PThere's no need for thanks. I merely\x01",
            "did what needed to be done.\x02\x03",
            "#3601063V#1400FNow...is that the girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3601064V#0000F#12PYeah. I'm sure you heard about\x01",
            "her from Michel, right?\x02\x03",
            "#3601065V#0004FHer name is KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#3601066V#1405F#5PIs that right?\x02\x03",
            "#3601067V...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#3601068V#0005F#12PIs something wrong?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_E0C0")

    ChrTalk(
        0x102,
        "#3601069V#0101F#12PWait...do you know her?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E13A")

    label("loc_E0C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_E100")

    ChrTalk(
        0x103,
        "#3601070V#0201F#12PHave you met her before?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E13A")

    label("loc_E100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_E13A")

    ChrTalk(
        0x104,
        "#3601071V#0301F#12PNo way... You know her?!\x02",
    )

    CloseMessageWindow()

    label("loc_E13A")


    ChrTalk(
        0x21,
        (
            "#3601072V#1402F#5PNo. I simply find her curious.\x02\x03",
            "#3601073V#1404FYou see, Shizuku is as well behaved as a\x01",
            "father could ever hope for, but she's usually\x01",
            "incredibly shy.\x02\x03",
            "#3601074VAs a result, she hasn't been able to make\x01",
            "many friends her own age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3601075V#0012F#12PSo that's what you meant.\x02\x03",
            "#3601076V#0002FIt looks like they're having the\x01",
            "time of their lives, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#3601077V#1402F#5PIndeed it does...\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x21)

    ChrTalk(
        0x21,
        (
            "#3601078V#1403F#5PI'm unaware of that girl's background or past.\x02\x03",
            "#3601079V#1400FHowever, since you willingly got yourselves\x01",
            "involved, you must take responsibility for her\x01",
            "until the bitter end.\x02\x03",
            "#3601080V#1404FSo...take good care of her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3601081V#0005F#12P...\x02\x03",
            "#3601082V#0004FYeah. We intend to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "#3601083V#1505F#1PFather?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_E480")

    ChrTalk(
        0x20,
        "#3601084V#1107F#1PLloyd?! Elie?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E4E3")

    label("loc_E480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_E4B3")

    ChrTalk(
        0x20,
        "#3601085V#1107F#1PLloyd?! Tio?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E4E3")

    label("loc_E4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_E4E3")

    ChrTalk(
        0x20,
        "#3601086V#1107F#1PLloyd?! Randy?!\x02",
    )

    CloseMessageWindow()

    label("loc_E4E3")


    def lambda_E4E8():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E4E8)
    Sleep(50)

    def lambda_E4F8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_E4F8)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#3601087V#0012F#5PCaught at last.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#3601088V#1402F#5PHaha...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-24710, 200, -23740, 0)
    MoveCamera(44, 16, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(27550, 0)
    SetCameraDistance(24550, 3000)
    SetChrPos(0x1F, -23760, -1000, -24640, 0)
    SetChrPos(0x20, -25130, -1000, -24700, 45)
    SetChrPos(0x101, -24850, -1000, -17000, 180)
    SetChrPos(0xEF, -26280, -1000, -17870, 180)
    SetChrPos(0x21, -23900, -1000, -18210, 180)

    def lambda_E5E1():

        label("loc_E5E1")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_E5E1")

    QueueWorkItem2(0x20, 2, lambda_E5E1)

    def lambda_E5F3():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E5F3)
    Sleep(50)

    def lambda_E60B():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_E60B)
    Sleep(50)

    def lambda_E623():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_E623)
    WaitChrThread(0xEF, 1)

    def lambda_E63C():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_E63C)
    WaitChrThread(0x101, 1)

    def lambda_E64D():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E64D)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x21, 1)
    EndChrThread(0x20, 0x2)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x1F,
        (
            "#3601089V#1500F#12PWelcome back, Father.\x02\x03",
            "#3601090VHow was work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#3601091V#1404F#5PIt wasn't too difficult this time\x01",
            "around.\x02\x03",
            "#3601092V#1402FI'm glad to be back, Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#3601093V#1105F#6POh! This is your dad, Shizuku?\x02\x03",
            "#3601094V#1110FHe's as tall as a tree!\x02\x03",
            "#3601095V#1109FAnd looks as tough as one, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x10E, 0x190)

    ChrTalk(
        0x1F,
        "#3601096V#1502F#11PHeehee. You think so?\x02",
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_E7FA():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_E7FA)
    Sleep(150)

    def lambda_E80A():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_E80A)
    Sleep(150)

    ChrTalk(
        0x1F,
        (
            "#3601097V#1500F#12POh, and hello, SSS. It's good to\x01",
            "see you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3601098V#0002F#5PYeah. You, too.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_E8DE")

    ChrTalk(
        0x102,
        (
            "#3601099V#0109F#5PYou must be getting along well\x01",
            "with KeA, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E992")

    label("loc_E8DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_E939")

    ChrTalk(
        0x103,
        (
            "#3601100V#0202F#5PIt is good to see you getting along\x01",
            "with KeA so well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E992")

    label("loc_E939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_E992")

    ChrTalk(
        0x104,
        (
            "#3601101V#0309F#5PLooks like you're gettin' along well\x01",
            "with KeDo here, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E992")


    ChrTalk(
        0x1F,
        (
            "#3601102V#1502F#12POh, no. She's the one who's\x01",
            "getting along with me.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x20,
        (
            "#3601103V#1103F#12P...Lloyd.\x02\x03",
            "#3601104V#1101FI am absolutely not staying in a place\x01",
            "like this, you hear me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3601105V#0006F#5PYou made that painfully clear.\x02\x03",
            "#3601106V#0002FBut, you know...if you decided to stay\x01",
            "here, you would be able to play with\x01",
            "Shizuku every day.\x02\x03",
            "#3601107VYou two are friends, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x20,
        (
            "#3601108V#1110F#12PI would?!\x02\x03",
            "#3601109V#1108FBut I don't want to be away\x01",
            "from you guys...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#3601110V#1508F#12PLloyd, try to be more sensitive.\x02\x03",
            "#3601111VYou're just hurting her feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3601112V#0012F#5PMaybe you're right.\x02\x03",
            "#3601113V#0000FI'm sorry, KeA. Are you about\x01",
            "ready to head on home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#3601114V#1112F#12PAww. I wanted to talk to Shizuku\x01",
            "for a little bit longer...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_ED63")

    ChrTalk(
        0x102,
        (
            "#3601115V#0104F#5PWe'll come visit. I promise.\x02\x03",
            "#3601116V#0100FAlso, Shizuku is welcome to come play\x01",
            "with you whenever she's in the city.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EEF7")

    label("loc_ED63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_EE2C")

    ChrTalk(
        0x103,
        (
            "#3601117V#0204F#5PWe can come visit some other time.\x02\x03",
            "#3601118V#0202FAlso, I doubt there would be any objections\x01",
            "to inviting Shizuku to come play whenever\x01",
            "she visits Crossbell City.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EEF7")

    label("loc_EE2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_EEF7")

    ChrTalk(
        0x104,
        (
            "#3601119V#0304F#5PWe'll visit again, don't you worry about that.\x02\x03",
            "#3601120V#0300FBesides, I'm sure lil' Shizuku would be more\x01",
            "than happy to come play with you in the city\x01",
            "whenever she can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EEF7")


    ChrTalk(
        0x20,
        "#3601121V#1110F#12PReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#3601122V#1404F#5PI'll leave her in your hands, then.\x02",
    )

    CloseMessageWindow()
    OP_93(0x21, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x21,
        "#3601123V#1402F#5PUp you go, Shizuku.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "#3601124V#1500F#12PO-Okay!\x02",
    )

    CloseMessageWindow()
    OP_68(-24710, 200, -23540, 2000)
    OP_9B(0x0, 0x1F, 0x0, 0x3E8, 0x5DC, 0x0)
    OP_6F(0x79)
    Fade(500)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    Sound(804, 0, 100, 0)
    OP_0D()

    def lambda_EFEC():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EFEC)
    Sleep(50)

    def lambda_EFFC():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_EFFC)
    Sleep(50)

    def lambda_F00C():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_F00C)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3601125V#0000F#5PArios, are you planning to stay\x01",
            "here for the rest of the day?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0xEF, 400)
    Sleep(150)

    ChrTalk(
        0x21,
        "#3601126V#1404F#11PYes. I'm going to spend the night.\x02",
    )

    CloseMessageWindow()
    OP_93(0x21, 0xE1, 0x190)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#3601127V#1402F#11PKeA. As her father, I would be pleased\x01",
            "if you would be a good friend to Shizuku\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#3601140V#1109F#6PAbsolutely!\x02\x03",
            "#3601129V#1110FSee ya, Shizuku!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x21,
        "Shizuku",
        "#3601130V#1502F#5PGoodbye, KeA!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    OP_93(0x21, 0x0, 0x190)
    Sleep(300)
    OP_68(-24710, 200, -23040, 5000)

    def lambda_F1CB():

        label("loc_F1CB")

        TurnDirection(0x101, 0x21, 500)
        Yield()
        Jump("loc_F1CB")

    QueueWorkItem2(0x101, 1, lambda_F1CB)

    def lambda_F1DD():

        label("loc_F1DD")

        TurnDirection(0xEF, 0x21, 500)
        Yield()
        Jump("loc_F1DD")

    QueueWorkItem2(0xEF, 1, lambda_F1DD)

    def lambda_F1EF():

        label("loc_F1EF")

        TurnDirection(0x20, 0x21, 500)
        Yield()
        Jump("loc_F1EF")

    QueueWorkItem2(0x20, 1, lambda_F1EF)

    def lambda_F201():
        OP_95(0xFE, -23810, 0, -9390, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_F201)
    WaitChrThread(0x21, 1)
    ClearChrFlags(0x21, 0x8000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x20, 0x1)
    OP_6F(0x1)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    Sleep(1000)
    OP_68(-25130, 200, -23360, 1000)
    MoveCamera(36, 16, 0, 1000)

    def lambda_F265():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F265)
    Sleep(50)

    def lambda_F275():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_F275)
    OP_93(0x20, 0x0, 0x1F4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#3601131V#0002F#5PWell, it's time for us to get going.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_F32A")

    ChrTalk(
        0x102,
        (
            "#3601132V#0102F#5PThat's right. Sunset is going to\x01",
            "hit us before we know it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F3CB")

    label("loc_F32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_F378")

    ChrTalk(
        0x103,
        "#3601133V#0202F#5PIndeed. It is almost evening, after all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F3CB")

    label("loc_F378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_F3CB")

    ChrTalk(
        0x104,
        (
            "#3601134V#0302F#5PYup. If we don't hurry, the sun's\x01",
            "gonna set on us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F3CB")


    ChrTalk(
        0x20,
        (
            "#3601135V#1105F#12PNow that I think about it, the sky's\x01",
            "turning all reddish, isn't it?\x02\x03",
            "#3601136V#1109FAnd I'm hungry, too!\x02\x03",
            "#3601137V#1110FWhat's for dinner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3601138V#0012F#5PShe sure is a bundle of energy.\x02\x03",
            "#3601139V#0000FLet's go say our goodbyes to Cecile\x01",
            "and then hop on one of the buses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#3601128V#1109F#12POkie dokie!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23550, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_F567")
    RemoveParty(0x1, 0x0)
    Jump("loc_F584")

    label("loc_F567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_F578")
    RemoveParty(0x2, 0x0)
    Jump("loc_F584")

    label("loc_F578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_F584")
    RemoveParty(0x3, 0x0)

    label("loc_F584")

    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    StopBGM(0x1388)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 3)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_57_D586 end

    def Function_58_F5AC(): pass

    label("Function_58_F5AC")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-35700, 900, 0, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    SetCameraDistance(21000, 2500)
    SetChrPos(0x101, -42200, 0, -1000, 90)
    SetChrPos(0x102, -42200, 0, 400, 90)
    SetChrPos(0x103, -43600, 0, -1000, 90)
    SetChrPos(0x104, -43600, 0, 400, 90)

    def lambda_F633():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F633)
    Sleep(50)

    def lambda_F64B():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F64B)
    Sleep(50)

    def lambda_F663():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F663)
    Sleep(50)

    def lambda_F67B():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F67B)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    ModifyEventFlags(0, 3, 0x80)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#4200843V#0001F#6PWell, let's see if Doctor Guenter\x01",
            "has some time to meet with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200844V#0100F#5PYes. We should probably ask the\x01",
            "receptionist about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200845V#0306F#5PI just hope he didn't play hooky\x01",
            "to go fishin' again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200846V#0211F#6PI would not even be surprised if\x01",
            "that were the case.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -37900, 0, -300, 90)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetScenarioFlags(0xC3, 2)
    OP_29(0x4C, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_58_F5AC end

    def Function_59_F81A(): pass

    label("Function_59_F81A")

    EventBegin(0x0)
    LoadChrToIndex("apl/ch50410.itc", 0x1E)
    Fade(1000)
    OP_68(-50560, 1300, 0, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(18250, 3000)
    ClearMapObjFlags(0x6, 0x10)
    OP_71(0x6, 0xA, 0xA, 0x0, 0x0)
    OP_79(0x6)
    SetChrPos(0x101, -44720, 0, -560, 270)
    SetChrPos(0x102, -43930, 0, 910, 270)
    SetChrPos(0x103, -42520, 0, -220, 270)
    SetChrPos(0x104, -46240, 0, 700, 270)

    def lambda_F8BC():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F8BC)
    Sleep(50)

    def lambda_F8D4():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F8D4)
    Sleep(50)

    def lambda_F8EC():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F8EC)
    Sleep(50)

    def lambda_F904():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F904)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    ModifyEventFlags(0, 4, 0x80)
    OP_6F(0x10)
    OP_0D()
    OP_93(0x104, 0x5A, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#4200982V#0302F#6PSo, now that it's evenin', we wanna\x01",
            "grab the next bus?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200983V#0002F#11PNo complaints here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200984V#0102F#11PThank goodness for the convenience\x01",
            "of the bus system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200998V#0208F#11P#50W...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-49060, 1300, 0, 1500)

    def lambda_FA6A():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FA6A)

    def lambda_FA77():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FA77)
    Sleep(100)

    def lambda_FA87():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FA87)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#4200986V#0005F#6PTio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200987V#0305F#6PWhat's the matter, Tio Tot? You've been\x01",
            "awfully quiet for a bit now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200988V#0206F#11P#60W...I am fine.\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_FB5F():
        OP_9B(0x0, 0xFE, 0x0, 0x352, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FB5F)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#4200989V#0101F#5PTio?!\x02\x03",
            "#4200990VThe sun makes it hard to see,\x01",
            "but your face... It's so pale!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4200991V#0011F#6PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200992V#0202F#11P#50WI told you, I am fine. I just feel a bit\x01",
            "unwell, is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200993V#0306F#6PSounds like a contradiction to me.\x02\x03",
            "#4200994V#0301FThere's gotta be some place to rest around--\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    ChrTalk(
        0x103,
        "#4200995V#0206F#11P#60WAh...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrFlags(0x103, 0x2)
    SetChrFlags(0x103, 0x10)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    Sound(910, 0, 100, 0)
    OP_0D()
    Sleep(150)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x103, 0x1)
    Sleep(150)
    SetChrSubChip(0x103, 0x2)
    Sleep(300)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4200996V#0007F#6PTio?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200997V#0101F#5PThis isn't good!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200985V#11P#60W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200999V#0307F#6PI'll go get a doctor!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201000V#0007F#5PQuickly!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 60)
    Sleep(300)
    OP_68(-48210, 1300, -210, 2000)

    def lambda_FE6F():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FE6F)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x104, 0x3)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x2)
    ClearChrFlags(0x103, 0x10)
    OP_49()
    OP_D5(0x1E)
    Sleep(2000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_59_F81A end

    def Function_60_FEBC(): pass

    label("Function_60_FEBC")

    OP_95(0xFE, -49190, 0, 2050, 5000, 0x0)
    OP_95(0xFE, -35480, 0, 180, 5000, 0x0)
    Return()

    # Function_60_FEBC end

    def Function_61_FEE5(): pass

    label("Function_61_FEE5")

    OP_A1(0xFE, 0x3E8, 0x4, 0x2, 0x3, 0x4, 0x3)
    Return()

    # Function_61_FEE5 end

    def Function_62_FEF0(): pass

    label("Function_62_FEF0")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-18180, 0, -17650, 0)
    MoveCamera(352, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x101, -18160, -1000, -18590, 45)
    SetChrPos(0x102, -18950, -1000, -17790, 45)
    SetChrPos(0x103, -19750, -1000, -18590, 45)
    SetChrPos(0x104, -18950, -1000, -19390, 45)
    SetChrPos(0x109, -18160, -1000, -20020, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x17, 0x2)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x17,
        "#11PI've been dead tired, lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PFirst, when I asked Cirone to order\x01",
            "new equipment, we were delivered\x01",
            "something entirely different...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P...and on top of that, my son, Kienz,\x01",
            "still has no intentions of leaving that\x01",
            "foolish 'gang' he's in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PI may be a doctor and all, but\x01",
            "life just won't give me a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005F(He's a doctor here? I sort of feel terrible\x01",
            "for the guy...)\x02\x03",
            "#0003F(Still, he might have some idea about\x01",
            "what materials would be good for\x01",
            "Shizuku's present.)\x02\x03",
            "#0000FExcuse us. There was something we\x01",
            "wanted to ask you about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#11PHmm? What is it?\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that they were collecting materials\x01",
            "for a present Shizuku wanted to make.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#6P#0000FRight now, we're still trying to figure\x01",
            "out what to look for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#11POh, it's for little Shizuku?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PIf that's the case, there might be\x01",
            "something over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FWhere, exactly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PAllow me to explain. In this hospital,\x01",
            "a large quantity of goods are stored\x01",
            "away and forgotten about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PI'd go so far as to say that they're\x01",
            "in mint condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0105FWhat kind of goods? And why are\x01",
            "they here at St. Ursula?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PA while ago, I asked one of our nurses,\x01",
            "Cirone, to order some surgical supplies,\x01",
            "like scalpels and things of that nature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PBut instead, what was delivered was\x01",
            "an assortment of random goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PHow did this happen, you may ask?\x01",
            "That's what I would like to know.\x02",
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
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#6P#0300FThat's unlucky, man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#0506FIn a way, it reminds me of all the\x01",
            "headaches the commander causes\x01",
            "for the rest of the Guardian Force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FWould you mind if we took a look at them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PI don't mind. Frankly, it's been a pain trying\x01",
            "to get someone to take them off our hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PYou can find that container on the terrace\x01",
            "right outside of the men's dormitory on the\x01",
            "second floor of the Le Lectier Inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11PIf you see something that catches your\x01",
            "eye, by all means, take it with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FThat's great. Thanks for the help.\x02\x03",
            "#0003F(So, the dormitory's second floor terrace...\x01",
            "That should be where they put the fence\x01",
            "up after the monster attack.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -18160, -1000, -18590, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, -23040, -1000, -25910, 0)
    BeginChrThread(0x9, 0, 0, 1)
    OP_29(0x2C, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_62_FEF0 end

    def Function_63_108C8(): pass

    label("Function_63_108C8")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-36870, 4000, 16950, 0)
    MoveCamera(35, 29, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23790, 0)
    SetChrPos(0x101, -36910, 3000, 16290, 90)
    SetChrPos(0x102, -38300, 3000, 16300, 90)
    SetChrPos(0x103, -38300, 3000, 17300, 90)
    SetChrPos(0x104, -37000, 3000, 17300, 90)
    SetChrPos(0x109, -37000, 3000, 18600, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x17, 0x2)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#0000FI think this is the container the doctor mentioned.\x02\x03",
            "All right. Let's check it out.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#5P#0505FDo you see anything that will work for us\x01",
            "in there?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)

    ChrTalk(
        0x101,
        "#12P#0000FYeah. At least, I think so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FIs that...a knitted leather string?\x02\x03",
            "#0100FIt looks well made, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FIs there anything else?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FW-Well, I gave it another look, and...\x02\x03",
            "...it's full of creepy dolls and figurines.\x01",
            "I guess these are to ward off evil spirits\x01",
            "or something along those lines.\x02\x03",
            "#0000FI think this knitted string is the best\x01",
            "we're going to find in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0306FI can see why the doctor was havin'\x01",
            "trouble gettin' rid of it, now.\x02\x03",
            "#0300FGuess we should consider ourselves\x01",
            "lucky, findin' at least one good thing in\x01",
            "there, eh?\x02",
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
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x343),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x343, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D9F")

    ChrTalk(
        0x101,
        (
            "#12P#0003F(With a string as sturdy as this one,\x01",
            "I doubt it'd end up snapping even if\x01",
            "Arios was the one wearing it.)\x02\x03",
            "(All that's left is to find a pendant top\x01",
            "that can fit Shizuku's stone.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D9F")

    OP_29(0x2C, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10E8A")
    OP_29(0x2C, 0x1, 0x5)

    ChrTalk(
        0x101,
        (
            "#12P#0000F(We should have everything, now. I bet\x01",
            "the gift box and ribbon will go great with\x01",
            "the rest of the present, too.)\x02\x03",
            "(I think it's about time to show Shizuku\x01",
            "what we found.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E8A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -37600, 3000, 16800, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_65(0x8, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_63_108C8 end

    def Function_64_10EBA(): pass

    label("Function_64_10EBA")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11051")

    ChrTalk(
        0x101,
        (
            "#0001FThe road's in that direction.\x02\x03",
            "#0003FIt's not like we can steal Cecile\x01",
            "away from her job.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FC4")

    ChrTalk(
        0x136,
        (
            "#1300FYou still have to conduct your\x01",
            "investigation, right?\x02\x03",
            "I'll show you to the second floor\x01",
            "of the hospital, if you follow me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11051")

    label("loc_10FC4")


    ChrTalk(
        0x136,
        (
            "#1300FYou still have to conduct your\x01",
            "investigation, right?\x02\x03",
            "The scene of the crime took place on\x01",
            "the roof. I'll show you the way there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_110D2")

    ChrTalk(
        0x101,
        (
            "#0000FThe road's in that direction.\x02\x03",
            "#0003FBefore we head home, we need to\x01",
            "fill Cecile in on what we learned.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_110D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1117D")

    ChrTalk(
        0x101,
        (
            "#0000FIt's late. It'd be smarter to take the\x01",
            "bus back to Crossbell City.\x02\x03",
            "If we check the bus stop, we should\x01",
            "be able to see when the next bus\x01",
            "arrives.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1117D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11248")

    ChrTalk(
        0x101,
        (
            "#0000FOh, we can't leave yet. It'd be a waste\x01",
            "to come all the way out here and not\x01",
            "consult them regarding neurology.\x02\x03",
            "Let's try asking the receptionist about\x01",
            "the Neurology Department.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1130B")

    ChrTalk(
        0x101,
        (
            "#0003FKeA's with us right now. It wouldn't be a good\x01",
            "idea to go out onto the road with her.\x02\x03",
            "#0000FFor now, we need to ask Doctor Guenter\x01",
            "for advice about KeA's lost memories.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1130B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_113E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1138B")

    ChrTalk(
        0x101,
        (
            "#0003FKeA should still be somewhere on the\x01",
            "hospital grounds.\x02\x03",
            "#0001FLet's hurry and find her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_113E5")

    label("loc_1138B")


    ChrTalk(
        0x101,
        (
            "#0001FI doubt KeA would have left the hospital\x01",
            "grounds. Let's hurry up and find her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113E5")

    Sleep(50)
    SetChrPos(0x0, -61000, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_64_10EBA end

    def Function_65_113FC(): pass

    label("Function_65_113FC")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "St. Ursula Medical College\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_65_113FC end

    def Function_66_1144F(): pass

    label("Function_66_1144F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "St. Ursula Medical College\x01",
            "Le Lectier Inn\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_66_1144F end

    SaveToFile()

Try(main)
