from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t114b.bin",                # FileName
        "t114b",                    # MapName
        "t114b",                    # Location
        0x0049,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 73, 0, 3, 0, 4],
    )

    BuildStringList((
        "t114b",                  # 0
        "Kilika",                 # 1
        "Don Marconi",            # 2
        "Speaker Hartmann",       # 3
        "Guide Berkeley",         # 4
        "Butler Christoph",       # 5
        "Judy",                   # 6
        "Imelda",                 # 7
        "Man in Suit",            # 8
        "Man in Suit",            # 9
        "Invitee",                # 10
        "Invitee",                # 11
        "Invitee",                # 12
        "Invitee",                # 13
        "Invitee",                # 14
        "Invitee",                # 15
        "Invitee",                # 16
        "Invitee",                # 17
        "Invitee",                # 18
        "Invitee",                # 19
    ))

    AddCharChip((
        "chr/ch07302.itc",                   # 00
        "chr/ch06200.itc",                   # 01
        "chr/ch06500.itc",                   # 02
        "chr/ch25800.itc",                   # 03
        "chr/ch36200.itc",                   # 04
        "chr/ch36100.itc",                   # 05
        "chr/ch25900.itc",                   # 06
        "chr/ch25700.itc",                   # 07
        "chr/ch09002.itc",                   # 08
        "chr/ch33000.itc",                   # 09
        "chr/ch32400.itc",                   # 0A
        "chr/ch27702.itc",                   # 0B
        "chr/ch21600.itc",                   # 0C
        "chr/ch33300.itc",                   # 0D
        "chr/ch33002.itc",                   # 0E
        "chr/ch21800.itc",                   # 0F
        "chr/ch33100.itc",                   # 10
        "chr/ch27700.itc",                   # 11
        "chr/ch27900.itc",                   # 12
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

    DeclNpc(-5769,   150,     -18959,  90,   469,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-3500,   0,       2670,    90,   389,  0x0, 0,   1,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-4690,   0,       1710,    180,  389,  0x0, 0,   2,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-1350,   0,       3720,    135,  389,  0x0, 0,   3,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(9,       0,       -24540,  0,    389,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(2680,    0,       -18510,  180,  389,  0x0, 0,   7,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-5690,   0,       -12970,  90,   469,  0x0, 0,   8,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-1899,   0,       5139,    180,  389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(1990,    0,       5139,    180,  389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(1200,    0,       -12069,  22,   389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4070,    0,       -10859,  265,  389,  0x0, 0,   18,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-5670,   150,     -949,    90,   469,  0x0, 0,   11,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-5030,   0,       9,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(2990,    0,       -12119,  336,  389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-910,    0,       -13859,  270,  389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-1970,   0,       -13859,  90,   389,  0x0, 0,   10,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(6389,    150,     -1009,   270,  469,  0x0, 0,   14,  0,   255, 255, 0,   18,  255,  0)
    DeclNpc(3880,    0,       -15199,  135,  389,  0x0, 0,   15,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4159,    0,       -22899,  135,  389,  0x0, 0,   16,  0,   0,   0,   0,   20,  255,  0)

    DeclEvent(0x0000, 0, 26,  0.0,                   -6.5,                  -1.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  2.1666667461395264,    0.20000000298023224,   1.0])
    DeclEvent(0x0040, 0, 25,  -4.28000020980835,     2.509999990463257,     -1.0,                  6.25,                  [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.8560000658035278,    -0.5020000338554382,   0.20000000298023224,   1.0])

    ScpFunction((
        "Function_0_458",          # 00, 0
        "Function_1_510",          # 01, 1
        "Function_2_53B",          # 02, 2
        "Function_3_5C4",          # 03, 3
        "Function_4_71B",          # 04, 4
        "Function_5_755",          # 05, 5
        "Function_6_7AE",          # 06, 6
        "Function_7_A1A",          # 07, 7
        "Function_8_C60",          # 08, 8
        "Function_9_101F",         # 09, 9
        "Function_10_1787",        # 0A, 10
        "Function_11_180E",        # 0B, 11
        "Function_12_187A",        # 0C, 12
        "Function_13_1CF1",        # 0D, 13
        "Function_14_1E54",        # 0E, 14
        "Function_15_2244",        # 0F, 15
        "Function_16_25E6",        # 10, 16
        "Function_17_2750",        # 11, 17
        "Function_18_28FB",        # 12, 18
        "Function_19_2BB6",        # 13, 19
        "Function_20_2E1B",        # 14, 20
        "Function_21_2EC5",        # 15, 21
        "Function_22_2F0C",        # 16, 22
        "Function_23_2F53",        # 17, 23
        "Function_24_3529",        # 18, 24
        "Function_25_498A",        # 19, 25
        "Function_26_4E16",        # 1A, 26
        "Function_27_6113",        # 1B, 27
        "Function_28_6143",        # 1C, 28
        "Function_29_61A1",        # 1D, 29
    ))


    def Function_0_458(): pass

    label("Function_0_458")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_498"),
        (1, "loc_4A4"),
        (2, "loc_4B0"),
        (3, "loc_4BC"),
        (4, "loc_4C8"),
        (5, "loc_4D4"),
        (6, "loc_4E0"),
        (SWITCH_DEFAULT, "loc_4EC"),
    )


    label("loc_498")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4A4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4B0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4BC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4C8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4D4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_50F")

    Return()

    # Function_0_458 end

    def Function_1_510(): pass

    label("Function_1_510")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53A")
    OP_94(0xFE, 0xFFFFFCC2, 0xFFFFFCA4, 0x88E, 0x884, 0x3E8)
    Sleep(300)
    Jump("Function_1_510")

    label("loc_53A")

    Return()

    # Function_1_510 end

    def Function_2_53B(): pass

    label("Function_2_53B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C3")
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, -110, 0, -9870, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(1600)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, -940, 0, -14060, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, 820, 0, -5350, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Jump("Function_2_53B")

    label("loc_5C3")

    Return()

    # Function_2_53B end

    def Function_3_5C4(): pass

    label("Function_3_5C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_5D7")
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_709")

    label("loc_5D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_61D")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 820, 0, -5350, 315)
    BeginChrThread(0xC, 0, 0, 2)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 680, 0, 650, 135)
    BeginChrThread(0xD, 0, 0, 1)
    Jump("loc_709")

    label("loc_61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_663")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 820, 0, -5350, 315)
    BeginChrThread(0xC, 0, 0, 2)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 680, 0, 650, 135)
    BeginChrThread(0xD, 0, 0, 1)
    Jump("loc_709")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_6C4")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    Event(0, 5)
    Jump("loc_709")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_709")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)

    label("loc_709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71A")
    Event(0, 23)

    label("loc_71A")

    Return()

    # Function_3_5C4 end

    def Function_4_71B(): pass

    label("Function_4_71B")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_738")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74B")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_74B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_754")

    label("loc_754")

    Return()

    # Function_4_71B end

    def Function_5_755(): pass

    label("Function_5_755")

    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x11, -3200, 0, 280, 315)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x15, -2040, 0, 1320, 315)
    SetChrFlags(0x15, 0x10)
    SetChrPos(0x16, -1700, 0, 3200, 270)
    SetChrFlags(0x16, 0x10)
    OP_93(0x17, 0xB4, 0x0)
    Return()

    # Function_5_755 end

    def Function_6_7AE(): pass

    label("Function_6_7AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C4")
    Call(0, 24)
    Jump("loc_A19")

    label("loc_7C4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_858")
    Jump("loc_8A2")

    label("loc_858")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_878")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8A2")

    label("loc_878")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_898")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8A2")

    label("loc_898")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8A2")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_940")

    ChrTalk(
        0x8,
        (
            "#3401FSo that's Hartmann, Crossbell's Speaker\x01",
            "of the Diet...\x02\x03",
            "He looks like quite the formidable man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A12")

    label("loc_940")


    ChrTalk(
        0x8,
        (
            "#3400FStill, a chance to quash this auction once\x01",
            "and for all may be closer than I thought.\x02\x03",
            "Make sure you look around and take it\x01",
            "all in. I'm sure this experience will prove\x01",
            "quite useful for you later on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A12")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)

    label("loc_A19")

    Return()

    # Function_6_7AE end

    def Function_7_A1A(): pass

    label("Function_7_A1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_A2B")
    Jump("loc_C5C")

    label("loc_A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_AD5")

    ChrTalk(
        0xFE,
        (
            "I managed to finish cleaning up the\x01",
            "salon. At least for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We still have the afterparty, so I hope you\x01",
            "will stay and join us for that, as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5C")

    label("loc_AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_B49")

    ChrTalk(
        0xFE,
        "Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Hartmann and all the guests have\x01",
            "already gone to the auction venue.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5C")

    label("loc_B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_BB0")

    ChrTalk(
        0xFE,
        "Oh, do you need anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I assure you, we are more than\x01",
            "happy to accommodate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5C")

    label("loc_BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_C5C")

    ChrTalk(
        0xFE,
        (
            "Each dish presented tonight is an\x01",
            "unmatched delicacy, prepared by\x01",
            "the mansion's very own chef.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, feel free to stop me if you\x01",
            "need anything at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5C")

    TalkEnd(0xFE)
    Return()

    # Function_7_A1A end

    def Function_8_C60(): pass

    label("Function_8_C60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_C71")
    Jump("loc_101B")

    label("loc_C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_DCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D39")

    ChrTalk(
        0xFE,
        (
            "Between you and me, those guard\x01",
            "dogs they're keeping in the courtyard\x01",
            "give me the creeps...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what they say, those are\x01",
            "totally Revache & Co.'s war hounds.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DCA")

    label("loc_D39")


    ChrTalk(
        0xFE,
        (
            "Letting war hounds loose in a giant\x01",
            "courtyard? Yeah, no thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What would they do if one escaped\x01",
            "and bit one of the guests? *shudder*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DCA")

    Jump("loc_101B")

    label("loc_DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_EA7")

    ChrTalk(
        0xFE,
        (
            "Since the auction's about to start, they\x01",
            "went ahead and wrapped up dinner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After tonight's auction, an afterparty\x01",
            "will be held in the estate's courtyard.\x01",
            "We would love it if you could attend.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101B")

    label("loc_EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_F5F")

    ChrTalk(
        0xFE,
        (
            "If you can wait a bit longer, the auction\x01",
            "will soon be underway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The opening dinner party will be ending\x01",
            "soon. Please get something to eat while\x01",
            "you still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101B")

    label("loc_F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_101B")

    ChrTalk(
        0xFE,
        (
            "Tonight's dinner party was hosted and\x01",
            "funded by Mr. Hartmann, entirely out\x01",
            "of the kindness of his heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On his behalf, please feel free to eat\x01",
            "to your heart's content.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101B")

    TalkEnd(0xFE)
    Return()

    # Function_8_C60 end

    def Function_9_101F(): pass

    label("Function_9_101F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10B3")
    Jump("loc_10FD")

    label("loc_10B3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10D3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10FD")

    label("loc_10D3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10F3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10FD")

    label("loc_10F3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10FD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1635")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 1)), scpexpr(EXPR_END)), "loc_132D")

    ChrTalk(
        0xFE,
        (
            "Oh, what do we have here...? I know\x01",
            "I've seen those two faces before.\x01",
            "Hyeh hyeh hyeh...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_11B8")

    ChrTalk(
        0x101,
        "#5105FImelda?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_11F9")

    label("loc_11B8")


    ChrTalk(
        0x101,
        (
            "#5105FAren't you that antiques dealer\x01",
            "from the Back Alley?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1231")

    ChrTalk(
        0x102,
        "#5305FWhy in the world are you here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_12AE")

    label("loc_1231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1263")

    ChrTalk(
        0x103,
        "#5405FHow did you end up here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_12AE")

    label("loc_1263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_12AE")

    ChrTalk(
        0x104,
        (
            "#5606FYo, Granny! Why the hell are you\x01",
            "in a place like this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12AE")


    ChrTalk(
        0xFE,
        (
            "Well, an invitation found its way to\x01",
            "my doorstep. Curiosity bid me come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5106F(A shady old lady, as always...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1551")

    label("loc_132D")


    ChrTalk(
        0xFE,
        (
            "Oh, what do we have here...? I believe\x01",
            "you're with the CPD, aren't you?\x02",
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
        "#5105FHow did you figure that out?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hyeh hyeh hyeh! So I was right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I run an old antiques shop\x01",
            "out of Crossbell City's Back Alley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've read stories about you all in the\x01",
            "Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5106FL-Let's ignore our affiliation for now...\x01",
            "So how did you even end up here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, an invitation found its way to my\x01",
            "doorstep and curiosity bid me come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5106F(What a shady old lady...)\x02",
    )

    CloseMessageWindow()

    label("loc_1551")


    ChrTalk(
        0x101,
        "#5101FUm, if you don't mind, could you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Don't worry, I don't intend to snitch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Knowing that you're here, sneaking around\x01",
            "a place crawling with some unsavory people,\x01",
            "is quite amusing for this old woman.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAE, 2)
    Jump("loc_177F")

    label("loc_1635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_1701")

    ChrTalk(
        0xFE,
        (
            "Every time I lay eyes on that Marconi kid,\x01",
            "I can't help but see a big fat raccoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I don't just mean his mannerisms.\x01",
            "His face itself reminds me of a raccoon!\x01",
            "Hyeh hyeh hyeh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_177F")

    label("loc_1701")


    ChrTalk(
        0xFE,
        (
            "I came here with my eyes set on a\x01",
            "certain something, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...this has taken an unexpected turn.\x01",
            "Hyeh hyeh hyeh...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_101F end

    def Function_10_1787(): pass

    label("Function_10_1787")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_180A")

    ChrTalk(
        0xFE,
        (
            "(The boss and Speaker Hartmann\x01",
            "seem like they're in a good mood...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "(With luck, they'll stay that way.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_180A")

    label("loc_180A")

    TalkEnd(0xFE)
    Return()

    # Function_10_1787 end

    def Function_11_180E(): pass

    label("Function_11_180E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_1876")

    ChrTalk(
        0xFE,
        "Hmm...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't mind us. We're simply here to\x01",
            "ensure the safety of our guests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1876")

    label("loc_1876")

    TalkEnd(0xFE)
    Return()

    # Function_11_180E end

    def Function_12_187A(): pass

    label("Function_12_187A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_1B89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A82")
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0xFE, 0)

    ChrTalk(
        0xFE,
        (
            "You really bailed me out of a nasty\x01",
            "situation when you did me that favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to you, those accursed journalists\x01",
            "weren't able to get their story. Ever since\x01",
            "then, everything has been quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2700FHaha. That's good news.\x02\x03",
            "#2703FAs representative of the Crossbell Diet, it's\x01",
            "only natural to lend my strength to others.\x02\x03",
            "#2702FAnd besides, I will need your support in the\x01",
            "coming years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hohoho! I always knew you were a sharp\x01",
            "one, Speaker Hartmann.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    OP_4C(0xA, 0xFF)
    TurnDirection(0xA, 0x14, 0)
    Jump("loc_1B84")

    label("loc_1A82")


    ChrTalk(
        0xFE,
        (
            "I've shown up at this party for several years\x01",
            "now, but they've really gone the extra mile\x01",
            "this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho. I usually try to stay able-bodied, but from\x01",
            "now on, I think I'll wish to get even healthier if it\x01",
            "means I can attend more parties like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B84")

    Jump("loc_1CED")

    label("loc_1B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C53")

    ChrTalk(
        0xFE,
        (
            "Apparently, the centerpiece of the auction\x01",
            "is being kept secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can only assume it is something of immense\x01",
            "value... Perhaps it's something stolen by that\x01",
            "Phantom Thief B?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CED")

    label("loc_1C53")


    ChrTalk(
        0xFE,
        (
            "Apparently, the centerpiece of the auction\x01",
            "is being kept secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can only assume it's something of immense\x01",
            "value... What exactly could it be?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CED")

    TalkEnd(0xFE)
    Return()

    # Function_12_187A end

    def Function_13_1CF1(): pass

    label("Function_13_1CF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_1DA0")

    ChrTalk(
        0xFE,
        "Oh, I can't wait much longer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not sure what things are\x01",
            "going to be shown yet, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have no doubt they'll be\x01",
            "positively charming items.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E50")

    label("loc_1DA0")


    ChrTalk(
        0xFE,
        (
            "If my eyes don't deceive me,\x01",
            "you aren't well acquainted\x01",
            "with the auction, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe... Once you experience the\x01",
            "thrill of the bid, you'll never want\x01",
            "to let it go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E50")

    TalkEnd(0xFE)
    Return()

    # Function_13_1CF1 end

    def Function_14_1E54(): pass

    label("Function_14_1E54")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EE8")
    Jump("loc_1F32")

    label("loc_1EE8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F08")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F32")

    label("loc_1F08")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F28")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F32")

    label("loc_1F28")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F32")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_2177")
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20DF")

    ChrTalk(
        0xFE,
        (
            "It is a pleasure to finally make your\x01",
            "acquaintance, Speaker Hartmann.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am most grateful for the invitation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2705FOh? You're that Republican diet member,\x01",
            "are you not?\x02\x03",
            "#2700FGood. I've been meaning to meet you for\x01",
            "a while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gahaha. Is that so? Does that mean\x01",
            "I can expect a healthy relationship\x01",
            "between us now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2702FBut of course.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_216E")

    label("loc_20DF")


    ChrTalk(
        0xFE,
        (
            "Wonderful. That reminds me. I had a gift\x01",
            "prepared for you to show my thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, if I could have a few minutes after\x01",
            "the auction...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_216E")

    OP_4C(0xA, 0xFF)
    Jump("loc_223C")

    label("loc_2177")


    ChrTalk(
        0xFE,
        (
            "Speaker Hartmann's name supposedly carries\x01",
            "quite a lot of influence within the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I could somehow use this opportunity to get\x01",
            "in his good graces...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...my future will be set.\x02",
    )

    CloseMessageWindow()

    label("loc_223C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_1E54 end

    def Function_15_2244(): pass

    label("Function_15_2244")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_23F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2353")
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0xFE, 0)

    ChrTalk(
        0xFE,
        "I have high expectations for you, Marconi.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't screw this up and let some police\x01",
            "dogs dig up something, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3000FBwahahaha, have some faith.\x02\x03",
            "Don't worry, we're always careful\x01",
            "in our endeavors.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    TurnDirection(0x9, 0x16, 0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_23F1")

    label("loc_2353")


    ChrTalk(
        0xFE,
        (
            "Good to hear. Besides, there's no way\x01",
            "the police could ever do something as\x01",
            "bold as exposing the auction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You took the words right out of my mouth.\x02",
    )

    CloseMessageWindow()

    label("loc_23F1")

    Jump("loc_25E2")

    label("loc_23F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2532")

    ChrTalk(
        0xFE,
        (
            "I always have a good chuckle whenever\x01",
            "I think of Crossbell's police department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They could never dream of shedding light\x01",
            "on something like the auction, no matter\x01",
            "how public its existence may be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha... After all, Speaker Hartmann's\x01",
            "authority is absolute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5101F(Damn it...!)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_25E2")

    label("loc_2532")


    ChrTalk(
        0xFE,
        (
            "The Crossbell Police Department\x01",
            "is full of washed-up cops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank goodness they're so incompetent,\x01",
            "otherwise we wouldn't be able to enjoy\x01",
            "such lovely parties. Hahaha!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E2")

    TalkEnd(0xFE)
    Return()

    # Function_15_2244 end

    def Function_16_25E6(): pass

    label("Function_16_25E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_26A7")

    ChrTalk(
        0xFE,
        (
            "I plan to win a marvelous jewel in tonight's\x01",
            "auction and go to this year's afterparty a\x01",
            "new woman!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The exhibits this year better not be\x01",
            "a step down from last year's.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_274C")

    label("loc_26A7")


    ChrTalk(
        0xFE,
        (
            "Here, have a nice, long look at\x01",
            "the esmelas ring I won last year.\x01",
            "Beautiful, is it not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This year, I'm going to win something\x01",
            "that can match its splendor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_274C")

    TalkEnd(0xFE)
    Return()

    # Function_16_25E6 end

    def Function_17_2750(): pass

    label("Function_17_2750")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_280D")

    ChrTalk(
        0xFE,
        (
            "I wonder if there will be any historical\x01",
            "items up for bid this year?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Jewels and things of that sort shine\x01",
            "even brighter when their origins are\x01",
            "veiled in mystery.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28F7")

    label("loc_280D")


    ChrTalk(
        0xFE,
        (
            "It's said that Speaker Hartmann has\x01",
            "connections with Erebonia's Blood\x01",
            "and Iron Chancellor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess that's to be expected from a man\x01",
            "descended from Imperial nobility. His company\x01",
            "isn't going to be the same as a common man's.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F7")

    TalkEnd(0xFE)
    Return()

    # Function_17_2750 end

    def Function_18_28FB(): pass

    label("Function_18_28FB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_298F")
    Jump("loc_29D9")

    label("loc_298F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29AF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29D9")

    label("loc_29AF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29CF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29D9")

    label("loc_29CF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29D9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_2AC2")

    ChrTalk(
        0xFE,
        (
            "Hmph, damn that clever Marconi... His\x01",
            "smugness of being Speaker Hartmann's\x01",
            "dog is infuriating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's obvious that he's being extremely\x01",
            "cautious in order to avoid any flubs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BAE")

    label("loc_2AC2")


    ChrTalk(
        0xFE,
        (
            "Those men in the black suits working security...\x01",
            "they're from Revache & Co., aren't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That Marconi is deep within Speaker\x01",
            "Hartmann's pocket, that much is clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, I'll show him. Dogs like Marconi\x01",
            "don't last long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BAE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_28FB end

    def Function_19_2BB6(): pass

    label("Function_19_2BB6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_2C30")

    ChrTalk(
        0xFE,
        (
            "It would be best to hurry and introduce\x01",
            "myself to Speaker Hartmann...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Okay, time to say hello.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E17")

    label("loc_2C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA6")

    ChrTalk(
        0xFE,
        (
            "Hmm? You look pretty young...and to be\x01",
            "invited here, you must be a noble,\x01",
            "a millionaire or something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you don't mind, could you tell me\x01",
            "your social status?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5105FU-Um, about that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Tense, are you? It's no\x01",
            "wonder, given your age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being curious about you was\x01",
            "uncalled for. Please, accept\x01",
            "my apologies, young man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2E17")

    label("loc_2DA6")


    ChrTalk(
        0xFE,
        (
            "Young or old, everyone here\x01",
            "is a fine man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, then, I suppose I'll go say\x01",
            "hello to some more people.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E17")

    TalkEnd(0xFE)
    Return()

    # Function_19_2BB6 end

    def Function_20_2E1B(): pass

    label("Function_20_2E1B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Why are hounds inside the mansion...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "H-Hey, you! What's with this commotion?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If something happens to me, I swear that\x01",
            "you won't get away with it!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2E1B end

    def Function_21_2EC5(): pass

    label("Function_21_2EC5")

    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x8000)
    Return()

    # Function_21_2EC5 end

    def Function_22_2F0C(): pass

    label("Function_22_2F0C")

    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    Return()

    # Function_22_2F0C end

    def Function_23_2F53(): pass

    label("Function_23_2F53")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -600, 0, 4250, 180)
    SetChrPos(0xEF, 600, 0, 4250, 180)
    Call(0, 22)
    FadeToBright(1000, 0)
    OP_68(0, 1300, -21000, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18490, 0)
    OP_68(0, 1300, 4000, 12000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#3500841V#5101F#5PA full-spread buffet.\x02\x03",
            "#3500842VThere really are a lot of party\x01",
            "guests, too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_31CA")
    TurnDirection(0xEF, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#3500843V#5306F#11PI can't tell what's more stunning,\x01",
            "the food or the drinks...\x02\x03",
            "#3500844V#5301FI bet they hired a professional\x01",
            "chef to make all the dishes.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)

    ChrTalk(
        0x101,
        (
            "#3500845V#5106F#5PI'd love to try them out, if we were\x01",
            "in any other situation...\x02\x03",
            "#3500846VBut honestly, thanks to my nerves,\x01",
            "I don't have much of an appetite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500847V#5302F#11PI can't blame you there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_350C")

    label("loc_31CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3370")

    ChrTalk(
        0x103,
        (
            "#3500848V#5405F#11PEverywhere I look, all I see is piles\x01",
            "and piles of extravagant food...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        "#3500849V#11P#5402FLloyd, are you hungry?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)

    ChrTalk(
        0x101,
        (
            "#3500850V#5106F#5PNo. I think my nerves made me lose any\x01",
            "appetite I may have had.\x02\x03",
            "#3500851V#5100FThough, if you wanted to grab something,\x01",
            "Tio, be my guest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500852V#5404F#11PI am fine. It is not like I'm particularly\x01",
            "hungry or anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_350C")

    label("loc_3370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_350C")

    ChrTalk(
        0x104,
        "#3500853V#5607F#11PWhew, what a spread!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#3500854V#11P#5602FHey, Lloyd. Mind if I conduct\x01",
            "a lil' taste test?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)

    ChrTalk(
        0x101,
        (
            "#3500855V#5106F#5PI don't really mind, but please, lay off\x01",
            "the alcohol for tonight.\x02\x03",
            "#3500856V#5101FWe have to be on our toes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500857V#5606F#11PDamn... I guess I'll have to pass, then.\x02\x03",
            "#3500858V#5601FEating this kinda food without a drink\x01",
            "would be a sin.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_350C")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 5100, 180)
    SetScenarioFlags(0xA5, 2)
    Call(0, 21)
    EventEnd(0x5)
    Return()

    # Function_23_2F53 end

    def Function_24_3529(): pass

    label("Function_24_3529")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-3990, 1800, -19530, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19500, 0)
    SetCameraDistance(18500, 2500)
    SetChrPos(0x101, -4070, 0, -18880, 270)
    SetChrPos(0xEF, -3880, 0, -17470, 225)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03400.itp")
    Sleep(2000)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#3500859V#3405F#5PWould you look at this...\x02",
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
        "#3500900V#5105F#12PAh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3680")

    ChrTalk(
        0x102,
        "#3500861V#5305F#12PKilika?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_36EA")

    label("loc_3680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_36B1")

    ChrTalk(
        0x103,
        "#3500862V#5405F#12PYou are...\x02",
    )

    CloseMessageWindow()
    Jump("loc_36EA")

    label("loc_36B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_36EA")

    ChrTalk(
        0x104,
        "#3500863V#5605F#12PWhoa! That you, Kilika?\x02",
    )

    CloseMessageWindow()

    label("loc_36EA")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x8,
        (
            "#3500864VWhat a surprise.\x02\x03",
            "#3500865VI can't say I was expecting to run\x01",
            "into you two here.\x02",
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
        "#3500866V#5112F#12PYou don't say...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_380F")

    ChrTalk(
        0x102,
        "#3500867V#5306F#12PIt's a long story...\x02",
    )

    CloseMessageWindow()
    Jump("loc_389B")

    label("loc_380F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_384A")

    ChrTalk(
        0x103,
        "#3500868V#5403F#12PWe have our reasons.\x02",
    )

    CloseMessageWindow()
    Jump("loc_389B")

    label("loc_384A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_389B")

    ChrTalk(
        0x104,
        (
            "#3500869V#5609F#12PThere's a simple explanation\x01",
            "for that, I swear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_389B")


    ChrTalk(
        0x8,
        (
            "#3500870V#3404F#5PIt doesn't pertain to me, so I\x01",
            "won't press the issue.\x02\x03",
            "#3500871V#3402FSo, what names should I use\x01",
            "to address you two?\x02",
        )
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
        "#3500872V#5111F#12PWh-What?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_39BB")

    ChrTalk(
        0x102,
        "#3500873V#5301F#12PHow did you know...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A29")

    label("loc_39BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_39F1")

    ChrTalk(
        0x103,
        "#3500874V#5401F#12PHow did you...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A29")

    label("loc_39F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3A29")

    ChrTalk(
        0x104,
        "#3500875V#5606F#12PWait, did you just...?\x02",
    )

    CloseMessageWindow()

    label("loc_3A29")


    ChrTalk(
        0x8,
        (
            "#3500876V#3404F#5PConsidering your affiliation, it's not\x01",
            "hard to guess why you're here.\x02\x03",
            "#3500877VPlus, you're supposed to provide\x01",
            "your name when you hand over\x01",
            "your invitation out front.\x02\x03",
            "#3500878V#3402FSo? How should I address you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3500879V#5106F#12PYou can call me Guy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500880V#3404F#5PHehe. Very well, Guy.\x02\x03",
            "#3500881V#3400FYou can keep calling me Kilika.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500882V#5103F#12PAll right.\x02\x03",
            "#3500883V#5101FSo, what brings you to the Schwarze\x01",
            "Auction, Kilika?\x02\x03",
            "#3500884VInterested in bidding on something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500885V#3404F#5PGiven the nature of my job, I've come\x01",
            "to know my fair share of collectors.\x02\x03",
            "#3500886VAnd so, they politely asked me if I\x01",
            "would inspect what kind of things are\x01",
            "being auctioned off here.\x02\x03",
            "#3500887V#3400FMarket research, if you will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500888V#5106F#12PGot it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500889V#3404F#5PYou know, that Speaker Hartmann strikes\x01",
            "me as quite the shrewd character.\x02\x03",
            "#3500890VThis auction's structure might actually be\x01",
            "foolproof...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500891V#5105F#12PFoolproof?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3E88")

    ChrTalk(
        0x102,
        "#3500892V#5305F#12PWhat do you mean?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EFF")

    label("loc_3E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3EC1")

    ChrTalk(
        0x103,
        "#3500893V#5405F#12PCould you explain?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EFF")

    label("loc_3EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3EFF")

    ChrTalk(
        0x104,
        "#3500894V#5605F#12PWhat's that s'posed to mean?\x02",
    )

    CloseMessageWindow()

    label("loc_3EFF")


    ChrTalk(
        0x8,
        (
            "#3500895V#3400F#5PThink about it. An unknown, underground\x01",
            "auction designed exclusively for the elite...\x02\x03",
            "#3500896VThat's quite the convenient meeting place\x01",
            "for prominent figures across Zemuria.\x02\x03",
            "#3500897V#3403FAnd there's more than just smuggled goods\x01",
            "being sold here. You have bribery material,\x01",
            "illicit fundraiser items, and more.\x02\x03",
            "#3500898VIf said figures tried to dispose of everything in\x01",
            "their own countries, they wouldn't be able to\x01",
            "escape the law.\x02\x03",
            "#3500899V#3402FHowever, such matters are glossed\x01",
            "over in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500860V#5113F#12PYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500901V#3404F#5PThat is exactly why the Empire and Republic have\x01",
            "turned a blind eye to the Schwarze Auction.\x02\x03",
            "#3500902VI expect there's a number of questionable pieces\x01",
            "that will be presented tonight...\x02\x03",
            "#3500903V#3400F...such as some dubious items that both countries\x01",
            "would be more than willing to part with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500904V#5110F#12P...\x02\x03",
            "#3500905VIn other words, this is an international\x01",
            "black market.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4303")

    ChrTalk(
        0x102,
        "#3500906V#5306F#12PThat's outrageous...\x02",
    )

    CloseMessageWindow()
    Jump("loc_438D")

    label("loc_4303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_434E")

    ChrTalk(
        0x103,
        "#3500907V#5406F#12PIt is a nasty situation, all around.\x02",
    )

    CloseMessageWindow()
    Jump("loc_438D")

    label("loc_434E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_438D")

    ChrTalk(
        0x104,
        "#3500908V#5608F#12PThis stuff is nasty business.\x02",
    )

    CloseMessageWindow()

    label("loc_438D")


    ChrTalk(
        0x8,
        (
            "#3500909V#3404F#5POf course, one could claim that such a structure\x01",
            "is only possible because it exists in Crossbell.\x02\x03",
            "#3500910V#3400FThis may be a hard truth to swallow, but...\x02\x03",
            "#3500911V...going against this will be an uphill battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500912V#5108F#12P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_44C7")

    ChrTalk(
        0x102,
        "#3500913V#5308F#11PLloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4545")

    label("loc_44C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4507")

    ChrTalk(
        0x103,
        "#3500914V#5408F#11PHer reasoning is sound...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4545")

    label("loc_4507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4545")

    ChrTalk(
        0x104,
        "#3500915V#5603F#12PAtta way to kill the mood...\x02",
    )

    CloseMessageWindow()

    label("loc_4545")


    ChrTalk(
        0x8,
        (
            "#3500916V#3400F#5PHehe.\x02\x03",
            "#3500917V#3404FHowever... Even if the structure is foolproof,\x01",
            "it's still an unnatural creation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500918V#5105F#12PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500919V#3404F#5PChi encapsulates everything around us,\x01",
            "ever flowing in harmony...\x02\x03",
            "#3500920VUnnatural, distorted constructs are by no\x01",
            "means permanent.\x02\x03",
            "#3500921VOne tiny thing could be enough to make\x01",
            "the whole foundation fall apart.\x02\x03",
            "#3500922V#3400FWhat I mean to say is that perhaps your\x01",
            "efforts will not be in vain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500923V#5102F#12PKilika...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4793")

    ChrTalk(
        0x102,
        "#3500924V#5304F#12PIt's reassuring to hear you say that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4842")

    label("loc_4793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_47E2")

    ChrTalk(
        0x103,
        "#3500925V#5404F#12PI can feel my confidence rising already.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4842")

    label("loc_47E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4842")

    ChrTalk(
        0x104,
        (
            "#3500926V#5609F#12PThat lil' pep talk makes me feel like I can\x01",
            "take on the world!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4842")


    ChrTalk(
        0x8,
        (
            "#3500927V#3404F#5PHehe. It appears that I've taken up quite\x01",
            "a bit of your precious time.\x02\x03",
            "#3500928V#3400FThis is a rare opportunity. You should take\x01",
            "in everything you possibly can tonight.\x02\x03",
            "#3500929VI'm sure that it will serve you well in the\x01",
            "days to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500930V#5100F#12PRight!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -4450, 0, -18670, 90)
    OP_CA(0x1, 0xFF, 0x0)
    ModifyEventFlags(1, 0, 0x80)
    SetScenarioFlags(0xA5, 3)
    EventEnd(0x5)
    Return()

    # Function_24_3529 end

    def Function_25_498A(): pass

    label("Function_25_498A")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4210, 1200, 2390, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(22400, 0)
    SetChrPos(0x101, -990, 0, -870, 315)
    SetChrPos(0xEF, -150, 0, -530, 315)
    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B82")

    ChrTalk(
        0xA,
        (
            "#2703F#11PLadies and gentlemen. The auction will be\x01",
            "starting shortly, and with that, our friends\x01",
            "will become our rivals.\x02\x03",
            "#2702FLet us take this time to deepen our bonds\x01",
            "with friends and partners until it's time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3002F#5PTonight, we intend to present to you fine\x01",
            "men and women some extraordinary goods.\x02\x03",
            "I wish each and every one of you the best\x01",
            "of luck in winning what you desire!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C9B")

    label("loc_4B82")


    ChrTalk(
        0xA,
        (
            "#2702F#11PI assure you, we are happy to discuss\x01",
            "matters unrelated to the auction later.\x02\x03",
            "We hope and pray that you will enjoy a\x01",
            "long and pleasant night with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3004F#5PYes, that's right!\x02\x03",
            "#3002FThe enjoyment of our guests is the true\x01",
            "objective of the Schwarze Auction!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C9B")

    Fade(500)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_68(-150, 1500, -1390, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(22000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DBE")

    ChrTalk(
        0x101,
        (
            "#5113F(Speaker Hartmann of the Imperial Faction\x01",
            "and Revache & Co.'s Don Marconi...)\x02\x03",
            "#5106F(I'd like to speak with them to gauge what\x01",
            "kind of people they are, but I think it would\x01",
            "be best to step away for now.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DFF")

    label("loc_4DBE")


    ChrTalk(
        0x101,
        (
            "#5103F(They might recognize us, so let's back off\x01",
            "for now.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DFF")

    SetChrPos(0x0, -990, 0, -870, 315)
    SetScenarioFlags(0xB4, 3)
    EventEnd(0x5)
    Return()

    # Function_25_498A end

    def Function_26_4E16(): pass

    label("Function_26_4E16")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -1830, 0, -7850, 0)
    SetChrPos(0xEF, -2480, 0, -8680, 0)
    OP_4B(0xB, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 110, 0, 3900, 180)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x40)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 0, 6500, 180)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 0, 6500, 180)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x40)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Call(0, 22)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02700.itp")
    OP_68(-940, 1700, -9470, 0)
    MoveCamera(312, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16360, 0)
    SetCameraDistance(15360, 2000)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3500931V#5105F#6PWhat...?\x02",
    )

    CloseMessageWindow()
    OP_68(2120, 1700, 2009, 2500)
    SetCameraDistance(15000, 2500)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0xB,
        "#3500932V#11PLadies and gentlemen...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3500933V#11PThe sponsor of this event would like to honor\x01",
            "you with his presence and greet you all.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-1340, 1700, -8920, 0)
    MoveCamera(312, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16690, 0)
    SetChrSubChip(0x8, 0x1)
    SetChrSubChip(0xE, 0x1)
    OP_93(0x11, 0x0, 0x0)
    OP_93(0x12, 0x0, 0x0)
    SetChrSubChip(0x13, 0x1)
    OP_93(0x15, 0x0, 0x0)
    OP_93(0x16, 0x0, 0x0)
    OP_93(0x17, 0x0, 0x0)
    SetChrSubChip(0x18, 0x2)
    OP_93(0x19, 0x0, 0x0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(919, 0, 100, 0)
    Sleep(1000)
    Fade(1000)
    OP_68(1520, 1700, 2340, 0)
    MoveCamera(312, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13500, 0)
    OP_68(1520, 1700, 1340, 5000)
    BeginChrThread(0xB, 3, 0, 27)
    Sleep(1000)
    BeginChrThread(0x9, 3, 0, 28)
    Sleep(1000)
    BeginChrThread(0xA, 3, 0, 29)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3500934V#5107F#N(Those two...!)\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5209")

    ChrTalk(
        0x102,
        (
            "#3500935V#5303F#N(...)\x02\x03",
            "#3500936V#5301F(I suppose it was inevitable that we'd meet them.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_531A")

    label("loc_5209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_529E")

    ChrTalk(
        0x103,
        (
            "#3500937V#5401F#N(If I'm not mistaken...)\x02\x03",
            "#3500938V(...that's the mafia's don and the leader\x01",
            "of the Imperial Faction, isn't it?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_531A")

    label("loc_529E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_531A")

    ChrTalk(
        0x104,
        (
            "#3500939V#5603F#N(That's them, eh?)\x02\x03",
            "#3500940V#5600F(The mafia's don and the head of the\x01",
            "Imperial Faction...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_531A")

    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "#3500941VGood evening, everyone!\x02\x03",
            "#3500942VI am Marconi, president of Revache & Co. and\x01",
            "sponsor of this cherished auction.\x02\x03",
            "#3500943VBy my count, this is our eighth annual auction.\x01",
            "My, does time sure fly!\x02\x03",
            "#3500944VI'm happy to announce that attendance increases\x01",
            "with every year, and, of course, we've expanded\x01",
            "our lineup of auction exhibits to account for that.\x02\x03",
            "#3500945VEverything you see before you is the fruit of your\x01",
            "constant understanding and patronage. The night\x01",
            "is yours, my guests!\x02",
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
    Sound(884, 0, 100, 0)
    Sleep(2000)

    ChrTalk(
        0x9,
        (
            "#3500946V#3004F#11PThere is still one other thing that must be addressed.\x02\x03",
            "#3500947VEvery year without fail, one man graciously hosts\x01",
            "us and our auction at this breathtaking mansion.\x02\x03",
            "#3500948V#3002FI present to you a representative of Crossbell State,\x01",
            "a powerful politician within our diet...\x02\x03",
            "#3500949VSpeaker Hartmann!\x02",
        )
    )

    CloseMessageWindow()
    Sound(884, 0, 100, 0)
    OP_68(2120, 1700, 1340, 2000)

    def lambda_56DF():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_56DF)
    WaitChrThread(0xA, 1)
    Sound(920, 0, 100, 0)
    OP_6F(0x1)
    Sleep(1500)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xA,
        (
            "#3500950VThough previously mentioned, allow me to\x01",
            "introduce myself once more. I am Hartmann,\x01",
            "the Speaker of the Crossbell Diet.\x02\x03",
            "#3500951VIt is a great honor to serve as your host and\x01",
            "offer my humble home for tonight's festivities.\x02\x03",
            "#3500952VBelieve me, this is no ordinary auction.\x01",
            "Famous individuals from a multitude of fields\x01",
            "have come to socialize and mingle tonight.\x02\x03",
            "#3500953VRemember, the night is still young. I have\x01",
            "prepared a modest afterparty for you all\x01",
            "following the conclusion of the auction.\x02\x03",
            "#3500954VFor tonight, it would be my pleasure if you\x01",
            "would all consider my home as your home.\x01",
            "Everyone, please enjoy yourselves.\x02",
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
    Sound(884, 0, 100, 0)
    Sleep(500)
    Sound(920, 0, 100, 0)
    Sleep(2000)
    Fade(1000)
    OP_68(-1340, 1700, -8920, 0)
    MoveCamera(312, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16690, 0)
    SetChrPos(0xEF, -2430, 0, -8620, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3500955V#5113F#6P(So those are the two we've heard\x01",
            "so much about...)\x02\x03",
            "#3500956V#5106F(The speaker definitely has the air\x01",
            "of a politician, all right.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5BD8")

    ChrTalk(
        0x102,
        (
            "#3500957V#5308F#6P(Even more so than others. After all, he\x01",
            "believes his authority is unwavering.)\x02\x03",
            "#3500958V#5301F(This is the first time I've seen Revache's\x01",
            "don, but...)\x02\x03",
            "#3500959V(...he looks to be even more cunning than\x01",
            "I thought.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D48")

    label("loc_5BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5C9B")

    ChrTalk(
        0x103,
        (
            "#3500960V#5406F#6P(I'm almost certain that he believes he's\x01",
            "above everyone here.)\x02\x03",
            "#3500961V#5411F(And as for that Don Marconi, I get the\x01",
            "impression he's supremely obstinate.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D48")

    label("loc_5C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5D48")

    ChrTalk(
        0x104,
        (
            "#3500962V#5606F#6P(Could he have his head shoved any\x01",
            "further up his own ass? Typical noble.)\x02\x03",
            "#3500963V#5601F(Revache's don looks like a tough\x01",
            "customer, too.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D48")


    ChrTalk(
        0x101,
        (
            "#3500964V#5103F#6P(Yeah. They aren't going to be easy\x01",
            "to go up against.)\x02\x03",
            "#3500965V#5101F(I would speak with them, but I don't\x01",
            "think that would be a very smart move.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5EA4")

    ChrTalk(
        0x102,
        (
            "#3500966V#5306F#6P(Me, neither. You know, I've met the speaker\x01",
            "on a few occasions.)\x02\x03",
            "#3500967V#5300F(It would be best to avoid direct contact,\x01",
            "if possible.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FC8")

    label("loc_5EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5F50")

    ChrTalk(
        0x103,
        (
            "#3500968V#5403F#6P(Right. It would be prudent to avoid danger\x01",
            "if we can.)\x02\x03",
            "#3500969V#5400F(I recommend we attempt to stay as\x01",
            "inconspicuous as possible.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FC8")

    label("loc_5F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5FC8")

    ChrTalk(
        0x104,
        (
            "#3500970V#5604F#6P(Yeah, no use in playin' with fire.)\x02\x03",
            "#3500971V#5600F(I say we dip while we still can.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FC8")


    ChrTalk(
        0x101,
        (
            "#3500972V#5100F#6P(Agreed. Let's try to sneak out of the\x01",
            "salon without attracting much attention.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -1770, 0, -8090, 0)
    SetChrPos(0x9, -3500, 0, 2670, 90)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x40)
    OP_4C(0x9, 0xFF)
    SetChrPos(0xA, -4690, 0, 1710, 180)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x40)
    OP_4C(0xA, 0xFF)
    SetChrPos(0xB, -1350, 0, 3720, 135)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x40)
    OP_4C(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_93(0x11, 0x16, 0x0)
    OP_93(0x12, 0x109, 0x0)
    SetChrSubChip(0x13, 0x0)
    OP_93(0x15, 0x150, 0x0)
    OP_93(0x16, 0x5A, 0x0)
    OP_93(0x17, 0x10E, 0x0)
    SetChrSubChip(0x18, 0x0)
    OP_93(0x19, 0x87, 0x0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 3)
    Call(0, 21)
    Call(0, 5)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    SetScenarioFlags(0xA5, 4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_26_4E16 end

    def Function_27_6113(): pass

    label("Function_27_6113")


    def lambda_6118():
        OP_95(0xFE, -1310, 0, 3350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6118)
    WaitChrThread(0xFE, 1)

    def lambda_6136():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6136)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_6113 end

    def Function_28_6143(): pass

    label("Function_28_6143")


    def lambda_6148():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6148)

    def lambda_615D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_615D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_6176():
        OP_95(0xFE, 0, 0, 2810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6176)
    WaitChrThread(0xFE, 1)

    def lambda_6194():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6194)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_28_6143 end

    def Function_29_61A1(): pass

    label("Function_29_61A1")


    def lambda_61A6():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61A6)

    def lambda_61BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_61BB)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_61D4():
        OP_95(0xFE, 1200, 0, 3860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61D4)
    WaitChrThread(0xFE, 1)

    def lambda_61F2():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61F2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_61A1 end

    SaveToFile()

Try(main)
