from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1130.bin",                # FileName
        "c1130",                    # MapName
        "c1130",                    # Location
        0x0019,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 25, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1130",                  # 0
        "Cassal",                 # 1
        "Cassal",                 # 2
        "Novas",                  # 3
        "Shannah",                # 4
        "Shannah",                # 5
        "Abby",                   # 6
        "Abby",                   # 7
        "Miles",                  # 8
        "Tajik",                  # 9
        "Mariabell",              # 10
        "Lechter",                # 11
    ))

    AddCharChip((
        "chr/ch28200.itc",                   # 00
        "chr/ch28202.itc",                   # 01
        "chr/ch29402.itc",                   # 02
        "chr/ch20300.itc",                   # 03
        "chr/ch20302.itc",                   # 04
        "chr/ch34200.itc",                   # 05
        "chr/ch34202.itc",                   # 06
        "chr/ch20202.itc",                   # 07
        "chr/ch28102.itc",                   # 08
        "chr/ch05502.itc",                   # 09
        "chr/ch07400.itc",                   # 0A
    ))

    DeclNpc(29309,   4000,    -9439,   90,   261,  0x0, 0,   0,   0,   0,   1,   0,   4,   255,  0)
    DeclNpc(7699,    150,     7980,    270,  469,  0x0, 0,   1,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(18040,   180,     -9699,   180,  341,  0x0, 0,   2,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(3500,    0,       -6989,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(13199,   4000,    10529,   180,  341,  0x0, 0,   4,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(3500,    0,       -8789,   0,    389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(12649,   4000,    10529,   180,  341,  0x0, 1,   6,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(7699,    150,     7980,    270,  341,  0x0, 0,   7,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(10449,   180,     -12399,  300,  469,  0x0, 0,   8,   0,   255, 255, 0,   22,  255,  0)
    DeclNpc(30620,   4000,    -15439,  270,  469,  0x0, 0,   9,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(30540,   4000,    -10399,  90,   405,  0x0, 0,   10,  0,   0,   0,   0,   24,  255,  0)

    DeclActor(6290,    0,       8000,    1300,    7700,    1500,    7980,    0x007E, 0,  13, 0x0000)
    DeclActor(2750,    0,       11140,   1000,    2750,    1200,    11140,   0x007C, 0,  25, 0x0000)
    DeclActor(18610,   0,       -4500,   1000,    18610,   1200,    -4500,   0x007C, 0,  27, 0x0000)
    DeclActor(23750,   0,       -9500,   1000,    23750,   1200,    -9500,   0x007C, 0,  26, 0x0000)
    DeclActor(6500,    0,       -4500,   1000,    6500,    1200,    -4500,   0x007C, 0,  28, 0x0000)
    DeclActor(9300,    0,       -4500,   1000,    9300,    1200,    -4500,   0x007C, 0,  29, 0x0000)
    DeclActor(21300,   0,       -4500,   1000,    21300,   1200,    -4500,   0x007C, 0,  30, 0x0000)
    DeclActor(23750,   0,       -6600,   1000,    23750,   1200,    -6600,   0x007C, 0,  31, 0x0000)
    DeclActor(23750,   0,       -14700,  1000,    23750,   1200,    -14700,  0x007C, 0,  32, 0x0000)
    DeclActor(23750,   0,       -17600,  1000,    23750,   1200,    -17600,  0x007C, 0,  33, 0x0000)
    DeclActor(18500,   4000,    11800,   1000,    18500,   5200,    11800,   0x007C, 0,  34, 0x0000)
    DeclActor(21500,   4000,    11800,   1000,    21450,   5200,    11800,   0x007C, 0,  35, 0x0000)
    DeclActor(26400,   4000,    11800,   1000,    26400,   5200,    11800,   0x007C, 0,  36, 0x0000)
    DeclActor(29400,   4000,    11800,   1000,    29400,   5200,    11800,   0x007C, 0,  37, 0x0000)
    DeclActor(31800,   4000,    9200,    1000,    31750,   5200,    9200,    0x007C, 0,  38, 0x0000)
    DeclActor(31800,   4000,    6450,    1000,    31800,   5200,    6450,    0x007C, 0,  39, 0x0000)
    DeclActor(31800,   4000,    1440,    1000,    31800,   5200,    1440,    0x007C, 0,  40, 0x0000)
    DeclActor(31750,   4000,    -1650,   1000,    31750,   5200,    -1650,   0x007C, 0,  41, 0x0000)
    DeclActor(31750,   4000,    -6690,   1000,    31750,   5200,    -6690,   0x007C, 0,  42, 0x0000)

    ScpFunction((
        "Function_0_57C",          # 00, 0
        "Function_1_634",          # 01, 1
        "Function_2_6BD",          # 02, 2
        "Function_3_881",          # 03, 3
        "Function_4_980",          # 04, 4
        "Function_5_2501",         # 05, 5
        "Function_6_27AA",         # 06, 6
        "Function_7_45EC",         # 07, 7
        "Function_8_4768",         # 08, 8
        "Function_9_480E",         # 09, 9
        "Function_10_54FE",        # 0A, 10
        "Function_11_5540",        # 0B, 11
        "Function_12_5DBE",        # 0C, 12
        "Function_13_5EB2",        # 0D, 13
        "Function_14_5EC7",        # 0E, 14
        "Function_15_8203",        # 0F, 15
        "Function_16_8512",        # 10, 16
        "Function_17_8720",        # 11, 17
        "Function_18_8902",        # 12, 18
        "Function_19_8B98",        # 13, 19
        "Function_20_8C52",        # 14, 20
        "Function_21_8E7C",        # 15, 21
        "Function_22_8F74",        # 16, 22
        "Function_23_94A9",        # 17, 23
        "Function_24_A563",        # 18, 24
        "Function_25_AB23",        # 19, 25
        "Function_26_B040",        # 1A, 26
        "Function_27_B21C",        # 1B, 27
        "Function_28_B31E",        # 1C, 28
        "Function_29_B39D",        # 1D, 29
        "Function_30_B421",        # 1E, 30
        "Function_31_B49A",        # 1F, 31
        "Function_32_B520",        # 20, 32
        "Function_33_B641",        # 21, 33
        "Function_34_B6BF",        # 22, 34
        "Function_35_BD73",        # 23, 35
        "Function_36_C709",        # 24, 36
        "Function_37_CFA1",        # 25, 37
        "Function_38_D7CB",        # 26, 38
        "Function_39_DF99",        # 27, 39
        "Function_40_E93D",        # 28, 40
        "Function_41_EF43",        # 29, 41
        "Function_42_F2BE",        # 2A, 42
        "Function_43_F6EA",        # 2B, 43
        "Function_44_F966",        # 2C, 44
        "Function_45_FA97",        # 2D, 45
        "Function_46_FB93",        # 2E, 46
        "Function_47_10223",       # 2F, 47
        "Function_48_105CF",       # 30, 48
        "Function_49_10AE5",       # 31, 49
        "Function_50_10C90",       # 32, 50
        "Function_51_10D8C",       # 33, 51
        "Function_52_11A9B",       # 34, 52
        "Function_53_121EB",       # 35, 53
        "Function_54_123B4",       # 36, 54
    ))


    def Function_0_57C(): pass

    label("Function_0_57C")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_5BC"),
        (1, "loc_5C8"),
        (2, "loc_5D4"),
        (3, "loc_5E0"),
        (4, "loc_5EC"),
        (5, "loc_5F8"),
        (6, "loc_604"),
        (SWITCH_DEFAULT, "loc_610"),
    )


    label("loc_5BC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_5C8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_5D4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_5E0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_5EC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_5F8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_604")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_610")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_61C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_633")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_633")

    Return()

    # Function_0_57C end

    def Function_1_634(): pass

    label("Function_1_634")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6BC")
    OP_95(0xFE, 29310, 4000, 9100, 1000, 0x0)
    OP_95(0xFE, 17140, 4000, 9100, 1000, 0x0)
    OP_95(0xFE, 17140, 4000, 6840, 1000, 0x0)
    OP_95(0xFE, 27790, 4000, 6840, 1000, 0x0)
    OP_95(0xFE, 27790, 4000, -9440, 1000, 0x0)
    OP_95(0xFE, 29310, 4000, -9440, 1000, 0x0)
    Jump("Function_1_634")

    label("loc_6BC")

    Return()

    # Function_1_634 end

    def Function_2_6BD(): pass

    label("Function_2_6BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6F6")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F1")
    SetChrFlags(0xF, 0x80)

    label("loc_6F1")

    Jump("loc_86A")

    label("loc_6F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_704")
    Jump("loc_86A")

    label("loc_704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_712")
    Jump("loc_86A")

    label("loc_712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_720")
    Jump("loc_86A")

    label("loc_720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_733")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_86A")

    label("loc_733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_755")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_86A")

    label("loc_755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_777")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_86A")

    label("loc_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_799")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_86A")

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7BB")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_86A")

    label("loc_7BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7D8")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_86A")

    label("loc_7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7E6")
    Jump("loc_86A")

    label("loc_7E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7FE")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    Jump("loc_86A")

    label("loc_7FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_80C")
    Jump("loc_86A")

    label("loc_80C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_81A")
    Jump("loc_86A")

    label("loc_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_828")
    Jump("loc_86A")

    label("loc_828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_836")
    Jump("loc_86A")

    label("loc_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_844")
    Jump("loc_86A")

    label("loc_844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_852")
    Jump("loc_86A")

    label("loc_852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_86A")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_86A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_880")
    Event(0, 54)

    label("loc_880")

    Return()

    # Function_2_6BD end

    def Function_3_881(): pass

    label("Function_3_881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_893")
    OP_65(0x0, 0x1)

    label("loc_893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A8")
    OP_65(0x0, 0x1)

    label("loc_8A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C1")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_8C7")

    label("loc_8C1")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_8C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E3")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8FA")

    label("loc_8E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8FA")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8FA")

    label("loc_8FA")

    OP_65(0x4, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_913")
    OP_66(0x8, 0x1)

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_942")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_93E")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    OP_66(0x6, 0x1)
    Jump("loc_942")

    label("loc_93E")

    OP_65(0x3, 0x1)

    label("loc_942")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_95B")
    OP_66(0x2, 0x1)
    OP_66(0x4, 0x1)
    OP_66(0x6, 0x1)

    label("loc_95B")

    OP_65(0x5, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_97F")
    OP_66(0x5, 0x1)
    OP_66(0x7, 0x1)
    OP_66(0x9, 0x1)

    label("loc_97F")

    Return()

    # Function_3_881 end

    def Function_4_980(): pass

    label("Function_4_980")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_ADB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F6")

    ChrTalk(
        0xFE,
        "Oh, would you look at the time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd better get ready to close up.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A32")

    label("loc_9F6")


    ChrTalk(
        0xFE,
        (
            "The checkout and returns counter\x01",
            "will soon be closing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A32")

    Jump("loc_AD6")

    label("loc_A37")


    ChrTalk(
        0xFE,
        (
            "The director of the library is out\x01",
            "on official business right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, would you look at the time.\x01",
            "I'm responsible for closing up\x01",
            "the library today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD6")

    Jump("loc_24FD")

    label("loc_ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA3")

    ChrTalk(
        0xFE,
        (
            "Does Novas intend to have his face\x01",
            "buried in his books down to the very\x01",
            "last second again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's been awfully cheery this\x01",
            "last little while. Something good happen?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C75")

    label("loc_BA3")


    ChrTalk(
        0xFE,
        (
            "Oh, yes. I failed to mention this, but the\x01",
            "checking out of historical documents is\x01",
            "strictly prohibited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please inquire at the front desk during\x01",
            "our hours of operation if you'd like to\x01",
            "read them here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C75")

    Jump("loc_24FD")

    label("loc_C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D65")

    ChrTalk(
        0xFE,
        (
            "Boy, the weather is wonderful today!\x01",
            "Sounds like the perfect time to air\x01",
            "the dust out of these books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, they're not TOO terribly dirty.\x01",
            "I've seen worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "A light airing should do the trick.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DFB")

    label("loc_D65")


    ChrTalk(
        0xFE,
        (
            "This weather is making me want to\x01",
            "go out on a picnic, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll go out on a stroll and get\x01",
            "some fresh air during my break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DFB")

    Jump("loc_24FD")

    label("loc_E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_F2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA7")

    ChrTalk(
        0xFE,
        "I'm placing new books on the shelves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This author's works are all the rage\x01",
            "right now, so I'm sure our visitors\x01",
            "will be delighted.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F27")

    label("loc_EA7")


    ChrTalk(
        0xFE,
        "This author's works are all the rage right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd suggest getting a copy now if\x01",
            "you're planning on reading it, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F27")

    Jump("loc_24FD")

    label("loc_F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1023")

    ChrTalk(
        0xFE,
        (
            "You said you were looking for a\x01",
            "children's book? Let me think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We have a corner devoted to them.\x01",
            "Just take a right as you enter the library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Their popularity speaks for itself.\x01",
            "They're always flying off the shelves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24FD")

    label("loc_1023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_114E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C6")

    ChrTalk(
        0xFE,
        (
            "I've been taking care of some much-\x01",
            "needed cleaning today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's an opportune time to do it,\x01",
            "since there aren't many visitors.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1149")

    label("loc_10C6")


    ChrTalk(
        0xFE,
        "I managed to wake up bright and early today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're closing at 2PM today, so be sure\x01",
            "to check out your books before then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1149")

    Jump("loc_24FD")

    label("loc_114E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_128B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1213")

    ChrTalk(
        0xFE,
        (
            "Who would've thought the second floor\x01",
            "of the library would serve as first-class\x01",
            "seats for the parade?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha. I think I'll keep this little\x01",
            "secret to myself...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1286")

    label("loc_1213")


    ChrTalk(
        0xFE,
        (
            "I doubt even the director himself\x01",
            "knows about this sweet little spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha. This'll be my little secret.\x02",
    )

    CloseMessageWindow()

    label("loc_1286")

    Jump("loc_24FD")

    label("loc_128B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_140B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1363")

    ChrTalk(
        0xFE,
        "Gosh, it's more rambunctious than usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can still hear the bustle of the parade\x01",
            "from the confines of the library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think I'll take a little stroll during my lunch break.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1406")

    label("loc_1363")


    ChrTalk(
        0xFE,
        (
            "Y'know, Crossbellans ARE known for\x01",
            "being convivial...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I must say, I can absolutely relate.\x01",
            "I feel my Crossbellan heritage\x01",
            "coursing through my veins.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1406")

    Jump("loc_24FD")

    label("loc_140B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_149F")

    ChrTalk(
        0xFE,
        (
            "I always have trouble sorting through\x01",
            "returned books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must seize the opportunity to reshelve\x01",
            "them while business is slow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24FD")

    label("loc_149F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1662")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A1")

    ChrTalk(
        0xFE,
        (
            "Good morning, welcome to the Crossbell\x01",
            "City Library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew traffic would slow down during the\x01",
            "Anniversary Festival, but this is just sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, who am I to judge? There's no\x01",
            "better time to go out and enjoy yourself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_165D")

    label("loc_15A1")


    ChrTalk(
        0xFE,
        (
            "Ah, right. Please abide by the rules of\x01",
            "the library. No food or drink allowed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That means you'd better leave behind\x01",
            "any of those tasty treats you purchased\x01",
            "from the food stalls.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165D")

    Jump("loc_24FD")

    label("loc_1662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_17CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1760")

    ChrTalk(
        0xFE,
        (
            "The director is taking some time off\x01",
            "during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not nearly as busy during that period,\x01",
            "so he can afford to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be fine on my own, though admittedly,\x01",
            "it will be a little bit lonely...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17CA")

    label("loc_1760")


    ChrTalk(
        0xFE,
        "The director usually handles this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to seize this opportunity to\x01",
            "prove that I am capable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17CA")

    Jump("loc_24FD")

    label("loc_17CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_192D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1884")

    ChrTalk(
        0xFE,
        (
            "I heard a loud crashing noise\x01",
            "from the basement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew... I'm just glad the director\x01",
            "was unharmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Some of those books can get quite hefty.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1928")

    label("loc_1884")


    ChrTalk(
        0xFE,
        "I'm just glad the director came out unharmed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I must admit... Seeing the director buried\x01",
            "beneath a mountain of books was truly a\x01",
            "spectacle to behold.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1928")

    Jump("loc_24FD")

    label("loc_192D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1A85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19EE")

    ChrTalk(
        0xFE,
        (
            "Tickets for the new Arc en Ciel show\x01",
            "have sold out already, haven't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe I should have stayed in line.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have a knack for giving up too easily.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A80")

    label("loc_19EE")


    ChrTalk(
        0xFE,
        (
            "Speaking of Arc en Ciel, we have a\x01",
            "collection of their past performances,\x01",
            "as well as photo albums.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They're usually checked out, though.\x02",
    )

    CloseMessageWindow()

    label("loc_1A80")

    Jump("loc_24FD")

    label("loc_1A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1CC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C00")

    ChrTalk(
        0xFE,
        (
            "The director comes to work outside\x01",
            "our hours of operation to organize\x01",
            "the books on the shelves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not meant to serve his bibliophilic\x01",
            "desires, but to improve the quality of\x01",
            "service for our patrons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know 'Library Director' doesn't sound like\x01",
            "a flashy title, but he's one of the finest men\x01",
            "I've ever had the pleasure of working with.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CC0")

    label("loc_1C00")


    ChrTalk(
        0xFE,
        (
            "He even goes as far as to mow the\x01",
            "front lawn!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know 'Library Director' doesn't sound like\x01",
            "a flashy title, but he's one of the finest men\x01",
            "I've ever had the pleasure of working with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC0")

    Jump("loc_24FD")

    label("loc_1CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1EB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E05")

    ChrTalk(
        0xFE,
        (
            "My parents suggested I look into\x01",
            "becoming a public servant,\x01",
            "so I obliged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Most people perceive public servants as\x01",
            "unappreciated, unrewarded workers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, you know what? I work on a nice, quiet\x01",
            "street for a man I respect and trust. That in\x01",
            "itself is a more than adequate reward.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EAE")

    label("loc_1E05")


    ChrTalk(
        0xFE,
        (
            "My parents suggested I look into\x01",
            "becoming a public servant,\x01",
            "so I obliged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It pays well, and I have a quiet workspace\x01",
            "all to myself. I've taken a liking to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EAE")

    Jump("loc_24FD")

    label("loc_1EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2041")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F99")

    ChrTalk(
        0xFE,
        (
            "You're looking for the fairy tale about\x01",
            "the white wolf?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I remember seeing it over on the first\x01",
            "floor in the children's reading section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I imagine you'll have luck finding it\x01",
            "in that area.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_203C")

    label("loc_1F99")


    ChrTalk(
        0xFE,
        (
            "The fairy tale about the white wolf should\x01",
            "be on the first floor, in the children's\x01",
            "reading section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I imagine you'll have luck finding it\x01",
            "in that area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_203C")

    Jump("loc_24FD")

    label("loc_2041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_21AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2120")

    ChrTalk(
        0xFE,
        "Let's see, this book is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've worked here for five years, but there\x01",
            "are many books I've yet to discover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We have a collection of books so vast\x01",
            "that I manage to get lost at times.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21A6")

    label("loc_2120")


    ChrTalk(
        0xFE,
        (
            "This library has a very large catalog\x01",
            "of books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've improved at handling it, but I cannot\x01",
            "hope to compare to the director.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A6")

    Jump("loc_24FD")

    label("loc_21AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_238C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B5")

    ChrTalk(
        0xFE,
        "The director is a bona fide bibliophile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The director managed to bury himself under\x01",
            "a mountain of books the other day. He was\x01",
            "working too hastily and lost his footing, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Boy, was I surprised to see him in that state.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2387")

    label("loc_22B5")


    ChrTalk(
        0xFE,
        (
            "The director managed to bury himself under\x01",
            "a mountain of books the other day.\x01",
            "Boy, was I surprised to see him in that state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I must admit, if I'm being entirely truthful,\x01",
            "I found it most amusing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2387")

    Jump("loc_24FD")

    label("loc_238C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_24FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247A")

    ChrTalk(
        0xFE,
        (
            "We're competing with libraries from\x01",
            "neighboring nations to have the\x01",
            "most updated catalog of books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We don't have the manpower to compete.\x01",
            "We haven't finished accounting for all\x01",
            "of our collection, yet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24FD")

    label("loc_247A")


    ChrTalk(
        0xFE,
        (
            "We don't have the manpower to register\x01",
            "our broad collection of books. The public\x01",
            "won't be able to read them until we do, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24FD")

    TalkEnd(0xFE)
    Return()

    # Function_4_980 end

    def Function_5_2501(): pass

    label("Function_5_2501")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2595")
    Jump("loc_25DF")

    label("loc_2595")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25B5")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25DF")

    label("loc_25B5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25D5")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25DF")

    label("loc_25D5")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25DF")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26F8")

    ChrTalk(
        0x9,
        (
            "Good morning. Welcome to\x01",
            "the Crossbell City Library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm afraid the librarian isn't in yet, as he's\x01",
            "scheduled to work this afternoon.\x01",
            "I am similarly able to help you, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Treat me the same as you would him.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27A2")

    label("loc_26F8")


    ChrTalk(
        0x9,
        (
            "Miles is scheduled to work the\x01",
            "afternoon shift today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Treat me the same as you would him.\x01",
            "I am similarly able to help you with\x01",
            "checking out or returning books.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27A2")

    SetChrSubChip(0x9, 0x0)
    TalkEnd(0x9)
    Return()

    # Function_5_2501 end

    def Function_6_27AA(): pass

    label("Function_6_27AA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_283E")
    Jump("loc_2888")

    label("loc_283E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_285E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2888")

    label("loc_285E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_287E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2888")

    label("loc_287E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2888")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_292B")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        "Oh? Oh! What's this?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm on the verge of completing my thesis!\x01",
            "All I have to do is summarize it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45E4")

    label("loc_292B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2A85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A3C")

    ChrTalk(
        0xFE,
        (
            "I found an absolute treasure trove of data.\x01",
            "It won't be easy to incorporate all of it,\x01",
            "so I'll have to pick and choose the best stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You've gotta hand it to this library.\x01",
            "They've done a great job of giving\x01",
            "me the answers I've needed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A80")

    label("loc_2A3C")


    ChrTalk(
        0xFE,
        (
            "Okay, let's do this! It's full steam\x01",
            "ahead until closing time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A80")

    Jump("loc_45E4")

    label("loc_2A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7D")

    ChrTalk(
        0xFE,
        (
            "I got my hands on some pretty interesting\x01",
            "documents today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This here is the memoir of a trader's\x01",
            "exploits from 80 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is definitely a valuable relic that'll\x01",
            "help contextualize Crossbell's past.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C30")

    label("loc_2B7D")


    ChrTalk(
        0xFE,
        (
            "If you think about it, Crossbell hadn't even\x01",
            "been established as an autonomous\x01",
            "state 80 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The region suffered from instability,\x01",
            "which caused traders to suffer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C30")

    Jump("loc_45E4")

    label("loc_2C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2D12")

    ChrTalk(
        0xFE,
        "I've decided to abandon writing my thesis.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to settle down and redirect\x01",
            "my efforts wholly into research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a vast, unexplored sea of information\x01",
            "waiting to be discovered by me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45E4")

    label("loc_2D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2E75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE2")

    ChrTalk(
        0xFE,
        (
            "What? Do you have something to say to me,\x01",
            "the man who's had to repeat a year?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1100F...? That guy's a weirdo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ack!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E70")

    label("loc_2DE2")


    ChrTalk(
        0xFE,
        (
            "Haha... Hahahahaha...\x01",
            "Looks like my thesis won't be completed\x01",
            "in time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter. I'll just have to hang in there for\x01",
            "another year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E70")

    Jump("loc_45E4")

    label("loc_2E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2FDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F43")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "W-Wait, what time is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is bad... I should already be on my way\x01",
            "to the airport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I probably won't make it in time to\x01",
            "present my thesis...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FDA")

    label("loc_2F43")


    ChrTalk(
        0xFE,
        "I'm enrolled at a university in Leman State.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(*grumble* If I'm not careful about how\x01",
            "I calculate travel time, I might end up\x01",
            "not making it.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FDA")

    Jump("loc_45E4")

    label("loc_2FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_31BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_313A")

    ChrTalk(
        0xFE,
        (
            "The 'bell' in 'Crossbell' holds a special meaning,\x01",
            "relating back to ancient times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Supposedly, they symbolized a marketplace\x01",
            "opening, a wagon departing, or even an\x01",
            "incoming invasion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Furthermore, the ringing of the bell at\x01",
            "Crossbell Cathedral appears to be a\x01",
            "tradition that dates back to the Middle Ages.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31B8")

    label("loc_313A")


    ChrTalk(
        0xFE,
        (
            "Wh-Whoops, I almost slipped out of\x01",
            "consciousness for a second there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I may have worked myself a tad bit too hard...\x02",
    )

    CloseMessageWindow()

    label("loc_31B8")

    Jump("loc_45E4")

    label("loc_31BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_33B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3383")

    ChrTalk(
        0xFE,
        (
            "Hahaha... There's a festival going on\x01",
            "outside, but I'm stuck here writing my thesis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In case you were curious, the parade\x01",
            "began when an influential man put out\x01",
            "a float to celebrate Crossbell's anniversary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've become accustomed to commemorating\x01",
            "Crossbell's anniversary with a float parade\x01",
            "ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The parade even has the financial backing\x01",
            "of influential businessmen and large\x01",
            "corporations these days.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_33B1")

    label("loc_3383")


    ChrTalk(
        0xFE,
        "Everybody looks like they're having fun.\x02",
    )

    CloseMessageWindow()

    label("loc_33B1")

    Jump("loc_45E4")

    label("loc_33B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_358E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F0")

    ChrTalk(
        0xFE,
        (
            "Crossbell has been at the forefront of trading\x01",
            "as far back as the Middle Ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its geographical advantages made it an important\x01",
            "trade center for the western part of the continent.\x01",
            "It's as if man and mira naturally gravitated here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That fact remains unchanged to this day.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3589")

    label("loc_34F0")


    ChrTalk(
        0xFE,
        (
            "These days, we've got railroads and airships\x01",
            "coming in and out of the state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It wouldn't be a stretch to say that it's\x01",
            "become truer than ever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3589")

    Jump("loc_45E4")

    label("loc_358E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_36C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_368F")

    ChrTalk(
        0xFE,
        (
            "Whoa, the Anniversary Festival snuck up\x01",
            "so quickly that it caught me off guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, no! My thesis is due this month!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I'm going to put it all together, I can't\x01",
            "spend more time reading through\x01",
            "reference materials.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_36BE")

    label("loc_368F")


    ChrTalk(
        0xFE,
        "H-How could I forget about the deadline?!\x02",
    )

    CloseMessageWindow()

    label("loc_36BE")

    Jump("loc_45E4")

    label("loc_36C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3815")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_376A")

    ChrTalk(
        0xFE,
        (
            "Wait, what?! You're going to investigate\x01",
            "Stargazer's Tower?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's so unfair! I've been trying\x01",
            "to explore that place for ages...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3810")

    label("loc_376A")


    ChrTalk(
        0xFE,
        (
            "Stargazer's Tower is a historical\x01",
            "landmark constructed during the\x01",
            "Middle Ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, promise me you'll preserve\x01",
            "the contents in their original condition!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3810")

    Jump("loc_45E4")

    label("loc_3815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3979")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D5")

    ChrTalk(
        0xFE,
        (
            "The director won't let me enter the\x01",
            "archive room inside of the basement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's supposedly dangerous or something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm? How can a library be dangerous?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3974")

    label("loc_38D5")


    ChrTalk(
        0xFE,
        (
            "He offered to search for any reference\x01",
            "materials I was looking for himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is there a deeper meaning behind him\x01",
            "claiming the basement is dangerous?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3974")

    Jump("loc_45E4")

    label("loc_3979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3B54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ADF")

    ChrTalk(
        0xFE,
        (
            "The deadline for my thesis draws near.\x01",
            "I'm going to have to repeat the year if\x01",
            "I don't pick up the pace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahem. First things first, I've gotta ask the\x01",
            "director to let me search for something\x01",
            "in the archive room downstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a whole slew of information that I don't\x01",
            "understand with the material I've got on me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B4F")

    label("loc_3ADF")


    ChrTalk(
        0xFE,
        (
            "The archive room apparently contains\x01",
            "a plethora of antique books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd love to investigate down there.\x02",
    )

    CloseMessageWindow()

    label("loc_3B4F")

    Jump("loc_45E4")

    label("loc_3B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3D30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CAE")

    ChrTalk(
        0xFE,
        (
            "I bet you didn't know this, but this\x01",
            "very library is a historical landmark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The original traders of Crossbell used to\x01",
            "store their ledgers inside of this building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why you're able to find books\x01",
            "dating back 300 years here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I daresay this place is an absolute gold mine\x01",
            "for a historian like me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3D2B")

    label("loc_3CAE")


    ChrTalk(
        0xFE,
        (
            "This library managed to inherit those\x01",
            "very same historical documents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's a shame they're not publicly available.\x02",
    )

    CloseMessageWindow()

    label("loc_3D2B")

    Jump("loc_45E4")

    label("loc_3D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3FE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F45")

    ChrTalk(
        0xFE,
        (
            "Not many people know this, but there are\x01",
            "still some intact ruins from the Middle Ages\x01",
            "present in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The most famous one is the Ancient Battlefield,\x01",
            "a fortress on the outskirts of the Old Armorica\x01",
            "Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A group of researchers formed an expedition\x01",
            "team around 20 years ago to search through\x01",
            "the ruins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I recall correctly, they excavated that\x01",
            "giant bell sitting right in the middle of\x01",
            "Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm pretty sure they found it somewhere\x01",
            "around the Ancient Battlefield.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3FDC")

    label("loc_3F45")


    ChrTalk(
        0xFE,
        (
            "That's not the only famous ruin around\x01",
            "these parts, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish I didn't have to deal with this thesis.\x01",
            "I really want to go and see them!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FDC")

    Jump("loc_45E4")

    label("loc_3FE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_41D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_414D")

    ChrTalk(
        0xFE,
        (
            "There's hardly anyone knowledgeable\x01",
            "about Crossbell's rich history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sure, someone might be able to tell you history\x01",
            "about the last 50 years. But, go back 200--no,\x01",
            "100 years, and there's zilch. Nada.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to delve into the finer details of how\x01",
            "modern day Crossbell came to be, but\x01",
            "I don't think the average person cares.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_41D4")

    label("loc_414D")


    ChrTalk(
        0xFE,
        (
            "Crossbellans don't care for enriching\x01",
            "themselves with the deep history of\x01",
            "their land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "For a researcher like me, it's tragic.\x02",
    )

    CloseMessageWindow()

    label("loc_41D4")

    Jump("loc_45E4")

    label("loc_41D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4373")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42CE")

    ChrTalk(
        0xFE,
        "Researching history can be challenging.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You have to rummage through countless\x01",
            "old books, collect folklore, and visit the\x01",
            "occasional historical landmark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It is truly the field of investigating the truth.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_436E")

    label("loc_42CE")


    ChrTalk(
        0xFE,
        (
            "Historical research is essentially the\x01",
            "investigation of supposed facts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I may be a researcher, but I don't deny\x01",
            "that it can be a dull field to study.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_436E")

    Jump("loc_45E4")

    label("loc_4373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4496")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_438E")
    Call(0, 7)
    Jump("loc_4491")

    label("loc_438E")


    ChrTalk(
        0xFE,
        (
            "There's hardly ever new materials to research.\x01",
            "I had to beg the director with tears in my eyes\x01",
            "to show me some of his ancient books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, I wonder if this'll be enough...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to end up repeating the year if\x01",
            "I don't finish up this thesis.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4491")

    Jump("loc_45E4")

    label("loc_4496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_45E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44B1")
    Call(0, 7)
    Jump("loc_45E4")

    label("loc_44B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4555")

    ChrTalk(
        0xFE,
        "Crossbell Folklore, Mainz Local History...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's hopeless. There's just not enough material!\x01",
            "At this rate, I'm never going to make it...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_45E4")

    label("loc_4555")


    ChrTalk(
        0xFE,
        "I'm here researching Crossbellan history.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not going to finish my thesis at this rate.\x01",
            "I can't find any good research material...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45E4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_27AA end

    def Function_7_45EC(): pass

    label("Function_7_45EC")


    ChrTalk(
        0xFE,
        (
            "*sigh* Who would have thought writing\x01",
            "a thesis could be this difficult?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I purchased this novel a while before I started\x01",
            "my thesis, hoping to read and relax during my\x01",
            "downtime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, hey there. Would you like to\x01",
            "take this book off my hands?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm too busy to even consider reading it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2C6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2C6, 1)
    SetScenarioFlags(0x9C, 0)
    Return()

    # Function_7_45EC end

    def Function_8_4768(): pass

    label("Function_8_4768")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I had this book recommended to me by\x01",
            "the librarian, so I'm going to check it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He kept bothering me to read it to\x01",
            "its conclusion in my free time.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_4768 end

    def Function_9_480E(): pass

    label("Function_9_480E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_48A2")
    Jump("loc_48EC")

    label("loc_48A2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_48C2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48EC")

    label("loc_48C2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48E2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48EC")

    label("loc_48E2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48EC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_491F")
    Jump("loc_54F6")

    label("loc_491F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4C90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_END)), "loc_4AF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A2C")

    ChrTalk(
        0xFE,
        (
            "At long last, the final volume of Mark and the\x01",
            "Witch of the Deep Forest has arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is, bar none, the most popular\x01",
            "fairy tale in the library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Abby was completely engrossed with\x01",
            "every word while I read it to him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4AEB")

    label("loc_4A2C")


    ChrTalk(
        0xFE,
        (
            "Mark and the Witch of the Deep Forest is,\x01",
            "bar none, the most popular fairy tale in\x01",
            "this library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did you want to read it, too? You'll\x01",
            "be able to find it on the first floor shelves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AEB")

    Jump("loc_4C8B")

    label("loc_4AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B02")
    Call(0, 12)
    Jump("loc_4C8B")

    label("loc_4B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BF6")

    ChrTalk(
        0xFE,
        (
            "Abby's trying to show KeA a book\x01",
            "he enjoyed reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He hasn't been bothering all of\x01",
            "you, has he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0204FNot in the slightest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWe don't bring KeA out here often,\x01",
            "but I hope you'll play with her again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C8B")

    label("loc_4BF6")


    ChrTalk(
        0xFE,
        (
            "Abby's a bit of a bookworm. He'll have\x01",
            "his nose deep in a book as long as\x01",
            "the library is open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think he's grown to be\x01",
            "quite fond of KeA.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C8B")

    Jump("loc_54F6")

    label("loc_4C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4D00")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "The officer ran, ran, ran with all of\x01",
            "their might.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yet, the piggy still got away...\x02",
    )

    CloseMessageWindow()
    Jump("loc_54F6")

    label("loc_4D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4DC1")

    ChrTalk(
        0xFE,
        (
            "Abby kept asking me to read him\x01",
            "stories about police officers ever\x01",
            "since the Anniversary Festival ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heehee. I think he's completely\x01",
            "infatuated with their uniforms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54F6")

    label("loc_4DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4E32")

    ChrTalk(
        0xFE,
        (
            "Oh? I'm surprised there's another\x01",
            "child older than Abby here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope you become friends.\x02",
    )

    CloseMessageWindow()
    Jump("loc_54F6")

    label("loc_4E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4EC2")

    ChrTalk(
        0xFE,
        (
            "Oh, that's no good. It's already\x01",
            "getting pretty late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should go get some shopping done\x01",
            "and then head home afterwards.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54F6")

    label("loc_4EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4ED0")
    Jump("loc_54F6")

    label("loc_4ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4F71")

    ChrTalk(
        0xFE,
        (
            "My son has asked me to read him\x01",
            "his favorite book, over and over\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad he likes it, but I've read it\x01",
            "for the fifth time today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54F6")

    label("loc_4F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5056")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "And then, the voice of the Goddess\x01",
            "was carried to her ears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'Come forth, for the path has appeared.\x01",
            "Return to your friends.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The fox began to sprint as hard as\x01",
            "she could upon hearing those words.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54F6")

    label("loc_5056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_518C")

    ChrTalk(
        0xFE,
        (
            "On the topic of Aidios, Crossbell Cathedral's\x01",
            "architectural work is an absolute marvel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hear it's home to a number of\x01",
            "exceptional priests and sisters, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Abby will attend Sunday School there\x01",
            "starting next year, so I think I'll go\x01",
            "and offer a prayer sometime soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5214")

    label("loc_518C")


    ChrTalk(
        0xFE,
        (
            "I haven't gone to the cathedral\x01",
            "once since moving to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Abby loves the Goddess, so I'm sure\x01",
            "he'll be delighted to go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5214")

    Jump("loc_54F6")

    label("loc_5219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_52BC")

    ChrTalk(
        0xFE,
        (
            "It's a relief that the library carries so\x01",
            "many children's books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a bit sad that hardly anyone uses the library.\x01",
            "I wonder why that is?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54F6")

    label("loc_52BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5357")

    ChrTalk(
        0xFE,
        "I just recently moved to Crossbell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I love that Crossbell gives off a\x01",
            "picturesque vibe. It's a great\x01",
            "place to live, in my opinion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54F6")

    label("loc_5357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_53A5")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        "Suddenly, a terrifying demon appeared.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Bwahahaha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_54F6")

    label("loc_53A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_54F6")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5478")

    ChrTalk(
        0xFE,
        (
            "Then, the Goddess emanated a\x01",
            "radiant light upon the world.\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0xFE,
        "That very light engulfed the entire world.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The animals were astonished at what\x01",
            "they were seeing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_54F6")

    label("loc_5478")


    ChrTalk(
        0xFE,
        (
            "The radiant light emanated by the Goddess\x01",
            "engulfed the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The animals were astonished at what\x01",
            "they were seeing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54F6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_480E end

    def Function_10_54FE(): pass

    label("Function_10_54FE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm going to make Mom read it to me\x01",
            "when we get home!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_54FE end

    def Function_11_5540(): pass

    label("Function_11_5540")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_55D4")
    Jump("loc_561E")

    label("loc_55D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_55F4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_561E")

    label("loc_55F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5614")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_561E")

    label("loc_5614")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_561E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5651")
    Jump("loc_5DB2")

    label("loc_5651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_571E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_END)), "loc_56C5")

    ChrTalk(
        0xFE,
        "I wanna know what happens in the next book.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come on, can we read it now?! Can we?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5719")

    label("loc_56C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56D7")
    Call(0, 12)
    Jump("loc_5719")

    label("loc_56D7")


    ChrTalk(
        0xFE,
        (
            "I'm totally gonna tell KeA to read this\x01",
            "next time I see her!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5719")

    Jump("loc_5DB2")

    label("loc_571E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5755")
    SetChrSubChip(0xFE, 0x1)

    ChrTalk(
        0xFE,
        "Whoa, police officers are cool!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DB2")

    label("loc_5755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5862")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_583E")

    ChrTalk(
        0xFE,
        "Hey, where's KeA? I wanna see her!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha, sorry, little guy. She isn't\x01",
            "with us today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102FWe'll be sure to bring her with us\x01",
            "next time, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Okay. I can't wait to see her again!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_585D")

    label("loc_583E")


    ChrTalk(
        0xFE,
        "Tell her I said hi, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_585D")

    Jump("loc_5DB2")

    label("loc_5862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5A7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A29")

    ChrTalk(
        0xFE,
        "Yay! Mom's going to read me a book!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1110FOoh, I wanna listen!\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Oh, do you like books, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sweet! We're the same!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FYeah, totally!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_5984")

    ChrTalk(
        0x102,
        (
            "#0102F(How very much like children to\x01",
            "become friends so easily.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A21")

    label("loc_5984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_59CA")

    ChrTalk(
        0x103,
        (
            "#0204F(Children are very adept at\x01",
            "making friends.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A21")

    label("loc_59CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_5A21")

    ChrTalk(
        0x104,
        (
            "#0302F(Leave it up to the kiddos to become\x01",
            "pals in the blink of an eye.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A21")

    SetScenarioFlags(0x0, 4)
    Jump("loc_5A79")

    label("loc_5A29")


    ChrTalk(
        0xFE,
        "Let's play together next time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1110FSure, sounds fun!\x01",
            "See you again!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A79")

    Jump("loc_5DB2")

    label("loc_5A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5AAE")
    SetChrSubChip(0xFE, 0x1)

    ChrTalk(
        0xFE,
        "Mom! What happens next?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DB2")

    label("loc_5AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5ABC")
    Jump("loc_5DB2")

    label("loc_5ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5B1E")
    SetChrSubChip(0xFE, 0x1)

    ChrTalk(
        0xFE,
        "I really like this book.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Goddess is in it, and I really\x01",
            "like Her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DB2")

    label("loc_5B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5B78")

    ChrTalk(
        0xFE,
        "Wow! I'm so excited!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't wait! Mom's going to read\x01",
            "me a book!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DB2")

    label("loc_5B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5BFC")

    ChrTalk(
        0xFE,
        "Hey, hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard there's a biiiiiiig church called\x01",
            "a ca-thee-dral over that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wanna go see it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DB2")

    label("loc_5BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5C2C")
    SetChrSubChip(0xFE, 0x1)

    ChrTalk(
        0xFE,
        "Mom! What happens next?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DB2")

    label("loc_5C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5D45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CCE")

    ChrTalk(
        0xFE,
        "Hey, hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I grow up, I wanna become\x01",
            "a priest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And when I become one, I'm going to\x01",
            "read books to all of the kids.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5D40")

    label("loc_5CCE")


    ChrTalk(
        0xFE,
        (
            "When I grow up, I wanna become\x01",
            "a priest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll read books to all the little kids, just\x01",
            "like my mom does.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D40")

    Jump("loc_5DB2")

    label("loc_5D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5D82")
    SetChrSubChip(0xFE, 0x1)

    ChrTalk(
        0xFE,
        (
            "Whoaaaa...\x01",
            "What's gonna happen next?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DB2")

    label("loc_5D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5DB2")
    SetChrSubChip(0xFE, 0x1)

    ChrTalk(
        0xFE,
        "Wow!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What happens next?!\x02",
    )

    CloseMessageWindow()

    label("loc_5DB2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_11_5540 end

    def Function_12_5DBE(): pass

    label("Function_12_5DBE")

    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xE, 0x0)

    ChrTalk(
        0xC,
        (
            "And with that, everyone lived\x01",
            "happily ever after.\x01",
            "The end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Wasn't that an interesting book, Abby?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yeah, totally!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm going to tell KeA to read this\x01",
            "book next time I see her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'm sure she'll like it, too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_12_5DBE end

    def Function_13_5EB2(): pass

    label("Function_13_5EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5EC3")
    Call(0, 14)
    Jump("loc_5EC6")

    label("loc_5EC3")

    Call(0, 5)

    label("loc_5EC6")

    Return()

    # Function_13_5EB2 end

    def Function_14_5EC7(): pass

    label("Function_14_5EC7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F5B")
    Jump("loc_5FA5")

    label("loc_5F5B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F7B")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FA5")

    label("loc_5F7B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F9B")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FA5")

    label("loc_5F9B")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FA5")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5FDB")
    Call(0, 21)
    Jump("loc_81FB")

    label("loc_5FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_621A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_609E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6001")
    Call(0, 20)
    Jump("loc_6099")

    label("loc_6001")


    ChrTalk(
        0xF,
        (
            "Thanks, Lloyd. As you might imagine,\x01",
            "we're far too understaffed to handle\x01",
            "this task on our own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I'll contact you if there are any updates.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_6099")

    Jump("loc_6215")

    label("loc_609E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60C3")
    Call(0, 52)
    Jump("loc_6215")

    label("loc_60C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_61E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_60E1")
    Call(0, 20)
    Jump("loc_61E4")

    label("loc_60E1")


    ChrTalk(
        0xF,
        (
            "I'm counting on you to collect those\x01",
            "overdue books for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Everyone who checked out a book appears\x01",
            "to live on the outskirts of the state, so feel\x01",
            "free to take your time on this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Please return to me once you've collected\x01",
            "all three books.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_61E4")

    Jump("loc_6215")

    label("loc_61E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_61FE")
    Call(0, 49)
    Jump("loc_6215")

    label("loc_61FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6212")
    Call(0, 48)
    Jump("loc_6215")

    label("loc_6212")

    Call(0, 20)

    label("loc_6215")

    Jump("loc_81FB")

    label("loc_621A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6459")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_62DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6240")
    Call(0, 19)
    Jump("loc_62D8")

    label("loc_6240")


    ChrTalk(
        0xF,
        (
            "Thanks, Lloyd. As you might imagine,\x01",
            "we're far too understaffed to handle\x01",
            "this task on our own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I'll contact you if there are any updates.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_62D8")

    Jump("loc_6454")

    label("loc_62DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6302")
    Call(0, 52)
    Jump("loc_6454")

    label("loc_6302")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_6428")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6320")
    Call(0, 19)
    Jump("loc_6423")

    label("loc_6320")


    ChrTalk(
        0xF,
        (
            "I'm counting on you to collect those\x01",
            "overdue books for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Everyone who checked out a book appears\x01",
            "to live on the outskirts of the state, so feel\x01",
            "free to take your time on this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Please return to me once you've collected\x01",
            "all three books.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_6423")

    Jump("loc_6454")

    label("loc_6428")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_643D")
    Call(0, 49)
    Jump("loc_6454")

    label("loc_643D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6451")
    Call(0, 48)
    Jump("loc_6454")

    label("loc_6451")

    Call(0, 19)

    label("loc_6454")

    Jump("loc_81FB")

    label("loc_6459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6694")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6518")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_647F")
    Call(0, 18)
    Jump("loc_6513")

    label("loc_647F")


    ChrTalk(
        0xF,
        (
            "Thanks, Lloyd. As you might imagine,\x01",
            "we're far too understaffed to handle\x01",
            "that task on our own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I'll contact you if I need help again.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_6513")

    Jump("loc_668F")

    label("loc_6518")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_653D")
    Call(0, 52)
    Jump("loc_668F")

    label("loc_653D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_6663")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_655B")
    Call(0, 18)
    Jump("loc_665E")

    label("loc_655B")


    ChrTalk(
        0xF,
        (
            "I'm counting on you to collect those\x01",
            "overdue books for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Everyone who checked out a book appears\x01",
            "to live on the outskirts of the state, so feel\x01",
            "free to take your time on this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Please return to me once you've collected\x01",
            "all three books.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_665E")

    Jump("loc_668F")

    label("loc_6663")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_6678")
    Call(0, 49)
    Jump("loc_668F")

    label("loc_6678")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_668C")
    Call(0, 48)
    Jump("loc_668F")

    label("loc_668C")

    Call(0, 18)

    label("loc_668F")

    Jump("loc_81FB")

    label("loc_6694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6CE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C03")

    ChrTalk(
        0x153,
        (
            "#1110FI like how many books there are!\x02\x03",
            "#1109FCan I read them?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_52(0x153, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x153, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_679B")
    Jump("loc_67E5")

    label("loc_679B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_67BB")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67E5")

    label("loc_67BB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67DB")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67E5")

    label("loc_67DB")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_67E5")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        "Ohoho, who do we have here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "You like reading books, missy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1111FYeah, probably!\x02\x03",
            "#1110FI get excited looking at all the pretty\x01",
            "colors on the covers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Oh, yeah! I totally understand where you're\x01",
            "coming from. In fact, I love books so much\x01",
            "that I became a librarian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1105F...?\x02",
    )

    CloseMessageWindow()
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x101, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_69CA")
    Jump("loc_6A14")

    label("loc_69CA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_69EA")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A14")

    label("loc_69EA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A0A")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A14")

    label("loc_6A0A")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6A14")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        (
            "You should check out some books for her, Lloyd.\x01",
            "I'll even let you check out more than the limit\x01",
            "usually allows, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FS-Sure. Thanks, Uncle.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_6B3C")

    ChrTalk(
        0x102,
        (
            "#0100F(I'm glad we get to experience the perks\x01",
            "of Lloyd's uncle being a librarian.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BFB")

    label("loc_6B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_6BAC")

    ChrTalk(
        0x103,
        (
            "#0200F(I am elated KeA is able to reap the benefits\x01",
            "of Lloyd's relationship with his uncle.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BFB")

    label("loc_6BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_6BFB")

    ChrTalk(
        0x104,
        (
            "#0300F(Way to go, Lloyd. KeDo's scorin'\x01",
            "big time 'cause of you.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BFB")

    SetScenarioFlags(0xB0, 7)
    Jump("loc_6CDC")

    label("loc_6C03")


    ChrTalk(
        0xF,
        "You should borrow some books for her, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Reading helps a child's brain grow.\x01",
            "Now's the best time to get her\x01",
            "interested in reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI suppose you're right. Let's go\x01",
            "check out some books, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CDC")

    Jump("loc_81FB")

    label("loc_6CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6EF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E4E")

    ChrTalk(
        0xF,
        (
            "I've always told Cecile that she should\x01",
            "pursue any career she desires.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Definitely wasn't expecting her to\x01",
            "become a nurse, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It makes sense, for what it's worth. Back\x01",
            "when she was little, she used to ask me\x01",
            "to take her to St. Ursula all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "She must have already had her eyes\x01",
            "set on becoming one back then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6EEC")

    label("loc_6E4E")


    ChrTalk(
        0xF,
        (
            "I think my wife's a little worried about\x01",
            "Cecile having become a nurse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We must respect her wishes, however.\x01",
            "This is the path she chose for herself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EEC")

    Jump("loc_81FB")

    label("loc_6EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_71AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70D6")

    ChrTalk(
        0xF,
        (
            "Ouch... I was sorting the materials\x01",
            "in the archive room downstairs, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "One thing led to another, and I was\x01",
            "buried under an avalanche of books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'm lucky Cassal was around. I\x01",
            "might have suffocated otherwise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FAren't you exaggerating a bit, Uncle?\x02\x03",
            "#0000FIf it was that bad, you could have sent the\x01",
            "SSS a request to dig you out of there.\x01",
            "We're always here to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Sorry about that. I haven't had\x01",
            "any time to contact you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_71A7")

    label("loc_70D6")


    ChrTalk(
        0xF,
        (
            "It has been my dream to open the\x01",
            "archive room for public use. It's\x01",
            "going to take a lot of work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "There are way too many books, though.\x01",
            "I don't think I'll ever be able to make\x01",
            "the full room available.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71A7")

    Jump("loc_81FB")

    label("loc_71AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7381")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7315")

    ChrTalk(
        0xF,
        (
            "I'm putting together a list of\x01",
            "new books to purchase.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "This author is exceedingly popular\x01",
            "at the moment, so I plan to purchase\x01",
            "several volumes of his most recent book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FMakes sense. Crossbell City's\x01",
            "population is pretty high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'm glad people are borrowing our books.\x01",
            "They're doing us a huge favor by doing so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_737C")

    label("loc_7315")


    ChrTalk(
        0xF,
        (
            "The library is funded by taxpayers,\x01",
            "so I'd be elated if they came and put\x01",
            "their mira to good use.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_737C")

    Jump("loc_81FB")

    label("loc_7381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7610")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7560")

    ChrTalk(
        0xF,
        (
            "It's rare for you to show up here\x01",
            "around this time, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Are you off work today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FUnfortunately not.\x02\x03",
            "We've been working all morning.\x01",
            "Haven't had a day off in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FI only understood the full magnitude\x01",
            "of our work recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Haha, that so? I suppose the life\x01",
            "of a police officer is not an easy one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Working at the library is one of the easier\x01",
            "government jobs. We get an appropriate\x01",
            "amount of time off work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_760B")

    label("loc_7560")


    ChrTalk(
        0xF,
        (
            "We're only open six out of seven days\x01",
            "a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "My librarian spirit urges me to come in\x01",
            "when we're closed to tackle any odd\x01",
            "jobs that need taking care of, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_760B")

    Jump("loc_81FB")

    label("loc_7610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_77F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7699")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7691")

    ChrTalk(
        0xF,
        "Thanks a bunch for the help, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I'll be sure to contact you again if I need it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7694")

    label("loc_7691")

    Call(0, 17)

    label("loc_7694")

    Jump("loc_77EC")

    label("loc_7699")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D5, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D6, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D7, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76D0")
    Call(0, 47)
    Jump("loc_77EC")

    label("loc_76D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_77C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_76EE")
    Call(0, 15)
    Jump("loc_77BB")

    label("loc_76EE")


    ChrTalk(
        0xF,
        (
            "I'm counting on you to collect those\x01",
            "overdue books for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Please return to me once you've collected\x01",
            "all three books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Feel free to take your time, by the way.\x01",
            "I'm not exactly in a hurry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_77BB")

    Jump("loc_77EC")

    label("loc_77C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_77D5")
    Call(0, 44)
    Jump("loc_77EC")

    label("loc_77D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_77E9")
    Call(0, 43)
    Jump("loc_77EC")

    label("loc_77E9")

    Call(0, 15)

    label("loc_77EC")

    Jump("loc_81FB")

    label("loc_77F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_79D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_787A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7872")

    ChrTalk(
        0xF,
        "Thanks a bunch for the help, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I'll be sure to contact you again if I need it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7875")

    label("loc_7872")

    Call(0, 17)

    label("loc_7875")

    Jump("loc_79CD")

    label("loc_787A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D5, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D6, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D7, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78B1")
    Call(0, 47)
    Jump("loc_79CD")

    label("loc_78B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_79A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_78CF")
    Call(0, 16)
    Jump("loc_799C")

    label("loc_78CF")


    ChrTalk(
        0xF,
        (
            "I'm counting on you to collect those\x01",
            "overdue books for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Please return to me once you've collected\x01",
            "all three books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Feel free to take your time, by the way.\x01",
            "I'm not exactly in a hurry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_799C")

    Jump("loc_79CD")

    label("loc_79A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_79B6")
    Call(0, 44)
    Jump("loc_79CD")

    label("loc_79B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_79CA")
    Call(0, 43)
    Jump("loc_79CD")

    label("loc_79CA")

    Call(0, 16)

    label("loc_79CD")

    Jump("loc_81FB")

    label("loc_79D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7BB3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7A5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7A53")

    ChrTalk(
        0xF,
        "Thanks a bunch for the help, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I'll be sure to contact you again if I need it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A56")

    label("loc_7A53")

    Call(0, 17)

    label("loc_7A56")

    Jump("loc_7BAE")

    label("loc_7A5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D5, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D6, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D7, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A92")
    Call(0, 47)
    Jump("loc_7BAE")

    label("loc_7A92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_7B82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7AB0")
    Call(0, 16)
    Jump("loc_7B7D")

    label("loc_7AB0")


    ChrTalk(
        0xF,
        (
            "I'm counting on you to collect those\x01",
            "overdue books for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Please return to me once you've collected\x01",
            "all three books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Feel free to take your time, by the way.\x01",
            "I'm not exactly in a hurry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_7B7D")

    Jump("loc_7BAE")

    label("loc_7B82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_7B97")
    Call(0, 44)
    Jump("loc_7BAE")

    label("loc_7B97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7BAB")
    Call(0, 43)
    Jump("loc_7BAE")

    label("loc_7BAB")

    Call(0, 17)

    label("loc_7BAE")

    Jump("loc_81FB")

    label("loc_7BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_81F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F71")

    ChrTalk(
        0x101,
        (
            "#0000FIt's good to see you again, Uncle.\x01",
            "I haven't seen you in forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Well, if it isn't my favorite neighbor!\x01",
            "How are you doing, Lloyd?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Hahaha, what an excellent surprise!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'd heard you were returning home soon.\x01",
            "But, wow! You look completely different!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FNot true, Uncle. I've only grown a few rege.\x01",
            "I've still got a long way to go until I'm mature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Now, you know that's not true. You aced\x01",
            "the detective exam, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I am absolutely certain Guy would be\x01",
            "proud of you right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0008FYeah...you're probably right.\x02\x03",
            "Thanks, Uncle. I'm happy to hear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Of course. Anything for my honorary son!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The library keeps me plenty busy,\x01",
            "so I'm hardly ever home these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "That doesn't apply to your aunt, though.\x01",
            "Her door is always open for you,\x01",
            "should you need any help. Got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYep. Thanks, Uncle.\x02\x03",
            "#0003FI'll be sure to rely on your help\x01",
            "when the time comes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 7)
    Jump("loc_81ED")

    label("loc_7F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8133")

    ChrTalk(
        0xF,
        (
            "Hey there, Lloyd. Did you want to\x01",
            "check out any books?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FHaha, that brings me back. I've never\x01",
            "seen you miss an opportunity to\x01",
            "recommend a book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "What can I say? I love books!\x01",
            "I feel calmer just by surrounding\x01",
            "myself with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Anyway, no need to be shy. Our\x01",
            "collection of books will always be\x01",
            "ready for your perusal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We've got an enormous selection of books.\x01",
            "Who knows what's out there waiting for you?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_81ED")

    label("loc_8133")


    ChrTalk(
        0xF,
        (
            "Anyway, no need to be shy. Our\x01",
            "collection of books will always be\x01",
            "ready for your perusal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We've got an enormous selection of books.\x01",
            "Who knows what's out there waiting for you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81ED")

    Jump("loc_81FB")

    label("loc_81F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_81FB")

    label("loc_81FB")

    SetChrSubChip(0xF, 0x0)
    TalkEnd(0xF)
    Return()

    # Function_14_5EC7 end

    def Function_15_8203(): pass

    label("Function_15_8203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8477")

    ChrTalk(
        0xF,
        (
            "Huh? The numbers aren't matching\x01",
            "up again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We don't have enough staff to\x01",
            "implement proper bookkeeping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Most people fail to return their books\x01",
            "on time, too. It really throws a wrench\x01",
            "into keeping things organized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FSounds like a real pain.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_83DF")

    ChrTalk(
        0xF,
        (
            "Yeah, just a little. I'm still glad you were\x01",
            "able to help us, though. We were in\x01",
            "a little bit of a pickle there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "My librarian spirit drives me to keep\x01",
            "everything organized.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_846F")

    label("loc_83DF")


    ChrTalk(
        0xF,
        (
            "I'd say that one of our biggest problems\x01",
            "is people failing to return their books\x01",
            "on time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I assume they've long forgotten about them.\x02",
    )

    CloseMessageWindow()

    label("loc_846F")

    SetScenarioFlags(0x0, 5)
    Jump("loc_8511")

    label("loc_8477")


    ChrTalk(
        0xF,
        (
            "We don't have enough staff to\x01",
            "implement proper bookkeeping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Not only that, but we have to take into\x01",
            "account administrative costs in our budget.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8511")

    Return()

    # Function_15_8203 end

    def Function_16_8512(): pass

    label("Function_16_8512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_868B")

    ChrTalk(
        0xF,
        (
            "We have an enormous collection of\x01",
            "old books and unsorted miscellaneous\x01",
            "materials in the archive room downstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I like to dive in there every once in a while\x01",
            "and see what kind of rare book I pull out.\x01",
            "It's a pretty good feeling, if I may say so.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0000F(Good to see Uncle is still the same\x01",
            "bookworm I know and love.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_871F")

    label("loc_868B")


    ChrTalk(
        0xF,
        (
            "I can't keep up with the procedures required\x01",
            "to make the archive room accessible to the\x01",
            "public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "It's a bibliophile's paradise down there.\x02",
    )

    CloseMessageWindow()

    label("loc_871F")

    Return()

    # Function_16_8512 end

    def Function_17_8720(): pass

    label("Function_17_8720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8861")

    ChrTalk(
        0xF,
        (
            "Any individual can check out up\x01",
            "to three books at a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We're understaffed, so we can't handle sorting\x01",
            "through large volumes of books. We don't have the\x01",
            "funding to hire another full-time employee, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I think the locals would find it easier if\x01",
            "they could borrow up to five, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8901")

    label("loc_8861")


    ChrTalk(
        0xF,
        (
            "The library is too understaffed to handle\x01",
            "lending out many books at a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I wish we could do something to make\x01",
            "our patrons' lives easier, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8901")

    Return()

    # Function_17_8720 end

    def Function_18_8902(): pass

    label("Function_18_8902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AC6")

    ChrTalk(
        0xF,
        "KeA's an impressive little girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "She's been tearing through her books\x01",
            "like they're nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FYeah, I think she's grown to love reading.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Haha, fantastic! A new member has been\x01",
            "inducted into the Legion of Bibliophiles!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Bring her next time you come to check out books.\x01",
            "I'll be sure to whip up a personal package with\x01",
            "some of my favorite reads in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FShe would be elated to hear that, I think.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8B97")

    label("loc_8AC6")


    ChrTalk(
        0xF,
        "KeA's an impressive little girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Who knows? Maybe she'll follow my\x01",
            "footsteps and become a librarian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FHahaha... We'll see about that.\x01",
            "(Uncle has fallen absolutely head over\x01",
            "heels for her.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B97")

    Return()

    # Function_18_8902 end

    def Function_19_8B98(): pass

    label("Function_19_8B98")


    ChrTalk(
        0xF,
        (
            "The shoot-out wasn't really in the park,\x01",
            "was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "How could this have happened?\x01",
            "That area is meant for business!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Thinking about it all morning has put\x01",
            "me in a bad mood...\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_19_8B98 end

    def Function_20_8C52(): pass

    label("Function_20_8C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DE4")

    ChrTalk(
        0xF,
        (
            "I remember back when Guy used to work\x01",
            "for the police. I don't think there was a day\x01",
            "where he didn't love his job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Back when he was a rookie, he told me\x01",
            "that he had found himself one hell of\x01",
            "a partner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It hasn't been ten years since we had\x01",
            "that conversation, and yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Guy, Sergei, and even you have\x01",
            "changed considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0008FYeah, I suppose that's true...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8E7B")

    label("loc_8DE4")


    ChrTalk(
        0xF,
        (
            "Haha, sorry about that. I didn't mean to\x01",
            "get all sentimental on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I think conversations like this are more\x01",
            "suited for a mother to handle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E7B")

    Return()

    # Function_20_8C52 end

    def Function_21_8E7C(): pass

    label("Function_21_8E7C")


    ChrTalk(
        0xF,
        (
            "It's almost dark. I'd better start closing\x01",
            "up the library soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It was good seeing you, Lloyd. I'll head back\x01",
            "home once I've gathered my belongings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "See you tomorrow, okay?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F70")

    ChrTalk(
        0x101,
        "#0000FSounds good. See you later, Uncle.\x02",
    )

    CloseMessageWindow()

    label("loc_8F70")

    SetScenarioFlags(0x0, 5)
    Return()

    # Function_21_8E7C end

    def Function_22_8F74(): pass

    label("Function_22_8F74")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9008")
    Jump("loc_9052")

    label("loc_9008")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9028")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9052")

    label("loc_9028")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9048")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9052")

    label("loc_9048")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9052")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_91E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_915B")

    ChrTalk(
        0xFE,
        (
            "I've made a new discovery!\x01",
            "I'm always shocked by the amount of\x01",
            "work I can do at a library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The quiet atmosphere makes it easy to\x01",
            "concentrate, and there are no annoying\x01",
            "bosses yapping at you!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_91E3")

    label("loc_915B")


    ChrTalk(
        0xFE,
        "I can't believe how effective the library is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but feel bad for how few\x01",
            "visitors there are, but it only helps me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91E3")

    Jump("loc_94A1")

    label("loc_91E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_926D")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        "No, not like this... No, not that, either...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, I think I've got it...\x01",
            "I should put this here, and...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94A1")

    label("loc_926D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9387")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92E8")

    ChrTalk(
        0xFE,
        "Here...we...go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No time to celebrate over a small victory.\x01",
            "I need to keep on working.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9382")

    label("loc_92E8")


    ChrTalk(
        0xFE,
        (
            "I'm trying to concentrate.\x01",
            "I need to take this a little more seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The budget will come to a grinding halt\x01",
            "if I submit the documents late.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9382")

    Jump("loc_94A1")

    label("loc_9387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9498")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9439")

    ChrTalk(
        0xFE,
        (
            "I can't concentrate at City Hall.\x01",
            "It's too noisy there, so I figured\x01",
            "I'd try to work here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, the diet budget meeting\x01",
            "begins next week.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9493")

    label("loc_9439")


    ChrTalk(
        0xFE,
        (
            "Look at how hardworking I am!\x01",
            "I've even relocated to try and get\x01",
            "more work finished!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9493")

    Jump("loc_94A1")

    label("loc_9498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_94A1")

    label("loc_94A1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_8F74 end

    def Function_23_94A9(): pass

    label("Function_23_94A9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x0, 0)
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_953D")
    Jump("loc_9587")

    label("loc_953D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_955D")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9587")

    label("loc_955D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_957D")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9587")

    label("loc_957D")

    OP_52(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9587")

    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A037")
    EventBegin(0x0)
    Fade(500)
    OP_68(29400, 5020, -14320, 0)
    MoveCamera(51, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18590, 0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x101, 29930, 4030, -13780, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9627")
    SetChrPos(0x102, 28660, 4030, -13530, 135)
    Jump("loc_966E")

    label("loc_9627")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_964D")
    SetChrPos(0x103, 28660, 4030, -13530, 135)
    Jump("loc_966E")

    label("loc_964D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_966E")
    SetChrPos(0x104, 28660, 4030, -13530, 135)

    label("loc_966E")

    SetChrPos(0x153, 27220, 4030, -14020, 135)
    SetChrSubChip(0x11, 0x2)
    OP_0D()

    ChrTalk(
        0x11,
        "#2905F#11POh, what a coincidence seeing you all here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FMariabell?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_971F")

    ChrTalk(
        0x102,
        "#0102F#5PRather unusual to see you here, Bell.\x02",
    )

    CloseMessageWindow()
    Jump("loc_97A2")

    label("loc_971F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_976C")

    ChrTalk(
        0x103,
        (
            "#0202F#5PAn unlikely meeting in an unlikely\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97A2")

    label("loc_976C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97A2")

    ChrTalk(
        0x104,
        "#0305F#5PFancy meetin' you here.\x02",
    )

    CloseMessageWindow()

    label("loc_97A2")


    ChrTalk(
        0x11,
        (
            "#2904FDon't mind me. I come here on\x01",
            "my occasional day off from work.\x02\x03",
            "There's a trove of knowledge here\x01",
            "not found on the orbal network.\x02\x03",
            "#2902FI'd be a fool to not make use of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FI-I think I've been underestimating\x01",
            "you this whole time.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_990C")

    ChrTalk(
        0x102,
        "#0104F#5PStudious as ever, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#2904FI could say the same about you, Elie.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9989")

    label("loc_990C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_994E")

    ChrTalk(
        0x103,
        "#0204F#5PI see. You make a valid point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9989")

    label("loc_994E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9989")

    ChrTalk(
        0x104,
        "#0309F#5PAh... Hats off to you, then.\x02",
    )

    CloseMessageWindow()

    label("loc_9989")

    SetChrSubChip(0x11, 0x0)
    Sleep(300)

    ChrTalk(
        0x11,
        "#2900FThat's not important, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1101F(*stare*)\x02\x03",
            "#1110FHey. Hey, Lloyd! Who's the lady?\x01",
            "Do you know her?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9A0C():
        TurnDirection(0x101, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A0C)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A33")
    TurnDirection(0x102, 0x153, 500)
    Jump("loc_9A66")

    label("loc_9A33")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A4F")
    TurnDirection(0x103, 0x153, 500)
    Jump("loc_9A66")

    label("loc_9A4F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A66")
    TurnDirection(0x104, 0x153, 500)

    label("loc_9A66")


    ChrTalk(
        0x101,
        "#0002F#11PY-Yeah, I guess you could say that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2904F#11PI've already been made aware of\x01",
            "the little one's circumstances.\x02\x03",
            "#2902FShe is the 'doll' they planned to exhibit\x01",
            "at the auction, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_9B6B():
        TurnDirection(0x101, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B6B)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B98")

    def lambda_9B8B():
        TurnDirection(0x102, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B8B)
    Jump("loc_9BD7")

    label("loc_9B98")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BBA")

    def lambda_9BAD():
        TurnDirection(0x103, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9BAD)
    Jump("loc_9BD7")

    label("loc_9BBA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BD7")

    def lambda_9BCF():
        TurnDirection(0x104, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9BCF)

    label("loc_9BD7")

    Sleep(200)

    ChrTalk(
        0x101,
        "#0011FWhat?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C31")

    ChrTalk(
        0x102,
        "#0101F#5PHow do you know about that, Bell?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CBC")

    label("loc_9C31")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C79")

    ChrTalk(
        0x103,
        "#0205F#5PHow are you privy to that knowledge?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CBC")

    label("loc_9C79")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CBC")

    ChrTalk(
        0x104,
        "#0305F#5PThe hell did you find that out from?\x02",
    )

    CloseMessageWindow()

    label("loc_9CBC")


    ChrTalk(
        0x11,
        (
            "#2906F*sigh* Wouldn't it be stranger for me to\x01",
            "NOT know? Think about the mess you\x01",
            "made at the auction.\x02\x03",
            "#2902FAnd besides, I managed to catch a glimpse\x01",
            "of you escaping from afar.\x02\x03",
            "#2904FBetween that and the information trickling\x01",
            "in over the week, it's not hard to put the\x01",
            "pieces together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FI-I can't deny your reasoning.\x02\x03",
            "#0001FHey, Mariabell... Will you do us a solid\x01",
            "and--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2903FNaturally.\x02\x03",
            "#2902FPerhaps it was more than a mere\x01",
            "coincidence for me to be present during\x01",
            "the whole...situation, so to speak.\x02\x03",
            "And, for the record, my door is always open\x01",
            "to all of you, should you need any advice\x01",
            "for your troubles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0004FThanks, Mariabell.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F8D")

    ChrTalk(
        0x102,
        "#0102F#5PI appreciate it, Bell.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A002")

    label("loc_9F8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9FCC")

    ChrTalk(
        0x103,
        "#0204F#5PThank you for your concern.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A002")

    label("loc_9FCC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A002")

    ChrTalk(
        0x104,
        "#0304F#5PThanks a bunch, madame.\x02",
    )

    CloseMessageWindow()

    label("loc_A002")


    ChrTalk(
        0x153,
        "#1105F...?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 29930, 4030, -13780, 180)
    SetChrSubChip(0x11, 0x0)
    SetScenarioFlags(0xB4, 7)
    ClearChrFlags(0x8, 0x80)
    EventEnd(0x5)
    Jump("loc_A55B")

    label("loc_A037")

    OP_52(0x153, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x153, 0)
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A0CB")
    Jump("loc_A115")

    label("loc_A0CB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A0EB")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A115")

    label("loc_A0EB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A10B")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A115")

    label("loc_A10B")

    OP_52(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A115")

    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_A30A")

    ChrTalk(
        0x153,
        (
            "#1106FBut I don't wanna.\x02\x03",
            "#1110FI'm not going to join you if you won't\x01",
            "let Lloyd come, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#2905FHow unfortunate for me.\x02",
    )

    CloseMessageWindow()
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x101, 0)
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A25B")
    Jump("loc_A2A5")

    label("loc_A25B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A27B")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A2A5")

    label("loc_A27B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A29B")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A2A5")

    label("loc_A29B")

    OP_52(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A2A5")

    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    Sleep(300)

    ChrTalk(
        0x11,
        "#2910F*glare*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011F(H-How's this my fault?!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_A557")

    label("loc_A30A")


    ChrTalk(
        0x11,
        (
            "#2902FI have to say...\x02\x03",
            "...she's far cuter than any Rosenberg doll.\x01",
            "KeA, was it?\x02\x03",
            "#2909FHow would you like to come to my\x01",
            "house and play with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1105FCan Lloyd and the others come, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2901FI will have to respectfully decline.\x01",
            "Especially for Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0006F(Why does she always have to be\x01",
            "so uncomfortably hostile towards me?)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4D9")

    ChrTalk(
        0x102,
        "#0106F#5P(How unlucky of you, Lloyd.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_A554")

    label("loc_A4D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A51A")

    ChrTalk(
        0x103,
        "#0204F#5P(I offer you my condolences.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_A554")

    label("loc_A51A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A554")

    ChrTalk(
        0x104,
        "#0309F#5P(Hahaha, serves you right!)\x02",
    )

    CloseMessageWindow()

    label("loc_A554")

    SetScenarioFlags(0x1, 0)

    label("loc_A557")

    SetChrSubChip(0x11, 0x0)

    label("loc_A55B")

    SetChrSubChip(0x11, 0x0)
    TalkEnd(0x11)
    Return()

    # Function_23_94A9 end

    def Function_24_A563(): pass

    label("Function_24_A563")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 1)), scpexpr(EXPR_END)), "loc_A66A")

    ChrTalk(
        0x12,
        (
            "#3504FCool, I managed to finish up the\x01",
            "remaining bits and pieces of work\x01",
            "I had for the Empire.\x02\x03",
            "#3500FNothin' left to do but screw around\x01",
            "Crossbell for a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(I still don't get this guy. How much\x01",
            "does he actually know?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB1F")

    label("loc_A66A")

    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x0, 300)

    ChrTalk(
        0x12,
        (
            "#3500FOh? You guys like to read, too?\x02\x03",
            "#3509FWhat a lucky coincidence! Nothing better\x01",
            "than making friends with fellow bookworms. ♪\x02",
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
        "#0006FWhere do I even begin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FI refuse to believe that he came here just\x01",
            "to read, but it is almost unnatural how\x01",
            "well he blends in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(There's no use tryin' to wrap my\x01",
            "head around it.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 2)), scpexpr(EXPR_END)), "loc_AABC")

    ChrTalk(
        0x102,
        (
            "#0105FWeren't you headed back to the\x01",
            "Empire to handle business, Lechter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3505FWell, yeah. I guess.\x02\x03",
            "#3500FBut, just 'cause I said I'd be in the 'Empire,'\x01",
            "doesn't mean I had to go very far.\x02\x03",
            "I was right by Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        "#0005F(Near Bellguard Gate?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105F(It couldn't be... Is he referring to\x01",
            "Garrelia Fortress?!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305F(Ain't that bad news? That base is\x01",
            "pretty damn important to the Empire.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0211F(Your ordinary civilian would not go\x01",
            "there for simple business. I wish\x01",
            "I was able to discern his identity.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB15")

    label("loc_AABC")


    ChrTalk(
        0x102,
        (
            "#0106F(Agreed... I don't think we should take\x01",
            "anything he says seriously, for now.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB15")

    OP_93(0x12, 0x5A, 0x0)
    SetScenarioFlags(0xEF, 1)

    label("loc_AB1F")

    TalkEnd(0xFE)
    Return()

    # Function_24_A563 end

    def Function_25_AB23(): pass

    label("Function_25_AB23")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_AC5A")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "~ New Books This Month ~\x01",
            "Mark and the Witch of the Deep Forest - Last Volume\x01\x01",
            "You can find the newest volume on the first floor shelves.\x01",
            "Don't forget to take a look if you're interested!\x01",
            "★It's a part of a popular trilogy, so be sure to\x01",
            "check it out ahead of time!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_B03C")

    label("loc_AC5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_ACAA")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "~ New Books This Month ~\x01",
            "Coming Soon\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_B03C")

    label("loc_ACAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_AD87")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "~ New Books This Month ~\x01",
            "The Saint and the White Wolf - Last Volume\x01\x01",
            "You can find the newest volume on the first floor shelves.\x01",
            "Don't forget to take a look if you're interested!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_B03C")

    label("loc_AD87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_AE85")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "~ New Books This Month ~\x01",
            "Mark and the Witch of the Deep Forest - Middle Volume\x01",
            "Lip Smacker Quarterly\x01\x01",
            "You can find the newest volume on the first floor shelves.\x01",
            "Don't forget to take a look if you're interested!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_B03C")

    label("loc_AE85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_AF63")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "~ New Books This Month ~\x01",
            "The Saint and the White Wolf - First Volume\x01\x01",
            "You can find the newest volume on the first floor shelves.\x01",
            "Don't forget to take a look if you're interested!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_B03C")

    label("loc_AF63")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "~ New Books This Month ~\x01",
            "Mark and the Witch of the Deep Forest - First Volume\x01\x01",
            "You can find the newest volume on the first floor shelves.\x01",
            "Don't forget to take a look if you're interested!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_B03C")

    TalkEnd(0xFF)
    Return()

    # Function_25_AB23 end

    def Function_26_B040(): pass

    label("Function_26_B040")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mark and the Witch of the Deep Forest is on the shelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B13D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Read First Volume]\x01",       # 0
            "[Read Middle Volume]\x01",      # 1
            "[Read Last Volume]\x01",        # 2
            "[Leave]\x01",                   # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B110")
    UseItem(0x2D6, 0xFF)

    label("loc_B110")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B124")
    UseItem(0x2DD, 0xFF)

    label("loc_B124")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B138")
    UseItem(0x2DE, 0xFF)

    label("loc_B138")

    Jump("loc_B218")

    label("loc_B13D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B1C6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Read First Volume]\x01",       # 0
            "[Read Middle Volume]\x01",      # 1
            "[Leave]\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1AD")
    UseItem(0x2D6, 0xFF)

    label("loc_B1AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1C1")
    UseItem(0x2DD, 0xFF)

    label("loc_B1C1")

    Jump("loc_B218")

    label("loc_B1C6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Read First Volume]\x01",      # 0
            "[Leave]\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B218")
    UseItem(0x2D6, 0xFF)

    label("loc_B218")

    TalkEnd(0xFF)
    Return()

    # Function_26_B040 end

    def Function_27_B21C(): pass

    label("Function_27_B21C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lip Smacker Quarterly is on the shelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Read]\x01",       # 0
            "[Leave]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B31A")
    UseItem(0x2DC, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x12)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B31A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x12)

    label("loc_B31A")

    TalkEnd(0xFF)
    Return()

    # Function_27_B21C end

    def Function_28_B31E(): pass

    label("Function_28_B31E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Prominent Female Figures is on the shelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Read]\x01",       # 0
            "[Leave]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B399")
    UseItem(0x2D7, 0xFF)

    label("loc_B399")

    TalkEnd(0xFF)
    Return()

    # Function_28_B31E end

    def Function_29_B39D(): pass

    label("Function_29_B39D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Effective Use of Five Minutes is on the shelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Read]\x01",       # 0
            "[Leave]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B41D")
    UseItem(0x2D8, 0xFF)

    label("loc_B41D")

    TalkEnd(0xFF)
    Return()

    # Function_29_B39D end

    def Function_30_B421(): pass

    label("Function_30_B421")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Train Fanatic Recs is on the shelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Read]\x01",       # 0
            "[Leave]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B496")
    UseItem(0x2D5, 0xFF)

    label("loc_B496")

    TalkEnd(0xFF)
    Return()

    # Function_30_B421 end

    def Function_31_B49A(): pass

    label("Function_31_B49A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Paranormal Crossbell Collection is on the shelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Read]\x01",       # 0
            "[Leave]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B51C")
    UseItem(0x2D9, 0xFF)

    label("loc_B51C")

    TalkEnd(0xFF)
    Return()

    # Function_31_B49A end

    def Function_32_B520(): pass

    label("Function_32_B520")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Saint and the White Wolf is on the shelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B5EB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Read First Volume]\x01",      # 0
            "[Read Last Volume]\x01",       # 1
            "[Leave]\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5D2")
    UseItem(0x2DF, 0xFF)

    label("loc_B5D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5E6")
    UseItem(0x2E0, 0xFF)

    label("loc_B5E6")

    Jump("loc_B63D")

    label("loc_B5EB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Read First Volume]\x01",      # 0
            "[Leave]\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B63D")
    UseItem(0x2DF, 0xFF)

    label("loc_B63D")

    TalkEnd(0xFF)
    Return()

    # Function_32_B520 end

    def Function_33_B641(): pass

    label("Function_33_B641")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Arc en Ciel Enthusiasts is on the shelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Read]\x01",       # 0
            "[Leave]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6BB")
    UseItem(0x2DA, 0xFF)

    label("loc_B6BB")

    TalkEnd(0xFF)
    Return()

    # Function_33_B641 end

    def Function_34_B6BF(): pass

    label("Function_34_B6BF")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B6D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD66")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "A Section")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Arc en Ciel]\x01",                # 0
            "[Arteria, Holy City of]\x01",      # 1
            "[Artifacts]\x01",                  # 2
            "[Leave]\x01",                      # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8A4")
    MenuTitle(-1, 25, 0, "Arc en Ciel")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Arc en Ciel is a famous theatre troupe hailing from\x01",
            "Crossbell State.\x02\x03",
            "Their acrobatic and passionate performances\x01",
            "continue to draw large audiences.\x02\x03",
            "Its current leading actress, Ilya Platiere, is known\x01",
            "as the 'Fervent Dancer,' and has many fans around\x01",
            "the continent.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B8A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAEA")
    MenuTitle(-1, 25, 0, "Holy City of Arteria")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A city-state housing the High Seat of the Septian\x01",
            "Church, Arteria is located at the center of the\x01",
            "continent and acts as a gathering place for believers\x01",
            "and church officials alike.\x02\x03",
            "The church comprises a number of organizations,\x01",
            "including the Congregation for Divine Worship,\x01",
            "which handles liturgical matters, the Congregation\x01",
            "for the Sacraments, which handles administering\x01",
            "the sacraments of the Goddess, and the Papal Guard,\x01",
            "which is responsible for protecting the Holy City of\x01",
            "Arteria itself.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BAEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD61")
    MenuTitle(-1, 25, 0, "Artifacts")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Artifacts are essentially ancient orbments.\x01",
            "While both run on orbal energy, they are operated\x01",
            "very differently.\x02\x03",
            "Because they were likely produced by the ancient\x01",
            "Zemurian civilization, proper analysis is currently\x01",
            "beyond our technological grasp.\x02\x03",
            "Artifacts are occasionally found within ruins across\x01",
            "the continent, and many are capable of\x01",
            "demonstrating power that exceeds the bounds of\x01",
            "human comprehension.\x02\x03",
            "The Septian Church has as such defined artifacts as\x01",
            "'premature gifts from the Goddess,' and claims\x01",
            "responsibility for their collection and control.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BD61")

    Jump("loc_B6D6")

    label("loc_BD66")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_34_B6BF end

    def Function_35_BD73(): pass

    label("Function_35_BD73")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BD8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6FC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "B-C Section")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[B, Phantom Thief]\x01",      # 0
            "[Bracer Guild]\x01",          # 1
            "[Calvard Republic]\x01",      # 2
            "[Crossbell State]\x01",       # 3
            "[Leave]\x01",                 # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C003")
    MenuTitle(-1, 25, 0, "Phantom Thief B")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "B is an elusive thief who has stolen everything from\x01",
            "jewels to orbal tanks from people and organizations\x01",
            "across Zemuria. His strange, almost beautiful methods\x01",
            "have given rise to a small, dedicated fanbase.\x02\x03",
            "Though he sends messages to his intended targets\x01",
            "and makes public appearances clad in a white cape\x01",
            "and mask, B's identity remains a mystery. He calls\x01",
            "his recent unusual thefts 'the liberation of beauty.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C003")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C28E")
    MenuTitle(-1, 25, 0, "Bracer Guild")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Bracer Guild is a non-governmental\x01",
            "organization acting to keep the peace and protect\x01",
            "civilians wherever its numerous and continent-\x01",
            "spanning branches reach. Its members are known\x01",
            "as 'bracers.'\x02\x03",
            "Its guiding principle--to put the safety of civilians\x01",
            "above all else--is both its greatest strength and\x01",
            "a handicap as it cannot involve itself in political\x01",
            "matters unless civilians are directly threatened.\x02\x03",
            "Here in Crossbell, many international incidents\x01",
            "have attracted strong bracers, such as the Divine\x01",
            "Blade of Wind, Arios MacLaine, who have earned\x01",
            "the citizens' support.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C28E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C509")
    MenuTitle(-1, 25, 0, "Calvard Republic")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Calvard Republic lies to the east of Crossbell\x01",
            "State, and was established after a democratic\x01",
            "revolution roughly a hundred years ago. Its current\x01",
            "head of state is President Rocksmith.\x02\x03",
            "Calvard is a vast country and, thanks to their long-\x01",
            "standing open immigration policies, very culturally\x01",
            "diverse. Many immigrants from the East have made\x01",
            "Calvard their home.\x02\x03",
            "Although it has been significantly less hostile\x01",
            "towards Erebonia since the signing of their\x01",
            "non-aggression pact, the two nations have been at\x01",
            "each other's throats many times over the years.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C509")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6F7")
    MenuTitle(-1, 25, 0, "Crossbell State")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell sits on the western side of Zemuria,\x01",
            "between the Erebonian Empire and the Calvard\x01",
            "Republic. While established as an autonomous state\x01",
            "seventy years ago, its two neighbors still dispute its\x01",
            "ownership.\x02\x03",
            "At its center lies Crossbell City, one of the continent's\x01",
            "key centers of commerce. In addition to being a key\x01",
            "station on the Transcontinental Railroad, the city is\x01",
            "home to a major international airport.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C6F7")

    Jump("loc_BD8A")

    label("loc_C6FC")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_35_BD73 end

    def Function_36_C709(): pass

    label("Function_36_C709")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C720")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF94")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "E-F Section")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Eastern Quarter]\x01",         # 0
            "[Epstein Foundation]\x01",      # 1
            "[Erebonian Empire]\x01",        # 2
            "[Fisherman's Guild]\x01",       # 3
            "[Leave]\x01",                   # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C94B")
    MenuTitle(-1, 25, 0, "Eastern Quarter")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large city built by immigrants from the East\x01",
            "in the Calvard Republic, the Eastern Quarter is\x01",
            "rife with different cultures, people, and goods.\x01",
            "It is said to be the 'intersection of the East and\x01",
            "the West.'\x02\x03",
            "It is a famous tourist destination lined with\x01",
            "exotic buildings, overshadowed by the rumors of\x01",
            "a large crime syndicate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C94B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB30")
    MenuTitle(-1, 25, 0, "Epstein Foundation")
    SetMessageWindowPos(-1, 70, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Epstein Foundation is an organization dedicated\x01",
            "to continuing the work of Professor C. Epstein.\x01",
            "It researches and manufactures orbments, specializing\x01",
            "in information processing and communication.\x02\x03",
            "The Epstein Foundation is also the sole manufacturer\x01",
            "of battle orbments, which allow their users access to\x01",
            "arts. Their recent Orbal Network Project also promises\x01",
            "to be the future of orbal communication.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CB30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDEE")
    MenuTitle(-1, 25, 0, "Erebonian Empire")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Erebonian Empire is located to the west of\x01",
            "Crossbell State and represented by the emblem\x01",
            "of the golden stallion. The current emperor is\x01",
            "Eugent Reise Arnor.\x02\x03",
            "Despite the Empire's rule by an antiquated nobility\x01",
            "structure, it has begun to modernize due to the\x01",
            "railway expansion efforts of Giliath Osborne, a veteran\x01",
            "now known as the 'Blood and Iron Chancellor.'\x02\x03",
            "Between its mechanized armed forces and private\x01",
            "forces at the command of the nobles, Erebonia is\x01",
            "always strained with its neighbors.\x02\x03",
            "Last year, Olivert, the emperor's son, cooperated\x01",
            "with Liberl to resolve a crisis there, becoming\x01",
            "the talk of the Empire.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CDEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF8F")
    MenuTitle(-1, 25, 0, "Fisherman's Guild")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Fisherman's Guild is an organized group of\x01",
            "anglers working to spread fishing enthusiasm.\x01",
            "Mr. H. Fisher, former noble fishing fancier, founded\x01",
            "the guild in Grancel City.\x02\x03",
            "Their activities include seeking out and investigating\x01",
            "fishing spots, recruiting and training new members,\x01",
            "and, in recent years, developing new tools and bait.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CF8F")

    Jump("loc_C720")

    label("loc_CF94")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_36_C709 end

    def Function_37_CFA1(): pass

    label("Function_37_CFA1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CFB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7BE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "G-J Section")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Great Collapse]\x01",        # 0
            "[Hundred Days War]\x01",      # 1
            "[IBC]\x01",                   # 2
            "[Jaeger Corps]\x01",          # 3
            "[Leave]\x01",                 # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D19B")
    MenuTitle(-1, 25, 0, "Great Collapse")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The destruction of the ancient Zemurian civilization\x01",
            "is estimated to have occurred 1,200 years ago.\x01",
            "While the Great Collapse is commonly attributed to\x01",
            "a natural disaster, this theory remains unconfirmed.\x02\x03",
            "This ancient civilization's end marked the beginning\x01",
            "of the Dark Ages.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D19B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D441")
    MenuTitle(-1, 25, 0, "Hundred Days War")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Hundred Days War was a war of aggression\x01",
            "waged by the Empire against the Liberl Kingdom\x01",
            "in 1192. The name is drawn from the hundred days\x01",
            "between the start of the war and its church-\x01",
            "mediated end.\x02\x03",
            "Initially, Liberl appeared to be at a significant\x01",
            "disadvantage, with the Empire occupying a majority\x01",
            "of their territory, but a single operation using the\x01",
            "then-new patrol airships turned the tide of battle.\x02\x03",
            "The reasoning for the war is not public knowledge,\x01",
            "but the Erebonian Empire has since formally\x01",
            "apologized to Liberl, calling the war 'A mistake born\x01",
            "from an unfortunate misunderstanding.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D441")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D637")
    SetChrName("")
    MenuTitle(-1, 25, 0, "International Bank of Crossbell (IBC)")
    SetMessageWindowPos(-1, 70, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The International Bank of Crossbell is a large banking\x01",
            "organization which manages the vast quantities\x01",
            "of money flowing into Crossbell and supports the\x01",
            "economies of nations across the continent.\x02\x03",
            "The IBC's interests extend beyond banking, too.\x01",
            "In addition to providing most of the funding for the\x01",
            "Epstein Foundation's Orbal Network Project, the bank\x01",
            "manages theme parks and other similar diversions.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D637")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7B9")
    MenuTitle(-1, 25, 0, "Jaeger Corps")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Incredibly skilled mercenary groups which can be\x01",
            "found all over the continent are known as 'jaeger\x01",
            "corps.'\x02\x03",
            "Due to their combat proficiency and their willingness\x01",
            "to take on morally gray contracts, they are often\x01",
            "used as private armies. As such, several countries\x01",
            "have passed laws against their hire and use.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D7B9")

    Jump("loc_CFB8")

    label("loc_D7BE")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_37_CFA1 end

    def Function_38_D7CB(): pass

    label("Function_38_D7CB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D7E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF8C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "L-N Section")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Leman State]\x01",              # 0
            "[Liberl Kingdom]\x01",           # 1
            "[Mishelam]\x01",                 # 2
            "[Non-Aggression Pact]\x01",      # 3
            "[Leave]\x01",                    # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9AD")
    MenuTitle(-1, 25, 0, "Leman State")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Home to the Epstein Foundation and the birthplace\x01",
            "of Professor C. Epstein himself, Leman is a state in\x01",
            "the center of the Zemurian continent.\x02\x03",
            "It is also known for housing the headquarters of the\x01",
            "Bracer Guild, which has branches all across Zemuria.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D9AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC59")
    MenuTitle(-1, 25, 0, "Liberl Kingdom")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Liberl Kingdom is situated in the southwest\x01",
            "part of the Zemurian continent. Rich in nature and\x01",
            "history, the kingdom is ruled by the long-lived\x01",
            "Queen Alicia II, a staunch advocate for peace.\x02\x03",
            "While a humble nation compared to those around it,\x01",
            "its bountiful septium reserves, advanced technological\x01",
            "capabilities, and Queen Alicia's skillful diplomacy\x01",
            "allow it to stand on equal footing with any other.\x02\x03",
            "Last year, a large object of unknown origin appeared\x01",
            "above Valleria Lake, disabling orbments nationwide.\x01",
            "This crisis was resolved through the joint efforts of\x01",
            "the Royal Army and the Bracer Guild.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0xBF, 1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DC59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDAC")
    MenuTitle(-1, 25, 0, "Mishelam")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mishelam is a newly-popular luxury resort located\x01",
            "southeast of Lake Elm. The IBC funded the construction\x01",
            "of a high-class hotel and a theme park beginning two\x01",
            "years ago.\x02\x03",
            "Mishy, the mascot character of Mishelam, is becoming\x01",
            "popular with citizens and tourists alike.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DDAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF87")
    MenuTitle(-1, 25, 0, "Non-Aggression Pact")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Non-Aggression Pact was an international treaty\x01",
            "proposed by Queen Alicia II and signed in 1202 by the\x01",
            "Liberl Kingdom, Erebonian Empire, and Calvard\x01",
            "Republic in Liberl's Erbe Royal Villa.\x02\x03",
            "While not legally binding, the pact has had a\x01",
            "powerful effect, bringing an end to large-scale\x01",
            "Erebonian and Calvardian military exercises near\x01",
            "Crossbell and decreasing tensions between each\x01",
            "nation.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DF87")

    Jump("loc_D7E2")

    label("loc_DF8C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_38_D7CB end

    def Function_39_DF99(): pass

    label("Function_39_DF99")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DFB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E930")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "O Section")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Orbal Arts]\x01",                 # 0
            "[Orbal Network Project]\x01",      # 1
            "[Orbal Revolution]\x01",           # 2
            "[Orbments]\x01",                   # 3
            "[Leave]\x01",                      # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1F3")
    MenuTitle(-1, 25, 0, "Orbal Arts")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Orbal arts are a kind of magic which can be\x01",
            "activated by inserting quartz into a battle\x01",
            "orbment--a combat-ready orbment developed\x01",
            "by the Epstein Foundation.\x02\x03",
            "These 'arts,' as they are commonly known, are widely\x01",
            "used by armies, police forces, and bracers across the\x01",
            "continent for their ease of use. Sufficient training\x01",
            "can give anyone access to their incredible power.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E1F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3D0")
    MenuTitle(-1, 25, 0, "Orbal Network Project")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Orbal Network Project is an effort by the Epstein\x01",
            "Foundation to develop a network in which vast\x01",
            "quantities of information can be exchanged between\x01",
            "computers using a series of orbal cables.\x02\x03",
            "While initially a joint effort between the Epstein\x01",
            "Foundation and Liberl's ZCF, the IBC is currently\x01",
            "bankrolling the project. As a result, the network is\x01",
            "currently being tested in Crossbell City.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E3D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6EB")
    MenuTitle(-1, 25, 0, "Orbal Revolution")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Orbal Revolution was a technological revolution\x01",
            "that was brought about 50 years ago by the\x01",
            "invention of orbments.\x02\x03",
            "The public was initially skeptical of this\x01",
            "technological leap, but the invention of the orbal\x01",
            "telephone by the Epstein Foundation and ZCF's\x01",
            "orbal airships quickly proved orbments' practical\x01",
            "value.\x02\x03",
            "Orbments have since become an essential part of our\x01",
            "daily lives. Orbal technology powers everything from\x01",
            "essentials like heating and lighting, to transport\x01",
            "vehicles, to even modern weaponry.\x02\x03",
            "What's more, advancements in technology have\x01",
            "decreased the size of orbal engines, leading to the\x01",
            "development of more capable and affordable\x01",
            "consumer-level automobiles by the Verne and\x01",
            "Reinford companies.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E6EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E92B")
    MenuTitle(-1, 25, 0, "Orbments")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'Orbment' is a general term for devices that operate\x01",
            "by drawing orbal energy from septium.\x01",
            "This technology was invented by Professor C. Epstein.\x02\x03",
            "The internal structure of an orbment allows it to\x01",
            "interact with quartz, which in turn is manufactured\x01",
            "from septium. This design allows for the manufacture\x01",
            "of orbments with nearly limitless potential.\x02\x03",
            "Between their flexibility and ability to recover their\x01",
            "internal orbal energy over time, orbments are\x01",
            "significantly more efficient than combustion engines.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E92B")

    Jump("loc_DFB0")

    label("loc_E930")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_39_DF99 end

    def Function_40_E93D(): pass

    label("Function_40_E93D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E954")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF36")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Q-R Section")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Quartz]\x01",                          # 0
            "[Reinford Company]\x01",                # 1
            "[Remiferia, Principality of]\x01",      # 2
            "[Leave]\x01",                           # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB25")
    MenuTitle(-1, 25, 0, "Quartz")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A quartz is a circuit with a crystalline structure made\x01",
            "by refining and processing septium fragments known\x01",
            "as sepith.\x02\x03",
            "While quartz are both an energy source and capable\x01",
            "of producing variety of phenomena, without the use\x01",
            "of an orbment they are completely powerless.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EB25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECEA")
    MenuTitle(-1, 25, 0, "Reinford Company")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Reinford Company was initially a gunpowder-\x01",
            "based weapons manufacturer based out of the\x01",
            "Erebonian Empire and known for its cannons and\x01",
            "heavy firearms.\x02\x03",
            "Since the Orbal Revolution, however, it has expanded\x01",
            "its operation to include railways and airships.\x01",
            "This expansion has made it one of the continent's\x01",
            "two largest companies, rivaled only by Calvard's\x01",
            "Verne Company.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ECEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF31")
    MenuTitle(-1, 25, 0, "Principality of Remiferia")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The principality located in the northern part of Zemuria.\x01",
            "Though a tough northern country with a cold climate, it\x01",
            "is blessed with abundant forests and lakes, making it an\x01",
            "attractive place for visitors looking for picturesque\x01",
            "landscapes.\x02\x03",
            "It is also known for its highly advanced medical technology,\x01",
            "and is home to the continent's leading medical manufacturers\x01",
            "and specialists. Crossbell State's famous St. Ursula Medical\x01",
            "College was founded in cooperation with the Principality of\x01",
            "Remiferia.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EF31")

    Jump("loc_E954")

    label("loc_EF36")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_40_E93D end

    def Function_41_EF43(): pass

    label("Function_41_EF43")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EF5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2B1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "S Section")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Septian Church]\x01",      # 0
            "[Septium]\x01",             # 1
            "[Leave]\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F14D")
    MenuTitle(-1, 25, 0, "Septian Church")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Septian Church is the most widespread religion\x01",
            "in Zemuria and is based on the worship of the Sky\x01",
            "Goddess, Aidios. Its High Seat is in the Holy City of\x01",
            "Arteria.\x02\x03",
            "Although its influence has decreased somewhat\x01",
            "since the Orbal Revolution, it still has a significant\x01",
            "presence in the continent's education and health\x01",
            "systems.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F14D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2AC")
    MenuTitle(-1, 25, 0, "Septium")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The word 'septium' encompasses seven types of\x01",
            "precious stones mined across Zemuria.\x02\x03",
            "Viewed as symbols of mystery since ancient times,\x01",
            "their value as a resource shot up practically\x01",
            "overnight when the technology to refine sepith,\x01",
            "or septium fragments, into quartz was developed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F2AC")

    Jump("loc_EF5A")

    label("loc_F2B1")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_41_EF43 end

    def Function_42_F2BE(): pass

    label("Function_42_F2BE")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F2D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6DD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "V-Z Section")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Verne Company]\x01",      # 0
            "[ZCF]\x01",                # 1
            "[Leave]\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F500")
    MenuTitle(-1, 25, 0, "Verne Company")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Verne Company is a massive company\x01",
            "headquartered in the Calvard Republic.\x02\x03",
            "Like its industrial rival, the Reinford Company,\x01",
            "the Verne Company was a storied arms manufacturer\x01",
            "that expanded into orbal research and development\x01",
            "after the revolution.\x02\x03",
            "Particularly worth noting are the company's\x01",
            "innovative approaches to the development of orbal\x01",
            "vehicles such as orbal cars and buses.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F500")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6D8")
    MenuTitle(-1, 25, 0, "Zeiss Central Factory (ZCF)")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Zeiss Central Factory, or 'ZCF,' was founded as\x01",
            "the 'Zeiss Engineering Factory' in Liberl Kingdom's\x01",
            "Zeiss City by Professor A. Russell, a disciple of the\x01",
            "great Professor Epstein.\x02\x03",
            "ZCF was the very first orbment manufacturer to\x01",
            "successfully develop an airship. They recently\x01",
            "completed work on the high-speed cruiser Arseille,\x01",
            "a feather in the cap of the Royal Liberlian Army.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F6D8")

    Jump("loc_F2D5")

    label("loc_F6DD")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_42_F2BE end

    def Function_43_F6EA(): pass

    label("Function_43_F6EA")

    EventBegin(0x0)
    Fade(500)
    OP_68(5720, 800, 8440, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18730, 0)
    SetChrPos(0x101, 5000, 150, 7300, 90)
    SetChrPos(0x102, 4750, 150, 8300, 90)
    SetChrPos(0x103, 3500, 150, 7300, 90)
    SetChrPos(0x104, 3250, 150, 8300, 90)
    SetChrSubChip(0xF, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#0000FHi again, Uncle Miles.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PAh, Lloyd. It's good to see you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PHave you come to borrow more books?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FActually, we're here for your request.\x02\x03",
            "I believe you sent a request to the\x01",
            "SSS for help, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FYou were asking for help to locate\x01",
            "and retrieve some overdue books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PBy golly, you're right! I did submit\x01",
            "a request like that, didn't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PLet's get to it, shall we?\x01",
            "Allow me to explain the details.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x5, 0x1, 0x0)
    Call(0, 45)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F952")
    Call(0, 46)

    label("loc_F952")

    SetChrPos(0x0, 5000, 150, 7800, 90)
    EventEnd(0x5)
    Return()

    # Function_43_F6EA end

    def Function_44_F966(): pass

    label("Function_44_F966")

    EventBegin(0x0)
    Fade(500)
    OP_68(5720, 800, 8440, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18730, 0)
    SetChrPos(0x101, 5000, 150, 7300, 90)
    SetChrPos(0x102, 4750, 150, 8300, 90)
    SetChrPos(0x103, 3500, 150, 7300, 90)
    SetChrPos(0x104, 3250, 150, 8300, 90)
    SetChrSubChip(0xF, 0x0)
    OP_0D()

    ChrTalk(
        0xF,
        (
            "#11PAs you said, I've submitted a request for\x01",
            "help retrieving some overdue books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PShall I explain the details to\x01",
            "you, then?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 45)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA83")
    Call(0, 46)

    label("loc_FA83")

    SetChrPos(0x0, 5000, 150, 7800, 90)
    EventEnd(0x5)
    Return()

    # Function_44_F966 end

    def Function_45_FA97(): pass

    label("Function_45_FA97")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",      # 0
            "[Refuse]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB92")

    ChrTalk(
        0x101,
        (
            "#6P#0006FActually, Uncle...\x01",
            "I don't think we have time right now. Sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PAh, is that so? That's unfortunate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PI shall ask once more when your\x01",
            "schedule has freed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB92")

    Return()

    # Function_45_FA97 end

    def Function_46_FB93(): pass

    label("Function_46_FB93")


    ChrTalk(
        0x101,
        "#6P#0000FYeah, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PGreat! I'll get to it, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PWe've had several cases of people\x01",
            "forgetting to return their books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PI'd like for you to locate and return\x01",
            "the books to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0203FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#5P#0300FDoesn't sound too bad to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FSure. Do you have their addresses?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PYep. That information is tied to\x01",
            "their library cards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PGive me a moment to bring it up for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PThe first person is...Fay, who lives in\x01",
            "Bellheim Apartments on West Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PNext, we have Clarice from Acacia\x01",
            "Apartments on East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PLastly, we have Raymond from the CPD\x01",
            "headquarters in the Administrative District.\x02",
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
        0x102,
        "#5P#0106FD-Detective Raymond...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FI'm sorry, Uncle. I wasn't expecting someone\x01",
            "from the department to lack punctuality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PHaha, don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PI'm just hoping that the reader was\x01",
            "engrossed by the contents of their\x01",
            "book and forgot to return it on time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FI am afraid that you have gotten your\x01",
            "hopes up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 350)

    ChrTalk(
        0x103,
        (
            "#6P#0211FThis rotten world is filled with people\x01",
            "who are lazy to their cores.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        (
            "#5P#0306FWh-What the hell are you lookin' at me\x01",
            "like that for?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)

    ChrTalk(
        0x103,
        "#6P#0200FNo reason.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FA-Anyway.\x02\x03",
            "#0000FOur objective is clear. We'll retrieve\x01",
            "those books for you ASAP.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x5A, 0x1F4)

    ChrTalk(
        0xF,
        "#11PGreat, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PPlease return to me once you've collected\x01",
            "all three books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PI'm counting on you, Lloyd.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Overdue Book Retrieval]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x5, 0x1, 0x1)
    Return()

    # Function_46_FB93 end

    def Function_47_10223(): pass

    label("Function_47_10223")

    EventBegin(0x0)
    Fade(500)
    OP_68(5720, 800, 8440, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18730, 0)
    SetChrPos(0x101, 5000, 150, 7300, 90)
    SetChrPos(0x102, 4750, 150, 8300, 90)
    SetChrPos(0x103, 3500, 150, 7300, 90)
    SetChrPos(0x104, 3250, 150, 8300, 90)
    SetChrSubChip(0xF, 0x0)
    OP_0D()

    ChrTalk(
        0xF,
        "#11POh, you're back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PWere you able to collect all of the\x01",
            "overdue books already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0300FSure did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FHere you are.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Returned ",
            scpstr(SCPSTR_CODE_ITEM, 0x2D5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Returned ",
            scpstr(SCPSTR_CODE_ITEM, 0x2D6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Returned ",
            scpstr(SCPSTR_CODE_ITEM, 0x2D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x2D5, 1)
    SubItemNumber(0x2D6, 1)
    SubItemNumber(0x2D7, 1)

    ChrTalk(
        0xF,
        (
            "#11PGreat. Looks like you managed to\x01",
            "collect all three of them in one piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PThanks again. I'm glad I have a group\x01",
            "of reliable folks like you to count on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0100FWe're happy we could help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FI believe this completes your request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PSure does. You'll probably hear\x01",
            "from me again in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FWe look forward to it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Overdue Book Retrieval]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 6)
    SetChrPos(0x0, 5000, 150, 7800, 90)
    OP_29(0x5, 0x2, 0x1F)
    OP_29(0x5, 0x1, 0x5)
    OP_29(0x5, 0x4, 0x10)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    OP_66(0x6, 0x1)
    EventEnd(0x5)
    Return()

    # Function_47_10223 end

    def Function_48_105CF(): pass

    label("Function_48_105CF")

    EventBegin(0x0)
    Fade(500)
    OP_68(5720, 1000, 8220, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18730, 0)
    SetChrPos(0x101, 5000, 150, 7300, 90)
    SetChrPos(0x102, 4750, 150, 8300, 90)
    SetChrPos(0x103, 3500, 150, 7300, 90)
    SetChrPos(0x104, 3250, 150, 8300, 90)
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1067C")
    SetChrPos(0x109, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_106A7")

    label("loc_1067C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_106A7")
    SetChrPos(0x10A, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_106A7")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10881")

    ChrTalk(
        0x101,
        "#6P#0000FHi again, Uncle Miles.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PAh, Lloyd. It's good to see you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PHave you come to borrow more books?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FActually, we're here on business.\x02\x03",
            "I believe you submitted a request\x01",
            "to the SSS, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FYou were asking for help to locate\x01",
            "and retrieve some overdue books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PBy golly, you're right! I did submit\x01",
            "a request like that, didn't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PLet's get to it, shall we?\x01",
            "Allow me to explain the details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A91")

    label("loc_10881")


    ChrTalk(
        0x101,
        "#6P#0000FHi again, Uncle Miles.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PAh, Lloyd. It's good to see you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PCould it be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FYep, we're here for work.\x02\x03",
            "You've requested our help, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PYep, I sure did. I'm glad you guys\x01",
            "came so quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PThank you. I'm in your debt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FI believe you were asking for help to\x01",
            "locate and retrieve overdue books.\x01",
            "Haven't we done this before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PYep. This isn't the first time I've\x01",
            "requested this of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PLet's get to it, shall we?\x01",
            "Allow me to explain the details.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A91")

    OP_29(0x28, 0x1, 0x0)
    Call(0, 50)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AAC")
    Call(0, 51)

    label("loc_10AAC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10AD1")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_10AD1")

    SetChrPos(0x0, 5000, 150, 7800, 90)
    EventEnd(0x5)
    Return()

    # Function_48_105CF end

    def Function_49_10AE5(): pass

    label("Function_49_10AE5")

    EventBegin(0x0)
    Fade(500)
    OP_68(5720, 1000, 8220, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18730, 0)
    SetChrPos(0x101, 5000, 150, 7300, 90)
    SetChrPos(0x102, 4750, 150, 8300, 90)
    SetChrPos(0x103, 3500, 150, 7300, 90)
    SetChrPos(0x104, 3250, 150, 8300, 90)
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10B92")
    SetChrPos(0x109, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_10BBD")

    label("loc_10B92")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10BBD")
    SetChrPos(0x10A, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_10BBD")

    OP_0D()

    ChrTalk(
        0xF,
        (
            "#11PAs you said, I've submitted a request for\x01",
            "help retrieving some overdue books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PShall I explain the details to you?\x02",
    )

    CloseMessageWindow()
    Call(0, 50)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C57")
    Call(0, 51)

    label("loc_10C57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10C7C")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_10C7C")

    SetChrPos(0x0, 5000, 150, 7800, 90)
    EventEnd(0x5)
    Return()

    # Function_49_10AE5 end

    def Function_50_10C90(): pass

    label("Function_50_10C90")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",      # 0
            "[Refuse]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D8B")

    ChrTalk(
        0x101,
        (
            "#6P#0006FActually, Uncle...\x01",
            "I don't think we have time right now. Sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PAh, is that so? That's unfortunate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PI shall ask once more when your\x01",
            "schedule has freed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D8B")

    Return()

    # Function_50_10C90 end

    def Function_51_10D8C(): pass

    label("Function_51_10D8C")


    ChrTalk(
        0x101,
        "#6P#0000FYeah, of course.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FF9")

    ChrTalk(
        0xF,
        "#11PGreat! I'll get to it, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PWe've had several cases of people\x01",
            "forgetting to return their books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PI'd like for you to locate and return\x01",
            "the books to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0203FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0300FDoesn't sound too bad to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11POr so you'd think.\x01",
            "That unfortunately is not the case this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FCare to elaborate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PEach person with an overdue book\x01",
            "lives outside of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PThey live on the outskirts of the state.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0103FOh, I see what you mean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FDo you at least have their addresses?\x02",
    )

    CloseMessageWindow()
    Jump("loc_112D2")

    label("loc_10FF9")


    ChrTalk(
        0xF,
        "#11PGreat! I'll get to it, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PWe've had several cases of people\x01",
            "forgetting to return their books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PI'm terribly sorry, but I'd like for you to\x01",
            "locate and return the books to me\x01",
            "once more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FI am not surprised to see this many people\x01",
            "failing to return their books on time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0300FWell, whatever. Let's just knock this\x01",
            "bad boy outta the park again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PI don't mean to rain on your parade,\x01",
            "but it won't be as easy this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FCare to elaborate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PEvery person with an overdue book\x01",
            "is not a citizen of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PThey all live on the outskirts of the state.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0103FOh, I see what you mean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FDo you at least have their addresses?\x02",
    )

    CloseMessageWindow()

    label("loc_112D2")


    ChrTalk(
        0xF,
        "#11PI sure do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PFirst up is...\x01",
            "Alfred, who lives in Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PNext is Logy. He's a miner that\x01",
            "lives in Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PLastly, we have Flora. A medical intern\x01",
            "at St. Ursula Medical College.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11436")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_11436")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#0003FThey really are on the outskirts...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0306FMan, you're tellin' me we gotta go all\x01",
            "over the state for some books?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0211FI hate disorganized people.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0100FN-Now, now. This isn't so bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PI told you it was going to be difficult.\x01",
            "There was a reason we couldn't\x01",
            "do it ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PAnyway, do you mind taking care of this\x01",
            "for your uncle?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_116D4")

    ChrTalk(
        0x109,
        (
            "#12P#0500FOn the bright side, we can use my car\x01",
            "if we do it right now. That wouldn't be\x01",
            "too bad, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FThat's not a bad idea.\x02\x03",
            "#0000FSounds like we'll be relying on you\x01",
            "to drive us around, Sergeant Major.\x02\x03",
            "I think it's time we get started.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1199F")

    label("loc_116D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11953")

    ChrTalk(
        0x101,
        "#6P#0000FOkay, let's get to this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#12P#0603F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_11786():
        OP_93(0x101, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11786)

    def lambda_11793():
        OP_93(0x102, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11793)

    def lambda_117A0():
        OP_93(0x104, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_117A0)

    def lambda_117AD():
        OP_93(0x103, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_117AD)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x102,
        (
            "#0106F(Detective Dudley's been staring\x01",
            "daggers at us all day...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0303F(He hasn't said anythin' yet, though.\x01",
            "I don't think he plans on stoppin' us.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        "#11PWhat's wrong?\x02",
    )

    CloseMessageWindow()

    def lambda_1189E():
        OP_93(0x101, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1189E)

    def lambda_118AB():
        OP_93(0x102, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_118AB)

    def lambda_118B8():
        OP_93(0x104, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_118B8)

    def lambda_118C5():
        OP_93(0x103, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_118C5)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x101,
        (
            "#6P#0000FN-Nothing at all! We'll get started on\x01",
            "your request right away.\x01",
            "(Let's just get this over with...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1199F")

    label("loc_11953")


    ChrTalk(
        0x101,
        (
            "#6P#0000FLeave it to us. We'll get started on\x01",
            "your request right away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1199F")


    ChrTalk(
        0xF,
        "#11PGreat, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PPlease return to me once you've collected\x01",
            "all three books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PI'm counting on you, everybody.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[State-Wide Overdue Book Retrieval]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x28, 0x1, 0x1)
    Return()

    # Function_51_10D8C end

    def Function_52_11A9B(): pass

    label("Function_52_11A9B")

    EventBegin(0x0)
    Fade(500)
    OP_68(5720, 1000, 8220, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18730, 0)
    SetChrPos(0x101, 5000, 150, 7300, 90)
    SetChrPos(0x102, 4750, 150, 8300, 90)
    SetChrPos(0x103, 3500, 150, 7300, 90)
    SetChrPos(0x104, 3250, 150, 8300, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11B44")
    SetChrPos(0x109, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_11B6F")

    label("loc_11B44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11B6F")
    SetChrPos(0x10A, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_11B6F")

    SetChrSubChip(0xF, 0x0)
    OP_0D()

    ChrTalk(
        0xF,
        "#11POh, you're back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PWere you able to collect all of the\x01",
            "overdue books already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0300FYeah, about damn time we did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FHere you are, Uncle Miles.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Returned ",
            scpstr(SCPSTR_CODE_ITEM, 0x2D8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Returned ",
            scpstr(SCPSTR_CODE_ITEM, 0x2D9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Returned ",
            scpstr(SCPSTR_CODE_ITEM, 0x2DA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x2D8, 1)
    SubItemNumber(0x2D9, 1)
    SubItemNumber(0x2DA, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11D8D")

    ChrTalk(
        0xF,
        (
            "#11PGreat. Looks like you managed to\x01",
            "collect all three of them in one piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PYou've managed to do me yet\x01",
            "another huge favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PAllow me to express my utmost\x01",
            "gratitude again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E36")

    label("loc_11D8D")


    ChrTalk(
        0xF,
        (
            "#11PGreat. Looks like you managed to\x01",
            "collect all three of them in one piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PThanks again. I'm glad I have a group\x01",
            "of reliable folks like you to count on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E36")


    ChrTalk(
        0x101,
        (
            "#6P#0000FHaha... It feels kinda weird hearing\x01",
            "that come from you, Uncle.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11F3C")

    ChrTalk(
        0x109,
        (
            "#12P#0506FWasn't that a bit too challenging\x01",
            "to be a support request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FNot particularly. We handle requests\x01",
            "of a similar nature on a daily basis.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12074")

    label("loc_11F3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12026")

    ChrTalk(
        0x10A,
        (
            "#12P#0603FHmph. These are your famed 'support requests'?\x01",
            "That was far more time consuming than I\x01",
            "was anticipating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0006FS-Sorry about that, Dudley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0103FThis is how our daily routine looks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12074")

    label("loc_12026")


    ChrTalk(
        0x102,
        (
            "#5P#0100FIt may have been difficult, but\x01",
            "I feel like it was worth doing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12074")


    ChrTalk(
        0x103,
        (
            "#6P#0203FAnyway, I believe this completes\x01",
            "your request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PSure does, Tio. Thank you so much!\x01",
            "Again, I really appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FYou're most welcome, Uncle.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[State-Wide Overdue Book Retrieval]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 5000, 150, 7800, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_121CB")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_121CB")

    OP_29(0x28, 0x2, 0x1F)
    OP_29(0x28, 0x1, 0xB)
    OP_29(0x28, 0x4, 0x10)
    OP_66(0x5, 0x1)
    OP_66(0x7, 0x1)
    OP_66(0x9, 0x1)
    EventEnd(0x5)
    Return()

    # Function_52_11A9B end

    def Function_53_121EB(): pass

    label("Function_53_121EB")

    EventBegin(0x0)
    Fade(500)
    OP_68(31560, 5020, -6480, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18590, 0)
    SetChrPos(0x101, 30740, 4000, -6140, 135)
    SetChrPos(0x102, 30340, 4000, -7790, 45)
    SetChrPos(0x103, 29540, 4030, -6520, 135)
    SetChrPos(0x104, 29440, 4030, -7890, 45)
    EndChrThread(0x8, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#0003FI believe the aforementioned 'White Falcon'\x01",
            "is referring to Liberl's national symbol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FLiberl Kingdom is Crossbell State's\x01",
            "friendliest neighbor. They've fostered\x01",
            "a relationship with each other.\x02\x03",
            "Indeed, I've also heard that somewhere.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 30230, 4000, -6690, 90)
    SetChrPos(0x8, 29310, 4000, 0, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    BeginChrThread(0x8, 0, 0, 1)
    OP_29(0x22, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_53_121EB end

    def Function_54_123B4(): pass

    label("Function_54_123B4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(29750, 5020, 5000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 1310, 30, 750, 90)
    SetChrPos(0xEF, 1310, 30, -750, 90)
    SetChrPos(0x153, 3610, 30, 0, 135)
    OP_68(29750, 5020, -5500, 5000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    Fade(500)
    OP_68(17860, 1020, -12620, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23000, 0)
    OP_68(7380, 1030, -11050, 5000)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    OP_68(2250, 1030, -150, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18500, 0)
    OP_0D()
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_93(0x153, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0x153, 0x5A, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x153,
        (
            "#1105F#5PWhoa, look at all these books!\x01",
            "This is soooo cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0002FUhh...have you always been a fan of\x01",
            "books, KeA?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x153, 0x10E, 0x1F4)

    ChrTalk(
        0x153,
        (
            "#1110F#11PHmm... I don't really get them,\x01",
            "but I still like them!\x02\x03",
            "#1109FI get excited looking at all the pretty\x01",
            "colors on the covers!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_126AD")

    ChrTalk(
        0x102,
        (
            "#0109F#6PWe should come back when we have\x01",
            "more time and take a good look at them.\x02\x03",
            "#0102FOur library has a large selection of\x01",
            "children's books for KeA to read through.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12801")

    label("loc_126AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_12769")

    ChrTalk(
        0x103,
        (
            "#0204F#6PWe shall take our time on our next\x01",
            "visit, then.\x02\x03",
            "#0202FThe library has a large assortment of\x01",
            "children's books to read through.\x01",
            "You may find something you like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12801")

    label("loc_12769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_12801")

    ChrTalk(
        0x104,
        (
            "#0309F#6PLet's bring her back again when\x01",
            "we've got more time, then.\x02\x03",
            "#0300FLooks like they have a bunch of children's\x01",
            "books she can read.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12801")

    OP_5A()
    SetChrPos(0x0, 2500, 0, 0, 90)
    SetScenarioFlags(0xB7, 0)
    EventEnd(0x5)
    Return()

    # Function_54_123B4 end

    SaveToFile()

Try(main)
