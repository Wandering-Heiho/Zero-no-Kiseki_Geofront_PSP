from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t104b.bin",                # FileName
        "t104b",                    # MapName
        "t104b",                    # Location
        0x0044,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 68, 0, 2, 0, 3],
    )

    BuildStringList((
        "t104b",                  # 0
        "Lyte",                   # 1
        "Mercy",                  # 2
        "Girl",                   # 3
        "Young Man",              # 4
        "Tourist",                # 5
        "Old Man",                # 6
        "Old Lady",               # 7
        "Winona",                 # 8
        "Drona",                  # 9
        "Tourist",                # 10
    ))

    AddCharChip((
        "chr/ch25000.itc",                   # 00
        "chr/ch34500.itc",                   # 01
        "chr/ch21302.itc",                   # 02
        "chr/ch21202.itc",                   # 03
        "chr/ch21602.itc",                   # 04
        "chr/ch33002.itc",                   # 05
        "chr/ch21702.itc",                   # 06
        "chr/ch27900.itc",                   # 07
        "chr/ch26600.itc",                   # 08
        "chr/ch24400.itc",                   # 09
    ))

    DeclNpc(-104069, 0,       2980,    90,   257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-101099, 0,       5880,    90,   257,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-104949, 0,       8989,    45,   341,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-102970, 0,       10960,   225,  341,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-93940,  0,       11039,   225,  341,  0x0, 0,   4,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-97919,  0,       18979,   45,   341,  0x0, 0,   5,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-97930,  0,       20979,   135,  341,  0x0, 0,   6,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-1860,   0,       10640,   180,  257,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4159,    0,       2349,    0,    257,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(3950,    0,       3309,    270,  257,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)

    DeclActor(-1770,   0,       8810,    1000,    -1860,   1500,    10640,   0x007E, 0,  12, 0x0000)
    DeclActor(-101650, 0,       2470,    1000,    -104070, 1500,    2980,    0x007E, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_260",          # 00, 0
        "Function_1_318",          # 01, 1
        "Function_2_3A1",          # 02, 2
        "Function_3_3A8",          # 03, 3
        "Function_4_3A9",          # 04, 4
        "Function_5_3AD",          # 05, 5
        "Function_6_A0D",          # 06, 6
        "Function_7_ADB",          # 07, 7
        "Function_8_CEC",          # 08, 8
        "Function_9_E6B",          # 09, 9
        "Function_10_108C",        # 0A, 10
        "Function_11_1275",        # 0B, 11
        "Function_12_143B",        # 0C, 12
        "Function_13_143F",        # 0D, 13
        "Function_14_16BF",        # 0E, 14
        "Function_15_1766",        # 0F, 15
        "Function_16_1847",        # 10, 16
    ))


    def Function_0_260(): pass

    label("Function_0_260")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2A0"),
        (1, "loc_2AC"),
        (2, "loc_2B8"),
        (3, "loc_2C4"),
        (4, "loc_2D0"),
        (5, "loc_2DC"),
        (6, "loc_2E8"),
        (SWITCH_DEFAULT, "loc_2F4"),
    )


    label("loc_2A0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2AC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2B8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2C4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2D0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2DC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_300")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_317")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_317")

    Return()

    # Function_0_260 end

    def Function_1_318(): pass

    label("Function_1_318")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A0")
    OP_95(0xFE, -98090, 0, 5880, 2000, 0x0)
    OP_95(0xFE, -98090, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 5880, 2000, 0x0)
    Jump("Function_1_318")

    label("loc_3A0")

    Return()

    # Function_1_318 end

    def Function_2_3A1(): pass

    label("Function_2_3A1")

    BeginChrThread(0x9, 0, 0, 1)
    Return()

    # Function_2_3A1 end

    def Function_3_3A8(): pass

    label("Function_3_3A8")

    Return()

    # Function_3_3A8 end

    def Function_4_3A9(): pass

    label("Function_4_3A9")

    Call(0, 5)
    Return()

    # Function_4_3A9 end

    def Function_5_3AD(): pass

    label("Function_5_3AD")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A09")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_40B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A04")

    label("loc_42B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43F")
    Jump("loc_A04")

    label("loc_43F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A04")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_949")

    ChrTalk(
        0x8,
        (
            "How would you like dinner accompanied\x01",
            "by a bottle of El Voile? It is one of the finest\x01",
            "Erebonian wines in existence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It may fetch a modest price, but rest\x01",
            "assured, its aroma is said to rival even\x01",
            "Grand Chardonnay.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62A")

    ChrTalk(
        0x102,
        (
            "#0103FGrand Chardonnay... If I remember correctly,\x01",
            "that's a vintage wine mulled and distributed\x01",
            "in the Liberl Kingdom.\x02\x03",
            "#0100FRecently, I believe it's gone for almost\x01",
            "500,000 mira in auctions, believe it or not.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FF")

    label("loc_62A")


    ChrTalk(
        0x102,
        (
            "#5303FGrand Chardonnay... If I remember correctly,\x01",
            "that's a vintage wine mulled and distributed\x01",
            "in Liberl Kingdom.\x02\x03",
            "#5300FRecently, I believe it's gone for almost\x01",
            "500,000 mira in auctions, believe it or not.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FF")


    ChrTalk(
        0x101,
        (
            "#5005F500,000?! I knew people enjoyed their\x01",
            "wine, but to sell for that much?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_786")

    ChrTalk(
        0x103,
        "#0203FThis world makes no sense.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AC")

    label("loc_786")


    ChrTalk(
        0x103,
        "#5403FThis world makes no sense.\x02",
    )

    CloseMessageWindow()

    label("loc_7AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_812")

    ChrTalk(
        0x104,
        (
            "#0304FHey, if it's that good, it's that good.\x02\x03",
            "#0309FHmm, maybe just one glass...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_869")

    label("loc_812")


    ChrTalk(
        0x104,
        (
            "#5604FHey, if it's that good, it's that good.\x02\x03",
            "#5609FHmm, maybe just one glass...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_887")

    ChrTalk(
        0x103,
        "#0211F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_896")

    label("loc_887")


    ChrTalk(
        0x103,
        "#5411F...\x02",
    )

    CloseMessageWindow()

    label("loc_896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DB")

    ChrTalk(
        0x104,
        "#0306FWhoa, I'm jokin'! Cool your jets, Tio Tot!\x02",
    )

    CloseMessageWindow()
    Jump("loc_911")

    label("loc_8DB")


    ChrTalk(
        0x104,
        "#5606FWhoa, I'm jokin'! Cool your jets, Tio Tot!\x02",
    )

    CloseMessageWindow()

    label("loc_911")


    ChrTalk(
        0x101,
        "#5003FAs long as you aren't being serious.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A04")

    label("loc_949")


    ChrTalk(
        0x8,
        (
            "A bottle of El Voile is said to rival\x01",
            "even Grand Chardonnay, and that\x01",
            "is no small feat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wholeheartedly recommend it with dinner.\x01",
            "If you like, I can go fetch a bottle for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A04")

    Jump("loc_3BA")

    label("loc_A09")

    TalkEnd(0x8)
    Return()

    # Function_5_3AD end

    def Function_6_A0D(): pass

    label("Function_6_A0D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "If I've got my calendar right, today's the\x01",
            "last day of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been hearing that the city is wild,\x01",
            "right about now... Maybe I should have\x01",
            "spent my day there instead.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_A0D end

    def Function_7_ADB(): pass

    label("Function_7_ADB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B6F")
    Jump("loc_BB9")

    label("loc_B6F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B8F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BB9")

    label("loc_B8F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BAF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BB9")

    label("loc_BAF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BB9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C95")

    ChrTalk(
        0xFE,
        "*munch* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmmm...mmmmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes! This dish... It's a masterpiece!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this, I can finally forget about\x01",
            "that cruddy jeweler not letting me in!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_CE4")

    label("loc_C95")


    ChrTalk(
        0xFE,
        "Mmmmm... I'm in heaven.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x2)

    ChrTalk(
        0xFE,
        "Excuse me, waitress? Seconds, please! ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_CE4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_ADB end

    def Function_8_CEC(): pass

    label("Function_8_CEC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D80")
    Jump("loc_DCA")

    label("loc_D80")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DA0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCA")

    label("loc_DA0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCA")

    label("loc_DC0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DCA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E40")

    ChrTalk(
        0xFE,
        "Y-You're STILL eating?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "O-Oh, Goddess. All my mira...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_E63")

    label("loc_E40")


    ChrTalk(
        0xFE,
        "O-Oh, Goddess. All my mira...\x02",
    )

    CloseMessageWindow()

    label("loc_E63")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_CEC end

    def Function_9_E6B(): pass

    label("Function_9_E6B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EFF")
    Jump("loc_F49")

    label("loc_EFF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F1F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F49")

    label("loc_F1F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F3F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F49")

    label("loc_F3F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F49")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1011")

    ChrTalk(
        0xFE,
        "What a feast!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew, there's nothing more satisfying\x01",
            "than having a delicious meal. Each new\x01",
            "dish I try is another unforgettable memory!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1084")

    label("loc_1011")


    ChrTalk(
        0xFE,
        (
            "After having a meal like this, I can say,\x01",
            "with full confidence, that visiting Crossbell\x01",
            "was worth the effort.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1084")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_E6B end

    def Function_10_108C(): pass

    label("Function_10_108C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1120")
    Jump("loc_116A")

    label("loc_1120")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1140")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_116A")

    label("loc_1140")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1160")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_116A")

    label("loc_1160")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_116A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Oh, would you look at the time! It's almost\x01",
            "time for Speaker Hartmann's party to start.\x01",
            "We better hurry on over to his mansion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope my wife manages to have a good time.\x01",
            "It's her first time attending, you see.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_108C end

    def Function_11_1275(): pass

    label("Function_11_1275")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1309")
    Jump("loc_1353")

    label("loc_1309")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1329")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1353")

    label("loc_1329")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1349")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1353")

    label("loc_1349")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1353")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "My husband insisted on taking me to a\x01",
            "fancy annual party. Imagine my shock\x01",
            "when I found out it was in Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm looking forward to seeing\x01",
            "what sort of party this really is.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_1275 end

    def Function_12_143B(): pass

    label("Function_12_143B")

    Call(0, 13)
    Return()

    # Function_12_143B end

    def Function_13_143F(): pass

    label("Function_13_143F")

    TalkBegin(0xF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_144C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BB")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_149D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_149D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BD")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16B6")

    label("loc_14BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D1")
    Jump("loc_16B6")

    label("loc_14D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165D")

    ChrTalk(
        0xF,
        "Dear, that looks absolutely marvelous on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The balance is superb! While it shines with\x01",
            "a more modern fashion sense, it manages\x01",
            "to not look trashy in the process...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "If only Mr. Hemisphere worked for us! He\x01",
            "could teach us a thing or two about style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5005F(Wazy, you grow more and more mysterious\x01",
            "every second we spend together...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_16B6")

    label("loc_165D")


    ChrTalk(
        0xF,
        (
            "If only Mr. Hemisphere worked for us! He\x01",
            "could teach us a thing or two about style.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B6")

    Jump("loc_144C")

    label("loc_16BB")

    TalkEnd(0xF)
    Return()

    # Function_13_143F end

    def Function_14_16BF(): pass

    label("Function_14_16BF")

    TalkBegin(0xFE)
    TurnDirection(0x10, 0x11, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16DB")
    Call(0, 16)
    Jump("loc_1762")

    label("loc_16DB")


    ChrTalk(
        0xFE,
        "Are you not satisfied with your current attire?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If so, perhaps you should try this hat to\x01",
            "complement the rest of the outfit?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1762")

    TalkEnd(0xFE)
    Return()

    # Function_14_16BF end

    def Function_15_1766(): pass

    label("Function_15_1766")

    TalkBegin(0xFE)
    OP_93(0xFE, 0x10E, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1782")
    Call(0, 16)
    Jump("loc_1843")

    label("loc_1782")


    ChrTalk(
        0xFE,
        (
            "(I-I'm in quite the pickle here...\x01",
            "I just wanted to look around and\x01",
            "head back home, but I messed up!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(After talking to her THIS much, I can't\x01",
            "just leave without buying anything...!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1843")

    TalkEnd(0xFE)
    Return()

    # Function_15_1766 end

    def Function_16_1847(): pass

    label("Function_16_1847")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x10,
        (
            "Hmm, I think I've got it... From everything\x01",
            "you've said, it sounds like you prefer a\x01",
            "more casual, laid-back look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "This hat might be perfect for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "U-Uh, yeah, maybe...\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_16_1847 end

    SaveToFile()

Try(main)
