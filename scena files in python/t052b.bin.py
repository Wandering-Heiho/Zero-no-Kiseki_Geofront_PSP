from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t052b.bin",                # FileName
        "t052b",                    # MapName
        "t052b",                    # Location
        0x003F,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 63, 0, 2, 0, 3],
    )

    BuildStringList((
        "t052b",                  # 0
        "Noma",                   # 1
        "Luka",                   # 2
        "Carlos",                 # 3
        "Miner Marlow",           # 4
        "Miner Gantz",            # 5
        "Felicia",                # 6
        "Letina",                 # 7
    ))

    AddCharChip((
        "chr/ch23500.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch23602.itc",                   # 02
        "chr/ch26202.itc",                   # 03
        "chr/ch33300.itc",                   # 04
        "chr/ch34500.itc",                   # 05
        "chr/ch30702.itc",                   # 06
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

    DeclNpc(3700,    0,       4289,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4880,   -750,    -860,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-6130,   -600,    4219,    270,  469,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-9359,   -600,    -1110,   180,  469,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-8659,   -600,    -4480,   0,    469,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(204009,  0,       560,     270,  389,  0x0, 0,   4,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(199529,  0,       3160,    225,  389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)

    DeclActor(3700,    0,       2920,    1000,    3700,    1500,    4290,    0x007E, 0,  4,  0x0000)
    DeclActor(102600,  2000,    1500,    2000,    102600,  3200,    1500,    0x007C, 0,  12, 0x0000)

    ScpFunction((
        "Function_0_250",          # 00, 0
        "Function_1_308",          # 01, 1
        "Function_2_333",          # 02, 2
        "Function_3_41B",          # 03, 3
        "Function_4_432",          # 04, 4
        "Function_5_436",          # 05, 5
        "Function_6_760",          # 06, 6
        "Function_7_861",          # 07, 7
        "Function_8_AB2",          # 08, 8
        "Function_9_C42",          # 09, 9
        "Function_10_E27",         # 0A, 10
        "Function_11_1069",        # 0B, 11
        "Function_12_11C3",        # 0C, 12
        "Function_13_1511",        # 0D, 13
    ))


    def Function_0_250(): pass

    label("Function_0_250")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_290"),
        (1, "loc_29C"),
        (2, "loc_2A8"),
        (3, "loc_2B4"),
        (4, "loc_2C0"),
        (5, "loc_2CC"),
        (6, "loc_2D8"),
        (SWITCH_DEFAULT, "loc_2E4"),
    )


    label("loc_290")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_29C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2A8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2B4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2C0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2CC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_307")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_307")

    Return()

    # Function_0_250 end

    def Function_1_308(): pass

    label("Function_1_308")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_332")
    OP_94(0xFE, 0x31678, 0xFFFFFF1A, 0x321B8, 0x3DE, 0x3E8)
    Sleep(300)
    Jump("Function_1_308")

    label("loc_332")

    Return()

    # Function_1_308 end

    def Function_2_333(): pass

    label("Function_2_333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_341")
    Jump("loc_40B")

    label("loc_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_34F")
    Jump("loc_40B")

    label("loc_34F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_35D")
    Jump("loc_40B")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_36B")
    Jump("loc_40B")

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_379")
    Jump("loc_40B")

    label("loc_379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_387")
    Jump("loc_40B")

    label("loc_387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_395")
    Jump("loc_40B")

    label("loc_395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3A3")
    Jump("loc_40B")

    label("loc_3A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3B1")
    Jump("loc_40B")

    label("loc_3B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3BF")
    Jump("loc_40B")

    label("loc_3BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3CD")
    Jump("loc_40B")

    label("loc_3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_3F4")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_40B")

    label("loc_3F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_402")
    Jump("loc_40B")

    label("loc_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_40B")

    label("loc_40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_41A")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)

    label("loc_41A")

    Return()

    # Function_2_333 end

    def Function_3_41B(): pass

    label("Function_3_41B")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_431")
    OP_66(0x1, 0x1)

    label("loc_431")

    Return()

    # Function_3_41B end

    def Function_4_432(): pass

    label("Function_4_432")

    Call(0, 5)
    Return()

    # Function_4_432 end

    def Function_5_436(): pass

    label("Function_5_436")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_443")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Rest\x01",       # 2
            "Leave\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A3")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C3")
    OP_AF(0x52)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_757")

    label("loc_4C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E3")
    OP_AF(0x50)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_757")

    label("loc_4E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F7")
    Jump("loc_757")

    label("loc_4F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_757")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_640")

    ChrTalk(
        0x8,
        (
            "What'd you think of the room?\x01",
            "Nice and spacious, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's not every day that young folks like you\x01",
            "all decide to stay with us. It falls on me to\x01",
            "treat you right!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, you all going out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Things have been dangerous lately, so\x01",
            "try not to stay out TOO late, all right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_757")

    label("loc_640")


    ChrTalk(
        0x8,
        (
            "The miners usually come here to make\x01",
            "a ruckus, but barely anybody's been\x01",
            "wanting a drink today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh* That's just great. Still, it's not\x01",
            "like I can go blaming Max for being\x01",
            "attacked by a monster...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know what they are exactly,\x01",
            "but they need to cut it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_757")

    Jump("loc_443")

    label("loc_75C")

    TalkEnd(0x8)
    Return()

    # Function_5_436 end

    def Function_6_760(): pass

    label("Function_6_760")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_807")

    ChrTalk(
        0xFE,
        (
            "*sigh* Mr. Gantz... How can your liver\x01",
            "handle getting wasted day after day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish he'd just go home after work,\x01",
            "but that's a longshot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_85D")

    label("loc_807")


    ChrTalk(
        0xFE,
        (
            "Unfortunately, Mr. Gantz is the kind of person\x01",
            "to get cranky after a few drinks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85D")

    TalkEnd(0xFE)
    Return()

    # Function_6_760 end

    def Function_7_861(): pass

    label("Function_7_861")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F5")
    Jump("loc_93F")

    label("loc_8F5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_915")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93F")

    label("loc_915")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_935")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93F")

    label("loc_935")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_93F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A16")

    ChrTalk(
        0xFE,
        "Hmmmm, sake might be a good choice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It sends all your fatigue from\x01",
            "the day packing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just don't drink too much of it.\x01",
            "You'll regret it if you do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_AAA")

    label("loc_A16")


    ChrTalk(
        0xFE,
        (
            "The mining crew seems to be building\x01",
            "up a considerable amount of stress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm hoping some good alcohol will give\x01",
            "them energy for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_861 end

    def Function_8_AB2(): pass

    label("Function_8_AB2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAA")

    ChrTalk(
        0xB,
        "*glug* *glug*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Aaaaaaah! Cracking open a cold\x01",
            "one after work is the best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I can't drink too much, though. I'd never hear\x01",
            "the end of it if I showed up to work hungover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "On top of that, Gantz is a lightweight.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_C3E")

    label("loc_BAA")


    ChrTalk(
        0xB,
        "On top of that, Gantz is a lightweight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If I got too wasted, who'd take his drunk\x01",
            "ass back to his house...?\x01",
            "*sigh* I'm too good a friend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3E")

    TalkEnd(0xFE)
    Return()

    # Function_8_AB2 end

    def Function_9_C42(): pass

    label("Function_9_C42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5D")

    ChrTalk(
        0xC,
        (
            "J-Jusht ya wait... I'm gonna win big\x01",
            "at that cashino, shomeday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Life'll be a breeze after that... *hic*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ugh... Hey, Marlow! Are ya even\x01",
            "lishentin' to me...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yeah, yeah. I am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "C'mon man, how long are you going to\x01",
            "repeat that pipedream?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_E23")

    label("loc_D5D")


    ChrTalk(
        0xC,
        "Damn it, you... *hic*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I shwear to you and tha world... *hic* I'm gonna\x01",
            "hit the jackpot shometime this week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh* Yeah, we're waiting till you sober\x01",
            "up a bit before I drag you home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E23")

    TalkEnd(0xFE)
    Return()

    # Function_9_C42 end

    def Function_10_E27(): pass

    label("Function_10_E27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F56")

    ChrTalk(
        0xFE,
        (
            "You're the ones who rented the room\x01",
            "down the hall, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was trying to get that big room, but the\x01",
            "lady who runs this place said that room\x01",
            "was too spacious for a party of two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, she sure knows her stuff. It's been\x01",
            "a while since someone rejected one of\x01",
            "my whims.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1065")

    label("loc_F56")


    ChrTalk(
        0xFE,
        (
            "Well, we'll just have to make do with\x01",
            "the room we were given.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Besides, there are more important matters\x01",
            "to attend to! I've got to negotiate with the\x01",
            "mayor again tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't rest until those septium crystals are\x01",
            "mine...! They're just within my reach!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1065")

    TalkEnd(0xFE)
    Return()

    # Function_10_E27 end

    def Function_11_1069(): pass

    label("Function_11_1069")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1144")

    ChrTalk(
        0xFE,
        (
            "Oh... I should go return this tableware\x01",
            "to the inn owners while I still can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew... Of course she wanted to eat\x01",
            "in the 'comfort of her own room.' My lady\x01",
            "can truly be a selfish person...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_11BF")

    label("loc_1144")


    ChrTalk(
        0xFE,
        (
            "Bringing her meals to the room is the\x01",
            "easy part... I'm just worried about tripping\x01",
            "when I go to return the tableware.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11BF")

    TalkEnd(0xFE)
    Return()

    # Function_11_1069 end

    def Function_12_11C3(): pass

    label("Function_12_11C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1510")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Stand by until midnight.\x01",             # 0
            "We need to finish other things.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1246"),
        (1, "loc_1443"),
        (SWITCH_DEFAULT, "loc_150E"),
    )


    label("loc_1246")


    ChrTalk(
        0x101,
        (
            "#1200775V#0003FAll right. If we're ready, let's stand by\x01",
            "here until midnight.\x02\x03",
            "#1200776V#0001FWe still need to decide on our strategy\x01",
            "for when the monsters show up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200777V#0201FSimply driving them away from the\x01",
            "town will not be enough, correct...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200778V#0103FRight. We also have to corner the mafia\x01",
            "goons who are pulling the strings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200779V#0302FHeh. This is startin' to sound a bit\x01",
            "trickier than we thought, eh?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_65(0x2, 0x1)
    SetScenarioFlags(0x5C, 0)
    NewScene("t050B", 0, 0, 0)
    IdleLoop()
    Jump("loc_150E")

    label("loc_1443")


    ChrTalk(
        0x104,
        (
            "#1200780V#0300FWell, once we're all prepped, let's\x01",
            "head on back here. Sound good?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you are ready to wait for midnight,\x01",
            "inspect the table.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_150E")

    label("loc_150E")

    EventEnd(0x3)

    label("loc_1510")

    Return()

    # Function_12_11C3 end

    def Function_13_1511(): pass

    label("Function_13_1511")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50111.itc", 0x22)
    OP_68(102070, 4500, 1190, 0)
    MoveCamera(58, 19, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(32299, 0)
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
    SetChrPos(0x101, 102700, 2200, 3100, 180)
    SetChrPos(0x102, 102500, 2200, -300, 0)
    SetChrPos(0x103, 101200, 2200, 1700, 90)
    SetChrPos(0x104, 104400, 2200, 1300, 270)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis021.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis022.itp")
    FadeToBright(1000, 0)
    OP_68(102370, 3300, 1380, 4000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#1200623V#0003F#5PNow, let's try to sort through our information\x01",
            "and come up with a game plan.\x02\x03",
            "#1200624V#0001FMany details were foggy in the CGF's\x01",
            "initial report. We knew about the string\x01",
            "of monster attacks, but not much more...\x02\x03",
            "#1200625VFortunately, our investigation shed light\x01",
            "on many of those points.\x02\x03",
            "#1200626V#0003FBut there's still something important that we\x01",
            "haven't been able to confirm yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200627V#0105F#12PI thought we'd gotten everything...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200628V#0305F#11PHuh? What are you talkin' about?\x02",
    )

    CloseMessageWindow()
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
            "#1KWhat has yet to be confirmed?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Monsters' identity]\x01",       # 0
            "[Monsters' den]\x01",            # 1
            "[Monsters' objective]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1916"),
        (1, "loc_1AB8"),
        (2, "loc_1C8C"),
        (SWITCH_DEFAULT, "loc_1D4F"),
    )


    label("loc_1916")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#1200629V#0006F#5PWe still don't know the monsters' identity...\x01",
            "is what I'd like to say.\x02\x03",
            "#1200630V#0008FBut considering how elusive our culprits\x01",
            "have been, that'd be impossible to confirm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200631V#0206F#6PTrue. If we knew that, we would not be\x01",
            "nearly as stressed as we are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200637V#0003F#5PYou can say that again.\x02\x03",
            "#1200638V#0001FWait...couldn't it be the monsters' objective?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4F")

    label("loc_1AB8")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#1200634V#0006F#5PWe still don't know where the monsters live...\x01",
            "is what I'd like to say.\x02\x03",
            "#1200635V#0008FEven the CGF and all their resources weren't\x01",
            "able to find them during their sweep of the\x01",
            "mountains. There's no chance we could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200636V#0206F#6PIndeed. Four is not nearly enough for a\x01",
            "search of the surrounding mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200632V#0003F#5PYou can say that again.\x02\x03",
            "#1200633V#0001FWait...couldn't it be the monsters' objective?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4F")

    label("loc_1C8C")

    OP_2C(0x3F, 0x3)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#1200639V#0003F#5PWe still haven't pinned down the first\x01",
            "thing detectives usually look for in an\x01",
            "investigation...\x02\x03",
            "#1200640V#0001FThe monsters' objective behind all this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4F")

    label("loc_1D4F")


    ChrTalk(
        0x104,
        (
            "#1200641V#0303F#11PYeah, that's a good point...\x02\x03",
            "#1200642V#0301FTakin' the damage they did at St. Ursula into\x01",
            "account, it doesn't look like they did it 'cause\x01",
            "they had the munchies, does it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200643V#0108F#12PAnd according to Armorica Village's chief,\x01",
            "there's a possibility that all of these attacks\x01",
            "are a warning from the divine wolves, but...\x02\x03",
            "#1200644V#0101F...it's more likely that those black wolves are\x01",
            "our culprits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200645V#0203F#6PYes, I agree.\x02\x03",
            "#1200646V#0201FIf that is the case, our search for an objective\x01",
            "is just as bleak as it was minutes ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200647V#0003F#5PI'm afraid so.\x02\x03",
            "#1200648V#0001FStill, it's too early to conclude that everything\x01",
            "happened because those wolves felt like it.\x02\x03",
            "#1200649VWhile it may only apply to the hospital case,\x01",
            "the wolves must have needed quite the entry\x01",
            "route to reach the roof.\x02\x03",
            "#1200650V#0003FIt's also strange that they left without damaging\x01",
            "anything and seemingly held back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200651V#0103F#12PThat IS peculiar...\x02\x03",
            "#1200652V#0101FIt would be unprofessional to conclude\x01",
            "that it was just the pack's whim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200653V#0303F#11PBasically, our motive is hidin' from us...\x02\x03",
            "#1200654V#0300FThat in itself is a clue, ain't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200655V#0000F#5PExactly, Randy.\x02\x03",
            "#1200656V#0003FIn these sorts of cases, people generally\x01",
            "follow a particular framework.\x02\x03",
            "#1200657VDifferent attacks by the same pack...\x02\x03",
            "#1200658V#0001FI think if we analyze each individual framework,\x01",
            "that could lead us to a proper motive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1200659V#0208F#6PFramework?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1200660V#0000F#5PIt's nothing too complicated.\x02\x03",
            "#1200661V#0004FGenerally, crimes consist of four aspects:\x01",
            "culprit, objective, means, and result...\x02\x03",
            "#1200662V#0000FWhat do you think would happen if we\x01",
            "decided to shift what we know around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1200663V#0205F#6PHow so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200664V#0101F#12PW-Wait a second. I'll write these\x01",
            "out for us to see.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Culprit = Black Wolves\x01",
            "Objective = Unknown\x01",
            "Means = Wolves' Abilities\x01",
            "Result = Property Damage/Injuries\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    ChrTalk(
        0x101,
        "#1200665V#0000F#5PYeah, that's the gist of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200666V#0301F#11PSo how do we go about this\x01",
            "shifting you were talkin' about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200667V#0001F#5PWell, how about this?\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 5)

    label("loc_2612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB3")
    SetScenarioFlags(0x0, 5)
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
            "#1KWhich one corresponds to the 'Culprit'?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Black Wolves\x01",                  # 0
            "Unknown\x01",                       # 1
            "Wolves' Abilities\x01",             # 2
            "Property Damage/Injuries\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26CE")
    ClearScenarioFlags(0x0, 5)

    label("loc_26CE")

    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhich one corresponds to the 'Objective'?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Black Wolves\x01",                  # 0
            "Unknown\x01",                       # 1
            "Wolves' Abilities\x01",             # 2
            "Property Damage/Injuries\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2774")
    ClearScenarioFlags(0x0, 5)

    label("loc_2774")

    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhich one corresponds to the 'Means'?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Black Wolves\x01",                  # 0
            "Unknown\x01",                       # 1
            "Wolves' Abilities\x01",             # 2
            "Property Damage/Injuries\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2816")
    ClearScenarioFlags(0x0, 5)

    label("loc_2816")

    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhich one corresponds to the 'Result'?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Black Wolves\x01",                  # 0
            "Unknown\x01",                       # 1
            "Wolves' Abilities\x01",             # 2
            "Property Damage/Injuries\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28B9")
    ClearScenarioFlags(0x0, 5)

    label("loc_28B9")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A18")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_299E")
    OP_63(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#1200670V#0006F#5P(Hmm... Yeah, I'm not sure where\x01",
            "I was going with all this.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)

    ChrTalk(
        0x101,
        "#1200671V#0005F#5P(What if I try this...?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2A13")

    label("loc_299E")


    ChrTalk(
        0x101,
        (
            "#1200668V#0003F#5P(No, that still doesn't work...)\x02\x03",
            "#1200669V#0001F(Let's give this another try.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A13")

    Jump("loc_2AAE")

    label("loc_2A18")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2A28"),
        (SWITCH_DEFAULT, "loc_2A6B"),
    )


    label("loc_2A28")

    OP_2C(0x3F, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#1200672V#0000F#5P(This has got to be it.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AAE")

    label("loc_2A6B")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#1200673V#0003F#5P(I think this is right?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AAE")

    label("loc_2AAE")

    Jump("loc_2612")

    label("loc_2AB3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Culprit = Unknown\x01",
            "Objective = Wolves' Abilities\x01",
            "Means = Black Wolves\x01",
            "Result = Property Damage/Injuries\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
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
        "#1200674V#0105F#12PThat's it...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200675V#0201F#6PIf we go by this, now...\x02\x03",
            "#1200676VRather than the wolves being the culprits,\x01",
            "they were the means, and using the\x01",
            "wolves' abilities was the objective...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200677V#0305F#11PWhoa, Lloyd. You completely flipped\x01",
            "the case on its head!\x02\x03",
            "#1200678V#0301FSo you're thinkin' that people are behind\x01",
            "the attacks after all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200679V#0003F#5PIf they're able to control the wolves,\x01",
            "it's natural to think so.\x02\x03",
            "#1200680V#0008FOur only problem is not knowing the\x01",
            "exact method of control...\x02\x03",
            "#1200681V#0000FLuckily, we have a particular statement\x01",
            "that can help us guess their method.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200682V#0101F#12PFrom someone we talked to...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#1200683V#0300F#11POh, I think I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200684V#0004F#5PYou picked up on it, too?\x02\x03",
            "#1200685V#0000FYou see, that statement came from...\x02",
        )
    )

    CloseMessageWindow()
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
            "#1KWhat's the name of the witness?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Harold Hayworth]\x01",       # 0
            "[Intern Lytton]\x01",         # 1
            "[Shizuku MacLaine]\x01",      # 2
            "[Noel Seeker]\x01",           # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FC1"),
        (1, "loc_30B6"),
        (2, "loc_31A6"),
        (3, "loc_3245"),
        (SWITCH_DEFAULT, "loc_3335"),
    )


    label("loc_2FC1")


    ChrTalk(
        0x104,
        (
            "#1200686V#0303F#11PUh, you sure 'bout that, bud?\x02\x03",
            "#1200687V#0301FIsn't it that blind girl, Shizuku?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200688V#0011F#5POh, you're right.\x02\x03",
            "#1200689V#0006FShizuku's concrete statement will be the\x01",
            "key to cracking this case wide open.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3335")

    label("loc_30B6")


    ChrTalk(
        0x104,
        (
            "#1200686V#0303F#11PUh, you sure 'bout that, bud?\x02\x03",
            "#1200687V#0301FIsn't it that blind girl, Shizuku?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200688V#0011F#5POh, you're right.\x02\x03",
            "#1200689V#0006FShizuku's statement will be the key\x01",
            "key to cracking this case wide open.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3335")

    label("loc_31A6")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#1200690V#0003F#5PShizuku MacLaine...\x02\x03",
            "#1200691V#0001FThe Divine Blade of Wind's daughter will be\x01",
            "key to cracking this case wide open.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3335")

    label("loc_3245")


    ChrTalk(
        0x104,
        (
            "#1200686V#0303F#11PUh, you sure 'bout that, bud?\x02\x03",
            "#1200687V#0301FIsn't it that blind girl, Shizuku?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200688V#0011F#5POh, you're right.\x02\x03",
            "#1200689V#0006FShizuku's statement will be the key\x01",
            "key to cracking this case wide open.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3335")

    label("loc_3335")


    ChrTalk(
        0x103,
        "#1200692V#0205F#6PShizuku's statement...\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(40, 120, -1, -1)
    SetChrName("Shizuku's Statement")

    AnonymousTalk(
        0xFF,
        (
            "#1200693V\x07\x0C",
            "Well, I was starting to get a little\x01",
            "anxious, so I opened the window\x01",
            "and listened very carefully...\x02\x03",
            "#1200694VI didn't hear any more screams, but I did\x01",
            "hear something that almost reminded\x01",
            "me of someone breathing...\x02\x03",
            "#1200695VAfter hearing that for a few minutes,\x01",
            "I suddenly heard what sounded like\x01",
            "something jumping...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    SetMessageWindowPos(190, 140, -1, -1)
    SetChrName("Shizuku's Statement")

    AnonymousTalk(
        0xFF,
        (
            "#1200696V\x07\x0C",
            "B-But there's more, I think...\x02\x03",
            "#1200697VUm, there was something else I heard\x01",
            "on top of what I already told you...\x02\x03",
            "#1200698VFor some reason, I feel like I heard\x01",
            "a faint whistling sound coming from\x01",
            "outside the hospital.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis023.itp")

    ChrTalk(
        0x102,
        (
            "#1200699V\x07\x00",
            "#0105F#12PHold on... Was that whistling\x01",
            "how they controlled the wolves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200700V#0001F#5PYeah, I think it's likely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200701V#0203F#6PWolves are quite similar to dogs.\x01",
            "Their ears can pick up frequencies\x01",
            "that the average human ear cannot.\x02\x03",
            "#1200702V#0201FSpecial whistles have been made\x01",
            "to exploit that for a while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200703V#0304F#11POur perps are usin' a dog whistle, eh?\x02\x03",
            "#1200704V#0300FIf you train 'em well enough, you can get\x01",
            "war hounds to do damn near anything.\x02\x03",
            "#1200705V#0306FWell, it's not like armies use 'em. It's mainly\x01",
            "just jaegers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200706V#0005F#5PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200707V#0108F#12PInteresting. I think I'm starting to see\x01",
            "the dots connect.\x02\x03",
            "#1200708V#0101FIf this was their method, they'd need a\x01",
            "way to transport the wolves around.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#1200709V#0105F#12PWait, did they...?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 3)), scpexpr(EXPR_END)), "loc_42E9")
    OP_2C(0x3F, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x40, 0x1, 0xB)

    ChrTalk(
        0x101,
        (
            "#1200710V#0004F#5PI think you're on the right track, Elie.\x02\x03",
            "#1200711V#0000FAnd I also know a way to confirm\x01",
            "my line of reasoning.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1200712V#0000F#5PTio, can I still contact people on my Enigma\x01",
            "from all the way out here?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    Sleep(200)

    ChrTalk(
        0x103,
        (
            "#1200713V#0205F#6PYes. You should be able to make calls as\x01",
            "long as you are in Crossbell State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200714V#0305F#11POooh, we givin' someone a ring?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1200715V#0000F#5PYeah. The St. Ursula reception desk.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x10)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 101060, 2000, -560, 180)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x103, 0x2)
    SetChrSubChip(0x104, 0x1)
    Sleep(1000)
    OP_68(102370, 4500, 1380, 0)
    OP_68(102370, 3300, 1380, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x102,
        (
            "#1200716V#0101F#5PYes. That's right...\x02\x03",
            "#1200717V#0105F...!\x02\x03",
            "#1200718V#0103FIs that so? Thank you very much\x01",
            "for your cooperation.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x2)
    ClearChrFlags(0x102, 0x10)
    Sound(807, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#1200719V#0001F#5PHow'd it go?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#1200720V#0106F#11PIt was exactly as you thought.\x02\x03",
            "#1200721V#0101FThe night the wolves appeared on the roof,\x01",
            "there was a Revache & Co. van parked in\x01",
            "the St. Ursula parking lot.\x02\x03",
            "#1200722VThey apparently tried to force them to buy\x01",
            "some expensive medical equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200723V#0306F#5PUncanny timing.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#1200724V#0301F#11PBut wait a sec, Lloyd... How the hell\x01",
            "did you guess that they'd have a van\x01",
            "in the parking lot?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x0)
    Sleep(200)

    ChrTalk(
        0x103,
        (
            "#1200725V#0205F#6PHow do we know they did not drive there\x01",
            "late into the night to order the attack?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200726V#0003F#5PThey couldn't have. If they did, Shizuku's\x01",
            "sharp ears would have heard the van.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#1200727V#0000FAt first, I thought that the wolves probably\x01",
            "came from the nearby bushes, but\x01",
            "something about that doesn't add up.\x02\x03",
            "#1200728VThere wasn't a single trace of paw prints\x01",
            "on the wooden boxes facing that side.\x02\x03",
            "#1200729V#0003FThere were, however, visible signs of\x01",
            "scratches on the handrails facing the\x01",
            "parking lot.\x02\x03",
            "#1200730V#0001FThe chance that the parking lot was their\x01",
            "entry route seems pretty high, doesn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#1200731V#0106FI think I understand...\x02\x03",
            "#1200732V#0101FDue to the roof being so high up, I never\x01",
            "considered that possibility...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x104,
        (
            "#1200733V#0300FBut if they used the top of the van as a boost,\x01",
            "they could've easily made it up there, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#1200734V#0206FIt seems they were quite thorough with their\x01",
        "plans.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 102500, 2200, -300, 0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Jump("loc_43A2")

    label("loc_42E9")

    OP_29(0x40, 0x1, 0xC)

    ChrTalk(
        0x101,
        (
            "#1200735V#0003F#5PThat's right. We even saw that black\x01",
            "van earlier...\x02\x03",
            "#1200736V#0001FIt may lack decisive evidence, but it's still\x01",
            "the best explanation we've got right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43A2")

    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x102)

    ChrTalk(
        0x103,
        "#1200737V#0203F#6PIn the end, everything was connected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200738V#0108F#12PTheir motive must have been to monopolize\x01",
            "the septium industry, right?\x02\x03",
            "#1200739V#0101FNo... Maybe that was just a bonus?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200740V#0006F#5PThat's what I'm thinking.\x02\x03",
            "#1200741V#0008FRevache is going all out in their efforts to\x01",
            "overwhelm and conquer their rival group,\x01",
            "Heiyue.\x02\x03",
            "#1200742V#0001FAnd if they wanted to use those wolves\x01",
            "in their fight against them, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200743V#0303F#11PThey'd have to test whether or not they\x01",
            "can control the beasts.\x02\x03",
            "#1200744V'Cause they'd be useless if they couldn't\x01",
            "follow any of their orders.\x02\x03",
            "#1200745V#0301FThat's the truth behind all of these\x01",
            "different attacks, ain't it?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200746V#0003F#5PYeah, I have no doubt.\x02\x03",
            "#1200747V#0001FTo start off, the mafia visited the village\x01",
            "right after the CGF withdrew. Isn't that\x01",
            "too strange to be a coincidence?\x02\x03",
            "#1200748VThat order came from the CGF commander,\x01",
            "and he's said to have ties to a diet member.\x02\x03",
            "#1200749VDon't you think they probably collaborated\x01",
            "on this entire thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200750V#0106F#12PYes, that very well could be.\x02\x03",
            "#1200751V#0108FI knew there was corruption in the diet,\x01",
            "but to think they'd actually go this far...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)

    ChrTalk(
        0x102,
        "#1200752V#0101F#12PDo you think...they plan on going further?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200753V#0006F#5PConsidering they've already conducted combat\x01",
            "tests, you'd think it'd be enough.\x02\x03",
            "#1200754VHowever, the CGF withdrawing before Revache\x01",
            "visited today would imply the opposite: that they're\x01",
            "still planning something.\x02\x03",
            "#1200755V#0001FThat doesn't sit well with me. Their actions this\x01",
            "time around seem unnecessarily ambitious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200756V#0201F#6PA monopoly on the septium industry...\x02\x03",
            "#1200757VIf they really wanted that, they would\x01",
            "have to act one last time, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200758V#0301F#11PJudgin' by past encounters with Revache,\x01",
            "I'd say you're spot on there, Tio Tot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200759V#0101F#12PWhen do you think this supposed\x01",
            "attack will occur?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200760V#0003F#5PHmm, let's see...\x02\x03",
            "#1200761V#0008FWe know that Mayor Bickson is probably\x01",
            "going to contact the Bracer Guild tomorrow.\x02\x03",
            "#1200762V#0001FIf they really plan on following through on\x01",
            "their threat, tonight is their only option.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x102)

    ChrTalk(
        0x104,
        "#1200763V#0300F#11PWell, doesn't leave us much choice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200764V#0201F#6PWe are going to ambush the wolves and arrest\x01",
            "the Revache members behind this, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200765V#0103F#12PWe must. There's no overlooking\x01",
            "something this big.\x02\x03",
            "#1200766V#0101FShould we contact the CGF for support?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200767V#0006F#5PNo. If the CGF takes part in this, I bet\x01",
            "the mafia will get to go home scot-free,\x01",
            "given their ties to that diet member.\x02\x03",
            "#1200768V#0001FWe have to do this alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200769V#0103F#12PUnderstood.\x02\x03",
            "#1200770V#0101FIf they appear, it will most likely\x01",
            "be in the middle of the night, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200771V#0203F#6PAll the other incidents have occurred late into\x01",
            "the night, so that would be a safe assumption.\x02\x03",
            "#1200772V#0200FWe still have some time left before dark.\x01",
            "Should we go over our strategy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200773V#0000F#5PWell, if we're running short on supplies,\x01",
            "we should take care of that first.\x02\x03",
            "#1200774VOnce we're done preparing, let's wait here\x01",
            "on standby until midnight.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(32800, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(500)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you are ready to wait for midnight,\x01",
            "inspect the table.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
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
    SetChrPos(0x0, 101300, 2000, 3700, 180)
    OP_66(0x1, 0x1)
    SetScenarioFlags(0x65, 5)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayBGM("ed7513", 0)
    EventEnd(0x5)
    Return()

    # Function_13_1511 end

    SaveToFile()

Try(main)
