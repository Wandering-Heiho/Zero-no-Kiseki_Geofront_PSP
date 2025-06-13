from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c011b.bin",                # FileName
        "c011b",                    # MapName
        "c011b",                    # Location
        0x0009,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 1000, 0, 2000, 0, 0, 1, 9, 0, 1, 0, 2],
    )

    BuildStringList((
        "c011b",                  # 0
        "Randy",                  # 1
        "Randy",                  # 2
        "Elie",                   # 3
        "Tio",                    # 4
        "Tio",                    # 5
        "KeA",                    # 6
        "KeA",                    # 7
        "Zeit",                   # 8
        "Zeit",                   # 9
        "Chief Sergei",           # 10
        "Chief Sergei",           # 11
        "Mr. Grimwood",           # 12
        "Shizuku",                # 13
        "CGF Guardsman",          # 14
        "CGF Guardsman",          # 15
        "本",                     # 16
        "Tableware",              # 17
        "Tableware",              # 18
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch00300.itc",                   # 01
        "chr/ch00100.itc",                   # 02
        "chr/ch00200.itc",                   # 03
        "chr/ch08200.itc",                   # 04
        "chr/ch02700.itc",                   # 05
        "chr/ch02502.itc",                   # 06
        "chr/ch02702.itc",                   # 07
        "chr/ch08202.itc",                   # 08
        "chr/ch00202.itc",                   # 09
        "chr/ch00302.itc",                   # 0A
        "chr/ch02707.itc",                   # 0B
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

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(51840,   150,     126410,  270,  405,  0x0, 0,   10,  0,   255, 255, 0,   3,   255,  0)
    DeclNpc(157419,  0,       128649,  0,    389,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(205529,  29,      128350,  45,   389,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(203660,  150,     128610,  0,    389,  0x0, 0,   9,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(2710,    0,       2509,    225,  404,  0x0, 0,   11,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(102910,  0,       72099,   90,   389,  0x0, 0,   0,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(101139,  150,     65339,   180,  389,  0x0, 0,   6,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 20,  4.0,                   10.5,                  0.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -2.0,                  -2.0999999046325684,   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 58,  1.350000023841858,     12.390000343322754,    0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.675000011920929,    -6.195000171661377,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 60,  206.02999877929688,    121.13999938964844,    -1.0,                  1.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  1.0,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -103.01499938964844,   -121.13999938964844,   0.20000000298023224,   1.0])

    DeclActor(14000,   0,       63800,   2000,    14000,   1000,    63800,   0x007C, 0,  11, 0x0000)
    DeclActor(164000,  0,       63800,   2000,    164000,  1000,    63800,   0x007C, 0,  12, 0x0000)
    DeclActor(164000,  0,       63800,   2000,    164000,  1000,    63800,   0x007C, 0,  13, 0x0000)
    DeclActor(16960,   850,     10840,   2000,    16960,   1300,    10840,   0x007C, 0,  15, 0x0000)
    DeclActor(180910,  0,       62020,   1500,    180910,  1500,    62020,   0x007C, 0,  61, 0x0000)
    DeclActor(19980,   0,       63920,   1500,    19980,   1500,    63920,   0x007C, 0,  61, 0x0000)
    DeclActor(175940,  0,       63930,   1500,    175940,  1500,    63930,   0x007C, 0,  61, 0x0000)
    DeclActor(-3150,   0,       122280,  1200,    -3150,   1000,    122280,  0x007C, 0,  71, 0x0000)
    DeclActor(-2300,   0,       129960,  1200,    -2300,   2000,    129960,  0x007C, 0,  72, 0x0000)
    DeclActor(155150,  30,      129699,  1200,    153340,  2029,    130490,  0x007C, 0,  73, 0x0000)
    DeclActor(155120,  30,      123880,  1200,    155120,  2029,    123880,  0x007C, 0,  74, 0x0000)
    DeclActor(207280,  30,      128039,  1200,    208840,  3000,    130410,  0x007C, 0,  75, 0x0000)
    DeclActor(209020,  0,       126830,  1200,    209210,  2000,    127040,  0x007C, 0,  76, 0x0000)
    DeclActor(51920,   0,       130570,  1200,    51920,   2500,    130570,  0x007C, 0,  77, 0x0000)
    DeclActor(52900,   0,       124470,  1200,    53700,   2000,    125270,  0x007C, 0,  78, 0x0000)
    DeclActor(2750,    0,       125420,  1200,    2750,    1500,    125420,  0x007C, 0,  80, 0x0000)
    DeclActor(153580,  30,      127880,  1200,    153370,  1530,    128389,  0x007C, 0,  81, 0x0000)
    DeclActor(207040,  30,      128539,  1200,    207640,  1500,    129090,  0x007C, 0,  82, 0x0000)
    DeclActor(48000,   30,      127860,  1200,    47560,   1500,    128630,  0x007C, 0,  83, 0x0000)
    DeclActor(170000,  0,       63800,   2000,    170000,  1000,    63800,   0x007C, 0,  14, 0x0000)

    ScpFunction((
        "Function_0_844",          # 00, 0
        "Function_1_8FC",          # 01, 1
        "Function_2_CF7",          # 02, 2
        "Function_3_1149",         # 03, 3
        "Function_4_15B6",         # 04, 4
        "Function_5_16B2",         # 05, 5
        "Function_6_188A",         # 06, 6
        "Function_7_1C29",         # 07, 7
        "Function_8_1C97",         # 08, 8
        "Function_9_1DFC",         # 09, 9
        "Function_10_2052",        # 0A, 10
        "Function_11_2399",        # 0B, 11
        "Function_12_239D",        # 0C, 12
        "Function_13_23A1",        # 0D, 13
        "Function_14_23A5",        # 0E, 14
        "Function_15_23A9",        # 0F, 15
        "Function_16_2404",        # 10, 16
        "Function_17_32CF",        # 11, 17
        "Function_18_3759",        # 12, 18
        "Function_19_49C4",        # 13, 19
        "Function_20_5DF3",        # 14, 20
        "Function_21_7475",        # 15, 21
        "Function_22_7DDF",        # 16, 22
        "Function_23_9643",        # 17, 23
        "Function_24_9DCB",        # 18, 24
        "Function_25_A0E7",        # 19, 25
        "Function_26_F699",        # 1A, 26
        "Function_27_1055E",       # 1B, 27
        "Function_28_10623",       # 1C, 28
        "Function_29_10731",       # 1D, 29
        "Function_30_107AA",       # 1E, 30
        "Function_31_10823",       # 1F, 31
        "Function_32_12B43",       # 20, 32
        "Function_33_12B98",       # 21, 33
        "Function_34_12BED",       # 22, 34
        "Function_35_12C42",       # 23, 35
        "Function_36_1606B",       # 24, 36
        "Function_37_1608A",       # 25, 37
        "Function_38_19777",       # 26, 38
        "Function_39_198A6",       # 27, 39
        "Function_40_199A8",       # 28, 40
        "Function_41_19AD1",       # 29, 41
        "Function_42_19B62",       # 2A, 42
        "Function_43_19BD5",       # 2B, 43
        "Function_44_19C66",       # 2C, 44
        "Function_45_19D0A",       # 2D, 45
        "Function_46_19DAE",       # 2E, 46
        "Function_47_1A482",       # 2F, 47
        "Function_48_1A4A8",       # 30, 48
        "Function_49_1A4DB",       # 31, 49
        "Function_50_1A53F",       # 32, 50
        "Function_51_1A5B0",       # 33, 51
        "Function_52_1A605",       # 34, 52
        "Function_53_1A65A",       # 35, 53
        "Function_54_1A6AF",       # 36, 54
        "Function_55_1A722",       # 37, 55
        "Function_56_1A795",       # 38, 56
        "Function_57_1A923",       # 39, 57
        "Function_58_1AA1D",       # 3A, 58
        "Function_59_1ABB4",       # 3B, 59
        "Function_60_1AD6E",       # 3C, 60
        "Function_61_1AE85",       # 3D, 61
        "Function_62_1AF3A",       # 3E, 62
        "Function_63_1B10E",       # 3F, 63
        "Function_64_1B2E2",       # 40, 64
        "Function_65_1B4BC",       # 41, 65
        "Function_66_1B6A1",       # 42, 66
        "Function_67_1B870",       # 43, 67
        "Function_68_1BA3F",       # 44, 68
        "Function_69_1BC0B",       # 45, 69
        "Function_70_1BDE2",       # 46, 70
        "Function_71_1BE5E",       # 47, 71
        "Function_72_1BF06",       # 48, 72
        "Function_73_1C043",       # 49, 73
        "Function_74_1C0E6",       # 4A, 74
        "Function_75_1C18C",       # 4B, 75
        "Function_76_1C232",       # 4C, 76
        "Function_77_1C2D8",       # 4D, 77
        "Function_78_1C388",       # 4E, 78
        "Function_79_1C42A",       # 4F, 79
        "Function_80_1C463",       # 50, 80
        "Function_81_1C4F7",       # 51, 81
        "Function_82_1C58B",       # 52, 82
        "Function_83_1C61F",       # 53, 83
    ))


    def Function_0_844(): pass

    label("Function_0_844")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_884"),
        (1, "loc_890"),
        (2, "loc_89C"),
        (3, "loc_8A8"),
        (4, "loc_8B4"),
        (5, "loc_8C0"),
        (6, "loc_8CC"),
        (SWITCH_DEFAULT, "loc_8D8"),
    )


    label("loc_884")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_890")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_89C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8A8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8B4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8C0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E4")

    label("loc_8FB")

    Return()

    # Function_0_844 end

    def Function_1_8FC(): pass

    label("Function_1_8FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BE")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BE")
    SetChrPos(0x0, -2190, 0, 68010, 90)
    SetChrPos(0x1, -2190, 0, 68010, 90)
    SetChrPos(0x2, -2190, 0, 68010, 90)
    SetChrPos(0x3, -2190, 0, 68010, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_99A")
    SetChrPos(0x4, -2190, 0, 68010, 90)
    SetChrPos(0x5, -2190, 0, 68010, 90)
    Jump("loc_9B9")

    label("loc_99A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B9")
    SetChrPos(0x4, -2190, 0, 68010, 90)

    label("loc_9B9")

    Jump("loc_9BE")

    label("loc_9BE")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_B58")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x350, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A01")
    Event(0, 62)

    label("loc_A01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x351, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A32")
    Event(0, 63)

    label("loc_A32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x352, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A63")
    Event(0, 64)

    label("loc_A63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x353, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A94")
    Event(0, 65)

    label("loc_A94")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x354, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC5")
    Event(0, 66)

    label("loc_AC5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x355, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF6")
    Event(0, 67)

    label("loc_AF6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x356, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B27")
    Event(0, 68)

    label("loc_B27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x357, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B58")
    Event(0, 69)

    label("loc_B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_B97")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 124140, 30, 8440, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 123070, 0, 8320, 45)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_BF9")

    label("loc_B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_END)), "loc_BB9")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_BF9")

    label("loc_BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_BDB")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_BF9")

    label("loc_BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_END)), "loc_BF9")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 0)

    label("loc_BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C26")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 16170, 850, 10050, 45)

    label("loc_C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C41")
    SetMapFlags(0x10000000)
    Event(0, 26)
    Jump("loc_C5B")

    label("loc_C41")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C5B")
    Event(0, 31)

    label("loc_C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_C6F")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 16)
    Jump("loc_CF6")

    label("loc_C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_C83")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 17)
    Jump("loc_CF6")

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_C97")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 21)
    Jump("loc_CF6")

    label("loc_C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_CAB")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 22)
    Jump("loc_CF6")

    label("loc_CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_CBF")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 23)
    Jump("loc_CF6")

    label("loc_CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_CD3")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 25)
    Jump("loc_CF6")

    label("loc_CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 6)), scpexpr(EXPR_END)), "loc_CE7")
    ClearScenarioFlags(0x5C, 6)
    Event(0, 35)
    Jump("loc_CF6")

    label("loc_CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 7)), scpexpr(EXPR_END)), "loc_CF6")
    ClearScenarioFlags(0x5C, 7)
    Event(0, 37)

    label("loc_CF6")

    Return()

    # Function_1_8FC end

    def Function_2_CF7(): pass

    label("Function_2_CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D13")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D2A")

    label("loc_D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D2A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D2A")

    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9A")
    SetMapObjFrame(0xFF, "objects", 0x0, 0x1)
    SetMapObjFrame(0xFF, "r_huton", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tanmatu", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)
    Jump("loc_DB7")

    label("loc_D9A")

    SetMapObjFrame(0xFF, "box00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tanmatu2", 0x0, 0x1)

    label("loc_DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE3")
    SetMapObjFrame(0xFF, "objects2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "box01", 0x1, 0x1)
    Jump("loc_E00")

    label("loc_DE3")

    SetMapObjFrame(0xFF, "box01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "objects2", 0x1, 0x1)

    label("loc_E00")

    SetMapObjFrame(0xFF, "floor02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor02_wood", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor02_sd", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor02_dankon", 0x0, 0x1)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_END)), "loc_E72")
    OP_66(0x3, 0x1)

    label("loc_E72")

    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E9D")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x3, 0x10)

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB5")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x5, 0x10)

    label("loc_EB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ECD")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x5, 0x10)

    label("loc_ECD")

    OP_65(0x13, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EEA")
    OP_66(0x13, 0x1)
    ClearMapObjFlags(0x6, 0x10)

    label("loc_EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F01")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F15")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F59")
    SetBarrier(0x0, 0x0, 0x1, 0x0, -800, -1000, 128400, 8000, 5000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 1800, -1000, 122300, 5000, 5000, 90000)

    label("loc_F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F80")
    SetBarrier(0x0, 0x2, 0x1, 0x0, 257500, -1000, 68700, 11000, 5000, 90000)

    label("loc_F80")

    SetMapObjFlags(0x1F, 0x4)
    SetMapObjFlags(0x20, 0x4)
    SetMapObjFlags(0x21, 0x4)
    SetMapObjFlags(0x22, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB0")
    SetMapObjFrame(0xFF, "01", 0x0, 0x1)
    OP_65(0x7, 0x1)

    label("loc_FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC8")
    SetMapObjFrame(0xFF, "02", 0x0, 0x1)
    OP_65(0x8, 0x1)

    label("loc_FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE0")
    SetMapObjFrame(0xFF, "05", 0x0, 0x1)
    OP_65(0x9, 0x1)

    label("loc_FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1003")
    SetMapObjFrame(0xFF, "06", 0x0, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x0, 0x1)
    OP_65(0xA, 0x1)

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101B")
    SetMapObjFrame(0xFF, "07", 0x0, 0x1)
    OP_65(0xB, 0x1)

    label("loc_101B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1033")
    SetMapObjFrame(0xFF, "08", 0x0, 0x1)
    OP_65(0xC, 0x1)

    label("loc_1033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104B")
    SetMapObjFrame(0xFF, "03", 0x0, 0x1)
    OP_65(0xD, 0x1)

    label("loc_104B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106E")
    SetMapObjFrame(0xFF, "04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x0, 0x1)
    OP_65(0xE, 0x1)

    label("loc_106E")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1086")
    OP_1B(0x0, 0x0, 0x38)

    label("loc_1086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1099")
    OP_1B(0x0, 0x0, 0x38)

    label("loc_1099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10AC")
    OP_1B(0x0, 0x0, 0x38)

    label("loc_10AC")

    OP_1B(0x8, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C4")
    OP_1B(0x8, 0x0, 0x39)

    label("loc_10C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D7")
    OP_1B(0x8, 0x0, 0x39)

    label("loc_10D7")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10EF")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_10EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1102")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_111A")
    SetMapObjFlags(0x7, 0x10)
    OP_65(0x4, 0x1)
    Jump("loc_1124")

    label("loc_111A")

    ClearMapObjFlags(0x7, 0x10)
    OP_66(0x4, 0x1)

    label("loc_1124")

    ClearMapObjFlags(0x8, 0x10)
    ClearMapObjFlags(0x9, 0x10)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)
    OP_65(0xF, 0x1)
    OP_65(0x10, 0x1)
    OP_65(0x11, 0x1)
    OP_65(0x12, 0x1)
    Return()

    # Function_2_CF7 end

    def Function_3_1149(): pass

    label("Function_3_1149")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11DD")
    Jump("loc_1227")

    label("loc_11DD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_11FD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1227")

    label("loc_11FD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_121D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1227")

    label("loc_121D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1227")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_END)), "loc_149B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F7")

    ChrTalk(
        0xFE,
        (
            "#0305FOh? What'cha up to, Lloyd?\x01",
            "Goin' out on the town?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FWell, not exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#0303FIt's about Mademois-Elie, then?\x02\x03",
            "#0300FWell, I'm sure she has her own things to\x01",
            "worry about, y'know?\x02\x03",
            "Not sure if it's the kind of stuff we should\x01",
            "really be buttin' into, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0008FYeah, that might be true.\x01",
            "(But still, if something's on her mind, I want\x01",
            "her to know she can rely on us...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_1496")

    label("loc_13F7")


    ChrTalk(
        0xFE,
        (
            "#0306FTrust me, I don't wanna see her\x01",
            "down in the dumps, either.\x02\x03",
            "#0308FI'm just not sure if we should really be buttin'\x01",
            "into her personal issues is all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1496")

    Jump("loc_15AE")

    label("loc_149B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_END)), "loc_15AE")

    ChrTalk(
        0xFE,
        (
            "#0303FWell, it's not like I don't sympathize with\x01",
            "why you're at a loss.\x02\x03",
            "#0300FHow 'bout takin' the night to mull things\x01",
            "over, though?\x02\x03",
            "#0309FHey, if we DO officially become coworkers,\x01",
            "I say we hit the town and celebrate, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FHaha, I'll consider it.\x02",
    )

    CloseMessageWindow()

    label("loc_15AE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_3_1149 end

    def Function_4_15B6(): pass

    label("Function_4_15B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_END)), "loc_16AE")

    ChrTalk(
        0xFE,
        (
            "#0106FIt was only our first day, but we\x01",
            "were sure thrown right into it.\x02\x03",
            "#0100FI guess I'm a bit worn out.\x01",
            "Once I write a bit in my diary,\x01",
            "I'll probably turn in early.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16AE")

    ChrTalk(
        0x101,
        (
            "#0002FThat's a good idea.\x02\x03",
            "Good night, Elie.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_16AE")

    TalkEnd(0xFE)
    Return()

    # Function_4_15B6 end

    def Function_5_16B2(): pass

    label("Function_5_16B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_17A1")

    ChrTalk(
        0xFE,
        (
            "#0202FSorry. Please wait a moment. I will get\x01",
            "everything up and running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FAh, wait... You don't need to be in such\x01",
            "a rush, Tio. We'll all help out later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0204FVery well. I will be counting on you all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1886")

    label("loc_17A1")


    ChrTalk(
        0xFE,
        (
            "#0200FLloyd? Is there still something you wish\x01",
            "to discuss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FOh, it's nothing, don't worry about it.\x01",
            "Sorry for disturbing you, Tio.\x02\x03",
            "Make sure to get some sleep, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0204FUnderstood. Good night, Lloyd.\x02",
    )

    CloseMessageWindow()

    label("loc_1886")

    TalkEnd(0xFE)
    Return()

    # Function_5_16B2 end

    def Function_6_188A(): pass

    label("Function_6_188A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_191E")
    Jump("loc_1968")

    label("loc_191E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_193E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1968")

    label("loc_193E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_195E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1968")

    label("loc_195E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1968")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B58")

    ChrTalk(
        0x101,
        (
            "#0002FOh, were you busy reading\x01",
            "something, Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#0203FYes, I was halfway through this\x01",
            "science journal, actually.\x02\x03",
            "#0208FUm, Lloyd, about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FI know... You're worried about\x01",
            "Elie, too, aren't you?\x02\x03",
            "#0000FI was just thinking about\x01",
            "going to talk to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#0202FIs that so? If that is the case,\x01",
            "I will let you handle it, Lloyd.\x02\x03",
            "#0206FAfter all, dealing with these sort of issues\x01",
            "doesn't fall into my area of expertise...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_1C21")

    label("loc_1B58")


    ChrTalk(
        0xFE,
        (
            "#0202FI leave Elie in your capable hands, Lloyd.\x02\x03",
            "#0206FInitially, I believed that it might be\x01",
            "more appropriate for another girl\x01",
            "to handle this issue, but...\x02\x03",
            "...this field isn't really my forte.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C21")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_188A end

    def Function_7_1C29(): pass

    label("Function_7_1C29")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#1109FHelping, helping... ♪\x02\x03",
            "#1110FLloyd, dinner should be ready\x01",
            "in just a little bit...I think!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_1C29 end

    def Function_8_1C97(): pass

    label("Function_8_1C97")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1D5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D43")

    ChrTalk(
        0xFE,
        "#1203FGrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(This guy's nappin' without\x01",
            "a care in the world...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012F(Well, at this point, I'm not too surprised.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_1D5A")

    label("loc_1D43")


    ChrTalk(
        0xFE,
        "#1203FGrrrrowl...\x02",
    )

    CloseMessageWindow()

    label("loc_1D5A")

    Jump("loc_1DF8")

    label("loc_1D5F")


    ChrTalk(
        0xFE,
        "#1203FGrrrrowl...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB7")

    ChrTalk(
        0x101,
        "#0002F(Zeit definitely enjoys his lounging.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DF8")

    label("loc_1DB7")


    ChrTalk(
        0x101,
        (
            "#0008F(I imagine Zeit wouldn't\x01",
            "know where Elie is, either.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF8")

    TalkEnd(0xFE)
    Return()

    # Function_8_1C97 end

    def Function_9_1DFC(): pass

    label("Function_9_1DFC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3F")

    ChrTalk(
        0xFE,
        (
            "#1002FWhat's up, kid?\x02\x03",
            "#1003FI'll repeat it for you: It's well within your power\x01",
            "to decline your assignment to the SSS.\x02\x03",
            "You already earned your detective qualifications,\x01",
            "so I imagine you'd just be reassigned to one of\x01",
            "the investigative divisions.\x02\x03",
            "#1000FHey, at least give it a night of thought.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_204E")

    label("loc_1F3F")


    ChrTalk(
        0xFE,
        (
            "#1003FYou retain the right to decline your assignment\x01",
            "to the Special Support Section, y'know.\x02\x03",
            "You already earned your detective qualifications,\x01",
            "so I imagine you'd just be reassigned to one of\x01",
            "the investigative divisions.\x02\x03",
            "#1000FAt least give it a night of thought.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_204E")

    TalkEnd(0xFE)
    Return()

    # Function_9_1DFC end

    def Function_10_2052(): pass

    label("Function_10_2052")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20E6")
    Jump("loc_2130")

    label("loc_20E6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2106")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2130")

    label("loc_2106")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2126")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2130")

    label("loc_2126")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2130")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2303")

    ChrTalk(
        0xFE,
        (
            "#1005FOh, it's just you. Don't come in\x01",
            "bringing down the mood, got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FSorry about that.\x01",
            "Still working, Chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1006FThe SSS, unconventional as it may be, is still\x01",
            "part of the CPD...so that means paperwork.\x02\x03",
            "#1000FIf you don't have any pressing issues, kid,\x01",
            "could you leave me to this? I'd like to get\x01",
            "all this finished before daybreak, y'know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FRight, sorry for the interruption.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_2391")

    label("loc_2303")


    ChrTalk(
        0xFE,
        (
            "#1000FIf you don't have any pressing issues, kid,\x01",
            "could you leave me to this? I'd like to get\x01",
            "all this finished before daybreak, y'know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2391")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_2052 end

    def Function_11_2399(): pass

    label("Function_11_2399")

    Call(0, 18)
    Return()

    # Function_11_2399 end

    def Function_12_239D(): pass

    label("Function_12_239D")

    Call(0, 19)
    Return()

    # Function_12_239D end

    def Function_13_23A1(): pass

    label("Function_13_23A1")

    Call(0, 24)
    Return()

    # Function_13_23A1 end

    def Function_14_23A5(): pass

    label("Function_14_23A5")

    Call(0, 59)
    Return()

    # Function_14_23A5 end

    def Function_15_23A9(): pass

    label("Function_15_23A9")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The orbal terminal is down.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#0000FNo reason to use it now, anyway.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_15_23A9 end

    def Function_16_2404(): pass

    label("Function_16_2404")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    SetChrPos(0x11, 64000, 150, 11400, 180)
    SetChrChipByIndex(0x11, 0x6)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0200012V#0011FLet me get this straight. It's a division\x01",
            "that accepts requests from the public\x01",
            "and prioritizes the citizens' well-being?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(24000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x11,
        (
            "#0200013V#1P#1003FRight, that's the long and short of this\x01",
            "newly-established 'Special Support Section.'\x02\x03",
            "#0200014VTo win the hearts of our citizens, a separate\x01",
            "division was created. One that can become\x01",
            "part of their everyday lives.\x02\x03",
            "#0200015V#1002FHeh. Makes sense, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200016V#12P#0011FH-Hold on, that sounds like...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0200017V#0106F...we're meant to be an immitation\x01",
            "of the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200018V#4P#0211FSmells like plagiarism to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0200019V#0306FWhat the lil' lady said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0200020V#1P#1000FYou're probably already aware of this, but\x01",
            "the guild is killing the CPD when it comes\x01",
            "to Crossbell's popularity contest.\x02\x03",
            "#0200021V#1003FA-rank bracer, Arios MacLaine...\x02\x03",
            "#0200022VThe guy known as the 'Divine Blade of Wind'...\x01",
            "He and a bunch of other powerful folk work\x01",
            "out of the Crossbell branch of the guild.\x02\x03",
            "#0200023V#1000FYou starting to understand what that means\x01",
            "for all the big shots at the police department?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200024V#12P#0005FW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0200025V#0103FThe police and guild are constantly compared\x01",
            "to each other, making our flaws as an\x01",
            "organization that much more apparent...\x02\x03",
            "#0200026V#0108FFurthermore, that criticism will end up being\x01",
            "traced back to the Crossbell government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0200027V#0304FPieces are startin' to fall into place now.\x02\x03",
            "#0200028V#0300FSo basically, you're making a risky gamble\x01",
            "on us being able to snatch popularity back\x01",
            "from the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200029V#4P#0206FA bit shameless, is it not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0200030V#1P#1004FWell, to be honest...you're right.\x02\x03",
            "#0200031V#1001FHowever, the police's founding principles are\x01",
            "to maintain public order and enforce the laws\x01",
            "supplied by our government...\x02\x03",
            "#0200032VProtecting the citizenry has always been their\x01",
            "secondary objective.\x02\x03",
            "#0200033V#1003FFor that reason, there's a lot of people within\x01",
            "the police who aren't looking too kindly on a\x01",
            "blatant bid for popularity like this.\x02\x03",
            "#0200034VLet's see... I've heard 'utility workers,' 'bogus\x01",
            "bracers,' even 'circus monkeys'...\x02\x03",
            "#0200035V#1002FIn other words, there's already been a bit of\x01",
            "backlash towards you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200036V#12P#0011F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0200037V#0106FSo that's the case... This whole situation\x01",
            "is starting to make much more sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0200038V#0301FOh, boy. So you're tellin' us to join a team\x01",
            "where we'll be under fire from everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200039V#4P#0211FThis is not what I signed up for.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0200040V#1P#1004FNow, now, don't start freaking out just yet.\x02\x03",
            "#0200041V#1002FI'm sure you've already been told that you\x01",
            "can refuse this assignment, yeah?\x02",
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
        "#0200042V#12P#0005FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0200043V#1P#1003FIf you're officially assigned here, expect\x01",
            "to see all sorts of odd jobs and requests.\x02\x03",
            "#0200044VThat includes more monster exterminations\x01",
            "like the one you completed today...\x02\x03",
            "#0200045V...but there'll also be minor stuff like tracking\x01",
            "down lost items and helping out HQ.\x02\x03",
            "#0200046V#1001FAnyone who's not up for that wouldn't be a\x01",
            "great fit for this position.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(300)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x11,
        (
            "#0200047V#1003FI'll give you the night to sleep on it.\x02\x03",
            "#0200048VIf you end up refusing, don't worry.\x01",
            "You'll be reassigned to another unit.\x01",
            "On top of that, there'll be no demerits.\x02\x03",
            "#0200049V#1000FBall's in your court, everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CA(0x1, 0xFF, 0x0)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    Sleep(1000)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x47, 5)
    SetScenarioFlags(0x5C, 1)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2404 end

    def Function_17_32CF(): pass

    label("Function_17_32CF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50000.itc", 0x1E)
    OP_68(1900, 1100, 123500, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    SetChrPos(0x101, 1900, 300, 125500, 270)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis000.itp")
    OP_68(1900, 1100, 125500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#0200050V#0008F#11P...\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#0200051V#0006FHow in the world did I get here...?\x02\x03",
            "#0200052V#0008FImitating the Bracer Guild...\x02\x03",
            "#0200053VI didn't join the force to be a part\x01",
            "of something like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0200054V#0003F#11PGuy was assigned to the First Division.\x02\x03",
            "#0200055VAn elite unit that single-handedly solves major\x01",
            "cases, be it criminal or political in nature...not\x01",
            "to mention handling international matters...\x02\x03",
            "#0200056V#0008FOur divisions really are worlds apart...\x02\x03",
            "#0200057V...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_68(1550, 1100, 125710, 500)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 1000, 30, 125500, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0200058V#5P#0001FI wonder what the others are planning to do.\x02\x03",
            "#0200059VI don't think any of them attended the police\x01",
            "academy, but I'm sure they've got their own\x01",
            "reasons for joining the force.\x02\x03",
            "#0200060V#0000FMaybe talking to them will clear my head.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, 900, 0, 125500, 180)
    SetScenarioFlags(0x41, 1)
    OP_29(0x3C, 0x1, 0x4)
    OP_29(0x3C, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_17_32CF end

    def Function_18_3759(): pass

    label("Function_18_3759")

    EventBegin(0x0)
    Fade(1000)
    OP_68(13700, 1100, 62900, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 13700, 0, 62100, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_382A")

    ChrTalk(
        0x101,
        (
            "#0200061V#12P#0005FThis is Randy's room...\x02\x03",
            "#0200062V#0001FIt sounded like he was busy\x01",
            "unpacking all his stuff earlier.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_382A")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Knock]\x01",            # 0
            "[Don't knock]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_387A"),
        (1, "loc_49BC"),
        (SWITCH_DEFAULT, "loc_49C3"),
    )


    label("loc_387A")

    OP_95(0x101, 13700, 0, 62900, 2000, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(1000)
    SetChrPos(0x8, 13700, 0, 66000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)

    NpcTalk(
        0x8,
        "Randy's Voice",
        "#0200063V#5P#2SYeah? Who's knockin'?\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200064V#12P#0000FIt's me, Lloyd. Can we talk for a bit?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Randy's Voice",
        "#0200065V#5P#2SSure, man. C'mon in. Make yourself at home.\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200066V#12P#0000FCool. Thanks.\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_71(0x3, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x3)

    def lambda_39BB():
        OP_95(0xFE, 13700, 0, 64400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39BB)
    Sleep(300)

    def lambda_39D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_39D8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    OP_68(51500, 600, 130000, 0)
    MoveCamera(40, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0xA)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x8)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 51840, 150, 126400, 270)
    SetChrPos(0x101, 50000, 0, 121100, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00300.itp")
    OP_68(51500, 600, 125000, 5000)
    MoveCamera(55, 14, 0, 5000)
    SetCameraDistance(25500, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#0200067V#0005FOh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(51000, 1000, 124200, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)

    def lambda_3B2D():
        OP_95(0xFE, 51000, 0, 123200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B2D)
    OP_0D()
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    SetChrPos(0x8, 51000, 0, 126400, 270)
    OP_0D()
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_3B77():
        OP_95(0xFE, 51000, 0, 125100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3B77)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x8, 500)
    WaitChrThread(0x8, 1)
    Sound(1364, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#0200068VWelcome to my private castle.\x02\x03",
            "#0200069VSo, ya already finished unloadin'\x01",
            "all your things?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CEC")

    ChrTalk(
        0x101,
        (
            "#0200070V#12P#0006FN-No...not yet.\x02\x03",
            "#0200071V#0000FI see you were pretty quick to make\x01",
            "your decision, Randy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D5E")

    label("loc_3CEC")


    ChrTalk(
        0x101,
        (
            "#0200070V#12P#0006FN-No...Not yet.\x02\x03",
            "#0200072V#0000FI see you were pretty quick to\x01",
            "make your decision, Randy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D5E")


    ChrTalk(
        0x8,
        (
            "#0200073V#5P#0305FOh, about declinin' the assignment?\x02\x03",
            "#0200074V#0304FDoesn't sound like there'll be too much desk work,\x01",
            "so the job sounds like it's right up my alley.\x02\x03",
            "#0200075V#0300FHell, having my workplace and my home under one\x01",
            "roof is how I like it. So, yeah. I'm planning to\x01",
            "stick around and see how this shakes out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200076V#12P#0003FGot'cha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200077V#5P#0300FGotta say, confusion's written all over your\x01",
            "face. Not that it's a surprise or anything.\x02\x03",
            "#0200078VDoubt you want that detective license you\x01",
            "busted your ass off for to go to waste, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200079V#12P#0004FI guess that's one way of putting it.\x02\x03",
            "#0200080V#0008FI'm just worried that this will make\x01",
            "my goal that much harder to reach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0200081V#5P#0305FYour goal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200082V#12P#0012FErr... Don't worry about it. It's nothing\x01",
            "too important.\x02\x03",
            "#0200083V#0000FThat reminds me... How exactly were you\x01",
            "recruited in the first place, Randy?\x02\x03",
            "#0200084VYou're older than the rest of us, but...you\x01",
            "didn't attend the police academy, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200085V#5P#0305FYup, bingo.\x02\x03",
            "#0200086V#0303FHmm... How I ended up being\x01",
            "assigned here, huh?\x02\x03",
            "#0200087V#0301FYa really wanna know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200088V#12P#0005FY-Yeah. If you don't mind sharing,\x01",
            "that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200089V#5P#0303FS'pose it won't hurt to let you know.\x02\x03",
            "#0200090V#0302FThing is...I got in a bit of lady trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200091V#12P#0011FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200092V#5P#0309FWell, everyone found out I'd been foolin'\x01",
            "around with a bunch of 'em at my last\x01",
            "workplace.\x02\x03",
            "#0200093VJust as I was 'bout to get the hammer,\x01",
            "Sergei went and snatched me up.\x02\x03",
            "#0200094VI guess this is all accordin' to Aidios'\x01",
            "plan, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0200095V#12P#0011FUmm... Where'd you work before, Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200096V#5P#0300FOh, right. The Crossbell Guardian Force.\x02\x03",
            "#0200097VMore specifically, I was stationed at\x01",
            "Bellguard Gate. Y'know, that fortress\x01",
            "facin' the Empire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200098V#12P#0000FThe Guardian Force? Well, that answers that.\x02\x03",
            "#0200099VNo wonder you can swing that halberd of\x01",
            "yours around like it's nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200100V#5P#0306FTrust me, when you're stationed that close\x01",
            "to the border, there's absolutely nothin' to\x01",
            "do but train, patrol, and train some more.\x02\x03",
            "#0200101V#0300FBut hey, perk of workin' in Crossbell City\x01",
            "full-time is that I can chill over in the\x01",
            "Entertainment District whenever I want.\x02\x03",
            "#0200102V#0309FPhew, I definitely made the right choice\x01",
            "followin' Sergei after quitting the CGF! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200103V#12P#0012FHaha... Well, I can relate with wanting\x01",
            "to live in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200104V#5P#0305FA man after my own heart.\x02\x03",
            "#0200105V#0302FY'know, I've already scoped out a couple\x01",
            "clubs that have some insanely smokin'\x01",
            "ladies working in 'em.\x02\x03",
            "#0200106VHey, if we DO officially become coworkers,\x01",
            "I say we hit the town and celebrate, eh?\x02\x03",
            "#0200107V#0309FMademois-Elie seems a bit too prim and\x01",
            "proper, and kids don't belong where we'd\x01",
            "go. We'll have ourselves a guys' night out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200108V#12P#0002FHaha... Sure, I'll think about it.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_65(0x0, 0x1)
    SetMapObjFlags(0x3, 0x10)
    SetChrPos(0x0, 50250, 0, 122560, 180)
    OP_68(50250, 1300, 122560, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetScenarioFlags(0x41, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49B2")
    ModifyEventFlags(1, 0, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 16170, 850, 10050, 45)

    label("loc_49B2")

    Sleep(500)
    EventEnd(0x5)
    Jump("loc_49C3")

    label("loc_49BC")

    EventEnd(0x5)
    Jump("loc_49C3")

    label("loc_49C3")

    Return()

    # Function_18_3759 end

    def Function_19_49C4(): pass

    label("Function_19_49C4")

    EventBegin(0x0)
    Fade(1000)
    OP_68(163700, 1100, 62900, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 163700, 0, 62100, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A8F")

    ChrTalk(
        0x101,
        (
            "#0200109V#12P#0005FI think this is the room Elie was assigned.\x02\x03",
            "#0200110V#0001FI hope she isn't asleep already...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4A8F")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Knock]\x01",            # 0
            "[Don't knock]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4ADF"),
        (1, "loc_5DEB"),
        (SWITCH_DEFAULT, "loc_5DF2"),
    )


    label("loc_4ADF")

    OP_95(0x101, 163700, 0, 62900, 2000, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(1000)
    SetChrPos(0xA, 163700, 0, 66000, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)

    NpcTalk(
        0xA,
        "Elie's Voice",
        "#0200111V#5P#2SWho is it?\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200112V#12P#0000FOh, uh...it's me, Lloyd.\x02\x03",
            "#0200113VYou busy right now? I can come back later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Elie's Voice",
        "#0200114V#5P#2SAh, no. You can come on in.\x07\x00\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Elie's Voice",
        "#0200115V#5P#2SThe door shouldn't be locked.\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200116V#12P#0000FAll right, thanks.\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x5)

    def lambda_4C70():
        OP_95(0xFE, 163700, 0, 64400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C70)
    Sleep(300)

    def lambda_4C8D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C8D)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    OP_68(157300, 600, 130000, 0)
    MoveCamera(40, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x8)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0xA, 157800, 0, 126700, 45)
    SetChrPos(0x101, 155800, 0, 120800, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00100.itp")
    OP_68(157300, 600, 125000, 5000)
    MoveCamera(55, 14, 0, 5000)
    SetCameraDistance(25500, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#0200117V#0005F...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(157800, 1000, 123900, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)

    def lambda_4DCE():
        OP_95(0xFE, 157800, 0, 122900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DCE)
    Sleep(200)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(100)

    def lambda_4DF5():
        OP_95(0xFE, 157800, 0, 124800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4DF5)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xA, 500)
    WaitChrThread(0xA, 1)
    Sound(1174, 255, 90, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xA,
        (
            "#0200118VThank goodness I finished up my\x01",
            "cleaning before anyone visited.\x02\x03",
            "#0200119VWould you like to take a seat?\x01",
            "I'll brew some black tea, if\x01",
            "you'd like.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FBE")

    ChrTalk(
        0x101,
        (
            "#0200120V#12P#0004FNo, you don't need to do all that.\x02\x03",
            "#0200121V#0001FBesides, judging from your room,\x01",
            "you've already made your decision.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5041")

    label("loc_4FBE")


    ChrTalk(
        0x101,
        (
            "#0200120V#12P#0004FNo, you don't need to do all that.\x02\x03",
            "#0200122V#0001FFrom the look of it, you've already\x01",
            "made your decision.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5041")


    ChrTalk(
        0xA,
        (
            "#0200123V#5P#0105FOh, regarding my assignment here?\x02\x03",
            "#0200124V#0104FIn truth, I was unsure at first, but\x01",
            "I've decided to give this my best shot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200125V#12P#0000FThat so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0200126V#5P#0100FYou know, I can see the confusion\x01",
            "written all over your face, Lloyd.\x02\x03",
            "#0200127V#0106FBut I can't fault you for that one bit.\x02\x03",
            "#0200128V#0108FThe Special Support Section may be\x01",
            "overly ambitious from the start.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0200129V#12P#0005FOverly ambitious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0200130V#5P#0101FFrom what we heard, the SSS was founded with\x01",
            "several conditions in place, and it mainly exists\x01",
            "to serve the CPD's own interests.\x02\x03",
            "#0200131VIts establishment seems irrational to begin with,\x01",
            "and our objectives are vague to say the least.\x02\x03",
            "#0200132V#0103FSo, if we fail to produce results, the SSS will in\x01",
            "all likelihood be disbanded due to budget\x01",
            "constraints. Don't you agree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200133V#12P#0006FYeah, I can't help but draw the same\x01",
            "conclusion, too.\x02\x03",
            "#0200134V#0001FBut if you already knew that, why\x01",
            "stay, Elie?\x02\x03",
            "#0200135VDo you have some reason?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0200136V#5P#0100FThat's right...\x02\x03",
            "#0200137V#0104FI thought it'd be a good way to\x01",
            "see the truth for myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200138V#12P#0005FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0200139V#5P#0109FWell, I might be over-exaggerating.\x02\x03",
            "#0200140V#0100FHonestly, I doubt I'll stay a member\x01",
            "of the police force forever.\x02\x03",
            "#0200141VIn that sense, it's not too big a deal\x01",
            "if this position takes me off course\x01",
            "from my intended career track.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200142V#12P#0003FHuh, really?\x02\x03",
            "#0200143V#0000FNow that I think about it, you didn't\x01",
            "attend the police academy, right, Elie?\x02\x03",
            "#0200144VSo, how'd you happen to join the CPD?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0200145V#5P#0101FWell... To be honest, this is a part of\x01",
            "my plan to study our society.\x02\x03",
            "#0200146V#0103FWhile I didn't attend the academy, I did\x01",
            "take a written exam and marksmanship\x01",
            "test when I applied.\x02\x03",
            "#0200147V#0102FThey couldn't really reject me, since\x01",
            "I made perfect marks on both tests.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0200148V#12P#0012FY-You know, the more I learn, the more\x01",
            "I feel like we're worlds apart...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0200149V#5P#0100FDo you think? But it's pretty rare for rookies\x01",
            "to have already earned their detective license,\x01",
            "isn't it?\x02\x03",
            "#0200150VYou must have your reasons for joining the\x01",
            "police, too, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200151V#12P#0005FWell, yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0200152V#5P#0104FHeehee...\x02\x03",
            "#0200153V#0102FPerhaps it'd be best to continue this talk\x01",
            "after we've officially become coworkers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200154V#12P#0002FYeah, I suppose so.\x02\x03",
            "#0200155V#0004FSorry for making you go through all\x01",
            "this trouble for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0200156V#5P#0104FDon't worry about it.\x02\x03",
            "#0200157V#0102FIf you were to ask for my personal opinion,\x01",
            "I'd be happier if you decided to stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200158V#12P#0005FYou would?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0200159V#5P#0106FAfter all, we're both newcomers to the force\x01",
            "who can strive to improve ourselves...\x02\x03",
            "#0200160V#0102FBut, more importantly, you showed that\x01",
            "you could be the leader we needed today.\x02\x03",
            "#0200161VYour instructions were precise and quick,\x01",
            "so I was able to calmly provide support.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200162V#12P#0012FHaha. I'll take your word for it.\x02\x03",
            "#0200163V#0004FThanks for letting me take up your time.\x02\x03",
            "#0200164V#0000FI think I'll do a bit of self-reflection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0200165V#5P#0104FOf course. Any time.\x02\x03",
            "#0200166V#0102FGood night, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200167V#12P#0002F'Night, Elie.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_65(0x1, 0x1)
    SetMapObjFlags(0x5, 0x10)
    SetChrPos(0x0, 156610, 30, 121830, 180)
    OP_68(156610, 1330, 121830, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x40)
    SetChrPos(0xA, 157420, 0, 128650, 0)
    SetScenarioFlags(0x41, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DE1")
    ModifyEventFlags(1, 0, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 16170, 850, 10050, 45)

    label("loc_5DE1")

    Sleep(500)
    EventEnd(0x5)
    Jump("loc_5DF2")

    label("loc_5DEB")

    EventEnd(0x5)
    Jump("loc_5DF2")

    label("loc_5DF2")

    Return()

    # Function_19_49C4 end

    def Function_20_5DF3(): pass

    label("Function_20_5DF3")

    EventBegin(0x0)
    Fade(1000)
    OP_68(4000, 1850, 10300, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x101, 4000, 850, 10300, 90)
    SetChrPos(0xB, 16100, 850, 10200, 45)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4B(0xB, 0xFF)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00200.itp")
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(15000, 1850, 10300, 3000)
    SetCameraDistance(25500, 3000)
    Sleep(1000)

    def lambda_5EC1():
        OP_96(0xFE, 0x42CC, 0x352, 0x23F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5EC1)
    WaitChrThread(0xB, 1)
    Sleep(1000)

    def lambda_5EE2():
        OP_96(0xFE, 0x3EE4, 0x352, 0x27D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5EE2)
    OP_6F(0x1)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#0200168V#0005FTio... What are you doing?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(11900, 1850, 10200, 0)
    MoveCamera(50, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 8000, 1000, 10300, 90)
    OP_68(13900, 1850, 10200, 2000)

    def lambda_5F9D():
        OP_97(0x101, 0x12C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F9D)
    Sleep(500)
    TurnDirection(0xB, 0x101, 500)
    Sleep(500)

    def lambda_5FC4():
        OP_95(0xFE, 15000, 850, 10200, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5FC4)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    Sound(1267, 255, 90, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xB,
        (
            "#0200169VOh, Lloyd.\x02\x03",
            "#0200170VAs you could probably deduce,\x01",
            "I am checking our terminal.\x02",
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
        "#0200171V#6P#0005FThe terminal? That big thing?\x02",
    )

    CloseMessageWindow()
    OP_68(16500, 1750, 10300, 1500)
    MoveCamera(35, 16, 0, 1500)
    SetCameraDistance(22000, 1500)

    def lambda_6109():
        OP_95(0x101, 13300, 850, 9800, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6109)
    Sleep(300)
    OP_93(0xB, 0x5A, 0x1F4)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#0200172V#0200F#5PYes, it is an improved orbal terminal\x01",
            "based on ZCF's Capel computer system.\x02\x03",
            "#0200173VWith it, it is possible to receive data and\x01",
            "information from the police department,\x01",
            "thanks to the orbal network.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0200174V#6P#0011FUh...\x02\x03",
            "#0200175VL-Let's rewind for a bit. You lost me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#0200176V#0203F#5PHow should I explain this?\x02\x03",
            "#0200177V#0200FLloyd, what is the extent of your knowledge\x01",
            "about the Orbal Network Project?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200178V#6P#0005FThe orbal network...\x02\x03",
            "#0200179V#0006FI occasionally see articles about it in the\x01",
            "newspaper, but I'm not an expert on it.\x02\x03",
            "#0200180V#0001FI think I read something about the Epstein\x01",
            "Foundation proposing the project...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#0200181V#0200F#5POriginally, the Orbal Network Project began\x01",
            "as a collaboration between the foundation\x01",
            "and Zeiss Central Factory.\x02\x03",
            "#0200182VNow it progresses primarily due to the\x01",
            "efforts of the Epstein Foundation.\x02\x03",
            "#0200183VIts large-scale testing stage is currently\x01",
            "taking place right here in Crossbell State.\x02\x03",
            "#0200184VThis terminal is a part of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200185V#6P#0005FC-Can't say I follow that well...\x02\x03",
            "#0200186V#0012FIn the end, what's this project trying\x01",
            "to accomplish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#0200187V#0203F#5P*sigh*...\x02",
    )

    CloseMessageWindow()
    OP_68(15180, 1750, 10680, 1200)
    TurnDirection(0xB, 0x101, 500)
    Sleep(300)
    OP_6F(0x1)

    ChrTalk(
        0xB,
        (
            "#0200188V#11P#0200FSimply put, it is technology that improves\x01",
            "upon traditional communication devices.\x02\x03",
            "#0200189VIn addition to having communication functions,\x01",
            "it links terminals through orbal computing,\x01",
            "constructing an efficient information network.\x02\x03",
            "#0200190VThat is the project, in layman's terms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200191V#6P#0006FBut that wasn't clear at all...\x02\x03",
            "#0200192V#0001FSo basically, it's equipment that'll make\x01",
            "contacting HQ easier and optimize the\x01",
            "chain of command in the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#0200193V#11P#0204FIf you were only taking into account this\x01",
            "terminal, you would not be incorrect.\x02\x03",
            "#0200194V#0202FWhile terminals are not my specialty,\x01",
            "I can operate this one for us.\x02\x03",
            "#0200195VConsidering the future, I suppose I should\x01",
            "become more acquainted with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200196V#6P#0005FY-Yeah...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0200197V#6P#0000FI take that to mean you didn't even think\x01",
            "about refusing this assignment, huh, Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#0200198V#0205F#11PHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200199V#6P#0003FNo, what I'm trying to say is...when I was\x01",
            "your age, all I wanted to do was play\x01",
            "around with my friends.\x02\x03",
            "#0200200V#0000FBut you said you were transferred here\x01",
            "from the foundation... You aren't, uh...\x01",
            "being forced to work here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#0200222V#0205F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200202V#6P#0011FWhat?! Don't tell me...y-you actually are?!\x02\x03",
            "#0200203V#0013FNo matter your situation, you shouldn't\x01",
            "tolerate being forced to work like this!\x02\x03",
            "#0200204VIf you want, I'd be happy to give you\x01",
            "a helping hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#0200205V#0206F#11PNo. Please calm down.\x02\x03",
            "#0200206V#0208FNo cause for concern. I am not being\x01",
            "coerced into working by the foundation.\x02\x03",
            "#0200207V#0202FRather, this recent transfer was the\x01",
            "result of a selfish request of mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200208V#6P#0005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#0200209V#0204F#11PI have my reasons for accepting this\x01",
            "position.\x02\x03",
            "#0200210VThat should satisfy your curiosity.\x02\x03",
            "#0200211V#0211FBesides, I think it would be prudent to worry\x01",
            "about yourself before others, right, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200212V#6P#0005FY-Yeah...\x02\x03",
            "#0200213V#0006FYou make a good point, Tio.\x02\x03",
            "#0200214V#0000FI'm sorry for being pushy about\x01",
            "your situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#0200215V#0203F#11PIt is fine...\x02\x03",
            "#0200216V#0202FBeing too soft-hearted might have negative\x01",
            "ramifications on your detective work, however.\x02\x03",
            "#0200217VUnlike that of bracers, your occupation hinges\x01",
            "on the distrust of suspects, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200218V#6P#0011FUgh... You really don't pull any punches, do you?\x02\x03",
            "#0200219V#0006FMaybe I really am still a big softie...\x02\x03",
            "#0200220VGeez, and I thought I disciplined myself enough\x01",
            "during the police academy's training.\x02\x03",
            "#0200221V#0008FBut I guess that training alone doesn't make me\x01",
            "qualified to be a detective...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#0200201V#0202F#11P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0200223V#6P#0005F...Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#0200224V#0203F#11PMaintenance of the terminal has been completed.\x02\x03",
            "#0200225V#0200FConstruction work on the orbal cables is scheduled\x01",
            "for tomorrow, so I am going to turn in early tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200226V#6P#0000FAh, okay...\x02\x03",
            "#0200227V#0002F'Night. I hope you can get some sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#0200228V#0204F#11PThank you. If you will excuse me...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1270, 255, 90, 0)
    Sleep(300)

    def lambda_722C():

        label("loc_722C")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_722C")

    QueueWorkItem2(0x101, 2, lambda_722C)

    def lambda_723E():
        OP_95(0xFE, 13300, 850, 11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_723E)
    WaitChrThread(0xB, 1)
    OP_68(13300, 1850, 9800, 2000)

    def lambda_726D():
        OP_97(0xFE, 0xFFFFE2B4, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_726D)
    WaitChrThread(0xB, 1)
    EndChrThread(0x101, 0x2)
    SetChrFlags(0xB, 0x80)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0200229V#11P#0003FAll three of them have already given this\x01",
            "assignment thought and made their decisions.\x02\x03",
            "#0200230V#0008FSo I'm the only conflicted one...\x02\x03",
            "#0200231V...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0200232V#11P#0006FGeez, this is no good. All I'm doing is getting\x01",
            "nowhere fast.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#0200233V#5P#0000FMaybe some fresh air will do me some good...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_CA(0x1, 0xFF, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 9620, 850, 10260, 270)
    OP_68(9620, 1850, 10260, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetScenarioFlags(0x41, 4)
    OP_1B(0x0, 0xFF, 0xFFFF)
    ModifyEventFlags(1, 1, 0x80)
    EventEnd(0x1)
    Return()

    # Function_20_5DF3 end

    def Function_21_7475(): pass

    label("Function_21_7475")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(821)
    OP_68(800, 850, 1550, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 800, 40, 50, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x1F, 0x4)
    SetMapObjFlags(0x1F, 0x1000)
    OP_70(0x1F, 0x0)
    OP_74(0x1F, 0x1E)
    OP_71(0x1F, 0x0, 0x14, 0x0, 0x20)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_752F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_752F)

    def lambda_7540():
        OP_95(0xFE, 800, 40, 1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7540)
    WaitChrThread(0x101, 1)
    Sleep(300)
    Sound(821, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x2D, 0x1F4)

    ChrTalk(
        0x101,
        "#0200287V#6P#0005FA phone call?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    def lambda_75B5():
        OP_95(0xFE, 1800, 850, 10000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75B5)
    Sleep(800)
    OP_68(13800, 1850, 12000, 4000)
    SetCameraDistance(23000, 4000)
    WaitChrThread(0x101, 1)

    def lambda_75F0():
        OP_95(0xFE, 11800, 850, 10000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75F0)
    WaitChrThread(0x101, 1)

    def lambda_760E():
        OP_95(0xFE, 13800, 850, 12000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_760E)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x0)
    OP_6F(0x1)
    OP_24(0x335)
    Sound(822, 0, 100, 0)
    ClearMapObjFlags(0x1F, 0x20)
    OP_70(0x1F, 0x32)
    FadeToDark(500, 0, 100)
    OP_0D()
    Sound(1084, 255, 90, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0200288V#0001FYes, hello?\x02\x03",
            "#0200289VYou've reached the Crossbell Police\x01",
            "Department's Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0200290V\x07\x05",
            "Lloyd? Lloyd, is that you?\x02",
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
            "#0200291V\x07\x00",
            "#0005FWha...? Cecile?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0200292V\x07\x05",
            "*sigh* Thank goodness it's really you.\x02\x03",
            "#0200293VWhen I contacted the police department,\x01",
            "they told me to call this number.\x02\x03",
            "#0200294VThe 'Special Support Section,' you said?\x01",
            "Is that the division you're assigned to?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0200295V\x07\x00",
            "#0000FAh, well...nothing's official yet.\x02\x03",
            "#0200296V#0006FMore importantly, I'm really sorry, Cecile.\x01",
            "I was meant to stop by first thing, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0200297V\x07\x05",
            "No, don't beat yourself up over that.\x02\x03",
            "#0200298VI should have gone to greet you\x01",
            "when you arrived at the station...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0200299V\x07\x00",
            "#0000FDon't worry--it's fine. I promise.\x02\x03",
            "#0200300VAfter all, work has you busy, right?\x01",
            "We can meet up once you're able to\x01",
            "get some time off.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0200301V\x07\x05",
            "That's no good, Lloyd.\x02\x03",
            "#0200302VHow can you be so distant to someone\x01",
            "who's practically your sister? I haven't\x01",
            "seen you in three years, you know...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0200303V\x07\x00",
            "#0012FAh, geez... Fine. We'll find a way to\x01",
            "make time, somehow.\x02\x03",
            "#0200304V#0000FAnd I'll make sure to go see Uncle\x01",
            "Miles and Aunt Leyte tomorrow, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0200305V\x07\x05",
            "Great, they'll love that.\x02\x03",
            "#0200306VMom and Dad have been really\x01",
            "worried about you all this time...\x02\x03",
            "#0200307VBut, heehee... I'm so happy.\x02\x03",
            "#0200308VYou've finally come back to Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#0200309V\x07\x00",
            "#0004FYeah...\x02\x03",
            "#0200310V#0002FI'm home, Cecile.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0200311V\x07\x05",
            "Welcome home, Lloyd.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x335)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_7475 end

    def Function_22_7DDF(): pass

    label("Function_22_7DDF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    SetChrPos(0x11, 64000, 150, 11400, 180)
    SetChrChipByIndex(0x11, 0x6)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis151.itp")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x11,
        "#0401423VHmm, I think I get the picture.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7513", 0)
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8010")

    ChrTalk(
        0x11,
        (
            "#0401424V#5P#1004FI guess you guys did pretty okay...\x01",
            "for a bunch of rookies.\x02\x03",
            "#0401425V#1002FYou managed to put your heads\x01",
            "together and scrape by one way\x01",
            "or another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401426V#12P#0012FH-Haha, yeah...\x01",
            "(That's a compliment, right?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8246")

    label("loc_8010")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_813E")

    ChrTalk(
        0x11,
        (
            "#0401427V#5P#1003FWell, you're still rookies, so don't let the\x01",
            "messy performance get you down.\x02\x03",
            "#0401428V#1000FIf something similar happens in the future,\x01",
            "you should be able to handle it a bit smoother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401429V#12P#0005FY-Yes, sir.\x01",
            "(He's a pretty strict boss, isn't he?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8246")

    label("loc_813E")


    ChrTalk(
        0x11,
        (
            "#0401430V#5P#1006FDon't get me wrong, it's great it turned\x01",
            "out okay, but you had some bad gaffes.\x02\x03",
            "#0401431V#1000FYou're all still rookies, so I guess that's\x01",
            "how the cookie crumbles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401432V#12P#0006FSorry, sir.\x01",
            "(Sounds like we screwed up big time...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8246")

    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x11,
        (
            "#0401433V#5P#1003FSurely you must have caught a\x01",
            "glimpse of it during this case...\x02\x03",
            "#0401434V#1001FThe thorny, problematic side of\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401435V#12P#0008FWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401436V#0306FYup, it's definitely a pain in the ass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0401437V#4P#0211FCrossbell's seedy underbelly...\x01",
            "A cold, cruel reality made possible\x01",
            "by the corruption of its leadership.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0401438V#0108FAptly put.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0401439V#5P#1000FBut the CPD isn't filled to the brim with\x01",
            "a bunch of losers, y'know.\x02\x03",
            "#0401440VWhile some idiots decide to trade dignity\x01",
            "for bribes...\x02\x03",
            "#0401441V...most of our detectives have self-respect\x01",
            "and work with a strict code of justice.\x02\x03",
            "#0401442V#1003FHowever, they're often stopped by certain\x01",
            "'barriers.'\x02\x03",
            "#0401443V#1001FFor example, the politicians who degrade\x01",
            "themselves by making deals with the mafia\x01",
            "for money and power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401444V#12P#0008F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0401445V#5P#1002FSo how about it, Lloyd?\x02\x03",
            "#0401446VWant to pack your bags, turn in your\x01",
            "badge, and become a bracer?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        (
            "#0401447V#12P#0003FNo, sir.\x02\x03",
            "#0401448V#0000FThese barriers are the reason the Special\x01",
            "Support Section was established, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_870D():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_870D)
    Sleep(50)

    def lambda_871D():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_871D)
    Sleep(50)

    def lambda_872D():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_872D)
    WaitChrThread(0x102, 2)

    ChrTalk(
        0x11,
        "#0401449V#5P#1005FOh?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0401450V#12P#0001F'Protect civilians above all else...' The bracers'\x01",
            "code is admirable, but it has its limitations...\x01",
            "Some problems can't be solved by that alone.\x02\x03",
            "#0401451V#0003FSmuggling and illegal arms dealing...\x02\x03",
            "#0401452VThe sale of stolen goods and mira laundering...\x02\x03",
            "#0401453VAnd the collusion of the mafia and officials...\x02\x03",
            "#0401454V#0001FThey're all problems that lie outside of the\x01",
            "guild's jurisdiction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401455V#2P#0305FHe's got a point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0401456V#4P#0203FSo even the supporting gauntlet still\x01",
            "has its flaws...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401457V#12P#0004FHowever, as police officers, we have\x01",
            "the power to right these wrongs.\x02\x03",
            "#0401458V#0000FDespite the countless barriers that\x01",
            "are standing in our way...\x02\x03",
            "#0401459V...the possibility of getting over them\x01",
            "isn't zero.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0401460V#11P#0104FHe's right.\x02\x03",
            "#0401461V#0100FWe, as the SSS, can create possibilities\x01",
            "others can't for true change.\x02\x03",
            "#0401462VThat's what you're trying to say, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0401463V#6P#0000FYeah, but hopefully I'm not being\x01",
            "too optimistic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0401464V#4P#0204FI do think that reality is not as simple\x01",
            "as you make it out to be.\x02\x03",
            "#0401465V#0202FHowever, I agree that the possibility\x01",
            "is never zero.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0401466V#11P#0304FTake a look at this guy, would ya?\x02\x03",
            "#0401467VDuelin' with the head of a delinquent group,\x01",
            "volunteerin' as bait to lure out the mafia...\x02\x03",
            "#0401468V#0302FHow can a guy look so calm and collected,\x01",
            "but be so hot-blooded underneath it all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401469V#6P#0005FI'm not really sure if hot-blooded is the\x01",
            "right term...\x02\x03",
            "#0401470V#0000FStill, working with everyone helped me\x01",
            "realize something.\x02\x03",
            "#0401471V#0004FWhile it's true that we're still inexperienced...\x02\x03",
            "#0401472V#0002F...as long as we stick together, no matter\x01",
            "how high they may be, there isn't a single\x01",
            "barrier we can't overcome.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0401473V#11P#0105FL-Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401474V#11P#0302FHaha, I'm at a loss for words.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0401475V#4P#0206FA bit too cheesy for my liking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#0401476V#5P#1004FHeh heh heh...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x11,
        "#0401477V#5P#1009F#4SHAHAHAHA!\x02",
    )

    CloseMessageWindow()

    def lambda_8FAE():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8FAE)
    Sleep(50)

    def lambda_8FBE():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8FBE)
    Sleep(50)

    def lambda_8FCE():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8FCE)
    Sleep(50)

    def lambda_8FDE():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8FDE)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0401478V#12P#0011FY-You don't have to laugh THAT hard.\x02\x03",
            "#0401479V#0006FAlthough, I suppose I'm being too\x01",
            "idealistic again, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0401480V#5P#1004FHeh. Well, I'm sure this won't be too bad.\x02\x03",
            "#0401481V#1002FWhile it's true that the idea of the SSS was\x01",
            "initially met with opposition and resistance...\x02\x03",
            "#0401482V...you guys can use this division however you\x01",
            "see fit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401483V#12P#0002FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0401484V#5P#1004FSure, I might not be able to directly bail you\x01",
            "out of trouble...\x02\x03",
            "#0401485V...but if you end up pulling some crazy stunt\x01",
            "and tick off HQ, I can at least toss you a\x01",
            "bone and cover for you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401486V#12P#0000FChief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0401487V#0102FSo you're going the laissez-faire\x01",
            "route, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0401488V#0306FGeez, I get what you're gunnin' for, but\x01",
            "aren't you a bit TOO chill about this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0401489V#4P#0211FIn other words, he is trying to evade\x01",
            "any messes we may throw his way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#0401490V#5P#1002FThat's what's called veteran experience.\x02\x03",
            "#0401491V#1003FWill the SSS become a pale imitation of\x01",
            "the Bracer Guild...?\x02\x03",
            "#0401492VOr will it transform into something new\x01",
            "entirely?\x02\x03",
            "#0401493V#1002FI, for one, am going to kick back with a\x01",
            "cigarette and watch the fireworks.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x1388)
    WaitBGM()
    OP_29(0x3D, 0x4, 0x10)
    OP_29(0x3E, 0x4, 0x10)
    OP_29(0x3D, 0x4, 0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94EE")
    OP_29(0x2, 0x4, 0x40)
    Jump("loc_9500")

    label("loc_94EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9500")
    OP_29(0x2, 0x4, 0x40)

    label("loc_9500")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_951E")
    OP_29(0x3, 0x4, 0x40)
    Jump("loc_9530")

    label("loc_951E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9530")
    OP_29(0x3, 0x4, 0x40)

    label("loc_9530")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_954E")
    OP_29(0x4, 0x4, 0x40)
    Jump("loc_9560")

    label("loc_954E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9560")
    OP_29(0x4, 0x4, 0x40)

    label("loc_9560")

    SubItemNumber(0x337, 1)
    SubItemNumber(0x338, 1)
    SubItemNumber(0x339, 1)
    SubItemNumber(0x35A, 1)
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_DE(0x24, 0x0)
    OP_DE(0x1E, 0x0)
    OP_DE(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    OP_E3(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_7DDF end

    def Function_23_9643(): pass

    label("Function_23_9643")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50210.itc", 0x1E)
    OP_68(3000, 700, 127500, 0)
    MoveCamera(35, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x800)
    ClearChrFlags(0x101, 0x1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 3000, 500, 125500, 270)
    OP_68(3000, 700, 125500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    OP_63(0x101, 0xFFFFFE0C, 1300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#2101521V#0003F(Elie...)\x02\x03",
            "#2101522V#0008F(Over these past two months, I thought\x01",
            "we'd become pretty close...)\x02\x03",
            "#2101523V(Sounds like all the important issues she's\x01",
            "dealing with flew right over my head.)\x02\x03",
            "#2101524V#0006F(I suppose it makes sense that Mayor MacDowell's\x01",
            "granddaughter is an aspiring politician herself.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x101, 0x1)
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#2101525V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "Now that I think about it, you didn't\x01",
            "attend the police academy, right, Elie?\x02\x03",
            "#2101526VSo, how'd you happen to join the CPD?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#2101527V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "Well... To be honest, this is a part of\x01",
            "my plan to study our society.\x02\x03",
            "#2101528VWhile I didn't attend the academy, I did take a written\x01",
            "exam and marksmanship test when I applied.\x02\x03",
            "#2101529VThey couldn't really reject me, since I\x01",
            "made perfect marks on both tests.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#2101530V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "Y-You know, the more I learn, the more\x01",
            "I feel like we're worlds apart...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#2101531V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "Oh? But it's pretty rare for\x01",
            "rookies to already earn their\x01",
            "detective license, isn't it?\x02\x03",
            "#2101532VYou have your own circumstances, right, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#2101533V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "That's...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#2101534V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "Heehee.\x02\x03",
            "#2101535VPerhaps it'd be best to continue this talk\x01",
            "after we've officially become coworkers.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0xFFFFFE0C, 1300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(300)
    MoveCamera(45, 18, 0, 900)
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x101, 0x1)
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x3)
    Sleep(200)
    SetChrSubChip(0x101, 0x4)
    Sleep(500)
    OP_6F(0x40)

    ChrTalk(
        0x101,
        (
            "#2101536V\x07\x00",
            "#0000FAll right.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(2470, 700, 126170, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x800)
    SetChrFlags(0x101, 0x1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 1000, 30, 125500, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#2101537V\x07\x00",
            "#0004F#5P(I'll try talking to Elie for a bit.)\x02\x03",
            "#2101538V(If she's worried about something,\x01",
            "I might be able to lend a shoulder.)\x02\x03",
            "#2101539V#0000F(And...is it time we continue that\x01",
            "conversation we started?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_D5(0x1E)
    SetChrPos(0x0, 1000, 30, 125500, 180)
    SetScenarioFlags(0x81, 6)
    OP_29(0x42, 0x1, 0xA)
    EventEnd(0x5)
    Return()

    # Function_23_9643 end

    def Function_24_9DCB(): pass

    label("Function_24_9DCB")

    EventBegin(0x0)
    Fade(1000)
    OP_68(163700, 1100, 62900, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 163700, 0, 62100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#2101540V#4P#0003F(Here goes nothing...)\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 163700, 0, 62900, 2000, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2101541V#4P#0000FElie. Do you have a minute?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#2101542V#4P#0005F(No reply. Is she asleep?)\x02\x03",
            "#2101543V#0008F(No... I don't sense anyone inside.)\x02\x03",
            "#2101544V#0001FI hope she doesn't mind me checking.\x02",
        )
    )

    CloseMessageWindow()
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x5)

    def lambda_9F5E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9F5E)

    def lambda_9F6F():
        OP_95(0xFE, 163700, 0, 64400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F6F)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    OP_68(156000, 1300, 123500, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 156000, 0, 120000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_9FF2():
        OP_96(0xFE, 0x26160, 0x0, 0x1DA9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FF2)

    def lambda_A00C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A00C)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#2101545V#0008F(Just as I thought. She's not here.\x01",
            "Where could she have gone?)\x02\x03",
            "#2101546V#0000F(Maybe I should try searching for her.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_65(0x2, 0x1)
    SetMapObjFlags(0x5, 0x10)
    SetChrPos(0x0, 156000, 30, 121500, 0)
    SetScenarioFlags(0x81, 7)
    EventEnd(0x5)
    Return()

    # Function_24_9DCB end

    def Function_25_A0E7(): pass

    label("Function_25_A0E7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14100, 1850, 8000, 0)
    MoveCamera(7, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 15200, 850, 8500, 45)
    SetChrPos(0x102, 16400, 850, 7900, 0)
    SetChrPos(0x103, 16100, 850, 10000, 45)
    SetChrPos(0x104, 14400, 850, 9900, 90)
    SetMapObjFrame(0xFF, "tanmatu_add", 0x1, 0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis124.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis052.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis120.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_C9(0x0, 0x4, 0x0, 0x0, 0x0)
    OP_68(16100, 1850, 10000, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sound(72, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    SetMapFlags(0x400)
    MenuCmd(0, 0)
    MenuCmd(1, 0, "[Summary / History]")
    MenuCmd(1, 0, "[Arms / Influence]")
    MenuCmd(1, 0, "[Don Marconi]")
    MenuCmd(1, 0, "[Garcia Rossi]")
    MenuCmd(1, 0, "[Speaker Hartmann]")
    MenuCmd(1, 0, "[Finished]")
    MenuCmd(3, 0, 0x5)
    MenuCmd(4, 0, 0x3)
    MenuCmd(2, 0, -1, -1, 0)
    Sleep(1000)

    AnonymousTalk(
        0x103,
        (
            "#3300644V#0203FConnecting to the memory quartz.\x02\x03",
            "#3300645V#0200FWith this, we can access the\x01",
            "entire database's contents.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#3300646V#0001FWow, this is really comprehensive...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#3300647V#0103FUp until now, we've had quite a few gaping\x01",
            "holes in our intel on Revache...\x02\x03",
            "#3300648V#0101FThis might be the first time we get\x01",
            "any concrete information on them.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#3300649V#0300FWhy don't we take a little look-see\x01",
            "at what we got here, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#3300650V#0001FRight...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x0, 7)
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 5)
    ClearScenarioFlags(0x0, 6)
    ClearScenarioFlags(0x1, 0)
    ClearMapFlags(0x400)

    label("loc_A527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_A5E4")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "[Summary / History]")
    MenuCmd(1, 0, "[Arms / Influence]")
    MenuCmd(1, 0, "[Don Marconi]")
    MenuCmd(1, 0, "[Garcia Rossi]")
    MenuCmd(1, 0, "[Speaker Hartmann]")
    MenuCmd(1, 0, "[Finished]")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5CF")
    Jump("loc_A5D3")

    label("loc_A5CF")

    MenuCmd(3, 0, 0x5)

    label("loc_A5D3")

    MenuCmd(4, 0, 0x3)
    MenuCmd(2, 0, -1, -1, 0)
    Jump("loc_A5E7")

    label("loc_A5E4")

    SetScenarioFlags(0x1, 0)

    label("loc_A5E7")

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A61B"),
        (1, "loc_AB4F"),
        (2, "loc_B0D3"),
        (3, "loc_B649"),
        (4, "loc_BC2E"),
        (5, "loc_C2FF"),
        (SWITCH_DEFAULT, "loc_C3BA"),
    )


    label("loc_A61B")

    MenuTitle(-1, 30, 0, "Summary / History")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Revache is the largest criminal organization\x01",
            "currently operating within Crossbell State.\x02\x03",
            "Its inception dates back to roughly 1130 of\x01",
            "the Septian Calendar, coinciding with the\x01",
            "founding of the state itself.\x02\x03",
            "As the name Revache & Co. would suggest, its fortune was\x01",
            "amassed by smuggling goods between the Empire and the\x01",
            "Republic under the guise of a trading company. In turn,\x01",
            "Revache was able to seize control of Crossbell's underworld.\x02\x03",
            "Currently, Revache is known to participate in several\x01",
            "illegal businesses, including: arms smuggling, the sale\x01",
            "of stolen goods, land speculation, insider trading, mira\x01",
            "laundering, sex rings, intermediary agencies for jaeger\x01",
            "corps, and so on.\x02\x03",
            "Due to its close ties to influential diet members,\x01",
            "Revache is rarely punished for its criminal\x01",
            "offenses. While members may be arrested\x01",
            "from time to time, it is common for their bail\x01",
            "to be posted almost immediately.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB4A")

    AnonymousTalk(
        0x101,
        (
            "#3300651V#0005FI see... This entry sums\x01",
            "up Revache pretty well.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#3300652V#0100FIt's handy to have all the information we've\x01",
            "collected organized so neatly like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#3300653V#0206FAt any rate, reanalyzing this data\x01",
            "is really quite something.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#3300654V#0301FRight? These dudes are makin' a killing\x01",
            "through these illegal operations.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 2)

    label("loc_AB4A")

    Jump("loc_C3BA")

    label("loc_AB4F")

    MenuTitle(-1, 30, 0, "Arms / Influence")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Revache's main forces total about 300 members. Including\x01",
            "low-level workers both inside and outside the state, the\x01",
            "company employs approximately 500 people total.\x02\x03",
            "Revache's ranks include several former jaegers and\x01",
            "soldiers from neighboring countries. Combined with\x01",
            "its smuggling of cutting-edge orbal weaponry, Revache\x01",
            "is believed to have considerable fighting strength.\x02\x03",
            "Despite not being a large-scale crime syndicate, its\x01",
            "influence extends past Crossbell. Revache holds\x01",
            "deep ties with influential figures in both the Empire\x01",
            "and the Republic.\x02\x03",
            "According to recent intel, Revache had begun to\x01",
            "lose ground to Heiyue, a rival organization, but\x01",
            "has since bolstered its firepower by utilizing\x01",
            "war hounds. This new development has led to\x01",
            "Revache regaining superiority.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0CE")

    AnonymousTalk(
        0x101,
        (
            "#3300655V#0001FTaking all this into account...it makes you\x01",
            "realize how large Revache really is.\x02\x03",
            "#3300656VNot only that, but they have men in their\x01",
            "ranks with real battlefield experience.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#3300657V#0303FYeah, some of their men we've fought\x01",
            "have been a real pain in the ass.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#3300658V#0203FNot to mention their war hounds. They're still\x01",
            "using them, even after what happened.\x02\x03",
            "#3300659V#0211FIt is like the arrest we made in Mainz was for\x01",
            "nothing...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#3300660V#0006FI'm afraid so...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#3300661V#0106FThis seems a bit futile, doesn't it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 3)

    label("loc_B0CE")

    Jump("loc_C3BA")

    label("loc_B0D3")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis052.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "Don Marconi")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Marconi is the current president of Revache & Co.\x01",
            "and the don of its mafia organization.\x02\x03",
            "He is the fifth man to hold the position, of president,\x01",
            "but did not inherit it conventionally. Eight years ago,\x01",
            "Marconi gained control by overthrowing the fourth\x01",
            "don in an act of deceit and betrayal.\x02\x03",
            "Perhaps due to his Erebonian heritage, Marconi\x01",
            "prioritizes his relationships with members of the\x01",
            "diet's Imperial Faction. His ties with Speaker\x01",
            "Hartmann in particular are well documented.\x02\x03",
            "On the other hand, he has also made inroads with\x01",
            "the Republican Faction. Undoubtedly, Marconi seeks\x01",
            "to leverage both factions in order to take advantage\x01",
            "of Crossbell's unique circumstances.\x02\x03",
            "Furthermore, he seems to fashion himself after\x01",
            "Erebonian nobility. His personal tastes include\x01",
            "lavish garments and ostentatious furniture.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B631")

    AnonymousTalk(
        0x104,
        "#3300662V#0305FDamn... Look at this arrogant old fart.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#3300663V#0211FHe may look humorously rotund, but\x01",
            "his actions paint him as a nasty man.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#3300664V#0103FIt appears Marconi is a much more cunning\x01",
            "individual than we were led to believe.\x02\x03",
            "#3300665V#0101FDon't forget, he's managed to forge ties with\x01",
            "the Republic, despite being Erebonian...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#3300666V#0001FWe can't start underestimating him now...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 4)

    label("loc_B631")

    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_C3BA")

    label("loc_B649")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis053.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "Garcia Rossi")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Garcia Rossi's official position at Revache & Co. is\x01",
            "general manager of sales. Behind the scenes, however,\x01",
            "he acts as the mafia's underboss and is the commander\x01",
            "of its rank-and-file henchmen.\x02\x03",
            "Rossi previously served as a commanding officer of\x01",
            "the Zephyr jaeger corps. When Marconi toppled the\x01",
            "former don eight years ago, he contracted Rossi to\x01",
            "aid him in his bid for power.\x02\x03",
            "Afterward, Marconi recruited him away from the\x01",
            "corps to join Revache & Co. permanently. Rossi\x01",
            "was the architect behind the mafia's militarization\x01",
            "and large increase in strength.\x02\x03",
            "In his jaeger days, Garcia Rossi earned the moniker\x01",
            "'Killing Bear' by using his large frame and advanced\x01",
            "military combat prowess to overwhelm enemy soldiers\x01",
            "on the battlefield.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC16")

    AnonymousTalk(
        0x102,
        "#3300667V#0105FHe was a part of a jaeger corps?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#3300668V#0208FZephyr... That name sounds familiar to me.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#3300669V#0303FProbably 'cause it's known as one of the\x01",
            "strongest corps in all of western Zemuria.\x02\x03",
            "#3300670VIf that guy was a commanding officer of\x01",
            "Zephyr, trust me, his strength is no joke.\x02\x03",
            "#3300671V#0301FI've heard rumors about this Killing Bear\x01",
            "more than once.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#3300672V#0001FReally? Sounds like his strength\x01",
            "is nothing to scoff at.\x02\x03",
            "#3300673V#0005FBut, Randy, how do you\x01",
            "know so much about him?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#3300674V#0304FTravel as much as me and\x01",
            "you'll hear all sorts of rumors.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 5)

    label("loc_BC16")

    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_C3BA")

    label("loc_BC2E")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis054.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "Speaker Hartmann")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Hartmann is an extremely influential politician who\x01",
            "holds the position of Speaker of the Crossbell Diet.\x02\x03",
            "As a member of the diet, he also acts as the leader\x01",
            "of its Imperial Faction.\x02\x03",
            "A descendant of Erebonian nobility, Hartmann\x01",
            "owns a luxurious mansion, located at Mishelam\x01",
            "in the far southern reaches of Crossbell State.\x02\x03",
            "He is also considered an ally of Marconi, the\x01",
            "president of Revache & Co. It's believed Hartmann\x01",
            "cooperates in the mafia's various criminal enterprises,\x01",
            "including smuggling, mira laundering, and so on.\x02\x03",
            "Furthermore, sources say that Hartmann had an\x01",
            "unofficial meeting with the Imperial Chancellor,\x01",
            "Giliath Osborne, last year in order to demonstrate\x01",
            "his domestic and foreign authority.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2E7")

    AnonymousTalk(
        0x101,
        "#3300675V#0005FSo this is Speaker Hartmann...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#3300676V#0301FHe kinda strikes me as a high-and-mighty\x01",
            "noble rather than a politician.\x02\x03",
            "#3300677VBut, did he really manage to get an audience\x01",
            "with the Empire's Blood and Iron Chancellor?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#3300678V#0103FYes. Though it was evidently an informal one,\x01",
            "Chancellor Osborne did have a meeting with\x01",
            "the speaker.\x02\x03",
            "#3300679V#0101FIt still irks me to hear that he would meet with\x01",
            "Speaker Hartmann, completely disregarding my\x01",
            "grandfather in the process...\x02\x03",
            "#3300680VAt the time, the whole matter was quite the\x01",
            "hot topic in both nations' political spheres.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#3300681V#0001FI can't believe I never heard about that...\x02\x03",
            "#3300682V#0008FThe Blood and Iron Chancellor...\x01",
            "He's making a name for himself, all right.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#3300683V#0203FIt is troubling that we still do not know\x01",
            "the reason behind this visit of his.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 6)

    label("loc_C2E7")

    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_C3BA")

    label("loc_C2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C394")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "◆All entries viewed\x01",          # 0
            "◆All entries not viewed\x01",      # 1
            "◆Do not change\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C36C"),
        (1, "loc_C380"),
        (SWITCH_DEFAULT, "loc_C394"),
    )


    label("loc_C36C")

    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    Jump("loc_C394")

    label("loc_C380")

    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 5)
    ClearScenarioFlags(0x0, 6)
    Jump("loc_C394")

    label("loc_C394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3B5")
    SetScenarioFlags(0x0, 7)
    Jump("loc_C3B5")

    label("loc_C3B5")

    Jump("loc_C3BA")

    label("loc_C3BA")

    Jump("loc_A527")

    label("loc_C3BF")

    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    MenuCmd(4, 0, 0x0)

    ChrTalk(
        0x101,
        (
            "#3300684V#6P#0003FHmm, all right.\x02\x03",
            "#3300685V#0001FEverything was fuzzy up until now,\x01",
            "but I'm starting to see the big picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3300686V#6P#0106FI agree...\x02\x03",
            "#3300687V#0108FA ruthless, yet cunning boss and\x01",
            "a former jaeger commander as\x01",
            "his right-hand man...\x02\x03",
            "#3300688V#0101FHow strong are their ties with Speaker Hartmann?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3300689V#0306FI can't wrap my head around what kinda\x01",
            "relationship the Speaker has with this\x01",
            "Blood and Iron Chancellor, personally.\x02\x03",
            "#3300690VObviously, there's no chance in hell the\x01",
            "CPD could ever touch him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300691V#6P#0008FThat's true...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#3300692V#0205F#5PWait just a moment.\x02\x03",
            "#3300693V#0201FI believe I have discovered concealed\x01",
            "data within the memory quartz.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#3300694V#6P#0005FConcealed data? Can you pull it up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3300695V#0301FHold up, if there was stuff hidden, does\x01",
            "that mean that brat is messin' with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300696V#0206F#5PYes, if I were to guess, I bet he tried to\x01",
            "test whether I could notice it or not.\x02\x03",
            "#3300697V#0211FHis punishment will be long and painful.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#3300698V#6P#0000FWell, pushing Jona to the sideline...\x01",
            "are you able to recover the data?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300699V#0202F#5PYes. Practically in my sleep.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(849, 0, 100, 0)
    Sleep(1000)
    Sound(72, 0, 100, 0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    SetMapFlags(0x400)
    MenuCmd(0, 0)
    MenuCmd(1, 0, "[Summary / History]")
    MenuCmd(1, 0, "[Arms / Influence]")
    MenuCmd(1, 0, "[Don Marconi]")
    MenuCmd(1, 0, "[Garcia Rossi]")
    MenuCmd(1, 0, "[Speaker Hartmann]")
    MenuCmd(1, 0, "[Schwarze Auction]")
    MenuCmd(1, 0, "[Finished]")
    MenuCmd(3, 0, 0x6)
    MenuCmd(4, 0, 0x3)
    MenuCmd(2, 0, -1, -1, 0)
    Sleep(1000)
    MenuCmd(5, 0, 0x1)
    Sound(4, 0, 100, 0)
    Sleep(300)
    MenuCmd(5, 0, 0x2)
    Sound(4, 0, 100, 0)
    Sleep(300)
    MenuCmd(5, 0, 0x3)
    Sound(4, 0, 100, 0)
    Sleep(300)
    MenuCmd(5, 0, 0x4)
    Sound(4, 0, 100, 0)
    Sleep(300)
    MenuCmd(5, 0, 0x5)
    Sound(4, 0, 100, 0)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#3300700V#4S#0005FWait a sec!!\x02\x03",
            "#3300701V#0013F#3SIs that?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#3300702V#0101FThe 'Schwarze Auction'?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#3300703V#0305FOh, yeah? That's the thing Estelle and\x01",
            "Joshua were proddin' us about, right?\x02\x03",
            "#3300704V#0309FHaha, that lil' scoundrel. This is his\x01",
            "way of showing us his thanks, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#3300705V#0203FThis seems to confirm that it is,\x01",
            "in fact, a real event.\x02\x03",
            "#3300706V#0201FOn top of that, it is connected to\x01",
            "Revache, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#3300707V#0006FYeah... This is definitely suspicious.\x02\x03",
            "#3300708V#0001FAll right, should we take a look?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1, 0)
    ClearScenarioFlags(0x0, 7)
    ClearMapFlags(0x400)

    label("loc_CC65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E541")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_CD1A")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "[Summary / History]")
    MenuCmd(1, 0, "[Arms / Influence]")
    MenuCmd(1, 0, "[Don Marconi]")
    MenuCmd(1, 0, "[Garcia Rossi]")
    MenuCmd(1, 0, "[Speaker Hartmann]")
    MenuCmd(1, 0, "[Schwarze Auction]")
    MenuCmd(1, 0, "[Finished]")
    MenuCmd(3, 0, 0x6)
    MenuCmd(4, 0, 0x3)
    MenuCmd(2, 0, -1, -1, 0)
    Jump("loc_CD1D")

    label("loc_CD1A")

    SetScenarioFlags(0x1, 0)

    label("loc_CD1D")

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CD57"),
        (1, "loc_D113"),
        (2, "loc_D44E"),
        (3, "loc_D807"),
        (4, "loc_DB73"),
        (5, "loc_DECB"),
        (6, "loc_E537"),
        (SWITCH_DEFAULT, "loc_E53C"),
    )


    label("loc_CD57")

    MenuTitle(-1, 30, 0, "Summary / History")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Revache is the largest criminal organization\x01",
            "currently operating within Crossbell State.\x02\x03",
            "Its inception dates back to roughly 1130 of\x01",
            "the Septian Calendar, coinciding with the\x01",
            "founding of the state itself.\x02\x03",
            "As the name Revache & Co. would suggest, its fortune was\x01",
            "amassed by smuggling goods between the Empire and the\x01",
            "Republic under the guise of a trading company. In turn,\x01",
            "Revache was able to seize control of Crossbell's underworld.\x02\x03",
            "Currently, Revache is known to participate in several\x01",
            "illegal businesses, including: arms smuggling, the sale\x01",
            "of stolen goods, land speculation, insider trading, mira\x01",
            "laundering, sex rings, intermediary agencies for jaeger\x01",
            "corps, and so on.\x02\x03",
            "Due to its close ties to influential diet members,\x01",
            "Revache is rarely punished for its criminal\x01",
            "offenses. While members may be arrested\x01",
            "from time to time, it is common for their bail\x01",
            "to be posted almost immediately.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_E53C")

    label("loc_D113")

    MenuTitle(-1, 30, 0, "Arms / Influence")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Revache's main forces total about 300 members. Including\x01",
            "low-level workers both inside and outside the state, the\x01",
            "company employs approximately 500 people total.\x02\x03",
            "Revache's ranks include several former jaegers and\x01",
            "soldiers from neighboring countries. Combined with\x01",
            "its smuggling of cutting-edge orbal weaponry, Revache\x01",
            "is believed to have considerable fighting strength.\x02\x03",
            "Despite not being a large-scale crime syndicate, its\x01",
            "influence extends past Crossbell. Revache holds\x01",
            "deep ties with influential figures in both the Empire\x01",
            "and the Republic.\x02\x03",
            "According to recent intel, Revache had begun to\x01",
            "lose ground to Heiyue, a rival organization, but\x01",
            "has since bolstered its firepower by utilizing\x01",
            "war hounds. This new development has led to\x01",
            "Revache regaining superiority.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_E53C")

    label("loc_D44E")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis052.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "Don Marconi")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Marconi is the current president of Revache & Co.\x01",
            "and the don of its mafia organization.\x02\x03",
            "He is the fifth man to hold the position, of president,\x01",
            "but did not inherit it conventionally. Eight years ago,\x01",
            "Marconi gained control by overthrowing the fourth\x01",
            "don in an act of deceit and betrayal.\x02\x03",
            "Perhaps due to his Erebonian heritage, Marconi\x01",
            "prioritizes his relationships with members of the\x01",
            "diet's Imperial Faction. His ties with Speaker\x01",
            "Hartmann in particular are well documented.\x02\x03",
            "On the other hand, he has also made inroads with\x01",
            "the Republican Faction. Undoubtedly, Marconi seeks\x01",
            "to leverage both factions in order to take advantage\x01",
            "of Crossbell's unique circumstances.\x02\x03",
            "Furthermore, he seems to fashion himself after\x01",
            "Erebonian nobility. His personal tastes include\x01",
            "lavish garments and ostentatious furniture.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_E53C")

    label("loc_D807")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis053.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "Garcia Rossi")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Garcia Rossi's official position at Revache & Co. is\x01",
            "general manager of sales. Behind the scenes, however,\x01",
            "he acts as the mafia's underboss and is the commander\x01",
            "of its rank-and-file henchmen.\x02\x03",
            "Rossi previously served as a commanding officer of\x01",
            "the Zephyr jaeger corps. When Marconi toppled the\x01",
            "former don eight years ago, he contracted Rossi to\x01",
            "aid him in his bid for power.\x02\x03",
            "Afterward, Marconi recruited him away from the\x01",
            "corps to join Revache & Co. permanently. Rossi\x01",
            "was the architect behind the mafia's militarization\x01",
            "and large increase in strength.\x02\x03",
            "In his jaeger days, Garcia Rossi earned the moniker\x01",
            "'Killing Bear' by using his large frame and advanced\x01",
            "military combat prowess to overwhelm enemy soldiers\x01",
            "on the battlefield.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_E53C")

    label("loc_DB73")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis054.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "Speaker Hartmann")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Hartmann is an extremely influential politician who\x01",
            "holds the position of Speaker of the Crossbell Diet.\x02\x03",
            "As a member of the diet, he also acts as the leader\x01",
            "of its Imperial Faction.\x02\x03",
            "A descendant of Erebonian nobility, Hartmann\x01",
            "owns a luxurious mansion, located at Mishelam\x01",
            "in the far southern reaches of Crossbell State.\x02\x03",
            "He is also considered an ally of Marconi, the\x01",
            "president of Revache & Co. It's believed Hartmann\x01",
            "cooperates in the mafia's various criminal enterprises,\x01",
            "including smuggling, mira laundering, and so on.\x02\x03",
            "Furthermore, sources say that Hartmann had an\x01",
            "unofficial meeting with the Imperial Chancellor,\x01",
            "Giliath Osborne, last year in order to demonstrate\x01",
            "his domestic and foreign authority.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Jump("loc_E53C")

    label("loc_DECB")

    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis055.itp")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    MenuTitle(15, 100, 0, "Schwarze Auction")
    SetMessageWindowPos(10, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "The Schwarze Auction is an annual event staged by\x01",
            "Revache on the final day of the Anniversary Festival.\x02\x03",
            "It's held in the form of a private, largely secret party\x01",
            "hosted at Speaker Hartmann's mansion in Mishelam.\x02\x03",
            "Most items up for bid are first-class works of art,\x01",
            "such as paintings and jewelry, acquired through\x01",
            "theft, bribery, tax evasion, and illegal back channels.\x02\x03",
            "Additionally, invites are not limited to just Crossbellans.\x01",
            "Nobles and affluent people from across the continent\x01",
            "are extended invitations, making the auction function\x01",
            "as an off the record gathering of Zemuria's high society.\x02\x03",
            "The Schwarze Auction is a major source of income for\x01",
            "Revache. It also provides Speaker Hartmann with the\x01",
            "ideal place to network with influential figures.\x02\x03",
            "Security is solely handled by Revache's forces, as well.\x01",
            "Entry is prohibited unless a guest possesses a black\x01",
            "invitation card engraved with a golden rose.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#3300709V#0007FI-Is this real?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#3300710V#0105FU-Unbelievable...\x02\x03",
            "#3300711V#0101FTo think that something this massive\x01",
            "has been happening every single year...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#3300712V#0201FBut this is strange, is it not?\x02\x03",
            "#3300713VDespite being a secret, this information\x01",
            "describes it as a large-scale social event...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#3300714V#0306FWell, no doubt the police and mass media\x01",
            "know already and gotta keep it under wraps.\x02\x03",
            "#3300715V#0301FNeither of them would want the spotlight\x01",
            "on a shady event like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        "#3300716VExactly.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#3300717V#0011F...?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    SetScenarioFlags(0x0, 7)
    Jump("loc_E53C")

    label("loc_E537")

    Jump("loc_E53C")

    label("loc_E53C")

    Jump("loc_CC65")

    label("loc_E541")

    OP_68(14500, 1850, 10200, 2000)
    MoveCamera(60, 17, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24500, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, 6500, 850, 10500, 90)
    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01000.itp")
    OP_68(13500, 1850, 10200, 2000)

    def lambda_E5CF():
        OP_95(0xFE, 10500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E5CF)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    MenuCmd(4, 0, 0x0)

    def lambda_E600():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E600)
    Sleep(50)

    def lambda_E610():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E610)
    Sleep(50)

    def lambda_E620():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E620)
    Sleep(50)

    def lambda_E630():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E630)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x11, 1)

    ChrTalk(
        0x101,
        "#3300718V#0005F#11PChief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3300719V#11P#0108FG-Good evening.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x11,
        (
            "#3300720VColor me surprised.\x01",
            "You all found out the\x01",
            "truth on your own.\x02\x03",
            "#3300721VHmm, this place is a bit stuffy.\x02\x03",
            "#3300722VC'mon. I'll give you the full\x01",
            "rundown in my office.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    SetCameraDistance(25000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    SetChrPos(0x11, 64000, 150, 11400, 180)
    SetChrChipByIndex(0x11, 0x6)
    SetChrSubChip(0x11, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7513", 0)
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        (
            "#3300723V#12P#0013FSo you admit that all the information\x01",
            "in those files is accurate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3300724V#5P#1003FYeah, unfortunately so.\x02\x03",
            "#3300725V#1002FBeats me who was researching them,\x01",
            "but they made quite the pile of info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3300726V#0106FB-But...\x02\x03",
            "#3300727V#0101FAll the CPD's top brass\x01",
            "know about this, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3300728V#5P#1003FMore or less all of them.\x02\x03",
            "#3300729V#1001FPeople outranking inspectors, for sure,\x01",
            "but I'd be shocked if most of the First\x01",
            "Division wasn't aware of the auction.\x02\x03",
            "#3300730VHell, even Arios and the Bracer Guild\x01",
            "have probably known of its existence\x01",
            "for a while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300731V#12P#0010FTch... That means this is another\x01",
            "barrier standing in our way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3300732V#5P#1011FOh, yeah...an extraordinarily huge barrier.\x02\x03",
            "#3300733V#1001FLet me be blunt. I don't intend on\x01",
            "restricting what you do, but...\x02\x03",
            "#3300734V...stop poking your nose into\x01",
            "the Schwarze Auction, got it?\x02\x03",
            "#3300735VThis is beyond your pay grade, kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300736V#12P#0007FB-But Chief!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3300737V#0303FNow, now, Chief.\x01",
            "Let's not mince words here.\x02\x03",
            "#3300738V#0301FInstead of being beyond our ability, you mean\x01",
            "to say the police have their hands tied, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#3300739V#5P#1000F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3300740V#0108FConsidering all the influential figures\x01",
            "invited and the host of the entire\x01",
            "gathering, Speaker Hartmann...\x02\x03",
            "#3300741V#0106F...the auction is practically untouchable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300742V#12P#0206FIf the citizenry is not in imminent danger,\x01",
            "the Bracer Guild cannot act, either...\x02\x03",
            "#3300743VIs it futile to pursue this any further?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300744V#12P#0010FTh-That may be the case, but...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3300745V#5P#1003FCalm down. You aren't the only\x01",
            "frustrated person here, trust me.\x02\x03",
            "#3300746VThink about the First Division, grinding their\x01",
            "teeth every year, powerless to do anything.\x02\x03",
            "#3300747V#1001FIf this event ever gave them the slightest\x01",
            "chance, they'd be charging in to take it\x01",
            "down before even the guild could respond...\x02\x03",
            "#3300748VBut, despite being shady, it appears\x01",
            "to be just another gorgeous party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300749V#12P#0008FDamn...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3300750V#5P#1003FBasically, if you tried to crack down\x01",
            "on the Schwarze Auction and screwed\x01",
            "up, the SSS would be finished.\x02\x03",
            "#3300751VThat's why, for your own good,\x01",
            "I can't let you chase after this.\x02\x03",
            "#3300752V#1000FAnyway, that's the gist of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300753V#12P#0008F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3300754V#0108F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3300755V#0303FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300756V#12P#0203FThat was not bleak in the slightest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#3300757V#5P#1001FListen. I'm not telling you to accept how things are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300758V#12P#0005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3300759V#5P#1001FJust understand, sometimes you have to\x01",
            "chin up, look forward, and figure out how\x01",
            "much you can really accomplish.\x02\x03",
            "#3300760VDon't forget that pit in your stomach right\x01",
            "now, though. Do that, and your chance will\x01",
            "come one day.\x02\x03",
            "#3300761V#1004FSo don't get too down, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#3300762V#12P#0006F#40WI...understand, sir.\x02\x03",
            "#3300763V#0008F#30WFrom now on, we'll stop...\x01",
            "...stop looking into the auction.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F404():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F404)
    Sleep(50)

    def lambda_F414():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F414)
    Sleep(50)

    def lambda_F424():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F424)
    Sleep(300)

    ChrTalk(
        0x102,
        "#3300764V#0108F#11PLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300765V#12P#0208FAre you sure, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3300766V#0306FDamn. This turned out well...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "With that, the third day of the Anniversary Festival ended.\x02\x03",
            "Tio's past, a mysterious story of Lloyd's brother,\x01",
            "a hacker known as Kitty, a detailed report\x01",
            "regarding Revache...\x02\x03",
            "...and then the Schwarze Auction, sitting at\x01",
            "the center of Crossbell's injustices.\x02\x03",
            "With all of it still spinning inside of his head,\x01",
            "Lloyd quickly fell asleep.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(2000)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    ReplaceBGM("ed7000", "ed7000")
    SetScenarioFlags(0x5C, 2)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_A0E7 end

    def Function_26_F699(): pass

    label("Function_26_F699")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50092.itc", 0x1E)
    LoadChrToIndex("apl/ch50404.itc", 0x1F)
    LoadChrToIndex("chr/ch08201.itc", 0x20)
    LoadChrToIndex("apl/ch50380.itc", 0x21)
    OP_68(5500, 700, 6300, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26000, 0)
    SetChrPos(0x101, -1000, 0, -1500, 0)
    SetChrPos(0x102, 800, 0, 500, 0)
    SetChrPos(0x103, 800, 0, 0, 0)
    SetChrPos(0x104, 800, 0, 0, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    SetChrPos(0xD, 5500, 100, 6300, 180)
    SetChrPos(0x10, 2710, 0, 2100, 225)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x10)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 5300, 350, 4400, 0)
    ClearMapFlags(0x10000000)
    SetCameraDistance(25000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#4100751V#1P#0002FPhew. We're home.\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(2036, 255, 100, 0)
    Sleep(150)

    ChrTalk(
        0xD,
        "#4100752V#5P#1110FOh, you're back! Yay!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0xD, 0x20)
    ClearChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    Sound(804, 0, 100, 0)
    OP_9D(0xD, 0x157C, 0x0, 0x157C, 0x12C, 0xFA0)
    BeginChrThread(0xD, 3, 0, 27)
    SetChrPos(0x101, 800, 0, 500, 0)
    BeginChrThread(0x101, 3, 0, 28)
    Sleep(1000)
    Sound(2037, 255, 100, 0)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x101, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    ChrTalk(
        0x101,
        (
            "#4100753V#12P#0012F#11PHaha, I wish I could be as full of\x01",
            "energy as you always are, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4100754V#1109F#5PYup! I'm always\x01",
            "ready to roll!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x0)

    def lambda_F96A():
        OP_96(0xFE, 0xC8, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F96A)
    WaitChrThread(0xD, 1)
    SetChrFlags(0xD, 0x40)

    ChrTalk(
        0xD,
        (
            "#4100755V#1110F#5PYou're late... Was there\x01",
            "a lot of work today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100756V#0102F#11PHehe, more or less.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100757V#0309F#11PBet we would have keeled over\x01",
            "if we didn't have that nice car\x01",
            "to drive 'round in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4100758V#12P#0203FI second that...\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_FAA6():

        label("loc_FAA6")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_FAA6")

    QueueWorkItem2(0x101, 2, lambda_FAA6)

    def lambda_FAB8():

        label("loc_FAB8")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_FAB8")

    QueueWorkItem2(0x102, 2, lambda_FAB8)

    def lambda_FACA():

        label("loc_FACA")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_FACA")

    QueueWorkItem2(0x103, 2, lambda_FACA)

    def lambda_FADC():

        label("loc_FADC")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_FADC")

    QueueWorkItem2(0x104, 2, lambda_FADC)
    OP_68(200, 1000, 2500, 1500)

    def lambda_FAFF():
        OP_95(0xFE, -900, 0, 3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FAFF)
    WaitChrThread(0xD, 1)

    def lambda_FB1D():
        OP_95(0xFE, -900, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FB1D)
    WaitChrThread(0xD, 1)
    TurnDirection(0xD, 0x103, 500)

    ChrTalk(
        0xD,
        (
            "#4100759V#6P#1112FHey, Tio.\x02\x03",
            "#4100760VYou look super tired. Are you all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#4100761V#0204F#11PYes. I will be fine.\x02\x03",
            "#4100762V#0202FAfter all, seeing your cute face has\x01",
            "reenergized my batteries, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#4100763V#6P#1111FHmm...\x02",
    )

    CloseMessageWindow()
    OP_68(500, 1000, 2500, 600)

    def lambda_FC5B():
        OP_95(0xFE, -300, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FC5B)
    WaitChrThread(0xD, 1)

    def lambda_FC79():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_FC79)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    Sound(804, 0, 100, 0)
    Sound(910, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x103,
        "#4100764V#0205F#11PK-KeA?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4100765V#6P#1109FSince I'm so full of energy, I don't mind\x01",
            "sharing some with you!\x02\x03",
            "#4100766V#1104FHeehee... *snuggle*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4100767V#0202F#11PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100768V#5P#0009FHaha, that's KeA for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100769V#0304F#11PHeh. Never seen medicine that potent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100770V#5P#0109FHeehee, perhaps a KeA hug is stronger\x01",
            "than a wonder drug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100771V#0204F#11PThank you, KeA.\x02\x03",
            "#4100772V#0202FI think I am sufficiently recharged.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x0)

    def lambda_FE88():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FE88)
    WaitChrThread(0xD, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    ChrTalk(
        0xD,
        "#4100773V#6P#1110FI'm glad!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#4100774V#5P#0000FCome to think of it... Is the\x01",
            "chief not home yet, KeA?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)

    ChrTalk(
        0xD,
        (
            "#4100775V#6P#1100FThe chief? Oh, he's over\x01",
            "in his office.\x02\x03",
            "#4100776VA visitor came by, and he's\x01",
            "still talking with him.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#4100777V#5P#0005FA visitor? That's pretty rare,\x01",
            "considering the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100778V#5P#0100FDo you remember what he looked like?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4100779V#6P#1103FHmmm...he's an old man with a BIG\x01",
            "beard. He kinda reminds me of a bear.\x02\x03",
            "#4100780V#1110FI think the chief called him\x01",
            "something like a...lawyer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100781V#5P#0000FOh, Mr. Grimwood's here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100782V#0300F#11PWhy's he stoppin' by so late?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100783V#5P#0100FShall we go greet him while\x01",
            "we have the opportunity?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#4100784V#12P#0202FI will leave all that to you.\x01",
            "I am on kitchen duty tonight.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#4100785V#5P#0001FYou all right with cooking for everyone?\x01",
            "If you want, I could take over for you\x01",
            "tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100786V#12P#0204FNo, I already made preparations for\x01",
            "dinner earlier. It should be almost ready.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#4100787V#0202F#11PKeA, hold on for just a little while\x01",
            "longer, okay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x103, 500)

    ChrTalk(
        0xD,
        "#4100788V#6P#1109FOh, can I help you get the food ready?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100789V#0205F#11PYou want to?\x02\x03",
            "#4100790V#0204FWell, then, you will be my sous chef.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10419():

        label("loc_10419")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_10419")

    QueueWorkItem2(0x101, 2, lambda_10419)

    def lambda_1042B():

        label("loc_1042B")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1042B")

    QueueWorkItem2(0x102, 2, lambda_1042B)

    def lambda_1043D():

        label("loc_1043D")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1043D")

    QueueWorkItem2(0x104, 2, lambda_1043D)
    OP_93(0xD, 0x0, 0x1F4)
    BeginChrThread(0xD, 3, 0, 29)
    Sleep(250)
    BeginChrThread(0x103, 3, 0, 30)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0xD, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    RemoveParty(0x2, 0x0)
    SetChrPos(0xB, 124300, 0, 8200, 0)
    OP_4C(0xD, 0xFF)
    SetChrPos(0xD, 123300, 30, 8200, 0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_68(900, 1000, 2800, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 900, 0, 2800, 0)
    SetChrPos(0x1, 900, 0, 2800, 0)
    SetChrPos(0x2, 900, 0, 2800, 0)
    SetChrPos(0x10, 2710, 0, 2510, 225)
    SetScenarioFlags(0xC2, 1)
    OP_29(0x4A, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_26_F699 end

    def Function_27_1055E(): pass

    label("Function_27_1055E")

    SetChrFlags(0xD, 0x40)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    Sound(51, 0, 100, 0)
    Sound(58, 0, 100, 0)

    def lambda_1057C():
        OP_95(0xFE, 2800, 0, 5500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1057C)
    WaitChrThread(0xD, 1)
    OP_68(200, 1000, 3500, 1500)
    SetCameraDistance(23000, 1500)

    def lambda_105B4():
        OP_95(0xFE, 900, 0, 4900, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_105B4)
    WaitChrThread(0xD, 1)

    def lambda_105D2():
        OP_95(0xFE, 200, 0, 3500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_105D2)
    WaitChrThread(0xD, 1)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    Sound(819, 0, 100, 0)

    def lambda_105FE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_105FE)

    def lambda_1060B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1060B)
    Sleep(500)
    Return()

    # Function_27_1055E end

    def Function_28_10623(): pass

    label("Function_28_10623")


    def lambda_10628():
        OP_96(0xFE, 0xC8, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10628)

    def lambda_10642():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10642)
    Sleep(250)

    def lambda_10656():
        OP_96(0xFE, 0x514, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10656)

    def lambda_10670():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10670)
    Sleep(400)

    def lambda_10684():
        OP_96(0xFE, 0xC8, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10684)

    def lambda_1069E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1069E)
    Sleep(250)

    def lambda_106B2():
        OP_96(0xFE, 0x514, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_106B2)

    def lambda_106CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_106CC)
    WaitChrThread(0x101, 1)

    def lambda_106E1():

        label("loc_106E1")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_106E1")

    QueueWorkItem2(0x101, 2, lambda_106E1)
    WaitChrThread(0x102, 1)

    def lambda_106F7():

        label("loc_106F7")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_106F7")

    QueueWorkItem2(0x102, 2, lambda_106F7)
    WaitChrThread(0x103, 1)

    def lambda_1070D():

        label("loc_1070D")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1070D")

    QueueWorkItem2(0x103, 2, lambda_1070D)
    WaitChrThread(0x104, 1)

    def lambda_10723():

        label("loc_10723")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_10723")

    QueueWorkItem2(0x104, 2, lambda_10723)
    Return()

    # Function_28_10623 end

    def Function_29_10731(): pass

    label("Function_29_10731")


    def lambda_10736():
        OP_95(0xFE, -900, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10736)
    WaitChrThread(0xD, 1)

    def lambda_10754():
        OP_95(0xFE, 400, 0, 6600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10754)
    WaitChrThread(0xD, 1)

    def lambda_10772():
        OP_95(0xFE, 3500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10772)
    WaitChrThread(0xD, 1)

    def lambda_10790():
        OP_95(0xFE, 8500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10790)
    WaitChrThread(0xD, 1)
    Return()

    # Function_29_10731 end

    def Function_30_107AA(): pass

    label("Function_30_107AA")


    def lambda_107AF():
        OP_95(0xFE, -900, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_107AF)
    WaitChrThread(0x103, 1)

    def lambda_107CD():
        OP_95(0xFE, 400, 0, 6600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_107CD)
    WaitChrThread(0x103, 1)

    def lambda_107EB():
        OP_95(0xFE, 3500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_107EB)
    WaitChrThread(0x103, 1)

    def lambda_10809():
        OP_95(0xFE, 8500, 850, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10809)
    WaitChrThread(0x103, 1)
    Return()

    # Function_30_107AA end

    def Function_31_10823(): pass

    label("Function_31_10823")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05900.itc", 0x1E)
    OP_68(63800, 1000, 7900, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 59000, -1000, 3000, 90)
    SetChrPos(0x102, 59000, 0, 3400, 90)
    SetChrPos(0x104, 59000, 0, 3400, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x13, 64599, 0, 7900, 270)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, 62900, 0, 7900, 90)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02200.itp")
    FadeToBright(1000, 0)
    OP_0D()
    Sound(811, 0, 100, 0)
    Sleep(500)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#4100791V#2PExcuse us.\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(103, 0, 100, 0)
    OP_68(64000, 1000, 6900, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_109AC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_109AC)

    def lambda_109B9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_109B9)
    SetChrPos(0x101, 59000, 0, 3400, 90)
    BeginChrThread(0x101, 3, 0, 32)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 33)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 34)

    ChrTalk(
        0x11,
        "#4100792V#1005F#5PHey, what took so long?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#4100793V#2202F#5POh, sorry to be intruding when it's so late.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#4100794V#12P#0002FSo it was Mr. Grimwood, after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100795V#0100F#12PIt's not every day you\x01",
            "decide to visit us.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x13,
        (
            "#4100796VYes, well, I had some matters to discuss\x01",
            "with Sergei.\x02\x03",
            "#4100797VSince I was in the neighborhood, I took\x01",
            "the opportunity to stop by.\x02",
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
        "#4100798V#12P#0005FMatters to discuss?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4100799V#1003F#5PYeah, I'll cut to the heart of it.\x01",
            "It's about KeA's identity.\x02",
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4100800V#12P#0013FO-Oh, then did you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100801V#12P#0301FYou guys figure anything out?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100802V#2203F#5PUnfortunately not...\x02\x03",
            "#4100803V#2201FIt seems a request was also submitted\x01",
            "to the guild, but I, at Sergei's behest,\x01",
            "explored another possibility.\x02\x03",
            "#4100804V#2203FUnfortunately, it wasn't--no... Actually,\x01",
            "I'm pleased to say the possibility I looked\x01",
            "into was a bust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100805V#12P#0005FYou were happy it was a bust?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4100806V#1003F#5PRight... It was pertaining to a story\x01",
            "several years back.\x02\x03",
            "#4100807V#1000FThere were multiple cases of child\x01",
            "abductions, primarily focused in the\x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4100808V#12P#0007FChild abductions?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100809V#0101F#12PH-Horrible...\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    ChrTalk(
        0x11,
        (
            "#4100810V#1003F#5PI'll omit the more...unnecessary details, but\x01",
            "it was a pretty massive scandal.\x02\x03",
            "#4100811VBecause Calvard wasn't the only country\x01",
            "targeted, an international investigation team\x01",
            "was created to get to the bottom of things.\x02\x03",
            "#4100812V#1001FEach country's army, police forces, the Bracer\x01",
            "Guild, you name it... Everyone cooperated to\x01",
            "put an end to that mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100813V#12P#0001FThat's crazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100814V#0106F#12PIt's the first I've heard of it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100815V#12P#0303FSame here.\x02\x03",
            "#4100816V#0301FSince it was kept under wraps, it must\x01",
            "have been pretty damn serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100817V#2203F#5PYes... Eventually, the case was closed.\x02\x03",
            "#4100818VDue to its nature, in the end, the case\x01",
            "was treated as strictly confidential.\x02\x03",
            "#4100819V#2201FOnly reason I know about it is because\x01",
            "I was involved, serving as an adviser.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100820V#12P#0011FP-Please, hold on a second.\x02\x03",
            "#4100821V#0013FYou're saying there's a chance KeA could\x01",
            "be one of the victims from this whole\x01",
            "abduction incident?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100822V#2201F#5PI thought the same thing, so I searched\x01",
            "through the case records again...\x02\x03",
            "#4100823VTo my relief, I wasn't able to find any\x01",
            "children who matched KeA's description.\x02\x03",
            "#4100824V#2203FFor the record, the men responsible for\x01",
            "those horrors were almost all arrested,\x01",
            "and the rest committed suicide.\x02\x03",
            "#4100825V#2200FToday, I simply came to inform Sergei\x01",
            "of my findings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100826V#12P#0006FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100827V#0108F#12PI'm relieved that KeA wasn't a part of that,\x01",
            "but the fact that it actually happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4100828V#1003F#5PI would've ended up telling\x01",
            "you about all this eventually.\x02\x03",
            "#4100829V#1001FAnyway, we're back to square\x01",
            "one with KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100830V#12P#0302FWell, no skin off our back, right?\x02\x03",
            "#4100831VJust gotta keep lookin' after the kiddo\x01",
            "until we find one of her relatives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100832V#2202F#5PRight, I'd appreciate it if you kept\x01",
            "sheltering the child here.\x02\x03",
            "#4100833V#2210FBut in case we can't end up finding\x01",
            "a relative...\x02\x03",
            "#4100834V#2200F...we should consider entrusting her\x01",
            "to a foster family, or to a church\x01",
            "orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100835V#12P#0011FH-Hold on...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100836V#0108F#12PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4100837V#1003F#5PYou all need to wrap your heads around\x01",
            "those possibilities.\x02\x03",
            "#4100838V#1000FAdopting a kid and properly raising them?\x01",
            "That's not something you can jump into\x01",
            "half-assed.\x02\x03",
            "#4100839VNo matter how adorable she may be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100840V#12P#0008FTh-That might be true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100841V#12P#0306FIt's probably a bit more difficult than\x01",
            "takin' in a stray kitten or somethin'...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100842V#2202F#5PI'm sorry, everyone. Sounds like\x01",
            "I brought down the mood a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        (
            "#4100843V#2205F#5PYou all just returned from a long\x01",
            "day of work, correct?\x02\x03",
            "#4100844V#2202FI imagine you have a report to finish,\x01",
            "so it's about time I excuse myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100845V#12P#0000FNo, please wait.\x02\x03",
            "#4100846VThe truth is, there's something we were\x01",
            "planning on consulting you about...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        "#4100847V#2205F#5POh? With me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100848V#12P#0001FYes, actually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the situation with the missing\x01",
            "miner to Sergei and Mr. Grimwood.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0x11,
        (
            "#4100849V#1004F#5PSo you were working on a missing\x01",
            "persons case...\x02\x03",
            "#4100850V#1002FHeh. Sounds like a job for the SSS,\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100851V#12P#0006FIt didn't seem like anything illegal was going on,\x01",
            "so we just left him how he was.\x02\x03",
            "#4100852V#0001FI wonder if we should have tried a little harder\x01",
            "to get him to go home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4100853V#1003F#5PHmm, well, that's a complicated question.\x02\x03",
            "#4100854VIf you were bracers, there'd be a little more\x01",
            "wiggle room to negotiate. Comes with the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100855V#2203F#5PIf a police officer tried to pull that move, odds\x01",
            "are that the whole situation would turn into a\x01",
            "civil dispute...\x02\x03",
            "#4100856V#2200FIt's an exceedingly fine line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100857V#12P#0006FI was afraid you'd say that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100858V#12P#0304FThe guy is old enough to make his own decisions,\x01",
            "so, unfortunately, it's none of our business.\x02\x03",
            "#4100859V#0300FIf he were just some brat, we could have given\x01",
            "him a spankin' and taken him home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100860V#0102F#11PHeehee, that's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100861V#2201F#5PHowever, you mentioned he gained gambling skill,\x01",
            "luck, and intuition...like he was a different man?\x02\x03",
            "#4100862V#2203F...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_64(0x13)
    Sleep(1000)
    TurnDirection(0x11, 0x13, 500)

    ChrTalk(
        0x11,
        (
            "#4100863V#6P#1001FIan? Something about this rub you\x01",
            "the wrong way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100864V#5P#2203FWell, it might just be coincidence, but...\x02\x03",
            "#4100865V#2200FLately, two other similar stories have\x01",
            "come to my attention...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4100866V#12P#0001FIs that true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100867V#12P#0307FYou tellin' me there's not one, but THREE\x01",
            "lucky bastards who hit the jackpot?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100868V#2202F#5PNo, no, it's a bit different.\x02\x03",
            "#4100869V#2210FThe stories I heard about involve a stockbroker\x01",
            "who works for a securities firm, and the manager\x01",
            "of a trading company.\x02\x03",
            "#4100870V#2200FRecently, both companies sustained heavy losses\x01",
            "and were almost in the red...\x02\x03",
            "#4100871V...but in the last few days, they seem to have\x01",
            "experienced an incredible rebound. I could hardly\x01",
            "believe it until I saw the numbers.\x02\x03",
            "#4100872V#2203FEspecially that stockbroker... Story goes that he\x01",
            "bought and sold stocks with unprecedented luck\x01",
            "and intuition, as if he could see the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100873V#12P#0005FThat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100874V#12P#0301F...sounds pretty familiar.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100875V#2202F#5PHaha, don't worry. I'm sure it's only a\x01",
            "coincidence.\x02\x03",
            "#4100876V#2210FFrom what I've heard, their attitudes have\x01",
            "changed in addition to their skills. They've\x01",
            "supposedly become extremely arrogant.\x02\x03",
            "#4100877V#2200FThat tidbit piqued my interest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100878V#0103F#12PThat's definitely strange...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4100879V#6P#1003F...Hey, Ian.\x02\x03",
            "#4100880V#1000FAny chance you know the\x01",
            "backgrounds of these two?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x11, 500)

    ChrTalk(
        0x13,
        (
            "#4100881V#11P#2205FAh, not yet. But if you're interested,\x01",
            "I can start researching right away...\x02\x03",
            "#4100882V#2200FYou want to check possible ties,\x01",
            "I presume?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#4100883V#6P#1002FYes, if possible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100884V#12P#0001F#12PSomething catch your attention, Chief?\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#4100885V#1006F#5PWhen you're in this business, Lloyd,\x01",
            "it never hurts to have all the info\x01",
            "you can.\x02\x03",
            "#4100886V#1002FIt's as simple as that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100887V#12P#0000FAh, I understand...\x02\x03",
            "#4100888V#0004F(Guy told me something like that once, too...\x01",
            "That the decisive factors in an investigation\x01",
            "are intuition and the information you uncover.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0xB4, 0x1F4)

    ChrTalk(
        0x13,
        (
            "#4100889V#2210F#5PWell, then, I'll get out of your way now.\x02\x03",
            "#4100890V#2202FIf you ever have anything bothering you,\x01",
            "don't hesitate to stop by my office.\x02\x03",
            "#4100891VI'll do everything in my power to help out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100892V#12P#0002FThank you very much, Mr. Grimwood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100893V#0104F#12PWhen the time comes,\x01",
            "we'll come knocking.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    AddParty(0x2, 0xFF, 0xFF)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 1)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_10823 end

    def Function_32_12B43(): pass

    label("Function_32_12B43")


    def lambda_12B48():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12B48)

    def lambda_12B62():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12B62)
    WaitChrThread(0x101, 1)

    def lambda_12B77():
        OP_95(0xFE, 63500, 30, 5600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12B77)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_32_12B43 end

    def Function_33_12B98(): pass

    label("Function_33_12B98")


    def lambda_12B9D():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12B9D)

    def lambda_12BB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12BB7)
    WaitChrThread(0x102, 1)

    def lambda_12BCC():
        OP_95(0xFE, 64099, 30, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12BCC)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_33_12B98 end

    def Function_34_12BED(): pass

    label("Function_34_12BED")


    def lambda_12BF2():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12BF2)

    def lambda_12C0C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12C0C)
    WaitChrThread(0x104, 1)

    def lambda_12C21():
        OP_95(0xFE, 62900, 30, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12C21)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_34_12BED end

    def Function_35_12C42(): pass

    label("Function_35_12C42")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50411.itc", 0x1E)
    LoadChrToIndex("apl/ch50420.itc", 0x1F)
    LoadEffect(0x0, "event\\eva05_00.eff")
    OP_68(206000, 700, 123200, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x103, 0x20)
    SetChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x1F)
    SetChrPos(0x103, 208750, 50, 129400, 0)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x3)
    SetChrPos(0xD, 208900, 50, 128900, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, 206000, 30, 123200, 180)
    BeginChrThread(0xF, 1, 0, 36)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis088.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis089.itp")
    CreatePortrait(2, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis087.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetMapObjFlags(0x1C, 0x4)
    SetMapObjFrame(0xFF, "t_huton", 0x0, 0x1)
    ClearMapObjFlags(0x22, 0x4)
    OP_7D(0xB3, 0xB3, 0xC7, 0x0, 0x0)
    OP_68(208800, 700, 129100, 7000)
    MoveCamera(45, 20, 0, 7000)
    SetCameraDistance(22500, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(208800, 700, 129100, 0)
    MoveCamera(40, 29, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(20000, 4000)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(64800, 1600, 7250, 0)
    MoveCamera(54, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, 66600, 0, 6900, 90)
    OP_4B(0x11, 0xFF)
    SetChrPos(0x101, 62700, 0, 6900, 90)
    SetChrPos(0x102, 61400, 0, 6300, 90)
    SetChrPos(0x104, 61400, 0, 7500, 90)
    OP_68(64800, 1000, 7250, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#4201150V#1003F#5PDamn it. That name again...\x02\x03",
            "#4201151V#1001F'Gnosis'...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4201152V#0003F#6PChief, it's about time you tell us.\x02\x03",
            "#4201153V#0001FPlease, tell us what my brother was\x01",
            "involved in six years ago...and about\x01",
            "the cult that kidnapped Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4201154V#6P#0101FI take it you're aware of everything\x01",
            "that happened, right, Chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201155V#6P#0306FSame. I had a gut feelin' that you knew\x01",
            "what was up with Tio Tot from the start.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)
    OP_93(0x11, 0x10E, 0x190)
    Sleep(500)
    OP_68(64650, 900, 7570, 1300)

    def lambda_13118():
        OP_95(0xFE, 65600, 0, 6900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_13118)
    WaitChrThread(0x11, 1)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#4201156V#1003F#11POf course I know about the cult.\x02\x03",
            "#4201157V#1000FAt their height, Guy and I were the ones\x01",
            "who tracked down and suppressed\x01",
            "one of the cult's lodges.\x02",
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
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    SetCameraDistance(21500, 100000)

    ChrTalk(
        0x101,
        (
            "#4201158V#0005F#6PY-You did?!\x02\x03",
            "#4201159V#0001FThen, Chief...you were my brother's...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201160V#1004F#11P#11PYeah, I was Guy's superior officer.\x02\x03",
            "#4201161V#1006FBack then, I guess I stood\x01",
            "out a bit more than I do now.\x02\x03",
            "#4201162VOne day, I got two unconventional\x01",
            "rookies assigned to serve under me.\x02\x03",
            "#4201163V#1002FOne of them being your brother...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201270V#0005F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201165V#1002F#11PGuy was impulsive, a bit reckless, too, but...\x01",
            "He was a damn great detective.\x02\x03",
            "#4201166V#1004FNow, the other rookie was in stark contrast\x01",
            "with Guy, in all the right ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4201167V#6P#0101FWho exactly was this\x01",
            "other rookie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201168V#6P#0305FNo way...was it that Dudley\x01",
            "guy from the First Division?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201169V#1003F#11PNope. That guy went straight into\x01",
            "the First Division. He's a natural.\x02\x03",
            "#4201170VYou've probably heard of the\x01",
            "other rookie before, actually...\x02\x03",
            "#4201171V#1002FHis name is Arios MacLaine.\x02",
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
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#4201172V#0011F#6PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4201173V#6P#0105FH-He was a part of the police?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201174V#1003F#11PHe was. He traded his police badge in\x01",
            "for the bracers' gauntlet some years back.\x02\x03",
            "#4201175V#1000FHell, that's probably one of the reasons\x01",
            "the police here in Crossbell have such\x01",
            "animosity towards the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4201176V#6P#0306FWhat a twist...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4201177V#0006F#6PMy brother and Arios were both\x01",
            "in the force together...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201178V#1002F#11PAge-wise, Arios beats Guy\x01",
            "in that category.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#4201179V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30WArios already tied the knot and had\x01",
            "recently had a daughter. Trust me, he's\x01",
            "always been the serious man he is.\x02\x03",
            "#4201180V#30WOn the other hand, Guy was a wild card,\x01",
            "always acting rash...an optimistic fool.\x02\x03",
            "#4201181V#30WGiven how different they were, that's probably\x01",
            "why they started to get along in the first place.\x02\x03",
            "#4201182V#30WIn a little less than two years after\x01",
            "joining the force, these guys were\x01",
            "heralded as the police's ace duo.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0x0, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis090.itp")

    ChrTalk(
        0x101,
        "#4201183V#0008F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4201184V#6P#0106FJ-Judging by Arios' skill, I can\x01",
            "hardly doubt that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201185V#1002F#11PRight...? I'll be honest.\x01",
            "I was proud of those boys.\x02\x03",
            "#4201186VAfter all, not many are blessed with the chance\x01",
            "to raise such fine greenhorns like those two.\x02\x03",
            "#4201187V#1004FOur squad was able to accomplish\x01",
            "a lot while we were operating...\x02\x03",
            "#4201188VEventually, higher-ups decided to leave the\x01",
            "joint investigation of an international case\x01",
            "on our desk, instead of the First Division's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201189V#0005F#6PJoint investigation...? International case...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4201190V#6P#0301FYou aren't sayin' that it was...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201191V#1003F#11PYes. It involved the cult.\x02\x03",
            "#4201192V#1001FD∴G... That's their official name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201193V#0013F#6P'D...therefore G'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4201194V#6P#0301FWhat the hell's that mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4201195V#6P#0108FAs in, a mathematical equation\x01",
            "using 'therefore'? But then...\x02\x03",
            "#4201196V#0101F...what exactly do the 'D' and 'G'\x01",
            "stand for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201197V#1003F#11PWe never solved the entire riddle...\x01",
            "but we did uncover what the\x01",
            "meaning of the 'G' is.\x02\x03",
            "#4201198V#1001FIt stands for 'Gnosis'.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4201199V#0013F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4201200V#6P#0101FThe drug that unleashes demonic power\x01",
            "Doctor Guenter told us about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4201201V#6P#0307FThis has gotta be connected...!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7526", 0)

    ChrTalk(
        0x11,
        (
            "#4201202V#1001F#11PIt's already been six years since\x01",
            "that whole mess...\x02\x03",
            "#4201203V#1003FThose zealots left behind a lot of mysteries.\x01",
            "But I know one thing for sure...\x02\x03",
            "#4201204VOut of my decades of service on the force,\x01",
            "this was the most disgusting bunch I ever\x01",
            "had the displeasure of taking down.\x02\x03",
            "#4201205V#1010FThe bastards used those kids they\x01",
            "kidnapped as sacrifices at their lodges.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201206V#0010F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4201207V#6P#0108FThe abduction case Mr. Grimwood mentioned\x01",
            "yesterday...\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#4201208V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WThe D∴G cult...\x02\x03",
            "#4201209V#30WThey had more than ten active lodges\x01",
            "spread all across Zemuria.\x02\x03",
            "#4201210V#30WAnd they performed various 'rituals'\x01",
            "in each of them...\x02\x03",
            "#4201211V#30WSummoning horrific devils, taking\x01",
            "advantage of artifacts for their gain,\x01",
            "experimenting on those poor children...\x02\x03",
            "#4201212V#30WAnd there was always one\x01",
            "constant in their rituals...\x02\x03",
            "#4201213V#30WA mysterious drug called 'Gnosis.'\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis091.itp")

    ChrTalk(
        0x101,
        "#4201214V#0008F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4201215V#6P#0106FI mean...\x01",
            "It's a hard story to digest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201216V#6P#0301FSo, how'd you end up snuffin'\x01",
            "them out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#4201217V#1003F#11PRight.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#4201218V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30WLike I mentioned yesterday, this issue was spreading\x01",
            "into each country, so a joint investigation team was\x01",
            "organized by the nations affected.\x02\x03",
            "#4201219V#30WEach country's armies, police forces, and the Bracer\x01",
            "Guild collaborated.\x02\x03",
            "#4201220V#30WA large-scale operation to round up and suppress\x01",
            "every lodge operated by the cult was mounted--\x01",
            "all under the command of a famous bracer.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x4, 0x0, 0x0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#4201221V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30WAs for my small squad of three, we were in charge\x01",
            "of taking down a lodge located on the outskirts of\x01",
            "Altair, located in western Calvard.\x02\x03",
            "#4201222V#30WGuy rescued Tio Plato, who was eight years old at\x01",
            "the time.\x02\x03",
            "#4201223V#30WTio was completely and utterly debilitated, but\x01",
            "still in better shape than others...\x02\x03",
            "#4201224V#30WWe couldn't save any of the other children...\x02\x03",
            "#4201225V#30W...but compared to some of the monstrous rituals\x01",
            "happening in the other lodges, I like to think they\x01",
            "were shown a little mercy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)

    ChrTalk(
        0x101,
        "#4201226V#0006F#6PWhy...?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#4201227V#0010F#6PWhy are people like this\x01",
            "allowed to exist?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4201228V#6P#0108FI...I feel like I'm going to be sick.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201229V#6P#0303FThese guys are on a whole different level\x01",
            "than Crossbell's day-to-day criminals...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201230V#1003F#11PSo you say...\x02\x03",
            "#4201231V#1001FAt any rate, after that operation six years ago,\x01",
            "the cult was completely wiped off the map.\x02\x03",
            "#4201232VAll the cult's zealots either committed suicide\x01",
            "or suffered a mental breakdown and died.\x02\x03",
            "#4201233VSome have speculated that there were a few\x01",
            "survivors, but it's also been said that the church\x01",
            "and that 'society' exterminated the rest of them.\x02\x03",
            "#4201234V#1003FThe nightmare known as the D∴G cult\x01",
            "should have finally been over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201235V#0008F#6PHowever...these blue pills pose a threat.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#4201236V#0013FIt's possible that these pills are the same\x01",
            "Gnosis used in the cult's rituals.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x11,
        (
            "#4201237V#1003FRight now, that's just speculation on my part...\x02\x03",
            "#4201238V#1001FBut if this is the real deal, I'm afraid\x01",
            "the nightmare of six years ago might\x01",
            "have resurfaced in another form.\x02\x03",
            "#4201239VOne that will be at the heart of the\x01",
            "underworld's conflicts.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    ChrTalk(
        0x104,
        "#4201240V#6P#0306FThat's the worst-case scenario...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4201241V#6P#0101FBut if this is the truth, we...we can't\x01",
            "overlook this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#4201242V#1010F#11PI couldn't agree more.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(1000)
    Sound(852, 0, 100, 0)
    Sleep(500)
    PlayEffect(0x0, 0x0, 0x11, 0x140, 0, 1300, 350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)

    ChrTalk(
        0x11,
        (
            "#4201243V#1001F#11PLloyd.\x02\x03",
            "#4201244VThe criminal who murdered your brother\x01",
            "three years ago is still at large.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4201245V#0003F#6PI know.\x02\x03",
            "#4201246V#0001FNo leads were found and the case\x01",
            "eventually went cold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201247V#1006F#11PYeah... After Guy transferred to the First Division,\x01",
            "he would only investigate cases by himself, so\x01",
            "there were no witnesses.\x02\x03",
            "#4201248VThe culprit has been speculated to be one\x01",
            "of the major powers' intelligence agencies,\x01",
            "Revache, or maybe another crime syndicate...\x02\x03",
            "#4201249VHell, some have tossed around the idea of a\x01",
            "jaeger corps or terrorist cell being responsible.\x02\x03",
            "#4201250V#1001FHowever...there's always been another\x01",
            "possible culprit in my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201251V#0008F#6PA remnant of the cult...right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201252V#1003F#11PYeah. I'd say that possibility is even\x01",
            "more likely, now.\x02\x03",
            "#4201253VIn a sense, this is becoming a battle\x01",
            "to avenge my fallen subordinate.\x02\x03",
            "#4201254V#1002FPardon my selfishness, but from\x01",
            "now on, I'll be butting in, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201255V#0005F#6PChief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4201256V#6P#0102FO-On the contrary,\x01",
            "we'd love your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201257V#6P#0302FYou tryin' to imply that you haven't\x01",
            "had our back up until now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201258V#1004F#11PWho knows?\x02\x03",
            "#4201259V#1002FIt's about time you know. I founded the\x01",
            "Special Support Section based entirely\x01",
            "on Guy's original idea.\x02",
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4201260V#0005F#6PS-Seriously? My brother...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4201261V#6P#0101FBut what about the SSS being created\x01",
            "to oppose the guild's popularity...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201262V#1002F#11PThat was purely an excuse\x01",
            "to appease the top brass.\x02\x03",
            "#4201263V#1004FWhile he was still alive, Guy told\x01",
            "me something I'll never forget.\x02\x03",
            "#4201264VHe said that what Crossbell needs is\x01",
            "the strength to overcome 'barriers'...\x02\x03",
            "#4201265VA place where youth can continue to\x01",
            "move forward, despite failures, joining\x01",
            "their strength into one...\x02\x03",
            "#4201266V#1002F'Don't you think that's what the\x01",
            "police really needs?' he asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201267V#0000F#6PGuy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201268V#6P#0304FI swear... You had yourself quite\x01",
            "the earnest brother, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#4201269V#6P#0105FThen, is it simply coincidence that Tio\x01",
            "ended up joining the SSS...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201164V#0005F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201271V#1003F#11PI imagine not. She probably wanted, more than\x01",
            "anything, to be in a place where Guy's will lives.\x02\x03",
            "#4201272VNot that she's told me anything like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201273V#0008F#6PI see... That makes sense.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#4201274V#0003F#6PSetting aside Guy for now...\x02\x03",
            "#4201275V...our focus needs to be on our investigation\x01",
            "into stopping these drugs.\x02\x03",
            "#4201276V#0013FAnd, regarding KeA...\x02\x03",
            "#4201277V...it's possible that she was involved in that\x01",
            "cult in some shape or form.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#4201278V#6P#0101FAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201279V#6P#0308FTsk, pisses me off to say, but it's likely.\x02\x03",
            "#4201280VAfter all that talk about drugs being the\x01",
            "cause of her amnesia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201281V#1001F#11PYeah... Unfortunately, I'm beginning\x01",
            "to think that as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4201282V#0004F#6PSo, Chief...\x02\x03",
            "#4201283V#0000FCould you leave the heavy\x01",
            "lifting to us while you protect\x01",
            "KeA here?\x02\x03",
            "#4201284VWe should be able to cooperate with the\x01",
            "First Division, but we still need support.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        "#4201285V#1005F#11POh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4201286V#6P#0105FTh-That's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201287V#6P#0303FYeah, it's gonna be necessary for us to have\x01",
            "someone pullin' the strings back at the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4201288V#0006F#6PI'm sorry.\x02\x03",
            "#4201289VI know you went out of your way to offer\x01",
            "your help, but this is key to our success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4201290V#1009F#11PHeh. That right?\x02\x03",
            "#4201291V#1004FAll right, fine.\x02\x03",
            "#4201292V#1001FListen up, just like before, I won't be\x01",
            "giving any direct instruction.\x02\x03",
            "#4201293VYou can have all the advice you want.\x01",
            "I'll even take care of comms for you.\x02\x03",
            "#4201294VBut you're going to make your own decisions\x01",
            "and solve this case with your own will.\x02\x03",
            "#4201295V#1002FSo, are you up to the challenge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201296V#0000F#6PYes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4201297V#6P#0100FUnderstood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201298V#6P#0304FOh, boy. Startin' tomorrow, it sounds like\x01",
            "we're going to have our work cut out for us.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopEffect(0x0, 0x0)
    StopBGM(0x1388)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(2000)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x2)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetScenarioFlags(0x5D, 5)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_12C42 end

    def Function_36_1606B(): pass

    label("Function_36_1606B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16089")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_36_1606B")

    label("loc_16089")

    Return()

    # Function_36_1606B end

    def Function_37_1608A(): pass

    label("Function_37_1608A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x9, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch00150.itc", 0x1E)
    LoadChrToIndex("chr/ch00151.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00251.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("chr/ch00951.itc", 0x23)
    LoadChrToIndex("chr/ch08700.itc", 0x24)
    LoadChrToIndex("chr/ch08702.itc", 0x25)
    LoadChrToIndex("chr/ch31250.itc", 0x26)
    LoadChrToIndex("chr/ch31251.itc", 0x27)
    LoadChrToIndex("chr/ch31350.itc", 0x28)
    LoadChrToIndex("chr/ch31351.itc", 0x29)
    LoadChrToIndex("apl/ch50090.itc", 0x2A)
    LoadChrToIndex("apl/ch50011.itc", 0x2B)
    LoadChrToIndex("apl/ch50539.itc", 0x2C)
    LoadChrToIndex("apl/ch50506.itc", 0x2D)
    LoadChrToIndex("chr/ch02751.itc", 0x2E)
    LoadChrToIndex("chr/ch02752.itc", 0x2F)
    LoadChrToIndex("chr/ch10600.itc", 0x30)
    LoadChrToIndex("chr/ch10601.itc", 0x31)
    LoadChrToIndex("chr/ch10700.itc", 0x32)
    LoadChrToIndex("chr/ch10701.itc", 0x33)
    LoadChrToIndex("chr/ch00952.itc", 0x34)
    LoadChrToIndex("apl/ch50509.itc", 0x35)
    LoadEffect(0x0, "event\\ev606_00.eff")
    LoadEffect(0x1, "event\\ev608_00.eff")
    LoadEffect(0x2, "battle\\btgun00.eff")
    LoadEffect(0x3, "event\\eva01_00.eff")
    SoundLoad(821)
    OP_68(500, 900, 2500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    OP_4B(0x11, 0xFF)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 63800, 30, 8500, 0)
    SetChrPos(0x101, 63000, 0, 5700, 0)
    SetChrPos(0x102, 64300, 0, 5700, 0)
    SetChrPos(0x103, 63200, 0, 4400, 0)
    SetChrPos(0x104, 64500, 0, 4400, 0)
    SetChrPos(0x10A, 65200, 0, 8300, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrChipByIndex(0xD, 0x8)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 11300, 900, 6650, 90)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 500, 0, 2500, 180)
    BeginChrThread(0xF, 1, 0, 36)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13900, 900, 6650, 270)
    SetChrChipByIndex(0x15, 0x26)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x28)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrSubChip(0x18, 0x19)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13200, 1300, 6600, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x2A)
    SetChrSubChip(0x19, 0x19)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 12200, 1300, 6600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearMapObjFlags(0x20, 0x4)
    ClearMapObjFlags(0x21, 0x4)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    OP_68(12600, 1770, 6600, 7000)
    FadeToBright(2000, 0)
    Sleep(3000)
    OP_63(0xD, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x14, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_68(64000, 1100, 7600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    Sound(818, 0, 80, 0)
    Sleep(200)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x10A,
        (
            "#5200001V#0607FWhat could possibly be going through his\x01",
            "head right now?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)

    ChrTalk(
        0x10A,
        (
            "#5200002V#11P#0610FExactly what is Joachim Guenter hoping\x01",
            "to accomplish?\x02\x03",
            "#5200003VAnd what does he have to gain by intentionally\x01",
            "leaving behind incriminating evidence?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5200004V#1003F#11PAll valid questions, Dudley.\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x11,
        "#5200005V#1001F#5PWhat are the odds that this is just a setup?\x02",
    )

    CloseMessageWindow()

    def lambda_165A1():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_165A1)

    ChrTalk(
        0x101,
        (
            "#5200006V#12P#0006FGiven the situation, I don't think that would\x01",
            "accomplish much.\x02\x03",
            "#5200007V#0013FAll the evidence points to him. Not to mention\x01",
            "his connections with Revache and the speaker\x01",
            "are clear as day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200008V#0101FAnd if we factor in Yin's actions, the possibility\x01",
            "of Heiyue or the Republican Faction being the\x01",
            "true culprits is slim to none.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200009V#0306FIt's like the bastard is taunting us.\x02\x03",
            "#5200010V#0301FThat dumbass secretary was nothing like his\x01",
            "prissy self back in the hospital, either, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5200011V#12P#0206FI agree.\x02\x03",
            "#5200012V#0208FJudging by these files, and how obviously he\x01",
            "craved our attention, I felt as if this whole series of\x01",
            "events was nothing but a fanatic's provocation.\x02\x03",
            "#5200013V#0201FAnd then there is KeA to consider, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5200014V#1006F#5PRight...\x02\x03",
            "#5200015V#1001FWhat's so special about the kid that would\x01",
            "make him so obsessed with her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5200016V#11P#0602FH-How are you even entertaining the idea, Sergei?\x01",
            "She's just an ordinary girl, isn't she?\x02\x03",
            "#5200017VBut to go to such lengths to pull this off...\x01",
            "Just what is his aim?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5200018V#1003F#5PYou say that, Dudley, but...\x02\x03",
            "#5200019V#1001F...we still have to consider why KeA's photo\x01",
            "was in that white folder they found.\x02\x03",
            "#5200020VLloyd. Give me your thoughts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200021V#12P#0003FYes, sir.\x02\x03",
            "#5200022V#0008FWe know about all of those horrific rituals conducted\x01",
            "throughout Zemuria six years ago...\x02\x03",
            "#5200023V#0001FWhat if--and I hate to say this...but what if Guenter is\x01",
            "telling us that he plans on using KeA in the final ritual?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200024V#0101F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200025V#0310FTch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200026V#12P#0208FThat will NOT happen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200027V#12P#0003FRight. Of course it won't.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5200028V#6P#0013FDudley. How is the top brass reacting\x01",
            "to the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5200029V#0606F#5PUnfortunately, we've received a report\x01",
            "that the prison has been attacked.\x02\x03",
            "#5200030VAnd to put a cherry on top, I've heard that the\x01",
            "police academy, plus the training grounds nearby,\x01",
            "were raided, as well.\x02\x03",
            "#5200031V#0601FThe entire department is a hornet's nest right now.\x01",
            "No one knows how exactly to deal with the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200032V#6P#0006FThen we can't count on their backup anymore.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5200033V#12P#0001FFor now, let's move forward with asking the\x01",
            "Bracer Guild to get KeA out of the state.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_16F46():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_16F46)
    Sleep(50)

    def lambda_16F56():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_16F56)
    Sleep(50)

    def lambda_16F66():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_16F66)
    WaitChrThread(0x102, 2)

    ChrTalk(
        0x102,
        "#5200034V#0105F#11PAre you sure, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200035V#12P#0003FI am. But our condition will be that Arios, Estelle,\x01",
            "and Joshua have to be the ones to do it.\x02\x03",
            "#5200036V#0000FLiberl should be relatively safe and free from the\x01",
            "cult's influence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5200037V#1003F#5PLiberl, eh? Agreed. That would be the most secure\x01",
            "place for her right now.\x02\x03",
            "#5200038V#1000FI'll ask it again, though. Are you really okay with it?\x02\x03",
            "#5200039VYou'd be throwing away your ability to watch over\x01",
            "the kid yourself. Is it worth it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200040V#12P#0006FThis isn't about my pride or\x01",
            "self-satisfaction anymore.\x02\x03",
            "#5200041V#0008FYou can argue against this all you want...\x02\x03",
            "#5200042V#0001F...but if there's the slightest chance that KeA\x01",
            "can be safe, I'm taking it. No questions asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200043V#12P#0205FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200044V#0306FMan. There's no stoppin' you sometimes, is there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5200045V#0603F#5PIf that's your plan, you'd best not dawdle.\x02\x03",
            "#5200046V#0600FThe last international flight leaves at 9:30.\x02\x03",
            "#5200047VIf we hurry, she could be on her way to Liberl\x01",
            "by the end of the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5200048V#1003F#5PAll right, then. Contact the Bracer Guild.\x02\x03",
            "#5200049V#1002FIf Arios is back by now, it'd be smart to\x01",
            "let him handle KeA.\x02\x03",
            "#5200050VTrust me. He'd protect his daughter and KeA to\x01",
            "the bitter end, no matter what happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200122V#12P#0000FYes, sir!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x3)
    Sound(807, 0, 100, 0)
    Sleep(300)
    Sleep(300)
    Sound(902, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2800)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200052V\x07\x05",
            "Hellooo! You've reached the Crossbell branch\x01",
            "of the Bracer Guild!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5200053V\x07\x00",
            "#0001FMichel? This is Lloyd Bannings, from the\x01",
            "Special Support Section.\x02\x03",
            "#5200054VDo you have a moment? It's an emergency.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200055V\x07\x05",
            "Oh, hey sweetie.\x02\x03",
            "#5200056VWhat's the matter? If you were wondering\x01",
            "where any of my bracers are, none of 'em\x01",
            "made it back yet.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5200057V\x07\x00",
            "#0005FS-Seriously?\x02\x03",
            "#5200058V#0001FDo you know when Arios will be back in the\x01",
            "city?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200059V\x07\x05",
            "Arios? Well, he SHOULD be on his way back\x01",
            "already, if everything--\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0x1388)
    Sound(955, 0, 100, 0)
    Sleep(2000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200060V\x07\x05",
            "#2SWh-Who...?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200061V\x07\x05",
            "#2SIdentify yourself! I hope you aren't foolish\x01",
            "enough to cause trouble in the Bracer--\x02",
        )
    )

    CloseMessageWindow()
    Sound(531, 0, 60, 0)
    Sleep(300)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200062V\x07\x05",
            "#2SGah...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    Sound(356, 0, 70, 0)
    Sleep(1100)
    Sound(356, 0, 60, 0)
    Sleep(500)
    OP_24(0x164)
    Sound(825, 0, 100, 0)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5200063V\x07\x00",
            "#0005F...!\x02\x03",
            "#5200064V#0007FMichel! What's wrong?!\x02\x03",
            "#5200065V#0010F(Crap! Did someone cut the line?!)\x02",
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
        0x10A,
        "#5200066V#0605F#5PBannings! What's the situation?!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7526", 0)

    ChrTalk(
        0x101,
        (
            "#5200067V#12P#0003FThe Bracer Guild seems to have been attacked\x01",
            "by someone or some group.\x02\x03",
            "#5200068V#0013FJust before our call cut out, I heard the sound\x01",
            "of machine gun fire.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#5200069V#0105F#11PNo...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200070V#0307FDon't tell me that the mafia's behind\x01",
            "this! The Bracer Guild? Seriously?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5200071V#1001F#5PConsidering the circumstances, I'm not sure\x01",
            "if I'd even be surprised.\x02",
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
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5200072V#12P#0013FNo, wait...\x02\x03",
            "#5200073VA mafia raid? There's something about that\x01",
            "possibility that rubs me the wrong way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5200074V#1005F#5PAnd that is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200075V#12P#0008F(That's right, what stuck out to me was...)\x02",
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
            "[The sound of the machine guns]\x01",                  # 0
            "[Michel's reaction]\x01",                              # 1
            "[The timing of the communication being cut]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17D76"),
        (1, "loc_17E33"),
        (2, "loc_17ED7"),
        (SWITCH_DEFAULT, "loc_17F8E"),
    )


    label("loc_17D76")

    OP_2C(0x4E, 0x1)

    ChrTalk(
        0x101,
        (
            "#5200076V#12P#0003F(Right. Those definitely didn't sound like the\x01",
            "heavy machine guns that Revache has been\x01",
            "using up until now.)\x02\x03",
            "#5200077V#0013F(But what does that tell us?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F8E")

    label("loc_17E33")


    ChrTalk(
        0x101,
        (
            "#5200078V#12P#0006F(No, that's not it. He was shocked, but that was\x01",
            "a natural reaction...)\x02\x03",
            "#5200081V#0008F(What exactly was off about this whole thing?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F8E")

    label("loc_17ED7")


    ChrTalk(
        0x101,
        (
            "#5200080V#12P#0006F(Well, no. It was inconvenient, but I don't think\x01",
            "that it meant anything in particular...)\x02\x03",
            "#5200079V#0008F(What exactly was off about this whole thing?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F8E")

    label("loc_17F8E")

    Sound(821, 2, 80, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        "#5200082V#11P#0005FIs that the phone in the lobby?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200083V#0101F#11PQuick, Lloyd! Answer it!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(14200, 1750, 5000, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 19500, 850, 4000, 270)
    SetChrPos(0x102, 19500, 850, 4000, 270)
    SetChrPos(0x103, 19500, 850, 4000, 270)
    SetChrPos(0x104, 19500, 850, 4000, 270)
    SetChrPos(0x10A, 19500, 850, 4000, 270)
    SetChrPos(0x11, 19500, 850, 4000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x1F, 0x4)
    SetMapObjFlags(0x1F, 0x1000)
    OP_70(0x1F, 0x0)
    OP_74(0x1F, 0x1E)
    OP_71(0x1F, 0x0, 0x14, 0x0, 0x20)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    OP_0D()
    OP_25(0x335, 0x64)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x0)
    SetChrSubChip(0xD, 0x2)
    Sleep(50)
    SetChrSubChip(0x14, 0x1)
    Sleep(250)

    ChrTalk(
        0xD,
        (
            "#5200084V#1105FOh, Lloyd.\x02\x03",
            "#5200085VThe phone is ringing!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(13800, 1750, 11000, 3000)
    BeginChrThread(0xD, 3, 0, 49)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5200086V#0013F#11PYeah, I'll get it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200087V#0102F#11PSorry for all this\x01",
            "fuss, Shizuku...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5200088V#6008F#12PN-No, it's fine...\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 3)
    ClearMapObjFlags(0x1F, 0x20)
    OP_70(0x1F, 0x32)
    OP_24(0x335)
    Sound(822, 0, 100, 0)
    FadeToDark(500, 0, 100)
    OP_0D()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#5200089V#0013FYes, Special Support Section here!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200090V\x07\x05",
            "Oh, Lloyd, is that you?!\x02\x03",
            "#5200091VTh-Thank goodness the\x01",
            "call went through!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5200092V\x07\x00",
            "#0000FWait... Sergeant Major Seeker?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Noel's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200093V\x07\x05",
            "Yes, it's me!\x02\x03",
            "#5200094VThere's something that I need to\x01",
            "let you and the others know about!\x02\x03",
            "#5200095VContact with the Bellguard Gate forces\x01",
            "has been completely severed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5200096V\x07\x00",
            "#0007FWh-What?!\x02\x03",
            "#5200097V#0010FHow could that even happen?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Noel's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200098V\x07\x05",
            "I-I don't know! We're trying\x01",
            "to look into it right now...\x02\x03",
            "#5200099VDeputy Commander Baelz instructed me\x01",
            "to report all this to you, just in case!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5200100V\x07\x00",
            "#0013FRoger, thanks for the heads-up!\x02\x03",
            "#5200101V#0005FOh, wait. There's something\x01",
            "we need to tell you, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd briefly informed Noel about\x01",
            "the Bracer Guild being assaulted.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Noel's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200102V\x07\x05",
            "The guild was what?!\x02\x03",
            "#5200103VI-I understand! I'll report everything\x01",
            "to the deputy commander, ASAP!\x02\x03",
            "#5200104VI'm not exactly sure what's going on,\x01",
            "but be extremely careful, okay?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5200105V\x07\x00",
            "#0013FWe will. Same goes to you, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(500, 0)
    OP_0D()
    SetMapObjFlags(0x1F, 0x4)
    Sound(822, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x11,
        "#5200106V#6P#1001FSomething happen to the Guardian Force?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5200107V#5P#0006FApparently, communication with Bellguard\x01",
            "Gate has been completely cut off...\x02\x03",
            "#5200108V#0013FThey're checking into it as we speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#5200109V#6P#0605FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200110V#0101F#12PThis is bad...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(2048, 255, 100, 0)
    Sleep(1000)
    EndChrThread(0xF, 0x1)
    SetChrChipByIndex(0xF, 0x2F)
    SetChrSubChip(0xF, 0x3)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_18982():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_18982)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_18A34():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18A34)

    def lambda_18A41():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_18A41)

    def lambda_18A4E():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_18A4E)

    def lambda_18A5B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_18A5B)

    def lambda_18A68():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_18A68)

    def lambda_18A75():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_18A75)
    SetChrSubChip(0x14, 0x1)
    SetChrSubChip(0xD, 0x2)
    OP_68(500, 1000, 2500, 2000)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#5200112V#0005FZeit?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200113V#0301FWhat's the matter, boy?\x01",
            "Somethin' outside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5200114V#5P#1201FGrrrrowl...woof!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(13800, 1750, 11000, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0xD, 11300, 900, 6400, 180)
    EndChrThread(0xF, 0x2)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#5200115V#5P#0205F'Surrounded! Everyone, watch out!'\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5200116V#1101F#11PHe's saying that something's\x01",
            "trying to get in here, I think.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x14, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_18CBB():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18CBB)

    def lambda_18CC8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_18CC8)
    Sleep(50)

    def lambda_18CD8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_18CD8)

    def lambda_18CE5():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_18CE5)
    Sleep(50)

    def lambda_18CF5():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_18CF5)
    SetChrSubChip(0x14, 0x0)
    WaitChrThread(0x10A, 2)
    SetChrSubChip(0x14, 0x2)
    Sleep(50)
    Fade(250)
    SetChrPos(0xD, 11300, 900, 6650, 90)
    SetChrSubChip(0xD, 0x1)
    OP_0D()

    ChrTalk(
        0x101,
        "#5200117V#0013F#5PSeriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200118V#0101F#11PNo way... Could it be the same group\x01",
            "that attacked the Bracer Guild?!\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x11,
        (
            "#5200119V#6P#1010FHmph...\x01",
            "Yeah, most likely.\x02\x03",
            "#5200120V#1001FEveryone, prepare to evacuate.\x02\x03",
            "#5200121VLloyd, Randy, take KeA and\x01",
            "Shizuku with you, understood?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18E62():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18E62)
    Sleep(50)

    def lambda_18E72():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_18E72)
    Sleep(50)
    TurnDirection(0x10A, 0x11, 500)

    ChrTalk(
        0x101,
        "#5200051V#5P#0007FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200123V#0307F#11PYes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5200124V#6P#1003FTio, keep an eye on our surroundings.\x01",
            "Elie, provide support.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200125V#11P#0201FYes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200126V#0101F#11PUnderstood!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x11, 0x2C)
    SetChrSubChip(0x11, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x11, 0x10A, 500)

    ChrTalk(
        0x11,
        (
            "#5200127V#12P#1001FDudley. We'll watch over\x01",
            "everyone's six.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#5200128V#5P#0601FRoger!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    OP_68(13800, 1750, 8900, 2500)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(300)
    BeginChrThread(0x104, 3, 0, 48)
    Sleep(200)

    def lambda_1902E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1902E)
    Sleep(50)

    def lambda_1903E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_1903E)
    Sleep(50)

    def lambda_1904E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1904E)
    Sleep(50)
    WaitChrThread(0x101, 3)

    def lambda_19062():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_19062)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#5200129V#0000F#5PKeA. Hold tight and don't\x01",
            "let go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5200130V#12P#1110F#NLeave it to me!\x01",
            "Hehehe...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0x30)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x104, 3)

    ChrTalk(
        0x104,
        (
            "#5200131V#5P#0304FShizuku, you'll have\x01",
            "to excuse me.\x02\x03",
            "#5200132V#0300FI'm sure you'd rather your old man do\x01",
            "this, but you'll have to settle for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5200133V#12P#6002FI don't mind...\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x104, 0x32)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    def lambda_191F5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_191F5)
    Sleep(50)

    def lambda_19205():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_19205)
    WaitChrThread(0x104, 2)
    Sleep(200)

    ChrTalk(
        0x11,
        (
            "#5200134V#1001F#5PAll right, everyone...\x01",
            "Try not to break formation, eh?\x02",
        )
    )

    CloseMessageWindow()
    Sound(921, 0, 80, 0)
    Sleep(200)
    SetCameraDistance(29000, 3000)
    OP_82(0x384, 0x384, 0xBB8, 0xBB8)
    Sound(356, 0, 100, 0)
    Sound(956, 0, 100, 0)
    Sound(834, 0, 100, 0)
    BeginChrThread(0x11, 3, 0, 46)
    BlurSwitch(0xBB8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    Sound(539, 0, 100, 0)
    BeginChrThread(0x11, 2, 0, 46)
    Sleep(500)
    Sound(356, 0, 100, 0)
    Sound(956, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(500)
    Sound(539, 0, 100, 0)
    Sleep(400)
    Sound(153, 0, 100, 0)
    Sound(356, 0, 100, 0)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_6F(0x10)
    CancelBlur(0)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    OP_7D(0xB3, 0xB3, 0xC7, 0x0, 0x0)
    SetMapObjFrame(0xFF, "floor02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "floor02_wood", 0x1, 0x1)
    SetMapObjFrame(0xFF, "floor02_sd", 0x1, 0x1)
    SetMapObjFrame(0xFF, "floor02_dankon", 0x1, 0x1)
    SetMapObjFrame(0xFF, "floor01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor01_wood", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tanmatu", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tanmatu2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "white", 0x0, 0x1)
    SetMapObjFrame(0xFF, "white_sd", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd00", 0x0, 0x1)
    OP_68(13800, 1750, 8900, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26000, 0)
    SetChrPos(0x15, 15200, 850, -1800, 0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x16, 10200, 850, -1800, 0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    OP_68(12700, 1750, 10000, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x102, 15000, 850, 10300, 180)
    SetChrPos(0x103, 13300, 850, 9800, 180)
    SetChrPos(0x10A, 10300, 850, 10300, 180)
    SetChrPos(0x11, 11900, 850, 9300, 180)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    OP_68(12700, 1750, 8000, 2000)
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 16777215)
    Sleep(1000)
    Sound(854, 0, 100, 0)
    Sound(921, 0, 100, 0)
    BeginChrThread(0x15, 3, 0, 44)
    Sleep(100)
    BeginChrThread(0x16, 3, 0, 45)
    OP_6F(0x11)

    ChrTalk(
        0x101,
        "#5200135V#0011F#5PWh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200136V#11P#0107FTh-The Guardian Force?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5200137V\x07\x02",
            "#12P#30W...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5200138V\x07\x02",
            "#6P#35W...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5200139V\x07\x00",
            "#5P#1007FGo now! Evacuate through\x01",
            "the back door!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(11300, 1750, 11000, 0)
    MoveCamera(50, 13, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    OP_68(6300, 1750, 11000, 3000)
    BeginChrThread(0x15, 3, 0, 38)
    BeginChrThread(0x104, 3, 0, 43)
    BeginChrThread(0x11, 3, 0, 39)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 42)
    BeginChrThread(0x10A, 3, 0, 40)
    Sleep(450)
    BeginChrThread(0x103, 3, 0, 41)
    Sleep(100)
    BeginChrThread(0x16, 3, 0, 38)
    BeginChrThread(0x102, 3, 0, 41)
    Sleep(1350)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x11, 3)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipPat(0x0, 0x1, 0x9B)
    SetChrChipPat(0x3, 0x1, 0x9C)
    LoadChrChipPat()
    OP_24(0x335)
    SetScenarioFlags(0x5C, 0)
    NewScene("c020B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_1608A end

    def Function_38_19777(): pass

    label("Function_38_19777")

    Sleep(700)
    Sound(356, 0, 100, 0)
    Sound(956, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 9700, 870, 8500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 8700, 870, 11800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 8100, 870, 8500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 5900, 470, 7400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 6100, 870, 11300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_38_19777 end

    def Function_39_198A6(): pass

    label("Function_39_198A6")

    SetChrChipByIndex(0x11, 0x35)
    SetChrSubChip(0x11, 0x4)
    Sleep(900)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    SetChrSubChip(0x11, 0x5)
    Sleep(200)
    SetChrSubChip(0x11, 0x6)
    Sleep(100)
    SetChrSubChip(0x11, 0x7)
    Sleep(100)
    SetChrSubChip(0x11, 0x4)
    Sleep(100)
    SetChrSubChip(0x11, 0x3)
    Sleep(70)
    SetChrSubChip(0x11, 0x2)
    Sleep(70)
    SetChrSubChip(0x11, 0x1)
    Sleep(70)
    Sound(531, 0, 100, 0)
    SetChrSubChip(0x11, 0x0)
    Sleep(70)
    SetChrSubChip(0x11, 0x1)
    Sleep(70)
    SetChrSubChip(0x11, 0x2)
    Sleep(70)
    SetChrSubChip(0x11, 0x3)
    Sleep(70)
    SetChrSubChip(0x11, 0x4)
    Sleep(500)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    SetChrSubChip(0x11, 0x5)
    Sleep(200)
    Sound(531, 0, 100, 0)
    SetChrSubChip(0x11, 0x6)
    Sleep(100)
    SetChrSubChip(0x11, 0x7)
    Sleep(100)
    SetChrSubChip(0x11, 0x4)
    Sleep(100)
    Return()

    # Function_39_198A6 end

    def Function_40_199A8(): pass

    label("Function_40_199A8")

    SetChrChipByIndex(0x10A, 0x34)
    SetChrSubChip(0x10A, 0x0)
    Sleep(1000)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Return()

    # Function_40_199A8 end

    def Function_41_19AD1(): pass

    label("Function_41_19AD1")


    def lambda_19AD6():
        OP_95(0xFE, 11000, 850, 11400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19AD6)
    WaitChrThread(0xFE, 1)

    def lambda_19AF4():
        OP_95(0xFE, 9300, 850, 10400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19AF4)
    WaitChrThread(0xFE, 1)

    def lambda_19B12():
        OP_95(0xFE, 1600, 850, 10400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19B12)
    WaitChrThread(0xFE, 1)

    def lambda_19B30():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19B30)
    Sleep(500)

    def lambda_19B4D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_19B4D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_41_19AD1 end

    def Function_42_19B62(): pass

    label("Function_42_19B62")


    def lambda_19B67():
        OP_95(0xFE, 9500, 850, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19B67)
    WaitChrThread(0xFE, 1)

    def lambda_19B85():
        OP_95(0xFE, 1600, 850, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19B85)
    WaitChrThread(0xFE, 1)

    def lambda_19BA3():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19BA3)
    Sleep(500)

    def lambda_19BC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_19BC0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_42_19B62 end

    def Function_43_19BD5(): pass

    label("Function_43_19BD5")


    def lambda_19BDA():
        OP_95(0xFE, 13500, 870, 8600, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19BDA)
    WaitChrThread(0x104, 1)

    def lambda_19BF8():
        OP_95(0xFE, 9500, 850, 8600, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19BF8)
    WaitChrThread(0x104, 1)

    def lambda_19C16():
        OP_95(0xFE, 1600, 850, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19C16)
    WaitChrThread(0x104, 1)

    def lambda_19C34():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19C34)
    Sleep(500)

    def lambda_19C51():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_19C51)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    Return()

    # Function_43_19BD5 end

    def Function_44_19C66(): pass

    label("Function_44_19C66")

    SetChrChip(0x0, 0x15, 0x1E, 0x12C)
    SetChrChipByIndex(0x15, 0x27)
    SetChrSubChip(0x15, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 15200, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_19CBD():
        OP_9D(0xFE, 0x3B60, 0x352, 0x898, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_19CBD)

    def lambda_19CDA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_19CDA)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x26)
    SetChrSubChip(0x15, 0x0)
    Sound(58, 0, 100, 0)
    Sound(31, 0, 100, 0)
    Sleep(300)
    SetChrChip(0x1, 0x15, 0x0, 0x0)
    Return()

    # Function_44_19C66 end

    def Function_45_19D0A(): pass

    label("Function_45_19D0A")

    SetChrChip(0x0, 0x16, 0x1E, 0x12C)
    SetChrChipByIndex(0x16, 0x29)
    SetChrSubChip(0x16, 0x2)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 10200, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_19D61():
        OP_9D(0xFE, 0x27D8, 0x352, 0x898, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_19D61)

    def lambda_19D7E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_19D7E)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x28)
    SetChrSubChip(0x16, 0x0)
    Sound(59, 0, 100, 0)
    Sound(30, 0, 100, 0)
    Sleep(300)
    SetChrChip(0x1, 0x16, 0x0, 0x0)
    Return()

    # Function_45_19D0A end

    def Function_46_19DAE(): pass

    label("Function_46_19DAE")

    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 10200, 870, 5700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12500, 1470, 4700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 10200, 870, 5700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 17600, 870, 8400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 15300, 870, 3800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 17600, 870, 8400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12900, 1470, 4800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 10300, 870, 3700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 10300, 870, 3700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 9900, 870, 11500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 17100, 1470, 10500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 16900, 1470, 11000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 16900, 1470, 11000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 9200, 1270, 6000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 8000, 870, 5300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14000, 870, 5800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 8000, 870, 5300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 15100, 870, 5600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12600, 1470, 3100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 15100, 870, 5600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 11700, 1470, 5100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 15600, 870, 6900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 15600, 870, 6900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 16100, 870, 8300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 9700, 870, 9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 9500, 870, 10500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 9500, 870, 10500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12900, 1470, 6600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 9900, 870, 4500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 16800, 870, 5900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 16800, 870, 5900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_46_19DAE end

    def Function_47_1A482(): pass

    label("Function_47_1A482")


    def lambda_1A487():
        OP_95(0xFE, 11300, 870, 7900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A487)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_47_1A482 end

    def Function_48_1A4A8(): pass

    label("Function_48_1A4A8")

    OP_92(0x104, 0x3778, 0x1EDC, 0x1F4)

    def lambda_1A4BA():
        OP_95(0xFE, 14200, 870, 7900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A4BA)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_48_1A4A8 end

    def Function_49_1A4DB(): pass

    label("Function_49_1A4DB")

    BeginChrThread(0x101, 3, 0, 50)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 51)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 52)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 53)
    Sleep(500)
    BeginChrThread(0x10A, 3, 0, 54)
    Sleep(500)
    BeginChrThread(0x11, 3, 0, 55)
    Sleep(1000)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x11, 3)
    Return()

    # Function_49_1A4DB end

    def Function_50_1A53F(): pass

    label("Function_50_1A53F")


    def lambda_1A544():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A544)

    def lambda_1A555():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A555)
    WaitChrThread(0x101, 1)

    def lambda_1A573():
        OP_95(0xFE, 13800, 850, 12000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A573)
    Sleep(300)
    SetChrSubChip(0xD, 0x0)
    Sleep(100)
    SetChrSubChip(0x14, 0x1)
    Sleep(300)
    SetChrSubChip(0xD, 0x1)
    Sleep(100)
    SetChrSubChip(0x14, 0x2)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_50_1A53F end

    def Function_51_1A5B0(): pass

    label("Function_51_1A5B0")


    def lambda_1A5B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A5B5)

    def lambda_1A5C6():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A5C6)
    WaitChrThread(0x102, 1)

    def lambda_1A5E4():
        OP_95(0xFE, 14500, 850, 10300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A5E4)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_51_1A5B0 end

    def Function_52_1A605(): pass

    label("Function_52_1A605")


    def lambda_1A60A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A60A)

    def lambda_1A61B():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A61B)
    WaitChrThread(0x103, 1)

    def lambda_1A639():
        OP_95(0xFE, 13300, 850, 9800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A639)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_52_1A605 end

    def Function_53_1A65A(): pass

    label("Function_53_1A65A")


    def lambda_1A65F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A65F)

    def lambda_1A670():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A670)
    WaitChrThread(0x104, 1)

    def lambda_1A68E():
        OP_95(0xFE, 15300, 850, 9800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A68E)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x13B, 0x1F4)
    Return()

    # Function_53_1A65A end

    def Function_54_1A6AF(): pass

    label("Function_54_1A6AF")


    def lambda_1A6B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A6B4)

    def lambda_1A6C5():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1A6C5)
    WaitChrThread(0x10A, 1)

    def lambda_1A6E3():
        OP_95(0xFE, 15500, 850, 7000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1A6E3)
    WaitChrThread(0x10A, 1)

    def lambda_1A701():
        OP_95(0xFE, 11000, 850, 10300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1A701)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0x2D, 0x1F4)
    Return()

    # Function_54_1A6AF end

    def Function_55_1A722(): pass

    label("Function_55_1A722")


    def lambda_1A727():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A727)

    def lambda_1A738():
        OP_95(0xFE, 16500, 850, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1A738)
    WaitChrThread(0x11, 1)

    def lambda_1A756():
        OP_95(0xFE, 15500, 850, 7000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1A756)
    WaitChrThread(0x11, 1)

    def lambda_1A774():
        OP_95(0xFE, 11400, 850, 9300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1A774)
    WaitChrThread(0x11, 1)
    OP_93(0x11, 0x2D, 0x1F4)
    Return()

    # Function_55_1A722 end

    def Function_56_1A795(): pass

    label("Function_56_1A795")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A843")

    ChrTalk(
        0x101,
        (
            "#0001FI suppose I could head outside.\x01",
            "A walk sounds nice right now.\x02\x03",
            "#0006FBut first, I should ask the others\x01",
            "how they're feeling about this\x01",
            "assignment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A8B0")

    ChrTalk(
        0x101,
        (
            "#0008FElie...did you head outside?\x02\x03",
            "#0001FI should check everywhere\x01",
            "inside the SSS first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A90C")

    ChrTalk(
        0x101,
        (
            "#0000FMr. Grimwood came to meet with\x01",
            "the chief? Might as well say hello.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A90C")

    Sleep(50)
    SetChrPos(0x0, 1000, 0, 970, 0)
    EventEnd(0x4)
    Return()

    # Function_56_1A795 end

    def Function_57_1A923(): pass

    label("Function_57_1A923")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A994")

    ChrTalk(
        0x101,
        (
            "#0005FIs this a back entrance?\x02\x03",
            "#0000FWell, it's not like I need to\x01",
            "go outside now, anyway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AA06")

    ChrTalk(
        0x101,
        (
            "#0008FCould Elie have gone outside?\x02\x03",
            "#0001FI think I'll check everywhere\x01",
            "inside the SSS first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA06")

    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_57_1A923 end

    def Function_58_1AA1D(): pass

    label("Function_58_1AA1D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AB41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAB8")

    ChrTalk(
        0x101,
        (
            "#0000FMan, I'm hopeless. All this and I'm still just\x01",
            "as confused as I was.\x02\x03",
            "Maybe a short walk would clear my mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_1AB41")

    label("loc_1AAB8")


    ChrTalk(
        0x101,
        (
            "#0000FThis way leads to the second floor. I don't\x01",
            "want to head back to my room just yet...\x02\x03",
            "Maybe a short walk would clear my mind?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AB9D")

    ChrTalk(
        0x101,
        (
            "#0000FMr. Grimwood came to meet with\x01",
            "the chief? Might as well say hello.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB9D")

    Sleep(50)
    SetChrPos(0x0, 1000, 850, 9460, 180)
    EventEnd(0x4)
    Return()

    # Function_58_1AA1D end

    def Function_59_1ABB4(): pass

    label("Function_59_1ABB4")

    EventBegin(0x0)
    Fade(1000)
    OP_68(170700, 1100, 62900, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 170000, 0, 62100, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC57")

    ChrTalk(
        0x101,
        (
            "#12P#0005FI think this is Tio's room...\x02\x03",
            "#0003FShe may already be asleep.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)

    label("loc_1AC57")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Knock]\x01",            # 0
            "[Don't knock]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1ACA7"),
        (1, "loc_1AD66"),
        (SWITCH_DEFAULT, "loc_1AD6D"),
    )


    label("loc_1ACA7")

    OP_95(0x101, 170000, 0, 62900, 2000, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#0005F#12PNo one home? Hmm, I can't hear her\x01",
            "moving around.\x02\x03",
            "#0001FMaybe she's not even here...\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x13, 0x1)
    SetMapObjFlags(0x6, 0x10)
    SetChrPos(0x0, 170000, 0, 62900, 0)
    SetScenarioFlags(0x4A, 6)
    EventEnd(0x5)
    Jump("loc_1AD6D")

    label("loc_1AD66")

    EventEnd(0x5)
    Jump("loc_1AD6D")

    label("loc_1AD6D")

    Return()

    # Function_59_1ABB4 end

    def Function_60_1AD6E(): pass

    label("Function_60_1AD6E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 206030, 0, 119060, 360)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(205930, 1330, 125780, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(206030, 1330, 121140, 3000)
    Sleep(1000)

    def lambda_1ADE7():
        OP_96(0xFE, 0x324CE, 0x1E, 0x1D934, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1ADE7)

    def lambda_1AE01():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AE01)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#0001F#12P(Yeah, looks like I was right.)\x02\x03",
            "(Though, she's already unpacked\x01",
            "all of her luggage...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x47, 1)
    ModifyEventFlags(0, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_60_1AD6E end

    def Function_61_1AE85(): pass

    label("Function_61_1AE85")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1AECD")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a vacant room that is kept locked.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF36")

    label("loc_1AECD")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#0001F(This must be a spare room...\x01",
            "Well, no reason to mess with it now.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF36")

    TalkEnd(0xFF)
    Return()

    # Function_61_1AE85 end

    def Function_62_1AF3A(): pass

    label("Function_62_1AF3A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    OP_68(-1560, 1330, 122920, 0)
    MoveCamera(38, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AF92")
    SetChrFlags(0x0, 0x8)

    label("loc_1AF92")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AFA5")
    SetChrFlags(0x1, 0x8)

    label("loc_1AFA5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AFB8")
    SetChrFlags(0x2, 0x8)

    label("loc_1AFB8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AFCB")
    SetChrFlags(0x3, 0x8)

    label("loc_1AFCB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AFDE")
    SetChrFlags(0x4, 0x8)

    label("loc_1AFDE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AFF1")
    SetChrFlags(0x5, 0x8)

    label("loc_1AFF1")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1830, 30, 122400, 270)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0000FThis looks good, right?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Lloyd's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x350, 1)
    SetScenarioFlags(0x50, 6)
    OP_66(0x7, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B098")
    ClearChrFlags(0x0, 0x8)

    label("loc_1B098")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B0AB")
    ClearChrFlags(0x1, 0x8)

    label("loc_1B0AB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B0BE")
    ClearChrFlags(0x2, 0x8)

    label("loc_1B0BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B0D1")
    ClearChrFlags(0x3, 0x8)

    label("loc_1B0D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B0E4")
    ClearChrFlags(0x4, 0x8)

    label("loc_1B0E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B0F7")
    ClearChrFlags(0x5, 0x8)

    label("loc_1B0F7")

    Call(0, 79)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_62_1AF3A end

    def Function_63_1B10E(): pass

    label("Function_63_1B10E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)
    OP_68(-2440, 1300, 129810, 0)
    MoveCamera(36, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(20500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B166")
    SetChrFlags(0x0, 0x8)

    label("loc_1B166")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B179")
    SetChrFlags(0x1, 0x8)

    label("loc_1B179")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B18C")
    SetChrFlags(0x2, 0x8)

    label("loc_1B18C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B19F")
    SetChrFlags(0x3, 0x8)

    label("loc_1B19F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B1B2")
    SetChrFlags(0x4, 0x8)

    label("loc_1B1B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B1C5")
    SetChrFlags(0x5, 0x8)

    label("loc_1B1C5")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1940, 0, 128820, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0000FThat looks good, right?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Lloyd's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x351, 1)
    SetScenarioFlags(0x50, 7)
    OP_66(0x8, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B26C")
    ClearChrFlags(0x0, 0x8)

    label("loc_1B26C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B27F")
    ClearChrFlags(0x1, 0x8)

    label("loc_1B27F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B292")
    ClearChrFlags(0x2, 0x8)

    label("loc_1B292")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B2A5")
    ClearChrFlags(0x3, 0x8)

    label("loc_1B2A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B2B8")
    ClearChrFlags(0x4, 0x8)

    label("loc_1B2B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B2CB")
    ClearChrFlags(0x5, 0x8)

    label("loc_1B2CB")

    Call(0, 79)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_63_1B10E end

    def Function_64_1B2E2(): pass

    label("Function_64_1B2E2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "05", 0x1, 0x1)
    OP_68(153830, 1330, 130810, 0)
    MoveCamera(29, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B33A")
    SetChrFlags(0x0, 0x8)

    label("loc_1B33A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B34D")
    SetChrFlags(0x1, 0x8)

    label("loc_1B34D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B360")
    SetChrFlags(0x2, 0x8)

    label("loc_1B360")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B373")
    SetChrFlags(0x3, 0x8)

    label("loc_1B373")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B386")
    SetChrFlags(0x4, 0x8)

    label("loc_1B386")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B399")
    SetChrFlags(0x5, 0x8)

    label("loc_1B399")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 155090, 30, 129770, 344)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0100FHmm, does this look all right?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Elie's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x352, 1)
    SetScenarioFlags(0x51, 0)
    OP_66(0x9, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B446")
    ClearChrFlags(0x0, 0x8)

    label("loc_1B446")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B459")
    ClearChrFlags(0x1, 0x8)

    label("loc_1B459")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B46C")
    ClearChrFlags(0x2, 0x8)

    label("loc_1B46C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B47F")
    ClearChrFlags(0x3, 0x8)

    label("loc_1B47F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B492")
    ClearChrFlags(0x4, 0x8)

    label("loc_1B492")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B4A5")
    ClearChrFlags(0x5, 0x8)

    label("loc_1B4A5")

    Call(0, 79)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_64_1B2E2 end

    def Function_65_1B4BC(): pass

    label("Function_65_1B4BC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x1, 0x1)
    OP_68(154150, 1330, 121920, 0)
    MoveCamera(53, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B51F")
    SetChrFlags(0x0, 0x8)

    label("loc_1B51F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B532")
    SetChrFlags(0x1, 0x8)

    label("loc_1B532")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B545")
    SetChrFlags(0x2, 0x8)

    label("loc_1B545")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B558")
    SetChrFlags(0x3, 0x8)

    label("loc_1B558")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B56B")
    SetChrFlags(0x4, 0x8)

    label("loc_1B56B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B57E")
    SetChrFlags(0x5, 0x8)

    label("loc_1B57E")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 154150, 30, 121920, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0100FHmm, does this look all right?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Elie's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x353, 1)
    SetScenarioFlags(0x51, 1)
    OP_66(0xA, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B62B")
    ClearChrFlags(0x0, 0x8)

    label("loc_1B62B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B63E")
    ClearChrFlags(0x1, 0x8)

    label("loc_1B63E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B651")
    ClearChrFlags(0x2, 0x8)

    label("loc_1B651")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B664")
    ClearChrFlags(0x3, 0x8)

    label("loc_1B664")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B677")
    ClearChrFlags(0x4, 0x8)

    label("loc_1B677")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B68A")
    ClearChrFlags(0x5, 0x8)

    label("loc_1B68A")

    Call(0, 79)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_65_1B4BC end

    def Function_66_1B6A1(): pass

    label("Function_66_1B6A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "07", 0x1, 0x1)
    OP_68(208030, 1330, 127590, 0)
    MoveCamera(25, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B6F9")
    SetChrFlags(0x0, 0x8)

    label("loc_1B6F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B70C")
    SetChrFlags(0x1, 0x8)

    label("loc_1B70C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B71F")
    SetChrFlags(0x2, 0x8)

    label("loc_1B71F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B732")
    SetChrFlags(0x3, 0x8)

    label("loc_1B732")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B745")
    SetChrFlags(0x4, 0x8)

    label("loc_1B745")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B758")
    SetChrFlags(0x5, 0x8)

    label("loc_1B758")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 208030, 30, 127590, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0200FThis should be fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Tio's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x354, 1)
    SetScenarioFlags(0x51, 2)
    OP_66(0xB, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B7FA")
    ClearChrFlags(0x0, 0x8)

    label("loc_1B7FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B80D")
    ClearChrFlags(0x1, 0x8)

    label("loc_1B80D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B820")
    ClearChrFlags(0x2, 0x8)

    label("loc_1B820")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B833")
    ClearChrFlags(0x3, 0x8)

    label("loc_1B833")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B846")
    ClearChrFlags(0x4, 0x8)

    label("loc_1B846")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B859")
    ClearChrFlags(0x5, 0x8)

    label("loc_1B859")

    Call(0, 79)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_66_1B6A1 end

    def Function_67_1B870(): pass

    label("Function_67_1B870")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "08", 0x1, 0x1)
    OP_68(207830, 1330, 127120, 0)
    MoveCamera(56, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B8C8")
    SetChrFlags(0x0, 0x8)

    label("loc_1B8C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B8DB")
    SetChrFlags(0x1, 0x8)

    label("loc_1B8DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B8EE")
    SetChrFlags(0x2, 0x8)

    label("loc_1B8EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B901")
    SetChrFlags(0x3, 0x8)

    label("loc_1B901")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B914")
    SetChrFlags(0x4, 0x8)

    label("loc_1B914")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B927")
    SetChrFlags(0x5, 0x8)

    label("loc_1B927")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 207830, 30, 127120, 107)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0200FThis should be fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Tio's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x355, 1)
    SetScenarioFlags(0x51, 3)
    OP_66(0xC, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B9C9")
    ClearChrFlags(0x0, 0x8)

    label("loc_1B9C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B9DC")
    ClearChrFlags(0x1, 0x8)

    label("loc_1B9DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B9EF")
    ClearChrFlags(0x2, 0x8)

    label("loc_1B9EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA02")
    ClearChrFlags(0x3, 0x8)

    label("loc_1BA02")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA15")
    ClearChrFlags(0x4, 0x8)

    label("loc_1BA15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA28")
    ClearChrFlags(0x5, 0x8)

    label("loc_1BA28")

    Call(0, 79)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_67_1B870 end

    def Function_68_1BA3F(): pass

    label("Function_68_1BA3F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "03", 0x1, 0x1)
    OP_68(51760, 1300, 129800, 0)
    MoveCamera(29, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA97")
    SetChrFlags(0x0, 0x8)

    label("loc_1BA97")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BAAA")
    SetChrFlags(0x1, 0x8)

    label("loc_1BAAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BABD")
    SetChrFlags(0x2, 0x8)

    label("loc_1BABD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BAD0")
    SetChrFlags(0x3, 0x8)

    label("loc_1BAD0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BAE3")
    SetChrFlags(0x4, 0x8)

    label("loc_1BAE3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BAF6")
    SetChrFlags(0x5, 0x8)

    label("loc_1BAF6")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 51760, 0, 129800, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#0300FNot too shabby.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Randy's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x356, 1)
    SetScenarioFlags(0x51, 4)
    OP_66(0xD, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB95")
    ClearChrFlags(0x0, 0x8)

    label("loc_1BB95")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BBA8")
    ClearChrFlags(0x1, 0x8)

    label("loc_1BBA8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BBBB")
    ClearChrFlags(0x2, 0x8)

    label("loc_1BBBB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BBCE")
    ClearChrFlags(0x3, 0x8)

    label("loc_1BBCE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BBE1")
    ClearChrFlags(0x4, 0x8)

    label("loc_1BBE1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BBF4")
    ClearChrFlags(0x5, 0x8)

    label("loc_1BBF4")

    Call(0, 79)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_68_1BA3F end

    def Function_69_1BC0B(): pass

    label("Function_69_1BC0B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x1, 0x1)
    OP_68(52520, 1300, 124040, 0)
    MoveCamera(70, 13, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC6E")
    SetChrFlags(0x0, 0x8)

    label("loc_1BC6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC81")
    SetChrFlags(0x1, 0x8)

    label("loc_1BC81")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC94")
    SetChrFlags(0x2, 0x8)

    label("loc_1BC94")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BCA7")
    SetChrFlags(0x3, 0x8)

    label("loc_1BCA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BCBA")
    SetChrFlags(0x4, 0x8)

    label("loc_1BCBA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BCCD")
    SetChrFlags(0x5, 0x8)

    label("loc_1BCCD")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 52520, 0, 124040, 25)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#0300FNot too shabby.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new decoration was added to Randy's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x357, 1)
    SetScenarioFlags(0x51, 5)
    OP_66(0xE, 0x1)
    Call(0, 70)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD6C")
    ClearChrFlags(0x0, 0x8)

    label("loc_1BD6C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD7F")
    ClearChrFlags(0x1, 0x8)

    label("loc_1BD7F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD92")
    ClearChrFlags(0x2, 0x8)

    label("loc_1BD92")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BDA5")
    ClearChrFlags(0x3, 0x8)

    label("loc_1BDA5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BDB8")
    ClearChrFlags(0x4, 0x8)

    label("loc_1BDB8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BDCB")
    ClearChrFlags(0x5, 0x8)

    label("loc_1BDCB")

    Call(0, 79)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_69_1BC0B end

    def Function_70_1BDE2(): pass

    label("Function_70_1BDE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE5D")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When Lloyd finds decorations, he can give them\x01",
            "to each of the members to display in their rooms.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x51, 6)

    label("loc_1BE5D")

    Return()

    # Function_70_1BDE2 end

    def Function_71_1BE5E(): pass

    label("Function_71_1BE5E")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis164.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a model orbal car.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_71_1BE5E end

    def Function_72_1BF06(): pass

    label("Function_72_1BF06")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis165.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an orbal stereo.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(10)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1BFCC"),
        (1, "loc_1BFD5"),
        (2, "loc_1BFDE"),
        (3, "loc_1BFE7"),
        (4, "loc_1BFF0"),
        (5, "loc_1BFF9"),
        (6, "loc_1C002"),
        (7, "loc_1C00B"),
        (SWITCH_DEFAULT, "loc_1C014"),
    )


    label("loc_1BFCC")

    PlayBGM("ed7400", 0)
    Jump("loc_1C014")

    label("loc_1BFD5")

    PlayBGM("ed7401", 0)
    Jump("loc_1C014")

    label("loc_1BFDE")

    PlayBGM("ed7402", 0)
    Jump("loc_1C014")

    label("loc_1BFE7")

    PlayBGM("ed7204", 0)
    Jump("loc_1C014")

    label("loc_1BFF0")

    PlayBGM("ed7205", 0)
    Jump("loc_1C014")

    label("loc_1BFF9")

    PlayBGM("ed7201", 0)
    Jump("loc_1C014")

    label("loc_1C002")

    PlayBGM("ed7200", 0)
    Jump("loc_1C014")

    label("loc_1C00B")

    PlayBGM("ed7202", 0)
    Jump("loc_1C014")

    label("loc_1C014")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_72_1BF06 end

    def Function_73_1C043(): pass

    label("Function_73_1C043")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis167.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a wall clock.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_73_1C043 end

    def Function_74_1C0E6(): pass

    label("Function_74_1C0E6")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis166.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an elegant vase.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_74_1C0E6 end

    def Function_75_1C18C(): pass

    label("Function_75_1C18C")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis168.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a hanging Mishy.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_75_1C18C end

    def Function_76_1C232(): pass

    label("Function_76_1C232")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis057.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a sitting Mishy.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_76_1C232 end

    def Function_77_1C2D8(): pass

    label("Function_77_1C2D8")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis171.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a poster of Ilya Platiere.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_77_1C2D8 end

    def Function_78_1C388(): pass

    label("Function_78_1C388")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis170.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a dartboard.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_78_1C388 end

    def Function_79_1C42A(): pass

    label("Function_79_1C42A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C462")
    OP_DE(0x16, 0x0)

    label("loc_1C462")

    Return()

    # Function_79_1C42A end

    def Function_80_1C463(): pass

    label("Function_80_1C463")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C4DA")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1C4DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C4F6")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1C4F6")

    Return()

    # Function_80_1C463 end

    def Function_81_1C4F7(): pass

    label("Function_81_1C4F7")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C56E")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1C56E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C58A")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1C58A")

    Return()

    # Function_81_1C4F7 end

    def Function_82_1C58B(): pass

    label("Function_82_1C58B")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C602")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1C602")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C61E")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1C61E")

    Return()

    # Function_82_1C58B end

    def Function_83_1C61F(): pass

    label("Function_83_1C61F")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C696")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1C696")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C6B2")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1C6B2")

    Return()

    # Function_83_1C61F end

    SaveToFile()

Try(main)
