from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2100.bin",                # FileName
        "t2100",                    # MapName
        "t2100",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 2, 0, 3],
    )

    BuildStringList((
        "t2100",                  # 0
        "Guardsman Brood",        # 1
        "Guardsman Dalia",        # 2
        "Estelle",                # 3
        "Joshua",                 # 4
        "Tourist Dean",           # 5
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch34100.itc",                   # 01
        "chr/ch00600.itc",                   # 02
        "chr/ch00700.itc",                   # 03
        "chr/ch26700.itc",                   # 04
    ))

    DeclNpc(-13829,  10000,   -2960,   270,  389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-14060,  10000,   2900,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-15819,  5000,    -16600,  265,  405,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-16780,  5000,    -17700,  315,  405,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-17709,  5000,    -18780,  220,  385,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(-100,    10000,   -260,    1000,    -100,    10000,   -260,    0x007C, 0,  11, 0x0000)
    DeclActor(-1690,   10000,   -9200,   1000,    -1690,   10000,   -9200,   0x007C, 0,  12, 0x0000)
    DeclActor(8710,    10000,   -11130,  1000,    8710,    10000,   -11130,  0x007C, 0,  13, 0x0000)
    DeclActor(-16000,  10000,   0,       2000,    -16000,  10000,   0,       0x007C, 0,  14, 0x0000)
    DeclActor(15480,   10000,   4880,    1000,    19930,   7500,    5800,    0x007C, 0,  16, 0x0000)
    DeclActor(1500,    5050,    -20000,  1200,    1500,    6050,    -20000,  0x007C, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_250",          # 00, 0
        "Function_1_308",          # 01, 1
        "Function_2_369",          # 02, 2
        "Function_3_40D",          # 03, 3
        "Function_4_4D2",          # 04, 4
        "Function_5_63E",          # 05, 5
        "Function_6_D14",          # 06, 6
        "Function_7_1EB6",         # 07, 7
        "Function_8_2201",         # 08, 8
        "Function_9_22F7",         # 09, 9
        "Function_10_23ED",        # 0A, 10
        "Function_11_2684",        # 0B, 11
        "Function_12_28FD",        # 0C, 12
        "Function_13_2B42",        # 0D, 13
        "Function_14_2D5A",        # 0E, 14
        "Function_15_38E0",        # 0F, 15
        "Function_16_3B43",        # 10, 16
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

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_368")
    OP_95(0xFE, -13830, 10000, -2960, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -14060, 10000, 2900, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    Jump("Function_1_308")

    label("loc_368")

    Return()

    # Function_1_308 end

    def Function_2_369(): pass

    label("Function_2_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_381")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_399")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_39F")

    label("loc_399")

    BeginChrThread(0x9, 0, 0, 1)

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C9")
    SetChrPos(0x8, -8560, 5000, -19100, 175)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_3F9")

    label("loc_3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F9")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F9")
    Event(0, 10)

    label("loc_3F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40C")
    ClearChrFlags(0xC, 0x80)

    label("loc_40C")

    Return()

    # Function_2_369 end

    def Function_3_40D(): pass

    label("Function_3_40D")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_465")
    OP_66(0x4, 0x1)
    Jump("loc_4BA")

    label("loc_465")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_4BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_484")
    OP_66(0x0, 0x1)

    label("loc_484")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_496")
    OP_66(0x1, 0x1)

    label("loc_496")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A8")
    OP_66(0x2, 0x1)

    label("loc_4A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA")
    OP_66(0x3, 0x1)

    label("loc_4BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD")
    OP_70(0x2, 0x0)
    Jump("loc_4D1")

    label("loc_4CD")

    OP_70(0x2, 0x1E)

    label("loc_4D1")

    Return()

    # Function_3_40D end

    def Function_4_4D2(): pass

    label("Function_4_4D2")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BC")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x646, 1)"), scpexpr(EXPR_END)), "loc_552")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x113, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_5B7")

    label("loc_552")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_5B7")

    Jump("loc_632")

    label("loc_5BC")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Am I the only who thinks the name 'Bellguard'\x01",
            "is just a little on the nose?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_632")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4D2 end

    def Function_5_63E(): pass

    label("Function_5_63E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_733")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EC")

    ChrTalk(
        0xFE,
        (
            "Strangely enough, Dalia actually\x01",
            "spoke to me today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But she only talked about some really\x01",
            "confusing stuff, and I was completely lost.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_72E")

    label("loc_6EC")


    ChrTalk(
        0xFE,
        (
            "That was my chance to break the ice,\x01",
            "but I went and blew it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72E")

    Jump("loc_D10")

    label("loc_733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_849")

    ChrTalk(
        0xFE,
        (
            "It's so awkward, just the two of us\x01",
            "standing guard up here together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dalia's definitely a lot more polite than\x01",
            "others, so gossip isn't really an option...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I'd much rather do this alone...\x01",
            "I think I'm going to take another break.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8EB")

    label("loc_849")


    ChrTalk(
        0xFE,
        (
            "If I was stationed with someone\x01",
            "like Burrell over at Tangram Gate,\x01",
            "everything would be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've never been good when it\x01",
            "comes to speaking with women.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EB")

    Jump("loc_D10")

    label("loc_8F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AC")

    ChrTalk(
        0xFE,
        (
            "Phew, good thing this place is\x01",
            "finally starting to settle down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just a little while longer and all we'll have\x01",
            "to worry about is guarding the border...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9FA")

    label("loc_9AC")


    ChrTalk(
        0xFE,
        "Luckily, Dalia said she'd cover for me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm not slacking off, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_9FA")

    Jump("loc_D10")

    label("loc_9FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D10")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B06")

    ChrTalk(
        0xFE,
        "You sure the key is up here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dalia and I searched the entire roof\x01",
            "head-to-toe, but came up with zilch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, hey, we might have overlooked\x01",
            "something. I hope you have better luck\x01",
            "searching than we did.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BAB")

    label("loc_B06")


    ChrTalk(
        0xFE,
        (
            "We looked everywhere for the key, but it\x01",
            "was no good. It's possible that we may\x01",
            "have overlooked something, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sorry, but do you mind giving it a try?\x02",
    )

    CloseMessageWindow()

    label("loc_BAB")

    Jump("loc_D10")

    label("loc_BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C87")

    ChrTalk(
        0xFE,
        (
            "One of my friends, Burrell, is stationed\x01",
            "over at Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wish I was there, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm always nervous that our commander\x01",
            "isn't going to be here for when worst\x01",
            "comes to worst.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D10")

    label("loc_C87")


    ChrTalk(
        0xFE,
        (
            "I wish I was stationed over at Tangram\x01",
            "Gate, like my buddy, Burrell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Getting assigned to this place was just\x01",
            "my rotten luck...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D10")

    TalkEnd(0xFE)
    Return()

    # Function_5_63E end

    def Function_6_D14(): pass

    label("Function_6_D14")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_F24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA1")

    ChrTalk(
        0xFE,
        (
            "A couple years back, there was a massive\x01",
            "scandal where Erebonian branches of the\x01",
            "Bracer Guild were raided by jaegers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite the whole thing being fixed by\x01",
            "a famous bracer, a lot of factors about\x01",
            "the incident are still a mystery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In actuality, the raids themselves were\x01",
            "said to be a large-scale diversion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think there's more to them, though.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F1F")

    label("loc_EA1")


    ChrTalk(
        0xFE,
        (
            "About the raids on the Erebonian\x01",
            "guild branches a few years ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think there's more to them than\x01",
            "meets the eye.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1F")

    Jump("loc_1EB2")

    label("loc_F24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_FE8")

    ChrTalk(
        0xFE,
        (
            "I think I realize how defenseless this gate\x01",
            "really is, when stuck here against the\x01",
            "Empire's overwhelming might.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they were serious, I doubt this\x01",
            "place would last long...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB2")

    label("loc_FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_111B")

    ChrTalk(
        0xFE,
        (
            "You know about the Orbal Shutdown\x01",
            "Phenomenon that happened all over\x01",
            "Liberl, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When that happened, Chancellor Osborne\x01",
            "quickly dispatched new Imperial steam-engine\x01",
            "tanks to the border.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's as if he knew what was going to happen\x01",
            "and how to respond... What a frightening man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB2")

    label("loc_111B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_12EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_122B")

    ChrTalk(
        0xFE,
        (
            "Since we're stationed together, I've been\x01",
            "making effort to connect with Brood more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I tried asking him his thoughts on the\x01",
            "Liberl incident from last year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Geez, I probably shouldn't have asked\x01",
            "something like that out of the blue.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12E7")

    label("loc_122B")


    ChrTalk(
        0xFE,
        (
            "*sigh* I hate how shy I am sometimes.\x01",
            "I've never been very good at making\x01",
            "conversation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no hope for me. I think\x01",
            "it'd be best to stay quiet and\x01",
            "focus on my job for today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E7")

    Jump("loc_1EB2")

    label("loc_12EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_14EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141D")

    ChrTalk(
        0xFE,
        (
            "Any time I work up the nerve to\x01",
            "strike a conversation with Brood,\x01",
            "it doesn't last for very long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's easier to be more outgoing\x01",
            "around other female guardsmen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Truth is, I just want us to be able to talk\x01",
            "to each other normally since we're both\x01",
            "stationed up here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_14E9")

    label("loc_141D")


    ChrTalk(
        0xFE,
        (
            "Warrant Officer Mireille and I get along\x01",
            "great and talk to each other all the time,\x01",
            "but that's because she's a girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how hard I try, I can't get\x01",
            "comfortable when I'm alone with a man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E9")

    Jump("loc_1EB2")

    label("loc_14EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_169D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1611")

    ChrTalk(
        0xFE,
        (
            "Brood said he needed a smoke, so I\x01",
            "volunteered to watch the border alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Normally that's not allowed, but the\x01",
            "commander isn't here. It'll just be\x01",
            "our little secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know it's my job, but watching the same\x01",
            "scenery every single day can get boring.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1698")

    label("loc_1611")


    ChrTalk(
        0xFE,
        (
            "I think I'm going to have to take a short\x01",
            "break later, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who knows? Maybe the thrill of playing\x01",
            "hooky could be kinda fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1698")

    Jump("loc_1EB2")

    label("loc_169D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_19EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1779")

    ChrTalk(
        0xFE,
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Last night, the commander came up here and\x01",
            "couldn't stop singing. Loudly, I might add...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was hoping to get some rest from our\x01",
            "labors, but that didn't happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E9")

    label("loc_1779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18DD")

    ChrTalk(
        0xFE,
        (
            "Since there aren't many women in\x01",
            "the CGF, the few among us tend to\x01",
            "draw a lot of attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Deputy Commander Baelz and Sergeant Major\x01",
            "Seeker are both extremely beautiful,\x01",
            "so it's even more problematic for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someday, there's going to be a headline\x01",
            "that reads, 'Interview with the Beautiful\x01",
            "Guardsmen of the CGF!' *sigh*\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19E9")

    label("loc_18DD")


    ChrTalk(
        0xFE,
        (
            "On a similar note, after those strange\x01",
            "series of events in Liberl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Captain Schwarz of their Royal Guard has\x01",
            "garnered quite a lot of attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've only seen her through photographs,\x01",
            "but she looks like a distinguished woman...\x01",
            "She must have it rough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E9")

    Jump("loc_1EB2")

    label("loc_19EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1C00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4B")

    ChrTalk(
        0xFE,
        (
            "Two years ago, both of Garrelia Fortress'\x01",
            "railways guns were pointed right at us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was definitely touch and go for a while.\x01",
            "The possibility of a major conflict had us\x01",
            "on high alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to the Non-Aggression Pact, the\x01",
            "gate has been relatively peaceful...but I'll\x01",
            "never forget the fear I felt that day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BFB")

    label("loc_1B4B")


    ChrTalk(
        0xFE,
        (
            "The signing of the Non-Aggression Pact\x01",
            "two years ago finally relieved tensions\x01",
            "across Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I applaud Queen Alicia for leading the charge\x01",
            "for its establishment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BFB")

    Jump("loc_1EB2")

    label("loc_1C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1EB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DEF")

    ChrTalk(
        0xFE,
        (
            "Over on that mountainside is the pride of\x01",
            "the Imperial Army, Garrelia Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Empire's military is immensely strong,\x01",
            "so we can't ever let our guard down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FDon't wanna kill yourself with all the\x01",
            "stress that comes with that, though.\x02\x03",
            "#0304FDon't get me wrong, it's A-OK to be\x01",
            "serious, but it's also important to take\x01",
            "a breather every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something tells me you put a higher priority\x01",
            "on relaxing instead of seriousness, Randy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EB2")

    label("loc_1DEF")


    ChrTalk(
        0xFE,
        (
            "But perhaps you're right. After all,\x01",
            "everything has its boiling point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll take your advice and have\x01",
            "Brood switch out with me later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306F(Serious as a heart attack, that girl.)\x02",
    )

    CloseMessageWindow()

    label("loc_1EB2")

    TalkEnd(0xFE)
    Return()

    # Function_6_D14 end

    def Function_7_1EB6(): pass

    label("Function_7_1EB6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_21FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2116")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "#0805FWow, talk about a view...\x02\x03",
            "#0801FSo this is where Crossbell and Erebonia\x01",
            "border each other, right? This is my\x01",
            "first time seeing it this close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#0901FYes. Right on the other side of the border\x01",
            "should be Garrelia Fortress.\x02\x03",
            "Supposedly, it's one of Erebonia's most\x01",
            "important military bases.\x02\x03",
            "#0903FTaking everything into account, it's likely\x01",
            "because it's the closest base to Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0806FOh, right. Erebonia and Calvard have\x01",
            "always hated each other, haven't they?\x02\x03",
            "#0808FCrossbell really has its fair share of\x01",
            "burdens, huh, Joshua?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_21FD")

    label("loc_2116")


    ChrTalk(
        0xA,
        (
            "#0805FOh, hey everyone.\x02\x03",
            "#0806FYou know, seeing a view like this helps\x01",
            "remind me of how powerful the Erebonian\x01",
            "Empire really is.\x02\x03",
            "#0802FStill, the Erebonians I've met aren't bad\x01",
            "people. Well...one of them is a little strange.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21FD")

    TalkEnd(0xFE)
    Return()

    # Function_7_1EB6 end

    def Function_8_2201(): pass

    label("Function_8_2201")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_22F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221F")
    Call(0, 7)
    Jump("loc_22F3")

    label("loc_221F")


    ChrTalk(
        0xB,
        (
            "#0904FEstelle and I came here to meet with a client, so we\x01",
            "took the opportunity to see this with our own eyes.\x02\x03",
            "#0900FIf we're to understand Crossbell, we'll have to\x01",
            "observe its circumstances for ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F3")

    TalkEnd(0xFE)
    Return()

    # Function_8_2201 end

    def Function_9_22F7(): pass

    label("Function_9_22F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2378")

    ChrTalk(
        0xFE,
        (
            "Whoa! One wrong step and I'll\x01",
            "fall to the bottom of the canyon.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0xDC, 0x1F4)

    ChrTalk(
        0xFE,
        "Ah! This is freakin' nuts!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_23E9")

    label("loc_2378")


    ChrTalk(
        0xFE,
        (
            "If I slipped, I'd be a goner. Maybe\x01",
            "I'll take one more look...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0xDC, 0x1F4)

    ChrTalk(
        0xFE,
        "Oh, sweet Aidios, this is scary!\x02",
    )

    CloseMessageWindow()

    label("loc_23E9")

    TalkEnd(0xFE)
    Return()

    # Function_9_22F7 end

    def Function_10_23ED(): pass

    label("Function_10_23ED")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6670, 11000, 3120, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18620, 0)
    SetChrPos(0x101, 7300, 10000, 2500, 180)
    SetChrPos(0x102, 6000, 10000, 2500, 180)
    SetChrPos(0x103, 7300, 10000, 3800, 180)
    SetChrPos(0x104, 6000, 10000, 3800, 180)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#0000FWell, we made it to the roof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FAccording to Warrant Officer Mireille, the CGF\x01",
            "commander 'sung his heart out' up here.\x02\x03",
            "I imagine it took a while to climb the stairs\x01",
            "while he was under the influence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0106FYes, but our biggest issue is that he\x01",
            "doesn't remember where exactly he\x01",
            "misplaced the key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0300FIf he were to lose it anywhere, this\x01",
            "would be the place.\x02\x03",
            "Let's try searchin' for a while and\x01",
            "see where that takes us.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 7300, 10000, 2500, 180)
    OP_29(0x19, 0x1, 0x5)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_23ED end

    def Function_11_2684(): pass

    label("Function_11_2684")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2712")

    ChrTalk(
        0x101,
        (
            "#0005FWhat's with that shining light...?\x02\x03",
            "#0006FOh, it was just a 10 mira coin.\x01",
            "The commander probably dropped it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C3")

    label("loc_2712")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27A5")

    ChrTalk(
        0x102,
        (
            "#0105FOh, what's that sparkle...?\x02\x03",
            "#0106FJust a 10 mira coin. Did the commander\x01",
            "accidentally drop it while he was up here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C3")

    label("loc_27A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283E")

    ChrTalk(
        0x103,
        (
            "#0205FWhat could that sparkling object be...?\x02\x03",
            "#0211FA 10 mira coin. Figures. The commander\x01",
            "might have dropped it while up here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C3")

    label("loc_283E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C3")

    ChrTalk(
        0x104,
        (
            "#0305FWhat's the deal with that shine...?\x02\x03",
            "#0306FWould ya look at that, a 10 mira coin.\x01",
            "Geez, this is impossible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28C3")

    OP_65(0x0, 0x1)
    OP_29(0x19, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28F9")
    Call(0, 15)
    OP_66(0x4, 0x1)

    label("loc_28F9")

    TalkEnd(0xFF)
    Return()

    # Function_11_2684 end

    def Function_12_28FD(): pass

    label("Function_12_28FD")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2972")

    ChrTalk(
        0x101,
        (
            "#0005FWhat's this...?\x02\x03",
            "#0006FThe lid of a juice can? Yeah,\x01",
            "we can just throw this away...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B08")

    label("loc_2972")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29F5")

    ChrTalk(
        0x102,
        (
            "#0105FI think I see something...\x02\x03",
            "#0106FIs this a lid for a juice can? We\x01",
            "should probably dispose of it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B08")

    label("loc_29F5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A82")

    ChrTalk(
        0x103,
        (
            "#0205FI believe there is something here.\x02\x03",
            "#0203FExcellent. A lid to a can of juice.\x01",
            "We should dispose of it later...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B08")

    label("loc_2A82")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B08")

    ChrTalk(
        0x104,
        (
            "#0305FOh, I think I see somethin'.\x02\x03",
            "#0306FIs this a freakin' juice lid? Man,\x01",
            "the disappointments keep pilin' up...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B08")

    OP_29(0x19, 0x1, 0x7)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B3E")
    Call(0, 15)
    OP_66(0x4, 0x1)

    label("loc_2B3E")

    TalkEnd(0xFF)
    Return()

    # Function_12_28FD end

    def Function_13_2B42(): pass

    label("Function_13_2B42")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BB0")

    ChrTalk(
        0x101,
        (
            "#0005FWait, is that it...?\x02\x03",
            "#0006FWire? Just where in the\x01",
            "world could this key be?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D20")

    label("loc_2BB0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C24")

    ChrTalk(
        0x102,
        (
            "#0105FWhat's this...?\x02\x03",
            "#0106FOh, it's just a piece of wire. Where\x01",
            "could this key have gone?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D20")

    label("loc_2C24")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CA8")

    ChrTalk(
        0x103,
        (
            "#0205FI have found something...\x02\x03",
            "#0203FFalse alarm. It was a piece of wire.\x01",
            "Now, where could the key be...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D20")

    label("loc_2CA8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D20")

    ChrTalk(
        0x104,
        (
            "#0305FDid I finally find it...?\x02\x03",
            "#0301FNope. Just some wire. Damn it,\x01",
            "where did this key run off to?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D20")

    OP_29(0x19, 0x1, 0x8)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D56")
    Call(0, 15)
    OP_66(0x4, 0x1)

    label("loc_2D56")

    TalkEnd(0xFF)
    Return()

    # Function_13_2B42 end

    def Function_14_2D5A(): pass

    label("Function_14_2D5A")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -10400, 10000, -650, 270)
    SetChrPos(0x102, -10400, 10000, 650, 270)
    SetChrPos(0x103, -9400, 10000, -1300, 270)
    SetChrPos(0x104, -9400, 10000, 1300, 270)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(-29750, 13600, 710, 0)
    MoveCamera(256, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(35900, 0)
    SetCameraDistance(45900, 5000)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#5P#0005FThat tunnel leads into Erebonia, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0103FThat's right.\x02\x03",
            "#0101FMore specifically, that tunnel and the\x01",
            "fortified mountain base up ahead both\x01",
            "comprise Garrelia Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0208FAs the Empire's easternmost stronghold,\x01",
            "it is used to keep Calvard in check.\x02\x03",
            "#0206FSeeing it this close, I cannot help but feel\x01",
            "incredibly intimidated by the Empire...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-9200, 11500, -580, 0)
    MoveCamera(294, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19210, 0)
    OP_68(-9200, 11500, -580, 0)
    MoveCamera(294, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17710, 0)
    OP_0D()

    def lambda_2FC8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2FC8)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#11P#0304FHaha, can't blame ya for feelin'\x01",
            "that way, Tio Tot.\x02\x03",
            "#0301FAfter all, that mountain's hidin' two of the\x01",
            "Empire's scariest weapons: the railway guns.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_307C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_307C)

    def lambda_3089():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3089)

    def lambda_3096():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3096)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#0005FRailway guns...? I feel like I've heard\x01",
            "of them somewhere before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0303FI'm sure you have. They're the pride and\x01",
            "joy of the Imperial Army: their ultimate\x01",
            "weapons of mass destruction.\x02\x03",
            "#0301FHeard those bad boys fire 80-rege shells.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0201FThey were invented as a strategic safety\x01",
            "measure by the Reinford Company.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_31FD():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_31FD)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#11P#0103FTwo years ago, tensions between the Empire and\x01",
            "the Republic had finally reached a breaking point...\x02\x03",
            "#0101FWhile both countries began to conduct large-scale\x01",
            "military exercises, the wall over there opened,\x01",
            "revealing their two enormous railway guns.\x02\x03",
            "#0108FWeapons which have the capacity to hit Crossbell\x01",
            "City. If Erebonia were to unleash them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006F...tragedy would be unavoidable.\x02\x03",
            "#0008F(The Crossbell Times never once mentioned\x01",
            "these while I was living in Calvard...)\x02\x03",
            "#0013F(I never knew things were that unstable\x01",
            "at the time.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0304FWell, as you can see, they've got their\x01",
            "trump card stored away right now.\x02\x03",
            "#0300FWe might owe the Liberlian queen's\x01",
            "non-aggression pact thanks for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006FDefinitely. I'd always heard that she\x01",
            "was an admirable person, but I have\x01",
            "a newfound respect for her now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#6P#0005FLooks like we got side-tracked.\x01",
            "We should continue our search\x01",
            "for the key.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x19, 0x1, 0x9)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38C3")

    ChrTalk(
        0x102,
        (
            "#11P#0105FWe've already searched every place\x01",
            "it might be up here, haven't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0306FWell, at the very least, we know for a\x01",
            "fact that the commander was up here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FActing under the assumption that he\x01",
            "dropped the key on the roof may not\x01",
            "be the correct decision.\x02\x03",
            "#0200FIf that were the case, the guardsmen\x01",
            "would have found it immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FConsidering what Mr. Crois told us\x01",
            "earlier, we might need to change our\x01",
            "perspective on this entire thing.\x02\x03",
            "#0001FIt's only a possibility...but what if the key\x01",
            "fell into a place that we can't normally\x01",
            "reach?\x02\x03",
            "Let's investigate every nook and cranny\x01",
            "of this place one more time.\x02",
        )
    )

    CloseMessageWindow()
    OP_66(0x4, 0x1)
    OP_29(0x19, 0x1, 0x1F)

    label("loc_38C3")

    OP_5A()
    SetChrPos(0x0, -10400, 10000, -650, 270)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_14_2D5A end

    def Function_15_38E0(): pass

    label("Function_15_38E0")


    ChrTalk(
        0x102,
        "#0105FFinding it is proving difficult.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FWell, at the very least, we know for a\x01",
            "fact that the commander was up here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FActing under the assumption that he\x01",
            "dropped the key on the roof may not\x01",
            "be the correct decision.\x02\x03",
            "#0200FIf that were the case, the guardsmen\x01",
            "would have found it immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FConsidering what Mr. Crois told us\x01",
            "earlier, we might need to change our\x01",
            "perspective on this entire thing.\x02\x03",
            "#0001FIt's only a possibility...but what if the key\x01",
            "fell into a place that we can't normally\x01",
            "reach?\x02\x03",
            "Let's investigate every nook and cranny\x01",
            "of this place one more time.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x19, 0x1, 0x1F)
    Return()

    # Function_15_38E0 end

    def Function_16_3B43(): pass

    label("Function_16_3B43")

    EventBegin(0x0)
    LoadEffect(0x9, "event\\eva00_00.eff")
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(15330, 11000, 4890, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 15000, 10000, 4700, 90)
    SetChrPos(0x102, 15000, 10000, 3400, 90)
    SetChrPos(0x103, 15000, 10000, 2100, 90)
    SetChrPos(0x104, 15000, 10000, 800, 90)
    SetCameraDistance(19000, 2000)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5P#0001FHuh?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x103,
        "#5P#0205FLloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0105FWhat's the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FI see it!\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(24460, 11000, 1930, 3000)
    MoveCamera(310, 33, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(15440, 3000)
    OP_6F(0x79)
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 19510, 7000, 5830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(860, 0, 100, 0)
    Sleep(3000)

    ChrTalk(
        0x104,
        (
            "#5P#0306F#NHow the hell did it end up\x01",
            "in a place like that...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#5P#0206F#NGiven its true location, I am not surprised\x01",
            "that they were unable to find the key, no\x01",
            "matter how much they scoured the gate.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5P#0000F#NFor now, let's let the warrant officer know.\x02\x03",
            "We may need to borrow a ladder or\x01",
            "something in order to grab it.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#5P#0100F#NRight. Let's go find her.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    SetScenarioFlags(0x5C, 0)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3B43 end

    SaveToFile()

Try(main)
