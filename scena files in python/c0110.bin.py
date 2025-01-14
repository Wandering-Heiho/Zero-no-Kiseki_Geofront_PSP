from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0110.bin",                # FileName
        "c0110",                    # MapName
        "c0110",                    # Location
        0x0009,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("c0110", "c0110_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1000, 0, 2000, 0, 0, 1, 9, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0110",                  # 0
        "Chief Sergei",           # 1
        "Chief Sergei",           # 2
        "KeA",                    # 3
        "KeA",                    # 4
        "Zeit",                   # 5
        "Zeit",                   # 6
        "Zeit",                   # 7
        "Shizuku",                # 8
        "Elie",                   # 9
        "Tio",                    # 10
        "Randy",                  # 11
        "Deputy Commander Baelz", # 12
        "Sergeant Major Seeker",  # 13
        "Rixia",                  # 14
        "Detective Dudley",       # 15
        "White Boat",             # 16
        "魔獣調査レポート",       # 17
        "Tableware",              # 18
        "Tableware",              # 19
        "Tableware",              # 20
        "Tableware",              # 21
        "Tableware",              # 22
        "Tableware",              # 23
        "Tableware",              # 24
        "Tableware",              # 25
        "Tableware",              # 26
        "Tableware",              # 27
        "Tableware",              # 28
        "Tableware",              # 29
        "Tableware",              # 30
        "Tableware",              # 31
        "Tableware",              # 32
        "本",                     # 33
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch08200.itc",                   # 01
        "chr/ch02700.itc",                   # 02
        "chr/ch08700.itc",                   # 03
        "chr/ch02502.itc",                   # 04
        "chr/ch02707.itc",                   # 05
        "chr/ch02708.itc",                   # 06
        "chr/ch08202.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch02702.itc",                   # 09
        "chr/ch00100.itc",                   # 0A
        "chr/ch00202.itc",                   # 0B
        "chr/ch00302.itc",                   # 0C
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

    DeclNpc(14699,   850,     11199,   180,  389,  0x0, 0,   0,   0,   0,   0,   1,   2,   255,  0)
    DeclNpc(64000,   200,     11399,   180,  469,  0x0, 0,   4,   0,   255, 255, 1,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   1,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   7,   0,   255, 255, 1,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   2,   0,   255, 255, 1,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    404,  0x0, 0,   5,   0,   0,   0,   1,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   6,   0,   0,   0,   1,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   3,   0,   0,   0,   1,   9,   255,  0)
    DeclNpc(155759,  29,      129339,  0,    389,  0x0, 0,   10,  0,   0,   0,   1,   10,  255,  0)
    DeclNpc(203660,  150,     128610,  0,    469,  0x0, 0,   11,  0,   255, 255, 1,   11,  255,  0)
    DeclNpc(51840,   150,     126410,  270,  469,  0x0, 0,   12,  0,   255, 255, 1,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 17,  10.0,                  10.5,                  0.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -5.0,                  -2.0999999046325684,   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 51,  7.0,                   10.5,                  0.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -3.5,                  -2.0999999046325684,   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 52,  11.0,                  13.5,                  0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.5,                  -6.75,                 -0.0,                  1.0])
    DeclEvent(0x0000, 0, 53,  19.0,                  4.0,                   0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -9.5,                  -2.0,                  -0.0,                  1.0])

    DeclActor(16960,   850,     10840,   2000,    16960,   1300,    10840,   0x007C, 0,  3,  0x0000)
    DeclActor(18240,   850,     7560,    1000,    18240,   1850,    7560,    0x007C, 1,  0,  0x0000)
    DeclActor(12500,   850,     5600,    2500,    12500,   1500,    5600,    0x007C, 0,  4,  0x0000)
    DeclActor(64000,   30,      9800,    1500,    64000,   1500,    11400,   0x007E, 1,  1,  0x0000)
    DeclActor(180910,  0,       62020,   1500,    180910,  1500,    62020,   0x007C, 0,  56, 0x0000)
    DeclActor(19980,   0,       63920,   1500,    19980,   1500,    63920,   0x007C, 0,  56, 0x0000)
    DeclActor(175940,  0,       63930,   1500,    175940,  1500,    63930,   0x007C, 0,  56, 0x0000)
    DeclActor(-3150,   0,       122280,  1200,    -3150,   1000,    122280,  0x007C, 1,  31, 0x0000)
    DeclActor(-2300,   0,       129960,  1200,    -2300,   2000,    129960,  0x007C, 1,  32, 0x0000)
    DeclActor(155150,  30,      129699,  1200,    153340,  2029,    130490,  0x007C, 1,  33, 0x0000)
    DeclActor(155120,  30,      123880,  1200,    155120,  2029,    123880,  0x007C, 1,  34, 0x0000)
    DeclActor(208570,  0,       128030,  1200,    208840,  3000,    130410,  0x007C, 1,  35, 0x0000)
    DeclActor(208680,  0,       126170,  1200,    209210,  2000,    127040,  0x007C, 1,  36, 0x0000)
    DeclActor(51920,   0,       130570,  1200,    51920,   2500,    130570,  0x007C, 1,  37, 0x0000)
    DeclActor(52900,   0,       124470,  1200,    53700,   2000,    125270,  0x007C, 1,  38, 0x0000)
    DeclActor(2750,    0,       125420,  1200,    2750,    1500,    125420,  0x007C, 0,  57, 0x0000)
    DeclActor(153580,  30,      127880,  1200,    153370,  1530,    128389,  0x007C, 0,  58, 0x0000)
    DeclActor(207040,  30,      128539,  1200,    207640,  1500,    129090,  0x007C, 0,  59, 0x0000)
    DeclActor(48000,   30,      127860,  1200,    47560,   1500,    128630,  0x007C, 0,  60, 0x0000)
    DeclActor(257190,  0,       67990,   1200,    257350,  1500,    68870,   0x007E, 1,  9,  0x0000)

    ScpFunction((
        "Function_0_9EC",          # 00, 0
        "Function_1_AA4",          # 01, 1
        "Function_2_1311",         # 02, 2
        "Function_3_1824",         # 03, 3
        "Function_4_222F",         # 04, 4
        "Function_5_2402",         # 05, 5
        "Function_6_3321",         # 06, 6
        "Function_7_4600",         # 07, 7
        "Function_8_4640",         # 08, 8
        "Function_9_467D",         # 09, 9
        "Function_10_5718",        # 0A, 10
        "Function_11_57F2",        # 0B, 11
        "Function_12_6A8D",        # 0C, 12
        "Function_13_6AE5",        # 0D, 13
        "Function_14_6B3D",        # 0E, 14
        "Function_15_6B95",        # 0F, 15
        "Function_16_6BED",        # 10, 16
        "Function_17_6CA0",        # 11, 17
        "Function_18_71B3",        # 12, 18
        "Function_19_96C3",        # 13, 19
        "Function_20_9DE8",        # 14, 20
        "Function_21_B131",        # 15, 21
        "Function_22_F4E2",        # 16, 22
        "Function_23_F580",        # 17, 23
        "Function_24_F5D5",        # 18, 24
        "Function_25_F62A",        # 19, 25
        "Function_26_F67F",        # 1A, 26
        "Function_27_F6D4",        # 1B, 27
        "Function_28_10B67",       # 1C, 28
        "Function_29_10BDB",       # 1D, 29
        "Function_30_12BD1",       # 1E, 30
        "Function_31_133D7",       # 1F, 31
        "Function_32_13BAB",       # 20, 32
        "Function_33_15788",       # 21, 33
        "Function_34_164BC",       # 22, 34
        "Function_35_19A8E",       # 23, 35
        "Function_36_19AB7",       # 24, 36
        "Function_37_19AFB",       # 25, 37
        "Function_38_1A9A7",       # 26, 38
        "Function_39_1E623",       # 27, 39
        "Function_40_1E6CE",       # 28, 40
        "Function_41_1E6ED",       # 29, 41
        "Function_42_1ECE9",       # 2A, 42
        "Function_43_1F36B",       # 2B, 43
        "Function_44_1F9E6",       # 2C, 44
        "Function_45_25369",       # 2D, 45
        "Function_46_253FC",       # 2E, 46
        "Function_47_26BE0",       # 2F, 47
        "Function_48_2B4F3",       # 30, 48
        "Function_49_2BD27",       # 31, 49
        "Function_50_2D7DD",       # 32, 50
        "Function_51_2E2FA",       # 33, 51
        "Function_52_2E4A7",       # 34, 52
        "Function_53_2E588",       # 35, 53
        "Function_54_2E669",       # 36, 54
        "Function_55_2E727",       # 37, 55
        "Function_56_2EDAF",       # 38, 56
        "Function_57_2EFD9",       # 39, 57
        "Function_58_2F06D",       # 3A, 58
        "Function_59_2F101",       # 3B, 59
        "Function_60_2F195",       # 3C, 60
    ))


    def Function_0_9EC(): pass

    label("Function_0_9EC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_A2C"),
        (1, "loc_A38"),
        (2, "loc_A44"),
        (3, "loc_A50"),
        (4, "loc_A5C"),
        (5, "loc_A68"),
        (6, "loc_A74"),
        (SWITCH_DEFAULT, "loc_A80"),
    )


    label("loc_A2C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A38")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A44")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A50")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A5C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A68")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A74")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A80")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_A8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A8C")

    label("loc_AA3")

    Return()

    # Function_0_9EC end

    def Function_1_AA4(): pass

    label("Function_1_AA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6F")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B6F")
    SetChrPos(0x0, -2190, 0, 68010, 90)
    SetChrPos(0x1, -2190, 0, 68010, 90)
    SetChrPos(0x2, -2190, 0, 68010, 90)
    SetChrPos(0x3, -2190, 0, 68010, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B42")
    SetChrPos(0x4, -2190, 0, 68010, 90)
    SetChrPos(0x5, -2190, 0, 68010, 90)
    Jump("loc_B61")

    label("loc_B42")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B61")
    SetChrPos(0x4, -2190, 0, 68010, 90)

    label("loc_B61")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B6F")

    label("loc_B6F")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_D09")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x350, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB2")
    Event(1, 22)

    label("loc_BB2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x351, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE3")
    Event(1, 23)

    label("loc_BE3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x352, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C14")
    Event(1, 24)

    label("loc_C14")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x353, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C45")
    Event(1, 25)

    label("loc_C45")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x354, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C76")
    Event(1, 26)

    label("loc_C76")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x355, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA7")
    Event(1, 27)

    label("loc_CA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x356, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD8")
    Event(1, 28)

    label("loc_CD8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x357, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D09")
    Event(1, 29)

    label("loc_D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D5E")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 256490, 30, 69370, 180)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 257350, 0, 68870, 225)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 255850, 0, 67920, 225)
    Jump("loc_114B")

    label("loc_D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_D9D")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 5570, 150, 6230, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 3470, 30, 6380, 180)
    Jump("loc_114B")

    label("loc_D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DDC")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 257620, 350, 68650, 270)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 256820, 30, 69850, 180)
    Jump("loc_114B")

    label("loc_DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_E1B")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 5570, 150, 6230, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2880, 0, 1750, 225)
    Jump("loc_114B")

    label("loc_E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_E5F")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, 117660, 30, 8100, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2970, 0, 4170, 225)
    Jump("loc_114B")

    label("loc_E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_EAF")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 124620, 30, 5490, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 117660, 30, 8100, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2970, 0, 4170, 225)
    Jump("loc_114B")

    label("loc_EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_EBD")
    Jump("loc_114B")

    label("loc_EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_ECB")
    Jump("loc_114B")

    label("loc_ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_F37")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 14350, 850, 12060, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_F07")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_F32")

    label("loc_F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_F1F")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_F32")

    label("loc_F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_F32")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_F32")

    Jump("loc_114B")

    label("loc_F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_FDF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F67")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 30, 5850, 225)
    Jump("loc_FDA")

    label("loc_F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_F8B")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 30, 5850, 225)
    Jump("loc_FDA")

    label("loc_F8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_F9D")
    Jump("loc_FDA")

    label("loc_F9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_FC4")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 30, 5850, 225)
    Jump("loc_FDA")

    label("loc_FC4")

    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 30, 5850, 225)

    label("loc_FDA")

    Jump("loc_114B")

    label("loc_FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1071")
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1014")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 30, 5850, 225)
    Jump("loc_106C")

    label("loc_1014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_1038")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 30, 5850, 225)
    Jump("loc_106C")

    label("loc_1038")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_104A")
    Jump("loc_106C")

    label("loc_104A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_106C")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 30, 5850, 225)

    label("loc_106C")

    Jump("loc_114B")

    label("loc_1071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_107F")
    Jump("loc_114B")

    label("loc_107F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_108D")
    Jump("loc_114B")

    label("loc_108D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_10B1")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 97720, 0, 72570, 0)
    Jump("loc_114B")

    label("loc_10B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_10C4")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_114B")

    label("loc_10C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_10D2")
    Jump("loc_114B")

    label("loc_10D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_10E5")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_114B")

    label("loc_10E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_10F3")
    Jump("loc_114B")

    label("loc_10F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1106")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_114B")

    label("loc_1106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_END)), "loc_1119")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_114B")

    label("loc_1119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_112C")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_114B")

    label("loc_112C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_END)), "loc_114B")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 14700, 870, 11200, 180)

    label("loc_114B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1165")
    Event(0, 11)

    label("loc_1165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_119F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118E")
    SetMapFlags(0x10000000)
    Event(0, 30)
    Jump("loc_119F")

    label("loc_118E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119F")
    Event(0, 31)

    label("loc_119F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_11B3")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 5)
    Jump("loc_12F1")

    label("loc_11B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_11C7")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 6)
    Jump("loc_12F1")

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_11DB")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 19)
    Jump("loc_12F1")

    label("loc_11DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_11F2")
    ClearScenarioFlags(0x5C, 3)
    SetScenarioFlags(0x1, 6)
    Event(0, 20)
    Jump("loc_12F1")

    label("loc_11F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_1206")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 21)
    Jump("loc_12F1")

    label("loc_1206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_121A")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 27)
    Jump("loc_12F1")

    label("loc_121A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 6)), scpexpr(EXPR_END)), "loc_122E")
    ClearScenarioFlags(0x5C, 6)
    Event(0, 29)
    Jump("loc_12F1")

    label("loc_122E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 7)), scpexpr(EXPR_END)), "loc_123F")
    ClearScenarioFlags(0x5C, 7)
    Jump("loc_12F1")

    label("loc_123F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 0)), scpexpr(EXPR_END)), "loc_1253")
    ClearScenarioFlags(0x5D, 0)
    Event(0, 33)
    Jump("loc_12F1")

    label("loc_1253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 1)), scpexpr(EXPR_END)), "loc_1267")
    ClearScenarioFlags(0x5D, 1)
    Event(0, 34)
    Jump("loc_12F1")

    label("loc_1267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 2)), scpexpr(EXPR_END)), "loc_127E")
    ClearScenarioFlags(0x5D, 2)
    SetScenarioFlags(0x1, 6)
    Event(0, 37)
    Jump("loc_12F1")

    label("loc_127E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 3)), scpexpr(EXPR_END)), "loc_1292")
    ClearScenarioFlags(0x5D, 3)
    Event(0, 38)
    Jump("loc_12F1")

    label("loc_1292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 4)), scpexpr(EXPR_END)), "loc_12A6")
    ClearScenarioFlags(0x5D, 4)
    Event(0, 44)
    Jump("loc_12F1")

    label("loc_12A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 5)), scpexpr(EXPR_END)), "loc_12BA")
    ClearScenarioFlags(0x5D, 5)
    Event(0, 46)
    Jump("loc_12F1")

    label("loc_12BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 6)), scpexpr(EXPR_END)), "loc_12CE")
    ClearScenarioFlags(0x5D, 6)
    Event(0, 49)
    Jump("loc_12F1")

    label("loc_12CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 7)), scpexpr(EXPR_END)), "loc_12E2")
    ClearScenarioFlags(0x5D, 7)
    Event(0, 50)
    Jump("loc_12F1")

    label("loc_12E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 1)), scpexpr(EXPR_END)), "loc_12F1")
    ClearScenarioFlags(0x5E, 1)
    Event(1, 18)

    label("loc_12F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1310")
    Event(1, 14)

    label("loc_1310")

    Return()

    # Function_1_AA4 end

    def Function_2_1311(): pass

    label("Function_2_1311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_132D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_137A")

    label("loc_132D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_1347")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 6)
    Jump("loc_137A")

    label("loc_1347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1363")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_137A")

    label("loc_1363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_137A")

    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x1, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x13, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_13DE")
    OP_66(0x3, 0x1)
    OP_66(0x13, 0x1)
    Jump("loc_1525")

    label("loc_13DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_13F0")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_13F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1402")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_1402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1414")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_1414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_1426")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_1426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1434")
    Jump("loc_1525")

    label("loc_1434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1442")
    Jump("loc_1525")

    label("loc_1442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1454")
    OP_66(0x1, 0x1)
    Jump("loc_1525")

    label("loc_1454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1466")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_1466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1474")
    Jump("loc_1525")

    label("loc_1474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1486")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_1486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1494")
    Jump("loc_1525")

    label("loc_1494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_14A6")
    OP_66(0x1, 0x1)
    Jump("loc_1525")

    label("loc_14A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_14B4")
    Jump("loc_1525")

    label("loc_14B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_14C6")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_14C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_14D4")
    Jump("loc_1525")

    label("loc_14D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_14E6")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_14E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_14F8")
    OP_66(0x1, 0x1)
    Jump("loc_1525")

    label("loc_14F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_150A")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_150A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_151C")
    OP_66(0x3, 0x1)
    Jump("loc_1525")

    label("loc_151C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_END)), "loc_1525")

    label("loc_1525")

    SetMapObjFrame(0xFF, "tanmatu2", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1556")
    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)

    label("loc_1556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1572")
    SetMapObjFrame(0xFF, "box01", 0x0, 0x1)
    Jump("loc_1582")

    label("loc_1572")

    SetMapObjFrame(0xFF, "objects2", 0x0, 0x1)

    label("loc_1582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15CB")
    SetMapObjFrame(0xFF, "objects2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "box01", 0x1, 0x1)
    SetBarrier(0x0, 0x2, 0x1, 0x0, 257500, -1000, 68700, 11000, 5000, 90000)
    Jump("loc_15E8")

    label("loc_15CB")

    SetMapObjFrame(0xFF, "box01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "objects2", 0x1, 0x1)

    label("loc_15E8")

    OP_65(0x2, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1603")
    OP_66(0x2, 0x1)

    label("loc_1603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1616")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1616")

    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1646")
    SetMapObjFrame(0xFF, "01", 0x0, 0x1)
    OP_65(0x7, 0x1)

    label("loc_1646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165E")
    SetMapObjFrame(0xFF, "02", 0x0, 0x1)
    OP_65(0x8, 0x1)

    label("loc_165E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1676")
    SetMapObjFrame(0xFF, "05", 0x0, 0x1)
    OP_65(0x9, 0x1)

    label("loc_1676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1699")
    SetMapObjFrame(0xFF, "06", 0x0, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x0, 0x1)
    OP_65(0xA, 0x1)

    label("loc_1699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B1")
    SetMapObjFrame(0xFF, "07", 0x0, 0x1)
    OP_65(0xB, 0x1)

    label("loc_16B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16C9")
    SetMapObjFrame(0xFF, "08", 0x0, 0x1)
    OP_65(0xC, 0x1)

    label("loc_16C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E1")
    SetMapObjFrame(0xFF, "03", 0x0, 0x1)
    OP_65(0xD, 0x1)

    label("loc_16E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1704")
    SetMapObjFrame(0xFF, "04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x0, 0x1)
    OP_65(0xE, 0x1)

    label("loc_1704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1720")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_1737")

    label("loc_1720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1737")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_1737")

    label("loc_1737")

    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    OP_1B(0x8, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1768")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1783")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1796")
    OP_1B(0x8, 0x0, 0x37)

    label("loc_1796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17A9")
    OP_1B(0x8, 0x0, 0x37)

    label("loc_17A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D3")
    OP_1B(0x0, 0x0, 0x36)

    label("loc_17D3")

    ClearMapObjFlags(0x8, 0x10)
    ClearMapObjFlags(0x9, 0x10)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_17FF")
    SetMapObjFlags(0x7, 0x10)
    OP_65(0x4, 0x1)
    Jump("loc_1809")

    label("loc_17FF")

    ClearMapObjFlags(0x7, 0x10)
    OP_66(0x4, 0x1)

    label("loc_1809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1823")
    OP_65(0xF, 0x1)
    OP_65(0x10, 0x1)
    OP_65(0x11, 0x1)
    OP_65(0x12, 0x1)

    label("loc_1823")

    Return()

    # Function_2_1311 end

    def Function_3_1824(): pass

    label("Function_3_1824")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B58")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The orbal terminal is turned off.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF9")

    ChrTalk(
        0x101,
        (
            "#0000FWasn't maintenance for the department's\x01",
            "terminal line scheduled for today?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1964")

    ChrTalk(
        0x102,
        (
            "#0100FYes, I believe Fran mentioned that.\x02\x03",
            "Though, she's taking the day off since\x01",
            "she can't get much work done without\x01",
            "the orbal network.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA8")

    label("loc_1964")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19F9")

    ChrTalk(
        0x103,
        (
            "#0200FYes, I believe that's the case.\x02\x03",
            "I heard Fran was able to get the day off\x01",
            "because her terminal is out of commission.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA8")

    label("loc_19F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AA8")

    ChrTalk(
        0x104,
        (
            "#0300FPretty sure Fran mentioned something\x01",
            "along the lines of that, yeah.\x02\x03",
            "Something about the terminal bein' out\x01",
            "of order, which scored her the day off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA8")


    ChrTalk(
        0x101,
        (
            "#0000FHaha. Well, it's not like we'll be able to\x01",
            "work much, either.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 5)
    Jump("loc_1B54")

    label("loc_1AF9")


    ChrTalk(
        0x101,
        (
            "#0000FThe terminal is undergoing maintenance,\x01",
            "so we won't be able to go online today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B54")

    TalkEnd(0xFF)
    Return()

    label("loc_1B58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B70")
    Call(1, 20)
    Return()

    label("loc_1B70")

    OP_E3(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E3(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21E4")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E3(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1BB6"),
        (1, "loc_1D62"),
        (SWITCH_DEFAULT, "loc_21DF"),
    )


    label("loc_1BB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BDD")
    OP_2B(0x34, 0x31, 0x32, 0x2B, 0x33, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1BFE")
    OP_2B(0x31, 0x32, 0x2B, 0x33, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1C19")
    OP_2B(0x2D, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1C30")
    OP_2B(0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1C49")
    OP_2B(0x28, 0x29, 0x2A, 0x2F, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1C5C")
    OP_2B(0x25, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1C7B")
    OP_2B(0x22, 0x23, 0x18, 0x1A, 0x1C, 0x1E, 0x21, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1C9A")
    OP_2B(0x1F, 0x20, 0x21, 0x18, 0x1A, 0x1C, 0x1E, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1C9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1CB7")
    OP_2B(0x1B, 0x1C, 0x1D, 0x1E, 0x18, 0x1A, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1CD2")
    OP_2B(0x16, 0x17, 0x18, 0x19, 0x1A, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1CEF")
    OP_2B(0x11, 0x12, 0x13, 0x14, 0xE, 0x10, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1D08")
    OP_2B(0xD, 0xE, 0xF, 0x10, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1D25")
    OP_2B(0x9, 0xA, 0xB, 0x5, 0x6, 0x7, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1D3C")
    OP_2B(0x5, 0x6, 0x7, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1D3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_1D58")
    OP_2B(0x1, 0x35, 0x2, 0x3, 0xFFFF)
    Jump("loc_1D5D")

    label("loc_1D58")

    OP_2B(0x1, 0xFFFF)

    label("loc_1D5D")

    Jump("loc_21DF")

    label("loc_1D62")

    SetMapFlags(0x40000000)
    OP_E3(0x7)
    Sleep(500)
    SetChrName("Receptionist Fran")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DD8")
    Sound(2062, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Hello, you've reached the CPD. This is Fran speaking!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E0C")

    label("loc_1DD8")

    Sound(2061, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "As always, we appreciate your hard work!\x02",
    )

    CloseMessageWindow()

    label("loc_1E0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E3(0x4)"), scpexpr(EXPR_END)), "loc_2089")
    Sound(2067, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "Well, then, allow me to go over your reports...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E3(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FFE")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_1E95"),
        (13, "loc_1EDF"),
        (12, "loc_1F22"),
        (SWITCH_DEFAULT, "loc_1F63"),
    )


    label("loc_1E95")

    Sound(2075, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "1st Class... You're phenomenal, Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F63")

    label("loc_1EDF")

    Sound(2074, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "2nd Class... Great work, Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F63")

    label("loc_1F22")

    Sound(2073, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "3rd Class... Good job, Lloyd.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F63")

    label("loc_1F63")

    Sound(2076, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "I'll make sure your bonuses get transferred to you immediately!\x02",
    )

    CloseMessageWindow()
    Sound(2077, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Thank you, and please keep up the good work!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2081")

    label("loc_1FFE")

    Sound(2078, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "Thanks for the report, everyone.\x02",
    )

    CloseMessageWindow()
    Sound(2079, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "If you finish more support requests, please let me know!\x02",
    )

    CloseMessageWindow()

    label("loc_2081")

    SetScenarioFlags(0x1, 5)
    Jump("loc_21D1")

    label("loc_2089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_2148")
    Sound(2063, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "Hello again! Did you forget or something?\x02",
    )

    CloseMessageWindow()
    Sound(2064, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "You already submitted your report to me, so\x01",
            "call me when you complete more requests!\x01",
            "Bye-bye!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D1")

    label("loc_2148")

    Sound(2065, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
        "Hi, everyone! It seems there's nothing you\x01",
        "have to report now.\x02",
        )
    )

    CloseMessageWindow()
    Sound(2066, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "When you do, please let me know!\x02",
    )

    CloseMessageWindow()

    label("loc_21D1")

    OP_57(0x0)
    OP_E3(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_21DF")

    label("loc_21DF")

    Jump("loc_1B89")

    label("loc_21E4")

    OP_E3(0x6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2204")
    OP_E3(0xB)
    TalkEnd(0xFF)
    Call(0, 9)
    Return()

    label("loc_2204")

    FadeToBright(300, 0)
    OP_0D()
    OP_E3(0xB)
    TalkEnd(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_222E")
    OP_29(0x41, 0x1, 0x1)

    label("loc_222E")

    Return()

    # Function_3_1824 end

    def Function_4_222F(): pass

    label("Function_4_222F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2401")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Start the meeting]\x01",      # 0
            "[Hold off for now]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_22A0"),
        (1, "loc_2347"),
        (SWITCH_DEFAULT, "loc_23FF"),
    )


    label("loc_22A0")


    ChrTalk(
        0x101,
        (
            "#0400987V#0001FLet's get this meeting started, then.\x02\x03",
            "#0400988VFirst off, we should review all our info\x01",
            "that's relevant to the case.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    OP_65(0x2, 0x1)
    Call(0, 18)
    Jump("loc_23FF")

    label("loc_2347")


    ChrTalk(
        0x102,
        (
            "#0400989V#0100FOnce we're up to speed, let's meet\x01",
            "here again.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "To start the meeting, inspect the ! mark\x01",
            "at the table.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_23FF")

    label("loc_23FF")

    EventEnd(0x3)

    label("loc_2401")

    Return()

    # Function_4_222F end

    def Function_5_2402(): pass

    label("Function_5_2402")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        "#0200312VSo...you up for it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7110", 0)
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x104,
        (
            "#0200313V#0304FNo objections here.\x02\x03",
            "#0200314V#0301F'Sides, you're the one who dragged me\x01",
            "to the CPD in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200315V#5P#1002FHeh. Sure you don't want me to recommend\x01",
            "you to the First Division?\x02\x03",
            "#0200316VThey'd probably really benefit from someone\x01",
            "with your combat prowess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0200317V#0306FYeeeah, I'll pass.\x02\x03",
            "#0200318V#0300FHonestly, I'd rather sign up for the Guardian\x01",
            "Force again than do that. Less paperwork,\x01",
            "more action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0200319V#5P#1000FWhat about you, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0200320V#0104FI will happily accept the position.\x02\x03",
            "#0200321V#0100FI'm looking forward to working\x01",
            "under you, Chief Sergei.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200322V#5P#1006FGlad to hear. And, to be frank, I didn't expect\x01",
            "someone like you to be here.\x02\x03",
            "#0200323V#1001FI guess the higher-ups recommended you to this\x01",
            "division with hopes that your calm demeanor\x01",
            "would make for the perfect office girl.\x02\x03",
            "#0200324VYou're well aware that this won't be a bed of roses,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0200325V#0102FYes. Quite aware, sir.\x02\x03",
            "#0200326V#0104FFrom here on out, I intend to work on\x01",
            "things that actually make a difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200327V#5P#1004FGood answer.\x02\x03",
            "#0200328V#1002FWell, Tio. Do I even need to ask?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200329V#4P#0203FNot at all. This position is what we\x01",
            "agreed on from the start.\x02\x03",
            "#0200330V#0200FThough, on a side note, the orbal cables\x01",
            "are scheduled to be wired this evening.\x02\x03",
            "#0200331VWould you like me to set up the terminal,\x01",
            "as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200332V#5P#1004FYeah, I was counting on it.\x02\x03",
            "#0200333V#1000FSo...three down, one to go.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B17():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2B17)
    Sleep(50)

    def lambda_2B27():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2B27)
    Sleep(50)

    def lambda_2B37():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2B37)
    WaitChrThread(0x102, 2)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#0200334V#5P#1003FLloyd Bannings...\x02\x03",
            "#0200335VA Crossbell Police Academy graduate who earned\x01",
            "high marks in both police theory and practice...\x02\x03",
            "#0200336VYou took those skills and used them to ace the\x01",
            "CPD's detective exam.\x02\x03",
            "#0200337V#1001FIf you ask me, you're too talented for this team.\x01",
            "These guys aren't nearly as qualified as you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200338V#12P#0001F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200339V#5P#1004FA cop like you will find success in whatever\x01",
            "division or team he's assigned to.\x02\x03",
            "#0200340VHell, I bet no one here would blame you if\x01",
            "you walked right out that door.\x02\x03",
            "#0200341V#1002FWith that in mind, still have any lingering\x01",
            "doubts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200342V#12P#0004FNo, sir. None at all.\x02\x03",
            "#0200343V#0000FI'd be happy to join the SSS,\x01",
            "Chief Sergei.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0200344V#11P#0302FHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0200345V#11P#0102FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200346V#12P#0202F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200347V#5P#1006FYou're a real killjoy, kid.\x02\x03",
            "#0200348VI was hoping that you'd at least show\x01",
            "a hint of uncertainty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200349V#12P#0012FC'mon, sir...\x02",
    )

    CloseMessageWindow()

    def lambda_2F20():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2F20)
    Sleep(50)

    def lambda_2F30():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2F30)
    Sleep(50)

    def lambda_2F40():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2F40)
    WaitChrThread(0x103, 2)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#0200350V#5P#1003FWell, that settles that. You guys\x01",
            "have the day off today.\x02\x03",
            "#0200351VFrom tomorrow onward, you'll be\x01",
            "working your asses off.\x02\x03",
            "#0200352V#1002FTio? Terminal's all yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200353V#12P#0204FRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200354V#5P#1005FOops, I almost forgot...\x02\x03",
            "#0200355V#1003FListen up. Lloyd Bannings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200356V#12P#0001FSir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0200357V#5P#1001FElie MacDowell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0200358V#0101FSir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0200359V#5P#1001FRandy Orlando.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0200360V#0301F'Sup.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0200361V#5P#1001FTio Plato.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200362V#12P#0201FYes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0200363V#5P#1003FAs of today at 9AM, I officially approve\x01",
            "and acknowledge your new assignments.\x02\x03",
            "#0200364V#1002FWelcome to the Special Support Section.\x02\x03",
            "#0200365VLook forward to the mountain of different\x01",
            "jobs I'll be throwing at you.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "As initial investigation expenses,\x01",
            "the team received \x07\x02",
            "1000 mira\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddMira(1000)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("t4100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_2402 end

    def Function_6_3321(): pass

    label("Function_6_3321")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    OP_68(12600, 2350, 5200, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 11300, 900, 6650, 90)
    SetChrPos(0x102, 11300, 900, 4600, 90)
    SetChrPos(0x103, 13900, 900, 4600, 270)
    SetChrPos(0x104, 11300, 900, 2550, 90)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 13900, 900, 6650, 270)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrSubChip(0x8, 0x1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis011.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis120.itp")
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0300029VWell, time to get started on your\x01",
            "first official job as the SSS.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7110", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(12600, 1850, 5200, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#0300030V#5P#1000FThough maybe I should give you some more\x01",
            "information before we get ahead of ourselves.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    Sleep(200)

    ChrTalk(
        0x8,
        "#0300031V#11P#1000FLloyd, grab your Detective Notebook.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0300032V#0001FY-Yes, sir!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x104,
        (
            "#0300033V#0300FBlack notebook with the police crest, eh?\x01",
            "Looks like the real deal.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#0300034V#0100FWe can also use this to identify ourselves\x01",
            "as police officers, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#0300035V#1003FCorrect. There's also some more advice and\x01",
            "explanations in there, if you ever get curious.\x02\x03",
            "#0300036VHeck, it's even got info about your tactical\x01",
            "orbments. Pretty good reference to have.\x02\x03",
            "#0300037V#1002FHowever, its most important purpose is\x01",
            "to keep track of the investigation report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#0300038V#0305FInvestigation report?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x8,
        "#0300039V#1003FLloyd, your turn.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#0300040V#0000FYes, sir. (Good thing I learned all about it at\x01",
            "the academy.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#0300041V#0000FThe CPD maintains a rule that all of its\x01",
            "investigations are to be carefully and\x01",
            "thoroughly documented.\x02\x03",
            "#0300042V#0003FAfter an investigation is assigned to you,\x01",
            "you can record its status and keep track\x01",
            "of progress in the Detective Notebook.\x02\x03",
            "#0300043VWhen submitting a report, the department\x01",
            "evaluates what's in the notebook, and our\x01",
            "bonuses are decided around that.\x02\x03",
            "#0300044V#0000FThat's why we need to fill it out as detailed\x01",
            "and concisely as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0300045V#6P#0100FThat's a smart system.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300046V#12P#0306F*sigh* Just sounds like a bunch of\x01",
            "boring paperwork to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0300047V#11P#1000FThat's the gist of it.\x02\x03",
            "#0300048V#1003FHowever, the situation at the SSS is\x01",
            "slightly different from other divisions.\x02\x03",
            "#0300049V#1002FApart from your standard investigations,\x01",
            "you're also assigned to what we like to\x01",
            "call 'support requests.'\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)

    ChrTalk(
        0x101,
        "#0300050V#0005FHuh?\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x8, 0x1)
    Sleep(200)

    ChrTalk(
        0x8,
        "#0300051V#5P#1002FTio, if you will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0300052V#2P#0203FRoger.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 14800, 850, 5400, 270)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x103,
        "#0300053V#2P#0200FEveryone, follow me.\x02",
    )

    CloseMessageWindow()
    OP_68(16100, 1850, 10000, 3000)
    MoveCamera(7, 21, 0, 3000)
    SetCameraDistance(25000, 3000)

    def lambda_3D23():
        OP_95(0xFE, 16100, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3D23)
    Sleep(750)
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_90(0x8, 14700, 850, 7600, 270)
    OP_0D()
    OP_92(0x8, 0x396C, 0x2BC0, 0x1F4)

    def lambda_3D6C():
        OP_95(0xFE, 14700, 850, 11200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D6C)
    WaitChrThread(0x103, 1)

    def lambda_3D8A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3D8A)
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_90(0x101, 10400, 850, 7600, 90)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_90(0x102, 10400, 850, 5400, 125)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_90(0x104, 10400, 850, 3200, 125)
    OP_0D()
    BeginChrThread(0x104, 3, 0, 8)
    BeginChrThread(0x102, 3, 0, 7)
    OP_92(0x101, 0x3B60, 0x2134, 0x1F4)
    Sleep(150)

    def lambda_3E13():
        OP_95(0xFE, 15200, 850, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E13)
    WaitChrThread(0x8, 1)

    def lambda_3E31():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3E31)
    WaitChrThread(0x101, 1)

    def lambda_3E42():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E42)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x51)

    ChrTalk(
        0x101,
        "#0300054V#6P#0000FOh, I remember now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0300055V#3P#0100FIsn't this the terminal that you were busy\x01",
            "hooking up to the orbal network?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xE1, 0x1F4)

    ChrTalk(
        0x103,
        (
            "#0300056V#11P#0200FYes. I finished configuring it yesterday.\x02\x03",
            "#0300057VAfter booting up, you can select an option\x01",
            "from the menu screen.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x2D, 0x1F4)
    Sleep(300)
    Sound(72, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x104,
        "#0300058V#0305FWell, would ya look at that...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#0300059V#0005FIs this where we'll receive support requests?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x8,
        (
            "#0300060V#1000FRight. Aside from official missions from the\x01",
            "department, it can also receive other requests.\x02\x03",
            "#0300061V#1003FThink about requests coming from citizens,\x01",
            "tourists... Heck, maybe even the government\x01",
            "will send us jobs from time to time.\x02\x03",
            "#0300062V#1002FSupport requests are optional, but if you\x01",
            "decide to skip some, odds are that the\x01",
            "Bracer Guild will snatch them up.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4202():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4202)
    Sleep(50)

    def lambda_4212():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4212)
    Sleep(50)

    def lambda_4222():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4222)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x101,
        "#0300063V#12P#0001FOh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300064V#3P#0309FYeah, sounds about right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0300065V#3P#0103FBy doing support requests, we take some\x01",
            "of the guild's popularity for ourselves.\x02\x03",
            "#0300066V#0100FIs that what you're getting at?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#0300067V#5P#1002FBasically, but on a much smaller scale.\x02\x03",
            "#0300068VAnyway, when the department's busy,\x01",
            "they might force you to help them.\x02\x03",
            "#0300069VPatrolling the city, doing some menial\x01",
            "paperwork... Who knows?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#0300070V#3P#0306FYou're kiddin', right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0300071V#12P#0012FHaha. Come on, it won't be\x01",
            "that bad.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0300072V#6P#0000FSo has the terminal already started\x01",
            "receiving these requests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0300073V#5P#1003FWhy don't you take a look for yourselves?\x02\x03",
            "#0300074V#1000FJust don't forget to keep track of them in\x01",
            "your notebook.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x101,
        "#0300075V#12P#0000FUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x40)
    SetChrPos(0x0, 15000, 850, 8900, 45)
    SetScenarioFlags(0x41, 5)
    OP_29(0x3D, 0x4, 0x2)
    OP_29(0x3D, 0x1, 0x0)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    EventEnd(0x5)
    Return()

    # Function_6_3321 end

    def Function_7_4600(): pass

    label("Function_7_4600")

    Sleep(100)

    def lambda_4608():
        OP_95(0xFE, 10400, 850, 9300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4608)
    WaitChrThread(0x102, 1)

    def lambda_4626():
        OP_95(0xFE, 14000, 850, 9300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4626)
    WaitChrThread(0x102, 1)
    Return()

    # Function_7_4600 end

    def Function_8_4640(): pass

    label("Function_8_4640")


    def lambda_4645():
        OP_95(0xFE, 10400, 850, 10000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4645)
    WaitChrThread(0x104, 1)

    def lambda_4663():
        OP_95(0xFE, 13200, 850, 10000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4663)
    WaitChrThread(0x104, 1)
    Return()

    # Function_8_4640 end

    def Function_9_467D(): pass

    label("Function_9_467D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x103, 14100, 850, 9500, 45)
    SetChrPos(0x104, 15600, 850, 8000, 45)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 12400, 850, 10200, 90)
    OP_4B(0x8, 0xFF)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis120.itp")
    FadeToBright(1000, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Support Request Explanation]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#0300076V#12P#0305FSeems to me like this is just a glorified\x01",
            "notification system, but for cops.\x02\x03",
            "#0300077V#0300FNow we just gotta head down to HQ\x01",
            "and listen to their explanation, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0300078V#5P#0003FYeah, sounds like it.\x02\x03",
            "#0300079V#0000FI think I'm finally starting to get the idea\x01",
            "behind this whole orbal network thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0300080V#11P#0100FUnlike telephones, which are purely auditory,\x01",
            "the orbal network can transmit text and images.\x02\x03",
            "#0300081VI've heard about it before, but now that I've seen\x01",
            "it in practice, I can certainly see how it would be\x01",
            "advantageous in all sorts of situations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0300082V#6P#0203FYes. As we speak, beta testing is being\x01",
            "conducted throughout Crossbell State.\x02\x03",
            "#0300083V#0200FThe system implemented in the police\x01",
            "department is one such example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0300084V#6P#1003FThough I hear the guild has also started\x01",
            "experimenting with terminal systems, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x12C)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#0300085V#6P#1002FThat should be enough to get you started.\x02\x03",
            "#0300086VHow about I let you guys work on that\x01",
            "support request that just came in?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4C2C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C2C)
    Sleep(50)

    def lambda_4C3C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4C3C)
    Sleep(50)

    def lambda_4C4C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4C4C)
    Sleep(50)

    def lambda_4C5C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4C5C)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x101,
        (
            "#0300087V#11P#0000FUnderstood.\x02\x03",
            "#0300088V#0001FBut, uh... What do we do after that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0300089V#3P#1003FI'd love to say, 'Do whatever you feel like doing,'\x01",
            "but you can bet that the real requests will start\x01",
            "pouring in after your little lecture at HQ is over.\x02\x03",
            "#0300090V#1002FLet's see...\x02\x03",
            "#0300091VConsidering this is your first assignment, try\x01",
            "completing this as a statement to HQ saying\x01",
            "that you're capable of police work.\x02\x03",
            "#0300092VThat should shut them up for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0300093V#11P#0006F(Is that really why we should be\x01",
            "doing this?)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#0300094V#3P#1000FBy the way, Lloyd... You're in charge\x01",
            "of giving everyone a tour of the city.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0300095V#11P#0005FA tour of the city? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0300096V#3P#1000FYou're the ones protecting this place,\x01",
            "so go see it with your own eyes.\x01",
            "Know it like the back of your hands.\x02\x03",
            "#0300097VOh, and once you head out, make sure\x01",
            "to drop by the weapons shop and the\x01",
            "orbal store. They aren't too far away.\x02\x03",
            "#0300098VAs police officers, those places will be\x01",
            "pretty handy in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0300099V#11P#0000FWe'll stop by before going to the\x01",
            "department, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#0300100V#3P#1003FI'll be in my office most of the time, probably\x01",
            "either reading a magazine or taking a nap.\x02\x03",
            "#0300101VIf you run into any problems, don't bother me.\x01",
            "You're smart kids, so figure it out yourselves.\x02\x03",
            "#0300102V#1002FWell, then, off you go.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5247():

        label("loc_5247")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5247")

    QueueWorkItem2(0x101, 2, lambda_5247)

    def lambda_5259():

        label("loc_5259")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5259")

    QueueWorkItem2(0x102, 2, lambda_5259)

    def lambda_526B():

        label("loc_526B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_526B")

    QueueWorkItem2(0x104, 2, lambda_526B)
    BeginChrThread(0x8, 3, 0, 10)
    Sleep(1000)

    def lambda_5286():

        label("loc_5286")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5286")

    QueueWorkItem2(0x103, 2, lambda_5286)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0300103V#6P#0011FW-Wait a minute...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 3)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)

    ChrTalk(
        0x104,
        "#0300104V#6P#0301FThat's one irresponsible dude.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0300105V#0106FIs it really okay for him to slack off like that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0300106V#0211FI fear for our future.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0300107V#0012FA-Anyway...this is our first real assignment.\x02",
    )

    CloseMessageWindow()
    OP_68(15900, 1750, 9800, 1500)

    def lambda_53CD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_53CD)
    Sleep(50)

    def lambda_53DD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_53DD)
    Sleep(50)

    def lambda_53ED():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_53ED)
    Sleep(50)

    def lambda_53FD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_53FD)
    WaitChrThread(0x103, 2)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#0300108V#5P#0000FLet's walk around the city a bit first\x01",
            "and then take care of that support\x01",
            "request.\x02\x03",
            "#0300109VIt's natural to feel nervous, but as long\x01",
            "as we don't rush things, everything will\x01",
            "turn out okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0300110V#2P#0100FAgreed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0300111V#6P#0204FRoger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300112V#12P#0300FTime to hit the road, then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(500)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you inspect the terminal at the SSS and\x01",
            "choose 'Check Requests,' a list of available\x01",
            "support requests is displayed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The support requests are completely optional,\x01",
            "but completing them earns you mira and DP.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0xFF, 0x0)
    OP_68(15000, 1850, 8900, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrPos(0x1, 15000, 850, 8900, 225)
    SetChrPos(0x2, 15000, 850, 8900, 225)
    SetChrPos(0x3, 15000, 850, 8900, 225)
    SetScenarioFlags(0x41, 6)
    OP_29(0x3D, 0x1, 0x1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    PlayBGM("ed7100", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_9_467D end

    def Function_10_5718(): pass

    label("Function_10_5718")

    OP_68(15900, 1750, 5400, 4000)

    def lambda_572E():
        OP_95(0xFE, 16500, 850, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_572E)
    WaitChrThread(0x8, 1)

    def lambda_574C():
        OP_95(0xFE, 16500, 850, 3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_574C)
    WaitChrThread(0x8, 1)

    def lambda_576A():
        OP_95(0xFE, 18300, 850, 3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_576A)
    WaitChrThread(0x8, 1)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_579D():
        OP_95(0xFE, 19800, 850, 3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_579D)
    Sleep(300)

    def lambda_57BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_57BA)
    WaitChrThread(0x8, 1)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x1)
    Return()

    # Function_10_5718 end

    def Function_11_57F2(): pass

    label("Function_11_57F2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50091.itc", 0x1E)
    OP_68(64000, 1100, 11400, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 58500, 0, 3200, 90)
    SetChrPos(0x102, 58500, 0, 3200, 90)
    SetChrPos(0x103, 58500, 0, 3200, 90)
    SetChrPos(0x104, 58500, 0, 3200, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x28, 0x1E)
    SetChrSubChip(0x28, 0x1D)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 63700, 750, 10300, 0)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    SetChrFlags(0x9, 0x80)
    LoadEffect(0x0, "event\\eva05_00.eff")
    PlayEffect(0x0, 0x0, 0x8, 0x140, 0, 1300, 350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01000.itp")
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    OP_68(64000, 1100, 8600, 5000)
    BeginChrThread(0x101, 3, 0, 12)
    Sleep(650)
    BeginChrThread(0x102, 3, 0, 13)
    Sleep(650)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(650)
    BeginChrThread(0x103, 3, 0, 14)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x8,
        (
            "#0400754VOh, you're back already.\x02\x03",
            "#0400755VManaged to stop those delinquents?\x02",
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
            "#0400756V#12P#0006FWell, about that, Chief...\x02\x03",
            "#0400757V#0001FWe think this situation might be a bit\x01",
            "more complicated than you expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0400758V#5P#1005FHuh?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained everything that happened and\x01",
            "laid out all the facts for Chief Sergei.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#0400759V#5P#1001FHmm, interesting.\x02\x03",
            "#0400760V#1003F...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x101,
        "#0400761V#12P#0005FUh, Chief?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400762V#5P#1003F...All right.\x02\x03",
            "#0400763V#1000FYou can handle this as you see fit.\x02",
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
        "#0400764V#12P#0011FExcuse me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400765V#0105FWhat do you mean by that, exactly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400766V#5P#1003FWhether you're willing to continue the\x01",
            "investigation is entirely up to you.\x02\x03",
            "#0400767V#1000FYou won't be getting any information\x01",
            "regarding Revache out of me.\x02\x03",
            "#0400768VYou'll have to dig for it on your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400769V#12P#0013FB-But that doesn't make any sense...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400770V#5P#1001FIf I told you to stop the investigation,\x01",
            "would you follow orders?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0400771V#12P#0005FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400772V#5P#1003FIf the mafia really is involved in this,\x01",
            "things are only going to get nastier.\x02\x03",
            "#0400773VAs your supervisor, the most logical\x01",
            "step is to order you to close the case.\x01",
            "Immediately.\x02\x03",
            "#0400774V #1001FNow, is that what you want me to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400775V#12P#0008FNo...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400776V#0306FIf we gave up now, I'm pretty sure we'd\x01",
            "regret it down the road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400777V#0108FEspecially after coming this far.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400778V#4P#0203FI agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400779V#5P#1004FAll right, then.\x02\x03",
            "#0400780VI doubt I'd be able to rest easy knowing you\x01",
            "kids are getting beaten up by the mafia.\x02\x03",
            "#0400781V#1002FSo, I'll do you a favor and introduce you to a\x01",
            "trusty consultant of mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400782V#12P#0005FA consultant?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 62800, 0, 11600, 270)
    Sound(820, 0, 100, 0)

    def lambda_6224():

        label("loc_6224")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6224")

    QueueWorkItem2(0x101, 2, lambda_6224)

    def lambda_6236():

        label("loc_6236")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6236")

    QueueWorkItem2(0x102, 2, lambda_6236)

    def lambda_6248():

        label("loc_6248")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6248")

    QueueWorkItem2(0x103, 2, lambda_6248)

    def lambda_625A():

        label("loc_625A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_625A")

    QueueWorkItem2(0x104, 2, lambda_625A)
    OP_0D()

    def lambda_626D():
        OP_95(0xFE, 61600, 0, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_626D)
    WaitChrThread(0x8, 1)
    OP_68(64120, 1100, 7920, 2500)

    def lambda_629C():
        OP_95(0xFE, 61600, 0, 8300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_629C)
    WaitChrThread(0x8, 1)

    def lambda_62BA():
        OP_95(0xFE, 63000, 0, 7800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_62BA)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Sergei handed over a business card to Lloyd.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#0400783V#12P#0005F'Grimwood Law Office'?\x02\x03",
            "#0400784V#0001FSomething about that rings a bell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400785V#1004F#5PIt's a law office located over on West Street.\x02\x03",
            "#0400786V#1002FIt's run by a bearded lawyer named Ian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400787V#12P#0000FOh! Near the bakery, right?\x02\x03",
            "#0400788VI definitely ran across him a couple of\x01",
            "times when I used to live in the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400789V#0104FI've heard of him, too.\x02\x03",
            "#0400790V#0100FMr. Grimwood provides consulting services\x01",
            "to corporations and other businesses, right?\x02\x03",
            "#0400791VHe also frequently offers legal consultations\x01",
            "to ordinary citizens, I believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400792V#1003F#5PSpot on. 'Cause of that boxed beard and\x01",
            "build, he looks like a genuine bear.\x01",
            "People often refer to him as 'Grizzly Grim.'\x02\x03",
            "#0400793VHe probably has loads of info on the mafia.\x02\x03",
            "#0400794V#1002FWho knows? He might even have new intel\x01",
            "that even the CPD doesn't know.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0400795V#12P#0002FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400796V#12P#0202FThat is quite impressive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400797V#2P#0305FJust what kinda guy is this lawyer?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400798V#1004F#5PYou'll find out when you meet him.\x02\x03",
            "#0400799V#1000FI've spoken with him previously about\x01",
            "SSS-related matters.\x02\x03",
            "#0400800VHe'd at least let you finish explaining\x01",
            "why you're there if you tell him who\x01",
            "you are.\x02\x03",
            "#0400801VThis is the perfect opportunity for a\x01",
            "little meet and greet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400802V#12P#0001FWe'll get right on it.\x02",
    )

    CloseMessageWindow()

    def lambda_68E6():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_68E6)
    Sleep(150)

    def lambda_68F6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_68F6)
    Sleep(50)

    def lambda_6906():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6906)
    Sleep(50)

    def lambda_6916():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6916)
    WaitChrThread(0x102, 2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0400803V#6P#0000FWest Street is just around the corner.\x02\x03",
            "#0400804VEveryone okay with paying this law\x01",
            "office a visit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400805V#11P#0100FOf course. Shall we head out?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetChrFlags(0x8, 0x80)
    StopEffect(0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    OP_68(64000, 1330, 6000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 64000, 0, 6000, 0)
    SetChrPos(0x1, 64000, 0, 6000, 0)
    SetChrPos(0x2, 64000, 0, 6000, 0)
    SetChrPos(0x3, 64000, 0, 6000, 0)
    SetScenarioFlags(0x42, 6)
    OP_29(0x3E, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_11_57F2 end

    def Function_12_6A8D(): pass

    label("Function_12_6A8D")


    def lambda_6A92():
        OP_95(0xFE, 61000, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A92)
    Sleep(500)

    def lambda_6AAF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6AAF)
    WaitChrThread(0x101, 1)

    def lambda_6AC4():
        OP_95(0xFE, 63000, 0, 6700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AC4)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_12_6A8D end

    def Function_13_6AE5(): pass

    label("Function_13_6AE5")


    def lambda_6AEA():
        OP_95(0xFE, 61000, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6AEA)
    Sleep(500)

    def lambda_6B07():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6B07)
    WaitChrThread(0x102, 1)

    def lambda_6B1C():
        OP_95(0xFE, 64300, 0, 6700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B1C)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_13_6AE5 end

    def Function_14_6B3D(): pass

    label("Function_14_6B3D")


    def lambda_6B42():
        OP_95(0xFE, 61000, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B42)
    Sleep(500)

    def lambda_6B5F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6B5F)
    WaitChrThread(0x103, 1)

    def lambda_6B74():
        OP_95(0xFE, 63200, 0, 5400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B74)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_14_6B3D end

    def Function_15_6B95(): pass

    label("Function_15_6B95")


    def lambda_6B9A():
        OP_95(0xFE, 61000, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6B9A)
    Sleep(500)

    def lambda_6BB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6BB7)
    WaitChrThread(0x104, 1)

    def lambda_6BCC():
        OP_95(0xFE, 64500, 0, 5400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6BCC)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_15_6B95 end

    def Function_16_6BED(): pass

    label("Function_16_6BED")

    OP_92(0x8, 0xF0A0, 0x1FA4, 0x1F4)

    def lambda_6BFF():
        OP_95(0xFE, 61600, 0, 8300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6BFF)
    WaitChrThread(0x8, 1)

    def lambda_6C1D():
        OP_95(0xFE, 61600, 30, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6C1D)
    WaitChrThread(0x8, 1)

    def lambda_6C3B():
        OP_95(0xFE, 62800, 30, 11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6C3B)
    WaitChrThread(0x8, 1)
    Fade(250)
    SetChrPos(0x8, 64000, 0, 11500, 180)

    def lambda_6C6F():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6C6F)

    def lambda_6C7C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6C7C)

    def lambda_6C89():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6C89)

    def lambda_6C96():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6C96)
    OP_0D()
    Return()

    # Function_16_6BED end

    def Function_17_6CA0(): pass

    label("Function_17_6CA0")

    EventBegin(0x0)
    Fade(1000)
    OP_68(9900, 1750, 10600, 0)
    MoveCamera(50, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x101, 9900, 850, 9800, 90)
    SetChrPos(0x103, 9900, 850, 11000, 135)
    SetChrPos(0x102, 8700, 850, 9800, 90)
    SetChrPos(0x104, 8700, 850, 11000, 135)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0400977V#6P#0005FWhat's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400978V#6P#0105FA message, maybe?\x02",
    )

    CloseMessageWindow()
    OP_68(16800, 1750, 7500, 3500)

    def lambda_6D92():
        OP_95(0xFE, 16500, 850, 7000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D92)
    Sleep(300)

    def lambda_6DAF():
        OP_96(0xFE, 0x3F48, 0x352, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6DAF)
    Sleep(300)

    def lambda_6DCC():
        OP_95(0xFE, 15100, 850, 6500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6DCC)
    Sleep(300)

    def lambda_6DE9():
        OP_96(0xFE, 0x39D0, 0x352, 0x206C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6DE9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's a note stuck to the bulletin board.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#0400979V\x07\x05",
            "I've got some errands to run. Wrap up the\x01",
            "case however you see fit.\x01",
            "                                                 - Sergei\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#0400980V\x07\x00",
            "#6P#0003FThe chief went out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400981V\x07\x00",
            "#3P#0301FWho wants to bet that he ran away 'cause\x01",
            "the case seemed like a pain in the ass?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400982V\x07\x00",
            "#0203FWe cannot rule out that possibility...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#0400983V\x07\x00",
            "#12P#0100FPerhaps, but think about it like this. It's a\x01",
            "privilege to be given the chance to solve\x01",
            "a case however we like, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#0400984V#6P#0101FThat said, what's our plan?\x02\x03",
            "#0400985VShould we hold a meeting to review\x01",
            "what we know?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#0400986V#11P#0000FYeah, definitely.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "To start the meeting, inspect the exclamation\x01",
            "point at the table.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, 16500, 850, 7000, 90)
    ModifyEventFlags(0, 0, 0x80)
    OP_66(0x2, 0x1)
    SetScenarioFlags(0x43, 1)
    OP_29(0x3E, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_17_6CA0 end

    def Function_18_71B3(): pass

    label("Function_18_71B3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00102.itc", 0x1E)
    OP_68(12600, 2350, 7000, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13500, 850, 8400, 315)
    SetChrPos(0x102, 13900, 900, 6650, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    SetMapObjFrame(0xFF, "white", 0x0, 0x1)
    SetMapObjFrame(0xFF, "white_sd", 0x0, 0x1)
    ClearChrFlags(0x17, 0x80)
    OP_78(0xA, 0x17)
    OP_49()
    SetChrPos(0x17, 12600, 850, 9500, 0)
    OP_D3(0x17, 0x0, 0x0, 0x0, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis012.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis013.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis114.itp")
    PlayBGM("ed7516", 0)
    OP_68(12600, 1850, 7000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#0400990V#11P#0003FThe incident took place around midnight,\x01",
            "five days ago.\x02\x03",
            "#0400991VMembers of both the Saber Vipers and\x01",
            "Testaments were ambushed by an unknown\x01",
            "assailant. Possibly a group of assailants.\x02\x03",
            "#0400992V#0001FHowever, the attacks occurred at two different\x01",
            "locations in the city's Downtown District.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(300)

    AnonymousTalk(
        0x101,
        "#0400993V#0001FHere...and here.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x4, 0x0, 0x0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(1000)
    OP_C9(0x3, 0x4, 0x0, 0x0, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x102,
        (
            "#0400994V#0101FThe Testaments member was attacked in the\x01",
            "alleyway to the west...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#0400995V#0301F...and the Saber Viper got messed up in front of Ignis,\x01",
            "which is towards the east.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#0400996V#6P#0205FIn other words, the attacks happened\x01",
            "at opposite ends of the area.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 5)), scpexpr(EXPR_END)), "loc_7905")
    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#0401002V#5P#0001FExactly. By doing so, it made it hard for both\x01",
            "groups to learn what happened to the other.\x02\x03",
            "#0400998V#0008FAfter initial treatments in their respective\x01",
            "bases weren't enough, the victims were sent\x01",
            "to the hospital the next day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400999V#12P#0101FWeren't the victims transported there in the\x01",
            "same ambulance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401000V#5P#0006FYeah. I can only imagine how much of a\x01",
            "shock that was to the medical staff on board.\x02\x03",
            "#0401003V#0001FSo, consequently, each group firmly believes\x01",
            "that they were attacked by the other, which is\x01",
            "what we confirmed today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79E8")

    label("loc_7905")


    ChrTalk(
        0x101,
        (
            "#0400997V#5P#0003FExactly. By doing so, it made it hard for both\x01",
            "groups to learn what happened to the other.\x02\x03",
            "#0401001V#0000FAnd that leads us to the present, where each\x01",
            "group blames the other for their members'\x01",
            "injuries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79E8")


    ChrTalk(
        0x104,
        (
            "#0401004V#6P#0306F*sigh*. Yeah, the only answer that makes sense\x01",
            "is that there was a third party involved.\x02\x03",
            "#0401005V#0301FUnless both groups rehearsed their accounts,\x01",
            "chances of either group bein' responsible for\x01",
            "attackin' the other are pretty slim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401006V#5P#0000FAgreed. Based on the evidence so far,\x01",
            "it's safe to assume the attacks were\x01",
            "the work of some third party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0401007V#12P#0104FAll we can do now is consider all the\x01",
            "possibilities and rule out the ones that\x01",
            "don't seem feasible.\x02\x03",
            "#0401008V#0101FBut you already have an idea who that\x01",
            "third party might be, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401009V#5P#0003FI do.\x02\x03",
            "#0401010V#0001FRevache & Co.: the mafia that controls\x01",
            "Crossbell's criminal underbelly.\x02\x03",
            "#0401011VAccording to the intel Grace shared with us,\x01",
            "someone spotted mafiosos snooping around\x01",
            "the Downtown District a few weeks ago.\x02\x03",
            "#0401012V#0006FUnfortunately, we don't have the time to\x01",
            "verify the credibility of that. However...\x02\x03",
            "#0401013V#0001F...let's assume that Revache was responsible\x01",
            "for both attacks and continue our conversation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0401014V#6P#0203FIf that were the case...\x02\x03",
            "#0401015V#0201F...what was their motive?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401016V#5P#0003FBingo. The answer to that is crucial.\x02\x03",
            "#0401017V#0001FIf we can't answer that, we're all the\x01",
            "way back to square one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0401018V#6P#0303FSo, it comes down to motive...\x02\x03",
            "#0401019V#0308FThere's hardly any conflict of interest\x01",
            "between the mafia and the two gangs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0401020V#12P#0103FThere must be a line that connects the\x01",
            "three dots together.\x02\x03",
            "#0401021V#0100FAnd once again, you already have an\x01",
            "idea of what it is, don't you, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401022V#5P#0004FWell, I can't say with absolute certainty,\x01",
            "of course.\x02\x03",
            "#0401023V#0000FI think there's one thing that connects\x01",
            "these three factors.\x02",
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
            "[Wazy]\x01",                        # 0
            "[Wald]\x01",                        # 1
            "[The presence of Heiyue]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8132"),
        (1, "loc_8433"),
        (2, "loc_85B3"),
        (SWITCH_DEFAULT, "loc_87E7"),
    )


    label("loc_8132")

    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#0401024V#5P#0003FThis might sound ridiculous, but...\x02\x03",
            "#0401025V #0001FIt's possible that it's Wazy, who showed\x01",
            "up in the Downtown District two years ago.\x02\x03",
            "#0401026VAnd get this. Wazy could be the son of\x01",
            "Revache's boss.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0401027V#12P#0105FR-Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401028V#6P#0301FWow, man. How'd ya figure that out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401029V#5P#0006FIt's just a possibility!\x02\x03",
            "#0401030V#0000FSo, to get his runaway son back home, the boss\x01",
            "hatched a scheme that would take place in the\x01",
            "Downtown District.\x02\x03",
            "#0401031V#0012FYou know, if I keep piling up assumptions like this,\x01",
            "I might as well quit the force and start writing a\x01",
            "fantasy series.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401032V#6P#0306FDude... C'mon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_87E7")

    label("loc_8433")


    ChrTalk(
        0x101,
        (
            "#0401033V#5P#0003FI'm just thinking out loud here, but...\x02\x03",
            "#0401034V#0001F...what if someone in the mafia holds\x01",
            "a grudge against Wald?\x02\x03",
            "#0401035VThat would explain why the mafia caused\x01",
            "this incident the other night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0401036V#12P#0106FWell... Sorry, but I don't see it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401037V#6P#0301FThat's a pretty big reach, dude.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401038V#5P#0006FY-Yeah, maybe so...\x02",
    )

    CloseMessageWindow()
    Jump("loc_87E7")

    label("loc_85B3")

    OP_2C(0x3E, 0x3)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#0401039V#5P#0003FThe only realistic possibility that\x01",
            "comes to mind is Heiyue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0401040V#6P#0305FOh, right. Our grizzly friend\x01",
            "mentioned them, didn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0401041V#12P#0103FThat definitely feels like the most\x01",
            "likely possibility for now.\x02\x03",
            "#0401042V#0101FIn that case, though...what about\x01",
            "Heiyue connects these three?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0401043V#6P#0203FIn order to be connected, there has to\x01",
            "be some sort of inevitability.\x02\x03",
            "#0401044V#0200FFor example, was it this connection with\x01",
            "Heiyue that made the attacks against the\x01",
            "two gangs unavoidable?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87E7")

    label("loc_87E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_89F9")
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#0401045V#6P#0200FLloyd, if I may...\x02\x03",
            "#0402001VHave you considered the possibility that\x01",
            "Heiyue is the missing link?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x0)

    ChrTalk(
        0x101,
        "#0401046V#5P#0005FHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0401047V#6P#0305FYou sayin' that Heiyue are our\x01",
            "culprits? Not Revache?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0401048V#6P#0203FNo, I am still working under the\x01",
            "assumption that it was the mafia.\x02\x03",
            "#0401049V#0200FHowever, is it not possible for Heiyue\x01",
            "to be the connecting line Elie proposed?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89F9")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#0401050V#5P#0008F...Yeah. That would explain some things.\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x2)

    ChrTalk(
        0x102,
        "#0401051V#12P#0105FOh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401052V#6P#0300FWhat'cha thinkin', bud?\x02",
    )

    CloseMessageWindow()

    def lambda_8AE4():
        OP_95(0xFE, 12600, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8AE4)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#0401053V#0001F#5PWell, about that possibility Tio mentioned...\x02\x03",
            "#0401054VWhat do you think Revache would do if they\x01",
            "found out Heiyue was trying to establish a\x01",
            "foothold in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0401055V#6P#0305FWell, I imagine they'd look to expand\x01",
            "their combat capabilities.\x02\x03",
            "#0401056V#0303FRecruit more people and upgrade their\x01",
            "weaponry, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401057V#0003F#5PRevache should have no problems getting\x01",
            "new weapons, given their known smuggling\x01",
            "operations.\x02\x03",
            "#0401058V#0001FBut how do they go about recruiting people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401059V#6P#0305FGood question.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0401060V#12P#0108FNormally, you'd hire jaegers...\x02\x03",
            "#0401061V#0103FBut that's unlikely in Crossbell's case,\x01",
            "given the constant surveillance put on\x01",
            "us by neighboring countries.\x02\x03",
            "#0401062V#0101FSo long as the Non-Aggression Pact stands,\x01",
            "Erebonia and Calvard would never overlook\x01",
            "the involvement of jaegers.\x02\x03",
            "#0401063VThe two diet factions representing them\x01",
            "would likely react the exact same way, too...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0401064V#12P#0105FOh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0401065V#6P#0205FLloyd, could the mafia be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401066V#6P#0301F...lookin' to recruit the gang members?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401067V#0003F#5PHot-blooded and more or less disciplined.\x02\x03",
            "#0401068V#0001FI can't think of a more perfect pool of candidates\x01",
            "to beef up the mafia's presence in the city.\x02\x03",
            "#0401069VThen again, they can't just barge in and choose\x01",
            "whoever they like, now can they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0401070V#12P#0101FOf course not.\x02\x03",
            "#0401071VI mean, I could never see Wazy\x01",
            "cooperating with the mafia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0401072V#6P#0203FWald does not seem like the type to\x01",
            "bow down to authority, either.\x02\x03",
            "#0401073V#0201FHe is unlikely to agree to working under\x01",
            "the mafia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0401074V#6P#0308FSo, Revache realizes this and plots to weaken\x01",
            "the two gangs, intendin' to swoop in later and\x01",
            "bag the remaining members.\x02\x03",
            "#0401075V#0301FHell, that must be it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401076V#0012F#5PRemember, this is still nothing more\x01",
            "than a theory.\x02\x03",
            "#0401077V#0000FAll we've done is bring together the\x01",
            "facts and try to make sense of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401078V#6P#0309FAw! Look at you, bein' all modest!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0401079V#12P#0104FI think that your analysis of the situation\x01",
            "isn't too far off from the truth.\x02\x03",
            "#0401080V#0102FIt may only be a theory, but your reasoning\x01",
            "was sound and logical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0401081V#6P#0202FYou certainly proved that you acing the\x01",
            "detective exam was no fluke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401082V#0004F#5PHaha. Thanks.\x02\x03",
            "#0401083V#0000FIt's decided.\x02\x03",
            "#0401084VOur next move should be to explain our\x01",
            "theory to those two, don't you think?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0401085V#12P#0105F'Those two'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401086V#6P#0305FHey, you don't mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401087V#0003F#5PI do.\x02\x03",
            "#0401088VWald Wales and Wazy Hemisphere.\x02\x03",
            "#0401089V#0000FLeaders of the Saber Vipers and\x01",
            "the Testaments.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(26000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM("ed7100", "ed7000")
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(2000)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetScenarioFlags(0x43, 2)
    SetScenarioFlags(0x5C, 0)
    NewScene("c000B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_71B3 end

    def Function_19_96C3(): pass

    label("Function_19_96C3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    OP_68(12600, 2350, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    OP_68(12600, 1850, 5600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#1100053V#11P#0006FThe chief sure is late.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1100054V#5P#0001FIt's almost time for our regular\x01",
            "morning meeting to start, too.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Sleep(200)

    ChrTalk(
        0x102,
        (
            "#1100055V#0106FI really don't think we can begin\x01",
            "the meeting without him.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x1)
    Sleep(200)

    ChrTalk(
        0x104,
        (
            "#1100056V#6P#0303FI woulda slept in if I knew this was\x01",
            "how it was gonna roll...\x02\x03",
            "#1100057V#0302FDays like this are best spent wakin'\x01",
            "up at noon, and then hittin' up Barca\x01",
            "for some good times.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(200)

    ChrTalk(
        0x103,
        "#1100058V#5P#0211FTextbook example of a slacker.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 6000, 850, 10200, 90)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(
        0x8,
        "Man's Voice",
        "#1100059V#2PSorry I'm late.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x8, 0x8)
    OP_68(3000, 1850, 10200, 2000)
    SetChrPos(0x8, 3000, 850, 10200, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x103, 0x1)
    SetChrSubChip(0x104, 0x1)
    OP_6F(0x1)

    def lambda_9A7F():
        OP_96(0xFE, 0x3138, 0x352, 0x20D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9A7F)
    Sleep(3000)
    Fade(500)
    OP_68(12600, 1850, 6600, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        "#1100060V#2P#0000FMorning, Chief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100061V#4P#0100FGood morning. Do you want to go\x01",
            "ahead and start the meeting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100062V#5P#1003FNo need.\x02\x03",
            "#1100063V#1000FJust got a call from the department.\x02\x03",
            "#1100064VYou guys have been assigned a\x01",
            "special mission today. Congrats.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1100065V#2P#0005F'A special mission'...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100066V#6P#0301FSomethin' smells fishy about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100067V#6P#0200FIs it similar to the previous one?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100068V#5P#1004FI don't know the details.\x02\x03",
            "#1100069V#1002FJust head to the department.\x01",
            "Your client will be waiting for\x01",
            "you there.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(25500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetScenarioFlags(0x5C, 1)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_96C3 end

    def Function_20_9DE8(): pass

    label("Function_20_9DE8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    OP_68(12600, 1850, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    ClearChrFlags(0x18, 0x80)
    OP_78(0xB, 0x18)
    ClearMapObjFlags(0xB, 0x4)
    OP_49()
    SetChrPos(0x18, 12700, 1650, 5300, 0)
    OP_D3(0x18, 0x0, 0x15F90, 0x0, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis120.itp")
    Sleep(500)
    Sound(18, 0, 100, 0)
    UseItem(0x2D4, 0xFF)
    Sleep(500)
    PlayBGM("ed7110", 0)
    SetCameraDistance(25000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#1100207V#0001F#5PThis is bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100208V#0103F#11PSo it really is happening everywhere.\x02\x03",
            "#1100209V#0101FIt's strange the media hasn't reported\x01",
            "anything on it yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100210V#6P#0303FYeah, for sure.\x02\x03",
            "#1100211V#0301FThey don't exactly sound like your\x01",
            "average monster attacks, do they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100212V#6P#0200FDo we know whether or not these wolf-like\x01",
            "monsters are indigenous to Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100213V#5P#0003FIt's hard to say.\x02\x03",
            "#1100214V#0001FThey DID find paw prints at all the\x01",
            "different scenes.\x02\x03",
            "#1100215VAt this point, it's hard to deny that\x01",
            "they actually exist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100216V#0101F#11PThe Guardian Force still hasn't physically\x01",
            "seen the monsters, though, right?\x02\x03",
            "#1100217VThat's a little disconcerting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100218V#6P#0306FWell, we know one thing for sure.\x01",
            "They're pretty damn slick if they\x01",
            "managed to outsmart the CGF.\x02\x03",
            "#1100219V#0301FI mean, shouldn't they have hired\x01",
            "some kinda hunter to track them\x01",
            "down instead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100220V#6P#0203FProbably so.\x02\x03",
            "#1100221V#0200FI am not certain whether our chances of\x01",
            "solving this case are particularly high.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#1100222V#0105F#11PWhat's wrong, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100223V#6P#0300FDid that ace detective lightbulb of yours\x01",
            "start flickering again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100224V#5P#0004FI don't know if I'd put it like that, but...\x02\x03",
            "#1100225V#0000F...let's remember to tackle this like detectives.\x01",
            "If we approach the monster attacks like we would\x01",
            "any other investigation, we may find new clues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100226V#0105F#11PApproach this as detectives...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100227V#6P#0205FFor something a straightforward as\x01",
            "monster attacks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100228V#5P#0000FWell, yeah. And if we treat this series\x01",
            "of attacks as one solitary case...\x02\x03",
            "#1100229V...who would be our culprit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100230V#6P#0300FObviously those wolf-like monsters\x01",
            "the report mentioned, right?\x02\x03",
            "#1100231VAnd you know how wolves work.\x01",
            "They move in packs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100232V#5P#0003FBut with that in mind...\x02\x03",
            "#1100233V#0001F...what would the profile and motive\x01",
            "of the culprit be?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#1100234V#6P#0305FWell, uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100235V#0104F#11PNow I understand.\x02\x03",
            "#1100236V#0100FYou're trying to make us realize that we\x01",
            "can't answer those questions relying solely\x01",
            "on the reports we received.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100237V#5P#0003FExactly. More intelligent monsters usually\x01",
            "stay away from populated areas.\x02\x03",
            "#1100238VIf the motive was hunger, the hospital would\x01",
            "be the last place they would look for food.\x02\x03",
            "#1100239V#0000FThere has to be some truth that explains\x01",
            "their seemingly irrational behavior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100240V#6P#0300FHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100241V#6P#0204FThat is a valid point. And it is theoretically\x01",
            "sound as well, if I may add.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100242V#0100F#11PI suppose the objective of our investigation\x01",
            "has been decided, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100243V#5P#0003FI think so. First, we visit the affected areas\x01",
            "and gather information from eyewitnesses\x01",
            "and any potential victims.\x02\x03",
            "#1100244V#0000FThat should provide us with additional\x01",
            "insight into the reports, at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100245V#0104F#11PVery well.\x02\x03",
            "#1100246V#0100FEvery little clue and lead we can find will\x01",
            "go toward helping the Guardian Force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100247V#6P#0309FPhew, that's a relief!\x02\x03",
            "#1100248VAnd here I thought we'd be spending the day\x01",
            "blindly huntin' monsters in the mountains!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100249V#6P#0203FIn that case, Lloyd...\x02\x03",
            "#1100250V#0200FWhere do you suggest we head first?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    ChrTalk(
        0x101,
        "#1100251V#11P#0005FLet's see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#1100252V#11P#0000FHow about we start with Armorica Village,\x01",
            "the first area that was attacked?\x02\x03",
            "#1100253VConsidering the Armorica report was the most\x01",
            "detailed, maybe we'll be able to gather enough\x01",
            "clues to start building a profile of the monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100254V#0104F#11PThat sounds like a good place to start.\x02\x03",
            "#1100255V#0100FArmorica Village is northeast the city, right?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#1100256V#5P#0000FYeah. Taking the orbal bus near the east\x01",
            "exit is probably going to be our best bet.\x02\x03",
            "#1100257V#0003FAnd needless to say, this is our first mission\x01",
            "outside of the city.\x02\x03",
            "#1100258V#0001FWe don't know what we're heading into, so\x01",
            "let's make sure we leave prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100259V#6P#0300FYou said it, man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100260V#6P#0202FWe should also double-check the available\x01",
            "support requests, just to be safe.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(12000, 1850, 8700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrPos(0x1, 12000, 850, 8700, 270)
    SetChrPos(0x2, 12000, 850, 8700, 270)
    SetChrPos(0x3, 12000, 850, 8700, 270)
    SetChrPos(0x18, 25600, 1650, 9500, 0)
    SetChrFlags(0x18, 0x80)
    SetMapObjFlags(0xB, 0x4)
    SetScenarioFlags(0x60, 0)
    OP_65(0x1, 0x1)
    OP_29(0x3E, 0x1, 0x9)
    OP_29(0x3F, 0x4, 0x2)
    OP_29(0x3F, 0x1, 0x0)
    PlayBGM("ed7100", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_20_9DE8 end

    def Function_21_B131(): pass

    label("Function_21_B131")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05700.itc", 0x1E)
    LoadChrToIndex("chr/ch00800.itc", 0x1F)
    LoadChrToIndex("apl/ch50106.itc", 0x22)
    LoadChrToIndex("apl/ch50107.itc", 0x23)
    LoadChrToIndex("apl/ch50108.itc", 0x24)
    LoadChrToIndex("apl/ch50109.itc", 0x25)
    LoadChrToIndex("apl/ch50117.itc", 0x26)
    LoadChrToIndex("apl/ch50092.itc", 0x27)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis020.itp")
    CreatePortrait(1, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00500.itp")
    LoadEffect(0x0, "event\\eva05_00.eff")
    OP_68(3000, 700, 126000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 3000, 450, 126000, 180)
    SetChrChipByIndex(0x19, 0x27)
    SetChrSubChip(0x19, 0x12)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 2800, 850, 128500, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetMapObjFrame(0xFF, "r_huton", 0x0, 0x1)
    ClearMapObjFlags(0x10, 0x4)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#1200001V\x07\x0C",
            "#30WW-Wait a second!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7515", 0)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(800)
    SetMessageWindowPos(50, 170, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#1200002V\x07\x0C",
            "'I'm going on a trip'? You can't just say\x01",
            "that and immediately walk out the door!\x02\x03",
            "#1200003VWhere are you even going?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("Young Man")

    AnonymousTalk(
        0xFF,
        (
            "#1200004V\x07\x0C",
            "The Principality of Remiferia.\x02\x03",
            "#1200005VDon't worry, I should be back in a\x01",
            "month or two.\x02\x03",
            "#1200006VMight even be as short as two weeks,\x01",
            "depending on the situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#1200007V\x07\x0C",
            "Yeah, I get it, but...\x02\x03",
            "#1200008V...you're a CPD detective, aren't you?\x02\x03",
            "#1200009VIs it really okay for you to be out of the\x01",
            "state for that long?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("Young Man")

    AnonymousTalk(
        0xFF,
        (
            "#1200010V\x07\x0C",
            "Awww, what's with the long face?\x02\x03",
            "#1200011VYou gonna be depressed if your big\x01",
            "brother goes away for a bit?\x02\x03",
            "#1200012VC'mon, Lloyd. You get way too freaked\x01",
            "out when you're alone.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#1200013V\x07\x0C",
            "Why stop at two months? You can\x01",
            "leave for two years, for all I care!\x02\x03",
            "#1200014VI'm perfectly fine on my own, thanks!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("Young Man")

    AnonymousTalk(
        0xFF,
        (
            "#1200015V\x07\x0C",
            "Whoa, relax. I was just kidding.\x02\x03",
            "#1200016VY'see, the truth is...I'm not going\x01",
            "to Remiferia for fun and games.\x02\x03",
            "#1200017VThis is a top secret job, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#1200018V\x07\x0C",
            "Sounds fishy to me.\x02\x03",
            "#1200019VI mean, top secret? What kind of secrets\x01",
            "are we even talking about?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("Young Man")

    AnonymousTalk(
        0xFF,
        (
            "#1200020V\x07\x0C",
            "Hah! I knew you were going to ask that.\x02\x03",
            "#1200021VWell, I can't dive into specifics, but it's\x01",
            "actually a trip where I'm in charge of\x01",
            "escorting this cute little girl back home.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#1200022V\x07\x0C",
            "That's it...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("Young Man")

    AnonymousTalk(
        0xFF,
        (
            "#1200023V\x07\x0C",
            "The girl and I are escaping to Remiferia,\x01",
            "a beautiful northern country.\x02\x03",
            "#1200024VSo, tell me... Just how jealous are you?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#1200025V\x07\x0C",
            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("Young Man")

    AnonymousTalk(
        0xFF,
        (
            "#1200026V\x07\x0C",
            "Okay, okay. No more joking around.\x02\x03",
            "#1200027VI asked the neighbors to invite you\x01",
            "over for dinner while I'm away.\x02\x03",
            "#1200028VBreakfasts are on you, though!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#1200029V\x07\x0C",
            "I'm not a kid. I can cook my own\x01",
            "meals...\x02\x03",
            "#1200030VWait, that's beside the point!\x02\x03",
            "#1200031V'Cute little girl'? Just what exactly\x01",
            "are you planning, Guy?!\x02\x03",
            "#1200032VWhat are you going to do if Cecile\x01",
            "finds out about all this?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("Young Man")

    AnonymousTalk(
        0xFF,
        (
            "#1200033V\x07\x0C",
            "Hmm...\x02\x03",
            "#1200034VWhat does Cecile have to do\x01",
            "with anything?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#1200035V\x07\x0C",
            "What does she...? Argh, you're impossible!\x02\x03",
            "#1200036V(What could she possibly see in this\x01",
            "massive idiot?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("Young Man")

    AnonymousTalk(
        0xFF,
        (
            "#1200037V\x07\x0C",
            "...Well, okay, then.\x02\x03",
            "#1200038VFor your information, I've already\x01",
            "discussed this with her.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 170, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#1200039V\x07\x0C",
            "Wait, seriously?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("Young Man")

    AnonymousTalk(
        0xFF,
        (
            "#1200040V\x07\x0C",
            "Yeaaah, there seems to be a little\x01",
            "misunderstanding here, Lloyd.\x02\x03",
            "#1200041VEven though I call it a trip, it's\x01",
            "still very much police work.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0xBB8, 0x0)

    AnonymousTalk(
        0xFF,
        (
            "#1200042V\x07\x0C",
            "#40W#30AAnd the girl's #100Wonly #50Wnine years\x01",
            "old, y'know...\x07\x00\x02",
        )
    )

    Sleep(3000)
    OP_57(0x0)
    OP_5A()
    OP_CA(0x0, 0x0, 0x3)
    StopBGM(0xFA0)
    WaitBGM()
    SoundLoad(806)
    Sound(829, 0, 100, 0)
    Sleep(2000)
    SetCameraDistance(23500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#1200043V#5P...Mmm...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    OP_71(0x10, 0x0, 0x14, 0x0, 0x0)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x2)
    Sleep(150)
    SetChrSubChip(0x101, 0x3)
    Sleep(1000)
    SetChrSubChip(0x101, 0x4)
    Sleep(150)
    SetChrSubChip(0x101, 0x5)
    Sleep(1000)
    OP_79(0x10)
    SetChrSubChip(0x101, 0x7)
    Sleep(700)
    SetChrSubChip(0x101, 0x5)
    Sleep(100)
    SetChrSubChip(0x101, 0x6)
    Sleep(700)

    ChrTalk(
        0x101,
        (
            "#1200044V#5206F#5PA...dream?\x02\x03",
            "#1200045V#5208FTalk about nostalgic.\x02\x03",
            "#1200046VI must've been around 12 when that\x01",
            "happened...or was it 13?\x02\x03",
            "#1200047V#5205FAnd afterwards, I'm sure that--\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 1400, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 1000, 30, 125700, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_BF8D():
        OP_95(0xFE, 1000, 30, 128100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF8D)
    WaitChrThread(0x101, 1)

    def lambda_BFAB():
        OP_95(0xFE, 1700, 30, 128100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BFAB)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(500)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x1, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#1200048V#5201FLloyd, speaking.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7111", 0)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#1200049V\x07\x05",
            "Good. You're up.\x02\x03",
            "#1200050VHave you finished that report already?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#1200051V#5205FYes, sir.\x02\x03",
            "#1200052V#5200FYesterday's investigation is wrapped\x01",
            "up, more or less.\x02",
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
            "#1200053V\x07\x05",
            "Excellent.\x02\x03",
            "#1200054VNow, round up everyone and come to\x01",
            "my office.\x02\x03",
            "#1200055VYou have guests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#1200056V#5201F...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_CA(0x0, 0x1, 0x3)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_68(63800, 1000, 7900, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 62900, 0, 7900, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 64599, 0, 7900, 270)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 65600, 0, 7400, 270)
    SetChrPos(0x101, 59000, -1000, 3000, 90)
    SetChrPos(0x102, 59000, 0, 3400, 90)
    SetChrPos(0x103, 59000, 0, 3400, 90)
    SetChrPos(0x104, 59000, 0, 3400, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(811, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#1200057V#11PExcuse us, sir.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(64080, 1000, 7060, 4000)
    SetCameraDistance(22500, 4000)

    def lambda_C385():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C385)

    def lambda_C392():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_C392)

    def lambda_C39F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_C39F)
    Sound(103, 0, 100, 0)
    Sleep(200)
    SetChrPos(0x101, 59000, 0, 3400, 90)
    BeginChrThread(0x101, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 24)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 26)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 25)
    WaitChrThread(0x101, 3)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x103, 3)
    OP_6F(0x11)

    ChrTalk(
        0x101,
        "#1200058V#0005F#12PDeputy Commander Baelz?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200059V#0300F#12PMan, how did I know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#1200060V#5P#2002F#5PGood morning, you four.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x14,
        "Female Guardsman",
        "#1200061V#5P#0502FMorning, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200062V#6P#0104FIt's nice to see you, Deputy Commander.\x02\x03",
            "#1200063V#0102FOur guess as to who was visiting us\x01",
            "ended up being spot on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200064V#5P#1002F#5PShe stopped by not too long ago.\x02\x03",
            "#1200065VApparently, she wants to hear about\x01",
            "how your investigation is going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200066V#12P#0000FY-Yeah, of course...but isn't this on\x01",
            "a pretty short notice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200067V#6P#0105FWe still haven't quite finished our\x01",
            "investigation of Mainz yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200068V#5P#2006FI apologize, everyone. It wasn't my\x01",
            "intention to rush you.\x02\x03",
            "#1200069VThe situation, however, has changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200070V#0305F#12PWhat do ya mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200071V#5P#2001FUp until yesterday, the Guardian Force\x01",
            "was conducting regular patrols and\x01",
            "providing security to Mainz.\x02\x03",
            "#1200072VHowever, this morning, it was decided\x01",
            "that we're to issue a full withdrawal.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
        "#1200073V#12P#0001FYou're withdrawing the guardsmen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200074V#12P#0201FIt has only been three days since the\x01",
            "last monster sighting, has it not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200075V#5P#2003FCorrect. We had planned on providing\x01",
            "security for at least another week.\x02\x03",
            "#1200076V#2001FBut the order came directly from the\x01",
            "CGF commander. He claimed it was\x01",
            "a 'waste of resources'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200077V#6P#0101FHe thinks protecting innocent civilians\x01",
            "is a waste?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200078V#0308F#12PTch... I never liked that spineless\x01",
            "kiss-ass.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_CAA8():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CAA8)
    Sleep(50)

    def lambda_CAB8():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CAB8)
    Sleep(50)
    TurnDirection(0x103, 0x104, 500)

    ChrTalk(
        0x101,
        "#1200079V#5P#0005FYou know him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200080V#0303F#12POh, yeah. When I was serving at Bellguard Gate,\x01",
            "I saw him loads of times.\x02\x03",
            "#1200081V#0301FBasically, he's top dog of the Guardian Force and\x01",
            "buddy-buddy with some Imperial Faction big shot.\x02\x03",
            "#1200082VHe's more a fan of wining and dining instead than\x01",
            "he is doing his actual job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200083V#6P#0108FSo the rumors are true, after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200084V#6P#0201FHowever, wouldn't the CGF pulling out this early\x01",
            "present a problem? It would be too dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200085V#5P#2003FYes, precisely.\x02\x03",
            "#1200086V#2001FIf the attacks were limited to one location,\x01",
            "it might have been handed off to the guild...\x02\x03",
            "#1200087VBut unfortunately, the scale of the attacks\x01",
            "is too vast.\x02\x03",
            "#1200088VAs deputy commander of the Crossbell\x01",
            "Guardian Force, I cannot overlook this.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CDFD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CDFD)

    def lambda_CE0A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CE0A)

    def lambda_CE17():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CE17)
    WaitChrThread(0x103, 2)
    Sleep(300)

    NpcTalk(
        0x14,
        "Female Guardsman",
        (
            "#1200089V#5P#0506FThe real problem is that we weren't able\x01",
            "to neutralize the monsters before our\x01",
            "three week deadline.\x02\x03",
            "#1200090VAnd despite the attacks happening all\x01",
            "throughout Crossbell, the actual damages\x01",
            "weren't all that serious...\x02\x03",
            "#1200091V#0501FWith that as pretext, the commander gave\x01",
            "the order to cease all operations related to\x01",
            "the matter immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200092V#12P#0001FSo that's how it happened.\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        (
            "#1200093V#5P#2005FOh, how rude of me. I still haven't\x01",
            "introduced you yet, have I?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)

    def lambda_D050():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D050)

    def lambda_D05D():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D05D)

    def lambda_D06A():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D06A)
    Sleep(300)

    ChrTalk(
        0x13,
        (
            "#1200094V#5P#2004FThis is Sergeant Major Seeker.\x02\x03",
            "#1200095V#2002FShe's young, but also extremely\x01",
            "skilled in combat and a gifted driver.\x02\x03",
            "#1200096VShe serves as my aide-de-camp.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    Sound(1493, 255, 100, 0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1100)
    SetChrName("Female Guardsman")

    AnonymousTalk(
        0xFF,
        (
            "#1200097VI'm Noel Seeker. It's nice to officially\x01",
            "meet all of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    ChrTalk(
        0x101,
        "#1200098V#12P#0000FYeah, likewise.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1200099V#12P#0005FHold on... You said your last name was Seeker?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200100V#6P#0100FBy any chance, are you related to Fran,\x01",
            "one of the CPD receptionists?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#1200101V#5P#0509FI am! Fran's my little sister.\x02\x03",
            "#1200102V#0502FI heard that you've been\x01",
            "looking after her. Thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200103V#12P#0002FActually, I think you may have things\x01",
            "a little backwards there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200104V#0304F#12PHuh. So you're that sergeant major I heard so\x01",
            "much about...\x02\x03",
            "#1200105V#0300FSergeant Major Seeker, the young guardsman\x01",
            "who's become Tangram's shining beacon of hope.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    OP_0D()
    TurnDirection(0x14, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#1200106V#5P#0504FI wouldn't go that far. Besides, I've heard\x01",
            "about you, too, Randy.\x02\x03",
            "#1200107V#0500FThe Bellguard forces have had a lot to say.\x01",
            "It's nice to finally put a face to the stories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200108V#0309F#12PHaha. I'm flattered.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200109V#6P#0005FWhat kind of stories are we\x01",
            "talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200110V#6P#0211FPrimarily ones involving escapades with\x01",
            "women, I assume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200111V#0304F#12PYou got me there. The guys were always\x01",
            "jealous of my awesome skills with the ladies.\x01",
            "I mean, I would be, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x13,
        (
            "#1200112V#5P#2004F#5PI'll politely ask for you to leave\x01",
            "things at that, Orlando.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200113V#0306F#12P*gulp*\x02",
    )

    CloseMessageWindow()

    def lambda_D763():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D763)
    Sleep(50)

    def lambda_D773():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D773)
    Sleep(50)

    def lambda_D783():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D783)
    Sleep(50)

    def lambda_D793():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D793)
    Sleep(50)
    OP_93(0x14, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x13,
        (
            "#1200114V#5P#2001FNow you should be up to speed with\x01",
            "this unpleasant situation.\x02\x03",
            "#1200115VThe only factor that might break this\x01",
            "deadlock is your investigation...\x02\x03",
            "#1200116VTo be blunt, I'm grasping at straws here.\x01",
            "I need to know what you've found out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200157V#12P#0001FI didn't know things were this urgent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200118V#6P#0103FWell, we were about to submit our report\x01",
            "to the chief, anyway. Please allow us to\x01",
            "give you a short briefing as we do.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    OP_68(64080, 1000, 7060, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    Sleep(1000)
    SetCameraDistance(22500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x13,
        "#1200119V#5P#2005F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1200120V#5P#1003FHmm. That's that, then? Good job.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x13, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#1200121V#6P#1002FWell, Sonya? What do you think\x01",
            "of my rookies' abilities?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200122V#5P#2004FThey've exceeded my expectations.\x02\x03",
            "#1200123VThe legend of the divine wolves and\x01",
            "how the culprits appeared on the roof\x01",
            "of St. Ursula Medical College...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 400)
    Sleep(400)

    ChrTalk(
        0x13,
        "#1200124V#5P#2000FWhat do you make of all this, Seeker?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#1200125V#11P#0506FHonestly, I'm not really sure.\x02\x03",
            "#1200126V#0500FI guess a trained detective's observations\x01",
            "really ARE different from ours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200127V#5P#2000FIt's more than simply their observations,\x01",
            "Seeker. It's their entire way of thinking.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0xB4, 0x1F4)

    def lambda_DC8B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_DC8B)

    def lambda_DC98():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_DC98)
    Sleep(300)

    ChrTalk(
        0x13,
        (
            "#1200128V#5P#2004FI believe I've come to my decision.\x02\x03",
            "#1200129V#2001FI'll entrust the rest of the Mainz investigation\x01",
            "to the Special Support Section.\x02\x03",
            "#1200130VWith you four heading the operation, perhaps\x01",
            "new, unexpected leads may come to light.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200131V#12P#0005FWe intended to keep investigating,\x01",
            "but we'll keep what you said in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200132V#0301F#12PYou ain't tryin' to throw us under the\x01",
            "bus for ignoring the CGF commander's\x01",
            "orders, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200133V#5P#2004FIt's not within my jurisdiction to tell you\x01",
            "whether or not to abandon this case.\x02\x03",
            "#1200134V#2002FIf, however, we are able to get a solid\x01",
            "lead on the monsters, we could mobilize\x01",
            "immediately...\x02\x03",
            "#1200135VSurely you understand, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200136V#0302F#12PI hear ya loud and clear, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200137V#6P#0102FYou really are as capable as\x01",
            "everyone makes you out to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#1200138V#5P#0503FJust so you know, it seemed as if the\x01",
            "monsters were able to comprehend our\x01",
            "strategies and movements.\x02\x03",
            "#1200139VActing as a small team instead of a large\x01",
            "unit is probably smarter. With luck, you'll\x01",
            "even be able to uncover their weak spot.\x02\x03",
            "#1200140V#0500FI hope, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200141V#12P#0000FThanks for the heads-up.\x02\x03",
            "#1200142VIf possible, I'd like to head over to\x01",
            "the mining town ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200143V#5P#2000FYes, that would be for the best.\x02\x03",
            "#1200144VIf you uncover anything substantial,\x01",
            "contact my office at Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x13, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x13,
        (
            "#1200145V#11P#2000FSergei, would you mind saving that\x01",
            "talk for another day?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x13, 500)

    ChrTalk(
        0x8,
        (
            "#1200146V#6P#1003FNo complaints here.\x02\x03",
            "#1200147V#1000FDon't go taking any bad bets, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#1200148V#11P#2002FYou're one to talk.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    ChrTalk(
        0x13,
        "#1200149V#2000F#5PSeeker, we'll be off now.\x02",
    )

    CloseMessageWindow()
    Sound(1478, 255, 100, 0)

    NpcTalk(
        0x14,
        "Female Guardsman",
        "#1200150V#0502F#5PYes, ma'am!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x101, 500)
    Sleep(300)
    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    OP_0D()
    Sound(1498, 255, 100, 0)
    Sleep(1000)

    def lambda_E3BB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_E3BB)
    Sleep(150)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    OP_93(0x14, 0xE1, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(750)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)

    def lambda_E408():

        label("loc_E408")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_E408")

    QueueWorkItem2(0x8, 2, lambda_E408)
    BeginChrThread(0x13, 3, 0, 22)
    Sleep(500)
    BeginChrThread(0x14, 3, 0, 22)
    Sleep(300)

    def lambda_E42C():

        label("loc_E42C")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_E42C")

    QueueWorkItem2(0x101, 2, lambda_E42C)

    def lambda_E43E():

        label("loc_E43E")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_E43E")

    QueueWorkItem2(0x102, 2, lambda_E43E)

    def lambda_E450():

        label("loc_E450")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_E450")

    QueueWorkItem2(0x103, 2, lambda_E450)

    def lambda_E462():

        label("loc_E462")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_E462")

    QueueWorkItem2(0x104, 2, lambda_E462)
    Sleep(2700)
    Sound(103, 0, 100, 0)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x8, 0x2)
    StopBGM(0xBB8)
    OP_6F(0x1)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    Sleep(200)
    Sound(104, 0, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7110", 0)

    ChrTalk(
        0x101,
        (
            "#1200152V#5P#0001FShe looks like she's being worked to\x01",
            "the bone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200153V#5P#0103FYes, she does. She apparently oversaw the\x01",
            "entire withdrawal of her troops from Mainz\x01",
            "early this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200154V#5P#1003FShe sure did. Unfortunately, she's at the\x01",
            "mercy of an incompetent, sleazebag boss.\x02\x03",
            "#1200155V#1000FNot to mention, she can't neglect her vigil\x01",
            "over the Republic border.\x02\x03",
            "#1200156VBasically, it's her job to always draw the\x01",
            "short end of the stick.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E698():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E698)
    Sleep(50)

    def lambda_E6A8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E6A8)
    Sleep(50)

    def lambda_E6B8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E6B8)
    Sleep(50)

    def lambda_E6C8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E6C8)
    WaitChrThread(0x104, 2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1200117V#11P#0003FThat sounds awful.\x02\x03",
            "#1200158V#0005FBy the way, are you friends with the\x01",
            "deputy commander or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200159V#12P#0200FYou two did seem quite comfortable with\x01",
            "each other. Perhaps too comfortable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200160V#0303FWell, Deputy Commander Baelz was\x01",
            "the one who recommended me here\x01",
            "in the first place.\x02\x03",
            "#1200161V#0302FWhat kinda relationship are ya hidin'\x01",
            "from us, Boss?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        "#1200162V#5P#1003FCalm down. She's just an old friend.\x02",
    )

    CloseMessageWindow()
    Sound(852, 0, 100, 0)
    Sleep(1200)
    PlayEffect(0x0, 0x0, 0x8, 0x140, 0, 1300, 350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#1200163V#5P#1003F*sigh*\x02\x03",
            "#1200164V#1002FMore importantly, it's clear as day that\x01",
            "yesterday wore you guys out.\x02\x03",
            "#1200165VYou gotta head to Mainz, but are you\x01",
            "really planning to make that journey\x01",
            "on foot again?\x02",
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
            "#1200166V#11P#0006FDefinitely not. That really only\x01",
            "happened by chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200167V#12P#0100FWe intend to spare our feet from\x01",
            "blistering by taking the bus today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200168V#5P#1005FOh, that right?\x02\x03",
            "#1200169V#1004FHeh. And here I thought you were\x01",
            "following the bracers' example...\x02",
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
    Sleep(1000)

    ChrTalk(
        0x103,
        "#1200170V#12P#0205FHow does that correlate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200171V#0305FYeah, what'cha mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200172V#5P#1002FSure. It's sort of a tradition of theirs. As junior\x01",
            "bracers, they tend to tour the surrounding\x01",
            "area on foot.\x02\x03",
            "#1200173V#1004FThat way, they build up stamina, pile up loads\x01",
            "of combat experience, and, most importantly,\x01",
            "get the lay of the land.\x02\x03",
            "#1200174V#1002FThree birds, one stone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200175V#11P#0001FThat does seem pretty effective.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200176V#0301FThose guys seriously do that kinda\x01",
            "stuff? Willingly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200177V#12P#0201FPerhaps Estelle and Joshua were\x01",
            "doing a form of that when we met\x01",
            "them yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200178V#12P#0103FSo they intend to tour the entirety\x01",
            "of Crossbell on foot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200179V#5P#1002FHeh. Those two have got quite the\x01",
            "personal history, believe me.\x02\x03",
            "#1200180VI've even heard they led the effort\x01",
            "in fixing that fiasco that happened\x01",
            "in Liberl last year.\x02",
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
        "#1200181V#11P#0001FThe Liberl incident...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200182V#12P#0205FThat was when orbal power suddenly\x01",
            "shut down all across the country...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200183V#0301FNo kiddin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200184V#12P#0106FIf that's true...they must be pretty big\x01",
            "deals within the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200185V#5P#1002FEh, here in Crossbell, they're no more\x01",
            "than rookies, just like you.\x02\x03",
            "#1200186VAll you can do is work hard and pray\x01",
            "you can keep up with them.\x02\x03",
            "#1200187V#1003FIf you don't get results, you can bet\x01",
            "your ass the guild will snatch this\x01",
            "case out from under you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200188V#11P#0003FWe'll get to the bottom of it, sir.\x02",
    )

    CloseMessageWindow()

    def lambda_F1F6():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F1F6)
    Sleep(150)

    def lambda_F206():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F206)
    Sleep(50)

    def lambda_F216():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F216)
    Sleep(50)

    def lambda_F226():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F226)
    WaitChrThread(0x104, 2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1200189V#5P#0001FWe should head to Mainz once\x01",
            "we're ready.\x02\x03",
            "#1200190VIf we leave through the north exit,\x01",
            "the bus stop should be right ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200191V#6P#0101FLet's resupply and double-check our\x01",
            "gear while we have the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200192V#6P#0203FAs a precaution, I advise we check\x01",
            "the terminal before leaving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200193V#0300F#12PAll right! Let's get this show on the road.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22750, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    StopEffect(0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    OP_66(0x3, 0x1)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_68(64000, 1330, 6000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 64000, 0, 6000, 0)
    SetChrPos(0x1, 64000, 0, 6000, 0)
    SetChrPos(0x2, 64000, 0, 6000, 0)
    SetChrPos(0x3, 64000, 0, 6000, 0)
    SetMapObjFrame(0xFF, "r_huton", 0x1, 0x1)
    SetMapObjFlags(0x10, 0x4)
    SetScenarioFlags(0x64, 1)
    OP_29(0x40, 0x4, 0x2)
    OP_29(0x40, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F4B4")
    OP_29(0x8, 0x4, 0x40)
    Jump("loc_F4C6")

    label("loc_F4B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4C6")
    OP_29(0x8, 0x4, 0x40)

    label("loc_F4C6")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7103")
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_21_B131 end

    def Function_22_F4E2(): pass

    label("Function_22_F4E2")

    OP_92(0xFE, 0xF8D4, 0x1B58, 0x1F4)

    def lambda_F4F4():
        OP_95(0xFE, 63700, 0, 7300, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F4F4)
    WaitChrThread(0xFE, 1)

    def lambda_F512():
        OP_95(0xFE, 61600, 0, 6100, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F512)
    WaitChrThread(0xFE, 1)

    def lambda_F530():
        OP_95(0xFE, 61600, 0, 3300, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F530)
    WaitChrThread(0xFE, 1)

    def lambda_F54E():
        OP_95(0xFE, 59000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F54E)
    Sleep(500)

    def lambda_F56B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F56B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_F4E2 end

    def Function_23_F580(): pass

    label("Function_23_F580")


    def lambda_F585():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F585)

    def lambda_F59F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F59F)
    WaitChrThread(0x101, 1)

    def lambda_F5B4():
        OP_95(0xFE, 64099, 30, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F5B4)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_23_F580 end

    def Function_24_F5D5(): pass

    label("Function_24_F5D5")


    def lambda_F5DA():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F5DA)

    def lambda_F5F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F5F4)
    WaitChrThread(0x102, 1)

    def lambda_F609():
        OP_95(0xFE, 62800, 30, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F609)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_24_F5D5 end

    def Function_25_F62A(): pass

    label("Function_25_F62A")


    def lambda_F62F():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F62F)

    def lambda_F649():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F649)
    WaitChrThread(0x103, 1)

    def lambda_F65E():
        OP_95(0xFE, 62800, 30, 4400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F65E)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_25_F62A end

    def Function_26_F67F(): pass

    label("Function_26_F67F")


    def lambda_F684():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F684)

    def lambda_F69E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F69E)
    WaitChrThread(0x104, 1)

    def lambda_F6B3():
        OP_95(0xFE, 64099, 30, 4400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F6B3)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_26_F67F end

    def Function_27_F6D4(): pass

    label("Function_27_F6D4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02607.itc", 0x1E)
    LoadChrToIndex("chr/ch02608.itc", 0x1F)
    LoadChrToIndex("apl/ch50116.itc", 0x20)
    OP_68(900, 700, 6200, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 800, 0, 500, 0)
    SetChrPos(0x102, 800, 0, 500, 0)
    SetChrPos(0x103, 800, 0, 0, 0)
    SetChrPos(0x104, 800, 0, 0, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, 900, 0, 6200, 180)
    BeginChrThread(0xC, 3, 0, 0)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 800, 0, 0, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01200.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis153.itp")
    SetCameraDistance(24500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    OP_68(900, 700, 5200, 2000)
    SetCameraDistance(25500, 2000)

    def lambda_F8B8():
        OP_96(0xFE, 0xC8, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F8B8)

    def lambda_F8D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F8D2)
    Sleep(250)

    def lambda_F8E6():
        OP_96(0xFE, 0x514, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F8E6)

    def lambda_F900():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F900)
    Sleep(400)

    def lambda_F914():
        OP_96(0xFE, 0xC8, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F914)

    def lambda_F92E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F92E)
    Sleep(250)

    def lambda_F942():
        OP_96(0xFE, 0x514, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F942)

    def lambda_F95C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F95C)
    WaitChrThread(0x101, 1)
    Sleep(500)
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#1201038V#12P#0011FWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1201039V#0105FOh, my!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1201040V#0307FThe hell?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1201041V#4P#0205FWhy...?\x02",
    )

    CloseMessageWindow()

    def lambda_FA6C():
        OP_95(0xFE, 800, 0, 600, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FA6C)

    def lambda_FA86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_FA86)
    WaitChrThread(0x8, 1)

    def lambda_FA9B():
        OP_95(0xFE, 2850, 0, 2000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FA9B)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#1201042V#1011F#11PA friend of yours, I hope?\x02\x03",
            "#1201043V#1001FHe came in without knocking. Caused me\x01",
            "to subconsciously draw my gun, too.\x02\x03",
            "#1201044VBut, man, this guy is even lazier than me.\x01",
            "He just sprawled out on the ground there,\x01",
            "so I left him to his business.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FBCF():
        OP_95(0xFE, -900, 0, 3000, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FBCF)
    WaitChrThread(0x103, 1)
    OP_68(1470, 700, 5610, 1000)

    def lambda_FBFE():
        OP_95(0xFE, 600, 0, 4500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FBFE)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1201045V#11P#0205FHow did you... No...\x02\x03",
            "#1201046VWhy are you here?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xC, 0x3)
    Fade(250)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(300)
    Sound(2053, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("White Wolf")

    AnonymousTalk(
        0xFF,
        (
            "#1201047V#30WGrrrr...woof!\x02\x03",
            "#1201048VGrrrr...\x02",
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
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#1201049V#11P#0202FOhhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1201050V#12P#0005FTio? You catch any of that?\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1201051V#0204F#5PUm, let me see...\x02\x03",
            "#1201052V#0202F'I am known as Zeit.'\x02\x03",
            "#1201053V'I appreciate you clearing away the false\x01",
            "accusations against my brethren and I.'\x02\x03",
            "#1201054V#0204FSomething along those lines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1201055V#12P#0002FSo his name is Zeit...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1201056V#0102FH-He came to thank us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1201057V#0309FM-Maybe so, but this guy still sounds\x01",
            "like a pompous ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1201058V#5414F#5P#30WGrrr...\x02\x03",
            "#1201059VGrrrrrr...\x02\x03",
            "#1201071V#5413FGrrr...woof!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x0, 0x1F4)

    ChrTalk(
        0x103,
        "#1201061V#11P#0205FReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1201062V#12P#0001FWhat is it, Tio?\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1201063V#0208FHow do I put this?\x02\x03",
            "#1201064V#0203F'Make no mistake, you four are\x01",
            "still young and unreliable.'\x02\x03",
            "#1201065V'I shall lend you a paw every now\x01",
            "and then, out of pure necessity.'\x02\x03",
            "#1201066V'But only when I feel like it.'\x02",
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#1201067V#12P#0011FYou'll do WHAT?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1201068V#0105FHelp...from a wolf?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1201069V#0307FWhoa, whoa, whoa! Can we\x01",
            "back up a minute?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1201070V#5414F#5P#30WWoof.\x02\x03",
            "#1201060V#5412FGrrr...woof!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1201072V#0204F#5P'There is no need for concern.'\x02\x03",
            "#1201073V'I left the pack to a subordinate,\x01",
            "so they are in capable paws.'\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#1201074V#12P#0012FTh-That's not really the issue here!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)

    def lambda_10316():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_10316)
    Sound(848, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(1100)
    SetChrSubChip(0xC, 0x2)
    Sleep(130)
    SetChrSubChip(0xC, 0x3)
    Sleep(130)
    SetChrSubChip(0xC, 0x4)
    Sleep(130)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_63(0xC, 0x1F4, 1200, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1600)

    ChrTalk(
        0x8,
        (
            "#1201075V#1004F#11PHeh. A legendary divine wolf, eh?\x02\x03",
            "#1201076V#1002FCongrats. You guys just won yourselves\x01",
            "one hell of an ally.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10470():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10470)
    Sleep(50)

    def lambda_10480():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10480)
    Sleep(50)

    def lambda_10490():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10490)
    Sleep(50)

    def lambda_104A0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_104A0)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x101,
        "#1201077V#6P#0011FChief, you can't be serious...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1201078V#1002F#11PFor the time being, I'll just keep\x01",
            "telling myself he's a police dog.\x02\x03",
            "#1201079VBut, listen, this big guy is your\x01",
            "responsibility. Not mine.\x02\x03",
            "#1201080V#1004FAnd with that settled, I'm off to bed.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 28)
    Sleep(500)

    def lambda_105CA():

        label("loc_105CA")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_105CA")

    QueueWorkItem2(0x101, 2, lambda_105CA)

    def lambda_105DC():

        label("loc_105DC")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_105DC")

    QueueWorkItem2(0x102, 2, lambda_105DC)

    def lambda_105EE():

        label("loc_105EE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_105EE")

    QueueWorkItem2(0x103, 2, lambda_105EE)

    def lambda_10600():

        label("loc_10600")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_10600")

    QueueWorkItem2(0x104, 2, lambda_10600)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x101,
        "#1201081V#12P#0011FW-Wait a second, Chief!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    ChrTalk(
        0x104,
        "#1201082V#0301FJust our luck...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1201083V#0106F*sigh* Is this really okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1201084V#0204FI agree with the chief's decision. He will\x01",
            "prove to be an invaluable member of the\x01",
            "Special Support Section.\x02\x03",
            "#1201085V#0202FBesides, his fluffy white tuft of fur\x01",
            "is really cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1201086V#0109FY-Yes. It's incredibly adorable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1201087V#0302FWell, I s'pose we'll see how this plays\x01",
            "out. Might be useful for when we're in\x01",
            "a pinch, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1201088V#6P#0006F*sigh* Maybe you guys are right.\x02\x03",
            "#1201089V#0000FIf we just leave him like that, he'll look\x01",
            "like a stray. Maybe we should get him\x01",
            "a collar...\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(25000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x1388)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_29(0x3F, 0x4, 0x10)
    OP_29(0x40, 0x4, 0x10)
    OP_29(0x40, 0x4, 0x20)
    SubItemNumber(0x2D4, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10970")
    OP_29(0x5, 0x4, 0x40)
    Jump("loc_10982")

    label("loc_10970")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10982")
    OP_29(0x5, 0x4, 0x40)

    label("loc_10982")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109A0")
    OP_29(0x6, 0x4, 0x40)
    Jump("loc_109B2")

    label("loc_109A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109B2")
    OP_29(0x6, 0x4, 0x40)

    label("loc_109B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109D5")
    OP_29(0x7, 0x4, 0x40)
    SubItemNumber(0x35B, 1)
    Jump("loc_109E7")

    label("loc_109D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109E7")
    OP_29(0x7, 0x4, 0x40)

    label("loc_109E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A05")
    OP_29(0x9, 0x4, 0x40)
    Jump("loc_10A17")

    label("loc_10A05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A17")
    OP_29(0x9, 0x4, 0x40)

    label("loc_10A17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A35")
    OP_29(0xA, 0x4, 0x40)
    Jump("loc_10A47")

    label("loc_10A35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A47")
    OP_29(0xA, 0x4, 0x40)

    label("loc_10A47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xB, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A59")
    OP_29(0xB, 0x4, 0x40)

    label("loc_10A59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A77")
    OP_29(0xC, 0x4, 0x40)
    Jump("loc_10A89")

    label("loc_10A77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A89")
    OP_29(0xC, 0x4, 0x40)

    label("loc_10A89")

    SubItemNumber(0x2D5, 1)
    SubItemNumber(0x2D6, 1)
    SubItemNumber(0x2D7, 1)
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_DE(0x25, 0x0)
    OP_DE(0x1E, 0x0)
    OP_DE(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    OP_E3(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("c050B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_F6D4 end

    def Function_28_10B67(): pass

    label("Function_28_10B67")

    ClearChrFlags(0x8, 0x4)

    def lambda_10B71():
        OP_95(0xFE, 2600, 850, 9000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10B71)
    WaitChrThread(0x8, 1)

    def lambda_10B8F():
        OP_95(0xFE, 1300, 850, 10300, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10B8F)
    WaitChrThread(0x8, 1)

    def lambda_10BAD():
        OP_95(0xFE, 1300, 2650, 13800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10BAD)
    Sleep(1500)

    def lambda_10BCA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_10BCA)
    WaitChrThread(0x8, 1)
    Return()

    # Function_28_10B67 end

    def Function_29_10BDB(): pass

    label("Function_29_10BDB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch50090.itc", 0x20)
    LoadChrToIndex("apl/ch50092.itc", 0x21)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis113.itp")
    OP_68(500, 1100, 2500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 1000, 0, 0, 0)
    SetChrPos(0x102, 11100, 870, 5700, 90)
    SetChrPos(0x103, 12700, 870, 8200, 180)
    SetChrPos(0x104, 1000, 0, 0, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0xA)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1400, 6600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrSubChip(0x1A, 0xC)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13400, 1300, 6600, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0xA)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12400, 1400, 6600, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x20)
    SetChrSubChip(0x1C, 0xC)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12000, 1300, 6600, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0xA)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13000, 1400, 4600, 0)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0xC)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 13400, 1300, 4600, 0)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0xA)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 12400, 1400, 4600, 0)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0xC)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 12000, 1300, 4600, 0)
    SetChrChipByIndex(0x21, 0x20)
    SetChrSubChip(0x21, 0x7)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 12700, 1400, 5500, 0)
    SetCameraDistance(25000, 2500)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_10E03():
        OP_96(0xFE, 0x1F4, 0x0, 0x834, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10E03)

    def lambda_10E1D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10E1D)
    Sleep(700)

    def lambda_10E31():
        OP_96(0xFE, 0x5DC, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10E31)

    def lambda_10E4B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10E4B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#2100189V#0000F#5PWe're back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100190V#0300F#11PHome, sweet home.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x10E, 0x1F4)

    NpcTalk(
        0x102,
        "Elie's Voice",
        "#2100191V#3PHey, you two.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_10F0D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10F0D)
    Sleep(50)

    def lambda_10F1D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10F1D)
    OP_68(11100, 1950, 5700, 2000)
    MoveCamera(45, 19, 0, 2000)
    OP_6F(0x41)

    ChrTalk(
        0x101,
        "#2100192V#0005F#2POh, you guys made it back before us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100193V#11P#0104FWell, all we did was sort a few documents\x01",
            "down at headquarters.\x02\x03",
            "#2100194V#0102FTio and I even had time to make a\x01",
            "lovely lunch afterwards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100195V#0302F#2POooh, you make enough for four?\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#2100196V#0202F#5PIf you are okay with simple pasta and\x01",
            "salad, we did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100197V#0009F#9PSounds delicious. Thanks for the\x01",
            "meal, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100198V#11P#0109FOf course. Go wash your hands,\x01",
            "and I'll set the table for you.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(12600, 1850, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    Sleep(500)
    SetCameraDistance(25000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x103,
        (
            "#2100199V#6P#0205FOh, that reminds me...\x02\x03",
            "#2100200V#0200FLloyd, Randy. You assisted with traffic\x01",
            "control, correct? How did it go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100201V#11P#0006FIt definitely was harder than expected.\x02\x03",
            "#2100202V#0000FWe ended up having to move every\x01",
            "illegally parked car to the designated\x01",
            "area, all by ourselves.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(200)

    ChrTalk(
        0x104,
        (
            "#2100203V#6P#0300FBoy, the Entertainment District was\x01",
            "chock full of 'em.\x02\x03",
            "#2100204VThe whole place is buzzing about the new\x01",
            "show that got announced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100205V#0104F#11PNow that you mention it, Arc en Ciel has\x01",
            "been the talk of the town lately.\x02\x03",
            "#2100206V#0100FAren't they debuting their new performance\x01",
            "next month?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(200)

    ChrTalk(
        0x104,
        (
            "#2100207V#6P#0300FYep. 'Golden Sun, Silver Moon.'\x02\x03",
            "#2100208V#0306FI wanted to pick up some tickets for the\x01",
            "opener, but the damn things are already\x01",
            "sold out!\x02\x03",
            "#2100209VI had to settle for B section tickets for a\x01",
            "show two months from now.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#2100210V#6P#0205FIs Arc en Ciel really that popular?\x02\x03",
            "#2100211V#0203FI am aware of how famous the lead star,\x01",
            "Ilya Platiere, is, but aside from that...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#2100212V#5P#0003FYou know, I think I actually saw an\x01",
            "Arc en Ciel show a long time ago...\x02\x03",
            "#2100213V#0000FI've never seen one starring Ilya, though.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(200)

    ChrTalk(
        0x104,
        (
            "#2100214V#6P#0306FAnd to think you're supposed to be our leader...\x02\x03",
            "#2100215V#0301FThere's two kinds of people in this world:\x02\x03",
            "#2100216V#0304FThose who've seen an Ilya Platiere show,\x01",
            "and those who haven't. Your daily wisdom,\x01",
            "by Randy Orlando.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100217V#5P#0012FYeah, yeah, all right.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2100218V#0102FHeehee. She really is amazing, though.\x02\x03",
            "#2100219V#0104FOnce you see her perform, it's almost as\x01",
            "if she takes hold of your beating heart\x01",
            "and refuses to let go.\x02\x03",
            "#2100220V#0100FIf there really are legitimate geniuses out\x01",
            "there, Ilya Platiere is no doubt one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100221V#5P#0005FThat's some pretty high praise, Elie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100222V#6P#0202FConsider my interest piqued.\x02\x03",
            "#2100223V#0206FOn another note, I have been curious as to\x01",
            "why we have had so many requests lately...\x02\x03",
            "#2100224V#0200FCould Arc en Ciel be a part of that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100225V#0106FWell, the Anniversary Festival and debut\x01",
            "of Arc en Ciel's new show are scheduled\x01",
            "to overlap, after all.\x02\x03",
            "#2100226V#0100FThe CPD is bound to get busier than\x01",
            "other years with factors like that in play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100227V#6P#0306FEither way, we're mainly takin' care of those\x01",
            "odd jobs and requests no one down at the\x01",
            "department wants to deal with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100228V#5P#0012FMore or less, yeah.\x02\x03",
            "#2100229V#0000FBut still, you can't say we haven't been\x01",
            "getting more important jobs compared\x01",
            "to when we first started out.\x02\x03",
            "#2100230VEven the Crossbell Times hasn't written\x01",
            "another sarcastic hit piece on us again.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#2100231V#6P#0203FIt does not stop them from comparing\x01",
            "us to the bracers, though.\x02\x03",
            "#2100232V#0211FMore specifically, Estelle and Joshua...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#2100233V#5P#0006F*sigh* Yeah, I know.\x02\x03",
            "#2100234V#0001FHow can just two bracers accomplish\x01",
            "so much?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100235V#0108FPerhaps they're so efficient because\x01",
            "they're coordinating with other bracers.\x02\x03",
            "#2100236V#0106FThere's four of us, but we don't have\x01",
            "the luxury of requesting backup from\x01",
            "the rest of the force...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100237V#6P#0303FPardon me for judging a book by its\x01",
            "cover, but I bet Joshua is the key\x01",
            "behind the duo.\x02\x03",
            "#2100238VI've never seen a guy so efficient at\x01",
            "supporting someone who loves to run\x01",
            "into stuff full-speed like Estelle.\x02\x03",
            "#2100239V#0301FActually, it's rare to see a pair so in\x01",
            "sync with each other, whether in\x01",
            "combat or regular bracer work.\x02\x03",
            "#2100240VI can only imagine how much\x01",
            "they've been through together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100241V#6P#0206FYes, I would say we are still lacking\x01",
            "in the experience department.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#2100242V#5P#0012FC-C'mon, guys. We've come a long way.\x02\x03",
            "#2100243V#0000FWe even earned ourselves a reliable\x01",
            "police dog along the way.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#2100244V#11P#0005FSpeaking of Zeit, where IS he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100245V#0105FI don't think I've seen him today...\x02\x03",
            "#2100246V#0100FAll I know is that he spent all of yesterday\x01",
            "on the roof sunbathing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100247V#6P#0306FYou know, it's great when he chows\x01",
            "down on monsters for us...\x02\x03",
            "#2100248V#0300F...but what does he do to pass the time?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(200)

    ChrTalk(
        0x103,
        (
            "#2100249V#6P#0204FAs you can tell, he is a very proud wolf.\x02\x03",
            "#2100250VTo be honest, I'm surprised he decided\x01",
            "to comply with our rules in the first place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100251V#11P#0006FI mean, he's registered as a police dog.\x01",
            "Can you blame me for wanting to set\x01",
            "some ground rules?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2100252V#5P#0000FAt first, I thought the locals would scream\x01",
            "when they saw a massive wolf like him out\x01",
            "in public...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100253V#6P#0302FBut who woulda thought he'd end up savin'\x01",
            "a kid from a car wreck?\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x32, 0xBB8)
    MiniGame(0x17, 0xBB8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(3000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)

    AnonymousTalk(
        0x102,
        (
            "#2100254V#0103FA truck lost control of its steering and\x01",
            "smashed into the side of a fence...\x02\x03",
            "#2100255V#0102FWe wondered what that sound was, but\x01",
            "had no idea it was that dangerous.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#2100256V#0004FYeah, good thing Zeit was nearby.\x01",
            "The car almost slammed into Ryu\x01",
            "after he ran outside.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#2100257V#0309FHey, ya think Zeit would give Arios\x01",
            "a run for his money?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#2100258V#0202FYes, and I would bet on Zeit every time.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2100259V#0104FSince that accident, he's become\x01",
            "quite a celebrity on West Street.\x02\x03",
            "#2100260V#0102FNot to mention, Ryu and the other kids have\x01",
            "become especially attached to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100261V#5P#0004FHaha. Well, I can't blame them.\x02\x03",
            "#2100262V#0000FStill, we can't use Zeit's popularity as a\x01",
            "crutch.\x02\x03",
            "#2100263VWe have to earn the acceptance of the\x01",
            "citizenry with our own efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100264V#6P#0204FI concur. We cannot put it all on Zeit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100265V#6P#0300FWon't be a walk in the park, y'know. But\x01",
            "anyway, how 'bout we spend the rest of\x01",
            "the day finishing up support requests?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x2, 0xAC)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio learned the special craft \x07\x02",
            "[Summon Zeit]\x07\x05",
            "!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When used in battle, Zeit will appear\x01",
            "as a support character on the AT bar!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There may be times when this craft\x01",
            "cannot be used, however.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x5A, 2)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
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
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetChrPos(0x0, 13820, 850, 9650, 270)
    SetChrPos(0x1, 13820, 850, 9650, 270)
    SetChrPos(0x2, 13820, 850, 9650, 270)
    SetChrPos(0x3, 13820, 850, 9650, 270)
    SetScenarioFlags(0x80, 0)
    OP_29(0x40, 0x1, 0xD)
    OP_29(0x41, 0x4, 0x2)
    OP_29(0x41, 0x1, 0x0)
    ModifyEventFlags(1, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_29_10BDB end

    def Function_30_12BD1(): pass

    label("Function_30_12BD1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05200.itc", 0x1E)
    LoadChrToIndex("chr/ch05202.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00102.itc", 0x21)
    LoadChrToIndex("apl/ch50090.itc", 0x22)
    LoadChrToIndex("apl/ch50091.itc", 0x23)
    OP_68(1000, 900, 2800, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 500, 0, 1800, 0)
    SetChrPos(0x102, 1500, 0, 1800, 0)
    SetChrPos(0x103, 500, 0, 700, 0)
    SetChrPos(0x104, 1500, 0, 700, 0)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 3000, 0, 4700, 90)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01800.itp")
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_12D29():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12D29)
    Sleep(50)

    def lambda_12D39():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12D39)
    Sleep(50)

    def lambda_12D49():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_12D49)
    Sleep(50)

    def lambda_12D59():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12D59)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        "#2100293V#6P#0005FOh, uh, hello there...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100294V#6P#0100FIt looks like she was one step ahead of us.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x15, 0x101, 500)
    Sound(1635, 255, 100, 0)

    NpcTalk(
        0x15,
        "Purple-Haired Girl",
        "#2100295V#5POh? O-Oh!\x02",
    )

    CloseMessageWindow()
    OP_68(620, 1000, 2850, 1500)
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_12E54():
        OP_95(0xFE, 880, 0, 4250, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_12E54)

    def lambda_12E6E():

        label("loc_12E6E")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_12E6E")

    QueueWorkItem2(0x101, 2, lambda_12E6E)

    def lambda_12E80():

        label("loc_12E80")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_12E80")

    QueueWorkItem2(0x102, 2, lambda_12E80)

    def lambda_12E92():

        label("loc_12E92")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_12E92")

    QueueWorkItem2(0x103, 2, lambda_12E92)

    def lambda_12EA4():

        label("loc_12EA4")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_12EA4")

    QueueWorkItem2(0x104, 2, lambda_12EA4)
    WaitChrThread(0x15, 1)
    TurnDirection(0x15, 0x101, 500)
    OP_6F(0x1)

    NpcTalk(
        0x15,
        "Purple-Haired Girl",
        (
            "#2100296V#1805F#5PI-I'm so sorry!\x02\x03",
            "#2100297V#1803FIt was unlocked, so I let myself in.\x01",
            "I swear I didn't know you were\x01",
            "gone...\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    ChrTalk(
        0x101,
        (
            "#2100298V#12P#0004FNo, don't worry about it. We already\x01",
            "knew you were coming.\x02\x03",
            "#2100299V#0002FWelcome to the Special Support Section.\x01",
            "You were looking for some advice, right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Purple-Haired Girl",
        (
            "#2100300V#1802F#5PYes, exactly. I didn't know who else to\x01",
            "turn to.\x02",
        )
    )

    CloseMessageWindow()
    Sound(1636, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1000)
    SetChrName("Purple-Haired Girl")

    AnonymousTalk(
        0xFF,
        (
            "#2100302VUm, my name is Rixia Mao.\x02\x03",
            "#2100303VI-I just want to go ahead and thank\x01",
            "you! This means the world to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
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
    SetMessageWindowPos(14, 80, -1, -1)

    AnonymousTalk(
        0x101,
        "#2100304V#12P#0005F(Wh-Whoa...)\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 20, -1, -1)

    AnonymousTalk(
        0x104,
        "#2100305V#0301F(Get a grip, man.)\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 200, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#2100306V#0205F#12P(How is it humanly possible for\x01",
            "someone to be THIS pretty?)\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 200, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#2100307V#0106F(*sigh* Do you have to make your\x01",
            "ogling so...obvious?)\x02\x03",
            "#2100308V#0111F(L l o y d?)\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 80, -1, -1)

    AnonymousTalk(
        0x101,
        "#2100309V#12P#0011F(Huh?)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#2100310V#12P#0003FR-Right. Why don't you take a\x01",
            "seat, Miss Mao?\x02\x03",
            "#2100311V#0000FLet's hear this problem of yours.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x9C4)
    WaitBGM()
    ClearMapFlags(0x10000000)
    Call(0, 32)
    Return()

    # Function_30_12BD1 end

    def Function_31_133D7(): pass

    label("Function_31_133D7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05200.itc", 0x1E)
    LoadChrToIndex("chr/ch05202.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00102.itc", 0x21)
    LoadChrToIndex("apl/ch50090.itc", 0x22)
    LoadChrToIndex("apl/ch50091.itc", 0x23)
    OP_68(1700, 1200, 7000, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 1900, 850, 9900, 180)
    SetChrPos(0x102, 700, 850, 9900, 180)
    SetChrPos(0x103, 700, 850, 11100, 180)
    SetChrPos(0x104, 1900, 850, 11100, 180)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 2700, 0, 3200, 90)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01800.itp")
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2100293V#0005F#6POh, uh, hello there...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100294V#0100FIt looks like she was one step ahead of us.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x15, 0x101, 500)
    Sound(1635, 255, 100, 0)

    NpcTalk(
        0x15,
        "Purple-Haired Girl",
        "#2100295V#2PO-Oh!\x02",
    )

    CloseMessageWindow()
    OP_68(900, 1850, 7450, 1500)
    SetCameraDistance(26000, 1500)
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_1361B():
        OP_95(0xFE, 1150, 0, 6330, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1361B)

    def lambda_13635():
        OP_96(0xFE, 0x76C, 0x352, 0x20D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13635)
    Sleep(50)

    def lambda_13652():
        OP_96(0xFE, 0x2BC, 0x352, 0x20D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13652)
    Sleep(100)

    def lambda_1366F():
        OP_96(0xFE, 0x76C, 0x352, 0x2580, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1366F)
    Sleep(50)

    def lambda_1368C():
        OP_96(0xFE, 0x2BC, 0x352, 0x2580, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1368C)
    WaitChrThread(0x15, 1)
    TurnDirection(0x15, 0x101, 500)
    OP_6F(0x1)

    NpcTalk(
        0x15,
        "Purple-Haired Girl",
        (
            "#2100296V#1805F#2PI-I'm so sorry!\x02\x03",
            "#2100297V#1806FIt was unlocked, so I let myself in.\x01",
            "I swear I didn't know you were\x01",
            "gone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100298V#5P#0004FNo, don't worry about it. We already\x01",
            "knew you were coming.\x02\x03",
            "#2100299V#0002FWelcome to the Special Support Section.\x01",
            "You were looking for advice, right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Purple-Haired Girl",
        (
            "#2100300V#2P#1802FYes, exactly. I didn't know who else to\x01",
            "turn to.\x02",
        )
    )

    CloseMessageWindow()
    Sound(1636, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1000)
    SetChrName("Purple-Haired Girl")

    AnonymousTalk(
        0xFF,
        (
            "#2100302VUm, my name is Rixia Mao.\x02\x03",
            "#2100303VI-I just want to go ahead and thank\x01",
            "you! This means the world to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
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
    SetMessageWindowPos(14, 80, -1, -1)

    AnonymousTalk(
        0x101,
        "#2100304V#12P#0005F(Wh-Whoa...)\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 20, -1, -1)

    AnonymousTalk(
        0x104,
        "#2100305V#0301F(Get a grip, man.)\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 200, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#2100306V#0205F#12P(How is it humanly possible for\x01",
            "someone to be THIS pretty?)\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 200, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#2100307V#0106F(*sigh* Do you have to make your\x01",
            "ogling so...obvious?)\x02\x03",
            "#2100308V#0111F(L l o y d?)\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 80, -1, -1)

    AnonymousTalk(
        0x101,
        "#2100309V#12P#0011F(Huh?)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#2100310V#0003F#5PR-Right. Why don't you take a\x01",
            "seat, Miss Mao?\x02\x03",
            "#2100311V#0000FLet's hear this problem of yours.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(25500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x9C4)
    WaitBGM()
    Call(0, 32)
    Return()

    # Function_31_133D7 end

    def Function_32_13BAB(): pass

    label("Function_32_13BAB")

    FadeToDark(0, 0, -1)
    OP_68(5500, 950, 4300, 0)
    MoveCamera(43, 19, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 6050, 130, 6250, 180)
    SetChrPos(0x102, 4600, 130, 2200, 0)
    SetChrPos(0x103, 5500, 130, 2200, 0)
    SetChrPos(0x104, 6400, 130, 2200, 0)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 4900, 130, 6250, 180)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x19)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 4900, 280, 4600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x1A)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 5500, 330, 4300, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        "#2100312V#0013FA threat letter?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    SetCameraDistance(23000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x15,
        (
            "#2100313V#1P#1803FYes, it arrived exactly one week ago.\x02\x03",
            "#2100314VWhen Ilya checked her mail, she found\x01",
            "a letter with no return address...\x02\x03",
            "#2100315V#1805FOh, sorry, Ilya Platiere is--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100316V#0303FArc en Ciel's one and only Fervent Dancer!\x02\x03",
            "#2100317V#0301FThe continent-renowned actress who's recently\x01",
            "taken the world by storm!\x02\x03",
            "#2100318V#0309FOh, hell yes! Who would've thought\x01",
            "that we'd get a request involving\x01",
            "Ilya freakin' Platiere?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x103,
        (
            "#2100319V#12P#0203FI know you are excited, Randy, but\x01",
            "please try to control yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100320V#11P#0003FI mean, I know who she is, given\x01",
            "she's a celebrity and all...\x02\x03",
            "#2100321V#0001F...but a threat letter to her? Really?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#2100322V#1P#1803FApparently. She keeps claiming it's\x01",
            "just a dumb prank, but I'm not so sure.\x02\x03",
            "#2100323VIts contents are way too eerie for it to\x01",
            "be a mere prank.\x02\x03",
            "#2100324V#1801FI asked the troupe leader about it, and\x01",
            "he advised me to contact the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100325V#6P#0101FIf you don't mind me asking, who's in\x01",
            "possession of the threat letter now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#2100326V#1P#1806FUm, Ilya should still have it on her.\x02\x03",
            "#2100327VLuckily, I managed to convince her not\x01",
            "to immediately throw it in the trash...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100328V#11P#0003FA wise move. If she has it, we should\x01",
            "ask Ilya if we can inspect the letter.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#2100329V#11P#0005FBy the way, Miss Mao...\x02\x03",
            "#2100330V#0000FI'm assuming you must be related\x01",
            "to Arc en Ciel in some way?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    Sleep(300)

    ChrTalk(
        0x15,
        (
            "#2100331V#1P#1802FAh, yes. I'm one of the other actresses.\x02\x03",
            "#2100332V#1809FI'm just a beginner, though. Nothing\x01",
            "compared to Ilya herself.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#2100333V#0305F#4SWait a damn minute!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x15, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)

    ChrTalk(
        0x101,
        "#2100334V#5P#0011FWh-What's your problem, Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100335V#0301FYour face! I saw it in the front-page\x01",
            "feature about Arc en Ciel's new show!\x02\x03",
            "#2100336V#0303FYou're the co-star that plays the Moon\x01",
            "Princess, the ultimate complement to Ilya's\x01",
            "Sun Princess!\x02\x03",
            "#2100337V#0302FThe high-profile, up-and-coming actress,\x01",
            "scooped up by Ilya Platiere and made\x01",
            "famous in the blink of an eye, Rixia Mao!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "#2100338V#1P#1805FN-No, I wouldn't really call myself famous...\x02\x03",
            "#2100339V#1806FAll I do is stumble around and get in the\x01",
            "others' way...\x02\x03",
            "#2100340V#1808FTruth be told, I'm still not sure if\x01",
            "I'm ready for my debut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100341V#6P#0109FNo need to be so modest, Miss Mao.\x02\x03",
            "#2100342V#0102FBeing recruited by Arc en Ciel is an\x01",
            "incredible accomplishment! You should\x01",
            "be proud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#2100343V#1P#1806FOh, um, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100344V#11P#0004FBeing nervous about it is natural, I think.\x02\x03",
            "#2100345V#0001FThough, back to the topic at hand, you\x01",
            "implied that Ilya isn't really bothered by\x01",
            "the letter, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#2100346V#1P#1808FYes, but I wish she'd take this seriously.\x01",
            "She said she's busy perfecting the new play,\x01",
            "so she doesn't have time for non-issues.\x02\x03",
            "#2100347V#1806FNon-issues like 'dealing with buffoons from\x01",
            "the police,' I think were her exact words.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2100348V#11P#0011FWell, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100349V#12P#0211FWould that mean we are better off not\x01",
            "poking our heads into her private matters?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#2100350V#1P#1802FB-But...you're the Special Support Section.\x02\x03",
            "#2100351VI read in a magazine that you're supposed\x01",
            "to be friendlier than the rest of the CPD...\x02\x03",
            "#2100352V#1809FI think I can get Ilya to agree to trust the\x01",
            "matter to you four...hopefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100353V#11P#0003F(Sh-She really seems desperate...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100354V#6P#0100FI wouldn't normally suggest this, but have\x01",
            "you asked the Bracer Guild for help?\x02\x03",
            "#2100355VSince Ilya's a civilian, perhaps they could\x01",
            "work as bodyguards for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#2100356V#1P#1808FWell, there's a small problem with that.\x02\x03",
            "#2100357V#1803FYou know as well as I do how popular\x01",
            "the guild is in Crossbell.\x02\x03",
            "#2100358VIt'd be far too conspicuous if bracers\x01",
            "were constantly coming in and out of\x01",
            "Arc en Ciel. Rumors would spread.\x02\x03",
            "#2100359V#1802FSo with that in mind, I thought people\x01",
            "wouldn't really notice if it were you guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x15,
        (
            "#2100360V#1P#1801FO-Oh, I'm so sorry! That sounded so\x01",
            "much ruder than I thought it would.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100361V#11P#0012FI-It's fine, Miss Mao. We understand.\x02\x03",
            "#2100362V#0000FI think we have a grasp on the\x01",
            "situation now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#2100363V#5P#0000FI know where I stand, but what do you\x01",
            "think, guys? Should we take the case?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100364V#6P#0102FOf course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100365V#12P#0204FI have no objections.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    ChrTalk(
        0x104,
        "#2100366V#0309FHow could we NOT help 'em out?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2100367V#11P#0004FThere you have it, Miss Mao.\x02\x03",
            "#2100368V#0000FIf you'll let us, the Special Support Section\x01",
            "would be happy to tackle this threat letter.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    Sleep(200)

    ChrTalk(
        0x15,
        (
            "#2100369V#1P#1802FTh-Thank you so much!\x02\x03",
            "#2100370V#1809FI'll head back to the theater, if that's okay.\x02\x03",
            "#2100371VI need to tell the troupe leader and\x01",
            "Ilya the good news. Please, stop by\x01",
            "whenever works for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100372V#6P#0102FWe will.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(200)

    ChrTalk(
        0x104,
        "#2100373V#0309FSee ya, Rixia! Call me any time!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 4900, 30, 5500, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sound(1638, 255, 100, 0)
    Sleep(1000)
    OP_68(3000, 950, 1800, 3500)

    def lambda_1522A():
        OP_95(0xFE, 3600, 30, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1522A)
    WaitChrThread(0x15, 1)

    def lambda_15248():
        OP_95(0xFE, 1000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_15248)
    Sleep(500)
    SetChrSubChip(0x103, 0x1)
    Sleep(500)
    SetChrSubChip(0x102, 0x1)
    WaitChrThread(0x15, 1)

    def lambda_15274():
        OP_95(0xFE, 1000, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_15274)
    Sleep(500)
    Sound(103, 0, 100, 0)

    def lambda_15297():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_15297)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x15, 2)
    Sound(104, 0, 100, 0)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    OP_6F(0x1)
    Sleep(500)
    OP_68(6060, 950, 4530, 1600)
    Sleep(500)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#2100375V#5P#0003FWell, we should probably jump on this\x01",
            "soon and head to Arc en Ciel.\x02\x03",
            "#2100376V#0000FAfter all, we can't exactly conduct our\x01",
            "investigation without the key evidence,\x01",
            "can we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100377V#12P#0204FIndeed.\x02\x03",
            "#2100378V#0202FWe cannot ignore Ilya's theory that\x01",
            "it is simply a prank, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100379V#0302FMan, this is a blessing in disguise!\x02\x03",
            "#2100380VHangin' out in Arc en Ciel right before\x01",
            "the debut of their new show? Score!\x02\x03",
            "#2100381V#0309FAnd we get to see Ilya Platiere in all\x01",
            "her glory, baby!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2100382V#6P#0108FHonestly, Randy... Though, I can't\x01",
            "deny I'm excited to meet Ilya Platiere\x01",
            "myself.\x02\x03",
            "#2100383V#0106FD-Does my hair look okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100384V#5P#0005FYou two are really worked up about this.\x02\x03",
            "#2100385V#0006FWell, she's definitely a looker, based on what\x01",
            "I've seen in magazines...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100386V#12P#0202FI, too, would be lying if I said I was\x01",
            "not at least a tiny bit excited.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7100", 0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_68(3000, 1030, 4300, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 3000, 0, 4300, 270)
    SetChrPos(0x1, 3000, 0, 4300, 270)
    SetChrPos(0x2, 3000, 0, 4300, 270)
    SetChrPos(0x3, 3000, 0, 4300, 270)
    SetScenarioFlags(0x80, 2)
    OP_29(0x42, 0x4, 0x2)
    OP_29(0x42, 0x1, 0x0)
    OP_29(0x41, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_32_13BAB end

    def Function_33_15788(): pass

    label("Function_33_15788")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50120.itc", 0x1E)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 63600, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, 61600, 30, 8000, 225)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01000.itp")
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#2101488VHmm. So that's where things stand.\x02\x03",
            "#2101489VWell? Are you okay with leaving the\x01",
            "situation as is?\x02",
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
            "#2101490V#12P#0006FYou're saying we have a choice?\x02\x03",
            "#2101491V#0001FThe First Division took over the case.\x01",
            "There's no way we can oppose them,\x01",
            "given our team's position on the force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101492V#5P#1003FYou make a good point, Lloyd.\x02\x03",
            "#2101493V#1000FThe fox would probably track you down\x01",
            "and start barking at you till the sun set.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101494V#12P#0006FYeah, that seems to be one of the\x01",
            "vice commissioner's favorite pastimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101495V#12P#0200FCould we not simply offer our assistance\x01",
            "to the First Division?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101496V#0306FDunno how well that'd play out, considering\x01",
            "ol' four-eyes' attitude towards us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101497V#5P#1000FYep, that's also a long shot.\x02\x03",
            "#2101498V#1003FThe CPD is a territorial bunch, and it makes\x01",
            "the organization a hassle to deal with.\x02\x03",
            "#2101499VThat goes double for the First Division. Their\x01",
            "stubbornness wouldn't allow them to accept\x01",
            "help from a group of rookies like the SSS.\x02\x03",
            "#2101500V#1002FBut, if you're talking about working\x01",
            "incognito, that's another topic altogether.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
        "#2101501V#12P#0011FYou're proposing we go behind their backs?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101502V#5P#1004FHeh. This is the Special Support Section, the\x01",
            "most unconventional squad out there.\x02\x03",
            "#2101503VSince we're kinda ignored by the department,\x01",
            "that gives you a certain level of discretion that\x01",
            "you can use to your advantage.\x02\x03",
            "#2101504V#1002FBasically, if you play your cards right, you can\x01",
            "act without provoking that territorial nature of\x01",
            "theirs. Make sense?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101505V#12P#0005F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101506V#0305FDude. You do realize you just said we can\x01",
            "ignore our superiors' orders, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101507V#12P#0211FYou are being quite the bad influence...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101508V#5P#1004FHeh. Didn't I make myself clear?\x02\x03",
            "#2101509VI won't work with you in the field,\x01",
            "but I'll cover for you when I can.\x02\x03",
            "#2101510V#1002FYou're the ones jumping into the\x01",
            "fire, not me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101520V#12P#0008F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101512V#5P#1003FThat being said, the current situation might\x01",
            "make this plan impossible to pull off.\x02\x03",
            "#2101513V#1000FOne of you is struggling to figure out what\x01",
            "to do...\x02\x03",
            "#2101514V...and this situation is something you can\x01",
            "only overcome by operating as a unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101515V#12P#0006FYou're right, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101516V#0306FWell, if Mademois-Elie doesn't know what\x01",
            "to do, she must really be down in the dumps.\x02\x03",
            "#2101517V#0308FShe'll probably get over it, but I'd be lyin'\x01",
            "if I said I didn't have some butterflies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2101518V#12P#0208FShe has been like that all day, from what\x01",
            "I could tell...\x02\x03",
            "#2101519V#0206FIs Elie going to be all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101511V#12P#0008F...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x4)
    Sleep(130)
    SetChrSubChip(0xC, 0x3)
    Sleep(130)
    SetChrSubChip(0xC, 0x2)
    Sleep(130)

    def lambda_16409():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_16409)
    Sound(848, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(1100)
    SetChrSubChip(0xC, 0x2)
    Sleep(130)
    SetChrSubChip(0xC, 0x3)
    Sleep(130)
    SetChrSubChip(0xC, 0x4)
    Sleep(130)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    Sleep(300)
    OP_63(0xC, 0x12C, 1000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(500)
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x1388)
    WaitBGM()
    ReplaceBGM("ed7513", "ed7515")
    OP_CA(0x1, 0xFF, 0x0)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    SetScenarioFlags(0x5C, 2)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_15788 end

    def Function_34_164BC(): pass

    label("Function_34_164BC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    OP_68(12600, 2350, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis121.itp")
    OP_68(12600, 1850, 5600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x102,
        (
            "#2200001V#0103FIsn't it a bit ridiculous?\x02\x03",
            "#2200002V#0101FDespite our work, we had no choice but to\x01",
            "hand the case over to the First Division.\x02\x03",
            "#2200003VRixia was smart enough to ask us, but just\x01",
            "imagine if she hadn't. Everything we learned\x01",
            "about Yin would have stayed in the dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200004V#5P#0006FYeah, I know.\x02\x03",
            "#2200005V#0008FIf only there were some kind of diversion\x01",
            "that would allow us to continue investigating.\x02\x03",
            "#2200006V#0001FLet's think for a minute. Who would\x01",
            "know about the existence of Yin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200007V#0103FWell, obviously Heiyue, considering that's\x01",
            "his current employer.\x02\x03",
            "#2200008VAnd then there's their rival, Revache, and\x01",
            "the First Division, who's tracking Heiyue's\x01",
            "movements, according to Dudley...\x02\x03",
            "#2200009V#0100FFrom there, we can assume that Speaker\x01",
            "Hartmann, who's closely tied to Revache,\x01",
            "knows about him, as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#2200010V#5P#0005FThat's the man you mentioned yesterday,\x01",
            "right, Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200011V#0106FYes. He's a career politician who more-or-\x01",
            "less rules over the diet, serving as the\x01",
            "leader of the Imperial Faction.\x02\x03",
            "#2200012VHonestly, it wouldn't be far-fetched to say\x01",
            "that he's Revache's greatest supporter.\x02\x03",
            "#2200013V#0101FIncidentally, almost all of Grandfather's\x01",
            "reform bills were crushed by this man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200014V#5P#0008FI've always heard his name, but I never\x01",
            "understood the weight behind it.\x02\x03",
            "#2200015V#0001FBut, in this instance, wouldn't Yin be\x01",
            "their opponent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200016V#0106FThat would make sense...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(500)
    OP_64(0x103)
    OP_64(0x104)
    Sleep(500)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#2200017V#11P#0005FTio? Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200018V#0105F#11PYou two look completely bewildered.\x01",
            "Is there something we're missing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200019V#6P#0306FNo... It's just...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200020V#6P#0202FYou seem to be in a much better mood\x01",
            "today, Elie.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#2200021V#0105F#11PI guess so...\x02\x03",
            "#2200022V#0106F...I'm sorry about yesterday, everyone.\x01",
            "I wasn't acting like myself.\x02\x03",
            "#2200023V#0100FBut, I'm fine now, and I don't intend to\x01",
            "be a burden to the team.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2200024V#5P#0003FYou've never been a burden to us, Elie.\x02\x03",
            "#2200025V#0000FQuite the opposite, actually. You help\x01",
            "us out all the time.\x02\x03",
            "#2200026VI mean, look at us right now. You're\x01",
            "making connections in this case that\x01",
            "I'd never be able to make.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    ChrTalk(
        0x102,
        "#2200027V#0102FI-I guess so.\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x104,
        "#2200028V#6P#0301FSomethin' smells fishy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200029V#6P#0211FAgreed. Something is off. Very off.\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#2200030V#11P#0005FWhat's that supposed to mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200031V#0112F#11PW-Wait a minute, you two...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200032V#6P#0303FY'know, I could hear a pair of voices\x01",
            "chattering away on the roof from my\x01",
            "window.\x02\x03",
            "#2200033V#0302FI wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200034V#6P#0202FCongratulations, Lloyd and Elie.\x02\x03",
            "#2200035V#0204FI wish the best for you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)

    ChrTalk(
        0x101,
        (
            "#2200036V#11P#0011FH-Hold on! We didn't do anything that\x01",
            "warrants congratulations, right, Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200037V#0112F#11PYes! I-I mean, no!\x02\x03",
            "#2200038V#0113FWe were just talking about life and\x01",
            "other things of that nature...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200039V#6P#0302FLife, eh? Uh-huh, I'm sure you did.\x02\x03",
            "#2200040V#0309FSo, Lloyd, how far did ya go?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#2200041V#5P#0007FRANDY!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200042V#0112F#11PP-Please, Tio's sitting right there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200043V#6P#0205FHow far did you go...?\x02\x03",
            "#2200044V#0204FIs Randy referring to the intimacy\x01",
            "people engage in while in romantic\x01",
            "relationships?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#2200045V#11P#0012FNope, nope, nope! Not at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200046V#6P#0309FLloyd and Elie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200047V#6P#0202F...sitting in a tree...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0x3E8, 0x5DC)

    ChrTalk(
        0x102,
        "#2200048V#0109F#4S#90W#11PGuys? C u t  i t  o u t.#20W\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200049V#6P#0306FY-Yes, ma'am...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200050V#11P#0006FGeez, you guys are insane.\x02\x03",
            "#2200051VMe and Elie together? Romantically?\x01",
            "I'd say the odds of that happening are\x01",
            "pretty slim.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)

    ChrTalk(
        0x102,
        "#2200052V#0105F#40WWhat was that?#20W\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200053V#11P#0012FI mean, we're kind of incompatible,\x01",
            "and everything last night was strictly\x01",
            "professional...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#2200054V#5P#0000FRight, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200055V#0101F#70W...#20W\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200056V#5P#0005FWh-What's the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200057V#6P#0306F(You numbskull...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200058V#6P#0211F(You just signed your death\x01",
            "warrant, Lloyd.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200059V#0104F#40WOh, yes. You are SO right, Lloyd.\x02\x03",
            "#2200060VAll I did was ask you for some advice on a\x01",
            "very unimportant subject, that's all.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x0, 0x64, 0xBB8, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#2200061V#0101F#4SAnd there most DEFINITELY wasn't any sort\x01",
            "of romantic atmosphere, like you oh-so\x01",
            "graciously pointed out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200062V#5P#0011FU-Uh, all right, then...\x02\x03",
            "#2200063V#0012FYou know, by incompatible, I only\x01",
            "meant that we don't exactly make\x01",
            "a good match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200064V#0111F*glare*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200065V#5P#0006FSorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200066V#6P#0309FHaha...\x02\x03",
            "#2200067V#0302FWell, on the bright side, it looks like you've\x01",
            "perked up since yesterday, Mademois-Elie.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#2200068V#0105F#11PAh...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)

    ChrTalk(
        0x103,
        (
            "#2200069V#6P#0204FThank goodness.\x02\x03",
            "#2200070V#0208FI was not sure whether or not you were\x01",
            "going to stay with the CPD...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200071V#0106F#11PI'm sorry. I never meant to make\x01",
            "you all worry.\x02\x03",
            "#2200072V#0102FI don't know where the future will\x01",
            "take me...\x02\x03",
            "#2200073V...but right now, I know this is where\x01",
            "I'm meant to be.\x02\x03",
            "#2200074V#0104FSo, everyone, I'm happy that I get\x01",
            "to keep working with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200075V#5P#0002FElie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200076V#6P#0202FGood to have you back, Elie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200077V#6P#0309FHaha, damn straight. 'Sides, doubt we'd\x01",
            "get anything done around here without\x01",
            "you to keep us from goofing off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200078V#0111F#11PI wouldn't have to be so stern all the time\x01",
            "if you three would just stay on-task.\x02\x03",
            "#2200079V#0103FWell, that's enough of that.\x02\x03",
            "#2200080V#0101FDo we have any ideas what to do about\x01",
            "the investigation from here on out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200081V#5P#0003FGood question...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200082V#6P#0206FWe could always attempt to corner Yin with\x01",
            "a different approach than the one the First\x01",
            "Division is using...\x02\x03",
            "#2200083VBut considering how many methods there\x01",
            "actually are, we might just end up even\x01",
            "more confused than we are now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200084V#6P#0303FYeah, that's probably not the best strategy.\x02\x03",
            "#2200085V#0300FHow about we go on a lil' trip to Calvard's\x01",
            "Eastern Quarter?\x02\x03",
            "#2200086VI bet we'd find a few clues about Yin there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200087V#5P#0005FAre you being serious, Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200088V#0101F#11PWould we even get permission to go on\x01",
            "a business trip?\x02\x03",
            "#2200089VGiven our team's situation, I doubt we'd\x01",
            "be allowed to travel very far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200090V#6P#0203F...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 10400, 850, 7600, 90)
    Sound(820, 0, 100, 0)
    Sleep(500)
    OP_68(16100, 1850, 10000, 3000)
    MoveCamera(7, 21, 0, 3000)
    SetCameraDistance(25000, 3000)

    def lambda_18082():
        OP_95(0xFE, 16100, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18082)
    Sleep(300)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x104, 0x1)
    Sleep(500)
    SetChrSubChip(0x101, 0x2)
    WaitChrThread(0x103, 1)

    def lambda_180B9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_180B9)
    OP_6F(0x51)

    ChrTalk(
        0x101,
        "#2200091V#0005FTio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200092V#0105F#5PDid you think of something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200093V#0200FI was contemplating looking into the\x01",
            "police database a bit more.\x02\x03",
            "#2200094VPerhaps I would be able to learn about\x01",
            "the First Division's movements and so on.\x02\x03",
            "#2200095V#0203FThen again, I already searched it last night,\x01",
            "so it likely has not been updated since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200096V#0001FIt's not a bad idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200097V#1P#0300FHey, it beats sittin' around here and\x01",
            "doing nothing.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_90(0x101, 14800, 850, 7600, 270)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_90(0x102, 14800, 850, 5400, 270)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_90(0x104, 10400, 850, 5400, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    BeginChrThread(0x104, 3, 0, 36)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 35)
    OP_92(0x101, 0x3B60, 0x2134, 0x1F4)

    def lambda_18325():
        OP_95(0xFE, 15200, 850, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18325)
    WaitChrThread(0x101, 1)

    def lambda_18343():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18343)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    Sound(824, 0, 100, 0)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#2200152V#0205FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200099V#6P#0001FWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200100V#0202FHow strange...\x02\x03",
            "#2200101VIt seems as though we have received\x01",
            "an orbmail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200102V#6P#0005FWhat's that, again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200103V#6P#0100FAren't they essentially letters that can\x01",
            "be sent from terminal to terminal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200104V#0206FPrecisely. The peculiar thing is, despite\x01",
            "being extremely useful, almost no one\x01",
            "in the CPD uses orbal mail.\x02\x03",
            "#2200105VMost likely because not many officers\x01",
            "are trained to use keyboards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200106V#6P#0006FI'm one of those, unfortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200107V#0300FWell? Who's it from?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200108V#0202FLet me check.\x02",
    )

    CloseMessageWindow()
    Sound(849, 0, 100, 0)
    Sleep(1200)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#2200109V#0205FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200110V#6P#0005FIs something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200111V#6P#0105FWho would send us--\x02\x03",
            "#2200112V#0101F...?!\x02",
        )
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(-1, 130, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "I, Yin, hereby submit my support request.\x01",
            "Overcome this trial and face me. Only then\x01",
            "will I grant you your mission.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x101,
        "#2200113V#0007FIt's him!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#2200114V#0307FIs this some kinda joke?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#2200115V#0101FTio, where was the mail sent from?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#2200116V#0201FDefinitely not the police department...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(849, 0, 100, 0)
    Sleep(1000)

    AnonymousTalk(
        0x103,
        (
            "#2200117V#0205FGot it.\x02\x03",
            "#2200118V#0203FIt was sent from the International Bank of Crossbell...\x02\x03",
            "#2200119V#0201FOtherwise known as the IBC.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
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
        "#2200120V#6P#0013FWhat exactly does it mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200121V#0301FThe IBC's that bank that rakes in mira\x01",
            "from all over Zemuria, right?\x02\x03",
            "#2200122VWhy the hell would a place like that be\x01",
            "sending us prank mail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200123V#0206FDo not ask me.\x02\x03",
            "#2200124V#0201FI can say, however, that this mail was\x01",
            "definitely sent from an IBC terminal.\x02\x03",
            "#2200125VI have no way of knowing who sent it,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#2200126V#6P#0008FCould it be possible that Yin infiltrated\x01",
            "the IBC?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2200127V#12P#0103FIt's not out of the question.\x02\x03",
            "#2200128V#0101FThe IBC building is home to quite a few external\x01",
            "companies and organizations.\x02\x03",
            "#2200129VCorrect me if I'm wrong, but I think there's\x01",
            "an Epstein Foundation office, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#2200130V#0203FThat is correct. An acquaintance of mine\x01",
            "works there.\x02\x03",
            "#2200131V#0200FHowever, I should have been more clear.\x01",
            "The orbal mail was sent directly from the\x01",
            "IBC's main terminal.\x02\x03",
            "#2200132VBecause of that, I think the possibility of an\x01",
            "external company being involved is low.\x02",
        )
    )

    CloseMessageWindow()
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
        (
            "#2200133V#6P#0006FWell, we won't know until we ask them.\x02\x03",
            "#2200134VI wanted our investigation to fly under\x01",
            "the First Division's radar, but we really\x01",
            "don't have any other choice.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#2200135V#0306FYeeeeah. Goin' undercover this time might\x01",
            "be a lil' tricky.\x02\x03",
            "#2200136V#0300FShould we hurry up and check it out before\x01",
            "they screw everything up again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200137V#12P#0103F...\x02\x03",
            "#2200138V#0100FActually, we may be able to perform\x01",
            "our search in secret, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        "#2200139V#5P#0005FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200140V#0205FHow, exactly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200141V#12P#0104FMy best friend's father works at the IBC.\x02\x03",
            "#2200142V#0100FIf we told him about our unique situation,\x01",
            "he might give us a hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200163V#5P#0000FYou think so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200144V#0309F#5PHey, ain't that convenient?\x02\x03",
            "#2200145V#0300FYou got more connections than you know\x01",
            "what to do with, eh, Mademois-Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200146V#12P#0104FWell, I have a decent amount.\x02\x03",
            "#2200147V#0108FUnfortunately, I have no way of knowing\x01",
            "whether or not he's even in Crossbell City,\x01",
            "given how hectic his schedule is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200148V#0200FWhat sort of position does he hold there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200149V#12P#0103F...A pretty important one. Honestly, I'd be\x01",
            "surprised if you didn't know his name.\x02\x03",
            "#2200150V#0100FDieter Crois?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2200151V#5P#0005FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200098V#0205F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200153V#0305F#5PWhat? He famous or somethin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200154V#5P#0000FY-Yeah, he is.\x02\x03",
            "#2200155V#0003FHonestly, you could make the argument\x01",
            "that he's just as popular as Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200156V#0204FDieter Crois...\x02\x03",
            "#2200157VHe is a prominent Zemurian billionaire,\x01",
            "a leader of the world economy...\x02\x03",
            "#2200158V#0202F...and the current CEO of the International\x01",
            "Bank of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200159V#0307F#5PHe runs the freakin' bank?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200160V#12P#0104FI originally knew him as an old friend of my\x01",
            "father's.\x02\x03",
            "#2200161VBut he's also kept a friendly relationship with\x01",
            "my grandfather. Because of that, I've known\x01",
            "him a good portion of my life.\x02\x03",
            "#2200162V#0102FOh, and I almost forgot. His daughter is one\x01",
            "of my closest childhood friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200143V#5P#0002FWow, that's amazing.\x02\x03",
            "#2200164V#0006FThing is, we can't do much if he's not there,\x01",
            "even if he is the CEO.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200165V#12P#0106FYou're right. I heard that he spends almost\x01",
            "half of the year flying abroad.\x02\x03",
            "#2200166V#0101FNevertheless, there's no harm in trying,\x01",
            "is there?\x02\x03",
            "#2200167VEven if he isn't in town, my friend might\x01",
            "be. She may even be able to help us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200168V#5P#0000FLet's do it, then.\x02\x03",
            "#2200169V#0003FI think we already have a rough idea\x01",
            "of what the situation is, so we should\x01",
            "know what in particular to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200170V#0206FThe intentions behind the orbmail, right?\x02\x03",
            "#2200171V#0201FIt was rather intimidating, but what exactly\x01",
            "does he plan to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200172V#0302F#5PWell, he went out of his way to reach\x01",
            "out to us and lay down a challenge.\x02\x03",
            "#2200173VI say we take the bait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200174V#12P#0104FAgreed.\x02\x03",
            "#2200175V#0100FShall we head to the IBC?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    OP_68(15000, 1850, 8900, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 15000, 850, 8900, 45)
    SetChrPos(0x1, 15000, 850, 8900, 45)
    SetChrPos(0x2, 15000, 850, 8900, 45)
    SetChrPos(0x3, 15000, 850, 8900, 45)
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetChrPos(0x0, 15000, 850, 8900, 45)
    SetScenarioFlags(0x82, 0)
    OP_C7(0x1, 0x1000)
    OP_29(0x43, 0x4, 0x2)
    OP_29(0x43, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19A68")
    OP_29(0xF, 0x4, 0x40)
    Jump("loc_19A7A")

    label("loc_19A68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A7A")
    OP_29(0xF, 0x4, 0x40)

    label("loc_19A7A")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7100", 0)
    EventEnd(0x5)
    Return()

    # Function_34_164BC end

    def Function_35_19A8E(): pass

    label("Function_35_19A8E")

    Sleep(500)
    OP_93(0x102, 0x0, 0x1F4)

    def lambda_19A9D():
        OP_96(0xFE, 0x4010, 0x352, 0x1EDC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19A9D)
    WaitChrThread(0x102, 1)
    Return()

    # Function_35_19A8E end

    def Function_36_19AB7(): pass

    label("Function_36_19AB7")


    def lambda_19ABC():
        OP_95(0xFE, 10400, 850, 8600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19ABC)
    WaitChrThread(0x104, 1)

    def lambda_19ADA():
        OP_95(0xFE, 14400, 850, 9900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19ADA)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_36_19AB7 end

    def Function_37_19AFB(): pass

    label("Function_37_19AFB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("apl/ch50091.itc", 0x1F)
    OP_68(5500, 900, 4200, 0)
    MoveCamera(37, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 5500, 130, 6250, 180)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 4900, 130, 2200, 0)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x104, 6000, 130, 2200, 0)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 3000, 0, 2500, 225)
    ClearChrFlags(0xC, 0x1)
    BeginChrThread(0xC, 3, 0, 0)
    SetChrChipByIndex(0x28, 0x1F)
    SetChrSubChip(0x28, 0x1D)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 5300, 350, 4500, 0)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    Sleep(500)
    Sound(18, 0, 100, 0)
    UseItem(0x2BF, 0xFF)
    Sleep(500)
    PlayBGM("ed7110", 0)
    SetCameraDistance(24000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x104,
        (
            "#2201710V#4P#0306FYikes. Things really got outta hand.\x02\x03",
            "#2201711V#0301FMost of the public should be in an\x01",
            "uproar by now, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201712V#12P#0206FConsidering that the mayor was almost\x01",
            "assassinated at the debut of Arc en Ciel's\x01",
            "new show, yes, I would imagine so.\x02\x03",
            "#2201713V#0211FIt is the ultimate scandal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201714V#5P#0006FWe can at least take comfort in the fact that\x01",
            "Mayor MacDowell is getting a lot of support\x01",
            "from the citizenry...\x02\x03",
            "#2201715V#0008FBut, surely the name of the Imperial Faction\x01",
            "diet member that Ernest had ties to will\x01",
            "make the papers, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201716V#4P#0303FEh, it'll probably be censored.\x02\x03",
            "#2201717V#0301FBesides, wasn't this whole thing the\x01",
            "product of that secretary lunatic goin'\x01",
            "wild against his boss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201718V#5P#0003FYeah, maybe so.\x02\x03",
            "#2201719V#0001FThere really wouldn't be any benefit to assassinating\x01",
            "the mayor, as far as the Imperial Faction's concerned.\x02\x03",
            "#2201720V#0008FThen again, had the assassination been successful,\x01",
            "they could have pinned it on Yin and, by extension, the\x01",
            "Republican Faction due to their connections with Heiyue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2201721V#4P#0305FYou might be on to somethin' there...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201722V#12P#0208FPardon the interruption, but was Ernest\x01",
            "not acting sort of strange?\x02\x03",
            "#2201723V#0201FIt was as if he lost his sanity... Or perhaps\x01",
            "lost control would be more appropriate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201724V#5P#0006FYeah, I was thinking the same thing.\x02\x03",
            "#2201725V#0001FEither way, I can't help but wonder what\x01",
            "happened after the First Division took\x01",
            "over the investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x8, 16500, 850, 3700, 270)

    NpcTalk(
        0x8,
        "Man's Voice",
        (
            "#2201726VWell, as for Ernest, he's in a state of total\x01",
            "shock. Can't even speak properly.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x4)
    OP_68(14500, 1850, 3700, 2000)
    SetCameraDistance(23500, 2000)
    SetChrSubChip(0x101, 0x1)
    Sleep(100)
    SetChrSubChip(0x104, 0x2)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    OP_6F(0x11)

    ChrTalk(
        0x101,
        "#2201727V#0005FChief...\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_1A350():
        OP_95(0xFE, 16500, 850, 9100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A350)
    Sleep(1000)
    Fade(1000)
    OP_68(6500, 900, 5000, 0)
    MoveCamera(37, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    OP_68(4500, 900, 5000, 3000)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0x8, 0x1)
    SetChrPos(0x8, 4500, 850, 9100, 270)

    def lambda_1A3D2():
        OP_95(0xFE, 2500, 850, 9100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A3D2)
    WaitChrThread(0x8, 1)

    def lambda_1A3F0():
        OP_95(0xFE, 2500, 0, 5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A3F0)
    Sleep(700)
    SetChrSubChip(0x104, 0x1)
    Sleep(300)
    SetChrSubChip(0x103, 0x1)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x1F4)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#2201728V#11P#0301FYou're sayin' he's so messed up they\x01",
            "can't even interrogate him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2201729V#6P#1003FYep. Since they weren't making any progress\x01",
            "with him, they decided to go ahead and chuck\x01",
            "him in the clink.\x02\x03",
            "#2201730V#1000FLast I heard, they thought of calling in a church\x01",
            "counselor or asking if someone from St. Ursula\x01",
            "would examine him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201731V#5P#0006FYeah, that might help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2201732V#6P#1002FHeh. That aside, you four have become\x01",
            "quite the celebrities, haven't you?\x02\x03",
            "#2201733VWhile I was at the department today, I got\x01",
            "to witness the fox showering the SSS with\x01",
            "praises. Boy, you should've heard him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201734V#5P#0011FNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2201735V#12P#0211FI find that hard to picture.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201736V#11P#0306FVice Commish Jackass decided to flatter us.\x01",
            "I'm thrilled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2201737V#6P#1003FHey, it wasn't only him. The entire force had\x01",
            "something good to say about you guys.\x02\x03",
            "#2201738V#1002FActually, I take that back. The First Division\x01",
            "didn't really say much, but I'm sure that their\x01",
            "opinion of the SSS is a bit higher now.\x02\x03",
            "#2201739VShow some cheer. You earned it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201740V#5P#0000FYeah, we'll try.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201741V#12P#0208FBut how can we be happy at a time\x01",
            "like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201742V#11P#0303FYeah. Try to think about how Mademois-Elie\x01",
            "is feelin' right about now...\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x20B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x102, 0x8)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_19AFB end

    def Function_38_1A9A7(): pass

    label("Function_38_1A9A7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch50090.itc", 0x20)
    LoadChrToIndex("chr/ch05000.itc", 0x21)
    LoadChrToIndex("chr/ch08201.itc", 0x22)
    LoadChrToIndex("apl/ch50380.itc", 0x23)
    LoadChrToIndex("apl/ch50092.itc", 0x24)
    OP_68(258000, 700, 68700, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 256399, 0, 68100, 180)
    SetChrPos(0x103, 254900, 0, 68100, 90)
    SetChrPos(0x102, 256399, 0, 66600, 0)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 255400, 30, 71000, 180)

    def lambda_1AAA3():

        label("loc_1AAA3")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_1AAA3")

    QueueWorkItem2(0xC, 1, lambda_1AAA3)
    SetChrFlags(0x9, 0x80)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01109.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis158.itp")
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "One week passed.\x02\x03",
            "The Special Support Section was sheltering KeA\x01",
            "at the SSS building all while watching for possible\x01",
            "retaliation from the mafia.\x02\x03",
            "Relying on police intelligence and even Jona's vast\x01",
            "information network, they carefully monitored the\x01",
            "movements of Revache and Speaker Hartmann.\x02\x03",
            "On the other hand, KeA, despite her memories not\x01",
            "returning, quickly settled in to her new life with the\x01",
            "Special Support Section.\x02\x03",
            "And then...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    PlayBGM("ed7110", 0)
    OP_68(257000, 700, 68700, 2000)
    FadeToBright(2000, 0)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 39)
    WaitChrThread(0x102, 3)

    def lambda_1AD3C():
        OP_96(0xFE, 0x3E738, 0x0, 0x10A04, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AD3C)
    Sleep(300)

    def lambda_1AD59():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1AD59)
    WaitChrThread(0x103, 1)
    Sound(820, 0, 100, 0)
    OP_63(0xA, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    def lambda_1AD8B():
        OP_96(0xFE, 0x3E3B4, 0x0, 0x10A04, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AD8B)
    WaitChrThread(0x103, 1)

    def lambda_1ADA9():
        OP_93(0xA, 0x5A, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1ADA9)
    WaitChrThread(0xA, 2)

    def lambda_1ADBA():
        OP_93(0xA, 0x10F, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1ADBA)
    WaitChrThread(0xA, 2)
    OP_63(0xA, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)
    BeginChrThread(0x102, 3, 0, 39)
    OP_68(256000, 700, 68700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    OP_64(0x102)
    OP_64(0x103)
    SetMapObjFlags(0xE, 0x4)
    OP_68(64000, 1100, 6900, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 65300, 0, 6900, 270)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x101, 62700, 0, 6300, 90)
    SetChrPos(0x104, 62700, 0, 7500, 90)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        "#3600001V#0005FA truce?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x8,
        (
            "#3600002V#1003F#11PYep. It's informal, but apparently, that's the\x01",
            "message Revache has been sending to the\x01",
            "police department.\x02\x03",
            "#3600003V#1001FThey claim that a kid slipping into one of\x01",
            "the exhibits was a mistake. And better yet,\x01",
            "they have no idea who she is.\x02\x03",
            "#3600004V#1006FOf course, they pointed fingers at Heiyue,\x01",
            "but who knows what actually happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600005V#6P#0006FI'm not so sure about that theory.\x02\x03",
            "#3600006V#0001FWhen we busted into the exhibit room,\x01",
            "Yin had just defeated the mafiosos who\x01",
            "were standing guard.\x02\x03",
            "#3600007VI doubt he had time to bring in KeA from\x01",
            "the outside AND replace the doll with her.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1B21C")

    ChrTalk(
        0x104,
        (
            "#3600008V#6P#0306FDoes that mean she was already in the trunk\x01",
            "by the time it was sent to the mansion?\x02\x03",
            "#3600010V#0301FAnd where the hell did the original doll come\x01",
            "from in the first place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B2D9")

    label("loc_1B21C")


    ChrTalk(
        0x104,
        (
            "#3600009V#6P#0306FThat mean she was already in the trunk\x01",
            "by the time it was sent to the mansion?\x02\x03",
            "#3600010V#0301FAnd where the hell did the original doll come\x01",
            "from in the first place?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B2D9")


    ChrTalk(
        0x8,
        (
            "#3600011V#1003F#11PI can't say for sure, but I've heard some say\x01",
            "it was obtained through a Remiferian back\x01",
            "channel...\x02\x03",
            "#3600012V#1001F...on the last day of the festival, no less. In\x01",
            "other words, every exhibit was carried into\x01",
            "the mansion on the same day as the auction.\x02\x03",
            "#3600013VEven the shipping company that transported\x01",
            "everything says the accusations are made-up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600014V#6P#0011FMade-up? Are they crazy?\x02\x03",
            "#3600015V#0010FThat's the same as saying we put KeA\x01",
            "in there, ourselves!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600016V#1003F#11PAnd there you have it.\x02\x03",
            "#3600017VListen. I don't know what's true or not, but\x01",
            "it's clear that Revache is desperately trying\x01",
            "to justify what happened.\x02\x03",
            "#3600018V#1001FAfter all, if they aren't careful, they could be\x01",
            "accused of human trafficking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600019V#6P#0008F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3600020V#6P#0303FWeapons trafficking, mira laundering, and an\x01",
            "illegal auction that deals in stolen goods...\x02\x03",
            "#3600021V#0301FYou're tellin' me that those guys will do all that\x01",
            "stuff and not bat an eye, but human trafficking\x01",
            "is where it crosses the line?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600022V#1001F#11PThat goes without saying.\x02\x03",
            "#3600023V#1003FHuman trafficking falls under one of the highest\x01",
            "classes of offense. There's no chance you'll get\x01",
            "off lightly, given how serious it is.\x02\x03",
            "#3600024VNot even the CPD would stay silent about it.\x01",
            "But, more importantly, if the guild caught whiff\x01",
            "of it, they'd eradicate you, no questions asked.\x02\x03",
            "#3600025V#1000FThey have the honor of the supporting gauntlet\x01",
            "to uphold, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600026V#6P#0006FRevache couldn't risk that large a scandal,\x01",
            "let alone Speaker Hartmann...\x02\x03",
            "#3600027V#0001FThat excuse makes perfect sense, but to\x01",
            "be honest, I'm not fully convinced yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600028V#1003F#11PYeah, and that brings us to the truce.\x02\x03",
            "#3600029V#1000FThey claim that your undercover investigation\x01",
            "was a cut and dried case of trespassing, but it\x01",
            "sounds like they're willing to look past it.\x02\x03",
            "#3600030VThey intend to leave everything to us--even\x01",
            "the handling of the girl you took into custody\x01",
            "'by pure coincidence.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3600031V#6P#0306FAnd in exchange, we gotta accept whatever\x01",
            "they say happened as the truth...\x02\x03",
            "#3600032V...and not snitch on them to the guild. That\x01",
            "about sum it up?\x02\x03",
            "#3600033V#0300FSounds like they're in pretty dire straits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600034V#6P#0008F...\x02\x03",
            "#3600035V#0006FI'd rather not have any uncertainties\x01",
            "about this situation, but...\x02\x03",
            "#3600036V#0000FIf the mafia's saying they're not going\x01",
            "to try and take KeA back, then we might\x01",
            "have no choice but to take them at their word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600037V#1002F#11POh, I feel the same way.\x02\x03",
            "#3600038V#1003FRight now, our main concern is that we have\x01",
            "no clue where she came from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600039V#6P#0006FTrue...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3600040V#6P#0306FThe fact that she can't remember anything\x01",
            "'sides her name doesn't make it any easier.\x02\x03",
            "#3600041V#0302FStill, you gotta admit that she's the brightest,\x01",
            "friendliest lil' rascal you've ever met.\x02\x03",
            "#3600042VShe's gotten pretty attached to us over the\x01",
            "past week, hasn't she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600043V#6P#0014FIsn't that the truth?\x02\x03",
            "#3600044V#0002FThat includes you and Zeit, too, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600045V#1004F#11PI suppose.\x02\x03",
            "#3600046V#1002FChildren have never really been ones\x01",
            "to approach me, 'cause of my cigarettes.\x02\x03",
            "#3600047VDoesn't seem like she cares, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3600048V#6P#0302FYeah, and I think she's already obsessed\x01",
            "with Mademois-Elie and Tio Tot.\x02\x03",
            "#3600049VLike, I'm pretty sure they hauled in loads\x01",
            "of clothes from Times earlier today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600050V#6P#0004FGood thing we have those two.\x02\x03",
            "#3600051VRandy and I aren't the most detail-\x01",
            "oriented when it comes to that stuff.\x02\x03",
            "#3600052V#0008FBut anyway...all I can think about is\x01",
            "where she could have come from.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Sound(103, 0, 100, 0)
    Fade(500)
    OP_68(59700, 900, 3400, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(21500, 0)
    OP_68(61700, 900, 3400, 1500)
    SetChrPos(0xA, 59000, 0, 3400, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1C198():
        OP_96(0xFE, 0xF104, 0x0, 0xD48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1C198)

    def lambda_1C1B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1C1B2)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    OP_6F(0x1)

    ChrTalk(
        0xA,
        (
            "#3600053V#12P#1110FAha! I found you!\x02\x03",
            "#3600054V#1109FLloyd, look! Look!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1C26E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C26E)

    def lambda_1C27B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1C27B)

    def lambda_1C288():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1C288)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7105", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7105")
    ReplaceBGM("ed7101", "ed7105")
    OP_68(62600, 1200, 5800, 1000)
    MoveCamera(50, 15, 0, 1000)
    SetCameraDistance(23000, 1000)
    SetChrFlags(0xA, 0x40)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x0)

    def lambda_1C2E2():
        OP_95(0xFE, 62600, 0, 5800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1C2E2)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)

    def lambda_1C308():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C308)
    Sound(819, 0, 100, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#3600055V#0011F#5PK-KeA?! What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3600056V#12P#1109FLookie! Elie and Tio picked out a\x01",
            "bunch of clothes for me!\x02\x03",
            "#3600057VI think they're all cute, but this outfit's\x01",
            "my favorite!\x02\x03",
            "#3600058V#1110FWhaddya think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600059V#0012F#5PWell, it's kinda hard to say with you\x01",
            "hugging me like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#3600060V#12P#1105FAw, good point.\x02",
    )

    CloseMessageWindow()
    OP_68(62700, 1200, 4900, 1000)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)

    def lambda_1C49C():
        OP_96(0xFE, 0xF4EC, 0x0, 0x1324, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1C49C)
    WaitChrThread(0xA, 1)
    OP_6F(0x1)

    def lambda_1C4BC():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1C4BC)
    WaitChrThread(0xA, 2)

    def lambda_1C4CD():
        OP_93(0xA, 0x167, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1C4CD)
    Sleep(150)
    Sound(2031, 255, 100, 0)
    WaitChrThread(0xA, 2)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1000)
    SetChrPos(0x103, 64599, 30, 5100, 90)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMessageWindowPos(280, 150, -1, -1)

    NpcTalk(
        0x103,
        "KeA",
        "#3600062V#1POkay, how 'bout now?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(40, 120, -1, -1)

    AnonymousTalk(
        0x101,
        "#3600063V#0002FWow, they did good.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 70, -1, -1)

    AnonymousTalk(
        0x104,
        "#3600064V#0305FWould ya look at that...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(40, 20, -1, -1)

    AnonymousTalk(
        0x8,
        "#3600111V#1002FNot bad.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xA,
        "#3600066V#12P#1110FSo, you like it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600067V#0004F#5PIt's super cute, KeA.\x02\x03",
            "#3600068V#0002FIt definitely suits your personality,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3600069V#12P#1109FYou think?!\x02\x03",
            "#3600070V#1102FRandy, Chief! Do you think I'm cute, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3600071V#5P#0309FYup. Cutest girl in all of Crossbell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3600072V#5P#1002FNot too shabby, kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#3600073V#12P#1109FHeeheehee!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x102, 59000, 0, 3400, 90)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x103, 59000, 0, 3400, 90)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1C7F9():
        OP_95(0xFE, 61600, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C7F9)

    def lambda_1C813():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C813)
    Sleep(700)

    def lambda_1C827():
        OP_95(0xFE, 60000, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C827)

    def lambda_1C841():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1C841)
    WaitChrThread(0x102, 1)

    def lambda_1C856():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C856)
    WaitChrThread(0x103, 1)

    def lambda_1C867():
        OP_95(0xFE, 61000, 0, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C867)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x2D, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#3600074V#12P#0102FLooks like someone couldn't wait\x01",
            "to make her big debut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3600075V#6P#0206FWe wanted her to try on the rest\x01",
            "of the outfits, but she was restless.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x1F4)

    ChrTalk(
        0xA,
        (
            "#3600076V#1110FElie, Tio, guess what? Lloyd and the\x01",
            "others said I'm cute!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3600077V#12P#0109FIsn't that wonderful?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3600078V#6P#0202FI imagine Lloyd would say KeA looks\x01",
            "cute no matter what outfit she wore.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        "#3600079V#0012F#5PThat's...probably true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3600080V#5P#0309FHaha! Would ya look at that? Lloyd's\x01",
            "already a dear, doting father.\x02\x03",
            "#3600081V#0300FHard to believe it's already been a\x01",
            "week since KeDo arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3600082V#12P#0104FWho knew we would win a sweet\x01",
            "girl like her from the auction?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#3600083V#12P#0105FOh, that reminds me...\x02\x03",
            "#3600084V#0101FWhat'd you end up hearing from the\x01",
            "department, Chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3600085V#6P#0200FYou said Revache is trying to extend\x01",
            "an olive branch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3600086V#5P#1003FYeah, let's see here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600087V#0006F#5PDon't worry, I can explain everything\x01",
            "while we have lunch.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(12600, 2350, 4800, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 4600, 270)
    SetChrPos(0x102, 11300, 900, 6650, 90)
    SetChrPos(0x103, 11300, 900, 2550, 90)
    SetChrPos(0x104, 13900, 900, 2550, 270)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x40)
    SetChrChipByIndex(0xA, 0x7)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 11300, 900, 4600, 90)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x1)
    SetChrPos(0x8, 13900, 900, 6650, 270)
    SetChrChipByIndex(0xC, 0x9)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 16000, 850, 6400, 180)
    EndChrThread(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x6)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1400, 6600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrSubChip(0x1A, 0xC)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13400, 1300, 6600, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x24)
    SetChrSubChip(0x1B, 0x6)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12400, 1400, 6600, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x20)
    SetChrSubChip(0x1C, 0xC)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12000, 1300, 6600, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x6)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13000, 1400, 4600, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0xC)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 13400, 1300, 4600, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x24)
    SetChrSubChip(0x1F, 0x6)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 12400, 1400, 4600, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0xC)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 12000, 1300, 4600, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x24)
    SetChrSubChip(0x21, 0x6)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 12400, 1400, 2600, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x20)
    SetChrSubChip(0x22, 0xC)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 12000, 1300, 2600, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x6)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 13000, 1400, 2600, 0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x20)
    SetChrSubChip(0x24, 0xC)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 13400, 1300, 2600, 0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x20)
    SetChrSubChip(0x25, 0x7)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 12700, 1400, 5500, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x7)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 12700, 1400, 3500, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x24)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 16000, 750, 5500, 0)
    OP_68(12600, 1850, 4800, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x102,
        (
            "#3600088V#0104FWell, at least there's some good news.\x02\x03",
            "#3600089V#0100FOur fears of the mafia trying to bite back\x01",
            "seem to have disappeared, at least for\x01",
            "the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3600090V#6P#0208FHowever, there is still such a fundamental\x01",
            "issue to deal with...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600091V#5P#1006FYeah, well, all the decision-making was\x01",
            "left to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600092V#0003F#11PRight now, we should focus on her past\x01",
            "and figuring out where she's from...\x02\x03",
            "#3600093V#0001FHey, KeA. Do you really not remember\x01",
            "anything? Anything at all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3600094V#6P#1100FUmm... Nope, don't think so.\x02\x03",
            "#3600095V#1109FI DO remember seeing your funny face\x01",
            "when you found me, though! Your eyes\x01",
            "and mouth were wiiiiide open!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600096V#0006F#11P*sigh*...\x02\x03",
            "#3600097V#0011FWait, are you talking about when we\x01",
            "first met?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3600098V#6P#1108FYep. I don't really remember anything\x01",
            "before that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600099V#0000F#11PThat's okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3600100V#0304F#11PStill, not much we can do if she doesn't\x01",
            "remember, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3600101V#6P#0200F#6PChief, you mentioned you were going\x01",
            "to ask around about her, correct? Did\x01",
            "that yield any fruit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600102V#5P#1000FAh, about that...\x02\x03",
            "#3600103VI looked into the train station, airport,\x01",
            "even the city exits, but no one knew\x01",
            "anything about our mystery girl.\x02\x03",
            "#3600104V#1003FWho knows? Maybe it's a dead end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600105V#0008F#11PThere goes that plan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3600106V#6P#1105F...?\x02\x03",
            "#3600107V#1101FWhat's wrong, Lloyd? Does your\x01",
            "tummy hurt or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600108V#0012F#11PNo, no, I'm okay.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3600109V#0003F#11PChief, I have a request. From this\x01",
            "afternoon on...\x02\x03",
            "#3600110V#0001F...would you mind if we brought\x01",
            "KeA into the city with us?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#3600065V#5P#1001FHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3600112V#0101FDo you have any potential leads?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#3600113V#0004F#11PSort of...\x02\x03",
            "#3600114V#0000FI was actually thinking of asking\x01",
            "the Bracer Guild for a favor.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#3600115V#0105FExcuse me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3600116V#6P#0205FWhy them, of all people?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#3600117V#6P#1111FThe heck's a brayser?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600118V#5P#1004FClever...\x02\x03",
            "#3600119V#1002FThe guild has branches spanning\x01",
            "the entire continent...\x02\x03",
            "#3600120V...and you want to tap into their\x01",
            "information network.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#3600121V#0006F#11PThat's right. I think if there was ever a\x01",
            "time to turn to it, it'd be now.\x02\x03",
            "#3600122V#0001FSo? Should we go for it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600123V#5P#1002FEh, why not?\x02\x03",
            "#3600124V#1004FIt's not like the CPD and the guild are\x01",
            "enemies, per se.\x02\x03",
            "#3600125VIt's more so that most of the force harbors\x01",
            "petty resentment against their popularity.\x02\x03",
            "#3600126V#1002FA case is a case, and if you asked them\x01",
            "to collaborate, I doubt they'd refuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600127V#0004F#11PThat's what I'm thinking, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3600128V#0300F#11PEstelle and Joshua were pretty friendly\x01",
            "last time we ran into 'em, so maybe this\x01",
            "ain't such a bad idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3600129V#0104FWe could certainly use the assistance.\x02\x03",
            "#3600130V#0101FBut, Lloyd...do you intend to go out\x01",
            "with KeA alone?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#3600131V#0005F#11PThat was the plan.\x02\x03",
            "#3600132V#0000FIt'd probably be overkill if we all went,\x01",
            "so I thought I could go with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3600133V#0103FUnacceptable.\x02\x03",
            "#3600134V#0111FYou know how attached she is to you,\x01",
            "and you STILL want to monopolize her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600135V#0011F#11PUh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3600136V#6P#0206FClever, Lloyd. Very clever.\x02\x03",
            "#3600137V#0211FDo you not think everyone should have\x01",
            "equal opportunities to bond with her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#3600138V#6P#1100FHuuuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600139V#0011F#11PThat's what I want to know, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3600140V#0309F#11PThat right there is pure jealousy, my friend.\x02\x03",
            "#3600141VJust think about the last few days. Whenever\x01",
            "it's time to sleep, KeDo always cuddles up\x01",
            "with you in your room!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3600142V#0006F#5PIt's not like I ask her to! She always\x01",
            "crawls into my bed after I fall asleep...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3600143V#0001F#11PListen, KeA. Why don't you start using\x01",
            "the room we prepared for you? You\x01",
            "don't want it to go to waste, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3600144V#6P#1106FBut when I'm next to you, it makes it\x01",
            "a lot easier to fall asleep.\x02\x03",
            "#3600145V#1112FIf it's annoying, I guess I can stop...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600146V#0011F#11PN-No, I wouldn't call it annoying...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3600147V#0101FDon't be so inconsiderate, Lloyd.\x02\x03",
            "#3600148VShe's probably still anxious from everything\x01",
            "that happened to her, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3600149V#6P#0211FAll she wants is the security of sleeping\x01",
            "next to someone.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3600150V#0012F#11PWh-What do you want from me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600151V#5P#1002FHeh. Cut the girl some slack, kid.\x02\x03",
            "#3600152V#1003FBut as for going outside, you should\x01",
            "at least take someone else with you.\x02\x03",
            "#3600153V#1000FSure, Revache is reaching out to the\x01",
            "department, but for the time being, I\x01",
            "think it'd be better to stay on your toes.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3600154V#0005F#11PYou really think...?\x02\x03",
            "#3600155V#0000FAll right, then. We'll make sure to keep\x01",
            "our eyes peeled.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x32, 0x7D0)
    SetCameraDistance(25500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)
    OP_E3(0xA)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_57(0x3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_E3(0xB)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
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
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 14350, 850, 12060, 180)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWho should Lloyd and KeA travel with?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Elie]\x01",       # 0
            "[Tio]\x01",        # 1
            "[Randy]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E5BF"),
        (1, "loc_1E5E0"),
        (2, "loc_1E601"),
        (SWITCH_DEFAULT, "loc_1E622"),
    )


    label("loc_1E5BF")

    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 4)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Call(0, 41)
    Jump("loc_1E622")

    label("loc_1E5E0")

    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 5)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    Call(0, 42)
    Jump("loc_1E622")

    label("loc_1E601")

    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 6)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Call(0, 43)
    Jump("loc_1E622")

    label("loc_1E622")

    Return()

    # Function_38_1A9A7 end

    def Function_39_1E623(): pass

    label("Function_39_1E623")


    def lambda_1E628():
        OP_96(0xFE, 0x3E98F, 0x0, 0x107AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E628)
    Sleep(300)

    def lambda_1E645():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1E645)
    WaitChrThread(0x102, 1)
    Sound(820, 0, 100, 0)
    OP_63(0xA, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    def lambda_1E677():
        OP_96(0xFE, 0x3E98F, 0x0, 0x10428, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E677)
    WaitChrThread(0x102, 1)

    def lambda_1E695():
        OP_93(0xA, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1E695)
    WaitChrThread(0xA, 2)

    def lambda_1E6A6():
        OP_93(0xA, 0xB5, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1E6A6)
    WaitChrThread(0xA, 2)
    OP_63(0xA, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)
    Return()

    # Function_39_1E623 end

    def Function_40_1E6CE(): pass

    label("Function_40_1E6CE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E6EC")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_40_1E6CE")

    label("loc_1E6EC")

    Return()

    # Function_40_1E6CE end

    def Function_41_1E6ED(): pass

    label("Function_41_1E6ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x1, 0xEF, 0xFF)
    OP_68(1000, 1000, 3700, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 200, 0, 2200, 90)
    SetChrPos(0x102, 1800, 0, 2200, 270)
    SetChrPos(0x153, 1000, 0, 3800, 180)
    Sleep(1000)
    OP_68(1000, 1000, 2700, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3600156V#6P#0000FWell, ready to go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3600157V#0104F#11PThe Bracer Guild is over on East Street.\x02\x03",
            "#3600158V#0100FYou know, maybe detours aren't the best\x01",
            "idea this time around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600159V#6P#0003FBut then again, it might help jog KeA's\x01",
            "memories.\x02\x03",
            "#3600160V#0000FAs long as we're careful, it should be\x01",
            "all right to stop by other places after\x01",
            "the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3600161V#0102F#11POh, I didn't even think of that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x153, 500)

    def lambda_1E934():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E934)
    Sleep(300)

    ChrTalk(
        0x102,
        "#3600162V#0109FSo, KeA, shall we be off?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600207V#1109F#5PYep!\x02\x03",
            "#3600208V#1105FUh, where are we going again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3600165V#0103FIt is called the Bracer Guild.\x02\x03",
            "#3600166V#0100FHave you heard of it before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600211V#1103F#5PBrayser...\x02\x03",
            "#3600212V#1100FHmm, are the people there kinda\x01",
            "like superheroes?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3600169V#12P#0005FYou've heard of it?\x02\x03",
            "#3600170V#0000FMaybe she retained some common\x01",
            "knowledge, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3600171V#0100FYes, it looks like she has.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600216V#1100F#5PHehehe. I dunno why we have to\x01",
            "go there, but...\x02\x03",
            "#3600173V#1109F...if I'm with you two, I'd go anywhere!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(892, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3600174V#12P#0011FM-My heart...\x02",
    )

    CloseMessageWindow()
    OP_64(0x153)

    ChrTalk(
        0x102,
        "#3600175V#0109FOooooh, how is she THIS cute?!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x32, 0x0, 0x3E8, 0xC8)

    ChrTalk(
        0x153,
        "#3600220V#1109F#5P#4SC'mon, let's go!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 1000, 0, 2000, 180)
    SetScenarioFlags(0xA7, 6)
    OP_C7(0x0, 0x1000)
    OP_29(0x47, 0x1, 0x13)
    OP_29(0x48, 0x4, 0x2)
    OP_29(0x48, 0x1, 0x0)
    VolumeBGM(0x64, 0x7D0)
    EventEnd(0x5)
    Return()

    # Function_41_1E6ED end

    def Function_42_1ECE9(): pass

    label("Function_42_1ECE9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x2, 0xEF, 0xFF)
    OP_68(1000, 1000, 3700, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 200, 0, 2200, 90)
    SetChrPos(0x103, 1800, 0, 2200, 270)
    SetChrPos(0x153, 1000, 0, 3800, 180)
    Sleep(1000)
    OP_68(1000, 1000, 2700, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3600177V#6P#0000FWell, ready to go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3600178V#0204F#11PThe Bracer Guild is located on East Street.\x02\x03",
            "#3600179V#0201FPerhaps it would be prudent to avoid any\x01",
            "unnecessary detours this trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600180V#6P#0003FBut on the other hand, it might help\x01",
            "jog KeA's memories.\x02\x03",
            "#3600181V#0000FWe should definitely be careful, but\x01",
            "looking around the city afterwards\x01",
            "shouldn't be too big a deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3600182V#0204F#11PThat is indeed a possibility.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x153, 500)

    def lambda_1EF4B():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EF4B)
    Sleep(300)

    ChrTalk(
        0x103,
        "#3600183V#0202FWell, KeA, are you ready to go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600207V#1109F#5PYep!\x02\x03",
            "#3600208V#1105FUh, where are we going again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3600186V#0205FIt's called the Bracer Guild.\x02\x03",
            "#3600187V#0206FHave you never heard of it\x01",
            "before, KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600211V#1103F#5PBrayser...\x02\x03",
            "#3600212V#1100FHmm, are the people there kinda\x01",
            "like superheroes?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3600190V#12P#0005FYou've heard of it?\x02\x03",
            "#3600191V#0000FMaybe she retained some common\x01",
            "knowledge, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3600192V#0202FWith luck.\x02\x03",
            "#3600193V#0204FIt is possible that information is stored\x01",
            "in her long-term memory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600216V#1100F#5PHeeheehee. I dunno why we have to\x01",
            "go there, but...\x02\x03",
            "#3600195V#1109F...if I'm with you two, I'd go anywhere!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(892, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3600196V#12P#0011FM-My heart...\x02",
    )

    CloseMessageWindow()
    OP_64(0x153)

    ChrTalk(
        0x103,
        (
            "#3600197V#0209FIt should not be possible to have a\x01",
            "smile that pure.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x32, 0x0, 0x3E8, 0xC8)

    ChrTalk(
        0x153,
        "#3600220V#1109F#5P#4SC'mon, let's go!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 1000, 0, 2000, 180)
    SetScenarioFlags(0xA7, 6)
    OP_C7(0x0, 0x1000)
    OP_29(0x47, 0x1, 0x13)
    OP_29(0x48, 0x4, 0x2)
    OP_29(0x48, 0x1, 0x1)
    VolumeBGM(0x64, 0x7D0)
    EventEnd(0x5)
    Return()

    # Function_42_1ECE9 end

    def Function_43_1F36B(): pass

    label("Function_43_1F36B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x3, 0xEF, 0xFF)
    OP_68(1000, 1000, 3700, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 200, 0, 2200, 90)
    SetChrPos(0x104, 1800, 0, 2200, 270)
    SetChrPos(0x153, 1000, 0, 3800, 180)
    Sleep(1000)
    OP_68(1000, 1000, 2700, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3600199V#6P#0000FWell, ready to go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3600200V#0304F#11PThe guild's over on East Street.\x02\x03",
            "#3600201V#0301FBy the way, think we should avoid\x01",
            "goin' on detours or what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600202V#6P#0003FI'm not sure. After all, it might help\x01",
            "jog KeA's memories.\x02\x03",
            "#3600203V#0000FWe should definitely be careful, but\x01",
            "looking around the city afterwards\x01",
            "shouldn't be too big a deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3600204V#0300F#11PGot'cha.\x02\x03",
            "#3600205V#0309FWith you and me around, everything'll\x01",
            "turn out all right.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x153, 500)

    def lambda_1F5ED():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F5ED)
    Sleep(300)

    ChrTalk(
        0x104,
        "#3600206V#0302FOkay, KeDo! Let's roll!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600207V#1109F#5PYep!\x02\x03",
            "#3600208V#1105FUh, where are we going again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3600209V#0305FOh, yeah. It's called the Bracer Guild.\x02\x03",
            "#3600210V#0302FI wouldn't be too surprised if ya didn't\x01",
            "know what it is, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600211V#1103F#5PBrayser...\x02\x03",
            "#3600212V#1100FHmm, are the people there kinda\x01",
            "like superheroes?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3600213V#12P#0005FYou HAVE heard of it?\x02\x03",
            "#3600214V#0000FMaybe she retained some common\x01",
            "knowledge, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3600215V#0300FLooks that way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600216V#1100F#5PI dunno why we have to go\x01",
            "there, but...\x02\x03",
            "#3600217V#1109F...if I'm with you two, I'd go anywhere!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(892, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3600218V#12P#0011FM-My heart...\x02",
    )

    CloseMessageWindow()
    OP_64(0x153)

    ChrTalk(
        0x104,
        (
            "#3600219V#0306FI-I think I finally know what a dad feels\x01",
            "like when he looks at his kid.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x32, 0x0, 0x3E8, 0xC8)

    ChrTalk(
        0x153,
        "#3600220V#1109F#5P#4SC'mon, let's go!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 1000, 0, 2000, 180)
    SetScenarioFlags(0xA7, 6)
    OP_C7(0x0, 0x1000)
    OP_29(0x47, 0x1, 0x13)
    OP_29(0x48, 0x4, 0x2)
    OP_29(0x48, 0x1, 0x2)
    VolumeBGM(0x64, 0x7D0)
    EventEnd(0x5)
    Return()

    # Function_43_1F36B end

    def Function_44_1F9E6(): pass

    label("Function_44_1F9E6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x8, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch50090.itc", 0x20)
    LoadChrToIndex("apl/ch50092.itc", 0x21)
    LoadChrToIndex("chr/ch00802.itc", 0x22)
    LoadChrToIndex("chr/ch08201.itc", 0x23)
    LoadChrToIndex("apl/ch50380.itc", 0x24)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SoundLoad(821)
    OP_32(0x8, 0x0, 0x1D)
    RemoveCraft(0x8, 0xFFFF)
    OP_38(0x8, 0x80, 0x2)
    OP_38(0x8, 0x81, 0x2)
    OP_38(0x8, 0x82, 0x2)
    OP_38(0x8, 0x83, 0x2)
    OP_38(0x8, 0x84, 0x2)
    OP_38(0x8, 0x85, 0x2)
    OP_38(0x8, 0x86, 0x2)
    OP_42(0x8, 0x44D, 0xFF)
    OP_42(0x8, 0x5E9, 0xFF)
    OP_42(0x8, 0x64D, 0xFF)
    AddCraft(0x8, 0xE6)
    AddCraft(0x8, 0xE7)
    AddCraft(0x8, 0xE8)
    AddCraft(0x8, 0x122)
    SetChrChipPat(0x8, 0x6, 0x122)
    AddCraft(0x8, 0x144)
    OP_42(0x8, 0x6F, 0x0)
    OP_42(0x8, 0x92, 0x4)
    OP_42(0x8, 0x7B, 0x3)
    OP_42(0x8, 0x81, 0x2)
    OP_42(0x8, 0x65, 0x1)
    OP_42(0x8, 0x6B, 0x6)
    OP_42(0x8, 0xAC, 0x5)
    OP_68(900, 1000, 400, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 800, 0, 500, 0)
    SetChrPos(0x102, 800, 0, 500, 0)
    SetChrPos(0x103, 800, 0, 0, 0)
    SetChrPos(0x104, 800, 0, 0, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x8000)
    OP_90(0xA, 800, 3000, 14000, 180)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis080.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis081.itp")
    CreatePortrait(2, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis082.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01103.itp")
    OP_68(900, 1000, 2400, 2000)
    SetCameraDistance(25500, 2000)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_1FC3C():
        OP_96(0xFE, 0xC8, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FC3C)

    def lambda_1FC56():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FC56)
    Sleep(250)

    def lambda_1FC6A():
        OP_96(0xFE, 0x514, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FC6A)

    def lambda_1FC84():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1FC84)
    Sleep(400)

    def lambda_1FC98():
        OP_96(0xFE, 0xC8, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1FC98)

    def lambda_1FCB2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1FCB2)
    Sleep(250)

    def lambda_1FCC6():
        OP_96(0xFE, 0x514, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1FCC6)

    def lambda_1FCE0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1FCE0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#4100001V#0000F#12PWe're back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100002V#0309F#12PYo, everyone!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Sound(2036, 255, 90, 0)

    ChrTalk(
        0xA,
        "#4100003V#4P#1110FYay, you're home!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(800, 1900, 8000, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24000, 0)
    BeginChrThread(0xA, 3, 0, 45)

    def lambda_1FDC0():

        label("loc_1FDC0")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_1FDC0")

    QueueWorkItem2(0x102, 2, lambda_1FDC0)

    def lambda_1FDD2():

        label("loc_1FDD2")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_1FDD2")

    QueueWorkItem2(0x104, 2, lambda_1FDD2)
    Sleep(1000)
    Sound(2037, 255, 100, 0)
    WaitChrThread(0xA, 3)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)

    ChrTalk(
        0x101,
        (
            "#4100005V#12P#0014FHaha, nice tackle.\x02\x03",
            "#4100006V#0002FBeen a good girl while we\x01",
            "were gone, KeA?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xA,
        (
            "#4100060V#5PYep!\x02\x03",
            "#4100008VI've been watching over the SSS building\x01",
            "with Zeit aaaaall day long.\x02\x03",
            "#4100009VI even read three books from the\x01",
            "library, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    ChrTalk(
        0x101,
        "#4100010V#12P#0005FWow, that's impressive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100011V#0102F#11PThey may only be children's books,\x01",
            "but she blew through all three of\x01",
            "them this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100012V#0204F#12PI always knew she was quite the intelligent girl.\x01",
            "Seeing such growth in her reading comprehension\x01",
            "has only solidified that sentiment.\x02\x03",
            "#4100013V#0202FShe has a bright future ahead of her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100014V#0306F#11PGeez. Doting parents, each and every\x01",
            "one of ya.\x02\x03",
            "#4100015V#0302FHeh. Not like I'm one to talk.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)

    def lambda_20153():
        OP_96(0xFE, 0xC8, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_20153)
    WaitChrThread(0xA, 1)
    SetChrFlags(0xA, 0x40)

    ChrTalk(
        0xA,
        (
            "#4100016V#1105F#5PHuuuh?\x02\x03",
            "#4100017V#1110FOh, well! I'm too hungry to think about stuff.\x02\x03",
            "#4100018V#1109FWe should make lunch already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100019V#12P#0002FAll right, all right. It's about that time, anyway.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#4100020V#6P#0000FPretty sure it's my day to cook. Is everyone\x01",
            "fine with pasta?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100021V#0102F#11PThat sounds wonderful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100022V#12P#0204FI would eat just about anything you\x01",
            "cook, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100023V#0309F#11PSave me an extra serving or two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100024V#6P#0002FHaha, sure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4100025V#1105F#5PLloyd, you're making lunch?\x02\x03",
            "#4100026V#1109FI wanna help! Please, pleeease!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_20434():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20434)
    Sleep(300)

    ChrTalk(
        0x102,
        "#4100027V#0105F#11PHave you ever cooked before, KeA?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100028V#12P#0200FPerhaps you remember something\x01",
            "from your past involving it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4100029V#1100F#5PNope! In one of the books I was reading,\x01",
            "one of the characters was a chef.\x02\x03",
            "#4100030VAnd the stuff he made looked sooo tasty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100031V#0302F#11PThat explains that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100032V#12P#0000FWell, then, KeA, I don't think I have any\x01",
            "other choice but to take you up on your\x01",
            "offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4100033V#1109F#5PYay! To the kitchen!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(116700, 1200, 6000, 0)
    MoveCamera(60, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 116700, 30, 7600, 0)
    SetChrPos(0xA, 116700, 30, 6400, 0)
    OP_68(116700, 1200, 7000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#4100034V#0003F#11PHmm... We need to decide what kind of\x01",
            "pasta we want to make.\x02\x03",
            "#4100035V#0000FI think we have eggs and bacon from\x01",
            "Armorica Village, so a carbonara wouldn't\x01",
            "be too hard to pull off...\x02\x03",
            "#4100036V...but we also have some canned clams\x01",
            "from Liberl. With those, we could make\x01",
            "some spaghetti alle vongole.\x02\x03",
            "#4100037V#0005FStill, if we don't want to go fancy, we could\x01",
            "always just whip up some meat sauce and\x01",
            "chop some eggplant.\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhich dish do you want to make?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Carbonara]\x01",                   # 0
            "[Spaghetti alle Vongole]\x01",      # 1
            "[Eggplant Ragu]\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2092E"),
        (1, "loc_209A0"),
        (2, "loc_20A27"),
        (SWITCH_DEFAULT, "loc_20ABD"),
    )


    label("loc_2092E")


    ChrTalk(
        0x101,
        (
            "#4100038V#0000F#11PWell, might as well use the eggs while\x01",
            "they're fresh!\x02\x03",
            "#4100041VNow, let's see...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20ABD")

    label("loc_209A0")


    ChrTalk(
        0x101,
        (
            "#4100039V#0000F#11PIt's not every day we have clam, so we\x01",
            "might as well put them to good use!\x02\x03",
            "#4100041VNow, let's see...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20ABD")

    label("loc_20A27")


    ChrTalk(
        0x101,
        (
            "#4100040V#0000F#11PWe should have some ground beef left,\x01",
            "so we might as well make some meat\x01",
            "sauce with that!\x02\x03",
            "#4100041VNow, let's see...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_20ABD")

    label("loc_20ABD")


    ChrTalk(
        0xA,
        (
            "#4100042V#11P#1110FDon't forget about me, Lloyd!\x02\x03",
            "#4100043VWhat should I do?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#4100044V#0002F#5PHmm, would you mind bringing me\x01",
            "the ingredients as I ask for them?\x02\x03",
            "#4100045VI'm just about to start boiling the\x01",
            "noodles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4100046V#11P#1109FOkie dokie!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(122700, 1000, 8300, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 123700, 30, 8300, 0)
    SetChrPos(0xA, 122700, 30, 8300, 0)
    ClearMapObjFlags(0xF, 0x4)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x9)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 123100, 800, 9300, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetMapObjFrame(0xF, "pan00", 0x1, 0x1)
    SetMapObjFrame(0xF, "pan01", 0x0, 0x1)
    SetMapObjFrame(0xF, "kemuri2_add", 0x0, 0x1)
    Sleep(500)
    OP_68(123700, 1000, 8300, 2000)
    Sound(84, 0, 70, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0xA,
        "#4100047V#12P#1100FHehehe...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        "#4100048V#6P#1101FHey, Lloyd! Is it ready yet?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_20E53")

    ChrTalk(
        0x101,
        (
            "#4100049V#11P#0004FA little bit longer. When it comes to cooking\x01",
            "pasta, the amount of time the pasta spends\x01",
            "boiling is key.\x02\x03",
            "#4100050V#0000FOnce it hits that sweet spot, you take it out\x01",
            "of the pot, mix it together with a bunch of\x01",
            "carbonara sauce, scatter in the peppers...\x02\x03",
            "#4100053V#0014F...and bam! It's ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210F0")

    label("loc_20E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_20FA2")

    ChrTalk(
        0x101,
        (
            "#4100049V#11P#0004FA little bit longer. When it comes to cooking\x01",
            "pasta, the amount of time the pasta spends\x01",
            "boiling is key.\x02\x03",
            "#4100051V#0000FOnce it hits that sweet spot, you take it out\x01",
            "of the pot, toss the clams, sauce, and pasta\x01",
            "into the pan, add some garlic and parsley...\x02\x03",
            "#4100053V#0014F...and bam! It's ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210F0")

    label("loc_20FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_210F0")

    ChrTalk(
        0x101,
        (
            "#4100049V#11P#0004FA little bit longer. When it comes to cooking\x01",
            "pasta, the amount of time the pasta spends\x01",
            "boiling is key.\x02\x03",
            "#4100052V#0000FOnce it hits that sweet spot, you take it out\x01",
            "of the pot, throw it in the pan with the meat\x01",
            "sauce and fried eggplant, sprinkle in cheese...\x02\x03",
            "#4100053V#0014F...and bam! It's ready.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_210F0")


    ChrTalk(
        0xA,
        (
            "#4100054V#6P#1105FWooow, that's amazing!\x02\x03",
            "#4100055V#1110FI wanna try doing it! Please, please,\x01",
            "pleeeeease!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0xA, 500)

    ChrTalk(
        0x101,
        (
            "#4100056V#11P#0005FYou do?\x02\x03",
            "#4100057V#0004F(Not sure if this'll work out...but I guess\x01",
            "I'll just keep a close eye on her.)\x02\x03",
            "#4100058V#0000FAll right, then. Give it a try, KeA.\x02\x03",
            "#4100059VMind the flame, though!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4100007V#6P#1109FGot'cha!\x02",
    )

    CloseMessageWindow()
    OP_68(124090, 1000, 8260, 1500)

    def lambda_21289():
        OP_96(0xFE, 0x1E780, 0x1E, 0x206C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21289)
    Sleep(300)

    def lambda_212A6():
        OP_96(0xFE, 0x1E334, 0x1E, 0x206C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_212A6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#4100061V#1101F#11P#30WLemme see...\x02\x03",
            "#4100062V#30WYou said wait for when it hits the\x01",
            "sweet spot, then take it out and...\x01",
            "put it in the pan...\x02\x03",
            "#4100063V#1105F#40W...\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20500, 20000)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)

    ChrTalk(
        0x101,
        (
            "#4100064V#0006F#11P(Looks like she's a little lost.)\x02\x03",
            "#4100065V#0000F(I'm sure everyone will still scarf it down,\x01",
            "even if a few mistakes are made. KeA's\x01",
            "the one making it, after all.)\x02",
        )
    )

    CloseMessageWindow()
    Sound(931, 0, 80, 0)
    VolumeBGM(0x3C, 0x3E8)
    PlayEffect(0x0, 0x0, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1200)
    Sound(2038, 255, 100, 0)

    ChrTalk(
        0xA,
        "#4100066V#11P#1103F#30WI got it!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "KeA gracefully took the perfectly-cooked pasta from\x01",
            "the pot and began to cook it with the other ingredients\x01",
            "in the pan, as if she was an experienced chef.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4100067V#0011F#11PHuh?!\x02",
    )

    CloseMessageWindow()
    Sound(81, 0, 100, 0)
    Sleep(300)
    Fade(500)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(20500, 0)
    SetMapObjFrame(0xF, "pan00", 0x0, 0x1)
    SetMapObjFrame(0xF, "pan01", 0x1, 0x1)
    SetMapObjFrame(0xF, "kemuri2_add", 0x1, 0x1)
    OP_0D()
    OP_6F(0x10)
    CancelBlur(0)
    StopEffect(0x0, 0x2)
    VolumeBGM(0x64, 0x3E8)
    Sleep(1300)
    Sound(2039, 255, 100, 0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xA,
        "#4100068V#11P#1109F#4SMagnifique! It's ready!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_216A8")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jump("loc_2170B")

    label("loc_216A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_216DC")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Jump("loc_2170B")

    label("loc_216DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2170B")
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    label("loc_2170B")

    Sleep(1000)

    AnonymousTalk(
        0x101,
        (
            "#4100069V#0005FThat was incredible, KeA!\x02\x03",
            "#4100070VYou blew my cooking skills out of the\x01",
            "water! How'd you know what to do?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0xA, 0x101, 500)

    AnonymousTalk(
        0xA,
        (
            "#4100071V#1104FI dunno! Something just flashed\x01",
            "in my head, and I did it.\x02\x03",
            "#4100072V#1110FDid I do it wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21840")
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jump("loc_218A3")

    label("loc_21840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_21874")
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Jump("loc_218A3")

    label("loc_21874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_218A3")
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    label("loc_218A3")


    ChrTalk(
        0x101,
        (
            "#4100073V#0004F#11PDefinitely not. I doubt I could ever cook\x01",
            "a dish as amazing as this one.\x02\x03",
            "#4100074V#0000FKeA, have you learned to cook before?\x01",
            "That might explain it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4100075V#6P#1111FHmm. Maybe?\x02\x03",
            "#4100076V#1109FOh, well! I just know that my tummy's\x01",
            "rumbling, so let's go eat!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetMapObjFlags(0xF, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x104, 13900, 900, 4600, 270)
    SetChrPos(0x102, 11300, 900, 6650, 90)
    SetChrPos(0x103, 11300, 900, 2550, 90)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 0x7)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 11300, 900, 4600, 90)
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xC, 0x9)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 16000, 850, 6400, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    BeginChrThread(0xC, 1, 0, 40)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1400, 6600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrSubChip(0x1A, 0xC)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13400, 1300, 6600, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12400, 1400, 6600, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x20)
    SetChrSubChip(0x1C, 0xC)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12000, 1300, 6600, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13000, 1400, 4600, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0xC)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 13400, 1300, 4600, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 12400, 1400, 4600, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0xC)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 12000, 1300, 4600, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 12400, 1400, 2600, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x20)
    SetChrSubChip(0x22, 0xC)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 12000, 1300, 2600, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x21)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 13000, 1400, 2600, 0)
    SetChrChipByIndex(0x24, 0x20)
    SetChrSubChip(0x24, 0xE)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 13400, 1300, 2600, 0)
    SetChrChipByIndex(0x25, 0x20)
    SetChrSubChip(0x25, 0x7)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 12700, 1400, 5500, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x7)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 12700, 1400, 3500, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x21)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 16000, 750, 5500, 0)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21DB1")
    SetChrSubChip(0x19, 0xC)
    SetChrSubChip(0x1B, 0xC)
    SetChrSubChip(0x1D, 0xC)
    SetChrSubChip(0x1F, 0xC)
    SetChrSubChip(0x21, 0xC)
    SetChrSubChip(0x23, 0xC)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrPos(0x19, 13100, 1400, 6600, 0)
    SetChrPos(0x1B, 12300, 1400, 6600, 0)
    SetChrPos(0x1D, 13100, 1400, 4600, 0)
    SetChrPos(0x1F, 12300, 1400, 4600, 0)
    SetChrPos(0x21, 12300, 1400, 2600, 0)
    SetChrPos(0x23, 13100, 1400, 2600, 0)
    Jump("loc_21DF8")

    label("loc_21DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_21DD7")
    SetChrSubChip(0x19, 0xE)
    SetChrSubChip(0x1B, 0xE)
    SetChrSubChip(0x1D, 0xE)
    SetChrSubChip(0x1F, 0xE)
    SetChrSubChip(0x21, 0xE)
    SetChrSubChip(0x23, 0xE)
    Jump("loc_21DF8")

    label("loc_21DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_21DF8")
    SetChrSubChip(0x19, 0xA)
    SetChrSubChip(0x1B, 0xA)
    SetChrSubChip(0x1D, 0xA)
    SetChrSubChip(0x1F, 0xA)
    SetChrSubChip(0x21, 0xA)
    SetChrSubChip(0x23, 0xA)

    label("loc_21DF8")

    Sleep(1000)
    OP_68(12600, 2350, 4800, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    OP_68(12600, 1850, 4800, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2202D")

    ChrTalk(
        0x104,
        (
            "#4100077V#0305F#11PWhoa, what's with this spread?\x02\x03",
            "#4100078VYou're tellin' me KeDo really went\x01",
            "and made all this?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#4100093V#5P#0004FWell, I gathered all the ingredients\x01",
            "and did the prep.\x02\x03",
            "#4100094V#0002FBut after putting the pasta in the pot,\x01",
            "it was all her.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    ChrTalk(
        0x103,
        "#4100081V#12P#0202FImpressive...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#4100082V#0109F#5PAgreed. You could have told me you got\x01",
            "carry-out, and I'd have been fooled.\x02\x03",
            "#4100083V#0102FYou did such a good job, KeA!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223DA")

    label("loc_2202D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_22205")

    ChrTalk(
        0x102,
        (
            "#4100084V#0105F#5PMy tastebuds are having trouble taking\x01",
            "in all the flavor...\x02\x03",
            "#4100085VDid KeA really make all of this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100086V#11P#0004FWell, I gathered all the ingredients\x01",
            "and prepped them.\x02\x03",
            "#4100087V#0000FBut after putting the pasta in the pot,\x01",
            "it was all her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100088V#0305F#11PSeriously?!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#4100089V#12P#0204FFor a moment, I almost mistook the dish\x01",
            "for one served at high-end restaurants...\x02\x03",
            "#4100090V#0202FWell done, KeA.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223DA")

    label("loc_22205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_223DA")
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#4100091V#12P#0205FWhat a delicacy...\x02\x03",
            "#4100092VWas this really made by KeA, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#4100079V#5P#0000FWell, I gathered all the ingredients\x01",
            "and prepped them.\x02\x03",
            "#4100080VBut after putting the pasta in the pot,\x01",
            "it was all her.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    ChrTalk(
        0x102,
        "#4100095V#0102F#5PThis is absolutely superb...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100096V#0305F#11PAin't that the truth? This stuff's on par with\x01",
            "what you get at high-end restaurants.\x02\x03",
            "#4100097V#0309FKeDo, you're somethin' else!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223DA")


    ChrTalk(
        0xA,
        "#4100098V#6P#1109FHeeheehee. Glad ya like it!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#4100099V#5P#0000FWhat if she's the daughter of a family\x01",
            "of professional chefs...?\x02\x03",
            "#4100100V#0006FWell, if she has parents, they must be\x01",
            "freaking out about her by now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100101V#0103F#5P...One would think. However, there's not much\x01",
            "more we can do about it.\x02\x03",
            "#4100102V#0108FEven with the guild's information network\x01",
            "on our side, we still haven't learned anything\x01",
            "substantial yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100103V#6P#0208FShe may have been raised in a remote region\x01",
            "or was swept up in unusual circumstances,\x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4100104V#6P#1100FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100105V#0306F#11PHey, if you start thinkin' like that, we're\x01",
            "never gonna make any progress.\x02\x03",
            "#4100106V#0300FUntil we actually start findin' some clues,\x01",
            "she's our responsibility. Ain't that right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100107V#5P#0004FYeah, you're right.\x02\x03",
            "#4100108V#0002FAt any rate, I feel pretty bad for the\x01",
            "chief right about now.\x02\x03",
            "#4100109VHe totally missed out on trying some\x01",
            "of KeA's delicious, homemade pasta.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100110V#6P#0200FHe is in another meeting at headquarters, right?\x01",
            "There have been a lot of those recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100111V#0105F#5PNow that you mention it, there HAS been,\x01",
            "hasn't there? Could there be something\x01",
            "happening that we aren't aware of?\x02",
        )
    )

    CloseMessageWindow()
    Sound(821, 2, 100, 0)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    OP_70(0xD, 0x0)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x0, 0x14, 0x0, 0x20)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0xA, 0x1)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        "#4100112V#11P#0005FA call? I wonder who it's from...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100113V#0300F#11PDoubt it's the chief or Fran, considerin'\x01",
            "it's not comin' from your Enigma.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 14100, 850, 7600, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_92(0x101, 0x35E8, 0x2EE0, 0x1F4)
    OP_68(13800, 1850, 12000, 2500)

    def lambda_22A4D():
        OP_95(0xFE, 13800, 850, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22A4D)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    OP_6F(0x1)
    ClearMapObjFlags(0xD, 0x20)
    OP_70(0xD, 0x32)
    OP_24(0x335)
    Sound(822, 0, 100, 0)
    FadeToDark(500, 0, 100)
    OP_0D()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100114V#0000FHello, this is the Crossbell Police\x01",
            "Department, Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100115V\x07\x05",
            "Lloyd, is that you?\x02\x03",
            "#4100116VIt's Noel. Um, I mean, Sergeant Major\x01",
            "Seeker from the Guardian Force.\x02",
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
            "#4100117V\x07\x00",
            "#0009FOh, hey! It's been almost a month since\x01",
            "we last talked, right?\x02\x03",
            "#4100118V#0002FDid you need the SSS to help you with\x01",
            "something, Sergeant Major?\x02",
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
            "#4100119V\x07\x05",
            "Yes, actually. U-Umm...\x02\x03",
            "#4100120V...there's something I need a bit of private\x01",
            "advice about, so I decided to call you guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100121V\x07\x00",
            "#0005FPrivate? What's this about?\x02",
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
            "#4100122V\x07\x05",
            "Oh. I say private, but it's still very\x01",
            "much Guardian Force business.\x02\x03",
            "#4100123VI'm, uh, sorry for calling you out of the blue\x01",
            "like this...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100124V\x07\x00",
            "#0004FIt's no big deal. We were in the middle of\x01",
            "having lunch, anyway.\x02\x03",
            "#4100125V#0001FSo, where are you now? If you want to\x01",
            "talk face-to-face, we can make it happen.\x02",
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
            "#4100126V\x07\x05",
            "O-Oh, really?\x02\x03",
            "#4100127VAs of now, I'm at the city's north exit.\x02\x03",
            "#4100128VWould you care if I came to you?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100129V\x07\x00",
            "#0004FFeel free.\x02\x03",
            "#4100130V#0005FBy the way, have you eaten yet?\x02\x03",
            "#4100131VI could whip up some more pasta\x01",
            "for you, if you want.\x02",
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
            "#4100132V\x07\x05",
            "N-No, you don't have to put yourselves\x01",
            "out for me...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(932, 0, 100, 0)
    Sleep(1300)
    Sound(1496, 255, 100, 0)
    Sleep(800)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Noel's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100133V\x07\x05",
            "#2SThanks... I'll start making my way to\x01",
            "the SSS building, if you don't mind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100134V\x07\x00",
            "#0002FAwesome. We'll be waiting for you.\x02",
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
            "#4100135V\x07\x05",
            "See you soon!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(500, 0)
    OP_0D()
    SetMapObjFlags(0xD, 0x4)
    Sound(822, 0, 100, 0)
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_68(12600, 1850, 4800, 2500)

    def lambda_23190():
        OP_95(0xFE, 14100, 850, 7600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23190)
    WaitChrThread(0x101, 1)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x102,
        "#4100136V#0105F#6PWho was that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100137V#11P#0000FSergeant Major Seeker, believe it or not.\x02\x03",
            "#4100138VShe says she needs some advice on\x01",
            "something work-related.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100139V#0305F#11PHer? Shoot, somthing must be up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4100140V#6P#1110FIs someone coming to visit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4100141V#12P#0204FYes, KeA. A girl from the Guardian Force.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x2)
    Sleep(300)

    ChrTalk(
        0xA,
        "#4100142V#6P#1105FGuard-ee-an Force?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#4100143V#5P#0002FShe tried to make it sound like she wasn't\x01",
            "hungry, but I say we make another serving\x01",
            "of pasta for her.\x02\x03",
            "#4100144VUp to the challenge, KeA?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    ChrTalk(
        0xA,
        "#4100145V#6P#1109FLet's do it!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(26000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(13090, 1850, 5300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26000, 0)
    SetChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 13900, 900, 6650, 270)
    ClearChrFlags(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)
    SetChrPos(0x101, 13900, 900, 4600, 270)
    SetChrSubChip(0x101, 0x2)
    SetChrPos(0x104, 13900, 900, 2550, 270)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrSubChip(0x1A, 0x18)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13100, 1300, 7250, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x20)
    SetChrSubChip(0x1C, 0x18)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12300, 1300, 7250, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0x18)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 13100, 1300, 5200, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x18)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 12300, 1300, 5200, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x20)
    SetChrSubChip(0x22, 0x18)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 12300, 1300, 3150, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x21)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x20)
    SetChrSubChip(0x24, 0x18)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 13100, 1300, 3150, 0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_23641")
    SetChrSubChip(0x19, 0xD)
    SetChrSubChip(0x1B, 0xD)
    SetChrSubChip(0x1D, 0xD)
    SetChrSubChip(0x1F, 0xD)
    SetChrSubChip(0x21, 0xD)
    SetChrSubChip(0x23, 0xD)
    Jump("loc_23688")

    label("loc_23641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_23667")
    SetChrSubChip(0x19, 0xF)
    SetChrSubChip(0x1B, 0xF)
    SetChrSubChip(0x1D, 0xF)
    SetChrSubChip(0x1F, 0xF)
    SetChrSubChip(0x21, 0xF)
    SetChrSubChip(0x23, 0xF)
    Jump("loc_23688")

    label("loc_23667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_23688")
    SetChrSubChip(0x19, 0xB)
    SetChrSubChip(0x1B, 0xB)
    SetChrSubChip(0x1D, 0xB)
    SetChrSubChip(0x1F, 0xB)
    SetChrSubChip(0x21, 0xB)
    SetChrSubChip(0x23, 0xB)

    label("loc_23688")

    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 16500, 850, 6400, 225)
    ClearChrFlags(0xC, 0x1)
    OP_CA(0x1, 0x3, 0x0)
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis160.itp")
    Sleep(1000)
    SetCameraDistance(25000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x109,
        "#4100146V#11P#0504FPhew. I suppose I did need that.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#4100147V#5P#0502FI wouldn't have resisted at first had\x01",
            "I known it was going to be so tasty.\x01",
            "Did KeA really make it all on her own?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4100148V#6P#1100FYep, I sure did!\x02\x03",
            "#4100149V#1105FThough, Lloyd did all the...prep? I think\x01",
            "that's what he called it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4100150V#5P#0509FWell, you should be proud!\x02\x03",
            "#4100151V#0504FI've actually been hearing a lot of stories\x01",
            "about you from Fran, but...\x02\x03",
            "#4100152V#0502F...who knew that, on top of being the cutest\x01",
            "thing ever, you were also an amazing cook?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100153V#0002F#11PIt sounds like Fran has taken a real\x01",
            "liking to KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100154V#6P#0204F#NOh, she certainly has. Whenever we\x01",
            "communicate through the terminal,\x01",
            "she always asks to talk to KeA.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#4100155V#5P#0509FAhaha. That sounds like Fran, all right.\x01",
            "She's always had a soft spot for cute kids...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4100156V#6P#1110FHey, Noel! Are you Fran's big sister?\x02\x03",
            "#4100157V'Cause your hair is the same color as hers,\x01",
            "and your faces are so similiar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4100158V#5P#0505FY-You think so?\x02\x03",
            "#4100159V#0502FShe's always been the cuter Seeker sister,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#4100160V#5P#0503FO-Oh, I nearly forgot the reason why\x01",
            "I came here in the first place.\x02\x03",
            "#4100161V#0501FMind if I start explaining the situation,\x01",
            "everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100162V#0001F#11PNo, go ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100163V#0301FIt was about those ruins on the outskirts\x01",
            "of the mountain path, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#4100164V#5P#0508FRight. The thing is...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xDAC)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        "#4100165V#0005F...A ghost?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#4100166V#5P#0503FAllegedly.\x02\x03",
            "#4100167VA ghost or some sort of mythical beast, to be\x01",
            "more specific.\x02\x03",
            "#4100168V#0501FAt the very least, it wasn't seen up until\x01",
            "our investigations started and it never fails\x01",
            "to show up when we do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100169V#0303FSo, the guys over at Bellguard Gate were\x01",
            "in charge of the initial investigation, but\x01",
            "ended up withdrawing.\x02\x03",
            "#4100170V#0301FThat means that Tangram Gate is up\x01",
            "to bat now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4100171V#5P#0501FRight.\x02\x03",
            "#4100172V#0506FI attempted to investigate the place with\x01",
            "a handful of guardsmen yesterday...\x02\x03",
            "#4100173V...but as soon as that creepy monster\x01",
            "showed up, they all got cold feet.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#4100174V#0105F#6PW-Wait a second, Sergeant Major...\x02\x03",
            "#4100175V#0109F...are you, by any chance...asking us\x01",
            "to participate in an exorcism?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#4100176V#11P#0505FN-No, not exactly. The CGF's objective\x01",
            "is to simply perform a thorough search\x01",
            "of the ruins' interior.\x02\x03",
            "#4100177V#0506F...You can't do it, I assume?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100178V#0008F#11PW-Well, I wouldn't say that...\x02\x03",
            "#4100179V#0003FI'm just afraid that we don't have much\x01",
            "experience investigating ruins, that's all.\x02\x03",
            "#4100180V#0000F...But the fact that you turned to us of\x01",
            "all people means that you have some\x01",
            "particular reason, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#4100181V#5P#0500FSharp as always, Lloyd.\x02\x03",
            "#4100182V#0503FRemember when we fought those weird\x01",
            "monsters before?\x02\x03",
            "#4100183V#0501FAnd how our arts were working differently\x01",
            "than usual then?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4100184V#0013F#11PThe threat letter case?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100185V#0105F#6PDon't tell me...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100186V#6P#0203F#NAre you implying that it is the same as our\x01",
            "venture into Stargazer's Tower?\x02\x03",
            "#4100187V#0201FThen you suspect the higher elements may be\x01",
            "active there. Is that correct?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#4100188V#5P#0506FExactly. I couldn't help but be reminded of how\x01",
            "it was back then.\x02\x03",
            "#4100189VBecause of that, I was wondering if I could get\x01",
            "your input and, possibly, your cooperation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100190V#0003F#11PI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100191V#0106F#6PIt makes sense that you'd turn to us, now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4100192V#5P#0508FI'm well aware that you guys are really busy...\x02\x03",
            "#4100193V#0506F...but if nothing gets done, the commander\x01",
            "is probably going to order us to forget it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100194V#0301FWell, he's always been a big advocate of the\x01",
            "'Let sleepin' dogs lie' way of managing, so I\x01",
            "wouldn't be surprised if that's the case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100195V#0003F#11PHmm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#4100196V#0000F#11PSince she came all this way to ask us, why\x01",
            "don't we work together on this?\x02\x03",
            "#4100197VSure, it's outside the city, but the way she's\x01",
            "describing it has me worried.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    ChrTalk(
        0x102,
        "#4100198V#0108F#5PThe similarities ARE staggering.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4100199V#6P#0204F#NI have no objections.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#4100200V#0304F#11PNo problemo.\x02\x03",
            "#4100201V#0302FDoesn't look like Mademois-Elie is too hot\x01",
            "about the idea, though, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100202V#0113F#5PTh-That's not true!\x02\x03",
            "#4100203V#0112FOnly a child would be afraid of\x01",
            "gh-- Never mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100204V#0304F#11PCat's outta the bag.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4100205V#6P#1105FAre you scared of ghosts, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100206V#0109F#5PN-No, that's crazy talk.\x02\x03",
            "#4100207VIt's just that we'll need to be extremely cautious,\x01",
            "going up against an unknown foe and all...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#4100208V#11P#0506FI can't blame you for being scared, Elie.\x02\x03",
            "#4100209VI wouldn't want to go through with all this,\x01",
            "either, if it weren't for my duty.\x02\x03",
            "#4100210V#0508FBut leaving everything as is, as if nothing\x01",
            "happened...? I just can't accept that.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#4100211V#0108F#6P...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#4100212V#0006F#11PI understand that feeling all too well.\x02\x03",
            "#4100213V#0002FYou know, Elie...if you want, you can stay\x01",
            "behind and watch the SSS building...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#4100214V#0113F#5PGeez! All right, fine!\x02\x03",
            "#4100215V#0107FI'm definitely NOT staying behind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4100216V#6P#0202F#NElie, your desperation is showing.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#4100217V#0303F#11PC'mon, Mademois-Elie, I thought you were\x01",
            "supposed to be the composed one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100218V#0113F...Can we move on?\x02\x03",
            "#4100219V#0100FWe've received quite a few other\x01",
            "support requests today. What do\x01",
            "we do? Forget about them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100220V#0003F#11P*sigh* That's a good point...\x02\x03",
            "#4100221V#0008FIt'd probably be tricky to meet up with\x01",
            "her AFTER we take care of them...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#4100222V#5P#0505FOh, if that's the case...\x02\x03",
            "#4100223V#0502F...allow me to accompany you throughout\x01",
            "the rest of the day.\x02\x03",
            "#4100224VI drove my CGF car here, so I can take you\x01",
            "all across Crossbell if you'd like.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4100225V#0005F#11PWhoa. Is that even allowed?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4100226V#5P#0504FIf I'm just using it for transportation, it\x01",
            "shouldn't be a problem.\x02\x03",
            "#4100227V#0500FHow about we head to the ruins after we\x01",
            "finish up the support requests?\x01",
            "That should work, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100228V#0100F#6PI believe so. It'd certainly be more efficient\x01",
            "to use the car, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100229V#6P#0204F#NI, for one, would love to be driven around\x01",
            "by the sergeant major.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#4100230V#0309FHell yeah! Looks like we're finally gettin' the\x01",
            "First Division treatment today, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100231V#0004F#11PIt's decided, then.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#4100232V#0000F#11PKeA, we're going to be out for most of\x01",
            "the afternoon.\x02\x03",
            "#4100233VCould you watch the SSS building with\x01",
            "Zeit for us?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#4100234V#6P#1104FSure!\x02\x03",
            "#4100235V#1110FEveryone, have fun getting rid\x01",
            "of the big bad ghost!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(26000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_57(0x3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_E3(0xB)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7102")
    OP_24(0x335)
    SetScenarioFlags(0x5D, 2)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_1F9E6 end

    def Function_45_25369(): pass

    label("Function_45_25369")

    SetChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)

    def lambda_25380():
        OP_95(0xFE, 800, 850, 10000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_25380)
    WaitChrThread(0xA, 1)
    OP_68(200, 1000, 3500, 1500)
    SetCameraDistance(25000, 1500)

    def lambda_253B8():
        OP_95(0xFE, 200, 0, 3500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_253B8)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    Sound(819, 0, 100, 0)

    def lambda_253E4():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_253E4)
    Sleep(500)
    Return()

    # Function_45_25369 end

    def Function_46_253FC(): pass

    label("Function_46_253FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch50090.itc", 0x20)
    LoadChrToIndex("apl/ch50092.itc", 0x21)
    LoadChrToIndex("apl/ch50011.itc", 0x22)
    SoundLoad(806)
    OP_68(12600, 2350, 4800, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 4600, 270)
    SetChrPos(0x102, 11300, 900, 6650, 90)
    SetChrPos(0x103, 11300, 900, 2550, 90)
    SetChrPos(0x104, 13900, 900, 2550, 270)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 0x7)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 11300, 900, 4600, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 13900, 900, 6650, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0xC, 0x9)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 16000, 850, 6400, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    BeginChrThread(0xC, 1, 0, 40)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x5)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1400, 6600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrSubChip(0x1A, 0xC)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13400, 1300, 6600, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0x5)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12400, 1400, 6600, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x20)
    SetChrSubChip(0x1C, 0xC)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12000, 1300, 6600, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrSubChip(0x1D, 0x5)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13000, 1400, 4600, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0xC)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 13400, 1300, 4600, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x5)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 12400, 1400, 4600, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0xC)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 12000, 1300, 4600, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x5)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 12400, 1400, 2600, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x20)
    SetChrSubChip(0x22, 0xC)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 12000, 1300, 2600, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x21)
    SetChrSubChip(0x23, 0x5)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 13000, 1400, 2600, 0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x20)
    SetChrSubChip(0x24, 0xC)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 13400, 1300, 2600, 0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x20)
    SetChrSubChip(0x25, 0x7)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 12700, 1400, 5500, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x7)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 12700, 1400, 3500, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x21)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 16000, 750, 5500, 0)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    OP_68(12600, 1850, 4800, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#4200001V#0004F#11PThis girl is full of surprises.\x02\x03",
            "#4200002V#0000FYou're telling me that KeA cooked all of\x01",
            "these sunny-side up eggs for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200003V#0102F#5PShe sure did.\x02\x03",
            "#4200004V#0109FHer technique was so good that I found\x01",
            "myself taking mental notes while watching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4200005V#11P#1002FFried eggs with a bit of runny yolk. Nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200006V#0304F#11PGet a load of this bacon, too. It's, like,\x01",
            "perfectly crisp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200007V#6P#0204FShe does seem to have quite the knack for\x01",
            "the culinary arts. Yesterday's cream stew\x01",
            "was basically her own creation.\x02\x03",
            "#4200008V#0202FAre you sure you do not have any prior\x01",
            "cooking experience, KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4200009V#6P#1111FI dunno. Maybe?\x02\x03",
            "#4200010V#1102FWhenever I cook, it's like my hands\x01",
            "are moving on their own...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200011V#0003F#11PWell, I guess it's true that cooking is more\x01",
            "through personal experience than anything\x01",
            "else, but...\x02\x03",
            "#4200012V#0000F(...the fact that she's THIS talented at her\x01",
            "age is pretty amazing.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xA, 0x2)

    ChrTalk(
        0xA,
        (
            "#4200013V#5P#1101FHey, Tio! I was wondering...\x02\x03",
            "#4200014VDo you feel okay today?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    ChrTalk(
        0x103,
        "#4200015V#12P#0205FAh...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x1)
    Sleep(150)

    ChrTalk(
        0x102,
        "#4200016V#0108F#5PYou look fine, as far as I can tell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200017V#0301F#11PBut don'tcha think it'd be better to\x01",
            "take the day off and rest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200018V#6P#0204FNo. I am fine.\x02\x03",
            "#4200019V#0202FAfter all, I went to bed quite a bit\x01",
            "earlier than usual yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4200051V#5P#1000FHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200021V#0000F#5PI don't think we have any urgent requests\x01",
            "to take care of, so we can always wait and\x01",
            "see how you're feeli--\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xA, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)

    ChrTalk(
        0x101,
        "#4200022V#0005F#11POh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200023V#0305F#11PPretty early for that, ain't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200024V#0100F#5PIs it Fran?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200025V#0001F#11PI'll check.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x8)
    OP_24(0x326)
    Sound(804, 0, 100, 0)
    Sound(807, 0, 100, 0)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4200026V\x07\x00",
            "#0000FHello, this is Lloyd Bannings, of the\x01",
            "Special Suppo--\x02",
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
            "#4200027V\x07\x05",
            "Yeah, yeah, I know already!\x02\x03",
            "#4200028VNow, where the heck are you? What\x01",
            "are you doing right now?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4200029V\x07\x00",
            "#0005FJ-Jona...?\x02\x03",
            "#4200030V#0002FWow, I wasn't expecting a night owl\x01",
            "like yourself to be awake this early\x01",
            "in the morning.\x02",
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
            "#4200031V\x07\x05",
            "Hah! Implying I didn't pull an all-nighter!\x02\x03",
            "#4200032VBut enough about that! It doesn't matter!\x02\x03",
            "#4200033VFrom how carefree you sound, I bet you\x01",
            "don't know anything at all, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4200034V\x07\x00",
            "#0005FDon't know what, exactly?\x02",
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
            "#4200035V\x07\x05",
            "So you don't know. Well, then, I, the great and\x01",
            "brilliant Jona, will do you a favor!\x02\x03",
            "#4200036VIn the dead of night yesterday... Well, technically\x01",
            "today, I guess, but that's beside the point.\x02\x03",
            "#4200037VEither way, someone raided Heiyue's office!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4200038V\x07\x00",
            "#0013FWhat?!\x02",
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
            "#4200039V\x07\x05",
            "They were caught completely off guard,\x01",
            "too! No offense, all defense, y'know?\x02\x03",
            "#4200040VApparently, they took some SERIOUS\x01",
            "damage.\x02\x03",
            "#4200041VIf you ask me, it had to have been done\x01",
            "by those Revache guys!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4200042V\x07\x00",
            "#0003FIt's not outside the realm of possibility...\x02\x03",
            "#4200043V#0000FThanks for the heads-up, Jona.\x02",
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
            "#4200044V\x07\x05",
            "Haha! You owe me one, Lloyd!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(825, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)

    ChrTalk(
        0x103,
        "#4200045V#6P#0205FThat was Jona?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sound(807, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#4200046V#0006F#11PYeah. Something crazy's popped up.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd relayed the information he heard from Jona\x01",
            "to the rest of the Special Support Section.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#4200047V#0101F#5PI-Is that really true, Lloyd?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200048V#0301F#11PThat's freakin' insane!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200049V#6P#0206FIt is bold to pull such a thing in the city,\x01",
            "even if it was in the middle of the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4200050V#6P#1105FWhaaat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200020V#5P#1003FHmm...\x02\x03",
            "#4200052VIf true, I'd bet anything that the First Division\x01",
            "has already jumped on the case.\x02\x03",
            "#4200053V#1002FIf it bothers you that much, go check it out.\x01",
            "But only after you finish eating.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        "#4200054V#0001FWill do, sir!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#4200055V#0005F#5POh, right. Will you be good to go, Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200056V#6P#0204FYes, of course.\x02\x03",
            "#4200057V#0202FWe can walk over to the Harbor District\x01",
            "after we finish our breakfast.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(26000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
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
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_68(12000, 1850, 8700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrPos(0x1, 12000, 850, 8700, 270)
    SetChrPos(0x2, 12000, 850, 8700, 270)
    SetChrPos(0x3, 12000, 850, 8700, 270)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x4)
    OP_4C(0xA, 0xFF)
    SetChrPos(0xA, 122940, 0, 5100, 180)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x8, 124620, 30, 5490, 90)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2970, 0, 4170, 225)
    SetScenarioFlags(0xC2, 2)
    OP_C7(0x1, 0x1000)
    OP_29(0x4A, 0x1, 0x7)
    OP_29(0x4B, 0x4, 0x2)
    OP_29(0x4B, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26B95")
    OP_29(0x2A, 0x4, 0x40)
    Jump("loc_26BA7")

    label("loc_26B95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26BA7")
    OP_29(0x2A, 0x4, 0x40)

    label("loc_26BA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26BC5")
    OP_29(0x2C, 0x4, 0x40)
    Jump("loc_26BD7")

    label("loc_26BC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26BD7")
    OP_29(0x2C, 0x4, 0x40)

    label("loc_26BD7")

    OP_24(0x326)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_46_253FC end

    def Function_47_26BE0(): pass

    label("Function_47_26BE0")

    SetChrSubChip(0x9, 0x0)
    TalkEnd(0x9)
    EventBegin(0x0)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, 57000, -1030, 3400, 90)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, 59000, 30, 3400, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xA, 0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis087.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00600.itp")
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#4200622V#5P#1001F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200623V#12P#0005FUm...Chief?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200624V#0106FS-Sorry. Was it too convoluted, after all?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4200625V#5P#1003FNope.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#4200626V#5P#1001FIt's just, this series of events...\x02\x03",
            "#4200627VI'm starting to think that it might\x01",
            "all be connected.\x02",
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
        "#4200675V#12P#0011FYou do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200629V#0307FSeriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200630V#0101FHow do you figure that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200631V#12P#0208F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200632V#5P#1003FI know a lot's gone down in the last day\x01",
            "or two...\x02\x03",
            "#4200633V...but I want you to try to connect the dots.\x02\x03",
            "#4200634V#1002FBetter buckle up, Lloyd. We're going to need\x01",
            "those detective skills you've been honing if\x01",
            "we want to get anywhere with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200635V#12P#0011FS-Sure, leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#4200636V#12P#0008FToday, we were able to discover roughly\x01",
            "three pieces of key evidence.\x02\x03",
            "#4200637V#0003FThe information we heard from Cao about\x01",
            "the raid on Heiyue...\x02\x03",
            "#4200638V...the intel we exchanged with Grace about\x01",
            "the current state of Revache...\x02\x03",
            "#4200639V#0001F...and everything we learned about Gantz,\x01",
            "the miner from Mainz.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_271E6():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_271E6)
    Sleep(50)

    def lambda_271F6():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_271F6)
    Sleep(50)

    def lambda_27206():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_27206)
    WaitChrThread(0x102, 2)

    ChrTalk(
        0x102,
        (
            "#4200640V#0100FSo there has to be something that ties the\x01",
            "three things together, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200641V#0300FHmm... Y'know, I'm not there just yet, but\x01",
            "I'm starting to see the big picture here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#4200642V#6P#0000FFor now, let's sort through what we know.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 3)

    label("loc_2732D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277D6")
    SetScenarioFlags(0x0, 3)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhich element of the info regarding the raid\x01",
            "on Heiyue can be tied to the others?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Assailants' physical abilities\x01",      # 0
            "Heiyue reinforcements\x01",               # 1
            "Informant's relation to KeA\x01",         # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27424")
    ClearScenarioFlags(0x0, 3)

    label("loc_27424")

    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhich element of the info regarding Revache\x01",
            "can be tied to the others?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Don Marconi's actions\x01",           # 0
            "Investment in war hounds\x01",        # 1
            "Haphazard chain of command\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_274F1")
    ClearScenarioFlags(0x0, 3)

    label("loc_274F1")

    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhich element of the info regarding Gantz\x01",
            "can be tied to the others?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "When he disappeared from Mainz\x01",                 # 0
            "Poker match against Lechter at the casino\x01",      # 1
            "Blue pills in Gantz's possession\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_275DC")
    ClearScenarioFlags(0x0, 3)

    label("loc_275DC")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2774A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_276AC")
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#4200643V#0006F#6P(Hmm... Yeah, that doesn't really line up.)\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)

    ChrTalk(
        0x101,
        "#4200644V#0005F#6P(How about this...?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_27745")

    label("loc_276AC")


    ChrTalk(
        0x101,
        (
            "#4200645V#6P#0006F(No, I don't see how that would fit the\x01",
            "rest of the information.)\x02\x03",
            "#4200646V#0001F(Let's think through this again.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27745")

    Jump("loc_277D1")

    label("loc_2774A")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2775A"),
        (SWITCH_DEFAULT, "loc_27790"),
    )


    label("loc_2775A")

    OP_2C(0x4C, 0x2)

    ChrTalk(
        0x101,
        "#4200647V#6P#0000F(This has to be it.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_277D1")

    label("loc_27790")

    OP_2C(0x4C, 0x1)

    ChrTalk(
        0x101,
        "#4200648V#6P#0003F(...Pretty sure this is right.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_277D1")

    label("loc_277D1")

    Jump("loc_2732D")

    label("loc_277D6")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "[Related Elements]\x01",
            "① Assailants' physical abilities\x01",
            "② Haphazard chain of command\x01",
            "③ Blue pills in Gantz's possession\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#4200649V#0101FYou think these factors overlap?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200650V#0310FThey're definitely suspicious, that's for sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200651V#6P#0006FI think so, Elie. If we take a closer look, we\x01",
            "can see certain things linking the cases.\x02\x03",
            "#4200652V#0008FThe enhanced strength displayed by the\x01",
            "mafiosos who raided Heiyue...\x02\x03",
            "#4200653VGantz and his spontaneous gambling skills...\x02\x03",
            "#4200654V#0013FThey may seem independent of each other,\x01",
            "but they both deal with the augmentation of\x01",
            "their hidden potential.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#4200655V#0013FNow, suppose we say that the connecting\x01",
            "factor in all this are these blue pills...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#4200656V#0203F...The mafia must have started acting as the\x01",
            "distributor for these illegal drugs.\x02\x03",
            "#4200657VAnd the general public were not the only ones\x01",
            "affected by them. Revache must have been\x01",
            "using them to strengthen its henchmen.\x02\x03",
            "#4200658V#0201FIs that the general idea, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#4200659V#0006FYeah, more or less. But, in the end, it's\x01",
            "still just another theory.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0x102,
        (
            "#4200660V#0101FHowever, if that's how it is, wouldn't it\x01",
            "explain a lot?\x02\x03",
            "#4200661VMaybe that's why Garcia's influence\x01",
            "has started to wane...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200662V#0306FSo a bunch of those mafiosos took\x01",
            "the drugs to toughen up and, as a\x01",
            "result, it gave 'em all big egos.\x02\x03",
            "#4200663V#0301FIs that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200664V#5P#1003FNicely put, everyone.\x02\x03",
            "#4200665V#1000FBy the way, remember the rumors Ian\x01",
            "told us about yesterday?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_27E58():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27E58)
    Sleep(150)

    def lambda_27E68():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_27E68)

    def lambda_27E75():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_27E75)
    Sleep(50)

    def lambda_27E85():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_27E85)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x101,
        "#4200666V#12P#0005FOf course! The trader and that stockbroker...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200667V#0105FYou think those two are already under\x01",
            "the influence of the pills?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200668V#5P#1006FWho can say? At this point, that's nothing\x01",
            "more than pure speculation.\x02\x03",
            "#4200669V#1003FHowever, things are beginning to come\x01",
            "together, piece by piece...\x02\x03",
            "#4200670V#1002FYou feel the same way, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200671V#12P#0006FI do.\x02\x03",
            "#4200672V#0008FBut if I'm being honest, I don't think the Special\x01",
            "Support Section will be able to handle a case\x01",
            "of this size.\x02\x03",
            "#4200673V#0001FWe might even need to call in the First Division\x01",
            "for support, given that the incidents revolve\x01",
            "around the distribution of illegal drugs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4200674V#5P#1004FHeh. Perfect timing, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200628V#12P#0005FPerfect timing? What are you...?\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_68(63000, 1100, 4600, 2000)
    MoveCamera(60, 17, 0, 2000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    def lambda_281E4():
        OP_95(0xFE, 62000, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_281E4)

    def lambda_281FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_281FE)
    WaitChrThread(0xA, 1)
    TurnDirection(0xA, 0x101, 500)
    OP_6F(0x41)

    ChrTalk(
        0xA,
        "#4200676V#12P#1110FOh, I found you!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_28290():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28290)
    Sleep(50)

    def lambda_282A0():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_282A0)
    Sleep(50)

    def lambda_282B0():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_282B0)
    Sleep(50)

    def lambda_282C0():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_282C0)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x101,
        "#4200677V#0005F#5PWhat's wrong, KeA?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200678V#5P#0100FAre you getting hungry?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4200679V#12P#1103FNope, not yet! I brought a visitor.\x02\x03",
            "#4200680V#1105FHe's super grumpy, but he said he\x01",
            "really needed to talk to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200681V#0001F#5PGrumpy...?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    Sleep(150)
    Sound(1561, 255, 100, 0)
    Sleep(1000)
    SetChrPos(0x16, 59000, 30, 3400, 90)

    def lambda_283FF():

        label("loc_283FF")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_283FF")

    QueueWorkItem2(0xA, 2, lambda_283FF)

    def lambda_28411():
        OP_95(0xFE, 61800, 0, 3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_28411)

    def lambda_2842B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_2842B)
    Sleep(300)

    def lambda_2843F():
        OP_96(0xFE, 0xF8D4, 0x0, 0xD48, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2843F)
    WaitChrThread(0x16, 1)
    TurnDirection(0x16, 0x9, 500)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0xA, 1)

    ChrTalk(
        0x101,
        "#4200804V#0011F#5POh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200684V#5P#0105FDetective Dudley!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4200685V#1002F#5P#NYou're late.\x02",
    )

    CloseMessageWindow()
    OP_68(64000, 1100, 8600, 2000)
    MoveCamera(50, 17, 0, 2000)

    def lambda_2855A():

        label("loc_2855A")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_2855A")

    QueueWorkItem2(0x101, 2, lambda_2855A)

    def lambda_2856C():

        label("loc_2856C")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_2856C")

    QueueWorkItem2(0x102, 2, lambda_2856C)

    def lambda_2857E():

        label("loc_2857E")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_2857E")

    QueueWorkItem2(0x103, 2, lambda_2857E)

    def lambda_28590():

        label("loc_28590")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_28590")

    QueueWorkItem2(0x104, 2, lambda_28590)

    def lambda_285A2():
        OP_95(0xFE, 62800, 0, 7200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_285A2)
    Sleep(500)

    def lambda_285BF():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_285BF)
    Sleep(100)

    def lambda_285DC():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_285DC)
    Sleep(100)

    def lambda_285F9():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_285F9)
    Sleep(100)

    def lambda_28616():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28616)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xA, 0x2)
    OP_6F(0x41)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x16,
        (
            "#4200686VApologies, Sergei. Investigation meeting ran\x01",
            "a bit long.\x02\x03",
            "#4200687VIf this is about the same thing we discussed\x01",
            "earlier, do you mind if we go ahead and begin?\x02",
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
        0x9,
        (
            "#4200688V#5P#1003FSounds good to me.\x02\x03",
            "#4200689V#1002FFill them in, too, if you don't mind.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#4200690V#12P#0601FI don't exactly have time for jokes, Sergei!\x02\x03",
            "#4200691VThis isn't something rookies should know\x01",
            "about, and--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200692V#5P#1004FActually, I think the information they've\x01",
            "found will end up being pretty useful to\x01",
            "you and your investigation.\x02\x03",
            "#4200693V#1000FC'mon, it won't take any time at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#4200694V#12P#0605FAre you insane...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x16,
        (
            "#4200695V#6P#0601FThen again, I did leave the Heiyue investigation\x01",
            "to the Special Support Section.\x02\x03",
            "#4200696V#0608FPerhaps it should be fine, then... N-No!\x01",
            "What in the world am I saying?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x16)

    ChrTalk(
        0x101,
        (
            "#4200697V#11P#0006FUm, Chief...\x02\x03",
            "#4200698V#0000FIf we're that much of a bother, we can\x01",
            "always just leave the room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200699V#5P#1003FNope. Stay right where you are.\x02\x03",
            "#4200700V#1002FThey don't call Dudley the ace of the\x01",
            "First Division for nothing, after all.\x02\x03",
            "#4200701VI'm sure he realizes what he needs\x01",
            "in a situation like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#4200702V#6P#0603FTch. You win this time.\x02\x03",
            "#4200703V#0601FListen up. The information I'm about to\x01",
            "disclose is strictly confidential...\x02\x03",
            "#4200704V#0607FIt does not leave this room, otherwise\x01",
            "there WILL be consequences! Got it?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200705V#11P#0005FY-Yeah. That won't be a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4200706V#1110FOoooh, is this a secret? I love secrets!\x02\x03",
            "#4200707V#1109FTell me, too!\x02",
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
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1000)

    def lambda_28D8D():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28D8D)

    def lambda_28D9A():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_28D9A)

    def lambda_28DA7():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_28DA7)

    def lambda_28DB4():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_28DB4)

    def lambda_28DC1():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_28DC1)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x101,
        "#4200708V#5P#0012FW-Well, the thing is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200709V#5P#0102FThere should be some leftover sweets\x01",
            "in the kitchen. Why don't you go share\x01",
            "some with Zeit, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xBB8)
    WaitBGM()
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_68(63880, 1100, 8580, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x16, 65300, 0, 6900, 270)
    SetChrPos(0x101, 62700, 0, 6300, 90)
    SetChrPos(0x102, 62700, 0, 7500, 90)
    SetChrPos(0x103, 61400, 0, 6500, 90)
    SetChrPos(0x104, 61400, 0, 7700, 90)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4200710V#0013FThe First Division is being pressured\x01",
            "from the inside?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x16,
        (
            "#4200711V#0603F#11PWell, it's not quite as simple\x01",
            "as that, Bannings...\x02\x03",
            "#4200712V#0601FAfter the raid on Heiyue, we received orders to\x01",
            "devote all our resources to quell any disputes\x01",
            "between them and the mafia.\x02\x03",
            "#4200713V#0606FSo, we recently had to end on our investigation\x01",
            "into the mystery drugs circulating throughout\x01",
            "Crossbell.\x02",
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#4200714V#6P#0011FReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200715V#6P#0205FThe First Division was investigating the\x01",
            "blue pills, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#4200716V#0603F#11PIndeed. It's been a few days since\x01",
            "the decision was made now.\x02\x03",
            "#4200717V#0600FFrankly, I'm shocked that you were\x01",
            "able to uncover as much as you did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200718V#5P#1001FHow exactly did the First Division find\x01",
            "out about the drugs in the first place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#4200719V#0603FWe were tipped off about them by a longtime\x01",
            "informant of ours.\x02\x03",
            "#4200720V#0600FOf course, we couldn't act on her word alone,\x01",
            "so we did some digging of our own...\x02\x03",
            "#4200721VAnd from what we could gather, it just seemed\x01",
            "like a silly urban legend.\x02\x03",
            "#4200722V#0606FI mean, medicine that grants wishes and can\x01",
            "bestow happiness?\x02\x03",
            "#4200723VNevertheless, we couldn't ignore drug trafficking\x01",
            "allegations and were in the middle of compiling a\x01",
            "list of involved citizens before it was put on ice.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x16,
        (
            "#4200724V#0605F#11PWhat? Why are all of you looking at me\x01",
            "like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200725V#5P#1003FLooks like we hit the jackpot.\x02\x03",
            "#4200726V#1000FShow him, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200727V#6P#0003FYes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#4200728V#0605F#11P...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x16, 0)

    def lambda_29628():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29628)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#4200729V#6P#0001FTake a look at this, Detective.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(300)
    Sound(1558, 255, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    AnonymousTalk(
        0x16,
        (
            "#4200730V#0607F#4S...!\x02\x03",
            "#4200731VAre these what I think they are?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#4200732V#0006FWe found them on a certain source\x01",
            "during our investigation today.\x02\x03",
            "#4200733V#0001FWe were allowed to keep them on the condition\x01",
            "that we protect their identity.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)

    def lambda_297D8():
        OP_96(0xFE, 0xF4EC, 0x0, 0x189C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_297D8)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained in great detail what had transpired\x01",
            "prior to Dudley.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#4200734V#0608F#11PDamn it all. So it is real.\x02\x03",
            "#4200735V#0610FAnd you're saying that it's possible\x01",
            "that Revache is the distributor?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200736V#5P#1003FDudley, about the order to stop\x01",
            "the drug investigation...\x02\x03",
            "#4200737V#1000FAny idea who made the call?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#4200738V#0606FIt had to have been someone high up.\x02\x03",
            "#4200739V#0608FOur chief didn't agree with the decision,\x01",
            "but he enforced it nonetheless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4200740V#5P#1006FWhat a mess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200741V#6P#0105FWait a moment, please.\x02\x03",
            "#4200742V#0110FDoes that mean someone high on the\x01",
            "CPD's chain of command gave in to the\x01",
            "mafia's demands?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)
    OP_64(0x16)

    ChrTalk(
        0x101,
        "#4200743V#6P#0006FThat's unbelievable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200744V#6P#0301FC'mon, how low can you go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200745V#6P#0206FThe situation appears quite grave.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200746V#5P#1003FHey, Dudley.\x02\x03",
            "#4200747V#1000FIt's clear that you came to me because\x01",
            "you don't trust the department brass.\x02\x03",
            "#4200748VThat being said, what's your move?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#4200749V#0608F...\x02\x03",
            "#4200750V#0606FTo be honest, I didn't intend to do anything\x01",
            "about the drug investigation.\x02\x03",
            "#4200751VIf any of us were to take action, our bosses\x01",
            "would do whatever they could to interfere.\x02\x03",
            "#4200752V#0610FBut, as a member of the police, it'd\x01",
            "be too frustrating to let this go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200753V#6P#0005FDetective Dudley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200754V#5P#1002FEasy, then. Leave the investigation\x01",
            "to the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x9, 0x2)
    Sleep(300)

    ChrTalk(
        0x9,
        "#4200755V#5P#1000FLloyd, Elie. You, too, Randy and Tio.\x02",
    )

    CloseMessageWindow()

    def lambda_29E4D():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29E4D)
    Sleep(50)

    def lambda_29E5D():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_29E5D)
    Sleep(50)

    def lambda_29E6D():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_29E6D)
    Sleep(50)

    def lambda_29E7D():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_29E7D)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#4200756V#5P#1003FFrom here on out, the SSS will be informally\x01",
            "collaborating with the First Division.\x02\x03",
            "#4200757V#1001FYou four will take over their investigation into\x01",
            "these drugs in their stead, since they currently\x01",
            "have their hands tied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200758V#12P#0001FYes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200759V#12P#0101FUnderstood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4200760V#5P#1003FAnd in return...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x9, 0x0)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#4200761V#5P#1002F...we'll get every bit of intel the First Division\x01",
            "has about Revache. Sound fair?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x16, 0x9, 500)

    def lambda_2A096():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A096)
    Sleep(50)

    def lambda_2A0A6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2A0A6)
    Sleep(50)

    def lambda_2A0B6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2A0B6)
    Sleep(50)

    def lambda_2A0C6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2A0C6)
    Sleep(150)

    ChrTalk(
        0x16,
        (
            "#4200762V#0605FSergei?!\x02\x03",
            "#4200763VRegardless of the circumstances, we can't\x01",
            "just go handing out top secret intelligence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200764V#5P#1002FCan't say I particularly care, Dudley.\x02\x03",
            "#4200765VYou're stuck in a stalemate and you know\x01",
            "it. But by all means, do whatever strikes\x01",
            "your fancy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#4200766V#0601FTch...\x02\x03",
            "#4200767V#0606FFine. You can have whatever information\x01",
            "your grubby hands want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4200768V#5P#1002FHeh. Glad we could come to an agreement.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200769V#6P#0309FOooh, so we're doin' the First Division's\x01",
            "work for 'em now, is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200770V#6P#0204FI can feel the superiority washing over\x01",
            "me already.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x16, 0x10E, 0x1F4)

    ChrTalk(
        0x16,
        "#4200771V#0610F#11P*glare*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200772V#6P#0305FYikes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200773V#6P#0206FComment retracted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#4200774V#0603F#11PHmph. Whatever.\x02\x03",
            "#4200775V#0601FAll right, you gained my permission to handle\x01",
            "the drug investigation.\x02\x03",
            "#4200776VHow do you actually plan on proceeding, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200777V#6P#0003FAbout that...\x02\x03",
            "#4200778V#0001FWe already hold the key in our hands.\x02\x03",
            "#4200779VAll we need to do is figure out what the\x01",
            "drug is made of, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#4200780V#0600F#11PNot a bad start. Do you have any idea how\x01",
            "to determine that? Who to go to?\x02\x03",
            "#4200781VBased on what we know, we can assume\x01",
            "that this is a new, never-before-seen drug.\x02\x03",
            "#4200782VUsing the forensic tools back at HQ is out\x01",
            "of the question, as I have no experience\x01",
            "with them and would be easily caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200783V#6P#0008FWell, there goes that idea.\x02\x03",
            "#4200784V#0000FYou know, maybe we should just ask\x01",
            "the medical college for assistance.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2A75E")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#4200785V#5P#0100FYou must be talking about that doctor,\x01",
            "right, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A841")

    label("loc_2A75E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2A7DC")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#4200786V#6P#0202FAh, I see. You must be talking about\x01",
            "that particular doctor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A841")

    label("loc_2A7DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2A841")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        "#4200787V#3P#0300FI think we know just the guy, eh, Lloyd?\x02",
    )

    CloseMessageWindow()

    label("loc_2A841")


    ChrTalk(
        0x16,
        (
            "#4200788V#0605F#11PMedical college...? You're referring to\x01",
            "St. Ursula, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A89E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2A89E)

    def lambda_2A8AB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2A8AB)

    def lambda_2A8B8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2A8B8)

    ChrTalk(
        0x101,
        (
            "#4200789V#6P#0004FRight. We know a doctor there who specializes\x01",
            "in pharmaceutical research, actually.\x02\x03",
            "#4200790V#0000FI've heard nothing but good things about his\x01",
            "work, so there might be a good chance he\x01",
            "could figure out the drug's composition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#4200791V#0600F#11PHmph. That's a stroke of good luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200792V#5P#1003FAnd it might just be our best option.\x02\x03",
            "#4200793V#1000FIf you can, could you put together a report\x01",
            "of the First Division's intel and send it to us\x01",
            "by the end of the day?\x02\x03",
            "#4200794VI want them to decide how to approach\x01",
            "the investigation for themselves.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x9, 500)
    Sleep(150)

    ChrTalk(
        0x16,
        (
            "#4200795V#0600FFine. I'll send it over as soon as I can.\x02\x03",
            "#4200796V#0604FWell, then, I should go. Thank you\x01",
            "for your cooperation, Sergei.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200797V#5P#1004FLikewise.\x02\x03",
            "#4200798V#1002FOh, and don't forget to give them well\x01",
            "wishes, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#4200799V#0610FUgh...\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)
    OP_93(0x16, 0x10E, 0x1F4)

    ChrTalk(
        0x16,
        (
            "#4200800V#0603FListen well, you four.\x02\x03",
            "#4200801V#0601FIf you do anything stupid, this entire\x01",
            "situation might nosedive. Understand?\x02\x03",
            "#4200802V#0607FNotwithstanding your investigation into\x01",
            "the drugs, leave dealing with the mafia\x01",
            "to the First Division!\x02\x03",
            "#4200803VStay close to the ground, behave, and\x01",
            "most importantly, don't get in our way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200683V#6P#0005F...\x02",
    )

    CloseMessageWindow()

    def lambda_2ADB7():

        label("loc_2ADB7")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_2ADB7")

    QueueWorkItem2(0x101, 2, lambda_2ADB7)

    def lambda_2ADC9():

        label("loc_2ADC9")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_2ADC9")

    QueueWorkItem2(0x102, 2, lambda_2ADC9)

    def lambda_2ADDB():

        label("loc_2ADDB")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_2ADDB")

    QueueWorkItem2(0x103, 2, lambda_2ADDB)

    def lambda_2ADED():

        label("loc_2ADED")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_2ADED")

    QueueWorkItem2(0x104, 2, lambda_2ADED)
    OP_92(0x16, 0xF230, 0xD48, 0x1F4)
    OP_68(62000, 1100, 5500, 2000)

    def lambda_2AE1D():
        OP_95(0xFE, 62000, 0, 3400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2AE1D)
    WaitChrThread(0x16, 1)

    def lambda_2AE3B():
        OP_95(0xFE, 59000, 0, 3400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2AE3B)
    Sleep(500)
    SetChrSubChip(0x9, 0x2)
    Sound(103, 0, 100, 0)

    def lambda_2AE62():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_2AE62)
    WaitChrThread(0x16, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    OP_6F(0x1)
    Sound(104, 0, 100, 0)
    Sleep(500)
    Fade(500)
    OP_68(63500, 1100, 9000, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23000, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#4200805V#5P#0302FGeez. That goof just can't be honest\x01",
            "with his feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200806V#5P#0204FAnger is one way of hiding one's\x01",
            "embarrassment, is it not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200807V#5P#0109FMaybe so.\x02\x03",
            "#4200808V#0102FAlso, he has a stronger sense of justice\x01",
            "than I initially presumed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200809V#11P#0002FYeah. I think we can trust him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200810V#5P#1004FI'd vouch for him. Hell, most of the First\x01",
            "Division is driven by diligence and their\x01",
            "distaste for injustice, same as Dudley.\x02\x03",
            "#4200811VSadly, most of them are sticklers for the\x01",
            "rules, making them pretty obstinate.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x9, 0x0)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#4200812V#5P#1005FSo, you going to head to St. Ursula\x01",
            "right away?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B15C():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B15C)
    Sleep(100)

    def lambda_2B16C():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2B16C)
    Sleep(50)

    def lambda_2B17C():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2B17C)
    Sleep(50)
    TurnDirection(0x104, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#4200813V#12P#0000FThat's the plan, at least.\x02\x03",
            "#4200814VWell, if we have some time, I'm sure we'll\x01",
            "try to knock out a few support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200815V#0106F#6PAfter all, we didn't have time to leave\x01",
            "the city this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200816V#6P#0300FSounds like it's about to get busy!\x01",
            "I say we just tackle the requests\x01",
            "little by little as the day goes on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200817V#5P#1004FHeh. Glad to see you're all raring to go.\x02\x03",
            "#4200818V#1002FNow, I know we're cooperating with the\x01",
            "First Division, but don't get too excited.\x02\x03",
            "#4200819VJust do things as you'd usually do.\x01",
            "Show me that you're capable of cracking\x01",
            "the mystery behind these drugs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200820V#12P#0000FUnderstood!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_68(64000, 1330, 5500, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 64000, 30, 5500, 180)
    SetChrPos(0x1, 64000, 30, 5500, 180)
    SetChrPos(0x2, 64000, 30, 5500, 180)
    SetChrPos(0x3, 64000, 30, 5500, 180)
    SetChrSubChip(0x9, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0xC3, 0)
    OP_29(0x4A, 0x4, 0x10)
    OP_29(0x4B, 0x4, 0x10)
    OP_29(0x4C, 0x4, 0x2)
    OP_29(0x4C, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_47_26BE0 end

    def Function_48_2B4F3(): pass

    label("Function_48_2B4F3")

    EventBegin(0x0)
    Fade(1000)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#4200821V#5P#1000FSt. Ursula Medical College, huh?\x02\x03",
            "#4200822VThis doctor you mentioned... That's the guy\x01",
            "who looked into KeA's amnesia, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200823V#12P#0000FYes, sir. Doctor Joachim Guenter, an associate professor\x01",
            "of pharmacology and neurology at St. Ursula.\x02\x03",
            "#4200824VWhen we last spoke, it was clear that he knew\x01",
            "his stuff when it came to pharmacology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200825V#5P#1003FWell, then. He should be reliable for this kind\x01",
            "of thing, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4200826V#12P#0005FWhat's the matter, Chief?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200827V#0101FIs something bothering you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200828V#5P#1006FYou could say that.\x02\x03",
            "#4200829V#1003FStrength, speed, concentration, and intuition.\x02\x03",
            "#4200830VSupposedly, those are what the drug is able\x01",
            "to augment.\x02\x03",
            "#4200831V#1001FBut is it able to increase your luck?\x02",
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
        "#4200832V#12P#0011FW-Well, I'm not sure about that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200833V#0106FRationally speaking, you would think that\x01",
            "it would be impossible...\x02\x03",
            "#4200834V#0101FBut how would that explain Gantz's\x01",
            "miraculous luck at the casino?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200835V#0303FYeah, gamblin' is a tricky thing. You can't keep\x01",
            "winning on intuition and strategy alone. There's\x01",
            "always an element of luck.\x02\x03",
            "#4200836V#0308FAnd that just begs the question, was it Aidios\x01",
            "or demons whisperin' in his ear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200837V#12P#0208F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4200838V#5P#1003FSounds like there's still a few more mysteries\x01",
            "to be solved.\x02\x03",
            "#4200839V#1000FTio. If you're up to the task, I want you to look\x01",
            "into that for me, as thoroughly as you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200840V#12P#0203FVery well. I was already planning to, anyway.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_2BC6D():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BC6D)
    Sleep(50)

    def lambda_2BC7D():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BC7D)
    Sleep(50)

    def lambda_2BC8D():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BC8D)
    Sleep(200)

    ChrTalk(
        0x101,
        "#4200841V#5P#0005F(Why is he asking only Tio...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200842V#5P#0105F(Perhaps he knows something we don't.)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 64000, 30, 5500, 180)
    SetScenarioFlags(0xC3, 1)
    EventEnd(0x5)
    Return()

    # Function_48_2B4F3 end

    def Function_49_2BD27(): pass

    label("Function_49_2BD27")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(800, 1700, 3400, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(23220, 0)
    SetChrPos(0x101, 800, 0, 2400, 0)
    SetChrPos(0x102, -500, 0, 1300, 0)
    SetChrPos(0x103, 1000, 0, 4500, 180)
    SetChrPos(0x104, 1400, 0, 1500, 0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, 3000, 0, 4700, 225)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, 0, 0, 4600, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xE, -320, 0, 5900, 168)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    OP_68(800, 1300, 3400, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#4300001V#0006F#11PAre you sure you're okay, Tio?\x02\x03",
            "#4300002V#0001FYou can always wait here with the chief and\x01",
            "KeA if you don't feel well enough to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300003V#0204F#5PYour worry is unwarranted, I assure you.\x02\x03",
            "#4300004V#0202FI was able to turn in early and get a good\x01",
            "night's rest. I am feeling much better\x01",
            "than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300005V#0002F#11PWell, you DO look a lot better.\x02\x03",
            "#4300006V#0006FBut I was still pretty surprised when\x01",
            "KeA said she wanted to sleep next\x01",
            "to you last night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4300007V#5P#1100FMy gut told me to do it!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 500)

    ChrTalk(
        0xA,
        "#4300008V#6P#1101FHey, Tio. Did you sleep good?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xA, 500)

    ChrTalk(
        0x103,
        (
            "#4300009V#11P#0202FYes, of course.\x02\x03",
            "#4300010V#0204FI can only imagine the reason I am in\x01",
            "such pristine condition is because\x01",
            "I spent so much time with you, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4300011V#6P#1109FHeeheehee. Yay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4300012V#12P#0309FYou're a lifesaver, kiddo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300013V#12P#0109FIndeed. It's as if she's our very own\x01",
            "special pick-me-up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300014V#0004FOh#11P... That reminds me.\x02\x03",
            "#4300015V#0008FI want you to promise me this one\x01",
            "thing, Tio.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2C2AC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2C2AC)
    Sleep(100)
    OP_93(0xA, 0xB4, 0x1F4)

    ChrTalk(
        0x103,
        "#4300016V#0205F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300017V#0006F#11PIf something like yesterday happens\x01",
            "again, please tell us about it.\x02\x03",
            "#4300018VDon't bottle it up. That'll only make it\x01",
            "that much harder on yourself.\x02\x03",
            "#4300019V#0001FI don't mean to be harsh, but if you\x01",
            "were to collapse in the middle of a\x01",
            "fight, we'd all be in trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300020V#0204F#5PRoger. I will keep that in mind.\x02\x03",
            "#4300021VI'm a member of the Special Support Section,\x01",
            "and I intend to stand on equal footing with the\x01",
            "rest of you.\x02\x03",
            "#4300022V#0214FSo, if you would...please share your burdens\x01",
            "and pain with me, too. I will do everything in\x01",
            "my power to ease them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4300023V#12P#0102FTio...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4300024V#12P#0309FHaha. Your wish is my command!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300025V#0002F#11PYeah, you can count on it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4300026V#5P#1105FWow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4300027V#5P#1009FHeh. Well, I doubt you need this old\x01",
            "man to participate.\x02\x03",
            "#4300028V#1002FSo, you're planning to question some\x01",
            "of the citizens suspected of drug use\x01",
            "this morning, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C697():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C697)
    Sleep(50)

    def lambda_2C6A7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2C6A7)
    Sleep(50)

    def lambda_2C6B7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2C6B7)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#4300029V#6P#0003FYes, sir. I want to confirm what we found\x01",
            "in the First Division's report, if possible.\x02\x03",
            "#4300030V#0000FAnd since we'll be busy anyway, we hope\x01",
            "to take care of support requests as they\x01",
            "come our way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300031V#6P#0203FIndeed. If we let this opportunity slip away,\x01",
            "we might not have any time left to venture\x01",
            "outside of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300032V#12P#0306FAs of now, we wanna look into that stockbroker\x01",
            "in the Residential District and that errand boy\x01",
            "from the Saber Vipers...\x02\x03",
            "#4300033V#0301FAnd finally, Arc en Ciel's new cast member.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C961")
    OP_2C(0x4C, 0x2)

    ChrTalk(
        0x102,
        (
            "#4300034V#0106F#6PThey were all acting a little strange\x01",
            "yesterday, weren't they?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA2E")

    label("loc_2C961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C9D5")

    ChrTalk(
        0x102,
        (
            "#4300035V#0101F#6PIt's not surprising the First Division\x01",
            "was able to pick up on this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA2E")

    label("loc_2C9D5")

    OP_2C(0x4C, 0x1)

    ChrTalk(
        0x102,
        (
            "#4300036V#0108F#6PA number of people were acting\x01",
            "pretty strangely yesterday...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA2E")


    ChrTalk(
        0x8,
        (
            "#4300037V#5P#1003FIf you have time, you should go check in with\x01",
            "Ian, too.\x02\x03",
            "#4300038V#1001FOut of the two he told us about, it looks like\x01",
            "the stockbroker is the same one from the\x01",
            "First Division's records.\x02\x03",
            "#4300039VAnd as for the trading company manager, it\x01",
            "doesn't look like anyone has any substantial\x01",
            "information on him yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300040V#6P#0003FThanks for the advice. We'll make it a\x01",
            "priority to stop by there.\x02\x03",
            "#4300041V#0001FDoctor Guenter should be contacting us\x01",
            "later with the drug composition results.\x01",
            "Around noon, I think.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2CCB8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2CCB8)
    Sleep(50)

    def lambda_2CCC8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2CCC8)
    Sleep(50)

    def lambda_2CCD8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2CCD8)
    Sleep(50)

    def lambda_2CCE8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2CCE8)
    Sleep(300)
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
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4300042V\x07\x00",
            "#0001FHello, this is Lloyd Bannings, of the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Mayor's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4300043V\x07\x05",
            "Lloyd? It's me, Bickson from Mainz.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4300044V\x07\x00",
            "#0005FOh, hello, sir.\x02\x03",
            "#4300045V#0000FThis is good timing, actually. How's\x01",
            "Gantz been holding up?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Mayor's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4300046V\x07\x05",
            "Y-Yes, about that...\x02\x03",
            "#4300047VHe, um, seems to have disappeared again.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4300048V\x07\x00",
            "#0013FWhat?!\x02\x03",
            "#4300049V#0001FCan you fill us in on the details?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Mayor's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4300050V\x07\x05",
            "Of course. You see, Gantz woke up late into\x01",
            "the night, but...\x02\x03",
            "#4300051V...he kept fading in and out of consciousness,\x01",
            "so we coaxed him into sleeping again.\x02\x03",
            "#4300052VJust to be safe, I stayed with him overnight,\x01",
            "hoping to report back to you in the morning.\x02\x03",
            "#4300053VBut when I awoke in the morning, Gantz was\x01",
            "nowhere to be found.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4300054V\x07\x00",
            "#0003FI see.\x02\x03",
            "#4300055V#0001FHave you called the hotel or the casino?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Mayor's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4300056V\x07\x05",
            "Yes, but I was told that no one has seen him\x01",
            "for quite some time...\x02\x03",
            "#4300057VWhat do you think we should do, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4300058V\x07\x00",
            "#0003FSir, if you don't mind, I want you to stay\x01",
            "at the hotel.\x02\x03",
            "#4300059VIt's possible that Gantz might come back.\x02\x03",
            "#4300060V#0000FWe were already going out to gather some\x01",
            "information, so we'll make sure to keep an\x01",
            "eye out for anything involving him.\x02\x03",
            "#4300061VIf something comes up, please don't hesitate\x01",
            "to give us another call.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Mayor's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4300062V\x07\x05",
            "A-All right. Thank you, everyone!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayBGM("ed7103", 0)
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
            "#4300063V#12P#0101FDid I hear that right? Gantz disappeared\x01",
            "again?\x02",
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
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#4300064V#0006F#5PYeah. Apparently, he snuck out of the hotel\x01",
            "this morning.\x02\x03",
            "#4300065V#0008FEither by his own accord, or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300066V#0201F#5PIn any case, we will need to check on the\x01",
            "others' conditions as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4300067V#12P#0301FMan, I gotta bad feelin' about this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4300068V#5P#1003FThe situation might be escalating faster\x01",
            "than we anticipated.\x02\x03",
            "#4300069V#1000FDon't worry about things here. Just go\x01",
            "and see what you can find.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D5E6():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D5E6)
    Sleep(50)

    def lambda_2D5F6():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2D5F6)
    Sleep(50)

    def lambda_2D606():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2D606)
    Sleep(300)

    ChrTalk(
        0x101,
        "#4300070V#6P#0000FYes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4300071V#5P#1109FHave a good daaaaay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#4300072V#1200F#5PWoof!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23720, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_68(800, 1000, 2000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 750, 0, 3410, 180)
    SetChrPos(0x1, 750, 0, 3410, 180)
    SetChrPos(0x2, 750, 0, 3410, 180)
    SetChrPos(0x3, 750, 0, 3410, 180)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 257620, 350, 68650, 270)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, 256820, 30, 69850, 180)
    SetScenarioFlags(0xC3, 6)
    OP_29(0x4C, 0x1, 0x5)
    OP_29(0x4C, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D795")
    OP_29(0x2D, 0x4, 0x40)
    Jump("loc_2D7A7")

    label("loc_2D795")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7A7")
    OP_29(0x2D, 0x4, 0x40)

    label("loc_2D7A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D7C5")
    OP_29(0x30, 0x4, 0x40)
    Jump("loc_2D7D7")

    label("loc_2D7C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7D7")
    OP_29(0x30, 0x4, 0x40)

    label("loc_2D7D7")

    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_49_2BD27 end

    def Function_50_2D7DD(): pass

    label("Function_50_2D7DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch08702.itc", 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xB)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xC)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, 256000, 0, 68700, 90)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x1)
    SetChrPos(0xF, 257550, 400, 68700, 270)
    SetChrChipByIndex(0xC, 0x6)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, 256000, 0, 67200, 45)
    BeginChrThread(0xC, 3, 0, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_68(258000, 1000, 68700, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    OP_68(257000, 1000, 68700, 2000)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_63(0xA, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(100)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(300)
    OP_63(0xA, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(500)
    OP_63(0xF, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    def lambda_2D9CA():
        OP_93(0xA, 0x10E, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2D9CA)
    WaitChrThread(0xA, 2)

    def lambda_2D9DB():
        OP_93(0xA, 0x59, 0x320)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2D9DB)
    WaitChrThread(0xA, 2)
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0xF, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_68(256000, 1000, 68700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(12600, 2350, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    OP_68(12600, 1850, 5600, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#5100213V#11P#0003F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100214V#0103F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100215V#6P#0206F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100216V#6P#0306F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        (
            "#5100217V#6P#0307FAaargh! He's gotta be messin' with us\x01",
            "at this point, right?!\x02\x03",
            "#5100218V#0301FLike, wasn't Guenter going to contact\x01",
            "us at noon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100219V#0108F#11PYes, he was. I called the hospital, but\x01",
            "apparently he's shut himself up in his\x01",
            "lab, conducting all sorts of experiments...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100220V#6P#0203FThe doctor may have run into trouble\x01",
            "while analyzing the drug's composition.\x02\x03",
            "#5100221V#0211FThen again, he very well may have let\x01",
            "his lazy nature take over and left to fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100222V#11P#0012FY-Yeah, I don't think that's the case this\x01",
            "time, Tio...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 19000, 850, 3500, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_68(14200, 1850, 5000, 2500)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)
    Sleep(300)

    def lambda_2DDFE():
        OP_96(0xFE, 0x3A34, 0x352, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2DDFE)

    def lambda_2DE18():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2DE18)
    WaitChrThread(0x8, 2)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x13B, 0x1F4)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#5100223V#12P#1005FHmm? That doctor still hasn't got back\x01",
            "to you with the results?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100224V#5P#0006FNo, sir. According to St. Ursula, he's holed\x01",
            "himself up in his lab, running test after test.\x02\x03",
            "#5100225V#0000FIf things continue like this, it might be better\x01",
            "to go talk to him face-to-face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100226V#12P#1003FHmm. Possibly.\x02\x03",
            "#5100227V#1000FI want to know what that drug's made of\x01",
            "before anyone else gets hurt.\x02\x03",
            "#5100228VYou four hurry to St. Ursula. Leave\x01",
            "coordinating with the guild to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100229V#0100F#5PThank you, Chief. We'll leave right away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100230V#6P#0300FThen I guess we'd better go catch a\x01",
            "bus down to the St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 256490, 30, 69370, 180)
    SetChrChipByIndex(0xF, 0x3)
    SetChrSubChip(0xF, 0x0)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x1)
    SetChrPos(0xF, 257350, 0, 68870, 225)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 255850, 0, 67920, 225)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_68(12000, 1850, 8700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrPos(0x1, 12000, 850, 8700, 270)
    SetChrPos(0x2, 12000, 850, 8700, 270)
    SetChrPos(0x3, 12000, 850, 8700, 270)
    SetScenarioFlags(0xE0, 0)
    OP_C7(0x1, 0x1000)
    OP_29(0x4C, 0x1, 0x1B)
    OP_29(0x4D, 0x4, 0x2)
    OP_29(0x4D, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E270")
    OP_29(0x2B, 0x4, 0x40)

    label("loc_2E270")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E282")
    OP_29(0x2F, 0x4, 0x40)

    label("loc_2E282")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x33, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E294")
    OP_29(0x33, 0x4, 0x40)

    label("loc_2E294")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E2B2")
    OP_29(0x28, 0x4, 0x40)
    Jump("loc_2E2C4")

    label("loc_2E2B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2C4")
    OP_29(0x28, 0x4, 0x40)

    label("loc_2E2C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E2E2")
    OP_29(0x2E, 0x4, 0x40)
    Jump("loc_2E2F4")

    label("loc_2E2E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2F4")
    OP_29(0x2E, 0x4, 0x40)

    label("loc_2E2F4")

    Sleep(1000)
    EventEnd(0x5)
    Return()

    # Function_50_2D7DD end

    def Function_51_2E2FA(): pass

    label("Function_51_2E2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E3C6")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FWe should probably check on the support\x01",
            "requests before we head out...\x02\x03",
            "Who knows? Something urgent may have\x01",
            "popped up since we last checked.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)
    Jump("loc_2E4A6")

    label("loc_2E3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E4A6")
    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#1000FWhere do you think you're going?\x02\x03",
            "Hurry up and check these support requests.\x01",
            "All you have to do is log in to the terminal\x01",
            "and see what they're about.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)

    label("loc_2E4A6")

    Return()

    # Function_51_2E2FA end

    def Function_52_2E4A7(): pass

    label("Function_52_2E4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E587")
    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#1000FWhere do you think you're going?\x02\x03",
            "Hurry up and check these support requests.\x01",
            "All you have to do is log in to the terminal\x01",
            "and see what they're about.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 11000, 850, 11350, 180)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)

    label("loc_2E587")

    Return()

    # Function_52_2E4A7 end

    def Function_53_2E588(): pass

    label("Function_53_2E588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E668")
    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#1000FWhere do you think you're going?\x02\x03",
            "Hurry up and check these support requests.\x01",
            "All you have to do is log in to the terminal\x01",
            "and see what they're about.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 17000, 850, 4000, 270)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)

    label("loc_2E668")

    Return()

    # Function_53_2E588 end

    def Function_54_2E669(): pass

    label("Function_54_2E669")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E726")
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
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    label("loc_2E726")

    Return()

    # Function_54_2E669 end

    def Function_55_2E727(): pass

    label("Function_55_2E727")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E7D8")

    ChrTalk(
        0x101,
        (
            "#0000FThis way's the back door to the SSS building.\x02\x03",
            "Since we're taking KeA to the Bracer Guild,\x01",
            "we should probably just leave through the\x01",
            "front door.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ED98")

    label("loc_2E7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E916")

    ChrTalk(
        0x101,
        (
            "#0005FWait. We should stop by the orbal\x01",
            "store before exploring the city.\x02\x03",
            "#0000FI'm pretty sure it's on the northeast\x01",
            "corner of Central Square.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E8B4")

    ChrTalk(
        0x103,
        "#0200FRoger. Ready when you are.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E911")

    label("loc_2E8B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E8E7")

    ChrTalk(
        0x104,
        "#0300FGot'cha. Let's roll!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E911")

    label("loc_2E8E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E911")

    ChrTalk(
        0x102,
        "#0100FOff we go, then.\x02",
    )

    CloseMessageWindow()

    label("loc_2E911")

    Jump("loc_2ED98")

    label("loc_2E916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2ED98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EC8D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E9F2")

    ChrTalk(
        0x101,
        (
            "#0000FThis is the SSS building's rear entrance.\x02\x03",
            "In order to get the lay of the land better,\x01",
            "we should probably use the front door.\x01",
            "That one leads right to Central Square.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC85")

    label("loc_2E9F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EAD7")

    ChrTalk(
        0x102,
        "#0100FIsn't this the SSS building's back door?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, but we should probably head out\x01",
            "through the front door. It'll be easier to\x01",
            "get our bearings that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FThe front door it is, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EC85")

    label("loc_2EAD7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EBB2")

    ChrTalk(
        0x103,
        (
            "#0200FI believe this is the SSS building's\x01",
            "rear entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, but we should probably head out\x01",
            "through the front door. It'll be easier to\x01",
            "get our bearings that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FRoger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EC85")

    label("loc_2EBB2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EC85")

    ChrTalk(
        0x104,
        "#0300FOh, ain't this the back door?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, but we should probably head out\x01",
            "through the front door. It'll be easier to\x01",
            "get our bearings that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FWhatever you say, Leader.\x02",
    )

    CloseMessageWindow()

    label("loc_2EC85")

    SetScenarioFlags(0x1, 3)
    Jump("loc_2ED98")

    label("loc_2EC8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED2E")

    ChrTalk(
        0x101,
        (
            "#0000FCentral Square is right outside the front door.\x02\x03",
            "And if it's up to me to show everyone around,\x01",
            "that'll be the best place to start.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ED98")

    label("loc_2ED2E")


    ChrTalk(
        0x101,
        (
            "#0000FCentral Square is right outside the front door.\x02\x03",
            "Follow me, and I'll show you around the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ED98")

    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_55_2E727 end

    def Function_56_2EDAF(): pass

    label("Function_56_2EDAF")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2EDF7")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a vacant room that is kept locked.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EFD5")

    label("loc_2EDF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EFA4")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#0000FThis room's empty, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FIt seems so. The building is a bit dated,\x01",
            "but it's impressive just how many rooms\x01",
            "it holds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FTell me about it. I could be wrong, but I think\x01",
            "the Crossbell Times used this building as their\x01",
            "main office. When I lived here, at least.\x02\x03",
            "#0003FI know it's locked, but we might as well try to\x01",
            "clean this room out on one of our days off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4A, 5)
    Jump("loc_2EFD5")

    label("loc_2EFA4")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a vacant room that is kept locked.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EFD5")

    TalkEnd(0xFF)
    Return()

    # Function_56_2EDAF end

    def Function_57_2EFD9(): pass

    label("Function_57_2EFD9")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F050")
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

    label("loc_2F050")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F06C")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2F06C")

    Return()

    # Function_57_2EFD9 end

    def Function_58_2F06D(): pass

    label("Function_58_2F06D")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F0E4")
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

    label("loc_2F0E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F100")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2F100")

    Return()

    # Function_58_2F06D end

    def Function_59_2F101(): pass

    label("Function_59_2F101")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F178")
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

    label("loc_2F178")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F194")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2F194")

    Return()

    # Function_59_2F101 end

    def Function_60_2F195(): pass

    label("Function_60_2F195")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F20C")
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

    label("loc_2F20C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F228")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2F228")

    Return()

    # Function_60_2F195 end

    SaveToFile()

Try(main)
