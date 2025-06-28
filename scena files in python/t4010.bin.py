from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t4010.bin",                # FileName
        "t4010",                    # MapName
        "t4010",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 2, 0, 3],
    )

    BuildStringList((
        "t4010",                  # 0
        "Archbishop Eralda",      # 1
        "Father Genus",           # 2
        "Father Renton",          # 3
        "Sister Hatina",          # 4
        "Sister Marble",          # 5
        "Trader Morgio",          # 6
        "Sergeant Major Seeker",  # 7
        "Tamil",                  # 8
        "Hamil",                  # 9
        "Momo",                   # 10
        "Pansy",                  # 11
        "Couta",                  # 12
        "Eugot",                  # 13
        "Anri",                   # 14
        "Tourist Takt",           # 15
        "Boy",                    # 16
        "Girl",                   # 17
        "Boy",                    # 18
        "Girl",                   # 19
        "Boy",                    # 20
        "Girl",                   # 21
        "Harold",                 # 22
        "Sophia",                 # 23
        "Colin",                  # 24
        "Leyte",                  # 25
        "Ryu",                    # 26
        "SE制御",                 # 27
    ))

    AddCharChip((
        "chr/ch26500.itc",                   # 00
        "chr/ch25300.itc",                   # 01
        "chr/ch25400.itc",                   # 02
        "chr/ch25500.itc",                   # 03
        "chr/ch21802.itc",                   # 04
        "chr/ch00800.itc",                   # 05
        "chr/ch23800.itc",                   # 06
        "chr/ch23802.itc",                   # 07
        "chr/ch20702.itc",                   # 08
        "chr/ch22302.itc",                   # 09
        "chr/ch21402.itc",                   # 0A
        "chr/ch20602.itc",                   # 0B
        "chr/ch22202.itc",                   # 0C
        "chr/ch09302.itc",                   # 0D
        "chr/ch09402.itc",                   # 0E
        "chr/ch07202.itc",                   # 0F
        "chr/ch10300.itc",                   # 10
        "chr/ch24602.itc",                   # 11
        "chr/ch24702.itc",                   # 12
        "chr/ch23902.itc",                   # 13
        "chr/ch34202.itc",                   # 14
        "chr/ch21502.itc",                   # 15
        "chr/ch24400.itc",                   # 16
    ))

    DeclNpc(-209,    379,     23229,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-2960,   250,     20010,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(98069,   0,       6789,    315,  257,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(2950,    189,     19709,   165,  257,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(150800,  200,     17500,   180,  257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-3849,   150,     6519,    0,    341,  0x0, 0,   4,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(1289,    0,       23229,   270,  385,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(153690,  200,     16420,   45,   385,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(154850,  200,     16180,   0,    385,  0x0, 0,   6,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(147139,  150,     12229,   0,    469,  0x0, 0,   8,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(148490,  150,     9130,    0,    469,  0x0, 0,   9,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(148490,  150,     12229,   0,    469,  0x0, 0,   10,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(147139,  150,     9130,    0,    469,  0x0, 0,   20,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(154929,  150,     12229,   0,    469,  0x0, 0,   12,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(1649,    0,       11819,   0,    385,  0x0, 0,   22,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(154929,  150,     9130,    0,    469,  0x0, 0,   17,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(153619,  150,     6150,    0,    469,  0x0, 0,   18,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(153619,  150,     6150,    0,    469,  0x0, 0,   7,   0,   255, 255, 0,   28,  255,  0)
    DeclNpc(148490,  150,     6150,    0,    469,  0x0, 0,   19,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(154929,  150,     12229,   0,    469,  0x0, 0,   11,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(153619,  150,     9130,    0,    469,  0x0, 0,   21,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(-5250,   200,     16600,   360,  389,  0x0, 0,   13,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(-3250,   200,     16600,   360,  389,  0x0, 0,   14,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(-4250,   200,     16600,   360,  389,  0x0, 0,   15,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(29,      0,       10930,   0,    385,  0x0, 0,   16,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(153619,  150,     12229,   0,    453,  0x0, 0,   11,  0,   255, 255, 0,   34,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(150910,  200,     16530,   1200,    150800,  1700,    17500,   0x007E, 0,  10, 0x0000)
    DeclActor(40,      500,     21930,   1200,    -210,    2100,    23230,   0x007E, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_500",          # 00, 0
        "Function_1_5B8",          # 01, 1
        "Function_2_5E3",          # 02, 2
        "Function_3_86D",          # 03, 3
        "Function_4_99E",          # 04, 4
        "Function_5_9A2",          # 05, 5
        "Function_6_226D",         # 06, 6
        "Function_7_2556",         # 07, 7
        "Function_8_3125",         # 08, 8
        "Function_9_426B",         # 09, 9
        "Function_10_4D84",        # 0A, 10
        "Function_11_4D88",        # 0B, 11
        "Function_12_642E",        # 0C, 12
        "Function_13_65AB",        # 0D, 13
        "Function_14_6FFE",        # 0E, 14
        "Function_15_7CFA",        # 0F, 15
        "Function_16_7DE7",        # 10, 16
        "Function_17_8283",        # 11, 17
        "Function_18_8839",        # 12, 18
        "Function_19_8B16",        # 13, 19
        "Function_20_8D6A",        # 14, 20
        "Function_21_8F93",        # 15, 21
        "Function_22_91B9",        # 16, 22
        "Function_23_936D",        # 17, 23
        "Function_24_9584",        # 18, 24
        "Function_25_9741",        # 19, 25
        "Function_26_993C",        # 1A, 26
        "Function_27_9AAA",        # 1B, 27
        "Function_28_9BDA",        # 1C, 28
        "Function_29_9D59",        # 1D, 29
        "Function_30_9EEB",        # 1E, 30
        "Function_31_A588",        # 1F, 31
        "Function_32_A6C5",        # 20, 32
        "Function_33_A8E3",        # 21, 33
        "Function_34_AC81",        # 22, 34
        "Function_35_AE76",        # 23, 35
        "Function_36_AFD2",        # 24, 36
        "Function_37_B386",        # 25, 37
        "Function_38_B6B0",        # 26, 38
        "Function_39_E6C0",        # 27, 39
        "Function_40_E703",        # 28, 40
        "Function_41_F545",        # 29, 41
        "Function_42_1035D",       # 2A, 42
        "Function_43_1060A",       # 2B, 43
        "Function_44_11465",       # 2C, 44
        "Function_45_11DE6",       # 2D, 45
        "Function_46_18EAB",       # 2E, 46
        "Function_47_18EC7",       # 2F, 47
        "Function_48_18EEA",       # 30, 48
        "Function_49_1A1A8",       # 31, 49
        "Function_50_1A21D",       # 32, 50
        "Function_51_1A236",       # 33, 51
        "Function_52_1A2A8",       # 34, 52
    ))


    def Function_0_500(): pass

    label("Function_0_500")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_540"),
        (1, "loc_54C"),
        (2, "loc_558"),
        (3, "loc_564"),
        (4, "loc_570"),
        (5, "loc_57C"),
        (6, "loc_588"),
        (SWITCH_DEFAULT, "loc_594"),
    )


    label("loc_540")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_54C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_558")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_564")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_570")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_57C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_588")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_594")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_5A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A0")

    label("loc_5B7")

    Return()

    # Function_0_500 end

    def Function_1_5B8(): pass

    label("Function_1_5B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E2")
    OP_94(0xFE, 0x17A8E, 0x125C, 0x186A0, 0x1D4C, 0x3E8)
    Sleep(450)
    Jump("Function_1_5B8")

    label("loc_5E2")

    Return()

    # Function_1_5B8 end

    def Function_2_5E3(): pass

    label("Function_2_5E3")

    BeginChrThread(0xA, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5FC")
    ClearChrFlags(0x20, 0x80)
    Jump("loc_859")

    label("loc_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_62E")
    SetChrPos(0xB, 149530, 200, 17470, 90)
    OP_93(0xC, 0x10E, 0x0)
    ClearChrFlags(0xE, 0x80)
    OP_93(0x8, 0x5A, 0x0)
    Jump("loc_859")

    label("loc_62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_63C")
    Jump("loc_859")

    label("loc_63C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_66D")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_859")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_6F3")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 154930, 150, 9130, 0)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0xF, 148490, 150, 12230, 0)
    SetChrChipByIndex(0x10, 0x7)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, 147140, 150, 12230, 0)
    Jump("loc_859")

    label("loc_6F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_701")
    Jump("loc_859")

    label("loc_701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_720")
    SetChrPos(0xC, 148920, 0, 13890, 180)
    Jump("loc_859")

    label("loc_720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_72E")
    Jump("loc_859")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_757")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xC, 154300, 200, 17590, 180)
    Jump("loc_859")

    label("loc_757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_765")
    Jump("loc_859")

    label("loc_765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_773")
    Jump("loc_859")

    label("loc_773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7AC")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xA, 96000, 0, 7830, 270)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_859")

    label("loc_7AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7D6")
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xA, 96000, 0, 7830, 270)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_859")

    label("loc_7D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_850")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0xF, 154930, 0, 12230, 0)
    SetChrChipByIndex(0x10, 0x7)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, 153620, 0, 12230, 0)
    Jump("loc_859")

    label("loc_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_859")

    label("loc_859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86C")
    ClearChrFlags(0x16, 0x80)

    label("loc_86C")

    Return()

    # Function_2_5E3 end

    def Function_3_86D(): pass

    label("Function_3_86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_87B")
    Jump("loc_942")

    label("loc_87B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_889")
    Jump("loc_942")

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_897")
    Jump("loc_942")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8A5")
    Jump("loc_942")

    label("loc_8A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_8B3")
    Jump("loc_942")

    label("loc_8B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_8C1")
    Jump("loc_942")

    label("loc_8C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8D3")
    OP_65(0x0, 0x1)
    Jump("loc_942")

    label("loc_8D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8E1")
    Jump("loc_942")

    label("loc_8E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8F3")
    OP_65(0x0, 0x1)
    Jump("loc_942")

    label("loc_8F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_901")
    Jump("loc_942")

    label("loc_901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_90F")
    Jump("loc_942")

    label("loc_90F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_91D")
    Jump("loc_942")

    label("loc_91D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_92B")
    Jump("loc_942")

    label("loc_92B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_939")
    Jump("loc_942")

    label("loc_939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_942")

    label("loc_942")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_970")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96B")
    Event(0, 37)

    label("loc_96B")

    Jump("loc_98B")

    label("loc_970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98B")
    Event(0, 36)

    label("loc_98B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_99D")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_99D")

    Return()

    # Function_3_86D end

    def Function_4_99E(): pass

    label("Function_4_99E")

    Call(0, 5)
    Return()

    # Function_4_99E end

    def Function_5_9A2(): pass

    label("Function_5_9A2")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB0")

    ChrTalk(
        0x8,
        (
            "How am I going to deal with that pesky bell\x01",
            "in the ruins...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "(If it really is an artifact, those meddlesome\x01",
            "frumps will come to intervene...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "(Hmph. Well, I'd like to see them try! Their\x01",
            "kind is NOT welcome in my Crossbell.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B06")

    label("loc_AB0")


    ChrTalk(
        0x8,
        (
            "Hmph, very well.\x01",
            "We shall investigate those ruins,\x01",
            "as well as Stargazer's Tower.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B06")

    Jump("loc_2269")

    label("loc_B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B26")
    Call(0, 6)
    Jump("loc_B99")

    label("loc_B26")


    ChrTalk(
        0x8,
        (
            "A bell capable of summoning fiends...?\x01",
            "If such an object truly does exist there,\x01",
            "we'll have to act quickly...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B99")

    Jump("loc_2269")

    label("loc_B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_D4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C96")

    ChrTalk(
        0x8,
        "I heard the mafia have started to move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am relieved no citizens got caught up\x01",
            "in their antics, but still...such tomfoolery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, Aidios, please deliver mankind from\x01",
            "the hardships brought by such strife...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D45")

    label("loc_C96")


    ChrTalk(
        0x8,
        (
            "I take much comfort in knowing that innocent\x01",
            "lives weren't involved in the conflict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, Aidios, please deliver mankind from\x01",
            "the hardships brought by such strife...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D45")

    Jump("loc_2269")

    label("loc_D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_E49")

    ChrTalk(
        0x8,
        (
            "Hmm... It may just be my imagination,\x01",
            "but I could've sworn I heard the toll\x01",
            "of a bell coming from the mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, there isn't supposed to be a\x01",
            "bell tower between us and Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#0505F(A bell...? What's up with that?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2269")

    label("loc_E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_FF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6C")

    ChrTalk(
        0x8,
        "You've spoken with Sister Marble, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I trust your business is now finished.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FY-Yes. Her expertise was really helpful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Very well, then. Feel free to visit us\x01",
            "whenever we can be of assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, Aidios, please guide their souls...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FF4")

    label("loc_F6C")


    ChrTalk(
        0x8,
        (
            "If you run into any trouble, you are always\x01",
            "welcome in the sanctity of the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, Aidios, please guide their souls...\x02",
    )

    CloseMessageWindow()

    label("loc_FF4")

    Jump("loc_2269")

    label("loc_FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_12C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1256")

    ChrTalk(
        0x8,
        (
            "Welcome to the Crossbell Cathedral,\x01",
            "you three.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1110FOoh, ooh! A beard! Hey, can I touch\x01",
            "it a little bit? It looks so fluffy!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 500)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x153, 500)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FH-Hey, KeA!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_113F")

    ChrTalk(
        0x102,
        (
            "#0103FWe're terribly sorry, Archbishop. She's\x01",
            "still learning to mind her manners...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CF")

    label("loc_113F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_119B")

    ChrTalk(
        0x103,
        (
            "#0203FOur sincerest apologies. As you can\x01",
            "see, she is still quite young.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CF")

    label("loc_119B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_11CF")

    ChrTalk(
        0x104,
        "#0303FS-Sorry 'bout that, Archbishop.\x02",
    )

    CloseMessageWindow()

    label("loc_11CF")


    ChrTalk(
        0x8,
        "Please, do not fret.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Few things in life can beat seeing\x01",
            "children so full of life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, Aidios, bless this child.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12BB")

    label("loc_1256")


    ChrTalk(
        0x8,
        (
            "Few things in life can beat seeing\x01",
            "children so full of life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, Aidios, bless this child.\x02",
    )

    CloseMessageWindow()

    label("loc_12BB")

    Jump("loc_2269")

    label("loc_12C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1436")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B2")

    ChrTalk(
        0x8,
        (
            "Now...once tonight's Mass comes to\x01",
            "a close, so will our activities for the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Many found their way to our parish this\x01",
            "week. I pray that Aidios be with them in\x01",
            "their endeavors, always...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1431")

    label("loc_13B2")


    ChrTalk(
        0x8,
        (
            "Many people who came for the festival\x01",
            "made their way to our parish. May Aidios\x01",
            "walk with them during their journeys home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1431")

    Jump("loc_2269")

    label("loc_1436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_166E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C7")

    ChrTalk(
        0x8,
        (
            "Late last night, we were visited by a man\x01",
            "supposedly from the Imperial government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I saw right through his futile attempt to\x01",
            "inveigle me into allowing him to tap into\x01",
            "the influential network of the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Eventually, I was forced to raise my voice\x01",
            "and drive him out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a servant of Aidios, it is my obligation\x01",
            "to stay politically neutral at all times.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1669")

    label("loc_15C7")


    ChrTalk(
        0x8,
        (
            "The Septian Church is firmly invested in\x01",
            "every human life on this continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Using our faith to make political advances\x01",
            "is nothing more than blasphemy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1669")

    Jump("loc_2269")

    label("loc_166E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1901")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1878")

    ChrTalk(
        0x8,
        (
            "I heard that there was a squabble in the\x01",
            "Downtown District last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And the juvenile gangs were not the only involved\x01",
            "parties, as one would expect. Supposedly, bracers\x01",
            "and the police took part in it as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(*gulp*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmph. So it was you, was it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "During festivals, people become so worked up\x01",
            "that they lose their ability to think rationally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "The police should be better than that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FS-Sorry...\x02\x03",
            "(Guys, this oldtimer is straight-up\x01",
            "nightmare fuel!)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18FC")

    label("loc_1878")


    ChrTalk(
        0x8,
        (
            "Well, I suppose we should feel fortunate\x01",
            "that no one was hurt in the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I trust you will not repeat your mistakes.\x02",
    )

    CloseMessageWindow()

    label("loc_18FC")

    Jump("loc_2269")

    label("loc_1901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9E")

    ChrTalk(
        0x8,
        (
            "Crossbell has been through quite a lot\x01",
            "in its 70 years of existence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Pain and sadness are unavoidable when\x01",
            "reading the pages of our history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This week, the people will spend their time\x01",
            "however they please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm... I should try to find time for\x01",
            "leisure in between Mass as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Perhaps I'll open up some medicine textbooks\x01",
            "to get back into the spirit I once had.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B53")

    label("loc_1A9E")


    ChrTalk(
        0x8,
        (
            "Surely I'll find ways to spend this year's\x01",
            "Anniversary Festival besides holding Mass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Perhaps I'll open up some medicine textbooks\x01",
            "to get back into the spirit I once had.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B53")

    Jump("loc_2269")

    label("loc_1B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1D3A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_1B76")
    Call(0, 42)
    Jump("loc_1D35")

    label("loc_1B76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_1B8B")
    Call(0, 40)
    Jump("loc_1D35")

    label("loc_1B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB0")

    ChrTalk(
        0x8,
        (
            "It's said that when we pray to Aidios, the\x01",
            "hearts of mankind become pure again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In the darkness that comes with their bowed\x01",
            "head, they are relieved from their troubles and\x01",
            "given a chance to reflect upon their ways...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please, come to Mass if you have the time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D35")

    label("loc_1CB0")


    ChrTalk(
        0x8,
        (
            "It's said that when we pray to Aidios, the\x01",
            "hearts of mankind become pure again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please, come to Mass if you have the time.\x02",
    )

    CloseMessageWindow()

    label("loc_1D35")

    Jump("loc_2269")

    label("loc_1D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1F1B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_1D58")
    Call(0, 42)
    Jump("loc_1F16")

    label("loc_1D58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_1D6D")
    Call(0, 40)
    Jump("loc_1F16")

    label("loc_1D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E96")

    ChrTalk(
        0x8,
        (
            "Today we shall hold a Mass in this most\x01",
            "sacred of cathedrals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Goddess of the Sky watches over us,\x01",
            "bestowing upon us the miracle of life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "During Mass, we remind ourselves to be grateful\x01",
            "that we have been given a chance to live, breathe,\x01",
            "and love in this world.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F16")

    label("loc_1E96")


    ChrTalk(
        0x8,
        (
            "Today we shall hold a Mass in this most\x01",
            "sacred of cathedrals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Forget not to express your gratitude to\x01",
            "Aidios as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F16")

    Jump("loc_2269")

    label("loc_1F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_204C")

    ChrTalk(
        0x8,
        (
            "Through whispers in my ears, I am aware\x01",
            "of the Special Support Section's actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Pay no mind to those accusing you of\x01",
            "blatantly copying the bracers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...for the Goddess of the Sky shall never\x01",
            "abandon those who act under the belief\x01",
            "of righteousness and justice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2123")

    label("loc_204C")


    ChrTalk(
        0x8,
        (
            "It is nothing short of a miracle that there are\x01",
            "people in this world willing to help others in need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Goddess of the Sky shall never abandon\x01",
            "those who act under the belief of righteousness\x01",
            "and justice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2123")

    Jump("loc_2269")

    label("loc_2128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2269")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F5")

    ChrTalk(
        0x8,
        "Welcome, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Correct me if I'm mistaken, but doesn't your\x01",
            "next destination lead you into the northern\x01",
            "mountain range?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, Aidios, guide these brave souls...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2269")

    label("loc_21F5")


    ChrTalk(
        0x8,
        (
            "The teachings of Aidios will assuredly\x01",
            "keep you from losing your way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, Aidios, guide these children...\x02",
    )

    CloseMessageWindow()

    label("loc_2269")

    TalkEnd(0x8)
    Return()

    # Function_5_9A2 end

    def Function_6_226D(): pass

    label("Function_6_226D")

    OP_4B(0x8, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0x8, 0xE, 0)
    TurnDirection(0xE, 0x8, 0)

    ChrTalk(
        0xE,
        (
            "#0501FAnd that sums up the investigation report\x01",
            "regarding the interior of the ruins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A bell that summons fiends...?\x01",
            "It irks me that something like that has been\x01",
            "right under our noses this entire time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's a possibility that this bell you saw\x01",
            "is indeed an artifact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Thank you for your report.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#0500FSir!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_254A")

    ChrTalk(
        0x10A,
        (
            "#0604FSergeant Major Seeker of the Guardian Force.\x01",
            "I heard her politeness is overwhelming and her\x01",
            "capabilities look promising.\x02\x03",
            "#0602FHmph. You could learn a thing or two\x01",
            "from her diligence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0310F(Ouch. Tio Tot, got any water for that sick burn?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0211F(I am sorry to inform you that the jab was\x01",
            "clearly directed toward you...and only you.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_254A")

    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_6_226D end

    def Function_7_2556(): pass

    label("Function_7_2556")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_263D")

    ChrTalk(
        0xFE,
        (
            "Sergeant Major Seeker stopped by to\x01",
            "deliver her investigation report on the\x01",
            "ruins this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The possibility that there may be an\x01",
            "artifact in there is enough to warrant\x01",
            "the Septian Church's attention.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3121")

    label("loc_263D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_26DB")

    ChrTalk(
        0xFE,
        (
            "I'm not sure what the bell she spoke of\x01",
            "truly is, but I'll admit it worries me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, just why exactly did that bell start\x01",
            "ringing...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3121")

    label("loc_26DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_275E")

    ChrTalk(
        0xFE,
        (
            "The archbishop is deeply disheartened\x01",
            "by the incident in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Immorality pains him like nothing else.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3121")

    label("loc_275E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2802")

    ChrTalk(
        0xFE,
        (
            "Sister Hatina went to visit the Downtown District\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since the children there don't come here for\x01",
            "Sunday School, we go to them instead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3121")

    label("loc_2802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_294C")

    ChrTalk(
        0xFE,
        (
            "Both Thaumaturgy of the Septian Church and\x01",
            "the modern medicine developed at St. Ursula\x01",
            "have the capability to heal people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, one heals the heart, and the other\x01",
            "the body. Unfortunately, these two methods\x01",
            "aren't compatible yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As of now, modern medicine is advancing at\x01",
            "an extraordinary rate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3121")

    label("loc_294C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2A27")

    ChrTalk(
        0xFE,
        (
            "The week after the Anniversary Festival has\x01",
            "been as peaceful as could be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, some citizens still feel anxious and\x01",
            "come here to find relief through prayer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm... Did something happen?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3121")

    label("loc_2A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2ADD")

    ChrTalk(
        0xFE,
        (
            "Like every year, a great number of people\x01",
            "came to attend our festival Mass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that all our visitors stay safe and\x01",
            "return here in high spirits next year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3121")

    label("loc_2ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2B50")

    ChrTalk(
        0xFE,
        (
            "Oh, Aidios, She Who Dwells Above,\x01",
            "give guidance to the lambs who have\x01",
            "wandered off your path...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3121")

    label("loc_2B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2C24")

    ChrTalk(
        0xFE,
        (
            "Archbishop Eralda's achievements left a\x01",
            "mark on the pharmaceutical world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "St. Ursula Hospital still prescribes medicines\x01",
            "based on the foundations once laid by\x01",
            "Archbishop Eralda, actually.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3121")

    label("loc_2C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2D1D")

    ChrTalk(
        0xFE,
        (
            "Mayor MacDowell and Speaker Hartmann\x01",
            "came to pray on the first day of the festival,\x01",
            "hoping for its success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They are considered rivals, but for the sake\x01",
            "of Crossbell's citizenry, I hope they would\x01",
            "join hands and work as one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3121")

    label("loc_2D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2E7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E27")

    ChrTalk(
        0xFE,
        (
            "Harold and his family often visit our cathedral.\x01",
            "They're pious people who pray with vigor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Their belief in She Who Dwells Above\x01",
            "has never waned. Bless them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Aidios, She Who Dwells Above,\x01",
            "please watch over Your children.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_2E76")

    label("loc_2E27")


    ChrTalk(
        0xFE,
        (
            "Oh, Aidios, She Who Dwells Above,\x01",
            "please watch over Your pious followers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E76")

    Jump("loc_3121")

    label("loc_2E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2F4D")

    ChrTalk(
        0xFE,
        (
            "Dieter Crois of the IBC always comes to\x01",
            "the cathedral in his huge limousine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though he nearly runs over people,\x01",
            "I can't get angry after he apologizes with\x01",
            "that bright smile of his.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3121")

    label("loc_2F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_301D")

    ChrTalk(
        0xFE,
        (
            "The mayor of Crossbell City also stops by\x01",
            "the cathedral to pray on a regular basis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he prays for the peace and safety\x01",
            "of fellow Crossbellans whenever his\x01",
            "schedule allows him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3121")

    label("loc_301D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3121")

    ChrTalk(
        0xFE,
        (
            "Immediately following the Great Collapse of\x01",
            "days long past, the Septian Church went to\x01",
            "bestow Her light upon the people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This cathedral is only one facet of the\x01",
            "Septian Church. Here, Aidios guides\x01",
            "those who are lost to their rightful paths.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3121")

    TalkEnd(0xFE)
    Return()

    # Function_7_2556 end

    def Function_8_3125(): pass

    label("Function_8_3125")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_33AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32BA")

    ChrTalk(
        0xFE,
        (
            "Archbishop Eralda doesn't think too highly of\x01",
            "the Congregation for the Sacraments, the\x01",
            "organization in charge of retrieving artifacts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He heard rumors of its chivalric order, the\x01",
            "Gralsritter, resorting to some...less than\x01",
            "ethical practices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's nothing Archbishop Eralda loathes\x01",
            "more than immorality. I doubt he will ever\x01",
            "forgive or approve of them again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_33A6")

    label("loc_32BA")


    ChrTalk(
        0xFE,
        (
            "Archbishop Eralda doesn't think highly of\x01",
            "the Gralsritter, the chivalric order of the\x01",
            "Congregation for the Sacraments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's nothing Archbishop Eralda loathes\x01",
            "as much as immorality. Therefore, he will\x01",
            "never approve of them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33A6")

    Jump("loc_4267")

    label("loc_33AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_33F2")

    ChrTalk(
        0xFE,
        (
            "It's quiet around here with no\x01",
            "Sunday School today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4267")

    label("loc_33F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_34BC")

    ChrTalk(
        0xFE,
        (
            "The incident in the city has enraged\x01",
            "Archbishop Eralda.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's relieved no one got injured, but having\x01",
            "so many live in fear over a selfish squabble\x01",
            "is something he can't tolerate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4267")

    label("loc_34BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3602")

    ChrTalk(
        0xFE,
        (
            "The Testaments of the Septian Church mention\x01",
            "the existence of creatures known as fiends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fiends oppose the Goddess and are said to\x01",
            "take shelter in the hearts of mankind, forcing\x01",
            "them to bring harm to innocent souls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To us at the church, they are a warning\x01",
            "of things to come. An omen, if you will.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4267")

    label("loc_3602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_36F6")

    ChrTalk(
        0xFE,
        (
            "Sister Marble has been serving here at the\x01",
            "cathedral for a very long time. She's fairly\x01",
            "well known within the Septian Church, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to her cheerful personality, there are\x01",
            "always people stopping by just to see her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4267")

    label("loc_36F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3753")

    ChrTalk(
        0xFE,
        (
            "Phew... I'm really slaving away at this\x01",
            "assignment for Archbishop Eralda.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4267")

    label("loc_3753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_380B")

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival ends today and\x01",
            "tomorrow, Sunday School will resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Knowing all the children will be back in class\x01",
            "gives me all the motivation I need.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4267")

    label("loc_380B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3957")

    ChrTalk(
        0xFE,
        (
            "The position of archbishop comes with a\x01",
            "considerable amount of influence within\x01",
            "the Septian Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Archbishop Eralda is an especially prominent\x01",
            "figure within the Congregation for Divine Worship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "His stance to never, ever lend his hand to\x01",
            "wickedness inspired us to follow him and\x01",
            "trust in his judgment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4267")

    label("loc_3957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3A1F")

    ChrTalk(
        0xFE,
        (
            "I heard that the IBC's CEO, Dieter Crois, uses\x01",
            "his wealth to support various charity projects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As someone with the church, I can't stress\x01",
            "enough how deeply I respect that man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4267")

    label("loc_3A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3C53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B53")

    ChrTalk(
        0xFE,
        (
            "Trader Morgio often comes here to pray...\x01",
            "but I'm afraid that he relies on the Goddess\x01",
            "a little bit TOO much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He claims his financial success comes from\x01",
            "his devout prayers, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I honestly don't know what to make of it.\x01",
            "Are his own efforts really the Goddess'?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3C4E")

    label("loc_3B53")


    ChrTalk(
        0xFE,
        (
            "Trader Morgio often comes here to pray...\x01",
            "but I'm afraid that he relies on the Goddess\x01",
            "a little bit TOO much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I may be a priest, but I discourage overly\x01",
            "depending on Aidios. If you aren't careful,\x01",
            "you might lose your sense of self-reliance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C4E")

    Jump("loc_4267")

    label("loc_3C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3EEA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3D0D")

    ChrTalk(
        0xA,
        (
            "I hope the Lupinus Grass will prove useful\x01",
            "to the medical college.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We of the Septian Church are expecting\x01",
            "nothing short of greatness from St. Ursula.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EE5")

    label("loc_3D0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_3DCB")

    ChrTalk(
        0xA,
        (
            "Stubborn as he may be, the archbishop knows\x01",
            "what's right and what's wrong without fail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So I'm sure he'll recognize Doctor Lago's\x01",
            "skills if he deems them worthy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EE5")

    label("loc_3DCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3DE0")
    Call(0, 41)
    Jump("loc_3EE5")

    label("loc_3DE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_3E5D")

    ChrTalk(
        0xA,
        "Oh? How can I help you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is the office of Archbishop Eralda.\x01",
            "You can't simply barge in here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EE5")

    label("loc_3E5D")


    ChrTalk(
        0xFE,
        (
            "Archbishop Eralda has published several\x01",
            "books on the Septian Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're actually quite the easy read,\x01",
            "believe it or not.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE5")

    Jump("loc_4267")

    label("loc_3EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_40A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4016")

    ChrTalk(
        0xFE,
        (
            "The two gangs operating out of the Downtown District\x01",
            "are the Saber Vipers and Testaments, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those Testament hooligans in particular look\x01",
            "like they belong to some religious cult...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If only I could help them to find their way\x01",
            "back to their rightful path.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_409F")

    label("loc_4016")


    ChrTalk(
        0xFE,
        (
            "I truly wish I could help those Saber Viper\x01",
            "and Testaments kids...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Give them a little push in the right\x01",
            "direction, that's all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_409F")

    Jump("loc_4267")

    label("loc_40A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4267")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_419D")

    ChrTalk(
        0xFE,
        "To be honest, Archbishop Eralda is pretty strict.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "His punishment for immorality is merciless, but\x01",
            "his guidance for those in need is compassionate\x01",
            "and sincere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "As a priest, I aspire to become a man like him.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4267")

    label("loc_419D")


    ChrTalk(
        0xFE,
        (
            "His punishment for immorality is merciless, but\x01",
            "his guidance for those in need is compassionate\x01",
            "and sincere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's Archbishop Eralda for you. I hope that\x01",
            "I can become a man like him someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4267")

    TalkEnd(0xFE)
    Return()

    # Function_8_3125 end

    def Function_9_426B(): pass

    label("Function_9_426B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_42EA")

    ChrTalk(
        0xFE,
        (
            "Tomorrow morning, I'll be leaving on a\x01",
            "business trip to Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope the kids will be all right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D80")

    label("loc_42EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_43C3")

    ChrTalk(
        0xFE,
        (
            "I'll be leaving for Mainz tomorrow to teach\x01",
            "Sunday School, so I'm currently figuring\x01",
            "out the lesson plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Going on trips can be exhausting, but\x01",
            "seeing the kids again makes it worth\x01",
            "the effort.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D80")

    label("loc_43C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4457")

    ChrTalk(
        0xFE,
        (
            "I think there are more people attending\x01",
            "today than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The commotion over at the harbor\x01",
            "caused anxiety among the people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D80")

    label("loc_4457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4465")
    Jump("loc_4D80")

    label("loc_4465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_44EA")

    ChrTalk(
        0xFE,
        (
            "The looks on your faces tell me that\x01",
            "coming here was worth your time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd expect no less from Sister Marble.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D80")

    label("loc_44EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_45CB")

    ChrTalk(
        0xFE,
        "Is something bothering you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to consult the archbishop\x01",
            "or Sister Marble at your leisure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both have been active in the Septian\x01",
            "Church for a long time, so I'm sure\x01",
            "they can offer guidance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D80")

    label("loc_45CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_465A")

    ChrTalk(
        0xFE,
        (
            "Today is the final day of the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Aidios, guide these festivities\x01",
            "to a most peaceful conclusion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D80")

    label("loc_465A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_47DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4734")

    ChrTalk(
        0xFE,
        (
            "The thought that someone would simply\x01",
            "barge in like that and make such a bold\x01",
            "proposal to the archbishop...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell's roots of darkness may run\x01",
            "deeper than we originally thought.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_47D9")

    label("loc_4734")


    ChrTalk(
        0xFE,
        (
            "Trying to use the archbishop and the\x01",
            "rest of the parish for political benefits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell's roots of darkness may run\x01",
            "deeper than we originally thought.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47D9")

    Jump("loc_4D80")

    label("loc_47DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_487D")

    ChrTalk(
        0xFE,
        (
            "For someone as clumsy as Sister Juju,\x01",
            "she's a surprisingly good cook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if the kids are so drawn\x01",
            "to her because of her cookies?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D80")

    label("loc_487D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_497E")

    ChrTalk(
        0xFE,
        (
            "During the festival's opening day yesterday,\x01",
            "many came and joined us for Mass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Many mourned the souls of those who lost\x01",
            "their lives during past strife...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but wonder what the future\x01",
            "holds for Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4A1D")

    label("loc_497E")


    ChrTalk(
        0xFE,
        (
            "Memories of past conflicts are deeply rooted\x01",
            "in the lives of Crossbellans near and far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but wonder what the future\x01",
            "holds for Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A1D")

    Jump("loc_4D80")

    label("loc_4A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4A30")
    Jump("loc_4D80")

    label("loc_4A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4BBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B0E")

    ChrTalk(
        0xFE,
        (
            "The Septian Church wanted to invest in the\x01",
            "education of Zemuria's youth, and that led\x01",
            "to the creation of our Sunday Schools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sister Marble is teaching again today,\x01",
            "if you were curious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4BB6")

    label("loc_4B0E")


    ChrTalk(
        0xFE,
        (
            "Sister Marble has been in charge of this\x01",
            "cathedral's Sunday School for a long time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm preparing for my business trip to the\x01",
            "Downtown District tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BB6")

    Jump("loc_4D80")

    label("loc_4BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4D80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CE4")

    ChrTalk(
        0xFE,
        (
            "I heard that wolf-like monsters have been\x01",
            "damaging properties throughout the state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People keep voicing their concern that they\x01",
            "might become the next victim of their attacks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just hope the situation won't take a turn\x01",
            "for the worse from here on out...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4D80")

    label("loc_4CE4")


    ChrTalk(
        0xFE,
        (
            "I heard that someone finally got injured\x01",
            "during the wolf attacks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just hope the situation won't take a turn\x01",
            "for the worse from here on out...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D80")

    TalkEnd(0xFE)
    Return()

    # Function_9_426B end

    def Function_10_4D84(): pass

    label("Function_10_4D84")

    Call(0, 11)
    Return()

    # Function_10_4D84 end

    def Function_11_4D88(): pass

    label("Function_11_4D88")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DA1")
    Call(0, 38)
    Jump("loc_642A")

    label("loc_4DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E40")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_4DC3")
    Jump("loc_4E38")

    label("loc_4DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4DD1")
    Jump("loc_4E38")

    label("loc_4DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4DDF")
    Jump("loc_4E38")

    label("loc_4DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4DED")
    Jump("loc_4E38")

    label("loc_4DED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4DFB")
    Jump("loc_4E38")

    label("loc_4DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4E09")
    Jump("loc_4E38")

    label("loc_4E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4E17")
    Jump("loc_4E38")

    label("loc_4E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4E2F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E38")

    label("loc_4E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4E38")

    label("loc_4E38")

    Call(0, 13)
    Jump("loc_642A")

    label("loc_4E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4F12")

    ChrTalk(
        0xC,
        (
            "Ah, Lloyd and Elie... I assure you that\x01",
            "seeing you again fills me with joy, but\x01",
            "I'm in the middle of class right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Would you mind coming back on a day\x01",
            "I'm not teaching Sunday School?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_642A")

    label("loc_4F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5114")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5080")

    ChrTalk(
        0xC,
        (
            "It sounds like you did a great job assisting\x01",
            "the Guardian Force's investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You two seem to pop up everywhere.\x01",
            "It makes me proud to be your former teacher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Maybe I should brag about your successes\x01",
            "during the next Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FThat's really not necessary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0113FYou don't have to tease us, you know.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_510F")

    label("loc_5080")


    ChrTalk(
        0xC,
        "But I AM really proud of you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My former pupils have become model\x01",
            "citizens and the embodiment of justice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I couldn't be prouder.\x02",
    )

    CloseMessageWindow()

    label("loc_510F")

    Jump("loc_642A")

    label("loc_5114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_527B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51E1")
    OP_93(0xC, 0x10E, 0x0)

    ChrTalk(
        0xC,
        (
            "The Mainz area has always been an\x01",
            "important pillar of the Crossbell economy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Perhaps I should include that in my next\x01",
            "lesson to raise the kids' hometown spirit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5276")

    label("loc_51E1")


    ChrTalk(
        0xC,
        (
            "Hello, Lloyd, Elie. Were you looking\x01",
            "for me, by chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm terribly sorry, but I'm a little busy\x01",
            "today. Would you mind coming back\x01",
            "later?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5276")

    Jump("loc_642A")

    label("loc_527B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5524")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5472")

    ChrTalk(
        0xC,
        "Why, hello, you two. Did something happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Those looks on your faces can't fool me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0008FI don't know what you're talking about...\x02\x03",
            "#0003F(We definitely can't bring up the pills we\x01",
            "found in Crossbell City...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Anyway, remember to smile!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Lots of people rely on the Special Support\x01",
            "Section! You can't go worrying them with\x01",
            "that gloom and doom surrounding you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FYou...have a good point there. Thank you\x01",
            "very much for the advice, Sister Marble.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_551F")

    label("loc_5472")


    ChrTalk(
        0xC,
        (
            "Lots of people rely on the Special Support\x01",
            "Section! You can't go worrying them with\x01",
            "that gloom and doom surrounding you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "No matter what, always remember to smile.\x02",
    )

    CloseMessageWindow()

    label("loc_551F")

    Jump("loc_642A")

    label("loc_5524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_58C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5847")
    OP_93(0xC, 0xB4, 0x0)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0x0, 500)

    ChrTalk(
        0xC,
        "Oh, Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I understand KeA didn't want to be\x01",
            "hospitalized for some examinations?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FThat's right... Sorry. I feel like we went\x01",
            "and wasted your advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, no, please don't fret about it. Children\x01",
            "shouldn't be forced to do things they don't\x01",
            "want to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you have patience, I think she'll agree to\x01",
            "the examinations sooner or later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FYou might be right there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Sister Marbleeee! Since you're talking,\x01",
            "does that mean we can talk in class now?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x1B, 500)

    ChrTalk(
        0xC,
        (
            "Oh, pardon me. To think the teacher\x01",
            "herself would start chatting in class...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FOops, our bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FIt looks like we interrupted your lesson.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    ChrTalk(
        0xC,
        (
            "(Let's postpone our talk to sometime\x01",
            "I'm not teaching class, all right?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_58BD")

    label("loc_5847")

    OP_93(0xC, 0xB4, 0x0)

    ChrTalk(
        0xC,
        "Now, where was I...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm not as young as I used to be, but that's\x01",
            "no reason to excuse forgetfulness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58BD")

    Jump("loc_642A")

    label("loc_58C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_5B8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_5A2B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5A23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_598B")

    ChrTalk(
        0xC,
        "Thank you for your help today, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You, too, KeA. Please know that you're\x01",
            "always welcome to join Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FThank you, miss!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5A1E")

    label("loc_598B")


    ChrTalk(
        0xC,
        (
            "KeA, feel free to join Sunday School\x01",
            "whenever you can make it. Okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm sure the other children will be overjoyed\x01",
            "to have a new friend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A1E")

    Jump("loc_5A26")

    label("loc_5A23")

    Call(0, 43)

    label("loc_5A26")

    Jump("loc_5B8A")

    label("loc_5A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B16")

    ChrTalk(
        0xC,
        (
            "I don't think my Thaumaturgy can do much\x01",
            "more for KeA's memories than this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The Neurology Department at St. Ursula Hospital\x01",
            "might be able to provide further details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I recommend consulting them next.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5B8A")

    label("loc_5B16")


    ChrTalk(
        0xC,
        (
            "St. Ursula's staff might be able to\x01",
            "uncover more about KeA's condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I recommend consulting them next.\x02",
    )

    CloseMessageWindow()

    label("loc_5B8A")

    Jump("loc_642A")

    label("loc_5B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5BA0")
    Call(0, 38)
    Jump("loc_642A")

    label("loc_5BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5CF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C38")

    ChrTalk(
        0xC,
        "I'm busy preparing tomorrow's lesson.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh! It might be worthwhile to touch on\x01",
            "the geography of foreign countries...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5CF1")

    label("loc_5C38")


    ChrTalk(
        0xC,
        (
            "Perhaps including a worksheet on the\x01",
            "geography of foreign countries would\x01",
            "be beneficial.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even though we all share the continent of\x01",
            "Zemuria, cultures differ vastly per nation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CF1")

    Jump("loc_642A")

    label("loc_5CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5DDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D11")
    Call(0, 12)
    Jump("loc_5DD8")

    label("loc_5D11")


    ChrTalk(
        0xC,
        (
            "Even on days off from school, the\x01",
            "children like to come see me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The world has continued to move and change\x01",
            "since I started working as a teacher, but the\x01",
            "cuteness of children is a constant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DD8")

    Jump("loc_642A")

    label("loc_5DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5EC0")

    ChrTalk(
        0xC,
        (
            "Whenever I'm not teaching Sunday School,\x01",
            "I'm preparing the children's next lessons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But sometimes, the children still drop by to\x01",
            "visit me and the others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "It's more crowded than I thought it'd be.\x02",
    )

    CloseMessageWindow()
    Jump("loc_642A")

    label("loc_5EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5F4F")

    ChrTalk(
        0xC,
        "Are you enjoying the Anniversary Festival?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If your schedules allow it, I recommend you\x01",
            "put aside some time for prayer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_642A")

    label("loc_5F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6158")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60B7")

    ChrTalk(
        0xC,
        (
            "Recently, we started to hold Sunday School\x01",
            "outside of the cathedral every now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Children of Armorica, Mainz, and the Downtown\x01",
            "District rarely show up to class, so we've opted to\x01",
            "bring the lessons to them instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sister Hatina has been a great help in\x01",
            "holding Sunday School outside of the\x01",
            "Crossbell Cathedral.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6153")

    label("loc_60B7")


    ChrTalk(
        0xC,
        (
            "Sister Hatina is visiting the Downtown District\x01",
            "today on my behalf.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's a shame that children outside the city\x01",
            "hardly show up for Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6153")

    Jump("loc_642A")

    label("loc_6158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_62DC")
    OP_93(0xC, 0xB4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_625B")

    ChrTalk(
        0xC,
        (
            "The Great Collapse occurred a long, long\x01",
            "time ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It is what caused the destruction of\x01",
            "the continent we live on, Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It also annihilated the highly advanced\x01",
            "ancient Zemurian civilization along\x01",
            "with it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_62D7")

    label("loc_625B")


    ChrTalk(
        0xC,
        (
            "As the name implies, the Great Collapse laid\x01",
            "the continent of Zemuria to ruin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "*sigh* Are they even listening...?\x02",
    )

    CloseMessageWindow()

    label("loc_62D7")

    Jump("loc_642A")

    label("loc_62DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_642A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6396")

    ChrTalk(
        0xC,
        (
            "After all these years, I'm still working as\x01",
            "the teacher of Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you'd like, please feel free to drop by\x01",
            "to say hello from time to time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_642A")

    label("loc_6396")


    ChrTalk(
        0xC,
        (
            "The overwhelming cuteness of children\x01",
            "never fails to amaze me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you'd like, please feel free to drop by\x01",
            "to say hello from time to time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_642A")

    TalkEnd(0xC)
    Return()

    # Function_11_4D88 end

    def Function_12_642E(): pass

    label("Function_12_642E")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_93(0xC, 0xB4, 0x0)
    TurnDirection(0xF, 0xC, 0)
    TurnDirection(0x10, 0xC, 0)

    ChrTalk(
        0xF,
        "We're thinking of heading into the city later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I heard there are a lot of food stalls, so\x01",
            "my tummy's saying, 'Go!' You should\x01",
            "come, too, Sister!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, you're all so lucky. I wish I could...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'm afraid I'll be busy preparing Mass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Please enjoy yourselves in my stead!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Man, that stinks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Too bad...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x1, 1)
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_12_642E end

    def Function_13_65AB(): pass

    label("Function_13_65AB")

    EventBegin(0x0)
    Fade(500)
    OP_68(150650, 1700, 16780, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x101, 149440, 200, 17150, 90)
    SetChrPos(0x102, 149390, 200, 15890, 45)
    SetChrPos(0x103, 148500, 200, 17170, 90)
    SetChrPos(0x104, 149330, 200, 18150, 135)
    OP_93(0xC, 0xB4, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6749")
    OP_63(0xC, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_93(0xC, 0x10E, 0x1F4)
    Sleep(500)

    ChrTalk(
        0xC,
        "Oh...? Who might you be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F#5PSorry for barging in like this, ma'am. But\x01",
            "man, seeing this classroom again really\x01",
            "brings back memories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105F(Wait a second. I swear I've seen this\x01",
            "sister somewhere before...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67B9")

    label("loc_6749")


    ChrTalk(
        0x102,
        (
            "#0105F(Wait a second. I swear I've seen this\x01",
            "sister somewhere before...)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x10E, 0x1F4)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_67B9")


    ChrTalk(
        0xC,
        "Hold on. Are you, by any chance...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...Lloyd? Lloyd Bannings?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F#5PYou know me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FFriend of yours?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002F#5PW-Wait... Sister Marble?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "It's wonderful to see you again, Lloyd.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)

    ChrTalk(
        0xC,
        (
            "And the young lady next to you must\x01",
            "be Elie, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Look at you two, all grown up now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0109FI knew I recognized you! It really has\x01",
            "been a while, Sister Marble.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#0000F#11PHuh? You know her, too, Elie?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#0102FI do! Sister Marble was my teacher\x01",
            "when I attended Sunday School.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        (
            "#0205F#5PLloyd and Elie are close in age and even\x01",
            "took classes from the same sister...\x02\x03",
            "How could they not have known each other?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, Crossbell City is so large, each district\x01",
            "has its own Sunday School class on different\x01",
            "days of the week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "These two were in different classes, you see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FMakes sense to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FIt's sort of strange if you think about it...\x02\x03",
            "#0102FWe could've been childhood friends, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0009F#11PHaha, I wish!\x02",
    )

    CloseMessageWindow()

    def lambda_6BAC():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BAC)
    Sleep(50)

    def lambda_6BBC():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BBC)

    def lambda_6BC9():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6BC9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x101,
        (
            "#0002F#5PSo, Sister Marble, how'd you manage to\x01",
            "recognize us after all these years?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Are you implying that I would forget the\x01",
            "faces of two of my beloved students?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Besides, the two of you in particular\x01",
            "were always unique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0205F#5PHow so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well, let's see here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Poor Lloyd was spoiled beyond belief\x01",
            "and always clung to Cecile...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And little Elie was particularly well versed\x01",
            "in topics related to the birds and the bees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011F#5PC-Come again?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0112FS-Sister Marble!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FHaha! I really appreciate this HIGHLY\x01",
            "educational history lesson, teacher.\x02\x03",
            "#0309FYou got any other interestin' chapters in\x01",
            "these kiddos' lives we should know about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, I know plenty. Let's see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012F#5PC-C'mon, give us a break!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0113FWe were young, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'm just teasing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0206F#5PWhat a shame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Anyway, I'm so happy to see both of you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please, drop by whenever you want. I can brew\x01",
            "some tea, and we can reminisce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002F#5PYou can count on it!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 149440, 200, 17150, 90)
    SetScenarioFlags(0x8C, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FFB")
    SetScenarioFlags(0x0, 4)

    label("loc_6FFB")

    EventEnd(0x5)
    Return()

    # Function_13_65AB end

    def Function_14_6FFE(): pass

    label("Function_14_6FFE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7092")
    Jump("loc_70DC")

    label("loc_7092")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70B2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70DC")

    label("loc_70B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70D2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70DC")

    label("loc_70D2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70DC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7190")

    ChrTalk(
        0xFE,
        (
            "That lady visits the church quite\x01",
            "often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She understands how important piousness\x01",
            "is, and I want to follow her example.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF2")

    label("loc_7190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7202")

    ChrTalk(
        0xFE,
        (
            "Huh. This is the first time I've seen someone\x01",
            "from the Guardian Force actually come to church.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF2")

    label("loc_7202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_72B4")

    ChrTalk(
        0xFE,
        (
            "Those mafia lunatics! How dare they\x01",
            "fire off their guns in the city?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Aidios... Please protect us hardworking\x01",
            "citizens from their horrible schemes...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF2")

    label("loc_72B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7398")

    ChrTalk(
        0xFE,
        (
            "I think the centerpiece of my next trade deal\x01",
            "should be that septium I got in Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though, I admit it's a little intimidating to\x01",
            "sell things I'm unfamiliar with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I'm sure Aidios has my back.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CF2")

    label("loc_7398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_7410")

    ChrTalk(
        0xFE,
        (
            "Oh, Aidios... Please watch over your\x01",
            "humble servant during next year's\x01",
            "Anniversary Festival as well!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF2")

    label("loc_7410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_750A")

    ChrTalk(
        0xFE,
        (
            "I amassed quite the fortune during this year's\x01",
            "festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I can attribute that to the insane amount\x01",
            "of tourists that poured into Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then again, zealously praying to Aidios might\x01",
            "have made a difference as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF2")

    label("loc_750A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_75DF")

    ChrTalk(
        0xFE,
        (
            "Today's the final day... With so many tourists\x01",
            "heading to Mishelam, I should probably join\x01",
            "them and try to strike a few good deals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, dear Aidios...\x01",
            "Grant me more business opportunities!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF2")

    label("loc_75DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_767F")

    ChrTalk(
        0xFE,
        (
            "Dear Aidios, this year has been nothing\x01",
            "short of amazing. My stock has been\x01",
            "selling like hotcakes, thanks to you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thank you, thank you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CF2")

    label("loc_767F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_76F1")

    ChrTalk(
        0xFE,
        (
            "Yesterday's sales were pretty good,\x01",
            "too, Aidios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, keep blessing me with this luck!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CF2")

    label("loc_76F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_78D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7853")

    ChrTalk(
        0xFE,
        (
            "I'm incredibly busy with work, but I'm still\x01",
            "going to attend Mass during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's because, well...the countless prayers\x01",
            "I've offered to our loving Goddess over the\x01",
            "years have shaped me into the man I am today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By regularly giving Aidios my praise, I'm hoping\x01",
            "to show how much I truly appreciate Her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_78D1")

    label("loc_7853")


    ChrTalk(
        0xFE,
        "Aidios made me the man I am today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Consistently going to Mass is the least\x01",
            "I can do to express my gratitude, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78D1")

    Jump("loc_7CF2")

    label("loc_78D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7A35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79CE")

    ChrTalk(
        0xFE,
        (
            "Looks like the long-awaited Anniversary\x01",
            "Festival arrives next month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's gonna be crunch time for us merchants.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray to Aidios, asking that my business gets\x01",
            "the opportunity to prosper again this year.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7A30")

    label("loc_79CE")


    ChrTalk(
        0xFE,
        (
            "Oh, Goddess of the Sky... Bestow upon me your\x01",
            "divine protection during this year's festival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A30")

    Jump("loc_7CF2")

    label("loc_7A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B20")

    ChrTalk(
        0xFE,
        (
            "Haha. There's never a dull moment with all\x01",
            "these kids running around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Honestly, kids used to bug me to no end...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but, thanks to my prayers, I think Aidios\x01",
            "has made my heart grow a few rege.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7BB0")

    label("loc_7B20")


    ChrTalk(
        0xFE,
        (
            "By offering up my prayers, Aidios has shaped\x01",
            "me into a kinder, gentler man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm so, so grateful for Her and this cathedral.\x01",
            "Hahaha...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BB0")

    Jump("loc_7CF2")

    label("loc_7BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7CF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CA8")

    ChrTalk(
        0xFE,
        (
            "Immediately after I started praying here, my\x01",
            "business dealings began to flourish. Now,\x01",
            "who said a merchant can't be pious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, ever since then, I've been coming\x01",
            "here to offer my prayers to the Goddess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7CF2")

    label("loc_7CA8")


    ChrTalk(
        0xFE,
        (
            "Oh, Aidios... Give me the wit I need to make\x01",
            "this next deal go well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CF2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_6FFE end

    def Function_15_7CFA(): pass

    label("Function_15_7CFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7DE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D18")
    Call(0, 6)
    Jump("loc_7DE3")

    label("loc_7D18")


    ChrTalk(
        0xE,
        (
            "#0502FHello, everyone.\x02\x03",
            "#0504FI just handed Archbishop Eralda the report\x01",
            "on our big investigation of the Moon Temple.\x02\x03",
            "#0508FI'm happy with it, but I wish we could've made\x01",
            "a little more progress...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DE3")

    TalkEnd(0xFE)
    Return()

    # Function_15_7CFA end

    def Function_16_7DE7(): pass

    label("Function_16_7DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7DF5")
    Jump("loc_8282")

    label("loc_7DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7E03")
    Jump("loc_8282")

    label("loc_7E03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7E11")
    Jump("loc_8282")

    label("loc_7E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7E1F")
    Jump("loc_8282")

    label("loc_7E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8027")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7EBC")
    Jump("loc_7F06")

    label("loc_7EBC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7EDC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F06")

    label("loc_7EDC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EFC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F06")

    label("loc_7EFC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F06")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7FB6")

    ChrTalk(
        0xFE,
        (
            "Tsk. I hoped we didn't have to go back\x01",
            "to the normal lessons after this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sister Marble doesn't miss a beat.\x02",
    )

    CloseMessageWindow()
    Jump("loc_801B")

    label("loc_7FB6")


    ChrTalk(
        0xFE,
        (
            "Phew... I totally forgot that we had\x01",
            "Sunday School today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Geez. I just wanna play outside.\x02",
    )

    CloseMessageWindow()

    label("loc_801B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_8282")

    label("loc_8027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8035")
    Jump("loc_8282")

    label("loc_8035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_80DA")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8053")
    Call(0, 12)
    Jump("loc_80D2")

    label("loc_8053")


    ChrTalk(
        0xFE,
        (
            "I would have much rather given her\x01",
            "a grand tour of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Every day is a drag now, since I'm\x01",
            "always with Hamil...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80D2")

    TalkEnd(0xFE)
    Jump("loc_8282")

    label("loc_80DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_80E8")
    Jump("loc_8282")

    label("loc_80E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_80F6")
    Jump("loc_8282")

    label("loc_80F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8104")
    Jump("loc_8282")

    label("loc_8104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8279")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81A1")
    Jump("loc_81EB")

    label("loc_81A1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_81C1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_81EB")

    label("loc_81C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81E1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_81EB")

    label("loc_81E1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_81EB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8222")
    Call(0, 18)
    Jump("loc_826D")

    label("loc_8222")


    ChrTalk(
        0xFE,
        (
            "Ugh. Hamil's so full of himself just\x01",
            "because he's better at studying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_826D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_8282")

    label("loc_8279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8282")

    label("loc_8282")

    Return()

    # Function_16_7DE7 end

    def Function_17_8283(): pass

    label("Function_17_8283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8291")
    Jump("loc_8838")

    label("loc_8291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_829F")
    Jump("loc_8838")

    label("loc_829F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_82AD")
    Jump("loc_8838")

    label("loc_82AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_82BB")
    Jump("loc_8838")

    label("loc_82BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8538")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8358")
    Jump("loc_83A2")

    label("loc_8358")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8378")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_83A2")

    label("loc_8378")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8398")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_83A2")

    label("loc_8398")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_83A2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_846D")

    ChrTalk(
        0xFE,
        (
            "What was up with Tamil earlier...?\x01",
            "His enthusiasm is kinda scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Always know right from wrong! If you don't,\x01",
            "you're gonna be in a pickle!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_852C")

    label("loc_846D")

    SetChrSubChip(0xFE, 0x2)

    ChrTalk(
        0xFE,
        (
            "Hasn't Tamil been strangely happy for a\x01",
            "while now? Tell me I'm not crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's important to know what's right\x01",
            "and what's wrong. At least, that's\x01",
            "what Sister Marble always says!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_852C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_8838")

    label("loc_8538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8546")
    Jump("loc_8838")

    label("loc_8546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_863F")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8564")
    Call(0, 12)
    Jump("loc_8637")

    label("loc_8564")


    ChrTalk(
        0xFE,
        (
            "I really wanted to check out the food stalls\x01",
            "with our teacher, Sister Marble. It stinks that\x01",
            "she's busy with cathedral stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I got the chance, I was going to treat her\x01",
            "to some delicious ice cream.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8637")

    TalkEnd(0xFE)
    Jump("loc_8838")

    label("loc_863F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_864D")
    Jump("loc_8838")

    label("loc_864D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_865B")
    Jump("loc_8838")

    label("loc_865B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8669")
    Jump("loc_8838")

    label("loc_8669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_882F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_868A")
    TalkBegin(0xFE)
    Call(0, 18)
    TalkEnd(0xFE)
    Jump("loc_882A")

    label("loc_868A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_871E")
    Jump("loc_8768")

    label("loc_871E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_873E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8768")

    label("loc_873E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_875E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8768")

    label("loc_875E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8768")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "My twin brother Tamil isn't that great\x01",
            "when it comes to studying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guess this goes to show that being\x01",
            "athletic isn't everything, huh, Tamil?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_882A")

    Jump("loc_8838")

    label("loc_882F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8838")

    label("loc_8838")

    Return()

    # Function_17_8283 end

    def Function_18_8839(): pass

    label("Function_18_8839")

    OP_52(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x10, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_88CD")
    Jump("loc_8917")

    label("loc_88CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_88ED")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8917")

    label("loc_88ED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_890D")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8917")

    label("loc_890D")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8917")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        (
            "Hey, Hamil. Were you able to follow\x01",
            "what Sister Marble just said?\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x10)
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0xF, 0)
    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8A17")
    Jump("loc_8A61")

    label("loc_8A17")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8A37")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8A61")

    label("loc_8A37")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A57")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8A61")

    label("loc_8A57")

    OP_52(0x10, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8A61")

    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x10)

    ChrTalk(
        0x10,
        (
            "Uh...were you even listening? It wasn't\x01",
            "even that hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "O-Oh, really? Uh, just show me your\x01",
            "notes when we get home later.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_18_8839 end

    def Function_19_8B16(): pass

    label("Function_19_8B16")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BAA")
    Jump("loc_8BF4")

    label("loc_8BAA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8BCA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8BF4")

    label("loc_8BCA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BEA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8BF4")

    label("loc_8BEA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8BF4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8CF8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C7E")

    ChrTalk(
        0xFE,
        (
            "Today's class was sorta hard, but still\x01",
            "pretty fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Um...thanks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CF3")

    label("loc_8C7E")


    ChrTalk(
        0xFE,
        (
            "Being able to study with Ryu and Anri\x01",
            "makes me super happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what today's lesson will be about...?\x02",
    )

    CloseMessageWindow()

    label("loc_8CF3")

    Jump("loc_8D62")

    label("loc_8CF8")


    ChrTalk(
        0xFE,
        "Wait...the Great Collapse actually happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I don't wanna think about scary stuff like that...\x02",
    )

    CloseMessageWindow()

    label("loc_8D62")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_8B16 end

    def Function_20_8D6A(): pass

    label("Function_20_8D6A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8DFE")
    Jump("loc_8E48")

    label("loc_8DFE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8E1E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E48")

    label("loc_8E1E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E3E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E48")

    label("loc_8E3E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8E48")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F42")

    ChrTalk(
        0xFE,
        (
            "My papa loves to talk about old stuff like\x01",
            "the ancient Zemurian civilization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did Ryu and Anri end up forgetting about\x01",
            "class today...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I even told them we had Sunday School today!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8F8B")

    label("loc_8F42")


    ChrTalk(
        0xFE,
        (
            "Well...it's not like I'm their mommy. I'll just\x01",
            "study without them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F8B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_8D6A end

    def Function_21_8F93(): pass

    label("Function_21_8F93")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9027")
    Jump("loc_9071")

    label("loc_9027")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9047")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9071")

    label("loc_9047")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9067")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9071")

    label("loc_9067")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9071")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "If orbal technology continues to develop at the\x01",
            "rate it has so far, I wonder if things will become\x01",
            "even MORE convenient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like, what if we were able to do all our grocery\x01",
            "shopping from home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wait, I don't want that! All my rewards for going\x01",
            "on errands would disappear!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_8F93 end

    def Function_22_91B9(): pass

    label("Function_22_91B9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_924D")
    Jump("loc_9297")

    label("loc_924D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_926D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9297")

    label("loc_926D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_928D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9297")

    label("loc_928D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9297")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "You can get your very own Epstein orbment\x01",
            "when you join the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maaan. Wouldn't it be sweet if I could cast a\x01",
            "bunch of super cool arts one day, too?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_91B9 end

    def Function_23_936D(): pass

    label("Function_23_936D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9401")
    Jump("loc_944B")

    label("loc_9401")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9421")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_944B")

    label("loc_9421")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9441")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_944B")

    label("loc_9441")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_944B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_947E")
    Jump("loc_957C")

    label("loc_947E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9515")

    ChrTalk(
        0xFE,
        (
            "To be honest, I didn't know a lot about the\x01",
            "CPD, so today's class was really cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come be our teacher again someday, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_957C")

    label("loc_9515")


    ChrTalk(
        0xFE,
        "You're KeA, right? From earlier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Are you going to join our class?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1106FUhhh, maybe...?\x02",
    )

    CloseMessageWindow()

    label("loc_957C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_936D end

    def Function_24_9584(): pass

    label("Function_24_9584")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9618")
    Jump("loc_9662")

    label("loc_9618")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9638")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9662")

    label("loc_9638")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9658")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9662")

    label("loc_9658")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9662")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "The Epstein Foundation was established with\x01",
            "the enormous inheritance Professor C. Epstein\x01",
            "left behind after passing away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what kind of person he really was?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_9584 end

    def Function_25_9741(): pass

    label("Function_25_9741")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_97D5")
    Jump("loc_981F")

    label("loc_97D5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_97F5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_981F")

    label("loc_97F5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9815")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_981F")

    label("loc_9815")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_981F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9915")

    ChrTalk(
        0xFE,
        (
            "This is so elementary, it just makes me laugh.\x01",
            "This material would only pose a challenge to\x01",
            "those lacking common sense!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wow. Don't you know it's, like, super rude to\x01",
            "talk in class?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9934")

    label("loc_9915")


    ChrTalk(
        0xFE,
        "Quiet down! I'm studying!\x02",
    )

    CloseMessageWindow()

    label("loc_9934")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_9741 end

    def Function_26_993C(): pass

    label("Function_26_993C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99D0")
    Jump("loc_9A1A")

    label("loc_99D0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_99F0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A1A")

    label("loc_99F0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A10")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A1A")

    label("loc_9A10")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A1A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Wouldn't we be able to protect ourselves\x01",
            "against a disaster like that with modern\x01",
            "technology?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_993C end

    def Function_27_9AAA(): pass

    label("Function_27_9AAA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B3E")
    Jump("loc_9B88")

    label("loc_9B3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9B5E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9B88")

    label("loc_9B5E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B7E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9B88")

    label("loc_9B7E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9B88")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Eeeeek! Don't read my notebook!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_9AAA end

    def Function_28_9BDA(): pass

    label("Function_28_9BDA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C6E")
    Jump("loc_9CB8")

    label("loc_9C6E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9C8E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9CB8")

    label("loc_9C8E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CAE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9CB8")

    label("loc_9CAE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9CB8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "*yawn* Studying just makes me sleepy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And there's the death stare from the\x01",
            "teacher. Gotta...hold...out...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_28_9BDA end

    def Function_29_9D59(): pass

    label("Function_29_9D59")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9DED")
    Jump("loc_9E37")

    label("loc_9DED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9E0D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E37")

    label("loc_9E0D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E2D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E37")

    label("loc_9E2D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9E37")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "My mom always tells me I should study\x01",
            "hard for the sake of my future, whatever\x01",
            "that means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did you have to study a lot, too?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_9D59 end

    def Function_30_9EEB(): pass

    label("Function_30_9EEB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F7F")
    Jump("loc_9FC9")

    label("loc_9F7F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9F9F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9FC9")

    label("loc_9F9F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9FBF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9FC9")

    label("loc_9FBF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9FC9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 7)), scpexpr(EXPR_END)), "loc_A1FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_A0B9")

    ChrTalk(
        0x1D,
        (
            "#3600FI try to attend Mass as much as possible,\x01",
            "but my work often prevents me from coming.\x02\x03",
            "#3603FPutting all these burdens on my wife...\x01",
            "I can really be a worthless husband.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1FA")

    label("loc_A0B9")


    ChrTalk(
        0x1D,
        (
            "#3600FMy wife has made it a habit to come to\x01",
            "Mass at least once a week.\x02\x03",
            "#3603FI try to attend Mass as much as possible,\x01",
            "but my work often prevents me from going.\x02\x03",
            "#3600F*sigh* I hate making my wife shoulder\x01",
            "the burden alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(He seems really torn up. Did he come to\x01",
            "pray for something in particular?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_A1FA")

    Jump("loc_A580")

    label("loc_A1FF")


    ChrTalk(
        0x1D,
        (
            "#3605FAh, the SSS.\x02\x03",
            "#3609FI wasn't expecting to run into you here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FIt's nice to see you again, Mr. Hayworth.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FAre you here to pray, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#3600FIndeed I am. My wife has made it a habit\x01",
            "of hers to come pray whenever she can.\x02\x03",
            "#3609FI usually have to play hooky, but I decided\x01",
            "to make an effort to join her more often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309FAlways the family man, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FIt is impressive how faithful you are despite\x01",
            "your busy schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#3609FHaha, I wouldn't put it like that...\x02\x03",
            "#3608F...\x02",
        )
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
        0x1D,
        (
            "#3603F...I'm sorry; it's nothing.\x02\x03",
            "#3600FIt's not like I consider myself an overly\x01",
            "pious man to begin with.\x02\x03",
            "I simply heard that praying can help\x01",
            "in business endeavors, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FFor real? THAT'S why you're here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#3609FAhahaha... Sorry to disappoint.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 7)

    label("loc_A580")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_9EEB end

    def Function_31_A588(): pass

    label("Function_31_A588")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A61C")
    Jump("loc_A666")

    label("loc_A61C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A63C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A666")

    label("loc_A63C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A65C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A666")

    label("loc_A65C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A666")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0x1E, 0x0)

    ChrTalk(
        0x1E,
        "#3700FThank you once again, kind Father.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_A588 end

    def Function_32_A6C5(): pass

    label("Function_32_A6C5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A759")
    Jump("loc_A7A3")

    label("loc_A759")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A779")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A7A3")

    label("loc_A779")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A799")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A7A3")

    label("loc_A799")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A7A3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_A83C")

    ChrTalk(
        0x1F,
        (
            "#3809FPraaaying, praaaying...! Praaaying is fun!\x02\x03",
            "Coming here with Papa and Mama\x01",
            "is the funnest!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8DB")

    label("loc_A83C")


    ChrTalk(
        0x1F,
        (
            "#3800FToday's praying-with-mama day.\x02\x03",
            "But get this! Papa was able to come\x01",
            "today, too!\x02\x03",
            "#3809FPapa always says he's too busy, so\x01",
            "today's extra special!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_A8DB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_A6C5 end

    def Function_33_A8E3(): pass

    label("Function_33_A8E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB92")

    ChrTalk(
        0x102,
        "#0105FOh, aren't you Cecile's mother?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, aren't you all a sight for sore eyes?\x01",
            "Did you stop by to pray a bit?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 500)

    ChrTalk(
        0xFE,
        "Did something happen, Lloyd?\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FHuh? What do you mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Don't mind me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You really are the spitting image of Guy, aren't you?\x01",
            "Truth be told, I would probably mistake you for him\x01",
            "if I ran into you at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011FY-You think so? Well, I suppose we are brothers...\x01",
            "(I'm starting to look like Guy did?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, would you like to pray together\x01",
            "sometime, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, this is Guy's resting place,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_AC7D")

    label("loc_AB92")


    ChrTalk(
        0xFE,
        (
            "You really have taken after Guy,\x01",
            "haven't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure you'll become a fine detective.\x01",
            "Maybe an even finer one than Guy someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be rooting for you. Don't let anyone hold you\x01",
            "back or stand in your way, you hear me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC7D")

    TalkEnd(0xFE)
    Return()

    # Function_33_A8E3 end

    def Function_34_AC81(): pass

    label("Function_34_AC81")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AD15")
    Jump("loc_AD5F")

    label("loc_AD15")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AD35")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AD5F")

    label("loc_AD35")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD55")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AD5F")

    label("loc_AD55")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AD5F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AE03")

    ChrTalk(
        0xFE,
        "Your lesson wasn't too shabby.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll make sure to stop by the SSS\x01",
            "whenever I feel like petting Zeit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE6E")

    label("loc_AE03")


    ChrTalk(
        0xFE,
        "Bleh. Studying is such a drag.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well...at least Sister Marble's lessons are\x01",
            "somewhat interesting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE6E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_AC81 end

    def Function_35_AE76(): pass

    label("Function_35_AE76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF2B")

    ChrTalk(
        0xFE,
        "I'm here praying for a safe trip.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd be devastated if something happened\x01",
            "to me now, ruining my big vacation. Aidios,\x01",
            "give me a hand here, all right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_AFCE")

    label("loc_AF2B")


    ChrTalk(
        0xFE,
        (
            "If my entire vacation was ruined because\x01",
            "I tripped and hurt myself or something,\x01",
            "I don't think I'd ever recover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe one more prayer, just to be safe.\x02",
    )

    CloseMessageWindow()

    label("loc_AFCE")

    TalkEnd(0xFE)
    Return()

    # Function_35_AE76 end

    def Function_36_AFD2(): pass

    label("Function_36_AFD2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(151810, 1500, 11060, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(31350, 0)
    SetChrPos(0x101, 148350, 0, 3500, 0)
    SetChrPos(0x102, 146900, 0, 3750, 0)
    SetChrPos(0x103, 148350, 0, 1920, 0)
    SetChrPos(0x104, 146900, 0, 2250, 0)
    OP_4B(0xC, 0xFF)
    OP_68(151810, 1500, 13060, 5000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "Long ago, the Great Collapse shook the world\x01",
            "to its core, irrefutably changing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It caused the utter destruction of the very\x01",
            "continent we call home, Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Concurrently, it annihilated the ancient civilization that\x01",
            "inhabited this land, alongside their advanced technology,\x01",
            "which is said to have been even greater than our own.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(147550, 1500, 2910, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#0100FLooks like they're in the middle of a Sunday School\x01",
            "lesson right now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_END)), "loc_B2B8")

    ChrTalk(
        0x101,
        (
            "#0000FThis really brings me back. I think I see\x01",
            "some familiar faces in the class, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B36B")

    label("loc_B2B8")


    ChrTalk(
        0x101,
        (
            "#0000FThis really brings me back. I think I see\x01",
            "some familiar faces in the class, too.\x02\x03",
            "#0005F(Speaking of which, is that teacher who\x01",
            "I think it is? It couldn't possibly...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B36B")

    SetChrPos(0x0, 147550, 0, 2900, 0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x86, 4)
    EventEnd(0x5)
    Return()

    # Function_36_AFD2 end

    def Function_37_B386(): pass

    label("Function_37_B386")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(151810, 1500, 11060, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(31350, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B439")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B3F5")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x109, 149460, 0, 1750, 0)

    label("loc_B3F5")

    SetChrPos(0x101, 148350, 0, 3500, 0)
    SetChrPos(0x102, 146900, 0, 3750, 0)
    SetChrPos(0x103, 148350, 0, 1920, 0)
    SetChrPos(0x104, 146900, 0, 2250, 0)

    label("loc_B439")

    OP_4B(0xC, 0xFF)
    OP_68(151810, 1500, 13060, 5000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "Half a century ago, a professor named\x01",
            "C. Epstein brought about the so-called\x01",
            "Orbal Revolution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Orbal technology met plenty of resistance\x01",
            "at first, but fast-forward 50 years and we're\x01",
            "surrounded by orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Convenient innovations such as orbal cars\x01",
            "crop up one after the other these days.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B67B")
    Fade(500)
    OP_68(147550, 1500, 2910, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#0100FLooks like they're in the middle of a Sunday School\x01",
            "lesson right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThis really brings me back. I think I see\x01",
            "some familiar faces in the class, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B67B")

    SetChrPos(0x0, 147550, 0, 2900, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6A6")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_B6A6")

    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x86, 5)
    EventEnd(0x5)
    Return()

    # Function_37_B386 end

    def Function_38_B6B0(): pass

    label("Function_38_B6B0")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("apl/ch50381.itc", 0x1E)
    LoadEffect(0x0, "event\\ev400_00.eff")
    LoadEffect(0x1, "event\\ev401_00.eff")
    SoundLoad(840)
    OP_4B(0xC, 0xFF)
    SetChrPos(0xC, 148920, 0, 13890, 90)
    SetChrPos(0x101, 150330, 0, 14130, 270)
    SetChrPos(0x153, 151460, 0, 13520, 270)
    SetChrPos(0xEF, 150640, 0, 12780, 315)
    FadeToBright(1000, 0)
    OP_68(150000, 1100, 14000, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24000, 0)
    OP_0D()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_B84D")

    ChrTalk(
        0xC,
        "#3600491V#5POh? How nice of you two to stop by.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600495V#0002F#11PGood morning, Sister Marble.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3600493V#0102F#6PForgive us for intruding at\x01",
            "such an inconvenient time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8E9")

    label("loc_B84D")


    ChrTalk(
        0xC,
        "#3600494V#5POh? How nice of you to stop by, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600492V#0002F#11PGood morning, Sister Marble.\x02\x03",
            "#3600496VSorry if I'm being an inconvenience.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8E9")


    ChrTalk(
        0xC,
        (
            "#3600497V#5PPlease, don't think anything of it. I was\x01",
            "actually just about to begin my break.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB34")
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#3600498V#5POh, that's right. You two are coworkers\x01",
            "now! Funny how things turn out like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600499V#5PI can honestly say that it moves me to\x01",
            "see you two standing side-by-side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600500V#0012F#11PO-Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3600501V#0112F#6PI-Is it really that big a deal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600502V#5PI'll leave that to your imagination.\x01",
            "So, is something the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600503V#5PAre you simply here to worship?\x01",
            "Or are you visiting the cemetery?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB8B")

    label("loc_BB34")


    ChrTalk(
        0xC,
        (
            "#3600504V#5PAre you two simply here to worship?\x01",
            "Or are you visiting the cemetery?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB8B")


    ChrTalk(
        0x101,
        "#3600505V#0008F#11PWell, about that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600506V#1100F#12PHey, Lloyd, I got a question!\x02\x03",
            "#3600507VIs this one of those sister people?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#3600508V#5POh, my. Now who is this little one?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600509V#0003F#11POur reason for coming, actually.\x02\x03",
            "#3600510V#0001FThere's something in particular we\x01",
            "wanted to ask you about her.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(23000, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_68(151000, 1100, 12500, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0xC, 151000, 0, 13800, 180)
    SetChrPos(0x153, 151000, 0, 12000, 0)
    SetChrPos(0x101, 151500, 0, 10800, 0)
    SetChrPos(0xEF, 150500, 0, 10800, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#3600511V#11PAh, so that's why she's been hiding\x01",
            "behind you all this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600512V#11POh, dearest Aidios, please shine thy\x01",
            "light and happiness on this lost lamb.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600513V#11PFurthermore, I thank you for having\x01",
            "guided her to these kind individuals...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600514V#0000F#6PThat means a lot, Sister Marble.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_BF2E")

    ChrTalk(
        0x102,
        (
            "#3600515V#0104F#6PMaybe Aidios really did have a hand\x01",
            "in leading KeA into our arms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFE7")

    label("loc_BF2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_BF84")

    ChrTalk(
        0x103,
        (
            "#3600516V#0204F#6PPerhaps it really was Aidios that led\x01",
            "KeA to us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFE7")

    label("loc_BF84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_BFE7")

    ChrTalk(
        0x104,
        (
            "#3600517V#0304F#6PMaybe our good Goddess really was\x01",
            "the one that led KeDo to us, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFE7")


    ChrTalk(
        0x153,
        "#3600518V#1105F#6PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600519V#11PAnyway, you've come to inquire whether\x01",
            "or not I know anything about her memory\x01",
            "loss, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600520V#11PI understand that she doesn't remember\x01",
            "anything aside from her name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600521V#0006F#6PYeah. We'd love any advice you might have.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600522V#1106F#6PUm, I really did try my best to remember,\x01",
            "but it didn't work. I even closed my eyes\x01",
            "and focused super hard!\x02\x03",
            "#3600523V#1108FDid I do it wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600524V#11PYou're a good girl, aren't you, KeA?\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "#3600525V#11PKnowledge and techniques involving tapping\x01",
            "into one's spirit and mind are handed down in\x01",
            "the Septian Church. That much is true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600526V#11PAmong them are treatments for amnesia.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3600527V#0002F#6PThen there's hope!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_C386")

    ChrTalk(
        0x102,
        (
            "#3600528V#0100F#6PYou think it's possible to restore\x01",
            "her memories?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C451")

    label("loc_C386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_C3E9")

    ChrTalk(
        0x103,
        (
            "#3600529V#0202F#6PSo there is a possibility that her\x01",
            "memories can be restored?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C451")

    label("loc_C3E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_C451")

    ChrTalk(
        0x104,
        (
            "#3600530V#0300F#6PYou think the church can work their\x01",
            "magic and bring back her memories?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C451")


    ChrTalk(
        0xC,
        (
            "#3600531V#11PWell, I'm not positive that I will be able\x01",
            "to restore them in full, but it's surely\x01",
            "worth trying, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600532V#11PTime is of the essence. Shall I begin?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3600533V#0005F#6PWait, are you saying you're going to\x01",
            "be the one doing it, Sister Marble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600534V#11PWell, yes. I've built up mastery in a few\x01",
            "of these techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600535V#11PI've also dabbled in Thaumaturgy: the\x01",
            "church's secret techniques pertaining\x01",
            "to the mind and spirit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600536V#0001F#6PThaumaturgy?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_C6FC")

    ChrTalk(
        0x102,
        (
            "#3600537V#0101F#6PI believe they primarily incorporate prayer and\x01",
            "sacraments passed down by the clergy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C8")

    label("loc_C6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_C765")

    ChrTalk(
        0x103,
        (
            "#3600538V#0201F#6PSo instead of relying on orbments, this\x01",
            "uses the power of prayer...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C8")

    label("loc_C765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_C7C8")

    ChrTalk(
        0x104,
        (
            "#3600539V#0301F#6POh, you're talkin' about that prayer stuff\x01",
            "the clergy uses, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7C8")


    ChrTalk(
        0xC,
        (
            "#3600540V#11PEssentially. There is an organization within\x01",
            "the church that specializes in Thaumaturgy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600541V#11P...but those specialists rarely come to\x01",
            "Crossbell, unfortunately.\x02",
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
        "#3600542V#0005F#6PSeriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600543V#11PI'm not supposed to let this out, but the church\x01",
            "is not entirely a uniform institution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600544V#11POne organization that resides within the Congregation\x01",
            "for the Sacraments, another branch of the church, is\x01",
            "known for their expertise in Thaumaturgy, but you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600545V#11P...the man in charge of the Crossbell Cathedral,\x01",
            "Archbishop Eralda, does not think too kindly of\x01",
            "their inner activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600546V#11PBecause of that, members of the Congregation for\x01",
            "the Sacraments rarely find themselves in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600547V#0006F#6PW-Wow. I never thought that the Septian Church\x01",
            "would have their share of internal disputes.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_CD22")

    ChrTalk(
        0x102,
        (
            "#3600548V#0103F#6PYou said that group is affiliated with the\x01",
            "Congregation for the Sacraments? So\x01",
            "you're talking about the Gralsritter?\x02\x03",
            "#3600549V#0108FI've heard that Archbishop Eralda holds a\x01",
            "lot of pull within the Congregation for Divine\x01",
            "Worship, but I never knew about this divide...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600550V#11PI see you're well versed in knowledge of the\x01",
            "Septian Church, Elie. I suppose I shouldn't\x01",
            "be too surprised.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE95")

    label("loc_CD22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_CDF2")

    ChrTalk(
        0x103,
        (
            "#3600551V#0201F#6PSo what you are trying to say is that there is\x01",
            "a sort of power struggle going on within the\x01",
            "Septian Church?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600554V#11PI'm afraid so. It's all rather embarrassing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE95")

    label("loc_CDF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_CE95")

    ChrTalk(
        0x104,
        (
            "#3600553V#0301F#6PSo, basically, the church is smack dab\x01",
            "in the middle of a turf war?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600552V#11PI'm afraid so. It's all rather embarrassing.\x02",
    )

    CloseMessageWindow()

    label("loc_CE95")


    ChrTalk(
        0xC,
        (
            "#3600555V#11PThat being said, there's no difference between\x01",
            "their Thaumaturgy and mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600556V#11PI believe it's worth the try.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600557V#0000F#6PAll right, then. We'll leave\x01",
            "you to it, Sister Marble.\x02\x03",
            "#3600558V#0005FEr, do we need to go\x01",
            "somewhere else for this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600559V#11PNo need.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600560V#11PYour name is KeA, correct? Do you\x01",
            "mind coming a bit closer to me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600561V#1109F#6PNo problem!\x02",
    )

    CloseMessageWindow()
    OP_68(151110, 1100, 12960, 1000)

    def lambda_D056():
        OP_9B(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_D056)
    WaitChrThread(0x153, 1)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#3600562V#11PNow, I need you to close your eyes and\x01",
            "take sloooow, deep breaths. Can you do\x01",
            "that for me, little one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600563V#1110F#5PSure! I can do that easy peasy!\x02\x03",
            "#3600565V#1103F#40W*inhale*...*exhale*...\x02\x03",
            "#3600564V#40W*inhale*...*exhale*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600566V#11PThat's perfect, KeA. Keep it up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600567V#11PWell, then...\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    Fade(500)
    SetCameraDistance(23500, 0)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x10)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    Sound(882, 0, 100, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)

    ChrTalk(
        0xC,
        (
            "#3600568V#11P#40WIn the name of She Who Dwells Above do I hold\x01",
            "this consecrated septium.\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x0, 0x0, 0xC, 0x40, 200, 900, -450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(893, 0, 100, 0)
    Sound(840, 2, 100, 0)
    SetCameraDistance(23000, 30000)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3600569V#0005F#6P(What the...?)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_D308")

    ChrTalk(
        0x102,
        "#3600570V#0105F#6P(So this is Thaumaturgy...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_D38D")

    label("loc_D308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_D34B")

    ChrTalk(
        0x103,
        "#3600571V#0201F#6P(This must be Thaumaturgy...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_D38D")

    label("loc_D34B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_D38D")

    ChrTalk(
        0x104,
        "#3600572V#0301F#6P(This is that Thaumaturgy stuff?)\x02",
    )

    CloseMessageWindow()

    label("loc_D38D")


    ChrTalk(
        0xC,
        "#3600573V#11P#40WSpace's golden glow... Consciousness' silver glow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600574V#11P#40WBy your opposing natures, lead this lamb to her lost\x01",
            "fragments' true whereabouts...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x1, 0x1, 0x153, 0x40, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(228, 0, 100, 0)
    Sleep(500)

    def lambda_D48A():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_D48A)
    Sleep(800)

    ChrTalk(
        0x153,
        "#3600575V#1105F#5PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600576V#0013F#6PKeA, what's wrong?!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x10)
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xC,
        "#3600577V#11PCalm yourself. There's no need to fret.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600578V#11PHow do you feel, KeA?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600579V#11PCan you remember anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600580V#1103F#5P#40WHmmm...\x02\x03",
            "#3600581V#40W...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x153)

    ChrTalk(
        0x153,
        (
            "#3600582V#1108F#5PAll I remember is a big, dark room...\x02\x03",
            "#3600583V#1112FA light shined down from above, but\x01",
            "it always made me a little scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600584V#0005F#6PA big, dark room...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_D6EA")

    ChrTalk(
        0x102,
        "#3600585V#0108F#6PWhere in the world could that be...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D771")

    label("loc_D6EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_D739")

    ChrTalk(
        0x103,
        "#3600586V#0208F#6PThat might prove difficult to pinpoint...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D771")

    label("loc_D739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_D771")

    ChrTalk(
        0x104,
        "#3600587V#0301F#6PNot very specific, huh?\x02",
    )

    CloseMessageWindow()

    label("loc_D771")


    ChrTalk(
        0xC,
        "#3600588V#11PAnything else come to mind, KeA?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600589V#11PPerhaps memories of your family, or\x01",
            "where you lived beforehand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600590V#1106F#5PUmm...nope. I got nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600591V#11PIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600592V#11P...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    StopBGM(0xFA0)
    BeginChrThread(0x22, 1, 0, 39)
    StopEffect(0x1, 0x2)
    Sleep(3000)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    EndChrThread(0x22, 0x1)

    ChrTalk(
        0x101,
        "#3600593V#0001F#6PWhat is it, Sister Marble?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7124", 0)
    OP_64(0xC)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#3600594V#11PSadly, this seems to be the best\x01",
            "result we'll get from Thaumaturgy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600595V#11PIn other words, focusing on the psychological\x01",
            "side of things will only get us this far...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600596V#11PIt's possible that the problem may\x01",
            "lie with her nervous system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600597V#0005F#6PNo way...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_DA36")

    ChrTalk(
        0x102,
        "#3600598V#0101F#6PWh-Why is that?\x02",
    )

    CloseMessageWindow()
    Jump("loc_DABB")

    label("loc_DA36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_DA77")

    ChrTalk(
        0x103,
        "#3600599V#0201F#6PCould you expand upon that?\x02",
    )

    CloseMessageWindow()
    Jump("loc_DABB")

    label("loc_DA77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_DABB")

    ChrTalk(
        0x104,
        "#3600600V#0301F#6PWhat exactly are you tryin' to say?\x02",
    )

    CloseMessageWindow()

    label("loc_DABB")


    ChrTalk(
        0xC,
        (
            "#3600601V#11PTo be frank, I think there might be\x01",
            "some issue with her cranial nerves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600602V#11PTheir transmissions regarding memories\x01",
            "seem to be inhibited, for whatever reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600603V#11PThough, that's merely a possibility.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600604V#0011F#6PYou think there's something wrong\x01",
            "with her brain...?\x02\x03",
            "#3600605V#0007FThere's nothing else you can do?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600606V#11PI'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600607V#11PThaumaturgy strictly works within the\x01",
            "confines of one's spirit and mind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600608V#11PIt pains me to say that modern medicine\x01",
            "might be your best option in remedying\x01",
            "her condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600609V#0005F#6P...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_DD96")

    ChrTalk(
        0x102,
        (
            "#3600610V#0105F#6POnly one place comes to mind when you\x01",
            "say modern medicine...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE3D")

    label("loc_DD96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_DDF2")

    ChrTalk(
        0x103,
        (
            "#3600611V#0205F#6PIf we need information on treatments of\x01",
            "that nature...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE3D")

    label("loc_DDF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_DE3D")

    ChrTalk(
        0x104,
        "#3600612V#0305F#6PMedicine, eh? You must be talkin' about...\x02",
    )

    CloseMessageWindow()

    label("loc_DE3D")


    ChrTalk(
        0xC,
        "#3600613V#11PYes. St. Ursula Medical College.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600614V#11PDespite not much research being done\x01",
            "into the field of the spirit and mind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600615V#11P...a few years back, a new Neurology\x01",
            "Department was formed, and I hear\x01",
            "that an excellent researcher heads it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600616V#11PI'm sure a consultation there will open\x01",
            "many more doors for you to take than\x01",
            "continuing the church's methods would.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600617V#0000F#6PNeurology, you said?\x01",
            "(Hold on. Why does this sound so familiar?)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_E096")

    ChrTalk(
        0x102,
        (
            "#3600618V#0103F#6PListen, Lloyd...\x02\x03",
            "#3600619V#0101FWe should check into this, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1A9")

    label("loc_E096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_E12A")

    ChrTalk(
        0x103,
        (
            "#3600620V#0203F#6PExcuse me, Lloyd.\x02\x03",
            "#3600621V#0201FI believe that this might be our best\x01",
            "chance to help KeA. What do you think?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1A9")

    label("loc_E12A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_E1A9")

    ChrTalk(
        0x104,
        (
            "#3600622V#0303F#6PYo, man.\x02\x03",
            "#3600623V#0300FIt's soundin' like this is our best bet\x01",
            "for KeDo. Wanna check it out?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1A9")


    ChrTalk(
        0x101,
        (
            "#3600624V#0003F#6PYeah, I'm on the same page.\x02\x03",
            "#3600625V#0002FSister Marble, I can't thank you enough.\x02\x03",
            "#3600626VWe're going to take your advice and\x01",
            "head to St. Ursula right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3600627V#11PWonderful. I think that's for the best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600628V#11PI'm truly sorry I couldn't be more\x01",
            "help to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600629V#0005F#6PC-C'mon, Sister Marble. Without you,\x01",
            "we wouldn't have known to look into\x01",
            "this Neurology Department!\x02\x03",
            "#3600630V#0000FOn top of that, I think that bit of info\x01",
            "KeA remembered might end up being\x01",
            "a valuable clue down the line.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_E40E")

    ChrTalk(
        0x102,
        "#3600631V#0103F#6P'A big, dark room...'\x02",
    )

    CloseMessageWindow()
    Jump("loc_E47D")

    label("loc_E40E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_E449")

    ChrTalk(
        0x103,
        "#3600632V#0203F#6P'A big, dark room...'\x02",
    )

    CloseMessageWindow()
    Jump("loc_E47D")

    label("loc_E449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_E47D")

    ChrTalk(
        0x104,
        "#3600633V#0303F#6PBig, dark room, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_E47D")

    OP_93(0x153, 0xB4, 0x1F4)

    ChrTalk(
        0x153,
        (
            "#3600634V#1103F#11PYeah. But I also remember this light\x01",
            "shining down from above. It wasn't\x01",
            "very bright.\x02\x03",
            "#3600635V#1112FOh, I also remember hearing this really\x01",
            "deep sound there. It was kinda pretty,\x01",
            "but also a little spooky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600636V#0003F#6PTh-That right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600637V#11PWell, it's obvious that this place is\x01",
            "anything but ordinary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600638V#11PMay the Goddess bless you all with\x01",
            "luck and good fortune.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3600639V#11PI will be praying for KeA in the\x01",
            "meantime.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(23250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    SetChrPos(0x0, 150800, 0, 14000, 180)
    SetChrPos(0xC, 150800, 200, 17500, 180)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0xA8, 2)
    SetScenarioFlags(0x8C, 3)
    OP_29(0x48, 0x1, 0x5)
    OP_66(0x0, 0x1)
    OP_24(0x348)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_38_B6B0 end

    def Function_39_E6C0(): pass

    label("Function_39_E6C0")

    OP_25(0x348, 0x5A)
    Sleep(100)
    OP_25(0x348, 0x50)
    Sleep(100)
    OP_25(0x348, 0x46)
    Sleep(100)
    OP_25(0x348, 0x3C)
    Sleep(100)
    OP_25(0x348, 0x32)
    Sleep(100)
    OP_25(0x348, 0x28)
    Sleep(100)
    OP_25(0x348, 0x1E)
    Sleep(100)
    OP_25(0x348, 0x14)
    Sleep(100)
    OP_25(0x348, 0xA)
    Sleep(100)
    OP_24(0x348)
    Return()

    # Function_39_E6C0 end

    def Function_40_E703(): pass

    label("Function_40_E703")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(2780, 2290, 22200, 0)
    MoveCamera(319, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28080, 0)
    OP_93(0x8, 0x5A, 0x0)
    SetChrPos(0x101, 2500, 500, 22500, 270)
    SetChrPos(0x102, 2500, 500, 24000, 270)
    SetChrPos(0x103, 4000, 500, 22500, 270)
    SetChrPos(0x104, 4000, 500, 24000, 270)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#5PThank you for coming to the Crossbell Cathedral.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWhat nature of business do you have with me\x01",
            "today? Prayer, worship, guidance...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FArchbishop Eralda, correct?\x02\x03",
            "We're the Special Support Section, here\x01",
            "about one of our support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PAh. On duty, are we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FYes, sir. The request is from the doctor in charge\x01",
            "of the Internal Medicine Department at St. Ursula\x01",
            "Hospital: Doctor Lago.\x02\x03",
            "He contacted you about getting a sample\x01",
            "of Lupinus Grass, didn't he?\x02\x03",
            "#0103FConsidering how busy he is at St. Ursula,\x01",
            "he asked us to retrieve the herbs in his\x01",
            "stead, Archbishop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PWait a moment.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5PDoctor Lago, you said?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI indeed received a letter from him just\x01",
            "the other day, but this is the first I've\x01",
            "heard of such a request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0305FH-Huh? How does that make sense?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5POh, the explanation is quite simple.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI've made it my prerogative to ignore\x01",
            "every letter sent by this doctor of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FWh-What?!\x02\x03",
            "What could he have possibly done to deserve that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThat's no business of yours. Besides, I already swore\x01",
            "upon the Goddess to uphold this solemn vow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0305F(The hell is this guy's deal?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0203F(These two have a troublesome relationship.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106F(That may be, but that puts us in\x01",
            "a tight spot, doesn't it?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003F(S-Still, we accepted the doctor's request.\x01",
            "It's our duty to follow through, no matter how\x01",
            "difficult the archbishop may be.)\x02\x03",
            "#0001FE-Excuse me, Archbishop Eralda.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FWe were informed by Doctor Lago that he\x01",
            "intends to use all the herbs for internal\x01",
            "medicine research.\x02\x03",
            "Considering how renowned St. Ursula is as\x01",
            "a medical institution, I'm sure those herbs\x01",
            "will go a long way in helping future patients.\x02\x03",
            "#0008FWe don't intend to ask any personal questions\x01",
            "about you and the doctor's relationship.\x02\x03",
            "#0003FHowever, despite your differences, is it not at\x01",
            "all possible for you to let us have some of the\x01",
            "Lupinus Grass?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt seems as though you four have\x01",
            "misunderstood me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWhen did I say that I wouldn't hand\x01",
            "over the herbs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FCome again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou will find my office on the left-hand\x01",
            "side of the sanctuary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf you tell Father Renton that you have\x01",
            "my permission, he should supply you\x01",
            "with a sufficient quantity of the grass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNow, I'd say this conversation is well\x01",
            "over. Go on. Get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FTh-Thank you, sir?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(2750, 2490, 2009, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27740, 1000)
    OP_93(0x8, 0x5A, 0x0)
    SetChrPos(0x101, -500, 500, 7500, 180)
    SetChrPos(0x102, 1000, 500, 7500, 180)
    SetChrPos(0x103, -500, 500, 9000, 180)
    SetChrPos(0x104, 1000, 500, 9000, 180)

    def lambda_F20C():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F20C)

    def lambda_F226():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F226)

    def lambda_F240():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F240)

    def lambda_F25A():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F25A)
    Sleep(500)
    SetCameraDistance(26740, 0)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_F29A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F29A)

    def lambda_F2A7():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F2A7)

    def lambda_F2B4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F2B4)

    def lambda_F2C1():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F2C1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#5P#0003FSo...that happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FGuess we were able to persuade the\x01",
            "old fart after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FDid we even persuade him in the first\x01",
            "place? He played it off as if he was\x01",
            "going to give it to us anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FI am still confused about the whole\x01",
            "ordeal.\x02\x03",
            "Would it not be wise to pick up the\x01",
            "Lupinus Grass before he changes his\x01",
            "mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FWe definitely should.\x02\x03",
            "#0000FHe said it was the office on the left,\x01",
            "right? Let's hurry over there.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1900, 2490, 2430, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(22000, 0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrPos(0x0, -500, 0, 3500, 180)
    SetChrPos(0x1, -500, 0, 3500, 180)
    SetChrPos(0x2, -500, 0, 3500, 180)
    SetChrPos(0x3, -500, 0, 3500, 180)
    OP_29(0x13, 0x1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_40_E703 end

    def Function_41_F545(): pass

    label("Function_41_F545")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(97580, 1200, 7510, 0)
    MoveCamera(314, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27740, 0)
    OP_93(0xA, 0x5A, 0x0)
    SetChrPos(0x101, 98000, 0, 7000, 270)
    SetChrPos(0x102, 98000, 0, 8300, 270)
    SetChrPos(0x103, 99300, 500, 7000, 270)
    SetChrPos(0x104, 99300, 500, 8300, 270)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xA,
        "#5PExcuse me. Do you have some business here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThis is the archbishop's office. You can't simply\x01",
            "barge in unannounced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FOh, sorry about that. We're the Special\x01",
            "Support Section, of the CPD. You see...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd carefully explained that the SSS had Archbishop\x01",
            "Eralda's permission to pick up some Lupinus Grass.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        "#5PAh, why didn't you say so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYou said you already got the archbishop's\x01",
            "approval? Wait just a minute, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(98390, 1500, 8960, 4000)
    OP_93(0xA, 0x0, 0x1F4)

    def lambda_F7C7():
        OP_95(0xFE, 96000, 0, 11500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F7C7)
    WaitChrThread(0xA, 1)

    def lambda_F7E5():
        OP_95(0xFE, 100000, 0, 11500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F7E5)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    Sleep(1000)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    Sound(910, 0, 100, 0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    OP_68(97580, 1500, 7510, 4000)
    OP_93(0xA, 0x10E, 0x1F4)

    def lambda_F849():
        OP_95(0xFE, 96000, 0, 11500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F849)
    WaitChrThread(0xA, 1)

    def lambda_F867():
        OP_95(0xFE, 96000, 0, 7830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F867)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x5A, 0x1F4)

    ChrTalk(
        0xA,
        "#5PHere. One sample of Lupinus Grass.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x341),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x341, 1)

    ChrTalk(
        0xA,
        (
            "#5PAs for why it's called Lupinus, it's actually\x01",
            "from an old word meaning 'wolf.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAnd this particular herb has a fascinating\x01",
            "history. It's said that it was gifted to mankind\x01",
            "by the divine wolves a long, long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt flourished in one area near Crossbell\x01",
            "City, but the density has thinned out due\x01",
            "to the city's expansion and development...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FI think my grandfather told me a similar\x01",
            "story when I was younger. It's sad, in a\x01",
            "way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FReally? I never knew about it.\x02\x03",
            "#0003FThat just raises another question. If the grass\x01",
            "is so rare, why would Archbishop Eralda\x01",
            "just hand it over like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0306FCan't say I understand it, either. I got\x01",
            "the vibe that he was out to get poor\x01",
            "Doctor Lago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FOur conversation certainly piqued my\x01",
            "interest in the drama between them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5POh, you're talking about Lago? That's\x01",
            "old news, so I might as well tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PDoctor Lago originally studied to\x01",
            "be a priest at this very cathedral.\x02",
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
        "#12P#0005FDoctor Lago wanted to work in the church?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PThere's nothing strange about the notion, actually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PInternal medicine and its relevant subjects\x01",
            "are surprisingly similar to subjects studied\x01",
            "by the Septian Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FIt is true. The church is known for its research\x01",
            "into medicinal treatments and the like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0105FBut, why exactly did Doctor Lago leave\x01",
            "to join the medical college?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PSupposedly, he was scouted out by the\x01",
            "hospital's director.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PDespite learning everything he knew about\x01",
            "general medicine from Archbishop Eralda...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P...his desire to challenge the field of modern\x01",
            "medicine trumped all else, so he ended up\x01",
            "leaving the path of priesthood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThe archbishop can be a stubborn man.\x01",
            "Forgiveness doesn't come to him easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FHmm, I get that. Lago's move probably\x01",
            "felt like a stab to the back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWell, stubborn as he may be, he is still\x01",
            "able to tell right from wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI've no doubt that's why he allowed you\x01",
            "to take those herbs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAs much as it may frustrate him, he doesn't\x01",
            "deny Doctor Lago's skill in medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FSo, from what I am hearing, those two\x01",
            "do not have a bad relationship...\x02\x03",
            "#0200F...they have a terrible relationship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0012FH-Haha... (Isn't that a bit too blunt, Tio?)\x02\x03",
            "#0003FIn the end, we got what we came here for.\x02\x03",
            "#0000FLet's go on and deliver these to Doctor Lago\x01",
            "before doing anything else.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(98000, 2000, 7000, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(33000, 0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrPos(0x0, 98000, 0, 7000, 270)
    SetChrPos(0x1, 98000, 0, 7000, 270)
    SetChrPos(0x2, 98000, 0, 7000, 270)
    SetChrPos(0x3, 98000, 0, 7000, 270)
    OP_29(0x13, 0x1, 0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_41_F545 end

    def Function_42_1035D(): pass

    label("Function_42_1035D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_103DA")

    ChrTalk(
        0x8,
        (
            "Doctor Lago chose to pursue modern\x01",
            "medicine of his own accord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "That's all I'll say on the matter.\x02",
    )

    CloseMessageWindow()
    Jump("loc_10609")

    label("loc_103DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_10465")

    ChrTalk(
        0x8,
        (
            "Yes? Do you still need me for\x01",
            "something, officers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You have the herbs, don't you?\x01",
            "Get on with delivering them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10609")

    label("loc_10465")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_10609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1052E")

    ChrTalk(
        0x8,
        (
            "The Lupinus Grass is stored in my office,\x01",
            "on the left-hand side of the sanctuary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Speak to Father Renton when you get there.\x01",
            "He should get you a sufficient amount.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10609")

    label("loc_1052E")


    ChrTalk(
        0x8,
        (
            "The Lupinus Grass is stored in my office,\x01",
            "on the left-hand side of the sanctuary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Speak to Father Renton when you get there.\x01",
            "He should get you a sufficient amount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Anything else?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FN-No, sir.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_10609")

    Return()

    # Function_42_1035D end

    def Function_43_1060A(): pass

    label("Function_43_1060A")

    EventBegin(0x0)
    Fade(500)
    OP_68(152600, 1700, 16650, 0)
    MoveCamera(322, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27870, 0)
    OP_93(0xC, 0x5A, 0x0)
    SetChrPos(0x101, 153300, 200, 16500, 270)
    SetChrPos(0xEF, 154500, 200, 17180, 270)
    SetChrPos(0x153, 153300, 200, 17700, 270)
    OP_4B(0xC, 0xFF)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B5B")

    ChrTalk(
        0x153,
        "#11P#1110FHello again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5POh, my. Hello again to you, too, KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PDid you forget something, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FNo, actually.\x02\x03",
            "After passing by the kids earlier, we\x01",
            "got a little interested in Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIs that so? Perfect timing.\x01",
            "We were just about to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PYou know...maybe the Goddess planned\x01",
            "for this to happen.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#5PTruth be told, I've been contemplating\x01",
            "teaching the children about the CPD\x01",
            "for quite a while now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_108C0")

    ChrTalk(
        0x102,
        "#12P#0105FReally now?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1095A")

    label("loc_108C0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1090A")

    ChrTalk(
        0x103,
        "#12P#0205FThat is surprising, to say the least.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1095A")

    label("loc_1090A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1095A")

    ChrTalk(
        0x104,
        (
            "#12P#0305FYou wanna cover cops during one\x01",
            "of your lessons?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1095A")


    ChrTalk(
        0xC,
        "#5PIndeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PAnd I was thinking, who better to teach\x01",
            "about the CPD than the CPD itself?\x01",
            "Would you care to be a guest lecturer?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#0005FGuest lecturer? Me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PPlease, if you don't mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PWho better to inform the children\x01",
            "about how the police operate than\x01",
            "a police officer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI'm certain your explanations would\x01",
            "make far more sense than mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PHow about it? Would you join our\x01",
            "lesson as a guest lecturer?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x27, 0x4, 0x2)
    OP_29(0x27, 0x1, 0x0)
    Jump("loc_10B95")

    label("loc_10B5B")


    ChrTalk(
        0xC,
        (
            "#5PWould you be interested in giving\x01",
            "the lesson now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B95")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Let's do it!]\x01",                    # 0
            "[I'm not sure about this...]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D39")

    ChrTalk(
        0x101,
        (
            "#12P#0003FI'm sorry, Sister Marble. I think I'm\x01",
            "going to have to pass on this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI'm sorry to hear that. I thought it\x01",
            "was a creative idea, but no matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIf you're uncomfortable with it, I\x01",
            "won't force your hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PStill, if you feel like participating,\x01",
            "just come talk to me.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 153260, 200, 16760, 270)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)

    label("loc_10D39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11464")

    ChrTalk(
        0x101,
        "#12P#0000FYou know what? I'd love to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5POh, really? Thank you, Lloyd. I have\x01",
            "no doubt the class will appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10DCC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_10DCC)

    def lambda_10DD9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_10DD9)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10E6D")

    ChrTalk(
        0x102,
        (
            "#12P#0105FAre you sure about this, Lloyd?\x02\x03",
            "#0103FTeaching people isn't exactly the\x01",
            "easiest thing to do, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FA7")

    label("loc_10E6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10EFC")

    ChrTalk(
        0x103,
        (
            "#12P#0200FAre you positive you want to do this?\x02\x03",
            "#0203FDo not underestimate the difficulty that\x01",
            "comes with teaching.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FA7")

    label("loc_10EFC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10FA7")

    ChrTalk(
        0x104,
        (
            "#12P#0306FYou sure about this, man?\x02\x03",
            "#0300FI know it sounds weird coming from\x01",
            "me of all people, but going into this\x01",
            "without thinkin' ahead is ballsy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FA7")


    def lambda_10FAC():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10FAC)

    ChrTalk(
        0x101,
        (
            "#6P#0000FDon't worry--I know. It's not like I agreed\x01",
            "to this without some semblance of a plan.\x02\x03",
            "#0003FIt's just...it's rare to get the opportunity\x01",
            "to tell people about how the police and\x01",
            "justice system really work.\x02\x03",
            "#0000FWho knows? There could be a future\x01",
            "recruit of the Crossbell Police Academy\x01",
            "in this room--just like I was.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1115F")

    ChrTalk(
        0x102,
        (
            "#12P#0104FI see. That way of thinking is very\x01",
            "much like you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11208")

    label("loc_1115F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1119F")

    ChrTalk(
        0x103,
        "#12P#0204FHmm. That is a valid point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11208")

    label("loc_1119F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11208")

    ChrTalk(
        0x104,
        (
            "#12P#0300FOh, I got'cha. We're usin' this as a\x01",
            "promotional event for the force, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11208")


    def lambda_1120D():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1120D)

    ChrTalk(
        0x101,
        (
            "#6P#0000FWe might have to put our trip\x01",
            "to St. Ursula on hold for now.\x01",
            "Are you okay with that, KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#11P#1109FUh-huh!\x02\x03",
            "#1100FIf you wanna do this lesson thingy,\x01",
            "Lloyd, I'll cheer you on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0009FHaha. Thanks a lot, KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PIf we're in agreement, would you\x01",
            "mind stepping outside for a moment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI will give you a brief outline on how\x01",
            "to proceed with the lecture, all right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_113A9():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_113A9)

    def lambda_113B6():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_113B6)

    def lambda_113C3():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_113C3)

    ChrTalk(
        0x101,
        "#12P#0000FOf course, Sister Marble.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Guest Lecturer for Sunday School]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Call(0, 44)
    Call(0, 45)
    Call(0, 48)

    label("loc_11464")

    Return()

    # Function_43_1060A end

    def Function_44_11465(): pass

    label("Function_44_11465")

    OP_68(7710, 2300, -90, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(26410, 0)
    SetChrPos(0xC, 7600, 0, 1320, 270)
    SetChrPos(0x101, 5570, 0, 1350, 90)
    SetChrPos(0xEF, 4380, 0, 2050, 90)
    SetChrPos(0x153, 4720, 0, 510, 90)
    Sleep(500)
    SetCameraDistance(25410, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_64(0xC)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#5P#0003FOkay, let's see if I've got everything.\x02\x03",
            "First, I'll give a broad, easy-to-understand\x01",
            "explanation of what the CPD does...\x02\x03",
            "#0000F...and then I'll move on to the Q&A.\x01",
            "That's at least the general plan, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12PThat should be perfect.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12PI do have one suggestion, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FYou do? What's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12PIt's, of course, your decision...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12P...but how about you have KeA\x01",
            "attend the lesson, as well?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#0005FOh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11744")

    ChrTalk(
        0x102,
        "#5P#0100FThat's a wonderful idea, Sister Marble.\x02",
    )

    CloseMessageWindow()
    Jump("loc_117D9")

    label("loc_11744")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11791")

    ChrTalk(
        0x103,
        "#5P#0204FI imagine she would enjoy that very much.\x02",
    )

    CloseMessageWindow()
    Jump("loc_117D9")

    label("loc_11791")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_117D9")

    ChrTalk(
        0x104,
        "#5P#0309FHaha! She'll be your best student, Lloyd.\x02",
    )

    CloseMessageWindow()

    label("loc_117D9")


    ChrTalk(
        0x153,
        "#5P#1105FCan I? Oh, can I, can I, can I?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12PYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAfter all, most children your age have\x01",
            "already started attending Sunday School.\x01",
            "It would be a good experience for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#5P#1110FYay!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)

    ChrTalk(
        0x153,
        (
            "#6P#1109FI'll be the bestest student there ever was!\x02\x03",
            "I wanna learn everything about you, Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11926():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11926)
    Sleep(50)

    def lambda_11936():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_11936)

    ChrTalk(
        0x101,
        "#12P#0005FKeA...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_119B8")

    ChrTalk(
        0x102,
        (
            "#5P#0100FNo backing out now, Lloyd. I doubt\x01",
            "she'd let you, anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A6E")

    label("loc_119B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11A05")

    ChrTalk(
        0x103,
        "#5P#0200FYou backed yourself into a corner, Lloyd.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11A6E")

    label("loc_11A05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11A6E")

    ChrTalk(
        0x104,
        (
            "#5P#0300FBetter put your mira where your mouth is,\x01",
            "my friend. She's ready to learn.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A6E")


    ChrTalk(
        0x101,
        (
            "#12P#0004FHaha. You're right about that.\x02\x03",
            "#0000FKeA, make sure to try to get along with\x01",
            "the other kids. Make some friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#6P#1110FWill do!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11B90")

    ChrTalk(
        0x102,
        (
            "#5P#0104FI'll keep an eye on everything from\x01",
            "the back of the classroom, okay?\x02\x03",
            "#0100FDo your best, Mr. Bannings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CD6")

    label("loc_11B90")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11C33")

    ChrTalk(
        0x103,
        (
            "#5P#0203FI plan to observe the lesson from the\x01",
            "back of the classroom.\x02\x03",
            "#0211FI am rooting for you, but try not to\x01",
            "mess it up, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CD6")

    label("loc_11C33")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11CD6")

    ChrTalk(
        0x104,
        (
            "#5P#0304FI'm gonna chill in the back and watch\x01",
            "this trainwreck unfold.\x02\x03",
            "#0300FI'll be gradin' your skills as a teacher,\x01",
            "so don't let me down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CD6")


    def lambda_11CDB():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11CDB)

    ChrTalk(
        0x101,
        (
            "#12P#0006F(Talk about unfair...)\x02\x03",
            "#0000FHey, all I can do is try my best.\x02\x03",
            "This is a once-in-a-lifetime chance\x01",
            "to teach these kids about the police.\x01",
            "I don't plan to run away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12PThat's the spirit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12PNow, then, shall we begin?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Return()

    # Function_44_11465 end

    def Function_45_11DE6(): pass

    label("Function_45_11DE6")

    LoadChrToIndex("chr/ch08202.itc", 0x1E)
    OP_68(151700, 1500, 4100, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29780, 0)
    SetChrPos(0xC, 150800, 200, 17500, 180)
    SetChrPos(0x153, 153000, 200, 17650, 180)
    SetChrPos(0x101, 155630, 200, 17510, 270)
    SetChrPos(0xEF, 150910, 0, 1530, 0)
    OP_68(151620, 1500, 14920, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xC,
        "#11PListen up, class.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PBefore we begin today's lesson,\x01",
            "there's a new friend I would like\x01",
            "to introduce to you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x153, 500)

    ChrTalk(
        0xC,
        "#5PKeA, if you'd come forward.\x02",
    )

    CloseMessageWindow()

    def lambda_11F26():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_11F26)
    OP_98(0x153, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)

    ChrTalk(
        0x153,
        (
            "#11P#1110FHey there! My name's KeA!\x01",
            "Nice to meet'cha!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 200, -1, -1)
    SetChrName("Children")

    AnonymousTalk(
        0xFF,
        "#5SNice to meet you!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#11PThere's the energetic greeting I was expecting.\x01",
            "KeA, you may sit at any of the empty seats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#11P#1109FI want that one!\x02",
    )

    CloseMessageWindow()
    OP_68(154300, 1500, 8280, 4000)
    OP_95(0x153, 153000, 200, 14000, 2000, 0x0)
    OP_95(0x153, 152000, 200, 14000, 2000, 0x0)
    OP_95(0x153, 152000, 200, 9100, 2000, 0x0)
    OP_93(0x153, 0x5A, 0x12C)
    Fade(500)
    SetChrChipByIndex(0x153, 0x1E)
    SetChrPos(0x153, 153620, 150, 9130, 0)
    SetChrFlags(0x153, 0x4)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x153, 0x2)
    SetChrSubChip(0x11, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(
        0x153,
        "#5P#1109FHiya, neighbor!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#12PH-Hello. It's nice to meet you.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(152620, 1500, 3180, 0)
    MoveCamera(331, 19, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29780, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_121C8")

    ChrTalk(
        0x102,
        (
            "#6P#0104F(This must be what a mother\x01",
            "feels like on Parents' Day.)\x02\x03",
            "#0100F(Do your best, KeA!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122D6")

    label("loc_121C8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1224A")

    ChrTalk(
        0x103,
        (
            "#6P#0204F(This vaguely reminds me of Parents'\x01",
            "Day at school...)\x02\x03",
            "#0200F(I am here to support you, KeA.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122D6")

    label("loc_1224A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_122D6")

    ChrTalk(
        0x104,
        (
            "#6P#0304F(Watchin' over your kid as they learn\x01",
            "and grow... Oh, I'm gonna cry!)\x02\x03",
            "#0309F(You got this in the bag, KeDo!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_122D6")

    OP_5A()
    Fade(500)
    SetChrSubChip(0x153, 0x0)
    SetChrSubChip(0x11, 0x0)
    OP_68(152750, 1500, 15630, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29780, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#11PFor today's lesson, we have\x01",
            "a very special guest with us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 300)

    ChrTalk(
        0xC,
        "#5PNow, without further ado...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0003FHere we go...\x02",
    )

    CloseMessageWindow()
    OP_68(152250, 1700, 12670, 3000)
    MoveCamera(310, 14, 0, 3000)
    SetCameraDistance(30190, 3000)
    BeginChrThread(0x101, 3, 0, 46)
    Sleep(500)
    BeginChrThread(0xC, 3, 0, 47)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)

    ChrTalk(
        0x21,
        (
            "#6PWhoa! I was tryin' not to get\x01",
            "my hopes up, but heck yeah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#6PI can't believe it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FU-Um, hello, everyone. I definitely see\x01",
            "some familiar faces, but for those who\x01",
            "don't know me...\x02\x03",
            "#0000F...my name is Lloyd Bannings.\x02\x03",
            "I work as a police officer on active duty\x01",
            "at the Crossbell Police Department,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5PThe police...? Ryu, you know them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5PThe Special Support Section...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PWait a minute! You were in the\x01",
            "Crossbell Times that one time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5POh, I remember now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PI skipped the article, but I saw that\x01",
            "teeny tiny photo of you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PAll right, everyone. Quiet down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI've been meaning to teach you all\x01",
            "about Crossbell's police, so I asked\x01",
            "Lloyd here to lead the lesson today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PMake sure to pay extra close\x01",
            "attention to him, okay?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("Children")

    AnonymousTalk(
        0xFF,
        "#5SOkaaaaaaay!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TurnDirection(0xC, 0x101, 300)

    ChrTalk(
        0xC,
        "#5PThe floor is yours, Mr. Bannings. ㈱\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 300)

    ChrTalk(
        0x101,
        "#11P#0003FLeave it to me, Sister Marble.\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x10E, 0x12C)
    OP_95(0xC, 146430, 200, 17490, 2000, 0x0)
    OP_93(0xC, 0x87, 0x12C)
    OP_93(0x101, 0xB4, 0x12C)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#11P#0003F(Crap, I can already feel the\x01",
            "butterflies in my stomach.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(153200, 1700, 9500, 3000)
    MoveCamera(319, 10, 0, 3000)
    OP_6F(0x79)
    OP_64(0x153)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x153,
        "#6P#1107F#5S#NYou got this, Lloyd!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x21, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x21,
        (
            "#6PHaha! Did you bring her\x01",
            "along as a cheerleader?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#6PCut it out, Ryu.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#6PCan't you see he's doing his best?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0006FUm, KeA... Class has started, so I'm\x01",
            "going to need you to refrain from\x01",
            "the outbursts, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#6P#1106FAw, boo. I cheered for you and everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0004F(You know, I think I actually feel a little\x01",
            "more relaxed now. Thanks, KeA.)\x02\x03",
            "#0000FAhem. Ready to start, class?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    StopBGM(0x7D0)
    Fade(500)
    OP_68(151090, 1500, 15660, 0)
    MoveCamera(0, 17, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32470, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　Lecture Start!\x01",
            "~General Police Information~\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Choose the correct answers and lead\x01",
            "the lesson toward a shining success!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#0004FTo start things off, I want to teach you all about\x01",
            "what the police force, as a whole, actually is.\x02\x03",
            "#0000FIn Crossbell State, there's a certain something\x01",
            "that we aren't allowed to establish, despite\x01",
            "other countries doing so.\x02\x03",
            "To compensate for this certain something, we\x01",
            "formed the Crossbell Guardian Force and the\x01",
            "Crossbell Police Department, where I work.\x02\x03",
            "#0003FAnd even though we aren't allowed to have one,\x01",
            "this certain something is extremely important to\x01",
            "other countries. This something being...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "What is crucial to other Zemurian countries,\x01",
            "but Crossbell is forbidden to have?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Intelligence Agency]\x01",      # 0
            "[② Bracer Guild]\x01",             # 1
            "[③ Military]\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12E59"),
        (1, "loc_13051"),
        (2, "loc_1317F"),
        (SWITCH_DEFAULT, "loc_13367"),
    )


    label("loc_12E59")


    ChrTalk(
        0x101,
        "#0000F...an intelligence agency.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    ChrTalk(
        0x101,
        (
            "#0005F(Or, now that I think about it, I know that we\x01",
            "DON'T have one, but they aren't against state\x01",
            "law...)\x02\x03",
            "#0012FYou see...to protect Crossbell State, knowing\x01",
            "information about our neighboring countries\x01",
            "is key to our survival.\x02\x03",
            "We can usually prevent crimes before they\x01",
            "happen, but in order to do that, we have to\x01",
            "gather info from tourists and other...people.\x02\x03",
            "#0011F(Wh-What in the world am I saying? All of\x01",
            "that sounded like a bunch of nonsense.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13367")

    label("loc_13051")


    ChrTalk(
        0x101,
        "#0000F...the Bracer Guild.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    ChrTalk(
        0x101,
        (
            "#0012FYou see, the Bracer Guild plays an active\x01",
            "role in protecting Crossbell, but, uh...\x02\x03",
            "...long ago, it was up to the police to\x01",
            "carry the burden of protecting the public.\x02\x03",
            "#0006F(I-I'm all over the place. All of that sounded\x01",
            "like a bunch of nonsense.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13367")

    label("loc_1317F")


    ChrTalk(
        0x101,
        (
            "#0000F...a military.\x02\x03",
            "For example, the Erebonian Empire to our west\x01",
            "uses their military to prevent crime and protect\x01",
            "their sovereignty...\x02\x03",
            "...but Crossbell doesn't have an active military.\x01",
            "Therefore, those roles are divided between\x01",
            "several different organizations.\x02\x03",
            "Among those is the CPD. It's our duty to carry\x01",
            "out investigations of crimes, and, if we're lucky,\x01",
            "prevent them from happening in the first place.\x02\x03",
            "#0004F(That sounded like a pretty good summary to me.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_13367")

    label("loc_13367")

    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0000FThe CPD is split into multiple groups, or what we\x01",
            "like to call division--and officers and police duties\x01",
            "are divided among them.\x02\x03",
            "Different divisions are dispatched depending on the\x01",
            "nature and severity of a case so that we can respond\x01",
            "with the appropriate countermeasures.\x02\x03",
            "#0003FOut of all of them, the division that deals the most\x01",
            "with massive, sometimes international, crimes and\x01",
            "incidents would be...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Which division of the CPD is in charge of major\x01",
            "cases and international matters?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① First Investigative Division]\x01",       # 0
            "[② Second Investigative Division]\x01",      # 1
            "[③ Special Support Section]\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1363B"),
        (1, "loc_137CE"),
        (2, "loc_13997"),
        (SWITCH_DEFAULT, "loc_13B4C"),
    )


    label("loc_1363B")


    ChrTalk(
        0x101,
        (
            "#0000F...the First Investigative Division.\x02\x03",
            "For kidnappings, murders, and other large-scale\x01",
            "cases, the CPD likes to put only the best-of-the-best\x01",
            "detectives on the job.\x02\x03",
            "All of the force's elite detectives are gathered\x01",
            "in what's known as the First Division. They're\x01",
            "even known for solving cases single-handedly.\x02\x03",
            "#0004F(And we can't lose to them, no matter how\x01",
            "impressive they are.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_13B4C")

    label("loc_137CE")


    ChrTalk(
        0x101,
        "#0000F...the Second Investigative Division.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    ChrTalk(
        0x101,
        (
            "#0000FFor kidnappings, murders, and other major cases,\x01",
            "it's obvious that police officers first need the\x01",
            "ability to solve smaller cases, right?\x02\x03",
            "That's why the Second Division primarily takes on\x01",
            "thefts and other petty crimes, but also investigates\x01",
            "major cases when they're more clear-cut.\x02\x03",
            "#0006F(That doesn't sound completely implausible, but\x01",
            "is that really what happens? My gut's saying no.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B4C")

    label("loc_13997")


    ChrTalk(
        0x101,
        "#0000F...us, the Special Support Section.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    ChrTalk(
        0x101,
        (
            "#0000FIf you really want to investigate major cases such\x01",
            "as kidnappings and murders the right way, one has\x01",
            "to possess a wide range of investigative skills.\x02\x03",
            "Because of that, the Special Support Section, with\x01",
            "its flexibility and agility, is the perfect team to\x01",
            "tackle major cases. You know, the really big ones.\x02\x03",
            "#0006F(Uh, I think I made us sound WAY too cool there...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B4C")

    label("loc_13B4C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0000FEvery detective in the CPD is given an extremely\x01",
            "handy book, simply called the Detective Notebook.\x02\x03",
            "In addition to doubling as our identification, it\x01",
            "also has an even more important use for detectives.\x02\x03",
            "#0003FThat would be...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "What is the Detective Notebook's most important use\x01",
            "for CPD detectives?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① To record the progress of investigations]\x01",      # 0
            "[② To substitute as an arrest warrant]\x01",            # 1
            "[③ To upload location data]\x01",                       # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13D76"),
        (1, "loc_13EB0"),
        (2, "loc_1403D"),
        (SWITCH_DEFAULT, "loc_141BD"),
    )


    label("loc_13D76")


    ChrTalk(
        0x101,
        (
            "#0000F...recording our progress on a case. Basically, it's\x01",
            "a glorified notepad for us detectives.\x02\x03",
            "It helps us sort through the current state of cases\x01",
            "and is used to jot down our thoughts and even\x01",
            "keep track of business expenses.\x02\x03",
            "I'd be lost without mine, that's for sure.\x02\x03",
            "#0004F(Nailed it.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_141BD")

    label("loc_13EB0")


    ChrTalk(
        0x101,
        "#0000F...substituting as an arrest warrant.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    ChrTalk(
        0x101,
        (
            "#0012FR-Right. When you apprehend a suspect, you're\x01",
            "required to submit an application to the department\x01",
            "before actually making the arrest.\x02\x03",
            "#0000FHowever, in emergency situations, officers are able\x01",
            "to show their Detective Notebook and make the\x01",
            "arrest without having a warrant.\x02\x03",
            "#0006F(Can't say I'm too confident about that one...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141BD")

    label("loc_1403D")


    ChrTalk(
        0x101,
        "#0000F...uploading our location data.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    ChrTalk(
        0x101,
        (
            "#0012FU-Uh, yeah, I didn't believe it at first, either.\x01",
            "These particular notebooks are able to transmit our\x01",
            "location back to the CPD's database.\x02\x03",
            "#0000FThrough that system, we're able to check our exact\x01",
            "location and even find out where other officers are.\x01",
            "Cool, right?\x02\x03",
            "#0006F(Yeah, that's impossible. It's just a notebook.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141BD")

    label("loc_141BD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0000FSimilar to the Bracer Guild, the police force is\x01",
            "equipped with the latest generation orbments to use\x01",
            "in combat scenarios.\x02\x03",
            "#0003FDespite most officers not being combat experts,\x01",
            "there are times when a fight is unavoidable,\x01",
            "notably when in hot pursuit of an active criminal.\x02\x03",
            "#0000FFun fact: There's already been many iterations of\x01",
            "orbments created through the years. With each\x01",
            "generation, brand new features are added.\x02\x03",
            "#0003FThe orbments we currently use are...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "What is the current generation of orbments?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Fifth generation]\x01",        # 0
            "[② Sixth generation]\x01",        # 1
            "[③ Seventh generation]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1448B"),
        (1, "loc_145B0"),
        (2, "loc_146E0"),
        (SWITCH_DEFAULT, "loc_14817"),
    )


    label("loc_1448B")


    ChrTalk(
        0x101,
        (
            "#0000F...fifth generation orbments, otherwise known as the\x01",
            "Enigma combat orbments.\x02\x03",
            "The special part of this generation is its portable\x01",
            "comms feature. It lets us contact fellow officers in\x01",
            "emergencies, it's perfect for police work.\x02\x03",
            "#0004F(That sounded right to me.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_14817")

    label("loc_145B0")


    ChrTalk(
        0x101,
        (
            "#0000F...sixth generation orbments, otherwise known as the\x01",
            "Enigma combat orbments.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    ChrTalk(
        0x101,
        (
            "#0000FNow that the standard has changed and only new\x01",
            "quartz can be used for this generation, they can\x01",
            "end up being quite the hassle to deal with.\x02\x03",
            "#0006F(Wait a sec, was the Enigma really sixth gen?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14817")

    label("loc_146E0")


    ChrTalk(
        0x101,
        (
            "#0000F...seventh generation orbments, otherwise known as\x01",
            "the Enigma combat orbments.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    ChrTalk(
        0x101,
        (
            "#0012FW-Well, the tricky thing about orbments is that\x01",
            "they keep getting replaced with newer ones. That\x01",
            "can make maintenance pretty confusing at times.\x02\x03",
            "#0006F(Are orbments really switched out that often?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14817")

    label("loc_14817")

    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0000FThere are quite a lot of different positions at the\x01",
            "CPD, ranging from your standard police officer to\x01",
            "detectives like me. That being said, we all work for\x01",
            "Crossbell's sake.\x02\x03",
            "#0003FAt first glance, you might not think those two roles\x01",
            "are related, but you'd be surprised.\x02\x03",
            "#0000FAll police work is rooted in one basic principle.\x02\x03",
            "#0003FAnd that's...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "What is the basic principle behind the CPD's work?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Protecting Crossbell's citizenry]\x01",                            # 0
            "[② Public order and state law compliance]\x01",      # 1
            "[③ Guarding against foreign nations & preserving peace]\x01",         # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_14ACE"),
        (1, "loc_14C44"),
        (2, "loc_14E9E"),
        (SWITCH_DEFAULT, "loc_1506C"),
    )


    label("loc_14ACE")


    ChrTalk(
        0x101,
        "#0000F...protecting Crossbell's citizenry from danger.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    ChrTalk(
        0x101,
        (
            "#0000FThe CPD's mission statement is to protect the people\x01",
            "of Crossbell, no matter what hardships stand in our\x01",
            "way.\x02\x03",
            "We strive to create a society free from worry and\x01",
            "stress, where everyone can cooperate in peace.\x02\x03",
            "#0006F(That might be a part of it, but probably not the\x01",
            "best answer for that one.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1506C")

    label("loc_14C44")


    ChrTalk(
        0x101,
        (
            "#0000F...maintaining public order and compliance with\x01",
            "state law.\x02\x03",
            "It's our mission to crack down on criminals in order\x01",
            "to ensure that the rest of the public can live in\x01",
            "harmony, without having to worry about crime.\x02\x03",
            "We strive to be model citizens ourselves by upholding\x01",
            "the law, in hopes that we can serve as an example\x01",
            "to others. Also, we work to control crime outbreaks\x01",
            "as a whole.\x02\x03",
            "By doing so, we're able to maintain peace and set our\x01",
            "sights on someday living in a world without crime.\x01",
            "That, I'd say, is the CPD's mission statement.\x02\x03",
            "#0004F(Hey, that came together nicely!)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1506C")

    label("loc_14E9E")


    ChrTalk(
        0x101,
        (
            "#0000F...guarding against foreign nations\x01",
            "and preserving peace.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 51)

    ChrTalk(
        0x101,
        (
            "#0000FIf you didn't know, Crossbell is sandwiched between\x01",
            "the Erebonian Empire and the Calvard Republic.\x01",
            "Unfortunately, that has led to higher crime rates.\x02\x03",
            "By limiting foreign infiltration into Crossbell,\x01",
            "we can create a safer environment for the public.\x01",
            "That, I'd say, is what the CPD works towards.\x02\x03",
            "#0006F(I think I accidentally described the Guardian\x01",
            "Force...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1506C")

    label("loc_1506C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    BeginChrThread(0x101, 3, 0, 52)
    WaitChrThread(0x101, 3)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0004FAnd that's all from me. I hope, at the very least,\x01",
            "you got a better understanding of how the police\x01",
            "operate in Crossbell State.\x02\x03",
            "#0000F...It might have been hard to follow at times, but\x01",
            "did you manage to understand most of it?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(152620, 1500, 3180, 0)
    MoveCamera(331, 19, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29780, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15427")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_152D1")

    ChrTalk(
        0x102,
        (
            "#6P#0100F(Now, class should be halfway finished.)\x02\x03",
            "#0104F(It was clear that he was nervous at first,\x01",
            "but I think his teaching style covered that\x01",
            "up nicely.)\x02\x03",
            "#0100F(I can see his skills used to pass the\x01",
            "detective exam aren't just for show.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15422")

    label("loc_152D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_15381")

    ChrTalk(
        0x102,
        (
            "#6P#0100F(Now, class should be halfway finished.)\x02\x03",
            "#0103F(Lloyd is having a rough time up there,\x01",
            "isn't he?)\x02\x03",
            "(Did his initial nervousness never pass?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15422")

    label("loc_15381")


    ChrTalk(
        0x102,
        (
            "#6P#0103F(Now, class should be halfway finished.)\x02\x03",
            "#0111F(Honestly, I expected better from Lloyd.)\x02\x03",
            "(I'm sure Sister Marble isn't too impressed,\x01",
            "either...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15422")

    Jump("loc_15A7C")

    label("loc_15427")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15773")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1557E")

    ChrTalk(
        0x103,
        (
            "#6P#0200F(And that should mark the halfway point.)\x02\x03",
            "#0204F(He hit all of the main points accurately and\x01",
            "concisely, and made sure to project his voice\x01",
            "throughout the classroom. Well done, Lloyd.)\x02\x03",
            "(After this is said and done, he just might be\x01",
            "recruited by a university to become a full-time\x01",
            "lecturer.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1576E")

    label("loc_1557E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1567C")

    ChrTalk(
        0x103,
        (
            "#6P#0200F(And that should mark the halfway point.)\x02\x03",
            "#0203F(His tone lacks confidence now and then,\x01",
            "which is a bit worrying...)\x02\x03",
            "(...considering he represents the\x01",
            "Special Support Section, I wish he\x01",
            "would perform a little better.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1576E")

    label("loc_1567C")


    ChrTalk(
        0x103,
        (
            "#6P#0203F(And that should mark the halfway point.)\x02\x03",
            "#0211F(His eyes are darting back and forth, and\x01",
            "his body language is all over the place...)\x02\x03",
            "(Sloppy, truly sloppy. Perhaps I should\x01",
            "have volunteered to give the lecture in\x01",
            "his stead.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1576E")

    Jump("loc_15A7C")

    label("loc_15773")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15A7C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_15876")

    ChrTalk(
        0x104,
        (
            "#6P#0305F(That's halftime, eh?)\x02\x03",
            "#0309F(Lloyd looks like he was born to teach\x01",
            "for a livin', not bust bad guys.)\x02\x03",
            "#0303F(But if life's taught me anything, it's that women\x01",
            "are weak to guys like that. Lloyd, you genius.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A7C")

    label("loc_15876")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1598A")

    ChrTalk(
        0x104,
        (
            "#6P#0305F(That's halftime, eh?)\x02\x03",
            "#0303F(Not gonna lie, that was pretty shaky.\x01",
            "Makin' mistakes that even I know are\x01",
            "wrong? That's not great.)\x02\x03",
            "#0309F(Then again, being a lil' out of it might\x01",
            "seem cute to the ladies and their inner\x01",
            "motherly instincts.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A7C")

    label("loc_1598A")


    ChrTalk(
        0x104,
        (
            "#6P#0300F(That's halftime, eh?)\x02\x03",
            "#0306F(C'mon, dude. Don't embarrass us in front of all\x01",
            "these kids.)\x02\x03",
            "(What happened to that suave, smart, glasses-wearing\x01",
            "guy at Mishelam? Sheesh, I wasn't expecting to be\x01",
            "disappointed, but here we are.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A7C")

    OP_5A()
    Fade(500)
    OP_68(151640, 2100, 12440, 0)
    MoveCamera(329, 14, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30960, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#5PLet us continue the lesson, everyone. Does\x01",
            "anyone have questions for Mr. Bannings?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI'm sure he will be more than happy to answer\x01",
            "any question you might have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0005F(ANY question?! That's a bit of an\x01",
            "overstatement, isn't it?)\x02\x03",
            "#0006F(*sigh* Let's see how this goes.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "     Q&A Start!\x01",
            "~General Questions~\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Choose the correct answers to get through\x01",
            "potentially dangerous questions!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#0000FWell, does anyone have any questions?\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(
        0xF,
        "#5PMe! Pick meeee!\x02",
    )

    CloseMessageWindow()
    OP_68(149370, 1500, 14370, 2000)
    OP_93(0x101, 0xE1, 0x12C)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#11P#0000FAll right. What have you got?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#6PHow do you become a police officer\x01",
            "in the first place, Mr. Bannings?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#6P...Not that I'd ever become one, though.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)

    ChrTalk(
        0x10,
        "#6PTamil, don't be rude!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0006FI'll just pretend I didn't hear that.\x02\x03",
            "#0000FYou're basically asking if there's any special\x01",
            "requirements to become one, right?\x02\x03",
            "Well, to become a police officer...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "What is required to become a CPD police officer?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Pass the detective exam]\x01",               # 0
            "[② Graduate from the police academy]\x01",      # 1
            "[③ Nothing in particular]\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_15F4C"),
        (1, "loc_1610A"),
        (2, "loc_1634F"),
        (SWITCH_DEFAULT, "loc_165C1"),
    )


    label("loc_15F4C")


    ChrTalk(
        0x101,
        "#11P#0000F...you have to pass the detective exam.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    ChrTalk(
        0x101,
        (
            "#11P#0006FWait, that's not right. You only have to take\x01",
            "that exam if you want to be a detective...\x02\x03",
            "#0000FSorry. If you want to become a member of\x01",
            "the CPD, you have to graduate from the\x01",
            "Crossbell Police Academy.\x02\x03",
            "Now, my teammates were able to join the\x01",
            "force without attending the academy, but\x01",
            "they're all special exceptions.\x02\x03",
            "#0006F(Phew. I was able to catch myself there.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_165C1")

    label("loc_1610A")


    ChrTalk(
        0x101,
        "#11P#0000F...you have to graduate from the police academy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FBy attending the academy, you'll learn everything\x01",
            "you need to know about being on the force.\x02\x03",
            "However, as I previously mentioned, there are\x01",
            "many different positions within the CPD.\x02\x03",
            "For example, if you wanted to pursue a career\x01",
            "in detective work, there's a separate exam you\x01",
            "have to pass, in addition to the base curriculum.\x02\x03",
            "There are special exceptions to these rules, like\x01",
            "my teammates. They were able to join the force\x01",
            "without attending the academy at all.\x02\x03",
            "#0004F(That sums it up.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_165C1")

    label("loc_1634F")


    ChrTalk(
        0x101,
        "#11P#0000F...honestly, you don't have to do anything in particular.\x02",
    )

    BeginChrThread(0x101, 3, 0, 50)

    ChrTalk(
        0x101,
        (
            "#11P#0006FS-Sorry, I got confused. You see, my teammates\x01",
            "were able to join the CPD without attending the\x01",
            "police academy, due to special circumstances.\x02\x03",
            "#0000FIf you want to become a member of the CPD,\x01",
            "you have to graduate from the Crossbell Police\x01",
            "Academy.\x02\x03",
            "However, as I previously mentioned, there are\x01",
            "many different positions within the CPD.\x02\x03",
            "For example, if you wanted to pursue a career\x01",
            "in detective work, there's a separate exam you\x01",
            "have to pass, in addition to the base curriculum.\x02\x03",
            "#0006F(Screwed that one up a little, didn't I?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_165C1")

    label("loc_165C1")

    SetChrSubChip(0x10, 0x0)

    ChrTalk(
        0xF,
        "#6PHmm, got'cha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#6PI'm still not going to join the police, but\x01",
            "thanks for the answer, Mr. Bannings!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5PUm...do you mind if I ask a question, too?\x02",
    )

    CloseMessageWindow()
    OP_68(152570, 1200, 14810, 2000)
    OP_93(0x101, 0x87, 0x12C)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5P#0000FSure, Anri. What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#12PWell, we don't hear many details about\x01",
            "big incidents that happen in Crossbell,\x01",
            "so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#12P...I just want to know how the SSS was\x01",
            "able to solve the wolf attacks case. I've\x01",
            "been wondering about it for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0005FOh, where the mafia was misusing their\x01",
            "war hounds throughout the state?\x02\x03",
            "#0003FIf I remember correctly, the turning point\x01",
            "in that particular case was...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "What was the turning point in the war hounds case?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① The SSS's deductive reasoning]\x01",      # 0
            "[② The white wolves' assistance]\x01",       # 1
            "[③ The CGF's backup]\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16912"),
        (1, "loc_16B1C"),
        (2, "loc_16C6F"),
        (SWITCH_DEFAULT, "loc_16DFF"),
    )


    label("loc_16912")


    ChrTalk(
        0x101,
        "#5P#0000F...the SSS's deductive reasoning.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    ChrTalk(
        0x101,
        (
            "#5P#0006FBut, actually, it was Zeit who swooped in at the\x01",
            "end and saved us from the mafia. We were really\x01",
            "in a pinch, then.\x02\x03",
            "If he wasn't there, I'm not sure if the truth behind\x01",
            "the case would have gotten out, much less how we\x01",
            "would have handled their war hounds...\x02\x03",
            "#0000FThat being the case, I'd say that Zeit and his\x01",
            "pack of white wolves were the deciding factor in\x01",
            "that case, Anri.\x02\x03",
            "#0006F(I'm sure Zeit would be offended if he found out\x01",
            "that I forgot.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DFF")

    label("loc_16B1C")


    ChrTalk(
        0x101,
        (
            "#5P#0000F...the white wolves' assistance.\x02\x03",
            "Just when we were about to be done in by\x01",
            "the mafia's war hounds, a pack of white\x01",
            "wolves came to our rescue.\x02\x03",
            "And after that, Zeit, their leader, decided to\x01",
            "come stay with us at the SSS building.\x02\x03",
            "#0004F(I doubt I'll ever forget a moment as amazing\x01",
            "as that one. Thanks, Zeit.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_16DFF")

    label("loc_16C6F")


    ChrTalk(
        0x101,
        "#5P#0000F...the Guardian Force's backup.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    ChrTalk(
        0x101,
        (
            "#5P#0005FWait, hadn't the CGF withdrawn before the final\x01",
            "confrontation of the case? They helped us out\x01",
            "in the end, but that was after the arrest...\x02\x03",
            "#0000FOh, right! We were only able to apprehend the\x01",
            "culprits after being helped out of a pickle by\x01",
            "Zeit and his pack of white wolves.\x02\x03",
            "#0006F(Yikes. Accidentally misremembered that one...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DFF")

    label("loc_16DFF")


    ChrTalk(
        0x15,
        (
            "#12PThat's incredible! Zeit really is\x01",
            "one-of-a-kind, isn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#12PThank you, Mr. Bannings!\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(
        0x11,
        (
            "#6P#NE-Excuse me, sir. I have a question,\x01",
            "if you don't mind...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(153270, 1500, 12030, 2000)
    SetCameraDistance(30650, 2000)
    MoveCamera(327, 8, 0, 2000)
    OP_6F(0x79)
    OP_93(0x101, 0x87, 0x12C)

    ChrTalk(
        0x101,
        "#11P#0000FI don't mind at all. What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6PDo you remember when Ryu and Anri\x01",
            "got lost underground? It was a long time\x01",
            "ago, I think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#6PWhere exactly was that place?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_93(0x21, 0x5A, 0x0)
    SetChrSubChip(0x21, 0x2)
    OP_0D()

    ChrTalk(
        0x21,
        (
            "#5PM-Momo! Don't remind everyone of that!\x01",
            "And for the record, I wasn't lost.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x11)

    ChrTalk(
        0x11,
        "#6PB-But you guys never tell me anything...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FThat incident in the Geofront?\x02\x03",
            "#0003FWell, we found Ryu and Anri in...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Specifically, where were Ryu and Anri lost?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Geofront A Sector]\x01",      # 0
            "[② Geofront B Sector]\x01",      # 1
            "[③ Geofront C Sector]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17170"),
        (1, "loc_1723A"),
        (2, "loc_17371"),
        (SWITCH_DEFAULT, "loc_174BB"),
    )


    label("loc_17170")


    ChrTalk(
        0x101,
        (
            "#11P#0000F...the Geofront's A Sector.\x02\x03",
            "We found ourselves in trouble when monsters\x01",
            "surrounded Ryu, but we were able to make it\x01",
            "out safely with Arios' help.\x02\x03",
            "#0004F(Short and sweet.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_174BB")

    label("loc_1723A")


    ChrTalk(
        0x101,
        (
            "#11P#0000F...the Geofront's B Sector.\x02\x03",
            "#0005FWait a second. Did I say B...?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    ChrTalk(
        0x15,
        "#12PHuh? Wasn't it A Sector?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0012FGood catch, Anri.\x02\x03",
            "#0003FAnyway, thanks to Arios' help, we were able to\x01",
            "get Anri and Ryu out of the Geofront safely.\x02\x03",
            "#0006F(Right. B Sector is where Jona's hideout is.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_174BB")

    label("loc_17371")


    ChrTalk(
        0x101,
        (
            "#11P#0000F...the Geofront's C Sector.\x02\x03",
            "#0005FWait a second. Have we even been\x01",
            "in C Sector yet...?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 50)

    ChrTalk(
        0x15,
        "#12PHuh? Wasn't it A Sector?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0012FGood catch, Anri.\x02\x03",
            "#0003FAnyway, thanks to Arios' help, we were able to\x01",
            "get Anri and Ryu out of the Geofront safely.\x02\x03",
            "#0006F(Huh. My memory must be a little fuzzy...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_174BB")

    label("loc_174BB")


    ChrTalk(
        0x11,
        (
            "#6PW-Wow, that's incredible. Thank you for\x01",
            "the story, Mr. Bannings.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    SetChrSubChip(0x21, 0x0)
    OP_93(0x21, 0x0, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#11P#0000FYou're welcome. Any other questions?\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(
        0x21,
        "#6PPick me! I just came up with a good one!\x02",
    )

    CloseMessageWindow()
    OP_68(152480, 1500, 13840, 2000)
    SetCameraDistance(29120, 2000)
    OP_93(0x101, 0x87, 0x12C)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#11P#0000FGo ahead, Ryu.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#6PI heard somethin' about this a while ago, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#6P...is there some kind of big difference between\x01",
            "the police and the Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#6PBoth of you guys beat up the bad guys, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003F(There's a tougher one...)\x02\x03",
            "#0000FWell, yes... I'm sure everyone else is curious\x01",
            "about this question, too.\x02\x03",
            "#0003FIf I were to pick one specific difference between\x01",
            "the police and the Bracer Guild, it would be...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "What is a big difference between the CPD and the\x01",
            "Bracer Guild?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Right to arrest]\x01",                             # 0
            "[② Power to interfere with the government]\x01",      # 1
            "[③ Not much]\x01",                                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1787A"),
        (1, "loc_17AAC"),
        (2, "loc_17D27"),
        (SWITCH_DEFAULT, "loc_17F65"),
    )


    label("loc_1787A")


    ChrTalk(
        0x101,
        "#11P#0000F...the right to arrest, I guess.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#11P#0011FA-Actually, I guess bracers technically\x01",
            "have the right to make citizen's arrest.\x02\x03",
            "#0003FIt's probably the fact that bracers aren't\x01",
            "allowed to arrest individuals of military\x01",
            "or political standing.\x02\x03",
            "Granted, if they suddenly started attacking\x01",
            "innocent bystanders or something, they're\x01",
            "able to make arrests, then.\x02\x03",
            "#0001FAnd that's where they're different from us. We\x01",
            "have the authority to place politicians and other\x01",
            "officials under arrest, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F65")

    label("loc_17AAC")


    ChrTalk(
        0x101,
        (
            "#11P#0004FIt's somewhat difficult to explain, but bracers\x01",
            "follow what they call the guild code.\x02\x03",
            "And it's precisely because of that code that the\x01",
            "Bracer Guild is given room to operate in most\x01",
            "Zemurian countries.\x02\x03",
            "#0000FOne of their main tenets is one of non-intervention.\x01",
            "That means that they aren't allowed to arrest\x01",
            "individuals of military or political standing.\x02\x03",
            "Granted, if they suddenly started attacking\x01",
            "innocent bystanders or something, they're\x01",
            "able to make arrests, then.\x02\x03",
            "#0003FAnd that's where they're different from us. We\x01",
            "have the authority to place politicians and other\x01",
            "officials under arrest, but...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_17F65")

    label("loc_17D27")


    ChrTalk(
        0x101,
        "#11P#0004F...You know, I'm not sure if there is one.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#11P#0011F(What am I saying?! Of course there is!)\x02\x03",
            "#0003FWell, one of their main tenets is non-intervention.\x01",
            "That means that they aren't allowed to arrest\x01",
            "individuals of military or political standing.\x02\x03",
            "Granted, if they suddenly started attacking innocent\x01",
            "bystanders or something, they're able to make\x01",
            "arrests, then.\x02\x03",
            "#0001FAnd that's where they're different from us. We\x01",
            "have the authority to place politicians and other\x01",
            "officials under arrest, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F65")

    label("loc_17F65")


    ChrTalk(
        0x21,
        "#6PYou sure about that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#6PMy dad's always telling me that the police\x01",
            "are pathetic because they never arrest\x01",
            "corrupt government people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#12PR-Ryu, isn't that a little harsh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0006F...He has a point. Up until now, our efforts\x01",
            "haven't been enough. I'll admit it.\x02\x03",
            "#0000FAnd change may not be possible right this\x01",
            "very second, but you can count on us to\x01",
            "keep working towards being able to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#6PHey, you've got my support!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#12P*sigh* You're all talk, Ryu...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x12C)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#11P#0012FWell, then, any more questions? We\x01",
            "should have time for another.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(
        0x153,
        "#6P#1109F#NLloyd! Lloooooyd! I have a question!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(153250, 1500, 11180, 2000)
    SetCameraDistance(29120, 2000)
    OP_93(0x101, 0x87, 0x12C)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#11P#0011FKeA?! (Her silence WAS getting suspicious.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#6P#1105FSo, can I ask my question?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FS-Sure, go ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#6P#1110FI wanna know...\x02\x03",
            "...why did you become a police officer?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#0005F(Why did I join the CPD...?)\x02\x03",
            "#0003FU-Uh...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#11P#0008F(I asked myself the same thing the first night\x01",
            "I was assigned to the Special Support Section,\x01",
            "didn't I?)\x02\x03",
            "#0004F(You know...I think I have an answer now.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        "#6P#1105FLloyd? Still thinkin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0002FNo, I got it.\x02\x03",
            "#0003F(I don't think this necessarily has a\x01",
            "'right' answer.)\x02\x03",
            "(I just need to speak from the heart\x01",
            "and tell them how I've grown by being\x01",
            "a part of the Special Support Section.)\x02\x03",
            "#0000FThe reason I became a police officer was...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Why did Lloyd join the CPD?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① To Become Strong]\x01",         # 0
            "[② To Protect Everyone]\x01",      # 1
            "[③ Not Sure]\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_185FC"),
        (1, "loc_1883E"),
        (2, "loc_18A4B"),
        (SWITCH_DEFAULT, "loc_18D1F"),
    )


    label("loc_185FC")


    ChrTalk(
        0x101,
        (
            "#11P#0003F...Honestly, I'm at a loss.\x02\x03",
            "#0000FBut, if I were to pick something, I think it's\x01",
            "because I want to help those in need and\x01",
            "stop injustice.\x02\x03",
            "#0008FThing is, in order to do that, I have to\x01",
            "become stronger. A lot stronger...\x02\x03",
            "I think I've been able to do that, working\x01",
            "in the CPD, but...\x02\x03",
            "#0012FI must sound like a bracer.\x02\x03",
            "#0006FSorry, KeA. I know that wasn't a very\x01",
            "good answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#6P#1104FNo problem! I liked it, 'cause it told me\x01",
            "something about you, Lloyd.\x02\x03",
            "#1110FYou're really determined, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0002FHaha, yeah. You aren't wrong there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18D1F")

    label("loc_1883E")


    ChrTalk(
        0x101,
        (
            "#11P#0003F...Honestly, I'm at a loss.\x02\x03",
            "#0000FIf I were to pick something, it'd probably be\x01",
            "that I want to protect everyone.\x02\x03",
            "#0008FThat includes friends and family, of course,\x01",
            "but more specifically...\x02\x03",
            "...the people of Crossbell, I guess? Maybe\x01",
            "there's more to it than that...\x02\x03",
            "#0006FSorry, KeA. I know that wasn't a very good\x01",
            "answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#6P#1104FNo problem! I liked it, 'cause it told me\x01",
            "#1110Fsomething about you, Lloyd.\x02\x03",
            "You're really determined, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0002FHaha, yeah. You aren't wrong there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18D1F")

    label("loc_18A4B")


    ChrTalk(
        0x101,
        (
            "#11P#0006FTo be brutally honest, I don't know right now.\x02\x03",
            "#0008FIn the beginning, I just wanted to chase after\x01",
            "my role model, so I decided to join the CPD,\x01",
            "just like him.\x02\x03",
            "I don't think that's everything, though...\x02\x03",
            "#0003FMy desire to follow my brother's footsteps\x01",
            "hasn't changed, but I've been made painfully\x01",
            "aware just how hard surpassing him will be.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#11P#0011FS-Sorry, everyone. I know that probably\x01",
            "didn't make any sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#6P#1110FIt's all right! I liked it, 'cause it told me\x01",
            "something about you, Lloyd.\x02\x03",
            "#1109FWhen you set your mind on things, you\x01",
            "go after them with all your might!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FThanks, KeA. That means a lot.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18D1F")

    label("loc_18D1F")

    OP_68(151640, 2100, 12440, 2000)
    MoveCamera(329, 14, 0, 2000)
    SetCameraDistance(30960, 2000)
    OP_93(0x101, 0xB4, 0x12C)
    OP_6F(0x79)
    OP_93(0xC, 0x87, 0x12C)

    ChrTalk(
        0xC,
        (
            "#5PWith that, we will put a bow on\x01",
            "our Q&A section of the lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PMr. Bannings, your assistance today was\x01",
            "extremely helpful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PEveryone, make sure to tell him thanks, okay?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Children")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5SThank you, Mr. Bannings!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0x101,
        "#11P#0000FMy pleasure. I'll see you all later.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    ClearChrFlags(0x153, 0x4)
    OP_D5(0x1E)
    Return()

    # Function_45_11DE6 end

    def Function_46_18EAB(): pass

    label("Function_46_18EAB")

    OP_95(0xFE, 151000, 200, 17500, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_46_18EAB end

    def Function_47_18EC7(): pass

    label("Function_47_18EC7")

    OP_93(0xFE, 0x10E, 0x12C)
    OP_98(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_47_18EC7 end

    def Function_48_18EEA(): pass

    label("Function_48_18EEA")

    OP_68(7710, 2300, -90, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(26410, 0)
    SetChrPos(0xC, 7600, 0, 1320, 270)
    SetChrPos(0x101, 5570, 0, 1350, 90)
    SetChrPos(0xEF, 4380, 0, 2050, 90)
    SetChrPos(0x153, 4720, 0, 510, 90)
    Sleep(500)
    PlayBGM("ed7124", 0)
    SetCameraDistance(25410, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_19172")

    ChrTalk(
        0xC,
        (
            "#12PMarvelous work, Lloyd. Your assistance\x01",
            "today was greatly appreciated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAll the children seemed to have a ball\x01",
            "listening to your lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0009FWell, I sure hope so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12PNo need to be so humble.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PIt was an amazing, well-thought-out lesson.\x01",
            "I even learned quite a bit myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PRemembering how small you used to be and seeing you\x01",
            "teach like that has shown me how far you've come. That,\x01",
            "above all else, was my favorite part of the lesson.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x27, 0x1, 0x1)
    Jump("loc_19490")

    label("loc_19172")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_19320")

    ChrTalk(
        0xC,
        (
            "#12PFine work, Lloyd. Your assistance\x01",
            "today was greatly appreciated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAll the children seemed to have a ball\x01",
            "listening to your lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FWell, I sure hope so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PAt the very least, I learned\x01",
            "quite a bit during it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PRemembering how small you used to be and seeing\x01",
            "you teach has shown me how far you've come. That,\x01",
            "above all else, was my favorite part of the lesson.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x27, 0x1, 0x2)
    Jump("loc_19490")

    label("loc_19320")


    ChrTalk(
        0xC,
        (
            "#12PGood job, Lloyd. Your assistance\x01",
            "today was greatly appreciated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PThat said...you aren't much of a\x01",
            "studier anymore, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0006FY-Yeah... I'm so sorry about that\x01",
            "disaster of a lesson.\x02\x03",
            "You'd think a member of the force\x01",
            "would know a bit more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PNo, no, it's fine. I apologize for asking\x01",
            "this of you at such an inconvenient time.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x27, 0x1, 0x3)

    label("loc_19490")

    TurnDirection(0x153, 0x101, 500)

    ChrTalk(
        0x153,
        (
            "#5P#1109FI thought you were awesome, Lloyd!\x01",
            "Best teacher ever!\x02\x03",
            "#1100FI didn't really understand anything\x01",
            "you said, but it was still awesome!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_19547():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19547)
    Sleep(50)

    def lambda_19557():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_19557)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#0003FThat lesson probably went over\x01",
            "a lot of kids' heads, didn't it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_195B6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_195B6)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_197A8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_196B5")

    ChrTalk(
        0x102,
        (
            "#5P#0103FYou really should study up a bit, Lloyd.\x02\x03",
            "#0111FThough, the kids might have gained a\x01",
            "little familiarity with the police through\x01",
            "that sorry showing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006FAll's well that ends well, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_197A3")

    label("loc_196B5")


    ChrTalk(
        0x102,
        (
            "#5P#0104FI'm proud of you, Lloyd.\x02\x03",
            "#0100FI imagine the kids are a lot more familiar\x01",
            "with the police now, thanks to you and\x01",
            "your excellent teaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0004FI'm just thankful that I had the opportunity\x01",
            "to share with the class.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197A3")

    Jump("loc_19B9A")

    label("loc_197A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_199B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_198B2")

    ChrTalk(
        0x103,
        (
            "#5P#0203FThat certainly was an...entertaining class.\x02\x03",
            "#0211FI suppose, in a way, they became more\x01",
            "familiar with the police, albeit through\x01",
            "less than ideal teaching strategies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006FAll's well that ends well, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_199AF")

    label("loc_198B2")


    ChrTalk(
        0x103,
        (
            "#5P#0204FCongratulations, Lloyd. Your lesson\x01",
            "was able to end with minimal damage.\x02\x03",
            "#0202FIt seems as though the children have\x01",
            "a bright outlook on the police, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0004FI'm just thankful that I had the opportunity\x01",
            "to share with the class.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_199AF")

    Jump("loc_19B9A")

    label("loc_199B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19B9A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_19AB2")

    ChrTalk(
        0x104,
        (
            "#5P#0306FDude. What the hell were you talkin'\x01",
            "about up there?\x02\x03",
            "#0309FOh, well. It sounds like the kiddos got\x01",
            "a positive impression of the police, so\x01",
            "job well done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006FAll's well that ends well, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B9A")

    label("loc_19AB2")


    ChrTalk(
        0x104,
        (
            "#5P#0300FWhew, man. That went off without a hitch.\x02\x03",
            "#0309FSounds like the kids got a pretty positive\x01",
            "impression of the police, too. Atta boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0004FI'm just thankful that I had the opportunity\x01",
            "to share with the class.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B9A")


    def lambda_19B9F():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19B9F)

    def lambda_19BAC():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_19BAC)

    def lambda_19BB9():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_19BB9)

    ChrTalk(
        0xC,
        (
            "#12POnce again, thank you. Now, there's\x01",
            "still time left in my lesson, so I'm afraid\x01",
            "I'll have to excuse myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PKeA, if you would like, you are more\x01",
            "than welcome to come to this Sunday\x01",
            "School class whenever you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PI'm certain the other children would\x01",
            "love to have you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#5P#1110FOkie dokie! I'm kinda busy right now,\x01",
            "but I promise I'll come again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000F(It looks like KeA has really taken a\x01",
            "shine to Sunday School.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_19F0A")
    OP_2C(0x27, 0x3)

    ChrTalk(
        0xC,
        "#12PI can't wait.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12POh, Lloyd. I would love for you to take\x01",
            "this. A token of my gratitude.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x61),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x61, 1)

    ChrTalk(
        0x101,
        "#5P#0005FAre you sure this is okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PConsider it thanks for giving such a great\x01",
            "lesson while already being tied up. Please\x01",
            "accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12PWell, then, until next time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_19F58")

    label("loc_19F0A")


    ChrTalk(
        0xC,
        "#12PI'll be looking forward to it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12PWell, then, until next time.\x02",
    )

    CloseMessageWindow()

    label("loc_19F58")

    BeginChrThread(0xC, 3, 0, 49)
    WaitChrThread(0xC, 3)

    ChrTalk(
        0x101,
        (
            "#5P#0003FAll right. Time to get back on track.\x02\x03",
            "#0000FWe should make our way to St. Ursula.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A019")

    ChrTalk(
        0x102,
        (
            "#5P#0100FAgreed. Shall we wait for a bus\x01",
            "by the south exit?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0F2")

    label("loc_1A019")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A091")

    ChrTalk(
        0x103,
        (
            "#5P#0200FThat seems to be our best course\x01",
            "of action. We can wait for a bus by\x01",
            "the south exit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0F2")

    label("loc_1A091")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A0F2")

    ChrTalk(
        0x104,
        (
            "#5P#0300FRight on. I say we catch a ride on\x01",
            "the bus outside the south exit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A0F2")


    ChrTalk(
        0x153,
        "#5P#1110FAway we gooooo!\x02",
    )

    CloseMessageWindow()
    Sound(9, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Guest Lecturer for Sunday School]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 5570, 0, 1350, 90)
    SetChrPos(0xC, 150800, 200, 17500, 180)
    OP_29(0x27, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_48_18EEA end

    def Function_49_1A1A8(): pass

    label("Function_49_1A1A8")


    def lambda_1A1AD():
        OP_95(0xFE, 8600, 0, 1320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1A1AD)
    WaitChrThread(0xC, 1)

    def lambda_1A1CB():
        OP_95(0xFE, 8600, 0, 2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1A1CB)
    WaitChrThread(0xC, 1)

    def lambda_1A1E9():
        OP_95(0xFE, 11600, 0, 2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1A1E9)
    Sleep(1000)
    Sound(103, 0, 100, 0)

    def lambda_1A20C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1A20C)
    WaitChrThread(0xC, 1)
    Return()

    # Function_49_1A1A8 end

    def Function_50_1A21D(): pass

    label("Function_50_1A21D")

    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    Return()

    # Function_50_1A21D end

    def Function_51_1A236(): pass

    label("Function_51_1A236")

    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_63(0x10, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x21, 0x2)
    Sleep(300)
    OP_63(0x15, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x15, 0x1)
    Sleep(200)
    OP_63(0x11, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Return()

    # Function_51_1A236 end

    def Function_52_1A2A8(): pass

    label("Function_52_1A2A8")

    OP_64(0xFFFF)
    SetChrSubChip(0x21, 0x0)
    SetChrSubChip(0x15, 0x0)
    Return()

    # Function_52_1A2A8 end

    SaveToFile()

Try(main)
