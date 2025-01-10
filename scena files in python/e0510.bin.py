from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0510.bin",                # FileName
        "e0510",                    # MapName
        "e0510",                    # Location
        0x00A1,                     # MapIndex
        "ed7104",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 161, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0510",                  # 0
        "Kilika",                 # 1
        "Stewardess Salsa",       # 2
        "Girl",                   # 3
        "Young Man",              # 4
        "Man",                    # 5
        "Young Man",              # 6
        "Tourist",                # 7
    ))

    AddCharChip((
        "chr/ch07302.itc",                   # 00
        "chr/ch28400.itc",                   # 01
        "chr/ch21302.itc",                   # 02
        "chr/ch21202.itc",                   # 03
        "chr/ch27702.itc",                   # 04
        "chr/ch23602.itc",                   # 05
        "chr/ch26702.itc",                   # 06
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

    DeclNpc(0,       -899,    7349,    0,    341,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(-100,    0,       -15420,  0,    257,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-3660,   150,     -8829,   180,  341,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(-2450,   150,     -8829,   180,  341,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(3049,    150,     -6349,   180,  341,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-2450,   150,     -3799,   180,  341,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(2180,    150,     -8829,   180,  341,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)

    ScpFunction((
        "Function_0_204",          # 00, 0
        "Function_1_299",          # 01, 1
        "Function_2_2BF",          # 02, 2
        "Function_3_2C6",          # 03, 3
        "Function_4_5B5",          # 04, 4
        "Function_5_739",          # 05, 5
        "Function_6_951",          # 06, 6
        "Function_7_B9F",          # 07, 7
        "Function_8_D44",          # 08, 8
        "Function_9_F7A",          # 09, 9
        "Function_10_1157",        # 0A, 10
        "Function_11_14EA",        # 0B, 11
        "Function_12_2659",        # 0C, 12
    ))


    def Function_0_204(): pass

    label("Function_0_204")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_227")
    Sleep(600)
    Jump("loc_250")

    label("loc_227")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23E")
    Sleep(400)
    Jump("loc_250")

    label("loc_23E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_250")
    Sleep(200)

    label("loc_250")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_298")
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Jump("loc_250")

    label("loc_298")

    Return()

    # Function_0_204 end

    def Function_1_299(): pass

    label("Function_1_299")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AF")
    Event(0, 12)

    label("loc_2AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_2BE")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 10)

    label("loc_2BE")

    Return()

    # Function_1_299 end

    def Function_2_2BF(): pass

    label("Function_2_2BF")

    Sound(480, 1, 100, 0)
    Return()

    # Function_2_2BF end

    def Function_3_2C6(): pass

    label("Function_3_2C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC")
    Call(0, 11)
    Jump("loc_5B4")

    label("loc_2DC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_370")
    Jump("loc_3BA")

    label("loc_370")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_390")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BA")

    label("loc_390")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B0")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BA")

    label("loc_3B0")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BA")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_551")

    ChrTalk(
        0x8,
        (
            "#3404FEverything's becoming more\x01",
            "interesting by the minute.\x02\x03",
            "#3400FA health resort, hmm...?\x01",
            "I have some business to attend to,\x01",
            "but, please, enjoy yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309FHell yeah, that's the plan!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0211F(Randy, did our objective slip out\x01",
            "of that thick skull of yours?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(C-Course not. Turn the glare\x01",
            "down a few notches, Tio Tot...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5AD")

    label("loc_551")


    ChrTalk(
        0x8,
        (
            "#3400FWe're headed to a resort, so you should\x01",
            "all enjoy yourselves, at the very least.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AD")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)

    label("loc_5B4")

    Return()

    # Function_3_2C6 end

    def Function_4_5B5(): pass

    label("Function_4_5B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69D")

    ChrTalk(
        0xFE,
        (
            "Is this everyone's first time traveling\x01",
            "on the cruise ship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though it's only an hour to Mishelam, please,\x01",
            "enjoy your trip. The deck is open for your\x01",
            "pleasure, so be our guest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_698")
    SetScenarioFlags(0xB5, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_698")

    Jump("loc_735")

    label("loc_69D")


    ChrTalk(
        0xFE,
        (
            "If you happen to feel seasick,\x01",
            "find one of our stewardesses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We have medicine that will calm your\x01",
            "stomach, so don't hesitate to ask for\x01",
            "some.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_735")

    TalkEnd(0xFE)
    Return()

    # Function_4_5B5 end

    def Function_5_739(): pass

    label("Function_5_739")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7CD")
    Jump("loc_817")

    label("loc_7CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7ED")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_817")

    label("loc_7ED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_817")

    label("loc_80D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_817")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DD")

    ChrTalk(
        0xFE,
        "Today's our long-awaited Mishelam trip! ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Boutiques and jewelers... Oh, this\x01",
            "will be a day lived in style!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D8")
    SetScenarioFlags(0xB5, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D8")

    Jump("loc_949")

    label("loc_8DD")


    ChrTalk(
        0xFE,
        (
            "My man withdrew quite a bit of\x01",
            "mira for this special occasion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, let's party till we drop! ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_949")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_739 end

    def Function_6_951(): pass

    label("Function_6_951")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E5")
    Jump("loc_A2F")

    label("loc_9E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A05")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A2F")

    label("loc_A05")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A25")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A2F")

    label("loc_A25")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A2F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B20")

    ChrTalk(
        0xFE,
        (
            "I, uh, kind of withdrew my entire\x01",
            "savings account for this trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to be careful to make sure\x01",
            "my girlfriend doesn't burn all my\x01",
            "mira on purses...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1B")
    SetScenarioFlags(0xB5, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B1B")

    Jump("loc_B97")

    label("loc_B20")


    ChrTalk(
        0xFE,
        "My girlfriend is a shopaholic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I could survive this trip with my\x01",
            "savings still intact, that'd be great...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B97")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_951 end

    def Function_7_B9F(): pass

    label("Function_7_B9F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC8")

    ChrTalk(
        0xFE,
        (
            "Gahaha... I managed to get more\x01",
            "funds for the evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'd be a shame if I couldn't get what\x01",
            "I'm aiming for because I'm short a little\x01",
            "mira. This time, it's mine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F(This must be another one\x01",
            "of the Schwarze Auction's\x01",
            "attendees.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC3")
    SetScenarioFlags(0xB5, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CC3")

    Jump("loc_D40")

    label("loc_CC8")


    ChrTalk(
        0xFE,
        (
            "Huehuehue...\x01",
            "I managed to increase\x01",
            "my funds for the evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have heard the rumors.\x01",
            "It's as good as mine...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D40")

    TalkEnd(0xFE)
    Return()

    # Function_7_B9F end

    def Function_8_D44(): pass

    label("Function_8_D44")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DD8")
    Jump("loc_E22")

    label("loc_DD8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DF8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E22")

    label("loc_DF8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E18")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E22")

    label("loc_E18")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E22")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F27")

    ChrTalk(
        0xFE,
        (
            "I'm pumped for this theme park. I've\x01",
            "got a map printed, so I'm ready to go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not lame for a guy to go\x01",
            "there alone, is it? I'm just really\x01",
            "looking forward to it, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F22")
    SetScenarioFlags(0xB5, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F22")

    Jump("loc_F72")

    label("loc_F27")


    ChrTalk(
        0xFE,
        (
            "What? Are you judging me because\x01",
            "I'm going to a theme park by myself?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F72")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_D44 end

    def Function_9_F7A(): pass

    label("Function_9_F7A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_100E")
    Jump("loc_1058")

    label("loc_100E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_102E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1058")

    label("loc_102E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_104E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1058")

    label("loc_104E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1058")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Hey, you catch a glimpse of that\x01",
            "stunner sitting in the back...?\x01",
            "Man, she rocks that pantsuit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gah, I can't take my eyes off her!\x01",
            "This trip was definitely worth the effort...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114F")
    SetScenarioFlags(0xB5, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_114F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_F7A end

    def Function_10_1157(): pass

    label("Function_10_1157")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
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
    SetChrPos(0x102, 3000, 150, -13830, 180)
    SetChrPos(0x101, 2120, 150, -13830, 180)
    SetChrPos(0x103, 3120, 150, -11330, 180)
    SetChrPos(0x104, 2120, 150, -11330, 180)
    OP_68(-600, 1100, -8060, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    OP_68(2560, 1100, -12450, 8000)
    OP_6F(0x1)
    OP_0D()
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3500178V#0000F#5PSo this is what the cruise ship is like.\x02\x03",
            "#3500179VThe interior is surprisingly elegant.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)

    ChrTalk(
        0x102,
        (
            "#3500180V#0104F#11PThere's a reason for that. Unlike\x01",
            "the bus system, the Mishelam cruise\x01",
            "ship is managed by the IBC.\x02\x03",
            "#3500181V#0102FThey don't even charge travel fare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500182V#0205F#5PThat is extremely generous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500183V#0304F#5PI mean, if you don't have the cash,\x01",
            "it's not like you can do anything\x01",
            "but look when ya get there.\x02\x03",
            "#3500184V#0300FI reckon we have about 20 more\x01",
            "minutes? Let's take it easy till then.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetChrPos(0x0, -200, 0, -11700, 0)
    SetScenarioFlags(0xA3, 5)
    OP_29(0x44, 0x4, 0x10)
    OP_29(0x47, 0x4, 0x2)
    OP_29(0x47, 0x1, 0x0)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_1157 end

    def Function_11_14EA(): pass

    label("Function_11_14EA")

    EventBegin(0x0)
    Fade(1000)
    OP_68(1260, 300, 7490, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18060, 0)
    SetCameraDistance(17060, 2000)
    SetChrPos(0x101, 1890, -1000, 8970, 225)
    SetChrPos(0x102, 2920, -1000, 8620, 225)
    SetChrPos(0x103, 2580, -1000, 7410, 270)
    SetChrPos(0x104, 3530, -1000, 7820, 270)
    SetChrSubChip(0x8, 0x2)
    OP_6F(0x10)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#3500260V#3404F#6PMishelam...\x01",
            "A fascinating little place, isn't it?\x02\x03",
            "#3500261V#3400FIf I had the time, I would have liked to\x01",
            "stop by that famous theme park of theirs.\x02",
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
            "#3500262V#0005F#5PUm, wait...didn't you have business\x01",
            "at the theme park?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500263V#3404F#6PWell, yes. But it's purely business.\x02\x03",
            "#3500264V#3400FNo matter. This won't be the last\x01",
            "time I visit Crossbell, after all...\x02\x03",
            "#3500265VPerhaps I'll visit Mishelam\x01",
            "for pleasure next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500266V#0109F#5PYes, I'm sure you'd enjoy it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500267V#0300F#11PNow that it's on my mind,\x01",
            "what'd you think of that new\x01",
            "Arc en Ciel performance?\x02\x03",
            "#3500268VDidn't ya see that yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500269V#3404F#6PYes, the evening performance.\x02\x03",
            "#3500270V#3402FIn my time, I've had the chance to see\x01",
            "many high-quality acts.\x02\x03",
            "#3500271VTruth be told, I've never seen a play\x01",
            "crafted with such extraordinary\x01",
            "balance before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500272V#0205F#11PBalance...? Could you explain?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500273V#3400F#6PThe script, production, costumes, music...\x02\x03",
            "#3500274VThe acrobatics on that beautifully crafted\x01",
            "stage...\x02\x03",
            "#3500275VEvery part of the play was first-rate.\x01",
            "That said, such is merely the minimum\x01",
            "expectation for a famous troupe.\x02\x03",
            "#3500276V#3404FBut, Ilya Platiere...\x02\x03",
            "#3500277VWith each of the critical components\x01",
            "working in unison with her core, the\x01",
            "play becomes almost alive.\x02\x03",
            "#3500278V#3402FIt was as if I was witnessing the creation\x01",
            "of life itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500279V#0002F#5PWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500280V#0104F#5PThe creation of new life...?\x01",
            "It sounds like a miracle to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500281V#0309F#11PDamn, leave it to an entertainment\x01",
            "producer to describe it like that, eh?\x02\x03",
            "#3500282VY'know what? That's almost word-\x01",
            "for-word what I was gonna say!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500283V#3404F#6POh, I'm sure...\x02\x03",
            "#3500284VThis new production also featured\x01",
            "another lead actress.\x02\x03",
            "#3500285V#3400FThe up-and-coming Rixia Mao, playing\x01",
            "the Moon Princess.\x02\x03",
            "#3500286VDespite that shadow of death following her,\x01",
            "she pushed the play to even greater heights.\x02",
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
        "#3500287V#0005F#5PRixia has what...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500288V#0105F#5PA shadow of death?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500289V#3400F#6PPay no mind, it's only my intuition.\x02\x03",
            "#3500290V#3404FSun and moon, gold and silver,\x01",
            "light and dark, and life and death...\x02\x03",
            "#3500291VThat girl and Ilya Platiere contain\x01",
            "remarkably contrasting chi.\x02\x03",
            "#3500292V#3400FOne could even say those two are the\x01",
            "embodiment of yin and yang or taiji.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500293V#0205F#11P'Yin and yang' or 'taiji'...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500294V#0300F#11PAin't those fancy concepts used\x01",
            "by Eastern martial artists?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500295V#3400F#6PWell, I wouldn't say it's particularly\x01",
            "limited to martial arts.\x02\x03",
            "#3500296V#3404FEither way, the fact that those two\x01",
            "met by chance must be the work\x01",
            "of fate.\x02\x03",
            "#3500297VAnd, I believe what guided them\x01",
            "was the singularity known as the\x01",
            "autonomous state of Crossbell.\x02\x03",
            "#3500298V#3400FWell, that's one way to put it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500299V#0001F#5PA singularity...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500300V#0103F#5PThat was a little hard to follow but I\x01",
            "think I understand what you mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500301V#3404F#6PWell, don't take everything\x01",
            "I say at face value.\x02\x03",
            "#3500302V#3400FStill, the charm of Arc en Ciel\x01",
            "is directly connected to\x01",
            "Crossbell itself.\x02\x03",
            "#3500303VIf I don't remember that, their\x01",
            "performances outside the state\x01",
            "may not go as well as I hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500304V#0205F#11PThen, are you intending to return to\x01",
            "the Republic empty-handed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500305V#3402F#6POf course not, that'd be a waste.\x02\x03",
            "#3500306VI'm sure there are ways to\x01",
            "draw out Arc en Ciel's charm,\x01",
            "even outside of Crossbell.\x02\x03",
            "#3500307V#3404FFor my hereafter negotiations,\x01",
            "that sort of planning will be key\x01",
            "to soliciting their talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500308V#0202F#11PInteresting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500309V#0302F#11PDamn, you're really\x01",
            "thinkin' ahead, aren't ya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500310V#3404F#6PHehe, I'm a professional, after all.\x02\x03",
            "#3500311V#3400FSeeing through the true nature of things,\x01",
            "establishing an ideal goal and situation,\x01",
            "and finding out how to achieve it...\x02\x03",
            "#3500312VRegardless of one's field, that's\x01",
            "the way a professional operates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500313V#0000F#5PHuh...is that right? I'll definitely\x01",
            "take that to heart, Kilika.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500314V#0109F#5POf course. We have to be ready\x01",
            "at a moment's notice.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 2970, -1000, 6660, 180)
    SetScenarioFlags(0xA3, 7)
    SetChrSubChip(0x8, 0x0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_11_14EA end

    def Function_12_2659(): pass

    label("Function_12_2659")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    Sound(801, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3500315V\x07\x05",
            "Thank you for your patience.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#3500316V\x07\x05",
            "The cruise ship will be arriving at\x01",
            "Mishelam shortly.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#3500317V\x07\x05",
            "Please, don't forget to take\x01",
            "your belongings with you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    OP_25(0x1E0, 0x5A)
    Sleep(100)
    OP_25(0x1E0, 0x50)
    Sleep(100)
    OP_25(0x1E0, 0x46)
    Sleep(100)
    OP_25(0x1E0, 0x3C)
    Sleep(100)
    OP_25(0x1E0, 0x32)
    Sleep(100)
    OP_25(0x1E0, 0x28)
    Sleep(100)
    OP_25(0x1E0, 0x1E)
    Sleep(100)
    OP_25(0x1E0, 0x14)
    Sleep(100)
    OP_25(0x1E0, 0xA)
    Sleep(100)
    OP_25(0x1E0, 0x0)
    WaitBGM()
    SetScenarioFlags(0x5C, 0)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2659 end

    SaveToFile()

Try(main)
