from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1650.bin",                # FileName
        "t1650",                    # MapName
        "t1650",                    # Location
        0x0058,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 50500, 0, 50000, 90, 0, 1, 88, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1650",                  # 0
        "Doctor Guenter",         # 1
        "Stool",                  # 2
        "Folding Chair",          # 3
        "Folding Chair",          # 4
        "Folding Chair",          # 5
        "Folding Chair",          # 6
        "教授イス",               # 7
    ))

    AddCharChip((
        "chr/ch07102.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
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

    DeclNpc(110690,  150,     57000,   270,  469,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(109380,  0,       57000,   1500,    110690,  1500,    57000,   0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_258",          # 00, 0
        "Function_1_310",          # 01, 1
        "Function_2_371",          # 02, 2
        "Function_3_3E9",          # 03, 3
        "Function_4_3ED",          # 04, 4
        "Function_5_A9E",          # 05, 5
        "Function_6_BF2",          # 06, 6
        "Function_7_C4B",          # 07, 7
        "Function_8_CA4",          # 08, 8
        "Function_9_CFD",          # 09, 9
        "Function_10_D3A",         # 0A, 10
        "Function_11_D8F",         # 0B, 11
        "Function_12_EEA",         # 0C, 12
        "Function_13_1203",        # 0D, 13
        "Function_14_3FA7",        # 0E, 14
        "Function_15_3FDE",        # 0F, 15
        "Function_16_4049",        # 10, 16
        "Function_17_43A0",        # 11, 17
        "Function_18_43DB",        # 12, 18
        "Function_19_440F",        # 13, 19
        "Function_20_6B43",        # 14, 20
        "Function_21_6B44",        # 15, 21
        "Function_22_6B7F",        # 16, 22
        "Function_23_6BBA",        # 17, 23
        "Function_24_6BF5",        # 18, 24
    ))


    def Function_0_258(): pass

    label("Function_0_258")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_298"),
        (1, "loc_2A4"),
        (2, "loc_2B0"),
        (3, "loc_2BC"),
        (4, "loc_2C8"),
        (5, "loc_2D4"),
        (6, "loc_2E0"),
        (SWITCH_DEFAULT, "loc_2EC"),
    )


    label("loc_298")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2A4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2B0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2BC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2C8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2D4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_30F")

    Return()

    # Function_0_258 end

    def Function_1_310(): pass

    label("Function_1_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_31E")
    Jump("loc_34D")

    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_331")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_34D")

    label("loc_331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_33F")
    Jump("loc_34D")

    label("loc_33F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_34D")
    ClearChrFlags(0x8, 0x80)

    label("loc_34D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_361")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)
    Jump("loc_370")

    label("loc_361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_370")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 19)

    label("loc_370")

    Return()

    # Function_1_310 end

    def Function_2_371(): pass

    label("Function_2_371")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_383")
    Jump("loc_3B0")

    label("loc_383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_395")
    OP_66(0x0, 0x1)
    Jump("loc_3B0")

    label("loc_395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3A3")
    Jump("loc_3B0")

    label("loc_3A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_3B0")
    OP_66(0x0, 0x1)

    label("loc_3B0")

    OP_1B(0x1, 0x0, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D1")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_3E8")

    label("loc_3D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E8")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_3E8")

    Return()

    # Function_2_371 end

    def Function_3_3E9(): pass

    label("Function_3_3E9")

    Call(0, 4)
    Return()

    # Function_3_3E9 end

    def Function_4_3ED(): pass

    label("Function_4_3ED")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_481")
    Jump("loc_4CB")

    label("loc_481")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A1")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB")

    label("loc_4A1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C1")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB")

    label("loc_4C1")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CB")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4FE")
    Jump("loc_A96")

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_717")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62B")

    ChrTalk(
        0x8,
        (
            "#2410FAre these pills the fabled Gnosis? Or are they some\x01",
            "different drug...?\x02\x03",
            "#2400FExcuse me for being brash, but as a pharmacologist,\x01",
            "this has piqued my interest.\x02\x03",
            "#2401FAt any rate, you can count on me to analyze these\x01",
            "blue pills and get back to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0208F...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_712")

    label("loc_62B")


    ChrTalk(
        0x8,
        (
            "#2403FA mystery drug that borrows the power of devils...\x01",
            "Without researching, I have no way of knowing if\x01",
            "these pills are the real deal.\x02\x03",
            "#2401FAt any rate, you can count on me to analyze these\x01",
            "blue pills and get back to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_712")

    Jump("loc_A96")

    label("loc_717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_725")
    Jump("loc_A96")

    label("loc_725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 6)), scpexpr(EXPR_END)), "loc_A96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F1")

    ChrTalk(
        0x8,
        (
            "#2400FKeA doesn't seem to like the idea of staying,\x01",
            "so maybe it'd be best to wait to run tests until\x01",
            "her next routine checkup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FI'm sorry about this. I know you took\x01",
            "time out of your day to help us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2404FHaha, it was nothing.\x02\x03",
            "#2405FActually, shouldn't you be trying to\x01",
            "find KeA right about now?\x02\x03",
            "It'd be a problem if she got lost in\x01",
            "a place as big as this, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_90B")

    ChrTalk(
        0x102,
        (
            "#0108FKeA DID look pretty angry.\x01",
            "We should hurry, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CD")

    label("loc_90B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_97E")

    ChrTalk(
        0x103,
        (
            "#0203FIndeed. It would be best for us to\x01",
            "find her before she inconveniences\x01",
            "the hospital staff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CD")

    label("loc_97E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9CD")

    ChrTalk(
        0x104,
        (
            "#0300FHe's right. Let's go find her pronto\x01",
            "and apologize to her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CD")


    ChrTalk(
        0x101,
        "#0000FRight, let's go.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A96")

    label("loc_9F1")


    ChrTalk(
        0x8,
        (
            "#2400FIt's possible that KeA might change\x01",
            "her mind, so I'll go ahead and prepare\x01",
            "some tests, just in case.\x02\x03",
            "If you ever need advice, you know\x01",
            "where to find me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A96")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_4_3ED end

    def Function_5_A9E(): pass

    label("Function_5_A9E")

    EventBegin(0x2)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    MenuCmd(0, 0)
    MenuCmd(1, 0, "[Exit research ward]")
    MenuCmd(1, 0, "[Cancel]")
    MenuCmd(2, 0, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B10"),
        (1, "loc_B1F"),
        (2, "loc_B4C"),
        (SWITCH_DEFAULT, "loc_B5B"),
    )


    label("loc_B10")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B5B")

    label("loc_B1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B47")

    label("loc_B3D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B47")

    Jump("loc_B5B")

    label("loc_B4C")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B5B")

    label("loc_B5B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_B77"),
        (1, "loc_BBE"),
        (2, "loc_BD9"),
        (SWITCH_DEFAULT, "loc_BF1"),
    )


    label("loc_B77")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B98")
    Call(0, 16)
    Jump("loc_BB9")

    label("loc_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BAE")
    Call(0, 20)
    Jump("loc_BB9")

    label("loc_BAE")

    EventEnd(0x5)
    NewScene("t1600", 104, 0, 0)
    IdleLoop()

    label("loc_BB9")

    Jump("loc_BF1")

    label("loc_BBE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("t1620", 114, 0, 0)
    IdleLoop()
    Jump("loc_BF1")

    label("loc_BD9")

    SetChrPos(0x0, 100500, 0, 50000, 90)
    EventEnd(0x5)
    Jump("loc_BF1")

    label("loc_BF1")

    Return()

    # Function_5_A9E end

    def Function_6_BF2(): pass

    label("Function_6_BF2")


    def lambda_BF7():
        OP_95(0xFE, -4460, 0, 90610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF7)

    def lambda_C11():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C11)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_C2A():
        OP_95(0xFE, -7820, 0, 90540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C2A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_6_BF2 end

    def Function_7_C4B(): pass

    label("Function_7_C4B")


    def lambda_C50():
        OP_95(0xFE, -4460, 0, 90610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C50)

    def lambda_C6A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C6A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_C83():
        OP_95(0xFE, -5900, 0, 89580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C83)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_7_C4B end

    def Function_8_CA4(): pass

    label("Function_8_CA4")


    def lambda_CA9():
        OP_95(0xFE, -4460, 0, 90610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CA9)

    def lambda_CC3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CC3)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_CDC():
        OP_95(0xFE, -6530, 0, 90480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CDC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_8_CA4 end

    def Function_9_CFD(): pass

    label("Function_9_CFD")


    def lambda_D02():
        OP_95(0xFE, -6720, 0, 95640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D02)
    WaitChrThread(0xFE, 1)

    def lambda_D20():
        OP_95(0xFE, -1680, 0, 99810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D20)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_9_CFD end

    def Function_10_D3A(): pass

    label("Function_10_D3A")


    def lambda_D3F():
        OP_95(0xFE, 57520, 0, 58790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D3F)
    WaitChrThread(0xFE, 1)

    def lambda_D5D():
        OP_95(0xFE, 59520, 0, 58790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D5D)
    Sleep(500)

    def lambda_D7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D7A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_10_D3A end

    def Function_11_D8F(): pass

    label("Function_11_D8F")

    OP_68(-5980, 1700, 90160, 0)
    MoveCamera(55, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -2320, 0, 90910, 270)
    SetChrPos(0xEF, -2320, 0, 90910, 270)
    SetChrPos(0x153, -2320, 0, 90910, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(160, 0, 100, 0)
    Sleep(500)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    Sleep(500)
    OP_68(-6980, 1700, 90160, 3000)
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(1000)
    BeginChrThread(0x153, 3, 0, 8)
    Sleep(1000)
    BeginChrThread(0xEF, 3, 0, 7)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x153, 3)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    OP_6F(0x1)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 9)
    Sleep(750)
    OP_68(-6980, 2700, 90160, 6000)
    BeginChrThread(0x153, 3, 0, 9)
    Sleep(325)
    BeginChrThread(0xEF, 3, 0, 9)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x153, 0x1)
    EndChrThread(0x101, 0x3)
    EndChrThread(0xEF, 0x3)
    EndChrThread(0x153, 0x3)
    Sleep(1000)
    Return()

    # Function_11_D8F end

    def Function_12_EEA(): pass

    label("Function_12_EEA")

    FadeToBright(1000, 0)
    OP_68(56390, 1400, 57940, 0)
    MoveCamera(47, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21940, 0)
    SetCameraDistance(20900, 3000)
    SetChrPos(0x101, 57020, 0, 58790, 90)
    SetChrPos(0xEF, 56370, 0, 60220, 135)
    SetChrPos(0x153, 55430, 0, 58580, 90)
    OP_6F(0x10)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pharmacology / Neurology Lab\x01",
            "Doctor Joachim Guenter\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#3600835V#0005F(Looks like this is the place.)\x02\x03",
            "#3600836V#0003FExcuse us. It's Lloyd Bannings,\x01",
            "of the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 59520, 0, 59900, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    NpcTalk(
        0x8,
        "Man's Voice",
        "#3600837V#11P#2SOh, I've been waiting for you!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Man's Voice",
        "#3600838V#11P#2SCome on inside. It's unlocked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600839V#0000FAll right.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 110690, 150, 57000, 270)
    TurnDirection(0x101, 0x153, 500)

    ChrTalk(
        0x101,
        "#3600840V#0000F#11PKeA, follow me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600841V#1110F#6PGot'cha!\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x190)
    Sleep(100)

    def lambda_117E():
        OP_95(0xFE, 57520, 0, 58790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_117E)
    WaitChrThread(0x101, 1)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    Sleep(200)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(750)
    BeginChrThread(0x153, 3, 0, 10)
    Sleep(1000)
    BeginChrThread(0xEF, 3, 0, 10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x153, 3)
    Sleep(500)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_12_EEA end

    def Function_13_1203(): pass

    label("Function_13_1203")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 11)
    Call(0, 12)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch08202.itc", 0x22)
    LoadChrToIndex("apl/ch50383.itc", 0x23)
    OP_68(113550, 1250, 51110, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23130, 0)
    SetChrPos(0x101, 108030, 0, 49200, 270)
    SetChrPos(0xEF, 108030, 0, 48000, 270)
    SetChrPos(0x153, 106810, 0, 48600, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02400.itp")
    FadeToBright(1000, 0)
    OP_68(108440, 1250, 57200, 7000)
    OP_6F(0x1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    ChrTalk(
        0x101,
        "#3600842V#0000FGood afternoon, Doctor.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(200)

    def lambda_136E():
        OP_95(0xFE, 108030, 0, 57600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_136E)
    Sleep(150)

    def lambda_138B():
        OP_95(0xFE, 106810, 0, 57000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_138B)
    Sleep(50)

    def lambda_13A8():
        OP_95(0xFE, 108030, 0, 56400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_13A8)
    Sleep(3000)
    SetChrSubChip(0x8, 0x0)
    WaitChrThread(0x101, 1)

    def lambda_13CD():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13CD)
    WaitChrThread(0x153, 1)

    def lambda_13DE():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_13DE)
    WaitChrThread(0xEF, 1)

    def lambda_13EF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_13EF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_154D")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x8,
        (
            "#3600843VHello, Lloyd. And Elie, right?\x02\x03",
            "#3600847VI appreciated our little duel during\x01",
            "the Anniversary Festival. It was a\x01",
            "lot of fun, thanks to you.\x02",
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
        0x102,
        "#3600845V#0102F#6PYou're the same as ever, Doctor Guenter.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17BB")

    label("loc_154D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1686")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x8,
        (
            "#3600846VHello, Lloyd. And Tio, right?\x02\x03",
            "#3600847VI appreciated our little duel during\x01",
            "the Anniversary Festival. Thanks\x01",
            "to you, I had a lot of fun.\x02",
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
        0x103,
        "#3600848V#0202F#6PYou are the same as usual.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17BB")

    label("loc_1686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_17BB")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x8,
        (
            "#3600849VHello, Lloyd. And Randy, right?\x02\x03",
            "#3600847VI appreciated our little duel during\x01",
            "the Anniversary Festival. It was a\x01",
            "lot of fun, thanks to you.\x02",
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
        "#3600851V#0302F#6PHaha. Never change, doc.\x02",
    )

    CloseMessageWindow()

    label("loc_17BB")


    ChrTalk(
        0x101,
        (
            "#3600852V#0003F#6PI'm sorry about this, Doctor.\x02\x03",
            "#3600853V#0000FI know you're usually supposed to set up\x01",
            "an appointment for these kinds of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600854V#2404F#11POh, no! I was just about to take\x01",
            "a break, anyway.\x02\x03",
            "#3600855V#2401FThe amnesiac you're taking care\x01",
            "of... Is that her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600856V#0001F#6PYes. This is KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600938V#1110F#6PHey, Lloyd.\x02\x03",
            "#3600858VIs this old man with the glasses\x01",
            "going to restore all my memories?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#3600859V#2405F#11PO-Old man?!\x02\x03",
            "#3600860V#2406FHaha. I was hoping my outfit would\x01",
            "make me look younger, but I guess\x01",
            "I can't run from the truth: I'm old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600861V#0011F#6PN-No, you're still plenty young.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x153, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1B0B")

    ChrTalk(
        0x102,
        (
            "#3600862V#0106F#11P(KeA, listen...)\x02\x03",
            "#3600863V#0100F(Even if it's flattery, you should still address\x01",
            "people as mister and miss, okay?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C44")

    label("loc_1B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1B87")

    ChrTalk(
        0x103,
        (
            "#3600864V#0203F#11P(KeA...)\x02\x03",
            "#3600865V#0202F(In times like this, just call people\x01",
            "mister and miss, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C44")

    label("loc_1B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1C44")

    ChrTalk(
        0x104,
        (
            "#3600866V#0306F#11P(Listen up, KeDo...)\x02\x03",
            "#3600867V#0300F(In times like this, just stick with callin'\x01",
            "people mister and miss, even if it's a\x01",
            "little too flatterin', all right?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C44")


    ChrTalk(
        0x153,
        "#3600868V#1105F#6P(That's what I should do?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#3600869V#2406F#11PI don't know what hurt worse,\x01",
            "her line or your pity.\x02\x03",
            "#3600870V#2400FWell, whatever. Why don't you have\x01",
            "a seat?\x02\x03",
            "#3600871VIf you could explain to me the current\x01",
            "situation, that would be extremely helpful.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1DBC")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_1DE3")

    label("loc_1DBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1DD2")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_1DE3")

    label("loc_1DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1DE3")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_1DE3")

    SetChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0x153, 0x22)
    SetChrSubChip(0x153, 0x0)
    SetChrFlags(0x153, 0x4)
    SetChrSubChip(0x8, 0x1)
    OP_68(111390, 2150, 55630, 0)
    MoveCamera(50, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20870, 0)
    SetChrPos(0x8, 111000, 150, 56700, 180)
    SetChrPos(0x153, 111000, 150, 55300, 0)
    SetChrPos(0x101, 112700, 0, 56600, 270)
    SetChrPos(0xEF, 112700, 0, 55500, 270)
    OP_78(0xA, 0xE)
    SetChrPos(0xE, 111000, 0, 57000, 0)
    OP_D3(0xE, 0x0, 0x0, 0x0, 0x0)
    OP_78(0x5, 0xA)
    SetChrPos(0xA, 111000, 0, 55000, 0)
    OP_78(0x6, 0xB)
    SetChrPos(0xB, 113000, 0, 56600, 0)
    OP_D3(0xB, 0x0, 0x15F90, 0x0, 0x0)
    OP_78(0x7, 0xC)
    SetChrPos(0xC, 113000, 0, 55500, 90)
    OP_D3(0xC, 0x0, 0x15F90, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(111390, 1150, 55630, 3000)
    OP_6F(0x1)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#3600872V#2403F#6PI think I understand the general situation.\x02\x03",
            "#3600873V#2401FEven the Septian Church's Thaumaturgy\x01",
            "couldn't recover her memories?\x02\x03",
            "#3600874VThat means, just like the sister said, there\x01",
            "could be an issue with her nervous system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600875V#0006F#11PI was afraid of that.\x02\x03",
            "#3600876V#0013FDo you know of any other way we could\x01",
            "potentially recover her memories?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600877V#2406F#6PI'll be honest with you. Research into cranial\x01",
            "nerves and brain cells has only just begun.\x02\x03",
            "#3600878VThere are many different possibilities as to\x01",
            "the source of her amnesia, but no treatment\x01",
            "for the condition currently exists.\x02\x03",
            "#3600879V#2400FHowever...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The doctor pulled out an ophthalmoscope from his coat.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetChrSubChip(0x8, 0x0)
    Sound(882, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x8,
        "#3600880V#2401F#5PKeA. Do you mind looking into my eyes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600881V#1110F#12PSure.\x02\x03",
            "#3600882V#1101F*staaaare*\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    ChrTalk(
        0x8,
        (
            "#3600883V#2403F#5PHmm, no issues with her pupils.\x02\x03",
            "#3600884V#2401FOver the past few days, have you\x01",
            "experienced headaches or nausea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600885V#1105F#12PHeadaches? Nozzy-ah?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3600886V#0000F#5PHe just wants to know if your head\x01",
            "or tummy has been hurting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600887V#1104F#12POh! No, I've felt great.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#3600888V#2401F#5PIs that so? I don't think she has\x01",
            "any brain damage, then.\x02\x03",
            "#3600889V#2403FThat must mean...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_24F1")

    ChrTalk(
        0x102,
        "#3600890V#0101F#11PDo you have some idea, now?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2566")

    label("loc_24F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2532")

    ChrTalk(
        0x103,
        "#3600891V#0201F#11PHave you narrowed it down?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2566")

    label("loc_2532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2566")

    ChrTalk(
        0x104,
        "#3600892V#0301F#11PGot some new idea?\x02",
    )

    CloseMessageWindow()

    label("loc_2566")

    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#3600893V#2403F#6PWell, it's simply my intuition speaking.\x02\x03",
            "#3600894V#2401FIt's possible that this case of amnesia\x01",
            "may be the side-effect of some drug.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3600895V#0007F#11PDrug?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_26C3")

    ChrTalk(
        0x102,
        (
            "#3600896V#0105F#11PYou think some kind of drug caused\x01",
            "her to lose her memories?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2771")

    label("loc_26C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_270B")

    ChrTalk(
        0x103,
        "#3600897V#0205F#11PDoes a drug like that even exist?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2771")

    label("loc_270B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2771")

    ChrTalk(
        0x104,
        (
            "#3600898V#0305F#11PYou're tellin' me meds might be what\x01",
            "caused her to lose her memory?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2771")


    ChrTalk(
        0x8,
        (
            "#3600899V#2403F#6PYes. As few as they are, there have\x01",
            "been cases like that in the past.\x02\x03",
            "#3600900V#2401FA drug's ingredients can sometimes\x01",
            "inhibit certain transmissions to the\x01",
            "nervous system...\x02\x03",
            "#3600901V#2406FThough, in most of those cases,\x01",
            "amnesia is accompanied by a\x01",
            "complete breakdown of the mind.\x02\x03",
            "#3600902VI doubt we will be able to apply the\x01",
            "same rules to KeA's case, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600903V#0008F#11PShe's definitely not crazy, that's\x01",
            "for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2997")

    ChrTalk(
        0x102,
        (
            "#3600904V#0108F#11PRight. She's always been bright\x01",
            "and so full of energy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A33")

    label("loc_2997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_29CE")

    ChrTalk(
        0x103,
        "#3600905V#0208F#11PThat is right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A33")

    label("loc_29CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2A33")

    ChrTalk(
        0x104,
        (
            "#3600906V#0308F#11PDefinitely not. She's a regular girl,\x01",
            "always bouncin' off the wall.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A33")

    SetChrSubChip(0x153, 0x2)
    Sleep(300)

    ChrTalk(
        0x153,
        "#3600907V#1100F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600908V#2403F#6PYou know, the field of pharmacology is\x01",
            "still very much developing.\x02\x03",
            "#3600909VIt's not impossible that a drug with these\x01",
            "unknown side-effects has been created.\x02\x03",
            "#3600910V#2401FIn other words, we should look at this from\x01",
            "both possible angles: an issue with the\x01",
            "nervous system and a side-effect of a drug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600911V#0003F#11PThat might be the best idea.\x02\x03",
            "#3600912V#0001FIs it possible to perform some\x01",
            "tests here at St. Ursula?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600913V#2405F#6POf course.\x02\x03",
            "#3600914V#2406FIt's just, on top of taking a long time, there's\x01",
            "no guarantee that her memories can even\x01",
            "be recovered at this point.\x02\x03",
            "#3600915V#2400FBut if you're fine with that, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600916V#0006F#11PThat's not very reassuring...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2D71")

    ChrTalk(
        0x102,
        "#3600917V#0108F#11PExactly how long would it be?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E10")

    label("loc_2D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2DC0")

    ChrTalk(
        0x103,
        "#3600918V#0201F#11PHow long would these tests take, Doctor?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E10")

    label("loc_2DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2E10")

    ChrTalk(
        0x104,
        (
            "#3600919V#0301F#11PSo how long's this test supposed\x01",
            "to take, Doc?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E10")


    ChrTalk(
        0x8,
        (
            "#3600920V#2403F#6PProbably around three days.\x02\x03",
            "#3600921V#2401FBut, if possible, I would like to run\x01",
            "tests on her here for at least a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600922V#0003F#11PThree days at the minimum...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600923V#2406F#6PThat's how long it will take for the test\x01",
            "pursuing the drug possibility to finish.\x02\x03",
            "#3600924VIt involves analyzing what's excreted from\x01",
            "one's body using certain chemicals.\x02\x03",
            "#3600925V#2400FNow, this is usually a costly examination,\x01",
            "but we can lower the medical fees, given\x01",
            "how unusual this case is.\x02\x03",
            "#3600926VHow does that sound?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3600927V#0002F#5PHey, KeA.\x02\x03",
            "#3600928VWould you mind staying at the\x01",
            "hospital for the next three days?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x153,
        (
            "#3600929V#1100F#6PStay here?\x02\x03",
            "#3600930VSure, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600931V#0012F#5PReally?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3154")

    ChrTalk(
        0x102,
        "#3600932V#0109F#11PThat's a relief.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31D8")

    label("loc_3154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_31A7")

    ChrTalk(
        0x103,
        (
            "#3600933V#0204F#11PShe agreed quicker than I\x01",
            "thought she would.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D8")

    label("loc_31A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_31D8")

    ChrTalk(
        0x104,
        "#3600934V#0309F#11PThat was quick!\x02",
    )

    CloseMessageWindow()

    label("loc_31D8")

    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#3600935V#2404F#6PWonderful. Shall we go ahead and\x01",
            "start the initial examinations?\x02\x03",
            "#3600936V#2400FIf she has any personal things or\x01",
            "clothes, you should probably drop\x01",
            "them by when you can.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3600937V#0000F#11PYes. We'll make sure to bring\x01",
            "them by sometime soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600857V#1111F#6PHey, Lloyd.\x02\x03",
            "#3600939VI'm okay with staying here, but\x01",
            "can I still sleep with you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x101,
        "#3600940V#0011F#5PKeA? U-Uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600941V#1106F#6PIf I can't, I'm sure I'll live, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600942V#0006F#5PThat's not it, KeA.\x02\x03",
            "#3600943V#0002FYou see, only you would be\x01",
            "staying at the hospital.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x153,
        (
            "#3600944V#1105F#6PWhat?\x02\x03",
            "#3600945V#1110FThen where are you guys\x01",
            "going to sleep?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600946V#0004F#5PWell, we're going to keep staying\x01",
            "in the old SSS building.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3600947V#0000F#5P#1KBut I promise we'll come see you\x01",
            "every day--\x02",
        )
    )

    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x153,
        "#3600948V#1103F#6P#1KNo.\x02",
    )

    OP_57(0x1)
    OP_5A()

    ChrTalk(
        0x101,
        "#3600949V#0005F#5PHuh?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    SetChrPos(0x153, 111510, 0, 55700, 45)
    Sound(820, 0, 100, 0)
    ClearChrFlags(0x153, 0x4)
    SetChrSubChip(0x8, 0x1)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x153,
        (
            "#3600950V#1101F#6PYou guys want to get rid of me...\x02\x03",
            "#3600951V#1107FYou don't want to take care of me anymore!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#3600952V#0013F#5PThat's not true!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3744")

    ChrTalk(
        0x102,
        (
            "#3600953V#0106F#11PY-You would just be staying here\x01",
            "for a few days...\x02\x03",
            "#3600954V#0102FAfter that, you can come live with\x01",
            "us, just like you have been.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_387B")

    label("loc_3744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_37E0")

    ChrTalk(
        0x103,
        (
            "#3600955V#0206F#11PIt is just for a few days, KeA.\x02\x03",
            "#3600956V#0202FAfter that, you can continue living\x01",
            "with us, just like you have been.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_387B")

    label("loc_37E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_387B")

    ChrTalk(
        0x104,
        (
            "#3600957V#0306F#11PCome on. He said it's just for a lil' bit.\x02\x03",
            "#3600958V#0300FOnce it's over, you'll come back and\x01",
            "live with us like normal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_387B")


    ChrTalk(
        0x153,
        (
            "#3600959V#1101F#6PI don't care!\x02\x03",
            "#3600960VI don't want to stay at that\x01",
            "guild OR this hospital!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(110240, 1150, 54670, 1000)
    BeginChrThread(0x153, 3, 0, 14)
    Sleep(300)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0xEF, 0x1)
    Sleep(600)
    SetChrSubChip(0x8, 0x2)
    WaitChrThread(0x153, 3)

    ChrTalk(
        0x101,
        "#3600961V#0011F#5P#NK-KeA?!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x153,
        "#3600962V#1107F#4S#6PYou're so stupid, Lloyd!\x02",
    )

    CloseMessageWindow()
    OP_68(100850, 1150, 50000, 3000)
    BeginChrThread(0x153, 3, 0, 15)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#3600963V#0007F#12PKeA, wait!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(112060, 1150, 56390, 0)
    MoveCamera(50, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20870, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3A6D")

    ChrTalk(
        0x102,
        (
            "#3600964V#0106F#11P*sigh* We could have done\x01",
            "that more elegantly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AE8")

    label("loc_3A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3AAA")

    ChrTalk(
        0x103,
        "#3600965V#0206F#11P*sigh* She is furious.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AE8")

    label("loc_3AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3AE8")

    ChrTalk(
        0x104,
        "#3600966V#0306F#11PWhew... She's mad. Real mad.\x02",
    )

    CloseMessageWindow()

    label("loc_3AE8")


    ChrTalk(
        0x101,
        "#3600967V#0006F#5PGeez...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0xEF, 0x0)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#3600968V#0001F#11PI'm sorry about this, Doctor Guenter.\x01",
            "You went through all this trouble and...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#3600969V#2409F#6PIt's fine. Besides, in that state, forcing\x01",
            "her to take the tests would just backfire.\x02\x03",
            "#3600970V#2400FActually, I don't know if those tests\x01",
            "would have produced any helpful results\x01",
            "in the first place.\x02\x03",
            "#3600971VHow about we pick up where we left off\x01",
            "once she's cooled her head?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600972V#0006F#11PAll right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600973V#2404F#6PWaiting for her memories to return\x01",
            "naturally might be a good plan, too.\x02\x03",
            "#3600974V#2400FIf you ever need advice on the matter,\x01",
            "don't hesitate to give me a call.\x02\x03",
            "#3600975VIn the meantime, I'll look into some of\x01",
            "these amnesia cases during my free\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600976V#0002F#11PThanks a lot, Doctor.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3E52")

    ChrTalk(
        0x102,
        "#3600977V#0104F#11PThis means a lot.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EC3")

    label("loc_3E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3E94")

    ChrTalk(
        0x103,
        "#3600978V#0204F#11PWe will be counting on you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EC3")

    label("loc_3E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3EC3")

    ChrTalk(
        0x104,
        "#3600979V#0304F#11P'Preciate it.\x02",
    )

    CloseMessageWindow()

    label("loc_3EC3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x52, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0xA, 0, 0, 0, 0)
    SetChrPos(0xB, 0, 0, 0, 0)
    SetChrPos(0xC, 0, 0, 0, 0)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_D3(0xE, 0x0, 0x15F90, 0x0, 0x0)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    SetChrPos(0x0, 107040, 0, 52930, 180)
    SetChrPos(0x8, 110690, 150, 57000, 270)
    OP_4C(0x8, 0xFF)
    OP_66(0x0, 0x1)
    SetScenarioFlags(0xA8, 6)
    OP_29(0x48, 0x1, 0x8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_1203 end

    def Function_14_3FA7(): pass

    label("Function_14_3FA7")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, 111670, 0, 54050, 5000, 0x1)
    OP_95(0xFE, 109780, 0, 53980, 5000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_14_3FA7 end

    def Function_15_3FDE(): pass

    label("Function_15_3FDE")

    OP_93(0xFE, 0xE1, 0x1F4)
    OP_95(0xFE, 105220, 0, 50000, 5000, 0x1)
    OP_95(0xFE, 100910, 0, 50000, 5000, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)

    def lambda_401B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_401B)
    OP_95(0xFE, 98450, 0, 50000, 5000, 0x0)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    Sound(107, 0, 100, 0)
    Return()

    # Function_15_3FDE end

    def Function_16_4049(): pass

    label("Function_16_4049")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(56390, 1400, 57940, 0)
    MoveCamera(47, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21440, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 60040, 0, 59000, 270)
    SetChrPos(0xEF, 60040, 0, 59000, 270)
    FadeToBright(1000, 0)
    SetCameraDistance(20900, 2000)
    OP_6F(0x10)
    OP_0D()
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    OP_68(55390, 1400, 57940, 3000)
    BeginChrThread(0x101, 3, 0, 17)
    Sleep(1000)
    BeginChrThread(0xEF, 3, 0, 18)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#3600980V#0006F#6PDarn, I didn't think she'd be\x01",
            "that against it...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_41E9")

    ChrTalk(
        0x102,
        (
            "#3600981V#0102F#11PIsn't the fact that she wants to stay with\x01",
            "us something to be happy about?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42CB")

    label("loc_41E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4249")

    ChrTalk(
        0x103,
        (
            "#3600982V#0202F#11PShe wants to stay with you.\x01",
            "Does that not make you happy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42CB")

    label("loc_4249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_42CB")

    ChrTalk(
        0x104,
        (
            "#3600983V#0302F#11PHaha, think 'bout it like this. KeDo\x01",
            "wants to stay with you SO badly,\x01",
            "she ran away so she could.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42CB")


    ChrTalk(
        0x101,
        (
            "#3600984V#0011F#6PYeah, you make a good point.\x02\x03",
            "#3600985V#0003FFor now, let's focus on finding her.\x02\x03",
            "#3600986V#0008FI just hope she hasn't managed to\x01",
            "get too far away...\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19940, 2000)
    FadeToDark(1000, 0, -1)
    OP_6F(0x10)
    OP_0D()
    SetScenarioFlags(0xA8, 7)
    SetScenarioFlags(0x5C, 2)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_4049 end

    def Function_17_43A0(): pass

    label("Function_17_43A0")


    def lambda_43A5():
        OP_95(0xFE, 55540, 0, 59000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43A5)

    def lambda_43BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_43BF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x190)
    Return()

    # Function_17_43A0 end

    def Function_18_43DB(): pass

    label("Function_18_43DB")


    def lambda_43E0():
        OP_95(0xFE, 57040, 0, 59000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43E0)

    def lambda_43FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_43FA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_43DB end

    def Function_19_440F(): pass

    label("Function_19_440F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis087.itp")
    OP_68(113550, 1250, 51110, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23130, 0)
    SetChrPos(0x101, 108030, 0, 49200, 270)
    SetChrPos(0x102, 108030, 0, 48000, 270)
    SetChrPos(0x103, 106810, 0, 48000, 270)
    SetChrPos(0x104, 106810, 0, 49200, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    FadeToBright(1000, 0)
    OP_68(108440, 1250, 57200, 8000)
    OP_6F(0x1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    ChrTalk(
        0x101,
        "#4200866V#0000FExcuse us.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(200)

    def lambda_4583():
        OP_95(0xFE, 108030, 0, 57600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4583)
    Sleep(150)

    def lambda_45A0():
        OP_95(0xFE, 106810, 0, 57600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_45A0)
    Sleep(50)

    def lambda_45BD():
        OP_95(0xFE, 108030, 0, 56400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_45BD)
    Sleep(100)

    def lambda_45DA():
        OP_95(0xFE, 106810, 0, 56400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_45DA)
    Sleep(3000)
    SetChrSubChip(0x8, 0x0)
    WaitChrThread(0x101, 1)

    def lambda_45FF():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45FF)
    WaitChrThread(0x104, 1)

    def lambda_4610():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4610)
    WaitChrThread(0x102, 1)

    def lambda_4621():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4621)
    WaitChrThread(0x103, 1)

    def lambda_4632():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4632)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x8,
        (
            "#4200867V#2406F#11PWelcome, everyone. How very\x01",
            "nice of you to visit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200868V#0012F#6PUh, about our interruption...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200869V#0106F#6PWe apologize for getting in the\x01",
            "way of your hobby, Doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200870V#2406F#11PIt's fine. Noon IS the ideal time to catch\x01",
            "noble carp...\x02\x03",
            "#4200871V#2401F...but if duty calls, duty calls.\x02\x03",
            "#4200872V#2403FTrust me, I'm not going to hold\x01",
            "a grudge against you for it.\x02",
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
        0x103,
        (
            "#4200873V#0206F#6P(He says that, but I feel like he resents\x01",
            "us with every fiber of his being.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200874V#0306F#6P(A fishin' nut, through and through.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200875V#2409F#11PWell, I'm happy we can leave this\x01",
            "minor feud in the past.\x02\x03",
            "#4200876V#2400FSo, what brings you here today?\x02\x03",
            "#4200877VDo you need some advice about\x01",
            "KeA's condition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200878V#0000F#6PActually, it's about something else.\x02\x03",
            "#4200879V#0006FKeA's the same as usual, though.\x01",
            "There hasn't been any improvement\x01",
            "with her memories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200880V#2410F#11PHmm, I see...\x02\x03",
            "#4200881V#2400FPersonally, I think you should have\x01",
            "had her hospitalized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200882V#0108F#6PAbout that... We tried suggesting it\x01",
            "to her again, albeit indirectly, but\x01",
            "she just won't have it.\x02\x03",
            "#4200883V#0106FI'm sorry we keep putting it off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200884V#2404F#11PYou can take your time, but\x01",
            "please, consider the option.\x02\x03",
            "#4200885V#2400FSo, what's this other matter?\x02\x03",
            "#4200886VIs it related to my field of\x01",
            "expertise, by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200887V#0003F#6PIt is. That's why we came today.\x02\x03",
            "#4200888V#0001FWould you mind taking a look at this\x01",
            "drug for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4200889V#2405F#11POh?\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)

    AnonymousTalk(
        0x8,
        (
            "#4200890V#2405FThese pills...\x02\x03",
            "#4200891V#2401FThey're so blue... A coloring agent\x01",
            "wouldn't be able to produce this.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#4200892V#0006FWe found these pills among the\x01",
            "possessions of a certain individual.\x02\x03",
            "#4200893V#0013FWe suspect they're illegal drugs.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    ChrTalk(
        0x8,
        (
            "#4200894V#2403F#11PI think I understand.\x02\x03",
            "#4200895V#2401FPlease, would you fill me in on the rest\x01",
            "of the details?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 102150, 150, 55850, 0)
    SetChrPos(0x101, 103000, 150, 55880, 0)
    SetChrPos(0x102, 103850, 150, 55890, 0)
    SetChrPos(0x104, 105270, 0, 56100, 315)
    SetChrPos(0x8, 102990, 150, 58690, 180)
    SetChrSubChip(0x8, 0x0)
    OP_68(103000, 1950, 57370, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    OP_68(103000, 950, 57370, 3000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#4200896V#2403F#5PI see...\x02\x03",
            "#4200897V...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200898V#0008F#12PSo, Doctor Guenter...\x02\x03",
            "#4200899V#0001F...do you know anything about these blue pills?\x02\x03",
            "#4200900VMaybe where they might have been developed\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200901V#2406F#5PI'm sorry to say, but I haven't seen this type\x01",
            "of drug before.\x02\x03",
            "#4200902V#2401FAs a pharmacologist, I have contacts in every\x01",
            "pharmaceutical company in Zemuria.\x02\x03",
            "#4200903VI typically receive samples of all newly-\x01",
            "developed medicine. However...\x02\x03",
            "#4200904V...I've never seen a pill of this coloration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200905V#0006F#12PThat's a surprise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200906V#2403F#5PAnd what's more, the effects of these pills\x01",
            "are particularly interesting.\x02\x03",
            "#4200907VA boost in strength, focus, reflexes,\x01",
            "judgment, and even intuition...?\x02\x03",
            "#4200908V#2401FIt managed to improve every single\x01",
            "one of those attributes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200909V#0106F#12PWell, we haven't been able to confirm\x01",
            "whether or not the mafia have been\x01",
            "taking these drugs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200910V#0301F#11PThat miner's been the only confirmed\x01",
            "case, so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200911V#0206F#6PAnd nothing has truly substantiated\x01",
            "Mr. Grimwood's rumor, yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200912V#2410F#5PEither way, I can tell you right now\x01",
            "that this is no ordinary drug.\x02\x03",
            "#4200913V#2400FHow about this? Allow me to keep\x01",
            "three of these pills.\x02\x03",
            "#4200914VI can conduct a composition analysis\x01",
            "right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200915V#0004F#12PThat would be great.\x02\x03",
            "#4200916V#0000FDo you know how long it will\x01",
            "take for the analysis to finish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200917V#2400F#5PWell, I have the medicine on me and\x01",
            "a general idea of its effects.\x02\x03",
            "#4200918VI'd like to think I'll have its composition\x01",
            "figured out by the end of the day...\x02\x03",
            "#4200919V#2406FBut if I'm not able to do that, this may\x01",
            "take a considerable amount of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200920V#0006F#12PSo we're flipping a coin, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200921V#2400F#5PI can contact you tomorrow around\x01",
            "noon to let you know how it's going.\x02\x03",
            "#4200922VWould that be okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200923V#0002F#12PPerfect. Thanks for your assistance\x01",
            "in all this, Doctor Guenter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200924V#0109F#12PWe'll be relying on your expertise, then.\x02\x03",
            "#4200925V#0105FThat reminds me. Do you think there\x01",
            "are any possible side-effects or toxicity?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200926V#2403F#5PHmm... Without further analysis, I can't\x01",
            "say for sure, but...\x02\x03",
            "#4200927V#2401F...if anything happens to that miner,\x01",
            "call me as soon as possible.\x02\x03",
            "#4200928VI'd like to take appropriate measures\x01",
            "in case you find any others who have\x01",
            "consumed these pills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200929V#0100F#12PWe can do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200930V#0306F#11PWho knows how many people are in\x01",
            "the market for this stuff?\x02\x03",
            "#4200931V#0301FWe're constantly hearin' rumors about\x01",
            "it in the city, y'know.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(200)

    ChrTalk(
        0x103,
        (
            "#4200932V#0206F#6POf course, it is impossible for us to\x01",
            "question Revache about this, but...\x02\x03",
            "#4200933V#0201F...if their members really are taking it,\x01",
            "I am concerned about the side-effects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200934V#0006F#12PYeah, likewise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4200935V#2403F#5P...\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x103, 0x0)

    ChrTalk(
        0x101,
        "#4200936V#0005F#12PDoctor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200937V#0101F#12PAre you worried about the side-effects, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200938V#2405F#5POh, no. That's not it.\x02\x03",
            "#4200939V#2410FWith all this talk of rumors, I was\x01",
            "reminded of one I've heard recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200940V#0005F#12PYou, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200941V#0301F#11PWhat kinda rumor?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7526", 0)
    SetCameraDistance(25000, 50000)

    ChrTalk(
        0x8,
        (
            "#4200942V#2409F#5PHaha, okay, okay. Remember, none\x01",
            "of this was ever officially confirmed\x01",
            "or explained, but...\x02\x03",
            "#4200943V#2410F...several years back, there was an\x01",
            "odd rumor that floated around the\x01",
            "pharmaceutical industry.\x02\x03",
            "#4200944V#2401FIt talked about a certain religious cult\x01",
            "that had created a new kind of drug.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4200945V#0011F#12PA-A religious cult...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200946V#0105F#12PA sect of radicals... Something like that,\x01",
            "Doctor Guenter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200947V#2403F#5PNo, it's not as simple as that.\x02\x03",
            "#4200948V#2401FApparently, they rejected the very\x01",
            "existence of Aidios and worshiped\x01",
            "devils instead.\x02\x03",
            "#4200949VAt least, that's what I heard.\x02",
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
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4200950V#0005F#12PThey worshiped devils?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200951V#0301F#11PThis story sounds more and more\x01",
            "suspicious by the second...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200952V#0205F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200953V#2400F#5PHaha, I definitely thought it was absurd when I first\x01",
            "heard it, too.\x02\x03",
            "#4200954V#2410FHowever, I can't help but worry about the effects of\x01",
            "that medicine they created...\x02\x03",
            "#4200955V#2401FI've heard that, by borrowing the power of devils,\x01",
            "it can unlock the hidden potential within humans,\x01",
            "even bringing the user good luck.\x02",
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
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#4200956V#0107F#12PTh-That sounds like...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200957V#0013F#12PThe same effects of these pills.\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#4200958V#0208F#6P#40WExcuse me, Doctor Guenter...\x02\x03",
            "#4200959V#0201F#40WDo you know the name of that drug?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200960V#2405F#5PLet's see, what was it again...?\x02\x03",
            "#4200961V#2403FOh, right. I remember now.\x02\x03",
            "#4200962V#2401FThey called it true wisdom--Gnosis.\x01",
            "Or so the rumor goes.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#4200963V#0210F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200964V#0005F#12PGnosis...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200965V#0101F#12PThat's quite the suggestive name, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200966V#2403F#5PWell, because of its absurdity, the story\x01",
            "became somewhat of an urban myth.\x02\x03",
            "#4200967V#2401FBut you've heard the rumors of the secret\x01",
            "society that was connected to that big\x01",
            "incident in Liberl last year, right?\x02\x03",
            "#4200968VMaybe the two could be connected\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200969V#0013F#12P(That must be the society that Estelle\x01",
            "and Joshua told us about.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200970V#0108F#12P(Do you think a devil-worshiping cult\x01",
            "might have some ties to it?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200971V#2410F#5PAnyway, in order to uncover the truth\x01",
            "behind these pills, I plan to contact some\x01",
            "colleagues of mine to help with the analysis.\x02\x03",
            "#4200972V#2400FWhile I do that, I'll also try looking into that\x01",
            "rumor to see if it still has any merit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200973V#0001F#12PWe'd appreciate that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200974V#0301F#11PA drug that borrows the power of devils...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200975V#0206F#6P#40W...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
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
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 110690, 150, 57000, 270)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetChrPos(0x0, 106850, 0, 52690, 180)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0xC3, 4)
    OP_29(0x4C, 0x1, 0x3)
    OP_68(57830, 1200, 58960, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21440, 0)
    SetChrPos(0x101, 60040, 0, 59000, 270)
    SetChrPos(0x102, 60040, 0, 59000, 270)
    SetChrPos(0x103, 60040, 0, 59000, 270)
    SetChrPos(0x104, 60040, 0, 59000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    SetCameraDistance(20900, 2000)
    OP_6F(0x10)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)
    OP_68(55830, 1200, 58960, 3000)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 22)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 23)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 24)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    Sound(107, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#4200976V#0006F#6PI can't say I was expecting to hear a\x01",
            "story like that when we walked in, but...\x02\x03",
            "#4200977V#0000F...for now, we should just trust the\x01",
            "doctor with the composition analysis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200978V#0100F#5PI agree. We need to return to Crossbell\x01",
            "City before it gets dark.\x02\x03",
            "#4200979VBesides, the First Division's investigation\x01",
            "report might have been delivered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200980V#0306F#11POh, I sure love spendin' all night\x01",
            "starin' at a bunch of papers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200981V#0208F#12P#40W...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(21400, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0xC3, 5)
    OP_29(0x4C, 0x1, 0x4)
    EventEnd(0x5)
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_19_440F end

    def Function_20_6B43(): pass

    label("Function_20_6B43")

    Return()

    # Function_20_6B43 end

    def Function_21_6B44(): pass

    label("Function_21_6B44")


    def lambda_6B49():
        OP_95(0xFE, 54500, 0, 59000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B49)

    def lambda_6B63():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6B63)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_21_6B44 end

    def Function_22_6B7F(): pass

    label("Function_22_6B7F")


    def lambda_6B84():
        OP_95(0xFE, 56000, 0, 59800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B84)

    def lambda_6B9E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6B9E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xE1, 0x12C)
    Return()

    # Function_22_6B7F end

    def Function_23_6BBA(): pass

    label("Function_23_6BBA")


    def lambda_6BBF():
        OP_95(0xFE, 56000, 0, 58000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6BBF)

    def lambda_6BD9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6BD9)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x13B, 0x12C)
    Return()

    # Function_23_6BBA end

    def Function_24_6BF5(): pass

    label("Function_24_6BF5")


    def lambda_6BFA():
        OP_95(0xFE, 57000, 0, 59000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6BFA)

    def lambda_6C14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6C14)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x10E, 0x12C)
    Return()

    # Function_24_6BF5 end

    SaveToFile()

Try(main)
