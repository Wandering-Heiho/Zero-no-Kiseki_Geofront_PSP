from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t113b.bin",                # FileName
        "t113b",                    # MapName
        "t113b",                    # Location
        0x0049,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 73, 0, 4, 0, 5],
    )

    BuildStringList((
        "t113b",                  # 0
        "Wazy",                   # 1
        "James",                  # 2
        "Evelyn",                 # 3
        "Nikita",                 # 4
        "Pamela",                 # 5
        "Butler Femto",           # 6
        "Butler Christoph",       # 7
        "Judy",                   # 8
    ))

    AddCharChip((
        "apl/ch50353.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch33300.itc",                   # 02
        "chr/ch26800.itc",                   # 03
        "chr/ch25600.itc",                   # 04
        "chr/ch25900.itc",                   # 05
        "chr/ch25700.itc",                   # 06
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

    DeclNpc(-150,    100,     -1149,   180,  469,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(5349,    0,       -3500,   315,  385,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4000,    0,       -2150,   135,  385,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4500,    0,       -3500,   180,  385,  0x0, 0,   3,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(5599,    0,       -12590,  0,    257,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3859,    0,       -13729,  0,    257,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-3150,   0,       3569,    90,   385,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-2099,   0,       3569,    270,  385,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)

    ScpFunction((
        "Function_0_22C",          # 00, 0
        "Function_1_2E4",          # 01, 1
        "Function_2_395",          # 02, 2
        "Function_3_3C0",          # 03, 3
        "Function_4_41A",          # 04, 4
        "Function_5_533",          # 05, 5
        "Function_6_53D",          # 06, 6
        "Function_7_899",          # 07, 7
        "Function_8_939",          # 08, 8
        "Function_9_9AC",          # 09, 9
        "Function_10_B36",         # 0A, 10
        "Function_11_E81",         # 0B, 11
        "Function_12_10B2",        # 0C, 12
        "Function_13_1106",        # 0D, 13
        "Function_14_116B",        # 0E, 14
        "Function_15_1ED0",        # 0F, 15
    ))


    def Function_0_22C(): pass

    label("Function_0_22C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_26C"),
        (1, "loc_278"),
        (2, "loc_284"),
        (3, "loc_290"),
        (4, "loc_29C"),
        (5, "loc_2A8"),
        (6, "loc_2B4"),
        (SWITCH_DEFAULT, "loc_2C0"),
    )


    label("loc_26C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_278")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_284")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_290")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_29C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2E3")

    Return()

    # Function_0_22C end

    def Function_1_2E4(): pass

    label("Function_1_2E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_394")
    OP_95(0xFE, 3320, 0, -13010, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, 3320, 0, -6980, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 3320, 0, -9020, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 3320, 0, -16960, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    Jump("Function_1_2E4")

    label("loc_394")

    Return()

    # Function_1_2E4 end

    def Function_2_395(): pass

    label("Function_2_395")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BF")
    OP_94(0xFE, 0x79E, 0xFFFFFB1E, 0x19E6, 0xFFFFFD8A, 0x3E8)
    Sleep(300)
    Jump("Function_2_395")

    label("loc_3BF")

    Return()

    # Function_2_395 end

    def Function_3_3C0(): pass

    label("Function_3_3C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_419")
    OP_95(0xFE, -5090, 0, -19580, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -5090, 0, -1190, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    Jump("Function_3_3C0")

    label("loc_419")

    Return()

    # Function_3_3C0 end

    def Function_4_41A(): pass

    label("Function_4_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_46A")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 4670, 0, -1000, 0)
    BeginChrThread(0xC, 0, 0, 2)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -5090, 0, -1190, 180)
    BeginChrThread(0xD, 0, 0, 3)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_521")

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4B0")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3020, 0, -13010, 360)
    BeginChrThread(0xC, 0, 0, 1)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -5090, 0, -1190, 180)
    BeginChrThread(0xD, 0, 0, 3)
    Jump("loc_521")

    label("loc_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_4F0")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3020, 0, -13010, 360)
    BeginChrThread(0xC, 0, 0, 1)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1660, 0, 4960, 180)
    Jump("loc_521")

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_521")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_521")
    ClearChrFlags(0xB, 0x80)

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_532")
    Event(0, 14)

    label("loc_532")

    Return()

    # Function_4_41A end

    def Function_5_533(): pass

    label("Function_5_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_53C")

    label("loc_53C")

    Return()

    # Function_5_533 end

    def Function_6_53D(): pass

    label("Function_6_53D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D1")
    Jump("loc_61B")

    label("loc_5D1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61B")

    label("loc_5F1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_611")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61B")

    label("loc_611")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80F")

    ChrTalk(
        0x8,
        (
            "#5702FWell, I'll meet up with you two later.\x02\x03",
            "#5709FThis little fuss might drag on for\x01",
            "a while, so I've decided to try to\x01",
            "defuse the whole thing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_73F")

    ChrTalk(
        0x102,
        (
            "#5306FYou act as if you had nothing to do\x01",
            "with starting the entire mess...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E8")

    label("loc_73F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_77E")

    ChrTalk(
        0x103,
        "#5411FIs this mess not yours to begin with?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E8")

    label("loc_77E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_7E8")

    ChrTalk(
        0x104,
        (
            "#5602FYou're one to talk. Or did you\x01",
            "forget straight up askin' that\x01",
            "lady to sleep with you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E8")


    ChrTalk(
        0x101,
        "#5106FGood luck, I guess.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_891")

    label("loc_80F")


    ChrTalk(
        0x8,
        (
            "#5702FI'll catch up with you two later.\x02\x03",
            "After our distraught couple settles their\x01",
            "affairs, I'll head towards the main hall.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_891")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_53D end

    def Function_7_899(): pass

    label("Function_7_899")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AE")
    Call(0, 9)
    Jump("loc_935")

    label("loc_8AE")

    TurnDirection(0x9, 0xA, 0)

    ChrTalk(
        0x9,
        (
            "I'll apologize however many times\x01",
            "it takes, Evelyn!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please, let's figure this out! I hate\x01",
            "seeing you upset like this!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_935")

    TalkEnd(0xFE)
    Return()

    # Function_7_899 end

    def Function_8_939(): pass

    label("Function_8_939")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94E")
    Call(0, 9)
    Jump("loc_9A8")

    label("loc_94E")

    TurnDirection(0xA, 0x9, 0)

    ChrTalk(
        0xA,
        (
            "I don't care anymore! If this is the way\x01",
            "things are, I'd rather go with Wazy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A8")

    TalkEnd(0xFE)
    Return()

    # Function_8_939 end

    def Function_9_9AC(): pass

    label("Function_9_9AC")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)

    ChrTalk(
        0x9,
        (
            "Evelyn, please wait! This is all my fault,\x01",
            "every bit of it! Please, just please don't\x01",
            "leave me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Nikita... Sh-She tempted me into\x01",
            "taking her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "How can you stand there and lie right\x01",
            "to my face! Have you no shame?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't take this anymore! You better\x01",
            "believe your mother will hear about\x01",
            "this, James!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "N-No, please! Anything but that!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_9_9AC end

    def Function_10_B36(): pass

    label("Function_10_B36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_C57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C16")

    ChrTalk(
        0xFE,
        "Sir, who is that child...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        "#5810FI'm KeA! Nice to meet'cha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Um, to you as well... (Did we have a girl\x01",
            "this young listed among the guests?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FSorry, we're in a hurry!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C52")

    label("loc_C16")


    ChrTalk(
        0xFE,
        (
            "(Was there a girl that young listed\x01",
            "among the guests?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C52")

    Jump("loc_E7D")

    label("loc_C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_C85")

    ChrTalk(
        0xFE,
        "It's super busy tonight...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E7D")

    label("loc_C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_DCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D49")

    ChrTalk(
        0xFE,
        (
            "Phew, thank goodness that couple\x01",
            "finally stopped arguing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were THIS close to drawing blood,\x01",
            "and I have no idea what I would've done\x01",
            "if it came to that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_DC6")

    label("loc_D49")


    ChrTalk(
        0xFE,
        (
            "With that done, now I can start cleaning\x01",
            "this area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm a little pressed for time, so I've\x01",
            "no time to dilly-dally.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC6")

    Jump("loc_E7D")

    label("loc_DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_E7D")

    ChrTalk(
        0xFE,
        (
            "Their argument is making me nervous,\x01",
            "and I never clean well when I'm nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I doubt I'll be able to mediate this fight,\x01",
            "considering this tense atmosphere...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E7D")

    TalkEnd(0xFE)
    Return()

    # Function_10_B36 end

    def Function_11_E81(): pass

    label("Function_11_E81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_F22")

    ChrTalk(
        0xFE,
        (
            "Someone from Revache & Co. ran in\x01",
            "here and told us not to leave under any\x01",
            "circumstances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why in the world were they in\x01",
            "such a rush?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AE")

    label("loc_F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_FAA")

    ChrTalk(
        0xFE,
        (
            "I have to finish preparations for the\x01",
            "afterparty before the auction ends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, this room won't clean itself...\x02",
    )

    CloseMessageWindow()
    Jump("loc_10AE")

    label("loc_FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_104D")

    ChrTalk(
        0xFE,
        (
            "This here is the banquet hall, where\x01",
            "VIPs are normally hosted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is not planned on being used today,\x01",
            "so please refrain from staying here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AE")

    label("loc_104D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_10AE")

    ChrTalk(
        0xFE,
        (
            "I suppose I have no choice but to\x01",
            "give up on cleaning until this storm\x01",
            "blows over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AE")

    TalkEnd(0xFE)
    Return()

    # Function_11_E81 end

    def Function_12_10B2(): pass

    label("Function_12_10B2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Is something the matter? We would\x01",
            "be happy to assist in any way we can.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_10B2 end

    def Function_13_1106(): pass

    label("Function_13_1106")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This place has gotten quite lively\x01",
            "the past few minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what caused that.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1106 end

    def Function_14_116B(): pass

    label("Function_14_116B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrSubChip(0x8, 0x1)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, -150, 100, -1150, 180)
    SetChrPos(0xA, 3750, 0, -3000, 90)
    SetChrPos(0x9, 5150, 0, -3600, 270)
    SetChrPos(0xB, 5150, 0, -2400, 270)
    SetChrPos(0x101, -600, 0, 4900, 180)
    SetChrPos(0xEF, 600, 0, 4900, 180)
    OP_68(0, 1200, 6000, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x9,
        "Man's Voice",
        "#3500973VI-It's just a great, big misunderstanding, okay?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Man's Voice",
        "#3500974VShe's just a coworker...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Woman's Voice",
        "#3500975VYou can't fool me!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Woman's Voice",
        (
            "#3500976VThis whole thing was suspicious from the\x01",
            "start, and to think that you actually came\x01",
            "here with another woman...!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2850, 1200, -2450, 3500)
    OP_6F(0x1)
    Sleep(300)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-550, 1200, -1000, 4000)
    SetChrSubChip(0x8, 0x0)

    def lambda_13B6():
        OP_95(0xFE, -1700, 0, -1250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13B6)
    Sleep(150)
    SetChrSubChip(0x8, 0x2)
    Sleep(350)

    def lambda_13DA():
        OP_95(0xFE, -1600, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_13DA)
    WaitChrThread(0x101, 1)

    def lambda_13F8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13F8)
    WaitChrThread(0xEF, 1)

    def lambda_1409():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1409)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#3500977V#5702F#11PHey. I see you were able to sneak\x01",
            "inside with relative ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500978V#5104F#6PAll thanks to you.\x02\x03",
            "#3500979V#5101FWhat's going on here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500980V#5704F#11POh, nothing more than your\x01",
            "run-of-the-mill argument.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(4450, 1200, -3000, 2000)
    SetChrSubChip(0x8, 0x0)
    Sleep(150)
    SetChrSubChip(0x8, 0x1)
    OP_6F(0x1)

    ChrTalk(
        0x9,
        (
            "#3500981V#11PY-You're one to talk! After all,\x01",
            "you brought this weirdo along\x01",
            "as your guest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3500982V#11PN-No, don't tell me...you have THAT\x01",
            "kind of relationship with him?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3500983V#5PThis man soothed my troubled heart\x01",
            "in my time of need, I'll have you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3500984V#5PAfter coming to Crossbell, a strange place\x01",
            "I've never been to in my life, Wazy came to\x01",
            "my rescue when I was lost and confused...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3500985V#5PHe even went as far as escorting me\x01",
            "to the Schwarze Auction...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3500986V#5POur relationship is nothing like this\x01",
            "suspicious...whatever it is between you\x01",
            "and that woman!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3500987V#11PUgh...\x02",
    )

    CloseMessageWindow()
    OP_68(1600, 1200, -2500, 1200)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#3500988V#5709F#6PHaha. I'd be more than happy to make\x01",
            "this something more, Evelyn.\x02\x03",
            "#3500989V#5702FI have a proposition...\x02\x03",
            "#3500990VHow about you ditch your heartless\x01",
            "husband and make love to me?\x02\x03",
            "#3500991V#5704FI can't deny that feisty, cute ladies like\x01",
            "yourself have a certain charm to them.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x10E, 0x1F4)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xA,
        "#3500992V#11PW-Wazy! I could never...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(1000)
    OP_98(0x9, 0xFFFFFD12, 0x0, 0x0, 0x7D0, 0x0)

    ChrTalk(
        0x9,
        "#3500993V#11PYOUUUU!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3500994V#11PHow about you go try to pull your moves\x01",
            "on someone else's wife, pal?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x9, 500)

    ChrTalk(
        0xB,
        (
            "#3500995V#5PYeah, I think I've had enough. I'm going\x01",
            "to have to cut this thing short.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3500996V#5PJames. If you want to have an affair,\x01",
            "try to handle it with a bit more tact\x01",
            "next time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1AA2():

        label("loc_1AA2")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_1AA2")

    QueueWorkItem2(0x9, 1, lambda_1AA2)

    def lambda_1AB4():

        label("loc_1AB4")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_1AB4")

    QueueWorkItem2(0xA, 1, lambda_1AB4)
    OP_93(0xB, 0x13B, 0x1F4)

    ChrTalk(
        0xB,
        (
            "#3500997V#2P*sigh* Now I've got to find some\x01",
            "other sucker to leech off of...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(950, 1200, -1850, 3000)
    BeginChrThread(0xB, 3, 0, 15)
    Sleep(500)

    ChrTalk(
        0x9,
        "#3500998V#11PN-Nikita, wait!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    OP_6F(0x1)
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0x9, 500)

    ChrTalk(
        0xA,
        (
            "#3500999V#5PS-So I was right! Her being a coworker\x01",
            "was a lie, after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#3501000V#5PI'm fed up with your crap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3501001V#5PIf this is how things are, I'd rather\x01",
            "go live with my parents again!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)

    ChrTalk(
        0x9,
        "#3501002V#11PEvelyn, hold on!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1D18")

    ChrTalk(
        0x102,
        (
            "#3501003V#5306F#6PI don't think interrupting them\x01",
            "would be very wise...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC4")

    label("loc_1D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1D75")

    ChrTalk(
        0x103,
        (
            "#3501004V#5400F#6PI see... This must be what they call\x01",
            "a lovers' quarrel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC4")

    label("loc_1D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1DC4")

    ChrTalk(
        0x104,
        (
            "#3501005V#5609F#6PHey, who said marriage was\x01",
            "a walk in the park?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC4")


    ChrTalk(
        0x101,
        (
            "#3501006V#5112F#6PI think we're going to head\x01",
            "out now, Wazy.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#3501007V#5704F#11PHaha, I can't say I blame you.\x02\x03",
            "#3501008V#5702FEnjoy the party, you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -2009, 0, -1560, 270)
    SetChrPos(0x9, 5350, 0, -3500, 315)
    SetChrPos(0xA, 4000, 0, -2150, 135)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetChrSubChip(0x8, 0x0)
    OP_49()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0xA5, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_116B end

    def Function_15_1ED0(): pass

    label("Function_15_1ED0")


    def lambda_1ED5():
        OP_95(0xFE, 0, 0, 4600, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1ED5)
    WaitChrThread(0xB, 1)

    def lambda_1EF3():
        OP_95(0xFE, 0, 0, 6750, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1EF3)
    Sleep(250)

    def lambda_1F10():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1F10)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    Return()

    # Function_15_1ED0 end

    SaveToFile()

Try(main)
