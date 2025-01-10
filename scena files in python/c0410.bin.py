from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0410.bin",                # FileName
        "c0410",                    # MapName
        "c0410",                    # Location
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
        "c0410",                  # 0
        "Ilya",                   # 1
        "Rixia",                  # 2
        "Karelia",                # 3
        "Manager Balsamo",        # 4
        "Receptionist Rowland",   # 5
        "Troupe Leader Avan",     # 6
        "Heinz",                  # 7
        "Eugene",                 # 8
        "Theodor",                # 9
        "Nikolai",                # 10
        "Plie",                   # 11
        "Selene",                 # 12
        "Sully",                  # 13
        "Ilya",                   # 14
        "Eugene",                 # 15
        "Selene",                 # 16
        "Spectator",              # 17
        "Spectator",              # 18
        "Spectator",              # 19
        "Spectator",              # 20
        "Mayor MacDowell",        # 21
        "Secretary Ernest",       # 22
        "Grace",                  # 23
        "Detective Dudley",       # 24
        "Officer",                # 25
        "Guest",                  # 26
        "Guest",                  # 27
        "Guest",                  # 28
        "Guest",                  # 29
        "Guest",                  # 30
        "Guest",                  # 31
        "Guest",                  # 32
        "Guest",                  # 33
        "Guest",                  # 34
        "Guest",                  # 35
    ))

    AddCharChip((
        "chr/ch05100.itc",                   # 00
        "chr/ch05200.itc",                   # 01
        "chr/ch21900.itc",                   # 02
        "chr/ch25800.itc",                   # 03
        "chr/ch25900.itc",                   # 04
        "chr/ch27500.itc",                   # 05
        "chr/ch24200.itc",                   # 06
        "chr/ch28700.itc",                   # 07
        "chr/ch28702.itc",                   # 08
        "chr/ch28800.itc",                   # 09
        "chr/ch28900.itc",                   # 0A
        "chr/ch29000.itc",                   # 0B
        "chr/ch29100.itc",                   # 0C
        "chr/ch29102.itc",                   # 0D
        "chr/ch36600.itc",                   # 0E
        "chr/ch36602.itc",                   # 0F
        "chr/ch36700.itc",                   # 10
        "chr/ch36900.itc",                   # 11
        "apl/ch50257.itc",                   # 12
        "chr/ch09800.itc",                   # 13
        "chr/ch10100.itc",                   # 14
        "chr/ch21200.itc",                   # 15
        "chr/ch33200.itc",                   # 16
        "chr/ch21100.itc",                   # 17
        "chr/ch20100.itc",                   # 18
    ))

    DeclNpc(-123849, 0,       -2240,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-123050, 0,       -920,    315,  389,  0x0, 0,   1,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-123800, 0,       -2289,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-2250,   2500,    15000,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(6969,    0,       3480,    270,  261,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-42090,  5599,    102569,  135,  389,  0x0, 0,   5,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-50150,  0,       24180,   0,    389,  0x0, 0,   6,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-125209, 0,       -479,    270,  389,  0x0, 0,   7,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-87309,  0,       -1980,   90,   261,  0x0, 0,   9,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-49939,  0,       13039,   90,   389,  0x0, 0,   10,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-93360,  0,       -2000,   180,  261,  0x0, 0,   11,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-125250, 0,       -460,    270,  261,  0x0, 0,   12,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(4920,    0,       5170,    225,  389,  0x0, 0,   20,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(-87550,  50,      -50,     90,   389,  0x0, 0,   18,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-87550,  50,      -50,     90,   261,  0x0, 0,   8,   0,   255, 255, 0,   21,  255,  0)
    DeclNpc(-87550,  50,      -50,     90,   389,  0x0, 0,   13,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(-39490,  5599,    99000,   0,    389,  0x0, 0,   21,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(-39279,  5599,    100540,  180,  389,  0x0, 0,   22,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(-340,    0,       2079,    315,  405,  0x0, 0,   23,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(-949,    0,       2880,    0,    389,  0x0, 0,   24,  0,   0,   0,   0,   35,  255,  0)
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

    DeclEvent(0x0000, 0, 86,  9.0,                   14.0,                  2.5,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -4.5,                  -2.799999713897705,    -0.4999999701976776,   1.0])

    DeclActor(0,       2500,    16500,   1200,    0,       3500,    16500,   0x007C, 0,  43, 0x0000)
    DeclActor(47000,   5600,    15300,   1200,    47000,   6600,    15300,   0x007C, 0,  45, 0x0000)
    DeclActor(-37500,  5600,    98000,   1200,    -37500,  6600,    98000,   0x007C, 0,  44, 0x0000)
    DeclActor(-47000,  11200,   125000,  1200,    -47000,  12200,   125000,  0x007C, 0,  46, 0x0000)
    DeclActor(6500,    0,       5000,    1200,    6970,    1500,    5000,    0x007E, 0,  9,  0x0000)
    DeclActor(6500,    0,       3480,    1200,    6970,    1500,    3480,    0x007E, 0,  12, 0x0000)
    DeclActor(-50140,  0,       24750,   1200,    -50140,  1500,    24750,   0x007C, 0,  89, 0x0000)

    ScpFunction((
        "Function_0_790",          # 00, 0
        "Function_1_848",          # 01, 1
        "Function_2_873",          # 02, 2
        "Function_3_89E",          # 03, 3
        "Function_4_8C9",          # 04, 4
        "Function_5_8F4",          # 05, 5
        "Function_6_11E0",         # 06, 6
        "Function_7_1517",         # 07, 7
        "Function_8_15FA",         # 08, 8
        "Function_9_25CC",         # 09, 9
        "Function_10_25D0",        # 0A, 10
        "Function_11_2747",        # 0B, 11
        "Function_12_3B97",        # 0C, 12
        "Function_13_3B9B",        # 0D, 13
        "Function_14_3CB5",        # 0E, 14
        "Function_15_4048",        # 0F, 15
        "Function_16_42D4",        # 10, 16
        "Function_17_4663",        # 11, 17
        "Function_18_514B",        # 12, 18
        "Function_19_5569",        # 13, 19
        "Function_20_5B61",        # 14, 20
        "Function_21_5C89",        # 15, 21
        "Function_22_6110",        # 16, 22
        "Function_23_6318",        # 17, 23
        "Function_24_682B",        # 18, 24
        "Function_25_7332",        # 19, 25
        "Function_26_79DA",        # 1A, 26
        "Function_27_806B",        # 1B, 27
        "Function_28_847C",        # 1C, 28
        "Function_29_9558",        # 1D, 29
        "Function_30_9677",        # 1E, 30
        "Function_31_99EC",        # 1F, 31
        "Function_32_9B34",        # 20, 32
        "Function_33_9BE4",        # 21, 33
        "Function_34_9C79",        # 22, 34
        "Function_35_9D08",        # 23, 35
        "Function_36_9DB6",        # 24, 36
        "Function_37_A669",        # 25, 37
        "Function_38_A6CE",        # 26, 38
        "Function_39_A6EA",        # 27, 39
        "Function_40_AAE3",        # 28, 40
        "Function_41_AD82",        # 29, 41
        "Function_42_B02B",        # 2A, 42
        "Function_43_B409",        # 2B, 43
        "Function_44_B648",        # 2C, 44
        "Function_45_B701",        # 2D, 45
        "Function_46_B7BA",        # 2E, 46
        "Function_47_B86D",        # 2F, 47
        "Function_48_C660",        # 30, 48
        "Function_49_CE63",        # 31, 49
        "Function_50_F900",        # 32, 50
        "Function_51_F937",        # 33, 51
        "Function_52_F97B",        # 34, 52
        "Function_53_F9BF",        # 35, 53
        "Function_54_10C77",       # 36, 54
        "Function_55_10CB2",       # 37, 55
        "Function_56_10CED",       # 38, 56
        "Function_57_115E9",       # 39, 57
        "Function_58_117D2",       # 3A, 58
        "Function_59_1195A",       # 3B, 59
        "Function_60_11B9A",       # 3C, 60
        "Function_61_11D97",       # 3D, 61
        "Function_62_11F9E",       # 3E, 62
        "Function_63_121CE",       # 3F, 63
        "Function_64_12395",       # 40, 64
        "Function_65_12502",       # 41, 65
        "Function_66_1264F",       # 42, 66
        "Function_67_12860",       # 43, 67
        "Function_68_129F0",       # 44, 68
        "Function_69_12C18",       # 45, 69
        "Function_70_12E76",       # 46, 70
        "Function_71_1307D",       # 47, 71
        "Function_72_135F8",       # 48, 72
        "Function_73_1363F",       # 49, 73
        "Function_74_14C3C",       # 4A, 74
        "Function_75_14CA5",       # 4B, 75
        "Function_76_14D0E",       # 4C, 76
        "Function_77_14D6A",       # 4D, 77
        "Function_78_150C7",       # 4E, 78
        "Function_79_1518A",       # 4F, 79
        "Function_80_15258",       # 50, 80
        "Function_81_152E7",       # 51, 81
        "Function_82_1533C",       # 52, 82
        "Function_83_15391",       # 53, 83
        "Function_84_158FE",       # 54, 84
        "Function_85_1591A",       # 55, 85
        "Function_86_15936",       # 56, 86
        "Function_87_15952",       # 57, 87
        "Function_88_15A3D",       # 58, 88
        "Function_89_15E22",       # 59, 89
    ))


    def Function_0_790(): pass

    label("Function_0_790")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_7D0"),
        (1, "loc_7DC"),
        (2, "loc_7E8"),
        (3, "loc_7F4"),
        (4, "loc_800"),
        (5, "loc_80C"),
        (6, "loc_818"),
        (SWITCH_DEFAULT, "loc_824"),
    )


    label("loc_7D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_7DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_7E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_7F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_800")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_80C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_818")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_824")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_830")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_847")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_830")

    label("loc_847")

    Return()

    # Function_0_790 end

    def Function_1_848(): pass

    label("Function_1_848")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_872")
    OP_94(0xFE, 0xFFFFF402, 0xFFFFF59C, 0xB72, 0xD0C, 0x3E8)
    Sleep(300)
    Jump("Function_1_848")

    label("loc_872")

    Return()

    # Function_1_848 end

    def Function_2_873(): pass

    label("Function_2_873")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_89D")
    OP_94(0xFE, 0xFFFE9F26, 0x5B4, 0xFFFE9346, 0xFFFFFA56, 0x3E8)
    Sleep(300)
    Jump("Function_2_873")

    label("loc_89D")

    Return()

    # Function_2_873 end

    def Function_3_89E(): pass

    label("Function_3_89E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8C8")
    OP_94(0xFE, 0xFFFE17C2, 0xFFFFF8C6, 0xFFFE244C, 0x546, 0x3E8)
    Sleep(300)
    Jump("Function_3_89E")

    label("loc_8C8")

    Return()

    # Function_3_89E end

    def Function_4_8C9(): pass

    label("Function_4_8C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8F3")
    OP_94(0xFE, 0xFFFF403E, 0x201C, 0xFFFF3760, 0x42E0, 0x3E8)
    Sleep(300)
    Jump("Function_4_8C9")

    label("loc_8F3")

    Return()

    # Function_4_8C9 end

    def Function_5_8F4(): pass

    label("Function_5_8F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90A")
    SetMapFlags(0x10000000)
    Event(0, 48)

    label("loc_90A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_94C")
    Event(0, 66)

    label("loc_94C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_98E")
    Event(0, 68)

    label("loc_98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9C7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C7")
    Event(0, 70)

    label("loc_9C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E1")
    Event(0, 73)

    label("loc_9E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F7")
    Event(0, 42)
    Jump("loc_A70")

    label("loc_9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A05")
    Jump("loc_A70")

    label("loc_A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A1B")
    Event(0, 41)
    Jump("loc_A70")

    label("loc_A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_A29")
    Jump("loc_A70")

    label("loc_A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3F")
    Event(0, 40)
    Jump("loc_A70")

    label("loc_A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_END)), "loc_A4D")
    Jump("loc_A70")

    label("loc_A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A63")
    Event(0, 39)
    Jump("loc_A70")

    label("loc_A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A70")
    Event(0, 36)

    label("loc_A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_A84")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 47)
    Jump("loc_BD3")

    label("loc_A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_A98")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 49)
    Jump("loc_BD3")

    label("loc_A98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_AAC")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 53)
    Jump("loc_BD3")

    label("loc_AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_AC0")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 56)
    Jump("loc_BD3")

    label("loc_AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_AD4")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 57)
    Jump("loc_BD3")

    label("loc_AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_AE8")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 58)
    Jump("loc_BD3")

    label("loc_AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 6)), scpexpr(EXPR_END)), "loc_AFC")
    ClearScenarioFlags(0x5C, 6)
    Event(0, 59)
    Jump("loc_BD3")

    label("loc_AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 7)), scpexpr(EXPR_END)), "loc_B10")
    ClearScenarioFlags(0x5C, 7)
    Event(0, 60)
    Jump("loc_BD3")

    label("loc_B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 0)), scpexpr(EXPR_END)), "loc_B24")
    ClearScenarioFlags(0x5D, 0)
    Event(0, 61)
    Jump("loc_BD3")

    label("loc_B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 1)), scpexpr(EXPR_END)), "loc_B38")
    ClearScenarioFlags(0x5D, 1)
    Event(0, 62)
    Jump("loc_BD3")

    label("loc_B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 2)), scpexpr(EXPR_END)), "loc_B4C")
    ClearScenarioFlags(0x5D, 2)
    Event(0, 63)
    Jump("loc_BD3")

    label("loc_B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 3)), scpexpr(EXPR_END)), "loc_B60")
    ClearScenarioFlags(0x5D, 3)
    Event(0, 64)
    Jump("loc_BD3")

    label("loc_B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 4)), scpexpr(EXPR_END)), "loc_B74")
    ClearScenarioFlags(0x5D, 4)
    Event(0, 65)
    Jump("loc_BD3")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 5)), scpexpr(EXPR_END)), "loc_B88")
    ClearScenarioFlags(0x5D, 5)
    Event(0, 67)
    Jump("loc_BD3")

    label("loc_B88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 6)), scpexpr(EXPR_END)), "loc_B9C")
    ClearScenarioFlags(0x5D, 6)
    Event(0, 69)
    Jump("loc_BD3")

    label("loc_B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 7)), scpexpr(EXPR_END)), "loc_BB0")
    ClearScenarioFlags(0x5D, 7)
    Event(0, 71)
    Jump("loc_BD3")

    label("loc_BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 0)), scpexpr(EXPR_END)), "loc_BC4")
    ClearScenarioFlags(0x5E, 0)
    Event(0, 77)
    Jump("loc_BD3")

    label("loc_BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 1)), scpexpr(EXPR_END)), "loc_BD3")
    ClearScenarioFlags(0x5E, 1)
    Event(0, 83)

    label("loc_BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_C99")
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -89630, 0, -390, 315)
    SetChrPos(0x10, -90490, 0, 470, 135)
    SetChrPos(0x12, -48930, 0, 4630, 0)
    SetChrPos(0xA, -48930, 0, 6000, 180)
    SetChrPos(0x13, 1440, 0, 14370, 270)
    SetChrPos(0x8, -122330, 0, 670, 270)
    SetChrPos(0xD, -123720, 0, 580, 90)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C85")
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C94")
    SetChrFlags(0xF, 0x10)

    label("loc_C94")

    Jump("loc_11DF")

    label("loc_C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D4F")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -90560, 0, 490, 225)
    SetChrPos(0x10, -90970, 0, 4810, 90)
    SetChrPos(0x13, -123590, 0, -450, 225)
    SetChrPos(0xA, -89290, 0, 4810, 270)
    BeginChrThread(0xF, 0, 0, 2)
    BeginChrThread(0x13, 0, 0, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D10")
    SetChrFlags(0xA, 0x10)

    label("loc_D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_D45")
    SetChrPos(0xB, -1160, 0, 130, 135)
    SetChrPos(0xC, 230, 0, -860, 315)
    SetChrFlags(0xC, 0x10)
    Jump("loc_D4A")

    label("loc_D45")

    SetChrFlags(0xB, 0x80)

    label("loc_D4A")

    Jump("loc_11DF")

    label("loc_D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DF5")
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xB, 3550, 0, -400, 90)
    SetChrPos(0xC, -280, 0, -260, 315)
    SetChrPos(0x9, -91140, 0, 3890, 315)
    SetChrPos(0x10, -88700, 0, -230, 90)
    SetChrPos(0x12, -92130, 0, 4890, 135)
    SetChrPos(0x11, -121580, 0, 1760, 90)
    SetChrChipByIndex(0x16, 0xF)
    BeginChrThread(0xC, 0, 0, 1)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x12, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF0")
    SetChrFlags(0x9, 0x10)

    label("loc_DF0")

    Jump("loc_11DF")

    label("loc_DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_EBB")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x9, 0x13)
    SetChrChipByIndex(0xF, 0xE)
    SetChrChipByIndex(0x10, 0x10)
    SetChrPos(0x9, -92130, 0, -3120, 270)
    SetChrPos(0xF, -88790, 0, 7470, 270)
    SetChrPos(0x10, -89930, 0, 7480, 0)
    SetChrPos(0x12, -125250, 0, -1380, 270)
    SetChrPos(0x11, -123430, 0, -2280, 180)
    SetChrPos(0xA, -87460, 0, -800, 0)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0xA, 0x10)
    Jump("loc_11DF")

    label("loc_EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_EFE")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -280, 0, -260, 315)
    BeginChrThread(0x14, 0, 0, 1)
    Jump("loc_11DF")

    label("loc_EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_F2F")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_11DF")

    label("loc_F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_F79")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0xA, -90560, 0, 490, 225)
    SetChrPos(0xB, 1360, 0, -1650, 180)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_11DF")

    label("loc_F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_FC2")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0xA, -87310, 0, -1980, 90)
    SetChrPos(0xB, 1360, 0, -1650, 180)
    SetChrFlags(0xA, 0x10)
    Jump("loc_11DF")

    label("loc_FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_100C")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0xA, -90560, 0, 490, 225)
    SetChrPos(0xB, 1360, 0, -1650, 180)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_11DF")

    label("loc_100C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_105D")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x9, -92130, 0, -3120, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1058")
    SetChrFlags(0x9, 0x10)

    label("loc_1058")

    Jump("loc_11DF")

    label("loc_105D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_10C2")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xB, 6970, 0, 5000, 270)
    SetChrPos(0x11, -90560, 0, 490, 225)
    SetChrPos(0xA, -124560, 0, -1610, 135)
    SetChrFlags(0xA, 0x10)
    BeginChrThread(0x11, 0, 0, 2)
    Jump("loc_11DF")

    label("loc_10C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_115B")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xB, -1160, 0, 130, 135)
    SetChrPos(0xC, 230, 0, -860, 315)
    SetChrPos(0x10, -124680, 0, 880, 225)
    SetChrPos(0x12, -123460, 0, -2280, 180)
    SetChrPos(0xA, -123410, 0, -980, 180)
    SetChrChipByIndex(0xF, 0xE)
    SetChrChipByIndex(0x12, 0x11)
    BeginChrThread(0x11, 0, 0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1156")
    SetChrFlags(0xA, 0x10)

    label("loc_1156")

    Jump("loc_11DF")

    label("loc_115B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_11DF")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x10, -88700, 0, -230, 90)
    SetChrPos(0x13, -90560, 0, 490, 225)
    SetChrPos(0xA, -124200, 0, 0, 180)
    SetChrPos(0x9, -124200, 0, -1330, 0)
    SetChrChipByIndex(0x16, 0xF)
    BeginChrThread(0x13, 0, 0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11CB")
    SetChrFlags(0x10, 0x10)

    label("loc_11CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11DA")
    SetChrFlags(0xA, 0x10)

    label("loc_11DA")

    Jump("loc_11DF")

    label("loc_11DF")

    Return()

    # Function_5_8F4 end

    def Function_6_11E0(): pass

    label("Function_6_11E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11F9")
    VolumeBGM(0x28, 0xC8)
    Jump("loc_122F")

    label("loc_11F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_121B")
    VolumeBGM(0x28, 0xC8)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x213), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_122F")

    label("loc_121B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_122F")
    VolumeBGM(0x32, 0x1F4)

    label("loc_122F")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_125C")
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x0, 0x1)
    Jump("loc_12A9")

    label("loc_125C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A9")
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0x7, 0x10)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 47500, 5650, 15300, 5000, 5000, 90000)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_12A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_12D1")
    SetMapObjFrame(0xFF, "pos01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pos02", 0x1, 0x1)
    Jump("loc_12EB")

    label("loc_12D1")

    SetMapObjFrame(0xFF, "pos01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "pos02", 0x0, 0x1)

    label("loc_12EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1304")
    OP_10(0x0, 0x0)
    OP_10(0x10, 0x1)
    Jump("loc_130A")

    label("loc_1304")

    OP_10(0x0, 0x1)
    OP_10(0x10, 0x0)

    label("loc_130A")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_131C")
    Jump("loc_13E8")

    label("loc_131C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1337")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_1332")
    OP_65(0x5, 0x1)

    label("loc_1332")

    Jump("loc_13E8")

    label("loc_1337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1349")
    OP_65(0x5, 0x1)
    Jump("loc_13E8")

    label("loc_1349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1369")
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_13E8")

    label("loc_1369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1377")
    Jump("loc_13E8")

    label("loc_1377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1389")
    OP_65(0x5, 0x1)
    Jump("loc_13E8")

    label("loc_1389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_13A9")
    OP_63(0xB, 0x0, 1900, 0x28, 0x2B, 0x64, 0x0)
    Jump("loc_13E8")

    label("loc_13A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_13B7")
    Jump("loc_13E8")

    label("loc_13B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_13C9")
    OP_65(0x5, 0x1)
    Jump("loc_13E8")

    label("loc_13C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_13DB")
    OP_66(0x4, 0x1)
    Jump("loc_13E8")

    label("loc_13DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_13E8")
    OP_65(0x5, 0x1)

    label("loc_13E8")

    OP_1B(0x3, 0xFF, 0xFFFF)
    OP_1B(0x4, 0xFF, 0xFFFF)
    OP_1B(0x0, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1419")
    OP_1B(0x3, 0x0, 0x55)
    OP_1B(0x4, 0x0, 0x54)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1447")
    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x3, 0x0, 0x55)

    label("loc_1447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1469")
    OP_1B(0x3, 0x0, 0x55)
    OP_1B(0x4, 0x0, 0x54)
    OP_1B(0x0, 0x0, 0x57)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1486")
    OP_1B(0x3, 0x0, 0x55)
    OP_1B(0x4, 0x0, 0x54)
    OP_1B(0x0, 0x0, 0x57)

    label("loc_1486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1499")
    OP_1B(0x0, 0x0, 0x57)

    label("loc_1499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14AC")
    OP_1B(0x0, 0x0, 0x57)

    label("loc_14AC")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14C4")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_14C4")

    SetMapObjFlags(0x1D, 0x4)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14E6")
    ClearMapObjFlags(0x1D, 0x4)
    OP_66(0x6, 0x1)

    label("loc_14E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14FE")
    ClearMapObjFlags(0x1D, 0x4)
    OP_66(0x6, 0x1)

    label("loc_14FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1516")
    ClearMapObjFlags(0x1D, 0x4)
    OP_66(0x6, 0x1)

    label("loc_1516")

    Return()

    # Function_6_11E0 end

    def Function_7_1517(): pass

    label("Function_7_1517")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_15F3")

    ChrTalk(
        0xD,
        (
            "We were able to finish the preparations\x01",
            "by adjusting the script and fiddling with\x01",
            "the order of character appearances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Nikolai returning right about now would\x01",
            "be the best-case scenario, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F6")

    label("loc_15F3")

    Call(0, 15)

    label("loc_15F6")

    TalkEnd(0xFE)
    Return()

    # Function_7_1517 end

    def Function_8_15FA(): pass

    label("Function_8_15FA")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1756")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_167E")

    ChrTalk(
        0xB,
        (
            "It truly seems as if Nikolai will not\x01",
            "be returning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Perhaps he was jealous of the\x01",
            "other actors?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1751")

    label("loc_167E")


    ChrTalk(
        0xB,
        (
            "It truly seems as if Nikolai will not\x01",
            "be returning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What a bind we're in. It's almost time\x01",
            "for the performance to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Do we have any options other than to\x01",
            "substitute him with another actor?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1751")

    Jump("loc_25C8")

    label("loc_1756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_17C2")

    ChrTalk(
        0xFE,
        (
            "We'll take care of the audience and\x01",
            "backstage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* I hope Nikolai returns to us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_25C8")

    label("loc_17C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_19CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17DD")
    Call(0, 10)
    Jump("loc_19CA")

    label("loc_17DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1965")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1872")

    ChrTalk(
        0xB,
        "Sully is intently watching Ilya practice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Her sense for the performing arts is\x01",
            "top-notch. She's going to be big.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1960")

    label("loc_1872")


    ChrTalk(
        0xB,
        (
            "I must try to have Sully give\x01",
            "the stage a shot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She's only an assistant at the moment,\x01",
            "but that's about to change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She's been studying Ilya's every move\x01",
            "during practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "That kid's going to be a star in the future.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1960")

    Jump("loc_19CA")

    label("loc_1965")


    ChrTalk(
        0xB,
        "We'll be performing in the afternoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We've got to do the cleaning while\x01",
            "we have the time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19CA")

    Jump("loc_25C8")

    label("loc_19CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19EA")
    Call(0, 10)
    Jump("loc_1B17")

    label("loc_19EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A7E")

    ChrTalk(
        0xB,
        "The nighttime performance will begin soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd like for our audience to be able to enjoy\x01",
            "the performance at their own pace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B17")

    label("loc_1A7E")


    ChrTalk(
        0xB,
        "Welcome to Arc en Ciel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The troupe will be performing\x01",
            "'Golden Sun, Silver Moon' tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I hope you all enjoy every last\x01",
            "second of it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B17")

    Jump("loc_25C8")

    label("loc_1B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1B67")

    ChrTalk(
        0xB,
        (
            "Up the stairs on the right! In the back!\x01",
            "Please, hurry!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C8")

    label("loc_1B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_1C66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B89")
    SetScenarioFlags(0x93, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BF0")

    ChrTalk(
        0xB,
        "The play is nearly over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Perhaps this evening will truly end\x01",
            "without incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C61")

    label("loc_1BF0")


    ChrTalk(
        0xB,
        "It has been an exciting performance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "More importantly, our guests appear\x01",
            "to be enjoying themselves.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1C61")

    Jump("loc_25C8")

    label("loc_1C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1E3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C88")
    SetScenarioFlags(0x93, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D4F")

    ChrTalk(
        0xB,
        (
            "We're in the second act of the play now...\x01",
            "Good, good. Everything is proceeding as\x01",
            "smoothly as we hoped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What a great success! I am ecstatic to\x01",
            "begin the public performances.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E37")

    label("loc_1D4F")


    ChrTalk(
        0xB,
        "Thank you for patrolling the premises.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We're in the second act of the play now...\x01",
            "Good, good. Everything is proceeding\x01",
            "as smoothly as we hoped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What a great success! I am ecstatic to\x01",
            "begin the public performances.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E37")

    Jump("loc_25C8")

    label("loc_1E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_1FDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5E")
    SetScenarioFlags(0x93, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F26")

    ChrTalk(
        0xB,
        (
            "I'll remain vigilant. However, our guest\x01",
            "list is entirely comprised of people\x01",
            "we've personally invited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Everything seems to be going smoothly.\x01",
            "Hopefully, we can relax for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FD8")

    label("loc_1F26")


    ChrTalk(
        0xB,
        "The performance has begun without incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Everything is going smoothly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No suspicious individuals have been spotted, either.\x01",
            "Hopefully, we can relax for now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1FD8")

    Jump("loc_25C8")

    label("loc_1FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_21E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_20C6")

    ChrTalk(
        0xB,
        (
            "They're currently inspecting the seats\x01",
            "on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Just a little while longer until the private\x01",
            "performance begins...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Not much we can do about it, though.\x01",
            "I'd rather be safe than sorry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E2")

    label("loc_20C6")


    ChrTalk(
        0xB,
        (
            "The First Division is currently\x01",
            "examining the theater.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Not only did they interrupt our practice,\x01",
            "but they've torn apart our dressing rooms...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*sigh* It's hard to keep calm at a time like this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Not much we can do about it, though.\x01",
            "I'd rather be safe than sorry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_21E2")

    Jump("loc_25C8")

    label("loc_21E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_237A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_228C")

    ChrTalk(
        0xB,
        (
            "We use the private performance as an opportunity\x01",
            "to announce our newest production to the public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Everything must proceed smoothly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2375")

    label("loc_228C")


    ChrTalk(
        0xB,
        (
            "I'm putting together a list of guests to\x01",
            "invite to the performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The list is filled with our sponsors,\x01",
            "so they're definitely interested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Every invitation must be specialized\x01",
            "for each and every one of our guests.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2375")

    Jump("loc_25C8")

    label("loc_237A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2429")

    ChrTalk(
        0xB,
        (
            "I truly appreciate the help you've\x01",
            "offered us today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It appears that the police will be protecting us\x01",
            "for now, so we shouldn't have to worry too much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C8")

    label("loc_2429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_24DA")

    ChrTalk(
        0xB,
        (
            "I don't want to bother our artists\x01",
            "with this matter while they're\x01",
            "practicing for the performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Good luck with the investigation.\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C8")

    label("loc_24DA")


    ChrTalk(
        0xB,
        (
            "We've treated the occasional threats we've\x01",
            "received as pranks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, the letter's contents, along with that\x01",
            "signature, give credence to its legitimacy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm counting on you, everyone.\x01",
            "Please get to the bottom of this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_25C8")

    TalkEnd(0xB)
    Return()

    # Function_8_15FA end

    def Function_9_25CC(): pass

    label("Function_9_25CC")

    Call(0, 8)
    Return()

    # Function_9_25CC end

    def Function_10_25D0(): pass

    label("Function_10_25D0")


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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2743")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26B3")

    ChrTalk(
        0x102,
        (
            "#0100FIt looks like she's managing\x01",
            "to handle herself just fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_26B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26F9")

    ChrTalk(
        0x103,
        (
            "#0200FShe appears to be operating\x01",
            "smoothly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_26F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2743")

    ChrTalk(
        0x104,
        "#0300FHeh. Looks like she's doin' a swell job to me.\x02",
    )

    CloseMessageWindow()

    label("loc_2743")

    SetScenarioFlags(0xD1, 6)
    Return()

    # Function_10_25D0 end

    def Function_11_2747(): pass

    label("Function_11_2747")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2909")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2869")

    ChrTalk(
        0xC,
        (
            "They refuse to compromise, no matter the\x01",
            "emergency they find themselves in.\x02\x03",
            "Ugh, how worrying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Today's performance will be delayed\x01",
            "to the evening, so I'm notifying the\x01",
            "appropriate parties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I apologize profusely for having caused\x01",
            "trouble for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2904")

    label("loc_2869")


    ChrTalk(
        0xC,
        (
            "H-Have Ilya and the troupe leader\x01",
            "come to agreeable terms yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "They've been going on and on about the\x01",
            "scenario. This isn't the time for it...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2904")

    Jump("loc_3B93")

    label("loc_2909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_29B7")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xC,
        "I understand. I'll handle the main hall.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'll have to inform Sully as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "She does a great job of noticing the\x01",
            "finer details.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_2B68")

    label("loc_29B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A41")

    ChrTalk(
        0xC,
        (
            "Do you have the time to visit the\x01",
            "auditorium?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'd like for you to consult with the\x01",
            "troupe leader, if that's okay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B68")

    label("loc_2A41")


    ChrTalk(
        0xC,
        (
            "I seem to recall you being police officers,\x01",
            "am I correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FY-Yes, you are...\x01",
            "(Is something going on?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sorry to bother you, but do you have time\x01",
            "to visit the auditorium?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The troupe leader's got himself into\x01",
            "a bit of a sticky situation, so we'd\x01",
            "appreciate some advice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2B68")

    Jump("loc_3B93")

    label("loc_2B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2CF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B88")
    Call(0, 13)
    Jump("loc_2CEB")

    label("loc_2B88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C10")

    ChrTalk(
        0xC,
        (
            "I'm surprised how passionate artists\x01",
            "like Rixia or Ilya can be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The rest of us staff members better\x01",
            "step it up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CEB")

    label("loc_2C10")


    ChrTalk(
        0xC,
        (
            "An artist by the name of Nikolai\x01",
            "works for us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've noticed that he's been training\x01",
            "as hard as he can these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I must say, his enthusiasm is impressive.\x01",
            "He pulled an all-nighter just to practice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2CEB")

    Jump("loc_3B93")

    label("loc_2CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_2E19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D0B")
    Call(0, 13)
    Jump("loc_2E14")

    label("loc_2D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D86")

    ChrTalk(
        0xC,
        "Ten more minutes until the performance starts...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'd love for all of our guests to enjoy the show.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E14")

    label("loc_2D86")


    ChrTalk(
        0xC,
        (
            "Welcome. Please allow me to\x01",
            "examine your tickets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you came to purchase, do note that\x01",
            "our normal seats are currently sold out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2E14")

    Jump("loc_3B93")

    label("loc_2E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_303F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E34")
    Call(0, 13)
    Jump("loc_303A")

    label("loc_2E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2EC2")

    ChrTalk(
        0xC,
        (
            "We're closed today, but some of the\x01",
            "performers came in for a voluntary\x01",
            "practice session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Would you like to meet them?\x02",
    )

    CloseMessageWindow()
    Jump("loc_303A")

    label("loc_2EC2")


    ChrTalk(
        0xC,
        "Everybody seems to enjoy the new production.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "All of our showings have had nearly full\x01",
            "attendance, and tickets for the next two\x01",
            "months have completely sold out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We're not open today, so naturally, there\x01",
            "won't be a performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FMakes perfect sense to me.\x02\x03",
            "#0003F(I've got KeA with me today. Loitering around\x01",
            "Arc en Ciel probably isn't a good idea.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_303A")

    Jump("loc_3B93")

    label("loc_303F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_3092")

    ChrTalk(
        0xC,
        "Huh? A suspicious attendee?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Y-You've got to be kidding me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B93")

    label("loc_3092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_31C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B4")
    SetScenarioFlags(0x93, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3137")

    ChrTalk(
        0xC,
        "I haven't noticed anything strange...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Have they given up? The First Division\x01",
            "is on the lookout, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BC")

    label("loc_3137")


    ChrTalk(
        0xC,
        "I haven't noticed anything strange here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No one has been allowed to enter through\x01",
            "the front doors since the play began.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_31BC")

    Jump("loc_3B93")

    label("loc_31C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3328")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31E3")
    SetScenarioFlags(0x93, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3278")

    ChrTalk(
        0xC,
        "This play is Rixia's debut.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I feel like I can share her anxiety.\x01",
            "Must be from all the time I spent\x01",
            "with her during practice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3323")

    label("loc_3278")


    ChrTalk(
        0xC,
        (
            "We've finally made it to the second act...\x01",
            "It's time for Rixia's debut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm sure she'll be fine. I trust Ilya's\x01",
            "keen senses to scout talent when\x01",
            "she sees it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3323")

    Jump("loc_3B93")

    label("loc_3328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_33BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_334A")
    SetScenarioFlags(0x93, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_334A")


    ChrTalk(
        0xC,
        "It sounds like the performance has begun...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I would greatly appreciate it\x01",
            "if nothing were to happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B93")

    label("loc_33BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_351B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3454")

    ChrTalk(
        0xC,
        (
            "The First Division has been keeping a\x01",
            "watchful eye for us all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "*sigh* Today's practice is running\x01",
            "a little late.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3516")

    label("loc_3454")


    ChrTalk(
        0xC,
        (
            "The First Division has been keeping a\x01",
            "watchful eye for us all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "None of the troupe members seem\x01",
            "to care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Practice is running a little late today,\x01",
            "thanks to the questioning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3516")

    Jump("loc_3B93")

    label("loc_351B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3607")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_35B1")

    ChrTalk(
        0xC,
        (
            "We've got a business meeting regarding\x01",
            "the announcement of the new production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "It's about to get hectic around here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3602")

    label("loc_35B1")


    ChrTalk(
        0xC,
        "Thanks for helping us out, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Do take care on your way home.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3602")

    Jump("loc_3B93")

    label("loc_3607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_36B7")

    ChrTalk(
        0xC,
        (
            "Oh? Do you wish to speak with Ilya or\x01",
            "the troupe leader?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You may proceed. They should be\x01",
            "practicing in the main hall. They've\x01",
            "been at it since morning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B93")

    label("loc_36B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_396B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_37D6")

    ChrTalk(
        0xC,
        (
            "This is the fifth leading role that the\x01",
            "Fervent Dancer, Ilya Platiere, is\x01",
            "performing in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Quite frankly, I'm a huge fan of hers.\x01",
            "She's the reason I'm working here\x01",
            "in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Actually, the same could be said about\x01",
            "a lot of our staff members.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3966")

    label("loc_37D6")


    ChrTalk(
        0xC,
        (
            "Arc en Ciel rolls out a new production\x01",
            "once a year on average, but that\x01",
            "isn't always the case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Some of the productions have taken\x01",
            "a year and a half to perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That's why there was a bit of an uproar\x01",
            "at the most recent announcement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This is the fifth leading role that the\x01",
            "Fervent Dancer, Ilya Platiere, is\x01",
            "performing in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, I definitely understand all\x01",
            "the hullabaloo.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3966")

    Jump("loc_3B93")

    label("loc_396B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_END)), "loc_3B55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3A2D")

    ChrTalk(
        0xC,
        (
            "This is a nightmare. Who'd have the\x01",
            "audacity to send a threat letter at a\x01",
            "time like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hope we quickly determine that this\x01",
            "is nothing more than a bad joke.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B50")

    label("loc_3A2D")


    ChrTalk(
        0xC,
        (
            "This is a nightmare. Who'd have the\x01",
            "audacity to send a threat letter at a\x01",
            "time like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hope we quickly determine that this\x01",
            "is nothing more than a bad joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I was asked to support you\x01",
            "in any way I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please don't hesitate to ask me\x01",
            "any questions you might have.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3B50")

    Jump("loc_3B93")

    label("loc_3B55")


    ChrTalk(
        0xC,
        "Welcome to Arc en Ciel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Please proceed to the hall.\x02",
    )

    CloseMessageWindow()

    label("loc_3B93")

    TalkEnd(0xC)
    Return()

    # Function_11_2747 end

    def Function_12_3B97(): pass

    label("Function_12_3B97")

    Call(0, 11)
    Return()

    # Function_12_3B97 end

    def Function_13_3B9B(): pass

    label("Function_13_3B9B")


    ChrTalk(
        0xC,
        (
            "A girl by the name of Sully joined\x01",
            "our troupe recently. She's quite\x01",
            "the hard worker, if I must say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "She's quick to catch on, and\x01",
            "best of all, she's proactive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "She's been an amazing help to the staff,\x01",
            "but I don't think she has any intention\x01",
            "of becoming an artist.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 7)
    Return()

    # Function_13_3B9B end

    def Function_14_3CB5(): pass

    label("Function_14_3CB5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3DCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3DC4")

    ChrTalk(
        0x8,
        (
            "#1703FNow that the show's been postponed\x01",
            "until 4PM, we'd better start busting\x01",
            "our humps perfecting this thing.\x02\x03",
            "#1700FWell, whatever. We're all pros here...\x01",
            "I'm sure we'll manage.\x02\x03",
            "#1709FOne more time from the top!\x01",
            "Heck yes, let's do this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC7")

    label("loc_3DC4")

    Call(0, 15)

    label("loc_3DC7")

    Jump("loc_4044")

    label("loc_3DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3E6C")

    ChrTalk(
        0x8,
        (
            "#1706FKarelia's been totally nagging at me\x01",
            "for a while now. Sheesh.\x02\x03",
            "#1700FIt's cool, though. I promise I'm not\x01",
            "going to delay our practice!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4044")

    label("loc_3E6C")


    ChrTalk(
        0x8,
        (
            "#1706F*yaaaaaaawn*...\x02\x03",
            "#1705FOh, my favorite little guy and his friends\x01",
            "have entered the scene. Morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FY-You look like you just woke up, Ilya.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1706FYeah, kinda. May have slept in a\x01",
            "bit too much this morning.\x02\x03",
            "#1700FNot to worry, my friends. I won't\x01",
            "fall behind 'cause of this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FWell, if you say so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301F(Oh, man. Can't believe we're gettin'\x01",
            "a glimpse of Ilya's personal life.)\x02\x03",
            "#0309F(I feel like a million mira right now!)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4044")

    TalkEnd(0xFE)
    Return()

    # Function_14_3CB5 end

    def Function_15_4048(): pass

    label("Function_15_4048")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "My goodness. We finally came to an\x01",
            "agreement on the scenario changes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You were being far too stubborn, so it\x01",
            "took forever for us to lock anything down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1706F#11PYeah, well, I don't wanna tone this\x01",
            "scene down at all!\x02\x03",
            "#1702FI've been busting my hump on this\x01",
            "scene, so what'd ya expect?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "And like I said...you're being as\x01",
            "stubborn as a mule!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'd say we lucked out, considering we\x01",
            "only have the daytime performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We don't have any time to waste,\x01",
            "so let's begin rehearsal immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1709F#11PYup, I'm on it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202F(A tense situation... I am glad they\x01",
            "have come to an agreement.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_15_4048 end

    def Function_16_42D4(): pass

    label("Function_16_42D4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4368")
    Jump("loc_43B2")

    label("loc_4368")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4388")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43B2")

    label("loc_4388")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43A8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43B2")

    label("loc_43A8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_43B2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4480")

    ChrTalk(
        0x15,
        (
            "#6102FI'm going to focus on getting my steps down\x01",
            "a little more cleanly for that scene.\x02\x03",
            "#6109FAll right, let's do this! It's time to kick some butt!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_465B")

    label("loc_4480")


    ChrTalk(
        0x15,
        "#6105FOh, it's Cecile's little brother and his friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FGood evening, Ilya. How are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0302FWe all gettin' ready to perform now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#6104FYep, you bet'cha. The attendees are\x01",
            "bound to arrive soon.\x02\x03",
            "#6102FI think I'll focus on getting my steps down\x01",
            "a little more cleanly for this scene.\x02\x03",
            "#6109FAll right, let's do this! It's time to kick some butt!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0109F(She's as motivated as ever.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0204F(Right... It is a strangely reassuring sight.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_465B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_42D4 end

    def Function_17_4663(): pass

    label("Function_17_4663")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_47B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_END)), "loc_47A9")

    ChrTalk(
        0x9,
        (
            "#1802FApparently, Nikolai's been engaged in some\x01",
            "special training... I could tell. His stamina\x01",
            "has improved considerably.\x02\x03",
            "#1806FIt's a remarkable idea, honestly. Although...\x01",
            "I feel as if his personality has changed.\x02\x03",
            "#1808FI'm a little bit worried. He doesn't seem\x01",
            "like his usual self anymore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47AC")

    label("loc_47A9")

    Call(0, 18)

    label("loc_47AC")

    Jump("loc_5147")

    label("loc_47B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_49B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4884")

    ChrTalk(
        0x9,
        (
            "#6202FI think I'm finally getting the hang of controlling\x01",
            "my nerves in front of a large crowd.\x02\x03",
            "#6209FI've still got a long way to go before\x01",
            "I can consider myself to be Ilya's equal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49AB")

    label("loc_4884")


    ChrTalk(
        0x9,
        (
            "#6202FOh, you're here!\x02\x03",
            "Are you here to watch the show\x01",
            "by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FI wish, but sadly not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102FWe had business to attend to nearby,\x01",
            "so we figured we'd drop by and say hi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6209FI see. I appreciate you visiting us. Thanks\x01",
            "for working so late to keep us all safe!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_49AB")

    Jump("loc_5147")

    label("loc_49B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4C7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 4)), scpexpr(EXPR_END)), "loc_4A96")

    ChrTalk(
        0x9,
        (
            "#1802FWe'll be applying the finishing touches to\x01",
            "the performance starting tomorrow.\x02\x03",
            "#1804FNot only that, but we'll have to rehearse\x01",
            "every day... I must focus and put\x01",
            "everything I have into practicing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C75")

    label("loc_4A96")


    ChrTalk(
        0x9,
        "#1803F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FIs something the matter, Rixia?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 750)

    ChrTalk(
        0x9,
        (
            "#1805FOh, no. It's nothing.\x02\x03",
            "#1806FI'm just feeling a little anxious with the\x01",
            "private performance drawing near.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FOh, yeah. Isn't that thing a week from now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1802FYes, we'll be applying the finishing touches\x01",
            "to the performance starting tomorrow.\x02\x03",
            "#1804FI must focus and put everything I have\x01",
            "into practicing.\x02\x03",
            "#1808FI don't want to fall behind and become\x01",
            "a burden to the others.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x91, 4)

    label("loc_4C75")

    Jump("loc_5147")

    label("loc_4C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 3)), scpexpr(EXPR_END)), "loc_4D92")

    ChrTalk(
        0x9,
        (
            "#1806FTo be honest, I don't have any confidence\x01",
            "that I'll perform well...\x02\x03",
            "#1802F...but Ilya's been reassuring me of my\x01",
            "talent. I think I'll believe in her faith\x01",
            "in me.\x02\x03",
            "#1804FI don't have as much practice as the others,\x01",
            "so I feel as if I'm in the way, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5147")

    label("loc_4D92")


    ChrTalk(
        0x9,
        (
            "#1805FOh... Hi, everyone.\x02\x03",
            "#1806FSorry for the ruckus. I'm getting ready\x01",
            "to practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FHaha. You're looking as busy as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0302FWhaddaya expect, man? She's a risin' star!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1809FAhahaha...\x02\x03",
            "#1810FI...actually had no intention of joining\x01",
            "the troupe originally.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0105FOh, really? Why the change of heart?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1802FWell, I've always wanted to watch one\x01",
            "of Arc en Ciel's famous performances.\x02\x03",
            "#1806FI came to watch one of their public\x01",
            "practice sessions when Ilya laid\x01",
            "her eyes upon me.\x02\x03",
            "She came up to me and exclaimed,\x01",
            "'I can feel the talent oozing from you!'\x01",
            "One thing led to another, and here we are...\x02",
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
        "#0206FI can clearly visualize the event in my mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FHaha, that definitely sounds like Ilya.\x01",
            "She can get pushy at times.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 3)

    label("loc_5147")

    TalkEnd(0xFE)
    Return()

    # Function_17_4663 end

    def Function_18_514B(): pass

    label("Function_18_514B")

    OP_4B(0x9, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x9,
        (
            "#1806FHey, Plie. Doesn't Nikolai seem a little\x01",
            "bit...different, lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Oh, you noticed it, too? I've been getting\x01",
            "some weird vibes from him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "It's as if he's a completely different person.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1808F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FExcuse me, is everything okay?\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x0, 750)
    TurnDirection(0x12, 0x0, 750)
    Sleep(750)

    ChrTalk(
        0x12,
        "Oh, the police officers have arrived.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "It's nothing serious. We were just\x01",
            "conversing about Nikolai.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1806FRight, apparently, Nikolai's been engaged\x01",
            "in some special training lately.\x02\x03",
            "It's paying off, too. His technique and\x01",
            "strength have improved considerably.\x02\x03",
            "#1808FThe strange thing is, his personality\x01",
            "seems to have changed as a result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FHuh? Ya think his personality's gone\x01",
            "haywire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FWell, I suppose it's possible...\x02\x03",
            "#0100FHow often do people completely change\x01",
            "overnight, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1804FI wonder about that. I think people can\x01",
            "change as long as they are motivated to\x01",
            "do so, however.\x02\x03",
            "#1810FI'm sure Nikolai must have had a life-changing\x01",
            "experience like that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x12, 0)
    TurnDirection(0x12, 0x9, 0)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0xCE, 3)
    OP_4C(0x9, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_18_514B end

    def Function_19_5569(): pass

    label("Function_19_5569")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_562D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5625")

    ChrTalk(
        0xF,
        (
            "Why must I, who plays the role of the prince,\x01",
            "play a filthy beggar alongside it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Ughhhh... This is too depressing.\x01",
            "I mustn't think about it any longer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5628")

    label("loc_5625")

    Call(0, 20)

    label("loc_5628")

    Jump("loc_5B5D")

    label("loc_562D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_57C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_56C9")

    ChrTalk(
        0xF,
        (
            "Our dear friend Nikolai has been\x01",
            "fervently training as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I must say, I thought he was improving\x01",
            "splendidly already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57C3")

    label("loc_56C9")


    ChrTalk(
        0xF,
        (
            "I hear our dear friend Nikolai has been\x01",
            "training late into the night recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I do believe his sudden surge of confidence\x01",
            "struck me as a little strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Damn it, Nikolai! You must notify your\x01",
            "colleagues before you vamoose as such!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_57C3")

    Jump("loc_5B5D")

    label("loc_57C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_591C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5843")

    ChrTalk(
        0xF,
        (
            "I do say, Nikolai has become strikingly different.\x01",
            "I suppose he has been training his hardest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5917")

    label("loc_5843")


    ChrTalk(
        0xF,
        (
            "Don't you think that Nikolai has\x01",
            "dramatically improved?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "He used to hesitate far more, but it's almost\x01",
            "as if he's become a different person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*sigh* Perhaps he has managed to\x01",
            "make a breakthrough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5917")

    Jump("loc_5B5D")

    label("loc_591C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_59F0")

    ChrTalk(
        0xF,
        (
            "Now that our focus is on rehearsing the\x01",
            "newest play, regular performances\x01",
            "have ceased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I must be careful, lest this costume\x01",
            "become an absolute wreck prior\x01",
            "to the debut of our performance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B5D")

    label("loc_59F0")


    ChrTalk(
        0xF,
        "Don't I look simply dashing in this prince outfit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Hah. 'Tis no surprise that yours truly has taken\x01",
            "the role of the prince in our new play,\x01",
            "'Golden Sun, Silver Moon.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "However, I must exercise caution.\x01",
            "Otherwise, this outfit will be in tatters\x01",
            "before the performance debuts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "What can I say? The glorious Arc en Ciel's\x01",
            "dances can be...intense.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5B5D")

    TalkEnd(0xFE)
    Return()

    # Function_19_5569 end

    def Function_20_5B61(): pass

    label("Function_20_5B61")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xF,
        (
            "What in blazes?! Why has my\x01",
            "part become shorter?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Huh. My part's a little longer now...\x01",
            "I figure they're doing it to buy time\x01",
            "for the artists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "So, I'm to use that time to transform\x01",
            "into a beggar?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "...\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        "Are they for true?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 4)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_20_5B61 end

    def Function_21_5C89(): pass

    label("Function_21_5C89")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D1D")
    Jump("loc_5D67")

    label("loc_5D1D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5D3D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D67")

    label("loc_5D3D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D5D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D67")

    label("loc_5D5D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D67")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5E24")
    OP_4B(0x10, 0xFF)
    SetChrSubChip(0x16, 0x0)

    ChrTalk(
        0x16,
        (
            "Hmm... Nikolai was partaking in some\x01",
            "rather...ostentatious acrobatics yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Has he always been such a peacock?\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    Jump("loc_6108")

    label("loc_5E24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5F39")
    OP_4B(0x10, 0xFF)
    SetChrSubChip(0x16, 0x0)

    ChrTalk(
        0x16,
        (
            "A-ha! I see, I see! Our fellow friend\x01",
            "lacks self-confidence, does he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "This is his acknowledgment of my skills,\x01",
            "is it not? I am indeed the best artist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "*sigh* Has anybody ever told you that\x01",
            "you sound like a pompous ass, Eugene?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    Jump("loc_5F3C")

    label("loc_5F39")

    Call(0, 22)

    label("loc_5F3C")

    Jump("loc_6108")

    label("loc_5F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6023")

    ChrTalk(
        0x16,
        (
            "A threat letter? No matter. Such trivialities\x01",
            "are commonplace for stars. I've received\x01",
            "many myself, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Hahaha. As the Prince of Arc en Ciel,\x01",
            "I, Eugene, have made enemies of\x01",
            "men across the land.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6108")

    label("loc_6023")


    ChrTalk(
        0x16,
        "Oh, police officers, are we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Hah. Must be cumbersome to investigate\x01",
            "the smallest of pranks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "A threat letter? No matter. Such trivialities\x01",
            "are commonplace for stars. Rest assured,\x01",
            "your investigation is unneeded.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6108")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_5C89 end

    def Function_22_6110(): pass

    label("Function_22_6110")

    OP_4B(0x10, 0xFF)
    SetChrSubChip(0x16, 0x0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Theodor is styling Eugene's hair.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x16,
        (
            "Theodor, what say you we have ourselves\x01",
            "a friendly gentleman's wager?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "With whom will the fair maidens in attendance\x01",
            "fall in love? You, or me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "As for the deciding factor... Oh, I know.\x01",
            "Why not count the number of love\x01",
            "letters we receive the following week?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "...*pinch*\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_A6(0x16, 0x0, 0x14, 0x258, 0xBB8)
    Sleep(500)

    ChrTalk(
        0x16,
        "Ouch! Stop! That hurts!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Pardon me, my dear stylist. What the\x01",
            "hell do you think you're doing?!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x16)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x0, 4)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_22_6110 end

    def Function_23_6318(): pass

    label("Function_23_6318")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_63A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_639E")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x10,
        "We need to do another quick rehearsal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Pick up your script and quit your\x01",
            "moaning, Eugene!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    Jump("loc_63A1")

    label("loc_639E")

    Call(0, 20)

    label("loc_63A1")

    Jump("loc_6827")

    label("loc_63A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_64B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6410")

    ChrTalk(
        0xFE,
        (
            "We've got today's performance to deal with,\x01",
            "but I'm not sure how it'll end...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64AB")

    label("loc_6410")


    ChrTalk(
        0x10,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Incidents like this tend to affect the troupe's\x01",
            "morale and put them in weak spirits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "I'm worried it'll show through the performance.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_64AB")

    Jump("loc_6827")

    label("loc_64B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_64EF")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x10,
        "...I have a bad feeling about this.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    Jump("loc_6827")

    label("loc_64EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_654A")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x10,
        "Shut your trap, Eugene!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "You're disturbing my reading time!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    Jump("loc_6827")

    label("loc_654A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_65F8")

    ChrTalk(
        0x10,
        (
            "There's really nothing better than\x01",
            "reading a good book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Books help nourish the soul. I'd recommend\x01",
            "reading as much as you can when you\x01",
            "have the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6827")

    label("loc_65F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_667D")

    ChrTalk(
        0x10,
        "You guys forget something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Are you looking for the troupe leader?\x01",
            "I'm pretty sure he's out in the main hall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6827")

    label("loc_667D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6705")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_66FD")

    ChrTalk(
        0x10,
        "Do you need something from Rixia?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Try checking out the dressing rooms,\x01",
            "I think she's in there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6700")

    label("loc_66FD")

    Call(0, 22)

    label("loc_6700")

    Jump("loc_6827")

    label("loc_6705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6798")

    ChrTalk(
        0x10,
        (
            "Please don't bother me. I'm trying\x01",
            "to prepare for my part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Are you here merely to make noise?\x01",
            "Feel free to make your exit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6827")

    label("loc_6798")


    ChrTalk(
        0x10,
        "I see some faces I don't recognize.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Well, whatever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Please be mindful of any noise when\x01",
            "you're in an artist's dressing room.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6827")

    TalkEnd(0xFE)
    Return()

    # Function_23_6318 end

    def Function_24_682B(): pass

    label("Function_24_682B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_69AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_68CD")

    ChrTalk(
        0x12,
        "Still no sign of Nikolai.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "It's a darn shame. But, like the troupe\x01",
            "leader said, we have to set aside\x01",
            "our feelings and move on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69A7")

    label("loc_68CD")


    ChrTalk(
        0x12,
        (
            "I just got the new script with all of the\x01",
            "adjustments implemented.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "All I've gotta say is...ouch. Eugene's\x01",
            "going to have a hard time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Anyway, I should probably inform\x01",
            "Rixia and Selene that it's ready.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_69A7")

    Jump("loc_732E")

    label("loc_69AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6AB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_END)), "loc_6AB1")
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x12,
        (
            "You know, I do seem to remember him\x01",
            "disappearing for a while after the\x01",
            "festival ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "It's entirely possible that something may\x01",
            "have happened then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1801FThat may be true, but he hardly ever\x01",
            "says anything to us...\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_6AB4")

    label("loc_6AB1")

    Call(0, 18)

    label("loc_6AB4")

    Jump("loc_732E")

    label("loc_6AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_6B3B")

    ChrTalk(
        0x12,
        "Look at Nikolai building up some confidence, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I was pretty worried there. He was in a rut\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_732E")

    label("loc_6B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6C9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6BC8")

    ChrTalk(
        0x12,
        (
            "I'm pretty sure Ilya's talent is\x01",
            "inherent for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I remember her being great even back\x01",
            "in her rookie days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C99")

    label("loc_6BC8")


    ChrTalk(
        0x12,
        (
            "Oh, Ilya. Why'd you have to sleep in\x01",
            "on a day like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Heh. Some things just never change...\x01",
            "Reminds me of her rookie days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "The police detectives didn't seem too\x01",
            "thrilled with her, either.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_6C99")

    Jump("loc_732E")

    label("loc_6C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_6D85")

    ChrTalk(
        0x12,
        "*chew* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I can't believe they forbade us from\x01",
            "eating or drinking during practice, even\x01",
            "if we're hiding in the dressing rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "If I'm going to chow down on this midday snack,\x01",
            "it's now or never! ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_732E")

    label("loc_6D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6F67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6E46")

    ChrTalk(
        0x12,
        "Our troupe leader is a truly capable man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Poor guy, though. He's been having to\x01",
            "keep up with Ilya's demands lately.\x01",
            "You can tell he can hardly deal with it. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F62")

    label("loc_6E46")


    ChrTalk(
        0x12,
        (
            "Our troupe leader doesn't seem\x01",
            "exactly...impressionable, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "You'd be surprised, though! He's actually\x01",
            "well versed in the fine arts. He's our\x01",
            "scenario and stage director.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I don't think it'd be a stretch to credit\x01",
            "Arc en Ciel's popularity entirely\x01",
            "to his efforts.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_6F62")

    Jump("loc_732E")

    label("loc_6F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 5)), scpexpr(EXPR_END)), "loc_70D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6FF0")

    ChrTalk(
        0x12,
        (
            "Rixia's development has been coming\x01",
            "along quite nicely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "I'm looking forward to seeing how she blossoms.\x02",
    )

    CloseMessageWindow()
    Jump("loc_70D4")

    label("loc_6FF0")


    ChrTalk(
        0x12,
        (
            "Ilya and I are not the only ones to reach\x01",
            "stardom in the troupe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Theodor and Eugene are quite popular,\x01",
            "especially with the ladies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "What can I say? The artists of Arc en Ciel\x01",
            "are a force to be reckoned with. ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_70D4")

    Jump("loc_732E")

    label("loc_70D9")


    ChrTalk(
        0x104,
        (
            "#0305FWhoa... Aren't you Plie?\x02\x03",
            "#0309FNo way, you totally are! You're Plie,\x01",
            "the Mysterious Songstress! I know\x01",
            "all about your fantasias.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "A fan, are we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "My apologies for presenting myself in\x01",
            "this unflattering training attire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FNot at all. I don't mind one bit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "You may not mind, but I most certainly do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Also, you seem to have forgotten, but\x01",
            "we're in a dressing room.\x01",
            "KEEP IT DOWN! Okay? ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYes, ma'am! Sorry, ma'am!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#0211F(Your motives are far too transparent,\x01",
            "Randy.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 5)

    label("loc_732E")

    TalkEnd(0xFE)
    Return()

    # Function_24_682B end

    def Function_25_7332(): pass

    label("Function_25_7332")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_7464")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_73B6")

    ChrTalk(
        0x13,
        (
            "Rixia's always forgetting her\x01",
            "stuff at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "That girl's missing a few screws,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_745F")

    label("loc_73B6")


    ChrTalk(
        0x13,
        (
            "Rixia Isn't here right now... She had\x01",
            "to go home and retrieve a few things\x01",
            "she forgot to bring with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "That girl's missing a few screws,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_745F")

    Jump("loc_79D6")

    label("loc_7464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_75CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_7505")

    ChrTalk(
        0x13,
        (
            "I was aware of Nikolai's condition, and yet\x01",
            "I turned a blind eye to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I...think I may have treated him a little\x01",
            "too cruelly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75C9")

    label("loc_7505")


    ChrTalk(
        0x13,
        (
            "...Nikolai's been acting a little strangely\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Even though I was aware of it, I\x01",
            "turned a blind eye to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I wasn't expecting it to take a\x01",
            "turn for the worse like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_75C9")

    Jump("loc_79D6")

    label("loc_75CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_775C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_7671")

    ChrTalk(
        0x13,
        (
            "I dream of the day that Ilya\x01",
            "recognizes my talents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Rixia may have surpassed me for now,\x01",
            "but I'm not about to take it lying down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7757")

    label("loc_7671")


    ChrTalk(
        0x13,
        (
            "The entire reason I auditioned for this\x01",
            "troupe was because I admire Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Rixia may have gotten a leg up on me,\x01",
            "but I'm not about to take it lying down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I'm going to train even harder\x01",
            "and pay her back the favor!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_7757")

    Jump("loc_79D6")

    label("loc_775C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_782C")

    ChrTalk(
        0x13,
        (
            "Look at the role Rixia managed to score... I guess\x01",
            "her talent really does speak for itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Well, she'd better knock her performance out\x01",
            "of the park, or else I'll be furious with her!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79D6")

    label("loc_782C")


    ChrTalk(
        0x13,
        (
            "Rixia's still a total rookie. She only\x01",
            "recently joined Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "It only makes her recent casting as the\x01",
            "co-star of our upcoming production that\x01",
            "much more impressive.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x13)

    ChrTalk(
        0x13,
        (
            "Well, I suppose I can't bellyache much.\x01",
            "She's been training her butt off from\x01",
            "the day she joined us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I've been here longer than her, yet she\x01",
            "managed to surpass me. I'll be so mad\x01",
            "at her if she screws this up!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_79D6")

    TalkEnd(0xFE)
    Return()

    # Function_25_7332 end

    def Function_26_79DA(): pass

    label("Function_26_79DA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7A6E")
    Jump("loc_7AB8")

    label("loc_7A6E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A8E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7AB8")

    label("loc_7A8E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7AAE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7AB8")

    label("loc_7AAE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7AB8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7EC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_7BA5")

    ChrTalk(
        0x17,
        (
            "I sometimes notice Rixia wearing a\x01",
            "nervous expression when she's all\x01",
            "alone. It's like she has no confidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I've gotta be honest with you, it\x01",
            "irritates me to no end.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EC4")

    label("loc_7BA5")


    ChrTalk(
        0x17,
        (
            "I sometimes notice Rixia wearing a\x01",
            "nervous expression when she's all\x01",
            "alone. It's like she has no confidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Seriously, girl. You're a natural pro\x01",
            "selected by Ilya herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Why the long face?! You've gotta\x01",
            "have some confidence in yourself,\x01",
            "girl!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D15")

    ChrTalk(
        0x101,
        (
            "#0006FI get where you're coming from, but\x01",
            "wouldn't it make more sense to tell her?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E38")

    label("loc_7D15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D69")

    ChrTalk(
        0x102,
        (
            "#0106FI believe you'd be better off telling\x01",
            "her personally.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E38")

    label("loc_7D69")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DD4")

    ChrTalk(
        0x103,
        (
            "#0206FWould it not be more logical to tell the\x01",
            "intended recipient, rather than us?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E38")

    label("loc_7DD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E38")

    ChrTalk(
        0x104,
        (
            "#0306FWhat are ya tellin' us for? Don't you\x01",
            "think she needs to hear those words?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E38")

    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0x17,
        "N-No way...\x02",
    )

    CloseMessageWindow()
    OP_64(0x17)

    ChrTalk(
        0x17,
        (
            "Ahem! I'm supposed to be her super\x01",
            "strict mentor, so there's no way I\x01",
            "could tell her that!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_7EC4")

    Jump("loc_8063")

    label("loc_7EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7FB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_7F4C")

    ChrTalk(
        0x17,
        (
            "Grr... I haven't gotten any practice in,\x01",
            "thanks to these police officers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "*sigh* What a bummer...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FB2")

    label("loc_7F4C")


    ChrTalk(
        0x17,
        (
            "That threat letter might actually\x01",
            "be the real deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "I've got a bad feeling about this...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_7FB2")

    Jump("loc_8063")

    label("loc_7FB7")


    ChrTalk(
        0x17,
        (
            "Apparently, my parents are coming to watch\x01",
            "our newest production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Better brush up on those skills. Wouldn't\x01",
            "wanna embarrass myself in front of them,\x01",
            "now would I?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8063")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_79DA end

    def Function_27_806B(): pass

    label("Function_27_806B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_817C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8100")

    ChrTalk(
        0x11,
        "Everybody watching me was shocked...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hahaha! I can't get enough of this feeling!\x01",
            "Serves all you naysayers right!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8177")

    label("loc_8100")


    ChrTalk(
        0x11,
        "Hahaha! Another perfect rehearsal!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I feel like I'm in perfect form...\x01",
            "I bet I could even take Rixia down!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_8177")

    Jump("loc_8478")

    label("loc_817C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_8266")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8214")

    ChrTalk(
        0x11,
        "Nobody's ever going to walk all over me again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I'm confident I train way harder than\x01",
            "anyone else. Bring it on, chumps!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8261")

    label("loc_8214")


    ChrTalk(
        0x11,
        (
            "Time to kick some ass during\x01",
            "today's practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#4SHahahahahaha!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_8261")

    Jump("loc_8478")

    label("loc_8266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_83D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_82FE")

    ChrTalk(
        0x11,
        (
            "Plie's been a star among the troupe\x01",
            "for a long time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Listening to her soothing voice can\x01",
            "relax just about anybody.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83D0")

    label("loc_82FE")


    ChrTalk(
        0x11,
        (
            "I appreciate that Plie's been\x01",
            "encouraging me all this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I just don't have much of a\x01",
            "competitive spirit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Phew... I'm pretty relieved,\x01",
            "to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "She said some amazing things to me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_83D0")

    Jump("loc_8478")

    label("loc_83D5")


    ChrTalk(
        0xFE,
        "Man, today's training session was brutal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And just when I thought I could get a role...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I was right all along. Maybe\x01",
            "I don't have any talent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8478")

    TalkEnd(0xFE)
    Return()

    # Function_27_806B end

    def Function_28_847C(): pass

    label("Function_28_847C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_85FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_852E")
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0xA,
        (
            "You'll have to change quickly, or you\x01",
            "won't make it in time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The order in which costumes are changed\x01",
            "is a crucial aspect to consider.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    Jump("loc_85F5")

    label("loc_852E")

    OP_4B(0x12, 0xFF)

    ChrTalk(
        0xA,
        "Oh, do you mind if I take a look?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Huh... They've even changed the order\x01",
            "in which the costumes are changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ugh, we don't have much time. You'll\x01",
            "just have to change quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    OP_4C(0x12, 0xFF)

    label("loc_85F5")

    Jump("loc_9554")

    label("loc_85FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8763")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_86B1")

    ChrTalk(
        0xA,
        (
            "Nikolai's strange behavior is making\x01",
            "everybody feel a little nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't blame them, though. Performing\x01",
            "arts are already stressful enough as is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_875E")

    label("loc_86B1")

    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        "I'll be responsible for Eugene, Karelia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Please, see to it that Selene doesn't get anxious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Okay, understood. I'll accompany her\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x1, 1)
    OP_4C(0x10, 0xFF)

    label("loc_875E")

    Jump("loc_9554")

    label("loc_8763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_87FE")

    ChrTalk(
        0xA,
        (
            "(Nikolai's attitude has changed drastically\x01",
            "in such a short amount of time...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "(Is this what gaining confidence\x01",
            "does to a person?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9554")

    label("loc_87FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_88D1")
    SetChrSubChip(0x15, 0x2)

    ChrTalk(
        0xA,
        (
            "Seriously? You're going to delay\x01",
            "the show by doing that now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#6104FOh, don't be so dramatic. I still have\x01",
            "ten minutes until it's go time!\x02\x03",
            "#6102FCome on, Karelia. Make it snappy!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    Jump("loc_9554")

    label("loc_88D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8A60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_8966")

    ChrTalk(
        0xA,
        (
            "Nikolai messed up pretty badly during\x01",
            "yesterday's performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope he isn't beating himself up\x01",
            "too hard over it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A5B")

    label("loc_8966")


    ChrTalk(
        0xA,
        (
            "Nikolai messed up pretty badly during\x01",
            "yesterday's performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It caused him to start panicking, which\x01",
            "made him forget some of his lines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't imagine he feels too great\x01",
            "about it. I'm a little worried for his\x01",
            "mental health.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_8A5B")

    Jump("loc_9554")

    label("loc_8A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_8BC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A82")
    SetScenarioFlags(0x93, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_8AE4")

    ChrTalk(
        0xA,
        "It's almost time for the play's climax.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Okay! I'd better finish cleaning.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BBD")

    label("loc_8AE4")


    ChrTalk(
        0xA,
        (
            "I thought I heard a loud thud coming\x01",
            "from the dressing room earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It was probably just my imagination.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Am I starting to hear things? I bet\x01",
            "it was just some loud sound effect\x01",
            "from the performance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_8BBD")

    Jump("loc_9554")

    label("loc_8BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_8C55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BE4")
    SetScenarioFlags(0x93, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8BE4")


    ChrTalk(
        0xA,
        (
            "Well, well, well. What do we have here?\x01",
            "Hiding pastries again, are we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Will you ever learn, Plie?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9554")

    label("loc_8C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_8DBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C77")
    SetScenarioFlags(0x93, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_8D23")

    ChrTalk(
        0xA,
        (
            "It's time for the real show to begin...\x01",
            "All I can do is pray for their success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well... I suppose I could also clean\x01",
            "their dressing rooms for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DB8")

    label("loc_8D23")


    ChrTalk(
        0xA,
        (
            "All of the artists have now entered\x01",
            "the backstage area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's time for the real show to begin...\x01",
            "All I can do is pray for their success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_8DB8")

    Jump("loc_9554")

    label("loc_8DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8F20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_8E33")

    ChrTalk(
        0xA,
        (
            "Just a little longer until our new play\x01",
            "debuts. I'll do everything I can to\x01",
            "support them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F1B")

    label("loc_8E33")


    ChrTalk(
        0xA,
        (
            "Every artist has a colorful personality, so\x01",
            "it can get hard to manage them at times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "One thing's for sure, though. They take\x01",
            "their jobs seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, I don't necessarily think that\x01",
            "supporting them is a bad job.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_8F1B")

    Jump("loc_9554")

    label("loc_8F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_8F85")

    ChrTalk(
        0xA,
        (
            "*sigh* How is every superstar\x01",
            "an absolute slob? I just don't\x01",
            "understand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_913B")

    label("loc_8F85")

    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xA,
        (
            "*sigh* Oh, Ilya... How typical of you to\x01",
            "come waltzing in as if you don't have\x01",
            "a care in the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You haven't bothered to change your\x01",
            "poor manners one bit, have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1703FI guess you could say that...\x02\x03",
            "#1700FAnyway, I'm about to start practicing.\x01",
            "Be a darling and help me into my\x01",
            "clothes, Karelia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Again with the attitude... I can't help\x01",
            "but feel bad for the hardships you\x01",
            "put the troupe leader through.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    OP_4C(0x8, 0xFF)

    label("loc_913B")

    Jump("loc_9554")

    label("loc_9140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_9275")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_91A1")

    ChrTalk(
        0xA,
        (
            "Plie is a completely different person\x01",
            "compared to her stage persona.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9270")

    label("loc_91A1")

    OP_4B(0x12, 0xFF)

    ChrTalk(
        0xA,
        (
            "I'm begging you, Plie. Please refrain from\x01",
            "eating and drinking after you've changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't help but feel that you're disrespecting\x01",
            "the hard work I put into designing the clothes!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x1, 1)
    OP_4C(0x12, 0xFF)

    label("loc_9270")

    Jump("loc_9554")

    label("loc_9275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_93CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_92F9")

    ChrTalk(
        0xA,
        (
            "It's time for the men in this room to make\x01",
            "themselves scarce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Rixia is about to starting changing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_93C6")

    label("loc_92F9")

    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xA,
        (
            "Please change as quickly as you\x01",
            "can, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I fixed the frayed thread on your\x01",
            "dress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1805FOh, you're right... That looks much\x01",
            "better now.\x02\x03",
            "#1800FThank you so much, Karelia!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x1, 1)
    OP_4C(0x9, 0xFF)

    label("loc_93C6")

    Jump("loc_9554")

    label("loc_93CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_9493")

    ChrTalk(
        0xA,
        (
            "The troupe has me working like a dog\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Between fine-tuning the costume designs,\x01",
            "or maintaining the artists' physique, I've\x01",
            "got a ton of behind-the-scenes work to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9554")

    label("loc_9493")


    ChrTalk(
        0xA,
        (
            "They're even adjusting the script in\x01",
            "the final hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Between fine-tuning the costume designs,\x01",
            "or maintaining the artists' physique, I've\x01",
            "got a ton of behind-the-scenes work to do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_9554")

    TalkEnd(0xFE)
    Return()

    # Function_28_847C end

    def Function_29_9558(): pass

    label("Function_29_9558")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_95E2")

    ChrTalk(
        0xE,
        (
            "It's about time for the evening\x01",
            "performance to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha. Looks like the theater's\x01",
            "going to be packed again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9673")

    label("loc_95E2")


    ChrTalk(
        0xE,
        (
            "My apologies. The performance is\x01",
            "moments away from beginning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Please refrain from going backstage, as\x01",
            "it is currently prohibited.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_9673")

    TalkEnd(0xFE)
    Return()

    # Function_29_9558 end

    def Function_30_9677(): pass

    label("Function_30_9677")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_97CE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9765")

    ChrTalk(
        0x101,
        (
            "#0005FWas this kid always a part\x01",
            "of the troupe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The heck? You aren't spectators, are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The theater isn't open to the public right\x01",
            "now. No ticket, no entry. Got it? Great,\x01",
            "now scram!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 0)
    Jump("loc_97C9")

    label("loc_9765")


    ChrTalk(
        0xFE,
        "No tickets, no entry. Got it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't try any funny business, pal.\x01",
            "I've got my eyes on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97C9")

    Jump("loc_99E8")

    label("loc_97CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_99E8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_97F1")
    Call(0, 31)
    Jump("loc_99E8")

    label("loc_97F1")


    ChrTalk(
        0xFE,
        (
            "I'm cleaning. You got a problem\x01",
            "with that?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_99E5")

    ChrTalk(
        0x101,
        "#0012FHaha. You're as rebellious as ever.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98AF")

    ChrTalk(
        0x102,
        "#0100FI feel like you've gotten used to it, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9945")

    label("loc_98AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98FC")

    ChrTalk(
        0x103,
        "#0200FI am under the impression you have adjusted.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9945")

    label("loc_98FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9945")

    ChrTalk(
        0x104,
        "#0300FLooks like you're gettin' the hang of it, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_9945")


    ChrTalk(
        0xFE,
        (
            "Wh-What's that supposed to mean? Anybody\x01",
            "could do something THIS simple!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1111F(Wow! Her hair is all pretty and silver...\x01",
            "Is she your friend, Lloyd?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99E5")

    SetScenarioFlags(0x1, 3)

    label("loc_99E8")

    TalkEnd(0xFE)
    Return()

    # Function_30_9677 end

    def Function_31_99EC(): pass

    label("Function_31_99EC")


    ChrTalk(
        0x101,
        (
            "#0005FWas this kid always a part\x01",
            "of the troupe?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A69")

    ChrTalk(
        0xFE,
        (
            "The heck? You guys Ilya's\x01",
            "friends or something?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A9E")

    label("loc_9A69")


    ChrTalk(
        0xFE,
        (
            "The heck? You guys Ilya's\x01",
            "friends or something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A9E")


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

    # Function_31_99EC end

    def Function_32_9B34(): pass

    label("Function_32_9B34")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I took the plunge and bought tickets\x01",
            "for S section seats!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sweating bullets, here! This is\x01",
            "the least I can do to make this\x01",
            "proposal go off without a hitch!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_9B34 end

    def Function_33_9BE4(): pass

    label("Function_33_9BE4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Okay, sweet! I got the tickets!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Not only that, but they're S section seats!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wow! He's a lot bolder than I gave him\x01",
            "credit for.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_9BE4 end

    def Function_34_9C79(): pass

    label("Function_34_9C79")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hurry up, Mom! It's going to start\x01",
            "any minute now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to be very upset with you if we\x01",
            "miss Ilya's performance, Mother!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_9C79 end

    def Function_35_9D08(): pass

    label("Function_35_9D08")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Let's see. Section B, seat 28-2... Looks like\x01",
            "it's on the right side of the theater.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All right, it's time to go! I finally\x01",
            "get to watch an Arc en Ciel show!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_9D08 end

    def Function_36_9DB6(): pass

    label("Function_36_9DB6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(0, 1450, -5360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13000, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x101, 500, 0, -8230, 0)
    SetChrPos(0x102, -500, 0, -8430, 0)
    SetChrPos(0x103, 500, 0, -9730, 0)
    SetChrPos(0x104, -500, 0, -9930, 0)
    SetChrPos(0x8, 10000, 2400, 13900, 270)
    SetChrPos(0x9, 11000, 2400, 13500, 270)
    SetChrPos(0xB, 4500, 0, 3190, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_9ECA():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9ECA)

    def lambda_9EE4():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9EE4)
    Sleep(50)

    def lambda_9EF8():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9EF8)

    def lambda_9F12():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9F12)
    Sleep(50)

    def lambda_9F26():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9F26)

    def lambda_9F40():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9F40)
    Sleep(50)

    def lambda_9F54():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9F54)

    def lambda_9F6E():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9F6E)
    OP_68(0, 1450, -4360, 3000)
    SetCameraDistance(12000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#0005F#11PHmm? What's going on?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(7680, 3950, 13870, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)
    OP_68(0, 3950, 13500, 5000)
    MoveCamera(33, 25, 0, 5000)
    SetCameraDistance(12920, 5000)
    BeginChrThread(0x8, 3, 0, 37)
    Sleep(800)

    NpcTalk(
        0x8,
        "Blonde-Haired Woman",
        (
            "#1706F#11POh, don't be so stubborn, Rixia.\x01",
            "I promise it's not a big deal.\x02\x03",
            "#1702FStay with me for as long\x01",
            "as you'd like.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        (
            "#1805F#11PN-No, really. I couldn't...\x02\x03",
            "#1809FYou don't need to do that. I'll find a\x01",
            "cheap and cozy apartment to settle\x01",
            "into soon.\x02\x03",
            "#1802FI can ask City Hall's information desk\x01",
            "about it, right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Blonde-Haired Woman",
        (
            "#1702F#5PYep. That's probably the quickest and\x01",
            "easiest way to go about it.\x02\x03",
            "#1709FYou can take care of your citizenship\x01",
            "application while you're there, too. ㈱\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Purple-Haired Girl",
        (
            "#1809F#11PI...suppose you're right.\x02\x03",
            "#1810FI'm sorry for constantly bothering you for help,\x01",
            "especially after all the guidance you've offered\x01",
            "during our practices.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    WaitChrThread(0x8, 3)
    OP_6F(0x79)
    Fade(500)
    OP_68(150, 1450, -3940, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12000, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#0307F#11PHoly smokes! Isn't that Ilya Platiere?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F#11PIlya Platiere?\x02\x03",
            "#0002FI think I've seen her in\x01",
            "a few magazines...\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xB, 0x0, 400)
    TurnDirection(0xC, 0x0, 400)
    Sleep(300)

    NpcTalk(
        0xB,
        "Man",
        "And who might you be?\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(15)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(12)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_A494():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A494)
    Sleep(15)

    def lambda_A4A4():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A4A4)

    def lambda_A4B1():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A4B1)
    Sleep(12)

    def lambda_A4C1():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A4C1)
    OP_68(-120, 1450, -3060, 3000)
    MoveCamera(39, 26, 0, 3000)
    SetCameraDistance(12260, 3000)
    BeginChrThread(0xB, 1, 0, 38)
    Sleep(1000)

    def lambda_A4FC():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A4FC)
    Sleep(180)

    def lambda_A50C():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A50C)
    Sleep(240)

    def lambda_A51C():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A51C)
    Sleep(250)

    def lambda_A52C():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A52C)
    OP_6F(0x79)
    WaitChrThread(0xB, 1)

    ChrTalk(
        0xB,
        (
            "#5PMy sincerest apologies, but Arc en Ciel\x01",
            "has a performance starting at 6PM.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PIf you're a fan, we would appreciate it if\x01",
            "you would return at a later time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F#12PS-Sorry, sir. We didn't intend to come\x01",
            "here unannounced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0102F#12PPlease excuse us, then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 3)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_9DB6 end

    def Function_37_A669(): pass

    label("Function_37_A669")


    def lambda_A66E():
        OP_97(0x8, 0xFFFFD6FC, 0x0, 0xFFFFFE70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A66E)

    def lambda_A688():
        OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A688)
    Sleep(50)

    def lambda_A69C():
        OP_97(0x9, 0xFFFFD6FC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A69C)

    def lambda_A6B6():
        OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A6B6)
    WaitChrThread(0x8, 1)
    TurnDirection(0x8, 0x9, 750)
    Return()

    # Function_37_A669 end

    def Function_38_A6CE(): pass

    label("Function_38_A6CE")

    OP_95(0xFE, -180, 0, -1760, 3000, 0x0)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_38_A6CE end

    def Function_39_A6EA(): pass

    label("Function_39_A6EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0xB, 0xFF)
    OP_68(0, 1450, -6360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16420, 0)
    SetChrPos(0x101, 500, 0, -8230, 0)
    SetChrPos(0x102, -500, 0, -8430, 0)
    SetChrPos(0x103, 500, 0, -9730, 0)
    SetChrPos(0x104, -500, 0, -9930, 0)
    SetChrPos(0xB, 5120, 0, 3190, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_A7AE():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A7AE)

    def lambda_A7C8():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A7C8)
    Sleep(50)

    def lambda_A7DC():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A7DC)

    def lambda_A7F6():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A7F6)
    Sleep(50)

    def lambda_A80A():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A80A)

    def lambda_A824():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A824)
    Sleep(50)

    def lambda_A838():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A838)

    def lambda_A852():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A852)
    OP_68(0, 1450, -4360, 3000)
    SetCameraDistance(17420, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A8E4():

        label("loc_A8E4")

        TurnDirection(0xFE, 0xB, 400)
        Yield()
        Jump("loc_A8E4")

    QueueWorkItem2(0x0, 1, lambda_A8E4)

    def lambda_A8F6():

        label("loc_A8F6")

        TurnDirection(0xFE, 0xB, 400)
        Yield()
        Jump("loc_A8F6")

    QueueWorkItem2(0x1, 1, lambda_A8F6)

    def lambda_A908():

        label("loc_A908")

        TurnDirection(0xFE, 0xB, 400)
        Yield()
        Jump("loc_A908")

    QueueWorkItem2(0x2, 1, lambda_A908)

    def lambda_A91A():

        label("loc_A91A")

        TurnDirection(0xFE, 0xB, 400)
        Yield()
        Jump("loc_A91A")

    QueueWorkItem2(0x3, 1, lambda_A91A)
    OP_95(0xB, 0, 0, -1760, 3000, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    ChrTalk(
        0xB,
        (
            "My sincerest apologies, but Arc en Ciel\x01",
            "has a performance starting at 6PM.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you're a fan, we would appreciate it if\x01",
            "you would leave and return another time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F#2PS-Sorry, sir. We didn't intend to come\x01",
            "here unannounced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F#2P(Arc en Ciel is an incredibly famous troupe...\x01",
            "I don't think we should bother them if we\x01",
            "don't have any business here.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x67, 7)
    SetScenarioFlags(0x5C, 4)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_39_A6EA end

    def Function_40_AAE3(): pass

    label("Function_40_AAE3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xB, 0x80)
    OP_4B(0xB, 0xFF)
    OP_68(-400, 1450, -2870, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, -800, 0, -3050, 0)
    SetChrPos(0x102, 600, 0, -3050, 0)
    SetChrPos(0x103, -800, 0, -4180, 0)
    SetChrPos(0x104, 600, 0, -4180, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB95")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x109, -30, 0, -5290, 0)

    label("loc_AB95")

    SetChrPos(0xB, -40, 0, -1140, 180)
    SetChrPos(0x14, 4670, 0, 3090, 90)
    BeginChrThread(0x14, 0, 0, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "Welcome, everybody.\x01",
            "Thank you for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, I regret to inform you that Ilya\x01",
            "and Rixia are currently occupied...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F#2PWe should be the ones apologizing.\x01",
            "Everybody's performing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F#2PWell, not like we had much to do here, eh?\x01",
            "We can drop by here another time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100F#2PI agree. We should leave.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F#2POur apologies for the disturbance.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xC8, 5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD75")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_AD75")

    SetScenarioFlags(0x5C, 4)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_AAE3 end

    def Function_41_AD82(): pass

    label("Function_41_AD82")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xB, 0x80)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_68(-400, 1450, -2870, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, -800, 0, -3050, 0)
    SetChrPos(0x102, 600, 0, -3050, 0)
    SetChrPos(0x103, -800, 0, -4180, 0)
    SetChrPos(0x104, 600, 0, -4180, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE3E")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, -30, 0, -5290, 0)

    label("loc_AE3E")

    SetChrPos(0xB, -40, 0, -1140, 180)
    SetChrPos(0x14, 4670, 0, 3090, 90)
    BeginChrThread(0x14, 0, 0, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "Welcome, everybody.\x01",
            "Thank you for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, I regret to inform you that Ilya\x01",
            "and Rixia are currently occupied...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F#2PWe should be the ones apologizing.\x01",
            "Everybody's performing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F#2PWell, not like we had much to do here, eh?\x01",
            "We can drop by here another time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100F#2PI agree. We should leave.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F#2POur apologies for the disturbance.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xC8, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B01E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_B01E")

    SetScenarioFlags(0x5C, 4)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_AD82 end

    def Function_42_B02B(): pass

    label("Function_42_B02B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xB, 0x80)
    OP_4B(0xB, 0xFF)
    OP_68(0, 1450, -4360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 500, 0, -3230, 0)
    SetChrPos(0x102, -500, 0, -3430, 0)
    SetChrPos(0x103, 500, 0, -4730, 0)
    SetChrPos(0x104, -500, 0, -4930, 0)
    SetChrPos(0xB, 0, 0, -1760, 180)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "Oh, the SSS has returned once more.\x01",
            "It's wonderful to see you again, friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FLikewise, Balsamo. How was the\x01",
            "performance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, the show was able to go on. The daytime\x01",
            "performance had to be postponed, but it's being\x01",
            "held right as we speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The complete lack of rehearsal had us a\x01",
            "pinch nervous, but I think we'll be able\x01",
            "to manage our way through this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FThat's wonderful news.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FI am unsurprised that a highly-adept\x01",
            "troupe such as yourselves managed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FAnyway, we still haven't found any\x01",
            "leads on your missing man.\x02\x03",
            "#0303FBut don't worry, we plan to keep the\x01",
            "investigation alive and kickin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thank you, and I'm terribly sorry about\x01",
            "the inconvenience. I'll leave Nikolai in your\x01",
            "capable hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWe won't rest until we find him, sir.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xE7, 0)
    SetScenarioFlags(0x5C, 4)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_B02B end

    def Function_43_B409(): pass

    label("Function_43_B409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B4B4")
    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#0000FA lot of people have come to watch\x01",
            "the show.\x02\x03",
            "Let's try to stay out of the auditorium\x01",
            "for now. We don't want to get in the\x01",
            "audience's way.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_B4B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_B595")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B530")

    ChrTalk(
        0x101,
        (
            "#0001FWe don't have time to watch the show! Let's\x01",
            "hurry and head to the east staircase!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B58D")

    label("loc_B530")


    ChrTalk(
        0x102,
        (
            "#0101FWe don't have time to watch the show! Let's\x01",
            "hurry and head to the east staircase!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B58D")

    TalkEnd(0xFF)
    Jump("loc_B647")

    label("loc_B595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B647")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Look Inside\x01",      # 0
            "Stop\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B5F0"),
        (1, "loc_B640"),
        (SWITCH_DEFAULT, "loc_B645"),
    )


    label("loc_B5F0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_B615")
    SetScenarioFlags(0x5C, 5)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_B63B")

    label("loc_B615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_B62F")
    SetScenarioFlags(0x5C, 4)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_B63B")

    label("loc_B62F")

    SetScenarioFlags(0x5C, 3)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()

    label("loc_B63B")

    Jump("loc_B645")

    label("loc_B640")

    Jump("loc_B645")

    label("loc_B645")

    EventEnd(0x3)

    label("loc_B647")

    Return()

    # Function_43_B409 end

    def Function_44_B648(): pass

    label("Function_44_B648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B700")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Look Inside\x01",      # 0
            "Stop\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B6A3"),
        (1, "loc_B6F9"),
        (SWITCH_DEFAULT, "loc_B6FE"),
    )


    label("loc_B6A3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x86, 3)
    ClearScenarioFlags(0x86, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_B6CE")
    SetScenarioFlags(0x5D, 0)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_B6F4")

    label("loc_B6CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_B6E8")
    SetScenarioFlags(0x5C, 7)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_B6F4")

    label("loc_B6E8")

    SetScenarioFlags(0x5C, 6)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()

    label("loc_B6F4")

    Jump("loc_B6FE")

    label("loc_B6F9")

    Jump("loc_B6FE")

    label("loc_B6FE")

    EventEnd(0x3)

    label("loc_B700")

    Return()

    # Function_44_B648 end

    def Function_45_B701(): pass

    label("Function_45_B701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B7B9")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Look Inside\x01",      # 0
            "Stop\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B75C"),
        (1, "loc_B7B2"),
        (SWITCH_DEFAULT, "loc_B7B7"),
    )


    label("loc_B75C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x86, 2)
    ClearScenarioFlags(0x86, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_B787")
    SetScenarioFlags(0x5D, 0)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_B7AD")

    label("loc_B787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_B7A1")
    SetScenarioFlags(0x5C, 7)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_B7AD")

    label("loc_B7A1")

    SetScenarioFlags(0x5C, 6)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()

    label("loc_B7AD")

    Jump("loc_B7B7")

    label("loc_B7B2")

    Jump("loc_B7B7")

    label("loc_B7B7")

    EventEnd(0x3)

    label("loc_B7B9")

    Return()

    # Function_45_B701 end

    def Function_46_B7BA(): pass

    label("Function_46_B7BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B86C")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Look Inside\x01",      # 0
            "Stop\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B815"),
        (1, "loc_B865"),
        (SWITCH_DEFAULT, "loc_B86A"),
    )


    label("loc_B815")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_B83A")
    SetScenarioFlags(0x5D, 3)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_B860")

    label("loc_B83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_B854")
    SetScenarioFlags(0x5D, 2)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_B860")

    label("loc_B854")

    SetScenarioFlags(0x5D, 1)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()

    label("loc_B860")

    Jump("loc_B86A")

    label("loc_B865")

    Jump("loc_B86A")

    label("loc_B86A")

    EventEnd(0x3)

    label("loc_B86C")

    Return()

    # Function_46_B7BA end

    def Function_47_B86D(): pass

    label("Function_47_B86D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -91050, 0, 6720, 0)
    OP_68(-91310, 1500, 6690, 0)
    MoveCamera(29, 11, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20500, 0)
    OP_74(0x1C, 0x1E)
    OP_70(0x1C, 0x0)
    SetMapObjFlags(0x1C, 0x1000)
    ClearMapObjFlags(0x1C, 0x4)
    OP_71(0x1C, 0x19, 0x2D, 0x0, 0x20)
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
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetCameraDistance(19500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_71(0x1C, 0x32, 0x46, 0x0, 0x20)
    Sleep(800)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        "#2100121V#1702FSorry to keep you waiting.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100122V\x07\x05",
            "No, no. It's no problem at all, Ilya.\x02\x03",
            "#2100123VIf I were to guess...you stayed after practice\x01",
            "to mentor your favorite new dancer?\x02\x03",
            "#2100124VAnd I'm sure that your enthusiasm wore out\x01",
            "the poor troupe leader.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#2100125V\x07\x00",
            "#1709FWh-Whaaat? No way...that's ridiculous.\x02\x03",
            "#2100126V#1702FSo anyway, what's up, Cecile?\x02\x03",
            "#2100127VKinda odd to get a call from you this late.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Cecile's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100128V\x07\x05",
            "Oh, right.\x02\x03",
            "#2100129VI just wanted to thank you.\x02\x03",
            "#2100130VYou know, for the tickets you sent me?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#2100131V\x07\x00",
            "#1700FOh, that's all?\x02\x03",
            "#2100132V#1704FI know you might be busy and all with\x01",
            "the hospital, but come if you can, okay?\x02\x03",
            "#2100133V#1702FIt's the opening day of the Anniversary\x01",
            "Festival, after all. Surely you'll be able\x01",
            "to get that one day off, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Cecile's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100134V\x07\x05",
            "I'll figure something out.\x02\x03",
            "#2100135VAlso, I can't help but feel a little sorry.\x02\x03",
            "#2100136VYou got me tickets for the first ever public\x01",
            "performance, AND they're S section seats...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#2100137V\x07\x00",
            "#1709FJust call it star privilege.\x02\x03",
            "#2100138V#1702FAnd besides, having my best friend come\x01",
            "watch me perform's going to put me at\x01",
            "the top of my game!\x02\x03",
            "#2100139VFeeling the heat from you is gonna\x01",
            "stop me from screwing up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Cecile's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100140V\x07\x05",
            "How very much like you to keep\x01",
            "strong in the face of adversity.\x02\x03",
            "#2100141VI suppose you've always been the type\x01",
            "that enjoys the thrill of challenging adversity\x01",
            "head-on.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#2100142V\x07\x00",
            "#1704FHaha. No denying that, my friend.\x02\x03",
            "#2100143V#1700FAnyway, make sure you bring a sexy\x01",
            "stud along with you.\x02\x03",
            "#2100144VI mean, you work at St. Ursula, don't you?\x01",
            "There should be plenty of promising bachelors\x01",
            "hanging around there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Cecile's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100145V\x07\x05",
            "Y-Yes, perhaps I will.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#2100146V\x07\x00",
            "#1705FO-Oh, Cecile.\x02\x03",
            "#2100147V#1706FI'm sorry. I didn't mean to...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Cecile's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100148V\x07\x05",
            "It's okay, Ilya. I know.\x02\x03",
            "#2100149VI've moved on.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#2100150V\x07\x00",
            "#1700FThat so?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#2100151V\x07\x00",
            "#1702FOh, that's right! Why don't you just\x01",
            "invite that little brother of yours?\x02\x03",
            "#2100152VDidn't he return to Crossbell\x01",
            "just recently?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Cecile's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100153V\x07\x05",
            "You're talking about Lloyd?\x02\x03",
            "#2100154VUm, are you sure? He might be\x01",
            "busy with his work.\x02\x03",
            "#2100155VThen again, I don't think he's ever seen one\x01",
            "of your plays, so this might be a once-in-a-\x01",
            "lifetime chance for him.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#2100156V\x07\x00",
            "#1709FYes, exactly! Go for it, girl!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Cecile's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100157V\x07\x05",
            "Oh? Sorry, Ilya. It's almost time for me\x01",
            "to start my night shift.\x02\x03",
            "#2100158VThanks for the tickets. Really. I can't\x01",
            "wait to watch you perform again.\x02\x03",
            "#2100159VPractice hard, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#2100160V\x07\x00",
            "#1702FAnd you go save some lives or something.\x01",
            "Talk to you later, Cecile.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMapObjFlags(0x1C, 0x4)
    Sound(822, 0, 100, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#2100161V\x07\x00",
            "#1701F(Three years...)\x02\x03",
            "#2100162V#1706F(Looks like it might still be too\x01",
            "soon for those wounds to heal.)\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("m0101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_47_B86D end

    def Function_48_C660(): pass

    label("Function_48_C660")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1250, -1000, 0)
    MoveCamera(54, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -600, 0, -2900, 0)
    SetChrPos(0x102, 600, 0, -2900, 0)
    SetChrPos(0x103, -900, 0, -4100, 0)
    SetChrPos(0x104, 900, 0, -4100, 0)
    SetChrPos(0xB, 4500, 0, 4500, 90)
    OP_68(0, 1750, 5000, 6000)
    MoveCamera(34, 10, 0, 6000)
    SetCameraDistance(25500, 6000)
    FadeToBright(1000, 0)
    StopBGM(0x5DC)
    WaitBGM()
    Sleep(50)
    PlayBGM("ed7529", 0)
    VolumeBGM(0x28, 0x64)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x211), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(0, 1050, -1700, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#2100396V#11P#0205FWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100397V#0109FThe lobby certainly is grand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100398V#6P#0000FI hear music playing... Do you think\x01",
            "they're in the middle of practice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100399V#0309FYep, I'd say so.\x02",
    )

    CloseMessageWindow()
    OP_4B(0xB, 0xFF)
    TurnDirection(0xB, 0x101, 500)

    NpcTalk(
        0xB,
        "Man's Voice",
        "#2100400V#6PWelcome, ladies and gentlemen.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    SetCameraDistance(19000, 2000)

    def lambda_C8ED():
        OP_95(0xFE, 0, 0, -500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C8ED)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0xB4, 0x1F4)

    ChrTalk(
        0xB,
        "#2100401V#5PI'm terribly sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2100402V#5POnly authorized personnel may enter\x01",
            "the theater at this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100403V#6P#0003FTh-That's okay. We're here for good reason.\x02\x03",
            "#2100404V#0000FWe're with the CPD. I believe we received\x01",
            "a request for a consultation from you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#2100405V#5PSo, you're the Special Support Section.\x01",
            "Thank you for coming...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2100406V#5PWelcome to Arc en Ciel. Rixia has already\x01",
            "given me the full story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2100407V#5PI believe you're here to speak with the\x01",
            "troupe leader and Ilya, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100408V#6P#0000FYeah. Are they free right now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2100409V#5PI believe so. Please go straight ahead\x01",
            "through the main doors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2100410V#5PAvan and Rixia are likely in the process of\x01",
            "watching Ilya practice right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100411V#6P#0005FOh... Are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100412V#0101FWe don't want to interrupt her while\x01",
            "she's practicing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2100413V#5POh, no. I assure you, she isn't the type to be\x01",
            "bothered by a minor trifle like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2100414V#5POn the contrary. With the show almost upon\x01",
            "us, she'd be quite happy to have visitors.\x02",
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
        "#2100415V#6P#0002FAll right, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100416V#0309FTo the auditorium!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 0, -2900, 0)
    OP_4C(0xB, 0xFF)
    SetChrPos(0xB, -2890, 2500, 14820, 180)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x80, 4)
    OP_29(0x42, 0x1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_48_C660 end

    def Function_49_CE63(): pass

    label("Function_49_CE63")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-90090, 1250, 3310, 0)
    MoveCamera(52, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22160, 0)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x8, -90050, 0, 4350, 180)
    SetChrPos(0x9, -90970, 0, 4840, 180)
    SetChrPos(0xD, -88670, 0, 4830, 225)
    SetChrPos(0x101, -89850, 0, 2450, 0)
    SetChrPos(0x102, -91090, 0, 2130, 0)
    SetChrPos(0x104, -91200, 0, 710, 0)
    SetChrPos(0x103, -89830, 0, 950, 0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    SetCameraDistance(21660, 1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#2100485V#1806F#1PYou need to calm down, Ilya...\x02\x03",
            "#2100486V#1801FIsn't hugging someone out of the blue\x01",
            "a little rude?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100487V#1709F#5PPshaw! Who needs formalities?\x02\x03",
            "#2100488V#1702FAdmit it, Lloyd. Didn't my hug make you\x01",
            "a little happy? A teensy weensy bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100489V#0012F#12PHahaha. Uh, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100490V#0211F#12P(*stare*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100491V#0111F#6P(First Cecile, now her...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100492V#0310F#12P(The hierarchy has made itself painfully\x01",
            "clear. The little brother character reigns\x01",
            "supreme!)\x02\x03",
            "#2100493V(Damn you! Turn down that lil' brother\x01",
            "charm of yours and save some ladies\x01",
            "for the rest of us!)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2100494V#0006F#12PA-Anyway, about the threat letter...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100495V#1705F#5POh, yeah. I nearly forgot about that thing.\x02\x03",
            "#2100496V#1704FCan't really say no to my favorite little\x01",
            "guy, can I? I made sure to bring the\x01",
            "letter to practice with me.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    OP_96(0x8, 0xFFFEA0CA, 0x0, 0xD34, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        "#2100497V#1700F#5PHere you go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100498V#0002F#12PTh-Thanks, Ilya... (I'm pretty sure YOU\x01",
            "guys asked us for help, though.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D3B2():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D3B2)

    def lambda_D3BF():
        OP_96(0xFE, 0xFFFEA03E, 0x0, 0x10FE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_D3BF)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#2100499V#0005F#12PLet's give it a read...\x02",
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "CEASE PRODUCTION OF YOUR NEW SHOW,\x01",
            "OR THE BELOVED FERVENT DANCER WILL\x01",
            "HAVE A TRAGIC ACCIDENT.    -Yin\x07\x00\x02",
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
        0x102,
        "#2100500V#0101F#6PWhat the...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100501V#0201F#12PCease production of your new show...\x02\x03",
            "#2100502V...or the beloved Fervent Dancer will\x01",
            "have a tragic accident. Signed by Yin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100503V#0301F#12PThat's a threat letter if I've ever seen one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100504V#1706F#5PYou sure about that? It sounds more like a\x01",
            "lame prank to me.\x02\x03",
            "#2100505V#1700FI'm going to be honest with you guys: This\x01",
            "sort of threat isn't out of the ordinary.\x01",
            "We're already kinda used to it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D73E():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D73E)

    ChrTalk(
        0x101,
        "#2100506V#0001F#12PReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2100507VUnfortunately so. We DO get a decent\x01",
            "amount of these sort of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2100508VMost of them are written out of jealousy\x01",
            "or in jest, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2100509VIn this particular case, however, there\x01",
            "is something that bothers me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100510V#0205F#12PAnd what would that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100511V#0301F#12PIt's the signature, ain't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#2100512VPrecisely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2100513VEssentially all of the letters we've been sent\x01",
            "up until now have been left anonymous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2100514V#1806F#5PSomething about the name Yin rubs me the\x01",
            "wrong way.\x02\x03",
            "#2100515V#1808FI just can't shake the feeling that this isn't\x01",
            "a simple prank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100516V#1703F#5PPretty sure that's just your overactive\x01",
            "imagination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100517V#0003F#12PHmmm...\x02\x03",
            "#2100518V#0001FDo you have an idea as to who this\x01",
            "'Yin' person is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100519V#1704F#5PNot in the slightest.\x02\x03",
            "#2100520V#1701FLike, is that even a person's name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2100521V#1806F#5PIt almost sounds like it's some\x01",
            "sort of code name...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2100522VI suppose it could be related to our new\x01",
            "show's title... Yin means silver, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#2100523VThat's where the well runs dry, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100524V#0103F#6PAn interesting coincidence, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100525V#0001F#12PAny other ideas?\x02\x03",
            "#2100526VI don't mean to pry, but have you done\x01",
            "anything recently that would cause\x01",
            "someone to hold a grudge against you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x9,
        "#2100527V#1808F#5PA-About that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#2100528VWait, you don't mean...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#2100529V#1705F#11PWhat is it, Rixia?\x02\x03",
            "#2100530VYou two have some idea about who\x01",
            "might have it out for you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_DDDC():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_DDDC)
    Sleep(50)
    TurnDirection(0xD, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        "#2100531V#11PWell, actually...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2100532V#1806F#6PIt's not about us. It's about you, Ilya.\x02\x03",
            "#2100533V#1801FRemember the other day? With the\x01",
            "president of that company...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#2100534V#1705F#11POh, that old baldy?\x02\x03",
            "#2100535V#1706FI couldn't care less about that. I'd\x01",
            "already forgotten, to be honest.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
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
        0x103,
        "#2100536V#0200F#12PWho exactly was this 'baldy'?\x02",
    )

    CloseMessageWindow()

    def lambda_E009():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E009)
    Sleep(200)

    def lambda_E019():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E019)
    Sleep(50)
    TurnDirection(0xD, 0x102, 500)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#2100537V#1700F#5PJust some greasy old loser\x01",
            "named Marconi.\x02\x03",
            "#2100538VApparently, he's the big boss of that\x01",
            "business, Revache & Co.\x02",
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

    ChrTalk(
        0x101,
        "#2100539V#0005F#12PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100540V#0101F#6PRevache?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100541V#0301F#12PSo the name finally comes out...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#2100542V#1705F#5PWhat's with all the freaking out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100543V#0006F#12PW-Well, we've been hearing that\x01",
            "name pretty often.\x02\x03",
            "#2100544V#0001FDo you mind filling us in on what happened\x01",
            "with Revache's president?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100545V#1706F#5PSure thing. He likes to bring his business\x01",
            "associates to Arc en Ciel for entertainment.\x02\x03",
            "#2100546V#1701FHe loves sitting in our exclusive seats, so\x01",
            "you know he's a big shot. The funny thing\x01",
            "is, he's not interested in our shows at all.\x02\x03",
            "#2100547VLike, he doesn't even appreciate my dancing.\x01",
            "All he does is ogle me with those lecherous\x01",
            "eyes of his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2100548V#1806F#1PI-Ilya...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2100549VShe does have a keen eye when it comes\x01",
            "to things of that nature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100550V#1704F#5POf course I do. The stage is my world,\x01",
            "and that includes the audience.\x02\x03",
            "#2100551V#1700FSo anyway, that old coot had the gall\x01",
            "to approach and patronize me.\x02\x03",
            "#2100552VHe kept babbling on and on about how he\x01",
            "would support my career and have me debut\x01",
            "at the Heimdallr Opera House.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100553V#0305F#12PWhoa. You plannin' to dance there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2100554VActually, we receive requests to perform\x01",
            "in both the Empire and the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2100555VWe're often asked to a hold limited run\x01",
            "of performances in both countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2100556VNow that I think about it, we even had an\x01",
            "offer to perform in Liberl's Grand Arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100557V#0003F#12PWow. Arc en Ciel really is as popular as\x01",
            "people make them out to be.\x02\x03",
            "#2100558V#0001FStill, why would Marconi approach Ilya\x01",
            "about backing her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2100559VHe supposedly has powerful contacts\x01",
            "within Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2100560VBut judging by the rumors, they aren't the\x01",
            "type of people we want to associate with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100561V#0108F#6PFrom all we've heard, Revache has deep\x01",
            "ties to the Empire.\x02\x03",
            "#2100562V#0101FAnd to a certain degree, its criminal underworld.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2100563V#1801F#5PI had no idea they were that devious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100564V#0205F#12PHow were you able to conclude the\x01",
            "situation with Marconi?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100565V#1709F#5PI politely refused, of course.\x02\x03",
            "#2100566VAnd for good measure...I gave\x01",
            "him a slap to the face.\x02",
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

    ChrTalk(
        0x101,
        "#2100567V#0011F#12PYou did WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100568V#0105F#6PYou slapped a mafia don? In the face?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2100569V#1806F#5PYes. Yes, she did. I swear, I nearly\x01",
            "fainted after she pulled that stunt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#2100570VI as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2100571VHowever, he had the audacity to touch Ilya\x01",
            "inappropriately. The recklessness...no,\x01",
            "rudeness of that man was unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2100572VThe nearby staff intervened, so we\x01",
            "somehow managed to settle it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100573V#0303F#12PSounds like he might be a little\x01",
            "salty 'cause of the whole thing.\x02\x03",
            "#2100574V#0301FI mean, wouldn't that make sense?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100575V#0203F#12PIt does seem like a plausible motive to\x01",
            "send a threat letter, yes.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#2100576V#0003F#12POkay, we understand the situation.\x02\x03",
            "#2100577V#0001FFirst off, we'll try to uncover some new leads\x01",
            "with the clues on hand.\x02\x03",
            "#2100578VDo you mind if we keep the letter, Ilya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100579V#1700F#5PBe my guest.\x02\x03",
            "#2100580V#1704FI can see that glint in your eyes now, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100581V#0005F#12PCome again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100582V#1704F#5PIt's like whenever I step onto the stage.\x01",
            "Our eyes are the same.\x02\x03",
            "#2100583V#1702FAnyway, I'm sure you four will do a\x01",
            "bang-up job.\x02\x03",
            "#2100584VHopefully, letting you handle this whole\x01",
            "mess will let poor Rixia sleep at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2100585V#1802F#1PThank you, Ilya.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100586V#0002F#12PWe'll happily tackle the case, Miss Mao.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100587V#0104F#6PI hope we can live up to your\x01",
            "high expectations.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21960, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddItemNumber(0x324, 1)
    StopBGM(0xBB8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    OP_68(-50, 1070, -1770, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x8, -120, 2500, 15910, 42)
    SetChrPos(0x9, -80, 0, -280, 179)
    SetChrPos(0x101, 0, 0, -2000, 0)
    SetChrPos(0x102, -1290, 0, -2840, 0)
    SetChrPos(0x104, 580, 0, -2980, 0)
    SetChrPos(0x103, -660, 0, -3670, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01800.itp")
    Sleep(500)
    SetCameraDistance(17000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    Sound(1639, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1000)

    AnonymousTalk(
        0x9,
        (
            "#2100588VIlya seems to finally understand the\x01",
            "situation now. Oh, I'm so happy that\x01",
            "I turned to you for help!\x02",
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
            "#2100589V#0004F#12PHaha... Well, it's only just begun.\x02\x03",
            "#2100590V#0001FI don't think we'll be able to solve\x01",
            "this using traditional methods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2100591V#1806F#5PI guess so...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#2100592V#1805F#5PB-By the way...\x02\x03",
            "#2100593V#1802FI'd appreciate it if you spoke less\x01",
            "formally to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100594V#0005F#12PWhy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2100595V#1804F#5PWell, I'm still just a novice...\x02\x03",
            "#2100596V...and I think I'm actually a little younger\x01",
            "than you and Elie.\x02\x03",
            "#2100597V#1800FI can't help but feel a little awkward when\x01",
            "you speak formally to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100598V#0000F#12PReally? I never meant anything by it.\x02\x03",
            "#2100599V#0002FWe'll treat you like a regular girl\x01",
            "from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2100600V#1809F#5PTh-Thank you! That's all I want.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Ilya's Voice",
        (
            "#2100601V#2SRixiaaa? The meeting's going to start\x01",
            "without you, if you don't hurry up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    ChrTalk(
        0x9,
        "#2100602V#1802F#2PI'll be right there!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "#2100603V#1804F#5PWell, then, everyone. If you'll excuse me.\x02\x03",
            "#2100604V#1802FIf you figure anything out, please don't\x01",
            "hesitate to stop by the theater.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)
    OP_68(150, 1070, 0, 4000)
    MoveCamera(25, 20, 0, 4000)
    OP_6E(520, 4000)
    SetCameraDistance(18500, 4000)
    SetChrFlags(0x9, 0x40)
    OP_95(0x9, 310, 0, 5940, 4000, 0x1)
    OP_95(0x9, 610, 2490, 11890, 4000, 0x1)
    OP_95(0x9, 570, 2490, 14730, 4000, 0x1)
    SetChrFlags(0x9, 0x80)

    ChrTalk(
        0x101,
        "#2100605V#0000F#5PArc en Ciel sure is busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100606V#0304FYou're tellin' me. I bet they practice another\x01",
            "hundred times before the actual show.\x02\x03",
            "#2100607V#0300FI'm startin' to get why they don't wanna\x01",
            "waste their time with this letter business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100608V#0204F#11PIndeed. An unnecessary use of their time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100609V#0102FI hope we can solve this soon, for the sake\x01",
            "of their new production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100610V#0004F#5PLet's get to it, then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    OP_68(0, 1450, -1000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x0, 0, 0, -1000, 0)
    SetChrPos(0x1, 0, 0, -1000, 0)
    SetChrPos(0x2, 0, 0, -1000, 0)
    SetChrPos(0x3, 0, 0, -1000, 0)
    SetScenarioFlags(0x80, 5)
    OP_29(0x42, 0x1, 0x2)
    OP_1B(0x4, 0xFF, 0xFFFF)
    OP_1B(0x0, 0xFF, 0xFFFF)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_49_CE63 end

    def Function_50_F900(): pass

    label("Function_50_F900")

    OP_95(0x9, -49720, 0, 370, 2500, 0x0)
    OP_95(0x9, -50520, 0, 10010, 2500, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_50_F900 end

    def Function_51_F937(): pass

    label("Function_51_F937")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_F946():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F946)
    OP_95(0xFE, -620, 0, 5850, 1500, 0x0)
    OP_95(0xFE, -620, 2390, 11360, 1500, 0x0)
    Return()

    # Function_51_F937 end

    def Function_52_F97B(): pass

    label("Function_52_F97B")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)

    def lambda_F98A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F98A)
    OP_95(0xFE, 520, 0, 5850, 1500, 0x0)
    OP_95(0xFE, 520, 2390, 11360, 1500, 0x0)
    Return()

    # Function_52_F97B end

    def Function_53_F9BF(): pass

    label("Function_53_F9BF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06200.itp")
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
    LoadChrToIndex("chr/ch09800.itc", 0x32)
    SetChrChipByIndex(0x21, 0x28)
    SetChrChipByIndex(0x22, 0x29)
    SetChrChipByIndex(0x23, 0x2A)
    SetChrChipByIndex(0x24, 0x2B)
    SetChrChipByIndex(0x25, 0x2C)
    SetChrChipByIndex(0x26, 0x2D)
    SetChrChipByIndex(0x27, 0x2E)
    SetChrChipByIndex(0x28, 0x2F)
    SetChrChipByIndex(0x29, 0x30)
    SetChrChipByIndex(0x2A, 0x31)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x22, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrPos(0x21, -670, 0, 5740, 0)
    SetChrPos(0x22, 520, 0, 5700, 0)
    SetChrPos(0x23, -670, 0, 240, 0)
    SetChrPos(0x24, 520, 0, 1240, 0)
    SetChrPos(0x25, -670, 0, -3240, 0)
    SetChrPos(0x26, 520, 0, -2240, 0)
    SetChrPos(0x27, -670, 0, -6240, 0)
    SetChrPos(0x28, 520, 0, -6240, 0)
    SetChrPos(0x29, -670, 0, -6240, 0)
    SetChrPos(0x2A, 520, 0, -6240, 0)
    SetChrPos(0x1C, -670, 0, -6240, 0)
    SetChrPos(0x1D, 520, 0, -6240, 0)
    ClearChrFlags(0xC, 0x80)
    SetMapObjFrame(0xFF, "pos01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pos02", 0x1, 0x1)
    OP_68(0, 1450, 1500, 0)
    MoveCamera(65, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    MoveCamera(90, 12, 0, 10000)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -45300, 0, 400, 90)
    SetChrPos(0x102, -45270, 0, -700, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -46840, 0, -100, 90)
    SetChrChipByIndex(0x9, 0x32)
    FadeToBright(2000, 0)
    BeginChrThread(0x21, 0, 0, 51)
    BeginChrThread(0x22, 0, 0, 52)
    BeginChrThread(0x23, 0, 0, 51)
    BeginChrThread(0x24, 0, 0, 52)
    BeginChrThread(0x25, 0, 0, 51)
    BeginChrThread(0x26, 0, 0, 52)
    Sleep(500)
    BeginChrThread(0x1C, 0, 0, 51)
    Sleep(200)
    BeginChrThread(0x1D, 0, 0, 52)
    Sleep(1500)
    BeginChrThread(0x27, 0, 0, 51)
    BeginChrThread(0x28, 0, 0, 52)
    Sleep(500)
    Sleep(2000)
    BeginChrThread(0x29, 0, 0, 51)
    Sleep(500)
    BeginChrThread(0x2A, 0, 0, 52)
    Fade(500)
    OP_68(-45820, 1300, -390, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    OP_0D()
    Sleep(300)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2201374V#0003F#5PEven Mayor MacDowell came to watch\x01",
            "the performance...\x02\x03",
            "#2201375V#0000FOh, right. Didn't he say something about\x01",
            "supporting the new production to the best\x01",
            "of his ability?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#2201376V#0104F#12PThat's right. Grandfather has been a fan of\x01",
            "Arc en Ciel since its inception.\x02\x03",
            "#2201377V#0102FI'm sure he's looking forward to your debut,\x01",
            "Rixia.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "#2201378VAhaha, really? I hope I don't let him down.\x02\x03",
            "#2201379VBut more importantly, do you think what\x01",
            "Yin said will hold true?\x02",
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

    def lambda_FFFB():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FFFB)
    Sleep(50)

    def lambda_1000B():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1000B)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2201380V#0006F#11PWe can't say for sure. Still, I think\x01",
            "there's a good chance it might.\x02\x03",
            "#2201381V#0000FFortunately for us, the First Division will be\x01",
            "keeping watch, so Ilya should be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2201382V#6206F#6PThat's a relief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201383V#0106F#11PYou know, was it really okay not telling\x01",
            "Ilya everything that happened?\x02\x03",
            "#2201384V#0101FI think the troupe leader is worried about\x01",
            "the same thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201385V#6204F#6PNo, it's okay.\x02\x03",
            "#2201386VAll I want is for Ilya to shine like the star\x01",
            "she is tonight, without any unnecessary\x01",
            "worries dragging her down.\x02\x03",
            "#2201387V#6202FThat's what I...no, that's what all of us\x01",
            "here at Arc en Ciel want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201388V#0002F#11PYou really admire Ilya.\x02\x03",
            "#2201389V#0000FWhy is that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201390V#6202F#6PHeehee...\x02\x03",
            "#2201391V#6204FAs you might know, I was forcibly\x01",
            "'invited' into the troupe by her.\x02\x03",
            "#2201392VDespite my circumstances, I'm happy.\x02\x03",
            "#2201393V#6208FAfter all, until I came to Crossbell,\x01",
            "I had only walked the path that I\x01",
            "was destined for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201394V#0005F#11PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201395V#6204F#6PSoon after, I was positively charmed by her\x01",
            "performances.\x02\x03",
            "#2201396VI thought to myself, 'Who knew that someone\x01",
            "could shine this brightly without once looking\x01",
            "back?'\x02\x03",
            "#2201397V#6210FPerhaps I ended up admiring her\x01",
            "because of how unreachable she is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201398V#0108F#11PRixia...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#2201399V#0004F#11P...But she's not unreachable, is she?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2201400V#6205F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201401V#0003F#11PYou play the role of the Moon Princess\x01",
            "for this production...\x02\x03",
            "#2201402VAnd, yes, maybe the role is elevated by the\x01",
            "radiance of the Sun Princess...\x02\x03",
            "#2201403V#0002F...but, coming from someone that doesn't\x01",
            "watch many plays, I believe both of your\x01",
            "acts are superb.\x02\x03",
            "#2201404V#0009FI know you'll shine brightly one day...\x01",
            "By your own merit, not Ilya's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2201405V#6210F#6PYou think so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201406V#0004F#11PDefinitely. And I'm sure that's the reason\x01",
            "why Ilya recruited you in the first place.\x02\x03",
            "#2201407V#0000FWe hit a barrier in this case, but we still\x01",
            "managed to get this far.\x02\x03",
            "#2201408VWe intend to see this through to the end.\x01",
            "So, we want you to tackle this show with\x01",
            "everything you've got, Rixia!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201409V#6209F#6PI will!\x02\x03",
            "#2201410V#6202FWell, it's time for me to go.\x02\x03",
            "#2201411VGood luck, you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201412V#0002F#11PThanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201413V#0109F#11PBreak a leg up there.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x190)
    OP_68(-47770, 1300, 420, 3000)
    BeginChrThread(0x9, 0, 0, 50)
    Sleep(1000)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(-45290, 1300, -570, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17580, 0)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2201414V#0000F#5PWell, you think we should stand by\x01",
            "somewhere else until they start?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2201415V#0005F#5PWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201416V#0113F#11P*sigh* I don't know what I expected.\x02\x03",
            "#2201417VThe fact you're this oblivious about\x01",
            "it is what makes you so dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201418V#0011F#5PUh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#2201419V#0111F#12PNever mind. Forget I said anything.\x02\x03",
            "#2201420V#0106FAnyway, we wouldn't want to let her\x01",
            "down after you said all that.\x02\x03",
            "#2201421V#0102FLet's solve this case, no matter what.\x01",
            "Okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201422V#0000F#5PYeah... We will.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18080, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 2)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_F9BF end

    def Function_54_10C77(): pass

    label("Function_54_10C77")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_95(0xFE, -7470, 0, 4730, 1500, 0x0)
    OP_95(0xFE, -6470, 0, 3720, 1500, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_54_10C77 end

    def Function_55_10CB2(): pass

    label("Function_55_10CB2")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_95(0xFE, -7470, 0, 4730, 1500, 0x0)
    OP_95(0xFE, -7000, 0, 5160, 1500, 0x0)
    OP_93(0xFE, 0x80, 0x1F4)
    Return()

    # Function_55_10CB2 end

    def Function_56_10CED(): pass

    label("Function_56_10CED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    OP_68(-7840, 1450, 4510, 0)
    MoveCamera(20, 26, 0, 5000)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -10000, 0, 4730, 90)
    SetChrPos(0x102, -10000, 0, 4730, 90)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    ClearChrFlags(0xC, 0x80)
    OP_66(0x5, 0x1)
    SetMapObjFrame(0xFF, "pos01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pos02", 0x1, 0x1)
    OP_68(-6840, 1450, 4510, 5000)
    MoveCamera(14, 26, 0, 5000)
    OP_6E(560, 5000)
    SetCameraDistance(17500, 5000)
    Sound(875, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0x101, 0, 0, 54)
    Sleep(1000)
    BeginChrThread(0x102, 0, 0, 55)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x101,
        (
            "#2201431V#0004F#12PIt must have started.\x02\x03",
            "#2201432V#0002FThe enthusiasm is electrifying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201433V#0109FIt's a shame. I would have loved to\x01",
            "have been able to watch it, too.\x02\x03",
            "#2201434V#0102FI'm jealous of the First Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201435V#0006F#12PI'm not so sure about that. I can't imagine\x01",
            "it's easy to focus on security while such an\x01",
            "amazing play is being performed.\x02\x03",
            "#2201436V#0001FI feel like we actually got the better\x01",
            "deal, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201437V#0104FYou may be right.\x02\x03",
            "#2201438V#0100FShall we start patrolling the theater, then?\x02\x03",
            "#2201439VLet's stay out of the First Division's line\x01",
            "of sight and only peek in at the audience\x01",
            "from time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201440V#0000F#12PGood call.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(500)
    Sound(807, 0, 100, 0)
    SetChrSubChip(0x101, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#2201441V#0000FIt's Lloyd. Can you guys hear me?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Randy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2201442V\x07\x05",
            "Loud and clear, boss.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2201443V\x07\x05",
            "Has it commenced, then?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#2201444V\x07\x00",
            "#0000FYeah. We're about to start patrolling\x01",
            "the inside of the theater.\x02\x03",
            "#2201445VYou two keep a close watch on the perimeter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2201446V\x07\x05",
            "Roger.\x02\x03",
            "#2201447VZeit has graciously offered his assistance,\x01",
            "so we'll be fine.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(2052, 255, 80, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#2201448V\x07\x00",
            "#0012FHow generous of him.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Randy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2201449V\x07\x05",
            "I'll give you a call if we spot anyone fishy.\x02\x03",
            "#2201450VDon't let the play distract you. Wouldn't want\x01",
            "the First Division to steal the spotlight, eh?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#2201451V\x07\x00",
            "#0000FYou don't have to worry about that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(807, 0, 100, 0)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2201452V#0003F#12PWe should get started.\x02\x03",
            "#2201453V#0001FFirst, let's check in with the staff and\x01",
            "see if they've noticed anything out of\x01",
            "the ordinary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201454V#0101FUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -6680, 0, 4710, 90)
    SetChrPos(0xB, 1360, 0, -1650, 180)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0x7, 0x10)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 45000, 5650, 15300, 3000, 5000, 0)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    SetScenarioFlags(0x84, 4)
    OP_29(0x43, 0x1, 0xA)
    OP_1B(0x0, 0x0, 0x57)
    ClearMapObjFlags(0x1D, 0x4)
    OP_66(0x6, 0x1)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x93, 1)
    ClearScenarioFlags(0x93, 2)
    ClearScenarioFlags(0x93, 3)
    EventEnd(0x5)
    Return()

    # Function_56_10CED end

    def Function_57_115E9(): pass

    label("Function_57_115E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1000, 3950, 15000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 0, 2500, 15000, 0)
    SetChrPos(0x102, -1000, 2500, 15000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#2201455V#0004FEverything looks all right so far.\x02\x03",
            "#2201456V#0002FMan, Ilya is incredible. I mean, I already\x01",
            "knew she was, but this is just...wow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201457V#0102FI completely agree.\x02\x03",
            "#2201458V#0104FWe should look elsewhere.\x02\x03",
            "#2201459VIf we continue to watch, we may\x01",
            "end up staying for the entire play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201460V#0012FYeah, you're probably right.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 2500, 15000, 0)
    SetScenarioFlags(0x84, 5)
    EventEnd(0x5)
    Return()

    # Function_57_115E9 end

    def Function_58_117D2(): pass

    label("Function_58_117D2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1000, 3950, 15000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 0, 2500, 15000, 0)
    SetChrPos(0x102, -1000, 2500, 15000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#2201461V#0004FNothing wrong here.\x02\x03",
            "#2201462V#0002FIlya is one thing, but Rixia is no\x01",
            "less amazing, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201463V#0102FAgreed. Those two are both in\x01",
            "top form.\x02\x03",
            "#2201464VShe truly has the presence of a moon\x01",
            "princess when bathed in silver light.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 2500, 15000, 0)
    SetScenarioFlags(0x85, 1)
    EventEnd(0x5)
    Return()

    # Function_58_117D2 end

    def Function_59_1195A(): pass

    label("Function_59_1195A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1000, 3950, 15000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 0, 2500, 15000, 0)
    SetChrPos(0x102, -1000, 2500, 15000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#2201465V#0012FThings are starting to pick up...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201466V#0104FThey are! Who could've guessed that\x01",
            "the two princesses would be sisters?\x02\x03",
            "#2201467V#0102FWhere will the plot take us next?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 800)

    ChrTalk(
        0x101,
        "#2201468V#0011FNo! We have to resist!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 800)

    ChrTalk(
        0x102,
        (
            "#2201469V#0106FS-Sorry, it's simply too compelling.\x02\x03",
            "#2201470VWe should focus on patrolling.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 2500, 15000, 0)
    SetScenarioFlags(0x85, 5)
    EventEnd(0x5)
    Return()

    # Function_59_1195A end

    def Function_60_11B9A(): pass

    label("Function_60_11B9A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_11C04")
    OP_68(48600, 6900, 14800, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 48600, 5600, 15800, 270)
    SetChrPos(0x102, 48600, 5600, 14800, 270)
    Jump("loc_11C5D")

    label("loc_11C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_11C5D")
    OP_68(-38700, 6900, 97200, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -38700, 5600, 98200, 90)
    SetChrPos(0x102, -38700, 5600, 97200, 90)

    label("loc_11C5D")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#2201471V#0003FEverything looks good in the S section seats.\x02\x03",
            "#2201472V#0000FHonestly, I doubt we have anything to worry\x01",
            "about with Dudley in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201473V#0100FYou're right about that.\x02\x03",
            "#2201474VLet's head to the next area.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_11D77")
    SetChrPos(0x0, 48600, 5600, 15800, 270)
    Jump("loc_11D91")

    label("loc_11D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_11D91")
    SetChrPos(0x0, -38700, 5600, 98200, 90)

    label("loc_11D91")

    SetScenarioFlags(0x84, 6)
    EventEnd(0x5)
    Return()

    # Function_60_11B9A end

    def Function_61_11D97(): pass

    label("Function_61_11D97")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_11E01")
    OP_68(48600, 6900, 14800, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 48600, 5600, 15800, 270)
    SetChrPos(0x102, 48600, 5600, 14800, 270)
    Jump("loc_11E5A")

    label("loc_11E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_11E5A")
    OP_68(-38700, 6900, 97200, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -38700, 5600, 98200, 90)
    SetChrPos(0x102, -38700, 5600, 97200, 90)

    label("loc_11E5A")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#2201475V#0000FNothing unusual here...\x02\x03",
            "#2201476V#0006FMan, Dudley must really be made of\x01",
            "sterner stuff.\x02\x03",
            "#2201477V#0001FHe's got a full view of the stage, yet\x01",
            "he's completely unfazed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201478V#0103FYet another example of his iron will.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_11F7E")
    SetChrPos(0x0, 48600, 5600, 15800, 270)
    Jump("loc_11F98")

    label("loc_11F7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_11F98")
    SetChrPos(0x0, -38700, 5600, 98200, 90)

    label("loc_11F98")

    SetScenarioFlags(0x85, 2)
    EventEnd(0x5)
    Return()

    # Function_61_11D97 end

    def Function_62_11F9E(): pass

    label("Function_62_11F9E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_12008")
    OP_68(48600, 6900, 14800, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 48600, 5600, 15800, 270)
    SetChrPos(0x102, 48600, 5600, 14800, 270)
    Jump("loc_12061")

    label("loc_12008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_12061")
    OP_68(-38700, 6900, 97200, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -38700, 5600, 98200, 90)
    SetChrPos(0x102, -38700, 5600, 97200, 90)

    label("loc_12061")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#2201479V#0012FHaha. It looks like Dudley IS interested in\x01",
            "the play, after all.\x02\x03",
            "#2201480V#0000FNot that it's making him neglect his work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201481V#0104FI can hardly blame him.\x02\x03",
            "#2201482V#0100FI bet there isn't a soul that would be unmoved\x01",
            "by one of Arc en Ciel's performances.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_121AE")
    SetChrPos(0x0, 48600, 5600, 15800, 270)
    Jump("loc_121C8")

    label("loc_121AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_121C8")
    SetChrPos(0x0, -38700, 5600, 98200, 90)

    label("loc_121C8")

    SetScenarioFlags(0x85, 6)
    EventEnd(0x5)
    Return()

    # Function_62_11F9E end

    def Function_63_121CE(): pass

    label("Function_63_121CE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-46700, 12500, 124000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -47700, 11200, 124000, 0)
    SetChrPos(0x102, -46700, 11200, 124000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#2201483V#0005F(This is the box for special guests...)\x02\x03",
            "#2201484V#0001F(Will everything be all right with only\x01",
            "one officer keeping watch?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201485V#0104F(At least Ernest is there to protect Grandfather.)\x02\x03",
            "#2201486V#0100F(If anything were to happen, I'm sure he can deal\x01",
            "with it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201487V#0000F(You think so?)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -47700, 11200, 124000, 0)
    SetScenarioFlags(0x84, 7)
    EventEnd(0x5)
    Return()

    # Function_63_121CE end

    def Function_64_12395(): pass

    label("Function_64_12395")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-46700, 12500, 124000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -47700, 11200, 124000, 0)
    SetChrPos(0x102, -46700, 11200, 124000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#2201488V#0003F(This side looks good.)\x02\x03",
            "#2201489V#0001F(But I think the officer assigned here\x01",
            "has gotten a little...preoccupied.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201490V#0106F(We ARE in the middle of an Arc en Ciel\x01",
            "play. Everyone's bound to be captivated.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -47700, 11200, 124000, 0)
    SetScenarioFlags(0x85, 3)
    EventEnd(0x5)
    Return()

    # Function_64_12395 end

    def Function_65_12502(): pass

    label("Function_65_12502")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-46700, 12500, 124000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -47700, 11200, 124000, 0)
    SetChrPos(0x102, -46700, 11200, 124000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#2201491V#0000F(Nothing suspicious here.)\x02\x03",
            "#2201492V(Officer aside, it looks like Ernest is paying\x01",
            "real close attention to their perimeter...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201493V#0100F(He'll stay on his toes. I know it.)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -47700, 11200, 124000, 0)
    SetScenarioFlags(0x85, 7)
    EventEnd(0x5)
    Return()

    # Function_65_12502 end

    def Function_66_1264F(): pass

    label("Function_66_1264F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126BE")
    OP_68(-7980, 3950, 13760, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8080, 2500, 14570, 90)
    SetChrPos(0x102, -8119, 2500, 13410, 89)
    Jump("loc_12771")

    label("loc_126BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12721")
    OP_68(7630, 3950, 13800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 7700, 2500, 14490, 270)
    SetChrPos(0x102, 7730, 2500, 13470, 270)
    Jump("loc_12771")

    label("loc_12721")

    OP_68(-8270, 1450, 4900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8310, 10, 5560, 89)
    SetChrPos(0x102, -8300, 10, 4420, 89)

    label("loc_12771")

    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x93, 1)
    ClearScenarioFlags(0x93, 2)
    ClearScenarioFlags(0x93, 3)
    Sound(875, 0, 100, 0)
    Sleep(1000)
    Sound(876, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    StopBGM(0x1388)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2201494V#0005FDoes that mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201495V#0100FYes. That should conclude the first act.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(2000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5D, 4)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_66_1264F end

    def Function_67_12860(): pass

    label("Function_67_12860")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-460, 3950, 12700, 0)
    MoveCamera(29, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -890, 2500, 12720, 0)
    SetChrPos(0x102, 210, 2500, 12660, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#2201500V#0004F#5PSounds like the second act is starting.\x02\x03",
            "#2201501V#0002FRixia's giving it her all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201502V#0104FTrue. Her debut scene was met\x01",
            "with thunderous applause.\x02\x03",
            "#2201503V#0100FShall we make another round, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201504V#0000F#5PDefinitely!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -890, 2500, 12720, 0)
    SetScenarioFlags(0x85, 0)
    OP_29(0x43, 0x1, 0xB)
    EventEnd(0x5)
    Return()

    # Function_67_12860 end

    def Function_68_129F0(): pass

    label("Function_68_129F0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A5F")
    OP_68(-7980, 3950, 13760, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8080, 2500, 14570, 90)
    SetChrPos(0x102, -8119, 2500, 13410, 89)
    Jump("loc_12B12")

    label("loc_12A5F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AC2")
    OP_68(7630, 3950, 13800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 7700, 2500, 14490, 270)
    SetChrPos(0x102, 7730, 2500, 13470, 270)
    Jump("loc_12B12")

    label("loc_12AC2")

    OP_68(-8270, 1450, 4900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8310, 10, 5560, 89)
    SetChrPos(0x102, -8300, 10, 4420, 89)

    label("loc_12B12")

    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x93, 1)
    ClearScenarioFlags(0x93, 2)
    ClearScenarioFlags(0x93, 3)
    Sound(875, 0, 100, 0)
    Sleep(1000)
    Sound(876, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    StopBGM(0x1388)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2201505V#0000FAnd that's the end of the second act.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201506V#0104FThings are starting to heat up, aren't\x01",
            "they?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(2000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5D, 5)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_68_129F0 end

    def Function_69_12C18(): pass

    label("Function_69_12C18")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-460, 3950, 12700, 0)
    MoveCamera(29, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -890, 2500, 12720, 0)
    SetChrPos(0x102, 210, 2500, 12660, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#2201512V#0000F#5PThe third act is where things usually start\x01",
            "turning around for the protagonists, right?\x02\x03",
            "#2201513V#0012FThe audience seems to be eating it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201514V#0104FI know I am. It's rare to see a play THIS\x01",
            "marvelous. It's more or less perfect.\x02\x03",
            "#2201515V#0108FNow, if only it would end without incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201516V#0006F#5PYeah. I sure hope so, too...\x02\x03",
            "#2201517V#0000FEven if it means that we don't catch the\x01",
            "culprit, it would be for the best.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -890, 2500, 12720, 0)
    SetScenarioFlags(0x85, 4)
    OP_29(0x43, 0x1, 0xC)
    EventEnd(0x5)
    Return()

    # Function_69_12C18 end

    def Function_70_12E76(): pass

    label("Function_70_12E76")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12EE5")
    OP_68(-7980, 3950, 13760, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8080, 2500, 14570, 90)
    SetChrPos(0x102, -8119, 2500, 13410, 89)
    Jump("loc_12F98")

    label("loc_12EE5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F48")
    OP_68(7630, 3950, 13800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 7700, 2500, 14490, 270)
    SetChrPos(0x102, 7730, 2500, 13470, 270)
    Jump("loc_12F98")

    label("loc_12F48")

    OP_68(-8270, 1450, 4900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -8310, 10, 5560, 89)
    SetChrPos(0x102, -8300, 10, 4420, 89)

    label("loc_12F98")

    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(875, 0, 100, 0)
    Sleep(1000)
    Sound(876, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    StopBGM(0x1388)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2201518V#0001FThat's the end of the third act.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201519V#0101FNow the final act begins.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(2000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5D, 6)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_70_12E76 end

    def Function_71_1307D(): pass

    label("Function_71_1307D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-280, 1450, -290, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    ClearChrFlags(0xB, 0x4)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0x101, 500, 0, -100, 0)
    SetChrPos(0x102, -740, 0, 330, 0)
    SetChrPos(0xB, -440, 2500, 15470, 180)
    PlayBGM("ed7531", 0)
    VolumeBGM(0x32, 0x64)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x213), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#2201527V#0004F#11PPhew. Thank Aidios.\x02\x03",
            "#2201528V#0000FIt looks like the play is going to wrap\x01",
            "up accident-free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201529V#0104F#5PAnd we didn't even notice anything\x01",
            "suspicious during our patrols, too.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Man's Voice",
        "#2201530VLloyd, Elie!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1323C():

        label("loc_1323C")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_1323C")

    QueueWorkItem2(0x101, 0, lambda_1323C)

    def lambda_1324E():

        label("loc_1324E")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_1324E")

    QueueWorkItem2(0x102, 0, lambda_1324E)
    Fade(500)
    OP_68(-260, 3950, 11720, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_68(190, 1450, 500, 3000)
    MoveCamera(45, 27, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15000, 3000)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xB, 310, 10, 2240, 4000, 0x0)
    OP_64(0xB)

    ChrTalk(
        0x101,
        "#2201531V#0005F#12PWhat's going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201532V#0105F#6PIs something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#2201533V#5PWell, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2201534V#5POne of the attendees has been behaving\x01",
            "unusually for a while now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2201535V#5PAnd we only just realized that she's not\x01",
            "on our guest list.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)

    ChrTalk(
        0x101,
        "#2201536V#0011F#12PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201537V#0101F#6PWhere is she?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#2201538V#5PUp the stairs on the right! In the back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2201539V#5PShe seems to be silently observing the\x01",
            "S section seats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201540V#0013F#12PGot it! We'll go check it out right away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201541V#0101F#6PStay here and wait for our return, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#2201542V#5PO-Of course!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -240, 0, -190, 0)
    SetChrPos(0xB, 1640, 0, 3600, 225)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x86, 0)
    OP_29(0x43, 0x1, 0xD)
    OP_63(0xB, 0x0, 1900, 0x28, 0x2B, 0x64, 0x0)
    OP_1B(0x3, 0x0, 0x55)
    OP_1B(0x4, 0x0, 0x54)
    OP_1B(0x0, 0x0, 0x57)
    EventEnd(0x5)
    Return()

    # Function_71_1307D end

    def Function_72_135F8(): pass

    label("Function_72_135F8")

    OP_92(0xFE, 0xBC98, 0x38A4, 0x320)
    OP_95(0xFE, 48280, 5600, 14500, 5000, 0x1)

    def lambda_1361E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1361E)
    OP_95(0xFE, 46280, 5600, 14900, 5000, 0x1)
    Return()

    # Function_72_135F8 end

    def Function_73_1363F(): pass

    label("Function_73_1363F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    OP_68(48850, 1300, 800, 0)
    MoveCamera(52, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 48060, 0, 480, 0)
    SetChrPos(0x102, 49680, 0, 560, 0)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 49400, 5600, 15100, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2201543V#0005F#5P(No way!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201544V#0101F#11P(Is that who I think it is?!)\x02",
    )

    CloseMessageWindow()
    OP_68(49230, 6900, 14230, 3000)
    MoveCamera(27, 22, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17000, 3000)
    Sleep(3000)

    ChrTalk(
        0x1E,
        (
            "#2201545V#2101F#11POh, darn it! Why'd Duddles have to\x01",
            "pick THIS spot to patrol?!\x02\x03",
            "#2201546VThis was the perfect spot to wait for my\x01",
            "big scoop, and he...is...ruining it!\x02\x03",
            "#2201547V#2106FHe's totally gonna catch me once I start\x01",
            "firing off my camera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201548VHey, Grace!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(49230, 6900, 14230, 3000)
    MoveCamera(44, 18, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17000, 3000)

    def lambda_138F6():
        OP_95(0xFE, 49000, 5600, 13200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_138F6)
    OP_93(0x1E, 0xB4, 0x1F4)

    def lambda_13917():
        OP_95(0xFE, 50400, 5600, 13200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_13917)
    WaitChrThread(0x101, 0)

    ChrTalk(
        0x1E,
        (
            "#2201549V#2105F#5PWhoa! Lloyd?!\x02\x03",
            "#2201550VAnd Elie, too? What in the world are\x01",
            "you guys doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201551V#0013F#12PThat's supposed to be my line!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201552V#0101FWhat are YOU doing here, Grace?\x02\x03",
            "#2201553VYou don't have a ticket, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#2201554V#2109F#5PUh...haha. Nope! But I have my reasons.\x02\x03",
            "#2201555VI...may have snuck in here using\x01",
            "a trick up my sleeve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201556V#0105FWhich was what, exactly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#2201557V#2106F#5PKeep this a secret, will you?\x02\x03",
            "#2201558V#2102FLong story short, I slipped in with the dry\x01",
            "cleaning, and voila! I was home free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201559V#0011F#12PAre you kidding me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201560V#0101FWhy did you have to go that far?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#2201561V#2106F#5PWell, there's a simple explanation for that.\x01",
            "Y'see, all of the friggin' tickets got snatched\x01",
            "up by the other CNS journalists!\x02\x03",
            "#2201562V#2110FI just HAD to take a peek at the private show,\x01",
            "but I was following another story at the time...\x01",
            "What was I supposed to do, NOT watch it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201563V#0006F#12PThat still doesn't make it right. Or legal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201564V#0106FYou're a real hassle, you know that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#2201565V#2102F#5PC-C'mon, guys! We're all friends here! How\x01",
            "about we go watch the rest of the play?\x02\x03",
            "#2201566V#2109FIt's finally reached the long-awaited climax,\x01",
            "after all! If we don't see it, we may regret it\x01",
            "for the rest of our lives!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201567V#0003F#12PYou could have just waited for the\x01",
            "public show like a normal person.\x02\x03",
            "#2201568V#0013FBesides, are you SURE that's your only\x01",
            "reason for sneaking in?\x02\x03",
            "#2201569VYou're not the one who sent the\x01",
            "threat letter, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#2201570V#2105F#5PTh-Threat letter?! What the heck\x01",
            "are you going on about?!\x02\x03",
            "#2201571VHold on... I thought it was kinda strange\x01",
            "to see Duddles patrolling the theater.\x02\x03",
            "#2201572V#2101FOoh, ooh! It has to do with this letter, right?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201573V#0108FI don't think she's our culprit, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201574V#0000F#12PY-Yeah. I figured it wouldn't hurt to ask.\x02\x03",
            "#2201575VI doubt even Grace would take\x01",
            "things that far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#2201576V#2101F#5PEven me, eh? Isn't that sorta rude?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201577V#0006F#12PIs it? You literally decided to sneak into a\x01",
            "private performance for a 'big scoop.'\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#2201578V#0001F#12POh, that reminds me. You mentioned that\x01",
            "you were following another story, right?\x02\x03",
            "#2201579VWhat's it about?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1E,
        (
            "#2201580V#2102F#5PNuh-uh-uh. My lips are sealed.\x02\x03",
            "#2201581V#2105FWait a second... Is the First Division\x01",
            "here because they're keeping tabs\x01",
            "on him?\x02\x03",
            "#2201582V#2106FDrat! I thought I was the only one to\x01",
            "have picked up on it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201583V#0005F#12P'Him'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201584V#0101FAre you referring to Yin?\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x1E,
        (
            "#2201585V#2105F#5PHuh? The heck's a Yin supposed to be?\x02\x03",
            "#2201586V#2101FDoes that have something to do with that\x01",
            "threat letter you're freaking out about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201587V#0105FN-No. Forget about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201588V#0003F#12PListen up, Grace. I'm going to need you\x01",
            "to tell me everything you know.\x02\x03",
            "#2201589V#0013FIf you don't, we'll have to take you in\x01",
            "for trespassing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1E,
        (
            "#2201590V#2105F#5PWhoa, Lloyd! Isn't that a little cruel?\x02\x03",
            "#2201591V#2109FYou and I are buddies, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201592V#0006F#12PSure. But what we need now is some\x01",
            "sort of clue, no matter how small it is.\x02\x03",
            "#2201593V#0013FSo please, Grace. Tell us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#2201594V#2106F#5P*sigh* Fine, fine. You're serious, right?\x02\x03",
            "#2201595V#2100FI'll spill the beans, but are you sure you\x01",
            "want to talk about this in front of Elie?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#2201596V#0005F#12PWhy would we not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201597V#0101FIs there something wrong with me\x01",
            "being here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#2201598V#2103F#5POh, whatever. Just brace yourselves, okay?\x02\x03",
            "#2201599V#2101FThe scoop I've been chasing involves a\x01",
            "dark rumor about the mayor's secretary.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#2201600V#0105F...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201601V#0007F#12PYou can't be serious!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#2201602V#2104F#5PI think his name is...Ernest? Either way, he's\x01",
            "extremely dangerous, with a capital D.\x02\x03",
            "#2201603V#2102FHe's supposedly been secretly embezzling\x01",
            "funds from the mayor's office...\x02\x03",
            "#2201604VAnd here's the kicker. He's been\x01",
            "covertly scheming with the Imperial\x01",
            "Faction diet members.\x02\x03",
            "#2201605V#2109FYou think he's trying to off the mayor?\x01",
            "Naaah. Probably too far fetched.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#2201606V#0108FH-Hey, Lloyd. I just had a thought...\x02\x03",
            "#2201607V#0101FIf Grandfather were to be killed\x01",
            "under these circumstances...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#2201608V#0005F#6PThe culprit could easily slip out during\x01",
            "all the commotion, so long as no one\x01",
            "witnesses the crime in action...\x02\x03",
            "#2201609V#0010FThat's it! That's his plan!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(49110, 6900, 15180, 1000)
    BeginChrThread(0x101, 0, 0, 72)
    Sleep(500)
    Sound(103, 0, 100, 0)
    BeginChrThread(0x102, 0, 0, 72)
    OP_93(0x1E, 0x10E, 0x1F4)
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1E,
        "#2201610V#2105F#11PWh-Whoa! Wait up!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x87, 5)
    SetScenarioFlags(0x5D, 7)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_73_1363F end

    def Function_74_14C3C(): pass

    label("Function_74_14C3C")


    def lambda_14C41():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14C41)
    OP_95(0xFE, -38080, 5600, 97990, 6000, 0x0)
    OP_95(0xFE, -47290, 5600, 107210, 6000, 0x0)
    OP_95(0xFE, -47070, 11200, 117460, 6000, 0x0)
    OP_95(0xFE, -47270, 11200, 123420, 6000, 0x0)
    TurnDirection(0xFE, 0x20, 800)
    Return()

    # Function_74_14C3C end

    def Function_75_14CA5(): pass

    label("Function_75_14CA5")


    def lambda_14CAA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14CAA)
    OP_95(0xFE, -38080, 5600, 97990, 6000, 0x0)
    OP_95(0xFE, -47290, 5600, 107210, 6000, 0x0)
    OP_95(0xFE, -47070, 11200, 117460, 6000, 0x0)
    OP_95(0xFE, -46940, 11200, 122160, 6000, 0x0)
    TurnDirection(0xFE, 0x20, 800)
    Return()

    # Function_75_14CA5 end

    def Function_76_14D0E(): pass

    label("Function_76_14D0E")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x1000)
    OP_52(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_92(0xFE, 0xFFFF4854, 0x1E672, 0x320)
    OP_95(0xFE, -47020, 11200, 124530, 6000, 0x0)

    def lambda_14D49():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14D49)
    OP_95(0xFE, -47020, 11200, 126530, 6000, 0x0)
    Return()

    # Function_76_14D0E end

    def Function_77_14D6A(): pass

    label("Function_77_14D6A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("apl/ch50222.itc", 0x1F)
    OP_68(-46700, 12500, 124000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -36500, 5600, 97990, 0)
    SetChrPos(0x102, -36500, 5600, 97990, 0)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -47470, 8000, 112190, 93)
    ClearChrFlags(0x1F, 0x4)
    SetChrFlags(0x20, 0x2)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x20, 0x1F)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -45230, 11200, 123570, 45)
    OP_6B(0x101)
    OP_68(-36500, 7050, 97990, 0)
    MoveCamera(57, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x6, 0x0, 0x5, 0x0, 0x0)
    ClearMapObjFlags(0x6, 0x2)
    Sound(103, 0, 100, 0)
    OP_79(0x6)
    MoveCamera(20, 22, 0, 7000)
    OP_6E(500, 7000)
    SetCameraDistance(19500, 7000)
    BeginChrThread(0x101, 0, 0, 74)
    Sleep(500)
    BeginChrThread(0x102, 0, 0, 75)
    Sleep(4000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x101, 0)

    ChrTalk(
        0x101,
        (
            "#2201612V#0010F#5PIsn't this the police officer who was\x01",
            "watching the box?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201613V#0101F#5PIt is!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(1559, 255, 100, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)

    def lambda_14F75():
        OP_95(0xFE, -47100, 11200, 119630, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_14F75)
    WaitChrThread(0x1F, 0)
    Sleep(150)

    ChrTalk(
        0x1F,
        "#2201615V#0607F#5PWhat the hell are you doing here?\x02",
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x1F,
        "#2201616V#0605F#5PWhat?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1F, 800)

    ChrTalk(
        0x101,
        "#2201617V#0007F#5PWe'll talk later! Elie, we're going in!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 800)

    ChrTalk(
        0x102,
        "#2201618V#0101FLet's hurry!\x02",
    )

    CloseMessageWindow()
    OP_71(0x7, 0x0, 0x5, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x2)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    BeginChrThread(0x101, 0, 0, 76)
    Sleep(100)
    BeginChrThread(0x102, 0, 0, 76)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5E, 0)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_77_14D6A end

    def Function_78_150C7(): pass

    label("Function_78_150C7")


    def lambda_150CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_150CC)
    OP_95(0xFE, -47010, 11200, 124560, 8000, 0x1)
    OP_95(0xFE, -47090, 11200, 117520, 8000, 0x1)
    OP_95(0xFE, -46520, 5600, 107590, 8000, 0x1)
    OP_95(0xFE, -41100, 5600, 100220, 8000, 0x1)
    OP_95(0xFE, -40120, 5600, 93460, 8000, 0x1)
    OP_95(0xFE, -39900, 0, 83980, 8000, 0x1)
    OP_95(0xFE, -37970, 0, 81930, 8000, 0x1)

    def lambda_15169():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15169)
    OP_95(0xFE, -36970, 0, 81930, 7000, 0x0)
    Return()

    # Function_78_150C7 end

    def Function_79_1518A(): pass

    label("Function_79_1518A")


    def lambda_1518F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1518F)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    OP_95(0xFE, -47010, 11200, 124560, 10000, 0x1)
    OP_95(0xFE, -47090, 11200, 117520, 10000, 0x1)
    OP_95(0xFE, -46520, 5600, 107590, 10000, 0x1)
    OP_95(0xFE, -41100, 5600, 100220, 10000, 0x1)
    OP_95(0xFE, -40120, 5600, 93460, 10000, 0x1)
    OP_9D(0xFE, 0xFFFF6424, 0x0, 0x1480C, 0x7D0, 0xBB8)
    OP_95(0xFE, -37970, 0, 81930, 10000, 0x1)

    def lambda_15237():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15237)
    OP_95(0xFE, -36970, 0, 81930, 7000, 0x0)
    Return()

    # Function_79_1518A end

    def Function_80_15258(): pass

    label("Function_80_15258")


    def lambda_1525D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1525D)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    OP_95(0xFE, -8490, 2500, 14030, 10000, 0x1)
    OP_95(0xFE, -1990, 2500, 13340, 10000, 0x1)
    OP_95(0xFE, -720, 2500, 11820, 10000, 0x1)
    OP_95(0xFE, -290, 0, -5210, 10000, 0x1)

    def lambda_152C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_152C6)
    OP_95(0xFE, -36970, 0, 81930, 600, 0x0)
    Return()

    # Function_80_15258 end

    def Function_81_152E7(): pass

    label("Function_81_152E7")


    def lambda_152EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_152EC)
    OP_95(0xFE, -8490, 2500, 14030, 6000, 0x1)
    OP_95(0xFE, -1990, 2500, 13340, 6000, 0x1)
    OP_95(0xFE, 1100, 2500, 11650, 6000, 0x1)
    OP_93(0xFE, 0xB4, 0x2BC)
    Return()

    # Function_81_152E7 end

    def Function_82_1533C(): pass

    label("Function_82_1533C")


    def lambda_15341():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15341)
    OP_95(0xFE, -8490, 2500, 14030, 6000, 0x1)
    OP_95(0xFE, -1990, 2500, 13340, 6000, 0x1)
    OP_95(0xFE, -720, 2500, 11820, 6000, 0x1)
    OP_93(0xFE, 0xB4, 0x2BC)
    Return()

    # Function_82_1533C end

    def Function_83_15391(): pass

    label("Function_83_15391")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50229.itc", 0x1E)
    LoadChrToIndex("apl/ch50222.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x28)
    LoadChrToIndex("chr/ch00051.itc", 0x29)
    LoadChrToIndex("apl/ch50011.itc", 0x2A)
    LoadChrToIndex("chr/ch00950.itc", 0x32)
    LoadChrToIndex("chr/ch00951.itc", 0x33)
    OP_71(0x7, 0x5, 0x5, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x2)
    OP_71(0x5, 0x5, 0x5, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x2)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x10)
    OP_68(-46700, 12500, 124000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrChipByIndex(0x101, 0x28)
    SetChrChipByIndex(0x1F, 0x33)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -47300, 11200, 118500, 0)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -46200, 11200, 121500, 315)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x4)
    SetChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1D, 0x4)
    SetChrPos(0x102, -47010, 11200, 125500, 0)
    SetChrPos(0x101, -47010, 11200, 125500, 0)
    SetChrPos(0x1F, -47010, 11200, 125500, 0)
    SetChrPos(0x1D, -47010, 11200, 125500, 0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -47700, 11200, 124000, 0)
    SetChrFlags(0x20, 0x2)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x20, 0x1F)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -45230, 11200, 123570, 45)
    OP_64(0xB)
    OP_64(0xC)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    FadeToBright(1000, 0)
    BeginChrThread(0x1D, 0, 0, 79)
    OP_68(-47130, 12500, 117520, 0)
    MoveCamera(68, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    OP_68(-46470, 8900, 108360, 3000)
    MoveCamera(113, 22, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(21500, 3000)
    Sleep(3000)
    Fade(500)
    OP_6B(0x101)
    OP_68(-47010, 12500, 125500, 0)
    MoveCamera(32, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    BeginChrThread(0x101, 0, 0, 78)
    Sleep(500)
    BeginChrThread(0x1F, 0, 0, 78)
    WaitChrThread(0x101, 0)
    Fade(500)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x1F, 0xFF)
    EndChrThread(0x1D, 0xFF)
    SetChrPos(0x101, -9490, 2500, 14030, 90)
    SetChrPos(0x1F, -9490, 2500, 14030, 90)
    SetChrPos(0x1D, -9490, 2500, 14030, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6B(0xFF)
    OP_68(-4290, 3950, 13100, 0)
    MoveCamera(39, 18, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18500, 0)
    OP_68(0, 3290, 10040, 4000)
    MoveCamera(67, 18, 0, 4000)
    OP_6E(540, 4000)
    SetCameraDistance(18500, 4000)
    BeginChrThread(0x1D, 0, 0, 80)
    Sleep(2000)
    BeginChrThread(0x101, 0, 0, 81)
    Sleep(1000)
    BeginChrThread(0x1F, 0, 0, 82)
    WaitChrThread(0x1F, 0)
    SetChrChipByIndex(0x1F, 0x32)
    SetChrSubChip(0x1F, 0x0)

    ChrTalk(
        0x1F,
        "#2201663V#0607FHow's he moving so quickly?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
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
            "#2201664V#0007FRandy, Tio! Brace yourselves! Mayor\x01",
            "MacDowell's secretary is headed your way!\x02\x03",
            "#2201665VHe's our man! Take him down!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Randy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2201666V\x07\x05",
            "G-Got'cha! We'll get him!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2201667V\x07\x05",
            "Ernest? Very well, then.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 1)
    NewScene("c040B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_83_15391 end

    def Function_84_158FE(): pass

    label("Function_84_158FE")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 88)
    SetChrPos(0x0, -8200, 0, 4980, 90)
    EventEnd(0x4)
    Return()

    # Function_84_158FE end

    def Function_85_1591A(): pass

    label("Function_85_1591A")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 88)
    SetChrPos(0x0, -8260, 2500, 14010, 90)
    EventEnd(0x4)
    Return()

    # Function_85_1591A end

    def Function_86_15936(): pass

    label("Function_86_15936")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 88)
    SetChrPos(0x0, 5760, 2500, 13790, 270)
    EventEnd(0x4)
    Return()

    # Function_86_15936 end

    def Function_87_15952(): pass

    label("Function_87_15952")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1596D")
    Call(0, 88)
    Jump("loc_15A29")

    label("loc_1596D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15983")
    Call(0, 88)
    Jump("loc_15A29")

    label("loc_15983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15999")
    Call(0, 88)
    Jump("loc_15A29")

    label("loc_15999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15A29")

    ChrTalk(
        0x101,
        (
            "#0000FWe don't have time to leave the theater.\x02\x03",
            "Let's leave the outside to Randy and Tio\x01",
            "and focus on securing the interior.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A29")

    SetChrPos(0x0, 0, 0, -4730, 0)
    EventEnd(0x4)
    Return()

    # Function_87_15952 end

    def Function_88_15A3D(): pass

    label("Function_88_15A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15AB2")

    ChrTalk(
        0x101,
        (
            "#0005FOh, yeah. We're supposed to meet\x01",
            "with Ilya.\x02\x03",
            "#0000FShe should be right past the main doors.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15B68")

    ChrTalk(
        0x101,
        (
            "#0000FI think this staircase leads to the second\x01",
            "floor seats.\x02\x03",
            "We'll just end up being a nuisance if we\x01",
            "stick around too long, so let's not.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15D09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15CA8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C26")

    ChrTalk(
        0x103,
        (
            "#0205FIs that music?\x02\x03",
            "#0200FI believe it is coming from the main stage.\x01",
            "Ilya must still be practicing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FProbably. Let's head on in.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15CA0")

    label("loc_15C26")


    ChrTalk(
        0x103,
        (
            "#0200FI hear music coming from the main stage.\x01",
            "Ilya must still be practicing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FProbably. Let's head on in.\x02",
    )

    CloseMessageWindow()

    label("loc_15CA0")

    SetScenarioFlags(0x1, 4)
    Jump("loc_15D09")

    label("loc_15CA8")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ilya seems to still be on stage. Try entering\x01",
            "the auditorium through the main doors.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_15D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15E21")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15DA5")

    ChrTalk(
        0x102,
        (
            "#0101FThe suspicious person is up the stairs\x01",
            "to the right, Lloyd. Let's go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FRight! We've no time to spare!\x02",
    )

    CloseMessageWindow()
    Jump("loc_15E21")

    label("loc_15DA5")


    ChrTalk(
        0x101,
        (
            "#0001FThe individual we're looking for is up the\x01",
            "stairs on the right. Let's go, Elie!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0101FI'm right behind you!\x02",
    )

    CloseMessageWindow()

    label("loc_15E21")

    Return()

    # Function_88_15A3D end

    def Function_89_15E22(): pass

    label("Function_89_15E22")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "To our guests: Please do not enter\x01",
            "while the stage is in use.\x01",
            "                  - Arc en Ciel\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15F67")

    ChrTalk(
        0x101,
        (
            "#0000FThe First Division was stationed backstage.\x01",
            "We can leave this area to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FWe should focus on patrolling the\x01",
            "interior of the theater instead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F67")

    TalkEnd(0xFF)
    Return()

    # Function_89_15E22 end

    SaveToFile()

Try(main)
