from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c011c.bin",                # FileName
        "c011c",                    # MapName
        "c011c",                    # Location
        0x0009,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 9, 0, 1, 0, 2],
    )

    BuildStringList((
        "c011c",                  # 0
        "Chief Sergei",           # 1
        "Chief Sergei",           # 2
        "Zeit",                   # 3
        "Coppe",                  # 4
        "Billy",                  # 5
        "Colin",                  # 6
        "Harold",                 # 7
        "Sophia",                 # 8
        "Estelle",                # 9
        "Joshua",                 # 10
        "Zeit",                   # 11
        "Tableware",              # 12
        "Tableware",              # 13
        "Tableware",              # 14
        "Tableware",              # 15
        "Tableware",              # 16
        "Tableware",              # 17
        "Tableware",              # 18
        "Tableware",              # 19
        "Tableware",              # 20
        "Tableware",              # 21
        "イス",                   # 22
        "金の薔薇のカード",       # 23
        "ノーパソ",               # 24
        "SE制御",                 # 25
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch02502.itc",                   # 01
        "chr/ch39200.itc",                   # 02
        "chr/ch02707.itc",                   # 03
        "apl/ch50092.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
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

    DeclNpc(0,       0,       0,       0,    385,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(64000,   200,     11399,   180,  469,  0x0, 0,   1,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(123940,  0,       5840,    225,  404,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(123139,  0,       7639,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 42,  7.0,                   10.5,                  0.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -3.5,                  -2.0999999046325684,   -0.0,                  1.0])

    DeclActor(18240,   850,     7560,    1000,    18240,   1850,    7560,    0x007C, 0,  3,  0x0000)
    DeclActor(64000,   30,      9800,    1500,    64000,   1500,    11400,   0x007E, 0,  4,  0x0000)
    DeclActor(-12920,  0,       7560,    2000,    -12920,  0,       7560,    0x007C, 0,  46, 0x0000)
    DeclActor(16960,   850,     10840,   2000,    16960,   1300,    10840,   0x007C, 0,  8,  0x0000)
    DeclActor(180910,  0,       62020,   1500,    180910,  1500,    62020,   0x007C, 0,  45, 0x0000)
    DeclActor(19980,   0,       63920,   1500,    19980,   1500,    63920,   0x007C, 0,  45, 0x0000)
    DeclActor(175940,  0,       63930,   1500,    175940,  1500,    63930,   0x007C, 0,  45, 0x0000)
    DeclActor(-3150,   0,       122280,  1200,    -3150,   1000,    122280,  0x007C, 0,  56, 0x0000)
    DeclActor(-2300,   0,       129960,  1200,    -2300,   2000,    129960,  0x007C, 0,  57, 0x0000)
    DeclActor(155150,  30,      129699,  1200,    153340,  2029,    130490,  0x007C, 0,  58, 0x0000)
    DeclActor(155120,  30,      123880,  1200,    155120,  2029,    123880,  0x007C, 0,  59, 0x0000)
    DeclActor(207280,  30,      128039,  1200,    208840,  3000,    130410,  0x007C, 0,  60, 0x0000)
    DeclActor(209020,  0,       126830,  1200,    209210,  2000,    127040,  0x007C, 0,  61, 0x0000)
    DeclActor(51920,   0,       130570,  1200,    51920,   2500,    130570,  0x007C, 0,  62, 0x0000)
    DeclActor(52900,   0,       124470,  1200,    53700,   2000,    125270,  0x007C, 0,  63, 0x0000)
    DeclActor(2750,    0,       125420,  1200,    2750,    1500,    125420,  0x007C, 0,  65, 0x0000)
    DeclActor(153580,  30,      127880,  1200,    153370,  1530,    128389,  0x007C, 0,  66, 0x0000)
    DeclActor(207040,  30,      128539,  1200,    207640,  1500,    129090,  0x007C, 0,  67, 0x0000)
    DeclActor(48000,   30,      127860,  1200,    47560,   1500,    128630,  0x007C, 0,  68, 0x0000)

    ScpFunction((
        "Function_0_7E8",          # 00, 0
        "Function_1_8A0",          # 01, 1
        "Function_2_CA0",          # 02, 2
        "Function_3_EFF",          # 03, 3
        "Function_4_FE7",          # 04, 4
        "Function_5_FEB",          # 05, 5
        "Function_6_1305",         # 06, 6
        "Function_7_131B",         # 07, 7
        "Function_8_13C4",         # 08, 8
        "Function_9_1A65",         # 09, 9
        "Function_10_2CD6",        # 0A, 10
        "Function_11_2CF5",        # 0B, 11
        "Function_12_4F00",        # 0C, 12
        "Function_13_5B69",        # 0D, 13
        "Function_14_6C23",        # 0E, 14
        "Function_15_6CB0",        # 0F, 15
        "Function_16_7973",        # 10, 16
        "Function_17_798E",        # 11, 17
        "Function_18_7DE3",        # 12, 18
        "Function_19_A094",        # 13, 19
        "Function_20_A0AF",        # 14, 20
        "Function_21_A0D8",        # 15, 21
        "Function_22_E2EB",        # 16, 22
        "Function_23_E340",        # 17, 23
        "Function_24_E392",        # 18, 24
        "Function_25_118BF",       # 19, 25
        "Function_26_118D9",       # 1A, 26
        "Function_27_118F4",       # 1B, 27
        "Function_28_11949",       # 1C, 28
        "Function_29_1199E",       # 1D, 29
        "Function_30_119F3",       # 1E, 30
        "Function_31_11A48",       # 1F, 31
        "Function_32_11AC4",       # 20, 32
        "Function_33_12FC9",       # 21, 33
        "Function_34_12FE4",       # 22, 34
        "Function_35_12FFF",       # 23, 35
        "Function_36_13034",       # 24, 36
        "Function_37_1341A",       # 25, 37
        "Function_38_13445",       # 26, 38
        "Function_39_1345E",       # 27, 39
        "Function_40_13D61",       # 28, 40
        "Function_41_1465E",       # 29, 41
        "Function_42_14996",       # 2A, 42
        "Function_43_14A2A",       # 2B, 43
        "Function_44_14AA0",       # 2C, 44
        "Function_45_14BD8",       # 2D, 45
        "Function_46_14BFE",       # 2E, 46
        "Function_47_14BFF",       # 2F, 47
        "Function_48_14DD3",       # 30, 48
        "Function_49_14FA7",       # 31, 49
        "Function_50_15181",       # 32, 50
        "Function_51_15366",       # 33, 51
        "Function_52_15535",       # 34, 52
        "Function_53_15704",       # 35, 53
        "Function_54_158D0",       # 36, 54
        "Function_55_15AA7",       # 37, 55
        "Function_56_15B23",       # 38, 56
        "Function_57_15BCB",       # 39, 57
        "Function_58_15D05",       # 3A, 58
        "Function_59_15DA8",       # 3B, 59
        "Function_60_15E4E",       # 3C, 60
        "Function_61_15EF4",       # 3D, 61
        "Function_62_15F9A",       # 3E, 62
        "Function_63_1604A",       # 3F, 63
        "Function_64_160EC",       # 40, 64
        "Function_65_16125",       # 41, 65
        "Function_66_161B9",       # 42, 66
        "Function_67_1624D",       # 43, 67
        "Function_68_162E1",       # 44, 68
    ))


    def Function_0_7E8(): pass

    label("Function_0_7E8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_828"),
        (1, "loc_834"),
        (2, "loc_840"),
        (3, "loc_84C"),
        (4, "loc_858"),
        (5, "loc_864"),
        (6, "loc_870"),
        (SWITCH_DEFAULT, "loc_87C"),
    )


    label("loc_828")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_834")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_840")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_84C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_858")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_864")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_870")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_87C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_888")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_89F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_888")

    label("loc_89F")

    Return()

    # Function_0_7E8 end

    def Function_1_8A0(): pass

    label("Function_1_8A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96B")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_96B")
    SetChrPos(0x0, -2190, 0, 68010, 90)
    SetChrPos(0x1, -2190, 0, 68010, 90)
    SetChrPos(0x2, -2190, 0, 68010, 90)
    SetChrPos(0x3, -2190, 0, 68010, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_93E")
    SetChrPos(0x4, -2190, 0, 68010, 90)
    SetChrPos(0x5, -2190, 0, 68010, 90)
    Jump("loc_95D")

    label("loc_93E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95D")
    SetChrPos(0x4, -2190, 0, 68010, 90)

    label("loc_95D")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96B")

    label("loc_96B")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x350, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A5")
    Event(0, 47)

    label("loc_9A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x351, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D6")
    Event(0, 48)

    label("loc_9D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x352, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A07")
    Event(0, 49)

    label("loc_A07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x353, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A38")
    Event(0, 50)

    label("loc_A38")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x354, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A69")
    Event(0, 51)

    label("loc_A69")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x355, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9A")
    Event(0, 52)

    label("loc_A9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x356, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACB")
    Event(0, 53)

    label("loc_ACB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x357, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFC")
    Event(0, 54)

    label("loc_AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B0A")
    Jump("loc_B7D")

    label("loc_B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_B45")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x13, 0x40)
    SetChrPos(0x13, 122440, 0, 7540, 45)
    SetChrChipByIndex(0x13, 0x4)
    SetChrSubChip(0x13, 0x0)
    Jump("loc_B7D")

    label("loc_B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B53")
    Jump("loc_B7D")

    label("loc_B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_B61")
    Jump("loc_B7D")

    label("loc_B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B6F")
    Jump("loc_B7D")

    label("loc_B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B7D")
    ClearChrFlags(0x9, 0x80)

    label("loc_B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA6")
    SetMapFlags(0x10000000)
    Event(0, 39)
    Jump("loc_BB7")

    label("loc_BA6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB7")
    Event(0, 40)

    label("loc_BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_BCE")
    ClearScenarioFlags(0x5C, 0)
    SetScenarioFlags(0x0, 3)
    Event(0, 9)
    Jump("loc_C9F")

    label("loc_BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_BE2")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 11)
    Jump("loc_C9F")

    label("loc_BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_C3D")
    ClearScenarioFlags(0x5C, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_DA(0x0)"), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C0F")
    Event(0, 12)
    Jump("loc_C38")

    label("loc_C0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C26")
    Event(0, 13)
    Jump("loc_C38")

    label("loc_C26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C38")
    Event(0, 15)

    label("loc_C38")

    Jump("loc_C9F")

    label("loc_C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_C51")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 18)
    Jump("loc_C9F")

    label("loc_C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_C65")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 21)
    Jump("loc_C9F")

    label("loc_C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_C79")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 24)
    Jump("loc_C9F")

    label("loc_C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 6)), scpexpr(EXPR_END)), "loc_C8D")
    ClearScenarioFlags(0x5C, 6)
    Event(0, 32)
    Jump("loc_C9F")

    label("loc_C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 7)), scpexpr(EXPR_END)), "loc_C9F")
    ClearScenarioFlags(0x5C, 7)
    SetScenarioFlags(0x0, 2)
    Event(0, 36)

    label("loc_C9F")

    Return()

    # Function_1_8A0 end

    def Function_2_CA0(): pass

    label("Function_2_CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_CB7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF8")

    label("loc_CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_CC5")
    Jump("loc_CF8")

    label("loc_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF8")

    label("loc_CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CF8")

    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D2F")
    Jump("loc_D5C")

    label("loc_D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_D3D")
    Jump("loc_D5C")

    label("loc_D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_D4F")
    OP_66(0x0, 0x1)
    Jump("loc_D5C")

    label("loc_D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D5C")
    OP_66(0x1, 0x1)

    label("loc_D5C")

    SetMapObjFrame(0xFF, "tanmatu2", 0x0, 0x1)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9C")
    SetMapObjFrame(0xFF, "01", 0x0, 0x1)
    OP_65(0x7, 0x1)

    label("loc_D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB4")
    SetMapObjFrame(0xFF, "02", 0x0, 0x1)
    OP_65(0x8, 0x1)

    label("loc_DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCC")
    SetMapObjFrame(0xFF, "05", 0x0, 0x1)
    OP_65(0x9, 0x1)

    label("loc_DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEF")
    SetMapObjFrame(0xFF, "06", 0x0, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x0, 0x1)
    OP_65(0xA, 0x1)

    label("loc_DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E07")
    SetMapObjFrame(0xFF, "07", 0x0, 0x1)
    OP_65(0xB, 0x1)

    label("loc_E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1F")
    SetMapObjFrame(0xFF, "08", 0x0, 0x1)
    OP_65(0xC, 0x1)

    label("loc_E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E37")
    SetMapObjFrame(0xFF, "03", 0x0, 0x1)
    OP_65(0xD, 0x1)

    label("loc_E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5A")
    SetMapObjFrame(0xFF, "04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x0, 0x1)
    OP_65(0xE, 0x1)

    label("loc_E5A")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E7A")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E95")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB0")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_EB0")

    OP_1B(0x8, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC8")
    OP_1B(0x8, 0x0, 0x2C)

    label("loc_EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_EE0")
    SetMapObjFlags(0x7, 0x10)
    OP_65(0x4, 0x1)
    Jump("loc_EEA")

    label("loc_EE0")

    ClearMapObjFlags(0x7, 0x10)
    OP_66(0x4, 0x1)

    label("loc_EEA")

    ClearMapObjFlags(0x8, 0x10)
    ClearMapObjFlags(0x9, 0x10)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)
    Return()

    # Function_2_CA0 end

    def Function_3_EFF(): pass

    label("Function_3_EFF")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a message on the bulletin board.\x07\x00\x02",
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
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I got a meeting I've got to attend at HQ.\x01",
            "You better not be slacking off when I return.\x01",
            "                                        - Sergei\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_EFF end

    def Function_4_FE7(): pass

    label("Function_4_FE7")

    Call(0, 5)
    Return()

    # Function_4_FE7 end

    def Function_5_FEB(): pass

    label("Function_5_FEB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_107F")
    Jump("loc_10C9")

    label("loc_107F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_109F")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10C9")

    label("loc_109F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10BF")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10C9")

    label("loc_10BF")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10C9")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1242")

    ChrTalk(
        0x9,
        (
            "#1000FI'd watch out, 'cause you're bound to\x01",
            "be swimming in support requests\x01",
            "during the Anniversary Festival.\x02\x03",
            "Until the final day of the festival, focus\x01",
            "solely on completing your requests.\x02\x03",
            "#1003FWilling to bet HQ will bug me to come\x01",
            "lend a hand, but...that's my problem.\x01",
            "I'll leave you guys to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FRoger.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12FD")

    label("loc_1242")


    ChrTalk(
        0x9,
        (
            "#1000FI'd watch out, cause you're bound to\x01",
            "be covered in support requests during\x01",
            "the Anniversary Festival.\x02\x03",
            "Don't mind me. Just focus\x01",
            "on finishing any support\x01",
            "requests that come in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12FD")

    SetChrSubChip(0x9, 0x0)
    TalkEnd(0x9)
    Return()

    # Function_5_FEB end

    def Function_6_1305(): pass

    label("Function_6_1305")

    TalkBegin(0xFE)

    ChrTalk(
        0xA,
        "#1200F...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_1305 end

    def Function_7_131B(): pass

    label("Function_7_131B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AB")

    ChrTalk(
        0xB,
        "Nyaa～～o... ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FHuh...? Wait a second,\x01",
            "Coppe, didn't I just give\x01",
            "you your food?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 1)
    Jump("loc_13C0")

    label("loc_13AB")


    ChrTalk(
        0xB,
        "Nyaa～～o... ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_13C0")

    TalkEnd(0xFE)
    Return()

    # Function_7_131B end

    def Function_8_13C4(): pass

    label("Function_8_13C4")

    TalkBegin(0xFF)
    OP_E3(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E3(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A3B")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E3(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_140D"),
        (1, "loc_15B9"),
        (SWITCH_DEFAULT, "loc_1A36"),
    )


    label("loc_140D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1434")
    OP_2B(0x34, 0x31, 0x32, 0x2B, 0x33, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_15B4")

    label("loc_1434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1455")
    OP_2B(0x31, 0x32, 0x2B, 0x33, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_15B4")

    label("loc_1455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1470")
    OP_2B(0x2D, 0x2E, 0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_15B4")

    label("loc_1470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1487")
    OP_2B(0x28, 0x29, 0x2F, 0xFFFF)
    Jump("loc_15B4")

    label("loc_1487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_14A0")
    OP_2B(0x28, 0x29, 0x2A, 0x2F, 0xFFFF)
    Jump("loc_15B4")

    label("loc_14A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_14B3")
    OP_2B(0x25, 0xFFFF)
    Jump("loc_15B4")

    label("loc_14B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_14D2")
    OP_2B(0x22, 0x23, 0x18, 0x1A, 0x1C, 0x1E, 0x21, 0xFFFF)
    Jump("loc_15B4")

    label("loc_14D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_14F1")
    OP_2B(0x1F, 0x20, 0x21, 0x18, 0x1A, 0x1C, 0x1E, 0xFFFF)
    Jump("loc_15B4")

    label("loc_14F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_150E")
    OP_2B(0x1B, 0x1C, 0x1D, 0x1E, 0x18, 0x1A, 0xFFFF)
    Jump("loc_15B4")

    label("loc_150E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1529")
    OP_2B(0x16, 0x17, 0x18, 0x19, 0x1A, 0xFFFF)
    Jump("loc_15B4")

    label("loc_1529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1546")
    OP_2B(0x11, 0x12, 0x13, 0x14, 0xE, 0x10, 0xFFFF)
    Jump("loc_15B4")

    label("loc_1546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_155F")
    OP_2B(0xD, 0xE, 0xF, 0x10, 0xFFFF)
    Jump("loc_15B4")

    label("loc_155F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_157C")
    OP_2B(0x9, 0xA, 0xB, 0x5, 0x6, 0x7, 0xFFFF)
    Jump("loc_15B4")

    label("loc_157C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1593")
    OP_2B(0x5, 0x6, 0x7, 0xFFFF)
    Jump("loc_15B4")

    label("loc_1593")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_15AF")
    OP_2B(0x1, 0x35, 0x2, 0x3, 0xFFFF)
    Jump("loc_15B4")

    label("loc_15AF")

    OP_2B(0x1, 0xFFFF)

    label("loc_15B4")

    Jump("loc_1A36")

    label("loc_15B9")

    SetMapFlags(0x40000000)
    OP_E3(0x7)
    Sleep(500)
    SetChrName("Receptionist Fran")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_162F")
    Sound(2062, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Hello, you've reached the CPD. This is Fran speaking!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1663")

    label("loc_162F")

    Sound(2061, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "As always, we appreciate your hard work!\x02",
    )

    CloseMessageWindow()

    label("loc_1663")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E3(0x4)"), scpexpr(EXPR_END)), "loc_18E0")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1855")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_16EC"),
        (13, "loc_1736"),
        (12, "loc_1779"),
        (SWITCH_DEFAULT, "loc_17BA"),
    )


    label("loc_16EC")

    Sound(2075, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "1st Class... You're phenomenal, Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_17BA")

    label("loc_1736")

    Sound(2074, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "2nd Class... Great work, Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_17BA")

    label("loc_1779")

    Sound(2073, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "3rd Class... Good job, Lloyd.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17BA")

    label("loc_17BA")

    Sound(2076, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "I'll make sure your bonuses get transferred to you\x01",
            "immediately!\x02",
        )
    )

    CloseMessageWindow()
    Sound(2077, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Thank you, and please keep up the good work!\x02",
    )

    CloseMessageWindow()
    Jump("loc_18D8")

    label("loc_1855")

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

    label("loc_18D8")

    SetScenarioFlags(0x0, 4)
    Jump("loc_1A28")

    label("loc_18E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_199F")
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
    Jump("loc_1A28")

    label("loc_199F")

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

    label("loc_1A28")

    OP_57(0x0)
    OP_E3(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_1A36")

    label("loc_1A36")

    Jump("loc_13E0")

    label("loc_1A3B")

    OP_E3(0x6)
    FadeToBright(300, 0)
    OP_0D()
    OP_E3(0xB)
    TalkEnd(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A64")
    Call(0, 41)

    label("loc_1A64")

    Return()

    # Function_8_13C4 end

    def Function_9_1A65(): pass

    label("Function_9_1A65")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50090.itc", 0x22)
    LoadChrToIndex("apl/ch50092.itc", 0x23)
    LoadChrToIndex("chr/ch02702.itc", 0x24)
    OP_68(12600, 2350, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, 16000, 850, 6400, 180)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    BeginChrThread(0x12, 0, 0, 10)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x5)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1400, 6600, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0xC)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13400, 1300, 6600, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x5)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12400, 1400, 6600, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x22)
    SetChrSubChip(0x16, 0xC)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12000, 1300, 6600, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x5)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13000, 1400, 4600, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x22)
    SetChrSubChip(0x18, 0xC)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13400, 1300, 4600, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x23)
    SetChrSubChip(0x19, 0x5)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 12400, 1400, 4600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0xC)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 12000, 1300, 4600, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x22)
    SetChrSubChip(0x1B, 0x7)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12700, 1400, 5500, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x23)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 16000, 750, 5500, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_52(0x1C, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KCrossbell Anniversary Festival, Third Day\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7110", 0)
    OP_68(12600, 1850, 5600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#3300001V#6P#0306FPhew, I'm beat. Yesterday really\x01",
            "sapped all of my energy.\x02\x03",
            "#3300002V#0302FAnd you're tellin' me we have three\x01",
            "more days like that ahead of us...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(200)

    ChrTalk(
        0x103,
        (
            "#3300003V#5P#0200FYou reap what you sow, Randy...\x02\x03",
            "#3300004V#0204FAfter all, who was the one who\x01",
            "proposed the race in the first place?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(200)

    ChrTalk(
        0x104,
        (
            "#3300005V#6P#0301FYeah, yeah. The regret is kickin' in.\x02\x03",
            "#3300006V#0306FI'm gettin' old. These shenanigans with\x01",
            "youngsters are bad for my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3300007V#0102FYou're still 20 or so, aren't you...?\x01",
            "What are you talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300008V#11P#0008F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#3300009V#0105FLloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300010V#6P#0205FWhat is wrong?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3300011V#5P#0005FOh, well...\x02\x03",
            "#3300012V#0012F...it's just I'm still thinking about what\x01",
            "Estelle and Joshua told us yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3300013V#0101FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3300014V#6P#0301FThe Schwarze Auction, wasn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300015V#6P#0200FLloyd, the probability of that being a mere\x01",
            "rumor is quite high, is it not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300016V#5P#0003FI mean, that's true, but...\x02\x03",
            "#3300017V#0001FGiven Crossbell's circumstances, I have\x01",
            "a feeling that this story might actually\x01",
            "have some ground to it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#3300018V#6P#0306FTrue. Even the mafia stroll around\x01",
            "casually, without a care in the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300019V#6P#0203FTaking everything into account, it\x01",
            "does not seem that unlikely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3300020V#0108F...\x02\x03",
            "#3300021V#0103FTruth be told, I've heard of a\x01",
            "similar, disturbing rumor before.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3300022V#5P#0005FYou have...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300023V#3P#0205FAbout the auction?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3300024V#0103FI believe I've already mentioned that I\x01",
            "studied abroad in multiple countries...\x02\x03",
            "#3300025VAround that time, I heard a story from\x01",
            "a noble girl I knew...\x02\x03",
            "#3300026V#0101FShe told me a secret party is thrown\x01",
            "every year in a certain area of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
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
        "#3300027V#5P#0011FA secret party...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3300028V#6P#0302FDefinitely sounds shady to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3300029V#0106FApparently, it's a party where nobles and\x01",
            "businessmen of each nation gather\x01",
            "behind closed doors...\x02\x03",
            "#3300030V#0108FOf course, I just dismissed\x01",
            "it as rumor. Although...\x02\x03",
            "#3300031V#0101F...now I'm not so sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300032V#5P#0003FRight...\x02\x03",
            "#3300033V#0001FCould it be possible that this party and the\x01",
            "Schwarze Auction are one and the same?\x02\x03",
            "#3300034V#0008FHmm, if that's the case, the chief\x01",
            "might know something about it...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#3300035V#6P#0200FThe chief had business at\x01",
            "headquarters today.\x02\x03",
            "#3300036VHe mentioned a mandatory meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300037V#5P#0006FYeah, I remember that.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#3300038V#6P#0303FLet's pretend that this is all true.\x01",
            "Can we even do anything about it?\x02\x03",
            "#3300039V#0301FWhat we think means jack all. Seems to me\x01",
            "like the diet would get on the CPD's ass the\x01",
            "second anybody tries to touch the auction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300040V#5P#0008FThat's true.\x02\x03",
            "#3300041V#0006FBut, still...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3300042V#0103FI understand how you feel, Lloyd.\x02\x03",
            "#3300043V#0100FBut for the time being, let's just keep it\x01",
            "in our minds during the festival, okay?\x02\x03",
            "#3300044VWe might run into some new leads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300045V#5P#0003FYeah, good call.\x02\x03",
            "#3300046V#0000FAll right, let's grab a quick bite and take\x01",
            "care of today's support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300047V#6P#0202F...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
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
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_68(12000, 1850, 8700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrPos(0x1, 12000, 850, 8700, 270)
    SetChrPos(0x2, 12000, 850, 8700, 270)
    SetChrPos(0x3, 12000, 850, 8700, 270)
    SetScenarioFlags(0xA0, 2)
    OP_29(0x44, 0x1, 0x2)
    OP_29(0x44, 0x1, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C7C")
    OP_29(0x17, 0x4, 0x40)
    Jump("loc_2C8E")

    label("loc_2C7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8E")
    OP_29(0x17, 0x4, 0x40)

    label("loc_2C8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CAC")
    OP_29(0x19, 0x4, 0x40)
    Jump("loc_2CBE")

    label("loc_2CAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CBE")
    OP_29(0x19, 0x4, 0x40)

    label("loc_2CBE")

    ModifyEventFlags(1, 0, 0x80)
    ClearScenarioFlags(0x0, 3)
    PlayBGM("ed7106", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_9_1A65 end

    def Function_10_2CD6(): pass

    label("Function_10_2CD6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CF4")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_10_2CD6")

    label("loc_2CF4")

    Return()

    # Function_10_2CD6 end

    def Function_11_2CF5(): pass

    label("Function_11_2CF5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50090.itc", 0x22)
    LoadChrToIndex("apl/ch50092.itc", 0x23)
    LoadChrToIndex("chr/ch02702.itc", 0x24)
    LoadChrToIndex("chr/ch23600.itc", 0x25)
    OP_68(12600, 2350, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    SetChrChipByIndex(0xC, 0x25)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x8)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 12700, 1400, 6600, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x18)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13300, 1300, 6700, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x18)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12100, 1300, 6700, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x8)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12700, 1400, 4600, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x18)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13300, 1300, 4700, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x22)
    SetChrSubChip(0x18, 0x18)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 12100, 1300, 4700, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x7)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 12700, 1400, 5500, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis062.itp")
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KCrossbell Anniversary Festival, Final Day\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7110", 0)
    OP_68(12600, 1850, 5600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#3500001V#6P#0309FMan! I'm still blown away by\x01",
            "yesterday's conversation.\x02\x03",
            "#3500002V#0300FHow much those two have gone\x01",
            "through, I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500003V#0103FI've heard my fair share of stories\x01",
            "about what happened in Liberl.\x02\x03",
            "#3500004V#0100FI would have never guessed\x01",
            "the actual truth behind it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500005V#6P#0206FThere is also the society...\x02\x03",
            "#3500006V#0201FI have heard speculation that they might\x01",
            "even surpass the Epstein Foundation and\x01",
            "ZCF in terms of cutting-edge technology.\x02\x03",
            "#3500007VI am still surprised at the extent of their\x01",
            "capabilities, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500008V#5P#0006FYeah... Honestly, it still doesn't\x01",
            "even seem real to me.\x02\x03",
            "#3500009V#0000FAccording to what Joshua said, the\x01",
            "society's influence hasn't extended\x01",
            "to Crossbell that much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500010V#0108FPerhaps it's harder for them to act under\x01",
            "the eyes of the Empire and Republic.\x02\x03",
            "#3500011VIntelligence personnel from both countries\x01",
            "are probably hiding all over the place, so\x01",
            "they wouldn't want to be caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500012V#5P#0006FWell, that definitely doesn't\x01",
            "paint a pretty picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500013V#6P#0303FA mysterious society? Intelligence\x01",
            "agencies? A massive crime syndicate?\x02\x03",
            "#3500014V#0301FYou'd be hard-pressed to find a\x01",
            "nice picture in all of that, man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500015V#6P#0206FExactly.\x02",
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    SetChrPos(0xC, 800, 0, -1500, 0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)

    NpcTalk(
        0xC,
        "Voice",
        (
            "#3500016V#5PGood moooorning!\x01",
            "Rhimes Deliveries here!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(800, 1000, 1500, 2000)
    OP_6F(0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    Sound(103, 0, 100, 0)

    def lambda_358D():
        OP_96(0xFE, 0x320, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_358D)

    def lambda_35A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_35A7)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xC, 1)

    ChrTalk(
        0x101,
        "#3500017V#3P#0005FOh, right. We met you yesterday...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500018V#0105FFrom that shipping company, right?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(800, 1100, 5500, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25500, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    OP_90(0x101, 300, 850, 7500, 180)
    OP_90(0x102, 1300, 850, 7500, 180)
    OP_90(0x103, 300, 850, 8700, 180)
    OP_90(0x104, 1300, 850, 8700, 180)
    OP_68(800, 1100, 2500, 2000)

    def lambda_36F0():
        OP_96(0xFE, 0x12C, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36F0)
    Sleep(50)

    def lambda_370D():
        OP_96(0xFE, 0x514, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_370D)
    Sleep(50)

    def lambda_372A():
        OP_96(0xFE, 0x12C, 0x0, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_372A)
    Sleep(50)

    def lambda_3747():
        OP_96(0xFE, 0x514, 0x0, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3747)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0xC,
        "#3500019V#2PYes, I can't thank you enough!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3500020V#2PGood thing you ended up\x01",
            "finding that kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3500021V#2PI bet his parents were freaking out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500022V#5P#0012FHaha, you're right about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500023V#5P#0300FYou end up gettin' chewed\x01",
            "out by your boss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3500024V#2PWell, the Guardian Force was a\x01",
            "little peeved at the late delivery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3500025V#2PLuckily, I wasn't blamed too\x01",
            "much by my fath--boss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3500026V#2PHe told me to inspect the interior of the\x01",
            "vehicle after giving me a nice punch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500027V#5P#0102FHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500028V#5P#0204FWell, I imagine you are lucky to\x01",
            "have gotten off with just that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3500029V#2PHaha, for sure!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3500030V#2POops, that's right. I didn't come\x01",
            "here to ponder over yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3500031V#2PGot a package to deliver to you.\x02",
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
        "#3500032V#5P#0005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500033V#5P#0105FIs it from headquarters?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3500034V#2PWell, I was just told that it came as an\x01",
            "express delivery, first thing in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3500035V#2PHere you go!\x02",
    )

    CloseMessageWindow()

    def lambda_3BCE():
        OP_96(0xFE, 0x12C, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3BCE)
    WaitChrThread(0xC, 1)

    def lambda_3BEC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3BEC)

    def lambda_3BF9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3BF9)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd received a small package.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_3C37():
        OP_96(0xFE, 0x320, 0x0, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3C37)

    ChrTalk(
        0x101,
        "#3500036V#5P#0005FWhat is this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500037V#11P#0100FIt's extremely tiny...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 1)

    ChrTalk(
        0xC,
        "#3500038V#2PWelp, my job is done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3500039V#2PI still got more deliveries to get\x01",
            "to, so I'll head on out now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D24():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3D24)
    Sleep(50)
    OP_93(0x102, 0xB4, 0x1F4)

    ChrTalk(
        0x104,
        "#3500040V#5P#0300FSounds good. Thank ya.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500041V#5P#0202FPlease try not to let another lost\x01",
            "child slip into your packages again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3500042V#2PHaha, trust me, lesson learned!\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)

    def lambda_3E00():
        OP_96(0xFE, 0x320, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3E00)
    Sleep(500)

    def lambda_3E1D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3E1D)
    WaitChrThread(0xC, 2)
    Sound(104, 0, 100, 0)
    WaitChrThread(0xC, 1)
    OP_68(800, 1100, 4100, 1500)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3500043V#6P#0008F...\x02",
    )

    CloseMessageWindow()

    def lambda_3E6A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3E6A)
    Sleep(50)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x104,
        "#3500044V#5P#0305FSo, who's it from?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500045V#6P#0003FLet's see here...\x02\x03",
            "#3500046V#0000FIt says it's from 'Kitty.'\x02",
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
        "#3500047V#0105F#11PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500048V#0205F#5PRenne...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    OP_68(12600, 1850, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
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
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    OP_78(0xC, 0x1E)
    ClearMapObjFlags(0xC, 0x4)
    OP_49()
    SetChrPos(0x1E, 12700, 1650, 6400, 0)
    OP_D3(0x1E, 0x0, 0x0, 0x0, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    SetCameraDistance(25000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd opened the package\x01",
            "and removed its contents.\x02\x03",
            "A card with a written message accompanied\x01",
            "by a set of jet-black cards were found inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
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
            "#3500049V\x07\x05",
            "I'm giving you these cards as\x01",
            "a thank-you gift for yesterday.\x02\x03",
            "#3500050VI intended to take a look myself,\x01",
            "thinking there might be some neat toys\x01",
            "there, but I'll hand them over to you.\x02\x03",
            "#3500051VHave fun, Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x329),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x329, 1)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
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
        "#3500052V#11P#0013FSchwarze Auction invitations?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500053V#0105FH-How in the world did she get\x01",
            "her hands on something like this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500054V#6P#0305FThese bad boys are only sent to\x01",
            "VIPs throughout Zemuria, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500055V#6P#0206FFurthermore...\x02\x03",
            "#3500056V#0201FHow did she know we were\x01",
            "looking into the auction in\x01",
            "the first place?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3500057V#5P#0003FI doubt we'll ever understand her,\x01",
            "no matter how hard we try.\x02\x03",
            "#3500058V#0001FMore importantly...are these\x01",
            "cards the real deal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500059V#0108FI would hope so...\x02\x03",
            "#3500060V#0101FThey certainly give off a luxurious feeling,\x01",
            "so I think there's a good chance they are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500061V#6P#0201FA seal of a golden rose...\x01",
            "It even uses real gold leaf.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500062V#6P#0301FThe event starts at 7 tonight, at\x01",
            "Speaker Hartmann's mansion\x01",
            "in Mishelam, yeah?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#3500063V#5P#0006FHey, guys.\x02\x03",
            "#3500064V#0008FI know the chief warned us\x01",
            "not to mess with this, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500065V#0100FNo need to finish, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500066V#6P#0309FHeh. I'm not one to ignore\x01",
            "a lady's generosity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500067V#6P#0202FIt is lucky the chief had another\x01",
            "meeting today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500068V#5P#0001FEveryone... Are you sure about this?\x02\x03",
            "#3500069VI didn't mean for my stubbornness\x01",
            "to drag you guys along with me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500070V#0104FDon't get me wrong.\x02\x03",
            "#3500071V#0108FFrom a certain perspective, I'm more\x01",
            "interested in the auction than you...\x02\x03",
            "#3500072V#0101FAfter all, it seems it's where people\x01",
            "from my sphere of life are gathering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500073V#6P#0204FI, too, am genuinely curious\x01",
            "about this auction.\x02\x03",
            "#3500074VI would like to investigate\x01",
            "those 'neat toys' that Renne\x01",
            "mentioned in the letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500075V#6P#0309FWell, I'm just interested in seein' if this\x01",
            "grand, spiffy party can live up to the hype.\x02\x03",
            "#3500076V#0304FAfter all, who am I to turn down a\x01",
            "night of food and drink, conversin'\x01",
            "with lovely, high-class ladies?\x02\x03",
            "#3500077V#0302FNo way we can ignore this, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500078V#5P#0002FEveryone...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#3500079V#5P#0003FToday's the final day of the festival.\x02\x03",
            "#3500080V#0001FLet's do our work until noon, then head over\x01",
            "to the Harbor District's boarding dock.\x02\x03",
            "#3500081VHow will we sneak into the auction...?\x01",
            "Try to think about that on the way to Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500082V#0100FYes, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500083V#6P#0300FWell, let's go ahead and knock\x01",
            "out these support requests, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500084V#6P#0204FRight. We should check the terminal\x01",
            "to see if it has been updated with\x01",
            "any new ones.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(25500, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
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
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_68(12000, 1850, 8700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrPos(0x1, 12000, 850, 8700, 270)
    SetChrPos(0x2, 12000, 850, 8700, 270)
    SetChrPos(0x3, 12000, 850, 8700, 270)
    SetChrPos(0x1E, 25600, 1650, 9500, 0)
    SetChrFlags(0x1E, 0x80)
    SetMapObjFlags(0xC, 0x4)
    SetScenarioFlags(0xA3, 3)
    OP_C7(0x1, 0x1000)
    OP_29(0x44, 0x1, 0x8)
    OP_29(0x46, 0x1, 0xF)
    OP_29(0x46, 0x4, 0x10)
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_2CF5 end

    def Function_12_4F00(): pass

    label("Function_12_4F00")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50332.itc", 0x1E)
    LoadChrToIndex("apl/ch50107.itc", 0x1F)
    OP_68(3000, 700, 126000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0xA)
    SetChrPos(0x101, 2450, 300, 125550, 180)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x102, 1000, 30, 125300, 90)
    SetMapObjFrame(0xFF, "r_huton", 0x0, 0x1)
    ClearMapObjFlags(0xD, 0x4)
    OP_70(0xD, 0x5)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00101.itp")
    Sound(910, 0, 100, 0)
    Sleep(1200)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("???")

    AnonymousTalk(
        0xFF,
        "#3400001V#2S#60W...yd...?     \x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        "#3400002V#2S#50W...Lloyd? Are you up?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#3400003V#5206F#40W*yawn*...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(910, 0, 100, 0)
    SetChrName("???")

    AnonymousTalk(
        0xFF,
        (
            "#3400004VHey! You need to wake up now. We have\x01",
            "a meeting, remember?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#3400005V#5205F#4S...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7104", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7104")
    ReplaceBGM("ed7101", "ed7104")
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(23500, 1000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_71(0xD, 0x5, 0x14, 0x0, 0x0)
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x101, 0xB)
    Sleep(100)
    SetChrSubChip(0x101, 0xC)
    Sleep(300)
    Sound(1128, 255, 90, 0)

    def lambda_5144():
        OP_96(0xFE, 0x2BC, 0x1E, 0x1E974, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5144)

    ChrTalk(
        0x102,
        "#3400006V#6P#0105F#8AAh!\x02",
    )

    Sleep(1000)
    WaitChrThread(0x102, 1)
    SetChrSubChip(0x101, 0xD)
    Sleep(150)
    SetChrSubChip(0x101, 0xE)
    Sleep(150)
    SetChrSubChip(0x101, 0xD)
    Sleep(150)
    SetChrSubChip(0x101, 0xC)
    Sleep(300)
    OP_6F(0x10)
    CancelBlur(0)

    ChrTalk(
        0x101,
        (
            "#3400007V#11P#5205FOh...\x02\x03",
            "#3400008VMorning, Elie. Any reason why, uh, you're\x01",
            "standing in my room?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_520C():
        OP_96(0xFE, 0x3E8, 0x1E, 0x1E974, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_520C)
    WaitChrThread(0x102, 1)
    Sound(1187, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1600)

    AnonymousTalk(
        0x102,
        (
            "#3400009VWell, since you hadn't come downstairs,\x01",
            "I thought I should come check on you.\x02\x03",
            "#3400010VI take it you didn't sleep well, given what\x01",
            "we heard yesterday. I can't blame you if\x01",
            "it made you restless.\x02",
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
            "#3400011V#11P#5212FSometimes you see right through me, Elie.\x02\x03",
            "#3400012V#5200FBut, hey... How are you holding up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3400013V#6P#0104FOh, I'm fine. If I were to lose heart due to\x01",
            "something like that, I might as well throw\x01",
            "all my goals out the window.\x02\x03",
            "#3400014V#0108FBesides, I think I always knew the truth\x01",
            "deep down.\x02\x03",
            "#3400015VThe reality that this secret 'party' was, in\x01",
            "fact, another example of Crossbell's corrupt\x01",
            "side, I mean.\x02\x03",
            "#3400016V#0106FI was simply in denial, trying to look\x01",
            "away from it.\x02\x03",
            "#3400017VBut not anymore. I don't intend on living\x01",
            "with regrets or feeling powerless to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400018V#11P#5201FElie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3400019V#6P#0102FI've decided to move forward and attack\x01",
            "those feelings with my head held high.\x02\x03",
            "#3400020VThat was the chief's sentiment, and I intend\x01",
            "on making it my own strength as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400021V#11P#5204FI see...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0xD)
    Sleep(100)
    SetChrSubChip(0x101, 0xE)
    Sleep(300)
    OP_63(0x101, 0xFFFFFE0C, 1500, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    SetChrSubChip(0x101, 0xD)
    Sleep(100)
    SetChrSubChip(0x101, 0xC)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#3400022V#11P#5200FThat settles it, then!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(2750, 700, 127100, 500)
    MoveCamera(45, 18, 0, 500)
    OP_6E(400, 500)
    SetCameraDistance(23500, 500)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    SetChrPos(0x101, 1000, 30, 126400, 270)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_57A8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_57A8)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3400023V#5204F#5PIf you've already found your resolve and\x01",
            "decided not to hesitate, then I have no\x01",
            "reason to, either.\x02\x03",
            "#3400024V#5200FOnce I get changed, I'll head down and\x01",
            "meet you all on the first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3400025V#12P#0102FSure thing.\x02\x03",
            "#3400026V#0109FOh, since breakfast is ready, would you mind\x01",
            "having our meeting while we eat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400027V#5202F#5PGreat idea! I'm starving.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    OP_68(2000, 700, 124000, 2000)

    def lambda_595E():
        OP_96(0xFE, 0x0, 0x0, 0x1D6B4, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_595E)
    WaitChrThread(0x102, 1)

    def lambda_597C():
        OP_96(0xFE, 0x0, 0x0, 0x1D0D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_597C)

    def lambda_5996():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5996)
    Sound(103, 0, 100, 0)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x102, 2)
    OP_6F(0x1)
    Sound(104, 0, 100, 0)
    Fade(500)
    OP_68(1000, 1000, 126400, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3400028V#5202F#5P(Elie's come a long way in this last month.\x01",
            "She's not carrying the same doubts she\x01",
            "used to.)\x02\x03",
            "#3400029V#5204F(It's time to catch up.)\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1390, 1000, 128419, 1500)
    OP_93(0x101, 0x163, 0x190)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#3400030V#2P#5200FFourth day of the Anniversary Festival...\x02\x03",
            "#3400031VWe're going to have our work cut out for us.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetMapObjFrame(0xFF, "r_huton", 0x1, 0x1)
    SetMapObjFlags(0xD, 0x4)
    Call(0, 17)
    Return()

    # Function_12_4F00 end

    def Function_13_5B69(): pass

    label("Function_13_5B69")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50332.itc", 0x1E)
    LoadChrToIndex("apl/ch50107.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    OP_68(3000, 700, 126000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0xA)
    SetChrPos(0x101, 2450, 300, 125550, 180)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x103, 1000, 30, 125300, 90)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetMapObjFrame(0xFF, "r_huton", 0x0, 0x1)
    ClearMapObjFlags(0xD, 0x4)
    OP_70(0xD, 0x5)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00200.itp")
    Sound(910, 0, 100, 0)
    Sleep(1200)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("???")

    AnonymousTalk(
        0xFF,
        "#3400032V#2S#60W...*nudge* *nudge*...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#3400033V#5206F#40W*yawn*...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(910, 0, 100, 0)
    SetChrName("???")

    AnonymousTalk(
        0xFF,
        "#3400034V#2S#40W*NUDGE* *NUDGE* *NUDGE*\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#3400035V#5208F#30W(What the...? An earthquake?)\x02\x03",
            "#3400036V(This...actually feels kind of nice...)\x02\x03",
            "#3400037V#5203F(Geez... I'm so sleepy...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("???")

    AnonymousTalk(
        0xFF,
        "#3400038V#2S#40W...          \x02",
    )

    CloseMessageWindow()
    Sound(1219, 255, 90, 0)
    Sleep(1200)
    SetChrName("???")

    AnonymousTalk(
        0xFF,
        (
            "#3400039V#2SOutput: minimum.\x01",
            "Power level: low.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("???")

    AnonymousTalk(
        0xFF,
        "#3400040V#2SFreezing process...begin.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)
    Sound(1221, 255, 100, 0)
    Sleep(500)
    Sound(184, 0, 90, 0)
    Sleep(700)
    Sound(371, 0, 90, 0)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        "#3400041V#5211F#4SC-COLD?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7104", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7104")
    ReplaceBGM("ed7101", "ed7104")
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(23500, 1000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_71(0xD, 0x5, 0x14, 0x0, 0x0)
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x101, 0xB)
    Sleep(100)
    SetChrSubChip(0x101, 0xC)
    Sleep(300)
    SetChrSubChip(0x101, 0xD)
    Sleep(150)
    SetChrSubChip(0x101, 0xE)
    Sleep(150)
    SetChrSubChip(0x101, 0xD)
    Sleep(150)
    SetChrSubChip(0x101, 0xC)
    Sleep(300)
    OP_6F(0x10)
    CancelBlur(0)

    ChrTalk(
        0x101,
        "#3400042V#11P#5205FWha...?!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    Sound(1283, 255, 100, 0)

    AnonymousTalk(
        0x103,
        "#3400043VGood morning, Lloyd.\x02",
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
            "#3400044V#11P#5202FY-Yeah. Good morning.\x02\x03",
            "#3400045V#5205FActually, why are you even in my room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400046V#6P#0203FOur morning meeting is about to begin,\x01",
            "so I came to wake you up, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0xFFFFFE0C, 1500, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3400047V#11P#5205FOh. I didn't realize how late it was.\x02\x03",
            "#3400048V#5206FStill, though... That was kind of strange.\x02\x03",
            "#3400049VI felt a weird, chilling sensation against\x01",
            "the back of my neck. I must have had a\x01",
            "wild dream...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400050V#6P#0203FThat was no dream.\x02\x03",
            "#3400051V#0200FMy efforts to nudge you awake were in vain,\x01",
            "so I cast a low-energy Diamond Dust.\x02",
        )
    )

    CloseMessageWindow()
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0xFFFFFE0C, 1500, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3400052V#11P#5211FExcuse me?\x02\x03",
            "#3400053VI must still be dreaming, because I could\x01",
            "have sworn you just said you used a\x01",
            "Diamond Dust on me in my sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400054V#6P#0204FIt was only a tiny amount, so there is no\x01",
            "need to be concerned.\x02\x03",
            "#3400055V#0202FIt worked out in the end, did it not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400056V#11P#5212FY-Yeah, I suppose it did.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#3400057V#6P#0208FBesides, I had difficulty deciding how to wake\x01",
            "up someone who is fast asleep...\x02\x03",
            "#3400058V#0206F...so, I ended up going with what I\x01",
            "considered to be a reliable method.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400059V#11P#5205FYou didn't know how to wake me up?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0xFFFFFE0C, 1500, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x101, 0xFFFFFE0C, 1500, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#3400060V#11P#5208F(Actually, now that I think about it...)\x02\x03",
            "#3400061V(I doubt she's ever had the opportunity\x01",
            "to do something like that.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#3400062V#6P#0205FLloyd?\x02\x03",
            "#3400063V#0206FAre you angry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400064V#11P#5204FNo, not really.\x02\x03",
            "#3400065V#5202FAlthough, I'd recommend raising your voice,\x01",
            "too, when nudging fails.\x02\x03",
            "#3400066VI'm sure that'll wake most people up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400067V#6P#0202FOh, I see.\x02\x03",
            "#3400068V#0204FIn that case, would it be more appropriate to\x01",
            "address you with 'Good morning, Master ㈱'\x01",
            "the next time the opportunity presents itself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400069V#11P#5201FWhy would you think that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400070V#6P#0211FOr perhaps you would enjoy, 'I'm going to kick\x01",
            "my lazy brother out of bed if he doesn't wake up!'\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        "#3400071V#11P#5207FWhere'd you even learn these phrases?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400072V#6P#0204FPlease relax. I am merely teasing you.\x02\x03",
            "#3400073V#0202FElie and I prepared breakfast, so please\x01",
            "come downstairs after you've changed.\x02\x03",
            "#3400074VI'll be taking my leave, now.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x190)

    ChrTalk(
        0x101,
        "#3400075V#11P#5205FW-Wait a minute.\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x103, 0x5A, 0x1F4)

    ChrTalk(
        0x103,
        "#3400076V#6P#0205FWhat is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(500)
    OP_68(2750, 700, 127100, 500)
    MoveCamera(45, 18, 0, 500)
    OP_6E(400, 500)
    SetCameraDistance(23500, 500)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 1000, 30, 126400, 270)
    Sound(804, 0, 100, 0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_69A2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_69A2)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3400077V#5204F#5PThanks, Tio.\x02\x03",
            "#3400078V#5202FYou were worried about me, so you\x01",
            "came to check in on me, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400079V#12P#0205F...?!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 14)
    Sleep(1800)

    ChrTalk(
        0x101,
        "#3400080V#5205F#5P#NHuh...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)
    Fade(500)
    OP_68(1000, 1000, 126400, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#3400081V#5204F#5PHaha. It feels like the stress from\x01",
            "yesterday just vanished.\x02\x03",
            "#3400082V#5202FIt's all thanks to you, Tio.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1390, 1000, 128419, 1500)
    OP_93(0x101, 0x163, 0x190)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#3400083V#2P#5200FFourth day of the Anniversary Festival...\x02\x03",
            "#3400084VWe're going to have our work cut out for us.\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x1)
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    SetMapObjFrame(0xFF, "r_huton", 0x1, 0x1)
    SetMapObjFlags(0xD, 0x4)
    Call(0, 17)
    Return()

    # Function_13_5B69 end

    def Function_14_6C23(): pass

    label("Function_14_6C23")

    OP_93(0x103, 0xB4, 0x2BC)
    OP_63(0x103, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_68(2000, 700, 124000, 1500)

    def lambda_6C52():
        OP_96(0xFE, 0x0, 0x0, 0x1D6B4, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C52)
    WaitChrThread(0x103, 1)
    OP_64(0x103)
    Sound(103, 0, 100, 0)

    def lambda_6C79():
        OP_96(0xFE, 0x0, 0x0, 0x1D0D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C79)

    def lambda_6C93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6C93)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    Sound(104, 0, 100, 0)
    OP_6F(0x1)
    Return()

    # Function_14_6C23 end

    def Function_15_6CB0(): pass

    label("Function_15_6CB0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50332.itc", 0x1E)
    LoadChrToIndex("apl/ch50107.itc", 0x1F)
    OP_68(3000, 700, 126000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0xA)
    SetChrPos(0x101, 2450, 300, 125550, 180)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x104, 700, 30, 125300, 90)
    SetMapObjFrame(0xFF, "r_huton", 0x0, 0x1)
    ClearMapObjFlags(0xD, 0x4)
    OP_70(0xD, 0x5)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00300.itp")
    Sound(910, 0, 100, 0)
    Sleep(1200)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("???")

    AnonymousTalk(
        0xFF,
        "#3400085V#2S#60WHelloooo... Wake up!\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#3400086V#2S#50WC'mon, man, you're sleepin'\x01",
            "like a log here!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#3400087V#5206F#40WUmm...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("???")

    AnonymousTalk(
        0xFF,
        "#3400088V#2S#30WGeez, you asked for it.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(1377, 255, 90, 0)
    Sleep(2000)

    AnonymousTalk(
        0x101,
        "#3400089V#5205FAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7104", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7104")
    ReplaceBGM("ed7101", "ed7104")
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(23500, 1000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_71(0xD, 0x5, 0x14, 0x0, 0x0)
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x101, 0xB)
    Sleep(100)
    SetChrSubChip(0x101, 0xC)
    Sleep(300)
    SetChrSubChip(0x101, 0xD)
    Sleep(150)
    SetChrSubChip(0x101, 0xE)
    Sleep(150)
    SetChrSubChip(0x101, 0xD)
    Sleep(150)
    SetChrSubChip(0x101, 0xC)
    Sleep(300)
    OP_6F(0x10)
    CancelBlur(0)

    ChrTalk(
        0x101,
        "#3400090V#11P#5205FWhat the...?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1366, 255, 90, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x104,
        (
            "#3400091VWhy the hell do I have to be the\x01",
            "one to wake up another dude?\x02\x03",
            "#3400092VIt's much more my style to be gently\x01",
            "roused from sleep by a half-naked\x01",
            "babe, after a long night of fun...\x02\x03",
            "#3400093VThen we'd make some joe or\x01",
            "somethin', takin' it easy...\x02\x03",
            "#3400094VHeck, maybe we could just go all\x01",
            "the way while we're at it.\x02",
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
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3400095V#11P#5206F...Sorry.\x01",
            "I haven't really put much thought on\x01",
            "how to go along with your fantasies.\x02\x03",
            "#3400096V#5205FUh... Is it already time\x01",
            "for our meeting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3400097V#6P#0304F'Already,' he says.\x02\x03",
            "#3400098V#0300FYeah man! Mademois-Elie and Tio Tot\x01",
            "have already cooked up some grub,\x01",
            "so let's go wolf it down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400099V#11P#5200FYeah, I hear you loud and clear.\x01",
            "I'll hurry and get changed.\x02\x03",
            "#3400100V#5209FHaha...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#3400101V#6P#0305FWhat are ya on about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400102V#11P#5204FYou're a pretty cool guy, Randy.\x02\x03",
            "#3400103V#5202FThat way you casually look after everyone...\x01",
            "I definitely couldn't imitate that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#3400104V#6P#0301FH-How the hell can you say\x01",
            "that with a straight face?\x02\x03",
            "#3400105V#0303FTrust me, I'm not a big fan of\x01",
            "comfortin' glum dorks like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400106V#11P#5214FHaha, whatever you say.\x02\x03",
            "#3400107V#5204FBut don't worry. I feel a lot better\x01",
            "after a good night's rest.\x02\x03",
            "#3400108V#5200FNot that I've forgotten our lingering issues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400109V#6P#0302FHuh, that right?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(3420, 700, 126420, 1500)
    SetChrFlags(0x104, 0x40)

    def lambda_7542():
        OP_96(0xFE, 0x578, 0x1E, 0x1EC30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7542)
    WaitChrThread(0x104, 1)
    Sleep(500)
    SetCameraDistance(22330, 500)
    Fade(500)
    SetChrFlags(0x104, 0x8)
    SetChrPos(0x101, 2350, 150, 125820, 180)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x101, 0x5)
    Sleep(50)
    SetChrSubChip(0x101, 0x6)
    Sleep(50)
    SetChrSubChip(0x101, 0x7)
    OP_0D()
    Sound(820, 0, 100, 0)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 16)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#3400110V#6P#0309FWell, remember that feelin', youngin'.\x02\x03",
            "#3400111VThat kinda frustration could be the push\x01",
            "you need to grow into a mature man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400112V#11P#5211FYeah? So how about you stop\x01",
            "treating me like a kid...?\x02\x03",
            "#3400113V#5213FI'm going to change now. I'll meet\x01",
            "you downstairs in a bit, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400114V#6P#0300FYeah, yeah.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x104, 0x8)
    EndChrThread(0x101, 0x3)
    SetChrPos(0x101, 2450, 300, 125550, 180)
    SetChrSubChip(0x101, 0xC)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_776D():
        OP_96(0xFE, 0x3E8, 0x1E, 0x1EB68, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_776D)
    WaitChrThread(0x104, 1)
    Sleep(300)
    ClearChrFlags(0x104, 0x40)
    OP_93(0x104, 0xB4, 0x1F4)
    OP_68(2000, 700, 124000, 2000)

    def lambda_77AB():
        OP_96(0xFE, 0x0, 0x0, 0x1D6B4, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_77AB)
    WaitChrThread(0x104, 1)
    Sound(103, 0, 100, 0)

    def lambda_77CF():
        OP_96(0xFE, 0x0, 0x0, 0x1D0D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_77CF)

    def lambda_77E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_77E9)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    Sound(104, 0, 100, 0)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3400115V#5204F#5P#NWell, then...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1000, 1000, 126400, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 1000, 30, 126400, 270)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_68(1390, 1000, 128419, 1500)
    OP_93(0x101, 0x163, 0x190)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#3400116V#2P#5200FFourth day of the Anniversary Festival...\x02\x03",
            "#3400117VWe're going to have our work cut out for us.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetMapObjFrame(0xFF, "r_huton", 0x1, 0x1)
    SetMapObjFlags(0xD, 0x4)
    Call(0, 17)
    Return()

    # Function_15_6CB0 end

    def Function_16_7973(): pass

    label("Function_16_7973")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_798D")
    OP_A1(0xFE, 0x3E8, 0x4, 0x7, 0x8, 0x9, 0x8)
    Jump("Function_16_7973")

    label("loc_798D")

    Return()

    # Function_16_7973 end

    def Function_17_798E(): pass

    label("Function_17_798E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(12000, 1850, 9700, 0)
    MoveCamera(37, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26000, 0)
    SetChrPos(0x101, 11300, 850, 9100, 45)
    SetChrPos(0x102, 11300, 850, 10400, 135)
    SetChrPos(0x103, 12600, 850, 9100, 315)
    SetChrPos(0x104, 12600, 850, 10400, 225)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KCrossbell Anniversary Festival, Fourth Day\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    SetCameraDistance(25000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        (
            "#3400118V#6P#0004FAll right, it's the fourth day of the\x01",
            "festival... Time to get to work.\x02\x03",
            "#3400119V#0000FI'm sure a load of support requests were\x01",
            "submitted overnight, so let's take a look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3400120V#0102FRight. Today's the day of\x01",
            "the big parade, too...\x02\x03",
            "#3400121V#0104FNot to mention, there's likely\x01",
            "tourists trying to travel all over\x01",
            "Crossbell during the festival...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400122V#0202FA lot of requests have come through\x01",
            "the system. Lost belongings, missing\x01",
            "children, etcetera...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3400123V#5P#0306FMight be a little much to try and\x01",
            "tackle all of 'em at once.\x02\x03",
            "#3400124V#0300FLet's do what's within our power\x01",
            "and go from there, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400125V#6P#0000FYep, that's the plan.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(25250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(12000, 1850, 8700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrPos(0x1, 12000, 850, 8700, 270)
    SetChrPos(0x2, 12000, 850, 8700, 270)
    SetChrPos(0x3, 12000, 850, 8700, 270)
    SetScenarioFlags(0xA1, 4)
    OP_C7(0x1, 0x1000)
    OP_29(0x44, 0x1, 0x5)
    OP_29(0x45, 0x1, 0x5)
    OP_29(0x45, 0x4, 0x10)
    ModifyEventFlags(1, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_798E end

    def Function_18_7DE3(): pass

    label("Function_18_7DE3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50335.itc", 0x1E)
    LoadChrToIndex("apl/ch50011.itc", 0x1F)
    OP_68(1300, 2850, 12300, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 1300, 3850, 14800, 180)
    SetChrPos(0x102, 800, 0, 0, 0)
    SetChrPos(0x103, 800, 0, 0, 0)
    SetChrPos(0x104, 800, 0, 0, 0)
    SetChrFlags(0x160, 0x4)
    SetChrFlags(0x160, 0x2)
    SetChrFlags(0x160, 0x20)
    SetChrChipByIndex(0x160, 0x1E)
    SetChrSubChip(0x160, 0x0)
    SetChrPos(0x160, 16500, 950, 10400, 45)
    BeginChrThread(0x160, 3, 0, 19)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    OP_78(0xE, 0x1D)
    OP_49()
    SetChrPos(0x1D, 16200, 0, 10100, 0)
    OP_D3(0x1D, 0x0, 0xAFC8, 0x0, 0x0)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    BeginChrThread(0x20, 1, 0, 20)
    OP_68(1300, 1850, 10300, 2000)
    FadeToBright(1000, 0)

    def lambda_7F52():
        OP_96(0xFE, 0x514, 0x352, 0x283C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F52)

    def lambda_7F6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7F6C)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3400532V#6P#0005FHold on...\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(16100, 1850, 10000, 3000)
    SetCameraDistance(24000, 3000)

    def lambda_7FE8():
        OP_96(0xFE, 0x364C, 0x352, 0x283C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7FE8)
    OP_6F(0x1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7522", 0)

    ChrTalk(
        0x160,
        "#3400581V#3301F#5P...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#3400489V#6P#0001FAre you searching for information on\x01",
            "that vehicle through the orbal network?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400490V#3303F#5PCorrect.\x02\x03",
            "#3400491VI'm attempting to locate anything on vehicles\x01",
            "parked at the southeast part of the Harbor\x01",
            "District in the past hour...\x02\x03",
            "#3400492VOf course, I'm searching every orbal database\x01",
            "accessible from within Crossbell City.\x02\x03",
            "#3400493V#3300FOh? Perhaps I should hack the IBC's terminal\x01",
            "and that Geofront one that Freckles is so very\x01",
            "fond of.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#3400494V#6P#0006FYou can do that? Renne, just who ARE you?\x02\x03",
            "#3400495V#0001FI'm starting to think...that you definitely aren't\x01",
            "that doll maker's granddaughter. Is that right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400496V#3304F#5POh, Gramps is just an accomplice of mine.\x02\x03",
            "#3400497VHe's a friend who repaired my dear\x01",
            "Pater-Mater for me...\x02\x03",
            "#3400498V#3302FAnd since I distrust the professor, I had to\x01",
            "be discreet about asking for the fixes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400499V#6P#0011FA professor? Who are you talking about now?\x02\x03",
            "#3400500V#0001FAnd what the heck is a Pater-Mater?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400501V#3304F#5PDon't think too hard. You don't need to know.\x02\x03",
            "#3400502VAfter all, I've just come to observe Crossbell.\x02\x03",
            "#3400503V#3302FUnder the persona of Kitty, of course.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3400504V#6P#0003FI knew it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400505V#3309F#5PYou know, playing that little game of tag\x01",
            "was quite the fun time.\x02\x03",
            "#3400506VFreckles is formidable behind a terminal,\x01",
            "but that friend of yours knows her stuff, too.\x02\x03",
            "#3400507V#3302FThough, I have a sneaking suspicion that\x01",
            "an underhanded trick was played. Why, is\x01",
            "that not the rudest thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400508V#6P#0005F*sigh* You even figured that out?\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_86B2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_86B2)
    OP_68(900, 1000, 3000, 2500)
    SetCameraDistance(25000, 2500)
    Sleep(1500)

    def lambda_86DC():
        OP_96(0xFE, 0x384, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_86DC)

    def lambda_86F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_86F6)
    Sleep(450)

    def lambda_870A():
        OP_96(0xFE, 0x640, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_870A)

    def lambda_8724():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8724)
    Sleep(450)

    def lambda_8738():
        OP_96(0xFE, 0xC8, 0x0, 0x640, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8738)

    def lambda_8752():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8752)
    WaitChrThread(0x102, 1)

    def lambda_8767():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8767)
    WaitChrThread(0x104, 1)

    def lambda_8778():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8778)
    WaitChrThread(0x103, 1)

    def lambda_8789():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8789)
    WaitChrThread(0x103, 2)
    OP_6F(0x11)

    ChrTalk(
        0x102,
        (
            "#3400509V#0105F#6PWe're here, Lloyd! We came back as soon\x01",
            "as you told us, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#3400510V#0105F#6POh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400511V#0205F#6PThis girl again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400512V#0305F#12PAin't she that doll maker's grandkid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400513V#6P#0006FYeah. Well, we thought so. Trust me, there's\x01",
            "a long explanation behind all this, but that will\x01",
            "have to wait.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(13000, 1850, 10000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    OP_93(0x101, 0x10E, 0x0)
    SetChrPos(0x102, 6500, 850, 9800, 90)
    SetChrPos(0x103, 6500, 850, 10800, 90)
    SetChrPos(0x104, 5300, 850, 10300, 90)
    OP_68(15000, 1850, 10000, 2500)

    def lambda_89B1():
        OP_96(0xFE, 0x30D4, 0x352, 0x2648, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_89B1)
    Sleep(50)

    def lambda_89CE():
        OP_96(0xFE, 0x30D4, 0x352, 0x2A30, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_89CE)
    Sleep(50)

    def lambda_89EB():
        OP_96(0xFE, 0x2C24, 0x352, 0x283C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_89EB)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    EndChrThread(0x20, 0x1)
    Sleep(300)
    OP_63(0x160, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x160, 0x3)

    ChrTalk(
        0x160,
        "#3400514V#5P#3301FFound it.\x02",
    )

    CloseMessageWindow()

    def lambda_8A58():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8A58)
    Sleep(500)

    ChrTalk(
        0x160,
        (
            "#3400515V#5P#3308FIt looks like a Rhimes Deliveries delivery\x01",
            "truck was parked there 30 minutes ago.\x02\x03",
            "#3400516VAnd it was heading to Bellguard Gate.\x02\x03",
            "#3400517V#3304FNow, for the truck's number...\x01",
            "Ah, here it is.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x160, 0x0)
    Sleep(70)
    SetChrSubChip(0x160, 0x1)
    Sleep(70)
    SetChrSubChip(0x160, 0x2)
    Sleep(70)
    SetChrSubChip(0x160, 0x3)
    Sleep(300)

    ChrTalk(
        0x160,
        (
            "#3400518V#11P#3300FTry contacting the driver with this number.\x02\x03",
            "#3400519VI'm all but certain that this will lead us to our\x01",
            "missing boy.\x02",
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
    Sleep(1300)

    ChrTalk(
        0x101,
        "#3400520V#6P#0004FAwesome. Thanks, Renne.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400521V#6P#0108FUm, could you explain what's happening now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3400522V#6P#0306FYeah, man. I'm havin' a hard time following\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400523V#0203F#5POh, of course.\x02\x03",
            "#3400524V#0201FYou must be Kitty.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x102, 0x103, 500)

    ChrTalk(
        0x102,
        "#3400525V#12P#0105FKitty?! That's impossible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3400526V#6P#0301FYeah! You're tellin' me that this kid was the\x01",
            "one who's been giving us a hard time?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400527V#11P#3309FTeehee! I really appreciate you guys playing\x01",
            "with me yesterday. It was oh-so fun.\x02\x03",
            "#3400528V#3302FHowever, wouldn't an unnecessary explanation\x01",
            "be more appropriate after you find the boy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400529V#0206F#5PShe makes a valid point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400530V#6P#0001FAll right, then. I'll give their number a call and\x01",
            "see if they pick up!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)

    def lambda_8F9B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8F9B)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd called the phone number he received.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(902, 0, 100, 0)
    Sleep(2700)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400531V\x07\x05",
            "Rhimes Deliveries. How can I help you?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400487V\x07\x00",
            "#0005FUh, hello there.\x02\x03",
            "#3400533V#0001FSorry to bother you, but I'm with the CPD,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400534V\x07\x05",
            "...!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#3400535V\x07\x05",
            "OH, THANK AIDIOS!\x01",
            "I was minutes away from calling the Bracer Guild or\x01",
            "the police!\x02\x03",
            "#3400536VBut I didn't have either of their numbers memorized,\x01",
            "so I just called Father and...and...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400537V\x07\x00",
            "#0011FP-Please, sir, just take a deep breath.\x02\x03",
            "#3400538V#0001FYou sound like you're in a panic...\x01",
            "Has something happened?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400539V\x07\x05",
            "W-Well, y'see...\x02\x03",
            "#3400540VTh-That little kid ran off somewhere! I have no\x01",
            "clue where, though!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400541V\x07\x00",
            "#0005FHuh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400542V\x07\x05",
            "I'm currently parked in the middle of West\x01",
            "Crossbell Highway!\x02\x03",
            "#3400543VI went to check my load after hearing some\x01",
            "sounds, and I found that kid in the back!\x02\x03",
            "#3400544VHe must have snuck in somehow! I knew that\x01",
            "taking him to Bellguard Gate would be a mess,\x01",
            "so I just panicked and called the company...!\x02\x03",
            "#3400545VBut while I was on the call, he must have went\x01",
            "and wandered away from the truck!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400546V\x07\x00",
            "#0013F...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x102,
        "#3400547V#0101FLloyd, what's the matter?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sleep(300)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(820, 0, 100, 0)
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        "#3400548V#11P#0001FWell, we've got a bit of an issue.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd briefly explained the situation to the others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x160, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
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
        0x160,
        "#3400549V#11P#3305FHe what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400550V#0201F#5PUnbelievable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400551V#6P#0301FThis is bad news, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400552V#11P#0003FAgreed. Let's hurry and locate the driver.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x1)
    Sound(820, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400553V#0001FListen! We're heading your way ASAP!\x02\x03",
            "#3400554VDon't move a muscle, okay? Keep your\x01",
            "truck exactly where it's parked.\x02\x03",
            "#3400555VThere's always a chance he'll come back.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400556V\x07\x05",
            "R-Right!\x02\x03",
            "#3400557VJust hurry, okay? This is stressing me out!\x02",
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
    Sound(807, 0, 100, 0)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#3400558V#11P#0003FEveryone, we're heading to the west exit.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        "#3400559V#0001F#6PAnd Renne, you can...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(14790, 1850, 10210, 500)
    ClearChrFlags(0x160, 0x4)
    ClearChrFlags(0x160, 0x2)
    ClearChrFlags(0x160, 0x20)
    SetChrChipByIndex(0x160, 0xFF)
    SetChrSubChip(0x160, 0x0)
    SetChrPos(0x160, 15300, 950, 10300, 315)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_93(0x160, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x160,
        (
            "#3400560V#11P#3300FI'm tagging along with you, of course.\x02\x03",
            "#3400561VI promise that I won't slow you down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400562V#6P#0105FIs that a good idea? She's just a little girl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400563V#0205F#5PI think it would be safer if you waited here\x01",
            "for us to return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400564V#11P#3303FDid you forget already? I was the one who\x01",
            "discovered the boy's whereabouts.\x02\x03",
            "#3400565V#3300FThus, I have an obligation to see how this\x01",
            "unfolds...\x02\x03",
            "#3400566V#3302F...no matter what fate has in store for him.\x01",
            "Heeheehee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400567V#6P#0101FThat...sounds ominous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3400568V#6P#0306FI don't know what your deal is, kid, but I guess\x01",
            "it's true that you're invested in this mission.\x02\x03",
            "#3400569V#0301FTime's a-wastin', Lloyd. C'mon, let's just let the\x01",
            "kid tag along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400570V#0006F#6PYou're right.\x02\x03",
            "#3400571V#0001FRenne. I know you aren't an ordinary girl, but\x01",
            "that doesn't mean you can do anything crazy. I\x01",
            "need you to let us handle whatever happens.\x02\x03",
            "#3400572VCan you do that for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400573V#11P#3306FFine, fine.\x02\x03",
            "#3400574V#3300FIn return, please stop treating me like an inept\x01",
            "child who can do nothing but play and cry.\x02\x03",
            "#3400575VYour concern has become quite embarrassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400576V#0004F#6PI guess that's fair.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#3400577V#11P#0007FAll right, everyone. To the west exit!\x02\x03",
            "#3400578VOur plan is to get to West Crossbell\x01",
            "Highway and commence our search\x01",
            "for Colin right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400579V#6P#0101FRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400580V#0201F#5PMission accepted!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3400488V#11P#3308F...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x1D, 0x80)
    ClearMapObjFlags(0xE, 0x1000)
    SetMapObjFlags(0xE, 0x4)
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
    SetChrPos(0x4, 12000, 850, 8700, 270)
    SetScenarioFlags(0xA2, 7)
    OP_29(0x46, 0x1, 0xC)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_7DE3 end

    def Function_19_A094(): pass

    label("Function_19_A094")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A0AE")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x6, 0x7, 0x6)
    Jump("Function_19_A094")

    label("loc_A0AE")

    Return()

    # Function_19_A094 end

    def Function_20_A0AF(): pass

    label("Function_20_A0AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A0D7")
    Sound(849, 0, 70, 0)
    Sound(850, 0, 70, 0)
    Sleep(900)
    Sound(849, 0, 70, 0)
    Sleep(900)
    Jump("Function_20_A0AF")

    label("loc_A0D7")

    Return()

    # Function_20_A0AF end

    def Function_21_A0D8(): pass

    label("Function_21_A0D8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50343.itc", 0x1E)
    LoadChrToIndex("chr/ch09300.itc", 0x1F)
    LoadChrToIndex("chr/ch09400.itc", 0x20)
    LoadChrToIndex("apl/ch50344.itc", 0x21)
    LoadChrToIndex("apl/ch50345.itc", 0x22)
    OP_68(3000, 700, 127500, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 0, 0, 119000, 0)
    SetChrPos(0x102, 0, -1000, 118000, 0)
    SetChrPos(0x103, 0, 0, 119000, 0)
    SetChrPos(0x104, 0, 0, 119000, 0)
    SetChrPos(0x160, 1000, 30, 125300, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrPos(0xD, 3000, 350, 126100, 180)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xE, 0, -1000, 118000, 0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, 0, 0, 119000, 0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "r_huton", 0x0, 0x1)
    ClearMapObjFlags(0xD, 0x4)
    OP_70(0xD, 0x5)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis058.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis059.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis060.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis061.itp")
    OP_68(3000, 700, 126000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sound(811, 0, 100, 0)
    Sleep(1000)
    Sound(103, 0, 100, 0)

    def lambda_A32B():
        OP_95(0xFE, 0, 0, 122000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A32B)

    def lambda_A345():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A345)
    Sleep(1000)

    def lambda_A359():

        label("loc_A359")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_A359")

    QueueWorkItem2(0x160, 2, lambda_A359)
    WaitChrThread(0x101, 1)

    def lambda_A36F():
        OP_95(0xFE, 1000, 30, 124000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A36F)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x101, 1)
    EndChrThread(0x160, 0x2)

    ChrTalk(
        0x101,
        "#3400683V#12P#0002FDid he doze off already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3400684V#3304F#5PHeeheehee...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x160, 0x20)
    SetChrFlags(0x160, 0x2)
    SetChrChipByIndex(0x160, 0x21)
    SetChrSubChip(0x160, 0x0)
    Sleep(70)
    SetChrSubChip(0x160, 0x1)
    Sleep(70)
    SetChrSubChip(0x160, 0x2)
    Sleep(70)
    SetChrSubChip(0x160, 0x3)
    Sleep(500)

    ChrTalk(
        0x160,
        (
            "#3400685V#3300F#5PHe sure is cute when he sleeps.\x02\x03",
            "#3400686VA pure, innocent child\x01",
            "who doesn't know sin.\x02\x03",
            "#3400687V#3304FHe's grown so much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400688V#12P#0008F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x160, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3400689V#12P#0003FRenne, you should know I just contacted\x01",
            "his parents.\x02\x03",
            "#3400690V#0000FThey dropped whatever they were doing and\x01",
            "are on their way now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3400691V#3308F#5PIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400692V#12P#0001FYou saved his life, Renne. You. Not us.\x02\x03",
            "#3400693VI think it's only right that we introduce\x01",
            "you to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400694V#3303F#5PThank you, but there is no need.\x02\x03",
            "#3400695V#3300FMy name, my mere existence... I would rather\x01",
            "you not tell them. It's unnecessary, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400696V#12P#0008FDo you really think that...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#3400697V#12P#0001FListen, Renne.\x02\x03",
            "#3400698VIt's obvious that you're something special. Girls your\x01",
            "age aren't supposed to be able to do what you do.\x02\x03",
            "#3400699V#0003FYour skill with that scythe...\x01",
            "Your hacking as Kitty...\x02\x03",
            "#3400700VYour logic and analytical skills were the key\x01",
            "to finding Colin...\x02\x03",
            "#3400701V#0008FHonestly, it's hard to believe that someone as\x01",
            "brilliant as you even exists in the first place.\x02\x03",
            "#3400702V#0000FI don't think it would be an exaggeration to call\x01",
            "what you possess true genius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3400703V#3304F#5PHeehee...\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x160, 0x21)
    SetChrSubChip(0x160, 0x3)
    Sleep(70)
    SetChrSubChip(0x160, 0x2)
    Sleep(70)
    SetChrSubChip(0x160, 0x1)
    Sleep(70)
    ClearChrFlags(0x160, 0x20)
    ClearChrFlags(0x160, 0x2)
    SetChrChipByIndex(0x160, 0xFF)
    SetChrSubChip(0x160, 0x0)
    Sleep(300)

    ChrTalk(
        0x160,
        (
            "#3400704V#3302F#5PLooks like you CAN put that brain\x01",
            "of yours to good use.\x02\x03",
            "#3400705V#3304FYes. That's the essence of who I am.\x02\x03",
            "#3400706VI can process information and immediately\x01",
            "make the appropriate adjustments to nearly\x01",
            "any situation I'm placed in...\x02\x03",
            "#3400707V#3300FMy combat, hacking, doctoral dissertations,\x01",
            "archaism control, and not to mention tea etiquette...\x01",
            "All of it is made possible by my true essence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400708V#1B#6Z#31B#60Z#67B#70Z#12P#0011FDoctoral dissertations?!\x02\x03",
            "#3400709V#0B#5Z#36B#74Z#0003F#0ENever mind--that's not important.\x02\x03",
            "#3400710V#0003FWhat I mean to say is this.\x02\x03",
            "#3400711V#0001FYou are painfully aware of what it takes to\x01",
            "make your dreams a reality. How could you\x01",
            "not be, with how smart you are?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400712V#3309F#5PI'm inclined to agree with you there.\x02\x03",
            "#3400713V#3302FDespite how impossible something may seem,\x01",
            "I know what is necessary to make it happen.\x02\x03",
            "#3400714VNo, that's not quite right. To be more accurate,\x01",
            "I know how to manipulate the world into giving\x01",
            "me whatever I want.\x02\x03",
            "#3400715V#3304FThat's my true power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400716V#12P#0006FSo, that's how you see it.\x02\x03",
            "#3400717V#0001FThen... What do you actually wish for? From the\x01",
            "bottom of your heart, what do you want most?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x160, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x160,
        "#3400718V#3305F#5PPardon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400719V#12P#0003FYou said it. You're the world's very own princess.\x01",
            "One who can be granted whatever she desires...\x02\x03",
            "#3400720VBut I don't buy that. To me, you look like a lost\x01",
            "kitten, confused about where she is and where\x01",
            "she should go.\x02\x03",
            "#3400721V#0008F...I take that back. Maybe you actually do know\x01",
            "where you should go.\x02\x03",
            "#3400722VPerhaps you think there are too many obstacles\x01",
            "standing in your way. You don't think that you can\x01",
            "make it there.\x02\x03",
            "#3400723V#0001FI'm right, aren't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3400737V#3308F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400725V#12P#0004FThat's just what my intuition is telling me, so\x01",
            "I apologize if I'm out of line or off-base.\x02\x03",
            "#3400726V#0000FBut remember: We're the Special Support Section.\x02\x03",
            "#3400727VIf we find someone in need, we want to help them\x01",
            "to the best of our ability. That includes you, Renne.\x02\x03",
            "#3400728V#0002FEven if we can't walk you all the way home, we can at\x01",
            "least give you the first boost you need to overcome those\x01",
            "obstacles. We have some experience in it ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400729V#3309F#5PHeehee.\x02\x03",
            "#3400730V#3300FI wasn't expecting your ability to conjure up delusions\x01",
            "to be as equally impressive as your reasoning skills.\x02\x03",
            "#3400731V#3302FHow could someone like you possibly understand\x01",
            "someone like me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400732V#12P#0006FI can't. And I'm not pretending to.\x02\x03",
            "#3400733VBut maybe others can. People that you want nothing\x01",
            "more than to trust and rely on.\x02\x03",
            "#3400734V#0000FAfter all, there isn't just a single obstacle in your\x01",
            "path, is there?\x02\x03",
            "#3400735VWhere's the harm in leaning on us just a little\x01",
            "bit as you begin your climb?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400736V#3308F#5P#30WY-You...have no clue...\x02\x03",
            "#3400724V#3306F#40W...!\x02",
        )
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x160, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0xBE, 0x1F4)

    NpcTalk(
        0x102,
        "Elie's Voice",
        (
            "#3400738V#1P#2SLloyd? The Hayworths just arrived.\x02\x03",
            "#3400739V#2SI'm sending them in, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400740V#0011F#5PW-Wait a second, Elie!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x160, 500)
    Sleep(800)

    ChrTalk(
        0x160,
        "#3400741V#3308F#40W#5P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#3400742V#12P#0000FHey. If you want, you can hide in that\x01",
            "closet, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400743V#3305F#5P...!\x02\x03",
            "#3400744V#3306F*nod*\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B655():

        label("loc_B655")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_B655")

    QueueWorkItem2(0x101, 2, lambda_B655)

    def lambda_B667():
        OP_96(0xFE, 0x0, 0x1E, 0x1E460, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B667)
    Sleep(500)

    def lambda_B684():
        OP_95(0xFE, 1000, 0, 122500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_B684)
    WaitChrThread(0x160, 1)

    def lambda_B6A2():
        OP_95(0xFE, 2000, 30, 121500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_B6A2)
    WaitChrThread(0x160, 1)
    SetMapObjFrame(0xFF, "boxopen", 0x2, "move")
    Sound(913, 0, 100, 0)
    Sleep(500)

    def lambda_B6D9():
        OP_96(0xFE, 0xBB8, 0x1E, 0x1D8A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_B6D9)

    def lambda_B6F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_B6F3)
    WaitChrThread(0x160, 1)
    WaitChrThread(0x160, 2)
    EndChrThread(0x101, 0x2)
    SetMapObjFrame(0xFF, "boxopen", 0x2, "move2")
    Sound(914, 0, 100, 0)
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        "#3400745V#0000F#5PAll right, Elie! You can send them in now.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Elie's Voice",
        "#3400746V#1P#2S...? S-Sure, we're coming in now.\x02",
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)

    NpcTalk(
        0xE,
        "Man's Voice",
        "#3400747V#1P#2SMy boy!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xE, 0, 0, 119000, 0)
    Sound(103, 0, 100, 0)
    BeginChrThread(0xE, 3, 0, 22)
    Sleep(500)

    def lambda_B81E():

        label("loc_B81E")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_B81E")

    QueueWorkItem2(0x101, 2, lambda_B81E)

    def lambda_B830():
        OP_96(0xFE, 0xFFFFFC7C, 0x1E, 0x1EC30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B830)
    BeginChrThread(0xF, 3, 0, 23)
    Sleep(500)

    ChrTalk(
        0xF,
        "#3400748V#3707F#5P#8AColin!\x02",
    )

    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    EndChrThread(0x101, 0x2)

    ChrTalk(
        0xE,
        "#3400749V#3609F#5PAidios, thank you! Oh, thank you!\x02",
    )

    CloseMessageWindow()
    OP_68(1000, 700, 126000, 2500)
    MoveCamera(45, 21, 0, 2500)
    SetCameraDistance(24000, 2500)
    SetChrPos(0x102, 0, 0, 119000, 0)

    def lambda_B8EE():
        OP_96(0xFE, 0xFFFFFC7C, 0x1E, 0x1E654, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B8EE)

    def lambda_B908():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B908)
    Sleep(500)

    def lambda_B91C():
        OP_96(0xFE, 0xFFFFFBB4, 0x1E, 0x1E0DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B91C)

    def lambda_B936():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B936)
    Sleep(500)

    def lambda_B94A():
        OP_96(0xFE, 0xFFFFFF9C, 0x1E, 0x1E0DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B94A)

    def lambda_B964():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B964)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#3400750V#12P#0105F(Where's Renne?)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#3400751V#0006F#5P(Well, one thing led to another, and...)\x02\x03",
            "#3400752V#0008F(...she's hiding in the closet over there.)\x02",
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
        "#3400753V#12P#0101F(She's what?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400754V#12P#0205F(Why would she do that?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400755V#12P#0305F(Feels like we're missin' something.)\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)

    def lambda_BB32():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BB32)

    def lambda_BB3F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BB3F)

    def lambda_BB4C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BB4C)

    def lambda_BB59():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BB59)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#3400756V#11P#3610FThank you, everyone. Thank you so much.\x02\x03",
            "#3400757V#3601FFor as long as I may live, I will never forget\x01",
            "what you have done for us today.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Harold deeply bowed his head in appreciation.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#3400758V#6P#0011FP-Please! You don't have to thank us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400759V#6P#0100FRight. We were just doing our jobs.\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x10E, 0x1F4)

    ChrTalk(
        0xF,
        (
            "#3400760V#3701F#11PNo, you don't understand the gravity of this!\x02\x03",
            "#3400761V#3708FIf you hadn't found him, Colin would be...\x01",
            "We could have...\x02\x03",
            "#3400762V#3710FTruly... Thank you...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 500)
    Sleep(300)

    ChrTalk(
        0xE,
        "#3400763V#3600FIt's all right, honey... Everything is fine now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400764V#12P#0301FHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400765V#6P#0208FWhy are they...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3400766V#11P#60WMm...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(3000, 700, 126000, 1500)
    MoveCamera(45, 24, 0, 1500)
    SetCameraDistance(23500, 1500)

    def lambda_BEDE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_BEDE)

    def lambda_BEEB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_BEEB)
    Sleep(1200)
    Fade(250)
    SetChrChipByIndex(0xD, 0x22)
    SetChrSubChip(0xD, 0x1)
    OP_0D()
    Sound(820, 0, 100, 0)
    SetChrSubChip(0xD, 0x0)
    Sleep(250)
    SetChrSubChip(0xD, 0x1)
    Sleep(250)
    SetChrSubChip(0xD, 0x0)
    Sleep(250)
    SetChrSubChip(0xD, 0x1)
    OP_6F(0x79)

    ChrTalk(
        0xF,
        "#3400797V#6P#3700FColin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3400779V#11P#3805FHuh?\x02\x03",
            "#3400769VWhy are Mama and Papa here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#3400770V#6P#3709FOh, Colin!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3400771V#6P#3609FThank the Goddess! He's okay!\x02\x03",
            "#3400772V#3600FDon't you know how much you made\x01",
            "Mama and Papa worry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3400773V#11P#3800FWhat do you mean?\x02\x03",
            "#3400774V#3809FOh! I had SO much fun today!\x02\x03",
            "#3400775VFirst, I followed the Mishy car aaall over the city,\x01",
            "and I made tons of new friends!\x02\x03",
            "#3400776VWhen we were playing hide and seek, I thought\x01",
            "I would hide in this big truck. But, then the lights\x01",
            "went out, and it started to move!\x02\x03",
            "#3400777VWhen I finally got out, I saw this yellow butterfly\x01",
            "and started to chase it! It was sooooo pretty!\x02\x03",
            "#3400778V#3802FAnd then, and then...!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0xFFFFFE70, 1200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "#3400768V#11P#3805FUm... Wait...\x02\x03",
            "#3400780VWhere's the purple girl?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#3400781V#6P#3605FPurple...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#3400782V#6P#3700F...girl?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3400783V#11P#3809FYeah!\x02\x03",
            "#3400784VYou should have seen her!\x01",
            "She was SO strong!\x02\x03",
            "#3400785VShe was nice and smelled nice...!\x02\x03",
            "#3400786V#3802FAnd she had purple hair just like Papa's!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        "#3400787V#6P#3705FWhat?\x02",
    )

    CloseMessageWindow()

    def lambda_C3DB():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_C3DB)
    Sleep(50)
    OP_93(0xF, 0x10E, 0x190)
    Sleep(200)

    ChrTalk(
        0xE,
        (
            "#3400788V#11P#3601FExcuse me, everyone. Just who is this girl\x01",
            "that he's talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400789V#6P#0006FWell... There was a girl who offered to\x01",
            "help us search for Colin.\x02\x03",
            "#3400790V#0008FShe might have been a tourist, but we can't be\x01",
            "sure. She didn't tell us much about herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#3400791V#11P#3603FI-I see. Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#3400792V#11P#3708FSo that's what happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3400793V#5P#3809F#40W*yawn* I wish...that I could see her again...\x02\x03",
            "#3400794V#60WSo we could play together...one last time...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(500)

    def lambda_C60B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_C60B)
    Sleep(50)
    OP_93(0xE, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xF,
        "#3400795V#6P#3705F...?\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0xD,
        "#3400796V#5P#60WZzz... Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#3400767V#6P#3700FColin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#3400798V#6P#3600FIt looks like he went right back to sleep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400799V#6P#0004FHe's welcome to rest here as long as\x01",
            "he needs, Mr. Hayworth.\x02\x03",
            "#3400800V#0000FWe don't mind. Honestly.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1420, 700, 126070, 2000)
    MoveCamera(45, 21, 0, 2000)
    SetCameraDistance(24000, 2000)

    def lambda_C76B():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_C76B)
    Sleep(100)
    OP_93(0xF, 0x10E, 0x190)
    OP_6F(0x79)

    ChrTalk(
        0xE,
        (
            "#3400801V#11P#3609FYou've already done so much for us.\x02\x03",
            "#3400802V#3600FA girl with the same hair as me, though?\x02\x03",
            "#3400803V#3604FPerhaps this was the protection of the\x01",
            "Goddess and...that child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#3400804V#3700F#11PIt must be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400805V#6P#0001FExcuse me, but do you know something that\x01",
            "we don't?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#3400806V#11P#3605FWell, you see...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 400)

    ChrTalk(
        0xF,
        (
            "#3400807V#3700FIt's okay, dear. You can tell them.\x02\x03",
            "#3400808VThey've done so much for us. It's only fair that\x01",
            "we share our story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#3400809V#11P#3600FYou're right.\x02",
    )

    CloseMessageWindow()

    def lambda_C996():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_C996)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)

    ChrTalk(
        0xE,
        (
            "#3400810V#11P#3603FThe truth is...we once had a daughter.\x02\x03",
            "#3400811VBut that was more than seven years ago.\x02",
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
        "#3400877V#6P#0005F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400813V#6P#0101FDoes that mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3400814V#11P#3608FYes. We lost her in a terrible accident...\x02\x03",
            "#3400815V#3610FNo, accident is too forgiving a word.\x02\x03",
            "#3400816V#3601FOur daughter... We may as well\x01",
            "have killed her ourselves.\x02",
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
        0x103,
        "#3400817V#6P#0205FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400818V#12P#0301FWhat are you saying...?\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7513", 0)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#3400819V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30WEight years ago...\x02\x03",
            "#3400820V#30WI had just started my trading business. I was\x01",
            "struggling to survive in Crossbell's growing,\x01",
            "cutthroat market.\x02\x03",
            "#3400821V#30WAs a result, I took a risk investing in a\x01",
            "company from the Calvard Republic.\x02\x03",
            "#3400822V#30WI racked up a very large debt in the process.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#3400823V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30WSo, we lived on the run with our little girl...\x02\x03",
            "#3400824VWe ran and ran and ran, but the debt collectors\x01",
            "always caught up... No place was safe for us.\x02\x03",
            "#3400825V#30WIt was only a matter of time before the mafia\x01",
            "decided to settle things once and for all.\x02\x03",
            "#3400826V#30WFearing that, we entrusted our daughter to an\x01",
            "old friend.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#3400827V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30WThis friend lived in the Republic, and he was\x01",
            "someone I trusted dearly.\x02\x03",
            "#3400828V#30WMy intention was to repay my debts and, after\x01",
            "wiping my slate clean, return for our daughter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#3400829V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30WLuckily, with sound advice from a reliable lawyer,\x01",
            "we were able to crawl out of debt.\x02\x03",
            "#3400830V#30WI rebuilt my livelihood by using every connection\x01",
            "at my disposal and working relentlessly.\x02\x03",
            "#3400831V#30WSomehow, someway... I managed to repay the\x01",
            "entire sum in just one year.\x02\x03",
            "#3400832V#30WIt meant I could finally see my daughter again.\x01",
            "We could go back to being a family again...\x02\x03",
            "#3400833V#30WOr at least, that's what I thought. When we\x01",
            "returned to my friend's estate...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(1500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#3400834V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W...it was gone. Burned down in a fire.\x02\x03",
            "#3400835V#30WAt that time, there was a rampant string\x01",
            "of organized arson and burglary cases in\x01",
            "Calvard.\x02\x03",
            "#3400836V#30WMy friend's home was one such victim.\x02\x03",
            "#3400837V#30WBecause it was in a rural area, the authorities\x01",
            "were unaware and hadn't responded.\x02\x03",
            "#3400838V#30WAnd...our daughter, who we'd entrusted to him\x01",
            "for that year...was...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#3400839V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30WWe searched. We searched and searched as\x01",
            "frantically as we could, but...\x02\x03",
            "#3400840V#30W...the bodies were beyond recognition. Autopsies\x01",
            "revealed that the fire was so intense that anyone\x01",
            "caught in it would have perished.\x02\x03",
            "#3400841V#30WOur daughter... Our irreplaceable treasure...was\x01",
            "gone forever.\x02\x03",
            "#3400842V#30WAll that remained was...despair.\x02\x03",
            "#3400843V#30WAfter sending our only daughter to her death,\x01",
            "we no longer knew what we were living for...\x02\x03",
            "#3400844V#30WWe even thought about taking our own lives.\x02\x03",
            "#3400845V#30WBut then, Sophia discovered...she was pregnant.\x02\x03",
            "#3400846V#30WShe was carrying our second child, Colin--the\x01",
            "little brother our baby girl would never know.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#3400847V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30WColin became our everything--our new reason\x01",
            "for living.\x02\x03",
            "#3400848V#30WI then dedicated myself to honest trade,\x01",
            "determined to avoid repeating past mistakes.\x02\x03",
            "#3400849V#30WOnce Colin was born, we felt as if we could\x01",
            "finally start over.\x02\x03",
            "#3400850V#30WThough, in doing that, all we were truly doing\x01",
            "was living in denial.\x02\x03",
            "#3400851V#30WAnd not just the denial of our grief from losing\x01",
            "our daughter. We were also in denial of our guilt...\x02\x03",
            "#3400852V#30WThe guilt we held for the sin we had committed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    SetCameraDistance(24000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0xF,
        "#3400853V#3710F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3400854V#11P#3608FThat...is the burden we carry.\x02\x03",
            "#3400855V#3603FForgive me for subjecting you to all of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400856V#6P#0008FSo, that's your story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400857V#6P#0106FI... I don't know what to say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400858V#12P#0306FFate can be a real bitch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400859V#6P#0208F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#3400860V#3708F#11PAs our son grew older, it became uncanny\x01",
            "how much he resembled our daughter.\x02\x03",
            "#3400861VThat's all it took. Our little boy's face brought\x01",
            "back those pangs of guilt we tried to bury.\x02\x03",
            "#3400862V#3710FWe never should have abandoned her.\x01",
            "How could we ever let her go like we did...?\x02\x03",
            "#3400863VFamilies are supposed to stay together,\x01",
            "no matter how painful things are. What\x01",
            "kind of parent leaves their child behind?\x02\x03",
            "#3400864VWe were consumed by that regret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3400865V#11P#3603FAnd so, we resolved to look at things in\x01",
            "a different, more optimistic light.\x02\x03",
            "#3400866V#3600FWe believe that it was through our daughter...\x01",
            "and the guidance of the Goddess Herself that\x01",
            "we were blessed to have Colin.\x02\x03",
            "#3400867VTherefore, to honor that blessing, our family\x01",
            "must persevere and find peace.\x02\x03",
            "#3400868VThat's the only way that we can repay our\x01",
            "daughter for watching over us as she has.\x02\x03",
            "#3400869V#3603FBelieve me, we're painfully aware of how\x01",
            "selfish it sounds, but...it's all we can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400870V#6P#0108FMr. Hayworth...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400871V#6P#0204FIt is a respectable sentiment.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#3400872V#12P#0302FYeah. Sometimes, the best way to mourn\x01",
            "someone is to move forward with them\x01",
            "in your heart, rather than stand still.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3400873V#11P#3609FHaha... Thank you for saying so.\x01",
            "I hope you're right.\x02\x03",
            "#3400874V#3600FThat aside, there's something I still\x01",
            "don't understand.\x02\x03",
            "#3400875VThe girl that helped Colin had purple\x01",
            "hair like mine, is that right?\x02\x03",
            "#3400876V#3604FOur late daughter also had my purple\x01",
            "hair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400812V#6P#0005FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400878V#6P#0108FThen...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#3400879V#3709F#11PYes. It's as if our little girl came down\x01",
            "from heaven to protect Colin herself.\x02\x03",
            "#3400880V#3700FWould you do me a favor, everyone?\x02\x03",
            "#3400881VIf you happen to see her again, could\x01",
            "you let us know? Please?\x02\x03",
            "#3400882VWe'd love to have the honor to meet her\x01",
            "and...to give her our sincerest thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400883V#6P#0003FOf course.\x02\x03",
            "#3400884V#0000FIf we do see her again, we'll pass along\x01",
            "the message.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x202), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x160, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c020C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_A0D8 end

    def Function_22_E2EB(): pass

    label("Function_22_E2EB")


    def lambda_E2F0():
        OP_95(0xFE, 0, 0, 122000, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E2F0)

    def lambda_E30A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_E30A)
    WaitChrThread(0xE, 1)

    def lambda_E31F():
        OP_95(0xFE, 1200, 30, 125700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E31F)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x5A, 0x1F4)
    Return()

    # Function_22_E2EB end

    def Function_23_E340(): pass

    label("Function_23_E340")


    def lambda_E345():
        OP_95(0xFE, 0, 0, 122000, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E345)

    def lambda_E35F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_E35F)
    WaitChrThread(0xF, 1)

    def lambda_E374():
        OP_95(0xFE, 1200, 30, 124700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E374)
    WaitChrThread(0xF, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_23_E340 end

    def Function_24_E392(): pass

    label("Function_24_E392")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch00600.itc", 0x22)
    LoadChrToIndex("apl/ch50346.itc", 0x23)
    LoadChrToIndex("chr/ch00700.itc", 0x24)
    LoadChrToIndex("apl/ch50349.itc", 0x25)
    LoadChrToIndex("apl/ch50115.itc", 0x26)
    OP_68(0, 900, 121500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 100, 30, 121800, 90)
    SetChrPos(0x104, 200, 30, 123100, 135)
    SetChrPos(0x103, -800, 30, 123000, 135)
    SetChrPos(0x102, -1300, 30, 121300, 90)
    SetChrPos(0x160, 3000, 30, 121000, 315)
    OP_A7(0x160, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00900.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_68(1500, 900, 121500, 3000)
    FadeToBright(2000, 0)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#3400885V#6P#0003FThey left, Renne.\x02\x03",
            "#3400886V#0000FIt's okay. You can come out now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x160,
        "Renne",
        "#3400887V#2S#11P#40W...\x02",
    )

    CloseMessageWindow()
    SetMapObjFrame(0xFF, "boxopen", 0x2, "move")
    Sound(913, 0, 100, 0)
    Sleep(500)
    SetCameraDistance(21500, 2500)

    def lambda_E5B4():
        OP_96(0xFE, 0x7D0, 0x1E, 0x1DA9C, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_E5B4)

    def lambda_E5CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_E5CE)
    WaitChrThread(0x160, 1)
    WaitChrThread(0x160, 2)
    SetMapObjFrame(0xFF, "boxopen", 0x2, "move2")
    Sound(914, 0, 100, 0)
    Sleep(500)
    OP_93(0x160, 0x10E, 0x190)
    Sleep(500)

    ChrTalk(
        0x160,
        "#3400888V#11P#3313F#60W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400889V#6P#0105FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400890V#0208F#6PRenne...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400891V#6P#0008FHey. Are you really okay with this?\x02\x03",
            "#3400892V#0001FIf you run, I'm sure you'd be able to\x01",
            "catch up with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400893V#11P#3312F#40WNo... It's fine.\x02\x03",
            "#3400894VIt's just that...one of my reasons for coming\x01",
            "to Crossbell is gone now.\x02\x03",
            "#3400895V#3314FSo, this is fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400896V#6P#0006FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3400897V#6P#0101FBut...are you sure?\x02\x03",
            "#3400898VHave you truly thought this all the way\x01",
            "through? Renne, aren't they your--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x104,
        (
            "#3400899V#0306F#5PEasy there, Mademois-Elie.\x02\x03",
            "#3400900V#0301FThere are some things in this world that can't\x01",
            "so easily be fixed. You know it--I know it.\x02\x03",
            "#3400901VThis one's way out of our jurisdiction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400902V#6P#0108FI-I know that, but...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        "#3400903V#0206FI am inclined to agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400904V#6P#0008F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400905V#11P#3314F#40WPlease... There's no reason to make\x01",
            "such a sad face.\x02\x03",
            "#3400906V#3312F#40WThank you, Detective.\x02\x03",
            "#3400907VYou were right. There have been\x01",
            "#40Wobstacles blocking my way home.\x02\x03",
            "#3400908V#3300FSo, thank you for removing that one.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EA7D():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_EA7D)
    Sleep(50)

    def lambda_EA8D():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_EA8D)

    ChrTalk(
        0x101,
        (
            "#3400909V#6P#0006FWell, all right.\x02\x03",
            "#3400910V#0000FAlways glad to be of service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400911V#11P#3300FOf course, it would be rude of me to ignore the\x01",
            "rest of you. Thank you, too, Elie, Tio, and Randy.\x02\x03",
            "#3400912V#3312FI promise that I'll find a way to repay you\x01",
            "for all you've done for me.\x02\x03",
            "#3400913V#3314FFor now, I'll have to excuse myself.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrFlags(0x160, 0x20)
    SetChrFlags(0x160, 0x2)
    SetChrChipByIndex(0x160, 0x26)
    SetChrSubChip(0x160, 0x4)
    Sleep(100)
    SetChrSubChip(0x160, 0x5)
    Sleep(100)
    SetChrSubChip(0x160, 0x6)
    Sound(820, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0x160, 0x7)
    Sleep(1000)
    SetChrSubChip(0x160, 0x6)
    Sleep(100)
    SetChrSubChip(0x160, 0x5)
    Sleep(100)
    ClearChrFlags(0x160, 0x20)
    ClearChrFlags(0x160, 0x2)
    SetChrChipByIndex(0x160, 0xFF)
    SetChrSubChip(0x160, 0x0)
    Sleep(500)
    OP_92(0x160, 0x0, 0x1D650, 0x1F4)

    def lambda_EC5B():

        label("loc_EC5B")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_EC5B")

    QueueWorkItem2(0x101, 2, lambda_EC5B)

    def lambda_EC6D():

        label("loc_EC6D")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_EC6D")

    QueueWorkItem2(0x102, 2, lambda_EC6D)

    def lambda_EC7F():

        label("loc_EC7F")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_EC7F")

    QueueWorkItem2(0x103, 2, lambda_EC7F)

    def lambda_EC91():

        label("loc_EC91")

        TurnDirection(0xFE, 0x160, 500)
        Yield()
        Jump("loc_EC91")

    QueueWorkItem2(0x104, 2, lambda_EC91)

    def lambda_ECA3():
        OP_95(0xFE, 0, 0, 120400, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_ECA3)
    WaitChrThread(0x160, 1)
    Sound(103, 0, 100, 0)

    def lambda_ECC7():
        OP_95(0xFE, 0, 0, 119000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_ECC7)

    def lambda_ECE1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_ECE1)
    Sleep(800)
    Sound(104, 0, 100, 0)

    ChrTalk(
        0x101,
        "#3400914V#0011F#5POh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x160, 1)
    WaitChrThread(0x160, 2)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    Fade(500)
    OP_68(3300, 1000, 63700, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 8000, 0, 64500, 180)
    SetChrPos(0x102, 8000, 0, 64500, 180)
    SetChrPos(0x103, 8000, 0, 64500, 180)
    SetChrPos(0x104, 8000, 0, 64500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x160, 2700, 0, 62700, 270)
    OP_A7(0x160, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0x160, 3, 0, 31)
    OP_68(-700, 1000, 63700, 4000)
    OP_0D()
    Sleep(1000)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    BeginChrThread(0x101, 3, 0, 27)
    Sleep(450)
    BeginChrThread(0x102, 3, 0, 28)
    Sleep(450)
    BeginChrThread(0x103, 3, 0, 29)
    Sleep(450)
    BeginChrThread(0x104, 3, 0, 30)
    WaitChrThread(0x160, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3400915V#0008F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3400916V#12P#0108FAre we really doing the right thing? Shouldn't we\x01",
            "chase after her and...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EEDF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EEDF)
    Sleep(50)

    def lambda_EEEF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_EEEF)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3400917V#5P#0006FI know. It crossed my mind, too.\x02\x03",
            "#3400918V#0000FBut I don't think it's our call to make this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400919V#0305FWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400920V#0205F#11PIs that what your intuition is saying?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400921V#5P#0002FNo, it's nothing like that--\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x10, 2000, -1000, 69500, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x10, 0x8)
    Sleep(300)
    Sound(1704, 255, 95, 0)
    Sleep(300)

    NpcTalk(
        0x10,
        "???",
        "#3400922V#1P#2S#15A#40WExcuuuuse me...!\x02",
    )

    Sleep(2000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_F0C6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F0C6)

    def lambda_F0D3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F0D3)

    def lambda_F0E0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F0E0)

    def lambda_F0ED():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F0ED)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3400923V#0005F#6PThat voice...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400924V#12P#0105FI think it came from the first floor.\x02",
    )

    CloseMessageWindow()
    OP_68(-700, 500, 63700, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_68(1500, 2850, 10200, 0)
    MoveCamera(47, 21, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, 900, 3000, 14000, 180)
    SetChrPos(0x102, 2000, 3000, 14000, 180)
    SetChrPos(0x103, 900, 3500, 14500, 180)
    SetChrPos(0x104, 2000, 3500, 14500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 400, 0, 1700, 0)
    SetChrPos(0x11, 1500, 0, 1500, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    OP_68(1500, 1850, 10100, 3000)
    FadeToBright(1000, 0)

    def lambda_F271():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F271)

    def lambda_F282():
        OP_96(0xFE, 0x384, 0x352, 0x251C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F282)
    Sleep(150)

    def lambda_F29F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F29F)

    def lambda_F2B0():
        OP_96(0xFE, 0x7D0, 0x352, 0x251C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F2B0)
    Sleep(50)

    def lambda_F2CD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F2CD)

    def lambda_F2DE():
        OP_96(0xFE, 0x384, 0x352, 0x2A30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F2DE)
    Sleep(150)

    def lambda_F2FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F2FB)

    def lambda_F30C():
        OP_96(0xFE, 0x7D0, 0x352, 0x2A30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F30C)
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
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        "#3400925V#0102F#5PWell, I wasn't expecting you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400926V#5P#0000FEstelle? Joshua?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(400, 1100, 2900, 2000)
    MoveCamera(53, 19, 0, 2000)
    SetCameraDistance(25000, 2000)
    Sleep(1000)

    def lambda_F439():
        OP_96(0xFE, 0xC8, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F439)
    Sleep(200)

    def lambda_F456():
        OP_96(0xFE, 0x5DC, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F456)
    Sleep(80)

    def lambda_F473():
        OP_96(0xFE, 0xFFFFFF9C, 0x0, 0x13EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F473)
    Sleep(120)

    def lambda_F490():
        OP_96(0xFE, 0x4B0, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F490)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7520", 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x10,
        (
            "#3400927VHey there, guys.\x02\x03",
            "#3400928VSorry for barging in like this. We didn't\x01",
            "even bother to call ahead of time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x11,
        (
            "#3400929VI know this might be inconvenient, but\x01",
            "we have something urgent we need to\x01",
            "confirm with you.\x02\x03",
            "#3400930VCould you spare us a few minutes? It shouldn't\x01",
            "take long.\x02",
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
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#3400931V#0000F#5PSure. I don't see why not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400932V#5P#0305FWhat's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400933V#5P#0201FIs it related to the Schwarze Auction?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#3400934V#12P#0806FNo, actually. We had to put that on the\x01",
            "back burner for a bit, unfortunately.\x02\x03",
            "#3400935V#0801FTh-The thing is...\x02\x03",
            "#3400936V...I heard from an eyewitness that Lloyd\x01",
            "was walking with a certain someone this\x01",
            "afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400937V#0005F#5PA certain someone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3400938V#12P#0903FA young girl with purple hair.\x02\x03",
            "#3400939V#0901FOne that was probably wearing\x01",
            "a frilly white dress.\x02",
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
        "#3400940V#0011F#5PWait, so you're talking about...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400941V#5P#0101FRenne, right?\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x10,
        "#3400942V#12P#0813F#4S...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#3400943V#12P#0901FI knew it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400944V#0011F#5PW-Wait a minute.\x02\x03",
            "#3400945V#0001FYou two know her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3400946V#12P#0903FYeah... It's kind of a long story.\x02\x03",
            "#3400947V#0908FWe haven't seen her in months, but...\x02\x03",
            "#3400948V#0902F...I suppose it's true. She really is in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#3400949V#12P#0809F#40WHaha...ha... Ahhh...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(130)
    SetChrSubChip(0x10, 0x1)
    Sleep(130)
    SetChrSubChip(0x10, 0x2)
    Sleep(200)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x11, 0x10, 500)

    ChrTalk(
        0x11,
        "#3400950V#0901F#11PEstelle?! Are you okay?\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    SetChrSubChip(0x10, 0x3)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x10,
        (
            "#3400951V#12P#0806FI-I'm fine. I'm just so relieved that\x01",
            "my legs gave out from under me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(200)
    Fade(250)
    ClearChrFlags(0x10, 0x20)
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x10,
        (
            "#3400952V#12P#0804FAll right! Now's not the time to be\x01",
            "resting!\x02\x03",
            "#3400953V#0802FI'm hunting you down, missy, and you\x01",
            "can't stop me!\x02",
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
        0x104,
        (
            "#3400954V#5P#0302FWould you look at that. She's one popular\x01",
            "kiddo, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400955V#5P#0204FNot to mention her rivalry with Jona.\x01",
            "She really knows how to make an impact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400956V#0006F#5PWait a minute... You don't mean to say\x01",
            "that Renne is a bracer, do you?\x02\x03",
            "#3400957V#0001FI know she's talented, but she's too young\x01",
            "to be doing something so dangerous.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0x0, 0x1F4)

    ChrTalk(
        0x11,
        "#3400958V#12P#0904FNo, she's not a bracer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#3400959V#12P#0804FShe's someone special to us.\x02\x03",
            "#3400960V#0800FFor the last six months, we've been chasing\x01",
            "her everywhere, hoping to catch her and\x01",
            "finally...well...\x02\x03",
            "#3400961V...become a family.\x02",
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
        "#3400962V#0005F#5PA family?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3400963V#5P#0101FI can't even begin to imagine how all of this\x01",
            "started...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#3400964V#12P#0806FOh, yeeeaahh... It's been a pretty\x01",
            "complicated story.\x02\x03",
            "#3400965V#0808F#30WAnd since coming to Crossbell, we've finally had\x01",
            "the chance to learn the full version ourselves...\x02\x03",
            "#3400966V#40W...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 500)

    ChrTalk(
        0x11,
        (
            "#3400967V#0906F#11PHey, now. It's not like you to get so discouraged.\x02\x03",
            "#3400968V#0900FWeren't you the one going on about how the\x01",
            "Hayworths' story was going to be crucial in\x01",
            "getting Renne to open up to us?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 500)

    ChrTalk(
        0x10,
        "#3400969V#6P#0800FY-Yes... That's right! It definitely will!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3400970V#0001F#5PThe Hayworths... You mean Harold and\x01",
            "Sophia Hayworth?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_10334():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_10334)

    def lambda_10341():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_10341)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x10,
        (
            "#3400971V#12P#0813FWH-WHAT?!\x02\x03",
            "#3400972VHow do you guys know those names?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400973V#0012F#5PI was about to ask you the same.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3400974V#5P#0106FLloyd, it might help to fill them in on everything\x01",
            "that happened today.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    Sleep(1000)
    OP_68(5500, 950, 4200, 0)
    MoveCamera(49, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22500, 0)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x1)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0xE)
    BeginChrThread(0x10, 3, 0, 25)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x11, 0x2)
    ClearChrFlags(0x11, 0x1)
    SetChrChipByIndex(0x11, 0x25)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x101, 5000, 130, 2200, 0)
    SetChrPos(0x102, 6000, 130, 2200, 0)
    SetChrPos(0x103, 3300, 0, 2500, 45)
    SetChrPos(0x104, 7000, 0, 3500, 315)
    SetChrPos(0x10, 5000, 130, 6250, 180)
    SetChrPos(0x11, 5800, 130, 6250, 180)
    SetCameraDistance(23000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    MoveCamera(37, 17, 0, 50000)

    ChrTalk(
        0x101,
        (
            "#3400975V#12P#0003F...And so, you just missed her. The two of you\x01",
            "showed up right after she had left.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3400976V#12P#0011FE-Estelle?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#3400977V#5P#0808F#60WI-I'm fine...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 0x1)
    EndChrThread(0x10, 0x3)
    SetChrSubChip(0x10, 0xE)
    Sleep(100)
    SetChrSubChip(0x10, 0x5)
    Sleep(100)
    SetChrSubChip(0x10, 0x6)
    Sleep(100)
    BeginChrThread(0x10, 3, 0, 26)
    Sleep(300)

    ChrTalk(
        0x10,
        (
            "#3400978V#5P#0811F#50WIt's just...\x02\x03",
            "#3400979V#0810F#60W*sob*\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    EndChrThread(0x10, 0x3)
    SetChrSubChip(0x10, 0xB)
    OP_0D()
    Sleep(500)

    def lambda_106B1():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_106B1)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x10,
        "#3400980V#0810F#5PAAAAAAAH!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x11, 0x2)
    Sleep(150)
    SetChrSubChip(0x11, 0x3)
    Sleep(150)
    SetChrSubChip(0x11, 0x4)
    Sound(820, 0, 100, 0)
    Sleep(150)
    SetChrSubChip(0x11, 0x5)
    Sleep(500)

    ChrTalk(
        0x11,
        "#3400981V#11P#0910F#40WIt's okay, Estelle...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x10,
        (
            "#3400982V#5P#0810F#40WY-Yeah. Sorry, Joshua. And you guys,\x01",
            "for causing such a scene...\x02\x03",
            "#3400983V#40WI...I just don't know where to begin.\x02\x03",
            "#3400984V#0808F#40WShould I tell her that she wasn't abandoned...?\x01",
            "That she was loved?\x02\x03",
            "#3400985V#40WOr that she can finally accept the\x01",
            "bittersweet truth facing her?\x02\x03",
            "#3400986V#0810F#40W*sniff* *sniff*\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x102,
        "#3400987V#12P#0108FA bittersweet truth...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400988V#12P#0008FSo, you knew the Hayworths' story, too...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)

    ChrTalk(
        0x11,
        (
            "#3400989V#5P#0908FYes, and the sorrow, grief, and misunderstandings\x01",
            "that comprise it.\x02\x03",
            "#3400990VAs a result, Renne has been walking a cruel path\x01",
            "of self-deception.\x02\x03",
            "#3400991V#0903FBy trying to replace her parents with Pater-Mater, she\x01",
            "abandoned all hope of ever uncovering the truth.\x02\x03",
            "#3400992VBut...maybe that's understandable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3400993V#0306FIt's not uncommon for kiddos to protect themselves\x01",
            "with psychological defenses like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400994V#6P#0208FYes, however, she cannot move forward by\x01",
            "relying on those.\x02\x03",
            "#3400995V#0206FAnd she cannot return to her past, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3400996V#5P#0908FRight.\x02\x03",
            "#3400997V#0903FAnd that's why we resolved to help Renne\x01",
            "find the courage to face the truth of her past.\x02\x03",
            "#3400998VThe truth may be sorrowful, but you can feel the\x01",
            "love buried deep within it--the warmth it carries.\x02\x03",
            "#3400999VBecause of that, we believed she could overcome it.\x02\x03",
            "#3401000V#0902FBut, in the end, it looks like we don't need to tell her\x01",
            "that ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3401001V#12P#0004FYeah.\x02\x03",
            "#3401002V#0000FIt seemed like she came to terms with it on her own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#3401003V#5P#0911FI'm glad...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrSubChip(0x11, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#3401004V#0903F#5PThank you, Lloyd. Special Support Section.\x02\x03",
            "#3401005VI don't know how we can repay you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3401006V#12P#0004FPlease, don't worry about it.\x02\x03",
            "#3401007V#0002FRenne helped us with a case, so it was the\x01",
            "least we could do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3401008V#12P#0104FThat's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#3401009V#5P#0810F*sniff*\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0x10, 0x14)
    OP_0D()
    SetChrSubChip(0x10, 0x15)
    Sleep(100)
    SetChrSubChip(0x10, 0x16)
    Sleep(200)
    SetChrSubChip(0x10, 0x15)
    Sleep(100)
    SetChrSubChip(0x10, 0xC)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x10,
        "#3401010V#5P#0800F#4SThen it's decided!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x11, 0x1)
    Fade(250)
    SetChrSubChip(0x10, 0xD)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x10,
        (
            "#3401011V#5P#0802FSince our biggest obstacle is gone now,\x01",
            "I won't be holding back anymore!\x02\x03",
            "#3401012V#0809FYou better watch out, Renne!\x02\x03",
            "#3401013VWith that outta the way, I'm going to catch you\x01",
            "and make you part of the Bright family for sure!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3401014V#12P#0009FHaha. There she is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3401015V#0309F#12PWeeell, let her figure out the details for\x01",
            "herself. If anyone can rein that girl in,\x01",
            "it's Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3401016V#6P#0202FIndeed. Her optimism is blinding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3401017V#11P#0904FThat's one of her strong points, trust me.\x02\x03",
            "#3401018V#0902FThere's nothing more terrifying than a wild\x01",
            "Estelle caught up in the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#3401019V#5P#0804FAnd don't you forget it, buster! Guys, leave\x01",
            "Renne to us!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x10, 0x4)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#3401020V#5P#0800FLloyd, Elie... Tio and Randy.\x02\x03",
            "#3401021VI'm not usually one for big formalities\x01",
            "or anything, but...\x02\x03",
            "#3401022V#0804FLet me just say...thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle bowed her head.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#3401023V#12P#0002FE-Estelle, it's fine...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3401024V#12P#0102FHe's right, Estelle.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x11, 0x0)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#3401025V#5P#0904FListen, guys. If you ever need a hand with\x01",
            "anything, don't hesitate to call us up.\x02\x03",
            "#3401026V#0902FIt doesn't matter that you're police and we're\x01",
            "bracers. It's not a rivalry worth keeping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#3401027V#5P#0809FHear, hear! If you ever need us, you can bet\x01",
            "your sweet bippies we'll come running!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3401028V#12P#0004FI'll keep that in mind.\x02\x03",
            "#3401029V#0000FIf the going gets rough, I know exactly who\x01",
            "we're calling first.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(800)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd, Estelle, and the others went over\x01",
            "to Long Lao Tavern & Inn on East Street and bonded\x01",
            "over dinner.\x02\x03",
            "The truth and finer points behind the incident that\x01",
            "happened in the Liberl Kingdom were discussed...\x02\x03",
            "...and the SSS learned of the enigmatic organization\x01",
            "known as 'the society' that Renne is affiliated with.\x02\x03",
            "All in all, the group shared a variety of stories and\x01",
            "secrets well into the night, bringing the fourth day\x01",
            "of the Anniversary Festival to a close.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(2000)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    RemoveParty(0x5F, 0x0)
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
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    SubItemNumber(0x327, 1)
    SubItemNumber(0x328, 1)
    Call(0, 11)
    Return()

    # Function_24_E392 end

    def Function_25_118BF(): pass

    label("Function_25_118BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_118D8")
    OP_A1(0xFE, 0x3E8, 0x3, 0xE, 0xF, 0x10)
    Jump("Function_25_118BF")

    label("loc_118D8")

    Return()

    # Function_25_118BF end

    def Function_26_118D9(): pass

    label("Function_26_118D9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_118F3")
    OP_A1(0xFE, 0x3E8, 0x4, 0x6, 0x7, 0x8, 0x9)
    Jump("Function_26_118D9")

    label("loc_118F3")

    Return()

    # Function_26_118D9 end

    def Function_27_118F4(): pass

    label("Function_27_118F4")


    def lambda_118F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_118F9)

    def lambda_1190A():
        OP_95(0xFE, 8000, 0, 62700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1190A)
    WaitChrThread(0x101, 1)

    def lambda_11928():
        OP_95(0xFE, 700, 0, 62700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11928)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x13B, 0x1F4)
    Return()

    # Function_27_118F4 end

    def Function_28_11949(): pass

    label("Function_28_11949")


    def lambda_1194E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1194E)

    def lambda_1195F():
        OP_95(0xFE, 8000, 0, 62700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1195F)
    WaitChrThread(0x102, 1)

    def lambda_1197D():
        OP_95(0xFE, 700, 0, 61500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1197D)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x13B, 0x1F4)
    Return()

    # Function_28_11949 end

    def Function_29_1199E(): pass

    label("Function_29_1199E")


    def lambda_119A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_119A3)

    def lambda_119B4():
        OP_95(0xFE, 8000, 0, 62700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_119B4)
    WaitChrThread(0x103, 1)

    def lambda_119D2():
        OP_95(0xFE, 2000, 0, 62700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_119D2)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x13B, 0x1F4)
    Return()

    # Function_29_1199E end

    def Function_30_119F3(): pass

    label("Function_30_119F3")


    def lambda_119F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_119F8)

    def lambda_11A09():
        OP_95(0xFE, 8000, 0, 62700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11A09)
    WaitChrThread(0x104, 1)

    def lambda_11A27():
        OP_95(0xFE, 2000, 0, 61500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11A27)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x13B, 0x1F4)
    Return()

    # Function_30_119F3 end

    def Function_31_11A48(): pass

    label("Function_31_11A48")


    def lambda_11A4D():
        OP_95(0xFE, -700, 0, 62700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_11A4D)
    WaitChrThread(0x160, 1)

    def lambda_11A6B():
        OP_95(0xFE, -2200, 0, 67900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_11A6B)
    WaitChrThread(0x160, 1)

    def lambda_11A89():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_11A89)
    Sound(103, 0, 100, 0)

    def lambda_11AA0():
        OP_95(0xFE, -5000, 0, 67900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_11AA0)
    WaitChrThread(0x160, 1)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x160, 2)
    Return()

    # Function_31_11A48 end

    def Function_32_11AC4(): pass

    label("Function_32_11AC4")

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
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01000.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis156.itp")
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KCrossbell Anniversary Festival, Second Day\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7110", 0)
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x8,
        (
            "#3200001VAll right, everyone. Hope you savored that\x01",
            "free day of yours.\x02\x03",
            "#3200002VYou've got a long four days ahead of you.\x01",
            "You kids had better last until the closing\x01",
            "day of the Anniversary Festival.\x02\x03",
            "#3200003VTrust me. I intend to throw whatever work\x01",
            "I can find at you. Better fasten your seatbelts.\x02",
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
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#3200004V#12P#0006F*sigh* Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200005V#0306FSo we only get one day off durin'\x01",
            "the whole festival.\x02\x03",
            "#3200006V#0301FDamn, ain't that a bit stingy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3200007V#0106FWell, I imagine the entire police force has\x01",
            "their hands full.\x02\x03",
            "#3200008V#0100FOfficers on security and patrol duty couldn't\x01",
            "have had it easy on that first day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3200009V#5P#1004FYeah, but what can you do about it?\x02\x03",
            "#3200010V#1002FBe grateful. That day off was your reward for\x01",
            "preventing the mayor's assassination, y'know.\x02\x03",
            "#3200011VAnd hey, seems like the department's gonna\x01",
            "spare you guys the more menial tasks during\x01",
            "the festival, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200012V#12P#0006FThat doesn't mean we aren't going to be\x01",
            "loaded with support requests.\x02\x03",
            "#3200013V#0000FFrom what I've seen, it seems like there's\x01",
            "more tourists in town than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3200014V#5P#1002FHope you all are ready, 'cause it's time to go\x01",
            "out and build up your rep. Work hard and\x01",
            "maybe you'll be as popular as the bracers.\x02\x03",
            "#3200015VEither way, just keep your nose to the grindstone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3200016V#12P#0002FYou've got a point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200017V#0306FI can't shake the feeling that you're\x01",
            "trickin' us with this mediocre pep talk...\x02\x03",
            "#3200018V#0308FMan, I just wanted to kick back over\x01",
            "at Mishelam with all of my lovely\x01",
            "nurse friends...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#3200019V#6P#0205FMishelam... That is home to the theme\x01",
            "park you can get to with one of the\x01",
            "Harbor District's cruise ships, right?\x02\x03",
            "#3200020V#0202FI've heard that Mishy works there\x01",
            "as the park's mascot...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12432():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12432)
    Sleep(50)
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#3200021V#5P#0005FMishy...? Oh, isn't he that gray cat?\x02\x03",
            "#3200022V#0000FI've heard of him before, but this theme park\x01",
            "wasn't a thing a few years ago, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3200023V#5P#0104FWell, Mishelam has operated as a wellness\x01",
            "resort for a long time now.\x02\x03",
            "#3200024V#0102FI think the theme park, on the other hand,\x01",
            "was built around two years ago...\x02\x03",
            "#3200025VIt's been extremely popular ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200026V#0309FOh, yeah, it is! I went there once, and it\x01",
            "honestly blew me away.\x02\x03",
            "#3200027V#0302FI bet that place is swamped with visitors\x01",
            "during the Anniversary Festival. Can't\x01",
            "say I envy the folks working there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3200028V#6P#0204FInteresting. Very interesting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3200029V#5P#1003F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_12751():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12751)
    Sleep(50)

    def lambda_12761():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12761)
    Sleep(50)
    OP_93(0x103, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#3200030V#12P#0005FChief?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3200031V#5P#1005FHmm...\x02\x03",
            "#3200032V#1003FAnyway, just focus on your support requests\x01",
            "for the next four days, got it?\x02\x03",
            "#3200033V#1002FAs usual, it's up to you how much you want\x01",
            "to get done.\x02\x03",
            "#3200034VYou'll get a fresh batch each day, so you\x01",
            "better get to it.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_57(0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_E3(0xB)
    OP_68(18000, 1850, 3500, 0)
    MoveCamera(37, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 19000, 850, 3500, 270)
    SetChrPos(0x102, 19000, 850, 3500, 270)
    SetChrPos(0x103, 19000, 850, 3500, 270)
    SetChrPos(0x104, 19000, 850, 3500, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayBGM("ed7106", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)
    OP_68(16000, 1850, 3500, 2000)

    def lambda_129CB():
        OP_96(0xFE, 0x3E80, 0x352, 0xB54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_129CB)

    def lambda_129E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_129E5)
    Sleep(250)

    def lambda_129F9():
        OP_96(0xFE, 0x3E80, 0x352, 0x1068, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_129F9)

    def lambda_12A13():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12A13)
    Sleep(400)

    def lambda_12A27():
        OP_96(0xFE, 0x4394, 0x352, 0xB54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12A27)

    def lambda_12A41():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_12A41)
    Sleep(250)

    def lambda_12A55():
        OP_96(0xFE, 0x4394, 0x0, 0x1068, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12A55)

    def lambda_12A6F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12A6F)
    WaitChrThread(0x101, 1)

    def lambda_12A84():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12A84)
    WaitChrThread(0x102, 1)

    def lambda_12A95():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12A95)
    WaitChrThread(0x103, 1)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)

    def lambda_12ABB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_12ABB)
    WaitChrThread(0x104, 1)

    def lambda_12ACC():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12ACC)
    WaitChrThread(0x104, 2)
    SetMapObjFlags(0x0, 0x10)
    OP_6F(0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3200035V#6P#0004F#6POkay, guys. Let's check what support requests\x01",
            "we have for the day.\x02\x03",
            "#3200036V#0000FJudging by the amount of tourists in Crossbell,\x01",
            "we might even have to work outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3200037V#0103F#5PYes, I wouldn't be surprised.\x02\x03",
            "#3200038V#0100FRecently, I've heard that tourists are sightseeing\x01",
            "at out-of-the-way places, like Armorica Village.\x02\x03",
            "#3200039VIn addition to the train station and airport,\x01",
            "a lot of tourists seem to be traveling by road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200040V#5P#0305FPhew, I bet Bellguard and Tangram\x01",
            "have their work cut out for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3200041V#0203FThe Anniversary Festival will not be easy for\x01",
            "Noel and the others, either.\x02\x03",
            "#3200042V#0200FThe Bracer Guild must be quite occupied, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3200043V#6P#0001FRight. We can't be outdone by them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3200044V#0104F#5PIf we push ourselves too hard,\x01",
            "I doubt our stamina will last long.\x02\x03",
            "#3200045V#0102FWouldn't it be wise to decide what\x01",
            "to do after evaluating the urgency\x01",
            "of each request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3200046V#6P#0000FThat's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3200047V#5P#0300FSlow and steady wins the race!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_68(16600, 1850, 3500, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 16600, 850, 3500, 0)
    SetChrPos(0x1, 16600, 850, 3500, 0)
    SetChrPos(0x2, 16600, 850, 3500, 0)
    SetChrPos(0x3, 16600, 850, 3500, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetScenarioFlags(0xA0, 0)
    OP_29(0x43, 0x1, 0xE)
    OP_29(0x44, 0x4, 0x2)
    OP_29(0x44, 0x1, 0x0)
    ModifyEventFlags(1, 0, 0x80)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_32_11AC4 end

    def Function_33_12FC9(): pass

    label("Function_33_12FC9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12FE3")
    OP_A1(0x103, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_33_12FC9")

    label("loc_12FE3")

    Return()

    # Function_33_12FC9 end

    def Function_34_12FE4(): pass

    label("Function_34_12FE4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12FFE")
    OP_A1(0x103, 0xBB8, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_34_12FE4")

    label("loc_12FFE")

    Return()

    # Function_34_12FE4 end

    def Function_35_12FFF(): pass

    label("Function_35_12FFF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13033")
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    Sleep(300)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(300)
    Jump("Function_35_12FFF")

    label("loc_13033")

    Return()

    # Function_35_12FFF end

    def Function_36_13034(): pass

    label("Function_36_13034")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis068.itp")
    CreatePortrait(1, 289, 127, 353, 191, 0, 0, 64, 64, 0, 0, 64, 64, 0xFFFFFF, 0x1, "c_vis069.itp")
    LoadEffect(0x0, "event\\ev398_00.eff")
    OP_68(190000, 10000, 111000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(1000, 0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 206000, 50, 127000, 180)
    LoadChrToIndex("chr/ch02707.itc", 0x1F)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x0)
    SetChrPos(0x12, 206000, 0, 127100, 180)
    BeginChrThread(0x12, 0, 0, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x12, 0x8000)
    LoadChrToIndex("apl/ch50302.itc", 0x1E)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x2)
    ClearMapObjFlags(0xB, 0x4)
    OP_78(0xB, 0x1F)
    SetChrPos(0x1F, 206000, 500, 126300, 0)
    OP_D3(0x1F, 0x0, 0x2BF20, 0x0, 0x0)
    OP_E5()
    FadeToBright(2000, 0)
    BeginChrThread(0x103, 0, 0, 33)
    BeginChrThread(0x20, 1, 0, 37)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_68(190000, 10000, 108000, 1000)
    OP_64(0x103)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    Sleep(1000)
    BeginChrThread(0x103, 2, 0, 35)
    Sleep(3000)
    EndChrThread(0x103, 0x2)
    OP_C9(0x1, 0x3, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFF000000, 0x1F4, 0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    VolumeBGM(0x3C, 0x1F4)
    FadeToBright(0, 0)
    PlayMovie(0x0, "ed7_ev06.pmf", 0x68, 0x1)
    Sound(725, 0, 100, 0)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(0, -1)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x20, 0x1)
    OP_6E(280, 3000)
    OP_A1(0x103, 0x5DC, 0x4, 0x0, 0x3, 0x4, 0x5)
    OP_A1(0x103, 0x5DC, 0x4, 0x5, 0x6, 0x7, 0x6)
    OP_A1(0x103, 0x5DC, 0x4, 0x5, 0x4, 0x3, 0x0)
    BeginChrThread(0x103, 2, 0, 35)
    PlayEffect(0x0, 0x0, 0x103, 0x0, 0, 136000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1199, 255, 100, 0)
    Sound(506, 0, 100, 0)
    Sound(565, 0, 100, 0)
    Sleep(2000)
    BeginChrThread(0x103, 0, 0, 34)
    BeginChrThread(0x20, 1, 0, 38)
    Sleep(1500)
    EndChrThread(0x103, 0x2)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFF000000, 0x1F4, 0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_68(190000, 10000, 111000, 0)
    OP_6E(350, 0)
    StopEffect(0x0, 0x0)
    VolumeBGM(0x3C, 0x1F4)
    FadeToBright(0, 0)
    PlayMovie(0x0, "ed7_ev07.pmf", 0x68, 0x1)
    Sound(726, 0, 100, 0)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(0, -1)
    FadeToDark(0, 0, -1)
    OP_0D()
    FadeToBright(500, 0)
    OP_0D()
    Sound(1282, 255, 90, 0)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x103, 0xFF)
    OP_A1(0x103, 0x3E8, 0x4, 0x0, 0x3, 0x4, 0x5)
    OP_63(0x103, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(2000)
    OP_6E(360, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x103, 0x4)
    OP_CA(0x1, 0xFF, 0x0)
    OP_E6()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0570", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_13034 end

    def Function_37_1341A(): pass

    label("Function_37_1341A")

    Sound(849, 0, 100, 0)
    Sleep(900)
    Sound(850, 0, 100, 0)
    Sleep(1800)
    Sound(849, 0, 100, 0)
    Sleep(900)
    Sound(850, 0, 100, 0)
    Sleep(1800)
    Sound(849, 0, 100, 0)
    Return()

    # Function_37_1341A end

    def Function_38_13445(): pass

    label("Function_38_13445")

    Sound(849, 0, 100, 0)
    Sleep(200)
    Sound(850, 0, 100, 0)
    Sleep(700)
    Sound(849, 0, 100, 0)
    Return()

    # Function_38_13445 end

    def Function_39_1345E(): pass

    label("Function_39_1345E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(1000, 900, 1900, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 400, 0, 1900, 0)
    SetChrPos(0x102, 1600, 0, 1900, 0)
    SetChrPos(0x103, 400, 0, 700, 0)
    SetChrPos(0x104, 1600, 0, 700, 0)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_13546():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_13546)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)
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
    Sound(1084, 255, 90, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3400126V#0000FYes, Lloyd Bannings here.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2083, 255, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400127V\x07\x05",
            "I'm sorry, I know you're busy.\x01",
            "Can I bother you for a minute?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400128V\x07\x00",
            "#0000FSure, we were just wrapping\x01",
            "up our break, so it's no\x01",
            "bother at all.\x02\x03",
            "#3400129VIs it something urgent?\x02",
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
            "#3400130V\x07\x05",
            "Yes, there's a man who's personally\x01",
            "requesting the aid of the SSS.\x02\x03",
            "#3400131VHe's a trader by the name\x01",
            "of Harold Hayworth.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400132V\x07\x00",
            "#0005FOh, he's an acquaintance of ours...\x01",
            "What happened?\x02",
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
            "#3400133V\x07\x05",
            "Ah, you see...\x02\x03",
            "#3400134VWhile he was watching the parade,\x01",
            "his little boy wandered off.\x02",
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
            "#3400135V\x07\x00",
            "#0003FReally? Thanks for the heads-up.\x02\x03",
            "#3400136V#0001FWhere can we find Mr. Hayworth?\x02",
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
            "#3400137V\x07\x05",
            "He's currently located at one of the\x01",
            "benches near headquarters.\x01",
            "I think it was by the water fountain?\x02\x03",
            "#3400138VAccording to him, that was where\x01",
            "he first lost sight of his son.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400139V\x07\x00",
            "#0000FRoger, we're heading there now.\x02",
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
            "#3400140V\x07\x05",
            "Yes, thank you.\x02",
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
            "#3400141V\x07\x00",
            "#11P#0105FWhat's the matter, Lloyd?\x02",
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
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#3400142V#6P#0003FWe've got a request\x01",
            "from Mr. Hayworth.\x02\x03",
            "#3400143V#0001FApparently, his son went missing\x01",
            "at some point during the parade.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#3400144V#11P#0101FThat's horrible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400145V#12P#0206FToday's crowd is as large as I have seen it.\x01",
            "This is a serious issue...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3400146V#0300F#11PStill, it's a standard missin' person case,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#3400147V#5P#0004FYeah, basically.\x02\x03",
            "#3400148V#0000FHe's waiting for us by the water fountain\x01",
            "near headquarters. We should go get\x01",
            "details about the situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, 1000, 0, 1900, 0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA1, 5)
    OP_29(0x44, 0x1, 0x7)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_39_1345E end

    def Function_40_13D61(): pass

    label("Function_40_13D61")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(1300, 1950, 9900, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 1900, 850, 9900, 180)
    SetChrPos(0x102, 700, 850, 9900, 180)
    SetChrPos(0x103, 700, 850, 11100, 180)
    SetChrPos(0x104, 1900, 850, 11100, 180)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(806, 2, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_13E46():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_13E46)
    Sleep(50)
    TurnDirection(0x103, 0x101, 500)
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
    Sound(1084, 255, 90, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3400126V#0000FYes, Lloyd Bannings here.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2083, 255, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400127V\x07\x05",
            "I'm sorry, I know you're busy.\x01",
            "Can I bother you for a minute?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400128V\x07\x00",
            "#0000FSure, we were just wrapping\x01",
            "up our break, so it's no\x01",
            "bother at all.\x02\x03",
            "#3400129VIs it something urgent?\x02",
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
            "#3400130V\x07\x05",
            "Yes, there's a man who's personally\x01",
            "requesting the aid of the SSS.\x02\x03",
            "#3400131VHe's a merchant by the\x01",
            "name of Harold Hayworth.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400132V\x07\x00",
            "#0005FOh, he's an acquaintance of ours...\x01",
            "What happened?\x02",
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
            "#3400133V\x07\x05",
            "Ah, you see...\x02\x03",
            "#3400134VWhile he was watching the parade,\x01",
            "his young son wandered off.\x02",
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
            "#3400135V\x07\x00",
            "#0003FReally? Thanks for the heads-up.\x02\x03",
            "#3400136V#0001FWhere can we find Mr. Hayworth?\x02",
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
            "#3400137V\x07\x05",
            "He's currently located at one of the\x01",
            "benches near headquarters.\x01",
            "I think it was by the water fountain?\x02\x03",
            "#3400138VAccording to him, that was where\x01",
            "he first lost sight of his son.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400139V\x07\x00",
            "#0000FRoger, we're heading there now.\x02",
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
            "#3400140V\x07\x05",
            "Yes, thank you.\x02",
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
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#3400141V\x07\x00",
            "#6P#0105FWhat's the matter, Lloyd?\x02",
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
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#3400142V#11P#0003FWe've got a request\x01",
            "from Mr. Hayworth.\x02\x03",
            "#3400143V#0001FApparently, his son went missing\x01",
            "at some point during the parade.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#3400144V#6P#0101FThat's horrible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3400145V#5P#0206FToday's crowd is as large as I've\x01",
            "seen it. This is a serious issue...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3400146V#0300F#5PStill, it's a standard missin'\x01",
            "person case, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#3400147V#12P#0004FYeah, basically.\x02\x03",
            "#3400148V#0000FHe's waiting for us by the water fountain\x01",
            "near headquarters. We should\x01",
            "go get details about the situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, 1300, 850, 9900, 180)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA1, 5)
    OP_29(0x44, 0x1, 0x7)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_40_13D61 end

    def Function_41_1465E(): pass

    label("Function_41_1465E")

    EventBegin(0x0)
    Fade(500)
    OP_68(15760, 1850, 10150, 0)
    MoveCamera(79, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 15760, 850, 10150, 45)
    SetChrPos(0x102, 16560, 850, 9350, 45)
    SetChrPos(0x103, 14830, 850, 9220, 45)
    SetChrPos(0x104, 15630, 850, 8410, 45)
    OP_0D()

    ChrTalk(
        0x101,
        "#0005FWe have a request from the Second Division.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FExposing the counterfeit dealers...\x01",
            "What exactly does that entail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0302FThat aside, ain't this the first time\x01",
            "the department has sent us an\x01",
            "important-lookin' mission?\x02\x03",
            "#0304FHaha, maybe they've finally come\x01",
            "to appreciate our hard work, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F#12PWell...it is not an impossibility.\x02\x03",
            "#0211FI'm more inclined to believe this is an\x01",
            "odd job that they pushed onto us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWell, it doesn't matter now. Let's go hear\x01",
            "the details from Inspector Donovan.\x02\x03",
            "If everything goes well, maybe the other\x01",
            "divisions will start to warm up to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FHopefully... Okay, we should head to\x01",
            "headquarters when we're ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_41_1465E end

    def Function_42_14996(): pass

    label("Function_42_14996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_149C7")
    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)

    label("loc_149C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_149F8")
    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)

    label("loc_149F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14A29")
    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)

    label("loc_14A29")

    Return()

    # Function_42_14996 end

    def Function_43_14A2A(): pass

    label("Function_43_14A2A")


    ChrTalk(
        0x101,
        (
            "#0000FShouldn't we check our support\x01",
            "requests before heading outside?\x02\x03",
            "There might be an urgent request\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_43_14A2A end

    def Function_44_14AA0(): pass

    label("Function_44_14AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BD7")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B5E")

    ChrTalk(
        0x103,
        (
            "#0200FRemember, Jona may contact us.\x02\x03",
            "We should not stray too far.\x02",
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
    Jump("loc_14BC1")

    label("loc_14B5E")


    ChrTalk(
        0x103,
        (
            "#0200FJona may still contact us.\x02\x03",
            "We should travel to the Geofront\x01",
            "after preparing ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14BC1")

    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)

    label("loc_14BD7")

    Return()

    # Function_44_14AA0 end

    def Function_45_14BD8(): pass

    label("Function_45_14BD8")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
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
    TalkEnd(0xFF)
    Return()

    # Function_45_14BD8 end

    def Function_46_14BFE(): pass

    label("Function_46_14BFE")

    Return()

    # Function_46_14BFE end

    def Function_47_14BFF(): pass

    label("Function_47_14BFF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    OP_68(-1560, 1330, 122920, 0)
    MoveCamera(38, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C57")
    SetChrFlags(0x0, 0x8)

    label("loc_14C57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C6A")
    SetChrFlags(0x1, 0x8)

    label("loc_14C6A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C7D")
    SetChrFlags(0x2, 0x8)

    label("loc_14C7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C90")
    SetChrFlags(0x3, 0x8)

    label("loc_14C90")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14CA3")
    SetChrFlags(0x4, 0x8)

    label("loc_14CA3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14CB6")
    SetChrFlags(0x5, 0x8)

    label("loc_14CB6")

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
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D5D")
    ClearChrFlags(0x0, 0x8)

    label("loc_14D5D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D70")
    ClearChrFlags(0x1, 0x8)

    label("loc_14D70")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D83")
    ClearChrFlags(0x2, 0x8)

    label("loc_14D83")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D96")
    ClearChrFlags(0x3, 0x8)

    label("loc_14D96")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14DA9")
    ClearChrFlags(0x4, 0x8)

    label("loc_14DA9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14DBC")
    ClearChrFlags(0x5, 0x8)

    label("loc_14DBC")

    Call(0, 64)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_47_14BFF end

    def Function_48_14DD3(): pass

    label("Function_48_14DD3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)
    OP_68(-2440, 1300, 129810, 0)
    MoveCamera(36, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(20500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E2B")
    SetChrFlags(0x0, 0x8)

    label("loc_14E2B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E3E")
    SetChrFlags(0x1, 0x8)

    label("loc_14E3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E51")
    SetChrFlags(0x2, 0x8)

    label("loc_14E51")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E64")
    SetChrFlags(0x3, 0x8)

    label("loc_14E64")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E77")
    SetChrFlags(0x4, 0x8)

    label("loc_14E77")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E8A")
    SetChrFlags(0x5, 0x8)

    label("loc_14E8A")

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
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14F31")
    ClearChrFlags(0x0, 0x8)

    label("loc_14F31")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14F44")
    ClearChrFlags(0x1, 0x8)

    label("loc_14F44")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14F57")
    ClearChrFlags(0x2, 0x8)

    label("loc_14F57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14F6A")
    ClearChrFlags(0x3, 0x8)

    label("loc_14F6A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14F7D")
    ClearChrFlags(0x4, 0x8)

    label("loc_14F7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14F90")
    ClearChrFlags(0x5, 0x8)

    label("loc_14F90")

    Call(0, 64)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_48_14DD3 end

    def Function_49_14FA7(): pass

    label("Function_49_14FA7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "05", 0x1, 0x1)
    OP_68(153830, 1330, 130810, 0)
    MoveCamera(29, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14FFF")
    SetChrFlags(0x0, 0x8)

    label("loc_14FFF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15012")
    SetChrFlags(0x1, 0x8)

    label("loc_15012")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15025")
    SetChrFlags(0x2, 0x8)

    label("loc_15025")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15038")
    SetChrFlags(0x3, 0x8)

    label("loc_15038")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1504B")
    SetChrFlags(0x4, 0x8)

    label("loc_1504B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1505E")
    SetChrFlags(0x5, 0x8)

    label("loc_1505E")

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
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1510B")
    ClearChrFlags(0x0, 0x8)

    label("loc_1510B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1511E")
    ClearChrFlags(0x1, 0x8)

    label("loc_1511E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15131")
    ClearChrFlags(0x2, 0x8)

    label("loc_15131")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15144")
    ClearChrFlags(0x3, 0x8)

    label("loc_15144")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15157")
    ClearChrFlags(0x4, 0x8)

    label("loc_15157")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1516A")
    ClearChrFlags(0x5, 0x8)

    label("loc_1516A")

    Call(0, 64)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_49_14FA7 end

    def Function_50_15181(): pass

    label("Function_50_15181")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x1, 0x1)
    OP_68(154150, 1330, 121920, 0)
    MoveCamera(53, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_151E4")
    SetChrFlags(0x0, 0x8)

    label("loc_151E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_151F7")
    SetChrFlags(0x1, 0x8)

    label("loc_151F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1520A")
    SetChrFlags(0x2, 0x8)

    label("loc_1520A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1521D")
    SetChrFlags(0x3, 0x8)

    label("loc_1521D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15230")
    SetChrFlags(0x4, 0x8)

    label("loc_15230")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15243")
    SetChrFlags(0x5, 0x8)

    label("loc_15243")

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
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_152F0")
    ClearChrFlags(0x0, 0x8)

    label("loc_152F0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15303")
    ClearChrFlags(0x1, 0x8)

    label("loc_15303")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15316")
    ClearChrFlags(0x2, 0x8)

    label("loc_15316")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15329")
    ClearChrFlags(0x3, 0x8)

    label("loc_15329")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1533C")
    ClearChrFlags(0x4, 0x8)

    label("loc_1533C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1534F")
    ClearChrFlags(0x5, 0x8)

    label("loc_1534F")

    Call(0, 64)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_50_15181 end

    def Function_51_15366(): pass

    label("Function_51_15366")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "07", 0x1, 0x1)
    OP_68(208030, 1330, 127590, 0)
    MoveCamera(25, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153BE")
    SetChrFlags(0x0, 0x8)

    label("loc_153BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153D1")
    SetChrFlags(0x1, 0x8)

    label("loc_153D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153E4")
    SetChrFlags(0x2, 0x8)

    label("loc_153E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153F7")
    SetChrFlags(0x3, 0x8)

    label("loc_153F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1540A")
    SetChrFlags(0x4, 0x8)

    label("loc_1540A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1541D")
    SetChrFlags(0x5, 0x8)

    label("loc_1541D")

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
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154BF")
    ClearChrFlags(0x0, 0x8)

    label("loc_154BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154D2")
    ClearChrFlags(0x1, 0x8)

    label("loc_154D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154E5")
    ClearChrFlags(0x2, 0x8)

    label("loc_154E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154F8")
    ClearChrFlags(0x3, 0x8)

    label("loc_154F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1550B")
    ClearChrFlags(0x4, 0x8)

    label("loc_1550B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1551E")
    ClearChrFlags(0x5, 0x8)

    label("loc_1551E")

    Call(0, 64)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_51_15366 end

    def Function_52_15535(): pass

    label("Function_52_15535")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "08", 0x1, 0x1)
    OP_68(207830, 1330, 127120, 0)
    MoveCamera(56, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1558D")
    SetChrFlags(0x0, 0x8)

    label("loc_1558D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_155A0")
    SetChrFlags(0x1, 0x8)

    label("loc_155A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_155B3")
    SetChrFlags(0x2, 0x8)

    label("loc_155B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_155C6")
    SetChrFlags(0x3, 0x8)

    label("loc_155C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_155D9")
    SetChrFlags(0x4, 0x8)

    label("loc_155D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_155EC")
    SetChrFlags(0x5, 0x8)

    label("loc_155EC")

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
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1568E")
    ClearChrFlags(0x0, 0x8)

    label("loc_1568E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156A1")
    ClearChrFlags(0x1, 0x8)

    label("loc_156A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156B4")
    ClearChrFlags(0x2, 0x8)

    label("loc_156B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156C7")
    ClearChrFlags(0x3, 0x8)

    label("loc_156C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156DA")
    ClearChrFlags(0x4, 0x8)

    label("loc_156DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156ED")
    ClearChrFlags(0x5, 0x8)

    label("loc_156ED")

    Call(0, 64)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_52_15535 end

    def Function_53_15704(): pass

    label("Function_53_15704")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "03", 0x1, 0x1)
    OP_68(51760, 1300, 129800, 0)
    MoveCamera(29, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1575C")
    SetChrFlags(0x0, 0x8)

    label("loc_1575C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1576F")
    SetChrFlags(0x1, 0x8)

    label("loc_1576F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15782")
    SetChrFlags(0x2, 0x8)

    label("loc_15782")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15795")
    SetChrFlags(0x3, 0x8)

    label("loc_15795")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_157A8")
    SetChrFlags(0x4, 0x8)

    label("loc_157A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_157BB")
    SetChrFlags(0x5, 0x8)

    label("loc_157BB")

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
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1585A")
    ClearChrFlags(0x0, 0x8)

    label("loc_1585A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1586D")
    ClearChrFlags(0x1, 0x8)

    label("loc_1586D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15880")
    ClearChrFlags(0x2, 0x8)

    label("loc_15880")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15893")
    ClearChrFlags(0x3, 0x8)

    label("loc_15893")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_158A6")
    ClearChrFlags(0x4, 0x8)

    label("loc_158A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_158B9")
    ClearChrFlags(0x5, 0x8)

    label("loc_158B9")

    Call(0, 64)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_53_15704 end

    def Function_54_158D0(): pass

    label("Function_54_158D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x1, 0x1)
    OP_68(52520, 1300, 124040, 0)
    MoveCamera(70, 13, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15933")
    SetChrFlags(0x0, 0x8)

    label("loc_15933")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15946")
    SetChrFlags(0x1, 0x8)

    label("loc_15946")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15959")
    SetChrFlags(0x2, 0x8)

    label("loc_15959")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1596C")
    SetChrFlags(0x3, 0x8)

    label("loc_1596C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1597F")
    SetChrFlags(0x4, 0x8)

    label("loc_1597F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15992")
    SetChrFlags(0x5, 0x8)

    label("loc_15992")

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
    Call(0, 55)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A31")
    ClearChrFlags(0x0, 0x8)

    label("loc_15A31")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A44")
    ClearChrFlags(0x1, 0x8)

    label("loc_15A44")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A57")
    ClearChrFlags(0x2, 0x8)

    label("loc_15A57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A6A")
    ClearChrFlags(0x3, 0x8)

    label("loc_15A6A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A7D")
    ClearChrFlags(0x4, 0x8)

    label("loc_15A7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A90")
    ClearChrFlags(0x5, 0x8)

    label("loc_15A90")

    Call(0, 64)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_54_158D0 end

    def Function_55_15AA7(): pass

    label("Function_55_15AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B22")
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

    label("loc_15B22")

    Return()

    # Function_55_15AA7 end

    def Function_56_15B23(): pass

    label("Function_56_15B23")

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

    # Function_56_15B23 end

    def Function_57_15BCB(): pass

    label("Function_57_15BCB")

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
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_15C8E"),
        (1, "loc_15C97"),
        (2, "loc_15CA0"),
        (3, "loc_15CA9"),
        (4, "loc_15CB2"),
        (5, "loc_15CBB"),
        (6, "loc_15CC4"),
        (7, "loc_15CCD"),
        (SWITCH_DEFAULT, "loc_15CD6"),
    )


    label("loc_15C8E")

    PlayBGM("ed7400", 0)
    Jump("loc_15CD6")

    label("loc_15C97")

    PlayBGM("ed7401", 0)
    Jump("loc_15CD6")

    label("loc_15CA0")

    PlayBGM("ed7402", 0)
    Jump("loc_15CD6")

    label("loc_15CA9")

    PlayBGM("ed7204", 0)
    Jump("loc_15CD6")

    label("loc_15CB2")

    PlayBGM("ed7205", 0)
    Jump("loc_15CD6")

    label("loc_15CBB")

    PlayBGM("ed7201", 0)
    Jump("loc_15CD6")

    label("loc_15CC4")

    PlayBGM("ed7200", 0)
    Jump("loc_15CD6")

    label("loc_15CCD")

    PlayBGM("ed7202", 0)
    Jump("loc_15CD6")

    label("loc_15CD6")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_57_15BCB end

    def Function_58_15D05(): pass

    label("Function_58_15D05")

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

    # Function_58_15D05 end

    def Function_59_15DA8(): pass

    label("Function_59_15DA8")

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

    # Function_59_15DA8 end

    def Function_60_15E4E(): pass

    label("Function_60_15E4E")

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

    # Function_60_15E4E end

    def Function_61_15EF4(): pass

    label("Function_61_15EF4")

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

    # Function_61_15EF4 end

    def Function_62_15F9A(): pass

    label("Function_62_15F9A")

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

    # Function_62_15F9A end

    def Function_63_1604A(): pass

    label("Function_63_1604A")

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

    # Function_63_1604A end

    def Function_64_160EC(): pass

    label("Function_64_160EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16124")
    OP_DE(0x16, 0x0)

    label("loc_16124")

    Return()

    # Function_64_160EC end

    def Function_65_16125(): pass

    label("Function_65_16125")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1619C")
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

    label("loc_1619C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_161B8")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_161B8")

    Return()

    # Function_65_16125 end

    def Function_66_161B9(): pass

    label("Function_66_161B9")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16230")
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

    label("loc_16230")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1624C")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1624C")

    Return()

    # Function_66_161B9 end

    def Function_67_1624D(): pass

    label("Function_67_1624D")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162C4")
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

    label("loc_162C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_162E0")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_162E0")

    Return()

    # Function_67_1624D end

    def Function_68_162E1(): pass

    label("Function_68_162E1")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16358")
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

    label("loc_16358")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16374")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_16374")

    Return()

    # Function_68_162E1 end

    SaveToFile()

Try(main)
